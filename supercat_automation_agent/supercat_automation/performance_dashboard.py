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
