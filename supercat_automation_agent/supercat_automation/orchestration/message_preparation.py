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