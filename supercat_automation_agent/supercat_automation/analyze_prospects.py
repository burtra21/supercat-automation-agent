#!/usr/bin/env python3
"""
Standalone CSV Processor for SuperCat GTM
Processes your 72 prospects through EDP detection
No dependencies - ready to run immediately
"""

import pandas as pd
import requests
from typing import Dict, List, Any
import json
from datetime import datetime
import argparse
from pathlib import Path
import time
import re
from urllib.parse import urlparse

class StandaloneEDPAnalyzer:
    """Analyzes companies for the 5 proven pain signals"""
    
    def __init__(self):
        # EDP definitions from your won-deal analysis
        self.edp_weights = {
            'sales_enablement_collapse': 1.0,  # 100% of won deals
            'technology_obsolescence': 0.93,   # 93% of won deals
            'rep_performance_crisis': 0.71,    # 71% of won deals
            'sku_complexity': 0.64,            # 64% of won deals
            'channel_conflict': 0.43           # 43% of won deals
        }
    
    def analyze_website(self, domain: str) -> Dict[str, Any]:
        """Analyze a website for pain signals"""
        
        # Normalize domain
        if not domain.startswith('http'):
            domain = f"https://{domain}"
        
        edp_scores = {}
        evidence = []
        
        try:
            # Make request with timeout
            response = requests.get(domain, timeout=10, verify=False)
            html_content = response.text.lower()
            
            # Check for Sales Enablement Collapse indicators
            sales_enablement_score = 0
            if 'product search' not in html_content and 'search products' not in html_content:
                sales_enablement_score += 0.3
                evidence.append("No product search functionality")
            if '.pdf' in html_content and 'catalog' in html_content:
                sales_enablement_score += 0.3
                evidence.append("PDF-only catalogs")
            if 'dealer login' in html_content or 'rep login' in html_content:
                sales_enablement_score += 0.2
                evidence.append("Manual dealer/rep login systems")
            if 'request quote' in html_content or 'call for pricing' in html_content:
                sales_enablement_score += 0.2
                evidence.append("Manual quote requests")
            edp_scores['sales_enablement_collapse'] = min(sales_enablement_score, 1.0)
            
            # Check for Technology Obsolescence
            tech_obsolescence_score = 0
            current_year = datetime.now().year
            copyright_match = re.search(r'©\s*(\d{4})', html_content)
            if copyright_match:
                year = int(copyright_match.group(1))
                if year < current_year - 2:
                    tech_obsolescence_score += 0.4
                    evidence.append(f"Outdated copyright year: {year}")
            if not response.url.startswith('https'):
                tech_obsolescence_score += 0.3
                evidence.append("No SSL certificate")
            if 'flash' in html_content or 'silverlight' in html_content:
                tech_obsolescence_score += 0.3
                evidence.append("Legacy technology detected")
            edp_scores['technology_obsolescence'] = min(tech_obsolescence_score, 1.0)
            
            # Check for Rep Performance Crisis
            rep_performance_score = 0
            if 'find a rep' not in html_content and 'locate dealer' not in html_content:
                rep_performance_score += 0.3
                evidence.append("No rep/dealer locator")
            if 'territory' not in html_content:
                rep_performance_score += 0.3
                evidence.append("No territory information")
            if 'sales resources' not in html_content and 'dealer resources' not in html_content:
                rep_performance_score += 0.4
                evidence.append("No sales resources section")
            edp_scores['rep_performance_crisis'] = min(rep_performance_score, 1.0)
            
            # Check for SKU Complexity
            sku_complexity_score = 0
            if 'configure' in html_content or 'customize' in html_content:
                sku_complexity_score += 0.3
                evidence.append("Product configuration complexity")
            if 'options' in html_content and 'finishes' in html_content:
                sku_complexity_score += 0.3
                evidence.append("Multiple options and finishes")
            if re.search(r'\d{3,}\s*products', html_content) or re.search(r'\d{3,}\s*items', html_content):
                sku_complexity_score += 0.4
                evidence.append("Large product catalog")
            edp_scores['sku_complexity'] = min(sku_complexity_score, 1.0)
            
            # Check for Channel Conflict
            channel_conflict_score = 0
            if html_content.count('login') > 2:
                channel_conflict_score += 0.4
                evidence.append("Multiple login portals")
            if 'dealer price' in html_content and 'retail price' in html_content:
                channel_conflict_score += 0.3
                evidence.append("Multiple pricing tiers visible")
            if 'where to buy' in html_content and 'buy online' in html_content:
                channel_conflict_score += 0.3
                evidence.append("Mixed channel messaging")
            edp_scores['channel_conflict'] = min(channel_conflict_score, 1.0)
            
        except Exception as e:
            print(f"  ⚠️ Could not analyze {domain}: {str(e)}")
            # Return neutral scores if can't access
            edp_scores = {edp: 0.5 for edp in self.edp_weights.keys()}
            evidence.append(f"Website analysis error: {str(e)}")
        
        # Calculate PSI (Pain Signal Intensity) score
        psi_score = sum(score * self.edp_weights[edp] for edp, score in edp_scores.items()) / sum(self.edp_weights.values())
        
        # Determine qualification tier
        if psi_score >= 0.7:
            tier = "Tier 1"
        elif psi_score >= 0.5:
            tier = "Tier 2"
        elif psi_score >= 0.3:
            tier = "Tier 3"
        else:
            tier = "Not Qualified"
        
        # Find primary EDP
        primary_edp = max(edp_scores.items(), key=lambda x: x[1] * self.edp_weights[x[0]])[0]
        
        return {
            'edp_scores': edp_scores,
            'psi_score': psi_score,
            'qualification_tier': tier,
            'primary_edp': primary_edp.replace('_', ' ').title(),
            'evidence': evidence
        }

