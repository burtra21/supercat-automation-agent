# orchestration/upload_pipeline.py
"""
Pipeline for processing uploaded CSV accounts
Runs them through the same analysis as scraped companies
Updated for actual prospect data
"""

import asyncio
import logging
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path
import pandas as pd

from scrapers.csv_uploader import CSVAccountUploader
from analysis.pain_detector import MultiSourcePainDetector
from analysis.qualification_scorer import WonDealQualificationScorer
from generation.evidence_based_messages import EvidenceBasedMessageGenerator
from database.connection import db
from orchestration.clay_webhook import ClayWebhookOrchestrator

logger = logging.getLogger(__name__)

class UploadPipeline:
    """
    Processes uploaded CSV accounts through the complete GTM pipeline
    """
    
    def __init__(self):
        self.uploader = CSVAccountUploader()
        self.pain_detector = MultiSourcePainDetector()
        self.qualifier = WonDealQualificationScorer()
        self.message_generator = EvidenceBasedMessageGenerator()
        self.clay_webhook = ClayWebhookOrchestrator()
        
        self.stats = {
            'uploaded': 0,
            'analyzed': 0,
            'qualified_tier1': 0,
            'qualified_tier2': 0,
            'qualified_tier3': 0,
            'disqualified': 0,
            'campaigns_created': 0,
            'sent_to_clay': 0,
            'errors': []
        }
    
    async def process_csv_upload(
        self, 
        csv_path: str,
        auto_campaign: bool = True,
        send_to_clay: bool = False,
        batch_size: int = 10
    ):
        """
        Process your 72 prospects through complete pipeline
        
        Args:
            csv_path: Path to your prospects CSV file
            auto_campaign: Automatically generate campaigns for qualified
            send_to_clay: Automatically send to Clay webhook
            batch_size: Process in batches for better performance
        """
        
        print(f"\n{'='*60}")
        print(f"SUPERCAT CSV UPLOAD PROCESSOR")
        print(f"File: {csv_path}")
        print(f"{'='*60}\n")
        
        # Step 1: Validate CSV
        print("📋 Step 1: Validating CSV...")
        valid, message = self.uploader.validate_csv(csv_path)
        if not valid:
            print(f"❌ Validation failed: {message}")
            return
        print(f"✅ {message}")
        
        # Step 2: Process CSV
        print("\n📥 Step 2: Loading companies from CSV...")
        companies = self.uploader.process_csv(csv_path)
        self.stats['uploaded'] = len(companies)
        print(f"✅ Loaded {len(companies)} companies")
        
        # Step 3: Analyze companies for pain signals (EDPs)
        print("\n🔍 Step 3: Analyzing websites for pain signals...")
        print(f"Processing in batches of {batch_size}...\n")
        
        analyzed_companies = []
        for i in range(0, len(companies), batch_size):
            batch = companies[i:i+batch_size]
            batch_num = (i // batch_size) + 1
            total_batches = (len(companies) + batch_size - 1) // batch_size
            
            print(f"Batch {batch_num}/{total_batches}: Processing {len(batch)} companies...")
            
            for company in batch:
                try:
                    # Run pain detection
                    analysis = await self.pain_detector.analyze_company(company)
                    
                    # Update company with analysis results
                    company.update(analysis)
                    
                    # Run qualification scoring
                    qualification = self.qualifier.score_company(company)
                    company.update(qualification)
                    
                    self.stats['analyzed'] += 1
                    
                    # Track tier distribution
                    tier = company.get('qualification_tier')
                    if tier == 'Tier 1':
                        self.stats['qualified_tier1'] += 1
                        print(f"  🔥 {company['company_name']}: TIER 1 (PSI: {company['psi_score']:.2f})")
                    elif tier == 'Tier 2':
                        self.stats['qualified_tier2'] += 1
                        print(f"  ✅ {company['company_name']}: Tier 2 (PSI: {company['psi_score']:.2f})")
                    elif tier == 'Tier 3':
                        self.stats['qualified_tier3'] += 1
                        print(f"  📊 {company['company_name']}: Tier 3 (PSI: {company['psi_score']:.2f})")
                    else:
                        self.stats['disqualified'] += 1
                        print(f"  ❌ {company['company_name']}: Not Qualified")
                    
                    analyzed_companies.append(company)
                    
                except Exception as e:
                    self.stats['errors'].append({
                        'company': company['company_name'],
                        'error': str(e)
                    })
                    print(f"  ⚠️ Error analyzing {company['company_name']}: {str(e)}")
                    
            # Small delay between batches
            if i + batch_size < len(companies):
                await asyncio.sleep(2)
        
        # Step 4: Generate campaigns for qualified companies
        if auto_campaign:
            print(f"\n✉️ Step 4: Generating campaigns for qualified companies...")
            qualified = [c for c in analyzed_companies if c.get('qualification_tier') in ['Tier 1', 'Tier 2']]
            
            if qualified:
                print(f"Creating campaigns for {len(qualified)} qualified companies...")
                
                for company in qualified:
                    try:
                        campaign = self.message_generator.generate_campaign(company)
                        company['campaign'] = campaign
                        self.stats['campaigns_created'] += 1
                        print(f"  ✅ Campaign created for {company['company_name']}")
                    except Exception as e:
                        print(f"  ⚠️ Campaign error for {company['company_name']}: {str(e)}")
            else:
                print("No qualified companies found for campaign generation")
        
        # Step 5: Save results to database
        print(f"\n💾 Step 5: Saving results to database...")
        await self._save_to_database(analyzed_companies)
        
        # Step 6: Send to Clay if requested
        if send_to_clay:
            print(f"\n🚀 Step 6: Sending to Clay webhook...")
            tier1_companies = [c for c in analyzed_companies if c.get('qualification_tier') == 'Tier 1']
            
            if tier1_companies:
                for company in tier1_companies[:5]:  # Send first 5 as test
                    try:
                        await self.clay_webhook.send_company(company)
                        self.stats['sent_to_clay'] += 1
                        print(f"  ✅ Sent {company['company_name']} to Clay")
                    except Exception as e:
                        print(f"  ⚠️ Clay error for {company['company_name']}: {str(e)}")
        
        # Step 7: Export results
        print(f"\n📊 Step 7: Exporting results...")
        results_path = self.uploader.export_results(analyzed_companies)
        
        # Print summary
        self._print_summary()
        
        return analyzed_companies
    
    async def _save_to_database(self, companies: List[Dict]):
        """Save companies to database"""
        try:
            for company in companies:
                # Save to companies table
                await db.execute("""
                    INSERT INTO companies (
                        company_name, domain, website, 
                        contact_first_name, contact_last_name, contact_email, contact_title,
                        industry, employee_count,
                        qualification_tier, psi_score, primary_edp,
                        source, created_at
                    ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14)
                    ON CONFLICT (domain) DO UPDATE SET
                        qualification_tier = $10,
                        psi_score = $11,
                        primary_edp = $12,
                        updated_at = NOW()
                """, 
                    company['company_name'], company['domain'], company['website'],
                    company.get('contact_first_name'), company.get('contact_last_name'),
                    company.get('contact_email'), company.get('contact_title'),
                    company.get('industry'), company.get('employee_count'),
                    company.get('qualification_tier'), company.get('psi_score'),
                    company.get('primary_edp'), 'csv_upload', datetime.now()
                )
            
            print(f"✅ Saved {len(companies)} companies to database")
        except Exception as e:
            print(f"⚠️ Database error: {str(e)}")
    
    def _print_summary(self):
        """Print processing summary"""
        print(f"\n{'='*60}")
        print(f"PROCESSING COMPLETE")
        print(f"{'='*60}")
        print(f"📊 Total uploaded: {self.stats['uploaded']}")
        print(f"✅ Successfully analyzed: {self.stats['analyzed']}")
        print(f"🔥 Tier 1 (Hot): {self.stats['qualified_tier1']}")
        print(f"🟡 Tier 2 (Warm): {self.stats['qualified_tier2']}")
        print(f"🔵 Tier 3 (Cool): {self.stats['qualified_tier3']}")
        print(f"❌ Not Qualified: {self.stats['disqualified']}")
        print(f"✉️ Campaigns created: {self.stats['campaigns_created']}")
        
        if self.stats['sent_to_clay'] > 0:
            print(f"🚀 Sent to Clay: {self.stats['sent_to_clay']}")
        
        if self.stats['errors']:
            print(f"\n⚠️ Errors encountered: {len(self.stats['errors'])}")
            for error in self.stats['errors'][:5]:
                print(f"  - {error['company']}: {error['error']}")
        
        # Calculate conversion rates
        if self.stats['analyzed'] > 0:
            tier1_rate = (self.stats['qualified_tier1'] / self.stats['analyzed']) * 100
            tier2_rate = (self.stats['qualified_tier2'] / self.stats['analyzed']) * 100
            qualified_rate = ((self.stats['qualified_tier1'] + self.stats['qualified_tier2']) / self.stats['analyzed']) * 100
            
            print(f"\n📈 Conversion Rates:")
            print(f"  Tier 1 Rate: {tier1_rate:.1f}%")
            print(f"  Tier 2 Rate: {tier2_rate:.1f}%")
            print(f"  Total Qualified: {qualified_rate:.1f}%")
        
        print(f"{'='*60}\n")

# Direct execution function for your 72 prospects
async def process_your_prospects():
    """Direct function to process your 72 prospects"""
    pipeline = UploadPipeline()
    
    # Update this path to your actual CSV file
    csv_path = "prospects.csv"  # YOUR FILE HERE
    
    # Process all 72 prospects
    results = await pipeline.process_csv_upload(
        csv_path=csv_path,
        auto_campaign=True,  # Generate campaigns for qualified
        send_to_clay=False,  # Set to True when ready to send to Clay
        batch_size=10  # Process 10 at a time
    )
    
    return results

if __name__ == "__main__":
    # Run the pipeline on your prospects
    asyncio.run(process_your_prospects())