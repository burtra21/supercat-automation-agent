# run_pipeline.py
"""
Run the complete pipeline from analysis to campaign generation
"""

import asyncio
from datetime import datetime
from pathlib import Path
import pandas as pd
import logging
from bs4 import BeautifulSoup
from typing import Dict

from scrapers.vegas_market import VegasMarketScraper
from analysis.pain_detector import MultiSourcePainDetector
from generation.evidence_based_messages import EvidenceBasedMessageGenerator
from database.connection import db

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def run_full_pipeline():
    """
    Complete pipeline execution
    """
    
    print("=" * 60)
    print("SUPERCAT GTM AUTOMATION - FULL PIPELINE")
    print(f"Started: {datetime.now()}")
    print("=" * 60)
    
    # Step 1: Get companies (from scraper or upload)
    print("\n📊 STEP 1: Getting Companies...")
    
    # Option A: From trade show scraper
    # scraper = VegasMarketScraper()
    # companies = scraper.run()
    
    # Option B: From CSV (for testing)
    test_companies = [
        {
            'id': 'test_001',
            'company_name': 'Ashley Furniture',
            'domain': 'ashleyfurniture.com',
            'trade_shows': ['Vegas Market', 'High Point Market']
        },
        {
            'id': 'test_002', 
            'company_name': 'Lighting Direct',
            'domain': 'lightingdirect.com',
            'trade_shows': ['Lightovation']
        }
    ]
    
    # Step 2: Analyze companies for pain
    print("\n🔍 STEP 2: Analyzing Pain Signals...")
    
    detector = MultiSourcePainDetector()
    analyzed = []
    
    for company in test_companies:
        print(f"  Analyzing {company['company_name']}...")
        analysis = detector.analyze_company(company)
        analyzed.append(analysis)
        
        print(f"    ✓ Tier: {analysis['tam_tier']}")
        print(f"    ✓ Primary EDP: {analysis['primary_edp']}")
        print(f"    ✓ Pain Score: {analysis['total_pain_score']:.2f}")
    
    # Step 3: Generate campaigns for qualified companies
    print("\n✉️ STEP 3: Generating Campaigns...")
    
    generator = EvidenceBasedMessageGenerator()
    campaigns = []
    
    for analysis in analyzed:
        if analysis['qualified']:
            print(f"  Generating campaign for {analysis['company_name']}...")
            campaign = generator.generate_campaign(analysis)
            campaigns.append(campaign)
            
            print(f"    ✓ Strategy: {campaign['campaign_strategy']}")
            print(f"    ✓ Emails: {len(campaign['email_sequence'])}")
            print(f"    ✓ LinkedIn: {len(campaign['linkedin_messages'])}")
    
    # Step 4: Display sample messages
    print("\n📝 SAMPLE MESSAGES:")
    
    if campaigns:
        sample = campaigns[0]
        print(f"\nCompany: {sample['company_name']}")
        print(f"First Email Subject: {sample['email_sequence'][0]['subject']}")
        print(f"First Email Preview:")
        print("-" * 40)
        print(sample['email_sequence'][0]['body'][:500] + "...")
    
    # Step 5: Summary
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print(f"Companies Analyzed: {len(test_companies)}")
    print(f"Qualified: {sum(1 for a in analyzed if a['qualified'])}")
    print(f"Campaigns Created: {len(campaigns)}")
    print(f"Completed: {datetime.now()}")
    print("=" * 60)

def _check_channel_indicators(self, domain: str, home_soup: BeautifulSoup) -> Dict:
    """Check for channel conflict indicators"""
    evidence = {
        'edp': 'channel_conflict',
        'score': 0,
        'indicators_found': [],
        'specific_issues': []
    }
    try:
        # Try to find a login or pricing page if available
        channel_page_url = self._find_page_by_keywords(domain, ['login', 'pricing', 'portal', 'account'], home_soup)
        if channel_page_url:
            html = self._get_dynamic_html(channel_page_url)
            soup = BeautifulSoup(html, 'html.parser')
            text_content = soup.get_text().lower()
        else:
            # Fallback to homepage soup
            soup = home_soup
            text_content = soup.get_text().lower()

        # Check for multiple login types
        login_types = ['dealer login', 'customer login', 'trade login', 'rep login']
        login_count = sum(1 for login in login_types if login in text_content)
        if login_count > 2:
            evidence['indicators_found'].append('multiple_portals')
            evidence['specific_issues'].append(f'{login_count} different login portals found')
            evidence['score'] += 0.35

        # Check pricing visibility
        if '$' in text_content or 'price' in text_content:
            if 'login' in text_content and 'price' in text_content:
                evidence['indicators_found'].append('hidden_pricing')
                evidence['specific_issues'].append('Pricing requires login - channel conflict likely')
                evidence['score'] += 0.30
        else:
            evidence['indicators_found'].append('no_pricing')
            evidence['specific_issues'].append('No pricing visible at all')
            evidence['score'] += 0.35

    except Exception as e:
        logger.error(f"Error checking channels: {e}")

    # Determine evidence strength
    if evidence['score'] >= 0.6:
        evidence['evidence_strength'] = 'strong'
    elif evidence['score'] >= 0.3:
        evidence['evidence_strength'] = 'moderate'
    elif evidence['score'] > 0:
        evidence['evidence_strength'] = 'weak'
    return evidence

if __name__ == "__main__":
    asyncio.run(run_full_pipeline())