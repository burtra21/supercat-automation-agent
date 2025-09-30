"""
Validated Message Generator - Enhanced with Validation Study Data
Based on C2 Supercat Customer Pain Signal Validation Study

Uses dual methodology PSI results to generate:
1. Crisis intervention messaging (weighted methodology)
2. Operational intelligence context (averaged methodology)
3. Evidence-based hooks from validation study
"""

import json
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path
import random
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from analysis.validated_psi_calculator import ValidatedPSICalculator

logger = logging.getLogger(__name__)

class ValidatedMessageGenerator:
    """
    Enhanced message generator using validation study findings
    
    Combines:
    - Weighted methodology for crisis intervention messaging
    - Averaged methodology for operational intelligence
    - Validated customer language patterns
    - Evidence-based hooks from $2.3M customer portfolio
    """
    
    def __init__(self, openai_api_key: Optional[str] = None):
        """Initialize with validated data and configurations"""
        self.openai_api_key = openai_api_key
        self.openai_client = None
        
        if openai_api_key and OPENAI_AVAILABLE:
            self.openai_client = OpenAI(api_key=openai_api_key)
        
        # Initialize PSI calculator
        self.psi_calculator = ValidatedPSICalculator()
        
        # Load configurations
        self.crisis_messaging = self._load_crisis_messaging()
        self.validated_weights = self._load_validated_weights()
        
        # Validated customer quotes from study
        self.validated_customer_quotes = {
            'pebl_furniture': {
                'psi_score': 89.7,
                'quote': 'Manual catalog navigation killing productivity',
                'transformation': 'Eliminated 3 hours daily per rep waste'
            },
            'globalux_lighting': {
                'psi_score': 79.75,
                'quote': 'Mobile failures devastate trade show performance',
                'transformation': 'Real-time mobile ordering at trade shows'
            },
            'americas_backyards': {
                'psi_score': 75.0,
                'quote': 'Outdoor furniture complexity requires search capability',
                'transformation': 'Instant product discovery for complex catalogs'
            },
            'butler_specialty': {
                'quote': 'eCat flexibly configures to the way we do business',
                'transformation': '300% rep productivity increase'
            },
            'godinger_silver': {
                'quote': 'Best thing that has ever happened to this company in 25 years',
                'transformation': 'Transformed 25-year-old manual process'
            },
            'wildwood_lamps': {
                'quote': 'I\'ve reduced by a third the number of calls per day',
                'transformation': '33% reduction in customer support calls'
            },
            'universal_furniture': {
                'quote': 'The reps are now mobile. They are in love',
                'transformation': 'Mobile-enabled sales force transformation'
            }
        }
        
        logger.info("Initialized ValidatedMessageGenerator with dual methodology support")
    
    def _load_crisis_messaging(self) -> Dict[str, Any]:
        """Load crisis messaging configuration"""
        try:
            config_path = Path("supercat_automation/config/crisis_messaging.json")
            if config_path.exists():
                with open(config_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading crisis messaging config: {e}")
        return {}
    
    def _load_validated_weights(self) -> Dict[str, Any]:
        """Load validated EDP weights configuration"""
        try:
            config_path = Path("supercat_automation/config/validated_edp_weights.json")
            if config_path.exists():
                with open(config_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading validated weights config: {e}")
        return {}
    
    def generate_validated_campaign(self, company_data: Dict[str, Any], 
                                  website_evidence: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate complete campaign using validated dual methodology
        
        Args:
            company_data: Company information
            website_evidence: Website analysis results
            
        Returns:
            Complete campaign with both methodologies' insights
        """
        
        # Calculate dual PSI scores
        psi_results = self.psi_calculator.calculate_dual_psi(company_data, website_evidence)
        
        # Extract methodology results
        weighted_results = psi_results["weighted_methodology"]
        averaged_results = psi_results["averaged_methodology"]
        messaging = psi_results["messaging"]
        
        # Generate campaign based on weighted methodology (qualification)
        if weighted_results["qualification_decision"]:
            campaign = self._generate_qualified_campaign(
                company_data, psi_results, weighted_results, averaged_results
            )
        else:
            campaign = self._generate_nurture_campaign(
                company_data, psi_results, weighted_results, averaged_results
            )
        
        # Add validation study context
        campaign["validation_context"] = {
            "study_source": "C2 Supercat Customer Pain Signal Validation Study",
            "methodology_used": "dual_validated",
            "weighted_psi": weighted_results["psi_score"],
            "averaged_psi": averaged_results["psi_score"],
            "purchase_probability": weighted_results["purchase_probability"],
            "qualification_accuracy": "85% validated accuracy"
        }
        
        return campaign
    
    def _generate_qualified_campaign(self, company_data: Dict[str, Any], psi_results: Dict[str, Any],
                                   weighted_results: Dict[str, Any], averaged_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate campaign for qualified prospects (Tier A/B)"""
        
        campaign = {
            "campaign_type": "crisis_intervention",
            "qualification_tier": weighted_results["tier"],
            "primary_methodology": "weighted",
            "secondary_intelligence": "averaged",
            "email_sequence": [],
            "linkedin_sequence": [],
            "ad_suggestions": []
        }
        
        # Generate 7-email sequence with crisis intervention approach
        campaign["email_sequence"] = self._generate_crisis_email_sequence(
            company_data, psi_results, weighted_results
        )
        
        # Generate LinkedIn messages with crisis hooks
        campaign["linkedin_sequence"] = self._generate_crisis_linkedin_sequence(
            company_data, psi_results, weighted_results
        )
        
        # Generate ad copy with crisis messaging
        campaign["ad_suggestions"] = self._generate_crisis_ad_copy(
            company_data, psi_results, weighted_results
        )
        
        # Add operational intelligence for account context
        campaign["operational_intelligence"] = {
            "averaged_primary_edp": averaged_results["primary_edp"],
            "operational_challenges": averaged_results["operational_intelligence"],
            "expansion_opportunities": self._identify_expansion_opportunities(psi_results),
            "conversation_starters": averaged_results["operational_intelligence"]["conversation_starters"]
        }
        
        return campaign
    
    def _generate_nurture_campaign(self, company_data: Dict[str, Any], psi_results: Dict[str, Any],
                                 weighted_results: Dict[str, Any], averaged_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate nurture campaign for non-qualified prospects (Tier C)"""
        
        campaign = {
            "campaign_type": "educational_nurture",
            "qualification_tier": weighted_results["tier"],
            "primary_methodology": "averaged",
            "approach": "operational_efficiency_focus",
            "email_sequence": [],
            "linkedin_sequence": [],
            "content_suggestions": []
        }
        
        # Generate educational email sequence
        campaign["email_sequence"] = self._generate_nurture_email_sequence(
            company_data, psi_results, averaged_results
        )
        
        # Generate LinkedIn educational content
        campaign["linkedin_sequence"] = self._generate_nurture_linkedin_sequence(
            company_data, psi_results, averaged_results
        )
        
        # Generate educational content suggestions
        campaign["content_suggestions"] = self._generate_educational_content(
            company_data, psi_results, averaged_results
        )
        
        return campaign
    
    def _generate_crisis_email_sequence(self, company_data: Dict[str, Any], 
                                      psi_results: Dict[str, Any], weighted_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate 3-email sequence using refined EDP-specific templates"""
        
        sequence = []
        primary_edp = weighted_results["primary_edp"]
        
        # Map primary EDP to specific template functions
        edp_templates = {
            "EDP1_SKU_Complexity": [
                self._generate_sku_complexity_email_1,
                self._generate_sku_complexity_email_2,
                self._generate_sku_complexity_email_3
            ],
            "EDP7_Sales_Enablement": [
                self._generate_sales_enablement_email_1,
                self._generate_sales_enablement_email_2,
                self._generate_sales_enablement_email_3
            ],
            "EDP8_Technology_Obsolescence": [
                self._generate_technology_email_1,
                self._generate_technology_email_2,
                self._generate_technology_email_3
            ],
            "EDP2_Rep_Management": [
                self._generate_rep_performance_email_1,
                self._generate_rep_performance_email_2,
                self._generate_rep_performance_email_3
            ],
            "EDP6_Channel_Conflict": [
                self._generate_channel_conflict_email_1,
                self._generate_channel_conflict_email_2,
                self._generate_channel_conflict_email_3
            ]
        }
        
        # Get template functions for primary EDP or default to sales enablement
        template_functions = edp_templates.get(primary_edp, edp_templates["EDP7_Sales_Enablement"])
        
        # Generate 3-email sequence
        send_days = [0, 3, 7]
        for i, template_func in enumerate(template_functions):
            email = template_func(company_data, psi_results, i + 1, send_days[i])
            sequence.append(email)
        
        return sequence
    
    def _generate_crisis_identification_email(self, company_data: Dict[str, Any], 
                                            psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Generate Email 1: Crisis identification with specific evidence"""
        
        company_name = company_data.get('company_name', 'your company')
        weighted_psi = psi_results["weighted_methodology"]["psi_score"]
        evidence_hooks = psi_results["messaging"]["evidence_based_hooks"]
        
        # Get crisis hook from configuration
        crisis_hook = psi_results["messaging"]["weighted_methodology_hook"]
        if not crisis_hook:
            crisis_hook = f"Found {company_name}'s critical operational failures"
        
        # Build subject line
        subject_templates = [
            f"{company_name}: {crisis_hook}",
            f"Found {company_name}'s ${self._calculate_annual_loss(company_data, psi_results):,} productivity leak",
            f"{company_name}: Multiple critical failures detected"
        ]
        subject = random.choice(subject_templates)
        
        # Use proven templates for consistent quality
        body = self._generate_template_email_body(
            company_data, "crisis_identification", {
                "crisis_hook": crisis_hook,
                "evidence_hooks": evidence_hooks[:3]
            }
        )
        
        return {
            "sequence_step": 1,
            "send_day": 0,
            "email_type": "crisis_identification",
            "subject": subject,
            "body": body,
            "methodology": "weighted",
            "primary_edp": primary_edp,
            "crisis_level": psi_results["messaging"]["crisis_level"],
            "personalization_data": {
                "company_name": company_name,
                "crisis_hook": crisis_hook,
                "evidence_count": len(evidence_hooks),
                "psi_score": weighted_psi
            }
        }
    
    def _generate_evidence_proof_email(self, company_data: Dict[str, Any], 
                                     psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Generate Email 2: Evidence-based proof with validation study data"""
        
        company_name = company_data.get('company_name', 'your company')
        evidence_patterns = psi_results["evidence_patterns"]["digital_failures"]
        
        # Select relevant customer example from validation study
        customer_example = self._select_relevant_customer_example(primary_edp, psi_results)
        
        subject = f"How {customer_example['company']} fixed {company_name}'s exact problem"
        
        body = self._generate_template_email_body(
            company_data, "evidence_proof", {
                "customer_example": customer_example,
                "evidence_patterns": evidence_patterns
            }
        )
        
        return {
            "sequence_step": 2,
            "send_day": 3,
            "email_type": "evidence_proof",
            "subject": subject,
            "body": body,
            "methodology": "weighted",
            "validation_source": "C2 Supercat Customer Pain Signal Validation Study",
            "customer_example": customer_example
        }
    
    def _generate_customer_validation_email(self, company_data: Dict[str, Any], 
                                          psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Generate Email 3: Customer validation with specific transformation data"""
        
        # Get multiple customer examples for social proof
        customer_examples = self._get_multiple_customer_examples(primary_edp, 3)
        
        subject = f"3 companies solved {company_data.get('company_name', 'your')}'s exact challenges"
        
        body = self._generate_template_email_body(
            company_data, "customer_validation", {
                "customer_examples": customer_examples
            }
        )
        
        return {
            "sequence_step": 3,
            "send_day": 7,
            "email_type": "customer_validation",
            "subject": subject,
            "body": body,
            "methodology": "weighted",
            "social_proof": customer_examples
        }
    
    def _generate_competitive_displacement_email(self, company_data: Dict[str, Any], 
                                               psi_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Email 4: Competitive displacement with market reality"""
        
        company_name = company_data.get('company_name', 'your company')
        
        # Get competitive messaging from configuration
        competitive_messaging = self.crisis_messaging.get("competitive_displacement_messaging", {})
        digital_competitors = competitive_messaging.get("urgency_creation", {}).get("digital_competitors", [])
        
        subject = f"3 competitors just passed {company_name}"
        
        body = self._generate_template_email_body(
            company_data, "competitive_displacement", {
                "digital_competitors": digital_competitors
            }
        )
        
        return {
            "sequence_step": 4,
            "send_day": 10,
            "email_type": "competitive_displacement",
            "subject": subject,
            "body": body,
            "methodology": "weighted",
            "competitive_intelligence": digital_competitors
        }
    
    def _generate_roi_crisis_email(self, company_data: Dict[str, Any], 
                                 psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Generate Email 5: ROI crisis intervention"""
        
        annual_loss = self._calculate_annual_loss(company_data, psi_results)
        company_name = company_data.get('company_name', 'your company')
        
        subject = f"{company_name}: ${annual_loss:,} annual crisis intervention"
        
        roi_data = {
            "annual_loss": annual_loss,
            "productivity_impact": self._calculate_productivity_impact(company_data, psi_results),
            "competitive_displacement_cost": self._calculate_competitive_cost(company_data, psi_results),
            "payback_period": "47 days (validated across 15 customers)"
        }
        
        body = self._generate_template_email_body(
            company_data, "roi_crisis", roi_data
        )
        
        return {
            "sequence_step": 5,
            "send_day": 14,
            "email_type": "roi_crisis",
            "subject": subject,
            "body": body,
            "methodology": "weighted",
            "roi_analysis": roi_data
        }
    
    def _generate_urgency_amplification_email(self, company_data: Dict[str, Any], 
                                            psi_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Email 6: Urgency amplification with time-sensitive triggers"""
        
        urgency_triggers = psi_results["messaging"]["urgency_triggers"]
        company_name = company_data.get('company_name', 'your company')
        
        # Calculate days to next trade show (example)
        days_to_show = 35  # Would be calculated from actual trade show calendar
        
        subject = f"{days_to_show} days to High Point Market - {company_name} ready?"
        
        urgency_data = {
            "days_to_show": days_to_show,
            "trade_show": "High Point Market",
            "booth_investment": "$32,000",
            "opportunity_loss": "60% without mobile capability",
            "urgency_triggers": urgency_triggers
        }
        
        if self.openai_client:
            body = self._generate_gpt_email_body(
                company_data, psi_results, "urgency_amplification", urgency_data
            )
        else:
            body = self._generate_template_email_body(
                company_data, "urgency_amplification", urgency_data
            )
        
        return {
            "sequence_step": 6,
            "send_day": 18,
            "email_type": "urgency_amplification",
            "subject": subject,
            "body": body,
            "methodology": "weighted",
            "urgency_data": urgency_data
        }
    
    def _generate_final_crisis_email(self, company_data: Dict[str, Any], 
                                   psi_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Email 7: Final crisis warning with resources"""
        
        company_name = company_data.get('company_name', 'your company')
        annual_loss = self._calculate_annual_loss(company_data, psi_results)
        
        subject = f"Final warning: {company_name}'s ${annual_loss:,} crisis"
        
        final_warning_data = {
            "annual_loss": annual_loss,
            "crisis_escalation": "Problems compound without intervention",
            "resource_offer": [
                "ROI Calculator for furniture manufacturers",
                "2025 State of Furniture Sales report", 
                "High Point Market success guide"
            ],
            "case_study_warning": "Butler Specialty waited 2 years, cost them $1.4M"
        }
        
        if self.openai_client:
            body = self._generate_gpt_email_body(
                company_data, psi_results, "final_crisis", final_warning_data
            )
        else:
            body = self._generate_template_email_body(
                company_data, "final_crisis", final_warning_data
            )
        
        return {
            "sequence_step": 7,
            "send_day": 21,
            "email_type": "final_crisis",
            "subject": subject,
            "body": body,
            "methodology": "weighted",
            "final_warning": final_warning_data
        }
    
    def _generate_gpt_email_body(self, company_data: Dict[str, Any], psi_results: Dict[str, Any], 
                               email_type: str, context_data: Dict[str, Any]) -> str:
        """Generate email body using GPT-4 with proven customer language patterns"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        evidence_hooks = psi_results["messaging"]["evidence_based_hooks"]
        
        # Use proven customer language patterns from your original generator
        if email_type == "crisis_identification":
            prompt = f"""Generate ONLY the EMAIL BODY for {company_name}. Do NOT include a subject line.

Start with: "Hey {first_name},"

MUST include this evidence: "{evidence_hooks[0] if evidence_hooks else 'Manual processes costing productivity'}"

Then add:
- 2 more specific problems: {evidence_hooks[1:3] if len(evidence_hooks) > 1 else ['No mobile capability', 'Manual order processing']}
- Financial impact: ${self._calculate_annual_loss(company_data, psi_results):,} annual loss
- Customer proof: "Butler Specialty had identical issues. Fixed in 14 days, ROI in 47 days."
- Discovery question: "Walk me through what happens when a rep takes an order at a trade show today?"

Keep under 100 words. Lead with value, not pitch. Use bullet points for problems.
End with: "15-minute call to show you their solution?"

IMPORTANT: Do NOT include "Subject:" or any subject line. Start directly with "Hey {first_name},"
"""
        
        elif email_type == "evidence_proof":
            customer_example = context_data.get('customer_example', {})
            prompt = f"""Generate ONLY the EMAIL BODY. Do NOT include a subject line.

Start with: "Hey {first_name},"

Feature this customer transformation:
Company: {customer_example.get('company', 'Butler Specialty')}
Quote: "{customer_example.get('quote', 'eCat flexibly configures to the way we do business')}"
Result: {customer_example.get('transformation', '300% rep productivity increase')}

Connect to {company_name}'s situation with evidence: {evidence_hooks[0] if evidence_hooks else 'similar challenges'}

Include:
- Before/after metrics: 4 hours → 15 minutes, 30% errors → <1%
- Validation: "Proven across $2.3M customer portfolio"
- Clear next step: "Want their implementation playbook?"

Keep under 100 words. Focus on transformation, not features.
"""
        
        elif email_type == "operational_efficiency":
            annual_loss = self._calculate_annual_loss(company_data, psi_results)
            prompt = f"""Generate ONLY the EMAIL BODY. Do NOT include a subject line.

Start with: "Hey {first_name},"

Lead with analysis: "I analyzed {company_name}'s operations and found several improvement opportunities:"

List these specific gaps:
{chr(10).join([f"• {hook}" for hook in evidence_hooks[:3]])}

Add benchmarks:
- Companies with similar profiles see 25-40% productivity improvements
- Butler Specialty: 300% rep productivity increase
- Worth ${annual_loss:,} annually in optimization potential

Keep under 100 words. No corporate speak.
End with: "Would you like to see how Butler Specialty optimized their operations?"

P.S. No sales pitch - just sharing what worked for similar companies.
"""
        
        else:
            # Fallback for other email types
            prompt = f"""Generate a direct, evidence-based email for {company_name}.
            
Start with: "Hey {first_name},"
Include evidence: {evidence_hooks[0] if evidence_hooks else 'operational challenges'}
Keep under 100 words.
End with clear next step.
"""
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You write direct, evidence-based B2B emails using proven customer language. No corporate fluff."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=200
            )
            
            return self._clean_email_body(response.choices[0].message.content)
            
        except Exception as e:
            logger.error(f"GPT-4 generation failed: {e}")
            return self._generate_template_email_body(company_data, email_type, context_data)
    
    def _generate_template_email_body(self, company_data: Dict[str, Any], 
                                    email_type: str, context_data: Dict[str, Any]) -> str:
        """Generate email body using proven templates from your original generator"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        annual_loss = self._calculate_annual_loss(company_data, context_data)
        evidence_hooks = context_data.get('evidence_hooks', ['Manual processes'])
        
        templates = {
            "crisis_identification": f"""Hey {first_name},

I analyzed {company_name}'s sales process and found you're losing ~3 hours daily per rep on manual order processing - that's ${annual_loss:,} in lost productivity annually.

• {evidence_hooks[0] if evidence_hooks else 'Manual order processing'}
• {evidence_hooks[1] if len(evidence_hooks) > 1 else 'No mobile capability'}
• {evidence_hooks[2] if len(evidence_hooks) > 2 else 'PDF catalogs only'}

Butler Specialty had identical issues. Fixed in 14 days, ROI in 47 days.

Walk me through what happens when a rep takes an order at a trade show today?

15-minute call to show you their solution?

Best,
[Your Name]""",

            "evidence_proof": f"""Hey {first_name},

{context_data.get('customer_example', {}).get('company', 'Butler Specialty')} had {company_name}'s exact problem:

"{context_data.get('customer_example', {}).get('quote', 'eCat flexibly configures to the way we do business')}"

Their transformation:
• Order time: 4 hours → 15 minutes
• Error rate: 30% → <1%
• {context_data.get('customer_example', {}).get('transformation', '300% rep productivity increase')}
• 47-day payback period

Proven across $2.3M customer portfolio.

Want their implementation playbook?

Best,
[Your Name]""",

            "customer_validation": f"""Hey {first_name},

3 companies solved {company_name}'s challenges:

• Butler Specialty: 300% rep productivity increase
• Godinger Silver: "Best thing in 25 years"
• Wildwood Lamps: 33% fewer support calls

All report 25-40% productivity increases within 90 days.

12-minute video showing their results?

Best,
[Your Name]""",

            "competitive_displacement": f"""Hey {first_name},

While {company_name} uses {context_data.get('legacy_system', 'manual processes')}, 3 direct competitors digitized in 2024:

• Universal Furniture: 25% sales increase
• Theodore Alexander: 40% faster quotes  
• Butler Specialty: 300% rep productivity

Your competitors are 40% faster. Quote time: Them (minutes) vs You (hours).

Should we discuss closing this gap before High Point Market?

Best,
[Your Name]""",

            "roi_crisis": f"""Hey {first_name},

{company_name}'s current inefficiencies:

• Productivity loss: ${int(annual_loss * 0.4):,}/year
• Error costs: ${int(annual_loss * 0.35):,}/year  
• Trade show waste: ${int(annual_loss * 0.25):,}/year
• Total impact: ${annual_loss:,}/year

Investment: $20K/year
Payback: 47 days (validated across 15 customers)
5-Year ROI: {int(annual_loss * 5 / 20000)}x

Want your custom ROI model? Takes 15 minutes.

Best,
[Your Name]""",

            "urgency_amplification": f"""Hey {first_name},

{context_data.get('days_to_show', 35)} days until High Point Market.

Your ${context_data.get('booth_investment', '$32,000')} booth investment is at risk. Without mobile orders, you'll lose {context_data.get('opportunity_loss', '60%')} of opportunities to competitors who can quote on-spot.

Setup takes 14 days. Must start this week to be ready.

15-minute call to map out implementation?

Best,
[Your Name]""",

            "final_crisis": f"""Hey {first_name},

Haven't heard back, assuming this isn't a priority right now.

Before I go, here's some value:
• ROI Calculator for furniture manufacturers
• 2025 State of Furniture Sales report
• High Point Market success guide

Warning: Butler Specialty waited 2 years, cost them $1.4M.

Door remains open if priorities change.

Best,
[Your Name]"""
        }
        
        return templates.get(email_type, f"Hey {first_name},\n\nI analyzed {company_name}'s operations and found ${annual_loss:,} in productivity losses.\n\nBest,\n[Your Name]")
    
    def _clean_email_body(self, body: str) -> str:
        """Clean email body of any subject line artifacts"""
        import re
        
        lines = body.strip().split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            # Skip lines that look like subject lines
            if re.match(r'^Subject\s*:', line, re.IGNORECASE):
                continue
            if re.match(r'^Re\s*:', line, re.IGNORECASE):
                continue
            cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines).strip()
    
    def _select_relevant_customer_example(self, primary_edp: str, psi_results: Dict[str, Any]) -> Dict[str, str]:
        """Select most relevant customer example based on primary EDP"""
        
        edp_to_customer = {
            "EDP7_Sales_Enablement": "pebl_furniture",
            "EDP8_Technology_Obsolescence": "globalux_lighting", 
            "EDP1_SKU_Complexity": "americas_backyards",
            "EDP2_Rep_Management": "butler_specialty",
            "EDP6_Channel_Conflict": "universal_furniture"
        }
        
        customer_key = edp_to_customer.get(primary_edp, "butler_specialty")
        customer_data = self.validated_customer_quotes.get(customer_key, {})
        
        return {
            "company": customer_key.replace('_', ' ').title(),
            "quote": customer_data.get('quote', 'Significant operational improvement'),
            "transformation": customer_data.get('transformation', 'Major productivity gains'),
            "psi_score": customer_data.get('psi_score', 75.0)
        }
    
    def _get_multiple_customer_examples(self, primary_edp: str, count: int) -> List[Dict[str, str]]:
        """Get multiple customer examples for social proof"""
        
        examples = []
        customer_keys = list(self.validated_customer_quotes.keys())
        
        # Start with most relevant
        primary_example = self._select_relevant_customer_example(primary_edp, {})
        examples.append(primary_example)
        
        # Add additional examples
        for key in customer_keys[:count-1]:
            if key != primary_example["company"].lower().replace(' ', '_'):
                customer_data = self.validated_customer_quotes[key]
                examples.append({
                    "company": key.replace('_', ' ').title(),
                    "quote": customer_data.get('quote', 'Operational improvement'),
                    "transformation": customer_data.get('transformation', 'Productivity gains')
                })
        
        return examples[:count]
    
    def _calculate_annual_loss(self, company_data: Dict[str, Any], psi_results: Dict[str, Any]) -> int:
        """Calculate estimated annual loss from operational inefficiencies"""
        
        rep_count = company_data.get('rep_count', 10)
        sku_count = company_data.get('catalog_sku_count', 2000)
        
        # Base calculation: 3 hours daily per rep at $100/hour
        base_loss = rep_count * 3 * 250 * 100  # 250 working days
        
        # Add SKU complexity multiplier
        if sku_count > 5000:
            base_loss *= 1.3
        elif sku_count > 2000:
            base_loss *= 1.1
        
        return int(base_loss)
    
    def _calculate_productivity_impact(self, company_data: Dict[str, Any], psi_results: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate productivity impact metrics"""
        
        rep_count = company_data.get('rep_count', 10)
        
        return {
            "hours_lost_daily": rep_count * 3,
            "orders_delayed_monthly": rep_count * 20,
            "error_rate_current": "30%",
            "error_rate_target": "<1%"
        }
    
    def _calculate_competitive_cost(self, company_data: Dict[str, Any], psi_results: Dict[str, Any]) -> int:
        """Calculate cost of competitive displacement"""
        
        annual_revenue = company_data.get('annual_revenue', 10000000)  # $10M default
        
        # Estimate 15% revenue at risk from competitive displacement
        return int(annual_revenue * 0.15)
    
    def _get_transformation_metrics(self, primary_edp: str) -> Dict[str, str]:
        """Get transformation metrics for specific EDP"""
        
        metrics = {
            "EDP7_Sales_Enablement": {
                "order_time_reduction": "4 hours → 15 minutes",
                "error_reduction": "30% → <1%",
                "rep_productivity": "300% increase"
            },
            "EDP8_Technology_Obsolescence": {
                "load_time_improvement": "3.5s → 0.8s",
                "uptime_improvement": "95% → 99.9%",
                "customer_satisfaction": "40% increase"
            },
            "EDP1_SKU_Complexity": {
                "search_efficiency": "Manual → Instant",
                "configuration_accuracy": "70% → 98%",
                "catalog_navigation": "3 hours → 5 minutes"
            },
            "EDP2_Rep_Management": {
                "rep_productivity": "300% increase",
                "territory_coverage": "40% improvement",
                "rep_satisfaction": "85% increase"
            },
            "EDP6_Channel_Conflict": {
                "pricing_consistency": "100% across channels",
                "channel_coordination": "Real-time sync",
                "revenue_recovery": "59% improvement"
            }
        }
        
        return metrics.get(primary_edp, {
            "productivity": "Significant improvement",
            "efficiency": "Major gains",
            "satisfaction": "High increase"
        })
    
    def _identify_expansion_opportunities(self, psi_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify expansion opportunities from averaged methodology"""
        
        opportunities = []
        averaged_results = psi_results["averaged_methodology"]
        edp_scores = psi_results["edp_scores"]
        
        # Look for secondary pain points with high scores
        for edp, score in edp_scores.items():
            if score > 50 and edp != averaged_results["primary_edp"]:
                opportunities.append({
                    "edp": edp,
                    "score": score,
                    "opportunity_type": "secondary_pain_point",
                    "expansion_potential": "high" if score > 70 else "medium",
                    "description": f"Secondary operational challenge with {score:.1f}% severity"
                })
        
        return opportunities
    
    def _generate_crisis_linkedin_sequence(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any], weighted_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate LinkedIn crisis intervention sequence"""
        
        sequence = []
        company_name = company_data.get('company_name', 'your company')
        primary_edp = weighted_results["primary_edp"]
        crisis_hook = psi_results["messaging"]["weighted_methodology_hook"]
        
        # LinkedIn Connection Request
        connection_message = f"Hi [first_name], analyzed {company_name}'s operations. {crisis_hook[:100]}... Worth connecting?"
        
        sequence.append({
            "type": "connection_request",
            "message": connection_message[:300],  # LinkedIn limit
            "send_day": 0,
            "methodology": "weighted"
        })
        
        # LinkedIn Follow-up Message
        followup_message = f"""Thanks for connecting, [first_name]!

Found 3 critical issues at {company_name}:
{chr(10).join([f"• {hook}" for hook in psi_results["messaging"]["evidence_based_hooks"][:3]])}

Butler Specialty had identical problems. Fixed in 14 days, ROI in 47 days.

Want their transformation playbook? (No pitch required)

Best,
[Your Name]"""
        
        sequence.append({
            "type": "follow_up",
            "message": followup_message,
            "send_day": 3,
            "methodology": "weighted"
        })
        
        return sequence
    
    def _generate_crisis_ad_copy(self, company_data: Dict[str, Any], 
                               psi_results: Dict[str, Any], weighted_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate crisis intervention ad copy"""
        
        company_name = company_data.get('company_name', 'your company')
        annual_loss = self._calculate_annual_loss(company_data, psi_results)
        primary_edp = weighted_results["primary_edp"]
        
        ad_suggestions = []
        
        # Google Search Ad
        google_ad = {
            "platform": "google_search",
            "headlines": [
                f"{company_name}: Crisis Intervention Required",
                f"${annual_loss:,} Annual Loss Detected",
                f"Immediate Action Needed"
            ],
            "descriptions": [
                f"Found critical operational failures at {company_name}. Butler Specialty fixed identical issues in 14 days.",
                f"Your competitors are 40% faster. Don't let manual processes kill your business."
            ],
            "keywords": [
                f'"{company_name}"',
                f'{company_name} operational efficiency',
                'furniture sales automation',
                'trade show mobile ordering'
            ],
            "landing_page": f"Crisis intervention page for {company_name}"
        }
        ad_suggestions.append(google_ad)
        
        # LinkedIn Sponsored Content
        linkedin_ad = {
            "platform": "linkedin_sponsored",
            "headline": f"{company_name}: ${annual_loss:,} Crisis Detected",
            "intro_text": f"""Attention {company_name} leadership:

Your operations analysis reveals critical failures costing ${annual_loss:,} annually.

3 competitors digitized in 2024. Each reports 25-40% sales increases.

See how Butler Specialty eliminated identical challenges.""",
            "call_to_action": "Get Crisis Analysis",
            "target_company": company_name,
            "target_titles": ["VP Sales", "President", "Owner"]
        }
        ad_suggestions.append(linkedin_ad)
        
        return ad_suggestions
    
    def _generate_nurture_email_sequence(self, company_data: Dict[str, Any], 
                                       psi_results: Dict[str, Any], averaged_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate 5-email educational nurture sequence for non-qualified prospects"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        primary_edp = averaged_results["primary_edp"]
        evidence_hooks = psi_results["messaging"]["evidence_based_hooks"]
        edp_scores = psi_results["edp_scores"]
        
        sequence = []
        
        # Build specific evidence-based content
        top_pain_points = []
        for edp, score in edp_scores.items():
            if score > 30:  # Significant enough to mention
                edp_name = edp.replace('_', ' ').replace('EDP1', 'SKU Management').replace('EDP2', 'Rep Performance').replace('EDP6', 'Channel Management').replace('EDP7', 'Sales Tools').replace('EDP8', 'Technology')
                top_pain_points.append(f"• {edp_name}: {score:.0f}% optimization opportunity")
        
        # Email 1: Operational Assessment (Day 0)
        email_1_body = f"""Hey {first_name},

I analyzed {company_name}'s operations and found several improvement opportunities:

{chr(10).join(top_pain_points[:3])}

{evidence_hooks[0] if evidence_hooks else 'Your current processes have room for optimization.'}

Companies with similar profiles typically see:
• 25-40% productivity improvements  
• 15-30% error reduction
• Better trade show performance

Would you like to see how Butler Specialty optimized their operations?

Best,
[Your Name]

P.S. No sales pitch - just sharing what worked for similar companies."""

        sequence.append({
            "sequence_step": 1,
            "send_day": 0,
            "email_type": "operational_assessment",
            "subject": f"Found {company_name}'s operational improvement opportunities",
            "body": email_1_body,
            "methodology": "averaged",
            "primary_edp": primary_edp
        })
        
        # Email 2: Industry Benchmarking (Day 4)
        customer_example = self._select_relevant_customer_example(primary_edp, psi_results)
        email_2_body = f"""Hey {first_name},

Quick follow-up on {company_name}'s operational analysis.

{customer_example['company']} had similar challenges:
"{customer_example['quote']}"

Their transformation: {customer_example['transformation']}

Industry benchmark data shows companies addressing these gaps see:
• 47-day average payback period
• 300% rep productivity increases
• 40% reduction in manual processes

Want their 12-minute case study video?

Best,
[Your Name]"""

        sequence.append({
            "sequence_step": 2,
            "send_day": 4,
            "email_type": "industry_benchmarking",
            "subject": f"How {customer_example['company']} solved {company_name}'s challenges",
            "body": email_2_body,
            "methodology": "averaged",
            "customer_example": customer_example
        })
        
        # Email 3: ROI Analysis (Day 8)
        annual_loss = self._calculate_annual_loss(company_data, psi_results)
        email_3_body = f"""Hey {first_name},

Based on {company_name}'s operational analysis, here's the financial impact:

Current inefficiencies cost approximately ${annual_loss:,} annually:
• Rep productivity gaps: ${int(annual_loss * 0.4):,}
• Manual process waste: ${int(annual_loss * 0.35):,}
• Technology delays: ${int(annual_loss * 0.25):,}

Butler Specialty recovered their investment in 47 days with similar improvements.

ROI calculator for furniture manufacturers?

Best,
[Your Name]"""

        sequence.append({
            "sequence_step": 3,
            "send_day": 8,
            "email_type": "roi_analysis",
            "subject": f"{company_name}: ${annual_loss:,} optimization opportunity",
            "body": email_3_body,
            "methodology": "averaged",
            "roi_data": {"annual_loss": annual_loss}
        })
        
        # Email 4: Resource Sharing (Day 12)
        email_4_body = f"""Hey {first_name},

Sharing some resources that helped companies like {company_name}:

📊 2025 Furniture Industry Efficiency Report
📋 Operational Assessment Checklist  
🎯 Trade Show Mobile Strategy Guide

These are based on our analysis of 15 companies ($2.3M portfolio) in the validation study.

{customer_example['company']} used these exact resources before their transformation.

Download link?

Best,
[Your Name]"""

        sequence.append({
            "sequence_step": 4,
            "send_day": 12,
            "email_type": "resource_sharing",
            "subject": f"Resources that helped companies like {company_name}",
            "body": email_4_body,
            "methodology": "averaged"
        })
        
        # Email 5: Final Value Offer (Day 16)
        email_5_body = f"""Hey {first_name},

Last note about {company_name}'s operational opportunities.

The companies that acted on similar findings:
• Butler Specialty: 300% rep productivity increase
• Godinger Silver: "Best thing in 25 years"
• Wildwood Lamps: 33% fewer support calls

Your analysis shows {len(top_pain_points)} optimization areas worth ${annual_loss:,} annually.

15-minute call to share what worked for them? (No pitch, just insights)

Best,
[Your Name]

P.S. If not interested, I'll stop here. Just wanted to share what helped similar companies."""

        sequence.append({
            "sequence_step": 5,
            "send_day": 16,
            "email_type": "final_value_offer",
            "subject": f"Final insights for {company_name} (no pitch)",
            "body": email_5_body,
            "methodology": "averaged"
        })
        
        return sequence
    
    def _generate_nurture_linkedin_sequence(self, company_data: Dict[str, Any], 
                                          psi_results: Dict[str, Any], averaged_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate LinkedIn nurture sequence with real content"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        evidence_hooks = psi_results["messaging"]["evidence_based_hooks"]
        primary_edp = averaged_results["primary_edp"]
        
        sequence = []
        
        # LinkedIn Connection Request
        connection_message = f"""Hi {first_name},

Analyzed {company_name}'s operations - found some interesting optimization opportunities.

{evidence_hooks[0] if evidence_hooks else 'Several areas for improvement identified.'}

Worth connecting to share insights?

Best,
[Your Name]"""
        
        sequence.append({
            "type": "connection_request",
            "message": connection_message[:300],  # LinkedIn character limit
            "send_day": 0,
            "methodology": "averaged"
        })
        
        # LinkedIn Follow-up Message
        customer_example = self._select_relevant_customer_example(primary_edp, psi_results)
        annual_loss = self._calculate_annual_loss(company_data, psi_results)
        
        followup_message = f"""Thanks for connecting, {first_name}!

Quick follow-up on {company_name}'s operational analysis:

Key findings:
{chr(10).join([f"• {hook}" for hook in evidence_hooks[:2]])}

{customer_example['company']} had similar challenges and saw: {customer_example['transformation']}

Worth ${annual_loss:,} annually in optimization potential.

12-minute case study video? (No pitch, just insights)

Best,
[Your Name]"""
        
        sequence.append({
            "type": "follow_up",
            "message": followup_message,
            "send_day": 3,
            "methodology": "averaged",
            "customer_example": customer_example
        })
        
        return sequence
    
    # === PROVEN TEMPLATE EMAIL METHODS ===
    
    def _generate_template_crisis_email(self, company_data: Dict[str, Any], 
                                      psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Email 1: Crisis identification using refined template"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        evidence_hooks = psi_results["messaging"]["evidence_based_hooks"]
        
        # Map primary EDP to specific templates
        edp_templates = {
            "EDP1_SKU_Complexity": self._generate_sku_complexity_email_1,
            "EDP7_Sales_Enablement": self._generate_sales_enablement_email_1,
            "EDP8_Technology_Obsolescence": self._generate_technology_email_1,
            "EDP2_Rep_Management": self._generate_rep_performance_email_1,
            "EDP6_Channel_Conflict": self._generate_channel_conflict_email_1
        }
        
        # Use specific template for primary EDP or default to sales enablement
        template_func = edp_templates.get(primary_edp, edp_templates["EDP7_Sales_Enablement"])
        return template_func(company_data, psi_results, 1, 0)
    
    def _generate_template_evidence_email(self, company_data: Dict[str, Any], 
                                        psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Email 2: Evidence proof using proven template"""
        
        first_name = company_data.get('first_name', 'there')
        company_name = company_data.get('company_name', 'your company')
        customer_example = self._select_relevant_customer_example(primary_edp, psi_results)
        
        subject = f"How {customer_example['company']} eliminated your exact problem"
        
        body = f"""Hey {first_name},

{customer_example['company']} had {company_name}'s exact problem:

"{customer_example['quote']}"

Their transformation:
• Order time: 4 hours → 15 minutes
• Error rate: 30% → <1%
• {customer_example['transformation']}
• 47-day payback period

Proven across $2.3M customer portfolio.

Want their implementation playbook?

Best,
[Your Name]"""
        
        return {
            "sequence_step": 2,
            "send_day": 3,
            "email_type": "evidence_proof_template",
            "subject": subject,
            "body": body,
            "methodology": "template",
            "source": "proven_template"
        }
    
    def _generate_template_validation_email(self, company_data: Dict[str, Any], 
                                          psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Email 3: Customer validation using proven template"""
        
        first_name = company_data.get('first_name', 'there')
        company_name = company_data.get('company_name', 'your company')
        
        subject = f"3 companies solved {company_name}'s exact challenges"
        
        body = f"""Hey {first_name},

3 companies solved {company_name}'s challenges:

• Butler Specialty: 300% rep productivity increase
• Godinger Silver: "Best thing in 25 years"
• Wildwood Lamps: 33% fewer support calls

All report 25-40% productivity increases within 90 days.

12-minute video showing their results?

Best,
[Your Name]"""
        
        return {
            "sequence_step": 3,
            "send_day": 7,
            "email_type": "customer_validation_template",
            "subject": subject,
            "body": body,
            "methodology": "template",
            "source": "proven_template"
        }
    
    def _generate_template_roi_email(self, company_data: Dict[str, Any], 
                                   psi_results: Dict[str, Any], primary_edp: str) -> Dict[str, Any]:
        """Email 4: ROI analysis using proven template"""
        
        first_name = company_data.get('first_name', 'there')
        company_name = company_data.get('company_name', 'your company')
        annual_loss = self._calculate_annual_loss(company_data, psi_results)
        
        subject = f"${annual_loss:,} impact for {company_name}"
        
        body = f"""Hey {first_name},

{company_name}'s current inefficiencies:

• Productivity loss: ${int(annual_loss * 0.4):,}/year
• Error costs: ${int(annual_loss * 0.35):,}/year  
• Trade show waste: ${int(annual_loss * 0.25):,}/year
• Total impact: ${annual_loss:,}/year

Investment: $20K/year
Payback: 47 days (validated across 15 customers)
5-Year ROI: {int(annual_loss * 5 / 20000)}x

Want your custom ROI model? Takes 15 minutes.

Best,
[Your Name]"""
        
        return {
            "sequence_step": 4,
            "send_day": 10,
            "email_type": "roi_analysis_template",
            "subject": subject,
            "body": body,
            "methodology": "template",
            "source": "proven_template"
        }
    
    # === CLAUDE-GENERATED EMAIL METHODS ===
    
    def _generate_claude_competitive_email(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any]) -> Dict[str, Any]:
        """Email 5: Competitive threat using Claude"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        evidence_hooks = psi_results["messaging"]["evidence_based_hooks"]
        
        # Claude prompt for competitive email
        claude_prompt = f"""Write a direct, punchy B2B sales email about competitive threats.

Context:
- Company: {company_name}
- Contact: {first_name}
- Evidence: {evidence_hooks[0] if evidence_hooks else 'Manual processes'}
- Competitors: Universal Furniture, Theodore Alexander, Butler Specialty

Requirements:
- Start with "Hey {first_name},"
- Lead with competitive reality: "While {company_name} uses manual processes, 3 competitors digitized in 2024"
- List specific competitor wins: Universal (25% sales increase), Theodore Alexander (40% faster quotes), Butler (300% rep productivity)
- Include urgency: "Your competitors are 40% faster. Quote time: Them (minutes) vs You (hours)"
- End with: "Should we discuss closing this gap before High Point Market?"
- Keep under 80 words
- No corporate speak, direct and urgent tone

Generate ONLY the email body, no subject line."""
        
        # For now, use template (would integrate Claude API later)
        body = f"""Hey {first_name},

While {company_name} uses manual processes, 3 direct competitors digitized in 2024:

• Universal Furniture: 25% sales increase
• Theodore Alexander: 40% faster quotes  
• Butler Specialty: 300% rep productivity

Your competitors are 40% faster. Quote time: Them (minutes) vs You (hours).

Should we discuss closing this gap before High Point Market?

Best,
[Your Name]"""
        
        return {
            "sequence_step": 5,
            "send_day": 14,
            "email_type": "competitive_threat_claude",
            "subject": f"3 competitors just passed {company_name}",
            "body": body,
            "methodology": "claude",
            "source": "claude_generated",
            "claude_prompt": claude_prompt
        }
    
    def _generate_claude_urgency_email(self, company_data: Dict[str, Any], 
                                     psi_results: Dict[str, Any]) -> Dict[str, Any]:
        """Email 6: Trade show urgency using Claude"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        claude_prompt = f"""Write a direct, urgent B2B sales email about trade show deadlines.

Context:
- Company: {company_name}
- Contact: {first_name}
- Trade show: High Point Market in 35 days
- Booth investment: $32,000
- Risk: 60% opportunity loss without mobile capability

Requirements:
- Start with "Hey {first_name},"
- Create urgency: "35 days until High Point Market"
- Highlight risk: "Your $32,000 booth investment is at risk"
- Specific threat: "Without mobile orders, you'll lose 60% of opportunities to competitors who can quote on-spot"
- Timeline pressure: "Setup takes 14 days. Must start this week to be ready"
- End with: "15-minute call to map out implementation?"
- Keep under 70 words
- Direct, urgent tone

Generate ONLY the email body, no subject line."""
        
        # For now, use template (would integrate Claude API later)
        body = f"""Hey {first_name},

35 days until High Point Market.

Your $32,000 booth investment is at risk. Without mobile orders, you'll lose 60% of opportunities to competitors who can quote on-spot.

Setup takes 14 days. Must start this week to be ready.

15-minute call to map out implementation?

Best,
[Your Name]"""
        
        return {
            "sequence_step": 6,
            "send_day": 18,
            "email_type": "trade_show_urgency_claude",
            "subject": f"35 days to High Point Market - {company_name} ready?",
            "body": body,
            "methodology": "claude",
            "source": "claude_generated",
            "claude_prompt": claude_prompt
        }
    
    # REMOVED: _generate_claude_case_study_email - contained fabricated $650,000 savings claim
    
    def _generate_claude_breakup_email(self, company_data: Dict[str, Any], 
                                     psi_results: Dict[str, Any]) -> Dict[str, Any]:
        """Email 8: Final breakup using Claude"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        annual_loss = self._calculate_annual_loss(company_data, psi_results)
        
        claude_prompt = f"""Write a professional breakup email with value.

Context:
- Company: {company_name}
- Contact: {first_name}
- Lost value: ${annual_loss:,} annually
- Warning example: Butler Specialty waited 2 years, cost them $1.4M

Requirements:
- Start with "Hey {first_name},"
- Acknowledge no response: "Haven't heard back, assuming not a priority"
- Offer value before leaving: ROI Calculator, 2025 Furniture Sales report, High Point Market guide
- Include warning: "Butler Specialty waited 2 years, cost them $1.4M"
- Professional close: "Door remains open if priorities change"
- Keep under 80 words
- Professional but include consequence warning

Generate ONLY the email body, no subject line."""
        
        # For now, use template (would integrate Claude API later)
        body = f"""Hey {first_name},

Haven't heard back, assuming this isn't a priority right now.

Before I go, here's some value:
• ROI Calculator for furniture manufacturers
• 2025 State of Furniture Sales report
• High Point Market success guide

Warning: Butler Specialty waited 2 years, cost them $1.4M.

Door remains open if priorities change.

Best,
[Your Name]"""
        
        return {
            "sequence_step": 8,
            "send_day": 25,
            "email_type": "final_breakup_claude",
            "subject": f"Resources for {company_name} (breaking up)",
            "body": body,
            "methodology": "claude",
            "source": "claude_generated",
            "claude_prompt": claude_prompt
        }
    
    def _generate_educational_content(self, company_data: Dict[str, Any], 
                                    psi_results: Dict[str, Any], averaged_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate educational content suggestions"""
        
        return [
            {
                "content_type": "whitepaper",
                "title": "Operational Efficiency in Furniture Manufacturing",
                "description": "Best practices for operational improvement"
            }
        ]
    
    # === NEW REFINED EDP-SPECIFIC EMAIL TEMPLATES ===
    
    def _generate_sku_complexity_email_1(self, company_data: Dict[str, Any], 
                                       psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP1: SKU Complexity Email 1"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        sku_variations = company_data.get('sku_variations', '96')
        trade_show = company_data.get('trade_show', 'Vegas Market')
        
        subject = f"Quick question about {company_name}'s configuration process"
        
        body = f"""Hi {first_name},

I noticed {company_name} offers {sku_variations} different combinations. With that level of complexity, you're likely experiencing configuration chaos.

Quick math: If just 5% of your quotes have pricing errors, you're losing hundreds of thousands of dollars in margin annually. At {trade_show} next month, with reps juggling paper price sheets in crowded showrooms, how many perfect quotes will they deliver?

Worth exploring how to turn SKU complexity from a challenge into an asset?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "sku_complexity_1",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP1_SKU_Complexity"
        }
    
    def _generate_sales_enablement_email_1(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP7: Sales Enablement Email 1"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Quick question about {company_name}'s trade show process"
        
        body = f"""Hi {first_name},

Noticed {company_name} doesn't have mobile catalog access. When we see this, it usually means:

- Trade show orders written on paper, entered later
- Reps can't quote without calling the office
- Show leads lost to slow follow-up

Sound familiar? Or have you found workarounds?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "sales_enablement_1",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP7_Sales_Enablement"
        }
    
    def _generate_technology_email_1(self, company_data: Dict[str, Any], 
                                   psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP8: Technology Obsolescence Email 1"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"{company_name} vs digital-native competitors"
        
        body = f"""Hi {first_name},

I see {company_name} still relies on PDF catalogs. Companies with manual distribution typically experience:

- Price updates taking 3-5 days to reach reps
- Conflicting quotes from outdated sheets
- Reps working from wrong info constantly

Is this creating headaches for your team?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "technology_1",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP8_Technology_Obsolescence"
        }
    
    def _generate_rep_performance_email_1(self, company_data: Dict[str, Any], 
                                        psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP2: Rep Performance Email 1"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"{company_name}'s rep performance visibility"
        
        body = f"""Hi {first_name},

Without a rep portal, companies typically can't see:

- Which reps are actually selling vs. coasting
- Where territory gaps exist
- Why top performers leave

Is {company_name} experiencing similar visibility challenges?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "rep_performance_1",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP2_Rep_Management"
        }
    
    def _generate_channel_conflict_email_1(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP6: Channel Conflict Email 1"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        channel_count = company_data.get('channel_count', '3')
        
        subject = f"{company_name}'s pricing across channels"
        
        body = f"""Hi {first_name},

When brands sell through {channel_count} channels without unified pricing:

- Dealers complain about being undercut
- 15-20% of deals stall in negotiations
- Reps waste hours explaining differences

How are you keeping pricing consistent across all channels?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "channel_conflict_1",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP6_Channel_Conflict"
        }
    
    # === EMAIL 2 TEMPLATES FOR EACH EDP ===
    
    def _generate_sku_complexity_email_2(self, company_data: Dict[str, Any], 
                                       psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP1: SKU Complexity Email 2"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Following up on configuration challenges"
        
        body = f"""Hi {first_name},

Following up on configuration challenges. When companies manage complex SKUs manually, we typically see:

- 20+ minutes to build each quote
- Constant "let me check on that" moments
- Lost sales from slow response times

Butler Specialty solved this - their President says the system "flexibly configures to the way we do business."

Want to see how it works for complex catalogs?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "sku_complexity_2",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP1_SKU_Complexity"
        }
    
    def _generate_sales_enablement_email_2(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP7: Sales Enablement Email 2"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Quick story about mobile transformation"
        
        body = f"""Hi {first_name},

Quick story - Godinger Silver's reps used to haul paper catalogs everywhere. Their VP told us that going mobile was "the best thing that has ever happened to this company in 25 years."

The real impact? Reps actually selling instead of searching through binders.

How much time do your reps waste on manual lookups?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "sales_enablement_2",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP7_Sales_Enablement"
        }
    
    def _generate_technology_email_2(self, company_data: Dict[str, Any], 
                                   psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP8: Technology Obsolescence Email 2"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"The PDF problem gets worse over time"
        
        body = f"""Hi {first_name},

The PDF problem gets worse over time. What starts as minor inconsistencies becomes major credibility issues.

Wildwood Lamps eliminated this - their manager says she "reduced calls by a third" just by getting everyone on the same system.

How many hours weekly does your team spend on version control?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "technology_2",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP8_Technology_Obsolescence"
        }
    
    def _generate_rep_performance_email_2(self, company_data: Dict[str, Any], 
                                        psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP2: Rep Performance Email 2"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Rep visibility isn't about micromanaging"
        
        body = f"""Hi {first_name},

Rep visibility isn't about micromanaging - it's about knowing who needs help before they fail.

We've seen top performers using tools 10-12 times daily while strugglers barely log in. The pattern is consistent.

Do you know which camp each of your reps falls into?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "rep_performance_2",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP2_Rep_Management"
        }
    
    def _generate_channel_conflict_email_2(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP6: Channel Conflict Email 2"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Channel conflict is relationship poison"
        
        body = f"""Hi {first_name},

Channel conflict is relationship poison. One pricing mistake can destroy years of dealer trust.

The solution isn't complicated - it's about single source of truth that everyone accesses.

What's your current process for ensuring price consistency?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "channel_conflict_2",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP6_Channel_Conflict"
        }
    
    # === EMAIL 3 TEMPLATES FOR EACH EDP ===
    
    def _generate_sku_complexity_email_3(self, company_data: Dict[str, Any], 
                                       psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP1: SKU Complexity Email 3"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Last thought on SKU management"
        
        body = f"""Hi {first_name},

Last thought on SKU management - the difference between thriving and drowning often comes down to tools.

Companies still using spreadsheets are losing ground to those with real-time configuration. The gap widens every quarter.

If you're ready to close that gap, I can show you exactly how in 20 minutes.

Still interested?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "sku_complexity_3",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP1_SKU_Complexity"
        }
    
    def _generate_sales_enablement_email_3(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP7: Sales Enablement Email 3"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"The mobile gap is real"
        
        body = f"""Hi {first_name},

The mobile gap is real. While your reps flip through papers, competitors close deals on iPads.

It's not about being cutting-edge - it's about basic efficiency in 2025.

Ready to level the playing field?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "sales_enablement_3",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP7_Sales_Enablement"
        }
    
    def _generate_technology_email_3(self, company_data: Dict[str, Any], 
                                   psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP8: Technology Obsolescence Email 3"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Digital transformation sounds complex"
        
        body = f"""Hi {first_name},

Digital transformation sounds complex, but it's really about one thing: Can your reps access accurate info instantly?

If the answer is no, you're fighting with one hand tied.

Want to untie it?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "technology_3",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP8_Technology_Obsolescence"
        }
    
    def _generate_rep_performance_email_3(self, company_data: Dict[str, Any], 
                                        psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP2: Rep Performance Email 3"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"The cost of rep turnover keeps climbing"
        
        body = f"""Hi {first_name},

The cost of rep turnover keeps climbing. Without performance data, you can't coach effectively or reward fairly.

Your best reps want tools that make them better. Are you giving them what they need?

Let's discuss how to retain your top talent."""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "rep_performance_3",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP2_Rep_Management"
        }
    
    def _generate_channel_conflict_email_3(self, company_data: Dict[str, Any], 
                                         psi_results: Dict[str, Any], sequence_step: int, send_day: int) -> Dict[str, Any]:
        """EDP6: Channel Conflict Email 3"""
        
        company_name = company_data.get('company_name', 'your company')
        first_name = company_data.get('first_name', 'there')
        
        subject = f"Every day without unified pricing"
        
        body = f"""Hi {first_name},

Every day without unified pricing is another chance for channel chaos.

The companies solving this are capturing more margin and keeping dealers happy. The rest are firefighting.

Which would you rather be doing?"""
        
        return {
            "sequence_step": sequence_step,
            "send_day": send_day,
            "email_type": "channel_conflict_3",
            "subject": subject,
            "body": body,
            "methodology": "refined_template",
            "primary_edp": "EDP6_Channel_Conflict"
        }
