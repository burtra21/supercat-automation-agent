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