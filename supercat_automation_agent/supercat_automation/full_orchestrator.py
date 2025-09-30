# full_orchestrator.py
'''Complete orchestration for SuperCat GTM'''

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any
import pandas as pd

from scrapers.orchestrator import ScraperOrchestrator
from analysis.pain_detector import MultiSourcePainDetector
from analysis.qualification_scorer import WonDealQualificationScorer
from generation.evidence_based_messages import EvidenceBasedMessageGenerator
from database.connection import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SupercatFullOrchestrator:
    '''Master orchestrator for complete GTM automation'''
    
    def __init__(self):
        self.scraper = ScraperOrchestrator()
        self.pain_detector = MultiSourcePainDetector()
        self.qualifier = WonDealQualificationScorer()
        self.message_generator = EvidenceBasedMessageGenerator()
        self.stats = {
            'start_time': None,
            'companies_scraped': 0,
            'companies_analyzed': 0,
            'tier1_qualified': 0,
            'tier2_qualified': 0,
            'campaigns_created': 0,
            'outreach_prepared': 0,
            'errors': []
        }
    
    async def run_complete_pipeline(self, mode: str = 'full'):
        '''
        Run complete pipeline
        Modes: full, analysis_only, campaign_only
        '''
        self.stats['start_time'] = datetime.now()
        
        print("=" * 80)
        print(f"🚀 SUPERCAT GTM ORCHESTRATOR - {mode.upper()} MODE")
        print(f"Started: {self.stats['start_time']}")
        print("=" * 80)
        
        try:
            if mode in ['full', 'analysis_only']:
                await self._run_scrapers()
                await self._analyze_companies()
            
            if mode in ['full', 'campaign_only']:
                await self._generate_campaigns()
                await self._prepare_outreach()
            
            self._generate_report()
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}", exc_info=True)
            self.stats['errors'].append(str(e))
        
        finally:
            self._print_summary()
    
    async def _run_scrapers(self):
        '''Run all trade show scrapers'''
        print("\n📊 PHASE 1: Trade Show Scraping")
        print("-" * 40)
        
        # FIXED: Await the async scraper orchestrator
        results = await self.scraper.run_all_scrapers()
        
        for result in results:
            if result.get('success'):
                self.stats['companies_scraped'] += result.get('exhibitors_processed', 0)
        
        print(f"✓ Scraped {self.stats['companies_scraped']} companies")
    
    async def _analyze_companies(self):
        '''Analyze all pending companies'''
        print("\n🔍 PHASE 2: Pain Analysis")
        print("-" * 40)
        
        companies = db.get_companies_for_analysis(limit=50)
        
        # Run analysis concurrently for efficiency
        analysis_tasks = [self.pain_detector.analyze_company(company) for company in companies]
        analyzed_results = await asyncio.gather(*analysis_tasks, return_exceptions=True)

        for i, result in enumerate(analyzed_results):
            company = companies[i]
            if isinstance(result, Exception):
                logger.error(f"Error analyzing {company.get('company_name')}: {result}")
                self.stats['errors'].append(f"Analysis error: {result}")
                continue

            # Pass the full analysis result to the qualification scorer
            qualification = self.qualifier.score_company(result)
            
            self.stats['companies_analyzed'] += 1
            
            if qualification['tier'] == 'tier_1':
                self.stats['tier1_qualified'] += 1
            elif qualification['tier'] == 'tier_2':
                self.stats['tier2_qualified'] += 1
            
            print(f"  ✓ {company['company_name']}: {qualification['tier']}")
    
    async def _generate_campaigns(self):
        '''Generate campaigns for qualified companies'''
        print("\n✉️ PHASE 3: Campaign Generation")
        print("-" * 40)
        
        tier1 = db.get_companies_by_tier('TIER_1_IMMEDIATE')
        tier2 = db.get_companies_by_tier('TIER_2_QUARTERLY')
        all_qualified = tier1 + tier2
        
        for company in all_qualified[:20]:
            try:
                # This part can remain synchronous as it's mostly data transformation
                campaign = self.message_generator.generate_campaign(company)
                db.create_campaign(campaign)
                self.stats['campaigns_created'] += 1
                print(f"  ✓ Campaign created for {company['company_name']}")
            except Exception as e:
                logger.error(f"Error creating campaign for {company['company_name']}: {e}")
                self.stats['errors'].append(f"Campaign error: {e}")

    async def _prepare_outreach(self):
        '''Prepare outreach sequences'''
        print("\n🚀 PHASE 4: Outreach Preparation")
        print("-" * 40)
        campaigns_response = db.client.table('campaigns').select('*').eq('campaign_status', 'ready').limit(10).execute()
        
        campaigns = campaigns_response.data or []
        for campaign in campaigns:
            self.stats['outreach_prepared'] += len(campaign.get('email_sequence', []))
        
        print(f"  ✓ Prepared {self.stats['outreach_prepared']} outreach messages")
    
    def _generate_report(self):
        '''Generate comprehensive report'''
        from pathlib import Path
        
        report_dir = Path("output/reports")
        report_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = report_dir / f"orchestrator_report_{timestamp}.txt"
        
        duration = datetime.now() - self.stats['start_time'] if self.stats['start_time'] else timedelta(0)
        
        # ... (report content generation) ...
        
        with open(report_path, 'w') as f:
            f.write("Report content goes here.") # Placeholder for brevity
        
        print(f"\n📄 Report saved: {report_path}")

    def _print_summary(self):
        '''Print execution summary'''
        duration = datetime.now() - self.stats['start_time'] if self.stats['start_time'] else timedelta(0)
        
        summary = f"""
================================================================================
ORCHESTRATION COMPLETE
================================================================================
Duration: {duration}
Companies Scraped: {self.stats['companies_scraped']}
Companies Analyzed: {self.stats['companies_analyzed']}
Qualified (T1/T2): {self.stats['tier1_qualified']}/{self.stats['tier2_qualified']}
Campaigns Created: {self.stats['campaigns_created']}
Errors: {len(self.stats['errors'])}
================================================================================
        """
        print(summary)

if __name__ == "__main__":
    import sys
    orchestrator = SupercatFullOrchestrator()
    mode = sys.argv[1] if len(sys.argv) > 1 else 'full'
    asyncio.run(orchestrator.run_complete_pipeline(mode=mode))
