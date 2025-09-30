"""
MVP Pipeline - Complete GTM Automation
This runs the entire flow from prospect identification to campaign generation
"""

import asyncio
import logging
from datetime import datetime
from pathlib import Path
import pandas as pd
from typing import Dict, List, Any
import uuid

from scrapers.vegas_market import VegasMarketScraper
from analysis.pain_detector import MultiSourcePainDetector
from analysis.prospect_processor import ProspectProcessor
from generation.evidence_based_messages import EvidenceBasedMessageGenerator
from database.connection import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SupercatMVPPipeline:
    """Complete MVP Pipeline for SuperCat GTM Automation"""
    
    def __init__(self):
        self.pain_detector = MultiSourcePainDetector()
        self.message_generator = EvidenceBasedMessageGenerator()
        self.prospect_processor = ProspectProcessor()
        self.stats = {
            "companies_processed": 0,
            "qualified_tier1": 0,
            "qualified_tier2": 0,
            "campaigns_created": 0,
            "errors": 0
        }
    
    async def run_mvp(self, source: str = "csv", csv_path: str = None):
        """
        Run the complete MVP pipeline
        
        Args:
            source: csv, scraper, or manual
            csv_path: Path to CSV if source is csv
        """
        
        print("=" * 70)
        print("SUPERCAT GTM AUTOMATION - MVP PIPELINE")
        print(f"Started: {datetime.now()}")
        print("=" * 70)
        
        try:
            # Step 1: Get Companies
            print("\nSTEP 1: Getting Companies...")
            companies = await self._get_companies(source, csv_path)
            print(f"Found {len(companies)} companies to process")
            
            # Step 2: Analyze for Pain
            print("\nSTEP 2: Analyzing Pain Signals...")
            analyzed_companies = await self._analyze_companies(companies)
            print(f"Analyzed {len(analyzed_companies)} companies")
            
            # Step 3: Generate Campaigns for Qualified
            print("\nSTEP 3: Generating Campaigns...")
            campaigns = await self._generate_campaigns(analyzed_companies)
            print(f"Generated {len(campaigns)} campaigns")
            
            # Step 4: Prepare for Execution
            print("\nSTEP 4: Preparing Outreach...")
            outreach_ready = await self._prepare_outreach(campaigns)
            print(f"Prepared {outreach_ready} outreach sequences")
            
            # Step 5: Generate Reports
            print("\nSTEP 5: Generating Reports...")
            self._generate_reports(analyzed_companies, campaigns)
            
            print("\n" + "=" * 70)
            print("MVP PIPELINE COMPLETE!")
            print(f"Results:")
            print(f"  - Companies Processed: {self.stats['companies_processed']}")
            print(f"  - Tier 1 Qualified: {self.stats['qualified_tier1']}")
            print(f"  - Tier 2 Qualified: {self.stats['qualified_tier2']}")
            print(f"  - Campaigns Created: {self.stats['campaigns_created']}")
            print(f"  - Errors: {self.stats['errors']}")
            print("=" * 70)
            
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            self.stats["errors"] += 1
            raise
    
    async def _get_companies(self, source: str, csv_path: str = None) -> List[Dict]:
        """Get companies from various sources"""
        
        companies = []
        
        if source == "csv" and csv_path:
            # Load from CSV
            df = pd.read_csv(csv_path)
            for _, row in df.iterrows():
                companies.append({
                    "id": str(uuid.uuid4()),
                    "company_name": row["company_name"],
                    "domain": row["domain"],
                    "trade_shows": row.get("trade_shows", "").split(",") if pd.notna(row.get("trade_shows")) else []
                })
                
        elif source == "scraper":
            # Use trade show scraper
            scraper = VegasMarketScraper()
            results = scraper.run()
            # Convert scraper results to company format
            # (Implementation depends on scraper output)
            
        elif source == "manual":
            # Use test companies
            companies = [
                {
                    "id": str(uuid.uuid4()),
                    "company_name": "Ashley Furniture",
                    "domain": "ashleyfurniture.com",
                    "trade_shows": ["Vegas Market", "High Point Market"]
                },
                {
                    "id": str(uuid.uuid4()),
                    "company_name": "Hooker Furniture",
                    "domain": "hookerfurniture.com",
                    "trade_shows": ["High Point Market"]
                }
            ]
        
        return companies
    
    async def _analyze_companies(self, companies: List[Dict]) -> List[Dict]:
        """Analyze companies for pain signals"""
        
        analyzed = []
        
        for company in companies:
            try:
                print(f"  Analyzing {company['company_name']}...")
                
                # Run pain detection
                analysis = self.pain_detector.analyze_company(company)
                
                # Add analysis to company data
                company["analysis"] = analysis
                company["tam_tier"] = analysis["tam_tier"]
                company["primary_edp"] = analysis["primary_edp"]
                company["psi_score"] = analysis["total_pain_score"]
                
                # Update stats
                self.stats["companies_processed"] += 1
                if analysis["tam_tier"] == "TIER_1_IMMEDIATE":
                    self.stats["qualified_tier1"] += 1
                elif analysis["tam_tier"] == "TIER_2_QUARTERLY":
                    self.stats["qualified_tier2"] += 1
                
                # Save to database
                self._save_company(company, analysis)
                
                analyzed.append(company)
                
                score = analysis["total_pain_score"]
                tier = analysis["tam_tier"]
                print(f"    {company['company_name']}: {tier} (Score: {score:.2f})")
                
            except Exception as e:
                logger.error(f"Error analyzing {company['company_name']}: {e}")
                self.stats["errors"] += 1
        
        return analyzed
    
    async def _generate_campaigns(self, companies: List[Dict]) -> List[Dict]:
        """Generate campaigns for qualified companies"""
        
        campaigns = []
        
        # Filter for qualified companies
        qualified = [c for c in companies if c.get("tam_tier") in ["TIER_1_IMMEDIATE", "TIER_2_QUARTERLY"]]
        
        for company in qualified:
            try:
                print(f"  Generating campaign for {company['company_name']}...")
                
                # Generate campaign
                campaign = self.message_generator.generate_campaign(company["analysis"])
                
                # Save to database
                campaign_record = {
                    "id": str(uuid.uuid4()),
                    "company_id": company["id"],
                    "campaign_type": campaign["campaign_strategy"],
                    "pain_point_focus": campaign["primary_edp"],
                    "email_sequence": campaign["email_sequence"],
                    "linkedin_messages": campaign.get("linkedin_messages", []),
                    "campaign_status": "ready",
                    "created_at": datetime.now().isoformat()
                }
                
                # Save campaign
                db.create_campaign(campaign_record)
                
                campaigns.append(campaign_record)
                self.stats["campaigns_created"] += 1
                
                print(f"    Campaign created: {campaign['campaign_strategy']}")
                
            except Exception as e:
                logger.error(f"Error generating campaign for {company['company_name']}: {e}")
                self.stats["errors"] += 1
        
        return campaigns
    
    async def _prepare_outreach(self, campaigns: List[Dict]) -> int:
        """Prepare outreach records for campaigns"""
        
        outreach_count = 0
        
        for campaign in campaigns:
            try:
                # Create outreach records for each email
                for i, email in enumerate(campaign.get("email_sequence", [])):
                    outreach = {
                        "campaign_id": campaign["id"],
                        "company_id": campaign["company_id"],
                        "channel": "email",
                        "sequence_step": i + 1,
                        "subject_line": email.get("subject"),
                        "message_body": email.get("body"),
                        "status": "pending",
                        "scheduled_send_date": email.get("send_date")
                    }
                    
                    # Save to database
                    db.create_outreach(outreach)
                    outreach_count += 1
                
            except Exception as e:
                logger.error(f"Error preparing outreach: {e}")
                self.stats["errors"] += 1
        
        return outreach_count
    
    def _save_company(self, company: Dict, analysis: Dict):
        """Save company and analysis to database"""
        
        try:
            db_record = {
                "id": company["id"],
                "company_name": company["company_name"],
                "domain": company["domain"],
                "trade_shows": company.get("trade_shows", []),
                "tam_tier": analysis["tam_tier"],
                "primary_edp": analysis["primary_edp"],
                "edp_tags": analysis["edp_tags"],
                "edp_scores": analysis["edp_scores"],
                "psi_score": analysis["total_pain_score"],
                "has_multiple_edps": analysis["has_multiple_edps"],
                "website_evidence": analysis["evidence"].get("website", {}),
                "last_website_scan": datetime.now().isoformat()
            }
            
            db.upsert_company(db_record)
            
        except Exception as e:
            logger.error(f"Error saving company: {e}")
    
    def _generate_reports(self, companies: List[Dict], campaigns: List[Dict]):
        """Generate analysis reports"""
        
        # Create reports directory
        Path("output/reports").mkdir(parents=True, exist_ok=True)
        
        # Generate summary report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = f"output/reports/mvp_report_{timestamp}.txt"
        
        with open(report_path, "w") as f:
            f.write(f"""SUPERCAT GTM AUTOMATION - MVP REPORT
=====================================
Generated: {datetime.now()}

COMPANIES ANALYZED: {len(companies)}
-----------------
""")
            
            for company in companies:
                analysis = company.get("analysis", {})
                f.write(f"""
Company: {company["company_name"]}
Domain: {company["domain"]}
TAM Tier: {analysis.get("tam_tier", "Unknown")}
Primary Pain: {analysis.get("primary_edp", "Unknown")}
Pain Score: {analysis.get("total_pain_score", 0):.2f}
EDPs Detected: {", ".join(analysis.get("edp_tags", []))}
""")
            
            f.write(f"""

CAMPAIGNS CREATED: {len(campaigns)}
-----------------
""")
            
            for campaign in campaigns:
                f.write(f"""
Campaign ID: {campaign["id"]}
Type: {campaign["campaign_type"]}
Focus: {campaign["pain_point_focus"]}
Emails: {len(campaign.get("email_sequence", []))}
Status: {campaign["campaign_status"]}
""")
        
        print(f"\nReport saved to: {report_path}")
        
        # Also create a CSV for easy analysis
        df = pd.DataFrame([{
            "company_name": c["company_name"],
            "domain": c["domain"],
            "tam_tier": c.get("tam_tier"),
            "primary_edp": c.get("primary_edp"),
            "pain_score": c.get("psi_score", 0),
            "qualified": c.get("tam_tier") in ["TIER_1_IMMEDIATE", "TIER_2_QUARTERLY"]
        } for c in companies])
        
        csv_path = f"output/reports/analysis_{timestamp}.csv"
        df.to_csv(csv_path, index=False)
        print(f"CSV saved to: {csv_path}")

# Run the MVP
if __name__ == "__main__":
    import sys
    
    pipeline = SupercatMVPPipeline()
    
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1].endswith(".csv"):
        # Run with CSV file
        asyncio.run(pipeline.run_mvp(source="csv", csv_path=sys.argv[1]))
    else:
        # Run with manual test companies
        asyncio.run(pipeline.run_mvp(source="manual"))
