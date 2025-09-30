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