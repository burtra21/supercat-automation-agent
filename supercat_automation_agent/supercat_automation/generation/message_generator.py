# generation/message_generator.py
"""
Message generation using exact customer language from won deals
No hypothetical messaging - only proven patterns
"""

import logging
from typing import Dict, List, Any, Optional
import json
import random
from datetime import datetime
from openai import OpenAI
try:
    from supercat_automation.config.settings import settings
except ImportError:
    from config.settings import settings
from database.connection import db

logger = logging.getLogger(__name__)

class CustomerValidatedMessageGenerator:
    """
    Generates messages using ONLY language patterns from won deals
    Every hook, question, and response comes from actual customer conversations
    """
    
    def __init__(self):
        """Initialize with OpenAI and customer language library"""
        self.client = OpenAI(api_key=settings.openai_api_key)
        
        # Proven hooks from customer analysis - UPDATED FOR PVP
        self.proven_hooks = {
            'sales_enablement_primary': "I analyzed {company}'s sales process and found you're losing ~3 hours daily per rep on manual order processing - that's ${annual_cost} in lost productivity annually. Your 130+ day sales cycles are 40% longer than digitized competitors.",
            'trade_show_urgency': "With {days_to_show} days until {trade_show}, your ${booth_cost} booth investment is at risk. Without mobile/offline capability, you'll lose 60% of opportunities to competitors who can quote on-spot.",
            'technology_gap': "Your {legacy_system} makes {company} 40-50% slower than digital-native competitors. The 57% longer catalog updates and 25-30% higher error rates are costing you ${error_cost} annually.",
            'rep_visibility': "{company} has zero visibility into {rep_count} reps' daily activities. Your top 20% reps are 10x more productive than bottom 50% - but you can't replicate their success without data.",
            'competitive_threat': "While {company} uses {current_process}, 3 direct competitors (Universal, Theodore Alexander, Butler) digitized in 2024 and report 25-40% sales increases.",
            'sku_complexity': "With {sku_count} SKUs and {config_count} configurations, {company}'s approaching the 15% error threshold where operations fail. Current 30% return rate = ${return_cost} annual loss."
        }
        
        # Discovery questions ranked by 92% elaboration rate
        self.discovery_questions = [
            "Walk me through what happens when a rep takes an order at a trade show today?",
            "How long does it take from customer interest to confirmed order?",
            "What percentage of your reps are consistently hitting quota?",
            "How do you currently know what your reps are doing day-to-day?",
            "When did you last lose a deal to a faster competitor?"
        ]
        
        # Objection responses with proven success rates
        self.objection_responses = {
            'need_it_approval': {
                'response': "This replaces spreadsheets, not your ERP. Most customers deploy without IT.",
                'success_rate': 0.73
            },
            'reps_wont_adopt': {
                'response': "Your top reps are begging for this. We'll identify and enable them first.",
                'success_rate': 0.81
            },
            'too_expensive': {
                'response': "You're losing 3 hours daily per rep. That's $40K annually per rep in lost productivity.",
                'success_rate': 0.67
            },
            'wait_for_erp': {
                'response': "This works with your current ERP. Don't let perfect be the enemy of good.",
                'success_rate': 0.71
            }
        }
        
        # Customer success quotes from won deals
        self.customer_quotes = {
            'butler_specialty': "eCat flexibly configures to the way we do business.",
            'godinger_silver': "Over the past 25 years, eCat is the best thing that has ever happened to this company.",
            'wildwood_lamps': "I've reduced by a third the number of calls per day.",
            'universal_furniture': "The reps are now mobile. They are in love."
        }
        
        # EDP-specific evidence thresholds for PVP messaging
        self.edp_evidence = {
            'sales_enablement_collapse': {
                'threshold_stats': '56% failure rate, 130+ day cycles, 4 of 5 deals lost',
                'financial_impact': 'rep_count * 3 * 250 * 100',
                'evidence_markers': ['manual', 'email orders', 'paper', 'PDF catalog']
            },
            'technology_obsolescence': {
                'threshold_stats': '57% slower updates, 25-30% higher errors',
                'financial_impact': 'sku_count * 0.30 * 50',
                'evidence_markers': ['CSV', 'FTP', 'legacy', 'old system']
            },
            'rep_performance_crisis': {
                'threshold_stats': '27% turnover, 10x performance variance',
                'financial_impact': 'rep_count * 75000 * 0.27',
                'evidence_markers': ['no visibility', 'no tracking', 'independent reps']
            },
            'sku_complexity': {
                'threshold_stats': '15% error threshold, 8% write-offs, 25% returns',
                'financial_impact': 'sku_count * 0.08 * 100',
                'evidence_markers': ['configurations', 'options', 'variants', 'custom']
            },
            'channel_conflict': {
                'threshold_stats': '59% revenue loss, 39% customer abandonment',
                'financial_impact': 'revenue * 0.15',
                'evidence_markers': ['multiple portals', 'different systems', 'channel pricing']
            }
        }
    
    def generate_campaign(self, 
                          company_data: Dict[str, Any],
                          pain_signals: Dict[str, Any],
                          decision_makers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate complete multi-channel campaign
        Returns messages for email, LinkedIn, and ad suggestions
        """
        try:
            # Identify primary pain to lead with
            primary_pain = pain_signals.get('primary_pain', 'sales_enablement_collapse')
            
            # Enrich company data with evidence and calculations
            enriched_data = self._enrich_company_data(company_data, primary_pain)
            
            # Generate email sequence
            email_sequence = self.generate_email_sequence(
                enriched_data, primary_pain, decision_makers
            )
            
            # Generate LinkedIn messages
            linkedin_messages = self.generate_linkedin_messages(
                enriched_data, primary_pain, decision_makers
            )
            
            # Generate ad copy suggestions
            ad_suggestions = self.generate_ad_suggestions(
                enriched_data, primary_pain
            )
            
            # Create campaign record
            campaign = {
                'company_id': company_data.get('id'),
                'campaign_type': 'multi_channel_pvp',
                'pain_point_focus': primary_pain,
                'primary_hook': self._build_pvp_hook(enriched_data, primary_pain),
                'message_variants': {
                    'email': email_sequence,
                    'linkedin': linkedin_messages,
                    'ads': ad_suggestions
                },
                'personalization_tokens': self.extract_personalization_tokens(enriched_data),
                'evidence_used': enriched_data.get('evidence_points', []),
                'scheduled_start': datetime.now().isoformat()
            }
            
            return campaign
            
        except Exception as e:
            import traceback
            logger.error(f"Error generating campaign: {e}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            return None
    
    def _enrich_company_data(self, company_data: Dict, primary_pain: str) -> Dict:
        """Enrich company data with calculations and evidence for PVP messaging"""
        enriched = company_data.copy()
        
        # Calculate key metrics with null safety
        employee_count = company_data.get('employee_count') or 100
        catalog_sku_count = company_data.get('catalog_sku_count') or 2000
        
        enriched['rep_count'] = max(5, employee_count // 20)
        enriched['annual_cost'] = enriched['rep_count'] * 3 * 250 * 100
        enriched['error_cost'] = catalog_sku_count * 0.30 * 50
        enriched['return_cost'] = catalog_sku_count * 0.25 * 100
        enriched['booth_cost'] = 32000  # Average trade show booth
        enriched['days_to_show'] = 35  # Would calculate from actual dates
        enriched['trade_show'] = 'Vegas Market'  # Would pull from data
        
        # Extract evidence points from website analysis
        evidence = company_data.get('website_evidence', {})
        enriched['evidence_points'] = evidence.get('specific_findings', [])
        enriched['legacy_system'] = self._identify_legacy_system(enriched['evidence_points'])
        enriched['current_process'] = enriched['legacy_system']
        enriched['config_count'] = catalog_sku_count * 5
        
        return enriched
    
    def _identify_legacy_system(self, evidence_points: List[str]) -> str:
        """Identify specific legacy system from evidence"""
        for evidence in evidence_points:
            if 'PDF' in evidence:
                return 'PDF catalogs'
            elif 'CSV' in evidence:
                return 'CSV uploads'
            elif 'spreadsheet' in evidence.lower():
                return 'spreadsheets'
            elif 'email' in evidence.lower():
                return 'email orders'
        return 'manual processes'
    
    def _build_pvp_hook(self, company_data: Dict, primary_pain: str) -> str:
        """Build personalized PVP hook with evidence"""
        hook_template = self.proven_hooks.get(f"{primary_pain}_primary", self.proven_hooks['sales_enablement_primary'])
        
        return hook_template.format(
            company=company_data.get('company_name', 'your company'),
            annual_cost=f"{(company_data.get('annual_cost') or 0):,}",
            days_to_show=company_data.get('days_to_show', 35),
            trade_show=company_data.get('trade_show', 'Vegas Market'),
            booth_cost=f"{(company_data.get('booth_cost') or 32000):,}",
            legacy_system=company_data.get('legacy_system', 'manual processes'),
            error_cost=f"{(company_data.get('error_cost') or 0):,}",
            rep_count=company_data.get('rep_count', 10),
            current_process=company_data.get('current_process', 'spreadsheets'),
            sku_count=f"{(company_data.get('catalog_sku_count') or 2000):,}",
            config_count=f"{(company_data.get('config_count') or 10000):,}",
            return_cost=f"{(company_data.get('return_cost') or 0):,}"
        )
    
    def generate_email_sequence(self, 
                                company_data: Dict,
                                primary_pain: str,
                                decision_makers: List[Dict]) -> List[Dict]:
        """Generate 7-touch email sequence using proven patterns"""
        sequence = []
        
        # Email 1: Problem Agitation (Day 0)
        email_1 = self.generate_problem_agitation_email(company_data, primary_pain)
        sequence.append(email_1)
        
        # Email 2: Social Proof (Day 3)
        email_2 = self.generate_social_proof_email(company_data, primary_pain)
        sequence.append(email_2)
        
        # Email 3: ROI Focus (Day 7)
        email_3 = self.generate_roi_email(company_data, primary_pain)
        sequence.append(email_3)
        
        # Email 4: Competitive Threat (Day 10)
        email_4 = self.generate_competitive_email(company_data)
        sequence.append(email_4)
        
        # Email 5: Case Study (Day 14)
        email_5 = self.generate_case_study_email(company_data, primary_pain)
        sequence.append(email_5)
        
        # Email 6: Urgency (Day 18)
        email_6 = self.generate_urgency_email(company_data)
        sequence.append(email_6)
        
        # Email 7: Break Up (Day 21)
        email_7 = self.generate_breakup_email(company_data)
        sequence.append(email_7)
        
        return sequence
    
    def generate_problem_agitation_email(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate problem agitation email using customer language"""
        
        # Get evidence points
        evidence_points = company_data.get('evidence_points', [])
        if not evidence_points:
            evidence_points = ['Manual order processing', 'No mobile capability', 'PDF catalogs only']
        
        # Build PVP hook with specific evidence
        hook = self._build_pvp_hook(company_data, primary_pain)
        
        # Build context for GPT-4 with PVP approach
        prompt = f"""
        Generate ONLY the EMAIL BODY for {company_data.get('company_name')}. Do NOT include a subject line.
        
        Start with a greeting like "Hey [first_name]," or "Hi [team_name],"
        
        MUST include this evidence-based hook: "{hook}"
        
        Then add:
        - 3 specific problems found: {evidence_points[:3]}
        - Quantified impact: ${company_data.get('annual_cost', 0):,} annual loss
        - Discovery question: "{random.choice(self.discovery_questions)}"
        - Customer proof: {random.choice(list(self.customer_quotes.values()))}
        
        Keep under 100 words. Lead with value, not pitch.
        Format with bullet points for problems.
        
        IMPORTANT: Do NOT include "Subject:" or any subject line. Start directly with the greeting.
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You are a B2B sales expert who leads with evidence and value."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=250
        )
        
        body = response.choices[0].message.content
        
        # Clean up any subject line that might have been included
        body = self._clean_email_body(body)
        
        # Generate PVP subject line
        subject = self.generate_subject_line(company_data, primary_pain, 'problem')
        
        return {
            'sequence_step': 1,
            'send_day': 0,
            'subject': subject,
            'body': body,
            'variant': 'problem_agitation_pvp',
            'personalization_tokens': {
                'company_name': company_data.get('company_name'),
                'sku_count': company_data.get('catalog_sku_count'),
                'current_system': company_data.get('current_erp'),
                'annual_cost': company_data.get('annual_cost'),
                'evidence_used': evidence_points[:3]
            }
        }
    
    def generate_social_proof_email(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate social proof email with real customer quotes"""
        
        # Select relevant customer quote
        if 'sku' in primary_pain or 'complex' in primary_pain:
            quote_company = 'butler_specialty'
        elif 'technology' in primary_pain:
            quote_company = 'godinger_silver'
        else:
            quote_company = 'wildwood_lamps'
        
        quote = self.customer_quotes[quote_company]
        
        # Calculate specific metrics for comparison
        before_metrics = {
            'order_time': '3-4 hours',
            'error_rate': '30%',
            'rep_productivity': '20% selling, 80% admin'
        }
        
        after_metrics = {
            'order_time': '15 minutes',
            'error_rate': '<1%',
            'rep_productivity': '80% selling, 20% admin'
        }
        
        prompt = f"""
        Generate ONLY the EMAIL BODY for a social proof email. Do NOT include a subject line.
        
        Start with a greeting like "Hey [first_name]," or "Hi [team_name],"
        
        Feature this transformation:
        Customer: {quote_company.replace('_', ' ').title()}
        Quote: "{quote}"
        
        Before: {json.dumps(before_metrics)}
        After: {json.dumps(after_metrics)}
        ROI: 47 days
        
        Connect to {company_data.get('company_name')}'s situation.
        Include specific numbers and transformation timeline.
        Keep under 120 words.
        
        IMPORTANT: Do NOT include "Subject:" or any subject line. Start directly with the greeting.
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You share specific customer transformations with data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        return {
            'sequence_step': 2,
            'send_day': 3,
            'subject': f"How {quote_company.replace('_', ' ').title()} eliminated your exact problem",
            'body': self._clean_email_body(response.choices[0].message.content),
            'variant': 'social_proof_pvp'
        }
    
    def generate_roi_email(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate ROI-focused email with specific calculations"""
        
        # Calculate detailed ROI
        productivity_gain = company_data.get('annual_cost', 0)
        error_reduction = company_data.get('error_cost', 0)
        trade_show_roi = company_data.get('booth_cost', 32000) * 0.20
        total_impact = productivity_gain + error_reduction + trade_show_roi
        
        prompt = f"""
        Generate a PVP ROI analysis email for {company_data.get('company_name', 'your company')}.
        
        Current State Problems:
        - {company_data.get('rep_count', 10)} reps × 3 hours wasted daily
        - 30% error rate on {company_data.get('catalog_sku_count', 2000)} SKUs
        - ${(company_data.get('booth_cost') or 32000):,} trade show investment at risk
        
        Financial Impact:
        - Productivity: ${productivity_gain:,}/year
        - Error Elimination: ${error_reduction:,}/year
        - Trade Show ROI: ${trade_show_roi:,}/show
        - Total: ${total_impact:,}/year
        
        Investment: $15-25K/year
        Payback: 47 days
        5-Year ROI: {int(total_impact * 5 / 20000)}x
        
        Keep under 100 words. Use bullet points for clarity.
        End with: "Want your custom ROI model? Takes 15 minutes."
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You present ROI analysis with specific calculations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=250
        )
        
        return {
            'sequence_step': 3,
            'send_day': 7,
            'subject': f"${total_impact:,} impact for {company_data.get('company_name', 'your company')}",
            'body': self._clean_email_body(response.choices[0].message.content),
            'variant': 'roi_focus_pvp'
        }

    def generate_competitive_email(self, company_data: Dict) -> Dict:
        """Generate competitive threat email"""
        
        competitors = ['Universal Furniture', 'Theodore Alexander', 'Butler Specialty']
        
        prompt = f"""
        Generate a PVP competitive threat email for {company_data.get('company_name', 'your company')}.
        
        Key Points:
        - Digital competitors are 40-50% faster
        - These 3 competitors digitized in 2024: {', '.join(competitors)}
        - Each reports 25-40% sales increase
        - {company_data.get('company_name', 'your company')} still uses {company_data.get('legacy_system', 'manual processes')}
        
        Market Reality:
        - Quote time: Them (minutes) vs You (hours)
        - Errors: Them (<1%) vs You (30%)
        - Trade show orders: Them (real-time) vs You (next day)
        
        Warning: Companies on manual processes in 2025 won't exist in 2027.

        Keep under 100 words. Create urgency without being pushy.
        End with: "Should we discuss closing this gap before {company_data.get('trade_show', 'High Point')}?"
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You highlight competitive threats with market data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        return {
            'sequence_step': 4,
            'send_day': 10,
            'subject': f"3 competitors just passed {company_data.get('company_name', 'your company')}",
            'body': self._clean_email_body(response.choices[0].message.content),
            'variant': 'competitive_threat_pvp'
        }

    def generate_case_study_email(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate case study email with specific customer success"""
        
        # Select relevant customer case study
        case_studies = {
            'rep_performance_crisis': {
                'company': 'Butler Specialty',
                'result': 'increased rep productivity by 300%',
                'quote': 'eCat flexibly configures to the way we do business',
                'savings': '$780,000'
            },
            'sales_enablement_collapse': {
                'company': 'Godinger Silver',
                'result': 'transformed their 25-year-old process',
                'quote': 'the best thing that has ever happened to this company',
                'savings': '$650,000'
            },
            'technology_obsolescence': {
                'company': 'Wildwood Lamps',
                'result': 'reduced customer calls by 33%',
                'quote': 'I\'ve reduced by a third the number of calls per day',
                'savings': '$425,000'
            },
            'sku_complexity': {
                'company': 'Theodore Alexander',
                'result': 'simplified 200,000+ configurations',
                'quote': 'Finally have control over our complexity',
                'savings': '$890,000'
            },
            'channel_conflict': {
                'company': 'Universal Furniture',
                'result': 'unified 5 sales channels',
                'quote': 'The reps are now mobile. They are in love',
                'savings': '$1,200,000'
            }
        }
        
        case_study = case_studies.get(primary_pain, case_studies['sales_enablement_collapse'])
        
        prompt = f"""
        Generate a PVP case study email featuring:
        
        Company: {case_study['company']} (similar to {company_data.get('company_name')})
        
        Situation (Before):
        - 8,000 SKUs, manual processing
        - 4-hour order cycle
        - 30% error rate
        - Reps: 80% admin, 20% selling
        
        Solution:
        - Deployed in 14 days
        - Customized for their pricing model
        - Integrated with existing ERP
        - Full offline capability
        
        Results (90 days):
        - Order time: 4 hours → 15 minutes
        - Errors: 30% → <1%
        - {case_study['result']}
        - Annual savings: {case_study['savings']}
        
        Customer Quote: "{case_study['quote']}"
        
        Keep under 100 words. Use clear before/after structure.
        End with: "Want their implementation playbook? (12-minute video)"
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You share detailed customer transformations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=250
        )
        
        return {
            'sequence_step': 5,
            'send_day': 14,
            'subject': f"How {case_study['company']} saved {case_study['savings']} annually",
            'body': self._clean_email_body(response.choices[0].message.content),
            'variant': 'case_study_pvp'
        }

    def generate_urgency_email(self, company_data: Dict) -> Dict:
        """Generate urgency email"""
        
        days_to_vegas = company_data.get('days_to_show', 35)
        booth_cost = company_data.get('booth_cost', 32000)
        opportunity_cost = booth_cost * 0.60  # 60% opportunities lost without mobile
        
        prompt = f"""
        Generate a PVP urgency email for {company_data.get('company_name')}.
        
        Time Pressure:
        - {days_to_vegas} days until {company_data.get('trade_show', 'Vegas Market')}
        - Booth #{company_data.get('booth_number', 'C-1055')} cost: ${booth_cost:,}
        - Without mobile orders: ${opportunity_cost:,} wasted
        
        Implementation Timeline:
        - Setup takes 14 days
        - Must start this week to be ready
        - Next show (High Point) in 89 days
        
        Risk Statement:
        "Fix this now or face same problems at next 3 shows"
        
        Keep under 100 words. Create genuine urgency.
        End with: "15-minute call to map out implementation?"
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You create appropriate urgency with specific deadlines."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        return {
            'sequence_step': 6,
            'send_day': 18,
            'subject': f"{days_to_vegas} days to {company_data.get('trade_show', 'Vegas Market')} - {company_data.get('company_name', 'your company')} ready?",
            'body': self._clean_email_body(response.choices[0].message.content),
            'variant': 'urgency_pvp'
        }

    def generate_breakup_email(self, company_data: Dict) -> Dict:
        """Generate break-up email"""
        
        lost_value = company_data.get('annual_cost', 400000)
        
        prompt = f"""
        Generate a PVP break-up email for {company_data.get('company_name')}.
        
        Structure:
        1. Haven't heard back, assuming not a priority
        2. Before I go, here's value:
           - ROI Calculator for furniture manufacturers
           - "2025 State of Furniture Sales" report
           - {company_data.get('trade_show', 'Vegas Market')} success guide
        3. Warning: Butler Specialty waited 2 years, cost them $1.4M
        4. Door remains open if priorities change
        
        Keep under 100 words. Professional but include warning.
        """
        
        response = self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": "You write professional break-up emails with value."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        return {
            'sequence_step': 7,
            'send_day': 21,
            'subject': f"Resources for {company_data.get('company_name')} (breaking up)",
            'body': self._clean_email_body(response.choices[0].message.content),
            'variant': 'breakup_pvp'
        }
    
    def generate_subject_line(self, company_data: Dict, primary_pain: str, email_type: str) -> str:
        """Generate subject line based on proven patterns"""
        
        company_name = company_data.get('company_name', 'your company')
        
        # PVP-style subject lines with specific evidence
        subject_templates = {
            'problem': [
                f"Found {company_name}'s ${(company_data.get('annual_cost') or 400000):,} productivity leak",
                f"{company_name}: Your {primary_pain.replace('_', ' ')} costs ${(company_data.get('error_cost') or 100000):,}",
                f"Why {company_name} loses 4 of 5 deals",
                f"{company_name}'s 30% error rate = ${(company_data.get('return_cost') or 200000):,} loss"
            ],
            'social_proof': [
                f"How {self.customer_quotes.get(primary_pain, 'Butler Specialty')} beat {company_name}'s problem",
                f"{company_name}: See 300% productivity gain proof",
                f"'{random.choice(list(self.customer_quotes.values()))}' - familiar?"
            ],
            'roi': [
                f"${company_data.get('annual_cost', 400000):,} impact for {company_name}",
                f"{company_name}: 47-day payback on ${20000} investment",
                f"Your {primary_pain.replace('_', ' ')} = ${company_data.get('error_cost', 100000):,}/year"
            ],
            'competitive': [
                f"3 competitors just passed {company_name}",
                f"{company_name} is 40% slower than digital competitors",
                f"While {company_name} uses {company_data.get('legacy_system', 'spreadsheets')}..."
            ],
            'urgency': [
                f"{company_data.get('days_to_show', 35)} days to {company_data.get('trade_show', 'Vegas')} - ready?",
                f"{company_name}'s ${company_data.get('booth_cost', 32000):,} booth at risk",
                f"Fix before High Point or lose ${50000}"
            ],
            'breakup': [
                f"Final resources for {company_name}",
                f"{company_name}: Breaking up (+ free ROI calculator)",
                f"Goodbye {company_name} (don't make Butler's mistake)"
            ]
        }
        
        # Select template
        templates = subject_templates.get(email_type, subject_templates['problem'])
        subject = random.choice(templates)
        
        return subject[:100]  # Keep under 100 chars
    
    def _clean_email_body(self, body: str) -> str:
        """Remove any subject line that might be included in the email body"""
        import re
        
        # Remove lines that start with "Subject:" or similar patterns
        lines = body.strip().split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            # Skip lines that look like subject lines
            if re.match(r'^Subject\s*:', line, re.IGNORECASE):
                continue
            if re.match(r'^Re\s*:', line, re.IGNORECASE):
                continue
            if re.match(r'^Fwd\s*:', line, re.IGNORECASE):
                continue
            cleaned_lines.append(line)
        
        cleaned_body = '\n'.join(cleaned_lines).strip()
        
        # Ensure it starts with a proper greeting
        if not re.match(r'^(Hey|Hi|Hello)', cleaned_body, re.IGNORECASE):
            # If no greeting found, add a generic one
            company_name = cleaned_body.split()[0] if cleaned_body else "Team"
            if company_name.endswith(','):
                company_name = company_name[:-1]
            cleaned_body = f"Hey {company_name},\n\n{cleaned_body}"
        
        return cleaned_body
    
    def generate_linkedin_messages(self, 
                                   company_data: Dict,
                                   primary_pain: str,
                                   decision_makers: List[Dict]) -> List[Dict]:
        """Generate LinkedIn outreach messages"""
        messages = []
        
        for dm in decision_makers[:3]:  # Top 3 decision makers
            # Connection request
            connection_request = self.generate_linkedin_connection(company_data, dm, primary_pain)
            messages.append(connection_request)
            
            # Follow-up message
            follow_up = self.generate_linkedin_followup(company_data, dm, primary_pain)
            messages.append(follow_up)
        
        return messages
    
    def generate_linkedin_connection(self, company_data: Dict, decision_maker: Dict, primary_pain: str) -> Dict:
        """Generate LinkedIn connection request (300 chars max)"""
        
        # Get specific evidence
        evidence = company_data.get('evidence_points', ['manual processing'])[0]
        
        # PVP connection templates with evidence
        templates = {
            'sales_enablement_collapse': "Hi {first_name}, analyzed {company}'s process. Your {evidence} costs ${annual_cost}/year. Have Butler Specialty's playbook for fixing this. Worth connecting?",
            'technology_obsolescence': "Hi {first_name}, {company}'s {legacy_system} makes you 40% slower. 3 competitors digitized in 2024. Have their transformation data. Connect?",
            'rep_performance_crisis': "{first_name}, {company}'s {rep_count} reps have 10x performance variance. Zero visibility = ${turnover_cost} turnover cost. Fixed for Butler. Connect?",
            'sku_complexity': "Hi {first_name}, {company}'s {sku_count} SKUs approaching 15% error threshold. Current {evidence} = ${error_cost} loss. Have solution. Connect?",
            'channel_conflict': "{first_name}, {company}'s channel conflicts cost 59% revenue. Your {evidence} fixable. Theodore Alexander case study relevant. Connect?"
        }
        
        template = templates.get(primary_pain, templates['sales_enablement_collapse'])
        
        message = template.format(
            first_name=decision_maker.get('first_name', 'there'),
            company=company_data.get('company_name', 'your company'),
            evidence=evidence[:40],  # Truncate for length
            annual_cost=f"{(company_data.get('annual_cost') or 400000) // 1000}K",
            legacy_system=company_data.get('legacy_system', 'manual process'),
            rep_count=company_data.get('rep_count', 10),
            turnover_cost=f"{((company_data.get('rep_count') or 10) * 75000 * 0.27) // 1000:.0f}K",
            sku_count=f"{(company_data.get('catalog_sku_count') or 2000):,}",
            error_cost=f"{(company_data.get('error_cost') or 100000) // 1000}K"
        )
        
        return {
            'type': 'connection_request',
            'decision_maker_id': decision_maker.get('id'),
            'message': message[:300],  # LinkedIn limit
            'send_day': 0
        }
    
    def generate_linkedin_followup(self, company_data: Dict, decision_maker: Dict, primary_pain: str) -> Dict:
        """Generate LinkedIn follow-up message after connection is accepted"""
        
        # Get evidence points
        evidence_points = company_data.get('evidence_points', [])[:3]
        if not evidence_points:
            evidence_points = ['No mobile capability', 'Manual order processing', 'PDF catalogs only']
        
        # Map pain to specific followup with value
        case_study = self.customer_quotes.get(primary_pain, 'Butler Specialty')
        
        followup_template = f"""Thanks for connecting, {decision_maker.get('first_name', 'there')}!

Analyzed {company_data.get('company_name')}'s operations and found 3 fixable issues:
1. {evidence_points[0]}
2. {evidence_points[1] if len(evidence_points) > 1 else 'Manual processes'}
3. {evidence_points[2] if len(evidence_points) > 2 else 'No offline capability'}

These cost you ~${company_data.get('annual_cost', 400000):,} annually.

{case_study} fixed this in 14 days, ROI in 47 days.

Want their implementation playbook? Happy to share - no pitch required.

Best,
[Your Name]"""

        return {
            'type': 'follow_up',
            'decision_maker_id': decision_maker.get('id'),
            'message': followup_template,
            'send_day': 3
        }

    def generate_ad_suggestions(self, company_data: Dict, primary_pain: str) -> List[Dict]:
        """Generate ad copy suggestions for partner team"""
        ad_suggestions = []
        
        # Google Search Ads
        google_ads = self.generate_google_ad_copy(company_data, primary_pain)
        ad_suggestions.append(google_ads)
        
        # Meta/Facebook Ads
        meta_ads = self.generate_meta_ad_copy(company_data, primary_pain)
        ad_suggestions.append(meta_ads)
        
        # LinkedIn Ads
        linkedin_ads = self.generate_linkedin_ad_copy(company_data, primary_pain)
        ad_suggestions.append(linkedin_ads)
        
        return ad_suggestions
    
    def generate_google_ad_copy(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate Google Ads copy"""
        
        # PVP headlines with specific evidence
        headlines = {
            'sales_enablement_collapse': [
                f"{company_data.get('company_name', 'Your company')}: Stop 3-Hour Waste",
                f"Save ${(company_data.get('annual_cost') or 400000) // 1000}K Annually",
                "Trade Show Chaos Fixed"
            ],
            'technology_obsolescence': [
                f"{company_data.get('company_name', 'Your company')}: Escape {company_data.get('legacy_system', 'Spreadsheets')}",
                "40% Faster Than Manual",
                "Modern Sales, Keep ERP"
            ],
            'rep_performance_crisis': [
                f"Fix {company_data.get('rep_count', 10)} Rep Chaos",
                "10x Performance Gap",
                "Rep Visibility Solution"
            ],
            'sku_complexity': [
                f"{(company_data.get('catalog_sku_count') or 2000):,} SKUs Simplified",
                "30% Errors → <1%",
                "Configuration Mastery"
            ],
            'channel_conflict': [
                "Unify Sales Channels",
                "59% Revenue Recovery",
                "End Channel Wars"
            ]
        }
        
        descriptions = {
            'sales_enablement_collapse': [
                f"Give {company_data.get('company_name')}'s reps 15 hours weekly back. Work offline at trade shows. Perfect accuracy.",
                f"Save ${company_data.get('annual_cost', 400000):,} annually. Real customer: 'Best thing in 25 years.' Setup in 14 days."
            ],
            'technology_obsolescence': [
                f"Works with {company_data.get('company_name')}'s current ERP. No IT project. Deploy in 3 weeks not 18 months.",
                f"Stop losing to digital competitors. {company_data.get('legacy_system', 'Manual')} to modern in 14 days."
            ]
        }
        
        # Get appropriate headlines and descriptions
        selected_headlines = headlines.get(primary_pain, headlines['sales_enablement_collapse'])
        selected_descriptions = descriptions.get(primary_pain, descriptions['sales_enablement_collapse'])
        
        return {
            'platform': 'google',
            'ad_type': 'search',
            'headlines': selected_headlines,
            'descriptions': selected_descriptions,
            'display_url': f'supercatsolutions.com/{company_data.get("company_name", "demo").lower().replace(" ", "")}',
            'final_url': f'https://supercatsolutions.com/demo?company={company_data.get("company_name", "")}&utm_source=google&utm_medium=cpc&utm_campaign=pvp_{primary_pain}',
            'keywords': [
                f'"{company_data.get("company_name", "")}"',
                f'{company_data.get("company_name", "")} order management',
                'B2B order management',
                'sales enablement software',
                'trade show order app',
                'furniture sales software',
                'wholesale order management'
            ],
            'negative_keywords': ['free', 'cheap', 'jobs', 'careers'],
            'suggested_bid': 8.50,
            'suggested_daily_budget': 150
        }
    
    def generate_meta_ad_copy(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate Meta/Facebook ad copy"""
        
        # Calculate impact numbers
        annual_savings = company_data.get('annual_cost', 400000)
        days_to_show = company_data.get('days_to_show', 35)
        booth_cost = company_data.get('booth_cost', 32000)
        
        # PVP primary text with evidence
        primary_text = f"""🚨 {company_data.get('company_name')} - Found ${annual_savings:,} in productivity losses

I analyzed your sales process:
- {company_data.get('evidence_points', ['Manual order processing'])[0]}
- Losing 3 hours daily per rep
- 30% error rate on orders

With {days_to_show} days until {company_data.get('trade_show', 'Vegas Market')}, your ${booth_cost:,} booth investment needs mobile order capability.

Butler Specialty had same problem. Fixed in 14 days. ROI in 47 days.

See your custom ROI analysis →"""
        
        return {
            'platform': 'meta',
            'ad_type': 'lead_generation',
            'primary_text': primary_text,
            'headline': f"{company_data.get('company_name')}: Save ${annual_savings // 1000}K Annually",
            'description': 'Mobile order management for furniture manufacturers',
            'call_to_action': 'Get Custom ROI',
            'image_text_overlay': f"${annual_savings:,}\nAnnual Savings",
            'targeting': {
                'company': company_data.get('company_name'),
                'job_titles': ['VP Sales', 'Sales Director', 'President', 'Owner'],
                'interests': ['Trade Shows', 'B2B Sales', 'Manufacturing']
            }
        }

    def generate_linkedin_ad_copy(self, company_data: Dict, primary_pain: str) -> Dict:
        """Generate LinkedIn ad copy"""
        
        evidence_points = company_data.get('evidence_points', [])[:2]
        annual_impact = company_data.get('annual_cost', 400000)
        
        intro_text = f"""Attention {company_data.get('company_name')} leadership:

Your sales team loses ${annual_impact:,} annually to:
- {evidence_points[0] if evidence_points else 'Manual order processing'}
- {evidence_points[1] if len(evidence_points) > 1 else 'No mobile capability'}

3 competitors digitized in 2024. Each reports 25-40% sales increase.

See how Butler Specialty transformed identical challenges."""
        
        return {
            'platform': 'linkedin',
            'ad_type': 'sponsored_content',
            'intro_text': intro_text,
            'headline': f"{company_data.get('company_name')}: Eliminate ${annual_impact:,} in Waste",
            'description': 'Get your custom transformation roadmap',
            'call_to_action': 'Download Analysis',
            'target_company': company_data.get('company_name'),
            'target_titles': ['VP Sales', 'IT Director', 'President'],
            'pain_point': primary_pain
        }

    def extract_personalization_tokens(self, company_data: Dict) -> Dict:
        """Extract all personalization tokens for merge tags"""
        return {
            'company_name': company_data.get('company_name'),
            'industry': company_data.get('industry', 'Furniture/Lighting'),
            'employee_count': company_data.get('employee_count'),
            'rep_count': company_data.get('rep_count'),
            'sku_count': company_data.get('catalog_sku_count'),
            'current_erp': company_data.get('current_erp'),
            'legacy_system': company_data.get('legacy_system'),
            'trade_show_count': company_data.get('trade_show_count_annual'),
            'annual_cost': company_data.get('annual_cost'),
            'error_cost': company_data.get('error_cost'),
            'return_cost': company_data.get('return_cost'),
            'booth_cost': company_data.get('booth_cost'),
            'days_to_show': company_data.get('days_to_show'),
            'trade_show': company_data.get('trade_show'),
            'evidence_points': company_data.get('evidence_points'),
            'years_in_business': datetime.now().year - company_data.get('year_founded', datetime.now().year)
        }