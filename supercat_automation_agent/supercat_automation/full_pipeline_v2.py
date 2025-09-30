#!/usr/bin/env python3
"""
SuperCat Pipeline v2 - Enhanced with Validation Study Integration
Uses validated PSI calculator, enhanced message generator, and comprehensive website analysis
Runs independently from v1 pipeline for safe testing
"""

import pandas as pd
import json
import os
import sys
import asyncio
import aiohttp
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Add current directory to path for imports
sys.path.append(os.path.dirname(__file__))

# Import validated components
try:
    from analysis.validated_psi_calculator import ValidatedPSICalculator
    from generation.validated_message_generator import ValidatedMessageGenerator
    from scrapers.website_evidence_v2 import WebsiteEvidenceExtractorV2
    from orchestration.clay_webhook import CompleteClayWebhookOrchestrator
    HAS_ALL_COMPONENTS = True
except ImportError as e:
    print(f"Import error: {e}")
    HAS_ALL_COMPONENTS = False

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
CLAY_WEBHOOK_URL = os.getenv('CLAY_WEBHOOK_URL')

# Initialize Supabase client
try:
    from supabase import create_client, Client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL else None
except ImportError:
    supabase = None

print(f"✅ SuperCat Pipeline v2 Environment:")
print(f"  • Validated Components: {'Available' if HAS_ALL_COMPONENTS else 'Missing'}")
print(f"  • OpenAI: {'Connected' if OPENAI_API_KEY else 'Not configured'}")
print(f"  • Supabase: {'Connected' if supabase else 'Not configured'}")
print(f"  • Clay Webhook: {'Connected' if CLAY_WEBHOOK_URL else 'Not configured'}")


