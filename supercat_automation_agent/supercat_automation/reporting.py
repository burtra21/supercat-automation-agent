# reporting.py
'''Comprehensive reporting for SuperCat GTM'''

import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import json
from database.connection import db

class ReportGenerator:
    '''Generate comprehensive reports and exports'''
    
    def __init__(self):
        Path("output/reports").mkdir(parents=True, exist_ok=True)
        Path("output/exports").mkdir(parents=True, exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def generate_executive_summary(self):
        '''Generate executive summary report'''
        
        # Get data from last 30 days
        cutoff = (datetime.now() - timedelta(days=30)).isoformat()
        
        companies = db.client.table('companies').select('*').gte(
            'created_at', cutoff
        ).execute()
        
        campaigns = db.client.table('campaigns').select('*').gte(
            'created_at', cutoff
        ).execute()
        
        # Calculate metrics
        total_companies = len(companies.data) if companies.data else 0
        tier1 = sum(1 for c in companies.data if c.get('tam_tier') == 'TIER_1_IMMEDIATE')
        tier2 = sum(1 for c in companies.data if c.get('tam_tier') == 'TIER_2_QUARTERLY')
        
        # Calculate percentages safely
        tier1_pct = (tier1/total_companies*100) if total_companies > 0 else 0
        tier2_pct = (tier2/total_companies*100) if total_companies > 0 else 0
        qual_rate = ((tier1+tier2)/total_companies*100) if total_companies > 0 else 0
        
        # Generate report
        report = f'''
SUPERCAT GTM - EXECUTIVE SUMMARY
=====================================
Generated: {datetime.now()}
Period: Last 30 Days

KEY METRICS
-----------
Total Companies Analyzed: {total_companies}
Tier 1 Qualified: {tier1} ({tier1_pct:.1f}%)
Tier 2 Qualified: {tier2} ({tier2_pct:.1f}%)
Campaigns Created: {len(campaigns.data) if campaigns.data else 0}

QUALIFICATION RATE: {qual_rate:.1f}%

TOP PAIN POINTS
---------------'''
        
        if total_companies > 0:
            # Count EDPs
            edp_counts = {}
            for company in companies.data:
                for edp in company.get('edp_tags', []):
                    edp_counts[edp] = edp_counts.get(edp, 0) + 1
            
            for edp, count in sorted(edp_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                report += f"\n  - {edp}: {count} companies ({count/total_companies*100:.1f}%)"
        else:
            report += "\n  No data available yet - process some companies first!"
        
        # Save report
        report_path = f"output/reports/executive_summary_{self.timestamp}.txt"
        with open(report_path, 'w') as f:
            f.write(report)
        
        print(f"✅ Executive summary saved to: {report_path}")
        return report_path
    
    def export_qualified_prospects(self):
        '''Export qualified prospects to CSV'''
        
        # Get Tier 1 and 2 companies
        tier1 = db.get_companies_by_tier('TIER_1_IMMEDIATE')
        tier2 = db.get_companies_by_tier('TIER_2_QUARTERLY')
        
        all_qualified = tier1 + tier2
        
        if all_qualified:
            df = pd.DataFrame(all_qualified)
            
            # Select key columns (check which ones exist)
            available_columns = df.columns.tolist()
            export_columns = [col for col in [
                'company_name', 'domain', 'tam_tier', 'primary_edp',
                'psi_score', 'trade_shows', 'created_at'
            ] if col in available_columns]
            
            df_export = df[export_columns]
            
            # Sort by score if available
            if 'psi_score' in df_export.columns:
                df_export = df_export.sort_values('psi_score', ascending=False)
            
            # Save to CSV
            export_path = f"output/exports/qualified_prospects_{self.timestamp}.csv"
            df_export.to_csv(export_path, index=False)
            
            print(f"✅ Exported {len(df_export)} qualified prospects to: {export_path}")
            return export_path
        else:
            print("ℹ️ No qualified prospects to export yet")
            return None
    
    def export_campaign_messages(self):
        '''Export all campaign messages'''
        
        campaigns = db.client.table('campaigns').select('*').execute()
        
        if campaigns.data:
            all_messages = []
            
            for campaign in campaigns.data:
                # Get company info
                company = db.client.table('companies').select('company_name').eq(
                    'id', campaign['company_id']
                ).execute()
                
                company_name = company.data[0]['company_name'] if company.data else 'Unknown'
                
                # Extract email sequence
                for i, email in enumerate(campaign.get('email_sequence', [])):
                    all_messages.append({
                        'company': company_name,
                        'campaign_type': campaign['campaign_type'],
                        'channel': 'email',
                        'sequence': i + 1,
                        'subject': email.get('subject'),
                        'message': email.get('body')
                    })
            
            # Convert to DataFrame
            df = pd.DataFrame(all_messages)
            
            # Save to CSV
            export_path = f"output/exports/campaign_messages_{self.timestamp}.csv"
            df.to_csv(export_path, index=False)
            
            print(f"✅ Exported {len(df)} messages to: {export_path}")
            return export_path
        else:
            print("ℹ️ No campaigns to export yet")
            return None
    
    def generate_all_reports(self):
        '''Generate all reports and exports'''
        
        print("\n📊 GENERATING ALL REPORTS")
        print("-" * 40)
        
        # Executive summary
        self.generate_executive_summary()
        
        # Qualified prospects
        self.export_qualified_prospects()
        
        # Campaign messages
        self.export_campaign_messages()
        
        print("-" * 40)
        print("✅ All reports generated!")

if __name__ == "__main__":
    reporter = ReportGenerator()
    reporter.generate_all_reports()
