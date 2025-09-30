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