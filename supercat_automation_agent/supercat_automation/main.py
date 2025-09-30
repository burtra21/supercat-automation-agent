# main.py
"""
Supercat Solutions GTM Automation System
Automated B2B Sales Pipeline for Mobile Sales Enablement Platform
Target: Manufacturers & Distributors with Complex Pricing/Configuration Needs
"""

import os
import sys
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
import asyncio
import json
from dataclasses import dataclass, asdict
from enum import Enum
import time

# Third-party imports
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv
import schedule
import requests
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/supercat_gtm.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


@dataclass
class SystemConfig:
    """System configuration for Supercat GTM Automation"""
    # API Keys
    supabase_url: str = os.getenv('SUPABASE_URL')
    supabase_key: str = os.getenv('SUPABASE_KEY')
    openai_api_key: str = os.getenv('OPENAI_API_KEY')
    clay_api_key: str = os.getenv('CLAY_API_KEY')
    sendgrid_api_key: str = os.getenv('SENDGRID_API_KEY')
    linkedin_api_key: str = os.getenv('LINKEDIN_API_KEY')
    
    # Operational Parameters
    daily_outreach_limit: int = 50
    min_pain_score: float = 0.6  # Threshold for qualification
    max_campaigns_per_company: int = 1
    follow_up_days: int = 3
    
    # Target Industries (from Supercat's focus)
    target_industries: List[str] = None
    
    def __post_init__(self):
        if self.target_industries is None:
            self.target_industries = [
                'furniture_manufacturing',
                'lighting_wholesale',
                'home_decor_distribution',
                'gift_wholesale',
                'commercial_furnishings'
            ]


class ExistentialDataPoint(Enum):
    """EDPs identified in Supercat analysis"""
    MARGIN_EROSION = "margin_erosion_from_pricing_errors"  # 5-7% margin loss
    ORDER_ERRORS = "order_error_catastrophe"  # 30% error rate
    TRADE_SHOW_RISK = "trade_show_revenue_concentration"  # 30-50% annual revenue
    SALES_ADMIN_TIME = "sales_rep_administrative_burden"  # 40% time wasted
    CONTRACT_COMPLIANCE = "contract_price_compliance_failure"  # Major account risk


class PainBasedSegment(Enum):
    """Pain-based segments from Supercat analysis"""
    HIGH_CUSTOMIZATION_FURNITURE = "high_customization_furniture"  # Grade Jump Riser Pricing
    CONTRACT_COMMERCIAL = "contract_reliant_commercial"  # Hotel/hospitality suppliers
    MULTI_BRAND_DISTRIBUTORS = "multi_brand_lighting_home"  # Complex catalog management
    HIGH_VOLUME_IMPORTERS = "high_volume_tiered_pricing"  # Volume-based complexity
    TRADE_SHOW_DEPENDENT = "trade_show_revenue_warriors"  # Vegas/High Point Market


