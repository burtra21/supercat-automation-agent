# Complete Project Context
Generated: 2025-08-25T14:43:59.834694

## Project Structure
```
./
  PROJECT_CONTEXT_FULL.md
  EDP_detection.txt
  project_context.txt
  upload_prospects.py
  evidence_based_EDP.txt
  output/
    ads/
    exports/
    reports/
  supercat_automation/
    analyze_prospects.py
    create_tables.sql
    generate_context.py
    full_pipeline.py
    requirements.txt
    PROJECT_CONTEXT_FULL.md
    full_orchestrator.py
    fix_imports.py
    health_monitor.py
    pipeline_results_20250823_074654.json
    mvp_pipeline.py
    menu.py
    add_personalization_method.py
    check_status.py
    generate_webhooks.py
    run_pipeline.py
    companies_to_analyze.csv
    automated_daily.py
    prospect_analysis_20250823_070442.csv
    test_companies.csv
    simple_test.py
    fix_type_hints.py
    sample_prospects.csv
    main.py
    prospects.csv
    performance_dashboard.py
    reporting.py
    master_control.py
    database/
      models.py
      __init__.py
      connection.py
      migrations.py
    analysis/
      psi_calculator.py
      __init__.py
      qualification_scorer.py
      customer_language.py
      prospect_processor.py
      pain_detector.py
    config/
      credentials.py
      __init__.py
      settings.py
    tests/
      test_pain_detection.py
    output/
      ads/
      exports/
      results/
        prospects_20250816_021459.csv
        prospects_20250816_030753.csv
      reports/
        scraping_report_20250817_093923.txt
        orchestrator_report_20250816_093339.txt
        orchestrator_report_20250816_090221.txt
        scraping_report_20250816_084202.txt
        scraping_report_20250816_085045.txt
        scraping_report_20250816_084615.txt
        orchestrator_report_20250816_060415.txt
        orchestrator_report_20250816_090519.txt
        scraping_report_20250816_080833.txt
        orchestrator_report_20250816_083216.txt
        scraping_report_20250816_092952.txt
        orchestrator_report_20250816_090901.txt
        orchestrator_report_20250816_092051.txt
        scraping_report_20250816_082823.txt
        scraping_report_20250816_081241.txt
        scraping_report_20250816_082403.txt
        orchestrator_report_20250816_055657.txt
        orchestrator_report_20250816_053151.txt
        executive_summary_20250816_030818.txt
        scraping_report_20250818_103254.txt
        scraping_report_20250816_093339.txt
        orchestrator_report_20250816_084202.txt
        scraping_report_20250816_090221.txt
        scraping_report_20250816_052944.txt
        orchestrator_report_20250816_085045.txt
        orchestrator_report_20250816_084615.txt
        scraping_report_20250816_060415.txt
        orchestrator_report_20250816_082823.txt
        scraping_report_20250816_092051.txt
        scraping_report_20250816_090901.txt
        orchestrator_report_20250816_092952.txt
        orchestrator_report_20250816_143851.txt
        scraping_report_20250816_090518.txt
        scraping_report_20250816_083216.txt
        orchestrator_report_20250816_082403.txt
        orchestrator_report_20250816_081242.txt
        scraping_report_20250816_115058.txt
        scraping_report_20250816_055440.txt
        orchestrator_report_20250816_080834.txt
    dashboard/
      metrics.py
      __init__.py
      visualizations.py
      app.py
    logs/
      daily_automation.log
    orchestration/
      message_preparation.py
      upload_pipeline.py
      __init__.py
      scheduling.py
      campaign_coordinator.py
      clay_webhook.py
    templates/
      prospect_upload_template.csv
      client_calidation_template.csv
    enrichment/
      company_enricher.py
      __init__.py
      clay_integration.py
    scrapers/
      high_point.py
      __init__.py
      base_scraper.py
      csv_uploader.py
      orchestrator.py
      americasmart.py
      vegas_market.py
      trade_show_scraper.py
      website_evidence.py
    webhooks/
      48640800-ed41-4a60-bc22-dfc2c42df639_ERG_International.json
      b2325193-d71a-41f7-99c4-6fa17c9a5afb_Anne_McGilvray_&_Company.json
      2ff89582-fc0d-4571-bc78-30a7fdc4b020_EJ_Victor.json
      c32cb0df-2c54-4b26-a6b3-ccfe3b13171e_Castelle.json
      8a0f4247-df5a-4b0b-a83e-84cf961ad799_Anne_McGilvray_Company.json
      4d6e7c96-a840-43d2-a9ba-b1a814338df2_Allstate_Floral,_Inc..json
      7f1149b6-9047-4cda-bbec-81d4565b779c_CTG_Brands_Inc..json
      efc00576-22a6-41a5-900c-6ad687c44b5e_Capel_Rugs.json
      76c2e653-99c4-489c-8533-25de660a567a_Dovetail_Furniture_Pvt_Ltd.json
      24e5f52c-4639-439f-9b54-40d5f60772cf_burton_+_BURTON.json
      53b5f9d2-405f-4cae-86ad-0b59a9c10260_Golden_Rabbit_II,_Inc..json
      cbd2f13a-fea3-4383-80a6-7d7fd43d475f_Bulbrite_Industries.json
      e1c68f85-5d0d-4601-9f21-a9df685cbc46_Fanimation.json
      2565aca4-1b2e-4527-9bfd-5d6821592729_A_B_HOME_GROUP_INC.json
      45fdbe0e-31bc-4d44-8b8c-f0c08d0aee7f_9to5_Seating.json
      9efce539-340b-4bf9-bf0f-3a61bf1b9dc6_A_Rudin.json
      summary_20250823_072035.csv
      0b23af6c-2481-41ad-9881-6d17b91c3eeb_EGLO_Leuchten.json
      fe2e9061-b350-465b-b33a-2c452a48b463_Golden_Rabbit_II_Inc.json
      c417c22b-63ce-42be-99cf-5a9af96a5741_Coaster_Company_of_America.json
      93156f30-f9ad-4335-a46f-10e4405cd7ab_Atkore.json
      b87cd46a-90ff-45e3-8723-e88e09d7472c_World_of_Eichholtz.json
      72143970-b29b-4766-80d8-8e13c887edea_9to5_Seating.json
      8c5068b8-92ff-45c4-a56a-b23fe8fecad1_Capel_Rugs.json
      56d8b7f2-fac0-48c4-b33b-09d393beef6e_Atkore.json
      a9cf24b1-3e1a-4df8-854b-b1355ee66f02_Castelle.json
      fb9a77d7-7544-468e-a427-efbb9810b31f_Century_Furniture.json
      1b443b5a-e030-41fa-b091-21664d6cb86a_Allstate_Floral_Inc.json
      05025502-d564-44c9-b208-1ac8a8a81a5b_Abbott_Collection.json
      51ea9907-d435-41a6-bc64-352c49a53ba0_Bernhardt_Furniture_Co.json
      batch_20250823_072035.json
    generation/
      evidence_based_messages.py
      message_generator.py
      email_sequences.py
      __init__.py
      ad_copy_generator.py
      linkedin_messages.py
      pvp_ad_generator.py
      pvp_message_generator.py
  logs/
```

## Python Source Files

### upload_prospects.py
```python

```

### supercat_automation/analyze_prospects.py
```python
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
```

### supercat_automation/generate_context.py
```python
#!/usr/bin/env python3
"""
Generate complete project context for Claude Code
"""

import os
import json
from pathlib import Path
from datetime import datetime
import argparse

class ProjectContextGenerator:
    def __init__(self, project_root='.', output_file='PROJECT_CONTEXT_FULL.md'):
        self.project_root = Path(project_root)
        self.output_file = output_file
        self.ignore_patterns = {
            '__pycache__', '.git', 'venv', 'env', '.venv',
            '.pytest_cache', 'node_modules', '*.pyc',
            '.DS_Store', '*.log'
        }
        
    def should_include(self, path):
        """Check if file should be included"""
        path_str = str(path)
        for pattern in self.ignore_patterns:
            if pattern in path_str:
                return False
        return True
    
    def get_file_tree(self):
        """Generate file tree structure"""
        tree_lines = []
        for root, dirs, files in os.walk(self.project_root):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not any(p in d for p in self.ignore_patterns)]
            
            level = root.replace(str(self.project_root), '').count(os.sep)
            indent = '  ' * level
            tree_lines.append(f"{indent}{os.path.basename(root)}/")
            
            subindent = '  ' * (level + 1)
            for file in files:
                if not any(p in file for p in self.ignore_patterns):
                    tree_lines.append(f"{subindent}{file}")
        
        return '\n'.join(tree_lines)
    
    def generate_context(self):
        """Generate the complete context file"""
        with open(self.output_file, 'w') as f:
            # Header
            f.write("# Complete Project Context\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")
            
            # Project structure
            f.write("## Project Structure\n")
            f.write("```\n")
            f.write(self.get_file_tree())
            f.write("\n```\n\n")
            
            # Python files
            f.write("## Python Source Files\n\n")
            for py_file in self.project_root.rglob("*.py"):
                if self.should_include(py_file):
                    relative_path = py_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```python\n")
                    try:
                        f.write(py_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # Configuration files
            f.write("## Configuration Files\n\n")
            
            # YAML files
            for yaml_file in list(self.project_root.rglob("*.yaml")) + list(self.project_root.rglob("*.yml")):
                if self.should_include(yaml_file):
                    relative_path = yaml_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```yaml\n")
                    try:
                        f.write(yaml_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # JSON files
            for json_file in self.project_root.rglob("*.json"):
                if self.should_include(json_file) and 'package-lock' not in str(json_file):
                    relative_path = json_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```json\n")
                    try:
                        f.write(json_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # SQL files
            f.write("## Database Schema\n\n")
            for sql_file in self.project_root.rglob("*.sql"):
                if self.should_include(sql_file):
                    relative_path = sql_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```sql\n")
                    try:
                        f.write(sql_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # Requirements
            if (self.project_root / "requirements.txt").exists():
                f.write("## Requirements\n")
                f.write("```\n")
                try:
                    f.write((self.project_root / "requirements.txt").read_text())
                except:
                    f.write("# Could not read file\n")
                f.write("\n```\n\n")
            
            # README
            if (self.project_root / "README.md").exists():
                f.write("## README\n")
                try:
                    f.write((self.project_root / "README.md").read_text())
                except:
                    f.write("# Could not read file\n")
                f.write("\n\n")
        
        # Print summary
        file_size = os.path.getsize(self.output_file) / 1024 / 1024  # MB
        with open(self.output_file, 'r') as f:
            line_count = sum(1 for _ in f)
        
        print(f"✅ Context file generated: {self.output_file}")
        print(f"�� File size: {file_size:.2f} MB")
        print(f"📝 Total lines: {line_count:,}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate project context')
    parser.add_argument('--root', default='.', help='Project root directory')
    parser.add_argument('--output', default='PROJECT_CONTEXT_FULL.md', help='Output file name')
    
    args = parser.parse_args()
    
    generator = ProjectContextGenerator(args.root, args.output)
    generator.generate_context()

```

### supercat_automation/full_pipeline.py
```python
#!/usr/bin/env python3
"""
SuperCat Integrated Pipeline - Combines full_pipeline.py with website_evidence.py
Uses your existing WebsiteEvidenceExtractor for detailed analysis
"""

import pandas as pd
import json
import os
import re
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import asyncio
import aiohttp
import logging
import sys

# Add scrapers to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scrapers'))

# Import your existing website evidence extractor
try:
    from scrapers.website_evidence import WebsiteEvidenceExtractor
    HAS_EVIDENCE_EXTRACTOR = True
except ImportError as e:
    print(f"Import error: {e}")
    HAS_EVIDENCE_EXTRACTOR = False

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4-turbo')
CLAY_WEBHOOK_URL = os.getenv('CLAY_WEBHOOK_URL')

# Initialize OpenAI (keeping your version detection)
try:
    from openai import OpenAI
    openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
    OPENAI_VERSION = "new"
except ImportError:
    import openai
    openai.api_key = OPENAI_API_KEY
    openai_client = None
    OPENAI_VERSION = "old"

# Supabase
try:
    from supabase import create_client, Client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL else None
except:
    supabase = None

print(f"✅ Environment loaded:")
print(f"  • OpenAI: {OPENAI_VERSION} version - {'Connected' if OPENAI_API_KEY else 'Not configured'}")
print(f"  • Supabase: {'Connected' if supabase else 'Not configured'}")
print(f"  • Clay Webhook: {'Connected' if CLAY_WEBHOOK_URL else 'Not configured'}")
print(f"  • Evidence Extractor: {'Available' if HAS_EVIDENCE_EXTRACTOR else 'Using basic mode'}")


class IntegratedPipelineProcessor:
    """Enhanced pipeline using WebsiteEvidenceExtractor for detailed analysis"""
    
    def __init__(self):
        self.session = None
        self.clay_webhook_url = CLAY_WEBHOOK_URL
        
        # Initialize the evidence extractor if available
        if HAS_EVIDENCE_EXTRACTOR:
            self.evidence_extractor = WebsiteEvidenceExtractor()
        else:
            self.evidence_extractor = None
        
        self.stats = {
            'processed': 0,
            'qualified': 0,
            'sent_to_clay': 0,
            'saved_to_supabase': 0,
            'errors': []
        }
        
        self.edp_weights = {
            'sales_enablement_collapse': 1.0,
            'technology_obsolescence': 0.93,
            'rep_performance_crisis': 0.71,
            'sku_complexity': 0.64,
            'channel_conflict': 0.43
        }
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
    
    def analyze_website_enhanced(self, domain: str) -> Dict:
        """
        Use WebsiteEvidenceExtractor for detailed analysis
        Falls back to basic analysis if not available
        """
        
        if self.evidence_extractor:
            # Use your sophisticated extractor
            print(f"  🔍 Using enhanced evidence extraction...")
            return self.evidence_extractor.analyze_website(domain)
        else:
            # Fallback to basic analysis
            return self.analyze_website_basic(domain)
    
    async def analyze_website_basic(self, domain: str) -> Dict:
        """Basic fallback analysis (your original method)"""
        
        if not domain.startswith('http'):
            domain = f"https://{domain}"
        
        analysis = {
            'domain': domain,
            'evidence': [],
            'tech_stack': []
        }
        
        try:
            async with self.session.get(domain, timeout=10, ssl=False) as response:
                html = await response.text()
                html_lower = html.lower()
                
                # Your original basic checks
                if 'product search' not in html_lower:
                    analysis['evidence'].append("No product search functionality")
                if '.pdf' in html_lower and 'catalog' in html_lower:
                    analysis['evidence'].append("PDF-only catalogs detected")
                if 'dealer login' in html_lower or 'rep login' in html_lower:
                    analysis['evidence'].append("Manual dealer/rep login system")
                if 'request quote' in html_lower:
                    analysis['evidence'].append("Manual quote request process")
                
                if not response.url.scheme == 'https':
                    analysis['evidence'].append("No SSL certificate")
                if 'wordpress' in html_lower:
                    analysis['tech_stack'].append("WordPress")
                    
        except Exception as e:
            analysis['error'] = str(e)
            logger.error(f"Scraping error for {domain}: {e}")
        
        return analysis
    
    def process_enhanced_evidence(self, evidence_data: Dict) -> Dict:
        """
        Process the enhanced evidence from WebsiteEvidenceExtractor
        into format needed for GPT and Clay
        """
        
        processed = {
            'edp_scores': {},
            'primary_edp': None,
            'psi_score': 0,
            'qualification_tier': 'NOT_QUALIFIED',
            'key_evidence': [],
            'detailed_evidence': {}
        }
        
        # Extract EDP scores
        if 'edp_evidence' in evidence_data:
            for edp_name, evidence in evidence_data['edp_evidence'].items():
                processed['edp_scores'][edp_name] = evidence.get('score', 0)
                
                # Collect specific issues as evidence
                if evidence.get('specific_issues'):
                    processed['key_evidence'].extend(evidence['specific_issues'][:2])
                
                # Store detailed evidence for Clay
                processed['detailed_evidence'][edp_name] = {
                    'score': evidence.get('score', 0),
                    'indicators': evidence.get('indicators_found', []),
                    'issues': evidence.get('specific_issues', []),
                    'strength': evidence.get('evidence_strength', 'none')
                }
        
        # Use TAM indicators if available
        if 'tam_indicators' in evidence_data:
            tam = evidence_data['tam_indicators']
            processed['primary_edp'] = tam.get('primary_edp', 'unknown')
            processed['psi_score'] = tam.get('total_pain_score', 0) * 100 / 3  # Normalize to 0-100
            
            # Map tier
            tier_map = {
                'TIER_1_HOT': 'TIER_1_IMMEDIATE',
                'TIER_2_WARM': 'TIER_2_ACTIVE', 
                'TIER_3_COOL': 'TIER_3_NURTURE',
                'TIER_4_COLD': 'NOT_QUALIFIED'
            }
            processed['qualification_tier'] = tier_map.get(tam.get('tier', 'TIER_4_COLD'), 'NOT_QUALIFIED')
        
        # Add personalization hooks
        if 'personalization_hooks' in evidence_data:
            processed['personalization_data'] = evidence_data['personalization_hooks']
        
        # Limit key evidence to top 5
        processed['key_evidence'] = processed['key_evidence'][:5]
        
        return processed
    
    def gpt_analysis_enhanced(self, company_data: Dict, website_analysis: Dict) -> Dict:
        """
        Enhanced GPT analysis using detailed evidence
        """
        
        if not OPENAI_API_KEY:
            # If no GPT, use the processed evidence directly
            return website_analysis
        
        # Build a more detailed prompt with specific evidence
        evidence_summary = []
        if 'detailed_evidence' in website_analysis:
            for edp, details in website_analysis['detailed_evidence'].items():
                if details['issues']:
                    evidence_summary.append(f"{edp}: {', '.join(details['issues'][:2])}")
        
        prompt = f"""
        Analyze this furniture/lighting company based on detailed website evidence.
        
        Company: {company_data['company_name']}
        Domain: {company_data['domain']}
        
        Evidence Found:
        {json.dumps(evidence_summary, indent=2)}
        
        EDP Scores (0-1 scale):
        {json.dumps(website_analysis.get('edp_scores', {}), indent=2)}
        
        Current Assessment:
        - Primary EDP: {website_analysis.get('primary_edp')}
        - PSI Score: {website_analysis.get('psi_score', 0):.1f}%
        - Suggested Tier: {website_analysis.get('qualification_tier')}
        
        Please validate and enhance this analysis. Return JSON with:
        1. validated_edp_scores: Adjusted scores based on evidence
        2. confirmed_primary_edp: Most critical pain point
        3. final_psi_score: Overall pain score (0-100)
        4. final_tier: TIER_1_IMMEDIATE, TIER_2_ACTIVE, TIER_3_NURTURE, or NOT_QUALIFIED
        5. messaging_hooks: Top 3 specific pain points to mention in outreach
        6. personalization_elements: Specific details to reference (trade shows, product categories, etc.)
        
        Focus on accuracy - only confirm pain points with strong evidence.
        """
        
        try:
            if OPENAI_VERSION == "new" and openai_client:
                response = openai_client.chat.completions.create(
                    model=OPENAI_MODEL,
                    messages=[
                        {"role": "system", "content": "You are a B2B sales expert analyzing furniture/lighting companies. Be precise and evidence-based."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                content = response.choices[0].message.content
            else:
                import openai
                response = openai.ChatCompletion.create(
                    model=OPENAI_MODEL,
                    messages=[
                        {"role": "system", "content": "You are a B2B sales expert analyzing furniture/lighting companies. Be precise and evidence-based."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                content = response.choices[0].message.content
            
            # Parse GPT response
            gpt_result = json.loads(content)
            
            # Merge with existing analysis
            website_analysis['edp_scores'] = gpt_result.get('validated_edp_scores', website_analysis['edp_scores'])
            website_analysis['primary_edp'] = gpt_result.get('confirmed_primary_edp', website_analysis['primary_edp'])
            website_analysis['psi_score'] = gpt_result.get('final_psi_score', website_analysis['psi_score'])
            website_analysis['qualification_tier'] = gpt_result.get('final_tier', website_analysis['qualification_tier'])
            website_analysis['messaging_hooks'] = gpt_result.get('messaging_hooks', website_analysis.get('key_evidence', []))
            website_analysis['personalization_elements'] = gpt_result.get('personalization_elements', [])
            
        except Exception as e:
            logger.error(f"GPT enhancement error: {e}")
            # Keep original analysis if GPT fails
        
        return website_analysis
    
    async def save_to_supabase_enhanced(self, company_data: Dict, analysis: Dict):
        """Save enhanced data to Supabase - FIXED"""
        
        if not supabase:
            return
        
        try:
            # Build record with proper data types
            record = {
                'company_name': str(company_data.get('company_name', '')),
                'domain': str(company_data.get('domain', '')),
                'qualification_tier': str(analysis.get('qualification_tier', '')),
                'primary_edp': str(analysis.get('primary_edp', ''))
            }
            
            # Add optional fields with proper types
            if company_data.get('email'):
                record['email'] = str(company_data['email'])
            if company_data.get('first_name'):
                record['first_name'] = str(company_data['first_name'])
            if company_data.get('last_name'):
                record['last_name'] = str(company_data['last_name'])
            
            # Handle psi_score as float if column exists
            if analysis.get('psi_score') is not None:
                try:
                    record['psi_score'] = float(analysis['psi_score'])
                except:
                    pass
            
            # Don't send complex objects - convert to JSON strings if needed
            # Skip edp_scores and key_evidence for now unless columns exist
            
            result = supabase.table('companies').insert(record).execute()
            self.stats['saved_to_supabase'] += 1
            print(f"  💾 Saved to Supabase")
            
        except Exception as e:
            logger.warning(f"Supabase save error (non-critical): {e}")
    
    async def send_to_clay_enhanced(self, company_data: Dict, analysis: Dict):
        """Send enhanced data to Clay webhook - FIXED"""
        
        if not self.clay_webhook_url:
            return
        
        try:
            # Clean the data - remove None values and ensure JSON serializable
            def clean_for_json(obj):
                if isinstance(obj, dict):
                    return {k: clean_for_json(v) for k, v in obj.items() if v is not None}
                elif isinstance(obj, list):
                    return [clean_for_json(item) for item in obj if item is not None]
                elif isinstance(obj, (str, int, float, bool)):
                    return obj
                else:
                    return str(obj)
            
            # Build webhook payload with cleaned data
            webhook_payload = {
                'company_name': company_data.get('company_name', ''),
                'domain': company_data.get('domain', ''),
                'tam_tier': analysis.get('qualification_tier', ''),
                'psi_score': float(analysis.get('psi_score', 0)),  # Ensure float
                'primary_edp': analysis.get('primary_edp', 'unknown'),
                'edp_scores': clean_for_json(analysis.get('edp_scores', {})),
                'key_evidence': analysis.get('key_evidence', [])[:5],  # Limit to 5
                'contact_info': {
                    'first_name': str(company_data.get('first_name', '')),
                    'last_name': str(company_data.get('last_name', '')),
                    'email': str(company_data.get('email', '')),
                    'title': str(company_data.get('title', ''))
                }
            }
            
            # Ensure valid JSON
            json_payload = json.dumps(webhook_payload)
            
            async with self.session.post(
                self.clay_webhook_url,
                data=json_payload,  # Use data instead of json
                headers={'Content-Type': 'application/json'}
            ) as response:
                if response.status in [200, 201, 202]:
                    self.stats['sent_to_clay'] += 1
                    print(f"  ✅ Sent to Clay webhook")
                else:
                    error_text = await response.text()
                    logger.error(f"Clay webhook failed: {response.status} - {error_text}")
                    
        except Exception as e:
            logger.error(f"Clay send error: {e}")
    
    async def process_company(self, company_data: Dict):
        """Process single company with enhanced extraction"""
        
        company_name = company_data['company_name']
        print(f"\n🏢 Processing: {company_name}")
        
        # Step 1: Enhanced website analysis
        print(f"  🔍 Analyzing website with enhanced extraction...")
        
        if self.evidence_extractor:
            # Use synchronous method (not async)
            website_analysis = self.analyze_website_enhanced(company_data['domain'])
            # Process the enhanced evidence
            analysis = self.process_enhanced_evidence(website_analysis)
        else:
            # Use async basic method
            website_analysis = await self.analyze_website_basic(company_data['domain'])
            # Convert basic to standard format
            analysis = self.rule_based_analysis(website_analysis)
        
        # Step 2: GPT enhancement (optional)
        if OPENAI_API_KEY:
            print(f"  🤖 Enhancing with GPT analysis...")
            analysis = self.gpt_analysis_enhanced(company_data, analysis)
        
        # Display results
        print(f"  📊 Tier: {analysis['qualification_tier']}")
        print(f"  📈 PSI Score: {analysis.get('psi_score', 0):.1f}%")
        print(f"  🎯 Primary EDP: {analysis.get('primary_edp', 'unknown')}")
        
        if analysis.get('key_evidence'):
            print(f"  📝 Key Evidence:")
            for evidence in analysis['key_evidence'][:3]:
                print(f"     • {evidence}")
        
        self.stats['processed'] += 1
        
        # Step 3: Save and send if qualified
        if analysis['qualification_tier'] != "NOT_QUALIFIED":
            self.stats['qualified'] += 1
            
            # Save to Supabase
            await self.save_to_supabase_enhanced(company_data, analysis)
            
            # Send to Clay
            await self.send_to_clay_enhanced(company_data, analysis)
            
            return {
                'company': company_name,
                'analysis': analysis,
                'status': 'qualified'
            }
        
        return {
            'company': company_name,
            'analysis': analysis,
            'status': 'not_qualified'
        }
    
    def rule_based_analysis(self, website_analysis: Dict) -> Dict:
        """Fallback analysis for basic extraction"""
        
        evidence = website_analysis.get('evidence', [])
        evidence_str = ' '.join(evidence).lower()
        
        edp_scores = {}
        
        # Sales Enablement
        score = 0
        if "no product search" in evidence_str:
            score += 0.3
        if "pdf" in evidence_str and "catalog" in evidence_str:
            score += 0.3
        if "login" in evidence_str:
            score += 0.2
        if "quote" in evidence_str:
            score += 0.2
        edp_scores['sales_enablement_collapse'] = min(score, 1.0)
        
        # Technology
        score = 0
        if "no ssl" in evidence_str:
            score += 0.4
        if "wordpress" in ' '.join(website_analysis.get('tech_stack', [])).lower():
            score += 0.3
        edp_scores['technology_obsolescence'] = min(score, 1.0)
        
        # Other EDPs (basic scores)
        edp_scores['rep_performance_crisis'] = 0.5 if "dealer" in evidence_str or "rep" in evidence_str else 0.3
        edp_scores['sku_complexity'] = 0.4
        edp_scores['channel_conflict'] = 0.3
        
        # Calculate PSI
        psi_score = sum(score * self.edp_weights[edp] for edp, score in edp_scores.items()) / sum(self.edp_weights.values())
        psi_percentage = psi_score * 100
        
        # Determine tier
        if psi_percentage >= 50:
            tier = "TIER_1_IMMEDIATE"
        elif psi_percentage >= 35:
            tier = "TIER_2_ACTIVE"
        elif psi_percentage >= 25:
            tier = "TIER_3_NURTURE"
        else:
            tier = "NOT_QUALIFIED"
        
        # Primary EDP
        primary_edp = max(edp_scores.items(), key=lambda x: x[1] * self.edp_weights[x[0]])[0]
        
        return {
            'edp_scores': edp_scores,
            'primary_edp': primary_edp,
            'psi_score': psi_percentage,
            'qualification_tier': tier,
            'key_evidence': evidence[:3]
        }
    
    async def process_csv(self, csv_path: str):
        """Process CSV file with enhanced extraction"""
        
        print(f"\n{'='*60}")
        print(f"SUPERCAT ENHANCED PIPELINE")
        print(f"{'='*60}\n")
        
        # Read CSV
        df = pd.read_csv(csv_path)
        df = df.dropna(subset=['company_name', 'domain'])
        
        print(f"📊 Processing {len(df)} companies")
        print(f"🔧 Using: {'Enhanced WebsiteEvidenceExtractor' if self.evidence_extractor else 'Basic extraction'}\n")
        
        # Process each company
        results = []
        async with self:
            for idx, row in df.iterrows():
                company_data = row.to_dict()
                result = await self.process_company(company_data)
                results.append(result)
                
                # Rate limiting
                await asyncio.sleep(2 if self.evidence_extractor else 1)
        
        # Summary
        print(f"\n{'='*60}")
        print(f"PROCESSING COMPLETE")
        print(f"{'='*60}")
        print(f"📊 Total Processed: {self.stats['processed']}")
        print(f"✅ Qualified: {self.stats['qualified']} ({self.stats['qualified']/max(self.stats['processed'],1)*100:.1f}%)")
        print(f"🚀 Sent to Clay: {self.stats['sent_to_clay']}")
        print(f"💾 Saved to Supabase: {self.stats['saved_to_supabase']}")
        
        if self.stats['errors']:
            print(f"⚠️ Errors: {len(self.stats['errors'])}")
        
        # Save results
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        results_file = f"results_enhanced_{timestamp}.json"
        
        with open(results_file, 'w') as f:
            json.dump({
                'stats': self.stats,
                'results': results,
                'timestamp': timestamp,
                'using_enhanced': bool(self.evidence_extractor)
            }, f, indent=2)
        
        print(f"\n📁 Results saved: {results_file}")
        
        # Save qualified companies to CSV
        qualified = [r for r in results if r['status'] == 'qualified']
        if qualified:
            qualified_df = pd.DataFrame([{
                'company': r['company'],
                'tier': r['analysis']['qualification_tier'],
                'psi_score': r['analysis'].get('psi_score', 0),
                'primary_edp': r['analysis'].get('primary_edp', ''),
                'evidence': ', '.join(r['analysis'].get('key_evidence', [])[:2])
            } for r in qualified])
            
            qualified_file = f"qualified_{timestamp}.csv"
            qualified_df.to_csv(qualified_file, index=False)
            print(f"📁 Qualified companies: {qualified_file}")
        
        return results


async def main():
    """Main execution"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python integrated_pipeline.py prospects.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    if not Path(csv_file).exists():
        print(f"❌ File not found: {csv_file}")
        sys.exit(1)
    
    processor = IntegratedPipelineProcessor()
    await processor.process_csv(csv_file)


if __name__ == "__main__":
    asyncio.run(main())
```

### supercat_automation/full_orchestrator.py
```python
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

```

### supercat_automation/fix_imports.py
```python
# Fix the imports in website_evidence.py

with open('scrapers/website_evidence.py', 'r') as f:
    lines = f.readlines()

# Find and fix the typing import line
for i, line in enumerate(lines):
    if 'from typing import' in line and 'Optional' not in line:
        # Add Optional to the imports
        if line.strip().endswith('Any'):
            lines[i] = line.rstrip() + ', Optional\n'
        else:
            lines[i] = line.replace('\n', ', Optional\n')
        print(f"✅ Added Optional to imports on line {i+1}")
        break

# Write back
with open('scrapers/website_evidence.py', 'w') as f:
    f.writelines(lines)

print("✅ Fixed imports!")

```

### supercat_automation/health_monitor.py
```python
# health_monitor.py
'''System health monitoring for SuperCat GTM'''

import psutil
import os
from datetime import datetime, timedelta
from database.connection import db
import logging

logger = logging.getLogger(__name__)

class HealthMonitor:
    '''Monitor system health and performance'''
    
    def __init__(self):
        self.checks = {
            'database': False,
            'disk_space': False,
            'memory': False,
            'recent_activity': False,
            'error_rate': False
        }
    
    def check_database(self):
        '''Check database connectivity'''
        try:
            result = db.client.table('companies').select('count').execute()
            self.checks['database'] = True
            return True, "Database connected"
        except Exception as e:
            self.checks['database'] = False
            return False, f"Database error: {e}"
    
    def check_disk_space(self):
        '''Check available disk space'''
        disk = psutil.disk_usage('/')
        free_gb = disk.free / (1024**3)
        
        if free_gb > 1:
            self.checks['disk_space'] = True
            return True, f"Disk space OK ({free_gb:.1f} GB free)"
        else:
            self.checks['disk_space'] = False
            return False, f"Low disk space ({free_gb:.1f} GB free)"
    
    def check_memory(self):
        '''Check memory usage'''
        memory = psutil.virtual_memory()
        
        if memory.percent < 90:
            self.checks['memory'] = True
            return True, f"Memory OK ({memory.percent:.1f}% used)"
        else:
            self.checks['memory'] = False
            return False, f"High memory usage ({memory.percent:.1f}%)"
    
    def check_recent_activity(self):
        '''Check for recent system activity'''
        try:
            # Check for companies analyzed in last 24 hours
            cutoff = (datetime.now() - timedelta(hours=24)).isoformat()
            
            result = db.client.table('companies').select('count').gte(
                'last_website_scan', cutoff
            ).execute()
            
            if result.data:
                self.checks['recent_activity'] = True
                return True, "Recent activity detected"
            else:
                self.checks['recent_activity'] = False
                return False, "No activity in last 24 hours"
        except:
            self.checks['recent_activity'] = False
            return False, "Could not check activity"
    
    def check_error_logs(self):
        '''Check error rate in logs'''
        try:
            log_file = 'logs/daily_automation.log'
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    lines = f.readlines()[-100:]  # Last 100 lines
                
                errors = sum(1 for line in lines if 'ERROR' in line)
                
                if errors < 10:
                    self.checks['error_rate'] = True
                    return True, f"Error rate OK ({errors} errors in last 100 lines)"
                else:
                    self.checks['error_rate'] = False
                    return False, f"High error rate ({errors} errors)"
            else:
                self.checks['error_rate'] = True
                return True, "No error log found"
        except:
            self.checks['error_rate'] = False
            return False, "Could not check error logs"
    
    def run_all_checks(self):
        '''Run all health checks'''
        
        print("\n" + "=" * 60)
        print("🏥 SYSTEM HEALTH CHECK")
        print(f"Time: {datetime.now()}")
        print("=" * 60)
        
        # Run each check
        checks_to_run = [
            ('Database', self.check_database),
            ('Disk Space', self.check_disk_space),
            ('Memory', self.check_memory),
            ('Recent Activity', self.check_recent_activity),
            ('Error Rate', self.check_error_logs)
        ]
        
        all_healthy = True
        
        for name, check_func in checks_to_run:
            success, message = check_func()
            
            if success:
                print(f"✅ {name}: {message}")
            else:
                print(f"❌ {name}: {message}")
                all_healthy = False
        
        print("=" * 60)
        
        if all_healthy:
            print("✅ SYSTEM HEALTHY")
        else:
            print("⚠️  ISSUES DETECTED - Review above")
        
        print("=" * 60)
        
        return all_healthy

if __name__ == "__main__":
    monitor = HealthMonitor()
    monitor.run_all_checks()

```

### supercat_automation/mvp_pipeline.py
```python
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

```

### supercat_automation/menu.py
```python
#!/usr/bin/env python3
import os
import sys

def main():
    print("\n🚀 SuperCat GTM Automation")
    print("=" * 40)
    print("1. Run simple test")
    print("2. Test pain detection")
    print("3. Process CSV prospects")
    print("4. Check database connection")
    print("5. Exit")
    print("=" * 40)
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        os.system("python simple_test.py")
    elif choice == "2":
        os.system("python test_pain_detection.py")
    elif choice == "3":
        csv_file = input("Enter CSV filename: ")
        os.system(f"python upload_prospects.py {csv_file}")
    elif choice == "4":
        os.system('python -c "from database.connection import db; print(\"✅ Database connected!\")"')
    elif choice == "5":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

```

### supercat_automation/add_personalization_method.py
```python
# Add the missing method to website_evidence.py

method_to_add = '''
    def _extract_personalization_data(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract specific data points for message personalization"""
        hooks = []
        
        try:
            # Extract company name from title
            title = soup.find('title')
            if title:
                hooks.append({
                    'type': 'company_name',
                    'value': title.text.split('|')[0].strip()
                })
            
            # Look for trade shows mentioned
            text_content = soup.get_text().lower()
            trade_shows = ['vegas market', 'high point market', 'neocon', 'lightovation']
            for show in trade_shows:
                if show.lower() in text_content:
                    hooks.append({
                        'type': 'trade_show',
                        'value': show
                    })
            
            # Extract product categories from navigation
            nav = soup.find('nav') or soup.find('div', class_='navigation')
            if nav:
                categories = [a.text.strip() for a in nav.find_all('a')[:5]]
                if categories:
                    hooks.append({
                        'type': 'product_categories',
                        'value': categories
                    })
                    
        except Exception as e:
            logger.error(f"Error extracting personalization: {e}")
        
        return hooks
'''

with open('scrapers/website_evidence.py', 'r') as f:
    content = f.read()

# Check if method exists
if '_extract_personalization_data' not in content:
    # Find where to insert (before _identify_tam_tier_indicators)
    insert_pos = content.find('def _identify_tam_tier_indicators')
    if insert_pos > 0:
        # Insert the method
        content = content[:insert_pos] + method_to_add + '\n' + content[insert_pos:]
        
        with open('scrapers/website_evidence.py', 'w') as f:
            f.write(content)
        print("✅ Added _extract_personalization_data method")
else:
    print("✅ Method already exists")

```

### supercat_automation/check_status.py
```python
import sys
print("🔍 Checking SuperCat GTM System Status...\n")

# Check imports
modules = {
    "Database": "database.connection",
    "Pain Detector": "analysis.pain_detector", 
    "Message Generator": "generation.evidence_based_messages",
    "Website Analyzer": "scrapers.website_evidence"
}

for name, module in modules.items():
    try:
        __import__(module)
        print(f"✅ {name}: OK")
    except SyntaxError as e:
        print(f"❌ {name}: Syntax error - {e}")
    except Exception as e:
        print(f"❌ {name}: {e}")

# Check settings
try:
    from config.settings import settings
    print(f"\n📋 Configuration:")
    print(f"  Environment: {settings.environment}")
    print(f"  Debug Mode: {settings.debug_mode}")
    
    # Check which services are configured
    services = {
        "Supabase": 'placeholder' not in settings.supabase_url,
        "OpenAI": 'placeholder' not in settings.openai_api_key,
        "Clay": 'placeholder' not in settings.clay_webhook_url
    }
    
    for service, configured in services.items():
        status = "✅ Configured" if configured else "⚠️  Using placeholder"
        print(f"  {service}: {status}")
        
except Exception as e:
    print(f"❌ Settings error: {e}")

print("\n🎯 Ready to:")
print("  1. Analyze companies for pain signals")
print("  2. Generate personalized campaigns")
print("  3. Process prospect lists")
print("\nRun: python run_pipeline.py to see it in action!")

```

### supercat_automation/generate_webhooks.py
```python
#!/usr/bin/env python3
"""
SuperCat Webhook Processor - Generates Clay-ready webhooks
Processes CSV and outputs campaign-ready JSON webhooks
"""

import pandas as pd
import requests
import json
from typing import Dict, List, Any
from datetime import datetime, timedelta
import argparse
from pathlib import Path
import time
import re
import uuid
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SuperCatWebhookProcessor:
    """Generates Clay-ready webhook payloads with full campaigns"""
    
    def __init__(self):
        # EDP definitions from won-deal analysis
        self.edp_weights = {
            'sales_enablement_collapse': 1.0,
            'technology_obsolescence': 0.93,
            'rep_performance_crisis': 0.71,
            'sku_complexity': 0.64,
            'channel_conflict': 0.43
        }
        
        # Trade show dates
        self.trade_shows = {
            'Vegas Market': datetime(2024, 1, 28),
            'High Point Market': datetime(2024, 4, 20)
        }
        
        # Customer testimonials from won deals
        self.testimonials = {
            'Butler Specialty': "eCat flexibly configures to the way we do business",
            'Godinger Silver': "Best thing in 25 years, reps are in love",
            'Wildwood Lamps': "Reduced calls by a third"
        }
    
    def analyze_website(self, domain: str) -> Dict[str, Any]:
        """Analyze website for pain signals"""
        if not domain.startswith('http'):
            domain = f"https://{domain}"
        
        edp_scores = {}
        evidence = []
        
        try:
            response = requests.get(domain, timeout=10, verify=False)
            html_content = response.text.lower()
            
            # Sales Enablement Collapse
            sales_score = 0
            if 'product search' not in html_content:
                sales_score += 0.3
                evidence.append("No product search")
            if '.pdf' in html_content and 'catalog' in html_content:
                sales_score += 0.3
                evidence.append("PDF-only catalogs")
            if 'dealer login' in html_content:
                sales_score += 0.2
                evidence.append("Manual dealer login")
            if 'request quote' in html_content:
                sales_score += 0.2
                evidence.append("Manual quote requests")
            edp_scores['sales_enablement_collapse'] = min(sales_score, 1.0)
            
            # Technology Obsolescence
            tech_score = 0
            copyright_match = re.search(r'©\s*(\d{4})', html_content)
            if copyright_match and int(copyright_match.group(1)) < 2022:
                tech_score += 0.4
                evidence.append(f"Outdated copyright")
            if not response.url.startswith('https'):
                tech_score += 0.3
                evidence.append("No SSL")
            if 'csv' in html_content and 'upload' in html_content:
                tech_score += 0.3
                evidence.append("CSV-based processes")
            edp_scores['technology_obsolescence'] = min(tech_score, 1.0)
            
            # Rep Performance Crisis
            rep_score = 0
            if 'find a rep' not in html_content:
                rep_score += 0.3
                evidence.append("No rep locator")
            if 'sales resources' not in html_content:
                rep_score += 0.4
                evidence.append("No sales resources")
            if 'territory' not in html_content:
                rep_score += 0.3
                evidence.append("No territory info")
            edp_scores['rep_performance_crisis'] = min(rep_score, 1.0)
            
            # SKU Complexity
            sku_score = 0
            if 'configure' in html_content or 'customize' in html_content:
                sku_score += 0.3
                evidence.append("Configuration complexity")
            if 'options' in html_content and 'finishes' in html_content:
                sku_score += 0.3
                evidence.append("Multiple options/finishes")
            if re.search(r'\d{3,}\s*products', html_content):
                sku_score += 0.4
                evidence.append("Large catalog")
            edp_scores['sku_complexity'] = min(sku_score, 1.0)
            
            # Channel Conflict
            channel_score = 0
            if html_content.count('login') > 2:
                channel_score += 0.4
                evidence.append("Multiple logins")
            if 'dealer price' in html_content:
                channel_score += 0.3
                evidence.append("Multiple pricing tiers")
            if 'where to buy' in html_content:
                channel_score += 0.3
                evidence.append("Mixed channels")
            edp_scores['channel_conflict'] = min(channel_score, 1.0)
            
        except Exception as e:
            edp_scores = {edp: 0.5 for edp in self.edp_weights.keys()}
            evidence.append(f"Analysis error: {str(e)}")
        
        # Calculate PSI score
        psi_score = sum(score * self.edp_weights[edp] for edp, score in edp_scores.items()) / sum(self.edp_weights.values())
        
        # Determine tier (adjusted thresholds for better distribution)
        if psi_score >= 0.5:  # Was 0.7
            tier = "TIER_1_IMMEDIATE"
            urgency = "high"
        elif psi_score >= 0.35:  # Was 0.5
            tier = "TIER_2_ACTIVE"
            urgency = "medium"
        elif psi_score >= 0.25:  # Was 0.3
            tier = "TIER_3_NURTURE"
            urgency = "low"
        else:
            tier = "NOT_QUALIFIED"
            urgency = "none"
        
        # Find primary EDP
        primary_edp = max(edp_scores.items(), key=lambda x: x[1] * self.edp_weights[x[0]])[0]
        
        return {
            'edp_scores': edp_scores,
            'psi_score': psi_score * 100,  # Convert to percentage
            'tier': tier,
            'urgency': urgency,
            'primary_edp': primary_edp,
            'evidence': evidence
        }
    
    def generate_email_sequence(self, company_name: str, primary_edp: str, urgency: str) -> List[Dict]:
        """Generate 7-email sequence based on primary EDP"""
        
        # Calculate days until next trade show
        today = datetime.now()
        days_until_vegas = (self.trade_shows['Vegas Market'] - today).days
        days_until_high_point = (self.trade_shows['High Point Market'] - today).days
        days_until_show = min(days_until_vegas, days_until_high_point) if days_until_vegas > 0 else days_until_high_point
        
        sequences = {
            'sales_enablement_collapse': [
                {
                    "day": 0,
                    "subject": f"{company_name} - Still using paper at trade shows?",
                    "body": f"Hi {{{{first_name}}}},\n\nI noticed {company_name} has a major presence at High Point Market. With the show in {days_until_show} days, how are your reps planning to handle orders when they can't access your systems?\n\nLast year, several exhibitors lost over $50K each during WiFi outages.\n\nHow do you currently handle order processing at trade shows?\n\nBest,\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "How Butler Specialty solved this",
                    "body": f"{{{{first_name}}}},\n\nQuick follow-up - Butler Specialty had the same challenge at High Point. Their President told me: '{self.testimonials['Butler Specialty']}'\n\nThey now process orders completely offline. Zero downtime.\n\nWorth a quick call?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 7,
                    "subject": "30% order error rate industry average",
                    "body": f"{{{{first_name}}}},\n\nDid you know the furniture industry averages a 30% order error rate with manual processes?\n\nAt your scale, that could mean $400K+ in lost margin annually.\n\nHere's a 2-minute video showing how eCat eliminates these errors: [link]\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 10,
                    "subject": f"ROI calculator for {company_name}",
                    "body": f"{{{{first_name}}}},\n\nI ran some numbers for {company_name}:\n\n- Time saved: 3 hours/day per rep\n- Error reduction: 25%\n- Trade show revenue protection: $150K+\n\nTotal first-year ROI: 412%\n\nWant to see the full breakdown?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 14,
                    "subject": "Godinger Silver case study",
                    "body": f"{{{{first_name}}}},\n\nJoel Stern, VP IT at Godinger Silver, called eCat '{self.testimonials['Godinger Silver']}'\n\nThey saw:\n- 67% reduction in order processing time\n- Zero trade show downtime\n- 40% increase in rep productivity\n\nHere's their full story: [link]\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 18,
                    "subject": f"Last chance before {days_until_show} days to show",
                    "body": f"{{{{first_name}}}},\n\nWith High Point Market approaching fast, you're running out of time to get a solution in place.\n\nImplementation takes just 2 weeks. Your reps could be fully trained before the show.\n\nCan we schedule 15 minutes this week?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 21,
                    "subject": "Should I close your file?",
                    "body": f"{{{{first_name}}}},\n\nI've reached out several times about solving {company_name}'s order processing challenges.\n\nIf this isn't a priority, I'll close your file and stop following up.\n\nBut if you're still losing money on manual processes, just reply 'interested' and I'll send over some times to connect.\n\n{{{{sender_name}}}}"
                }
            ],
            'technology_obsolescence': [
                {
                    "day": 0,
                    "subject": f"{company_name}'s systems are 40% slower than competitors",
                    "body": f"Hi {{{{first_name}}}},\n\nI noticed {company_name} is still using legacy systems for catalog management. Industry data shows this makes you 40-50% slower to quote than digital-native competitors.\n\nHow much business are you losing to faster competitors?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "Your competitors are 2 days faster",
                    "body": f"{{{{first_name}}}},\n\nWhile {company_name} takes 3-5 days to update pricing, your competitors push changes in hours.\n\neCat syncs with your existing ERP without replacement. No IT nightmare.\n\nInterested in learning more?\n\n{{{{sender_name}}}}"
                }
            ],
            'rep_performance_crisis': [
                {
                    "day": 0,
                    "subject": f"Why {company_name}'s top reps are 10x more productive",
                    "body": f"Hi {{{{first_name}}}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "27% rep turnover is killing your growth",
                    "body": f"{{{{first_name}}}},\n\nThe industry average 27% rep turnover costs {company_name} approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{{{sender_name}}}}"
                }
            ]
        }
        
        # Return the appropriate sequence or default to sales enablement
        base_sequence = sequences.get(primary_edp, sequences['sales_enablement_collapse'])
        
        # For tier 1, use all 7 emails. For tier 2, use first 5. For tier 3, use first 3.
        if urgency == "high":
            return base_sequence[:7]
        elif urgency == "medium":
            return base_sequence[:5]
        else:
            return base_sequence[:3]
    
    def generate_linkedin_sequence(self, company_name: str, primary_edp: str) -> List[Dict]:
        """Generate LinkedIn outreach sequence"""
        
        messages = {
            'sales_enablement_collapse': "noticed {}'s presence at High Point Market. Managing orders without reliable WiFi must be challenging. Would love to share how similar companies handle this.",
            'technology_obsolescence': "saw {} is modernizing operations. We help furniture brands bridge legacy systems to modern commerce without replacing ERPs.",
            'rep_performance_crisis': "noticed {} works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
        }
        
        message = messages.get(primary_edp, messages['sales_enablement_collapse']).format(company_name)
        
        return [
            {
                "type": "connection_request",
                "message": f"Hi {{{{first_name}}}}, {message}"
            },
            {
                "type": "follow_up_message",
                "day": 7,
                "message": f"{{{{first_name}}}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
            }
        ]
    
    def generate_webhook(self, company_data: Dict, analysis: Dict) -> Dict:
        """Generate complete webhook payload for Clay"""
        
        # Determine persona based on primary EDP
        persona_map = {
            'sales_enablement_collapse': 'sales_leadership',
            'technology_obsolescence': 'it_leadership',
            'rep_performance_crisis': 'sales_leadership',
            'sku_complexity': 'operations',
            'channel_conflict': 'c_suite'
        }
        
        primary_persona = persona_map.get(analysis['primary_edp'], 'sales_leadership')
        
        # Calculate days until next show
        today = datetime.now()
        days_until_vegas = (self.trade_shows['Vegas Market'] - today).days
        days_until_high_point = (self.trade_shows['High Point Market'] - today).days
        days_until_show = min(days_until_vegas, days_until_high_point) if days_until_vegas > 0 else days_until_high_point
        
        # Determine campaign strategy
        if analysis['urgency'] == 'high' and days_until_show < 60:
            strategy = "aggressive_trade_show"
        elif analysis['urgency'] == 'high':
            strategy = "aggressive_problem"
        elif analysis['urgency'] == 'medium':
            strategy = "educational"
        else:
            strategy = "nurture"
        
        webhook = {
            "company_id": str(uuid.uuid4()),
            "company_name": company_data['company_name'],
            "domain": company_data['domain'].replace('https://', '').replace('http://', ''),
            "tam_tier": analysis['tier'],
            "psi_score": round(analysis['psi_score'], 1),
            "primary_edp": analysis['primary_edp'],
            "edp_scores": analysis['edp_scores'],
            "evidence": analysis['evidence'][:5],  # Top 5 evidence points
            "persona_type": primary_persona,
            "backup_persona": "c_suite" if primary_persona != "c_suite" else "sales_leadership",
            "persona_reason": f"Primary EDP is {analysis['primary_edp']}",
            "urgency_level": analysis['urgency'],
            "campaign_strategy": strategy,
            "days_until_show": days_until_show,
            "email_sequence": self.generate_email_sequence(
                company_data['company_name'],
                analysis['primary_edp'],
                analysis['urgency']
            ),
            "linkedin_sequence": self.generate_linkedin_sequence(
                company_data['company_name'],
                analysis['primary_edp']
            ),
            "contact_info": {
                "first_name": company_data.get('first_name', ''),
                "last_name": company_data.get('last_name', ''),
                "email": company_data.get('email', ''),
                "title": company_data.get('title', ''),
                "linkedin": company_data.get('LinkedIn Profile', '')
            },
            "company_info": {
                "industry": company_data.get('industry', ''),
                "employee_count": company_data.get('employee_count', '')
            },
            "created_at": datetime.now().isoformat(),
            "webhook_version": "2.0"
        }
        
        return webhook

def process_csv_to_webhooks(file_path: str, limit: int = None, output_dir: str = "webhooks"):
    """Process CSV and generate webhook files"""
    
    print(f"\n{'='*60}")
    print(f"SUPERCAT WEBHOOK PROCESSOR")
    print(f"{'='*60}\n")
    
    # Read CSV
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Error reading CSV: {str(e)}")
        return
    
    # Clean data
    df = df.dropna(subset=['company_name', 'domain'])
    
    if limit:
        df = df.head(limit)
    
    print(f"📊 Processing {len(df)} companies...")
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Initialize processor
    processor = SuperCatWebhookProcessor()
    
    # Process each company
    webhooks = []
    tier_counts = {'TIER_1_IMMEDIATE': 0, 'TIER_2_ACTIVE': 0, 'TIER_3_NURTURE': 0, 'NOT_QUALIFIED': 0}
    errors = []
    
    for idx, row in df.iterrows():
        company_data = row.to_dict()
        
        print(f"\nAnalyzing {company_data['company_name']}...")
        
        try:
            # Analyze website
            analysis = processor.analyze_website(company_data['domain'])
            
            # Skip if not qualified
            if analysis['tier'] == "NOT_QUALIFIED":
                print(f"  ❌ Not qualified (PSI: {analysis['psi_score']:.1f})")
                tier_counts['NOT_QUALIFIED'] += 1
                continue
            
            # Generate webhook
            webhook = processor.generate_webhook(company_data, analysis)
            webhooks.append(webhook)
            tier_counts[analysis['tier']] += 1
            
            # Sanitize company name for filename (remove special characters)
            safe_company_name = re.sub(r'[^\w\s-]', '', company_data['company_name'])
            safe_company_name = re.sub(r'[-\s]+', '_', safe_company_name)
            
            # Save individual webhook file
            webhook_file = Path(output_dir) / f"{webhook['company_id']}_{safe_company_name}.json"
            with open(webhook_file, 'w') as f:
                json.dump(webhook, f, indent=2)
            
            # Print status
            if analysis['tier'] == 'TIER_1_IMMEDIATE':
                print(f"  🔥 TIER 1 - PSI: {analysis['psi_score']:.1f}% - {analysis['primary_edp']}")
                print(f"     → Webhook saved: {webhook_file.name}")
            elif analysis['tier'] == 'TIER_2_ACTIVE':
                print(f"  ✅ TIER 2 - PSI: {analysis['psi_score']:.1f}% - {analysis['primary_edp']}")
            else:
                print(f"  📊 TIER 3 - PSI: {analysis['psi_score']:.1f}% - {analysis['primary_edp']}")
            
        except Exception as e:
            error_msg = f"Error processing {company_data['company_name']}: {str(e)}"
            print(f"  ⚠️ {error_msg}")
            errors.append(error_msg)
            continue
        
        time.sleep(0.5)  # Rate limiting
    
    # Save batch webhook file
    if webhooks:
        batch_file = Path(output_dir) / f"batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(batch_file, 'w') as f:
            json.dump(webhooks, f, indent=2)
        
        print(f"\n📦 Batch webhook file: {batch_file}")
    
    # Save CSV summary
    summary_df = pd.DataFrame([{
        'company_name': w['company_name'],
        'domain': w['domain'],
        'tier': w['tam_tier'],
        'psi_score': w['psi_score'],
        'primary_edp': w['primary_edp'],
        'urgency': w['urgency_level'],
        'email': w['contact_info']['email'],
        'campaign_strategy': w['campaign_strategy']
    } for w in webhooks])
    
    summary_file = Path(output_dir) / f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    summary_df.to_csv(summary_file, index=False)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"🔥 Tier 1 (Immediate): {tier_counts['TIER_1_IMMEDIATE']}")
    print(f"✅ Tier 2 (Active): {tier_counts['TIER_2_ACTIVE']}")
    print(f"📊 Tier 3 (Nurture): {tier_counts['TIER_3_NURTURE']}")
    print(f"❌ Not Qualified: {tier_counts['NOT_QUALIFIED']}")
    print(f"\n📁 Output directory: {output_dir}/")
    print(f"📊 Summary CSV: {summary_file.name}")
    print(f"🔗 Total webhooks generated: {len(webhooks)}")
    
    if errors:
        print(f"\n⚠️ Errors encountered: {len(errors)}")
        for error in errors[:5]:  # Show first 5 errors
            print(f"  - {error}")
    
    # Show top Tier 1 companies
    if tier_counts['TIER_1_IMMEDIATE'] > 0:
        print(f"\n🎯 TOP TIER 1 TARGETS:")
        print(f"{'='*60}")
        tier1_webhooks = [w for w in webhooks if w['tam_tier'] == 'TIER_1_IMMEDIATE']
        tier1_webhooks.sort(key=lambda x: x['psi_score'], reverse=True)
        
        for w in tier1_webhooks[:5]:
            print(f"• {w['company_name']} (PSI: {w['psi_score']:.1f}%)")
            print(f"  Primary Pain: {w['primary_edp'].replace('_', ' ').title()}")
            print(f"  Strategy: {w['campaign_strategy']}")
            if w['contact_info']['email']:
                print(f"  Contact: {w['contact_info']['email']}")
            print()
    
    return webhooks

def main():
    parser = argparse.ArgumentParser(description='Generate SuperCat webhook campaigns')
    parser.add_argument('csv_file', help='Path to prospects CSV')
    parser.add_argument('--test', type=int, help='Test with N companies')
    parser.add_argument('--output', default='webhooks', help='Output directory')
    
    args = parser.parse_args()
    
    if not Path(args.csv_file).exists():
        print(f"❌ File not found: {args.csv_file}")
        return
    
    process_csv_to_webhooks(
        file_path=args.csv_file,
        limit=args.test,
        output_dir=args.output
    )

if __name__ == "__main__":
    main()
```

### supercat_automation/run_pipeline.py
```python
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
```

### supercat_automation/automated_daily.py
```python
# automated_daily.py
'''Automated daily runner for SuperCat GTM'''

import schedule
import time
import logging
from datetime import datetime
import asyncio
from full_orchestrator import SupercatFullOrchestrator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/daily_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DailyAutomation:
    '''Runs SuperCat automation on schedule'''
    
    def __init__(self):
        self.orchestrator = SupercatFullOrchestrator()
        self.run_count = 0
    
    def morning_run(self):
        '''Morning pipeline run - full analysis'''
        logger.info("=" * 60)
        logger.info("🌅 MORNING RUN STARTING")
        logger.info(f"Run #{self.run_count + 1} at {datetime.now()}")
        
        try:
            asyncio.run(self.orchestrator.run_complete_pipeline(mode='full'))
            self.run_count += 1
            logger.info("✅ Morning run completed successfully")
        except Exception as e:
            logger.error(f"❌ Morning run failed: {e}")
    
    def afternoon_run(self):
        '''Afternoon run - campaigns only'''
        logger.info("=" * 60)
        logger.info("🌆 AFTERNOON RUN STARTING")
        
        try:
            asyncio.run(self.orchestrator.run_complete_pipeline(mode='campaign_only'))
            logger.info("✅ Afternoon run completed successfully")
        except Exception as e:
            logger.error(f"❌ Afternoon run failed: {e}")
    
    def health_check(self):
        '''Hourly health check'''
        logger.info(f"💓 Health check - System running - Runs completed: {self.run_count}")
    
    def start(self):
        '''Start the scheduler'''
        
        # Schedule runs
        schedule.every().day.at("09:00").do(self.morning_run)
        schedule.every().day.at("14:00").do(self.afternoon_run)
        schedule.every().hour.do(self.health_check)
        
        # Run immediately on start
        logger.info("🚀 Daily Automation Started")
        logger.info("Scheduled:")
        logger.info("  - Morning run: 9:00 AM")
        logger.info("  - Afternoon run: 2:00 PM")
        logger.info("  - Health checks: Every hour")
        
        # Run once immediately
        self.morning_run()
        
        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    automation = DailyAutomation()
    automation.start()

```

### supercat_automation/simple_test.py
```python

# Simple test runner for SuperCat GTM
import asyncio
from datetime import datetime
from analysis.pain_detector import MultiSourcePainDetector
from generation.evidence_based_messages import EvidenceBasedMessageGenerator
from database.connection import db
import uuid

async def test_pipeline():
    print("=" * 70)
    print("SUPERCAT GTM - SIMPLE TEST")
    print(f"Started: {datetime.now()}")
    print("=" * 70)
    
    # Initialize components
    pain_detector = MultiSourcePainDetector()
    message_generator = EvidenceBasedMessageGenerator()
    
    # Test companies
    test_companies = [
        {
            'id': str(uuid.uuid4()),
            'company_name': 'Ashley Furniture',
            'domain': 'ashleyfurniture.com',
            'trade_shows': ['Vegas Market']
        },
        {
            'id': str(uuid.uuid4()),
            'company_name': 'Hooker Furniture',
            'domain': 'hookerfurniture.com',
            'trade_shows': ['High Point Market']
        }
    ]
    
    # Analyze each company
    for company in test_companies:
        print(f"\nAnalyzing {company['company_name']}...")
        
        try:
            # Analyze for pain
            analysis = pain_detector.analyze_company(company)
            
            print(f"  TAM Tier: {analysis['tam_tier']}")
            print(f"  Pain Score: {analysis['total_pain_score']:.2f}")
            print(f"  Primary EDP: {analysis['primary_edp']}")
            
            # Generate campaign if qualified
            if analysis['tam_tier'] in ['TIER_1_IMMEDIATE', 'TIER_2_QUARTERLY']:
                print(f"  ✓ Qualified! Generating campaign...")
                campaign = message_generator.generate_campaign(analysis)
                print(f"  Campaign Strategy: {campaign['campaign_strategy']}")
                print(f"  Emails Generated: {len(campaign['email_sequence'])}")
        
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    print("\n" + "=" * 70)
    print("TEST COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(test_pipeline())

```

### supercat_automation/fix_type_hints.py
```python
import re

# Read the file
with open('scrapers/website_evidence.py', 'r') as f:
    content = f.read()

# Fix the type hints - replace | None with Optional
content = content.replace('-> str | None:', '-> Optional[str]:')

# Make sure Optional is imported
if 'from typing import' in content and 'Optional' not in content:
    # Add Optional to the imports
    content = content.replace(
        'from typing import Dict, List, Any',
        'from typing import Dict, List, Any, Optional'
    )

# Write back
with open('scrapers/website_evidence.py', 'w') as f:
    f.write(content)

print("✅ Fixed type hints for Python 3.9 compatibility")

```

### supercat_automation/main.py
```python
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
```

### supercat_automation/performance_dashboard.py
```python
# performance_dashboard.py
'''Performance monitoring dashboard'''

import pandas as pd
from datetime import datetime, timedelta
from database.connection import db

class PerformanceDashboard:
    '''Monitor GTM performance metrics'''
    
    def __init__(self):
        self.metrics = {}
    
    def get_daily_metrics(self):
        '''Get today's performance metrics'''
        
        # Get companies analyzed today
        today = datetime.now().date()
        
        companies = db.client.table('companies').select('*').gte(
            'created_at', today.isoformat()
        ).execute()
        
        campaigns = db.client.table('campaigns').select('*').gte(
            'created_at', today.isoformat()
        ).execute()
        
        self.metrics = {
            'date': today.isoformat(),
            'companies_analyzed': len(companies.data) if companies.data else 0,
            'campaigns_created': len(campaigns.data) if campaigns.data else 0,
            'tier_distribution': self._get_tier_distribution(companies.data),
            'edp_distribution': self._get_edp_distribution(companies.data)
        }
        
        return self.metrics
    
    def _get_tier_distribution(self, companies):
        '''Get distribution by TAM tier'''
        tiers = {}
        for company in companies or []:
            tier = company.get('tam_tier', 'UNKNOWN')
            tiers[tier] = tiers.get(tier, 0) + 1
        return tiers
    
    def _get_edp_distribution(self, companies):
        '''Get distribution by EDP'''
        edps = {}
        for company in companies or []:
            for edp in company.get('edp_tags', []):
                edps[edp] = edps.get(edp, 0) + 1
        return edps
    
    def print_dashboard(self):
        '''Print dashboard to console'''
        
        metrics = self.get_daily_metrics()
        
        print("\n" + "=" * 60)
        print("📊 SUPERCAT GTM PERFORMANCE DASHBOARD")
        print(f"Date: {metrics['date']}")
        print("=" * 60)
        
        print(f"\n📈 TODAY'S METRICS")
        print(f"  Companies Analyzed: {metrics['companies_analyzed']}")
        print(f"  Campaigns Created: {metrics['campaigns_created']}")
        
        print(f"\n🎯 TAM TIER DISTRIBUTION")
        for tier, count in metrics['tier_distribution'].items():
            print(f"  {tier}: {count}")
        
        print(f"\n💔 EDP DISTRIBUTION")
        for edp, count in metrics['edp_distribution'].items():
            print(f"  {edp}: {count}")
        
        print("\n" + "=" * 60)

if __name__ == "__main__":
    dashboard = PerformanceDashboard()
    dashboard.print_dashboard()

```

### supercat_automation/reporting.py
```python
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

```

### supercat_automation/master_control.py
```python
#!/usr/bin/env python3
# master_control.py
'''Master control panel for SuperCat GTM - Enhanced'''

import os
import sys
from datetime import datetime

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 70)
        print("🚀 SUPERCAT GTM AUTOMATION - MASTER CONTROL v2.0")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
        
        print("\n📋 MAIN OPERATIONS")
        print("  1. Run Full Pipeline (Complete)")
        print("  2. Analyze Companies Only")
        print("  3. Generate Campaigns Only")
        print("  4. Process CSV File")
        
        print("\n🔧 TESTING & MONITORING")
        print("  5. Run Simple Test")
        print("  6. View Performance Dashboard")
        print("  7. System Health Check")
        
        print("\n📊 REPORTS & EXPORTS")
        print("  8. Generate All Reports")
        print("  9. Export Qualified Prospects")
        print("  10. Export Campaign Messages")
        
        print("\n⚙️ ADMINISTRATION")
        print("  11. Start Daily Automation")
        print("  12. View SQL Migrations")
        print("  13. Check Database Status")
        print("  0. Exit")
        
        print("=" * 70)
        choice = input("\nSelect option: ")
        
        if choice == "1":
            print("\n🚀 Running full pipeline...")
            os.system("python full_orchestrator.py full")
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            print("\n🔍 Running analysis only...")
            os.system("python full_orchestrator.py analysis_only")
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            print("\n✉️ Generating campaigns...")
            os.system("python full_orchestrator.py campaign_only")
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            csv_file = input("Enter CSV filename (or 'sample' for sample_prospects.csv): ")
            if csv_file == 'sample':
                csv_file = 'sample_prospects.csv'
            if os.path.exists(csv_file):
                os.system(f"python upload_prospects.py {csv_file}")
            else:
                print(f"❌ File not found: {csv_file}")
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            print("\n🧪 Running simple test...")
            os.system("python simple_test.py")
            input("\nPress Enter to continue...")
            
        elif choice == "6":
            print("\n📊 Performance Dashboard")
            os.system("python performance_dashboard.py")
            input("\nPress Enter to continue...")
            
        elif choice == "7":
            print("\n🏥 System Health Check")
            os.system("python health_monitor.py")
            input("\nPress Enter to continue...")
            
        elif choice == "8":
            print("\n📊 Generating all reports...")
            os.system("python reporting.py")
            input("\nPress Enter to continue...")
            
        elif choice == "9":
            print("\n📤 Exporting qualified prospects...")
            os.system('python -c "from reporting import ReportGenerator; r = ReportGenerator(); r.export_qualified_prospects()"')
            input("\nPress Enter to continue...")
            
        elif choice == "10":
            print("\n📤 Exporting campaign messages...")
            os.system('python -c "from reporting import ReportGenerator; r = ReportGenerator(); r.export_campaign_messages()"')
            input("\nPress Enter to continue...")
            
        elif choice == "11":
            print("\n⏰ Starting daily automation...")
            print("This will run continuously. Press Ctrl+C to stop.")
            confirm = input("Start automation? (y/n): ")
            if confirm.lower() == 'y':
                os.system("python automated_daily.py")
            
        elif choice == "12":
            print("\n📋 SQL Migrations")
            print("Copy and run in Supabase SQL editor:")
            print("-" * 40)
            os.system("cat create_tables.sql 2>/dev/null || type create_tables.sql 2>nul")
            input("\nPress Enter to continue...")
            
        elif choice == "13":
            print("\n🔍 Checking database...")
            os.system('python -c "from database.connection import db; print(\'✅ Database connected!\')"')
            input("\nPress Enter to continue...")
            
        elif choice == "0":
            print("\n👋 Goodbye!")
            sys.exit(0)
        
        else:
            print("\n❌ Invalid option")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()

```

### supercat_automation/database/models.py
```python

```

### supercat_automation/database/__init__.py
```python

```

### supercat_automation/database/connection.py
```python
# database/connection.py
"""
Database connection manager for Supabase
Handles all database operations with proper error handling
"""

from typing import Optional, List, Dict, Any
import logging
from datetime import datetime, timedelta
from supabase import create_client, Client
from config.settings import settings
import time
from functools import wraps

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry database operations on failure"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {delay} seconds...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

class DatabaseManager:
    """Manages all database operations with Supabase"""
    
    def __init__(self):
        """Initialize Supabase client"""
        try:
            self.client: Client = create_client(
                settings.supabase_url,
                settings.supabase_key
            )
            logger.info("✅ Successfully connected to Supabase")
        except Exception as e:
            logger.error(f"❌ Failed to connect to Supabase: {e}")
            raise
    
    # ============================================
    # TRADE SHOW OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def upsert_trade_show(self, trade_show_data: Dict[str, Any]) -> Optional[Dict]:
        """Insert or update a trade show"""
        try:
            # Check if trade show exists
            existing = self.client.table('trade_shows').select('*').eq(
                'name', trade_show_data['name']
            ).eq('start_date', trade_show_data['start_date']).execute()
            
            if existing.data:
                # Update existing
                result = self.client.table('trade_shows').update(trade_show_data).eq(
                    'id', existing.data[0]['id']
                ).execute()
                logger.info(f"Updated trade show: {trade_show_data['name']}")
            else:
                # Insert new
                result = self.client.table('trade_shows').insert(trade_show_data).execute()
                logger.info(f"Created new trade show: {trade_show_data['name']}")
            
            return result.data[0] if result.data else None
            
        except Exception as e:
            logger.error(f"Error upserting trade show: {e}")
            return None
    
    @retry_on_failure()
    def get_upcoming_trade_shows(self, days_ahead: int = 180) -> List[Dict]:
        """Get trade shows happening in the next N days"""
        try:
            future_date = (datetime.now() + timedelta(days=days_ahead)).isoformat()
            
            result = self.client.table('trade_shows').select('*').gte(
                'start_date', datetime.now().isoformat()
            ).lte('start_date', future_date).order('start_date').execute()
            
            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching upcoming trade shows: {e}")
            return []
    
    # ============================================
    # COMPANY OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def upsert_company(self, company_data: Dict[str, Any]) -> Optional[Dict]:
        """Insert or update a company"""
        try:
            # Clean the domain
            domain = company_data.get('domain', '').lower().strip()
            if domain.startswith('http'):
                domain = domain.split('//')[-1].split('/')[0]
            company_data['domain'] = domain
            
            # Check if company exists
            existing = self.client.table('companies').select('*').eq(
                'domain', domain
            ).execute()
            
            if existing.data:
                # Update existing
                company_id = existing.data[0]['id']
                result = self.client.table('companies').update(company_data).eq(
                    'id', company_id
                ).execute()
                logger.info(f"Updated company: {company_data.get('company_name', domain)}")
            else:
                # Insert new
                result = self.client.table('companies').insert(company_data).execute()
                logger.info(f"Created new company: {company_data.get('company_name', domain)}")
            
            return result.data[0] if result.data else None
            
        except Exception as e:
            logger.error(f"Error upserting company: {e}")
            return None
    
    @retry_on_failure()
    def get_qualified_companies(self, tier: str = 'tier_1') -> List[Dict]:
        """Get companies that meet qualification criteria"""
        try:
            column = f"{tier}_qualified"
            result = self.client.table('companies').select('*').eq(
                column, True
            ).order('overall_pain_score.desc').execute()
            
            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching qualified companies: {e}")
            return []
    
    @retry_on_failure()
    def update_pain_scores(self, company_id: str, pain_scores: Dict[str, float]) -> bool:
        """Update pain scores for a company"""
        try:
            # Calculate overall pain score
            scores = [
                pain_scores.get('sales_enablement_pain_score', 0) * 1.0,  # 100% weight
                pain_scores.get('technology_obsolescence_score', 0) * 0.93,  # 93% weight
                pain_scores.get('rep_performance_pain_score', 0) * 0.71,  # 71% weight
                pain_scores.get('sku_complexity_pain_score', 0) * 0.64  # 64% weight
            ]
            overall_score = sum(scores) / 3.28  # Normalized
            
            pain_scores['overall_pain_score'] = min(overall_score, 1.0)
            pain_scores['updated_at'] = datetime.now().isoformat()
            
            result = self.client.table('companies').update(pain_scores).eq(
                'id', company_id
            ).execute()
            
            return bool(result.data)
            
        except Exception as e:
            logger.error(f"Error updating pain scores: {e}")
            return False
    
    # ============================================
    # EXHIBITOR OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def link_exhibitor_to_show(self, exhibitor_data: Dict[str, Any]) -> Optional[Dict]:
        """Link a company as an exhibitor to a trade show"""
        try:
            # Check if link already exists
            existing = self.client.table('exhibitors').select('*').eq(
                'trade_show_id', exhibitor_data['trade_show_id']
            ).eq('company_id', exhibitor_data['company_id']).execute()
            
            if existing.data:
                # Update existing
                result = self.client.table('exhibitors').update(exhibitor_data).eq(
                    'id', existing.data[0]['id']
                ).execute()
            else:
                # Insert new
                result = self.client.table('exhibitors').insert(exhibitor_data).execute()
            
            return result.data[0] if result.data else None
            
        except Exception as e:
            logger.error(f"Error linking exhibitor: {e}")
            return None
    
    # ============================================
    # CAMPAIGN OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def create_campaign(self, campaign_data: Dict[str, Any]) -> Optional[Dict]:
        """Create a new campaign"""
        try:
            campaign_data['campaign_status'] = 'draft'
            campaign_data['created_at'] = datetime.now().isoformat()
            
            result = self.client.table('campaigns').insert(campaign_data).execute()
            
            if result.data:
                logger.info(f"Created campaign for company {campaign_data.get('company_id')}")
                return result.data[0]
            return None
            
        except Exception as e:
            logger.error(f"Error creating campaign: {e}")
            return None
    
    # ============================================
    # OUTREACH OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def create_outreach(self, outreach_data: Dict[str, Any]) -> Optional[Dict]:
        """Create an outreach record"""
        try:
            outreach_data['status'] = 'pending'
            outreach_data['created_at'] = datetime.now().isoformat()
            
            result = self.client.table('outreach').insert(outreach_data).execute()
            
            return result.data[0] if result.data else None
            
        except Exception as e:
            logger.error(f"Error creating outreach: {e}")
            return None
    
    @retry_on_failure()
    def get_pending_outreach(self, limit: int = 50) -> List[Dict]:
        """Get pending outreach records to send"""
        try:
            result = self.client.table('outreach').select(
                '*, companies(*), decision_makers(*), campaigns(*)'
            ).eq('status', 'pending').eq('sent_to_clay', False).limit(limit).execute()
            
            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching pending outreach: {e}")
            return []
    
    @retry_on_failure()
    def mark_outreach_sent_to_clay(self, outreach_id: str, response: Dict) -> bool:
        """Mark outreach as sent to Clay webhook"""
        try:
            update_data = {
                'sent_to_clay': True,
                'clay_webhook_response': response,
                'clay_sent_at': datetime.now().isoformat(),
                'status': 'sent_to_clay'
            }
            
            result = self.client.table('outreach').update(update_data).eq(
                'id', outreach_id
            ).execute()
            
            return bool(result.data)
            
        except Exception as e:
            logger.error(f"Error marking outreach as sent to Clay: {e}")
            return False
    
    # ============================================
    # AD SUGGESTION OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def save_ad_suggestions(self, ad_data: Dict[str, Any]) -> Optional[Dict]:
        """Save ad suggestions for partner team"""
        try:
            ad_data['created_at'] = datetime.now().isoformat()
            
            result = self.client.table('ad_suggestions').insert(ad_data).execute()
            
            if result.data:
                logger.info(f"Saved ad suggestions for campaign {ad_data.get('campaign_id')}")
                return result.data[0]
            return None
            
        except Exception as e:
            logger.error(f"Error saving ad suggestions: {e}")
            return None
    
    # ============================================
    # METRICS OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def update_daily_metrics(self, metrics: Dict[str, Any]) -> bool:
        """Update or insert daily performance metrics"""
        try:
            from datetime import date
            
            metrics['metric_date'] = date.today().isoformat()
            metrics['metric_week'] = date.today().isocalendar()[1]
            metrics['metric_month'] = date.today().month
            metrics['metric_year'] = date.today().year
            
            # Check if today's metrics exist
            existing = self.client.table('performance_metrics').select('*').eq(
                'metric_date', metrics['metric_date']
            ).execute()
            
            if existing.data:
                # Update
                result = self.client.table('performance_metrics').update(metrics).eq(
                    'id', existing.data[0]['id']
                ).execute()
            else:
                # Insert
                result = self.client.table('performance_metrics').insert(metrics).execute()
            
            return bool(result.data)
            
        except Exception as e:
            logger.error(f"Error updating daily metrics: {e}")
            return False
    
    # ============================================
    # CUSTOMER LANGUAGE OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def get_customer_language(self, category: str, limit: int = 10) -> List[Dict]:
        """Get customer language examples by category"""
        try:
            result = self.client.table('customer_language').select('*').eq(
                'category', category
            ).order('conversion_rate.desc').limit(limit).execute()

            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching customer language: {e}")
            return []
    
    # ============================================
    # EDP & TAM OPERATIONS
    # ============================================
    
    @retry_on_failure()
    def get_companies_for_analysis(self, limit: int = 100) -> List[Dict]:
        """Get companies that need pain analysis"""
        try:
            # Get companies without recent analysis
            cutoff_date = (datetime.now() - timedelta(days=7)).isoformat()
            
            result = self.client.table('companies').select('*').or_(
                f'last_website_scan.is.null,last_website_scan.lt.{cutoff_date}'
            ).limit(limit).execute()
            
            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching companies for analysis: {e}")
            return []
    
    @retry_on_failure()
    def get_companies_by_tier(self, tier: str) -> List[Dict]:
        """Get all companies in a specific TAM tier"""
        try:
            result = self.client.table('companies').select('*').eq(
                'tam_tier', tier
            ).order('psi_score.desc',).execute()
            
            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching tier {tier} companies: {e}")
            return []
    
    @retry_on_failure()
    def get_companies_by_edp(self, edp_tag: str) -> List[Dict]:
        """Get all companies with a specific EDP tag"""
        try:
            result = self.client.table('companies').select('*').contains(
                'edp_tags', [edp_tag]
            ).execute()
            
            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching companies with EDP {edp_tag}: {e}")
            return []
    
    @retry_on_failure()
    def get_multi_edp_companies(self) -> List[Dict]:
        """Get companies with multiple EDPs (high value targets)"""
        try:
            result = self.client.table('companies').select('*').eq(
                'has_multiple_edps', True
            ).order('edp_count.desc',).execute()

            return result.data
            
        except Exception as e:
            logger.error(f"Error fetching multi-EDP companies: {e}")
            return []
    
    @retry_on_failure()
    def get_tam_statistics(self) -> Dict:
        """Get TAM breakdown statistics"""
        try:
            # This would be better as a SQL query but Supabase doesn't support aggregates well
            all_companies = self.client.table('companies').select(
                'tam_tier', 'edp_tags', 'has_multiple_edps'
            ).execute()
            
            stats = {
                'total': len(all_companies.data),
                'by_tier': {},
                'by_edp': {},
                'multi_edp_count': 0
            }
            
            for company in all_companies.data:
                # Count by tier
                tier = company.get('tam_tier', 'UNKNOWN')
                stats['by_tier'][tier] = stats['by_tier'].get(tier, 0) + 1
                
                # Count by EDP
                for edp in company.get('edp_tags', []):
                    stats['by_edp'][edp] = stats['by_edp'].get(edp, 0) + 1
                
                # Count multi-EDP
                if company.get('has_multiple_edps'):
                    stats['multi_edp_count'] += 1
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting TAM statistics: {e}")
            return {}

# Create a singleton instance - THIS MUST BE AT THE BOTTOM, OUTSIDE THE CLASS
db = DatabaseManager()
```

### supercat_automation/database/migrations.py
```python
# database/migrations.py
"""
SQL migrations for EDP scoring system
Run these in your Supabase SQL editor
"""

migrations = """
-- Add EDP scoring columns to companies table
ALTER TABLE companies ADD COLUMN IF NOT EXISTS edp_scores JSONB DEFAULT '{}';
ALTER TABLE companies ADD COLUMN IF NOT EXISTS edp_tags TEXT[] DEFAULT '{}';
ALTER TABLE companies ADD COLUMN IF NOT EXISTS tam_tier VARCHAR(10);
ALTER TABLE companies ADD COLUMN IF NOT EXISTS website_evidence JSONB DEFAULT '{}';
ALTER TABLE companies ADD COLUMN IF NOT EXISTS last_website_scan TIMESTAMP;
ALTER TABLE companies ADD COLUMN IF NOT EXISTS psi_score FLOAT DEFAULT 0;

-- Create indexes for faster queries
CREATE INDEX IF NOT EXISTS idx_companies_tam_tier ON companies(tam_tier);
CREATE INDEX IF NOT EXISTS idx_companies_psi_score ON companies(psi_score DESC);
CREATE INDEX IF NOT EXISTS idx_companies_edp_tags ON companies USING GIN(edp_tags);

-- Add composite scoring
ALTER TABLE companies ADD COLUMN IF NOT EXISTS has_multiple_edps BOOLEAN DEFAULT FALSE;
ALTER TABLE companies ADD COLUMN IF NOT EXISTS primary_edp VARCHAR(50);
ALTER TABLE companies ADD COLUMN IF NOT EXISTS edp_count INTEGER DEFAULT 0;
"""

print("Copy and run these migrations in Supabase SQL editor:")
print(migrations)
```

### supercat_automation/analysis/psi_calculator.py
```python
# analysis/psi_calculator.py - NEW
class PainSignalIndex:
    """
    Calculate PSI score from website evidence
    Based on validated weights from 14 won deals
    """
    
    def calculate_psi(self, website_analysis):
        """
        Returns PSI score 0-100 and tier classification
        """
        
        # Use validated weights from won deals
        weights = {
            'sales_enablement_collapse': 0.35,  # 100% of won deals
            'technology_obsolescence': 0.30,     # 93% of won deals
            'rep_performance_crisis': 0.20,      # 71% of won deals
            'sku_complexity': 0.10,              # 64% of won deals
            'channel_conflict': 0.05             # 43% of won deals
        }
        
        scores = {}
        for edp_name, edp_data in website_analysis['edp_signals'].items():
            scores[edp_name] = self._calculate_edp_score(edp_name, edp_data)
        
        # Calculate weighted total
        total_psi = sum(scores[edp] * weights[edp] for edp in weights)
        
        # Determine tier
        if total_psi >= 70:
            tier = 'A'  # Crisis mode - will buy quickly
            urgency = 'immediate'
        elif total_psi >= 40:
            tier = 'B'  # Feeling pain - needs education
            urgency = 'quarterly'
        else:
            tier = 'C'  # Not ready - nurture only
            urgency = 'long_term'
        
        return {
            'psi_score': round(total_psi),
            'tier': tier,
            'urgency': urgency,
            'primary_pain': max(scores, key=scores.get),
            'edp_breakdown': scores,
            'evidence_strength': self._assess_evidence_quality(website_analysis)
        }
```

### supercat_automation/analysis/__init__.py
```python

```

### supercat_automation/analysis/qualification_scorer.py
```python
# analysis/qualification_scorer.py
"""
Qualification scoring based on won deal patterns
Uses exact criteria from successful customers
"""

import logging
from typing import Dict, List, Any
from datetime import datetime
from database.connection import db

logger = logging.getLogger(__name__)

class WonDealQualificationScorer:
    """
    Scores companies based on patterns from 14 won deals
    73% win rate when all Tier 1 criteria met
    """
    
    def __init__(self):
        """Initialize with proven qualification criteria"""
        # Tier 1: ALL must be true for highest win rate
        self.tier_1_criteria = {
            'b2b_wholesale': {
                'field': 'has_b2b_wholesale',
                'required_value': True,
                'weight': 1.0,
                'is_required': True
            },
            'field_sales_5plus': {
                'field': 'field_sales_count',
                'required_value': 5,
                'operator': '>=',
                'weight': 1.0,
                'is_required': True
            },
            'trade_shows_2plus': {
                'field': 'trade_show_count_annual',
                'required_value': 2,
                'operator': '>=',
                'weight': 1.0,
                'is_required': True
            },
            'manual_order_processing': {
                'field': 'uses_manual_order_process',
                'required_value': True,
                'weight': 1.0,
                'is_required': True
            },
            'complex_catalog_500plus': {
                'field': 'catalog_sku_count',
                'required_value': 500,
                'operator': '>=',
                'weight': 1.0,
                'is_required': True
            }
        }
        
        # Tier 2: 3+ should be true for strong score
        self.tier_2_criteria = {
            'legacy_erp': {
                'field': 'current_erp',
                'required_value': ['SAP', 'Oracle', 'QuickBooks'],
                'operator': 'in',
                'weight': 0.8
            },
            'international_ops': {
                'field': 'has_international_ops',
                'required_value': True,
                'weight': 0.6
            },
            'recent_acquisition': {
                'field': 'recent_acquisition_date',
                'required_value': 730,  # Within 2 years
                'operator': 'days_ago_less_than',
                'weight': 0.7
            },
            'configurable_products': {
                'field': 'has_complex_configurations',
                'required_value': True,
                'weight': 0.9
            },
            'multiple_price_levels': {
                'field': 'price_tier_count',
                'required_value': 3,
                'operator': '>=',
                'weight': 0.7
            },
            'independent_reps': {
                'field': 'has_independent_reps',
                'required_value': True,
                'weight': 0.8
            }
        }
        
        # Disqualifiers - immediate rejection
        self.disqualifiers = {
            'direct_to_consumer_only': {
                'field': 'is_b2c_only',
                'disqualify_if': True
            },
            'fewer_than_3_reps': {
                'field': 'field_sales_count',
                'disqualify_if': 3,
                'operator': '<'
            },
            'simple_catalog': {
                'field': 'catalog_sku_count',
                'disqualify_if': 100,
                'operator': '<'
            },
            'modern_tech_recent': {
                'field': 'tech_implementation_date',
                'disqualify_if': 730,  # Within 2 years
                'operator': 'days_ago_less_than'
            }
        }
    
    def score_company(self, company_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Score a company based on qualification criteria
        Returns qualification score and tier
        """
        try:
            # Check disqualifiers first
            disqualification = self.check_disqualifiers(company_data)
            if disqualification['disqualified']:
                return {
                    'qualified': False,
                    'tier': 'disqualified',
                    'score': 0.0,
                    'reason': disqualification['reason'],
                    'details': disqualification
                }
            
            # Score Tier 1 criteria
            tier_1_result = self.score_tier_1(company_data)
            
            # Score Tier 2 criteria
            tier_2_result = self.score_tier_2(company_data)
            
            # Calculate overall score
            overall_score = self.calculate_overall_score(tier_1_result, tier_2_result)
            
            # Determine tier
            tier = self.determine_tier(tier_1_result, tier_2_result, overall_score)
            
            # Determine if qualified
            qualified = tier in ['tier_1', 'tier_2']
            
            # Update database
            self.update_company_qualification(company_data.get('id'), {
                'tier_1_qualified': tier == 'tier_1',
                'tier_2_qualified': tier == 'tier_2',
                'qualification_score': overall_score,
                'disqualified': not qualified
            })
            
            return {
                'qualified': qualified,
                'tier': tier,
                'score': overall_score,
                'tier_1_criteria_met': tier_1_result['criteria_met'],
                'tier_1_missing': tier_1_result['missing_criteria'],
                'tier_2_criteria_met': tier_2_result['criteria_met'],
                'win_probability': self.estimate_win_probability(tier, overall_score),
                'recommended_action': self.recommend_action(tier, overall_score)
            }
            
        except Exception as e:
            logger.error(f"Error scoring company: {e}")
            return {
                'qualified': False,
                'error': str(e),
                'score': 0.0
            }
    
    def check_disqualifiers(self, company_data: Dict) -> Dict[str, Any]:
        """Check if company has any disqualifying characteristics"""
        for disqualifier_name, config in self.disqualifiers.items():
            field_value = company_data.get(config['field'])
            
            if field_value is None:
                continue
            
            operator = config.get('operator', '==')
            disqualify_value = config['disqualify_if']
            
            is_disqualified = False
            
            if operator == '==':
                is_disqualified = field_value == disqualify_value
            elif operator == '<':
                is_disqualified = field_value < disqualify_value
            elif operator == 'days_ago_less_than':
                # Check if date is within N days
                if isinstance(field_value, str):
                    from datetime import datetime, timedelta
                    field_date = datetime.fromisoformat(field_value)
                    days_ago = (datetime.now() - field_date).days
                    is_disqualified = days_ago < disqualify_value
            
            if is_disqualified:
                return {
                    'disqualified': True,
                    'reason': f"Disqualified due to: {disqualifier_name}",
                    'field': config['field'],
                    'value': field_value
                }
        
        return {'disqualified': False}
    
    def score_tier_1(self, company_data: Dict) -> Dict[str, Any]:
        """Score Tier 1 criteria - ALL must be met"""
        criteria_met = []
        missing_criteria = []
        total_score = 0
        
        for criterion_name, config in self.tier_1_criteria.items():
            field_value = company_data.get(config['field'])
            
            if field_value is None:
                if config.get('is_required', False):
                    missing_criteria.append(criterion_name)
                continue
            
            meets_criterion = self.evaluate_criterion(field_value, config)
            
            if meets_criterion:
                criteria_met.append(criterion_name)
                total_score += config['weight']
            else:
                missing_criteria.append(criterion_name)
        
        # For Tier 1, ALL criteria must be met
        all_met = len(missing_criteria) == 0 and len(criteria_met) == len(self.tier_1_criteria)
        
        return {
            'all_criteria_met': all_met,
            'criteria_met': criteria_met,
            'missing_criteria': missing_criteria,
            'score': total_score / len(self.tier_1_criteria) if self.tier_1_criteria else 0
        }
    
    def score_tier_2(self, company_data: Dict) -> Dict[str, Any]:
        """Score Tier 2 criteria - 3+ should be met"""
        criteria_met = []
        missing_criteria = []
        total_score = 0
        max_possible_score = sum(c['weight'] for c in self.tier_2_criteria.values())
        
        for criterion_name, config in self.tier_2_criteria.items():
            field_value = company_data.get(config['field'])
            
            if field_value is None:
                missing_criteria.append(criterion_name)
                continue
            
            meets_criterion = self.evaluate_criterion(field_value, config)
            
            if meets_criterion:
                criteria_met.append(criterion_name)
                total_score += config['weight']
            else:
                missing_criteria.append(criterion_name)
        
        # For Tier 2, 3+ criteria should be met
        sufficient_criteria = len(criteria_met) >= 3
        
        return {
            'sufficient_criteria_met': sufficient_criteria,
            'criteria_met': criteria_met,
            'missing_criteria': missing_criteria,
            'score': total_score / max_possible_score if max_possible_score else 0
        }
    
    def evaluate_criterion(self, field_value: Any, config: Dict) -> bool:
        """Evaluate if a field value meets the criterion"""
        required_value = config['required_value']
        operator = config.get('operator', '==')
        
        if operator == '==':
            return field_value == required_value
        elif operator == '>=':
            return field_value >= required_value
        elif operator == '<=':
            return field_value <= required_value
        elif operator == 'in':
            return field_value in required_value
        elif operator == 'days_ago_less_than':
            if isinstance(field_value, str):
                from datetime import datetime
                field_date = datetime.fromisoformat(field_value)
                days_ago = (datetime.now() - field_date).days
                return days_ago < required_value
        
        return False
    
    def calculate_overall_score(self, tier_1_result: Dict, tier_2_result: Dict) -> float:
        """Calculate overall qualification score"""
        # Tier 1 is weighted more heavily
        tier_1_weight = 0.7
        tier_2_weight = 0.3
        
        overall = (tier_1_result['score'] * tier_1_weight) + (tier_2_result['score'] * tier_2_weight)
        
        return min(overall, 1.0)
    
    def determine_tier(self, tier_1_result: Dict, tier_2_result: Dict, overall_score: float) -> str:
        """Determine qualification tier"""
        if tier_1_result['all_criteria_met']:
            return 'tier_1'
        elif tier_2_result['sufficient_criteria_met'] and overall_score >= 0.5:
            return 'tier_2'
        elif overall_score >= 0.3:
            return 'tier_3'
        else:
            return 'unqualified'
    
    def estimate_win_probability(self, tier: str, score: float) -> float:
        """Estimate win probability based on historical data"""
        win_rates = {
            'tier_1': 0.73,  # 73% win rate from analysis
            'tier_2': 0.48,  # 48% win rate from analysis
            'tier_3': 0.25,  # Estimated
            'unqualified': 0.05
        }
        
        base_rate = win_rates.get(tier, 0.05)
        
        # Adjust based on score
        adjusted_rate = base_rate * (0.8 + (score * 0.4))  # Score can boost up to 40%
        
        return min(adjusted_rate, 0.95)  # Cap at 95%
    
    def recommend_action(self, tier: str, score: float) -> str:
        """Recommend action based on qualification"""
        if tier == 'tier_1':
            return "🔥 HIGH PRIORITY - Immediate multi-channel outreach recommended"
        elif tier == 'tier_2':
            return "📊 GOOD FIT - Standard outreach sequence recommended"
        elif tier == 'tier_3':
            return "👀 MONITOR - Add to nurture campaign"
        else:
            return "⏸️ HOLD - Do not pursue at this time"
    
    def update_company_qualification(self, company_id: str, qualification_data: Dict):
        """Update company qualification in database"""
        try:
            db.client.table('companies').update(qualification_data).eq(
                'id', company_id
            ).execute()
        except Exception as e:
            logger.error(f"Error updating qualification: {e}")
```

### supercat_automation/analysis/customer_language.py
```python
# analysis/customer_language.py
'''Customer language patterns from won deals'''

class CustomerLanguageLibrary:
    '''Proven language patterns from 14 won deals'''
    
    def __init__(self):
        # Actual customer quotes by pain type
        self.pain_language = {
            'sales_enablement_collapse': {
                'customer_words': [
                    "taking 1-3 hours daily just for basic reporting",
                    "reps spending 20% time selling, 80% on admin",
                    "manually go through spreadsheets",
                    "can't work without WiFi at shows",
                    "no simple way to figure out top sellers"
                ],
                'impact_statements': [
                    "losing 4 out of 5 opportunities",
                    "3 hours daily per rep wasted",
                    "30% order error rate",
                    "missing critical selling time"
                ]
            },
            'technology_obsolescence': {
                'customer_words': [
                    "old SAP system not set up for modern",
                    "SFTP is ancient technology",
                    "asking CSV files around is not state of the art",
                    "can't import customers",
                    "ERP company went bankrupt"
                ],
                'impact_statements': [
                    "40-50% slower than competitors",
                    "embarrassing to customers",
                    "losing to digital-native companies",
                    "can't compete anymore"
                ]
            },
            'rep_performance_crisis': {
                'customer_words': [
                    "top reps logging in 10-12 times daily",
                    "others barely using it",
                    "60+ year old reps don't want to learn",
                    "zero visibility into what reps are doing",
                    "need to know if salespeople are hustling"
                ],
                'impact_statements': [
                    "10x usage difference between reps",
                    "can't coach effectively",
                    "no data for territory decisions",
                    "flying blind on performance"
                ]
            },
            'sku_complexity': {
                'customer_words': [
                    "5 different combinations per item",
                    "20 different option sets",
                    "2,000-3,000 SKUs with colors",
                    "19 levels for fabrics",
                    "tearing structure complexity"
                ],
                'impact_statements': [
                    "25% return rate from errors",
                    "quotes take hours",
                    "constantly shipping wrong products",
                    "margin erosion from mistakes"
                ]
            }
        }
        
        # Proven discovery questions
        self.discovery_questions = {
            'qualifying': [
                "Walk me through what happens when a rep takes an order at a trade show today?",
                "How long does it take from customer interest to confirmed order?",
                "What percentage of your reps are consistently hitting quota?",
                "How do you currently know what your reps are doing day-to-day?",
                "When did you last lose a deal to a faster competitor?"
            ],
            'pain_probing': [
                "How many hours daily do your reps spend on non-selling activities?",
                "What's your current order error rate?",
                "How often do pricing mistakes happen?",
                "Can your reps access inventory in real-time?",
                "How many systems do reps check for one quote?"
            ],
            'impact': [
                "What does each order error cost you?",
                "How much revenue do you generate at trade shows?",
                "What percentage of annual sales comes from your top 3 shows?",
                "How many deals do you lose to faster competitors?",
                "What's the productivity difference between top and bottom reps?"
            ]
        }
        
        # Objection handlers that worked
        self.objection_responses = {
            'too_expensive': {
                'response': "You're losing 3 hours daily per rep. At $100/hour loaded cost, that's $75,000 annually per rep.",
                'success_rate': 0.67
            },
            'need_it_approval': {
                'response': "This replaces spreadsheets, not your ERP. Most deploy without IT.",
                'success_rate': 0.73
            },
            'reps_wont_adopt': {
                'response': "Your top reps are begging for this. Start with them - the others will follow.",
                'success_rate': 0.81
            }
        }
    
    def get_pain_language(self, pain_type: str) -> dict:
        '''Get customer language for specific pain'''
        return self.pain_language.get(pain_type, self.pain_language['sales_enablement_collapse'])
    
    def get_discovery_question(self, stage: str = 'qualifying') -> list:
        '''Get discovery questions by stage'''
        return self.discovery_questions.get(stage, self.discovery_questions['qualifying'])
    
    def get_objection_response(self, objection: str) -> dict:
        '''Get proven objection response'''
        return self.objection_responses.get(objection, {
            'response': 'Let me show you the ROI calculation...',
            'success_rate': 0.5
        })

```

### supercat_automation/analysis/prospect_processor.py
```python
# analysis/prospect_processor.py
"""
Process prospects from multiple sources:
- CSV uploads
- Manual entry
- Client validation
- Trade show scraping
"""

import pandas as pd
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
import asyncio
from pathlib import Path

from analysis.pain_detector import MultiSourcePainDetector
from scrapers.website_evidence import WebsiteEvidenceExtractor
from database.connection import db

logger = logging.getLogger(__name__)

class ProspectProcessor:
    """
    Universal processor for prospects from any source.
    Can validate existing clients or analyze new prospects.
    """
    
    def __init__(self) -> None:
        """Initialize the ProspectProcessor with pain detector and website extractor."""
        self.pain_detector = MultiSourcePainDetector()
        self.website_extractor = WebsiteEvidenceExtractor()
    
    async def process_csv_upload(self, csv_path: str, is_client_validation: bool = False) -> Dict[str, Any]:
        """
        Process prospects from a CSV file.
        Args:
            csv_path (str): Path to the CSV file.
            is_client_validation (bool): Whether to validate existing clients.
        Returns:
            Dict[str, Any]: Results of processing.
        """
        """
        Process prospects from CSV file
        
        Expected CSV columns:
        - company_name (required)
        - domain (required)
        - trade_shows (optional, comma-separated)
        - employee_count (optional)
        - current_erp (optional)
        - is_customer (optional, for validation)
        - customer_tier (optional, for validation)
        """
        
        try:
            # Read CSV
            df = pd.read_csv(csv_path)
            
            # Validate required columns
            required = ['company_name', 'domain']
            missing = [col for col in required if col not in df.columns]
            if missing:
                raise ValueError(f"Missing required columns: {missing}")
            
            results = {
                'total_processed': 0,
                'successful': 0,
                'failed': 0,
                'companies': [],
                'validation_results': {} if is_client_validation else None
            }
            
            # Process each company
            for _, row in df.iterrows():
                company_data = self._prepare_company_data(row)
                
                try:
                    # Run analysis
                    analysis = self.pain_detector.analyze_company(company_data)
                    
                    # Store in database
                    saved = await self._save_prospect(company_data, analysis, is_client_validation)
                    
                    if saved:
                        results['successful'] += 1
                        results['companies'].append({
                            'company_name': company_data['company_name'],
                            'domain': company_data['domain'],
                            'tam_tier': analysis['tam_tier'],
                            'primary_edp': analysis['primary_edp'],
                            'psi_score': analysis['total_pain_score']
                        })
                        
                        # If validating clients, compare scores
                        if is_client_validation and row.get('is_customer'):
                            validation = self._validate_client_score(row, analysis)
                            results['validation_results'][company_data['company_name']] = validation
                    
                except Exception as e:
                    logger.error(f"Error processing {row['company_name']}: {e}")
                    results['failed'] += 1
                
                results['total_processed'] += 1
            
            # Generate summary
            results['summary'] = self._generate_processing_summary(results, is_client_validation)
            
            return results
            
        except Exception as e:
            logger.error(f"Error processing CSV: {e}")
            return {'error': str(e)}
    
    async def process_single_prospect(self, company_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a single prospect (manual entry or API).
        Args:
            company_data (Dict[str, Any]): Data for the company.
        Returns:
            Dict[str, Any]: Analysis results.
        """
        """
        Process a single prospect (manual entry or API)
        """
        
        try:
            # Ensure minimum required fields
            if not company_data.get('domain'):
                raise ValueError("Domain is required")
            
            if not company_data.get('company_name'):
                # Try to extract from domain
                company_data['company_name'] = company_data['domain'].replace('.com', '').title()
            
            # Run analysis
            analysis = self.pain_detector.analyze_company(company_data)
            
            # Save to database
            saved = await self._save_prospect(company_data, analysis, False)
            
            return {
                'success': saved,
                'company': company_data['company_name'],
                'analysis': analysis
            }
            
        except Exception as e:
            logger.error(f"Error processing prospect: {e}")
            return {'success': False, 'error': str(e)}
    
    async def validate_existing_clients(self, client_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Validate scoring against known client outcomes.
        Args:
            client_list (List[Dict[str, Any]]): List of client data.
        Returns:
            Dict[str, Any]: Validation results.
        """
        """
        Validate our scoring against known client outcomes
        Helps calibrate the scoring algorithm
        """
        
        validation_results = {
            'total_clients': len(client_list),
            'accurately_scored': 0,
            'overscored': 0,
            'underscored': 0,
            'accuracy_by_tier': {},
            'edp_correlation': {},
            'insights': []
        }
        
        for client in client_list:
            try:
                # Run current analysis
                analysis = self.pain_detector.analyze_company(client)
                
                # Compare to actual outcome
                actual_tier = client.get('actual_tier', 'UNKNOWN')
                predicted_tier = analysis['tam_tier']
                
                if predicted_tier == actual_tier:
                    validation_results['accurately_scored'] += 1
                elif self._tier_to_number(predicted_tier) > self._tier_to_number(actual_tier):
                    validation_results['overscored'] += 1
                elif self._tier_to_number(predicted_tier) < self._tier_to_number(actual_tier):
                    validation_results['underscored'] += 1
                
                # Track by tier
                if actual_tier not in validation_results['accuracy_by_tier']:
                    validation_results['accuracy_by_tier'][actual_tier] = {
                        'correct': 0, 'total': 0
                    }
                
                validation_results['accuracy_by_tier'][actual_tier]['total'] += 1
                if predicted_tier == actual_tier:
                    validation_results['accuracy_by_tier'][actual_tier]['correct'] += 1
                
                # Track EDP correlation
                for edp in analysis.get('edp_tags', []):
                    if edp not in validation_results['edp_correlation']:
                        validation_results['edp_correlation'][edp] = {
                            'won': 0, 'total': 0
                        }
                    validation_results['edp_correlation'][edp]['total'] += 1
                    if client.get('won_deal'):
                        validation_results['edp_correlation'][edp]['won'] += 1
                
            except Exception as e:
                logger.error(f"Error validating client {client.get('company_name')}: {e}")
        
        # Generate insights
        validation_results['insights'] = self._generate_validation_insights(validation_results)
        
        return validation_results
    
    def _prepare_company_data(self, row: pd.Series) -> Dict[str, Any]:
        """
        Convert CSV row to company data format.
        Args:
            row (pd.Series): Row from CSV.
        Returns:
            Dict[str, Any]: Company data.
        """
        """Convert CSV row to company data format"""
        
        company_data = {
            'company_name': row['company_name'],
            'domain': row['domain'].strip().lower()
        }
        
        # Add optional fields
        if 'trade_shows' in row and pd.notna(row['trade_shows']):
            company_data['trade_shows'] = [s.strip() for s in str(row['trade_shows']).split(',')]
        
        if 'employee_count' in row and pd.notna(row['employee_count']):
            company_data['employee_count'] = int(row['employee_count'])
        
        if 'current_erp' in row and pd.notna(row['current_erp']):
            company_data['current_erp'] = row['current_erp']
        
        # Add enrichment data if available
        enrichment = {}
        for col in ['technologies', 'industry', 'revenue']:
            if col in row and pd.notna(row[col]):
                enrichment[col] = row[col]
        
        if enrichment:
            company_data['enrichment_data'] = enrichment
        
        return company_data
    
    async def _save_prospect(self, company_data: Dict[str, Any], analysis: Dict[str, Any], is_validation: bool) -> bool:
        """
        Save prospect to database.
        Args:
            company_data (Dict[str, Any]): Company data.
            analysis (Dict[str, Any]): Analysis results.
            is_validation (bool): Is this a validation run.
        Returns:
            bool: Success status.
        """
        """Save prospect to database"""
        
        try:
            # Prepare database record
            db_record = {
                'company_name': company_data['company_name'],
                'domain': company_data['domain'],
                'source': 'manual_upload' if not is_validation else 'client_validation',
                'tam_tier': analysis['tam_tier'],
                'primary_edp': analysis['primary_edp'],
                'edp_tags': analysis['edp_tags'],
                'edp_scores': analysis['edp_scores'],
                'psi_score': analysis['total_pain_score'],
                'has_multiple_edps': analysis['has_multiple_edps'],
                'website_evidence': analysis['evidence'].get('website', {}),
                'last_website_scan': datetime.now().isoformat()
            }
            
            # Upsert to database
            result = db.upsert_company(db_record)
            
            return result is not None
            
        except Exception as e:
            logger.error(f"Error saving prospect: {e}")
            return False
    
    def _validate_client_score(self, client_row: pd.Series, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compare predicted vs actual for validation.
        Args:
            client_row (pd.Series): Client row.
            analysis (Dict[str, Any]): Analysis results.
        Returns:
            Dict[str, Any]: Validation comparison.
        """
        """Compare predicted vs actual for validation"""
        
        validation = {
            'predicted_tier': analysis['tam_tier'],
            'actual_tier': client_row.get('customer_tier', 'UNKNOWN'),
            'predicted_score': analysis['total_pain_score'],
            'predicted_edps': analysis['edp_tags'],
            'match': False,
            'insights': []
        }
        
        # Check if tiers match
        if validation['predicted_tier'] == validation['actual_tier']:
            validation['match'] = True
            validation['insights'].append("✅ Correctly predicted tier")
        else:
            validation['insights'].append(f"❌ Predicted {validation['predicted_tier']} but actual was {validation['actual_tier']}")
        
        # Check if primary EDP matches known pain
        if client_row.get('known_pain') and analysis['primary_edp']:
            if client_row['known_pain'].lower() in analysis['primary_edp'].lower():
                validation['insights'].append("✅ Primary pain correctly identified")
            else:
                validation['insights'].append(f"⚠️ Expected {client_row['known_pain']} but found {analysis['primary_edp']}")
        
        return validation
    
    def _tier_to_number(self, tier: str) -> int:
        """
        Convert tier string to number for comparison.
        Args:
            tier (str): Tier string.
        Returns:
            int: Numeric tier value.
        """
        """Convert tier to number for comparison"""
        
        tiers = {
            'TIER_1_IMMEDIATE': 4,
            'TIER_2_QUARTERLY': 3,
            'TIER_3_NURTURE': 2,
            'TIER_4_MONITOR': 1,
            'UNKNOWN': 0
        }
        
        return tiers.get(tier, 0)
    
    def _generate_processing_summary(self, results: Dict[str, Any], is_validation: bool) -> str:
        """
        Generate human-readable summary of processing results.
        Args:
            results (Dict[str, Any]): Processing results.
            is_validation (bool): Is this a validation run.
        Returns:
            str: Summary string.
        """
        """Generate human-readable summary"""
        
        summary = f"""
        Processing Complete
        ==================
        Total Processed: {results['total_processed']}
        Successful: {results['successful']}
        Failed: {results['failed']}
        
        TAM Distribution:
        """
        
        # Count by tier
        tier_counts = {}
        for company in results['companies']:
            tier = company['tam_tier']
            tier_counts[tier] = tier_counts.get(tier, 0) + 1
        
        for tier, count in sorted(tier_counts.items()):
            summary += f"  {tier}: {count}\n"
        
        if is_validation and results['validation_results']:
            summary += f"""
        
        Validation Results:
        ===================
        """
            correct = sum(1 for v in results['validation_results'].values() if v['match'])
            accuracy = (correct / len(results['validation_results']) * 100) if results['validation_results'] else 0
            
            summary += f"  Accuracy: {accuracy:.1f}%\n"
            summary += f"  Correct: {correct}/{len(results['validation_results'])}\n"
        
        return summary
    
    def _generate_validation_insights(self, validation_results: Dict[str, Any]) -> List[str]:
        """
        Generate insights from validation results.
        Args:
            validation_results (Dict[str, Any]): Results from client validation.
        Returns:
            List[str]: List of human-readable insights.
        """
        insights: List[str] = []

        # Overall accuracy
        accurately_scored: int = validation_results.get('accurately_scored', 0)
        total_clients: int = validation_results.get('total_clients', 0)
        accuracy: float = (accurately_scored / total_clients * 100) if total_clients else 0.0
        insights.append(f"Overall accuracy: {accuracy:.1f}%")

        # Tendency analysis
        overscored: int = validation_results.get('overscored', 0)
        underscored: int = validation_results.get('underscored', 0)
        if overscored > underscored:
            insights.append("⚠️ System tends to OVERSCORE (too optimistic)")
        elif underscored > overscored:
            insights.append("⚠️ System tends to UNDERSCORE (too conservative)")
        else:
            insights.append("✅ Scoring is well-balanced")

        # EDP correlation
        best_edp: Optional[str] = None
        best_correlation: float = 0.0
        edp_correlation: Dict[str, Dict[str, int]] = validation_results.get('edp_correlation', {})
        for edp, stats in edp_correlation.items():
            total: int = stats.get('total', 0)
            won: int = stats.get('won', 0)
            if total > 0:
                correlation: float = won / total
                if correlation > best_correlation:
                    best_correlation = correlation
                    best_edp = edp

        if best_edp:
            insights.append(f"🎯 Best predictor: {best_edp} ({best_correlation*100:.0f}% win rate)")

        return insights
```

### supercat_automation/analysis/pain_detector.py
```python
# analysis/pain_detector.py
"""
Multi-layered pain detection system
Combines website evidence with other data sources
Tags companies with multiple EDPs for TAM mapping
"""

import logging
from typing import Dict, List, Any, Set
from datetime import datetime, timedelta
from scrapers.website_evidence import WebsiteEvidenceExtractor
from database.connection import db

logger = logging.getLogger(__name__)

class MultiSourcePainDetector:
    """
    Detects and scores all 5 validated EDPs
    Companies can have multiple EDPs (overlapping pain)
    Designed for complete TAM mapping
    """
    
    def __init__(self):
        self.website_extractor = WebsiteEvidenceExtractor()
        
        # Validated from 14 won deals
        self.edp_definitions = {
            'sales_enablement_collapse': {
                'display_name': 'Sales Enablement System Collapse',
                'weight': 1.0,
                'won_deal_frequency': '100%',
                'qualifying_indicators': [
                    'manual_order_processing',
                    'no_mobile_access',
                    'paper_catalogs',
                    'no_real_time_inventory',
                    'trade_show_chaos'
                ]
            },
            'technology_obsolescence': {
                'display_name': 'Technology Obsolescence',
                'weight': 0.93,
                'won_deal_frequency': '93%',
                'qualifying_indicators': [
                    'legacy_erp',
                    'csv_uploads',
                    'no_api',
                    'outdated_systems',
                    'no_integrations'
                ]
            },
            'rep_performance_crisis': {
                'display_name': 'Rep Performance Crisis',
                'weight': 0.71,
                'won_deal_frequency': '71%',
                'qualifying_indicators': [
                    'no_rep_visibility',
                    'no_rep_tools',
                    'territory_chaos',
                    'high_rep_turnover'
                ]
            },
            'sku_complexity': {
                'display_name': 'SKU Proliferation & Complexity',
                'weight': 0.64,
                'won_deal_frequency': '64%',
                'qualifying_indicators': [
                    'high_sku_count',
                    'complex_configurations',
                    'no_product_search',
                    'catalog_chaos'
                ]
            },
            'channel_conflict': {
                'display_name': 'Channel Conflict',
                'weight': 0.43,
                'won_deal_frequency': '43%',
                'qualifying_indicators': [
                    'multiple_channels',
                    'pricing_inconsistency',
                    'dealer_confusion',
                    'brand_fragmentation'
                ]
            }
        }
    
    def analyze_company(self, company_data: Dict) -> Dict:
        """
        Complete pain analysis with multi-EDP tagging
        Returns comprehensive scoring for TAM mapping
        """
        
        analysis = {
            'company_id': company_data.get('id'),
            'company_name': company_data.get('company_name'),
            'analysis_timestamp': datetime.now().isoformat(),
            'data_sources_used': [],
            'edp_scores': {},
            'edp_tags': [],
            'tam_tier': None,
            'total_pain_score': 0,
            'primary_edp': None,
            'has_multiple_edps': False,
            'qualified': False,
            'evidence': {
                'website': {},
                'trade_show': {},
                'enrichment': {}
            },
            'personalization_data': {}
        }
        
        # Layer 1: Website Analysis (Primary Source)
        if company_data.get('domain'):
            logger.info(f"Analyzing website: {company_data['domain']}")
            website_results = self.website_extractor.analyze_website(company_data['domain'])
            
            analysis['data_sources_used'].append('website')
            analysis['evidence']['website'] = website_results
            
            # Process website evidence into EDP scores
            for edp_name, evidence in website_results.get('edp_evidence', {}).items():
                if evidence.get('weighted_score', 0) > 0:
                    analysis['edp_scores'][edp_name] = evidence['weighted_score']
        
        # Layer 2: Trade Show Data (Urgency Multiplier)
        if company_data.get('trade_shows'):
            analysis['data_sources_used'].append('trade_show')
            urgency_multiplier = self._calculate_trade_show_urgency(company_data['trade_shows'])
            
            # Boost all scores based on trade show proximity
            for edp_name in analysis['edp_scores']:
                analysis['edp_scores'][edp_name] *= urgency_multiplier
            
            analysis['evidence']['trade_show'] = {
                'shows': company_data['trade_shows'],
                'urgency_multiplier': urgency_multiplier
            }
        
        # Layer 3: Enrichment Data (Additional Signals)
        if company_data.get('enrichment_data'):
            analysis['data_sources_used'].append('enrichment')
            self._process_enrichment_signals(company_data['enrichment_data'], analysis)
        
        # Calculate final scores and tags
        analysis = self._finalize_scoring(analysis)
        
        # Save to database
        self._save_analysis(company_data.get('id'), analysis)
        
        return analysis
    
    def _calculate_trade_show_urgency(self, trade_shows: List[str]) -> float:
        """Calculate urgency multiplier based on trade show proximity"""
        
        # Trade show dates (you'd pull these from a database)
        show_dates = {
            'High Point Market': datetime(2024, 4, 20),
            'Vegas Market': datetime(2024, 1, 28),
            'NeoCon': datetime(2024, 6, 10),
            'Lightovation': datetime(2024, 1, 15)
        }
        
        # Find nearest show
        min_days = 365
        for show in trade_shows:
            if show in show_dates:
                days_until = (show_dates[show] - datetime.now()).days
                if 0 < days_until < min_days:
                    min_days = days_until
        
        # Calculate multiplier
        if min_days <= 30:
            return 1.8  # Extreme urgency
        elif min_days <= 60:
            return 1.5  # High urgency
        elif min_days <= 90:
            return 1.3  # Moderate urgency
        else:
            return 1.1  # Low urgency
    
    def _process_enrichment_signals(self, enrichment_data: Dict, analysis: Dict):
        """Process additional signals from enrichment"""
        
        # Employee count -> affects multiple EDPs
        if enrichment_data.get('employee_count'):
            emp_count = enrichment_data['employee_count']
            if emp_count > 100:
                # Larger companies have more complexity
                for edp in ['sku_complexity', 'channel_conflict']:
                    if edp in analysis['edp_scores']:
                        analysis['edp_scores'][edp] *= 1.2
        
        # Technology stack
        if enrichment_data.get('technologies'):
            tech_list = enrichment_data['technologies'].lower()
            
            # Check for legacy systems
            legacy_indicators = ['sap', 'oracle', 'as400', 'quickbooks']
            if any(legacy in tech_list for legacy in legacy_indicators):
                if 'technology_obsolescence' not in analysis['edp_scores']:
                    analysis['edp_scores']['technology_obsolescence'] = 0.5
                else:
                    analysis['edp_scores']['technology_obsolescence'] *= 1.3
    
    def _finalize_scoring(self, analysis: Dict) -> Dict:
        """
        Finalize scoring and determine TAM tier
        Handle multiple EDPs per company
        """
        
        # Identify all significant EDPs (score > 0.3)
        significant_edps = []
        for edp_name, score in analysis['edp_scores'].items():
            if score > 0.3:
                significant_edps.append({
                    'name': edp_name,
                    'score': score,
                    'display_name': self.edp_definitions[edp_name]['display_name']
                })
                # Add to tags
                analysis['edp_tags'].append(edp_name)
        
        # Sort by score
        significant_edps.sort(key=lambda x: x['score'], reverse=True)
        
        # Set primary EDP
        if significant_edps:
            analysis['primary_edp'] = significant_edps[0]['name']
            analysis['has_multiple_edps'] = len(significant_edps) > 1
        
        # Calculate total pain score
        analysis['total_pain_score'] = sum(e['score'] for e in significant_edps)
        
        # Determine TAM tier
        if analysis['total_pain_score'] >= 2.5 or len(significant_edps) >= 4:
            analysis['tam_tier'] = 'TIER_1_IMMEDIATE'
            analysis['qualified'] = True
        elif analysis['total_pain_score'] >= 1.5 or len(significant_edps) >= 3:
            analysis['tam_tier'] = 'TIER_2_QUARTERLY'
            analysis['qualified'] = True
        elif analysis['total_pain_score'] >= 0.8 or len(significant_edps) >= 2:
            analysis['tam_tier'] = 'TIER_3_NURTURE'
            analysis['qualified'] = False
        else:
            analysis['tam_tier'] = 'TIER_4_MONITOR'
            analysis['qualified'] = False
        
        # Add tier explanation
        analysis['tier_explanation'] = self._explain_tier(analysis)
        
        return analysis
    
    def _explain_tier(self, analysis: Dict) -> str:
        """Generate human-readable explanation of tier placement"""
        
        explanations = {
            'TIER_1_IMMEDIATE': f"Critical pain across {len(analysis['edp_tags'])} areas. Immediate outreach required.",
            'TIER_2_QUARTERLY': f"Significant pain in {len(analysis['edp_tags'])} areas. Quarterly follow-up recommended.",
            'TIER_3_NURTURE': f"Moderate pain detected. Add to nurture campaign.",
            'TIER_4_MONITOR': "Minimal pain detected. Monitor for changes."
        }
        
        return explanations.get(analysis['tam_tier'], "Unknown tier")
    
    def _save_analysis(self, company_id: str, analysis: Dict):
        """Save analysis results to database"""
        
        if not company_id:
            return
        
        try:
            update_data = {
                'edp_scores': analysis['edp_scores'],
                'edp_tags': analysis['edp_tags'],
                'tam_tier': analysis['tam_tier'],
                'primary_edp': analysis['primary_edp'],
                'has_multiple_edps': analysis['has_multiple_edps'],
                'psi_score': analysis['total_pain_score'],
                'website_evidence': analysis['evidence'].get('website', {}),
                'last_website_scan': datetime.now().isoformat(),
                'edp_count': len(analysis['edp_tags'])
            }
            
            db.client.table('companies').update(update_data).eq('id', company_id).execute()
            logger.info(f"Saved analysis for company {company_id}")
            
        except Exception as e:
            logger.error(f"Error saving analysis: {e}")
    
    def get_tam_summary(self) -> Dict:
        """
        Get summary of entire TAM by tiers and EDPs
        Useful for understanding market coverage
        """
        
        try:
            # Get tier distribution
            tier_counts = db.client.table('companies').select('tam_tier').execute()
            
            # Get EDP distribution
            edp_counts = db.client.table('companies').select('edp_tags').execute()
            
            # Process results
            summary = {
                'total_companies': len(tier_counts.data),
                'tier_distribution': {},
                'edp_distribution': {},
                'multi_edp_companies': 0
            }
            
            # Count tiers
            for company in tier_counts.data:
                tier = company.get('tam_tier', 'UNKNOWN')
                summary['tier_distribution'][tier] = summary['tier_distribution'].get(tier, 0) + 1
            
            # Count EDPs
            for company in edp_counts.data:
                tags = company.get('edp_tags', [])
                if len(tags) > 1:
                    summary['multi_edp_companies'] += 1
                for tag in tags:
                    summary['edp_distribution'][tag] = summary['edp_distribution'].get(tag, 0) + 1
            
            return summary
            
        except Exception as e:
            logger.error(f"Error getting TAM summary: {e}")
            return {}
```

### supercat_automation/config/credentials.py
```python

```

### supercat_automation/config/__init__.py
```python

```

### supercat_automation/config/settings.py
```python
# config/settings.py
"""
Complete and merged configuration for SuperCat GTM Automation.
Combines detailed application logic with enhanced scraper settings.
"""

import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """Centralized configuration using Pydantic for validation"""

    # --- Core API Keys (Required) ---
    supabase_url: str = Field(..., env='SUPABASE_URL')
    supabase_key: str = Field(..., env='SUPABASE_KEY')
    openai_api_key: str = Field(..., env='OPENAI_API_KEY')
    
    # --- Clay Configuration (Optional) ---
    clay_webhook_url: str = Field(default="https://api.clay.com/webhook/placeholder", env='CLAY_WEBHOOK_URL')
    clay_api_key: Optional[str] = Field(default=None, env='CLAY_API_KEY')
    clay_table_id: Optional[str] = Field(default=None, env='CLAY_TABLE_ID')

    # --- ENHANCED SCRAPER SETTINGS (Required for Scraping) ---
    twocaptcha_api_key: Optional[str] = Field(default=None, env='TWOCAPTCHA_API_KEY')
    BRIGHT_DATA_WSS_URL: Optional[str] = Field(default=None, env='BRIGHT_DATA_WSS_URL')
    use_proxies: bool = Field(default=False, env='USE_PROXIES')
    proxy_list: List[str] = Field(default_factory=list, env='PROXY_LIST')

    # --- Application Settings ---
    environment: str = Field(default='development', env='ENVIRONMENT')
    debug_mode: bool = Field(default=True, env='DEBUG_MODE')
    log_level: str = Field(default='INFO', env='LOG_LEVEL')
    openai_model: str = Field(default='gpt-4-turbo-preview', env='OPENAI_MODEL')
    
    # --- Rate Limiting ---
    max_daily_enrichments: int = Field(default=500, env='MAX_DAILY_ENRICHMENTS')
    max_concurrent_scrapers: int = Field(default=3, env='MAX_CONCURRENT_SCRAPERS')
    
    # --- Static Application Logic Configuration ---
    # Trade Show Configuration
    trade_shows_config: Dict[str, Any] = {
        'las_vegas_market': {
            'name': 'Las Vegas Market',
            'url': 'https://www.lasvegasmarket.com',
            'exhibitor_url': 'https://www.lasvegasmarket.com/exhibitors',
            'schedule': 'quarterly',
            'next_date': '2025-01-26'
        },
        'high_point_market': {
            'name': 'High Point Market',
            'url': 'https://www.highpointmarket.org',
            'exhibitor_url': 'https://www.highpointmarket.org/exhibitors',
            'schedule': 'bi-annual',
            'next_date': '2025-04-26'
        },
        'americasmart': {
            'name': 'AmericasMart Atlanta',
            'url': 'https://www.americasmart.com',
            'exhibitor_url': 'https://www.americasmart.com/exhibitors',
            'schedule': 'monthly',
            'next_date': '2025-01-14'
        }
    }
    
    # Validated Pain Signals from Won Deals
    validated_pain_signals: Dict[str, Any] = {
        'sales_enablement_collapse': {
            'weight': 1.0,
            'keywords': ['manual', 'hours', 'spreadsheet', 'paper', 'trade show'],
            'threshold': 0.7
        },
        'technology_obsolescence': {
            'weight': 0.93,
            'keywords': ['old', 'legacy', 'CSV', 'FTP', 'outdated'],
            'threshold': 0.6
        },
        'rep_performance_crisis': {
            'weight': 0.71,
            'keywords': ['visibility', 'tracking', 'quota', 'adoption'],
            'threshold': 0.5
        },
        'sku_complexity': {
            'weight': 0.64,
            'keywords': ['SKUs', 'configurations', 'options', 'variants'],
            'threshold': 0.5
        }
    }
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'

# Initialize a single settings object for the application to import
settings = Settings()

```

### supercat_automation/tests/test_pain_detection.py
```python
# tests/test_pain_detection.py
"""
Test suite for pain detection
"""

import pytest
import asyncio
from analysis.pain_detector import MultiSourcePainDetector
from scrapers.website_evidence import WebsiteEvidenceExtractor

class TestPainDetection:
    
    @pytest.fixture
    def detector(self):
        return MultiSourcePainDetector()
    
    @pytest.fixture
    def test_company(self):
        return {
            'id': 'test_001',
            'company_name': 'Test Furniture Co',
            'domain': 'ashleyfurniture.com',
            'trade_shows': ['Vegas Market']
        }
    
    def test_analyze_company(self, detector, test_company):
        """Test company analysis"""
        result = detector.analyze_company(test_company)
        
        assert result is not None
        assert 'tam_tier' in result
        assert 'primary_edp' in result
        assert 'psi_score' in result
    
    def test_edp_detection(self, detector, test_company):
        """Test EDP detection"""
        result = detector.analyze_company(test_company)
        
        assert 'edp_scores' in result
        assert len(result['edp_tags']) > 0
    
    def test_tam_classification(self, detector, test_company):
        """Test TAM tier classification"""
        result = detector.analyze_company(test_company)
        
        valid_tiers = ['TIER_1_IMMEDIATE', 'TIER_2_QUARTERLY', 
                      'TIER_3_NURTURE', 'TIER_4_MONITOR']
        
        assert result['tam_tier'] in valid_tiers
```

### supercat_automation/dashboard/metrics.py
```python
# dashboard/metrics.py
"""
Metrics calculation for dashboard
"""

from typing import Dict, List, Any
from datetime import datetime, timedelta
from database.connection import db
import pandas as pd

class MetricsCalculator:
    def get_current_metrics(self) -> Dict:
        """Get current metrics for dashboard"""
        
        # Get data from last 30 days
        cutoff = (datetime.now() - timedelta(days=30)).isoformat()
        
        # Companies analyzed
        companies = db.client.table('companies').select('*').gte(
            'created_at', cutoff
        ).execute()
        
        # Campaigns
        campaigns = db.client.table('campaigns').select('*').gte(
            'created_at', cutoff
        ).execute()
        
        # Calculate metrics
        total_companies = len(companies.data) if companies.data else 0
        
        qualified = sum(1 for c in companies.data 
                       if c.get('tam_tier') in ['TIER_1_IMMEDIATE', 'TIER_2_QUARTERLY'])
        
        active_campaigns = sum(1 for c in campaigns.data 
                              if c.get('campaign_status') == 'active')
        
        # Mock response rate (you'd calculate from real data)
        response_rate = 12.5
        
        return {
            'companies_analyzed': total_companies,
            'companies_delta': '+23',
            'qualified_companies': qualified,
            'qualified_delta': '+5',
            'active_campaigns': active_campaigns,
            'campaigns_delta': '+3',
            'response_rate': response_rate,
            'response_delta': 2.3
        }
    
    def get_hot_prospects(self) -> List[Dict]:
        """Get tier 1 prospects"""
        result = db.client.table('companies').select('*').eq(
            'tam_tier', 'TIER_1_IMMEDIATE'
        ).order('psi_score', desc=True).limit(10).execute()
        
        return result.data if result.data else []
    
    def get_active_campaigns(self) -> List[Dict]:
        """Get active campaigns with company info"""
        result = db.client.table('campaigns').select(
            '*, companies(company_name, domain)'
        ).eq('campaign_status', 'active').execute()
        
        return result.data if result.data else []
    
    def get_recent_activities(self) -> List[Dict]:
        """Get recent system activities"""
        # This would pull from an activity log table
        # For now, return mock data
        return [
            {
                'timestamp': '2 hours ago',
                'type': 'analysis',
                'company_name': 'Ashley Furniture',
                'tier': 'TIER_1_IMMEDIATE'
            },
            {
                'timestamp': '3 hours ago',
                'type': 'campaign',
                'company_name': 'Hooker Furniture'
            }
        ]
```

### supercat_automation/dashboard/__init__.py
```python

```

### supercat_automation/dashboard/visualizations.py
```python
# dashboard/visualizations.py
"""
Chart generation for dashboard
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from database.connection import db

class ChartGenerator:
    def create_tam_distribution(self):
        """Create TAM tier distribution pie chart"""
        
        # Get tier distribution
        companies = db.client.table('companies').select('tam_tier').execute()
        
        if companies.data:
            df = pd.DataFrame(companies.data)
            tier_counts = df['tam_tier'].value_counts()
            
            fig = px.pie(
                values=tier_counts.values,
                names=tier_counts.index,
                color_discrete_map={
                    'TIER_1_IMMEDIATE': '#FF4444',
                    'TIER_2_QUARTERLY': '#FFA500',
                    'TIER_3_NURTURE': '#4169E1',
                    'TIER_4_MONITOR': '#808080'
                }
            )
            
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=300)
            
            return fig
        
        return go.Figure()
    
    def create_pain_distribution(self):
        """Create pain signal distribution bar chart"""
        
        # Get EDP distribution
        companies = db.client.table('companies').select('primary_edp').execute()
        
        if companies.data:
            df = pd.DataFrame(companies.data)
            edp_counts = df['primary_edp'].value_counts()
            
            # Clean labels
            edp_counts.index = [x.replace('_', ' ').title() for x in edp_counts.index]
            
            fig = px.bar(
                x=edp_counts.values,
                y=edp_counts.index,
                orientation='h',
                color=edp_counts.values,
                color_continuous_scale='Reds'
            )
            
            fig.update_layout(
                height=300,
                showlegend=False,
                xaxis_title="Count",
                yaxis_title=""
            )
            
            return fig
        
        return go.Figure()
    
    def create_pipeline_chart(self):
        """Create pipeline velocity funnel"""
        
        stages = ['Identified', 'Analyzed', 'Qualified', 'Campaign Created', 'Outreach Sent', 'Response']
        values = [150, 120, 45, 38, 35, 8]  # Mock data
        
        fig = go.Figure(go.Funnel(
            y=stages,
            x=values,
            textinfo="value+percent initial"
        ))
        
        fig.update_layout(height=300)
        
        return fig
    
    def create_campaign_performance(self):
        """Create campaign performance metrics"""
        
        # Mock data - you'd pull from real campaign metrics
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        sent = [20, 22, 25, 23, 28, 30, 32, 35, 33, 38, 40, 42, 45, 43, 48,
                50, 52, 55, 53, 58, 60, 62, 65, 63, 68, 70, 72, 75, 73, 78]
        
        responses = [2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8,
                     8, 9, 9, 9, 10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=sent,
            mode='lines',
            name='Outreach Sent',
            line=dict(color='blue', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=responses,
            mode='lines',
            name='Responses',
            line=dict(color='green', width=2)
        ))
        
        fig.update_layout(
            height=300,
            xaxis_title="Date",
            yaxis_title="Count",
            hovermode='x unified'
        )
        
        return fig
```

### supercat_automation/dashboard/app.py
```python
# dashboard/app.py
"""
Streamlit dashboard for SuperCat GTM monitoring
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from database.connection import db
from dashboard.metrics import MetricsCalculator
from dashboard.visualizations import ChartGenerator

st.set_page_config(
    page_title="SuperCat GTM Dashboard",
    page_icon="🚀",
    layout="wide"
)

class SupercatDashboard:
    def __init__(self):
        self.metrics_calc = MetricsCalculator()
        self.chart_gen = ChartGenerator()
    
    def run(self):
        st.title("🚀 SuperCat GTM Automation Dashboard")
        
        # Sidebar
        with st.sidebar:
            st.header("Controls")
            date_range = st.date_input(
                "Date Range",
                value=(datetime.now() - timedelta(days=30), datetime.now()),
                max_value=datetime.now()
            )
            
            refresh = st.button("🔄 Refresh Data")
        
        # Main metrics row
        col1, col2, col3, col4 = st.columns(4)
        
        metrics = self.metrics_calc.get_current_metrics()
        
        with col1:
            st.metric(
                "Companies Analyzed",
                metrics['companies_analyzed'],
                delta=metrics.get('companies_delta')
            )
        
        with col2:
            st.metric(
                "Qualified (T1/T2)",
                metrics['qualified_companies'],
                delta=metrics.get('qualified_delta')
            )
        
        with col3:
            st.metric(
                "Campaigns Active",
                metrics['active_campaigns'],
                delta=metrics.get('campaigns_delta')
            )
        
        with col4:
            st.metric(
                "Response Rate",
                f"{metrics['response_rate']:.1f}%",
                delta=f"{metrics.get('response_delta', 0):.1f}%"
            )
        
        # Charts row 1
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 TAM Distribution")
            tam_chart = self.chart_gen.create_tam_distribution()
            st.plotly_chart(tam_chart, use_container_width=True)
        
        with col2:
            st.subheader("💔 Pain Signal Distribution")
            pain_chart = self.chart_gen.create_pain_distribution()
            st.plotly_chart(pain_chart, use_container_width=True)
        
        # Charts row 2
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Pipeline Velocity")
            pipeline_chart = self.chart_gen.create_pipeline_chart()
            st.plotly_chart(pipeline_chart, use_container_width=True)
        
        with col2:
            st.subheader("🎯 Campaign Performance")
            campaign_chart = self.chart_gen.create_campaign_performance()
            st.plotly_chart(campaign_chart, use_container_width=True)
        
        # Detailed tables
        st.header("📋 Detailed Views")
        
        tab1, tab2, tab3 = st.tabs(["Hot Prospects", "Active Campaigns", "Recent Activity"])
        
        with tab1:
            self.show_hot_prospects()
        
        with tab2:
            self.show_active_campaigns()
        
        with tab3:
            self.show_recent_activity()
    
    def show_hot_prospects(self):
        """Show tier 1 prospects table"""
        prospects = self.metrics_calc.get_hot_prospects()
        
        if prospects:
            df = pd.DataFrame(prospects)
            
            # Format columns
            column_config = {
                "company_name": "Company",
                "psi_score": st.column_config.ProgressColumn(
                    "Pain Score",
                    min_value=0,
                    max_value=100,
                ),
                "primary_edp": "Primary Pain",
                "trade_shows": "Trade Shows",
                "action": st.column_config.LinkColumn("Action")
            }
            
            st.dataframe(
                df,
                column_config=column_config,
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("No hot prospects found. Run analysis to identify opportunities.")
    
    def show_active_campaigns(self):
        """Show active campaigns"""
        campaigns = self.metrics_calc.get_active_campaigns()
        
        if campaigns:
            df = pd.DataFrame(campaigns)
            
            st.dataframe(
                df,
                hide_index=True,
                use_container_width=True
            )
            
            # Campaign actions
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📤 Send to Clay"):
                    st.success("Campaigns sent to Clay webhook!")
            
            with col2:
                if st.button("⏸️ Pause Selected"):
                    st.info("Selected campaigns paused")
            
            with col3:
                if st.button("📊 Export Report"):
                    st.download_button(
                        label="Download CSV",
                        data=df.to_csv(index=False),
                        file_name=f"campaigns_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
        else:
            st.info("No active campaigns. Generate campaigns for qualified companies.")
    
    def show_recent_activity(self):
        """Show recent system activity"""
        activities = self.metrics_calc.get_recent_activities()
        
        for activity in activities:
            with st.container():
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    st.write(activity['timestamp'])
                
                with col2:
                    if activity['type'] == 'analysis':
                        st.success(f"✅ Analyzed {activity['company_name']} - Tier: {activity['tier']}")
                    elif activity['type'] == 'campaign':
                        st.info(f"📧 Campaign created for {activity['company_name']}")
                    elif activity['type'] == 'outreach':
                        st.warning(f"🚀 Outreach sent to {activity['contact_name']}")

if __name__ == "__main__":
    dashboard = SupercatDashboard()
    dashboard.run()
```

### supercat_automation/orchestration/message_preparation.py
```python
# orchestration/message_preparation.py
"""
Prepare complete campaign messages before sending to Clay
"""

from generation.evidence_based_messages import EvidenceBasedMessageGenerator
from analysis.pain_detector import MultiSourcePainDetector
from typing import Dict

class CampaignPreparer:
    def __init__(self):
        self.message_generator = EvidenceBasedMessageGenerator()
        self.pain_detector = MultiSourcePainDetector()
    
    def prepare_campaign_for_clay(self, company_data: Dict) -> Dict:
        """
        Complete all analysis and message generation BEFORE Clay
        """
        
        # 1. Run pain analysis
        pain_analysis = self.pain_detector.analyze_company(company_data)
        
        # 2. Determine target persona based on EDP
        target_persona = self.determine_persona(pain_analysis)
        
        # 3. Generate complete email sequence
        email_sequence = self.message_generator.generate_email_sequence(
            company_data, 
            pain_analysis['primary_edp']
        )
        
        # 4. Generate LinkedIn messages
        linkedin_sequence = self.message_generator.generate_linkedin_messages(
            company_data,
            pain_analysis['primary_edp']
        )
        
        # 5. Package everything for Clay
        clay_payload = {
            # Company data
            "company_id": company_data['id'],
            "company_name": company_data['company_name'],
            "domain": company_data['domain'],
            
            # Tell Clay what personas to find
            "find_decision_makers": {
                "persona_type": target_persona,
                "backup_persona": self.get_backup_persona(target_persona),
                "reason": f"Primary EDP is {pain_analysis['primary_edp']}"
            },
            
            # Complete email sequence
            "email_sequence": email_sequence,
            
            # Complete LinkedIn sequence
            "linkedin_sequence": linkedin_sequence,
            
            # Campaign metadata
            "campaign_strategy": self.determine_strategy(pain_analysis),
            "primary_edp": pain_analysis['primary_edp'],
            "psi_score": pain_analysis['psi_score'],
            "tam_tier": pain_analysis['tam_tier'],
            
            # Urgency factors
            "days_until_show": self.calculate_trade_show_urgency(company_data),
            "urgency_level": "high" if pain_analysis['tam_tier'] == 'TIER_1_IMMEDIATE' else 'medium'
        }
        
        return clay_payload
    
    def determine_persona(self, pain_analysis: Dict) -> str:
        """
        Determine which persona to target based on pain
        """
        edp = pain_analysis['primary_edp']
        
        persona_map = {
            'sales_enablement_collapse': 'sales_leadership',
            'technology_obsolescence': 'it_operations',
            'rep_performance_crisis': 'sales_leadership',
            'sku_complexity': 'it_operations',
            'channel_conflict': 'sales_leadership'
        }
        
        return persona_map.get(edp, 'c_suite')
    
    def get_backup_persona(self, primary: str) -> str:
        """Get backup persona if primary not found"""
        backup_map = {
            'sales_leadership': 'c_suite',
            'it_operations': 'c_suite',
            'c_suite': 'sales_leadership'
        }
        return backup_map.get(primary, 'c_suite')
```

### supercat_automation/orchestration/upload_pipeline.py
```python
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
```

### supercat_automation/orchestration/__init__.py
```python

```

### supercat_automation/orchestration/scheduling.py
```python

```

### supercat_automation/orchestration/campaign_coordinator.py
```python
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
```

### supercat_automation/orchestration/clay_webhook.py
```python
# orchestration/clay_webhook_complete.py
"""
Complete Clay webhook with PVP messages AND ad copy
"""

import logging
import json
import time
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import requests

from config.settings import settings
from database.connection import db
from generation.pvp_message_generator import PVPMessageGenerator
from generation.pvp_ad_generator import PVPAdGenerator

logger = logging.getLogger(__name__)

class CompleteClayWebhookOrchestrator:
    def __init__(self):
        self.pvp_message_generator = PVPMessageGenerator()
        self.pvp_ad_generator = PVPAdGenerator()
        # ... existing init ...
    
    def prepare_complete_payload(self, outreach_data: Dict) -> Dict:
        """
        Prepare COMPLETE payload with PVP messages AND comprehensive ad copy
        """
        
        company = outreach_data.get('company', {})
        
        # Build analysis object
        analysis = {
            'company_id': company.get('id'),
            'company_name': company.get('company_name'),
            'domain': company.get('domain'),
            'primary_edp': company.get('primary_edp'),
            'tam_tier': company.get('tam_tier'),
            'evidence': {
                'website': company.get('website_evidence', {}),
                'trade_show': {'shows': company.get('trade_shows', [])}
            },
            'employee_count': company.get('employee_count'),
            'catalog_sku_count': company.get('catalog_sku_count')
        }
        
        # Extract evidence
        evidence = self.pvp_message_generator._extract_all_evidence(analysis)
        
        # Check if we have sufficient evidence
        if not evidence['has_sufficient_evidence']:
            logger.warning(f"Insufficient evidence for {company.get('company_name')}")
            self._trigger_additional_research(company)
            return None
        
        # Generate PVP email campaign
        pvp_campaign = self.pvp_message_generator.generate_pvp_campaign(analysis)
        
        # Generate complete ad campaign
        ad_campaign = self.pvp_ad_generator.generate_full_ad_campaign(analysis, evidence)
        
        # Build comprehensive payload for Clay
        payload = {
            'table_id': self.table_id,
            'data': {
                # === COMPANY INFORMATION ===
                'company_name': company.get('company_name'),
                'company_domain': company.get('domain'),
                'company_id': company.get('id'),
                
                # === ANALYSIS & SCORING ===
                'tam_tier': analysis['tam_tier'],
                'primary_edp': analysis['primary_edp'],
                'psi_score': company.get('psi_score'),
                'evidence_used': json.dumps(evidence),
                'personalization_score': pvp_campaign.get('quality_score'),
                
                # === PVP EMAIL SEQUENCE ===
                'email_sequence': json.dumps(pvp_campaign.get('email_sequence', [])),
                'email_quality_score': pvp_campaign.get('quality_score'),
                
                # === PVP LINKEDIN MESSAGES ===
                'linkedin_messages': json.dumps(pvp_campaign.get('linkedin_messages', [])),
                
                # === GOOGLE ADS ===
                'google_ads_headlines': json.dumps(ad_campaign['google_ads']['ad_groups'][0]['headlines']),
                'google_ads_descriptions': json.dumps(ad_campaign['google_ads']['ad_groups'][0]['descriptions']),
                'google_ads_keywords': json.dumps(ad_campaign['google_ads']['ad_groups'][0]['keywords']),
                'google_ads_final_url': ad_campaign['google_ads']['ad_groups'][0]['final_url'],
                'google_ads_extensions': json.dumps(ad_campaign['google_ads']['extensions']),
                
                # === META ADS (FACEBOOK/INSTAGRAM) ===
                'meta_ads_primary_text': ad_campaign['meta_ads']['creatives'][0]['primary_text'],
                'meta_ads_headline': ad_campaign['meta_ads']['creatives'][0]['headline'],
                'meta_ads_description': ad_campaign['meta_ads']['creatives'][0]['description'],
                'meta_ads_carousel': json.dumps(ad_campaign['meta_ads']['creatives'][1]['cards']),
                'meta_ads_video_script': json.dumps(ad_campaign['meta_ads']['creatives'][2]['video_script']),
                'meta_ads_targeting': json.dumps(ad_campaign['meta_ads']['ad_sets'][0]['targeting']),
                
                # === LINKEDIN ADS ===
                'linkedin_ads_intro': ad_campaign['linkedin_ads']['formats'][0]['intro_text'],
                'linkedin_ads_headline': ad_campaign['linkedin_ads']['formats'][0]['headline'],
                'linkedin_ads_conversation': json.dumps(ad_campaign['linkedin_ads']['formats'][1]),
                'linkedin_ads_targeting': json.dumps(ad_campaign['linkedin_ads']['targeting']),
                'linkedin_lead_form': json.dumps(ad_campaign['linkedin_ads']['lead_gen_form']),
                
                # === DISPLAY/BANNER ADS ===
                'display_ads_messages': json.dumps(ad_campaign['display_ads']['ad_sizes']),
                'display_ads_targeting': json.dumps(ad_campaign['display_ads']['targeting']),
                
                # === RETARGETING SEQUENCES ===
                'retargeting_sequences': json.dumps(ad_campaign['retargeting']['sequences']),
                
                # === BUDGET RECOMMENDATIONS ===
                'recommended_budgets': json.dumps({
                    'google': ad_campaign['google_ads']['budget'],
                    'meta': ad_campaign['meta_ads']['ad_sets'][0]['budget'],
                    'linkedin': ad_campaign['linkedin_ads']['budget']
                }),
                
                # === TRACKING & ATTRIBUTION ===
                'tracking_parameters': json.dumps({
                    'utm_source': '{platform}',
                    'utm_medium': '{ad_type}',
                    'utm_campaign': f"pvp_{company.get('company_name', '').lower().replace(' ', '_')}",
                    'utm_content': '{creative_variant}',
                    'utm_term': '{keyword}'
                }),
                
                # === QUALITY CONTROL ===
                'requires_human_review': pvp_campaign.get('quality_score', 0) < 0.7,
                'message_quality_score': pvp_campaign.get('quality_score'),
                'evidence_completeness': len(evidence['website_findings']) + len(evidence['personalization_hooks']),
                
                # === METADATA ===
                'created_at': datetime.now().isoformat(),
                'campaign_type': 'pvp_multi_channel',
                'source': 'supercat_automation_v2'
            }
        }
        
        return payload
    
    def send_to_clay_with_validation(self, outreach_data: Dict) -> Dict:
        """
        Send to Clay with validation and quality checks
        """
        
        # Prepare complete payload
        payload = self.prepare_complete_payload(outreach_data)
        
        if not payload:
            return {
                'success': False,
                'reason': 'Insufficient evidence for PVP campaign'
            }
        
        # Quality validation
        quality_score = payload['data'].get('message_quality_score', 0)
        
        if quality_score < 0.5:
            logger.warning(f"Low quality score ({quality_score}) for {payload['data']['company_name']}")
            # Trigger manual review
            self._flag_for_review(payload)
            return {
                'success': False,
                'reason': 'Quality score too low, flagged for review'
            }
        
        # Send to Clay
        try:
            response = requests.post(
                self.webhook_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                logger.info(f"✅ Complete campaign sent to Clay: {payload['data']['company_name']}")
                
                # Log what was sent
                self._log_campaign_details(payload)
                
                return {
                    'success': True,
                    'clay_response': response.json(),
                    'campaign_components': {
                        'emails': len(json.loads(payload['data']['email_sequence'])),
                        'linkedin_messages': len(json.loads(payload['data']['linkedin_messages'])),
                        'google_ads': len(json.loads(payload['data']['google_ads_headlines'])),
                        'meta_ads': len(json.loads(payload['data']['meta_ads_carousel'])),
                        'display_ads': len(json.loads(payload['data']['display_ads_messages']))
                    }
                }
            else:
                logger.error(f"Clay webhook failed: {response.status_code}")
                return {
                    'success': False,
                    'error': response.text
                }
                
        except Exception as e:
            logger.error(f"Error sending to Clay: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _log_campaign_details(self, payload: Dict):
        """
        Log details of what was sent for tracking
        """
        
        company_name = payload['data']['company_name']
        
        logger.info(f"""
        ==========================================
        CAMPAIGN SENT FOR: {company_name}
        ==========================================
        TAM Tier: {payload['data']['tam_tier']}
        Primary EDP: {payload['data']['primary_edp']}
        PSI Score: {payload['data']['psi_score']}
        Quality Score: {payload['data']['message_quality_score']}
        
        Components Included:
        - Email Sequences: ✅
        - LinkedIn Messages: ✅
        - Google Ads: ✅
        - Meta Ads: ✅
        - LinkedIn Ads: ✅
        - Display Ads: ✅
        - Retargeting: ✅
        
        Evidence Used: {payload['data']['evidence_completeness']} data points
        ==========================================
        """)
    
    def _trigger_additional_research(self, company: Dict):
        """
        Trigger deeper research workflow when evidence insufficient
        """
        
        logger.info(f"Triggering additional research for {company['company_name']}")
        
        # Queue for deeper website analysis
        # Queue for LinkedIn research
        # Queue for trade show booth research
        # Queue for competitive intelligence
        
        # This would integrate with your research pipeline
        pass
    
    def _flag_for_review(self, payload: Dict):
        """
        Flag low-quality campaigns for human review
        """
        
        # Save to review queue
        review_record = {
            'company_name': payload['data']['company_name'],
            'quality_score': payload['data']['message_quality_score'],
            'reason': 'Low quality score',
            'payload': payload,
            'flagged_at': datetime.now().isoformat()
        }
        
        # This would save to your review queue
        db.client.table('review_queue').insert(review_record).execute()
```

### supercat_automation/enrichment/company_enricher.py
```python

```

### supercat_automation/enrichment/__init__.py
```python

```

### supercat_automation/enrichment/clay_integration.py
```python

```

### supercat_automation/scrapers/high_point.py
```python
# scrapers/high_point.py
"""
Scraper for High Point Market trade show.
Enhanced version with robust loading strategies and multiple fallback approaches.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import asyncio
import random
import re
from bs4 import BeautifulSoup, Tag
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError
from .base_scraper import BaseTradeshowScraper

logger = logging.getLogger(__name__)

class HighPointMarketScraper(BaseTradeshowScraper):
    """Enhanced scraper for High Point Market with multiple strategies."""

    def __init__(self):
        super().__init__(
            trade_show_name="High Point Market",
            base_url="https://www.highpointmarket.org"
        )
        self.exhibitor_list_url = f"{self.base_url}/exhibitor"
        self.exhibitors_collected = set()  # Track unique exhibitors

    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape High Point Market general information."""
        try:
            logger.info(f"Navigating to High Point Market homepage: {self.base_url}")
            await page.goto(self.base_url, timeout=90000)
            await page.wait_for_load_state('networkidle')
            
            # Try to extract actual dates from the page
            date_info = await self._extract_show_dates(page)
            
            return {
                'name': 'High Point Market',
                'location': 'High Point, NC',
                'venue': 'High Point Market Authority',
                'start_date': date_info.get('start_date', '2025-04-26'),  # Spring 2025 market
                'end_date': date_info.get('end_date', '2025-04-30'),
                'industry': 'Furniture, Home Decor, Lighting',
                'estimated_attendance': 75000,
                'website_url': self.base_url,
                'exhibitor_list_url': self.exhibitor_list_url,
                'last_scraped': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error scraping trade show info: {e}")
            return self._get_default_show_info()

    async def scrape_exhibitor_list(self, page: Page) -> List[Dict[str, Any]]:
        """Enhanced exhibitor scraping with multiple strategies."""
        exhibitors = []
        
        try:
            logger.info(f"Navigating to exhibitor directory: {self.exhibitor_list_url}")
            
            # Navigate with extended timeout
            await page.goto(self.exhibitor_list_url, timeout=120000)
            await page.wait_for_load_state('networkidle')
            
            # Handle any popups or overlays
            await self._handle_overlays(page)
            
            # Wait for initial content to load
            await self._wait_for_exhibitor_content(page)
            
            # Strategy 1: Try to load all exhibitors using the Load More button
            await self._load_all_exhibitors(page)
            
            # Get the page content
            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            
            # Strategy 2: Find exhibitor elements using multiple selectors
            exhibitor_elements = self._find_all_exhibitor_elements(soup)
            logger.info(f"Found {len(exhibitor_elements)} potential exhibitor elements")
            
            # Parse each element
            for elem in exhibitor_elements:
                exhibitor = self._parse_exhibitor_comprehensive(elem)
                if exhibitor and exhibitor.get('company_name'):
                    # Avoid duplicates
                    company_key = exhibitor['company_name'].lower().strip()
                    if company_key not in self.exhibitors_collected:
                        self.exhibitors_collected.add(company_key)
                        exhibitors.append(exhibitor)
            
            logger.info(f"Successfully parsed {len(exhibitors)} unique exhibitors")
            
            # If we got very few results, try alternative strategies
            if len(exhibitors) < 50:
                logger.warning(f"Only found {len(exhibitors)} exhibitors, trying alternative methods...")
                additional = await self._try_alternative_strategies(page)
                for exhibitor in additional:
                    company_key = exhibitor['company_name'].lower().strip()
                    if company_key not in self.exhibitors_collected:
                        self.exhibitors_collected.add(company_key)
                        exhibitors.append(exhibitor)
                
                logger.info(f"Total exhibitors after alternative strategies: {len(exhibitors)}")
            
        except Exception as e:
            logger.error(f"Error in main scraping strategy: {e}")
            # Fallback to JavaScript extraction
            exhibitors = await self._javascript_extraction(page)
        
        return exhibitors

    async def _handle_overlays(self, page: Page):
        """Handle popups, cookie banners, and overlays."""
        overlay_selectors = [
            # Cookie consent
            "button#onetrust-accept-btn-handler",
            "button[id*='accept-cookies']",
            "button[class*='cookie-accept']",
            "button:has-text('Accept')",
            "button:has-text('I Agree')",
            
            # Newsletter/popup close buttons
            "button[aria-label='Close']",
            "button[class*='close']",
            "a[class*='close']",
            "div[class*='modal'] button[class*='close']",
            
            # Skip or dismiss buttons
            "button:has-text('Skip')",
            "button:has-text('No Thanks')",
            "button:has-text('Maybe Later')"
        ]
        
        for selector in overlay_selectors:
            try:
                elements = await page.locator(selector).all()
                for element in elements[:3]:  # Only try first 3 matches
                    if await element.is_visible():
                        await element.click()
                        logger.info(f"Clicked overlay element: {selector}")
                        await asyncio.sleep(1)
            except:
                continue

    async def _wait_for_exhibitor_content(self, page: Page):
        """Wait for exhibitor content to load using multiple strategies."""
        content_selectors = [
            # Known High Point selectors
            "div.exhibitors-list",
            "div.exhibitor-tile",
            "div[class*='exhibitor-card']",
            "article[class*='exhibitor']",
            
            # Generic patterns
            "div[class*='directory']",
            "div[class*='listing']",
            "div[class*='vendor']",
            "div[class*='company-card']",
            
            # Data attributes
            "[data-exhibitor]",
            "[data-vendor]",
            "[data-company]"
        ]
        
        for selector in content_selectors:
            try:
                await page.wait_for_selector(selector, timeout=10000)
                logger.info(f"Found content with selector: {selector}")
                return
            except:
                continue
        
        # If no specific selector worked, wait a bit for any content
        logger.warning("Could not find specific exhibitor content, waiting for general content...")
        await asyncio.sleep(5)

    async def _load_all_exhibitors(self, page: Page):
        """Load all exhibitors using various loading strategies."""
        logger.info("Starting to load all exhibitors...")
        
        # Strategy 1: Click Load More button repeatedly
        load_more_count = await self._click_load_more_buttons(page)
        
        # Strategy 2: Scroll to load lazy-loaded content
        if load_more_count < 5:  # If we didn't find many load more buttons, try scrolling
            await self._infinite_scroll(page)
        
        # Strategy 3: Check for pagination
        await self._handle_pagination(page)

    async def _click_load_more_buttons(self, page: Page) -> int:
        """Click all variations of load more buttons."""
        load_more_selectors = [
            "button.exhibitors-load-more-button",
            "button:has-text('Load More')",
            "button:has-text('Show More')",
            "button:has-text('View More')",
            "a:has-text('Load More')",
            "button[class*='load-more']",
            "button[class*='show-more']",
            "div[class*='load-more'] button",
            "[data-action='load-more']"
        ]
        
        clicks = 0
        max_clicks = 50
        
        for selector in load_more_selectors:
            consecutive_failures = 0
            
            while clicks < max_clicks and consecutive_failures < 3:
                try:
                    button = page.locator(selector).first
                    
                    # Check if button exists and is visible
                    if await button.count() > 0 and await button.is_visible():
                        # Scroll button into view
                        await button.scroll_into_view_if_needed()
                        await asyncio.sleep(0.5)
                        
                        # Click the button
                        await button.click()
                        clicks += 1
                        consecutive_failures = 0
                        
                        logger.info(f"Clicked '{selector}' button (total clicks: {clicks})")
                        
                        # Wait for new content to load
                        await asyncio.sleep(random.uniform(2.0, 4.0))
                    else:
                        consecutive_failures += 1
                        
                except Exception as e:
                    consecutive_failures += 1
                    if consecutive_failures == 1:
                        logger.debug(f"Could not click {selector}: {e}")
        
        logger.info(f"Total load more clicks: {clicks}")
        return clicks

    async def _infinite_scroll(self, page: Page):
        """Perform infinite scrolling to load content."""
        logger.info("Starting infinite scroll...")
        
        last_height = await page.evaluate("document.body.scrollHeight")
        same_height_count = 0
        max_scrolls = 30
        
        for i in range(max_scrolls):
            # Scroll to bottom
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            
            # Wait for content to load
            await asyncio.sleep(random.uniform(2.0, 4.0))
            
            # Check new height
            new_height = await page.evaluate("document.body.scrollHeight")
            
            if new_height == last_height:
                same_height_count += 1
                if same_height_count >= 3:
                    logger.info("Page height unchanged for 3 iterations, stopping scroll")
                    break
            else:
                same_height_count = 0
                logger.info(f"Scroll {i+1}: Height increased from {last_height} to {new_height}")
            
            last_height = new_height
            
            # Also try clicking load more during scroll
            try:
                load_more = page.locator("button:has-text('Load More')").first
                if await load_more.is_visible():
                    await load_more.click()
                    await asyncio.sleep(3)
            except:
                pass

    async def _handle_pagination(self, page: Page):
        """Handle pagination if present."""
        pagination_selectors = [
            "a[class*='pagination']",
            "button[class*='page-next']",
            "a:has-text('Next')",
            "button:has-text('Next')",
            "[aria-label='Next page']"
        ]
        
        pages_loaded = 0
        max_pages = 10
        
        for selector in pagination_selectors:
            while pages_loaded < max_pages:
                try:
                    next_button = page.locator(selector).first
                    if await next_button.is_visible():
                        await next_button.click()
                        pages_loaded += 1
                        logger.info(f"Navigated to page {pages_loaded + 1}")
                        await asyncio.sleep(3)
                    else:
                        break
                except:
                    break

    def _find_all_exhibitor_elements(self, soup: BeautifulSoup) -> List[Tag]:
        """Find exhibitor elements using comprehensive selectors."""
        all_elements = []
        seen_texts = set()
        
        # High Point specific selectors
        selectors = [
            "div.exhibitor-tile",
            "div.exhibitor-card",
            "article.exhibitor",
            "div[class*='exhibitor-item']",
            "div[class*='vendor-card']",
            "div[class*='company-listing']"
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for elem in elements:
                # Check for unique content to avoid duplicates
                text_content = elem.get_text(strip=True)[:100]  # First 100 chars as key
                if text_content and text_content not in seen_texts:
                    seen_texts.add(text_content)
                    all_elements.append(elem)
        
        # Also look for generic patterns
        generic_patterns = [
            {"name": "div", "class": re.compile(r"exhibitor|vendor|company|listing", re.I)},
            {"name": "article", "class": re.compile(r"card|item|tile", re.I)},
            {"name": "li", "class": re.compile(r"exhibitor|vendor|company", re.I)}
        ]
        
        for pattern in generic_patterns:
            elements = soup.find_all(**pattern)
            for elem in elements:
                text_content = elem.get_text(strip=True)[:100]
                if text_content and text_content not in seen_texts:
                    # Verify it looks like an exhibitor (has a name-like element)
                    if elem.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong']):
                        seen_texts.add(text_content)
                        all_elements.append(elem)
        
        logger.info(f"Found {len(all_elements)} unique potential exhibitor elements")
        return all_elements

    def _parse_exhibitor_comprehensive(self, element: Tag) -> Optional[Dict[str, Any]]:
        """Parse exhibitor with multiple extraction strategies."""
        try:
            exhibitor_data = {}
            
            # Extract company name (multiple strategies)
            company_name = self._extract_company_name(element)
            if not company_name:
                return None
            
            exhibitor_data['company_name'] = company_name
            
            # Extract website
            website = self._extract_website(element)
            if website:
                exhibitor_data['website'] = website
            
            # Extract booth information
            booth_info = self._extract_booth_info(element)
            if booth_info:
                exhibitor_data.update(booth_info)
            
            # Extract contact information
            contact_info = self._extract_contact_info(element)
            if contact_info:
                exhibitor_data.update(contact_info)
            
            # Extract categories/products
            categories = self._extract_categories(element)
            if categories:
                exhibitor_data['categories'] = categories
            
            return exhibitor_data
            
        except Exception as e:
            logger.debug(f"Error parsing exhibitor element: {e}")
            return None

    def _extract_company_name(self, element: Tag) -> Optional[str]:
        """Extract company name using multiple strategies."""
        # Strategy 1: Look in headings
        for heading_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            heading = element.find(heading_tag)
            if heading:
                # Get text, excluding nested elements
                name = heading.get_text(strip=True)
                if name and len(name) > 2:
                    return name
        
        # Strategy 2: Look for specific classes
        name_classes = ['exhibitor-name', 'company-name', 'vendor-name', 'title', 'name']
        for class_name in name_classes:
            name_elem = element.find(class_=re.compile(class_name, re.I))
            if name_elem:
                name = name_elem.get_text(strip=True)
                if name and len(name) > 2:
                    return name
        
        # Strategy 3: Look in links
        link = element.find('a', class_=re.compile(r'name|title', re.I))
        if link:
            name = link.get_text(strip=True)
            if name and len(name) > 2:
                return name
        
        # Strategy 4: Look for strong/bold text
        strong = element.find(['strong', 'b'])
        if strong:
            name = strong.get_text(strip=True)
            if name and len(name) > 2 and not any(skip in name.lower() for skip in ['booth', 'location', 'phone']):
                return name
        
        return None

    def _extract_website(self, element: Tag) -> Optional[str]:
        """Extract website URL."""
        # Look for external links
        for link in element.find_all('a', href=True):
            href = link['href']
            
            # Check if it's a website (not internal navigation)
            if href.startswith('http') and 'highpointmarket.org' not in href:
                return href
            elif href.startswith('www.'):
                return f"https://{href}"
            
            # Check for profile/detail links that might contain website info
            if '/exhibitor/' in href or '/vendor/' in href or '/company/' in href:
                # This might be a detail page, store it as a reference
                if href.startswith('/'):
                    return f"{self.base_url}{href}"
        
        return None

    def _extract_booth_info(self, element: Tag) -> Dict[str, Any]:
        """Extract booth number and location information."""
        booth_info = {}
        
        # Look for booth number
        booth_patterns = [
            r'(?:booth|space|stand)[\s:#]*([A-Z0-9\-]+)',
            r'([A-Z]+[\s\-]?\d+)',  # Common format like "C-1055" or "IHFC 209"
            r'(?:showroom|location)[\s:#]*([A-Z0-9\-]+)'
        ]
        
        text_content = element.get_text()
        
        for pattern in booth_patterns:
            match = re.search(pattern, text_content, re.IGNORECASE)
            if match:
                booth_info['booth_number'] = match.group(1).strip()
                break
        
        # Look for building/location
        building_patterns = [
            r'(?:building|hall|wing|floor)[\s:#]*([A-Z0-9\-]+)',
            r'(IHFC|Suites at Market Square|Plaza Suites|Showplace)',  # High Point specific
            r'(?:located in|location)[\s:#]*([^,\n]+)'
        ]
        
        for pattern in building_patterns:
            match = re.search(pattern, text_content, re.IGNORECASE)
            if match:
                booth_info['building'] = match.group(1).strip()
                break
        
        return booth_info

    def _extract_contact_info(self, element: Tag) -> Dict[str, Any]:
        """Extract contact information."""
        contact_info = {}
        
        # Phone number
        phone_pattern = r'(?:phone|tel|p)[\s:#]*\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}'
        phone_match = re.search(phone_pattern, element.get_text(), re.IGNORECASE)
        if phone_match:
            contact_info['phone'] = phone_match.group(0)
        
        # Email
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email_match = re.search(email_pattern, element.get_text())
        if email_match:
            contact_info['email'] = email_match.group(0)
        
        return contact_info

    def _extract_categories(self, element: Tag) -> Optional[str]:
        """Extract product categories."""
        category_indicators = ['category', 'categories', 'products', 'specialties', 'type']
        
        for indicator in category_indicators:
            cat_elem = element.find(class_=re.compile(indicator, re.I))
            if cat_elem:
                return cat_elem.get_text(strip=True)
        
        # Look for tags or labels
        tags = element.find_all(class_=re.compile(r'tag|label|badge', re.I))
        if tags:
            categories = [tag.get_text(strip=True) for tag in tags]
            return ', '.join(categories)
        
        return None

    async def _try_alternative_strategies(self, page: Page) -> List[Dict[str, Any]]:
        """Try alternative strategies if main approach fails."""
        exhibitors = []
        
        # Strategy 1: Look for links to exhibitor profiles
        profile_links = await page.evaluate("""
            () => {
                const links = Array.from(document.querySelectorAll('a[href*="/exhibitor/"], a[href*="/vendor/"], a[href*="/company/"]'));
                return links.map(link => ({
                    name: link.textContent.trim(),
                    url: link.href
                })).filter(item => item.name && item.name.length > 2);
            }
        """)
        
        for link_data in profile_links:
            if link_data['name']:
                exhibitors.append({
                    'company_name': link_data['name'],
                    'profile_url': link_data['url']
                })
        
        logger.info(f"Found {len(exhibitors)} exhibitors from profile links")
        
        return exhibitors

    async def _javascript_extraction(self, page: Page) -> List[Dict[str, Any]]:
        """Fallback JavaScript extraction method."""
        logger.info("Using JavaScript extraction as fallback...")
        
        try:
            exhibitors = await page.evaluate("""
                () => {
                    const results = [];
                    const processedNames = new Set();
                    
                    // Find all potential exhibitor containers
                    const containers = document.querySelectorAll(`
                        div[class*="exhibitor"],
                        div[class*="vendor"],
                        div[class*="company"],
                        article[class*="card"],
                        div[class*="tile"],
                        div[class*="listing"],
                        li[class*="exhibitor"]
                    `);
                    
                    containers.forEach(container => {
                        const data = {};
                        
                        // Find company name
                        const nameElement = container.querySelector('h1, h2, h3, h4, h5, h6, strong, .name, .title, a[class*="name"]');
                        if (nameElement) {
                            const name = nameElement.textContent.trim();
                            if (name && name.length > 2 && !processedNames.has(name.toLowerCase())) {
                                data.company_name = name;
                                processedNames.add(name.toLowerCase());
                                
                                // Find website
                                const linkElement = container.querySelector('a[href*="http"], a[href*="www"]');
                                if (linkElement) {
                                    data.website = linkElement.href;
                                }
                                
                                // Find booth number
                                const text = container.textContent;
                                const boothMatch = text.match(/(?:booth|space|stand)[:\s]*([A-Z0-9\-]+)/i);
                                if (boothMatch) {
                                    data.booth_number = boothMatch[1];
                                }
                                
                                // Find building
                                const buildingMatch = text.match(/(?:building|hall|IHFC|Suites|Plaza)[:\s]*([A-Z0-9\-\s]+)/i);
                                if (buildingMatch) {
                                    data.building = buildingMatch[1].trim();
                                }
                                
                                results.push(data);
                            }
                        }
                    });
                    
                    return results;
                }
            """)
            
            logger.info(f"JavaScript extraction found {len(exhibitors)} exhibitors")
            return exhibitors
            
        except Exception as e:
            logger.error(f"JavaScript extraction failed: {e}")
            return []

    async def _extract_show_dates(self, page: Page) -> Dict[str, str]:
        """Try to extract actual show dates from the page."""
        try:
            dates = await page.evaluate("""
                () => {
                    const text = document.body.innerText;
                    // Look for date patterns like "April 26-30, 2025"
                    const datePattern = /([A-Z][a-z]+)\s+(\d{1,2})[\-–]\s*(\d{1,2}),?\s+(\d{4})/i;
                    const match = text.match(datePattern);
                    
                    if (match) {
                        const month = match[1];
                        const startDay = match[2];
                        const endDay = match[3];
                        const year = match[4];
                        
                        // Convert month name to number
                        const months = {
                            'january': '01', 'february': '02', 'march': '03', 'april': '04',
                            'may': '05', 'june': '06', 'july': '07', 'august': '08',
                            'september': '09', 'october': '10', 'november': '11', 'december': '12'
                        };
                        
                        const monthNum = months[month.toLowerCase()] || '01';
                        
                        return {
                            start_date: `${year}-${monthNum}-${startDay.padStart(2, '0')}`,
                            end_date: `${year}-${monthNum}-${endDay.padStart(2, '0')}`
                        };
                    }
                    
                    return null;
                }
            """)
            
            if dates:
                return dates
                
        except:
            pass
        
        return {}

    def _get_default_show_info(self) -> Dict[str, Any]:
        """Return default show information as fallback."""
        return {
            'name': 'High Point Market',
            'location': 'High Point, NC',
            'venue': 'High Point Market Authority',
            'start_date': '2025-04-26',
            'end_date': '2025-04-30',
            'industry': 'Furniture, Home Decor, Lighting',
            'estimated_attendance': 75000,
            'website_url': self.base_url,
            'exhibitor_list_url': self.exhibitor_list_url,
            'last_scraped': datetime.now().isoformat()
        }
```

### supercat_automation/scrapers/__init__.py
```python

```

### supercat_automation/scrapers/base_scraper.py
```python
# scrapers/base_scraper.py
"""
Base scraper class that all trade show scrapers inherit from.
UPDATED to support connecting to a remote Scraping Browser (e.g., Bright Data)
via a WebSocket URL for maximum stealth and reliability.
"""

import asyncio
import logging
import random
from typing import Dict, List, Any, Optional
from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps

from playwright.async_api import async_playwright, Page, Browser, Playwright, TimeoutError as PlaywrightTimeoutError
from twocaptcha import TwoCaptcha

from database.connection import db
from config.settings import settings

logger = logging.getLogger(__name__)

def retry_async(retries=3, delay=5, backoff=2):
    """
    An async decorator to retry a function on failure with exponential backoff.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            _retries, _delay = retries, delay
            while _retries > 0:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    _retries -= 1
                    if _retries == 0:
                        logger.error(f"Function {func.__name__} failed after {retries} retries.")
                        raise
                    logger.warning(f"Function {func.__name__} failed with {e}. Retrying in {_delay} seconds...")
                    await asyncio.sleep(_delay)
                    _delay *= backoff
        return wrapper
    return decorator


class BaseTradeshowScraper(ABC):
    """Base class for all trade show scrapers using Playwright."""

    def __init__(self, trade_show_name: str, base_url: str):
        """Initialize the scraper."""
        self.trade_show_name = trade_show_name
        self.base_url = base_url
        self.trade_show_id: Optional[str] = None
        self.captcha_solver = TwoCaptcha(settings.twocaptcha_api_key) if settings.twocaptcha_api_key else None

    @abstractmethod
    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape general trade show information - must be implemented by child class."""
        pass

    @abstractmethod
    async def scrape_exhibitor_list(self, page: Page) -> List[Dict[str, Any]]:
        """Scrape the list of exhibitors - must be implemented by child class."""
        pass

    def validate_exhibitor_data(self, exhibitor: Dict) -> bool:
        """Validate that exhibitor data has required fields."""
        return 'company_name' in exhibitor and exhibitor['company_name']

    def clean_company_name(self, name: str) -> str:
        """Clean and standardize company name."""
        if not name: return ""
        suffixes = ['Inc.', 'LLC', 'Ltd.', 'Corp.', 'Corporation', 'Company', 'Co.']
        name = name.strip()
        for suffix in suffixes:
            if name.endswith(suffix):
                name = name[:-len(suffix)].strip()
        return name

    async def _save_and_link_exhibitor(self, exhibitor: Dict):
        """Saves a company and links it to the trade show as an exhibitor."""
        if self.validate_exhibitor_data(exhibitor):
            exhibitor['company_name'] = self.clean_company_name(exhibitor['company_name'])
            company_data = {
                'company_name': exhibitor['company_name'],
                'domain': exhibitor.get('website', ''),
                'source': f"{self.trade_show_name}_exhibitor"
            }
            company_record = db.upsert_company(company_data)

            if company_record and self.trade_show_id:
                exhibitor_link = {
                    'trade_show_id': self.trade_show_id,
                    'company_id': company_record['id'],
                    'booth_number': exhibitor.get('booth_number'),
                }
                db.link_exhibitor_to_show(exhibitor_link)
                return True
        return False

    @retry_async(retries=2, delay=10)
    async def run(self) -> Dict[str, Any]:
        """Main execution method using Playwright."""
        async with async_playwright() as p:
            browser = await self._get_browser(p)
            if not browser:
                return {'success': False, 'error': 'Failed to launch or connect to browser.'}
            
            try:
                context = await browser.new_context(
                    user_agent=self._get_random_user_agent(),
                    viewport={'width': 1920, 'height': 1080},
                    locale='en-US'
                )
                page = await context.new_page()
                await self._apply_stealth(page)

                logger.info(f"🚀 Starting scraper for {self.trade_show_name}")

                trade_show_data = await self.scrape_trade_show_info(page)
                if trade_show_data:
                    trade_show_record = db.upsert_trade_show(trade_show_data)
                    if trade_show_record:
                        self.trade_show_id = trade_show_record['id']

                exhibitors_raw = await self.scrape_exhibitor_list(page)

                processed_count = 0
                for exhibitor in exhibitors_raw:
                    if await self._save_and_link_exhibitor(exhibitor):
                        processed_count += 1
                
                logger.info(f"✅ Processed and saved {processed_count} exhibitors for {self.trade_show_name}")

                return {
                    'success': True,
                    'trade_show': self.trade_show_name,
                    'exhibitors_found': len(exhibitors_raw),
                    'exhibitors_processed': processed_count
                }

            except Exception as e:
                logger.error(f"❌ Scraper run failed for {self.trade_show_name}: {e}", exc_info=True)
                return {'success': False, 'error': str(e)}
            finally:
                if browser.is_connected():
                    await browser.close()

    async def _get_browser(self, p: Playwright) -> Optional[Browser]:
        """
        Connects to a remote scraping browser if WSS_URL is set, otherwise
        launches a local browser with a standard proxy.
        """
        if settings.BRIGHT_DATA_WSS_URL:
            logger.info("Connecting to Bright Data Scraping Browser...")
            return await p.chromium.connect_over_cdp(settings.BRIGHT_DATA_WSS_URL)
        else:
            logger.info("Launching local Playwright browser...")
            proxy_config = self._get_http_proxy()
            launch_options = {"headless": True}
            if proxy_config:
                launch_options["proxy"] = proxy_config
                logger.info(f"Using HTTP proxy: {proxy_config['server']}")
            return await p.chromium.launch(**launch_options)

    def _get_http_proxy(self) -> Optional[Dict[str, str]]:
        """
        Fetches standard HTTP proxy configuration for local browser fallback.
        """
        if settings.use_proxies and settings.proxy_list:
            proxy_url = random.choice(settings.proxy_list)
            try:
                auth, endpoint = proxy_url.split('@')
                user, password = auth.replace('http://', '').split(':')
                server = f"http://{endpoint}"
                return {"server": server, "username": user, "password": password}
            except ValueError:
                return {"server": proxy_url}
        return None

    async def _apply_stealth(self, page: Page):
        """Applies techniques to make Playwright harder to detect."""
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def _get_random_user_agent(self) -> str:
        """Provides a random, realistic User-Agent string."""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        ]
        return random.choice(user_agents)

    async def _simulate_human_behavior(self, page: Page):
        """Performs small, randomized actions to mimic a human user."""
        await asyncio.sleep(random.uniform(0.5, 1.5))
        await page.mouse.move(random.randint(50, 150), random.randint(50, 150))
        await asyncio.sleep(random.uniform(0.5, 1.0))

    async def _solve_captcha_if_present(self, page: Page) -> bool:
        """Detects and solves a reCAPTCHA if one is found on the page."""
        if not self.captcha_solver:
            return False
        try:
            captcha_frame = page.frame_locator('iframe[src*="recaptcha"]')
            await captcha_frame.locator('body').wait_for(timeout=5000)
            site_key_element = await captcha_frame.locator('.g-recaptcha').get_attribute('data-sitekey')
            if site_key_element:
                logger.info(f"reCAPTCHA detected with site key: {site_key_element}")
                result = self.captcha_solver.recaptcha(sitekey=site_key_element, url=page.url)
                if result and 'code' in result:
                    logger.info("CAPTCHA solved successfully. Submitting token.")
                    await page.evaluate(f'document.getElementById("g-recaptcha-response").innerHTML="{result["code"]}";')
                    await asyncio.sleep(3)
                    return True
                else:
                    logger.error("CAPTCHA solving failed.")
                    return False
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            logger.error(f"An error occurred during CAPTCHA solving: {e}")
            return False

```

### supercat_automation/scrapers/csv_uploader.py
```python
# scrapers/csv_uploader.py
"""
CSV Upload Handler for SuperCat GTM
Processes uploaded account lists through the same pipeline as scraped companies
Updated to match actual CSV headers
"""

import pandas as pd
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path
import uuid

logger = logging.getLogger(__name__)

class CSVAccountUploader:
    """
    Handles CSV uploads of target accounts
    Integrates with existing pain detection and campaign generation pipeline
    """
    
    def __init__(self):
        # Updated to match your actual CSV columns
        self.required_columns = ['company_name', 'domain']
        self.all_columns = [
            'first_name',
            'last_name', 
            'title',
            'company_name',
            'domain',
            'industry',
            'employee_count',
            'LinkedIn Profile',  # Note the space
            'email'
        ]
    
    def validate_csv(self, file_path: str) -> tuple[bool, str]:
        """
        Validate CSV has required columns and data
        """
        try:
            df = pd.read_csv(file_path)
            
            # Check required columns
            missing_cols = [col for col in self.required_columns if col not in df.columns]
            if missing_cols:
                return False, f"Missing required columns: {missing_cols}"
            
            # Check for empty required fields
            if df['company_name'].isna().any() or df['domain'].isna().any():
                return False, "Some rows have empty company_name or domain"
            
            # Validate domains (basic check)
            invalid_domains = df[~df['domain'].str.contains('.', na=False)]
            if not invalid_domains.empty:
                return False, f"Invalid domains found: {invalid_domains['domain'].tolist()[:5]}"
            
            # Count valid rows
            valid_rows = df.dropna(subset=['company_name', 'domain']).shape[0]
            return True, f"Valid CSV with {valid_rows} companies ready to process"
            
        except Exception as e:
            return False, f"Error reading CSV: {str(e)}"
    
    def process_csv(self, file_path: str, limit: int = None) -> List[Dict[str, Any]]:
        """
        Process CSV and return standardized company records
        
        Args:
            file_path: Path to CSV file
            limit: Optional limit on number of companies to process
            
        Returns:
            List of company dictionaries ready for pain analysis
        """
        df = pd.read_csv(file_path)
        
        # Drop rows with missing required fields
        df = df.dropna(subset=['company_name', 'domain'])
        
        # Apply limit if specified
        if limit:
            df = df.head(limit)
        
        companies = []
        for _, row in df.iterrows():
            # Normalize domain
            domain = str(row['domain']).lower().strip()
            if not domain.startswith('http'):
                domain = f"https://{domain}"
            
            # Build company record with your actual columns
            company = {
                'company_id': str(uuid.uuid4()),
                'company_name': str(row['company_name']).strip(),
                'domain': domain,
                'website': domain,
                'source': 'csv_upload',
                'upload_date': datetime.now().isoformat(),
                
                # Contact information from your columns
                'contact_first_name': str(row.get('first_name', '')).strip() if pd.notna(row.get('first_name')) else '',
                'contact_last_name': str(row.get('last_name', '')).strip() if pd.notna(row.get('last_name')) else '',
                'contact_email': str(row.get('email', '')).strip() if pd.notna(row.get('email')) else '',
                'contact_title': str(row.get('title', '')).strip() if pd.notna(row.get('title')) else '',
                'contact_linkedin': str(row.get('LinkedIn Profile', '')).strip() if pd.notna(row.get('LinkedIn Profile')) else '',
                
                # Company information
                'industry': str(row.get('industry', '')).strip() if pd.notna(row.get('industry')) else '',
                'employee_count': str(row.get('employee_count', '')).strip() if pd.notna(row.get('employee_count')) else '',
                
                # Initialize fields for pain analysis
                'edp_scores': {},
                'website_evidence': {},
                'qualification_tier': None,
                'psi_score': 0.0,
                'campaign_status': 'pending_analysis'
            }
            
            companies.append(company)
        
        logger.info(f"Processed {len(companies)} companies from CSV")
        return companies
    
    def export_results(self, companies: List[Dict], output_path: str = None):
        """
        Export processed companies with analysis results
        """
        if not output_path:
            output_path = f"uploads/results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # Create output directory if needed
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Flatten the company dictionaries for CSV export
        flattened = []
        for company in companies:
            flat = {
                'company_name': company['company_name'],
                'domain': company['domain'],
                'first_name': company.get('contact_first_name', ''),
                'last_name': company.get('contact_last_name', ''),
                'email': company.get('contact_email', ''),
                'title': company.get('contact_title', ''),
                'linkedin': company.get('contact_linkedin', ''),
                'industry': company.get('industry', ''),
                'employee_count': company.get('employee_count', ''),
                'qualification_tier': company.get('qualification_tier', ''),
                'psi_score': company.get('psi_score', 0),
                'primary_edp': company.get('primary_edp', ''),
                'campaign_status': company.get('campaign_status', '')
            }
            
            # Add EDP scores
            for edp, score in company.get('edp_scores', {}).items():
                flat[f'edp_{edp}'] = score
            
            flattened.append(flat)
        
        df = pd.DataFrame(flattened)
        df.to_csv(output_path, index=False)
        
        print(f"\n✅ Results exported to: {output_path}")
        return output_path

# Test function for your 72 prospects
def test_with_real_data():
    """Test function to validate your CSV"""
    uploader = CSVAccountUploader()
    
    # Replace with your actual CSV path
    csv_path = "prospects.csv"  # Update this to your file path
    
    # Validate
    valid, message = uploader.validate_csv(csv_path)
    print(f"Validation: {message}")
    
    if valid:
        # Process all 72 prospects
        companies = uploader.process_csv(csv_path)
        print(f"\nProcessed {len(companies)} companies")
        
        # Show first company as example
        if companies:
            first = companies[0]
            print(f"\nFirst company example:")
            print(f"  Company: {first['company_name']}")
            print(f"  Domain: {first['domain']}")
            print(f"  Contact: {first['contact_first_name']} {first['contact_last_name']}")
            print(f"  Title: {first['contact_title']}")
            print(f"  Email: {first['contact_email']}")
            
    return companies

if __name__ == "__main__":
    # Run test with your data
    test_with_real_data()
```

### supercat_automation/scrapers/orchestrator.py
```python
# scrapers/orchestrator.py
"""
Orchestrates all trade show scrapers.
FIXED to use asyncio.gather for running async scrapers concurrently,
resolving the 'coroutine was never awaited' error.
"""

import logging
import asyncio
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path # ADDED for file path operations

from scrapers.vegas_market import VegasMarketScraper
from scrapers.high_point import HighPointMarketScraper
from scrapers.americasmart import AmericasmartScraper
from database.connection import db
from config.settings import settings

logger = logging.getLogger(__name__)

class ScraperOrchestrator:
    """Manages and coordinates all async trade show scrapers."""

    def __init__(self):
        """Initialize the orchestrator with scraper instances."""
        self.scrapers = {
            'vegas_market': VegasMarketScraper(),
            'high_point': HighPointMarketScraper(),
            'americasmart': AmericasmartScraper(),
        }

    async def run_all_scrapers(self) -> List[Dict[str, Any]]:
        """Runs all configured scrapers concurrently using asyncio.gather."""
        logger.info(f"Starting concurrent run for {len(self.scrapers)} scrapers.")
        
        tasks = [instance.run() for name, instance in self.scrapers.items()]
        
        # return_exceptions=True prevents one failed scraper from stopping the others.
        results = await asyncio.gather(*tasks, return_exceptions=True)

        processed_results = []
        for i, result in enumerate(results):
            scraper_name = list(self.scrapers.keys())[i]
            if isinstance(result, Exception):
                logger.error(f"❌ Scraper '{scraper_name}' failed with an exception: {result}")
                processed_results.append({
                    'success': False,
                    'scraper': scraper_name,
                    'error': str(result)
                })
            else:
                logger.info(f"✅ Scraper '{scraper_name}' completed.")
                processed_results.append(result)
                if result.get('success'):
                    self._update_scraping_metrics(result)

        self.generate_scraping_report(processed_results)
        return processed_results

    def _update_scraping_metrics(self, result: Dict[str, Any]):
        """Update database metrics after a successful scrape."""
        try:
            metrics = {'companies_identified': result.get('exhibitors_processed', 0)}
            db.update_daily_metrics(metrics)
        except Exception as e:
            logger.error(f"Error updating metrics: {e}")

    def generate_scraping_report(self, results: List[Dict[str, Any]]):
        """
        Generates a summary report of the scraping results and saves it to a file.
        """
        total_found = sum(r.get('exhibitors_found', 0) for r in results if r.get('success'))
        total_processed = sum(r.get('exhibitors_processed', 0) for r in results if r.get('success'))
        successful_scrapers = sum(1 for r in results if r.get('success'))
        
        report = f"""
        ========================================
        TRADE SHOW SCRAPING REPORT
        ========================================
        Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Summary:
        - Scrapers Run: {len(results)}
        - Successful: {successful_scrapers}
        - Failed: {len(results) - successful_scrapers}
        
        Results:
        - Total Exhibitors Found: {total_found:,}
        - Total Exhibitors Processed & Saved: {total_processed:,}
        ========================================
        """
        logger.info(report)

        # --- ADDED: Save report to a file ---
        try:
            report_dir = Path("output/reports")
            report_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            report_path = report_dir / f"scraping_report_{timestamp}.txt"
            
            with open(report_path, 'w') as f:
                # Adding details of each scraper run to the file version
                detailed_report = report + "\n\n--- Run Details ---\n"
                for result in results:
                    if result.get('success'):
                        detailed_report += f"\n✅ {result.get('trade_show', 'Unknown')}: {result.get('exhibitors_found', 0)} found, {result.get('exhibitors_processed', 0)} processed"
                    else:
                        detailed_report += f"\n❌ {result.get('scraper', 'Unknown')}: {result.get('error', 'Unknown error')}"
                f.write(detailed_report)
            
            logger.info(f"📄 Scraping report saved to: {report_path}")

        except Exception as e:
            logger.error(f"Failed to save scraping report: {e}")

```

### supercat_automation/scrapers/americasmart.py
```python
# scrapers/americasmart.py
"""
Scraper for AmericasMart Atlanta trade show.
Enhanced version with robust loading strategies and multiple fallback approaches.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import asyncio
import random
import re
from bs4 import BeautifulSoup, Tag
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError
from .base_scraper import BaseTradeshowScraper

logger = logging.getLogger(__name__)

class AmericasmartScraper(BaseTradeshowScraper):
    """Enhanced scraper for AmericasMart Atlanta with multiple strategies."""

    def __init__(self):
        super().__init__(
            trade_show_name="AmericasMart Atlanta",
            base_url="https://www.americasmart.com"
        )
        self.exhibitor_list_url = f"{self.base_url}/exhibitor/exhibitor-directory"
        self.exhibitors_collected = set()  # Track unique exhibitors

    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape AmericasMart Atlanta general information."""
        try:
            logger.info(f"Navigating to AmericasMart homepage: {self.base_url}")
            await page.goto(self.base_url, timeout=90000)
            await page.wait_for_load_state('networkidle')
            
            date_info = await self._extract_show_dates(page)
            
            return {
                'name': 'AmericasMart Atlanta',
                'location': 'Atlanta, GA',
                'venue': 'AmericasMart',
                'start_date': date_info.get('start_date', '2026-01-13'),
                'end_date': date_info.get('end_date', '2026-01-19'),
                'industry': 'Gift, Home, Rug',
                'website_url': self.base_url,
                'exhibitor_list_url': self.exhibitor_list_url,
                'last_scraped': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error scraping trade show info: {e}")
            return self._get_default_show_info()

    async def scrape_exhibitor_list(self, page: Page) -> List[Dict[str, Any]]:
        """Enhanced exhibitor scraping with multiple strategies."""
        exhibitors = []
        
        try:
            logger.info(f"Navigating to exhibitor directory: {self.exhibitor_list_url}")
            await page.goto(self.exhibitor_list_url, timeout=120000)
            await page.wait_for_load_state('networkidle')
            
            await self._handle_overlays(page)
            await self._wait_for_exhibitor_content(page)
            
            # Primary Strategy: Paginate through all pages
            await self._handle_pagination(page, exhibitors)
            
            logger.info(f"Successfully parsed {len(exhibitors)} unique exhibitors")
            
        except Exception as e:
            logger.error(f"Error in main scraping strategy: {e}")
        
        return exhibitors

    async def _handle_overlays(self, page: Page):
        """Handle popups, cookie banners, and overlays."""
        overlay_selectors = [
            "button#onetrust-accept-btn-handler", "button:has-text('Accept')",
            "button[aria-label='Close']", "button[class*='close']"
        ]
        for selector in overlay_selectors:
            try:
                elements = await page.locator(selector).all()
                for element in elements:
                    if await element.is_visible():
                        await element.click(timeout=2000)
                        logger.info(f"Clicked overlay element: {selector}")
                        await asyncio.sleep(1)
            except:
                continue

    async def _wait_for_exhibitor_content(self, page: Page):
        """Wait for exhibitor content to load."""
        content_selectors = [
            "div[data-testid='exhibitor-card']", "div.imc-exhibitor-card",
            "div[class*='directory']", "div[class*='listing']"
        ]
        for selector in content_selectors:
            try:
                await page.wait_for_selector(selector, timeout=10000)
                logger.info(f"Found content with selector: {selector}")
                return
            except:
                continue
        logger.warning("Could not find specific exhibitor content, waiting...")
        await asyncio.sleep(5)

    async def _handle_pagination(self, page: Page, exhibitors: List[Dict[str, Any]]):
        """Handle pagination by repeatedly clicking the 'Next' button."""
        next_page_selector = "a[aria-label='Next Page']"
        max_pages = 50

        for i in range(max_pages):
            logger.info(f"Scraping page {i + 1}...")
            await self._parse_page_content(page, exhibitors)
            
            try:
                next_button = page.locator(next_page_selector)
                if await next_button.is_disabled(timeout=5000):
                    logger.info("Next button is disabled. Reached the last page.")
                    break
                
                await self._simulate_human_behavior(page)
                await next_button.click()
                await page.wait_for_load_state('networkidle', timeout=30000)
            except Exception:
                logger.info("Could not find or click 'Next Page' button. Assuming end of list.")
                break

    async def _parse_page_content(self, page: Page, exhibitors: List[Dict[str, Any]]):
        """Parse the content of the current page for exhibitors."""
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        exhibitor_elements = self._find_all_exhibitor_elements(soup)
        
        for elem in exhibitor_elements:
            exhibitor = self._parse_exhibitor_comprehensive(elem)
            if exhibitor and exhibitor.get('company_name'):
                company_key = exhibitor['company_name'].lower().strip()
                if company_key not in self.exhibitors_collected:
                    self.exhibitors_collected.add(company_key)
                    exhibitors.append(exhibitor)

    def _find_all_exhibitor_elements(self, soup: BeautifulSoup) -> List[Tag]:
        """Find exhibitor elements using comprehensive selectors."""
        selectors = [
            "div[data-testid='exhibitor-card']", "div.imc-exhibitor-card",
            "div[class*='exhibitor-item']", "div[class*='vendor-card']"
        ]
        all_elements = []
        for selector in selectors:
            all_elements.extend(soup.select(selector))
        return all_elements

    def _parse_exhibitor_comprehensive(self, element: Tag) -> Optional[Dict[str, Any]]:
        """Parse exhibitor with multiple extraction strategies."""
        try:
            company_name = self._extract_company_name(element)
            if not company_name:
                return None
            
            return {
                'company_name': company_name,
                'website': self._extract_website(element),
                'booth_number': self._extract_booth_info(element).get('booth_number'),
                'building': self._extract_booth_info(element).get('building'),
                'categories': self._extract_categories(element)
            }
        except Exception as e:
            logger.debug(f"Error parsing exhibitor element: {e}")
            return None

    def _extract_company_name(self, element: Tag) -> Optional[str]:
        """Extract company name using multiple strategies."""
        name_selectors = [
            "h3[data-testid='exhibitor-name'] a", "h3.imc-exhibitor-card__name a",
            "div[class*='-name']", "div[class*='-title']"
        ]
        for selector in name_selectors:
            tag = element.select_one(selector)
            if tag and tag.text.strip():
                return tag.text.strip()
        return None

    def _extract_website(self, element: Tag) -> Optional[str]:
        """Extract website URL."""
        for link in element.find_all('a', href=True):
            href = link['href']
            if href.startswith('http') and 'americasmart.com' not in href:
                return href
        return None

    def _extract_booth_info(self, element: Tag) -> Dict[str, Any]:
        """Extract booth number and location information."""
        booth_info = {}
        location_tag = element.select_one("p[data-testid='exhibitor-location']")
        if location_tag:
            booth_info['booth_number'] = location_tag.text.strip()
        return booth_info

    def _extract_categories(self, element: Tag) -> Optional[str]:
        """Extract product categories."""
        categories_tag = element.select_one("p[data-testid='exhibitor-categories']")
        if categories_tag:
            return categories_tag.text.strip()
        return None

    async def _extract_show_dates(self, page: Page) -> Dict[str, str]:
        """Try to extract actual show dates from the page."""
        # This is a placeholder; a real implementation would need a robust date-finding logic
        return {}

    def _get_default_show_info(self) -> Dict[str, Any]:
        """Return default show information as fallback."""
        return {
            'name': 'AmericasMart Atlanta',
            'location': 'Atlanta, GA',
            'venue': 'AmericasMart',
            'start_date': '2026-01-13',
            'end_date': '2026-01-19',
            'industry': 'Gift, Home, Rug',
            'website_url': self.base_url,
            'exhibitor_list_url': self.exhibitor_list_url,
            'last_scraped': datetime.now().isoformat()
        }

```

### supercat_automation/scrapers/vegas_market.py
```python
# scrapers/vegas_market.py
"""
Vegas Market Scraper - Production-Ready Version
Implements multiple fallback strategies and robust error handling
"""

import json
import logging
import asyncio
import random
from typing import Dict, List, Any, Optional, Set
from datetime import datetime
from urllib.parse import urljoin, urlparse
import re

from playwright.async_api import Page, Route, Request, Response, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup, Tag
from .base_scraper import BaseTradeshowScraper

logger = logging.getLogger(__name__)

class VegasMarketScraper(BaseTradeshowScraper):
    """
    Production-ready scraper for Las Vegas Market
    Implements multiple strategies with fallbacks
    """
    
    def __init__(self):
        super().__init__(
            trade_show_name="Las Vegas Market",
            base_url="https://www.lasvegasmarket.com"
        )
        # Multiple possible URLs to try
        self.exhibitor_urls = [
            f"{self.base_url}/exhibitor/exhibitor-directory",
            f"{self.base_url}/exhibitors",
            f"{self.base_url}/directory",
            f"{self.base_url}/exhibitor-list"
        ]
        self.api_data = []
        self.intercepted_responses = []
        
    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape Las Vegas Market general information with fallbacks"""
        try:
            await page.goto(self.base_url, timeout=60000, wait_until='networkidle')
            
            # Wait for main content to load
            await page.wait_for_selector('body', timeout=30000)
            
            # Extract dates using multiple strategies
            dates = await self._extract_show_dates(page)
            
            return {
                'name': 'Las Vegas Market',
                'location': 'Las Vegas, NV',
                'venue': 'World Market Center',
                'start_date': dates.get('start', '2025-07-27'),
                'end_date': dates.get('end', '2025-07-31'),
                'industry': 'Furniture, Home Decor, Gift',
                'website_url': self.base_url,
                'exhibitor_list_url': self.exhibitor_urls[0],
                'last_scraped': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error scraping trade show info: {e}")
            # Return fallback data
            return self._get_fallback_show_info()
    
    async def scrape_exhibitor_list(self, page: Page) -> List[Dict[str, Any]]:
        """
        Main scraping method with multiple strategies
        """
        exhibitors = []
        
        # Strategy 1: Try API interception first
        logger.info("Strategy 1: Attempting API interception...")
        exhibitors = await self._scrape_via_api_interception(page)
        
        if len(exhibitors) < 10:  # Likely failed
            logger.info("Strategy 2: Attempting DOM scraping...")
            exhibitors = await self._scrape_via_dom(page)
        
        if len(exhibitors) < 10:  # Still not enough
            logger.info("Strategy 3: Attempting search-based scraping...")
            exhibitors = await self._scrape_via_search(page)
        
        if len(exhibitors) < 10:  # Last resort
            logger.info("Strategy 4: Attempting sitemap/static page scraping...")
            exhibitors = await self._scrape_via_sitemap(page)
        
        # Deduplicate
        exhibitors = self._deduplicate_exhibitors(exhibitors)
        
        logger.info(f"Total unique exhibitors found: {len(exhibitors)}")
        return exhibitors
    
    async def _scrape_via_api_interception(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 1: Intercept API calls made by the page
        """
        exhibitors = []
        
        # Set up request interception
        async def handle_route(route: Route, request: Request):
            """Intercept and log API requests"""
            url = request.url
            
            # Log interesting API calls
            if any(keyword in url.lower() for keyword in ['exhibitor', 'vendor', 'company', 'directory', 'api', 'graphql']):
                logger.debug(f"Intercepted API call: {url}")
            
            await route.continue_()
        
        async def handle_response(response: Response):
            """Capture API responses"""
            url = response.url
            
            # Check if this looks like exhibitor data
            if any(keyword in url.lower() for keyword in ['exhibitor', 'vendor', 'company', 'directory']):
                try:
                    if response.status == 200:
                        content_type = response.headers.get('content-type', '')
                        if 'json' in content_type:
                            data = await response.json()
                            self.api_data.append(data)
                            logger.info(f"Captured API response from: {url}")
                except Exception as e:
                    logger.debug(f"Could not parse response from {url}: {e}")
        
        # Set up interception
        page.on('response', handle_response)
        await page.route('**/*', handle_route)
        
        # Try each possible URL
        for url in self.exhibitor_urls:
            try:
                logger.info(f"Trying URL: {url}")
                await page.goto(url, timeout=60000, wait_until='networkidle')
                
                # Wait for potential API calls
                await asyncio.sleep(5)
                
                # Check if we got data
                if self.api_data:
                    exhibitors = self._parse_api_data(self.api_data)
                    if exhibitors:
                        logger.info(f"Found {len(exhibitors)} exhibitors via API interception")
                        return exhibitors
                        
            except Exception as e:
                logger.warning(f"Failed to load {url}: {e}")
                continue
        
        return exhibitors
    
    async def _scrape_via_dom(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 2: Traditional DOM scraping with smart selectors
        """
        exhibitors = []
        
        # Try multiple possible selectors
        selector_sets = [
            # Set 1: Data attributes
            {
                'container': '[data-testid*="exhibitor"], [data-test*="exhibitor"]',
                'name': '[data-testid*="name"], [data-test*="name"], h2, h3, h4',
                'booth': '[data-testid*="booth"], [data-test*="location"], [data-test*="booth"]',
                'website': 'a[href*="http"]'
            },
            # Set 2: Class-based
            {
                'container': '.exhibitor-card, .vendor-card, .company-card, .directory-item',
                'name': '.exhibitor-name, .vendor-name, .company-name, .name, h2, h3',
                'booth': '.booth-number, .location, .booth, .stand',
                'website': 'a.website, a.link, a[href*="http"]'
            },
            # Set 3: Generic structure
            {
                'container': 'article, .card, .item, .result, div[class*="card"]',
                'name': 'h1, h2, h3, h4, .title',
                'booth': '.location, .booth, span:contains("Booth")',
                'website': 'a[href^="http"]'
            }
        ]
        
        for url in self.exhibitor_urls:
            try:
                await page.goto(url, timeout=60000, wait_until='domcontentloaded')
                
                # Handle popups
                await self._handle_popups(page)
                
                # Try infinite scroll
                await self._smart_infinite_scroll(page)
                
                # Try each selector set
                for selectors in selector_sets:
                    try:
                        # Wait for containers
                        await page.wait_for_selector(selectors['container'], timeout=10000)
                        
                        # Get all exhibitor containers
                        containers = await page.query_selector_all(selectors['container'])
                        
                        logger.info(f"Found {len(containers)} potential exhibitor containers")
                        
                        for container in containers[:500]:  # Limit to prevent memory issues
                            exhibitor = await self._extract_exhibitor_from_element(container, selectors)
                            if exhibitor and exhibitor.get('company_name'):
                                exhibitors.append(exhibitor)
                        
                        if exhibitors:
                            logger.info(f"Successfully extracted {len(exhibitors)} exhibitors")
                            return exhibitors
                            
                    except Exception as e:
                        logger.debug(f"Selector set failed: {e}")
                        continue
                        
            except Exception as e:
                logger.warning(f"Failed to scrape {url}: {e}")
                continue
        
        return exhibitors
    
    async def _scrape_via_search(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 3: Use the site's search functionality
        """
        exhibitors = []
        
        # Common search patterns for trade show sites
        search_urls = [
            f"{self.base_url}/search",
            f"{self.base_url}/exhibitor/search",
            f"{self.base_url}/directory/search"
        ]
        
        # Try alphabet search (A-Z)
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            for base_search_url in search_urls:
                try:
                    search_url = f"{base_search_url}?q={letter}"
                    logger.info(f"Searching with letter: {letter}")
                    
                    await page.goto(search_url, timeout=30000, wait_until='networkidle')
                    await asyncio.sleep(2)
                    
                    # Extract results
                    results = await self._extract_search_results(page)
                    exhibitors.extend(results)
                    
                    if len(exhibitors) > 100:  # Good enough sample
                        break
                        
                except Exception as e:
                    logger.debug(f"Search failed for {letter}: {e}")
                    continue
            
            if len(exhibitors) > 100:
                break
        
        return exhibitors
    
    async def _scrape_via_sitemap(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 4: Check sitemap or use a category/building approach
        """
        exhibitors = []
        
        # Common building/hall names at Vegas Market
        buildings = [
            'Building A', 'Building B', 'Building C',
            'Pavilion', 'Hall 1', 'Hall 2', 'Hall 3',
            'North', 'South', 'East', 'West'
        ]
        
        # Try sitemap first
        sitemap_urls = [
            f"{self.base_url}/sitemap.xml",
            f"{self.base_url}/sitemap",
            f"{self.base_url}/exhibitor-sitemap.xml"
        ]
        
        for sitemap_url in sitemap_urls:
            try:
                await page.goto(sitemap_url, timeout=30000)
                content = await page.content()
                
                # Extract exhibitor URLs from sitemap
                exhibitor_urls = re.findall(r'<loc>(.*?exhibitor.*?)</loc>', content, re.IGNORECASE)
                
                # Visit each exhibitor page (limit to prevent overload)
                for ex_url in exhibitor_urls[:50]:
                    try:
                        await page.goto(ex_url, timeout=20000)
                        exhibitor = await self._extract_exhibitor_from_page(page)
                        if exhibitor:
                            exhibitors.append(exhibitor)
                    except:
                        continue
                        
                if exhibitors:
                    return exhibitors
                    
            except Exception as e:
                logger.debug(f"Sitemap approach failed: {e}")
                continue
        
        return exhibitors
    
    async def _smart_infinite_scroll(self, page: Page, max_scrolls: int = 50):
        """
        Intelligent infinite scroll with multiple strategies
        """
        logger.info("Starting smart infinite scroll...")
        
        # Strategy 1: Check for a "Load More" button
        load_more_selectors = [
            'button:has-text("Load More")',
            'button:has-text("Show More")',
            'button:has-text("View More")',
            'a:has-text("Load More")',
            'button[class*="load"]',
            'button[class*="more"]'
        ]
        
        for selector in load_more_selectors:
            try:
                while True:
                    button = await page.query_selector(selector)
                    if button:
                        await button.click()
                        await asyncio.sleep(2)
                    else:
                        break
            except:
                continue
        
        # Strategy 2: Traditional scroll
        last_height = await page.evaluate('document.body.scrollHeight')
        same_height_count = 0
        
        for i in range(max_scrolls):
            # Scroll down
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            
            # Random wait to appear human
            await asyncio.sleep(random.uniform(1.5, 3.0))
            
            # Check for new content
            new_height = await page.evaluate('document.body.scrollHeight')
            
            if new_height == last_height:
                same_height_count += 1
                
                # Try scrolling up a bit then down again (sometimes triggers load)
                if same_height_count == 2:
                    await page.evaluate('window.scrollTo(0, document.body.scrollHeight - 1000)')
                    await asyncio.sleep(1)
                    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                    await asyncio.sleep(2)
                
                if same_height_count >= 3:
                    logger.info("No new content after 3 attempts, stopping scroll")
                    break
            else:
                same_height_count = 0
                last_height = new_height
                logger.debug(f"Scroll {i+1}: New content loaded")
        
        logger.info("Finished scrolling")
    
    async def _handle_popups(self, page: Page):
        """Handle various popups and overlays"""
        popup_selectors = [
            # Cookie banners
            'button:has-text("Accept")',
            'button:has-text("Accept All")',
            'button#onetrust-accept-btn-handler',
            'button[aria-label*="accept"]',
            # Newsletter/email popups
            'button[aria-label*="close"]',
            'button:has-text("No Thanks")',
            'button.close',
            '.modal-close',
            # Generic close buttons
            'button:has-text("X")',
            'button:has-text("×")',
        ]
        
        for selector in popup_selectors:
            try:
                button = await page.query_selector(selector)
                if button and await button.is_visible():
                    await button.click()
                    await asyncio.sleep(1)
                    logger.debug(f"Closed popup with selector: {selector}")
            except:
                continue
    
    async def _extract_exhibitor_from_element(self, element, selectors: Dict) -> Dict[str, Any]:
        """Extract exhibitor data from a page element"""
        try:
            exhibitor = {}
            
            # Get company name
            name_elem = await element.query_selector(selectors['name'])
            if name_elem:
                exhibitor['company_name'] = await name_elem.inner_text()
                exhibitor['company_name'] = exhibitor['company_name'].strip()
            
            # Get booth number
            booth_elem = await element.query_selector(selectors['booth'])
            if booth_elem:
                exhibitor['booth_number'] = await booth_elem.inner_text()
                exhibitor['booth_number'] = exhibitor['booth_number'].strip()
            
            # Get website
            website_elem = await element.query_selector(selectors['website'])
            if website_elem:
                exhibitor['website'] = await website_elem.get_attribute('href')
            
            # Get any additional text content for context
            try:
                full_text = await element.inner_text()
                exhibitor['raw_text'] = full_text[:500]  # Store for later parsing if needed
            except:
                pass
            
            return exhibitor if exhibitor.get('company_name') else None
            
        except Exception as e:
            logger.debug(f"Failed to extract exhibitor: {e}")
            return None
    
    async def _extract_exhibitor_from_page(self, page: Page) -> Dict[str, Any]:
        """Extract exhibitor data from a dedicated exhibitor page"""
        try:
            exhibitor = {}
            
            # Try multiple selectors for company name
            name_selectors = ['h1', 'h2', '.company-name', '.exhibitor-name', '[itemprop="name"]']
            for selector in name_selectors:
                try:
                    elem = await page.query_selector(selector)
                    if elem:
                        exhibitor['company_name'] = await elem.inner_text()
                        break
                except:
                    continue
            
            # Extract other details
            exhibitor['website'] = await self._extract_website(page)
            exhibitor['booth_number'] = await self._extract_booth_number(page)
            
            return exhibitor if exhibitor.get('company_name') else None
            
        except Exception as e:
            logger.debug(f"Failed to extract from page: {e}")
            return None
    
    async def _extract_website(self, page: Page) -> Optional[str]:
        """Extract website URL from page"""
        selectors = [
            'a:has-text("Website")',
            'a:has-text("Visit Website")',
            'a[href*="http"]:not([href*="lasvegasmarket"])',
            'a.website-link'
        ]
        
        for selector in selectors:
            try:
                elem = await page.query_selector(selector)
                if elem:
                    return await elem.get_attribute('href')
            except:
                continue
        return None
    
    async def _extract_booth_number(self, page: Page) -> Optional[str]:
        """Extract booth number from page"""
        # Look for booth number patterns
        content = await page.content()
        booth_patterns = [
            r'Booth[:\s#]+([A-Z0-9\-]+)',
            r'Stand[:\s#]+([A-Z0-9\-]+)',
            r'Location[:\s]+([A-Z0-9\-]+)',
        ]
        
        for pattern in booth_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return None
    
    async def _extract_show_dates(self, page: Page) -> Dict[str, str]:
        """Extract show dates from the page"""
        dates = {}
        
        # Look for date patterns
        content = await page.content()
        
        # Common date patterns
        date_patterns = [
            r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})-(\d{1,2}),?\s+(\d{4})',
            r'(\d{1,2})/(\d{1,2})/(\d{4})\s*-\s*(\d{1,2})/(\d{1,2})/(\d{4})',
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, content)
            if match:
                # Parse and format dates
                # (Implementation depends on pattern matched)
                logger.info(f"Found dates: {match.group()}")
                break
        
        return dates
    
    async def _extract_search_results(self, page: Page) -> List[Dict[str, Any]]:
        """Extract exhibitors from search results"""
        exhibitors = []
        
        # Common search result selectors
        result_selectors = [
            '.search-result',
            '.result-item',
            'article',
            '.exhibitor-result'
        ]
        
        for selector in result_selectors:
            try:
                results = await page.query_selector_all(selector)
                for result in results:
                    exhibitor = await self._extract_exhibitor_from_element(
                        result, 
                        {
                            'name': 'h2, h3, .title',
                            'booth': '.booth, .location',
                            'website': 'a[href^="http"]'
                        }
                    )
                    if exhibitor:
                        exhibitors.append(exhibitor)
                
                if exhibitors:
                    break
                    
            except:
                continue
        
        return exhibitors
    
    def _parse_api_data(self, api_responses: List[Any]) -> List[Dict[str, Any]]:
        """Parse exhibitor data from intercepted API responses"""
        exhibitors = []
        
        for response in api_responses:
            try:
                # Handle different API response structures
                if isinstance(response, dict):
                    # Check for common data locations
                    data_locations = [
                        response.get('data', []),
                        response.get('results', []),
                        response.get('exhibitors', []),
                        response.get('vendors', []),
                        response.get('companies', []),
                        response.get('items', []),
                    ]
                    
                    for data in data_locations:
                        if isinstance(data, list):
                            for item in data:
                                exhibitor = self._parse_api_exhibitor(item)
                                if exhibitor:
                                    exhibitors.append(exhibitor)
                        elif isinstance(data, dict):
                            exhibitor = self._parse_api_exhibitor(data)
                            if exhibitor:
                                exhibitors.append(exhibitor)
                
                elif isinstance(response, list):
                    for item in response:
                        exhibitor = self._parse_api_exhibitor(item)
                        if exhibitor:
                            exhibitors.append(exhibitor)
                            
            except Exception as e:
                logger.debug(f"Failed to parse API response: {e}")
                continue
        
        return exhibitors
    
    def _parse_api_exhibitor(self, item: Dict) -> Optional[Dict[str, Any]]:
        """Parse individual exhibitor from API data"""
        if not isinstance(item, dict):
            return None
        
        exhibitor = {}
        
        # Common field names for company name
        name_fields = ['name', 'companyName', 'company_name', 'exhibitorName', 
                      'exhibitor_name', 'vendorName', 'vendor_name', 'title']
        
        for field in name_fields:
            if field in item and item[field]:
                exhibitor['company_name'] = str(item[field]).strip()
                break
        
        # Common field names for booth
        booth_fields = ['booth', 'boothNumber', 'booth_number', 'location', 
                       'stand', 'standNumber', 'stand_number']
        
        for field in booth_fields:
            if field in item and item[field]:
                exhibitor['booth_number'] = str(item[field]).strip()
                break
        
        # Common field names for website
        website_fields = ['website', 'url', 'webUrl', 'web_url', 'link', 
                         'companyUrl', 'company_url']
        
        for field in website_fields:
            if field in item and item[field]:
                exhibitor['website'] = str(item[field]).strip()
                break
        
        # Store raw data for debugging
        exhibitor['raw_api_data'] = item
        
        return exhibitor if exhibitor.get('company_name') else None
    
    def _deduplicate_exhibitors(self, exhibitors: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Remove duplicate exhibitors based on company name"""
        seen = set()
        unique = []
        
        for exhibitor in exhibitors:
            name = exhibitor.get('company_name', '').lower().strip()
            if name and name not in seen:
                seen.add(name)
                unique.append(exhibitor)
        
        return unique
    
    def _get_fallback_show_info(self) -> Dict[str, Any]:
        """Return fallback trade show information"""
        return {
            'name': 'Las Vegas Market',
            'location': 'Las Vegas, NV',
            'venue': 'World Market Center',
            'start_date': '2025-07-27',
            'end_date': '2025-07-31',
            'industry': 'Furniture, Home Decor, Gift',
            'website_url': self.base_url,
            'exhibitor_list_url': self.exhibitor_urls[0],
            'last_scraped': datetime.now().isoformat(),
            'note': 'Fallback data - actual dates may vary'
        }
```

### supercat_automation/scrapers/trade_show_scraper.py
```python
# src/scrapers/trade_show_scraper.py
"""
Trade show scraper for identifying target companies
Focus on furniture, lighting, and home decor shows
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class TradeshowScraper:
    """Scrapes major trade shows for exhibitor lists"""
    
    def __init__(self, supabase_client):
        self.supabase = supabase_client
        self.trade_shows = [
            {
                'name': 'Las Vegas Market',
                'url': 'https://www.lasvegasmarket.com',
                'exhibitor_path': '/exhibitors',
                'industry': 'furniture_lighting_home_decor',
                'frequency': 'bi-annual',
                'next_dates': ['2025-01-26', '2025-07-27']
            },
            {
                'name': 'High Point Market',
                'url': 'https://www.highpointmarket.org',
                'exhibitor_path': '/exhibitors',
                'industry': 'furniture',
                'frequency': 'bi-annual',
                'next_dates': ['2025-04-26', '2025-10-25']
            },
            {
                'name': 'AmericasMart Atlanta',
                'url': 'https://www.americasmart.com',
                'exhibitor_path': '/markets/gift-home',
                'industry': 'gift_home_decor',
                'frequency': 'quarterly',
                'next_dates': ['2025-01-14', '2025-07-15']
            },
            {
                'name': 'Dallas Market Center',
                'url': 'https://www.dallasmarketcenter.com',
                'exhibitor_path': '/markets/lightovation',
                'industry': 'lighting',
                'frequency': 'bi-annual',
                'next_dates': ['2025-01-08', '2025-06-18']
            }
        ]
    
    async def scrape_all_shows(self) -> List[Dict]:
        """Scrape all configured trade shows"""
        all_exhibitors = []
        
        for show in self.trade_shows:
            try:
                exhibitors = await self.scrape_show(show)
                all_exhibitors.extend(exhibitors)
                logger.info(f"Scraped {len(exhibitors)} exhibitors from {show['name']}")
            except Exception as e:
                logger.error(f"Failed to scrape {show['name']}: {e}")
                continue
        
        return all_exhibitors
    
    async def scrape_show(self, show: Dict) -> List[Dict]:
        """Scrape individual trade show for exhibitors"""
        exhibitors = []
        
        try:
            async with aiohttp.ClientSession() as session:
                url = show['url'] + show['exhibitor_path']
                async with session.get(url) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Parse exhibitor listings (simplified - needs customization per site)
                    exhibitor_elements = soup.find_all(['div', 'article'], class_=['exhibitor', 'vendor', 'company'])
                    
                    for elem in exhibitor_elements:
                        exhibitor = self._parse_exhibitor(elem, show)
                        if exhibitor:
                            exhibitors.append(exhibitor)
        
        except Exception as e:
            logger.error(f"Error scraping {show['name']}: {e}")
        
        return exhibitors
    
    def _parse_exhibitor(self, element, show: Dict) -> Optional[Dict]:
        """Parse individual exhibitor element"""
        try:
            # Extract company name
            name_elem = element.find(['h2', 'h3', 'h4', 'a'], class_=['name', 'title', 'company-name'])
            if not name_elem:
                return None
            
            company_name = name_elem.get_text(strip=True)
            
            # Extract booth number
            booth_elem = element.find(['span', 'div'], class_=['booth', 'location', 'booth-number'])
            booth_number = booth_elem.get_text(strip=True) if booth_elem else None
            
            # Extract website/domain
            link_elem = element.find('a', href=True)
            website = link_elem['href'] if link_elem else None
            
            # Calculate urgency based on show date
            next_show_date = datetime.strptime(show['next_dates'][0], '%Y-%m-%d')
            days_until_show = (next_show_date - datetime.now()).days
            urgency_score = self._calculate_urgency(days_until_show)
            
            return {
                'company_name': company_name,
                'trade_show': show['name'],
                'booth_number': booth_number,
                'website': website,
                'industry': show['industry'],
                'show_date': show['next_dates'][0],
                'days_until_show': days_until_show,
                'urgency_score': urgency_score,
                'source': 'trade_show_scrape',
                'scraped_at': datetime.now().isoformat()
            }
        
        except Exception as e:
            logger.debug(f"Failed to parse exhibitor: {e}")
            return None
    
    def _calculate_urgency(self, days_until_show: int) -> float:
        """Calculate urgency score based on days until show"""
        if days_until_show <= 30:
            return 1.0
        elif days_until_show <= 60:
            return 0.8
        elif days_until_show <= 90:
            return 0.6
        elif days_until_show <= 120:
            return 0.4
        else:
            return 0.2


# src/scrapers/industry_directory_scraper.py
"""
Industry directory scraper for furniture/lighting manufacturers
"""

class IndustryDirectoryScraper:
    """Scrapes industry directories for target companies"""
    
    def __init__(self, supabase_client):
        self.supabase = supabase_client
        self.directories = [
            {
                'name': 'Furniture Today Top 100',
                'url': 'https://www.furnituretoday.com/research/',
                'industry': 'furniture_manufacturing'
            },
            {
                'name': 'Home Furnishings Association',
                'url': 'https://www.myhfa.org/members/',
                'industry': 'home_furnishings'
            },
            {
                'name': 'American Lighting Association',
                'url': 'https://www.americanlightingassoc.com/members/',
                'industry': 'lighting'
            },
            {
                'name': 'International Home Furnishings Representatives Association',
                'url': 'https://www.ihfra.org/manufacturers/',
                'industry': 'home_furnishings_reps'
            }
        ]
    
    async def scrape_directories(self) -> List[Dict]:
        """Scrape all configured directories"""
        all_companies = []
        
        for directory in self.directories:
            try:
                companies = await self.scrape_directory(directory)
                all_companies.extend(companies)
                logger.info(f"Scraped {len(companies)} companies from {directory['name']}")
            except Exception as e:
                logger.error(f"Failed to scrape {directory['name']}: {e}")
                continue
        
        return all_companies
    
    async def scrape_directory(self, directory: Dict) -> List[Dict]:
        """Scrape individual directory"""
        companies = []
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(directory['url']) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Parse company listings
                    company_elements = soup.find_all(['div', 'li', 'article'], 
                                                    class_=['member', 'company', 'listing'])
                    
                    for elem in company_elements:
                        company = self._parse_company(elem, directory)
                        if company:
                            companies.append(company)
        
        except Exception as e:
            logger.error(f"Error scraping {directory['name']}: {e}")
        
        return companies
    
    def _parse_company(self, element, directory: Dict) -> Optional[Dict]:
        """Parse individual company element"""
        try:
            # Extract company details
            name = element.find(['h2', 'h3', 'a']).get_text(strip=True)
            
            # Look for website
            website_elem = element.find('a', href=lambda x: x and 'http' in x)
            website = website_elem['href'] if website_elem else None
            
            # Extract additional details
            details = {
                'company_name': name,
                'website': website,
                'industry': directory['industry'],
                'source': f"directory_{directory['name']}",
                'directory_listing': True,
                'scraped_at': datetime.now().isoformat()
            }
            
            return details
        
        except Exception as e:
            logger.debug(f"Failed to parse company: {e}")
            return None
```

### supercat_automation/scrapers/website_evidence.py
```python
# scrapers/website_evidence.py

import logging
import re
import logging
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from typing import Dict, List, Any, Optional, Optional
from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class WebsiteEvidenceExtractor:
    """
    Extracts specific evidence of the 5 proven EDPs from websites
    Each method maps to validated pain points from 14 won deals
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Map website indicators to proven EDPs
        self.edp_indicators = {
            'sales_enablement_collapse': {
                'indicators': [
                    'no_product_search',
                    'pdf_only_catalog', 
                    'no_mobile_optimization',
                    'no_dealer_portal',
                    'manual_quote_process',
                    'no_inventory_visibility'
                ],
                'weight': 1.0  # 100% of won deals
            },
            'technology_obsolescence': {
                'indicators': [
                    'no_ssl_certificate',
                    'slow_page_load',
                    'outdated_copyright',
                    'flash_required',
                    'no_responsive_design',
                    'no_integrations_visible'
                ],
                'weight': 0.93  # 93% of won deals
            },
            'rep_performance_crisis': {
                'indicators': [
                    'no_rep_locator',
                    'no_rep_portal',
                    'no_territory_info',
                    'no_sales_resources',
                    'complex_territory_structure'
                ],
                'weight': 0.71  # 71% of won deals
            },
            'sku_complexity': {
                'indicators': [
                    'massive_catalog',
                    'no_filtering_options',
                    'complex_configurations',
                    'no_comparison_tool',
                    'confusing_navigation'
                ],
                'weight': 0.64  # 64% of won deals
            },
            'channel_conflict': {
                'indicators': [
                    'multiple_login_portals',
                    'hidden_pricing',
                    'conflicting_information',
                    'multiple_brand_sites',
                    'dealer_only_access'
                ],
                'weight': 0.43  # 43% of won deals
            }
        }
    
    def _get_dynamic_html(self, url: str) -> str:
        """
        Uses Selenium to fetch fully rendered HTML (including JS content)
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        html = driver.page_source
        driver.quit()
        return html

    def analyze_website(self, domain: str) -> Dict[str, Any]:
        """
        Complete website analysis for all 5 EDPs
        Returns evidence mapped to specific pain points
        """
        
        # Ensure proper URL format
        if not domain.startswith('http'):
            domain = f'https://{domain}'
        
        results = {
            'domain': domain,
            'scan_timestamp': datetime.now().isoformat(),
            'edp_evidence': {},
            'specific_findings': [],
            'personalization_hooks': [],
            'tam_indicators': {}
        }
        
        try:
            # Use Selenium to fetch fully rendered HTML
            html = self._get_dynamic_html(domain)
            soup = BeautifulSoup(html, 'html.parser')
            text_content = soup.get_text().lower()

            # Check each EDP
            for edp_name, edp_config in self.edp_indicators.items():
                evidence = self._check_edp_indicators(domain, edp_name, edp_config, soup, text_content)
                results['edp_evidence'][edp_name] = evidence
                # Add specific findings for messaging
                if evidence['score'] > 0.5:
                    results['specific_findings'].extend(evidence['specific_issues'])

            # Extract additional context
            results['personalization_hooks'] = self._extract_personalization_data(soup)
            results['tam_indicators'] = self._identify_tam_tier_indicators(results)

        except Exception as e:
            logger.error(f"Error analyzing {domain}: {e}")
            results['error'] = str(e)

        return results
    
    def _check_edp_indicators(self, domain: str, edp_name: str, config: Dict, soup: BeautifulSoup, text_content: str) -> Dict:
        """
        Check specific indicators for each EDP
        """
        
        evidence = {
            'edp': edp_name,
            'score': 0,
            'indicators_found': [],
            'specific_issues': [],
            'evidence_strength': 'none'
        }
        
        # Check each indicator based on EDP type
        if edp_name == 'sales_enablement_collapse':
            evidence = self._check_sales_enablement_indicators(domain, soup, text_content)
        elif edp_name == 'technology_obsolescence':
            evidence = self._check_technology_indicators(domain, soup, text_content)
        elif edp_name == 'rep_performance_crisis':
            evidence = self._check_rep_indicators(domain, soup, text_content)
        elif edp_name == 'sku_complexity':
            evidence = self._check_catalog_indicators(domain, soup)
        elif edp_name == 'channel_conflict':
            evidence = self._check_channel_indicators(domain, soup)
        
        # Apply weight from won deals
        evidence['weighted_score'] = evidence['score'] * config['weight']
        
        return evidence
    
    def _check_sales_enablement_indicators(self, domain: str, soup: BeautifulSoup, text_content: str) -> Dict:
        """Check for sales enablement collapse indicators"""
        
        evidence = {
            'edp': 'sales_enablement_collapse',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Check for product search
            search_elements = soup.find_all(['input', 'button'], 
                                           attrs={'type': 'search'}) or \
                            soup.find_all(text=lambda t: t and 'search' in t.lower())
            
            if not search_elements:
                evidence['indicators_found'].append('no_product_search')
                evidence['specific_issues'].append('No product search functionality found')
                evidence['score'] += 0.25
            
            # Check for PDF-only resources
            download_links = soup.find_all('a', href=lambda h: h and '.pdf' in h.lower())
            if len(download_links) > 5:
                evidence['indicators_found'].append('pdf_heavy')
                evidence['specific_issues'].append(f'Found {len(download_links)} PDF downloads - indicates manual processes')
                evidence['score'] += 0.20
            
            # Check mobile optimization
            viewport = soup.find('meta', attrs={'name': 'viewport'})
            if not viewport:
                evidence['indicators_found'].append('no_mobile_optimization')
                evidence['specific_issues'].append('Not mobile optimized - critical for trade shows')
                evidence['score'] += 0.30
            
            # Check for dealer/rep portal
            portal_indicators = ['dealer login', 'rep login', 'partner portal', 'sales portal']
            portal_found = any(indicator in text_content for indicator in portal_indicators)
            
            if not portal_found:
                evidence['indicators_found'].append('no_dealer_portal')
                evidence['specific_issues'].append('No dealer/rep portal detected')
                evidence['score'] += 0.25
            
        except Exception as e:
            logger.error(f"Error checking sales enablement: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.7:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.4:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    def _check_technology_indicators(self, domain: str, soup: BeautifulSoup, text_content: str) -> Dict:
        """Check for technology obsolescence indicators"""
        
        evidence = {
            'edp': 'technology_obsolescence',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Check SSL certificate
            if not domain.startswith('https'):
                evidence['indicators_found'].append('no_ssl')
                evidence['specific_issues'].append('No SSL certificate - major security issue')
                evidence['score'] += 0.35

            # Remove misleading page load speed check

            # Check copyright year (search all footer and visible text for year)
            copyright_texts = soup.find_all(string=re.compile(r'©|copyright', re.I))
            found_outdated = False
            for copyright_text in copyright_texts:
                year_match = re.search(r'(\d{4})', copyright_text)
                if year_match:
                    year = int(year_match.group(1))
                    if year < datetime.now().year - 1:
                        evidence['indicators_found'].append('outdated_copyright')
                        evidence['specific_issues'].append(f'Copyright year is {year} - site appears unmaintained')
                        evidence['score'] += 0.20
                        found_outdated = True
                        break

            # Check for modern features
            modern_indicators = ['react', 'vue', 'angular', 'webpack']
            has_modern = any(ind in text_content for ind in modern_indicators)
            
            if not has_modern:
                evidence['indicators_found'].append('no_modern_framework')
                evidence['specific_issues'].append('No modern web framework detected')
                evidence['score'] += 0.20
                
        except Exception as e:
            logger.error(f"Error checking technology: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    def _check_rep_indicators(self, domain: str, soup: BeautifulSoup, text_content: str) -> Dict:
        """Check for rep performance crisis indicators"""
        
        evidence = {
            'edp': 'rep_performance_crisis',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Check for rep locator
            locator_indicators = ['find a rep', 'find a dealer', 'where to buy', 'locate a representative']
            has_locator = any(ind in text_content for ind in locator_indicators)
            
            if not has_locator:
                evidence['indicators_found'].append('no_rep_locator')
                evidence['specific_issues'].append('No rep/dealer locator found')
                evidence['score'] += 0.35
            
            # Check for rep resources
            resource_indicators = ['rep resources', 'sales resources', 'partner resources', 'dealer resources']
            has_resources = any(ind in text_content for ind in resource_indicators)
            
            if not has_resources:
                evidence['indicators_found'].append('no_rep_resources')
                evidence['specific_issues'].append('No dedicated rep resources section')
                evidence['score'] += 0.35
            
            # Check for territory information
            territory_indicators = ['territory', 'territories', 'region', 'coverage area']
            has_territory = any(ind in text_content for ind in territory_indicators)
            
            if not has_territory:
                evidence['indicators_found'].append('no_territory_info')
                evidence['specific_issues'].append('No territory information visible')
                evidence['score'] += 0.30
                
        except Exception as e:
            logger.error(f"Error checking rep indicators: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    def _check_catalog_indicators(self, domain: str, home_soup: BeautifulSoup) -> Dict:
        """Check for SKU complexity indicators"""
        
        evidence = {
            'edp': 'sku_complexity',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Dynamically find the product/catalog page instead of guessing URLs
            product_page_url = self._find_page_by_keywords(domain, ['product', 'catalog', 'shop', 'store'], home_soup)

            if not product_page_url:
                evidence['specific_issues'].append('Could not find a product or catalog page.')
                evidence['score'] += 0.10
                return evidence

            # Use Selenium to fetch fully rendered HTML for the catalog/product page
            html = self._get_dynamic_html(product_page_url)
            soup = BeautifulSoup(html, 'html.parser')

            # Check for filtering options (heuristic: less than 3 is poor for B2B)
            filter_elements = soup.find_all(['select', 'input'], 
                                           attrs={'class': lambda c: c and 'filter' in c.lower()})

            if len(filter_elements) < 3:
                evidence['indicators_found'].append('limited_filtering')
                evidence['specific_issues'].append(f'Only {len(filter_elements)} filter options found on catalog page.')
                evidence['score'] += 0.25

            # Check for product count indicators
            product_count_text = soup.find(text=re.compile(r'\d+\s*(products|items|SKUs)', re.I))
            if product_count_text:
                count_match = re.search(r'(\d+)', product_count_text)
                if count_match:
                    count = int(count_match.group(1))
                    if count > 500: # Adjusted threshold
                        evidence['indicators_found'].append('high_sku_count')
                        evidence['specific_issues'].append(f'Over {count} SKUs detected')
                        evidence['score'] += 0.35

            # Check for configurator
            config_indicators = ['configure', 'customize', 'build your', 'options']
            has_configurator = any(ind in html.lower() for ind in config_indicators)

            if has_configurator:
                evidence['indicators_found'].append('complex_configurations')
                evidence['specific_issues'].append('Product configurator detected - high complexity')
                evidence['score'] += 0.40

        except Exception as e:
            logger.error(f"Error checking catalog: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    # ...existing code...
    # ...existing code...
        
        hooks = []
        
        try:
            # Extract company name
            title = soup.find('title')
            if title:
                hooks.append({
                    'type': 'company_name',
                    'value': title.text.split('|')[0].strip()
                })
            
            # Look for trade shows mentioned
            text_content = soup.get_text().lower()
            trade_shows = ['High Point Market', 'Vegas Market', 'NeoCon', 'Lightovation']
            for show in trade_shows:
                if show.lower() in text_content:
                    hooks.append({
                        'type': 'trade_show',
                        'value': show
                    })
            
            # Extract product categories
            nav = soup.find('nav') or soup.find('div', class_='navigation')
            if nav:
                categories = [a.text.strip() for a in nav.find_all('a')[:5]]
                if categories:
                    hooks.append({
                        'type': 'product_categories',
                        'value': categories
                    })
                    
        except Exception as e:
            logger.error(f"Error extracting personalization: {e}")
        
        return hooks
    
    def _identify_tam_tier_indicators(self, results: Dict) -> Dict:
        """
        Identify which TAM tier this company belongs to
        Based on number and severity of EDPs
        """
        
        tam_indicators = {
            'tier': None,
            'has_multiple_edps': False,
            'total_pain_score': 0
        }
        
        # Count EDPs with meaningful evidence
        active_edps = []
        for edp_name, evidence in results['edp_evidence'].items():
            if evidence.get('score', 0) > 0.3:
                active_edps.append({
                    'name': edp_name,
                    'score': evidence.get('weighted_score', evidence.get('score', 0))
                })
        
        tam_indicators['edp_count'] = len(active_edps)
        tam_indicators['has_multiple_edps'] = len(active_edps) > 1
        
        if active_edps:
            # Sort by score to find primary
            active_edps.sort(key=lambda x: x['score'], reverse=True)
            tam_indicators['primary_edp'] = active_edps[0]['name']
            tam_indicators['total_pain_score'] = sum(e['score'] for e in active_edps)
        
        # Determine TAM tier
        if tam_indicators['total_pain_score'] >= 2.0 or tam_indicators['edp_count'] >= 3:
            tam_indicators['tier'] = 'TIER_1_HOT'
        elif tam_indicators['total_pain_score'] >= 1.0 or tam_indicators['edp_count'] >= 2:
            tam_indicators['tier'] = 'TIER_2_WARM'
        elif tam_indicators['total_pain_score'] >= 0.5:
            tam_indicators['tier'] = 'TIER_3_COOL'
        else:
            tam_indicators['tier'] = 'TIER_4_COLD'
        
        return tam_indicators
    def _find_page_by_keywords(self, domain: str, keywords: List[str], soup: BeautifulSoup) -> Optional[str]:
        """
        Find a page URL by looking for keywords in links
        """
        for keyword in keywords:
            # Look for links containing the keyword
            links = soup.find_all('a', href=True)
            for link in links:
                href = link.get('href', '').lower()
                text = link.get_text().lower()
                if keyword in href or keyword in text:
                    # Build full URL
                    if href.startswith('http'):
                        return href
                    elif href.startswith('/'):
                        return f"{domain.rstrip('/')}{href}"
                    else:
                        return f"{domain.rstrip('/')}/{href}"
        return None

    def _check_channel_indicators(self, domain: str, soup: BeautifulSoup) -> Dict:
        """
        Check for channel conflict indicators
        """
        evidence = {
            'edp': 'channel_conflict',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        try:
            text_content = soup.get_text().lower()
            # Check for multiple login types
            login_types = ['dealer login', 'customer login', 'trade login', 'rep login']
            login_count = sum(1 for login in login_types if login in text_content)
            if login_count >= 2:
                evidence['indicators_found'].append('multiple_portals')
                evidence['specific_issues'].append(f'{login_count} different login portals found')
                evidence['score'] += 0.35
            # Check pricing visibility
            if 'login' in text_content and 'price' in text_content:
                evidence['indicators_found'].append('hidden_pricing')
                evidence['specific_issues'].append('Pricing requires login - channel conflict likely')
                evidence['score'] += 0.30
        except Exception as e:
            logger.error(f"Error in channel check: {e}")
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        else:
            evidence['evidence_strength'] = 'none'
        return evidence
    def _extract_personalization_data(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract specific data points for message personalization"""
        hooks = []
        
        try:
            # Extract company name from title
            title = soup.find('title')
            if title:
                hooks.append({
                    'type': 'company_name',
                    'value': title.text.split('|')[0].strip()
                })
            
            # Look for trade shows mentioned
            text_content = soup.get_text().lower()
            trade_shows = ['vegas market', 'high point market', 'neocon', 'lightovation']
            for show in trade_shows:
                if show.lower() in text_content:
                    hooks.append({
                        'type': 'trade_show',
                        'value': show
                    })
            
            # Extract product categories from navigation
            nav = soup.find('nav') or soup.find('div', class_='navigation')
            if nav:
                categories = [a.text.strip() for a in nav.find_all('a')[:5]]
                if categories:
                    hooks.append({
                        'type': 'product_categories',
                        'value': categories
                    })
                    
        except Exception as e:
            logger.error(f"Error extracting personalization: {e}")
        
        return hooks
```

### supercat_automation/generation/evidence_based_messages.py
```python
# generation/evidence_based_messages.py
"""
Generate hyper-personalized messages using website evidence
Uses actual customer language from 14 won deals
"""

import logging
from typing import Dict, List, Any, Optional
import random
from datetime import datetime, timedelta
from database.connection import db

logger = logging.getLogger(__name__)

class EvidenceBasedMessageGenerator:
    """
    Creates messages using specific website evidence
    Every message references actual problems found
    """
    
    def __init__(self):
        # Actual quotes from 14 won deals
        self.customer_quotes = {
            'sales_enablement_collapse': [
                "taking 1-3 hours daily",
                "reps spending 20% time selling",
                "can't work without WiFi",
                "manually go through spreadsheets"
            ],
            'technology_obsolescence': [
                "old SAP system",
                "not set up for modern",
                "SFTP is ancient technology",
                "40-50% slower"
            ],
            'rep_performance_crisis': [
                "zero visibility into what reps are doing",
                "top reps logging in 10-12 times daily",
                "60+ year old reps don't want to learn",
                "minimal usage in the field"
            ],
            'sku_complexity': [
                "5 different combinations",
                "20 different option sets",
                "2,000-3,000 SKUs",
                "19 levels for fabrics"
            ]
        }
        
        # Proven discovery questions (92% elaboration rate)
        self.discovery_questions = {
            'sales_enablement_collapse': [
                "Walk me through what happens when a rep takes an order at a trade show today?",
                "How long does it take from customer interest to confirmed order?",
                "What happens when your reps don't have WiFi?"
            ],
            'technology_obsolescence': [
                "How many different systems do your reps need to check for one quote?",
                "When did you last lose a deal to a faster competitor?",
                "How long does it take to onboard a new rep to your systems?"
            ],
            'rep_performance_crisis': [
                "How do you currently know what your reps are doing day-to-day?",
                "What percentage of your reps are consistently hitting quota?",
                "How do you identify which reps need help?"
            ],
            'sku_complexity': [
                "How often do orders get revised due to configuration errors?",
                "What's your current return rate due to wrong products shipped?",
                "How long does it take to generate a complex quote?"
            ]
        }
    
    def generate_campaign(self, company_analysis: Dict) -> Dict:
        """
        Generate complete email campaign based on pain analysis
        """
        
        campaign = {
            'company_id': company_analysis.get('company_id'),
            'company_name': company_analysis.get('company_name'),
            'tam_tier': company_analysis.get('tam_tier'),
            'primary_edp': company_analysis.get('primary_edp'),
            'campaign_strategy': self._determine_strategy(company_analysis),
            'email_sequence': [],
            'linkedin_messages': [],
            'call_script': None
        }
        
        # Generate email sequence based on tier
        if company_analysis['tam_tier'] == 'TIER_1_IMMEDIATE':
            campaign['email_sequence'] = self._generate_tier1_sequence(company_analysis)
            campaign['call_script'] = self._generate_call_script(company_analysis)
        elif company_analysis['tam_tier'] == 'TIER_2_QUARTERLY':
            campaign['email_sequence'] = self._generate_tier2_sequence(company_analysis)
        else:
            campaign['email_sequence'] = self._generate_nurture_sequence(company_analysis)
        
        # Generate LinkedIn messages for Tier 1 & 2
        if company_analysis['tam_tier'] in ['TIER_1_IMMEDIATE', 'TIER_2_QUARTERLY']:
            campaign['linkedin_messages'] = self._generate_linkedin_messages(company_analysis)
        
        return campaign
    
    def _determine_strategy(self, analysis: Dict) -> str:
        """Determine outreach strategy based on pain profile"""
        
        if analysis['tam_tier'] == 'TIER_1_IMMEDIATE':
            if analysis.get('has_multiple_edps'):
                return 'AGGRESSIVE_MULTI_PAIN'
            else:
                return 'AGGRESSIVE_SINGLE_PAIN'
        elif analysis['tam_tier'] == 'TIER_2_QUARTERLY':
            return 'EDUCATIONAL'
        else:
            return 'NURTURE'
    
    def _generate_tier1_sequence(self, analysis: Dict) -> List[Dict]:
        """
        Generate aggressive 7-email sequence for Tier 1
        Heavy personalization with specific evidence
        """
        
        sequence = []
        evidence = analysis['evidence']['website'].get('specific_findings', [])
        primary_edp = analysis['primary_edp']
        
        # Email 1: Direct Pain Observation (Day 0)
        sequence.append({
            'day': 0,
            'type': 'pain_observation',
            'subject': self._generate_subject_line(analysis, evidence, 'observation'),
            'body': self._generate_pain_observation_email(analysis, evidence),
            'priority': 'high'
        })
        
        # Email 2: Customer Success Story (Day 2)
        sequence.append({
            'day': 2,
            'type': 'social_proof',
            'subject': self._generate_subject_line(analysis, evidence, 'success'),
            'body': self._generate_success_story_email(analysis, primary_edp),
            'priority': 'high'
        })
        
        # Email 3: ROI Breakdown (Day 5)
        sequence.append({
            'day': 5,
            'type': 'roi',
            'subject': self._generate_subject_line(analysis, evidence, 'roi'),
            'body': self._generate_roi_email(analysis, evidence),
            'priority': 'medium'
        })
        
        # Email 4: Trade Show Urgency (Day 8) - if applicable
        if self._has_upcoming_trade_show(analysis):
            sequence.append({
                'day': 8,
                'type': 'urgency',
                'subject': self._generate_trade_show_subject(analysis),
                'body': self._generate_trade_show_email(analysis, evidence),
                'priority': 'high'
            })
        
        # Email 5: Competitive Threat (Day 12)
        sequence.append({
            'day': 12,
            'type': 'competitive',
            'subject': self._generate_subject_line(analysis, evidence, 'competitive'),
            'body': self._generate_competitive_email(analysis),
            'priority': 'medium'
        })
        
        # Email 6: Final Case Study (Day 16)
        sequence.append({
            'day': 16,
            'type': 'case_study',
            'subject': "How Butler Specialty solved exactly this",
            'body': self._generate_case_study_email(analysis),
            'priority': 'medium'
        })
        
        # Email 7: Break Up (Day 21)
        sequence.append({
            'day': 21,
            'type': 'breakup',
            'subject': "Should I close your file?",
            'body': self._generate_breakup_email(analysis, evidence),
            'priority': 'low'
        })
        
        return sequence
    
    def _generate_subject_line(self, analysis: Dict, evidence: List, email_type: str) -> str:
        """Generate subject line using specific evidence"""
        
        company_name = analysis['company_name']
        
        if email_type == 'observation' and evidence:
            # Use specific evidence in subject
            if any('PDF' in str(e) for e in evidence):
                return f"{company_name} - Your PDF catalog is killing sales"
            elif any('mobile' in str(e).lower() for e in evidence):
                return f"{company_name} - No mobile site for Vegas Market?"
            elif any('SSL' in str(e) for e in evidence):
                return f"URGENT: {company_name}'s site isn't secure"
            else:
                return f"{company_name} - Found {len(evidence)} issues hurting sales"
        
        elif email_type == 'success':
            return f"How {self._get_peer_company(analysis)} solved this"
        
        elif email_type == 'roi':
            return f"{company_name}: Save 3 hours/day per rep"
        
        elif email_type == 'competitive':
            return "Your competitors are 40% faster"
        
        else:
            return f"{company_name} - Time to fix your sales process"
    
    def _generate_pain_observation_email(self, analysis: Dict, evidence: List) -> str:
        """Generate email highlighting specific problems found"""
        
        company_name = analysis['company_name']
        primary_edp = analysis['primary_edp']
        
        # Get relevant customer quote
        customer_quote = random.choice(self.customer_quotes.get(primary_edp, ['manual processes']))
        
        # Build evidence bullets
        evidence_points = ""
        for e in evidence[:3]:  # Top 3 issues
            evidence_points += f"• {e}\n"
        
        email = f"""Hi [First Name],

I just spent 20 minutes on {company_name}'s website and found several issues that are likely costing you significant revenue:

{evidence_points}

This reminds me of what the VP at {self._get_peer_company(analysis)} told me: "{customer_quote}."

They were losing 4 out of 5 opportunities because of these exact issues.

{random.choice(self.discovery_questions[primary_edp])}

Worth a quick call to discuss?

Best,
[Your Name]

P.S. {self._add_ps_line(analysis, evidence)}
"""
        
        return email
    
    def _generate_success_story_email(self, analysis: Dict, primary_edp: str) -> str:
        """Generate email with relevant customer success story"""
        
        success_stories = {
            'sales_enablement_collapse': {
                'company': 'Godinger Silver',
                'person': 'Joel Stern, VP of IT',
                'quote': 'Over the past 25 years, eCat is the best thing that has ever happened to this company. The reps are now mobile. They are in love.',
                'result': 'Reps now spend 80% of time selling vs 20% on admin'
            },
            'technology_obsolescence': {
                'company': 'Universal Furniture',
                'person': 'Their IT Director',
                'quote': 'We went from 40-50% slower than competitors to leading the industry',
                'result': 'Deployed in 3 weeks without replacing their ERP'
            },
            'rep_performance_crisis': {
                'company': 'Theodore Alexander',
                'person': 'Sales Manager',
                'quote': 'Now I know exactly what reps are doing and who needs help',
                'result': 'Rep productivity up 45% in 90 days'
            },
            'sku_complexity': {
                'company': 'Butler Specialty',
                'person': 'Monty Sihweil, President',
                'quote': 'eCat flexibly configures to the way we do business',
                'result': 'Eliminated configuration errors completely'
            }
        }
        
        story = success_stories.get(primary_edp, success_stories['sales_enablement_collapse'])
        
        email = f"""[First Name],

Quick update on how {story['company']} solved the exact problems I noticed on your site.

{story['person']} told me:
"{story['quote']}"

The result? {story['result']}.

They had the same challenges:
- {random.choice(self.customer_quotes[primary_edp])}
- Manual processes killing productivity
- No visibility into field operations

Want to see their implementation playbook?

[Your Name]
"""
        
        return email
    
    def _generate_roi_email(self, analysis: Dict, evidence: List) -> str:
        """Generate ROI-focused email"""
        
        company_name = analysis['company_name']
        
        # Calculate rough ROI based on evidence
        hours_saved = 3  # Conservative estimate
        reps_estimate = 10  # Conservative estimate
        hourly_value = 100  # Loaded cost
        
        annual_savings = hours_saved * reps_estimate * hourly_value * 250  # Working days
        
        email = f"""[First Name],

Let's talk numbers for {company_name}:

Current State (based on your website):
- Manual order processing (3+ hours/day per rep)
- No mobile access for trade shows
- PDF-only resources
- {len(evidence)} critical gaps identified

Potential Impact:
- Time Saved: {hours_saved} hours/day per rep
- Productivity Gain: 40% more selling time
- Error Reduction: 95% fewer order mistakes
- Annual Value: ${annual_savings:,}

Our average customer sees ROI in 47 days.

Want to see the math specific to your situation?

[Your Name]

P.S. With [upcoming trade show] approaching, the timing is critical.
"""
        
        return email
    
    def _generate_trade_show_subject(self, analysis: Dict) -> str:
        """Generate trade show specific subject"""
        
        show = self._get_next_trade_show(analysis)
        days = self._days_until_show(show)
        
        if days < 30:
            return f"URGENT: {days} days until {show}"
        else:
            return f"{show} prep - mobile tools needed"
    
    def _generate_trade_show_email(self, analysis: Dict, evidence: List) -> str:
        """Generate trade show urgency email"""
        
        show = self._get_next_trade_show(analysis)
        days = self._days_until_show(show)
        
        email = f"""[First Name],

{show} is in {days} days.

Your website shows you're not ready:
- No mobile optimization
- PDF-only catalogs
- No offline capability

At your last show, how many orders did you lose because reps couldn't:
- Access real-time inventory?
- Generate accurate quotes?
- Process orders without WiFi?

Your booth investment deserves better tools.

We can get you mobile-ready in 2 weeks. Interested?

[Your Name]
"""
        
        return email
    
    def _generate_competitive_email(self, analysis: Dict) -> str:
        """Generate competitive pressure email"""
        
        email = f"""[First Name],

Your competitors are winning deals while your reps struggle with manual processes.

Industry data:
- Digital-first companies close 40% faster
- Mobile-enabled reps are 3x more productive
- Modern tools reduce errors by 95%

Meanwhile at {analysis['company_name']}:
- Still using {random.choice(['PDFs', 'spreadsheets', 'manual processes'])}
- No mobile capability
- Limited rep visibility

Every day you wait, the gap widens.

Ready to level the playing field?

[Your Name]
"""
        
        return email
    
    def _generate_case_study_email(self, analysis: Dict) -> str:
        """Generate detailed case study email"""
        
        email = f"""[First Name],

Here's the Butler Specialty transformation story:

BEFORE:
- 30% order error rate
- Reps spending hours on admin
- No visibility into field activity
- Trade show chaos

AFTER (90 days):
- Zero configuration errors
- 3 hours/day saved per rep
- Complete visibility into all activity
- Seamless trade show operations

Their President said: "eCat flexibly configures to the way we do business. We are very pleased with what it enables us to do."

Want to see their implementation timeline?

[Your Name]
"""
        
        return email
    
    def _generate_breakup_email(self, analysis: Dict, evidence: List) -> str:
        """Generate breakup email"""
        
        email = f"""[First Name],

I've reached out several times about the issues I found on {analysis['company_name']}'s website.

Maybe fixing these isn't a priority:
{chr(10).join('• ' + str(e) for e in evidence[:3])}

Should I close your file, or is there a better time to discuss?

If you're not the right person, could you point me to who handles sales operations?

[Your Name]

P.S. Your competitors aren't waiting.
"""
        
        return email
    
    def _generate_linkedin_messages(self, analysis: Dict) -> List[Dict]:
        """Generate LinkedIn outreach messages"""
        
        messages = []
        evidence = analysis['evidence']['website'].get('specific_findings', [])
        
        # Connection request
        connection_msg = f"""Hi [First Name],

Noticed {analysis['company_name']}'s {evidence[0] if evidence else 'sales challenges'}. 

We helped {self._get_peer_company(analysis)} solve exactly this. Worth connecting?

[Your Name]"""
        
        messages.append({
            'type': 'connection_request',
            'message': connection_msg[:300]  # LinkedIn limit
        })
        
        # Follow-up message
        followup_msg = f"""Thanks for connecting!

Quick question: {random.choice(self.discovery_questions[analysis['primary_edp']])}

We typically see companies like yours save 3 hours/day per rep.

Open to a brief call?

[Your Name]"""
        
        messages.append({
            'type': 'followup',
            'delay_days': 1,
            'message': followup_msg
        })
        
        return messages
    
    def _generate_call_script(self, analysis: Dict) -> Dict:
        """Generate call script for Tier 1 prospects"""
        
        evidence = analysis['evidence']['website'].get('specific_findings', [])
        
        script = {
            'opening': f"Hi [Name], I'm calling because I noticed {analysis['company_name']} has {evidence[0] if evidence else 'some sales enablement challenges'} on your website.",
            
            'pain_probe': random.choice(self.discovery_questions[analysis['primary_edp']]),
            
            'evidence_points': evidence[:3],
            
            'peer_reference': f"{self._get_peer_company(analysis)} had the same challenge",
            
            'value_prop': "We help furniture and lighting manufacturers eliminate manual order processing and give reps 3 hours back per day.",
            
            'close': "Based on what you've shared, it sounds like we should talk further. Do you have 20 minutes this week for a screen share where I can show you exactly how this works?"
        }
        
        return script
    
    def _generate_tier2_sequence(self, analysis: Dict) -> List[Dict]:
        """Generate educational sequence for Tier 2"""
        
        # Simplified - similar structure but less aggressive
        sequence = []
        
        # Start with education rather than direct pain
        sequence.append({
            'day': 0,
            'type': 'educational',
            'subject': f"Industry insight for {analysis['company_name']}",
            'body': self._generate_educational_email(analysis),
            'priority': 'medium'
        })
        
        # Add 4 more emails over 30 days
        # ... (abbreviated for space)
        
        return sequence
    
    def _generate_nurture_sequence(self, analysis: Dict) -> List[Dict]:
        """Generate light nurture for Tier 3"""
        
        # Quarterly touches with industry insights
        sequence = []
        
        sequence.append({
            'day': 0,
            'type': 'nurture',
            'subject': "Furniture industry sales trends",
            'body': "Industry insight with soft mention of solutions...",
            'priority': 'low'
        })
        
        return sequence
    
    def _generate_educational_email(self, analysis: Dict) -> str:
        """Generate educational email for Tier 2"""
        
        return f"""[First Name],

Thought you might find this interesting...

We just analyzed 100 furniture manufacturers and found:
- 73% still use manual order processing
- Average rep spends 3 hours/day on admin
- 30% error rate at trade shows

{analysis['company_name']} seems to be ahead in some areas but might benefit from seeing what industry leaders are doing.

Interested in the full report?

[Your Name]"""
    
    # Helper methods
    
    def _get_peer_company(self, analysis: Dict) -> str:
        """Get relevant peer company for comparison"""
        
        if 'lighting' in analysis.get('company_name', '').lower():
            return 'Wildwood Lamps'
        elif 'silver' in analysis.get('company_name', '').lower():
            return 'Godinger Silver'
        else:
            return 'Butler Specialty'
    
    def _has_upcoming_trade_show(self, analysis: Dict) -> bool:
        """Check if company has upcoming trade show"""
        
        return bool(analysis.get('evidence', {}).get('trade_show', {}).get('shows'))
    
    def _get_next_trade_show(self, analysis: Dict) -> str:
        """Get next trade show name"""
        
        shows = analysis.get('evidence', {}).get('trade_show', {}).get('shows', [])
        return shows[0] if shows else 'your next trade show'
    
    def _days_until_show(self, show_name: str) -> int:
        """Calculate days until trade show"""
        
        # You'd look this up from database
        show_dates = {
            'High Point Market': 60,
            'Vegas Market': 45,
            'NeoCon': 90
        }
        
        return show_dates.get(show_name, 60)
    
    def _add_ps_line(self, analysis: Dict, evidence: List) -> str:
        """Add PS line based on evidence"""
        
        if self._has_upcoming_trade_show(analysis):
            show = self._get_next_trade_show(analysis)
            return f"With {show} coming up, fixing these issues is critical."
        elif any('SSL' in str(e) for e in evidence):
            return "Your SSL certificate issue is hurting SEO and trust."
        elif any('mobile' in str(e).lower() for e in evidence):
            return "75% of trade show orders are placed via mobile devices now."
```

### supercat_automation/generation/message_generator.py
```python
# generation/message_generator.py
"""
Message generation using exact customer language from won deals
No hypothetical messaging - only proven patterns
"""

import logging
from typing import Dict, List, Any, Optional
import json
import random
from datetime import datetime
from openai import OpenAI
from config.settings import settings
from database.connection import db

logger = logging.getLogger(__name__)

class CustomerValidatedMessageGenerator:
    """
    Generates messages using ONLY language patterns from won deals
    Every hook, question, and response comes from actual customer conversations
    """
    
    def __init__(self):
        """Initialize with OpenAI and customer language library"""
        self.client = OpenAI(api_key=settings.openai_api_key)
        
        # Proven hooks from customer analysis
        self.proven_hooks = {
            'sales_enablement_primary': "Your sales team is wasting 3+ hours daily on manual order processing while competitors using modern tools close deals in minutes.",
            'trade_show_urgency': "At your last trade show, how many opportunities did you lose because reps couldn't access inventory, pricing, or customer history?",
            'technology_gap': "Your legacy systems are making you 40-50% slower than digital-native competitors.",
            'rep_visibility': "You have zero visibility into what your reps are actually doing.",
            'competitive_threat': "While you're updating spreadsheets, nimble competitors are capturing your market share.",
            'sku_complexity': "With {sku_count} SKUs and {config_count} configurations, your error rate is exponential."
        }
        
        # Discovery questions ranked by 92% elaboration rate
        self.discovery_questions = [
            "Walk me through what happens when a rep takes an order at a trade show today?",
            "How long does it take from customer interest to confirmed order?",
            "What percentage of your reps are consistently hitting quota?",
            "How do you currently know what your reps are doing day-to-day?",
            "When did you last lose a deal to a faster competitor?"
        ]
        
        # Objection responses with proven success rates
        self.objection_responses = {
            'need_it_approval': {
                'response': "This replaces spreadsheets, not your ERP. Most customers deploy without IT.",
                'success_rate': 0.73
            },
            'reps_wont_adopt': {
                'response': "Your top reps are begging for this. We'll identify and enable them first.",
                'success_rate': 0.81
            },
            'too_expensive': {
                'response': "You're losing 3 hours daily per rep. That's $40K annually per rep in lost productivity.",
                'success_rate': 0.67
            },
            'wait_for_erp': {
                'response': "This works with your current ERP. Don't let perfect be the enemy of good.",
                'success_rate': 0.71
            }
        }
        
        # Customer success quotes from won deals
        self.customer_quotes = {
            'butler_specialty': "eCat flexibly configures to the way we do business.",
            'godinger_silver': "Over the past 25 years, eCat is the best thing that has ever happened to this company.",
            'wildwood_lamps': "I've reduced by a third the number of calls per day.",
            'universal_furniture': "The reps are now mobile. They are in love."
        }
    
    def generate_campaign(self, 
                          company_data: Dict[str, Any],
                          pain_signals: Dict[str, Any],
                          decision_makers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate complete multi-channel campaign
        Returns messages for email, LinkedIn, and ad suggestions
        """
        try:
            # Identify primary pain to lead with
            primary_pain = pain_signals.get('primary_pain', 'sales_enablement_collapse')
            
            # Generate email sequence
            email_sequence = self.generate_email_sequence(
                company_data, primary_pain, decision_makers
            )
            
            # Generate LinkedIn messages
            linkedin_messages = self.generate_linkedin_messages(
                company_data, primary_pain, decision_makers
            )
            
            # Generate ad copy suggestions
            ad_suggestions = self.generate_ad_suggestions(
                company_data, primary_pain
            )
            
            # Create campaign record
            campaign = {
                'company_id': company_data.get('id'),
                'campaign_type': 'multi_channel',
                'pain_point_focus': primary_pain,
                'primary_hook': self.proven_hooks.get(f"{primary_pain}_primary"),
                'message_variants': {
                    'email': email_sequence,
                    'linkedin': linkedin_messages,
                    'ads': ad_suggestions
                },
                'personalization_tokens': self.extract_personalization_tokens(company_data),
                'scheduled_start': datetime.now().isoformat()
            }
            
            return campaign
            
        except Exception as e:
            logger.error(f"Error generating campaign: {e}")
            return None
    
    def generate_email_sequence(self, 
                                company_data: Dict,
                                primary_pain: str,
                                decision_makers: List[Dict]) -> List[Dict]:
        """Generate 7-touch email sequence using proven patterns"""
        sequence = []
        
        # Email 1: Problem Agitation (Day 0)
        email_1 = self.generate_problem_agitation_email(company_data, primary_pain)
        sequence.append(email_1)
        
        # Email 2: Social Proof (Day 3)
        email_2 = self.generate_social_proof_email(company_data, primary_pain)
        sequence.append(email_2)
        
        # Email 3: ROI Focus (Day 7)
        email_3 = self.generate_roi_email(company_data, primary_pain)
        sequence.append(email_3)
        
        # Email 4: Competitive Threat (Day 10)
        email_4 = self.generate_competitive_email(company_data)
        sequence.append(email_4)
        
        # Email 5: Case Study (Day 14)
        email_5 = self.generate_case_study_email(company_data, primary_pain)
        sequence.append(email_5)
        
        # Email 6: Urgency (Day 18)
        email_6 = self.generate_urgency_email(company_data)
        sequence.append(email_6)
        
        # Email 7: Break Up (Day 21)
        email_7 = self.generate_breakup_email(company_data)
        sequence.append(email_7)
        
        return sequence
    
    def generate_problem_agitation_email(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate problem agitation email using customer language"""
        
        # Build context for GPT-4
        prompt = f"""
        Generate a SHORT (under 100 words) email for {company_data.get('company_name')}.
        
        Their primary pain: {primary_pain}
        Company details:
        - Industry: {company_data.get('industry', 'Furniture/Lighting')}
        - Employees: {company_data.get('employee_count', 'Unknown')}
        - SKUs: {company_data.get('catalog_sku_count', 'Unknown')}
        - Uses: {company_data.get('current_erp', 'legacy system')}
        
        Use this EXACT hook: "{self.proven_hooks.get(f'{primary_pain}_primary', self.proven_hooks['sales_enablement_primary'])}"
        
        Structure:
        1. Address the pain directly
        2. Quantify the impact
        3. Ask: "{random.choice(self.discovery_questions)}"
        
        Keep it conversational, not salesy.
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You are a B2B sales expert who uses customer language."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        body = response.choices[0].message.content
        
        # Generate subject line
        subject = self.generate_subject_line(company_data, primary_pain, 'problem')
        
        return {
            'sequence_step': 1,
            'send_day': 0,
            'subject': subject,
            'body': body,
            'variant': 'problem_agitation',
            'personalization_tokens': {
                'company_name': company_data.get('company_name'),
                'sku_count': company_data.get('catalog_sku_count'),
                'current_system': company_data.get('current_erp')
            }
        }
    
    def generate_social_proof_email(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate social proof email with real customer quotes"""
        
        # Select relevant customer quote
        if 'sku' in primary_pain or 'complex' in primary_pain:
            quote_company = 'butler_specialty'
        elif 'technology' in primary_pain:
            quote_company = 'godinger_silver'
        else:
            quote_company = 'wildwood_lamps'
        
        quote = self.customer_quotes[quote_company]
        
        prompt = f"""
        Generate a SHORT email (under 100 words) featuring this EXACT customer quote:
        "{quote}" - {quote_company.replace('_', ' ').title()}
        
        Context:
        - Company: {company_data.get('company_name')}
        - Their pain: {primary_pain}
        
        Structure:
        1. Reference their specific situation
        2. Share the customer quote
        3. Connect it to their problem
        4. Simple CTA: "Worth a quick call?"
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You are sharing customer success stories."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        return {
            'sequence_step': 2,
            'send_day': 3,
            'subject': f"How {quote_company.replace('_', ' ').title()} solved this",
            'body': response.choices[0].message.content,
            'variant': 'social_proof'
        }
    
    def generate_subject_line(self, company_data: Dict, primary_pain: str, email_type: str) -> str:
        """Generate subject line based on proven patterns"""
        
        subject_templates = {
            'problem': [
                "Your {pain_metric} is costing {company} ${impact}",
                "{Company} - {specific_number} {time_unit} wasted daily",
                "Re: {Company}'s {next_trade_show} preparation"
            ],
            'social_proof': [
                "How {similar_company} solved {specific_problem}",
                '"Best thing in 25 years" - {role} at {similar_company}',
                "{Company} - see how others fixed this"
            ],
            'roi': [
                "ROI calculator for {Company}",
                "{Company}: {money_saved} in productivity gains",
                "The math on your {pain_point} problem"
            ],
            'competitive': [
                "Your competitors are {specific_advantage}",
                "While {Company} uses {old_method}...",
                "{Company} falling behind on {specific_metric}"
            ]
        }
        
        # Select template
        templates = subject_templates.get(email_type, subject_templates['problem'])
        template = random.choice(templates)
        
        # Fill in variables
        subject = template.format(
            company=company_data.get('company_name', 'your company'),
            Company=company_data.get('company_name', 'Your company'),
            pain_metric=primary_pain.replace('_', ' '),
            impact=random.choice(['400K annually', '3 hours daily', '30% of revenue']),
            specific_number=random.choice(['3', '5', '15']),
            time_unit=random.choice(['hours', 'days']),
            next_trade_show=random.choice(['Vegas Market', 'High Point', 'trade show']),
            similar_company=random.choice(['Butler Specialty', 'Godinger', 'a competitor']),
            specific_problem='manual order processing',
            role='VP',
            money_saved='$40K per rep',
            pain_point=primary_pain.replace('_', ' '),
            specific_advantage='40% faster',
            old_method='spreadsheets',
            specific_metric='order processing'
        )
        
        return subject[:100]  # Keep under 100 chars
    
    def generate_linkedin_messages(self, 
                                   company_data: Dict,
                                   primary_pain: str,
                                   decision_makers: List[Dict]) -> List[Dict]:
        """Generate LinkedIn outreach messages"""
        messages = []
        
        for dm in decision_makers[:3]:  # Top 3 decision makers
            # Connection request
            connection_request = self.generate_linkedin_connection(company_data, dm, primary_pain)
            messages.append(connection_request)
            
            # Follow-up message
            follow_up = self.generate_linkedin_followup(company_data, dm, primary_pain)
            messages.append(follow_up)
        
        return messages
    
    def generate_linkedin_connection(self, company_data: Dict, decision_maker: Dict, primary_pain: str) -> Dict:
        """Generate LinkedIn connection request (300 chars max)"""
        
        templates = [
            "Hi {first_name}, noticed {company}'s impressive growth. {pain_observation}. Would love to share how similar companies streamlined this.",
            "Hi {first_name}, saw {company} at {trade_show}. {pain_observation}. Have insights from working with {similar_company}.",
            "{first_name}, managing {challenge} at {company}? Helped {similar_company} solve exactly this. Worth connecting?"
        ]
        
        template = random.choice(templates)
        
        # Map pain to observation
        pain_observations = {
            'sales_enablement_collapse': "Managing complex orders manually must be challenging",
            'technology_obsolescence': "Legacy systems holding you back",
            'rep_performance_crisis': "Tracking rep performance across territories",
            'sku_complexity': f"With {company_data.get('catalog_sku_count', 'thousands of')} SKUs"
        }
        
        message = template.format(
            first_name=decision_maker.get('first_name', 'there'),
            company=company_data.get('company_name'),
            trade_show='Vegas Market',
            pain_observation=pain_observations.get(primary_pain, "Scaling operations"),
            similar_company=random.choice(['Butler Specialty', 'Godinger', 'Universal']),
            challenge=primary_pain.replace('_', ' ')
        )
        
        return {
            'type': 'connection_request',
            'decision_maker_id': decision_maker.get('id'),
            'message': message[:300],  # LinkedIn limit
            'send_day': 0
        }
    
    def generate_ad_suggestions(self, company_data: Dict, primary_pain: str) -> List[Dict]:
        """Generate ad copy suggestions for partner team"""
        ad_suggestions = []
        
        # Google Search Ads
        google_ads = self.generate_google_ad_copy(company_data, primary_pain)
        ad_suggestions.append(google_ads)
        
        # Meta/Facebook Ads
        meta_ads = self.generate_meta_ad_copy(company_data, primary_pain)
        ad_suggestions.append(meta_ads)
        
        # LinkedIn Ads
        linkedin_ads = self.generate_linkedin_ad_copy(company_data, primary_pain)
        ad_suggestions.append(linkedin_ads)
        
        return ad_suggestions
    
    def generate_google_ad_copy(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate Google Ads copy"""
        
        headlines = {
            'sales_enablement_collapse': [
                "Stop Wasting 3 Hours Daily",
                "Trade Show Order Chaos?",
                "Manual Orders Killing Sales?"
            ],
            'technology_obsolescence': [
                "Escape Legacy System Prison",
                "40% Faster Than Spreadsheets",
                "Modern Sales Without New ERP"
            ]
        }
        
        descriptions = {
            'sales_enablement_collapse': [
                "Give reps 15 hours weekly back. Work offline at trade shows. Perfect order accuracy.",
                "Transform manual order processing. Real customer: 'Best thing in 25 years.'"
            ],
            'technology_obsolescence': [
                "Works with your current ERP. No IT project. Deploy in 3 weeks not 18 months.",
                "Stop losing to digital-native competitors. Modernize sales without replacing systems."
            ]
        }
        
        return {
            'platform': 'google',
            'ad_type': 'search',
            'headlines': headlines.get(primary_pain, headlines['sales_enablement_collapse']),
            'descriptions': descriptions.get(primary_pain, descriptions['sales_enablement_collapse']),
            'display_url': 'supercatsolutions.com/demo',
            'final_url': f'https://supercatsolutions.com/demo?utm_source=google&utm_medium=cpc&utm_campaign={primary_pain}',
            'keywords': [
                'B2B order management',
                'sales enablement software',
                'trade show order app',
                'furniture sales software',
                'wholesale order management'
            ],
            'negative_keywords': ['free', 'cheap', 'jobs', 'careers'],
            'suggested_bid': 8.50,
            'suggested_daily_budget': 150
        }
    
    def extract_personalization_tokens(self, company_data: Dict) -> Dict:
        """Extract all personalization tokens for merge tags"""
        return {
            'company_name': company_data.get('company_name'),
            'industry': company_data.get('industry'),
            'employee_count': company_data.get('employee_count'),
            'sku_count': company_data.get('catalog_sku_count'),
            'current_erp': company_data.get('current_erp'),
            'trade_show_count': company_data.get('trade_show_count_annual'),
            'rep_count': company_data.get('field_sales_count'),
            'years_in_business': datetime.now().year - company_data.get('year_founded', datetime.now().year)
        }
```

### supercat_automation/generation/email_sequences.py
```python

```

### supercat_automation/generation/__init__.py
```python

```

### supercat_automation/generation/ad_copy_generator.py
```python
# generation/ad_copy_generator.py
"""
Generate ad copy for multiple platforms
"""

from typing import Dict, List

class AdCopyGenerator:
    def generate_google_ads(self, company: Dict, pain: str) -> Dict:
        """Generate Google Ads copy"""
        
        headlines = {
            'sales_enablement_collapse': [
                "Stop Wasting 3 Hours Daily",
                "Trade Show Order Chaos?",
                "Manual Orders Killing Sales?"
            ],
            'technology_obsolescence': [
                "Escape Legacy System Prison",
                "40% Faster Than Spreadsheets",
                "Modern Sales Without New ERP"
            ]
        }
        
        descriptions = [
            "Give reps 15 hours weekly back. Work offline at trade shows.",
            "Transform manual orders. Real customer: 'Best thing in 25 years.'"
        ]
        
        return {
            'platform': 'google',
            'headlines': headlines.get(pain, headlines['sales_enablement_collapse']),
            'descriptions': descriptions,
            'display_url': 'supercatsolutions.com/demo',
            'keywords': [
                'B2B order management',
                'trade show order app',
                'furniture sales software'
            ]
        }
    
    def generate_meta_ads(self, company: Dict, pain: str) -> Dict:
        """Generate Meta/Facebook ads"""
        
        return {
            'platform': 'meta',
            'primary_text': f"Still processing orders manually? {company.get('company_name')} could save 3 hours daily per rep.",
            'headline': "Transform Your Sales Process",
            'description': "Join Butler Specialty and 100+ manufacturers",
            'cta': 'Learn More'
        }
    
    def generate_linkedin_ads(self, company: Dict, pain: str) -> Dict:
        """Generate LinkedIn ads"""
        
        return {
            'platform': 'linkedin',
            'intro_text': "Is manual order processing killing your sales productivity?",
            'headline': "Give Your Reps 15 Hours Back Weekly",
            'description': "Supercat Solutions helps furniture manufacturers eliminate order chaos"
        }
```

### supercat_automation/generation/linkedin_messages.py
```python
# generation/linkedin_messages.py
"""
LinkedIn message generation with templates
"""

from typing import Dict, List
import random

class LinkedInMessageGenerator:
    def __init__(self):
        self.connection_templates = [
            "Hi {first_name}, noticed {company}'s growth in {industry}. {pain_hook}. Worth connecting?",
            "{first_name}, managing {challenge} at {company}? Have insights from similar companies.",
            "Hi {first_name}, saw {company} at {trade_show}. {pain_hook}. Would love to share insights."
        ]
        
        self.followup_templates = [
            "Thanks for connecting! {discovery_question} Happy to share how {peer_company} solved this.",
            "Appreciate the connection! Quick question: {discovery_question}",
            "Great to connect! {pain_observation}. Open to a brief call?"
        ]
    
    def generate_connection_request(self, company: Dict, contact: Dict, pain: str) -> str:
        """Generate connection request (300 char max)"""
        
        template = random.choice(self.connection_templates)
        
        pain_hooks = {
            'sales_enablement_collapse': "Managing orders manually must be challenging",
            'technology_obsolescence': "Legacy systems holding growth back",
            'rep_performance_crisis': "Tracking rep performance across territories",
            'sku_complexity': f"With thousands of SKUs to manage"
        }
        
        message = template.format(
            first_name=contact.get('first_name', 'there'),
            company=company.get('company_name'),
            industry='furniture/lighting',
            trade_show='Vegas Market',
            pain_hook=pain_hooks.get(pain, "Scaling operations"),
            challenge=pain.replace('_', ' ')
        )
        
        return message[:300]
    
    def generate_followup(self, company: Dict, contact: Dict, pain: str) -> str:
        """Generate follow-up message"""
        
        template = random.choice(self.followup_templates)
        
        discovery_questions = {
            'sales_enablement_collapse': "How do reps handle orders at trade shows?",
            'technology_obsolescence': "How many systems do reps check for one quote?",
            'rep_performance_crisis': "How do you track rep activity?",
            'sku_complexity': "How often do configuration errors occur?"
        }
        
        message = template.format(
            discovery_question=discovery_questions.get(pain),
            peer_company='Butler Specialty',
            pain_observation=f"I see {company.get('company_name')} faces {pain.replace('_', ' ')}"
        )
        
        return message
```

### supercat_automation/generation/pvp_ad_generator.py
```python
# generation/pvp_ad_generator.py
"""
PVP-Quality Ad Copy Generator
Creates hyper-specific ads based on company evidence
"""

import logging
from typing import Dict, List, Any
import json

logger = logging.getLogger(__name__)

class PVPAdGenerator:
    """
    Generates evidence-based ad copy for multiple platforms
    Every ad references specific pain points and evidence
    """
    
    def generate_full_ad_campaign(self, company_analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate complete ad campaign across all platforms
        """
        
        ad_campaign = {
            'company_name': company_analysis['company_name'],
            'campaign_name': f"{company_analysis['company_name']}_PVP_{company_analysis['primary_edp']}",
            'google_ads': self._generate_google_ads_pvp(company_analysis, evidence),
            'meta_ads': self._generate_meta_ads_pvp(company_analysis, evidence),
            'linkedin_ads': self._generate_linkedin_ads_pvp(company_analysis, evidence),
            'display_ads': self._generate_display_ads_pvp(company_analysis, evidence),
            'retargeting': self._generate_retargeting_ads(company_analysis, evidence)
        }
        
        return ad_campaign
    
    def _generate_google_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate Google Ads with specific evidence
        """
        
        company_name = analysis['company_name']
        primary_edp = analysis['primary_edp']
        
        # Build specific headlines based on evidence
        headlines = []
        
        if evidence.get('website_findings'):
            for finding in evidence['website_findings'][:3]:
                if 'PDF' in finding:
                    headlines.append(f"{company_name}: Stop PDF Chaos")
                    headlines.append("PDF Catalogs Killing Sales?")
                elif 'mobile' in finding.lower():
                    headlines.append(f"{company_name}: No Mobile = Lost Sales")
                    headlines.append("Trade Shows Need Mobile")
                elif 'manual' in finding.lower():
                    headlines.append("3 Hours Daily Wasted")
                    headlines.append(f"{company_name}: Manual Orders?")
        
        # Add trade show specific if applicable
        if evidence.get('trade_show_data'):
            show = evidence['trade_show_data']['show_name']
            days = evidence['trade_show_data'].get('days_until_show', 35)
            headlines.append(f"{days} Days Until {show}")
            headlines.append(f"Booth #{evidence['trade_show_data'].get('booth_number', 'C-1055')} Ready?")
        
        # Fallback headlines
        if len(headlines) < 5:
            headlines.extend([
                "Furniture Sales Automation",
                "Stop Manual Order Processing",
                "Mobile Sales Enablement"
            ])
        
        # Descriptions based on evidence
        descriptions = []
        
        if evidence.get('trade_show_data'):
            booth_cost = evidence['trade_show_data'].get('booth_details', {}).get('estimated_cost', 32000)
            descriptions.append(
                f"Your ${booth_cost:,} booth investment needs mobile tools. "
                f"Work offline. Perfect accuracy. Setup in 14 days."
            )
        
        if 'manual' in str(evidence.get('website_findings', [])):
            descriptions.append(
                f"{company_name}: Save 3 hours daily per rep. "
                f"Eliminate order errors. Real customer: 'Best thing in 25 years.'"
            )
        
        descriptions.append(
            f"Built for {company_name}'s exact needs. "
            f"Works with your ERP. No IT project. See ROI in 47 days."
        )
        
        return {
            'platform': 'google_ads',
            'campaign_type': 'search',
            'ad_groups': [
                {
                    'name': f"{company_name}_Brand",
                    'headlines': headlines[:5],  # Google allows up to 15, we'll use 5
                    'descriptions': descriptions[:2],  # Google allows up to 4, we'll use 2
                    'display_url': f"supercatsolutions.com/{company_name.lower().replace(' ', '')}",
                    'final_url': f"https://supercatsolutions.com/demo?company={company_name}&utm_source=google&utm_medium=cpc&utm_campaign=pvp_{primary_edp}",
                    'keywords': self._generate_specific_keywords(analysis, evidence),
                    'negative_keywords': ['free', 'cheap', 'jobs', 'careers', 'used'],
                    'targeting': {
                        'company_name': company_name,
                        'radius': '50 miles',
                        'audience': 'furniture_manufacturers'
                    }
                }
            ],
            'extensions': {
                'sitelinks': [
                    {'text': 'See ROI Calculator', 'url': '/roi-calculator'},
                    {'text': 'Trade Show Solution', 'url': '/trade-show'},
                    {'text': 'Customer Success', 'url': '/customers'},
                    {'text': 'Book Demo', 'url': '/demo'}
                ],
                'callouts': [
                    'Works Offline',
                    'No IT Required',
                    'ROI in 47 Days',
                    'Perfect Order Accuracy'
                ],
                'structured_snippets': {
                    'header': 'Features',
                    'values': ['Mobile Orders', 'Offline Mode', 'ERP Integration', 'Trade Show Ready']
                }
            },
            'budget': {
                'daily': 150,
                'monthly': 4500,
                'bid_strategy': 'maximize_conversions',
                'target_cpa': 250
            }
        }
    
    def _generate_meta_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate Meta (Facebook/Instagram) ads with specific evidence
        """
        
        company_name = analysis['company_name']
        
        # Primary text with specific evidence
        primary_text_options = []
        
        if evidence.get('website_findings'):
            finding = evidence['website_findings'][0]
            primary_text_options.append(
                f"Still using {finding.lower()}? "
                f"{company_name} could save 3 hours daily per rep with mobile order management. "
                f"Butler Specialty called it 'the best thing in 25 years.'"
            )
        
        if evidence.get('trade_show_data'):
            show_data = evidence['trade_show_data']
            primary_text_options.append(
                f"📍 {company_name} - Booth #{show_data.get('booth_number', 'C-1055')} at {show_data['show_name']}\n\n"
                f"With {show_data.get('days_until_show', 35)} days until setup, you need mobile order capability. "
                f"Your ${show_data.get('booth_details', {}).get('estimated_cost', 32000):,} investment deserves better than paper forms.\n\n"
                f"✅ Work completely offline\n"
                f"✅ Perfect order accuracy\n"
                f"✅ Setup in 14 days"
            )
        
        # Carousel cards with specific pain points
        carousel_cards = []
        
        for i, finding in enumerate(evidence.get('website_findings', [])[:3]):
            carousel_cards.append({
                'headline': f"Problem #{i+1}",
                'description': finding,
                'cta': 'Fix This Issue'
            })
        
        # Add ROI card
        roi_data = self._calculate_simple_roi(analysis)
        carousel_cards.append({
            'headline': f"Save ${roi_data['annual_savings']:,}",
            'description': f"ROI in {roi_data['payback_days']} days",
            'cta': 'Calculate Your ROI'
        })
        
        return {
            'platform': 'meta',
            'campaign_objectives': ['lead_generation', 'traffic'],
            'ad_sets': [
                {
                    'name': f"{company_name}_Lookalike",
                    'targeting': {
                        'custom_audiences': [f"{company_name}_website_visitors"],
                        'lookalike_audiences': ['furniture_manufacturers_1%'],
                        'location': self._get_company_location(analysis),
                        'age': '25-65',
                        'interests': ['B2B', 'Trade Shows', 'Manufacturing', 'Sales Management'],
                        'behaviors': ['Business Decision Makers'],
                        'job_titles': ['VP Sales', 'Sales Director', 'IT Director', 'President', 'Owner']
                    },
                    'placements': ['facebook_feed', 'instagram_feed', 'audience_network'],
                    'budget': {
                        'daily': 100,
                        'bid_strategy': 'lowest_cost_with_bid_cap',
                        'bid_cap': 50
                    }
                }
            ],
            'creatives': [
                {
                    'format': 'single_image',
                    'primary_text': primary_text_options[0] if primary_text_options else f"{company_name}: Transform your sales process",
                    'headline': f"{company_name}: Save 3 Hours Daily",
                    'description': 'Mobile order management for furniture manufacturers',
                    'cta_button': 'Learn More',
                    'image_specs': {
                        'main_text': f"{company_name}\n3 Hours Saved Daily",
                        'subtext': 'Per Sales Rep',
                        'background': 'gradient_blue',
                        'logo_placement': 'bottom_right'
                    }
                },
                {
                    'format': 'carousel',
                    'cards': carousel_cards,
                    'primary_text': primary_text_options[1] if len(primary_text_options) > 1 else primary_text_options[0],
                    'headline': 'Fix These Issues Now',
                    'cta_button': 'Get Started'
                },
                {
                    'format': 'video',
                    'video_script': self._generate_video_script(analysis, evidence),
                    'primary_text': f"{company_name}: See how Butler Specialty transformed their sales",
                    'headline': 'Transform Sales in 14 Days',
                    'cta_button': 'Watch Demo'
                }
            ],
            'tracking': {
                'pixel_events': ['ViewContent', 'Lead', 'CompleteRegistration'],
                'utm_parameters': {
                    'source': 'meta',
                    'medium': 'paid_social',
                    'campaign': f'pvp_{company_name.lower().replace(" ", "_")}',
                    'content': '{creative_name}'
                }
            }
        }
    
    def _generate_linkedin_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate LinkedIn ads targeting specific company and competitors
        """
        
        company_name = analysis['company_name']
        
        # Intro text with specific pain point
        intro_texts = []
        
        if evidence.get('website_findings'):
            intro_texts.append(
                f"Attention {company_name} sales team:\n\n"
                f"Still struggling with {evidence['website_findings'][0].lower()}?"
            )
        
        if evidence.get('trade_show_data'):
            show = evidence['trade_show_data']['show_name']
            intro_texts.append(
                f"Preparing for {show}?\n\n"
                f"Don't let manual processes ruin your ${evidence['trade_show_data'].get('booth_details', {}).get('estimated_cost', 32000):,} investment."
            )
        
        return {
            'platform': 'linkedin',
            'campaign_type': 'sponsored_content',
            'objective': 'lead_generation',
            'formats': [
                {
                    'type': 'single_image',
                    'intro_text': intro_texts[0] if intro_texts else f"{company_name}: Transform your sales process",
                    'headline': f"{company_name}: Eliminate Manual Order Processing",
                    'description': 'Join Butler Specialty and 100+ manufacturers who transformed their sales',
                    'cta': 'Download Guide'
                },
                {
                    'type': 'conversation_ad',
                    'intro_message': f"Hi! I noticed {company_name} still uses manual order processing. Interested in seeing how similar companies save 3 hours daily?",
                    'cta_options': [
                        {'text': 'Yes, show me how', 'next': 'case_study'},
                        {'text': 'What about trade shows?', 'next': 'trade_show_info'},
                        {'text': 'Not interested', 'next': 'close'}
                    ],
                    'conversation_flows': {
                        'case_study': "Butler Specialty eliminated all order errors and saved 3 hours daily per rep. Here's their story: [Link]",
                        'trade_show_info': f"With {evidence.get('trade_show_data', {}).get('days_until_show', 35)} days until your next show, you need mobile capability. We can set you up in 14 days.",
                        'close': "No problem! Feel free to reach out if priorities change."
                    }
                },
                {
                    'type': 'document_ad',
                    'document_title': f"{company_name} Sales Transformation Guide",
                    'document_description': 'How to eliminate manual processing and save 3 hours daily',
                    'intro_text': f"Created specifically for {company_name} based on your current challenges"
                }
            ],
            'targeting': {
                'account_targeting': [
                    {'company_name': company_name, 'priority': 'high'},
                    {'company_names': self._get_competitor_names(analysis), 'priority': 'medium'}
                ],
                'job_functions': ['Sales', 'Information Technology', 'Operations'],
                'seniority': ['Director', 'VP', 'CXO', 'Owner'],
                'company_size': '50-500',
                'industries': ['Furniture Manufacturing', 'Wholesale', 'Manufacturing'],
                'member_traits': {
                    'groups': ['Furniture Industry Professionals', 'B2B Sales Leaders'],
                    'skills': ['Sales Management', 'ERP', 'Supply Chain']
                }
            },
            'budget': {
                'daily': 75,
                'total': 2250,
                'bid_type': 'automated',
                'optimization_goal': 'lead_generation'
            },
            'lead_gen_form': {
                'headline': f"Get {company_name}'s Custom ROI Analysis",
                'description': 'See exactly how much you could save',
                'fields': [
                    'first_name',
                    'last_name',
                    'email',
                    'company',
                    'job_title',
                    'phone'
                ],
                'custom_questions': [
                    {
                        'question': 'How many sales reps do you have?',
                        'type': 'multiple_choice',
                        'options': ['1-5', '6-10', '11-20', '20+']
                    },
                    {
                        'question': 'Which trade shows do you attend?',
                        'type': 'multiple_choice',
                        'options': ['Vegas Market', 'High Point', 'NeoCon', 'Other']
                    }
                ],
                'privacy_policy_url': 'https://supercatsolutions.com/privacy',
                'thank_you_message': "Thanks! We'll send your custom ROI analysis within 24 hours."
            }
        }
    
    def _generate_display_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate display/banner ads for retargeting
        """
        
        company_name = analysis['company_name']
        
        banner_messages = []
        
        if evidence.get('trade_show_data'):
            days = evidence['trade_show_data'].get('days_until_show', 35)
            banner_messages.append({
                'headline': f"{company_name}: {days} Days Until {evidence['trade_show_data']['show_name']}",
                'subtext': "Get Mobile-Ready Now",
                'cta': 'Start Free Trial'
            })
        
        if evidence.get('website_findings'):
            for finding in evidence['website_findings'][:2]:
                if 'PDF' in finding:
                    banner_messages.append({
                        'headline': f"{company_name}: Ditch The PDFs",
                        'subtext': "Go Digital in 14 Days",
                        'cta': 'Learn How'
                    })
                elif 'manual' in finding.lower():
                    banner_messages.append({
                        'headline': "Stop Wasting 3 Hours Daily",
                        'subtext': f"{company_name} Could Save ${self._calculate_simple_roi(analysis)['annual_savings']:,}",
                        'cta': 'Calculate Savings'
                    })
        
        return {
            'platform': 'display_network',
            'campaign_type': 'remarketing',
            'ad_sizes': [
                {
                    'size': '728x90',
                    'name': 'leaderboard',
                    'message': banner_messages[0] if banner_messages else {
                        'headline': f"{company_name}: Transform Your Sales",
                        'subtext': "Mobile Order Management",
                        'cta': 'Learn More'
                    }
                },
                {
                    'size': '300x250',
                    'name': 'medium_rectangle',
                    'message': banner_messages[1] if len(banner_messages) > 1 else banner_messages[0]
                },
                {
                    'size': '336x280',
                    'name': 'large_rectangle',
                    'message': banner_messages[0]
                },
                {
                    'size': '300x600',
                    'name': 'half_page',
                    'message': self._create_vertical_banner(analysis, evidence)
                },
                {
                    'size': '320x50',
                    'name': 'mobile_banner',
                    'message': {
                        'headline': f"{company_name}: Mobile Sales",
                        'cta': 'Start Now'
                    }
                }
            ],
            'targeting': {
                'remarketing_lists': [
                    f"{company_name}_website_visitors",
                    f"{company_name}_email_opens",
                    'competitor_visitors'
                ],
                'frequency_cap': {
                    'impressions': 5,
                    'time_period': 'day'
                },
                'placements': {
                    'websites': ['industry_publications', 'trade_publications'],
                    'exclude': ['competitor_sites', 'negative_content']
                }
            },
            'creative_rotation': {
                'method': 'optimize',
                'test_variants': 3
            }
        }
    
    def _generate_retargeting_ads(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate retargeting sequences based on behavior
        """
        
        company_name = analysis['company_name']
        
        return {
            'platform': 'multi_platform_retargeting',
            'sequences': [
                {
                    'trigger': 'visited_pricing_page',
                    'sequence': [
                        {
                            'day': 0,
                            'message': f"{company_name}: See Your Custom Pricing",
                            'platform': 'display'
                        },
                        {
                            'day': 2,
                            'message': f"ROI Calculator Ready for {company_name}",
                            'platform': 'facebook'
                        },
                        {
                            'day': 5,
                            'message': "Last Chance: 20% Off First Year",
                            'platform': 'google'
                        }
                    ]
                },
                {
                    'trigger': 'downloaded_guide',
                    'sequence': [
                        {
                            'day': 1,
                            'message': "Ready to See a Demo?",
                            'platform': 'email'
                        },
                        {
                            'day': 3,
                            'message': f"{company_name}: Your Questions Answered",
                            'platform': 'linkedin'
                        },
                        {
                            'day': 7,
                            'message': "Schedule Your Custom Demo",
                            'platform': 'display'
                        }
                    ]
                },
                {
                    'trigger': 'abandoned_demo_form',
                    'sequence': [
                        {
                            'day': 0,
                            'message': "Still There? Let's Chat",
                            'platform': 'chat_widget'
                        },
                        {
                            'day': 1,
                            'message': f"{company_name}: Quick Question?",
                            'platform': 'email'
                        },
                        {
                            'day': 3,
                            'message': "15-Minute Demo Available",
                            'platform': 'calendar_popup'
                        }
                    ]
                }
            ],
            'dynamic_creative': {
                'use_ai_optimization': True,
                'test_elements': ['headline', 'image', 'cta'],
                'learning_period': 7
            }
        }
    
    def _generate_video_script(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate video ad script with specific pain points
        """
        
        company_name = analysis['company_name']
        
        script = {
            'duration': '30_seconds',
            'scenes': [
                {
                    'time': '0-3s',
                    'visual': f"Text overlay: '{company_name}'",
                    'voiceover': f"{company_name}...",
                    'text_overlay': company_name
                },
                {
                    'time': '3-8s',
                    'visual': 'Sales rep struggling with paper forms at trade show',
                    'voiceover': f"Still losing orders to manual processing?",
                    'text_overlay': evidence['website_findings'][0] if evidence.get('website_findings') else "Manual Order Chaos"
                },
                {
                    'time': '8-15s',
                    'visual': 'Split screen: Paper chaos vs. Digital ease',
                    'voiceover': "Your competitors are 40% faster with digital tools",
                    'text_overlay': "40% Faster Sales Cycles"
                },
                {
                    'time': '15-22s',
                    'visual': 'Happy sales rep using tablet',
                    'voiceover': "Join Butler Specialty and 100+ manufacturers",
                    'text_overlay': "'Best thing in 25 years' - Joel, Godinger"
                },
                {
                    'time': '22-28s',
                    'visual': 'ROI numbers animating',
                    'voiceover': f"Save ${self._calculate_simple_roi(analysis)['annual_savings']:,} annually",
                    'text_overlay': f"ROI in {self._calculate_simple_roi(analysis)['payback_days']} Days"
                },
                {
                    'time': '28-30s',
                    'visual': 'Logo and CTA',
                    'voiceover': "Transform your sales now",
                    'text_overlay': "Get Demo → supercatsolutions.com"
                }
            ],
            'music': 'upbeat_corporate',
            'style': 'professional_b2b',
            'cta_overlay': {
                'start': 25,
                'text': 'Get Your Demo',
                'url': f'https://supercatsolutions.com/demo?company={company_name}'
            }
        }
        
        return script
    
    def _generate_specific_keywords(self, analysis: Dict, evidence: Dict) -> List[str]:
        """
        Generate specific keywords based on evidence
        """
        
        keywords = [
            f'"{analysis["company_name"]}"',
            f'{analysis["company_name"]} sales software',
            f'{analysis["company_name"]} order management'
        ]
        
        # Add pain-specific keywords
        if 'PDF' in str(evidence.get('website_findings', [])):
            keywords.extend([
                'replace pdf catalog',
                'digital catalog software',
                'pdf to digital catalog'
            ])
        
        if 'manual' in str(evidence.get('website_findings', [])):
            keywords.extend([
                'manual order processing',
                'automate sales orders',
                'digital order forms'
            ])
        
        if evidence.get('trade_show_data'):
            keywords.extend([
                f'{evidence["trade_show_data"]["show_name"]} order app',
                'trade show order management',
                'offline order app'
            ])
        
        # Add competitor keywords
        keywords.extend([
            'supercat alternatives',
            'ecat software',
            'b2b order management'
        ])
        
        return keywords
    
    def _calculate_simple_roi(self, analysis: Dict) -> Dict:
        """
        Quick ROI calculation for ad copy
        """
        
        employees = analysis.get('employee_count', 50)
        reps = max(5, employees // 10)  # Estimate reps
        
        annual_savings = reps * 3 * 100 * 250  # reps * hours * rate * days
        investment = 15000 * (reps // 5)  # Scale by company
        payback_days = int((investment / annual_savings) * 365)
        
        return {
            'annual_savings': annual_savings,
            'investment': investment,
            'payback_days': payback_days
        }
    
    def _get_company_location(self, analysis: Dict) -> str:
        """
        Get company location for targeting
        """
        # This would look up actual location
        # For now, return general area
        return "United States"
    
    def _get_competitor_names(self, analysis: Dict) -> List[str]:
        """
        Get competitor names for targeting
        """
        # This would do competitive research
        return [
            'Universal Furniture',
            'Hooker Furniture',
            'Butler Specialty',
            'Lexington Home Brands'
        ]
    
    def _create_vertical_banner(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Create vertical banner message for half-page ad
        """
        
        return {
            'headline': f"{analysis['company_name']}:",
            'points': [
                "Save 3 Hours Daily",
                "Perfect Order Accuracy",
                "Works Offline",
                "ROI in 47 Days"
            ],
            'cta': 'Transform Your Sales'
        }
```

### supercat_automation/generation/pvp_message_generator.py
```python
# generation/pvp_message_generator.py
"""
True PVP (Permissionless Value Proposition) Message Generator
Creates hyper-specific, evidence-based outreach that demonstrates deep research
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)

class PVPMessageGenerator:
    """
    Generates TRUE PVP messages with specific, researched evidence
    Every message must reference actual findings from website/data analysis
    """
    
    def __init__(self):
        self.message_quality_threshold = 0.8  # Messages must score 80%+ on specificity
    
    def generate_pvp_campaign(self, company_analysis: Dict) -> Dict:
        """
        Generate high-quality PVP campaign with deep personalization
        """
        
        # Extract ALL available evidence
        evidence = self._extract_all_evidence(company_analysis)
        
        if not evidence['has_sufficient_evidence']:
            logger.warning(f"Insufficient evidence for {company_analysis['company_name']} - need more research")
            return self._request_additional_research(company_analysis)
        
        # Build PVP campaign
        campaign = {
            'company_id': company_analysis.get('company_id'),
            'company_name': company_analysis.get('company_name'),
            'campaign_type': 'pvp_evidence_based',
            'evidence_used': evidence,
            'email_sequence': self._generate_pvp_email_sequence(company_analysis, evidence),
            'linkedin_messages': self._generate_pvp_linkedin_messages(company_analysis, evidence),
            'quality_score': self._calculate_message_quality(evidence)
        }
        
        return campaign
    
    def _extract_all_evidence(self, analysis: Dict) -> Dict:
        """
        Extract ALL available evidence for personalization
        """
        
        evidence = {
            'website_findings': [],
            'trade_show_data': {},
            'competitive_intel': {},
            'financial_indicators': {},
            'specific_pain_evidence': {},
            'personalization_hooks': [],
            'has_sufficient_evidence': False
        }
        
        # Website evidence
        if analysis.get('evidence', {}).get('website'):
            website_data = analysis['evidence']['website']
            
            # Extract specific findings
            for finding in website_data.get('specific_findings', []):
                evidence['website_findings'].append(finding)
            
            # Extract personalization hooks
            for hook in website_data.get('personalization_hooks', []):
                evidence['personalization_hooks'].append(hook)
        
        # Trade show evidence
        if analysis.get('trade_shows'):
            evidence['trade_show_data'] = self._research_trade_show_specifics(
                analysis['company_name'],
                analysis['trade_shows']
            )
        
        # Pain-specific evidence
        primary_edp = analysis.get('primary_edp')
        if primary_edp:
            evidence['specific_pain_evidence'] = self._get_pain_specific_evidence(
                analysis,
                primary_edp
            )
        
        # Determine if we have enough
        evidence['has_sufficient_evidence'] = (
            len(evidence['website_findings']) >= 3 or
            len(evidence['personalization_hooks']) >= 2 or
            bool(evidence['trade_show_data'].get('booth_details'))
        )
        
        return evidence
    
    def _generate_pvp_email_sequence(self, analysis: Dict, evidence: Dict) -> List[Dict]:
        """
        Generate truly personalized emails with specific evidence
        """
        
        sequence = []
        company_name = analysis['company_name']
        
        # Email 1: Ultra-specific observation
        sequence.append(self._generate_observation_email(analysis, evidence))
        
        # Email 2: Competitive intelligence
        sequence.append(self._generate_competitive_intel_email(analysis, evidence))
        
        # Email 3: Trade show specific (if applicable)
        if evidence['trade_show_data']:
            sequence.append(self._generate_trade_show_specific_email(analysis, evidence))
        
        # Email 4: ROI with their numbers
        sequence.append(self._generate_specific_roi_email(analysis, evidence))
        
        # Email 5: Direct challenge
        sequence.append(self._generate_challenge_email(analysis, evidence))
        
        return sequence
    
    def _generate_observation_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate email with specific observations from research
        """
        
        company_name = analysis['company_name']
        website_findings = evidence['website_findings']
        
        # Build specific observations
        observations = []
        for finding in website_findings[:3]:
            observations.append(f"• {finding}")
        
        if evidence['trade_show_data'].get('booth_details'):
            booth = evidence['trade_show_data']['booth_details']
            observations.append(
                f"• Your {booth.get('size', 'booth')} booth in {booth.get('location', 'Building C')} "
                f"(#{booth.get('number', 'C-1055')}) represents a ${booth.get('estimated_cost', '32,000'):,} investment"
            )
        
        subject = self._generate_pvp_subject(analysis, evidence, 'observation')
        
        body = f"""Hi {{{{first_name}}}},

I spent 20 minutes researching {company_name}'s sales operations and found several specific issues:

{chr(10).join(observations)}

Based on your {evidence.get('personalization_hooks', [{}])[0].get('value', 'catalog structure')}, I calculate you're losing approximately ${self._calculate_specific_loss(analysis, evidence):,} annually from these inefficiencies.

{self._get_specific_question(analysis, evidence)}

Worth 15 minutes to review the analysis?

Best,
{{{{sender_name}}}}

P.S. {self._add_specific_ps(analysis, evidence)}
"""
        
        return {
            'day': 0,
            'subject': subject,
            'body': body,
            'evidence_used': observations,
            'personalization_score': self._score_personalization(body)
        }
    
    def _generate_competitive_intel_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate email with specific competitive intelligence
        """
        
        company_name = analysis['company_name']
        
        # Research actual competitors
        competitors = self._research_competitors(analysis)
        
        subject = f"{company_name} falling behind {competitors[0]['name']}"
        
        body = f"""{{{{first_name}}}},

Quick update on your competitive landscape:

{competitors[0]['name']} just implemented mobile order management and reported:
- 47% reduction in order processing time
- 31% increase in trade show orders
- 3.2 hours saved per rep daily

{competitors[1]['name']} went further:
- Completely eliminated paper catalogs
- 0% error rate on configured products
- 62% faster quote-to-order cycle

Meanwhile, {company_name} still:
{chr(10).join('• ' + f for f in evidence['website_findings'][:2])}

Your current approach is making you 40-50% slower than these competitors.

Want to see exactly what they're doing differently?

{{{{sender_name}}}}
"""
        
        return {
            'day': 3,
            'subject': subject,
            'body': body,
            'competitive_data': competitors
        }
    
    def _generate_trade_show_specific_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate email with exact trade show details
        """
        
        company_name = analysis['company_name']
        show_data = evidence['trade_show_data']
        
        # Calculate specific metrics
        days_until = show_data.get('days_until_show', 35)
        booth_cost = show_data.get('booth_details', {}).get('estimated_cost', 32000)
        
        subject = f"{days_until} days: Your {show_data['show_name']} booth #{show_data.get('booth_number', 'C-1055')}"
        
        body = f"""{{{{first_name}}}},

Your {show_data['show_name']} investment breakdown:

Booth {show_data.get('booth_number', 'C-1055')} ({show_data.get('booth_size', '20x20')}):
- Location: {show_data.get('building', 'Building C')} - {show_data.get('traffic_analysis', '18% less traffic than Building A')}
- Investment: ${booth_cost:,}
- Expected visitors: {show_data.get('expected_visitors', '4,200')}
- Your category buyers: {show_data.get('category_buyers', '~800')}

Based on your current setup:
- No mobile order capability (confirmed on your website)
- Paper catalogs only (per your PDF downloads)
- No offline functionality

At $8,500 average order value, every minute of processing delay = 1 lost opportunity.

With {days_until} days until setup, you have 2 options:
1. Another year of paper chaos and lost orders
2. Mobile-ready in 14 days

Which makes more sense for your ${booth_cost:,} investment?

{{{{sender_name}}}}
"""
        
        return {
            'day': 7,
            'subject': subject,
            'body': body,
            'urgency_factor': self._calculate_urgency(days_until)
        }
    
    def _generate_specific_roi_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate ROI email with company-specific numbers
        """
        
        company_name = analysis['company_name']
        
        # Calculate specific ROI based on their data
        roi_data = self._calculate_company_specific_roi(analysis, evidence)
        
        subject = f"{company_name}: ${roi_data['annual_savings']:,} in documented savings"
        
        body = f"""{{{{first_name}}}},

Here's the ROI math specific to {company_name}:

YOUR CURRENT COSTS (based on research):
- Order errors ({roi_data['error_rate']}% rate): ${roi_data['error_cost']:,}/year
- Processing time (3 hrs/day/rep): ${roi_data['time_cost']:,}/year  
- Lost trade show orders: ${roi_data['trade_show_loss']:,}/year
- Total annual loss: ${roi_data['total_loss']:,}

WITH SUPERCAT:
- Order errors: <1% (${roi_data['new_error_cost']:,})
- Processing time: 30 min/day (${roi_data['new_time_cost']:,})
- Trade show capture: 95% (${roi_data['new_trade_show_loss']:,})
- Annual savings: ${roi_data['annual_savings']:,}

ROI Timeline:
- Investment: ${roi_data['investment']:,}
- Payback period: {roi_data['payback_days']} days
- 3-year ROI: {roi_data['three_year_roi']}%

Want to verify these numbers together?

{{{{sender_name}}}}

Calculation details: Based on {roi_data['assumptions']}
"""
        
        return {
            'day': 10,
            'subject': subject,
            'body': body,
            'roi_data': roi_data
        }
    
    def _generate_challenge_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate direct challenge email
        """
        
        company_name = analysis['company_name']
        primary_challenge = self._identify_primary_challenge(analysis, evidence)
        
        subject = f"Can {company_name} survive another year like this?"
        
        body = f"""{{{{first_name}}}},

Honest question:

{primary_challenge['question']}

Because here's what I see:
{chr(10).join('• ' + point for point in primary_challenge['evidence_points'])}

{primary_challenge['competitor_comparison']}

At what point does this become unsustainable?

I've helped 14 companies in your exact situation. Every one waited too long.

If you're ready to fix this: [Calendar Link]

If not, when will you be?

{{{{sender_name}}}}

P.S. {primary_challenge['ps_line']}
"""
        
        return {
            'day': 14,
            'subject': subject,
            'body': body,
            'challenge_type': primary_challenge['type']
        }
    
    def _generate_pvp_linkedin_messages(self, analysis: Dict, evidence: Dict) -> List[Dict]:
        """
        Generate LinkedIn messages with specific evidence
        """
        
        messages = []
        
        # Connection request with specific observation
        connection = f"""Hi {{{{first_name}}}},

Noticed {analysis['company_name']}'s booth #{evidence.get('trade_show_data', {}).get('booth_number', 'C-1055')} at {evidence.get('trade_show_data', {}).get('show_name', 'High Point')}.

Also saw you're still using {evidence['website_findings'][0] if evidence['website_findings'] else 'manual processes'}.

Have insights from helping Butler Specialty solve exactly this. Worth connecting?
"""
        
        messages.append({
            'type': 'connection_request',
            'message': connection[:300]  # LinkedIn limit
        })
        
        # Follow-up with specific question
        followup = f"""Thanks for connecting!

Quick question: {self._get_specific_question(analysis, evidence)}

The reason I ask - we helped {self._get_relevant_peer(analysis)} reduce order processing from 3 hours to 20 minutes.

They had the same {analysis['primary_edp'].replace('_', ' ')} challenges.

Open to a brief call to share their playbook?
"""
        
        messages.append({
            'type': 'follow_up',
            'message': followup,
            'send_day': 1
        })
        
        return messages
    
    # Helper methods for specific research
    
    def _research_trade_show_specifics(self, company_name: str, trade_shows: List[str]) -> Dict:
        """
        Research specific trade show details for the company
        """
        
        # This would query your database or external sources
        # For now, returning example structure
        
        show_data = {
            'show_name': trade_shows[0] if trade_shows else 'High Point Market',
            'days_until_show': 35,
            'booth_details': {
                'number': 'C-1055',
                'size': '20x20',
                'location': 'Building C',
                'estimated_cost': 32000,
                'traffic_analysis': '18% less traffic than Building A'
            },
            'expected_visitors': 4200,
            'category_buyers': 800,
            'competitor_presence': [
                'Hooker Furniture - Booth A-200',
                'Universal Furniture - Booth A-100'
            ]
        }
        
        return show_data
    
    def _research_competitors(self, analysis: Dict) -> List[Dict]:
        """
        Research actual competitors and their initiatives
        """
        
        # This would do real competitive research
        # For now, returning structured example
        
        competitors = [
            {
                'name': 'Universal Furniture',
                'recent_initiative': 'Implemented mobile order management',
                'reported_results': {
                    'order_time_reduction': '47%',
                    'trade_show_increase': '31%',
                    'rep_time_saved': '3.2 hours/day'
                }
            },
            {
                'name': 'Hooker Furniture',
                'recent_initiative': 'Digital catalog transformation',
                'reported_results': {
                    'paper_elimination': '100%',
                    'error_rate': '0%',
                    'cycle_time_improvement': '62%'
                }
            }
        ]
        
        return competitors
    
    def _calculate_specific_loss(self, analysis: Dict, evidence: Dict) -> int:
        """
        Calculate specific annual loss based on evidence
        """
        
        # Base calculations on actual company data
        base_loss = 100000  # Conservative base
        
        # Add multipliers based on evidence
        if 'no_mobile' in str(evidence['website_findings']):
            base_loss *= 1.5
        
        if 'PDF' in str(evidence['website_findings']):
            base_loss *= 1.3
        
        if evidence.get('trade_show_data'):
            base_loss *= 1.4
        
        return int(base_loss)
    
    def _calculate_company_specific_roi(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Calculate ROI with company-specific data
        """
        
        # Use actual company metrics where available
        employee_count = analysis.get('employee_count', 50)
        sku_count = analysis.get('catalog_sku_count', 2000)
        
        # Calculate based on their specifics
        roi_data = {
            'error_rate': 30 if 'manual' in str(evidence['website_findings']) else 15,
            'error_cost': int(sku_count * 0.3 * 420),  # SKUs * error rate * cost per error
            'time_cost': int(employee_count * 0.2 * 3 * 100 * 250),  # Reps * hours * rate * days
            'trade_show_loss': 50000 if evidence.get('trade_show_data') else 0,
            'total_loss': 0,
            'annual_savings': 0,
            'investment': 15000 * (employee_count // 10),  # Scale by company size
            'payback_days': 0,
            'three_year_roi': 0,
            'assumptions': f"Based on {employee_count} employees, {sku_count} SKUs"
        }
        
        roi_data['total_loss'] = roi_data['error_cost'] + roi_data['time_cost'] + roi_data['trade_show_loss']
        roi_data['new_error_cost'] = int(roi_data['error_cost'] * 0.05)
        roi_data['new_time_cost'] = int(roi_data['time_cost'] * 0.2)
        roi_data['new_trade_show_loss'] = int(roi_data['trade_show_loss'] * 0.1)
        roi_data['annual_savings'] = roi_data['total_loss'] - (roi_data['new_error_cost'] + roi_data['new_time_cost'] + roi_data['new_trade_show_loss'])
        roi_data['payback_days'] = int((roi_data['investment'] / roi_data['annual_savings']) * 365)
        roi_data['three_year_roi'] = int((roi_data['annual_savings'] * 3 - roi_data['investment']) / roi_data['investment'] * 100)
        
        return roi_data
    
    def _get_specific_question(self, analysis: Dict, evidence: Dict) -> str:
        """
        Generate specific discovery question based on evidence
        """
        
        if 'PDF' in str(evidence['website_findings']):
            return "How many hours do your reps spend downloading and searching through PDFs daily?"
        
        elif 'no_mobile' in str(evidence['website_findings']):
            return "What happens when reps need to quote a custom configuration at a trade show?"
        
        elif evidence.get('trade_show_data'):
            return f"How many orders did you lose at last year's {evidence['trade_show_data']['show_name']} due to processing delays?"
        
        else:
            return "Walk me through what happens when a rep needs to create a complex quote on-site?"
    
    def _add_specific_ps(self, analysis: Dict, evidence: Dict) -> str:
        """
        Add specific PS line based on evidence
        """
        
        if evidence.get('trade_show_data'):
            days = evidence['trade_show_data'].get('days_until_show', 35)
            return f"With only {days} days until {evidence['trade_show_data']['show_name']}, timing is critical."
        
        elif 'no_ssl' in str(evidence['website_findings']):
            return "Your missing SSL certificate is also hurting your Google rankings and customer trust."
        
        elif 'outdated_copyright' in str(evidence['website_findings']):
            return "Your copyright still shows 2019 - customers notice these details."
        
        else:
            return "Your competitors aren't waiting to modernize."
    
    def _generate_pvp_subject(self, analysis: Dict, evidence: Dict, email_type: str) -> str:
        """
        Generate specific subject line with evidence
        """
        
        company_name = analysis['company_name']
        
        if email_type == 'observation' and evidence['website_findings']:
            finding = evidence['website_findings'][0]
            if 'PDF' in finding:
                return f"{company_name}'s 47 PDF downloads = lost revenue"
            elif 'mobile' in finding.lower():
                return f"{company_name} losing trade show orders (no mobile)"
            else:
                return f"{company_name}: Found {len(evidence['website_findings'])} fixable revenue leaks"
        
        elif evidence.get('trade_show_data'):
            show = evidence['trade_show_data']['show_name']
            days = evidence['trade_show_data'].get('days_until_show', 35)
            return f"{days} days: {company_name}'s {show} readiness"
        
        else:
            return f"{company_name}: Your {analysis['primary_edp'].replace('_', ' ')}"
    
    def _identify_primary_challenge(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Identify the primary challenge to focus on
        """
        
        challenge = {
            'type': analysis['primary_edp'],
            'question': '',
            'evidence_points': [],
            'competitor_comparison': '',
            'ps_line': ''
        }
        
        if analysis['primary_edp'] == 'sales_enablement_collapse':
            challenge['question'] = "How long can you accept 3+ hours of daily admin work per rep?"
            challenge['evidence_points'] = evidence['website_findings'][:3]
            challenge['competitor_comparison'] = "Universal Furniture reps now spend 80% of time selling vs your 20%."
            challenge['ps_line'] = "Every day you wait costs you $1,600 in lost productivity."
        
        elif analysis['primary_edp'] == 'technology_obsolescence':
            challenge['question'] = "When will your legacy systems become completely uncompetitive?"
            challenge['evidence_points'] = ["Still using " + f for f in evidence['website_findings'][:2]]
            challenge['competitor_comparison'] = "Digital-native competitors are 40% faster to quote."
            challenge['ps_line'] = "Your technology gap is widening daily."
        
        return challenge
    
    def _get_relevant_peer(self, analysis: Dict) -> str:
        """
        Get relevant peer company for comparison
        """
        
        if 'furniture' in analysis.get('company_name', '').lower():
            return 'Butler Specialty'
        elif 'lighting' in analysis.get('company_name', '').lower():
            return 'Wildwood Lamps'
        else:
            return 'Godinger Silver'
    
    def _score_personalization(self, message: str) -> float:
        """
        Score how personalized the message is
        """
        
        score = 0.0
        
        # Check for specific evidence
        if 'booth #' in message.lower():
            score += 0.2
        if '$' in message and ',' in message:  # Specific dollar amounts
            score += 0.2
        if any(word in message.lower() for word in ['pdf', 'manual', 'spreadsheet', 'paper']):
            score += 0.15
        if 'building' in message.lower() and any(char.isupper() for char in message):
            score += 0.15
        if '%' in message:  # Specific percentages
            score += 0.15
        if 'days' in message and any(char.isdigit() for char in message):
            score += 0.15
        
        return min(score, 1.0)
    
    def _calculate_message_quality(self, evidence: Dict) -> float:
        """
        Calculate overall message quality score
        """
        
        score = 0.0
        
        # Evidence completeness
        if len(evidence['website_findings']) >= 3:
            score += 0.3
        if evidence.get('trade_show_data', {}).get('booth_details'):
            score += 0.3
        if len(evidence.get('personalization_hooks', [])) >= 2:
            score += 0.2
        if evidence.get('competitive_intel'):
            score += 0.2
        
        return min(score, 1.0)
    
    def _request_additional_research(self, analysis: Dict) -> Dict:
        """
        Request additional research when evidence insufficient
        """
        
        return {
            'status': 'insufficient_evidence',
            'company_name': analysis['company_name'],
            'needed_research': [
                'Deep website analysis for specific pain evidence',
                'Trade show booth research and investment calculation',
                'Competitive intelligence on peer companies',
                'LinkedIn research for decision maker details'
            ],
            'message': 'Need more research before creating PVP campaign'
        }
    
    def _calculate_urgency(self, days_until_event: int) -> str:
        """
        Calculate urgency level based on days
        """
        
        if days_until_event <= 14:
            return 'critical'
        elif days_until_event <= 30:
            return 'high'
        elif days_until_event <= 60:
            return 'medium'
        else:
            return 'low'
```

## Configuration Files

### supercat_automation/pipeline_results_20250823_074654.json
```json
{
  "stats": {
    "processed": 72,
    "qualified": 20,
    "sent_to_clay": 20,
    "saved_to_supabase": 0,
    "errors": []
  },
  "webhooks": [
    {
      "company_id": "csv_0003",
      "company_name": "A & B HOME GROUP, INC.",
      "domain": "abhomeinc.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.05929919137466,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Emad",
        "last_name": "Botros",
        "email": "emadb@abhongda.net",
        "title": "Director of Operations & Logistics",
        "linkedin": "https://www.linkedin.com/in/emadbotors/"
      },
      "company_info": {
        "industry": "Wholesale",
        "employee_count": 43
      },
      "analyzed_at": "2025-08-23T07:44:13.555736"
    },
    {
      "company_id": "csv_0009",
      "company_name": "Atkore",
      "domain": "atkore.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.436657681940698,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.5,
        "technology_obsolescence": 0,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "Manual quote request process"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Eric",
        "last_name": "Banks",
        "email": "ebanks@atkore.com",
        "title": "Vice President, Operations",
        "linkedin": "https://www.linkedin.com/in/ericbanks1775/"
      },
      "company_info": {
        "industry": "Appliances, Electrical, and Electronics Manufacturing",
        "employee_count": 1969
      },
      "analyzed_at": "2025-08-23T07:44:23.064266"
    },
    {
      "company_id": "csv_0016",
      "company_name": "Century Furniture",
      "domain": "centuryfurniture.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 31.132075471698112,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.6,
        "technology_obsolescence": 0,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "PDF-only catalogs detected"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Alesia",
        "last_name": "Smith",
        "email": "asmith@centuryfurniture.com",
        "title": "Research And Development Assistant",
        "linkedin": "https://www.linkedin.com/in/alesia-smith-416766155/"
      },
      "company_info": {
        "industry": "Furniture",
        "employee_count": 347
      },
      "analyzed_at": "2025-08-23T07:44:33.726934"
    },
    {
      "company_id": "csv_0017",
      "company_name": "Coaster Company of America",
      "domain": "coasterfurniture.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 33.423180592991905,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.5,
        "technology_obsolescence": 0,
        "rep_performance_crisis": 0.5,
        "sku_complexity": 0.4,
        "channel_conflict": 0.3
      },
      "key_evidence": [
        "No product search functionality",
        "Manual dealer login system"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Nelson",
        "last_name": "Lc",
        "email": "nlc@coasteramer.com",
        "title": "Director",
        "linkedin": "https://www.linkedin.com/in/nelson-lc-294a7537/"
      },
      "company_info": {
        "industry": "Furniture",
        "employee_count": 327
      },
      "analyzed_at": "2025-08-23T07:44:36.062219"
    },
    {
      "company_id": "csv_0020",
      "company_name": "Dovetail Furniture Pvt Ltd",
      "domain": "dovetail.in",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.05929919137466,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Radhakrishnan",
        "last_name": "Nair",
        "email": "rkn@dovetail.in",
        "title": "Chief Operating Officer",
        "linkedin": "https://www.linkedin.com/in/radhakrishnan-nair-96796214b/"
      },
      "company_info": {
        "industry": "Furniture and Home Furnishings Manufacturing",
        "employee_count": 29
      },
      "analyzed_at": "2025-08-23T07:44:52.433271"
    },
    {
      "company_id": "csv_0022",
      "company_name": "World of Eichholtz",
      "domain": "eichholtz.com",
      "tam_tier": "TIER_2_ACTIVE",
      "psi_score": 38.65229110512129,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.6,
        "technology_obsolescence": 0.3,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "PDF-only catalogs detected"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Dennis",
        "last_name": "Hendriks ",
        "email": "dhendriks@eichholtzusa.com",
        "title": "Vice President Operations",
        "linkedin": "https://www.linkedin.com/in/dennis-hendriks-523684263/"
      },
      "company_info": {
        "industry": "Furniture and Home Furnishings Manufacturing",
        "employee_count": 170
      },
      "analyzed_at": "2025-08-23T07:44:58.215571"
    },
    {
      "company_id": "csv_0025",
      "company_name": "Fairmont Designs",
      "domain": "fairmontdesignshospitality.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.05929919137466,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Jason",
        "last_name": "Liu",
        "email": "jasonliu@fairmontdesigns.com",
        "title": "CEO",
        "linkedin": "https://www.linkedin.com/in/jason-liu-086a4025/"
      },
      "company_info": {
        "industry": "Furniture",
        "employee_count": 111
      },
      "analyzed_at": "2025-08-23T07:45:04.048718"
    },
    {
      "company_id": "csv_0026",
      "company_name": "Fanimation",
      "domain": "fanimation.com",
      "tam_tier": "TIER_2_ACTIVE",
      "psi_score": 36.14555256064689,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.6,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "PDF-only catalogs detected"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Christopher",
        "last_name": "Wheeler",
        "email": "chris.wheeler@fanimation.com",
        "title": "Vice President Operations",
        "linkedin": "https://www.linkedin.com/in/christopher-wheeler45/"
      },
      "company_info": {
        "industry": "Manufacturing",
        "employee_count": 63
      },
      "analyzed_at": "2025-08-23T07:45:05.708639"
    },
    {
      "company_id": "csv_0028",
      "company_name": "F&H Group A/S",
      "domain": "fh-group.dk",
      "tam_tier": "TIER_2_ACTIVE",
      "psi_score": 38.436657681940694,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.5,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.5,
        "sku_complexity": 0.4,
        "channel_conflict": 0.3
      },
      "key_evidence": [
        "No product search functionality",
        "Manual dealer login system"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Kim",
        "last_name": "Dybdal",
        "email": "d.kim@fh-group.dk",
        "title": "Head of Export",
        "linkedin": "https://www.linkedin.com/in/kim-dybdal-6323aa14/"
      },
      "company_info": {
        "industry": "Wholesale",
        "employee_count": 294
      },
      "analyzed_at": "2025-08-23T07:45:14.058189"
    },
    {
      "company_id": "csv_0034",
      "company_name": "Kaleen Rugs",
      "domain": "kaleen.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 30.566037735849054,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.3,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "No SSL certificate"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Radhe",
        "last_name": "Rathi",
        "email": "radhe.rathi@kaleen.com",
        "title": "Director",
        "linkedin": "https://www.linkedin.com/in/radhe-rathi-23437676/"
      },
      "company_info": {
        "industry": "Textile Manufacturing",
        "employee_count": 97
      },
      "analyzed_at": "2025-08-23T07:45:23.126856"
    },
    {
      "company_id": "csv_0035",
      "company_name": "Keystone Collections Group",
      "domain": "keystonecollects.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.05929919137466,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "David",
        "last_name": "Kratzenberg",
        "email": "dwkratzenberg@keystonecollects.com",
        "title": "Chief Executive Officer",
        "linkedin": "https://www.linkedin.com/in/david-kratzenberg-a82b25173/"
      },
      "company_info": {
        "industry": "Financial Services",
        "employee_count": 107
      },
      "analyzed_at": "2025-08-23T07:45:24.783242"
    },
    {
      "company_id": "csv_0038",
      "company_name": "OFS",
      "domain": "ofs.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 31.132075471698112,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.6,
        "technology_obsolescence": 0,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "PDF-only catalogs detected"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Adam",
        "last_name": "Bedell",
        "email": "abedell@ofs.com",
        "title": "Regional Vice President -Northeast ",
        "linkedin": "https://www.linkedin.com/in/adambedell/"
      },
      "company_info": {
        "industry": "Furniture",
        "employee_count": 829
      },
      "analyzed_at": "2025-08-23T07:45:31.762509"
    },
    {
      "company_id": "csv_0041",
      "company_name": "Outdoor Interiors",
      "domain": "outdoorinteriors.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.05929919137466,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Samantha",
        "last_name": "Scott",
        "email": "sscott@outdoorinteriors.com",
        "title": "Vice President Sales and Operations",
        "linkedin": "https://www.linkedin.com/in/samantha-scott-2950/"
      },
      "company_info": {
        "industry": "Furniture",
        "employee_count": 9
      },
      "analyzed_at": "2025-08-23T07:45:42.514743"
    },
    {
      "company_id": "csv_0043",
      "company_name": "Porcelanosa",
      "domain": "porcelanosa.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 30.566037735849054,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.3,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Manuel",
        "last_name": "Prior Diago",
        "email": "mprior@porcelanosa.com",
        "title": "Executive Director",
        "linkedin": "https://www.linkedin.com/in/manuel-prior-diago-739823211/"
      },
      "company_info": {
        "industry": "Construction",
        "employee_count": 3296
      },
      "analyzed_at": "2025-08-23T07:45:46.647305"
    },
    {
      "company_id": "csv_0046",
      "company_name": "Green Furniture Concept",
      "domain": "greenfc.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.05929919137466,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Joakim",
        "last_name": "Lundgren",
        "email": "joakim.lundgren@greenfc.com",
        "title": "Head of Design & Sustainability",
        "linkedin": "https://www.linkedin.com/in/joakim-lundgren-a4a3954b/"
      },
      "company_info": {
        "industry": "Furniture and Home Furnishings Manufacturing",
        "employee_count": 39
      },
      "analyzed_at": "2025-08-23T07:45:54.162262"
    },
    {
      "company_id": "csv_0048",
      "company_name": "Quorum",
      "domain": "quorum.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 33.45013477088949,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.5,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "Manual quote request process"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Jim",
        "last_name": "Garn",
        "email": "jim.garn@quorum.com",
        "title": "Chief Executive Officer",
        "linkedin": "https://www.linkedin.com/in/jimgarn/"
      },
      "company_info": {
        "industry": "IT Services and IT Consulting",
        "employee_count": 65
      },
      "analyzed_at": "2025-08-23T07:45:58.860504"
    },
    {
      "company_id": "csv_0052",
      "company_name": "Okamura",
      "domain": "okamura.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 28.05929919137466,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.3,
        "technology_obsolescence": 0.2,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Ayumu",
        "last_name": "Nagai",
        "email": "ayumu.nagai@us.okamura.com",
        "title": "Vice President, North America",
        "linkedin": "https://www.linkedin.com/in/ayumu-nagai-821491113/"
      },
      "company_info": {
        "industry": "Office Furniture and Fixtures Manufacturing",
        "employee_count": 236
      },
      "analyzed_at": "2025-08-23T07:46:09.400322"
    },
    {
      "company_id": "csv_0058",
      "company_name": "Vice President Business Development",
      "domain": "sunnydesigns.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 31.132075471698112,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.6,
        "technology_obsolescence": 0,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "PDF-only catalogs detected"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Bill",
        "last_name": "Caples",
        "email": "bcaples@greentouchhome.com",
        "title": "Vice President of Business Development",
        "linkedin": "https://www.linkedin.com/in/billcaples/"
      },
      "company_info": {
        "industry": "Furniture and Home Furnishings Manufacturing",
        "employee_count": 37
      },
      "analyzed_at": "2025-08-23T07:46:19.659778"
    },
    {
      "company_id": "csv_0064",
      "company_name": "Acme furniture",
      "domain": "acmecorp.com",
      "tam_tier": "TIER_3_NURTURE",
      "psi_score": 31.132075471698112,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.6,
        "technology_obsolescence": 0,
        "rep_performance_crisis": 0.3,
        "sku_complexity": 0.4,
        "channel_conflict": 0.2
      },
      "key_evidence": [
        "No product search functionality",
        "PDF-only catalogs detected"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Eric",
        "last_name": "Wang",
        "email": "eric.wang@acmecorp.com",
        "title": "VP Sales",
        "linkedin": "https://www.linkedin.com/in/eric-wang-6b554829/"
      },
      "company_info": {
        "industry": "Wholesale",
        "employee_count": 110
      },
      "analyzed_at": "2025-08-23T07:46:29.818241"
    },
    {
      "company_id": "csv_0065",
      "company_name": "Steve Silver Company",
      "domain": "stevesilver.com",
      "tam_tier": "TIER_2_ACTIVE",
      "psi_score": 45.95687331536388,
      "primary_edp": "sales_enablement_collapse",
      "edp_scores": {
        "sales_enablement_collapse": 0.5,
        "technology_obsolescence": 0.5,
        "rep_performance_crisis": 0.5,
        "sku_complexity": 0.4,
        "channel_conflict": 0.3
      },
      "key_evidence": [
        "No product search functionality",
        "Manual dealer login system"
      ],
      "recommended_approach": "nurture",
      "contact_info": {
        "first_name": "Ian",
        "last_name": "Geltner",
        "email": "igeltner@stevesilver.com",
        "title": "VP Sales",
        "linkedin": "https://www.linkedin.com/in/iangeltner/"
      },
      "company_info": {
        "industry": "Furniture and Home Furnishings Manufacturing",
        "employee_count": 125
      },
      "analyzed_at": "2025-08-23T07:46:32.920600"
    }
  ]
}
```

### supercat_automation/webhooks/48640800-ed41-4a60-bc22-dfc2c42df639_ERG_International.json
```json
{
  "company_id": "48640800-ed41-4a60-bc22-dfc2c42df639",
  "company_name": "ERG International",
  "domain": "erginternational.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 36.5,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.6,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "Configuration complexity",
    "Multiple options/finishes"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why ERG International's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs ERG International approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed ERG International works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Jack",
    "last_name": "Werksman",
    "email": "jackw@erginternational.com",
    "title": "Vice President of Sales",
    "linkedin": "https://www.linkedin.com/in/jackwerksman/"
  },
  "company_info": {
    "industry": "Furniture",
    "employee_count": 56
  },
  "created_at": "2025-08-23T07:15:44.058375",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/b2325193-d71a-41f7-99c4-6fa17c9a5afb_Anne_McGilvray_&_Company.json
```json
{
  "company_id": "b2325193-d71a-41f7-99c4-6fa17c9a5afb",
  "company_name": "Anne McGilvray & Company",
  "domain": "annemcgilvray.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 31.3,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.3,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No sales resources",
    "No territory info",
    "Configuration complexity",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Anne McGilvray & Company's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Anne McGilvray & Company approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Anne McGilvray & Company works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Ms.",
    "last_name": "Lisa Bach",
    "email": "lbach@annemcgilvray.com",
    "title": "Director of Sales & Publisher Relations",
    "linkedin": "https://www.linkedin.com/in/lisasbach/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 101
  },
  "created_at": "2025-08-23T07:15:13.210333",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/2ff89582-fc0d-4571-bc78-30a7fdc4b020_EJ_Victor.json
```json
{
  "company_id": "2ff89582-fc0d-4571-bc78-30a7fdc4b020",
  "company_name": "EJ Victor",
  "domain": "ejvictor.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 30.7,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0.3
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Mixed channels"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why EJ Victor's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs EJ Victor approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed EJ Victor works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "John",
    "last_name": "Jokinen",
    "email": "john@ejvictor.com",
    "title": "CEO",
    "linkedin": "https://www.linkedin.com/in/john-jokinen-92720497/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 82
  },
  "created_at": "2025-08-23T07:15:42.689824",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/c32cb0df-2c54-4b26-a6b3-ccfe3b13171e_Castelle.json
```json
{
  "company_id": "c32cb0df-2c54-4b26-a6b3-ccfe3b13171e",
  "company_name": "Castelle",
  "domain": "castellefurniture.com",
  "tam_tier": "TIER_2_ACTIVE",
  "psi_score": 42.8,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0.3,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.6,
    "channel_conflict": 0.3
  },
  "evidence": [
    "No product search",
    "CSV-based processes",
    "No rep locator",
    "No sales resources",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "medium",
  "campaign_strategy": "educational",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Castelle's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Castelle approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Castelle works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Sergio",
    "last_name": "Flores",
    "email": "sflores@castellefurniture.com",
    "title": "Vice President Operations",
    "linkedin": "https://www.linkedin.com/in/sergio-flores-55830916/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 69
  },
  "created_at": "2025-08-23T07:20:32.748396",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/8a0f4247-df5a-4b0b-a83e-84cf961ad799_Anne_McGilvray_Company.json
```json
{
  "company_id": "8a0f4247-df5a-4b0b-a83e-84cf961ad799",
  "company_name": "Anne McGilvray & Company",
  "domain": "annemcgilvray.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 31.3,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.3,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No sales resources",
    "No territory info",
    "Configuration complexity",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Anne McGilvray & Company's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Anne McGilvray & Company approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Anne McGilvray & Company works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Ms.",
    "last_name": "Lisa Bach",
    "email": "lbach@annemcgilvray.com",
    "title": "Director of Sales & Publisher Relations",
    "linkedin": "https://www.linkedin.com/in/lisasbach/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 101
  },
  "created_at": "2025-08-23T07:20:31.839262",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/4d6e7c96-a840-43d2-a9ba-b1a814338df2_Allstate_Floral,_Inc..json
```json
{
  "company_id": "4d6e7c96-a840-43d2-a9ba-b1a814338df2",
  "company_name": "Allstate Floral, Inc.",
  "domain": "allstatefloral.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 34.1,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.4,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Large catalog"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Allstate Floral, Inc.'s top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Allstate Floral, Inc. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Allstate Floral, Inc. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Tim",
    "last_name": "Turntine",
    "email": NaN,
    "title": "Vice President of Sales",
    "linkedin": "https://www.linkedin.com/in/tim-turntine-60919b120/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 63
  },
  "created_at": "2025-08-23T07:15:10.039882",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/7f1149b6-9047-4cda-bbec-81d4565b779c_CTG_Brands_Inc..json
```json
{
  "company_id": "7f1149b6-9047-4cda-bbec-81d4565b779c",
  "company_name": "CTG Brands Inc.",
  "domain": "ctgbrands.com",
  "tam_tier": "TIER_2_ACTIVE",
  "psi_score": 50.0,
  "primary_edp": "sales_enablement_collapse",
  "edp_scores": {
    "sales_enablement_collapse": 0.5,
    "technology_obsolescence": 0.5,
    "rep_performance_crisis": 0.5,
    "sku_complexity": 0.5,
    "channel_conflict": 0.5
  },
  "evidence": [
    "Analysis error: HTTPSConnectionPool(host='ctgbrands.com', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x11bd12ca0>, 'Connection to ctgbrands.com timed out. (connect timeout=10)'))"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is sales_enablement_collapse",
  "urgency_level": "medium",
  "campaign_strategy": "educational",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "CTG Brands Inc. - Still using paper at trade shows?",
      "body": "Hi {{first_name}},\n\nI noticed CTG Brands Inc. has a major presence at High Point Market. With the show in -491 days, how are your reps planning to handle orders when they can't access your systems?\n\nLast year, several exhibitors lost over $50K each during WiFi outages.\n\nHow do you currently handle order processing at trade shows?\n\nBest,\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "How Butler Specialty solved this",
      "body": "{{first_name}},\n\nQuick follow-up - Butler Specialty had the same challenge at High Point. Their President told me: 'eCat flexibly configures to the way we do business'\n\nThey now process orders completely offline. Zero downtime.\n\nWorth a quick call?\n\n{{sender_name}}"
    },
    {
      "day": 7,
      "subject": "30% order error rate industry average",
      "body": "{{first_name}},\n\nDid you know the furniture industry averages a 30% order error rate with manual processes?\n\nAt your scale, that could mean $400K+ in lost margin annually.\n\nHere's a 2-minute video showing how eCat eliminates these errors: [link]\n\n{{sender_name}}"
    },
    {
      "day": 10,
      "subject": "ROI calculator for CTG Brands Inc.",
      "body": "{{first_name}},\n\nI ran some numbers for CTG Brands Inc.:\n\n- Time saved: 3 hours/day per rep\n- Error reduction: 25%\n- Trade show revenue protection: $150K+\n\nTotal first-year ROI: 412%\n\nWant to see the full breakdown?\n\n{{sender_name}}"
    },
    {
      "day": 14,
      "subject": "Godinger Silver case study",
      "body": "{{first_name}},\n\nJoel Stern, VP IT at Godinger Silver, called eCat 'Best thing in 25 years, reps are in love'\n\nThey saw:\n- 67% reduction in order processing time\n- Zero trade show downtime\n- 40% increase in rep productivity\n\nHere's their full story: [link]\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed CTG Brands Inc.'s presence at High Point Market. Managing orders without reliable WiFi must be challenging. Would love to share how similar companies handle this."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Robert",
    "last_name": "Read",
    "email": "rread@ctgbrands.com",
    "title": "Director of Sales, USA",
    "linkedin": "https://www.linkedin.com/in/robert-read-b8277015/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 84
  },
  "created_at": "2025-08-23T07:15:33.890104",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/efc00576-22a6-41a5-900c-6ad687c44b5e_Capel_Rugs.json
```json
{
  "company_id": "efc00576-22a6-41a5-900c-6ad687c44b5e",
  "company_name": "Capel Rugs",
  "domain": "capelrugs.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 31.9,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Capel Rugs's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Capel Rugs approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Capel Rugs works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Ron",
    "last_name": "Capel",
    "email": "ronc@capel.net",
    "title": "Managing Director - Retail",
    "linkedin": "https://www.linkedin.com/in/ron-capel-35877915/"
  },
  "company_info": {
    "industry": "Design Services",
    "employee_count": 50
  },
  "created_at": "2025-08-23T07:20:30.793562",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/76c2e653-99c4-489c-8533-25de660a567a_Dovetail_Furniture_Pvt_Ltd.json
```json
{
  "company_id": "76c2e653-99c4-489c-8533-25de660a567a",
  "company_name": "Dovetail Furniture Pvt Ltd",
  "domain": "dovetail.in",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 32.4,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.3,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Dovetail Furniture Pvt Ltd's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Dovetail Furniture Pvt Ltd approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Dovetail Furniture Pvt Ltd works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Radhakrishnan",
    "last_name": "Nair",
    "email": "rkn@dovetail.in",
    "title": "Chief Operating Officer",
    "linkedin": "https://www.linkedin.com/in/radhakrishnan-nair-96796214b/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 29
  },
  "created_at": "2025-08-23T07:15:36.946635",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/24e5f52c-4639-439f-9b54-40d5f60772cf_burton_+_BURTON.json
```json
{
  "company_id": "24e5f52c-4639-439f-9b54-40d5f60772cf",
  "company_name": "burton + BURTON",
  "domain": "burtonandburton.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 38.8,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.4,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Large catalog"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why burton + BURTON's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs burton + BURTON approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed burton + BURTON works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Elaine",
    "last_name": "Chandler",
    "email": "echandler@burtonandburton.com",
    "title": "Corporate Sales Executive",
    "linkedin": "https://www.linkedin.com/in/elaine-chandler-1810b614a/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 151
  },
  "created_at": "2025-08-23T07:15:19.578422",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/53b5f9d2-405f-4cae-86ad-0b59a9c10260_Golden_Rabbit_II,_Inc..json
```json
{
  "company_id": "53b5f9d2-405f-4cae-86ad-0b59a9c10260",
  "company_name": "Golden Rabbit II, Inc.",
  "domain": "crowcanyonhome.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 31.9,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Golden Rabbit II, Inc.'s top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Golden Rabbit II, Inc. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Golden Rabbit II, Inc. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Cara",
    "last_name": "Barde",
    "email": "cara@crowcanyonhome.com",
    "title": "Owner/President",
    "linkedin": "https://www.linkedin.com/in/carabarde/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 21
  },
  "created_at": "2025-08-23T07:15:16.034397",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/cbd2f13a-fea3-4383-80a6-7d7fd43d475f_Bulbrite_Industries.json
```json
{
  "company_id": "cbd2f13a-fea3-4383-80a6-7d7fd43d475f",
  "company_name": "Bulbrite Industries",
  "domain": "bulbrite.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 35.3,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0.7
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Bulbrite Industries's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Bulbrite Industries approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Bulbrite Industries works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Eric",
    "last_name": "Choi",
    "email": "echoi@bulbrite.com",
    "title": "VP of Product",
    "linkedin": "https://www.linkedin.com/in/erickchoi/"
  },
  "company_info": {
    "industry": "Appliances, Electrical, and Electronics Manufacturing",
    "employee_count": 46
  },
  "created_at": "2025-08-23T07:15:18.392482",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/e1c68f85-5d0d-4601-9f21-a9df685cbc46_Fanimation.json
```json
{
  "company_id": "e1c68f85-5d0d-4601-9f21-a9df685cbc46",
  "company_name": "Fanimation",
  "domain": "fanimation.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 48.0,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.6,
    "technology_obsolescence": 0.3,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.3,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "PDF-only catalogs",
    "CSV-based processes",
    "No rep locator",
    "No sales resources"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Fanimation's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Fanimation approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Fanimation works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Christopher",
    "last_name": "Wheeler",
    "email": "chris.wheeler@fanimation.com",
    "title": "Vice President Operations",
    "linkedin": "https://www.linkedin.com/in/christopher-wheeler45/"
  },
  "company_info": {
    "industry": "Manufacturing",
    "employee_count": 63
  },
  "created_at": "2025-08-23T07:15:46.955182",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/2565aca4-1b2e-4527-9bfd-5d6821592729_A_B_HOME_GROUP_INC.json
```json
{
  "company_id": "2565aca4-1b2e-4527-9bfd-5d6821592729",
  "company_name": "A & B HOME GROUP, INC.",
  "domain": "abhomeinc.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 26.1,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why A & B HOME GROUP, INC.'s top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs A & B HOME GROUP, INC. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed A & B HOME GROUP, INC. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Emad",
    "last_name": "Botros",
    "email": "emadb@abhongda.net",
    "title": "Director of Operations & Logistics",
    "linkedin": "https://www.linkedin.com/in/emadbotors/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 43
  },
  "created_at": "2025-08-23T07:20:27.978199",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/45fdbe0e-31bc-4d44-8b8c-f0c08d0aee7f_9to5_Seating.json
```json
{
  "company_id": "45fdbe0e-31bc-4d44-8b8c-f0c08d0aee7f",
  "company_name": "9to5 Seating",
  "domain": "9to5seating.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 32.4,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.3,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why 9to5 Seating's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs 9to5 Seating approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed 9to5 Seating works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Ed",
    "last_name": "Lachman",
    "email": "ed.lachman@9to5seating.com",
    "title": "Chief Operating Officer",
    "linkedin": "https://www.linkedin.com/in/ed-lachman-15b1a862/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 59
  },
  "created_at": "2025-08-23T07:15:04.852976",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/9efce539-340b-4bf9-bf0f-3a61bf1b9dc6_A_Rudin.json
```json
{
  "company_id": "9efce539-340b-4bf9-bf0f-3a61bf1b9dc6",
  "company_name": "A. Rudin",
  "domain": "arudin.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 27.2,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why A. Rudin's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs A. Rudin approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed A. Rudin works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Natalie",
    "last_name": "Mata Pizarro",
    "email": "npizarro@arudin.com",
    "title": "National Sales Director",
    "linkedin": "https://www.linkedin.com/in/natalie-mata-pizarro-99862461/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 24
  },
  "created_at": "2025-08-23T07:20:29.863408",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/0b23af6c-2481-41ad-9881-6d17b91c3eeb_EGLO_Leuchten.json
```json
{
  "company_id": "0b23af6c-2481-41ad-9881-6d17b91c3eeb",
  "company_name": "EGLO Leuchten",
  "domain": "eglo.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 38.8,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.4,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Large catalog"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why EGLO Leuchten's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs EGLO Leuchten approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed EGLO Leuchten works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Mag. Ren\u00e9",
    "last_name": "Tiefenbacher",
    "email": "rene.tiefenbacher@eglo.com",
    "title": "CEO",
    "linkedin": "https://www.linkedin.com/in/mag-ren\u00e9-tiefenbacher-b13b25280/"
  },
  "company_info": {
    "industry": "Appliances, Electrical, and Electronics Manufacturing",
    "employee_count": 381
  },
  "created_at": "2025-08-23T07:15:39.166276",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/fe2e9061-b350-465b-b33a-2c452a48b463_Golden_Rabbit_II_Inc.json
```json
{
  "company_id": "fe2e9061-b350-465b-b33a-2c452a48b463",
  "company_name": "Golden Rabbit II, Inc.",
  "domain": "crowcanyonhome.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 31.9,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Golden Rabbit II, Inc.'s top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Golden Rabbit II, Inc. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Golden Rabbit II, Inc. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Cara",
    "last_name": "Barde",
    "email": "cara@crowcanyonhome.com",
    "title": "Owner/President",
    "linkedin": "https://www.linkedin.com/in/carabarde/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 21
  },
  "created_at": "2025-08-23T07:20:34.529731",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/c417c22b-63ce-42be-99cf-5a9af96a5741_Coaster_Company_of_America.json
```json
{
  "company_id": "c417c22b-63ce-42be-99cf-5a9af96a5741",
  "company_name": "Coaster Company of America",
  "domain": "coasterfurniture.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 40.7,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.5,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0.7
  },
  "evidence": [
    "No product search",
    "Manual dealer login",
    "No rep locator",
    "No sales resources",
    "No territory info"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Coaster Company of America's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Coaster Company of America approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Coaster Company of America works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Nelson",
    "last_name": "Lc",
    "email": "nlc@coasteramer.com",
    "title": "Director",
    "linkedin": "https://www.linkedin.com/in/nelson-lc-294a7537/"
  },
  "company_info": {
    "industry": "Furniture",
    "employee_count": 327
  },
  "created_at": "2025-08-23T07:15:23.377090",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/93156f30-f9ad-4335-a46f-10e4405cd7ab_Atkore.json
```json
{
  "company_id": "93156f30-f9ad-4335-a46f-10e4405cd7ab",
  "company_name": "Atkore",
  "domain": "atkore.com",
  "tam_tier": "TIER_2_ACTIVE",
  "psi_score": 43.6,
  "primary_edp": "sales_enablement_collapse",
  "edp_scores": {
    "sales_enablement_collapse": 0.5,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.7,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "Manual quote requests",
    "No rep locator",
    "No sales resources",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is sales_enablement_collapse",
  "urgency_level": "medium",
  "campaign_strategy": "educational",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Atkore - Still using paper at trade shows?",
      "body": "Hi {{first_name}},\n\nI noticed Atkore has a major presence at High Point Market. With the show in -491 days, how are your reps planning to handle orders when they can't access your systems?\n\nLast year, several exhibitors lost over $50K each during WiFi outages.\n\nHow do you currently handle order processing at trade shows?\n\nBest,\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "How Butler Specialty solved this",
      "body": "{{first_name}},\n\nQuick follow-up - Butler Specialty had the same challenge at High Point. Their President told me: 'eCat flexibly configures to the way we do business'\n\nThey now process orders completely offline. Zero downtime.\n\nWorth a quick call?\n\n{{sender_name}}"
    },
    {
      "day": 7,
      "subject": "30% order error rate industry average",
      "body": "{{first_name}},\n\nDid you know the furniture industry averages a 30% order error rate with manual processes?\n\nAt your scale, that could mean $400K+ in lost margin annually.\n\nHere's a 2-minute video showing how eCat eliminates these errors: [link]\n\n{{sender_name}}"
    },
    {
      "day": 10,
      "subject": "ROI calculator for Atkore",
      "body": "{{first_name}},\n\nI ran some numbers for Atkore:\n\n- Time saved: 3 hours/day per rep\n- Error reduction: 25%\n- Trade show revenue protection: $150K+\n\nTotal first-year ROI: 412%\n\nWant to see the full breakdown?\n\n{{sender_name}}"
    },
    {
      "day": 14,
      "subject": "Godinger Silver case study",
      "body": "{{first_name}},\n\nJoel Stern, VP IT at Godinger Silver, called eCat 'Best thing in 25 years, reps are in love'\n\nThey saw:\n- 67% reduction in order processing time\n- Zero trade show downtime\n- 40% increase in rep productivity\n\nHere's their full story: [link]\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Atkore's presence at High Point Market. Managing orders without reliable WiFi must be challenging. Would love to share how similar companies handle this."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Eric",
    "last_name": "Banks",
    "email": "ebanks@atkore.com",
    "title": "Vice President, Operations",
    "linkedin": "https://www.linkedin.com/in/ericbanks1775/"
  },
  "company_info": {
    "industry": "Appliances, Electrical, and Electronics Manufacturing",
    "employee_count": 1969
  },
  "created_at": "2025-08-23T07:20:33.794355",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/b87cd46a-90ff-45e3-8723-e88e09d7472c_World_of_Eichholtz.json
```json
{
  "company_id": "b87cd46a-90ff-45e3-8723-e88e09d7472c",
  "company_name": "World of Eichholtz",
  "domain": "eichholtz.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 44.6,
  "primary_edp": "sales_enablement_collapse",
  "edp_scores": {
    "sales_enablement_collapse": 0.6,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.6,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "PDF-only catalogs",
    "No rep locator",
    "No sales resources",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is sales_enablement_collapse",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "World of Eichholtz - Still using paper at trade shows?",
      "body": "Hi {{first_name}},\n\nI noticed World of Eichholtz has a major presence at High Point Market. With the show in -491 days, how are your reps planning to handle orders when they can't access your systems?\n\nLast year, several exhibitors lost over $50K each during WiFi outages.\n\nHow do you currently handle order processing at trade shows?\n\nBest,\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "How Butler Specialty solved this",
      "body": "{{first_name}},\n\nQuick follow-up - Butler Specialty had the same challenge at High Point. Their President told me: 'eCat flexibly configures to the way we do business'\n\nThey now process orders completely offline. Zero downtime.\n\nWorth a quick call?\n\n{{sender_name}}"
    },
    {
      "day": 7,
      "subject": "30% order error rate industry average",
      "body": "{{first_name}},\n\nDid you know the furniture industry averages a 30% order error rate with manual processes?\n\nAt your scale, that could mean $400K+ in lost margin annually.\n\nHere's a 2-minute video showing how eCat eliminates these errors: [link]\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed World of Eichholtz's presence at High Point Market. Managing orders without reliable WiFi must be challenging. Would love to share how similar companies handle this."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Dennis",
    "last_name": "Hendriks ",
    "email": "dhendriks@eichholtzusa.com",
    "title": "Vice President Operations",
    "linkedin": "https://www.linkedin.com/in/dennis-hendriks-523684263/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 170
  },
  "created_at": "2025-08-23T07:15:41.486384",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/72143970-b29b-4766-80d8-8e13c887edea_9to5_Seating.json
```json
{
  "company_id": "72143970-b29b-4766-80d8-8e13c887edea",
  "company_name": "9to5 Seating",
  "domain": "9to5seating.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 32.4,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.3,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why 9to5 Seating's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs 9to5 Seating approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed 9to5 Seating works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Ed",
    "last_name": "Lachman",
    "email": "ed.lachman@9to5seating.com",
    "title": "Chief Operating Officer",
    "linkedin": "https://www.linkedin.com/in/ed-lachman-15b1a862/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 59
  },
  "created_at": "2025-08-23T07:20:22.854146",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/8c5068b8-92ff-45c4-a56a-b23fe8fecad1_Capel_Rugs.json
```json
{
  "company_id": "8c5068b8-92ff-45c4-a56a-b23fe8fecad1",
  "company_name": "Capel Rugs",
  "domain": "capelrugs.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 31.9,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Multiple logins"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Capel Rugs's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Capel Rugs approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Capel Rugs works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Ron",
    "last_name": "Capel",
    "email": "ronc@capel.net",
    "title": "Managing Director - Retail",
    "linkedin": "https://www.linkedin.com/in/ron-capel-35877915/"
  },
  "company_info": {
    "industry": "Design Services",
    "employee_count": 50
  },
  "created_at": "2025-08-23T07:15:11.634862",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/56d8b7f2-fac0-48c4-b33b-09d393beef6e_Atkore.json
```json
{
  "company_id": "56d8b7f2-fac0-48c4-b33b-09d393beef6e",
  "company_name": "Atkore",
  "domain": "atkore.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 43.6,
  "primary_edp": "sales_enablement_collapse",
  "edp_scores": {
    "sales_enablement_collapse": 0.5,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.7,
    "channel_conflict": 0.4
  },
  "evidence": [
    "No product search",
    "Manual quote requests",
    "No rep locator",
    "No sales resources",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is sales_enablement_collapse",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Atkore - Still using paper at trade shows?",
      "body": "Hi {{first_name}},\n\nI noticed Atkore has a major presence at High Point Market. With the show in -491 days, how are your reps planning to handle orders when they can't access your systems?\n\nLast year, several exhibitors lost over $50K each during WiFi outages.\n\nHow do you currently handle order processing at trade shows?\n\nBest,\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "How Butler Specialty solved this",
      "body": "{{first_name}},\n\nQuick follow-up - Butler Specialty had the same challenge at High Point. Their President told me: 'eCat flexibly configures to the way we do business'\n\nThey now process orders completely offline. Zero downtime.\n\nWorth a quick call?\n\n{{sender_name}}"
    },
    {
      "day": 7,
      "subject": "30% order error rate industry average",
      "body": "{{first_name}},\n\nDid you know the furniture industry averages a 30% order error rate with manual processes?\n\nAt your scale, that could mean $400K+ in lost margin annually.\n\nHere's a 2-minute video showing how eCat eliminates these errors: [link]\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Atkore's presence at High Point Market. Managing orders without reliable WiFi must be challenging. Would love to share how similar companies handle this."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Eric",
    "last_name": "Banks",
    "email": "ebanks@atkore.com",
    "title": "Vice President, Operations",
    "linkedin": "https://www.linkedin.com/in/ericbanks1775/"
  },
  "company_info": {
    "industry": "Appliances, Electrical, and Electronics Manufacturing",
    "employee_count": 1969
  },
  "created_at": "2025-08-23T07:15:15.200296",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/a9cf24b1-3e1a-4df8-854b-b1355ee66f02_Castelle.json
```json
{
  "company_id": "a9cf24b1-3e1a-4df8-854b-b1355ee66f02",
  "company_name": "Castelle",
  "domain": "castellefurniture.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 42.8,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0.3,
    "rep_performance_crisis": 0.7,
    "sku_complexity": 0.6,
    "channel_conflict": 0.3
  },
  "evidence": [
    "No product search",
    "CSV-based processes",
    "No rep locator",
    "No sales resources",
    "Configuration complexity"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Castelle's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Castelle approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Castelle works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Sergio",
    "last_name": "Flores",
    "email": "sflores@castellefurniture.com",
    "title": "Vice President Operations",
    "linkedin": "https://www.linkedin.com/in/sergio-flores-55830916/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 69
  },
  "created_at": "2025-08-23T07:15:14.114740",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/fb9a77d7-7544-468e-a427-efbb9810b31f_Century_Furniture.json
```json
{
  "company_id": "fb9a77d7-7544-468e-a427-efbb9810b31f",
  "company_name": "Century Furniture",
  "domain": "centuryfurniture.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 35.3,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.6,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "PDF-only catalogs",
    "No rep locator",
    "No sales resources",
    "No territory info"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Century Furniture's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Century Furniture approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Century Furniture works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Alesia",
    "last_name": "Smith",
    "email": "asmith@centuryfurniture.com",
    "title": "Research And Development Assistant",
    "linkedin": "https://www.linkedin.com/in/alesia-smith-416766155/"
  },
  "company_info": {
    "industry": "Furniture",
    "employee_count": 347
  },
  "created_at": "2025-08-23T07:15:21.132446",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/1b443b5a-e030-41fa-b091-21664d6cb86a_Allstate_Floral_Inc.json
```json
{
  "company_id": "1b443b5a-e030-41fa-b091-21664d6cb86a",
  "company_name": "Allstate Floral, Inc.",
  "domain": "allstatefloral.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 34.1,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.4,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Large catalog"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Allstate Floral, Inc.'s top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Allstate Floral, Inc. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Allstate Floral, Inc. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Tim",
    "last_name": "Turntine",
    "email": NaN,
    "title": "Vice President of Sales",
    "linkedin": "https://www.linkedin.com/in/tim-turntine-60919b120/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 63
  },
  "created_at": "2025-08-23T07:20:28.843928",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/05025502-d564-44c9-b208-1ac8a8a81a5b_Abbott_Collection.json
```json
{
  "company_id": "05025502-d564-44c9-b208-1ac8a8a81a5b",
  "company_name": "Abbott Collection",
  "domain": "abbottcollection.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 27.2,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0,
    "channel_conflict": 0
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Abbott Collection's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Abbott Collection approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Abbott Collection works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Lee",
    "last_name": "Abbott",
    "email": "lee.a@abbottcollection.com",
    "title": "Vice President",
    "linkedin": "https://www.linkedin.com/in/lee-abbott-a789694b/"
  },
  "company_info": {
    "industry": "Wholesale",
    "employee_count": 95
  },
  "created_at": "2025-08-23T07:20:24.516412",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/51ea9907-d435-41a6-bc64-352c49a53ba0_Bernhardt_Furniture_Co.json
```json
{
  "company_id": "51ea9907-d435-41a6-bc64-352c49a53ba0",
  "company_name": "Bernhardt Furniture Co",
  "domain": "bernhardt.com",
  "tam_tier": "TIER_3_NURTURE",
  "psi_score": 35.9,
  "primary_edp": "rep_performance_crisis",
  "edp_scores": {
    "sales_enablement_collapse": 0.3,
    "technology_obsolescence": 0,
    "rep_performance_crisis": 1.0,
    "sku_complexity": 0.3,
    "channel_conflict": 0.3
  },
  "evidence": [
    "No product search",
    "No rep locator",
    "No sales resources",
    "No territory info",
    "Multiple options/finishes"
  ],
  "persona_type": "sales_leadership",
  "backup_persona": "c_suite",
  "persona_reason": "Primary EDP is rep_performance_crisis",
  "urgency_level": "low",
  "campaign_strategy": "nurture",
  "days_until_show": -491,
  "email_sequence": [
    {
      "day": 0,
      "subject": "Why Bernhardt Furniture Co's top reps are 10x more productive",
      "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
    },
    {
      "day": 3,
      "subject": "27% rep turnover is killing your growth",
      "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Bernhardt Furniture Co approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
    }
  ],
  "linkedin_sequence": [
    {
      "type": "connection_request",
      "message": "Hi {{first_name}}, noticed Bernhardt Furniture Co works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
    },
    {
      "type": "follow_up_message",
      "day": 7,
      "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
    }
  ],
  "contact_info": {
    "first_name": "Meghan",
    "last_name": "Sziklai",
    "email": "meghansziklai@bernhardt.com",
    "title": "Global Director of Sales ",
    "linkedin": "https://www.linkedin.com/in/meghan-sziklai/"
  },
  "company_info": {
    "industry": "Furniture and Home Furnishings Manufacturing",
    "employee_count": 380
  },
  "created_at": "2025-08-23T07:15:17.441934",
  "webhook_version": "2.0"
}
```

### supercat_automation/webhooks/batch_20250823_072035.json
```json
[
  {
    "company_id": "72143970-b29b-4766-80d8-8e13c887edea",
    "company_name": "9to5 Seating",
    "domain": "9to5seating.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 32.4,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 1.0,
      "sku_complexity": 0.3,
      "channel_conflict": 0
    },
    "evidence": [
      "No product search",
      "No rep locator",
      "No sales resources",
      "No territory info",
      "Configuration complexity"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why 9to5 Seating's top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs 9to5 Seating approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed 9to5 Seating works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Ed",
      "last_name": "Lachman",
      "email": "ed.lachman@9to5seating.com",
      "title": "Chief Operating Officer",
      "linkedin": "https://www.linkedin.com/in/ed-lachman-15b1a862/"
    },
    "company_info": {
      "industry": "Furniture and Home Furnishings Manufacturing",
      "employee_count": 59
    },
    "created_at": "2025-08-23T07:20:22.854146",
    "webhook_version": "2.0"
  },
  {
    "company_id": "05025502-d564-44c9-b208-1ac8a8a81a5b",
    "company_name": "Abbott Collection",
    "domain": "abbottcollection.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 27.2,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 1.0,
      "sku_complexity": 0,
      "channel_conflict": 0
    },
    "evidence": [
      "No product search",
      "No rep locator",
      "No sales resources",
      "No territory info"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why Abbott Collection's top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Abbott Collection approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed Abbott Collection works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Lee",
      "last_name": "Abbott",
      "email": "lee.a@abbottcollection.com",
      "title": "Vice President",
      "linkedin": "https://www.linkedin.com/in/lee-abbott-a789694b/"
    },
    "company_info": {
      "industry": "Wholesale",
      "employee_count": 95
    },
    "created_at": "2025-08-23T07:20:24.516412",
    "webhook_version": "2.0"
  },
  {
    "company_id": "2565aca4-1b2e-4527-9bfd-5d6821592729",
    "company_name": "A & B HOME GROUP, INC.",
    "domain": "abhomeinc.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 26.1,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 0.7,
      "sku_complexity": 0,
      "channel_conflict": 0.4
    },
    "evidence": [
      "No product search",
      "No rep locator",
      "No sales resources",
      "Multiple logins"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why A & B HOME GROUP, INC.'s top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs A & B HOME GROUP, INC. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed A & B HOME GROUP, INC. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Emad",
      "last_name": "Botros",
      "email": "emadb@abhongda.net",
      "title": "Director of Operations & Logistics",
      "linkedin": "https://www.linkedin.com/in/emadbotors/"
    },
    "company_info": {
      "industry": "Wholesale",
      "employee_count": 43
    },
    "created_at": "2025-08-23T07:20:27.978199",
    "webhook_version": "2.0"
  },
  {
    "company_id": "1b443b5a-e030-41fa-b091-21664d6cb86a",
    "company_name": "Allstate Floral, Inc.",
    "domain": "allstatefloral.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 34.1,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 1.0,
      "sku_complexity": 0.4,
      "channel_conflict": 0
    },
    "evidence": [
      "No product search",
      "No rep locator",
      "No sales resources",
      "No territory info",
      "Large catalog"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why Allstate Floral, Inc.'s top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Allstate Floral, Inc. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed Allstate Floral, Inc. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Tim",
      "last_name": "Turntine",
      "email": NaN,
      "title": "Vice President of Sales",
      "linkedin": "https://www.linkedin.com/in/tim-turntine-60919b120/"
    },
    "company_info": {
      "industry": "Wholesale",
      "employee_count": 63
    },
    "created_at": "2025-08-23T07:20:28.843928",
    "webhook_version": "2.0"
  },
  {
    "company_id": "9efce539-340b-4bf9-bf0f-3a61bf1b9dc6",
    "company_name": "A. Rudin",
    "domain": "arudin.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 27.2,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 1.0,
      "sku_complexity": 0,
      "channel_conflict": 0
    },
    "evidence": [
      "No product search",
      "No rep locator",
      "No sales resources",
      "No territory info"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why A. Rudin's top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs A. Rudin approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed A. Rudin works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Natalie",
      "last_name": "Mata Pizarro",
      "email": "npizarro@arudin.com",
      "title": "National Sales Director",
      "linkedin": "https://www.linkedin.com/in/natalie-mata-pizarro-99862461/"
    },
    "company_info": {
      "industry": "Furniture and Home Furnishings Manufacturing",
      "employee_count": 24
    },
    "created_at": "2025-08-23T07:20:29.863408",
    "webhook_version": "2.0"
  },
  {
    "company_id": "efc00576-22a6-41a5-900c-6ad687c44b5e",
    "company_name": "Capel Rugs",
    "domain": "capelrugs.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 31.9,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 1.0,
      "sku_complexity": 0,
      "channel_conflict": 0.4
    },
    "evidence": [
      "No product search",
      "No rep locator",
      "No sales resources",
      "No territory info",
      "Multiple logins"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why Capel Rugs's top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Capel Rugs approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed Capel Rugs works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Ron",
      "last_name": "Capel",
      "email": "ronc@capel.net",
      "title": "Managing Director - Retail",
      "linkedin": "https://www.linkedin.com/in/ron-capel-35877915/"
    },
    "company_info": {
      "industry": "Design Services",
      "employee_count": 50
    },
    "created_at": "2025-08-23T07:20:30.793562",
    "webhook_version": "2.0"
  },
  {
    "company_id": "8a0f4247-df5a-4b0b-a83e-84cf961ad799",
    "company_name": "Anne McGilvray & Company",
    "domain": "annemcgilvray.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 31.3,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 0.7,
      "sku_complexity": 0.3,
      "channel_conflict": 0.4
    },
    "evidence": [
      "No product search",
      "No sales resources",
      "No territory info",
      "Configuration complexity",
      "Multiple logins"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why Anne McGilvray & Company's top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Anne McGilvray & Company approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed Anne McGilvray & Company works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Ms.",
      "last_name": "Lisa Bach",
      "email": "lbach@annemcgilvray.com",
      "title": "Director of Sales & Publisher Relations",
      "linkedin": "https://www.linkedin.com/in/lisasbach/"
    },
    "company_info": {
      "industry": "Wholesale",
      "employee_count": 101
    },
    "created_at": "2025-08-23T07:20:31.839262",
    "webhook_version": "2.0"
  },
  {
    "company_id": "c32cb0df-2c54-4b26-a6b3-ccfe3b13171e",
    "company_name": "Castelle",
    "domain": "castellefurniture.com",
    "tam_tier": "TIER_2_ACTIVE",
    "psi_score": 42.8,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0.3,
      "rep_performance_crisis": 0.7,
      "sku_complexity": 0.6,
      "channel_conflict": 0.3
    },
    "evidence": [
      "No product search",
      "CSV-based processes",
      "No rep locator",
      "No sales resources",
      "Configuration complexity"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "medium",
    "campaign_strategy": "educational",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why Castelle's top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Castelle approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed Castelle works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Sergio",
      "last_name": "Flores",
      "email": "sflores@castellefurniture.com",
      "title": "Vice President Operations",
      "linkedin": "https://www.linkedin.com/in/sergio-flores-55830916/"
    },
    "company_info": {
      "industry": "Furniture and Home Furnishings Manufacturing",
      "employee_count": 69
    },
    "created_at": "2025-08-23T07:20:32.748396",
    "webhook_version": "2.0"
  },
  {
    "company_id": "93156f30-f9ad-4335-a46f-10e4405cd7ab",
    "company_name": "Atkore",
    "domain": "atkore.com",
    "tam_tier": "TIER_2_ACTIVE",
    "psi_score": 43.6,
    "primary_edp": "sales_enablement_collapse",
    "edp_scores": {
      "sales_enablement_collapse": 0.5,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 0.7,
      "sku_complexity": 0.7,
      "channel_conflict": 0.4
    },
    "evidence": [
      "No product search",
      "Manual quote requests",
      "No rep locator",
      "No sales resources",
      "Configuration complexity"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is sales_enablement_collapse",
    "urgency_level": "medium",
    "campaign_strategy": "educational",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Atkore - Still using paper at trade shows?",
        "body": "Hi {{first_name}},\n\nI noticed Atkore has a major presence at High Point Market. With the show in -491 days, how are your reps planning to handle orders when they can't access your systems?\n\nLast year, several exhibitors lost over $50K each during WiFi outages.\n\nHow do you currently handle order processing at trade shows?\n\nBest,\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "How Butler Specialty solved this",
        "body": "{{first_name}},\n\nQuick follow-up - Butler Specialty had the same challenge at High Point. Their President told me: 'eCat flexibly configures to the way we do business'\n\nThey now process orders completely offline. Zero downtime.\n\nWorth a quick call?\n\n{{sender_name}}"
      },
      {
        "day": 7,
        "subject": "30% order error rate industry average",
        "body": "{{first_name}},\n\nDid you know the furniture industry averages a 30% order error rate with manual processes?\n\nAt your scale, that could mean $400K+ in lost margin annually.\n\nHere's a 2-minute video showing how eCat eliminates these errors: [link]\n\n{{sender_name}}"
      },
      {
        "day": 10,
        "subject": "ROI calculator for Atkore",
        "body": "{{first_name}},\n\nI ran some numbers for Atkore:\n\n- Time saved: 3 hours/day per rep\n- Error reduction: 25%\n- Trade show revenue protection: $150K+\n\nTotal first-year ROI: 412%\n\nWant to see the full breakdown?\n\n{{sender_name}}"
      },
      {
        "day": 14,
        "subject": "Godinger Silver case study",
        "body": "{{first_name}},\n\nJoel Stern, VP IT at Godinger Silver, called eCat 'Best thing in 25 years, reps are in love'\n\nThey saw:\n- 67% reduction in order processing time\n- Zero trade show downtime\n- 40% increase in rep productivity\n\nHere's their full story: [link]\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed Atkore's presence at High Point Market. Managing orders without reliable WiFi must be challenging. Would love to share how similar companies handle this."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Eric",
      "last_name": "Banks",
      "email": "ebanks@atkore.com",
      "title": "Vice President, Operations",
      "linkedin": "https://www.linkedin.com/in/ericbanks1775/"
    },
    "company_info": {
      "industry": "Appliances, Electrical, and Electronics Manufacturing",
      "employee_count": 1969
    },
    "created_at": "2025-08-23T07:20:33.794355",
    "webhook_version": "2.0"
  },
  {
    "company_id": "fe2e9061-b350-465b-b33a-2c452a48b463",
    "company_name": "Golden Rabbit II, Inc.",
    "domain": "crowcanyonhome.com",
    "tam_tier": "TIER_3_NURTURE",
    "psi_score": 31.9,
    "primary_edp": "rep_performance_crisis",
    "edp_scores": {
      "sales_enablement_collapse": 0.3,
      "technology_obsolescence": 0,
      "rep_performance_crisis": 1.0,
      "sku_complexity": 0,
      "channel_conflict": 0.4
    },
    "evidence": [
      "No product search",
      "No rep locator",
      "No sales resources",
      "No territory info",
      "Multiple logins"
    ],
    "persona_type": "sales_leadership",
    "backup_persona": "c_suite",
    "persona_reason": "Primary EDP is rep_performance_crisis",
    "urgency_level": "low",
    "campaign_strategy": "nurture",
    "days_until_show": -491,
    "email_sequence": [
      {
        "day": 0,
        "subject": "Why Golden Rabbit II, Inc.'s top reps are 10x more productive",
        "body": "Hi {{first_name}},\n\nI've noticed a pattern: top furniture reps use tools 10-12 times daily, while bottom performers barely log in.\n\nWithout visibility into rep activity, you can't coach the underperformers.\n\nHow do you currently track rep productivity?\n\n{{sender_name}}"
      },
      {
        "day": 3,
        "subject": "27% rep turnover is killing your growth",
        "body": "{{first_name}},\n\nThe industry average 27% rep turnover costs Golden Rabbit II, Inc. approximately $500K annually in lost relationships and training.\n\neCat shows exactly which reps need help before they fail.\n\nWorth discussing?\n\n{{sender_name}}"
      }
    ],
    "linkedin_sequence": [
      {
        "type": "connection_request",
        "message": "Hi {{first_name}}, noticed Golden Rabbit II, Inc. works with independent reps. Getting them to adopt new tools must be challenging. We've solved this for 50+ brands."
      },
      {
        "type": "follow_up_message",
        "day": 7,
        "message": "{{first_name}}, thanks for connecting! Curious - what's your biggest challenge with sales operations right now?"
      }
    ],
    "contact_info": {
      "first_name": "Cara",
      "last_name": "Barde",
      "email": "cara@crowcanyonhome.com",
      "title": "Owner/President",
      "linkedin": "https://www.linkedin.com/in/carabarde/"
    },
    "company_info": {
      "industry": "Wholesale",
      "employee_count": 21
    },
    "created_at": "2025-08-23T07:20:34.529731",
    "webhook_version": "2.0"
  }
]
```

## Database Schema

### supercat_automation/create_tables.sql
```sql
-- Core Tables for SuperCat GTM Automation

-- Companies table
CREATE TABLE IF NOT EXISTS companies (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    domain VARCHAR(255) UNIQUE,
    industry VARCHAR(100),
    employee_count INTEGER,
    revenue_estimate BIGINT,
    current_erp VARCHAR(100),
    trade_shows TEXT[],
    source VARCHAR(50),
    
    -- Pain scoring
    edp_scores JSONB DEFAULT '{}',
    edp_tags TEXT[] DEFAULT '{}',
    tam_tier VARCHAR(50),
    primary_edp VARCHAR(100),
    has_multiple_edps BOOLEAN DEFAULT FALSE,
    edp_count INTEGER DEFAULT 0,
    psi_score FLOAT DEFAULT 0,
    overall_pain_score FLOAT DEFAULT 0,
    
    -- Evidence
    website_evidence JSONB DEFAULT '{}',
    last_website_scan TIMESTAMP,
    
    -- Qualification
    tier_1_qualified BOOLEAN DEFAULT FALSE,
    tier_2_qualified BOOLEAN DEFAULT FALSE,
    qualification_score FLOAT DEFAULT 0,
    disqualified BOOLEAN DEFAULT FALSE,
    
    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Trade shows table
CREATE TABLE IF NOT EXISTS trade_shows (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    venue VARCHAR(255),
    start_date DATE,
    end_date DATE,
    industry VARCHAR(100),
    website_url VARCHAR(500),
    exhibitor_list_url VARCHAR(500),
    estimated_attendance INTEGER,
    last_scraped TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Decision makers table
CREATE TABLE IF NOT EXISTS decision_makers (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    company_id UUID REFERENCES companies(id),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    title VARCHAR(200),
    linkedin_url VARCHAR(500),
    is_champion_persona BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Campaigns table
CREATE TABLE IF NOT EXISTS campaigns (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    company_id UUID REFERENCES companies(id),
    campaign_type VARCHAR(50),
    campaign_status VARCHAR(50) DEFAULT 'draft',
    pain_point_focus VARCHAR(100),
    primary_hook TEXT,
    email_sequence JSONB DEFAULT '[]',
    linkedin_messages JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_companies_tam_tier ON companies(tam_tier);
CREATE INDEX IF NOT EXISTS idx_companies_domain ON companies(domain);

```

