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