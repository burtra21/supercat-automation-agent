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