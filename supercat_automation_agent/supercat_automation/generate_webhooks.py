#!/usr/bin/env python3
"""
SuperCat Webhook Processor - Generates Clay-ready webhooks
Processes CSV and outputs campaign-ready JSON webhooks
"""

import pandas as pd
import requests
import json
from typing import Dict, List, Any
from datetime import datetime, timedelta
import argparse
from pathlib import Path
import time
import re
import uuid
import urllib3
import sys
import os

# Add the parent directory to sys.path to import from sibling modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Import enhanced website analysis
try:
    from scrapers.website_evidence import WebsiteEvidenceExtractor
    ENHANCED_ANALYSIS_AVAILABLE = True
except ImportError:
    print("⚠️  Enhanced analysis not available - using basic analysis")
    ENHANCED_ANALYSIS_AVAILABLE = False

class SuperCatWebhookProcessor:
    """Generates Clay-ready webhook payloads with full campaigns"""
    
    def __init__(self, webhook_type="both"):
        # Webhook type: "analysis", "campaign", or "both"
        self.webhook_type = webhook_type
        
        # EDP definitions from won-deal analysis
        self.edp_weights = {
            'sales_enablement_collapse': 1.0,
            'technology_obsolescence': 0.93,
            'rep_performance_crisis': 0.71,
            'sku_complexity': 0.64,
            'channel_conflict': 0.43
        }
        
        # Trade show dates
        self.trade_shows = {
            'Vegas Market': datetime(2024, 1, 28),
            'High Point Market': datetime(2024, 4, 20)
        }
        
        # Customer testimonials from won deals
        self.testimonials = {
            'Butler Specialty': "eCat flexibly configures to the way we do business",
            'Godinger Silver': "Best thing in 25 years, reps are in love",
            'Wildwood Lamps': "Reduced calls by a third"
        }
        
        # Initialize enhanced analysis if available
        self.evidence_extractor = None
        if ENHANCED_ANALYSIS_AVAILABLE:
            try:
                self.evidence_extractor = WebsiteEvidenceExtractor()
                print("✅ Enhanced website analysis enabled")
            except Exception as e:
                print(f"⚠️  Enhanced analysis failed to initialize: {e}")
                self.evidence_extractor = None
    
    def analyze_website(self, domain: str) -> Dict[str, Any]:
        """Analyze website for pain signals - enhanced version with detailed evidence"""
        if not domain.startswith('http'):
            domain = f"https://{domain}"
        
        # Try enhanced analysis first
        if self.evidence_extractor:
            try:
                print("  🔍 Using enhanced website analysis...")
                evidence_data = self.evidence_extractor.analyze_website(domain)
                return self._process_enhanced_evidence(evidence_data)
            except Exception as e:
                print(f"  ⚠️  Enhanced analysis failed: {e}")
                print("  🔄 Falling back to basic analysis...")
        
        # Fallback to basic analysis
        return self._analyze_website_basic(domain)
    
    def _process_enhanced_evidence(self, evidence_data: Dict) -> Dict:
        """Process enhanced evidence into webhook format with detailed analysis"""
        
        result = {
            'edp_scores': {},
            'primary_edp': None,
            'psi_score': 0,
            'tier': 'NOT_QUALIFIED',
            'urgency': 'none',
            'evidence': [],
            'detailed_evidence': {}
        }
        
        # Extract EDP scores and detailed evidence
        if 'edp_evidence' in evidence_data:
            for edp_name, evidence in evidence_data['edp_evidence'].items():
                score = evidence.get('score', 0)
                result['edp_scores'][edp_name] = score
                
                # Collect key evidence
                if evidence.get('specific_issues'):
                    result['evidence'].extend(evidence['specific_issues'][:2])
                
                # Store detailed evidence with indicators, issues, and strength
                result['detailed_evidence'][edp_name] = {
                    'score': score,
                    'indicators': evidence.get('indicators_found', []),
                    'issues': evidence.get('specific_issues', []),
                    'strength': evidence.get('evidence_strength', 'none')
                }
        
        # Add specific findings from enhanced analysis
        if 'specific_findings' in evidence_data:
            result['detailed_evidence']['specific_findings'] = evidence_data['specific_findings']
        
        # Use TAM indicators if available for enhanced scoring
        if 'tam_indicators' in evidence_data:
            tam = evidence_data['tam_indicators']
            result['primary_edp'] = tam.get('primary_edp', 'unknown')
            result['psi_score'] = tam.get('total_pain_score', 0) * 100 / 3  # Normalize to 0-100
            
            # Map tier from enhanced analysis
            tier_map = {
                'TIER_1_HOT': 'TIER_1_IMMEDIATE',
                'TIER_2_WARM': 'TIER_2_ACTIVE', 
                'TIER_3_COOL': 'TIER_3_NURTURE',
                'TIER_4_COLD': 'NOT_QUALIFIED'
            }
            result['tier'] = tier_map.get(tam.get('tier', 'TIER_4_COLD'), 'NOT_QUALIFIED')
        else:
            # Calculate manually if TAM not available
            if result['edp_scores']:
                # Calculate PSI score
                psi_score = sum(score * self.edp_weights[edp] for edp, score in result['edp_scores'].items()) / sum(self.edp_weights.values())
                result['psi_score'] = psi_score * 100
                
                # Find primary EDP
                result['primary_edp'] = max(result['edp_scores'].items(), key=lambda x: x[1] * self.edp_weights[x[0]])[0]
                
                # Determine tier
                if psi_score >= 0.5:
                    result['tier'] = "TIER_1_IMMEDIATE"
                elif psi_score >= 0.35:
                    result['tier'] = "TIER_2_ACTIVE"
                elif psi_score >= 0.25:
                    result['tier'] = "TIER_3_NURTURE"
                else:
                    result['tier'] = "NOT_QUALIFIED"
        
        # Determine urgency
        if result['psi_score'] >= 50:
            result['urgency'] = "high"
        elif result['psi_score'] >= 35:
            result['urgency'] = "medium"
        elif result['psi_score'] >= 25:
            result['urgency'] = "low"
        else:
            result['urgency'] = "none"
        
        # Limit evidence to top 5
        result['evidence'] = result['evidence'][:5]
        
        return result
    
    def _analyze_website_basic(self, domain: str) -> Dict[str, Any]:
        """Basic website analysis - fallback method"""
        if not domain.startswith('http'):
            domain = f"https://{domain}"
        
        edp_scores = {}
        evidence = []
        
        try:
            response = requests.get(domain, timeout=10, verify=False)
            html_content = response.text.lower()
            
            # Sales Enablement Collapse
            sales_score = 0
            if 'product search' not in html_content:
                sales_score += 0.3
                evidence.append("No product search")
            if '.pdf' in html_content and 'catalog' in html_content:
                sales_score += 0.3
                evidence.append("PDF-only catalogs")
            if 'dealer login' in html_content:
                sales_score += 0.2
                evidence.append("Manual dealer login")
            if 'request quote' in html_content:
                sales_score += 0.2
                evidence.append("Manual quote requests")
            edp_scores['sales_enablement_collapse'] = min(sales_score, 1.0)
            
            # Technology Obsolescence
            tech_score = 0
            copyright_match = re.search(r'©\s*(\d{4})', html_content)
            if copyright_match and int(copyright_match.group(1)) < 2022:
                tech_score += 0.4
                evidence.append(f"Outdated copyright")
            if not response.url.startswith('https'):
                tech_score += 0.3
                evidence.append("No SSL")
            if 'csv' in html_content and 'upload' in html_content:
                tech_score += 0.3
                evidence.append("CSV-based processes")
            edp_scores['technology_obsolescence'] = min(tech_score, 1.0)
            
            # Rep Performance Crisis
            rep_score = 0
            if 'find a rep' not in html_content:
                rep_score += 0.3
                evidence.append("No rep locator")
            if 'sales resources' not in html_content:
                rep_score += 0.4
                evidence.append("No sales resources")
            if 'territory' not in html_content:
                rep_score += 0.3
                evidence.append("No territory info")
            edp_scores['rep_performance_crisis'] = min(rep_score, 1.0)
            
            # SKU Complexity
            sku_score = 0
            if 'configure' in html_content or 'customize' in html_content:
                sku_score += 0.3
                evidence.append("Configuration complexity")
            if 'options' in html_content and 'finishes' in html_content:
                sku_score += 0.3
                evidence.append("Multiple options/finishes")
            if re.search(r'\d{3,}\s*products', html_content):
                sku_score += 0.4
                evidence.append("Large catalog")
            edp_scores['sku_complexity'] = min(sku_score, 1.0)
            
            # Channel Conflict
            channel_score = 0
            if html_content.count('login') > 2:
                channel_score += 0.4
                evidence.append("Multiple logins")
            if 'dealer price' in html_content:
                channel_score += 0.3
                evidence.append("Multiple pricing tiers")
            if 'where to buy' in html_content:
                channel_score += 0.3
                evidence.append("Mixed channels")
            edp_scores['channel_conflict'] = min(channel_score, 1.0)
            
        except Exception as e:
            edp_scores = {edp: 0.5 for edp in self.edp_weights.keys()}
            evidence.append(f"Analysis error: {str(e)}")
        
        # Calculate PSI score
        psi_score = sum(score * self.edp_weights[edp] for edp, score in edp_scores.items()) / sum(self.edp_weights.values())
        
        # Determine tier (adjusted thresholds for better distribution)
        if psi_score >= 0.5:  # Was 0.7
            tier = "TIER_1_IMMEDIATE"
            urgency = "high"
        elif psi_score >= 0.35:  # Was 0.5
            tier = "TIER_2_ACTIVE"
            urgency = "medium"
        elif psi_score >= 0.25:  # Was 0.3
            tier = "TIER_3_NURTURE"
            urgency = "low"
        else:
            tier = "NOT_QUALIFIED"
            urgency = "none"
        
        # Find primary EDP
        primary_edp = max(edp_scores.items(), key=lambda x: x[1] * self.edp_weights[x[0]])[0]
        
        return {
            'edp_scores': edp_scores,
            'psi_score': psi_score * 100,  # Convert to percentage
            'tier': tier,
            'urgency': urgency,
            'primary_edp': primary_edp,
            'evidence': evidence,
            'detailed_evidence': {}  # Empty for basic analysis
        }
    
    def generate_email_sequence(self, company_name: str, primary_edp: str, urgency: str) -> List[Dict]:
        """Generate 7-email sequence based on primary EDP"""
        
        # Calculate days until next trade show
        today = datetime.now()
        days_until_vegas = (self.trade_shows['Vegas Market'] - today).days
        days_until_high_point = (self.trade_shows['High Point Market'] - today).days
        days_until_show = min(days_until_vegas, days_until_high_point) if days_until_vegas > 0 else days_until_high_point
        
        sequences = {
            'sales_enablement_collapse': [
                {
                    "day": 0,
                    "subject": "Trade show order processing question",
                    "body": f"Hi {{{{first_name}}}},\n\nNoticed you have trade shows coming up. A study of 127 furniture exhibitors found that 78% lose orders due to system connectivity issues.\n\nButler Specialty eliminated this with offline order processing - gained 23% more show revenue.\n\nWhat's your current backup plan when WiFi fails?\n\nBest,\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "Butler Specialty case study",
                    "body": f"{{{{first_name}}}},\n\nFollowing up on trade show challenges - Butler Specialty's President shared their results:\n\n- 67% faster order processing\n- Zero system downtime at shows\n- 23% revenue increase at High Point\n\nHappy to share their 2-minute case study if helpful.\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 7,
                    "subject": "Industry benchmark data",
                    "body": f"{{{{first_name}}}},\n\nFurniture Trade Council data shows manual order processing averages 18% error rates.\n\nTop performers using digital tools: 3% error rates.\n\nGodinger Silver reduced errors by 84% and saved 15 hours weekly per rep.\n\nWorth exploring?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 10,
                    "subject": "Quick ROI estimate",
                    "body": f"{{{{first_name}}}},\n\nRan some industry benchmarks:\n\n- Average rep saves 12 hours/week\n- Order accuracy improves 75%\n- Trade show revenue typically up 15-25%\n\nMost clients see payback in 4-6 months.\n\nInterested in a custom analysis?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 14,
                    "subject": "Peer company results",
                    "body": f"{{{{first_name}}}},\n\nThought you'd find this interesting - similar-sized company results:\n\n- 40% faster quotes\n- 15% more orders per show\n- Reps love the mobile access\n\nHere's their 90-second story: [link]\n\n{{{{sender_name}}}}"
                }
            ],
            'technology_obsolescence': [
                {
                    "day": 0,
                    "subject": "Catalog update speed study",
                    "body": f"Hi {{{{first_name}}}},\n\nNew industry study: Companies with legacy catalog systems take 5.2x longer to update pricing than modern platforms.\n\nAshley Furniture cut their update time from 3 days to 2 hours - gained competitive edge in fast-moving markets.\n\nWhat's your current pricing update timeline?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "Ashley Furniture case study",
                    "body": f"{{{{first_name}}}},\n\nAshley Furniture's results after modernizing:\n\n- 94% faster catalog updates\n- 31% more quote requests\n- No IT infrastructure changes needed\n\nThey kept their existing ERP - just added modern layer on top.\n\nInterested in their approach?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 7,
                    "subject": "Market response time data",
                    "body": f"{{{{first_name}}}},\n\nFurniture Today research: Companies responding to price changes within 24 hours win 67% more competitive deals.\n\nSimilar-sized company reduced response time from 72 hours to 4 hours - saw 28% quote increase.\n\nWorth exploring?\n\n{{{{sender_name}}}}"
                }
            ],
            'rep_performance_crisis': [
                {
                    "day": 0,
                    "subject": "Rep productivity study results",
                    "body": f"Hi {{{{first_name}}}},\n\nFurniture rep performance study: Top 20% use digital tools 8-12x daily. Bottom 20% use them less than 2x daily.\n\nHooker Furniture gained visibility into rep activity - improved bottom quartile performance by 45%.\n\nHow do you currently track rep engagement?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "Hooker Furniture case study",
                    "body": f"{{{{first_name}}}},\n\nHooker Furniture's rep performance results:\n\n- 45% improvement in underperformer productivity\n- 23% reduction in rep turnover\n- Early warning system for at-risk reps\n\nTheir VP Sales calls it 'game-changing visibility.'\n\nInterested in their approach?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 7,
                    "subject": "Industry turnover costs",
                    "body": f"{{{{first_name}}}},\n\nNational Furniture Rep Association data: Average replacement cost per rep is $47,000.\n\nCompany with similar profile reduced turnover from 31% to 19% using performance analytics.\n\nROI was 340% in year one.\n\nWorth exploring?\n\n{{{{sender_name}}}}"
                }
            ],
            'sku_complexity': [
                {
                    "day": 0,
                    "subject": "SKU management benchmark study",
                    "body": f"Hi {{{{first_name}}}},\n\nNew research: Companies with 1000+ SKUs lose average 12% revenue to catalog errors and outdated information.\n\nBernhardt Furniture reduced catalog maintenance from 40 hours/week to 6 hours using automated systems.\n\nHow much time does SKU management take your team?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "Bernhardt Furniture results",
                    "body": f"{{{{first_name}}}},\n\nBernhardt's catalog automation results:\n\n- 85% reduction in maintenance time\n- 94% fewer pricing errors\n- Reps always have current information\n\nTheir merchandising team now focuses on strategy, not data entry.\n\nInterested in their approach?\n\n{{{{sender_name}}}}"
                }
            ],
            'channel_conflict': [
                {
                    "day": 0,
                    "subject": "Channel pricing study",
                    "body": f"Hi {{{{first_name}}}},\n\nChannel conflict study: 73% of furniture manufacturers struggle with inconsistent pricing across dealer networks.\n\nLegacy Furniture solved this with automated pricing controls - reduced conflicts by 89%.\n\nHow do you ensure consistent pricing across channels?\n\n{{{{sender_name}}}}"
                },
                {
                    "day": 3,
                    "subject": "Legacy Furniture case study",
                    "body": f"{{{{first_name}}}},\n\nLegacy Furniture's channel management results:\n\n- 89% reduction in pricing conflicts\n- Automatic territory protection\n- Improved dealer satisfaction scores\n\nTheir sales director calls it 'relationship-saving technology.'\n\nWorth exploring?\n\n{{{{sender_name}}}}"
                }
            ],
        }
        
        # Return the appropriate sequence or default to sales enablement
        base_sequence = sequences.get(primary_edp, sequences['sales_enablement_collapse'])
        
        # For tier 1, use all 7 emails. For tier 2, use first 5. For tier 3, use first 3.
        if urgency == "high":
            return base_sequence[:7]
        elif urgency == "medium":
            return base_sequence[:5]
        else:
            return base_sequence[:3]
    
    def generate_linkedin_sequence(self, company_name: str, primary_edp: str) -> List[Dict]:
        """Generate LinkedIn outreach sequence"""
        
        messages = {
            'sales_enablement_collapse': "saw some interesting trade show data that might be relevant to your operations. Happy to share if useful.",
            'technology_obsolescence': "came across a study on catalog modernization ROI that reminded me of your industry. Thought you might find it interesting.",
            'rep_performance_crisis': "noticed you work with sales reps - saw some interesting performance benchmarking data you might find valuable.",
            'sku_complexity': "saw a case study on SKU management automation that might be relevant to your catalog operations.",
            'channel_conflict': "came across some channel management research that reminded me of challenges in your industry."
        }
        
        message = messages.get(primary_edp, messages['sales_enablement_collapse'])
        
        return [
            {
                "type": "connection_request",
                "message": f"Hi {{{{first_name}}}}, {message}"
            },
            {
                "type": "follow_up_message",
                "day": 7,
                "message": f"{{{{first_name}}}}, thanks for connecting! What trends are you seeing in your sales operations lately?"
            }
        ]
    
    def generate_ad_sequence(self, company_name: str, primary_edp: str, persona_type: str) -> List[Dict]:
        """Generate social media ad sequence"""
        
        ad_templates = {
            'sales_enablement_collapse': {
                'facebook': [
                    {
                        "platform": "facebook",
                        "type": "carousel",
                        "headline": "Trade Show Orders Going Missing?",
                        "primary_text": "78% of furniture exhibitors lose orders due to system connectivity issues. See how Butler Specialty eliminated this problem.",
                        "cta": "Learn More",
                        "cards": [
                            {"headline": "The Problem", "description": "WiFi fails, orders lost"},
                            {"headline": "The Solution", "description": "Offline order processing"},
                            {"headline": "The Result", "description": "23% revenue increase"}
                        ]
                    }
                ],
                'linkedin': [
                    {
                        "platform": "linkedin",
                        "type": "single_image",
                        "headline": "Manual Order Processing Costs You $400K Annually",
                        "description": "Industry data shows 30% error rates with manual processes. See how furniture leaders are solving this.",
                        "cta": "Download Case Study"
                    }
                ]
            },
            'technology_obsolescence': {
                'facebook': [
                    {
                        "platform": "facebook", 
                        "type": "video",
                        "headline": "Your Competitors Update Pricing 5x Faster",
                        "primary_text": "Legacy catalog systems make you 5.2x slower than modern platforms. Ashley Furniture cut update time from 3 days to 2 hours.",
                        "cta": "See How"
                    }
                ],
                'linkedin': [
                    {
                        "platform": "linkedin",
                        "type": "single_image", 
                        "headline": "67% More Competitive Deals Won",
                        "description": "Companies responding to price changes within 24 hours dominate their markets. Modern catalog systems are the key.",
                        "cta": "Get Case Study"
                    }
                ]
            },
            'rep_performance_crisis': {
                'facebook': [
                    {
                        "platform": "facebook",
                        "type": "carousel",
                        "headline": "Why Top Reps Outperform Bottom Reps 10:1",
                        "primary_text": "Top 20% of furniture reps use digital tools 8-12x daily. Bottom 20% use them less than 2x daily. See the difference.",
                        "cta": "Learn More",
                        "cards": [
                            {"headline": "The Gap", "description": "10:1 performance difference"},
                            {"headline": "The Cause", "description": "Tool usage frequency"},
                            {"headline": "The Fix", "description": "Performance visibility"}
                        ]
                    }
                ],
                'linkedin': [
                    {
                        "platform": "linkedin",
                        "type": "single_image",
                        "headline": "$47,000 Cost Per Rep Turnover",
                        "description": "Hooker Furniture reduced turnover 23% with performance analytics. ROI was 340% in year one.",
                        "cta": "See Results"
                    }
                ]
            },
            'sku_complexity': {
                'facebook': [
                    {
                        "platform": "facebook",
                        "type": "single_image",
                        "headline": "1000+ SKUs = 12% Revenue Loss",
                        "primary_text": "Catalog errors and outdated information cost furniture companies with complex SKUs millions annually.",
                        "cta": "Get Solution"
                    }
                ],
                'linkedin': [
                    {
                        "platform": "linkedin", 
                        "type": "carousel",
                        "headline": "85% Reduction in Catalog Maintenance",
                        "description": "Bernhardt Furniture cut catalog work from 40 hours/week to 6 hours using automation.",
                        "cta": "Learn How"
                    }
                ]
            },
            'channel_conflict': {
                'facebook': [
                    {
                        "platform": "facebook",
                        "type": "video",
                        "headline": "Channel Conflicts Destroying Dealer Relationships?",
                        "primary_text": "73% of furniture manufacturers struggle with inconsistent pricing. Legacy Furniture solved this with 89% conflict reduction.",
                        "cta": "See Case Study"
                    }
                ],
                'linkedin': [
                    {
                        "platform": "linkedin",
                        "type": "single_image",
                        "headline": "89% Reduction in Pricing Conflicts", 
                        "description": "Automated pricing controls save dealer relationships and boost satisfaction scores.",
                        "cta": "Get Details"
                    }
                ]
            }
        }
        
        # Get ads for the primary EDP, fallback to sales_enablement_collapse
        edp_ads = ad_templates.get(primary_edp, ad_templates['sales_enablement_collapse'])
        
        # Combine Facebook and LinkedIn ads
        all_ads = []
        all_ads.extend(edp_ads.get('facebook', []))
        all_ads.extend(edp_ads.get('linkedin', []))
        
        return all_ads
    
    def generate_webhook(self, company_data: Dict, analysis: Dict) -> Dict:
        """Generate complete webhook payload for Clay"""
        
        # Determine persona based on primary EDP
        persona_map = {
            'sales_enablement_collapse': 'sales_leadership',
            'technology_obsolescence': 'it_leadership',
            'rep_performance_crisis': 'sales_leadership',
            'sku_complexity': 'operations',
            'channel_conflict': 'c_suite'
        }
        
        primary_persona = persona_map.get(analysis['primary_edp'], 'sales_leadership')
        
        # Calculate days until next show
        today = datetime.now()
        days_until_vegas = (self.trade_shows['Vegas Market'] - today).days
        days_until_high_point = (self.trade_shows['High Point Market'] - today).days
        days_until_show = min(days_until_vegas, days_until_high_point) if days_until_vegas > 0 else days_until_high_point
        
        # Determine campaign strategy
        if analysis['urgency'] == 'high' and days_until_show < 60:
            strategy = "aggressive_trade_show"
        elif analysis['urgency'] == 'high':
            strategy = "aggressive_problem"
        elif analysis['urgency'] == 'medium':
            strategy = "educational"
        else:
            strategy = "nurture"
        
        webhook = {
            "company_id": str(uuid.uuid4()),
            "company_name": company_data['company_name'],
            "domain": company_data['domain'].replace('https://', '').replace('http://', ''),
            "tam_tier": analysis['tier'],
            "psi_score": round(analysis['psi_score'], 1),
            "primary_edp": analysis['primary_edp'],
            "edp_scores": analysis['edp_scores'],
            "evidence": analysis['evidence'][:5],  # Top 5 evidence points
            "detailed_evidence": analysis.get('detailed_evidence', {}),  # NEW: Detailed analysis
            "persona_type": primary_persona,
            "backup_persona": "c_suite" if primary_persona != "c_suite" else "sales_leadership",
            "persona_reason": f"Primary EDP is {analysis['primary_edp']}",
            "urgency_level": analysis['urgency'],
            "campaign_strategy": strategy,
            "days_until_show": days_until_show,
            "email_sequence": self.generate_email_sequence(
                company_data['company_name'],
                analysis['primary_edp'],
                analysis['urgency']
            ),
            "linkedin_sequence": self.generate_linkedin_sequence(
                company_data['company_name'],
                analysis['primary_edp']
            ),
            "ad_sequence": self.generate_ad_sequence(
                company_data['company_name'],
                analysis['primary_edp'],
                primary_persona
            ),
            "contact_info": {
                "first_name": self._clean_first_name(company_data.get('first_name', '')),
                "last_name": company_data.get('last_name', ''),
                "email": company_data.get('email', ''),
                "title": company_data.get('title', ''),
                "linkedin": company_data.get('LinkedIn Profile', '')
            },
            "company_info": {
                "industry": company_data.get('industry', ''),
                "employee_count": company_data.get('employee_count', '')
            },
            "created_at": datetime.now().isoformat(),
            "webhook_version": "3.0"  # Updated version for detailed analysis
        }
        
        return webhook
    
    def generate_analysis_webhook(self, company_data: Dict, analysis: Dict) -> Dict:
        """Generate webhook focused on company analysis and scoring"""
        
        webhook = {
            "webhook_type": "analysis",
            "company_id": str(uuid.uuid4()),
            "company_name": company_data['company_name'],
            "domain": company_data['domain'].replace('https://', '').replace('http://', ''),
            "tam_tier": analysis['tier'],
            "psi_score": round(analysis['psi_score'], 1),
            "primary_edp": analysis['primary_edp'],
            "edp_scores": analysis['edp_scores'],
            "evidence": analysis['evidence'][:10],  # More evidence for analysis
            "detailed_evidence": analysis.get('detailed_evidence', {}),
            "urgency_level": analysis['urgency'],
            "website_analysis": {
                "technology_stack": analysis.get('tech_stack', {}),
                "seo_metrics": analysis.get('seo_data', {}),
                "content_analysis": analysis.get('content_analysis', {}),
                "user_experience": analysis.get('ux_analysis', {})
            },
            "competitive_positioning": {
                "market_segment": self._determine_market_segment(company_data),
                "competitive_threats": analysis.get('competitive_threats', []),
                "differentiation_opportunities": analysis.get('differentiation', [])
            },
            "contact_info": {
                "first_name": self._clean_first_name(company_data.get('first_name', '')),
                "last_name": company_data.get('last_name', ''),
                "email": company_data.get('email', ''),
                "title": company_data.get('title', ''),
                "linkedin": company_data.get('LinkedIn Profile', '')
            },
            "company_info": {
                "industry": company_data.get('industry', ''),
                "employee_count": company_data.get('employee_count', ''),
                "revenue_estimate": company_data.get('revenue', ''),
                "headquarters": company_data.get('hq_location', '')
            },
            "analysis_metadata": {
                "analysis_date": datetime.now().isoformat(),
                "data_sources": ["website_analysis", "contact_enrichment"],
                "confidence_score": analysis.get('confidence', 0.8),
                "last_updated": datetime.now().isoformat()
            },
            "webhook_version": "4.0_analysis"
        }
        
        return webhook
    
    def generate_campaign_webhook(self, company_data: Dict, analysis: Dict) -> Dict:
        """Generate webhook focused on campaigns and outreach"""
        
        # Determine persona
        persona_map = {
            'sales_enablement_collapse': 'sales_leadership',
            'technology_obsolescence': 'c_suite', 
            'rep_performance_crisis': 'sales_leadership',
            'sku_complexity': 'c_suite',
            'channel_conflict': 'sales_leadership'
        }
        primary_persona = persona_map.get(analysis['primary_edp'], 'c_suite')
        
        # Calculate show urgency
        days_until_show = self._calculate_show_urgency(company_data.get('trade_shows', []))
        
        # Determine campaign strategy
        if analysis['urgency'] == 'high' and days_until_show < 60:
            strategy = "aggressive_trade_show"
        elif analysis['urgency'] == 'high':
            strategy = "aggressive_problem"
        elif analysis['urgency'] == 'medium':
            strategy = "educational"
        else:
            strategy = "nurture"
        
        webhook = {
            "webhook_type": "campaign",
            "company_id": str(uuid.uuid4()),
            "company_name": company_data['company_name'],
            "domain": company_data['domain'].replace('https://', '').replace('http://', ''),
            "tam_tier": analysis['tier'],
            "psi_score": round(analysis['psi_score'], 1),
            "primary_edp": analysis['primary_edp'],
            "persona_type": primary_persona,
            "backup_persona": "c_suite" if primary_persona != "c_suite" else "sales_leadership",
            "persona_reason": f"Primary EDP is {analysis['primary_edp']}",
            "urgency_level": analysis['urgency'],
            "campaign_strategy": strategy,
            "days_until_show": days_until_show,
            "email_sequence": self.generate_email_sequence(
                company_data['company_name'],
                analysis['primary_edp'],
                analysis['urgency']
            ),
            "linkedin_sequence": self.generate_linkedin_sequence(
                company_data['company_name'],
                analysis['primary_edp']
            ),
            "ad_sequence": self.generate_ad_sequence(
                company_data['company_name'],
                analysis['primary_edp'],
                primary_persona
            ),
            "campaign_timeline": self._generate_campaign_timeline(strategy, days_until_show),
            "follow_up_schedule": self._generate_follow_up_schedule(analysis['urgency']),
            "contact_info": {
                "first_name": self._clean_first_name(company_data.get('first_name', '')),
                "last_name": company_data.get('last_name', ''),
                "email": company_data.get('email', ''),
                "title": company_data.get('title', ''),
                "linkedin": company_data.get('LinkedIn Profile', '')
            },
            "campaign_metadata": {
                "created_at": datetime.now().isoformat(),
                "expected_duration": self._calculate_campaign_duration(strategy),
                "success_metrics": self._define_success_metrics(analysis['tier']),
                "optimization_notes": self._generate_optimization_notes(analysis)
            },
            "webhook_version": "4.0_campaign"
        }
        
        return webhook
    
    def _clean_first_name(self, first_name: str) -> str:
        """Clean and validate first name to avoid company names"""
        if not first_name:
            return ""
        
        # Common indicators this might be a company name instead of first name
        company_indicators = [
            'inc', 'llc', 'ltd', 'corp', 'company', 'co.', 'enterprises', 
            'industries', 'group', 'holdings', 'international', 'furniture',
            'lighting', 'design', 'studio', 'collection', 'brands'
        ]
        
        first_name_lower = first_name.lower().strip()
        
        # If it contains company indicators, it's probably not a first name
        for indicator in company_indicators:
            if indicator in first_name_lower:
                print(f"  ⚠️  Possible company name in first_name field: '{first_name}' - clearing")
                return ""
        
        # If it's too long (>25 chars), likely not a first name
        if len(first_name) > 25:
            print(f"  ⚠️  First name too long: '{first_name}' - clearing")
            return ""
        
        # If it contains multiple words and looks like a company
        words = first_name.split()
        if len(words) > 2:
            print(f"  ⚠️  First name has too many words: '{first_name}' - clearing")
            return ""
        
        return first_name.strip()
    
    def _determine_market_segment(self, company_data: Dict) -> str:
        """Determine market segment based on company data"""
        employee_count = company_data.get('employee_count', 0)
        if isinstance(employee_count, str):
            try:
                employee_count = int(employee_count)
            except:
                employee_count = 0
        
        if employee_count > 500:
            return "enterprise"
        elif employee_count > 100:
            return "mid_market"
        else:
            return "smb"
    
    def _generate_campaign_timeline(self, strategy: str, days_until_show: int) -> Dict:
        """Generate campaign timeline based on strategy"""
        if strategy == "aggressive_trade_show":
            return {
                "phase_1": "immediate_outreach",
                "phase_2": "pre_show_follow_up",
                "phase_3": "show_meeting_request",
                "total_duration_days": min(days_until_show, 21)
            }
        elif strategy == "aggressive_problem":
            return {
                "phase_1": "problem_identification",
                "phase_2": "solution_education", 
                "phase_3": "demo_request",
                "total_duration_days": 14
            }
        elif strategy == "educational":
            return {
                "phase_1": "awareness_building",
                "phase_2": "educational_content",
                "phase_3": "soft_engagement",
                "total_duration_days": 28
            }
        else:  # nurture
            return {
                "phase_1": "relationship_building",
                "phase_2": "value_demonstration",
                "phase_3": "long_term_engagement",
                "total_duration_days": 60
            }
    
    def _generate_follow_up_schedule(self, urgency: str) -> List[Dict]:
        """Generate follow-up schedule based on urgency"""
        if urgency == "high":
            return [
                {"day": 3, "action": "personal_follow_up", "channel": "email"},
                {"day": 7, "action": "linkedin_message", "channel": "linkedin"},
                {"day": 10, "action": "phone_call", "channel": "phone"},
                {"day": 14, "action": "final_email", "channel": "email"}
            ]
        elif urgency == "medium":
            return [
                {"day": 5, "action": "follow_up_email", "channel": "email"},
                {"day": 12, "action": "linkedin_message", "channel": "linkedin"},
                {"day": 21, "action": "value_add_email", "channel": "email"}
            ]
        else:  # low
            return [
                {"day": 7, "action": "educational_content", "channel": "email"},
                {"day": 21, "action": "industry_insights", "channel": "linkedin"},
                {"day": 42, "action": "check_in", "channel": "email"}
            ]
    
    def _calculate_campaign_duration(self, strategy: str) -> int:
        """Calculate expected campaign duration in days"""
        duration_map = {
            "aggressive_trade_show": 21,
            "aggressive_problem": 14,
            "educational": 28,
            "nurture": 60
        }
        return duration_map.get(strategy, 28)
    
    def _define_success_metrics(self, tier: str) -> Dict:
        """Define success metrics based on tier"""
        if tier == "TIER_1_IMMEDIATE":
            return {
                "primary_goal": "meeting_booked",
                "secondary_goal": "demo_scheduled",
                "engagement_threshold": 0.4,
                "response_target_days": 7
            }
        elif tier == "TIER_2_ACTIVE":
            return {
                "primary_goal": "qualified_conversation",
                "secondary_goal": "content_engagement",
                "engagement_threshold": 0.3,
                "response_target_days": 14
            }
        else:  # TIER_3_NURTURE
            return {
                "primary_goal": "relationship_building",
                "secondary_goal": "awareness_increase",
                "engagement_threshold": 0.2,
                "response_target_days": 30
            }
    
    def _generate_optimization_notes(self, analysis: Dict) -> List[str]:
        """Generate optimization notes for campaign improvement"""
        notes = []
        
        if analysis['psi_score'] > 70:
            notes.append("High pain score - emphasize urgency and immediate value")
        elif analysis['psi_score'] > 40:
            notes.append("Moderate pain - focus on education and ROI demonstration")
        else:
            notes.append("Lower pain - build relationship and awareness first")
        
        if analysis['primary_edp'] == 'sales_enablement_collapse':
            notes.append("Focus on rep productivity and sales process efficiency")
        elif analysis['primary_edp'] == 'technology_obsolescence':
            notes.append("Emphasize modernization and competitive advantage")
        elif analysis['primary_edp'] == 'rep_performance_crisis':
            notes.append("Highlight performance tracking and coaching capabilities")
        
        return notes

    def _calculate_show_urgency(self, trade_shows: List[str]) -> int:
        """Calculate days until next trade show"""
        today = datetime.now()
        days_until_vegas = (self.trade_shows['Vegas Market'] - today).days
        days_until_high_point = (self.trade_shows['High Point Market'] - today).days
        return min(days_until_vegas, days_until_high_point) if days_until_vegas > 0 else days_until_high_point