class SupercatGTMAutomation:
    """
    Main orchestration system for Supercat Solutions GTM Automation
    Targets: B2B manufacturers/distributors with complex pricing needs
    """
    
    def __init__(self, config: SystemConfig):
        self.config = config
        self.supabase = self._init_supabase()
        self.metrics = {
            'companies_analyzed': 0,
            'qualified_companies': 0,
            'campaigns_launched': 0,
            'emails_sent': 0,
            'linkedin_connections': 0,
            'responses': 0,
            'demos_booked': 0
        }
        self.testimonials = {
            'butler_specialty': "eCat flexibly configures to the way we do business.",
            'godinger_silver': "Over the past 25 years, eCat is the best thing that has ever happened to this company.",
            'wildwood_lamps': "I've reduced by a third the number of calls per day"
        }
    
    def _init_supabase(self) -> Client:
        """Initialize Supabase client"""
        try:
            client = create_client(
                self.config.supabase_url,
                self.config.supabase_key
            )
            logger.info("✅ Supabase connection established")
            return client
        except Exception as e:
            logger.error(f"❌ Failed to connect to Supabase: {e}")
            raise
    
    async def run_daily_automation(self):
        """
        Execute the complete daily GTM automation pipeline
        Following the Supercat GTM strategy
        """
        logger.info("=" * 70)
        logger.info("🚀 SUPERCAT GTM AUTOMATION - DAILY RUN")
        logger.info(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("=" * 70)
        
        try:
            # Step 1: Identify Target Companies
            logger.info("\n📊 PHASE 1: Company Identification")
            target_companies = await self._identify_target_companies()
            logger.info(f"✓ Identified {len(target_companies)} potential targets")
            
            # Step 2: Detect Pain Signals & Score
            logger.info("\n🔍 PHASE 2: Pain Signal Detection")
            scored_companies = await self._detect_pain_signals(target_companies)
            qualified = [c for c in scored_companies if c['pain_score'] >= self.config.min_pain_score]
            logger.info(f"✓ Qualified {len(qualified)} companies (score >= {self.config.min_pain_score})")
            
            # Step 3: Enrich with Clay
            logger.info("\n💎 PHASE 3: Company Enrichment")
            enriched_companies = await self._enrich_companies(qualified)
            logger.info(f"✓ Enriched {len(enriched_companies)} companies with Clay data")
            
            # Step 4: Generate Personalized Campaigns
            logger.info("\n✉️ PHASE 4: Campaign Generation")
            campaigns = await self._generate_campaigns(enriched_companies)
            logger.info(f"✓ Generated {len(campaigns)} personalized campaigns")
            
            # Step 5: Execute Multi-Channel Outreach
            logger.info("\n🚀 PHASE 5: Campaign Execution")
            execution_results = await self._execute_campaigns(campaigns[:self.config.daily_outreach_limit])
            logger.info(f"✓ Executed {len(execution_results)} campaigns")
            
            # Step 6: Process Follow-ups
            logger.info("\n🔄 PHASE 6: Follow-up Processing")
            follow_ups = await self._process_follow_ups()
            logger.info(f"✓ Processed {len(follow_ups)} follow-ups")
            
            # Step 7: Analytics & Reporting
            logger.info("\n📈 PHASE 7: Performance Analytics")
            report = await self._generate_performance_report()
            await self._send_daily_report(report)
            
            logger.info("\n✅ Daily automation completed successfully!")
            
        except Exception as e:
            logger.error(f"❌ Pipeline failed: {e}")
            await self._send_alert(f"GTM Pipeline Failure: {str(e)}")
            raise
    
    async def _identify_target_companies(self) -> List[Dict]:
        """
        Step 1: Identify companies matching Supercat's ICP
        Sources: Trade shows, industry directories, web scraping
        """
        companies = []
        
        # 1. Trade Show Exhibitors (Vegas Market, High Point Market)
        trade_show_companies = await self._scrape_trade_shows()
        companies.extend(trade_show_companies)
        
        # 2. Industry Directories
        directory_companies = await self._scrape_industry_directories()
        companies.extend(directory_companies)
        
        # 3. LinkedIn Sales Navigator
        linkedin_companies = await self._search_linkedin_companies()
        companies.extend(linkedin_companies)
        
        # Deduplicate and filter
        unique_companies = self._deduplicate_by_domain(companies)
        new_companies = await self._filter_already_contacted(unique_companies)
        
        # Save to database
        for company in new_companies:
            await self._save_company(company)
        
        return new_companies
    
    async def _scrape_trade_shows(self) -> List[Dict]:
        """Scrape major furniture/lighting trade shows for exhibitors"""
        trade_shows = [
            {
                'name': 'Las Vegas Market',
                'url': 'https://www.lasvegasmarket.com/exhibitors',
                'next_date': '2025-01-26',
                'industry': 'furniture_lighting_decor'
            },
            {
                'name': 'High Point Market',
                'url': 'https://www.highpointmarket.org/exhibitors',
                'next_date': '2025-04-26',
                'industry': 'furniture'
            }
        ]
        
        exhibitors = []
        for show in trade_shows:
            try:
                # Scrape exhibitor list
                response = requests.get(show['url'], timeout=10)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Extract exhibitor data (simplified - would need specific selectors)
                for exhibitor in soup.find_all('div', class_='exhibitor'):
                    company_data = {
                        'company_name': exhibitor.find('h3').text.strip(),
                        'booth_number': exhibitor.find('span', class_='booth').text if exhibitor.find('span', class_='booth') else None,
                        'trade_show': show['name'],
                        'show_date': show['next_date'],
                        'industry': show['industry'],
                        'source': 'trade_show_scrape',
                        'pain_indicator': 'trade_show_dependency'
                    }
                    
                    # Calculate days until show (urgency factor)
                    days_until_show = (datetime.strptime(show['next_date'], '%Y-%m-%d') - datetime.now()).days
                    company_data['urgency_score'] = min(1.0, 1 - (days_until_show / 180))
                    
                    exhibitors.append(company_data)
                    
            except Exception as e:
                logger.error(f"Error scraping {show['name']}: {e}")
                continue
        
        return exhibitors
    
    async def _detect_pain_signals(self, companies: List[Dict]) -> List[Dict]:
        """
        Detect Existential Data Points (EDPs) for each company
        Based on Supercat's identified pain points
        """
        scored_companies = []
        
        for company in companies:
            pain_signals = {}
            
            # Check for Grade Jump Riser Pricing complexity
            if await self._has_product_configurator(company):
                pain_signals['configurator_complexity'] = 0.9
            
            # Check for PDF catalogs (manual process indicator)
            if await self._has_pdf_catalogs(company):
                pain_signals['manual_processes'] = 0.8
            
            # Check for "call for pricing" (pricing complexity)
            if await self._has_call_for_pricing(company):
                pain_signals['pricing_complexity'] = 0.85
            
            # Trade show dependency (if from trade show source)
            if company.get('source') == 'trade_show_scrape':
                pain_signals['trade_show_dependency'] = 0.9
            
            # Calculate overall pain score
            if pain_signals:
                company['pain_score'] = sum(pain_signals.values()) / len(pain_signals)
                company['pain_signals'] = pain_signals
                company['segment'] = self._assign_segment(company)
                scored_companies.append(company)
        
        return scored_companies
    
    async def _has_product_configurator(self, company: Dict) -> bool:
        """Check if company website has product configurator (complexity indicator)"""
        if not company.get('domain'):
            return False
        
        try:
            response = requests.get(f"https://{company['domain']}", timeout=10)
            content = response.text.lower()
            
            # Indicators of configurator/customization
            indicators = [
                'configure your', 'customize your', 'build your own',
                'fabric options', 'finish options', 'grade', 'tier pricing',
                'product configurator', 'customization options'
            ]
            
            return any(indicator in content for indicator in indicators)
            
        except:
            return False
    
    async def _enrich_companies(self, companies: List[Dict]) -> List[Dict]:
        """
        Enrich companies using Clay API
        Get decision maker info, company size, tech stack, etc.
        """
        enriched = []
        
        for company in companies:
            try:
                # Clay enrichment request
                enrichment_data = await self._call_clay_api(company)
                
                # Find decision makers (VP Sales, IT Director)
                decision_makers = await self._find_decision_makers(company['domain'])
                
                company.update({
                    'employee_count': enrichment_data.get('employee_count'),
                    'revenue_estimate': enrichment_data.get('revenue'),
                    'technologies': enrichment_data.get('technologies', []),
                    'decision_makers': decision_makers,
                    'has_salesforce': 'Salesforce' in enrichment_data.get('technologies', []),
                    'has_legacy_erp': self._detect_legacy_erp(enrichment_data.get('technologies', []))
                })
                
                enriched.append(company)
                
            except Exception as e:
                logger.error(f"Failed to enrich {company.get('company_name')}: {e}")
                continue
        
        return enriched
    
    async def _generate_campaigns(self, companies: List[Dict]) -> List[Dict]:
        """
        Generate personalized multi-channel campaigns
        Using Supercat's messaging framework and testimonials
        """
        campaigns = []
        
        for company in companies:
            campaign = {
                'company_id': company.get('id'),
                'company': company,
                'channels': [],
                'messages': {},
                'created_at': datetime.now()
            }
            
            # Generate email sequence (7 emails as per Supercat strategy)
            email_sequence = await self._generate_email_sequence(company)
            campaign['messages']['emails'] = email_sequence
            campaign['channels'].append('email')
            
            # Generate LinkedIn messages
            if company.get('decision_makers'):
                linkedin_messages = await self._generate_linkedin_messages(company)
                campaign['messages']['linkedin'] = linkedin_messages
                campaign['channels'].append('linkedin')
            
            # Generate landing page
            landing_page = await self._generate_landing_page(company)
            campaign['messages']['landing_page'] = landing_page
            campaign['channels'].append('web')
            
            campaigns.append(campaign)
        
        return campaigns
    
    async def _generate_email_sequence(self, company: Dict) -> List[Dict]:
        """
        Generate 7-email sequence based on Supercat's strategy
        Incorporating real testimonials and pain-specific messaging
        """
        segment = company.get('segment', PainBasedSegment.HIGH_CUSTOMIZATION_FURNITURE.value)
        pain_score = company.get('pain_score', 0.7)
        
        emails = []
        
        # Email 1: Problem Agitation
        if segment == PainBasedSegment.HIGH_CUSTOMIZATION_FURNITURE.value:
            subject = f"Your Grade Jump Riser Pricing is costing {company['company_name']} $400,000 annually"
            preview = "Each pricing error costs you 5% margin..."
            body = self._generate_margin_erosion_email(company)
        elif segment == PainBasedSegment.TRADE_SHOW_DEPENDENT.value:
            days_until_show = (datetime.strptime(company.get('show_date', '2025-01-26'), '%Y-%m-%d') - datetime.now()).days
            subject = f"Your Vegas Market booth in {days_until_show} days - avoiding the 30% error rate"
            preview = f"Booth {company.get('booth_number', 'C-1055')} investment at risk..."
            body = self._generate_trade_show_email(company)
        else:
            subject = f"The hidden cost of manual orders at {company['company_name']}"
            preview = "Industry average: 30% order error rate..."
            body = self._generate_generic_pain_email(company)
        
        emails.append({
            'sequence': 1,
            'day': 0,
            'subject': subject,
            'preview': preview,
            'body': body,
            'type': 'problem_agitation'
        })
        
        # Email 2: Success Story (Day 3)
        emails.append({
            'sequence': 2,
            'day': 3,
            'subject': '"Best thing in 25 years" - How Godinger Silver transformed sales',
            'preview': 'Their reps are "in love" with the solution...',
            'body': self._generate_testimonial_email('godinger', company),
            'type': 'social_proof'
        })
        
        # Email 3: Feature Focus (Day 7)
        emails.append({
            'sequence': 3,
            'day': 7,
            'subject': 'Works perfectly offline - even at trade shows',
            'preview': 'No WiFi? No problem. Every order captured perfectly...',
            'body': self._generate_offline_capability_email(company),
            'type': 'feature_benefit'
        })
        
        # Email 4: ROI Calculator (Day 10)
        emails.append({
            'sequence': 4,
            'day': 10,
            'subject': f"ROI Calculator: {company['company_name']}'s savings with Supercat",
            'preview': 'See your exact savings in 60 seconds...',
            'body': self._generate_roi_email(company),
            'type': 'value_proposition'
        })
        
        # Email 5: Case Study (Day 14)
        emails.append({
            'sequence': 5,
            'day': 14,
            'subject': 'How Butler Specialty eliminated pricing chaos',
            'preview': '"Flexibly configures to the way we do business"',
            'body': self._generate_case_study_email('butler', company),
            'type': 'case_study'
        })
        
        # Email 6: Urgency (Day 18)
        if segment == PainBasedSegment.TRADE_SHOW_DEPENDENT.value:
            subject = f"⏰ {days_until_show} days until Vegas Market"
            preview = "Don't repeat last year's order errors..."
        else:
            subject = "Your competitors are already digital"
            preview = "While you manage paper catalogs..."
        
        emails.append({
            'sequence': 6,
            'day': 18,
            'subject': subject,
            'preview': preview,
            'body': self._generate_urgency_email(company),
            'type': 'urgency'
        })
        
        # Email 7: Final Offer (Day 21)
        emails.append({
            'sequence': 7,
            'day': 21,
            'subject': f"Final: Free setup for {company['company_name']} this month",
            'preview': 'This offer expires in 48 hours...',
            'body': self._generate_final_offer_email(company),
            'type': 'final_offer'
        })
        
        return emails
    
    def _generate_margin_erosion_email(self, company: Dict) -> str:
        """Generate email focused on margin erosion pain point"""
        return f"""
Hi [First Name],

I noticed {company['company_name']} offers complex product configurations with multiple fabric grades and finish options.

Quick question: What percentage of your quotes have pricing errors?

Industry data shows furniture manufacturers with Grade Jump Riser Pricing lose an average of 5-7% of gross margin annually due to quoting errors. For a company your size, that's potentially $400,000+ in lost profit.

Butler Specialty had the same challenge. Their President, Monty Sihweil, told us: "eCat flexibly configures to the way we do business. We are very pleased with what it enables us to do."

They eliminated pricing errors completely. Every quote is now perfect.

Worth a quick conversation to see how they did it?

Best regards,
[Your Name]
P.S. With your Vegas Market booth coming up, perfect pricing becomes even more critical.
"""
    
    def _generate_testimonial_email(self, testimonial_key: str, company: Dict) -> str:
        """Generate email featuring specific customer testimonial"""
        testimonials = {
            'godinger': {
                'company': 'Godinger Silver Art',
                'person': 'Joel Stern, VP of IT',
                'quote': 'Over the past 25 years, eCat is the best thing that has ever happened to this company. The reps are now mobile. They are in love. And they certainly don\'t miss all the paper!',
                'metric': '25 years in business, this is their #1 improvement'
            },
            'butler': {
                'company': 'Butler Specialty',
                'person': 'Monty Sihweil, President',
                'quote': 'eCat flexibly configures to the way we do business. We are very pleased with what it enables us to do.',
                'metric': 'Complex furniture configurations handled perfectly'
            },
            'wildwood': {
                'company': 'Wildwood Lamps',
                'person': 'Erin Yevak, Sales and Marketing Manager',
                'quote': 'I\'ve reduced by a third the number of calls per day',
                'metric': '33% reduction in support calls'
            }
        }
        
        t = testimonials[testimonial_key]
        
        return f"""
[First Name],

{t['person']} at {t['company']} doesn't mince words:

"{t['quote']}"

{t['metric']}.

{company['company_name']} faces similar challenges with [specific pain point]. Your reps deserve tools they'll love too.

Want to see why Joel calls it "the best thing in 25 years"?

[Your Name]
"""
    
    async def _execute_campaigns(self, campaigns: List[Dict]) -> List[Dict]:
        """
        Execute multi-channel campaigns
        Orchestrate email, LinkedIn, and retargeting
        """
        execution_results = []
        
        for campaign in campaigns:
            result = {
                'campaign_id': campaign.get('id'),
                'company': campaign['company']['company_name'],
                'channels_executed': [],
                'status': 'executing'
            }
            
            try:
                # Execute email sequence
                if 'emails' in campaign['messages']:
                    email_result = await self._send_email_sequence(
                        campaign['messages']['emails'],
                        campaign['company']
                    )
                    result['channels_executed'].append('email')
                    result['email_status'] = email_result
                
                # Execute LinkedIn outreach
                if 'linkedin' in campaign['messages'] and campaign['company'].get('decision_makers'):
                    linkedin_result = await self._send_linkedin_messages(
                        campaign['messages']['linkedin'],
                        campaign['company']['decision_makers']
                    )
                    result['channels_executed'].append('linkedin')
                    result['linkedin_status'] = linkedin_result
                
                # Create landing page
                if 'landing_page' in campaign['messages']:
                    landing_url = await self._create_landing_page(
                        campaign['messages']['landing_page'],
                        campaign['company']
                    )
                    result['landing_page_url'] = landing_url
                    result['channels_executed'].append('web')
                
                result['status'] = 'completed'
                execution_results.append(result)
                
                # Log campaign execution
                await self._log_campaign_execution(campaign, result)
                
            except Exception as e:
                logger.error(f"Failed to execute campaign for {campaign['company']['company_name']}: {e}")
                result['status'] = 'failed'
                result['error'] = str(e)
                execution_results.append(result)
        
        return execution_results
    
    async def _generate_performance_report(self) -> Dict:
        """Generate daily performance report"""
        # Get today's metrics
        today_metrics = await self._get_today_metrics()
        
        # Get response data
        responses = await self._get_response_data()
        
        # Calculate conversion rates
        email_open_rate = (today_metrics['emails_opened'] / today_metrics['emails_sent'] * 100) if today_metrics['emails_sent'] > 0 else 0
        response_rate = (responses['total_responses'] / today_metrics['emails_sent'] * 100) if today_metrics['emails_sent'] > 0 else 0
        demo_conversion = (responses['demos_booked'] / responses['total_responses'] * 100) if responses['total_responses'] > 0 else 0
        
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'summary': {
                'companies_analyzed': self.metrics['companies_analyzed'],
                'qualified_companies': self.metrics['qualified_companies'],
                'campaigns_launched': self.metrics['campaigns_launched'],
                'emails_sent': self.metrics['emails_sent'],
                'linkedin_connections': self.metrics['linkedin_connections']
            },
            'performance': {
                'email_open_rate': f"{email_open_rate:.1f}%",
                'response_rate': f"{response_rate:.1f}%",
                'demo_conversion': f"{demo_conversion:.1f}%",
                'demos_booked': responses['demos_booked']
            },
            'top_performing': {
                'best_subject_line': await self._get_best_subject_line(),
                'best_segment': await self._get_best_segment(),
                'best_pain_point': await self._get_best_pain_point()
            },
            'pipeline': {
                'total_pipeline_value': await self._calculate_pipeline_value(),
                'opportunities_created': await self._count_opportunities(),
                'expected_close_rate': '25%'
            }
        }
        
        return report
    
    def _assign_segment(self, company: Dict) -> str:
        """Assign company to pain-based segment"""
        pain_signals = company.get('pain_signals', {})
        
        if pain_signals.get('configurator_complexity', 0) > 0.8:
            return PainBasedSegment.HIGH_CUSTOMIZATION_FURNITURE.value
        elif pain_signals.get('trade_show_dependency', 0) > 0.8:
            return PainBasedSegment.TRADE_SHOW_DEPENDENT.value
        elif pain_signals.get('pricing_complexity', 0) > 0.7:
            return PainBasedSegment.CONTRACT_COMMERCIAL.value
        elif pain_signals.get('manual_processes', 0) > 0.7:
            return PainBasedSegment.MULTI_BRAND_DISTRIBUTORS.value
        else:
            return PainBasedSegment.HIGH_VOLUME_IMPORTERS.value


async def main():
    """Main entry point for the GTM automation system"""
    
    # Initialize configuration
    config = SystemConfig()
    
    # Initialize the automation system
    automation = SupercatGTMAutomation(config)
    
    # Run the daily automation
    await automation.run_daily_automation()
    
    # Schedule for continuous operation
    schedule.every().day.at("09:00").do(lambda: asyncio.run(automation.run_daily_automation()))
    schedule.every().day.at("14:00").do(lambda: asyncio.run(automation._process_follow_ups()))
    
    logger.info("🚀 Supercat GTM Automation System Started")
    logger.info("📅 Scheduled runs: 9:00 AM and 2:00 PM daily")
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())