class SuperCatPipelineV2:
    """
    Enhanced SuperCat Pipeline v2 with validation study integration
    
    Features:
    - Dual methodology PSI calculation (weighted + averaged)
    - Crisis intervention messaging
    - Comprehensive website evidence extraction
    - Enhanced Clay webhook integration
    - Validated customer language patterns
    """
    
    def __init__(self):
        self.session = None
        self.clay_webhook_url = CLAY_WEBHOOK_URL
        
        # Initialize validated components
        if HAS_ALL_COMPONENTS:
            self.psi_calculator = ValidatedPSICalculator()
            self.message_generator = ValidatedMessageGenerator(openai_api_key=OPENAI_API_KEY)
            self.evidence_extractor = WebsiteEvidenceExtractorV2()
            self.clay_webhook = CompleteClayWebhookOrchestrator() if CLAY_WEBHOOK_URL else None
        else:
            logger.error("Missing required components - cannot initialize pipeline")
            return
        
        # Pipeline statistics
        self.stats = {
            'processed': 0,
            'qualified': 0,
            'tier_a_immediate': 0,
            'tier_b_active': 0,
            'tier_c_monitor': 0,
            'sent_to_clay': 0,
            'saved_to_supabase': 0,
            'campaigns_generated': 0,
            'errors': []
        }
        
        logger.info("Initialized SuperCat Pipeline v2 with validated components")
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def process_company_v2(self, company_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process single company with v2 enhanced analysis
        
        Args:
            company_data: Company information from CSV
            
        Returns:
            Complete analysis and campaign results
        """
        
        company_name = company_data.get('company_name', 'Unknown Company')
        domain = company_data.get('domain', '')
        
        print(f"\n🏢 Processing v2: {company_name}")
        print(f"  🌐 Domain: {domain}")
        
        result = {
            'company_name': company_name,
            'domain': domain,
            'processing_version': 'v2_validated',
            'timestamp': datetime.now().isoformat(),
            'status': 'processing',
            'error': None
        }
        
        try:
            # Step 1: Enhanced website evidence extraction
            print(f"  🔍 Extracting comprehensive website evidence...")
            website_evidence = self.evidence_extractor.analyze_website_comprehensive(domain)
            
            if 'error' in website_evidence:
                print(f"  ⚠️ Website analysis error: {website_evidence['error']}")
                result['website_analysis_error'] = website_evidence['error']
            
            result['website_evidence'] = website_evidence
            
            # Step 2: Dual methodology PSI calculation
            print(f"  📊 Calculating dual methodology PSI scores...")
            psi_results = self.psi_calculator.calculate_dual_psi(company_data, website_evidence)
            result['psi_analysis'] = psi_results
            
            # Extract key metrics
            weighted_psi = psi_results['weighted_methodology']['psi_score']
            averaged_psi = psi_results['averaged_methodology']['psi_score']
            qualification_tier = psi_results['weighted_methodology']['tier']
            qualification_decision = psi_results['weighted_methodology']['qualification_decision']
            
            print(f"  📈 Weighted PSI: {weighted_psi:.1f}% | Averaged PSI: {averaged_psi:.1f}%")
            print(f"  🎯 Tier: {qualification_tier} | Qualified: {qualification_decision}")
            
            # Update statistics
            self.stats['processed'] += 1
            if qualification_tier == 'TIER_A_IMMEDIATE':
                self.stats['tier_a_immediate'] += 1
            elif qualification_tier == 'TIER_B_ACTIVE':
                self.stats['tier_b_active'] += 1
            elif qualification_tier == 'TIER_C_MONITOR':
                self.stats['tier_c_monitor'] += 1
            
            if qualification_decision:
                self.stats['qualified'] += 1
            
            # Step 3: Generate validated campaign (if qualified)
            if qualification_decision:
                print(f"  📧 Generating validated campaign...")
                campaign = self.message_generator.generate_validated_campaign(
                    company_data, website_evidence
                )
                result['campaign'] = campaign
                self.stats['campaigns_generated'] += 1
                
                print(f"  ✅ Generated {campaign['campaign_type']} campaign")
                print(f"     • {len(campaign.get('email_sequence', []))} emails")
                print(f"     • {len(campaign.get('linkedin_sequence', []))} LinkedIn messages")
                print(f"     • {len(campaign.get('ad_suggestions', []))} ad variations")
            else:
                print(f"  📝 Company not qualified - generating nurture approach")
                campaign = self.message_generator.generate_validated_campaign(
                    company_data, website_evidence
                )
                result['campaign'] = campaign
            
            # Step 4: Save to Supabase (enhanced data)
            if supabase:
                await self.save_to_supabase_v2(company_data, psi_results, website_evidence)
            
            # Step 5: Send to Clay webhook (comprehensive data)
            if self.clay_webhook_url:
                await self.send_to_clay_v2(company_data, psi_results, website_evidence, result.get('campaign'))
            
            result['status'] = 'completed'
            
            # Display key evidence
            if psi_results.get('messaging', {}).get('evidence_based_hooks'):
                print(f"  📝 Key Evidence:")
                for hook in psi_results['messaging']['evidence_based_hooks'][:3]:
                    print(f"     • {hook}")
            
        except Exception as e:
            logger.error(f"Error processing {company_name}: {e}")
            result['error'] = str(e)
            result['status'] = 'error'
            self.stats['errors'].append({
                'company': company_name,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            })
        
        return result
    
    async def save_to_supabase_v2(self, company_data: Dict[str, Any], 
                                 psi_results: Dict[str, Any], 
                                 website_evidence: Dict[str, Any]):
        """Save enhanced v2 data to Supabase"""
        
        if not supabase:
            return
        
        try:
            # Build comprehensive record
            record = {
                'company_name': str(company_data.get('company_name', '')),
                'domain': str(company_data.get('domain', '')),
                'processing_version': 'v2_validated',
                'timestamp': datetime.now().isoformat(),
                
                # Dual methodology results
                'weighted_psi_score': float(psi_results['weighted_methodology']['psi_score']),
                'averaged_psi_score': float(psi_results['averaged_methodology']['psi_score']),
                'qualification_tier': str(psi_results['weighted_methodology']['tier']),
                'qualification_decision': bool(psi_results['weighted_methodology']['qualification_decision']),
                'purchase_probability': float(psi_results['weighted_methodology']['purchase_probability']),
                
                # Primary EDPs
                'weighted_primary_edp': str(psi_results['weighted_methodology']['primary_edp']),
                'averaged_primary_edp': str(psi_results['averaged_methodology']['primary_edp']),
                'primary_edp_match': bool(psi_results['methodology_comparison']['primary_edp_match']),
                
                # EDP scores
                'edp1_sku_complexity_score': float(psi_results['edp_scores'].get('EDP1_SKU_Complexity', 0)),
                'edp2_rep_management_score': float(psi_results['edp_scores'].get('EDP2_Rep_Management', 0)),
                'edp6_channel_conflict_score': float(psi_results['edp_scores'].get('EDP6_Channel_Conflict', 0)),
                'edp7_sales_enablement_score': float(psi_results['edp_scores'].get('EDP7_Sales_Enablement', 0)),
                'edp8_technology_obsolescence_score': float(psi_results['edp_scores'].get('EDP8_Technology_Obsolescence', 0)),
                
                # Website analysis summary
                'has_product_search': bool(website_evidence.get('EDP7_Has_Product_Search', False)),
                'has_mobile_optimization': bool(website_evidence.get('EDP7_Has_Mobile_Optimization', False)),
                'has_ssl': bool(website_evidence.get('EDP8_Has_SSL', False)),
                'page_speed_score': str(website_evidence.get('EDP8_Page_Speed_Score', 'Unknown')),
                'sku_count_estimate': int(website_evidence.get('EDP1_SKU_Count_Estimate', 0)),
                'channel_count': int(website_evidence.get('EDP6_Channel_Count', 0)),
                
                # Business context
                'target_audience': str(website_evidence.get('Target_Audience', 'Unknown')),
                'geographic_presence': str(website_evidence.get('Geographic_Presence', 'Unknown')),
                'trade_shows_mentioned': json.dumps(website_evidence.get('Trade_Shows_Mentioned', [])),
                'product_types': json.dumps(website_evidence.get('Product_Types', [])),
            }
            
            # Add contact info if available
            if company_data.get('email'):
                record['email'] = str(company_data['email'])
            if company_data.get('first_name'):
                record['first_name'] = str(company_data['first_name'])
            if company_data.get('last_name'):
                record['last_name'] = str(company_data['last_name'])
            
            # Insert record
            result = supabase.table('companies_v2').insert(record).execute()
            self.stats['saved_to_supabase'] += 1
            print(f"  💾 Saved to Supabase v2")
            
        except Exception as e:
            logger.warning(f"Supabase v2 save error (non-critical): {e}")
    
    async def send_to_clay_v2(self, company_data: Dict[str, Any], 
                             psi_results: Dict[str, Any], 
                             website_evidence: Dict[str, Any],
                             campaign: Optional[Dict[str, Any]] = None):
        """Send comprehensive v2 data to Clay webhook"""
        
        if not self.clay_webhook_url:
            return
        
        try:
            # Build comprehensive webhook payload
            webhook_payload = {
                'processing_version': 'v2_validated',
                'timestamp': datetime.now().isoformat(),
                'validation_study_source': 'C2 Supercat Customer Pain Signal Validation Study',
                
                # Company information
                'company_name': company_data.get('company_name', ''),
                'domain': company_data.get('domain', ''),
                'contact_info': {
                    'first_name': str(company_data.get('first_name', '')),
                    'last_name': str(company_data.get('last_name', '')),
                    'email': str(company_data.get('email', '')),
                    'title': str(company_data.get('title', ''))
                },
                
                # Dual methodology PSI results
                'psi_analysis': {
                    'weighted_methodology': {
                        'psi_score': psi_results['weighted_methodology']['psi_score'],
                        'tier': psi_results['weighted_methodology']['tier'],
                        'primary_edp': psi_results['weighted_methodology']['primary_edp'],
                        'qualification_decision': psi_results['weighted_methodology']['qualification_decision'],
                        'purchase_probability': psi_results['weighted_methodology']['purchase_probability']
                    },
                    'averaged_methodology': {
                        'psi_score': psi_results['averaged_methodology']['psi_score'],
                        'tier': psi_results['averaged_methodology']['tier'],
                        'primary_edp': psi_results['averaged_methodology']['primary_edp'],
                        'operational_intelligence': psi_results['averaged_methodology']['operational_intelligence']
                    },
                    'methodology_comparison': psi_results['methodology_comparison']
                },
                
                # Individual EDP scores
                'edp_scores': psi_results['edp_scores'],
                
                # Comprehensive website analysis
                'website_analysis': {
                    # EDP1: SKU Complexity
                    'sku_analysis': {
                        'sku_count_estimate': website_evidence.get('EDP1_SKU_Count_Estimate', 0),
                        'product_categories': website_evidence.get('EDP1_Product_Categories', []),
                        'category_count': website_evidence.get('EDP1_Category_Count', 0),
                        'has_search': website_evidence.get('EDP1_Has_Search', False),
                        'search_sophistication': website_evidence.get('EDP1_Search_Sophistication', 'None'),
                        'filter_count': website_evidence.get('EDP1_Filter_Count', 0),
                        'has_configurator': website_evidence.get('EDP1_Has_Configurator', False),
                        'catalog_format': website_evidence.get('EDP1_Catalog_Format', 'Unknown'),
                        'pain_score': website_evidence.get('EDP1_SKU_Complexity_Pain_Score', 0)
                    },
                    
                    # EDP2: Rep Management
                    'rep_analysis': {
                        'has_rep_locator': website_evidence.get('EDP2_Has_Rep_Locator', False),
                        'rep_portal_exists': website_evidence.get('EDP2_Rep_Portal_Exists', False),
                        'rep_resources_accessible': website_evidence.get('EDP2_Rep_Resources_Accessible', False),
                        'territory_structure_visible': website_evidence.get('EDP2_Territory_Structure_Visible', False),
                        'rep_count_estimate': website_evidence.get('EDP2_Rep_Count_Estimate', 0),
                        'territory_complexity': website_evidence.get('EDP2_Territory_Complexity', 'Unknown'),
                        'rep_login_keywords': website_evidence.get('EDP2_Rep_Login_Keywords', []),
                        'pain_score': website_evidence.get('EDP2_Rep_Performance_Pain_Score', 0)
                    },
                    
                    # EDP6: Channel Conflict
                    'channel_analysis': {
                        'channels_detected': website_evidence.get('EDP6_Channels_Detected', []),
                        'channel_count': website_evidence.get('EDP6_Channel_Count', 0),
                        'has_direct_sales': website_evidence.get('EDP6_Has_Direct_Sales', False),
                        'has_dealer_network': website_evidence.get('EDP6_Has_Dealer_Network', False),
                        'has_ecommerce': website_evidence.get('EDP6_Has_Ecommerce', False),
                        'has_trade_program': website_evidence.get('EDP6_Has_Trade_Program', False),
                        'pricing_transparency': website_evidence.get('EDP6_Pricing_Transparency', 'Unknown'),
                        'brand_count': website_evidence.get('EDP6_Brand_Count', 0),
                        'multi_brand_detected': website_evidence.get('EDP6_Multi_Brand_Detected', False),
                        'pain_score': website_evidence.get('EDP6_Channel_Conflict_Pain_Score', 0)
                    },
                    
                    # EDP7: Sales Enablement
                    'sales_enablement_analysis': {
                        'has_product_search': website_evidence.get('EDP7_Has_Product_Search', False),
                        'has_advanced_filters': website_evidence.get('EDP7_Has_Advanced_Filters', False),
                        'has_comparison_tool': website_evidence.get('EDP7_Has_Comparison_Tool', False),
                        'has_wishlist_quotes': website_evidence.get('EDP7_Has_Wishlist_Quotes', False),
                        'has_project_boards': website_evidence.get('EDP7_Has_Project_Boards', False),
                        'has_mobile_optimization': website_evidence.get('EDP7_Has_Mobile_Optimization', False),
                        'has_downloadable_assets': website_evidence.get('EDP7_Has_Downloadable_Assets', False),
                        'resource_formats': website_evidence.get('EDP7_Resource_Formats', []),
                        'missing_tools': website_evidence.get('EDP7_Missing_Tools', []),
                        'pain_score': website_evidence.get('EDP7_Sales_Enablement_Pain_Score', 0)
                    },
                    
                    # EDP8: Technology Obsolescence
                    'technology_analysis': {
                        'has_ssl': website_evidence.get('EDP8_Has_SSL', False),
                        'page_speed_score': website_evidence.get('EDP8_Page_Speed_Score', 'Unknown'),
                        'load_time_seconds': website_evidence.get('EDP8_Load_Time_Seconds', 0),
                        'modern_features': website_evidence.get('EDP8_Modern_Features', []),
                        'modern_feature_count': website_evidence.get('EDP8_Modern_Feature_Count', 0),
                        'javascript_frameworks': website_evidence.get('JavaScript_Frameworks', []),
                        'has_modern_js_framework': website_evidence.get('Has_Modern_JS_Framework', False),
                        'cms_detected': website_evidence.get('EDP8_CMS_Detected', 'Unknown'),
                        'uses_cdn': website_evidence.get('EDP8_Uses_CDN', False),
                        'copyright_year': website_evidence.get('EDP8_Copyright_Year', datetime.now().year),
                        'staleness_score': website_evidence.get('EDP8_Staleness_Score', 0),
                        'has_legacy_tech': website_evidence.get('EDP8_Has_Legacy_Tech', False),
                        'legacy_tech_found': website_evidence.get('EDP8_Legacy_Tech_Found', []),
                        'pain_score': website_evidence.get('EDP8_Tech_Obsolescence_Pain_Score', 0)
                    }
                },
                
                # Business context
                'business_context': {
                    'trade_shows_mentioned': website_evidence.get('Trade_Shows_Mentioned', []),
                    'trade_show_count': website_evidence.get('Trade_Show_Count', 0),
                    'next_trade_show': website_evidence.get('Next_Trade_Show'),
                    'weeks_to_next_show': website_evidence.get('Weeks_To_Next_Show'),
                    'product_types': website_evidence.get('Product_Types', []),
                    'target_audience': website_evidence.get('Target_Audience', 'Unknown'),
                    'geographic_presence': website_evidence.get('Geographic_Presence', 'Unknown'),
                    'specific_missing_features': website_evidence.get('Specific_Missing_Features', [])
                },
                
                # Messaging and hooks
                'messaging': psi_results.get('messaging', {}),
                'evidence_patterns': psi_results.get('evidence_patterns', {})
            }
            
            # Add campaign data if generated
            if campaign:
                webhook_payload['campaign'] = {
                    'campaign_type': campaign.get('campaign_type'),
                    'qualification_tier': campaign.get('qualification_tier'),
                    'email_sequence_count': len(campaign.get('email_sequence', [])),
                    'linkedin_sequence_count': len(campaign.get('linkedin_sequence', [])),
                    'ad_suggestions_count': len(campaign.get('ad_suggestions', [])),
                    'validation_context': campaign.get('validation_context', {}),
                    'operational_intelligence': campaign.get('operational_intelligence', {})
                }
                
                # Include COMPLETE email sequence (not just first email)
                if campaign.get('email_sequence'):
                    webhook_payload['campaign']['email_sequence'] = campaign['email_sequence']
                    webhook_payload['campaign']['first_email'] = campaign['email_sequence'][0]
                
                # Include COMPLETE LinkedIn sequence (not just connection)
                if campaign.get('linkedin_sequence'):
                    webhook_payload['campaign']['linkedin_sequence'] = campaign['linkedin_sequence']
                    webhook_payload['campaign']['linkedin_connection'] = campaign['linkedin_sequence'][0]
                
                # Include complete ad suggestions
                if campaign.get('ad_suggestions'):
                    webhook_payload['campaign']['ad_suggestions'] = campaign['ad_suggestions']
            
            # Send to Clay webhook
            async with self.session.post(
                self.clay_webhook_url,
                json=webhook_payload,
                headers={'Content-Type': 'application/json'}
            ) as response:
                if response.status in [200, 201, 202]:
                    self.stats['sent_to_clay'] += 1
                    print(f"  🚀 Sent comprehensive data to Clay webhook")
                else:
                    error_text = await response.text()
                    logger.error(f"Clay webhook failed: {response.status} - {error_text}")
                    
        except Exception as e:
            logger.error(f"Clay webhook error: {e}")
    
    async def process_csv_v2(self, csv_path: str, batch_size: int = 5) -> Dict[str, Any]:
        """
        Process CSV file with v2 enhanced pipeline
        
        Args:
            csv_path: Path to prospects CSV file
            batch_size: Number of companies to process in parallel
            
        Returns:
            Complete processing results
        """
        
        print(f"\n{'='*70}")
        print(f"SUPERCAT PIPELINE V2 - VALIDATION STUDY INTEGRATION")
        print(f"{'='*70}\n")
        
        # Read and validate CSV
        try:
            df = pd.read_csv(csv_path)
            df = df.dropna(subset=['company_name', 'domain'])
            print(f"📊 Processing {len(df)} companies with v2 pipeline")
        except Exception as e:
            logger.error(f"Error reading CSV: {e}")
            return {'error': f"Failed to read CSV: {e}"}
        
        print(f"🔧 Using validated components:")
        print(f"  • ValidatedPSICalculator (dual methodology)")
        print(f"  • ValidatedMessageGenerator (crisis intervention)")
        print(f"  • WebsiteEvidenceExtractorV2 (comprehensive analysis)")
        print(f"  • Enhanced Clay webhook integration")
        print(f"")
        
        # Process companies in batches
        results = []
        async with self:
            for i in range(0, len(df), batch_size):
                batch = df.iloc[i:i+batch_size]
                batch_results = []
                
                print(f"📦 Processing batch {i//batch_size + 1} ({len(batch)} companies)")
                
                # Process batch
                for idx, row in batch.iterrows():
                    company_data = row.to_dict()
                    result = await self.process_company_v2(company_data)
                    batch_results.append(result)
                    results.append(result)
                    
                    # Rate limiting between companies
                    await asyncio.sleep(2)
                
                # Rate limiting between batches
                if i + batch_size < len(df):
                    print(f"  ⏳ Batch complete, waiting 5 seconds before next batch...")
                    await asyncio.sleep(5)
        
        # Generate summary
        summary = self._generate_processing_summary(results)
        
        # Save results
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        results_file = f"results_v2_enhanced_{timestamp}.json"
        
        output_data = {
            'processing_version': 'v2_validated',
            'validation_study_source': 'C2 Supercat Customer Pain Signal Validation Study',
            'timestamp': timestamp,
            'summary': summary,
            'stats': self.stats,
            'results': results
        }
        
        with open(results_file, 'w') as f:
            json.dump(output_data, f, indent=2, default=str)
        
        print(f"\n📁 Results saved: {results_file}")
        
        # Save qualified companies to CSV
        qualified_results = [r for r in results if r.get('psi_analysis', {}).get('weighted_methodology', {}).get('qualification_decision', False)]
        if qualified_results:
            qualified_df = self._create_qualified_csv(qualified_results)
            qualified_file = f"qualified_v2_{timestamp}.csv"
            qualified_df.to_csv(qualified_file, index=False)
            print(f"📁 Qualified companies v2: {qualified_file}")
        
        return output_data
    
    def _generate_processing_summary(self, results: List[Dict]) -> Dict[str, Any]:
        """Generate comprehensive processing summary"""
        
        total = len(results)
        successful = len([r for r in results if r.get('status') == 'completed'])
        errors = len([r for r in results if r.get('status') == 'error'])
        
        # PSI score analysis
        psi_scores = []
        tier_distribution = {'TIER_A_IMMEDIATE': 0, 'TIER_B_ACTIVE': 0, 'TIER_C_MONITOR': 0, 'NOT_QUALIFIED': 0}
        
        for result in results:
            if result.get('psi_analysis'):
                weighted_psi = result['psi_analysis']['weighted_methodology']['psi_score']
                psi_scores.append(weighted_psi)
                tier = result['psi_analysis']['weighted_methodology']['tier']
                tier_distribution[tier] = tier_distribution.get(tier, 0) + 1
        
        avg_psi = sum(psi_scores) / len(psi_scores) if psi_scores else 0
        
        summary = {
            'total_processed': total,
            'successful': successful,
            'errors': errors,
            'success_rate': f"{(successful/total*100):.1f}%" if total > 0 else "0%",
            
            'qualification_results': {
                'total_qualified': self.stats['qualified'],
                'qualification_rate': f"{(self.stats['qualified']/total*100):.1f}%" if total > 0 else "0%",
                'tier_distribution': tier_distribution,
                'tier_a_immediate': self.stats['tier_a_immediate'],
                'tier_b_active': self.stats['tier_b_active'],
                'tier_c_monitor': self.stats['tier_c_monitor']
            },
            
            'psi_analysis': {
                'average_weighted_psi': f"{avg_psi:.1f}%",
                'psi_range': f"{min(psi_scores):.1f}% - {max(psi_scores):.1f}%" if psi_scores else "N/A",
                'high_psi_count': len([p for p in psi_scores if p >= 70]),
                'medium_psi_count': len([p for p in psi_scores if 40 <= p < 70]),
                'low_psi_count': len([p for p in psi_scores if p < 40])
            },
            
            'campaign_generation': {
                'campaigns_generated': self.stats['campaigns_generated'],
                'generation_rate': f"{(self.stats['campaigns_generated']/total*100):.1f}%" if total > 0 else "0%"
            },
            
            'integration_results': {
                'sent_to_clay': self.stats['sent_to_clay'],
                'saved_to_supabase': self.stats['saved_to_supabase'],
                'clay_success_rate': f"{(self.stats['sent_to_clay']/total*100):.1f}%" if total > 0 else "0%",
                'supabase_success_rate': f"{(self.stats['saved_to_supabase']/total*100):.1f}%" if total > 0 else "0%"
            }
        }
        
        return summary
    
    def _create_qualified_csv(self, qualified_results: List[Dict]) -> pd.DataFrame:
        """Create CSV of qualified companies with key metrics"""
        
        csv_data = []
        for result in qualified_results:
            psi_analysis = result.get('psi_analysis', {})
            website_evidence = result.get('website_evidence', {})
            campaign = result.get('campaign', {})
            
            csv_row = {
                'company_name': result.get('company_name', ''),
                'domain': result.get('domain', ''),
                'processing_version': 'v2_validated',
                
                # PSI Scores
                'weighted_psi_score': psi_analysis.get('weighted_methodology', {}).get('psi_score', 0),
                'averaged_psi_score': psi_analysis.get('averaged_methodology', {}).get('psi_score', 0),
                'qualification_tier': psi_analysis.get('weighted_methodology', {}).get('tier', ''),
                'purchase_probability': psi_analysis.get('weighted_methodology', {}).get('purchase_probability', 0),
                
                # Primary EDPs
                'weighted_primary_edp': psi_analysis.get('weighted_methodology', {}).get('primary_edp', ''),
                'averaged_primary_edp': psi_analysis.get('averaged_methodology', {}).get('primary_edp', ''),
                'primary_edp_match': psi_analysis.get('methodology_comparison', {}).get('primary_edp_match', False),
                
                # Key Website Indicators
                'has_product_search': website_evidence.get('EDP7_Has_Product_Search', False),
                'has_mobile_optimization': website_evidence.get('EDP7_Has_Mobile_Optimization', False),
                'has_ssl': website_evidence.get('EDP8_Has_SSL', False),
                'page_speed_score': website_evidence.get('EDP8_Page_Speed_Score', 'Unknown'),
                'sku_count_estimate': website_evidence.get('EDP1_SKU_Count_Estimate', 0),
                'channel_count': website_evidence.get('EDP6_Channel_Count', 0),
                'rep_count_estimate': website_evidence.get('EDP2_Rep_Count_Estimate', 0),
                
                # Business Context
                'target_audience': website_evidence.get('Target_Audience', 'Unknown'),
                'geographic_presence': website_evidence.get('Geographic_Presence', 'Unknown'),
                'trade_shows_mentioned': ', '.join(website_evidence.get('Trade_Shows_Mentioned', [])),
                'product_types': ', '.join(website_evidence.get('Product_Types', [])),
                
                # Campaign Information
                'campaign_type': campaign.get('campaign_type', ''),
                'email_count': len(campaign.get('email_sequence', [])),
                'linkedin_count': len(campaign.get('linkedin_sequence', [])),
                'ad_suggestions_count': len(campaign.get('ad_suggestions', [])),
                
                # Key Evidence
                'missing_features': ', '.join(website_evidence.get('Specific_Missing_Features', [])),
                'evidence_hooks': ', '.join(psi_analysis.get('messaging', {}).get('evidence_based_hooks', [])[:3])
            }
            
            csv_data.append(csv_row)
        
        return pd.DataFrame(csv_data)


async def main():
    """Main execution function"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python full_pipeline_v2.py prospects.csv [batch_size]")
        print("Example: python full_pipeline_v2.py prospects.csv 3")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    if not Path(csv_file).exists():
        print(f"❌ File not found: {csv_file}")
        sys.exit(1)
    
    # Initialize and run pipeline
    pipeline = SuperCatPipelineV2()
    
    if not HAS_ALL_COMPONENTS:
        print("❌ Missing required components - cannot run pipeline")
        sys.exit(1)
    
    try:
        results = await pipeline.process_csv_v2(csv_file, batch_size)
        
        # Display final summary
        print(f"\n{'='*70}")
        print(f"SUPERCAT PIPELINE V2 COMPLETE")
        print(f"{'='*70}")
        
        summary = results.get('summary', {})
        print(f"📊 Processing Summary:")
        print(f"  • Total Processed: {summary.get('total_processed', 0)}")
        print(f"  • Success Rate: {summary.get('success_rate', '0%')}")
        print(f"  • Qualified: {summary.get('qualification_results', {}).get('total_qualified', 0)}")
        print(f"  • Qualification Rate: {summary.get('qualification_results', {}).get('qualification_rate', '0%')}")
        
        tier_dist = summary.get('qualification_results', {}).get('tier_distribution', {})
        print(f"  • Tier A (Immediate): {tier_dist.get('TIER_A_IMMEDIATE', 0)}")
        print(f"  • Tier B (Active): {tier_dist.get('TIER_B_ACTIVE', 0)}")
        print(f"  • Tier C (Monitor): {tier_dist.get('TIER_C_MONITOR', 0)}")
        
        psi_analysis = summary.get('psi_analysis', {})
        print(f"  • Average PSI: {psi_analysis.get('average_weighted_psi', '0%')}")
        print(f"  • PSI Range: {psi_analysis.get('psi_range', 'N/A')}")
        
        integration = summary.get('integration_results', {})
        print(f"  • Clay Success: {integration.get('clay_success_rate', '0%')}")
        print(f"  • Supabase Success: {integration.get('supabase_success_rate', '0%')}")
        
        print(f"\n✅ SuperCat Pipeline v2 completed successfully!")
        
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        print(f"❌ Pipeline failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