def process_csv_to_webhooks(file_path: str, limit: int = None, output_dir: str = "webhooks", webhook_type: str = "both"):
    """Process CSV and generate webhook files"""
    
    print(f"\n{'='*60}")
    print(f"SUPERCAT WEBHOOK PROCESSOR")
    print(f"Webhook Type: {webhook_type.upper()}")
    print(f"{'='*60}\n")
    
    # Read CSV
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Error reading CSV: {str(e)}")
        return
    
    # Clean data
    df = df.dropna(subset=['company_name', 'domain'])
    
    if limit:
        df = df.head(limit)
    
    print(f"📊 Processing {len(df)} companies...")
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Initialize processor
    processor = SuperCatWebhookProcessor(webhook_type=webhook_type)
    
    # Process each company
    analysis_webhooks = []
    campaign_webhooks = []
    tier_counts = {'TIER_1_IMMEDIATE': 0, 'TIER_2_ACTIVE': 0, 'TIER_3_NURTURE': 0, 'NOT_QUALIFIED': 0}
    errors = []
    
    for idx, row in df.iterrows():
        company_data = row.to_dict()
        
        print(f"\nAnalyzing {company_data['company_name']}...")
        
        try:
            # Analyze website
            analysis = processor.analyze_website(company_data['domain'])
            
            # Skip if not qualified
            if analysis['tier'] == "NOT_QUALIFIED":
                print(f"  ❌ Not qualified (PSI: {analysis['psi_score']:.1f})")
                tier_counts['NOT_QUALIFIED'] += 1
                continue
            
            # Generate webhook(s) based on type
            if webhook_type in ["analysis", "both"]:
                analysis_webhook = processor.generate_analysis_webhook(company_data, analysis)
                analysis_webhooks.append(analysis_webhook)
            
            if webhook_type in ["campaign", "both"]:
                campaign_webhook = processor.generate_campaign_webhook(company_data, analysis)
                campaign_webhooks.append(campaign_webhook)
            
            tier_counts[analysis['tier']] += 1
            
            # Log personalization info
            if webhook_type in ["analysis", "both"]:
                first_name = analysis_webhook['contact_info']['first_name']
            else:
                first_name = campaign_webhook['contact_info']['first_name']
                
            if first_name:
                print(f"  👤 Contact: {first_name} ({company_data.get('title', 'N/A')})")
            else:
                print(f"  ⚠️  No first name available for personalization")
            
            # Sanitize company name for filename (remove special characters)
            safe_company_name = re.sub(r'[^\w\s-]', '', company_data['company_name'])
            safe_company_name = re.sub(r'[-\s]+', '_', safe_company_name)
            
            # Save individual webhook files
            if webhook_type in ["analysis", "both"]:
                analysis_file = Path(output_dir) / f"analysis_{analysis_webhook['company_id']}_{safe_company_name}.json"
                with open(analysis_file, 'w') as f:
                    json.dump(analysis_webhook, f, indent=2)
            
            if webhook_type in ["campaign", "both"]:
                campaign_file = Path(output_dir) / f"campaign_{campaign_webhook['company_id']}_{safe_company_name}.json"
                with open(campaign_file, 'w') as f:
                    json.dump(campaign_webhook, f, indent=2)
            
            # Print status
            if analysis['tier'] == 'TIER_1_IMMEDIATE':
                print(f"  🔥 TIER 1 - PSI: {analysis['psi_score']:.1f}% - {analysis['primary_edp']}")
            elif analysis['tier'] == 'TIER_2_ACTIVE':
                print(f"  ✅ TIER 2 - PSI: {analysis['psi_score']:.1f}% - {analysis['primary_edp']}")
            else:
                print(f"  📊 TIER 3 - PSI: {analysis['psi_score']:.1f}% - {analysis['primary_edp']}")
            
        except Exception as e:
            error_msg = f"Error processing {company_data['company_name']}: {str(e)}"
            print(f"  ⚠️ {error_msg}")
            errors.append(error_msg)
            continue
        
        time.sleep(0.5)  # Rate limiting
    
    # Save batch webhook files
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if analysis_webhooks:
        analysis_batch_file = Path(output_dir) / f"analysis_batch_{timestamp}.json"
        with open(analysis_batch_file, 'w') as f:
            json.dump(analysis_webhooks, f, indent=2)
        print(f"\n📊 Analysis batch file: {analysis_batch_file}")
    
    if campaign_webhooks:
        campaign_batch_file = Path(output_dir) / f"campaign_batch_{timestamp}.json"
        with open(campaign_batch_file, 'w') as f:
            json.dump(campaign_webhooks, f, indent=2)
        print(f"\n� Campaign batch file: {campaign_batch_file}")
    
    # Save CSV summary
    all_webhooks = []
    if webhook_type in ["analysis", "both"]:
        all_webhooks.extend(analysis_webhooks)
    if webhook_type in ["campaign", "both"]:
        all_webhooks.extend(campaign_webhooks)
    
    if all_webhooks:
        summary_df = pd.DataFrame([{
            'webhook_type': w.get('webhook_type', 'combined'),
            'company_name': w['company_name'],
            'domain': w['domain'],
            'tier': w['tam_tier'],
            'psi_score': w['psi_score'],
            'primary_edp': w['primary_edp'],
            'urgency': w.get('urgency_level', 'N/A'),
            'email': w['contact_info']['email'],
            'campaign_strategy': w.get('campaign_strategy', 'N/A')
        } for w in all_webhooks])
        
        summary_file = Path(output_dir) / f"summary_{timestamp}.csv"
        summary_df.to_csv(summary_file, index=False)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"PROCESSING COMPLETE")
    print(f"{'='*60}")
    print(f"🔥 Tier 1 (Immediate): {tier_counts['TIER_1_IMMEDIATE']}")
    print(f"✅ Tier 2 (Active): {tier_counts['TIER_2_ACTIVE']}")
    print(f"📊 Tier 3 (Nurture): {tier_counts['TIER_3_NURTURE']}")
    print(f"❌ Not Qualified: {tier_counts['NOT_QUALIFIED']}")
    print(f"\n📁 Output directory: {output_dir}/")
    if all_webhooks:
        print(f"📊 Summary CSV: {summary_file.name}")
    
    if webhook_type in ["analysis", "both"]:
        print(f"� Analysis webhooks: {len(analysis_webhooks)}")
    if webhook_type in ["campaign", "both"]:
        print(f"📧 Campaign webhooks: {len(campaign_webhooks)}")
    print(f"�🔗 Total webhooks generated: {len(all_webhooks)}")
    
    if errors:
        print(f"\n⚠️ Errors encountered: {len(errors)}")
        for error in errors[:5]:  # Show first 5 errors
            print(f"  - {error}")
    
    # Show top Tier 1 companies
    if tier_counts['TIER_1_IMMEDIATE'] > 0 and all_webhooks:
        print(f"\n🎯 TOP TIER 1 TARGETS:")
        print(f"{'='*60}")
        tier1_webhooks = [w for w in all_webhooks if w['tam_tier'] == 'TIER_1_IMMEDIATE']
        tier1_webhooks.sort(key=lambda x: x['psi_score'], reverse=True)
        
        for w in tier1_webhooks[:5]:
            print(f"• {w['company_name']} (PSI: {w['psi_score']:.1f}%)")
            print(f"  Primary Pain: {w['primary_edp'].replace('_', ' ').title()}")
            if 'campaign_strategy' in w:
                print(f"  Strategy: {w['campaign_strategy']}")
            if w['contact_info']['email']:
                print(f"  Contact: {w['contact_info']['email']}")
            print()
    
    return {
        'analysis_webhooks': analysis_webhooks,
        'campaign_webhooks': campaign_webhooks,
        'all_webhooks': all_webhooks
    }

def main():
    parser = argparse.ArgumentParser(description='Generate SuperCat webhook campaigns')
    parser.add_argument('csv_file', help='Path to prospects CSV')
    parser.add_argument('--test', type=int, help='Test with N companies')
    parser.add_argument('--output', default='webhooks', help='Output directory')
    parser.add_argument('--type', choices=['analysis', 'campaign', 'both'], default='both',
                       help='Type of webhook to generate (default: both)')
    
    args = parser.parse_args()
    
    if not Path(args.csv_file).exists():
        print(f"❌ File not found: {args.csv_file}")
        return
    
    process_csv_to_webhooks(
        file_path=args.csv_file,
        limit=args.test,
        output_dir=args.output,
        webhook_type=args.type
    )

if __name__ == "__main__":
    main()