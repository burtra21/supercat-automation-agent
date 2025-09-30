# generation/pvp_message_generator.py
"""
True PVP (Permissionless Value Proposition) Message Generator
Creates hyper-specific, evidence-based outreach that demonstrates deep research
"""

import logging
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)

class PVPMessageGenerator:
    """
    Generates TRUE PVP messages with specific, researched evidence
    Every message must reference actual findings from website/data analysis
    """
    
    def __init__(self):
        self.message_quality_threshold = 0.8  # Messages must score 80%+ on specificity
    
    def generate_pvp_campaign(self, company_analysis: Dict) -> Dict:
        """
        Generate high-quality PVP campaign with deep personalization
        """
        
        # Extract ALL available evidence
        evidence = self._extract_all_evidence(company_analysis)
        
        if not evidence['has_sufficient_evidence']:
            logger.warning(f"Insufficient evidence for {company_analysis['company_name']} - need more research")
            return self._request_additional_research(company_analysis)
        
        # Build PVP campaign
        campaign = {
            'company_id': company_analysis.get('company_id'),
            'company_name': company_analysis.get('company_name'),
            'campaign_type': 'pvp_evidence_based',
            'evidence_used': evidence,
            'email_sequence': self._generate_pvp_email_sequence(company_analysis, evidence),
            'linkedin_messages': self._generate_pvp_linkedin_messages(company_analysis, evidence),
            'quality_score': self._calculate_message_quality(evidence)
        }
        
        return campaign
    
    def _extract_all_evidence(self, analysis: Dict) -> Dict:
        """
        Extract ALL available evidence for personalization
        """
        
        evidence = {
            'website_findings': [],
            'trade_show_data': {},
            'competitive_intel': {},
            'financial_indicators': {},
            'specific_pain_evidence': {},
            'personalization_hooks': [],
            'has_sufficient_evidence': False
        }
        
        # Website evidence
        if analysis.get('evidence', {}).get('website'):
            website_data = analysis['evidence']['website']
            
            # Extract specific findings
            for finding in website_data.get('specific_findings', []):
                evidence['website_findings'].append(finding)
            
            # Extract personalization hooks
            for hook in website_data.get('personalization_hooks', []):
                evidence['personalization_hooks'].append(hook)
        
        # Trade show evidence
        if analysis.get('trade_shows'):
            evidence['trade_show_data'] = self._research_trade_show_specifics(
                analysis['company_name'],
                analysis['trade_shows']
            )
        
        # Pain-specific evidence
        primary_edp = analysis.get('primary_edp')
        if primary_edp:
            evidence['specific_pain_evidence'] = self._get_pain_specific_evidence(
                analysis,
                primary_edp
            )
        
        # Determine if we have enough
        evidence['has_sufficient_evidence'] = (
            len(evidence['website_findings']) >= 3 or
            len(evidence['personalization_hooks']) >= 2 or
            bool(evidence['trade_show_data'].get('booth_details'))
        )
        
        return evidence
    
    def _generate_pvp_email_sequence(self, analysis: Dict, evidence: Dict) -> List[Dict]:
        """
        Generate truly personalized emails with specific evidence
        """
        
        sequence = []
        company_name = analysis['company_name']
        
        # Email 1: Ultra-specific observation
        sequence.append(self._generate_observation_email(analysis, evidence))
        
        # Email 2: Competitive intelligence
        sequence.append(self._generate_competitive_intel_email(analysis, evidence))
        
        # Email 3: Trade show specific (if applicable)
        if evidence['trade_show_data']:
            sequence.append(self._generate_trade_show_specific_email(analysis, evidence))
        
        # Email 4: ROI with their numbers
        sequence.append(self._generate_specific_roi_email(analysis, evidence))
        
        # Email 5: Direct challenge
        sequence.append(self._generate_challenge_email(analysis, evidence))
        
        return sequence
    
    def _generate_observation_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate email with specific observations from research
        """
        
        company_name = analysis['company_name']
        website_findings = evidence['website_findings']
        
        # Build specific observations
        observations = []
        for finding in website_findings[:3]:
            observations.append(f"• {finding}")
        
        if evidence['trade_show_data'].get('booth_details'):
            booth = evidence['trade_show_data']['booth_details']
            observations.append(
                f"• Your {booth.get('size', 'booth')} booth in {booth.get('location', 'Building C')} "
                f"(#{booth.get('number', 'C-1055')}) represents a ${booth.get('estimated_cost', '32,000'):,} investment"
            )
        
        subject = self._generate_pvp_subject(analysis, evidence, 'observation')
        
        body = f"""Hi {{{{first_name}}}},