def process_csv(file_path: str, limit: int = None, preview_only: bool = False):
    """Process the CSV file"""
    
    print(f"\n{'='*60}")
    print(f"SUPERCAT PROSPECT ANALYZER")
    print(f"{'='*60}\n")
    
    # Read CSV
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Error reading CSV: {str(e)}")
        return
    
    print(f"📁 File: {file_path}")
    print(f"📊 Total rows: {len(df)}")
    print(f"📋 Columns: {', '.join(df.columns)}\n")
    
    # Check for required columns
    required = ['company_name', 'domain']
    missing = [col for col in required if col not in df.columns]
    if missing:
        print(f"❌ Missing required columns: {missing}")
        return
    
    # Clean data
    df = df.dropna(subset=['company_name', 'domain'])
    print(f"✅ Valid companies: {len(df)}")
    
    if preview_only:
        print(f"\n📋 Preview (first 5 rows):")
        print(df.head().to_string())
        return
    
    # Apply limit if specified
    if limit:
        df = df.head(limit)
        print(f"🧪 Test mode: Processing only {limit} companies\n")
    
    # Initialize analyzer
    analyzer = StandaloneEDPAnalyzer()
    results = []
    
    # Process each company
    print(f"\n🔍 Analyzing websites for pain signals...\n")
    
    tier_counts = {'Tier 1': 0, 'Tier 2': 0, 'Tier 3': 0, 'Not Qualified': 0}
    
    for idx, row in df.iterrows():
        company_name = row['company_name']
        domain = row['domain']
        
        print(f"Analyzing {company_name}...", end=" ")
        
        # Analyze website
        analysis = analyzer.analyze_website(domain)
        
        # Build result record
        result = {
            'company_name': company_name,
            'domain': domain,
            'first_name': row.get('first_name', ''),
            'last_name': row.get('last_name', ''),
            'title': row.get('title', ''),
            'email': row.get('email', ''),
            'linkedin': row.get('LinkedIn Profile', ''),
            'industry': row.get('industry', ''),
            'employee_count': row.get('employee_count', ''),
            'qualification_tier': analysis['qualification_tier'],
            'psi_score': analysis['psi_score'],
            'primary_edp': analysis['primary_edp'],
            'evidence': '; '.join(analysis['evidence'][:3])  # Top 3 evidence points
        }
        
        # Add individual EDP scores
        for edp, score in analysis['edp_scores'].items():
            result[f'edp_{edp}'] = score
        
        results.append(result)
        tier_counts[analysis['qualification_tier']] += 1
        
        # Print result
        tier = analysis['qualification_tier']
        if tier == 'Tier 1':
            print(f"🔥 TIER 1 (PSI: {analysis['psi_score']:.2f})")
        elif tier == 'Tier 2':
            print(f"✅ Tier 2 (PSI: {analysis['psi_score']:.2f})")
        elif tier == 'Tier 3':
            print(f"📊 Tier 3 (PSI: {analysis['psi_score']:.2f})")
        else:
            print(f"❌ Not Qualified")
        
        # Small delay to avoid overwhelming servers
        time.sleep(0.5)
    
    # Save results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f"prospect_analysis_{timestamp}.csv"
    
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"ANALYSIS COMPLETE")
    print(f"{'='*60}")
    print(f"🔥 Tier 1 (Hot): {tier_counts['Tier 1']}")
    print(f"✅ Tier 2 (Warm): {tier_counts['Tier 2']}")
    print(f"📊 Tier 3 (Cool): {tier_counts['Tier 3']}")
    print(f"❌ Not Qualified: {tier_counts['Not Qualified']}")
    
    total = len(results)
    if total > 0:
        qualified = tier_counts['Tier 1'] + tier_counts['Tier 2']
        print(f"\n📈 Qualification Rate: {(qualified/total)*100:.1f}%")
        print(f"📈 Tier 1 Rate: {(tier_counts['Tier 1']/total)*100:.1f}%")
    
    print(f"\n📊 Results saved to: {output_file}")
    
    # Show top prospects
    if tier_counts['Tier 1'] > 0:
        print(f"\n🏆 TOP TIER 1 PROSPECTS:")
        print(f"{'='*60}")
        tier1_df = results_df[results_df['qualification_tier'] == 'Tier 1'].sort_values('psi_score', ascending=False)
        for idx, row in tier1_df.head(5).iterrows():
            print(f"• {row['company_name']}")
            print(f"  PSI Score: {row['psi_score']:.2f}")
            print(f"  Primary Pain: {row['primary_edp']}")
            if row['email']:
                print(f"  Contact: {row['first_name']} {row['last_name']} - {row['email']}")
            print()

def main():
    parser = argparse.ArgumentParser(description='Analyze prospects for SuperCat pain signals')
    parser.add_argument('csv_file', help='Path to your prospects CSV')
    parser.add_argument('--preview', action='store_true', help='Preview CSV without processing')
    parser.add_argument('--test', type=int, help='Test with only N companies')
    
    args = parser.parse_args()
    
    # Check file exists
    if not Path(args.csv_file).exists():
        print(f"❌ File not found: {args.csv_file}")
        print(f"Make sure to specify the correct path to your CSV file")
        return
    
    # Process
    process_csv(
        file_path=args.csv_file,
        limit=args.test,
        preview_only=args.preview
    )

if __name__ == "__main__":
    main()