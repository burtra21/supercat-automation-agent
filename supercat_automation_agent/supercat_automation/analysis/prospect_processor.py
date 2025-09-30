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
    Universal processor for prospects from any source
    Can validate existing clients or analyze new prospects
    """
    
    def __init__(self):
        self.pain_detector = MultiSourcePainDetector()
        self.website_extractor = WebsiteEvidenceExtractor()
    
    async def process_csv_upload(self, csv_path: str, is_client_validation: bool = False) -> Dict:
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
    
    async def process_single_prospect(self, company_data: Dict) -> Dict:
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
    
    async def validate_existing_clients(self, client_list: List[Dict]) -> Dict:
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
    
    def _prepare_company_data(self, row: pd.Series) -> Dict:
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
    
    async def _save_prospect(self, company_data: Dict, analysis: Dict, is_validation: bool) -> bool:
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
    
    def _validate_client_score(self, client_row: pd.Series, analysis: Dict) -> Dict:
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
        """Convert tier to number for comparison"""
        
        tiers = {
            'TIER_1_IMMEDIATE': 4,
            'TIER_2_QUARTERLY': 3,
            'TIER_3_NURTURE': 2,
            'TIER_4_MONITOR': 1,
            'UNKNOWN': 0
        }
        
        return tiers.get(tier, 0)
    
    def _generate_processing_summary(self, results: Dict, is_validation: bool) -> str:
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
    
    def _generate_validation_insights(self, validation_results: Dict) -> List[str]:
        """Generate insights from validation"""
        
        insights = []
        
        # Overall accuracy
        accuracy = (validation_results['accurately_scored'] / validation_results['total_clients'] * 100) if validation_results['total_clients'] else 0
        insights.append(f"Overall accuracy: {accuracy:.1f}%")
        
        # Tendency analysis
        if validation_results['overscored'] > validation_results['underscored']:
            insights.append("⚠️ System tends to OVERSCORE (too optimistic)")
        elif validation_results['underscored'] > validation_results['overscored']:
            insights.append("⚠️ System tends to UNDERSCORE (too conservative)")
        else:
            insights.append("✅ Scoring is well-balanced")
        
        # EDP correlation
        best_edp = None
        best_correlation = 0
        
        for edp, stats in validation_results['edp_correlation'].items():
            if stats['total'] > 0:
                correlation = stats['won'] / stats['total']
                if correlation > best_correlation:
                    best_correlation = correlation
                    best_edp = edp
        
        if best_edp:
            insights.append(f"🎯 Best predictor: {best_edp} ({best_correlation*100:.0f}% win rate)")
        
        return insights