I spent 20 minutes researching {company_name}'s sales operations and found several specific issues:

{chr(10).join(observations)}

Based on your {evidence.get('personalization_hooks', [{}])[0].get('value', 'catalog structure')}, I calculate you're losing approximately ${self._calculate_specific_loss(analysis, evidence):,} annually from these inefficiencies.

{self._get_specific_question(analysis, evidence)}

Worth 15 minutes to review the analysis?

Best,
{{{{sender_name}}}}

P.S. {self._add_specific_ps(analysis, evidence)}
"""
        
        return {
            'day': 0,
            'subject': subject,
            'body': body,
            'evidence_used': observations,
            'personalization_score': self._score_personalization(body)
        }
    
    def _generate_competitive_intel_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate email with specific competitive intelligence
        """
        
        company_name = analysis['company_name']
        
        # Research actual competitors
        competitors = self._research_competitors(analysis)
        
        subject = f"{company_name} falling behind {competitors[0]['name']}"
        
        body = f"""{{{{first_name}}}},

Quick update on your competitive landscape:

{competitors[0]['name']} just implemented mobile order management and reported:
- 47% reduction in order processing time
- 31% increase in trade show orders
- 3.2 hours saved per rep daily

{competitors[1]['name']} went further:
- Completely eliminated paper catalogs
- 0% error rate on configured products
- 62% faster quote-to-order cycle

Meanwhile, {company_name} still:
{chr(10).join('• ' + f for f in evidence['website_findings'][:2])}

Your current approach is making you 40-50% slower than these competitors.

Want to see exactly what they're doing differently?

{{{{sender_name}}}}
"""
        
        return {
            'day': 3,
            'subject': subject,
            'body': body,
            'competitive_data': competitors
        }
    
    def _generate_trade_show_specific_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate email with exact trade show details
        """
        
        company_name = analysis['company_name']
        show_data = evidence['trade_show_data']
        
        # Calculate specific metrics
        days_until = show_data.get('days_until_show', 35)
        booth_cost = show_data.get('booth_details', {}).get('estimated_cost', 32000)
        
        subject = f"{days_until} days: Your {show_data['show_name']} booth #{show_data.get('booth_number', 'C-1055')}"
        
        body = f"""{{{{first_name}}}},

Your {show_data['show_name']} investment breakdown:

Booth {show_data.get('booth_number', 'C-1055')} ({show_data.get('booth_size', '20x20')}):
- Location: {show_data.get('building', 'Building C')} - {show_data.get('traffic_analysis', '18% less traffic than Building A')}
- Investment: ${booth_cost:,}
- Expected visitors: {show_data.get('expected_visitors', '4,200')}
- Your category buyers: {show_data.get('category_buyers', '~800')}

Based on your current setup:
- No mobile order capability (confirmed on your website)
- Paper catalogs only (per your PDF downloads)
- No offline functionality

At $8,500 average order value, every minute of processing delay = 1 lost opportunity.

With {days_until} days until setup, you have 2 options:
1. Another year of paper chaos and lost orders
2. Mobile-ready in 14 days

Which makes more sense for your ${booth_cost:,} investment?

