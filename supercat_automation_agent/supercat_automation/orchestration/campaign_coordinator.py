# orchestration/campaign_coordinator.py
"""
Coordinates the entire campaign flow from scraping to Clay webhook
This is the main orchestration layer
"""

import logging
from typing import Dict, List, Any
from datetime import datetime, timedelta
import asyncio

from scrapers.orchestrator import ScraperOrchestrator
from analysis.pain_detector import ValidatedPainDetector
from analysis.qualification_scorer import WonDealQualificationScorer
from generation.message_generator import CustomerValidatedMessageGenerator
from orchestration.clay_webhook import ClayWebhookOrchestrator
from database.connection import db

logger = logging.getLogger(__name__)

class CampaignCoordinator:
    """
    Master coordinator for the entire GTM automation
    Manages the flow from data collection to campaign execution
    """
    
    def __init__(self):
        """Initialize all components"""
        self.scraper = ScraperOrchestrator()
        self.pain_detector = ValidatedPainDetector()
        self.qualifier = WonDealQualificationScorer()
        self.message_generator = CustomerValidatedMessageGenerator()
        self.clay_webhook = ClayWebhookOrchestrator()
        
        self.stats = {
            'companies_processed': 0,
            'qualified_companies': 0,
            'campaigns_created': 0,
            'outreach_sent': 0,
            'errors': 0
        }
    
    async def run_full_pipeline(self):
        """
        Run the complete pipeline:
        1. Scrape trade shows
        2. Detect pain signals
        3. Qualify companies
        4. Generate campaigns
        5. Send to Clay
        """
        try:
            logger.info("🚀 Starting full GTM pipeline")
            
            # Step 1: Scrape trade shows
            logger.info("Step 1: Scraping trade shows...")
            scraping_results = await self.run_scrapers()
            
            # Step 2: Process new companies
            logger.info("Step 2: Processing new companies...")
            await self.process_new_companies()
            
            # Step 3: Generate campaigns for qualified companies
            logger.info("Step 3: Generating campaigns...")
            await self.generate_campaigns()
            
            # Step 4: Send campaigns to Clay
            logger.info("Step 4: Sending to Clay webhook...")
            await self.send_campaigns_to_clay()
            
            # Step 5: Generate reports
            logger.info("Step 5: Generating reports...")
            self.generate_reports()
            
            logger.info(f"""
            ✅ Pipeline Complete!
            - Companies Processed: {self.stats['companies_processed']}
            - Qualified: {self.stats['qualified_companies']}
            - Campaigns Created: {self.stats['campaigns_created']}
            - Sent to Clay: {self.stats['outreach_sent']}
            - Errors: {self.stats['errors']}
            """)
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            self.stats['errors'] += 1
    
    async def run_scrapers(self) -> Dict:
        """Run trade show scrapers"""
        return self.scraper.run_all_scrapers(concurrent=True)
    
    async def process_new_companies(self):
        """Process companies that haven't been analyzed yet"""
        try:
            # Get unprocessed companies
            companies = db.client.table('companies').select('*').is_(
                'overall_pain_score', 'null'
            ).limit(100).execute()
            
            for company in companies.data:
                self.stats['companies_processed'] += 1
                
                # Detect pain signals
                pain_signals = self.pain_detector.detect_pain_signals(company)
                
                if not pain_signals.get('qualified'):
                    continue
                
                # Update pain scores in database
                db.update_pain_scores(company['id'], {
                    'sales_enablement_pain_score': pain_signals['signals'].get('sales_enablement_collapse', {}).get('score', 0),
                    'technology_obsolescence_score': pain_signals['signals'].get('technology_obsolescence', {}).get('score', 0),
                    'rep_performance_pain_score': pain_signals['signals'].get('rep_performance_crisis', {}).get('score', 0),
                    'sku_complexity_pain_score': pain_signals['signals'].get('sku_complexity', {}).get('score', 0)
                })
                
                # Run qualification scoring
                qualification = self.qualifier.score_company(company)
                
                if qualification['qualified']:
                    self.stats['qualified_companies'] += 1
                    logger.info(f"✅ Qualified: {company['company_name']} - Tier: {qualification['tier']}")
                
        except Exception as e:
            logger.error(f"Error processing companies: {e}")
            self.stats['errors'] += 1
    
    async def generate_campaigns(self):
        """Generate campaigns for qualified companies"""
        try:
            # Get qualified companies without campaigns
            qualified = db.get_qualified_companies('tier_1')
            qualified.extend(db.get_qualified_companies('tier_2'))
            
            for company in qualified[:20]:  # Limit to 20 per run
                # Check if campaign already exists
                existing = db.client.table('campaigns').select('id').eq(
                    'company_id', company['id']
                ).execute()
                
                if existing.data:
                    continue
                
                # Get decision makers (you'd need to implement this)
                decision_makers = self.get_decision_makers(company)
                
                if not decision_makers:
                    logger.warning(f"No decision makers found for {company['company_name']}")
                    continue
                
                # Get pain signals
                pain_signals = {
                    'primary_pain': self.identify_primary_pain(company),
                    'signals': {
                        'sales_enablement_collapse': {'score': company.get('sales_enablement_pain_score', 0)},
                        'technology_obsolescence': {'score': company.get('technology_obsolescence_score', 0)}
                    }
                }
                
                # Generate campaign
                campaign = self.message_generator.generate_campaign(
                    company,
                    pain_signals,
                    decision_makers
                )
                
                if campaign:
                    # Save campaign
                    saved_campaign = db.create_campaign(campaign)
                    
                    if saved_campaign:
                        self.stats['campaigns_created'] += 1
                        
                        # Create outreach records
                        self.create_outreach_records(saved_campaign, company, decision_makers)
                
        except Exception as e:
            logger.error(f"Error generating campaigns: {e}")
            self.stats['errors'] += 1
    
    async def send_campaigns_to_clay(self):
        """Send all pending campaigns to Clay"""
        try:
            # Process pending outreach
            self.clay_webhook.process_pending_outreach(limit=50)
            
            # Update stats
            sent_count = db.client.table('outreach').select('count').eq(
                'sent_to_clay', True
            ).gte('clay_sent_at', datetime.now() - timedelta(hours=1)).execute()
            
            if sent_count.data:
                self.stats['outreach_sent'] = sent_count.data[0].get('count', 0)
            
        except Exception as e:
            logger.error(f"Error sending to Clay: {e}")
            self.stats['errors'] += 1
    
    def get_decision_makers(self, company: Dict) -> List[Dict]:
        """Get decision makers for a company"""
        # This would typically call Clay or another enrichment service
        # For now, return placeholder
        return [
            {
                'id': 'dm_1',
                'first_name': 'John',
                'last_name': 'Doe',
                'email': f"john@{company.get('domain', 'example.com')}",
                'title': 'VP Sales',
                'is_champion_persona': True
            }
        ]
    
    def identify_primary_pain(self, company: Dict) -> str:
        """Identify primary pain from scores"""
        pain_scores = {
            'sales_enablement_collapse': company.get('sales_enablement_pain_score', 0),
            'technology_obsolescence': company.get('technology_obsolescence_score', 0),
            'rep_performance_crisis': company.get('rep_performance_pain_score', 0),
            'sku_complexity': company.get('sku_complexity_pain_score', 0)
        }
        
        return max(pain_scores, key=pain_scores.get)
    
    def create_outreach_records(self, campaign: Dict, company: Dict, decision_makers: List[Dict]):
        """Create outreach records for campaign"""
        for dm in decision_makers:
            # Create email outreach records
            email_sequence = campaign.get('message_variants', {}).get('email', [])
            for email in email_sequence:
                outreach = {
                    'campaign_id': campaign['id'],
                    'company_id': company['id'],
                    'decision_maker_id': dm['id'],
                    'channel': 'email',
                    'sequence_step': email.get('sequence_step'),
                    'subject_line': email.get('subject'),
                    'message_body': email.get('body'),
                    'status': 'pending'
                }
                db.create_outreach(outreach)
            
            # Create LinkedIn outreach records
            linkedin_messages = campaign.get('message_variants', {}).get('linkedin', [])
            for message in linkedin_messages:
                outreach = {
                    'campaign_id': campaign['id'],
                    'company_id': company['id'],
                    'decision_maker_id': dm['id'],
                    'channel': 'linkedin',
                    'message_body': message.get('message'),
                    'status': 'pending'
                }
                db.create_outreach(outreach)
    
    def generate_reports(self):
        """Generate and save reports"""
        try:
            # Update daily metrics
            db.update_daily_metrics({
                'companies_identified': self.stats['companies_processed'],
                'companies_qualified': self.stats['qualified_companies'],
                'campaigns_created': self.stats['campaigns_created'],
                'outreach_sent': self.stats['outreach_sent']
            })
            
            # Generate detailed report
            report = f"""
            ========================================
            GTM AUTOMATION DAILY REPORT
            ========================================
            Date: {datetime.now().strftime('%Y-%m-%d')}
            
            Pipeline Metrics:
            - Companies Processed: {self.stats['companies_processed']}
            - Qualified (Tier 1/2): {self.stats['qualified_companies']}
            - Campaigns Created: {self.stats['campaigns_created']}
            - Sent to Clay: {self.stats['outreach_sent']}
            - Errors: {self.stats['errors']}
            
            Qualification Breakdown:
            - Tier 1: [Query database for count]
            - Tier 2: [Query database for count]
            - Disqualified: [Query database for count]
            
            Pain Signal Distribution:
            - Sales Enablement: [Query for average score]
            - Technology Gap: [Query for average score]
            - Rep Performance: [Query for average score]
            - SKU Complexity: [Query for average score]
            
            Next Steps:
            - Monitor Clay webhook for delivery confirmations
            - Track engagement metrics in SmartLead
            - Review LinkedIn acceptance rates in HeyReach
            ========================================
            """
            
            # Save report
            with open(f"output/reports/daily_report_{datetime.now().strftime('%Y%m%d')}.txt", 'w') as f:
                f.write(report)
            
            logger.info("Report generated successfully")
            
        except Exception as e:
            logger.error(f"Error generating report: {e}")
            # Add this to your existing CampaignCoordinator class in orchestration/campaign_coordinator.py

