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