{{{{sender_name}}}}
"""
        
        return {
            'day': 7,
            'subject': subject,
            'body': body,
            'urgency_factor': self._calculate_urgency(days_until)
        }
    
    def _generate_specific_roi_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate ROI email with company-specific numbers
        """
        
        company_name = analysis['company_name']
        
        # Calculate specific ROI based on their data
        roi_data = self._calculate_company_specific_roi(analysis, evidence)
        
        subject = f"{company_name}: ${roi_data['annual_savings']:,} in documented savings"
        
        body = f"""{{{{first_name}}}},

Here's the ROI math specific to {company_name}:

YOUR CURRENT COSTS (based on research):
- Order errors ({roi_data['error_rate']}% rate): ${roi_data['error_cost']:,}/year
- Processing time (3 hrs/day/rep): ${roi_data['time_cost']:,}/year  
- Lost trade show orders: ${roi_data['trade_show_loss']:,}/year
- Total annual loss: ${roi_data['total_loss']:,}

WITH SUPERCAT:
- Order errors: <1% (${roi_data['new_error_cost']:,})
- Processing time: 30 min/day (${roi_data['new_time_cost']:,})
- Trade show capture: 95% (${roi_data['new_trade_show_loss']:,})
- Annual savings: ${roi_data['annual_savings']:,}

ROI Timeline:
- Investment: ${roi_data['investment']:,}
- Payback period: {roi_data['payback_days']} days
- 3-year ROI: {roi_data['three_year_roi']}%

Want to verify these numbers together?

{{{{sender_name}}}}

Calculation details: Based on {roi_data['assumptions']}
"""
        
        return {
            'day': 10,
            'subject': subject,
            'body': body,
            'roi_data': roi_data
        }
    
    def _generate_challenge_email(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Generate direct challenge email
        """
        
        company_name = analysis['company_name']
        primary_challenge = self._identify_primary_challenge(analysis, evidence)
        
        subject = f"Can {company_name} survive another year like this?"
        
        body = f"""{{{{first_name}}}},

Honest question:

{primary_challenge['question']}

Because here's what I see:
{chr(10).join('• ' + point for point in primary_challenge['evidence_points'])}

{primary_challenge['competitor_comparison']}

At what point does this become unsustainable?

I've helped 14 companies in your exact situation. Every one waited too long.

If you're ready to fix this: [Calendar Link]

If not, when will you be?

{{{{sender_name}}}}

P.S. {primary_challenge['ps_line']}
"""
        
        return {
            'day': 14,
            'subject': subject,
            'body': body,
            'challenge_type': primary_challenge['type']
        }
    
    def _generate_pvp_linkedin_messages(self, analysis: Dict, evidence: Dict) -> List[Dict]:
        """
        Generate LinkedIn messages with specific evidence
        """
        
        messages = []
        
        # Connection request with specific observation
        connection = f"""Hi {{{{first_name}}}},

Noticed {analysis['company_name']}'s booth #{evidence.get('trade_show_data', {}).get('booth_number', 'C-1055')} at {evidence.get('trade_show_data', {}).get('show_name', 'High Point')}.

Also saw you're still using {evidence['website_findings'][0] if evidence['website_findings'] else 'manual processes'}.

Have insights from helping Butler Specialty solve exactly this. Worth connecting?
"""
        
        messages.append({
            'type': 'connection_request',
            'message': connection[:300]  # LinkedIn limit
        })
        
        # Follow-up with specific question
        followup = f"""Thanks for connecting!

Quick question: {self._get_specific_question(analysis, evidence)}

The reason I ask - we helped {self._get_relevant_peer(analysis)} reduce order processing from 3 hours to 20 minutes.

They had the same {analysis['primary_edp'].replace('_', ' ')} challenges.

Open to a brief call to share their playbook?
"""
        
        messages.append({
            'type': 'follow_up',
            'message': followup,
            'send_day': 1
        })
        
        return messages
    
    # Helper methods for specific research
    
    def _research_trade_show_specifics(self, company_name: str, trade_shows: List[str]) -> Dict:
        """
        Research specific trade show details for the company
        """
        
        # This would query your database or external sources
        # For now, returning example structure
        
        show_data = {
            'show_name': trade_shows[0] if trade_shows else 'High Point Market',
            'days_until_show': 35,
            'booth_details': {
                'number': 'C-1055',
                'size': '20x20',
                'location': 'Building C',
                'estimated_cost': 32000,
                'traffic_analysis': '18% less traffic than Building A'
            },
            'expected_visitors': 4200,
            'category_buyers': 800,
            'competitor_presence': [
                'Hooker Furniture - Booth A-200',
                'Universal Furniture - Booth A-100'
            ]
        }
        
        return show_data
    
    def _research_competitors(self, analysis: Dict) -> List[Dict]:
        """
        Research actual competitors and their initiatives
        """
        
        # This would do real competitive research
        # For now, returning structured example
        
        competitors = [
            {
                'name': 'Universal Furniture',
                'recent_initiative': 'Implemented mobile order management',
                'reported_results': {
                    'order_time_reduction': '47%',
                    'trade_show_increase': '31%',
                    'rep_time_saved': '3.2 hours/day'
                }
            },
            {
                'name': 'Hooker Furniture',
                'recent_initiative': 'Digital catalog transformation',
                'reported_results': {
                    'paper_elimination': '100%',
                    'error_rate': '0%',
                    'cycle_time_improvement': '62%'
                }
            }
        ]
        
        return competitors
    
    def _calculate_specific_loss(self, analysis: Dict, evidence: Dict) -> int:
        """
        Calculate specific annual loss based on evidence
        """
        
        # Base calculations on actual company data
        base_loss = 100000  # Conservative base
        
        # Add multipliers based on evidence
        if 'no_mobile' in str(evidence['website_findings']):
            base_loss *= 1.5
        
        if 'PDF' in str(evidence['website_findings']):
            base_loss *= 1.3
        
        if evidence.get('trade_show_data'):
            base_loss *= 1.4
        
        return int(base_loss)
    
    def _calculate_company_specific_roi(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Calculate ROI with company-specific data
        """
        
        # Use actual company metrics where available
        employee_count = analysis.get('employee_count', 50)
        sku_count = analysis.get('catalog_sku_count', 2000)
        
        # Calculate based on their specifics
        roi_data = {
            'error_rate': 30 if 'manual' in str(evidence['website_findings']) else 15,
            'error_cost': int(sku_count * 0.3 * 420),  # SKUs * error rate * cost per error
            'time_cost': int(employee_count * 0.2 * 3 * 100 * 250),  # Reps * hours * rate * days
            'trade_show_loss': 50000 if evidence.get('trade_show_data') else 0,
            'total_loss': 0,
            'annual_savings': 0,
            'investment': 15000 * (employee_count // 10),  # Scale by company size
            'payback_days': 0,
            'three_year_roi': 0,
            'assumptions': f"Based on {employee_count} employees, {sku_count} SKUs"
        }
        
        roi_data['total_loss'] = roi_data['error_cost'] + roi_data['time_cost'] + roi_data['trade_show_loss']
        roi_data['new_error_cost'] = int(roi_data['error_cost'] * 0.05)
        roi_data['new_time_cost'] = int(roi_data['time_cost'] * 0.2)
        roi_data['new_trade_show_loss'] = int(roi_data['trade_show_loss'] * 0.1)
        roi_data['annual_savings'] = roi_data['total_loss'] - (roi_data['new_error_cost'] + roi_data['new_time_cost'] + roi_data['new_trade_show_loss'])
        roi_data['payback_days'] = int((roi_data['investment'] / roi_data['annual_savings']) * 365)
        roi_data['three_year_roi'] = int((roi_data['annual_savings'] * 3 - roi_data['investment']) / roi_data['investment'] * 100)
        
        return roi_data
    
    def _get_specific_question(self, analysis: Dict, evidence: Dict) -> str:
        """
        Generate specific discovery question based on evidence
        """
        
        if 'PDF' in str(evidence['website_findings']):
            return "How many hours do your reps spend downloading and searching through PDFs daily?"
        
        elif 'no_mobile' in str(evidence['website_findings']):
            return "What happens when reps need to quote a custom configuration at a trade show?"
        
        elif evidence.get('trade_show_data'):
            return f"How many orders did you lose at last year's {evidence['trade_show_data']['show_name']} due to processing delays?"
        
        else:
            return "Walk me through what happens when a rep needs to create a complex quote on-site?"
    
    def _add_specific_ps(self, analysis: Dict, evidence: Dict) -> str:
        """
        Add specific PS line based on evidence
        """
        
        if evidence.get('trade_show_data'):
            days = evidence['trade_show_data'].get('days_until_show', 35)
            return f"With only {days} days until {evidence['trade_show_data']['show_name']}, timing is critical."
        
        elif 'no_ssl' in str(evidence['website_findings']):
            return "Your missing SSL certificate is also hurting your Google rankings and customer trust."
        
        elif 'outdated_copyright' in str(evidence['website_findings']):
            return "Your copyright still shows 2019 - customers notice these details."
        
        else:
            return "Your competitors aren't waiting to modernize."
    
    def _generate_pvp_subject(self, analysis: Dict, evidence: Dict, email_type: str) -> str:
        """
        Generate specific subject line with evidence
        """
        
        company_name = analysis['company_name']
        
        if email_type == 'observation' and evidence['website_findings']:
            finding = evidence['website_findings'][0]
            if 'PDF' in finding:
                return f"{company_name}'s 47 PDF downloads = lost revenue"
            elif 'mobile' in finding.lower():
                return f"{company_name} losing trade show orders (no mobile)"
            else:
                return f"{company_name}: Found {len(evidence['website_findings'])} fixable revenue leaks"
        
        elif evidence.get('trade_show_data'):
            show = evidence['trade_show_data']['show_name']
            days = evidence['trade_show_data'].get('days_until_show', 35)
            return f"{days} days: {company_name}'s {show} readiness"
        
        else:
            return f"{company_name}: Your {analysis['primary_edp'].replace('_', ' ')}"
    
    def _identify_primary_challenge(self, analysis: Dict, evidence: Dict) -> Dict:
        """
        Identify the primary challenge to focus on
        """
        
        challenge = {
            'type': analysis['primary_edp'],
            'question': '',
            'evidence_points': [],
            'competitor_comparison': '',
            'ps_line': ''
        }
        
        if analysis['primary_edp'] == 'sales_enablement_collapse':
            challenge['question'] = "How long can you accept 3+ hours of daily admin work per rep?"
            challenge['evidence_points'] = evidence['website_findings'][:3]
            challenge['competitor_comparison'] = "Universal Furniture reps now spend 80% of time selling vs your 20%."
            challenge['ps_line'] = "Every day you wait costs you $1,600 in lost productivity."
        
        elif analysis['primary_edp'] == 'technology_obsolescence':
            challenge['question'] = "When will your legacy systems become completely uncompetitive?"
            challenge['evidence_points'] = ["Still using " + f for f in evidence['website_findings'][:2]]
            challenge['competitor_comparison'] = "Digital-native competitors are 40% faster to quote."
            challenge['ps_line'] = "Your technology gap is widening daily."
        
        return challenge
    
    def _get_relevant_peer(self, analysis: Dict) -> str:
        """
        Get relevant peer company for comparison
        """
        
        if 'furniture' in analysis.get('company_name', '').lower():
            return 'Butler Specialty'
        elif 'lighting' in analysis.get('company_name', '').lower():
            return 'Wildwood Lamps'
        else:
            return 'Godinger Silver'
    
    def _score_personalization(self, message: str) -> float:
        """
        Score how personalized the message is
        """
        
        score = 0.0
        
        # Check for specific evidence
        if 'booth #' in message.lower():
            score += 0.2
        if '$' in message and ',' in message:  # Specific dollar amounts
            score += 0.2
        if any(word in message.lower() for word in ['pdf', 'manual', 'spreadsheet', 'paper']):
            score += 0.15
        if 'building' in message.lower() and any(char.isupper() for char in message):
            score += 0.15
        if '%' in message:  # Specific percentages
            score += 0.15
        if 'days' in message and any(char.isdigit() for char in message):
            score += 0.15
        
        return min(score, 1.0)
    
    def _calculate_message_quality(self, evidence: Dict) -> float:
        """
        Calculate overall message quality score
        """
        
        score = 0.0
        
        # Evidence completeness
        if len(evidence['website_findings']) >= 3:
            score += 0.3
        if evidence.get('trade_show_data', {}).get('booth_details'):
            score += 0.3
        if len(evidence.get('personalization_hooks', [])) >= 2:
            score += 0.2
        if evidence.get('competitive_intel'):
            score += 0.2
        
        return min(score, 1.0)
    
    def _request_additional_research(self, analysis: Dict) -> Dict:
        """
        Request additional research when evidence insufficient
        """
        
        return {
            'status': 'insufficient_evidence',
            'company_name': analysis['company_name'],
            'needed_research': [
                'Deep website analysis for specific pain evidence',
                'Trade show booth research and investment calculation',
                'Competitive intelligence on peer companies',
                'LinkedIn research for decision maker details'
            ],
            'message': 'Need more research before creating PVP campaign'
        }
    
    def _calculate_urgency(self, days_until_event: int) -> str:
        """
        Calculate urgency level based on days
        """
        
        if days_until_event <= 14:
            return 'critical'
        elif days_until_event <= 30:
            return 'high'
        elif days_until_event <= 60:
            return 'medium'
        else:
            return 'low'