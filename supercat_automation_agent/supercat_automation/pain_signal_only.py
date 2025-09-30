#!/usr/bin/env python3
"""
Pain Signal Analysis CLI Script
Analyzes CSV of companies for pain signals and sends to Clay webhook + Supabase
Uses existing WebsiteEvidenceExtractor for sophisticated EDP analysis
"""

import csv
import sys
import json
import logging
from datetime import datetime
from typing import Dict, Any
import requests

# Import existing Supercat modules
from scrapers.website_evidence import WebsiteEvidenceExtractor
from database.connection import db

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Clay webhook URL from the manual
CLAY_WEBHOOK_URL = "https://api.clay.com/v3/sources/webhook/pull-in-data-from-a-webhook-ba8d0100-6e0f-4c26-8523-fac369f75a18"

class PainSignalProcessor:
    """
    Processes CSV files for pain signal analysis
    Leverages existing WebsiteEvidenceExtractor + Supabase integration
    """
    
    def __init__(self):
        self.extractor = WebsiteEvidenceExtractor()
        logger.info("✅ Initialized Pain Signal Processor")
    
    def analyze_company(self, company_name: str, domain: str) -> Dict[str, Any]:
        """
        Analyze a single company using existing WebsiteEvidenceExtractor
        """
        logger.info(f"🔍 Analyzing {company_name} ({domain})")
        
        try:
            # Use existing sophisticated analysis
            evidence = self.extractor.analyze_website(domain)
            
            # Transform to simplified pain signals format for Clay
            pain_signals = self._transform_evidence_to_pain_signals(evidence)
            
            # Store in Supabase using existing patterns
            company_record = self._save_to_supabase(company_name, domain, evidence, pain_signals)
            
            return {
                'company_name': company_name,
                'domain': domain,
                'pain_signals': pain_signals,
                'full_evidence': evidence,
                'company_id': company_record.get('id') if company_record else None,
                'analysis_timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Error analyzing {company_name}: {e}")
            return {
                'company_name': company_name,
                'domain': domain,
                'error': str(e),
                'analysis_timestamp': datetime.now().isoformat()
            }
    
    def _transform_evidence_to_pain_signals(self, evidence: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform sophisticated EDP analysis to simplified pain signals for Clay
        """
        edp_evidence = evidence.get('edp_evidence', {})
        
        pain_signals = {
            'total_pain_score': 0,
            'primary_pain_point': None,
            'pain_indicators': [],
            'evidence_strength': 'none',
            'tam_tier': evidence.get('tam_indicators', {}).get('tier', 'UNKNOWN')
        }
        
        # Process each EDP
        pain_scores = []
        for edp_name, edp_data in edp_evidence.items():
            score = edp_data.get('weighted_score', edp_data.get('score', 0))
            pain_scores.append({
                'edp': edp_name,
                'score': score,
                'strength': edp_data.get('evidence_strength', 'none'),
                'indicators': edp_data.get('indicators_found', []),
                'specific_issues': edp_data.get('specific_issues', [])
            })
        
        # Sort by score to find primary pain point
        pain_scores.sort(key=lambda x: x['score'], reverse=True)
        
        if pain_scores:
            pain_signals['primary_pain_point'] = pain_scores[0]['edp']
            pain_signals['total_pain_score'] = sum(p['score'] for p in pain_scores)
            pain_signals['evidence_strength'] = pain_scores[0]['strength']
            
            # Collect all indicators
            for pain in pain_scores:
                pain_signals['pain_indicators'].extend(pain['indicators'])
        
        # Add personalization hooks
        pain_signals['personalization_hooks'] = evidence.get('personalization_hooks', [])
        
        return pain_signals
    
    def _save_to_supabase(self, company_name: str, domain: str, evidence: Dict, pain_signals: Dict) -> Dict:
        """
        Save analysis results to Supabase using existing patterns
        """
        try:
            # Prepare company data
            company_data = {
                'company_name': company_name,
                'domain': domain,
                'last_website_scan': datetime.now().isoformat(),
                'website_evidence': evidence,
                'tam_tier': pain_signals.get('tam_tier', 'UNKNOWN'),
                'primary_edp': pain_signals.get('primary_pain_point'),
                'psi_score': pain_signals.get('total_pain_score', 0),
                'evidence_strength': pain_signals.get('evidence_strength', 'none'),
                'edp_tags': pain_signals.get('pain_indicators', []),
                'has_multiple_edps': len([p for p in evidence.get('edp_evidence', {}).values() if p.get('score', 0) > 0.3]) > 1,
                'edp_count': len([p for p in evidence.get('edp_evidence', {}).values() if p.get('score', 0) > 0.3])
            }
            
            # Upsert company using existing method
            company_record = db.upsert_company(company_data)
            
            if company_record:
                logger.info(f"💾 Saved {company_name} to Supabase")
                
                # Update pain scores using existing method
                pain_score_data = {
                    'sales_enablement_pain_score': evidence.get('edp_evidence', {}).get('sales_enablement_collapse', {}).get('weighted_score', 0),
                    'technology_obsolescence_score': evidence.get('edp_evidence', {}).get('technology_obsolescence', {}).get('weighted_score', 0),
                    'rep_performance_pain_score': evidence.get('edp_evidence', {}).get('rep_performance_crisis', {}).get('weighted_score', 0),
                    'sku_complexity_pain_score': evidence.get('edp_evidence', {}).get('sku_complexity', {}).get('weighted_score', 0)
                }
                
                db.update_pain_scores(company_record['id'], pain_score_data)
                
            return company_record
            
        except Exception as e:
            logger.error(f"❌ Error saving to Supabase: {e}")
            return {}
    
    def send_to_clay(self, analysis_result: Dict[str, Any]) -> bool:
        """
        Send pain signals to Clay webhook
        """
        if 'error' in analysis_result:
            logger.warning(f"⚠️ Skipping Clay webhook for {analysis_result['company_name']} due to analysis error")
            return False
        
        payload = {
            "company_name": analysis_result['company_name'],
            "domain": analysis_result['domain'],
            "pain_signals": analysis_result['pain_signals']
        }
        
        try:
            response = requests.post(CLAY_WEBHOOK_URL, json=payload, timeout=30)
            
            if response.status_code == 200:
                logger.info(f"✅ Sent pain signals for {analysis_result['company_name']} to Clay")
                return True
            else:
                logger.error(f"❌ Clay webhook failed for {analysis_result['company_name']}: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Exception sending {analysis_result['company_name']} to Clay: {e}")
            return False
    
    def process_csv(self, csv_path: str):
        """
        Process entire CSV file
        """
        logger.info(f"📊 Processing CSV file: {csv_path}")
        
        total_processed = 0
        total_sent_to_clay = 0
        total_errors = 0
        
        try:
            with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for row in reader:
                    # Support multiple column name variations
                    company_name = (row.get("company_name") or 
                                  row.get("Company Name") or 
                                  row.get("Company") or 
                                  row.get("Name"))
                    
                    domain = (row.get("domain") or 
                            row.get("Domain") or 
                            row.get("Website") or 
                            row.get("URL"))
                    
                    if not company_name or not domain:
                        logger.warning(f"⚠️ Skipping row with missing data: {row}")
                        total_errors += 1
                        continue
                    
                    # Clean domain
                    domain = domain.strip().lower()
                    if domain.startswith('http'):
                        domain = domain.split('//')[-1].split('/')[0]
                    
                    # Analyze company
                    analysis_result = self.analyze_company(company_name.strip(), domain)
                    total_processed += 1
                    
                    # Send to Clay
                    if self.send_to_clay(analysis_result):
                        total_sent_to_clay += 1
                    
                    logger.info(f"📈 Progress: {total_processed} analyzed, {total_sent_to_clay} sent to Clay, {total_errors} errors")
                    
        except FileNotFoundError:
            logger.error(f"❌ CSV file not found: {csv_path}")
            return
        except Exception as e:
            logger.error(f"❌ Error processing CSV: {e}")
            return
        
        # Final summary
        logger.info(f"""
        ==========================================
        PAIN SIGNAL ANALYSIS COMPLETE
        ==========================================
        Total companies processed: {total_processed}
        Successfully sent to Clay: {total_sent_to_clay}
        Errors encountered: {total_errors}
        Success rate: {(total_sent_to_clay/total_processed)*100:.1f}% 
        ==========================================
        """)

def main():
    """
    Main CLI entry point
    """
    if len(sys.argv) < 2:
        print("Usage: python pain_signal_only.py prospects.csv")
        print("Example: python pain_signal_only.py /path/to/your/prospects.csv")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    
    # Initialize processor
    processor = PainSignalProcessor()
    
    # Process the CSV
    processor.process_csv(csv_path)

if __name__ == "__main__":
    main()
