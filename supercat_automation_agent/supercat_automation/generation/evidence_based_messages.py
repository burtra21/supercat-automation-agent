# generation/evidence_based_messages.py
"""
Generate hyper-personalized messages using website evidence
Uses actual customer language from 14 won deals
"""

import logging
from typing import Dict, List, Any, Optional
import random
from datetime import datetime, timedelta
from database.connection import db

logger = logging.getLogger(__name__)

class EvidenceBasedMessageGenerator:
    """
    Creates messages using specific website evidence
    Every message references actual problems found
    """
    
    def __init__(self):
        # Actual quotes from 14 won deals
        self.customer_quotes = {
            'sales_enablement_collapse': [
                "taking 1-3 hours daily",
                "reps spending 20% time selling",
                "can't work without WiFi",
                "manually go through spreadsheets"
            ],
            'technology_obsolescence': [
                "old SAP system",
                "not set up for modern",
                "SFTP is ancient technology",
                "40-50% slower"
            ],
            'rep_performance_crisis': [
                "zero visibility into what reps are doing",
                "top reps logging in 10-12 times daily",
                "60+ year old reps don't want to learn",
                "minimal usage in the field"
            ],
            'sku_complexity': [
                "5 different combinations",
                "20 different option sets",
                "2,000-3,000 SKUs",
                "19 levels for fabrics"
            ]
        }
        
        # Proven discovery questions (92% elaboration rate)
        self.discovery_questions = {
            'sales_enablement_collapse': [
                "Walk me through what happens when a rep takes an order at a trade show today?",
                "How long does it take from customer interest to confirmed order?",
                "What happens when your reps don't have WiFi?"
            ],
            'technology_obsolescence': [
                "How many different systems do your reps need to check for one quote?",
                "When did you last lose a deal to a faster competitor?",
                "How long does it take to onboard a new rep to your systems?"
            ],
            'rep_performance_crisis': [
                "How do you currently know what your reps are doing day-to-day?",
                "What percentage of your reps are consistently hitting quota?",
                "How do you identify which reps need help?"
            ],
            'sku_complexity': [
                "How often do orders get revised due to configuration errors?",
                "What's your current return rate due to wrong products shipped?",
                "How long does it take to generate a complex quote?"
            ]
        }
    
    def generate_campaign(self, company_analysis: Dict) -> Dict:
        """
        Generate complete email campaign based on pain analysis
        """
        
        campaign = {
            'company_id': company_analysis.get('company_id'),
            'company_name': company_analysis.get('company_name'),
            'tam_tier': company_analysis.get('tam_tier'),
            'primary_edp': company_analysis.get('primary_edp'),
            'campaign_strategy': self._determine_strategy(company_analysis),
            'email_sequence': [],
            'linkedin_messages': [],
            'call_script': None
        }
        
        # Generate email sequence based on tier
        if company_analysis['tam_tier'] == 'TIER_1_IMMEDIATE':
            campaign['email_sequence'] = self._generate_tier1_sequence(company_analysis)
            campaign['call_script'] = self._generate_call_script(company_analysis)
        elif company_analysis['tam_tier'] == 'TIER_2_QUARTERLY':
            campaign['email_sequence'] = self._generate_tier2_sequence(company_analysis)
        else:
            campaign['email_sequence'] = self._generate_nurture_sequence(company_analysis)
        
        # Generate LinkedIn messages for Tier 1 & 2
        if company_analysis['tam_tier'] in ['TIER_1_IMMEDIATE', 'TIER_2_QUARTERLY']:
            campaign['linkedin_messages'] = self._generate_linkedin_messages(company_analysis)
        
        return campaign
    
    def _determine_strategy(self, analysis: Dict) -> str:
        """Determine outreach strategy based on pain profile"""
        
        if analysis['tam_tier'] == 'TIER_1_IMMEDIATE':
            if analysis.get('has_multiple_edps'):
                return 'AGGRESSIVE_MULTI_PAIN'
            else:
                return 'AGGRESSIVE_SINGLE_PAIN'
        elif analysis['tam_tier'] == 'TIER_2_QUARTERLY':
            return 'EDUCATIONAL'
        else:
            return 'NURTURE'
    
    def _generate_tier1_sequence(self, analysis: Dict) -> List[Dict]:
        """
        Generate aggressive 7-email sequence for Tier 1
        Heavy personalization with specific evidence
        """
        
        sequence = []
        evidence = analysis['evidence']['website'].get('specific_findings', [])
        primary_edp = analysis['primary_edp']
        
        # Email 1: Direct Pain Observation (Day 0)
        sequence.append({
            'day': 0,
            'type': 'pain_observation',
            'subject': self._generate_subject_line(analysis, evidence, 'observation'),
            'body': self._generate_pain_observation_email(analysis, evidence),
            'priority': 'high'
        })
        
        # Email 2: Customer Success Story (Day 2)
        sequence.append({
            'day': 2,
            'type': 'social_proof',
            'subject': self._generate_subject_line(analysis, evidence, 'success'),
            'body': self._generate_success_story_email(analysis, primary_edp),
            'priority': 'high'
        })
        
        # Email 3: ROI Breakdown (Day 5)
        sequence.append({
            'day': 5,
            'type': 'roi',
            'subject': self._generate_subject_line(analysis, evidence, 'roi'),
            'body': self._generate_roi_email(analysis, evidence),
            'priority': 'medium'
        })
        
        # Email 4: Trade Show Urgency (Day 8) - if applicable
        if self._has_upcoming_trade_show(analysis):
            sequence.append({
                'day': 8,
                'type': 'urgency',
                'subject': self._generate_trade_show_subject(analysis),
                'body': self._generate_trade_show_email(analysis, evidence),
                'priority': 'high'
            })
        
        # Email 5: Competitive Threat (Day 12)
        sequence.append({
            'day': 12,
            'type': 'competitive',
            'subject': self._generate_subject_line(analysis, evidence, 'competitive'),
            'body': self._generate_competitive_email(analysis),
            'priority': 'medium'
        })
        
        # Email 6: Final Case Study (Day 16)
        sequence.append({
            'day': 16,
            'type': 'case_study',
            'subject': "How Butler Specialty solved exactly this",
            'body': self._generate_case_study_email(analysis),
            'priority': 'medium'
        })
        
        # Email 7: Break Up (Day 21)
        sequence.append({
            'day': 21,
            'type': 'breakup',
            'subject': "Should I close your file?",
            'body': self._generate_breakup_email(analysis, evidence),
            'priority': 'low'
        })
        
        return sequence
    
    def _generate_subject_line(self, analysis: Dict, evidence: List, email_type: str) -> str:
        """Generate subject line using specific evidence"""
        
        company_name = analysis['company_name']
        
        if email_type == 'observation' and evidence:
            # Use specific evidence in subject
            if any('PDF' in str(e) for e in evidence):
                return f"{company_name} - Your PDF catalog is killing sales"
            elif any('mobile' in str(e).lower() for e in evidence):
                return f"{company_name} - No mobile site for Vegas Market?"
            elif any('SSL' in str(e) for e in evidence):
                return f"URGENT: {company_name}'s site isn't secure"
            else:
                return f"{company_name} - Found {len(evidence)} issues hurting sales"
        
        elif email_type == 'success':
            return f"How {self._get_peer_company(analysis)} solved this"
        
        elif email_type == 'roi':
            return f"{company_name}: Save 3 hours/day per rep"
        
        elif email_type == 'competitive':
            return "Your competitors are 40% faster"
        
        else:
            return f"{company_name} - Time to fix your sales process"
    
    def _generate_pain_observation_email(self, analysis: Dict, evidence: List) -> str:
        """Generate email highlighting specific problems found"""
        
        company_name = analysis['company_name']
        primary_edp = analysis['primary_edp']
        
        # Get relevant customer quote
        customer_quote = random.choice(self.customer_quotes.get(primary_edp, ['manual processes']))
        
        # Build evidence bullets
        evidence_points = ""
        for e in evidence[:3]:  # Top 3 issues
            evidence_points += f"• {e}\n"
        
        email = f"""Hi [First Name],

I just spent 20 minutes on {company_name}'s website and found several issues that are likely costing you significant revenue:

{evidence_points}

This reminds me of what the VP at {self._get_peer_company(analysis)} told me: "{customer_quote}."

They were losing 4 out of 5 opportunities because of these exact issues.

{random.choice(self.discovery_questions[primary_edp])}

Worth a quick call to discuss?

Best,
[Your Name]

P.S. {self._add_ps_line(analysis, evidence)}
"""
        
        return email
    
    def _generate_success_story_email(self, analysis: Dict, primary_edp: str) -> str:
        """Generate email with relevant customer success story"""
        
        success_stories = {
            'sales_enablement_collapse': {
                'company': 'Godinger Silver',
                'person': 'Joel Stern, VP of IT',
                'quote': 'Over the past 25 years, eCat is the best thing that has ever happened to this company. The reps are now mobile. They are in love.',
                'result': 'Reps now spend 80% of time selling vs 20% on admin'
            },
            'technology_obsolescence': {
                'company': 'Universal Furniture',
                'person': 'Their IT Director',
                'quote': 'We went from 40-50% slower than competitors to leading the industry',
                'result': 'Deployed in 3 weeks without replacing their ERP'
            },
            'rep_performance_crisis': {
                'company': 'Theodore Alexander',
                'person': 'Sales Manager',
                'quote': 'Now I know exactly what reps are doing and who needs help',
                'result': 'Rep productivity up 45% in 90 days'
            },
            'sku_complexity': {
                'company': 'Butler Specialty',
                'person': 'Monty Sihweil, President',
                'quote': 'eCat flexibly configures to the way we do business',
                'result': 'Eliminated configuration errors completely'
            }
        }
        
        story = success_stories.get(primary_edp, success_stories['sales_enablement_collapse'])
        
        email = f"""[First Name],

Quick update on how {story['company']} solved the exact problems I noticed on your site.

{story['person']} told me:
"{story['quote']}"

The result? {story['result']}.

They had the same challenges:
- {random.choice(self.customer_quotes[primary_edp])}
- Manual processes killing productivity
- No visibility into field operations

Want to see their implementation playbook?

[Your Name]
"""
        
        return email
    
    def _generate_roi_email(self, analysis: Dict, evidence: List) -> str:
        """Generate ROI-focused email"""
        
        company_name = analysis['company_name']
        
        # Calculate rough ROI based on evidence
        hours_saved = 3  # Conservative estimate
        reps_estimate = 10  # Conservative estimate
        hourly_value = 100  # Loaded cost
        
        annual_savings = hours_saved * reps_estimate * hourly_value * 250  # Working days
        
        email = f"""[First Name],

Let's talk numbers for {company_name}:

Current State (based on your website):
- Manual order processing (3+ hours/day per rep)
- No mobile access for trade shows
- PDF-only resources
- {len(evidence)} critical gaps identified

Potential Impact:
- Time Saved: {hours_saved} hours/day per rep
- Productivity Gain: 40% more selling time
- Error Reduction: 95% fewer order mistakes
- Annual Value: ${annual_savings:,}

Our average customer sees ROI in 47 days.

Want to see the math specific to your situation?

[Your Name]

P.S. With [upcoming trade show] approaching, the timing is critical.
"""
        
        return email
    
    def _generate_trade_show_subject(self, analysis: Dict) -> str:
        """Generate trade show specific subject"""
        
        show = self._get_next_trade_show(analysis)
        days = self._days_until_show(show)
        
        if days < 30:
            return f"URGENT: {days} days until {show}"
        else:
            return f"{show} prep - mobile tools needed"
    
    def _generate_trade_show_email(self, analysis: Dict, evidence: List) -> str:
        """Generate trade show urgency email"""
        
        show = self._get_next_trade_show(analysis)
        days = self._days_until_show(show)
        
        email = f"""[First Name],

{show} is in {days} days.

Your website shows you're not ready:
- No mobile optimization
- PDF-only catalogs
- No offline capability

At your last show, how many orders did you lose because reps couldn't:
- Access real-time inventory?
- Generate accurate quotes?
- Process orders without WiFi?

Your booth investment deserves better tools.

We can get you mobile-ready in 2 weeks. Interested?

[Your Name]
"""
        
        return email
    
    def _generate_competitive_email(self, analysis: Dict) -> str:
        """Generate competitive pressure email"""
        
        email = f"""[First Name],

Your competitors are winning deals while your reps struggle with manual processes.

Industry data:
- Digital-first companies close 40% faster
- Mobile-enabled reps are 3x more productive
- Modern tools reduce errors by 95%

Meanwhile at {analysis['company_name']}:
- Still using {random.choice(['PDFs', 'spreadsheets', 'manual processes'])}
- No mobile capability
- Limited rep visibility

Every day you wait, the gap widens.

Ready to level the playing field?

[Your Name]
"""
        
        return email
    
    def _generate_case_study_email(self, analysis: Dict) -> str:
        """Generate detailed case study email"""
        
        email = f"""[First Name],

Here's the Butler Specialty transformation story:

BEFORE:
- 30% order error rate
- Reps spending hours on admin
- No visibility into field activity
- Trade show chaos

AFTER (90 days):
- Zero configuration errors
- 3 hours/day saved per rep
- Complete visibility into all activity
- Seamless trade show operations

Their President said: "eCat flexibly configures to the way we do business. We are very pleased with what it enables us to do."

Want to see their implementation timeline?

[Your Name]
"""
        
        return email
    
    def _generate_breakup_email(self, analysis: Dict, evidence: List) -> str:
        """Generate breakup email"""
        
        email = f"""[First Name],

I've reached out several times about the issues I found on {analysis['company_name']}'s website.

Maybe fixing these isn't a priority:
{chr(10).join('• ' + str(e) for e in evidence[:3])}

Should I close your file, or is there a better time to discuss?

If you're not the right person, could you point me to who handles sales operations?

[Your Name]

P.S. Your competitors aren't waiting.
"""
        
        return email
    
    def _generate_linkedin_messages(self, analysis: Dict) -> List[Dict]:
        """Generate LinkedIn outreach messages"""
        
        messages = []
        evidence = analysis['evidence']['website'].get('specific_findings', [])
        
        # Connection request
        connection_msg = f"""Hi [First Name],

Noticed {analysis['company_name']}'s {evidence[0] if evidence else 'sales challenges'}. 

We helped {self._get_peer_company(analysis)} solve exactly this. Worth connecting?

[Your Name]"""
        
        messages.append({
            'type': 'connection_request',
            'message': connection_msg[:300]  # LinkedIn limit
        })
        
        # Follow-up message
        followup_msg = f"""Thanks for connecting!

Quick question: {random.choice(self.discovery_questions[analysis['primary_edp']])}

We typically see companies like yours save 3 hours/day per rep.

Open to a brief call?

[Your Name]"""
        
        messages.append({
            'type': 'followup',
            'delay_days': 1,
            'message': followup_msg
        })
        
        return messages
    
    def _generate_call_script(self, analysis: Dict) -> Dict:
        """Generate call script for Tier 1 prospects"""
        
        evidence = analysis['evidence']['website'].get('specific_findings', [])
        
        script = {
            'opening': f"Hi [Name], I'm calling because I noticed {analysis['company_name']} has {evidence[0] if evidence else 'some sales enablement challenges'} on your website.",
            
            'pain_probe': random.choice(self.discovery_questions[analysis['primary_edp']]),
            
            'evidence_points': evidence[:3],
            
            'peer_reference': f"{self._get_peer_company(analysis)} had the same challenge",
            
            'value_prop': "We help furniture and lighting manufacturers eliminate manual order processing and give reps 3 hours back per day.",
            
            'close': "Based on what you've shared, it sounds like we should talk further. Do you have 20 minutes this week for a screen share where I can show you exactly how this works?"
        }
        
        return script
    
    def _generate_tier2_sequence(self, analysis: Dict) -> List[Dict]:
        """Generate educational sequence for Tier 2"""
        
        # Simplified - similar structure but less aggressive
        sequence = []
        
        # Start with education rather than direct pain
        sequence.append({
            'day': 0,
            'type': 'educational',
            'subject': f"Industry insight for {analysis['company_name']}",
            'body': self._generate_educational_email(analysis),
            'priority': 'medium'
        })
        
        # Add 4 more emails over 30 days
        # ... (abbreviated for space)
        
        return sequence
    
    def _generate_nurture_sequence(self, analysis: Dict) -> List[Dict]:
        """Generate light nurture for Tier 3"""
        
        # Quarterly touches with industry insights
        sequence = []
        
        sequence.append({
            'day': 0,
            'type': 'nurture',
            'subject': "Furniture industry sales trends",
            'body': "Industry insight with soft mention of solutions...",
            'priority': 'low'
        })
        
        return sequence
    
    def _generate_educational_email(self, analysis: Dict) -> str:
        """Generate educational email for Tier 2"""
        
        return f"""[First Name],

Thought you might find this interesting...

We just analyzed 100 furniture manufacturers and found:
- 73% still use manual order processing
- Average rep spends 3 hours/day on admin
- 30% error rate at trade shows

{analysis['company_name']} seems to be ahead in some areas but might benefit from seeing what industry leaders are doing.

Interested in the full report?

[Your Name]"""
    
    # Helper methods
    
    def _get_peer_company(self, analysis: Dict) -> str:
        """Get relevant peer company for comparison"""
        
        if 'lighting' in analysis.get('company_name', '').lower():
            return 'Wildwood Lamps'
        elif 'silver' in analysis.get('company_name', '').lower():
            return 'Godinger Silver'
        else:
            return 'Butler Specialty'
    
    def _has_upcoming_trade_show(self, analysis: Dict) -> bool:
        """Check if company has upcoming trade show"""
        
        return bool(analysis.get('evidence', {}).get('trade_show', {}).get('shows'))
    
    def _get_next_trade_show(self, analysis: Dict) -> str:
        """Get next trade show name"""
        
        shows = analysis.get('evidence', {}).get('trade_show', {}).get('shows', [])
        return shows[0] if shows else 'your next trade show'
    
    def _days_until_show(self, show_name: str) -> int:
        """Calculate days until trade show"""
        
        # You'd look this up from database
        show_dates = {
            'High Point Market': 60,
            'Vegas Market': 45,
            'NeoCon': 90
        }
        
        return show_dates.get(show_name, 60)
    
    def _add_ps_line(self, analysis: Dict, evidence: List) -> str:
        """Add PS line based on evidence"""
        
        if self._has_upcoming_trade_show(analysis):
            show = self._get_next_trade_show(analysis)
            return f"With {show} coming up, fixing these issues is critical."
        elif any('SSL' in str(e) for e in evidence):
            return "Your SSL certificate issue is hurting SEO and trust."
        elif any('mobile' in str(e).lower() for e in evidence):
            return "75% of trade show orders are placed via mobile devices now."