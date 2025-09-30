# generation/pvp_ad_generator.py
"""
PVP-Quality Ad Copy Generator
Creates hyper-specific ads based on company evidence
"""

import logging
from typing import Dict, List, Any
import json

logger = logging.getLogger(__name__)

class PVPAdGenerator:
    """
    Generates evidence-based ad copy for multiple platforms
    Every ad references specific pain points and evidence
    """
    
    def generate_full_ad_campaign(self, company_analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate complete ad campaign across all platforms
        """
        
        ad_campaign = {
            'company_name': company_analysis['company_name'],
            'campaign_name': f"{company_analysis['company_name']}_PVP_{company_analysis['primary_edp']}",
            'google_ads': self._generate_google_ads_pvp(company_analysis, evidence),
            'meta_ads': self._generate_meta_ads_pvp(company_analysis, evidence),
            'linkedin_ads': self._generate_linkedin_ads_pvp(company_analysis, evidence),
            'display_ads': self._generate_display_ads_pvp(company_analysis, evidence),
            'retargeting': self._generate_retargeting_ads(company_analysis, evidence)
        }
        
        return ad_campaign
    
    def _generate_google_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate Google Ads with specific evidence
        """
        
        company_name = analysis['company_name']
        primary_edp = analysis['primary_edp']
        
        # Build specific headlines based on evidence
        headlines = []
        
        if evidence.get('website_findings'):
            for finding in evidence['website_findings'][:3]:
                if 'PDF' in finding:
                    headlines.append(f"{company_name}: Stop PDF Chaos")
                    headlines.append("PDF Catalogs Killing Sales?")
                elif 'mobile' in finding.lower():
                    headlines.append(f"{company_name}: No Mobile = Lost Sales")
                    headlines.append("Trade Shows Need Mobile")
                elif 'manual' in finding.lower():
                    headlines.append("3 Hours Daily Wasted")
                    headlines.append(f"{company_name}: Manual Orders?")
        
        # Add trade show specific if applicable
        if evidence.get('trade_show_data'):
            show = evidence['trade_show_data']['show_name']
            days = evidence['trade_show_data'].get('days_until_show', 35)
            headlines.append(f"{days} Days Until {show}")
            headlines.append(f"Booth #{evidence['trade_show_data'].get('booth_number', 'C-1055')} Ready?")
        
        # Fallback headlines
        if len(headlines) < 5:
            headlines.extend([
                "Furniture Sales Automation",
                "Stop Manual Order Processing",
                "Mobile Sales Enablement"
            ])
        
        # Descriptions based on evidence
        descriptions = []
        
        if evidence.get('trade_show_data'):
            booth_cost = evidence['trade_show_data'].get('booth_details', {}).get('estimated_cost', 32000)
            descriptions.append(
                f"Your ${booth_cost:,} booth investment needs mobile tools. "
                f"Work offline. Perfect accuracy. Setup in 14 days."
            )
        
        if 'manual' in str(evidence.get('website_findings', [])):
            descriptions.append(
                f"{company_name}: Save 3 hours daily per rep. "
                f"Eliminate order errors. Real customer: 'Best thing in 25 years.'"
            )
        
        descriptions.append(
            f"Built for {company_name}'s exact needs. "
            f"Works with your ERP. No IT project. See ROI in 47 days."
        )
        
        return {
            'platform': 'google_ads',
            'campaign_type': 'search',
            'ad_groups': [
                {
                    'name': f"{company_name}_Brand",
                    'headlines': headlines[:5],  # Google allows up to 15, we'll use 5
                    'descriptions': descriptions[:2],  # Google allows up to 4, we'll use 2
                    'display_url': f"supercatsolutions.com/{company_name.lower().replace(' ', '')}",
                    'final_url': f"https://supercatsolutions.com/demo?company={company_name}&utm_source=google&utm_medium=cpc&utm_campaign=pvp_{primary_edp}",
                    'keywords': self._generate_specific_keywords(analysis, evidence),
                    'negative_keywords': ['free', 'cheap', 'jobs', 'careers', 'used'],
                    'targeting': {
                        'company_name': company_name,
                        'radius': '50 miles',
                        'audience': 'furniture_manufacturers'
                    }
                }
            ],
            'extensions': {
                'sitelinks': [
                    {'text': 'See ROI Calculator', 'url': '/roi-calculator'},
                    {'text': 'Trade Show Solution', 'url': '/trade-show'},
                    {'text': 'Customer Success', 'url': '/customers'},
                    {'text': 'Book Demo', 'url': '/demo'}
                ],
                'callouts': [
                    'Works Offline',
                    'No IT Required',
                    'ROI in 47 Days',
                    'Perfect Order Accuracy'
                ],
                'structured_snippets': {
                    'header': 'Features',
                    'values': ['Mobile Orders', 'Offline Mode', 'ERP Integration', 'Trade Show Ready']
                }
            },
            'budget': {
                'daily': 150,
                'monthly': 4500,
                'bid_strategy': 'maximize_conversions',
                'target_cpa': 250
            }
        }
    
    def _generate_meta_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate Meta (Facebook/Instagram) ads with specific evidence
        """
        
        company_name = analysis['company_name']
        
        # Primary text with specific evidence
        primary_text_options = []
        
        if evidence.get('website_findings'):
            finding = evidence['website_findings'][0]
            primary_text_options.append(
                f"Still using {finding.lower()}? "
                f"{company_name} could save 3 hours daily per rep with mobile order management. "
                f"Butler Specialty called it 'the best thing in 25 years.'"
            )
        
        if evidence.get('trade_show_data'):
            show_data = evidence['trade_show_data']
            primary_text_options.append(
                f"📍 {company_name} - Booth #{show_data.get('booth_number', 'C-1055')} at {show_data['show_name']}\n\n"
                f"With {show_data.get('days_until_show', 35)} days until setup, you need mobile order capability. "
                f"Your ${show_data.get('booth_details', {}).get('estimated_cost', 32000):,} investment deserves better than paper forms.\n\n"
                f"✅ Work completely offline\n"
                f"✅ Perfect order accuracy\n"
                f"✅ Setup in 14 days"
            )
        
        # Carousel cards with specific pain points
        carousel_cards = []
        
        for i, finding in enumerate(evidence.get('website_findings', [])[:3]):
            carousel_cards.append({
                'headline': f"Problem #{i+1}",
                'description': finding,
                'cta': 'Fix This Issue'
            })
        
        # Add ROI card
        roi_data = self._calculate_simple_roi(analysis)
        carousel_cards.append({
            'headline': f"Save ${roi_data['annual_savings']:,}",
            'description': f"ROI in {roi_data['payback_days']} days",
            'cta': 'Calculate Your ROI'
        })
        
        return {
            'platform': 'meta',
            'campaign_objectives': ['lead_generation', 'traffic'],
            'ad_sets': [
                {
                    'name': f"{company_name}_Lookalike",
                    'targeting': {
                        'custom_audiences': [f"{company_name}_website_visitors"],
                        'lookalike_audiences': ['furniture_manufacturers_1%'],
                        'location': self._get_company_location(analysis),
                        'age': '25-65',
                        'interests': ['B2B', 'Trade Shows', 'Manufacturing', 'Sales Management'],
                        'behaviors': ['Business Decision Makers'],
                        'job_titles': ['VP Sales', 'Sales Director', 'IT Director', 'President', 'Owner']
                    },
                    'placements': ['facebook_feed', 'instagram_feed', 'audience_network'],
                    'budget': {
                        'daily': 100,
                        'bid_strategy': 'lowest_cost_with_bid_cap',
                        'bid_cap': 50
                    }
                }
            ],
            'creatives': [
                {
                    'format': 'single_image',
                    'primary_text': primary_text_options[0] if primary_text_options else f"{company_name}: Transform your sales process",
                    'headline': f"{company_name}: Save 3 Hours Daily",
                    'description': 'Mobile order management for furniture manufacturers',
                    'cta_button': 'Learn More',
                    'image_specs': {
                        'main_text': f"{company_name}\n3 Hours Saved Daily",
                        'subtext': 'Per Sales Rep',
                        'background': 'gradient_blue',
                        'logo_placement': 'bottom_right'
                    }
                },
                {
                    'format': 'carousel',
                    'cards': carousel_cards,
                    'primary_text': primary_text_options[1] if len(primary_text_options) > 1 else primary_text_options[0],
                    'headline': 'Fix These Issues Now',
                    'cta_button': 'Get Started'
                },
                {
                    'format': 'video',
                    'video_script': self._generate_video_script(analysis, evidence),
                    'primary_text': f"{company_name}: See how Butler Specialty transformed their sales",
                    'headline': 'Transform Sales in 14 Days',
                    'cta_button': 'Watch Demo'
                }
            ],
            'tracking': {
                'pixel_events': ['ViewContent', 'Lead', 'CompleteRegistration'],
                'utm_parameters': {
                    'source': 'meta',
                    'medium': 'paid_social',
                    'campaign': f'pvp_{company_name.lower().replace(" ", "_")}',
                    'content': '{creative_name}'
                }
            }
        }
    
    def _generate_linkedin_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate LinkedIn ads targeting specific company and competitors
        """
        
        company_name = analysis['company_name']
        
        # Intro text with specific pain point
        intro_texts = []
        
        if evidence.get('website_findings'):
            intro_texts.append(
                f"Attention {company_name} sales team:\n\n"
                f"Still struggling with {evidence['website_findings'][0].lower()}?"
            )
        
        if evidence.get('trade_show_data'):
            show = evidence['trade_show_data']['show_name']
            intro_texts.append(
                f"Preparing for {show}?\n\n"
                f"Don't let manual processes ruin your ${evidence['trade_show_data'].get('booth_details', {}).get('estimated_cost', 32000):,} investment."
            )
        
        return {
            'platform': 'linkedin',
            'campaign_type': 'sponsored_content',
            'objective': 'lead_generation',
            'formats': [
                {
                    'type': 'single_image',
                    'intro_text': intro_texts[0] if intro_texts else f"{company_name}: Transform your sales process",
                    'headline': f"{company_name}: Eliminate Manual Order Processing",
                    'description': 'Join Butler Specialty and 100+ manufacturers who transformed their sales',
                    'cta': 'Download Guide'
                },
                {
                    'type': 'conversation_ad',
                    'intro_message': f"Hi! I noticed {company_name} still uses manual order processing. Interested in seeing how similar companies save 3 hours daily?",
                    'cta_options': [
                        {'text': 'Yes, show me how', 'next': 'case_study'},
                        {'text': 'What about trade shows?', 'next': 'trade_show_info'},
                        {'text': 'Not interested', 'next': 'close'}
                    ],
                    'conversation_flows': {
                        'case_study': "Butler Specialty eliminated all order errors and saved 3 hours daily per rep. Here's their story: [Link]",
                        'trade_show_info': f"With {evidence.get('trade_show_data', {}).get('days_until_show', 35)} days until your next show, you need mobile capability. We can set you up in 14 days.",
                        'close': "No problem! Feel free to reach out if priorities change."
                    }
                },
                {
                    'type': 'document_ad',
                    'document_title': f"{company_name} Sales Transformation Guide",
                    'document_description': 'How to eliminate manual processing and save 3 hours daily',
                    'intro_text': f"Created specifically for {company_name} based on your current challenges"
                }
            ],
            'targeting': {
                'account_targeting': [
                    {'company_name': company_name, 'priority': 'high'},
                    {'company_names': self._get_competitor_names(analysis), 'priority': 'medium'}
                ],
                'job_functions': ['Sales', 'Information Technology', 'Operations'],
                'seniority': ['Director', 'VP', 'CXO', 'Owner'],
                'company_size': '50-500',
                'industries': ['Furniture Manufacturing', 'Wholesale', 'Manufacturing'],
                'member_traits': {
                    'groups': ['Furniture Industry Professionals', 'B2B Sales Leaders'],
                    'skills': ['Sales Management', 'ERP', 'Supply Chain']
                }
            },
            'budget': {
                'daily': 75,
                'total': 2250,
                'bid_type': 'automated',
                'optimization_goal': 'lead_generation'
            },
            'lead_gen_form': {
                'headline': f"Get {company_name}'s Custom ROI Analysis",
                'description': 'See exactly how much you could save',
                'fields': [
                    'first_name',
                    'last_name',
                    'email',
                    'company',
                    'job_title',
                    'phone'
                ],
                'custom_questions': [
                    {
                        'question': 'How many sales reps do you have?',
                        'type': 'multiple_choice',
                        'options': ['1-5', '6-10', '11-20', '20+']
                    },
                    {
                        'question': 'Which trade shows do you attend?',
                        'type': 'multiple_choice',
                        'options': ['Vegas Market', 'High Point', 'NeoCon', 'Other']
                    }
                ],
                'privacy_policy_url': 'https://supercatsolutions.com/privacy',
                'thank_you_message': "Thanks! We'll send your custom ROI analysis within 24 hours."
            }
        }
    
    def _generate_display_ads_pvp(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate display/banner ads for retargeting
        """
        
        company_name = analysis['company_name']
        
        banner_messages = []
        
        if evidence.get('trade_show_data'):
            days = evidence['trade_show_data'].get('days_until_show', 35)
            banner_messages.append({
                'headline': f"{company_name}: {days} Days Until {evidence['trade_show_data']['show_name']}",
                'subtext': "Get Mobile-Ready Now",
                'cta': 'Start Free Trial'
            })
        
        if evidence.get('website_findings'):
            for finding in evidence['website_findings'][:2]:
                if 'PDF' in finding:
                    banner_messages.append({
                        'headline': f"{company_name}: Ditch The PDFs",
                        'subtext': "Go Digital in 14 Days",
                        'cta': 'Learn How'
                    })
                elif 'manual' in finding.lower():
                    banner_messages.append({
                        'headline': "Stop Wasting 3 Hours Daily",
                        'subtext': f"{company_name} Could Save ${self._calculate_simple_roi(analysis)['annual_savings']:,}",
                        'cta': 'Calculate Savings'
                    })
        
        return {
            'platform': 'display_network',
            'campaign_type': 'remarketing',
            'ad_sizes': [
                {
                    'size': '728x90',
                    'name': 'leaderboard',
                    'message': banner_messages[0] if banner_messages else {
                        'headline': f"{company_name}: Transform Your Sales",
                        'subtext': "Mobile Order Management",
                        'cta': 'Learn More'
                    }
                },
                {
                    'size': '300x250',
                    'name': 'medium_rectangle',
                    'message': banner_messages[1] if len(banner_messages) > 1 else banner_messages[0]
                },
                {
                    'size': '336x280',
                    'name': 'large_rectangle',
                    'message': banner_messages[0]
                },
                {
                    'size': '300x600',
                    'name': 'half_page',
                    'message': self._create_vertical_banner(analysis, evidence)
                },
                {
                    'size': '320x50',
                    'name': 'mobile_banner',
                    'message': {
                        'headline': f"{company_name}: Mobile Sales",
                        'cta': 'Start Now'
                    }
                }
            ],
            'targeting': {
                'remarketing_lists': [
                    f"{company_name}_website_visitors",
                    f"{company_name}_email_opens",
                    'competitor_visitors'
                ],
                'frequency_cap': {
                    'impressions': 5,
                    'time_period': 'day'
                },
                'placements': {
                    'websites': ['industry_publications', 'trade_publications'],
                    'exclude': ['competitor_sites', 'negative_content']
                }
            },
            'creative_rotation': {
                'method': 'optimize',
                'test_variants': 3
            }
        }
    
    def _generate_retargeting_ads(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate retargeting sequences based on behavior
        """
        
        company_name = analysis['company_name']
        
        return {
            'platform': 'multi_platform_retargeting',
            'sequences': [
                {
                    'trigger': 'visited_pricing_page',
                    'sequence': [
                        {
                            'day': 0,
                            'message': f"{company_name}: See Your Custom Pricing",
                            'platform': 'display'
                        },
                        {
                            'day': 2,
                            'message': f"ROI Calculator Ready for {company_name}",
                            'platform': 'facebook'
                        },
                        {
                            'day': 5,
                            'message': "Last Chance: 20% Off First Year",
                            'platform': 'google'
                        }
                    ]
                },
                {
                    'trigger': 'downloaded_guide',
                    'sequence': [
                        {
                            'day': 1,
                            'message': "Ready to See a Demo?",
                            'platform': 'email'
                        },
                        {
                            'day': 3,
                            'message': f"{company_name}: Your Questions Answered",
                            'platform': 'linkedin'
                        },
                        {
                            'day': 7,
                            'message': "Schedule Your Custom Demo",
                            'platform': 'display'
                        }
                    ]
                },
                {
                    'trigger': 'abandoned_demo_form',
                    'sequence': [
                        {
                            'day': 0,
                            'message': "Still There? Let's Chat",
                            'platform': 'chat_widget'
                        },
                        {
                            'day': 1,
                            'message': f"{company_name}: Quick Question?",
                            'platform': 'email'
                        },
                        {
                            'day': 3,
                            'message': "15-Minute Demo Available",
                            'platform': 'calendar_popup'
                        }
                    ]
                }
            ],
            'dynamic_creative': {
                'use_ai_optimization': True,
                'test_elements': ['headline', 'image', 'cta'],
                'learning_period': 7
            }
        }
    
    def _generate_video_script(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate video ad script with specific pain points
        """
        
        company_name = analysis['company_name']
        
        script = {
            'duration': '30_seconds',
            'scenes': [
                {
                    'time': '0-3s',
                    'visual': f"Text overlay: '{company_name}'",
                    'voiceover': f"{company_name}...",
                    'text_overlay': company_name
                },
                {
                    'time': '3-8s',
                    'visual': 'Sales rep struggling with paper forms at trade show',
                    'voiceover': f"Still losing orders to manual processing?",
                    'text_overlay': evidence['website_findings'][0] if evidence.get('website_findings') else "Manual Order Chaos"
                },
                {
                    'time': '8-15s',
                    'visual': 'Split screen: Paper chaos vs. Digital ease',
                    'voiceover': "Your competitors are 40% faster with digital tools",
                    'text_overlay': "40% Faster Sales Cycles"
                },
                {
                    'time': '15-22s',
                    'visual': 'Happy sales rep using tablet',
                    'voiceover': "Join Butler Specialty and 100+ manufacturers",
                    'text_overlay': "'Best thing in 25 years' - Joel, Godinger"
                },
                {
                    'time': '22-28s',
                    'visual': 'ROI numbers animating',
                    'voiceover': f"Save ${self._calculate_simple_roi(analysis)['annual_savings']:,} annually",
                    'text_overlay': f"ROI in {self._calculate_simple_roi(analysis)['payback_days']} Days"
                },
                {
                    'time': '28-30s',
                    'visual': 'Logo and CTA',
                    'voiceover': "Transform your sales now",
                    'text_overlay': "Get Demo → supercatsolutions.com"
                }
            ],
            'music': 'upbeat_corporate',
            'style': 'professional_b2b',
            'cta_overlay': {
                'start': 25,
                'text': 'Get Your Demo',
                'url': f'https://supercatsolutions.com/demo?company={company_name}'
            }
        }
        
        return script
    
    def _generate_specific_keywords(self, analysis: Dict, evidence: Dict) -> List[str]:
        """
        Generate specific keywords based on evidence
        """
        
        keywords = [
            f'"{analysis["company_name"]}"',
            f'{analysis["company_name"]} sales software',
            f'{analysis["company_name"]} order management'
        ]
        
        # Add pain-specific keywords
        if 'PDF' in str(evidence.get('website_findings', [])):
            keywords.extend([
                'replace pdf catalog',
                'digital catalog software',
                'pdf to digital catalog'
            ])
        
        if 'manual' in str(evidence.get('website_findings', [])):
            keywords.extend([
                'manual order processing',
                'automate sales orders',
                'digital order forms'
            ])
        
        if evidence.get('trade_show_data'):
            keywords.extend([
                f'{evidence["trade_show_data"]["show_name"]} order app',
                'trade show order management',
                'offline order app'
            ])
        
        # Add competitor keywords
        keywords.extend([
            'supercat alternatives',
            'ecat software',
            'b2b order management'
        ])
        
        return keywords
    
    def _calculate_simple_roi(self, analysis: Dict) -> Dict:
        """
        Quick ROI calculation for ad copy
        """
        
        employees = analysis.get('employee_count', 50)
        reps = max(5, employees // 10)  # Estimate reps
        
        annual_savings = reps * 3 * 100 * 250  # reps * hours * rate * days
        investment = 15000 * (reps // 5)  # Scale by company
        payback_days = int((investment / annual_savings) * 365)
        
        return {
            'annual_savings': annual_savings,
            'investment': investment,
            'payback_days': payback_days
        }
    
    def _get_company_location(self, analysis: Dict) -> str:
        """
        Get company location for targeting
        """
        # This would look up actual location
        # For now, return general area
        return "United States"
    
    def _get_competitor_names(self, analysis: Dict) -> List[str]:
        """
        Get competitor names for targeting
        """
        # This would do competitive research
        return [
            'Universal Furniture',
            'Hooker Furniture',
            'Butler Specialty',
            'Lexington Home Brands'
        ]
    
    def _create_vertical_banner(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Create vertical banner message for half-page ad
        """
        
        return {
            'headline': f"{analysis['company_name']}:",
            'points': [
                "Save 3 Hours Daily",
                "Perfect Order Accuracy",
                "Works Offline",
                "ROI in 47 Days"
            ],
            'cta': 'Transform Your Sales'
        }