from generation.evidence_based_messages import EvidenceBasedMessageGenerator

def __init__(self):
    # ... existing init code ...
    self.message_generator = EvidenceBasedMessageGenerator()  # ADD THIS

async def generate_and_save_campaigns(self):
    """
    Generate campaigns for all qualified companies
    """
    
    # Get Tier 1 companies (highest priority)
    tier1_companies = db.get_companies_by_tier('TIER_1_IMMEDIATE')
    
    # Get Tier 2 companies
    tier2_companies = db.get_companies_by_tier('TIER_2_QUARTERLY')
    
    all_qualified = tier1_companies + tier2_companies
    
    logger.info(f"Generating campaigns for {len(all_qualified)} qualified companies")
    
    campaigns_created = 0
    
    for company in all_qualified:
        try:
            # Get the full analysis
            analysis = {
                'company_id': company['id'],
                'company_name': company['company_name'],
                'tam_tier': company['tam_tier'],
                'primary_edp': company['primary_edp'],
                'has_multiple_edps': company.get('has_multiple_edps', False),
                'evidence': {
                    'website': company.get('website_evidence', {})
                },
                'edp_tags': company.get('edp_tags', [])
            }
            
            # Generate campaign
            campaign = self.message_generator.generate_campaign(analysis)
            
            # Save campaign to database
            campaign_record = {
                'company_id': company['id'],
                'campaign_type': campaign['campaign_strategy'],
                'email_sequence': campaign['email_sequence'],
                'linkedin_messages': campaign['linkedin_messages'],
                'status': 'ready_to_send',
                'created_at': datetime.now().isoformat()
            }
            
            saved = db.create_campaign(campaign_record)
            
            if saved:
                campaigns_created += 1
                logger.info(f"Created campaign for {company['company_name']}")
                
        except Exception as e:
            logger.error(f"Error creating campaign for {company['company_name']}: {e}")
    
    logger.info(f"✅ Created {campaigns_created} campaigns")
    
    return campaigns_created