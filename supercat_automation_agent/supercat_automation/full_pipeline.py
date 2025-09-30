#!/usr/bin/env python3
"""
SuperCat Integrated Pipeline - Combines full_pipeline.py with website_evidence.py
Uses your existing WebsiteEvidenceExtractor for detailed analysis
"""

import pandas as pd
import json
import os
import re
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import asyncio
import aiohttp
import logging
import sys

# Add scrapers to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scrapers'))

# Import your existing website evidence extractor
try:
    from scrapers.website_evidence import WebsiteEvidenceExtractor
    HAS_EVIDENCE_EXTRACTOR = True
except ImportError as e:
    print(f"Import error: {e}")
    HAS_EVIDENCE_EXTRACTOR = False

# Import webhook generator
try:
    from generate_webhooks import SuperCatWebhookProcessor
    HAS_WEBHOOK_GENERATOR = True
except ImportError as e:
    print(f"Webhook generator import error: {e}")
    HAS_WEBHOOK_GENERATOR = False

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4-turbo')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
CLAY_WEBHOOK_URL = os.getenv('CLAY_WEBHOOK_URL')

# Initialize AI clients
try:
    from openai import OpenAI
    openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
    OPENAI_VERSION = "new"
except ImportError:
    import openai
    openai.api_key = OPENAI_API_KEY
    openai_client = None
    OPENAI_VERSION = "old"

# Initialize Anthropic client
anthropic_client = None
try:
    import anthropic
    anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None
except ImportError:
    pass

# Supabase
try:
    from supabase import create_client, Client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL else None
except:
    supabase = None

print(f"✅ Environment loaded:")
print(f"  • OpenAI: {OPENAI_VERSION} version - {'Connected' if OPENAI_API_KEY else 'Not configured'}")
print(f"  • Anthropic: {'Connected' if anthropic_client else 'Not configured'}")
print(f"  • Supabase: {'Connected' if supabase else 'Not configured'}")
print(f"  • Clay Webhook: {'Connected' if CLAY_WEBHOOK_URL else 'Not configured'}")
print(f"  • Evidence Extractor: {'Available' if HAS_EVIDENCE_EXTRACTOR else 'Using basic mode'}")
print(f"  • Webhook Generator: {'Available' if HAS_WEBHOOK_GENERATOR else 'Not available'}")


class IntegratedPipelineProcessor:
    """Enhanced pipeline using WebsiteEvidenceExtractor for detailed analysis"""
    
    def __init__(self):
        self.session = None
        self.clay_webhook_url = CLAY_WEBHOOK_URL
        
        # Initialize the evidence extractor if available
        if HAS_EVIDENCE_EXTRACTOR:
            self.evidence_extractor = WebsiteEvidenceExtractor()
        else:
            self.evidence_extractor = None
            
        # Initialize webhook generator for campaigns
        if HAS_WEBHOOK_GENERATOR:
            self.webhook_generator = SuperCatWebhookProcessor(webhook_type="campaign")
        else:
            self.webhook_generator = None
        
        self.stats = {
            'processed': 0,
            'qualified': 0,
            'sent_to_clay': 0,
            'saved_to_supabase': 0,
            'errors': []
        }
        
        self.edp_weights = {
            'sales_enablement_collapse': 1.0,
            'technology_obsolescence': 0.93,
            'rep_performance_crisis': 0.71,
            'sku_complexity': 0.64,
            'channel_conflict': 0.43
        }
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
    
    def analyze_website_enhanced(self, domain: str) -> Dict:
        """
        Use WebsiteEvidenceExtractor for detailed analysis
        Falls back to basic analysis if not available
        """
        
        if self.evidence_extractor:
            # Use your sophisticated extractor
            print(f"  🔍 Using enhanced evidence extraction...")
            return self.evidence_extractor.analyze_website(domain)
        else:
            # Fallback to basic analysis
            return self.analyze_website_basic(domain)
    
    async def analyze_website_basic(self, domain: str) -> Dict:
        """Basic fallback analysis (your original method)"""
        
        if not domain.startswith('http'):
            domain = f"https://{domain}"
        
        analysis = {
            'domain': domain,
            'evidence': [],
            'tech_stack': []
        }
        
        try:
            async with self.session.get(domain, timeout=10, ssl=False) as response:
                html = await response.text()
                html_lower = html.lower()
                
                # Your original basic checks
                if 'product search' not in html_lower:
                    analysis['evidence'].append("No product search functionality")
                if '.pdf' in html_lower and 'catalog' in html_lower:
                    analysis['evidence'].append("PDF-only catalogs detected")
                if 'dealer login' in html_lower or 'rep login' in html_lower:
                    analysis['evidence'].append("Manual dealer/rep login system")
                if 'request quote' in html_lower:
                    analysis['evidence'].append("Manual quote request process")
                
                if not response.url.scheme == 'https':
                    analysis['evidence'].append("No SSL certificate")
                if 'wordpress' in html_lower:
                    analysis['tech_stack'].append("WordPress")
                    
        except Exception as e:
            analysis['error'] = str(e)
            logger.error(f"Scraping error for {domain}: {e}")
        
        return analysis
    
    def process_enhanced_evidence(self, evidence_data: Dict) -> Dict:
        """
        Process the enhanced evidence from WebsiteEvidenceExtractor
        into format needed for GPT and Clay
        """
        
        processed = {
            'edp_scores': {},
            'primary_edp': None,
            'psi_score': 0,
            'qualification_tier': 'NOT_QUALIFIED',
            'key_evidence': [],
            'detailed_evidence': {}
        }
        
        # Extract EDP scores
        if 'edp_evidence' in evidence_data:
            for edp_name, evidence in evidence_data['edp_evidence'].items():
                processed['edp_scores'][edp_name] = evidence.get('score', 0)
                
                # Collect specific issues as evidence
                if evidence.get('specific_issues'):
                    processed['key_evidence'].extend(evidence['specific_issues'][:2])
                
                # Store detailed evidence for Clay
                processed['detailed_evidence'][edp_name] = {
                    'score': evidence.get('score', 0),
                    'indicators': evidence.get('indicators_found', []),
                    'issues': evidence.get('specific_issues', []),
                    'strength': evidence.get('evidence_strength', 'none')
                }
        
        # Use TAM indicators if available
        if 'tam_indicators' in evidence_data:
            tam = evidence_data['tam_indicators']
            processed['primary_edp'] = tam.get('primary_edp', 'unknown')
            processed['psi_score'] = tam.get('total_pain_score', 0) * 100 / 3  # Normalize to 0-100
            
            # Map tier
            tier_map = {
                'TIER_1_HOT': 'TIER_1_IMMEDIATE',
                'TIER_2_WARM': 'TIER_2_ACTIVE', 
                'TIER_3_COOL': 'TIER_3_NURTURE',
                'TIER_4_COLD': 'NOT_QUALIFIED'
            }
            processed['qualification_tier'] = tier_map.get(tam.get('tier', 'TIER_4_COLD'), 'NOT_QUALIFIED')
        
        # Add personalization hooks
        if 'personalization_hooks' in evidence_data:
            processed['personalization_data'] = evidence_data['personalization_hooks']
        
        # Calculate urgency based on tier and PSI score
        if processed['qualification_tier'] == 'TIER_1_IMMEDIATE':
            processed['urgency'] = "high"
        elif processed['qualification_tier'] == 'TIER_2_ACTIVE' and processed['psi_score'] > 40:
            processed['urgency'] = "medium"
        elif processed['qualification_tier'] == 'TIER_2_ACTIVE':
            processed['urgency'] = "low"
        else:
            processed['urgency'] = "none"
        
        # Limit key evidence to top 5
        processed['key_evidence'] = processed['key_evidence'][:5]
        
        return processed
    
    def gpt_analysis_enhanced(self, company_data: Dict, website_analysis: Dict) -> Dict:
        """
        Enhanced GPT analysis using detailed evidence
        """
        
        if not OPENAI_API_KEY:
            # If no GPT, use the processed evidence directly
            return website_analysis
        
        # Build a more detailed prompt with specific evidence
        evidence_summary = []
        if 'detailed_evidence' in website_analysis:
            for edp, details in website_analysis['detailed_evidence'].items():
                if details['issues']:
                    evidence_summary.append(f"{edp}: {', '.join(details['issues'][:2])}")
        
        prompt = f"""
        Analyze this furniture/lighting company based on detailed website evidence.
        
        Company: {company_data['company_name']}
        Domain: {company_data['domain']}
        
        Evidence Found:
        {json.dumps(evidence_summary, indent=2)}
        
        EDP Scores (0-1 scale):
        {json.dumps(website_analysis.get('edp_scores', {}), indent=2)}
        
        Current Assessment:
        - Primary EDP: {website_analysis.get('primary_edp')}
        - PSI Score: {website_analysis.get('psi_score', 0):.1f}%
        - Suggested Tier: {website_analysis.get('qualification_tier')}
        
        Please validate and enhance this analysis. Return JSON with:
        1. validated_edp_scores: Adjusted scores based on evidence
        2. confirmed_primary_edp: Most critical pain point
        3. final_psi_score: Overall pain score (0-100)
        4. final_tier: TIER_1_IMMEDIATE, TIER_2_ACTIVE, TIER_3_NURTURE, or NOT_QUALIFIED
        5. messaging_hooks: Top 3 specific pain points to mention in outreach
        6. personalization_elements: Specific details to reference (trade shows, product categories, etc.)
        
        Focus on accuracy - only confirm pain points with strong evidence.
        """
        
        try:
            content = None
            
            # Try OpenAI first
            try:
                if OPENAI_VERSION == "new" and openai_client:
                    response = openai_client.chat.completions.create(
                        model=OPENAI_MODEL,
                        messages=[
                            {"role": "system", "content": "You are a B2B sales expert analyzing furniture/lighting companies. Be precise and evidence-based."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.3
                    )
                    content = response.choices[0].message.content
                else:
                    import openai
                    response = openai.ChatCompletion.create(
                        model=OPENAI_MODEL,
                        messages=[
                            {"role": "system", "content": "You are a B2B sales expert analyzing furniture/lighting companies. Be precise and evidence-based."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.3
                    )
                    content = response.choices[0].message.content
                    
                logger.info("Used OpenAI for analysis enhancement")
                
            except Exception as openai_error:
                logger.warning(f"OpenAI failed: {openai_error}")
                
                # Fallback to Anthropic if OpenAI fails
                if anthropic_client:
                    try:
                        response = anthropic_client.messages.create(
                            model="claude-3-haiku-20240307",
                            max_tokens=2000,
                            temperature=0.3,
                            system="You are a B2B sales expert analyzing furniture/lighting companies. Be precise and evidence-based.",
                            messages=[
                                {"role": "user", "content": prompt}
                            ]
                        )
                        content = response.content[0].text
                        logger.info("Used Anthropic Claude as fallback for analysis enhancement")
                    except Exception as anthropic_error:
                        logger.error(f"Anthropic fallback also failed: {anthropic_error}")
                        raise openai_error  # Re-raise original error if both fail
                else:
                    logger.error("No Anthropic client available for fallback")
                    raise openai_error
            
            # Parse GPT response
            gpt_result = json.loads(content)
            
            # Merge with existing analysis
            website_analysis['edp_scores'] = gpt_result.get('validated_edp_scores', website_analysis['edp_scores'])
            website_analysis['primary_edp'] = gpt_result.get('confirmed_primary_edp', website_analysis['primary_edp'])
            website_analysis['psi_score'] = gpt_result.get('final_psi_score', website_analysis['psi_score'])
            website_analysis['qualification_tier'] = gpt_result.get('final_tier', website_analysis['qualification_tier'])
            website_analysis['messaging_hooks'] = gpt_result.get('messaging_hooks', website_analysis.get('key_evidence', []))
            website_analysis['personalization_elements'] = gpt_result.get('personalization_elements', [])
            
            # Recalculate urgency after GPT updates
            if website_analysis['qualification_tier'] == 'TIER_1_IMMEDIATE':
                website_analysis['urgency'] = "high"
            elif website_analysis['qualification_tier'] == 'TIER_2_ACTIVE' and website_analysis['psi_score'] > 40:
                website_analysis['urgency'] = "medium"
            elif website_analysis['qualification_tier'] == 'TIER_2_ACTIVE':
                website_analysis['urgency'] = "low"
            else:
                website_analysis['urgency'] = "none"
            
        except Exception as e:
            logger.error(f"GPT enhancement error: {e}")
            # Keep original analysis if GPT fails
        
        return website_analysis
    
    async def save_to_supabase_enhanced(self, company_data: Dict, analysis: Dict):
        """Save enhanced data to Supabase - FIXED"""
        
        if not supabase:
            return
        
        try:
            # Build record with proper data types
            record = {
                'company_name': str(company_data.get('company_name', '')),
                'domain': str(company_data.get('domain', '')),
                'qualification_tier': str(analysis.get('qualification_tier', '')),
                'primary_edp': str(analysis.get('primary_edp', ''))
            }
            
            # Add optional fields with proper types
            if company_data.get('email'):
                record['email'] = str(company_data['email'])
            if company_data.get('first_name'):
                record['first_name'] = str(company_data['first_name'])
            if company_data.get('last_name'):
                record['last_name'] = str(company_data['last_name'])
            
            # Handle psi_score as float if column exists
            if analysis.get('psi_score') is not None:
                try:
                    record['psi_score'] = float(analysis['psi_score'])
                except:
                    pass
            
            # Don't send complex objects - convert to JSON strings if needed
            # Skip edp_scores and key_evidence for now unless columns exist
            
            result = supabase.table('companies').insert(record).execute()
            self.stats['saved_to_supabase'] += 1
            print(f"  💾 Saved to Supabase")
            
        except Exception as e:
            logger.warning(f"Supabase save error (non-critical): {e}")
    
    async def send_to_clay_enhanced(self, company_data: Dict, analysis: Dict):
        """Send enhanced data with campaign content to Clay webhook"""
        
        if not self.clay_webhook_url:
            return
        
        try:
            # Clean the data - remove None values and ensure JSON serializable
            def clean_for_json(obj):
                if isinstance(obj, dict):
                    return {k: clean_for_json(v) for k, v in obj.items() if v is not None}
                elif isinstance(obj, list):
                    return [clean_for_json(item) for item in obj if item is not None]
                elif isinstance(obj, (str, int, float, bool)):
                    return obj
                else:
                    return str(obj)
            
            # Generate campaign content using webhook generator
            campaign_data = None
            if self.webhook_generator:
                # Add required fields for webhook generator
                analysis_for_webhook = analysis.copy()
                analysis_for_webhook['tier'] = analysis.get('qualification_tier', 'NOT_QUALIFIED')
                analysis_for_webhook['evidence'] = analysis.get('key_evidence', [])
                
                try:
                    campaign_data = self.webhook_generator.generate_campaign_webhook(
                        company_data, analysis_for_webhook
                    )
                except Exception as e:
                    logger.error(f"Campaign generation error: {e}")
            
            # Build comprehensive webhook payload
            webhook_payload = {
                'company_name': company_data.get('company_name', ''),
                'domain': company_data.get('domain', ''),
                'tam_tier': analysis.get('qualification_tier', ''),
                'psi_score': float(analysis.get('psi_score', 0)),  # Ensure float
                'primary_edp': analysis.get('primary_edp', 'unknown'),
                'edp_scores': clean_for_json(analysis.get('edp_scores', {})),
                'key_evidence': analysis.get('key_evidence', [])[:5],  # Limit to 5
                'contact_info': {
                    'first_name': str(company_data.get('first_name', '')),
                    'last_name': str(company_data.get('last_name', '')),
                    'email': str(company_data.get('email', '')),
                    'title': str(company_data.get('title', ''))
                }
            }
            
            # Add campaign data if generated successfully
            if campaign_data:
                webhook_payload['email_sequence'] = campaign_data.get('email_sequence', [])
                webhook_payload['linkedin_sequence'] = campaign_data.get('linkedin_sequence', [])
                webhook_payload['ad_sequence'] = campaign_data.get('ad_sequence', [])
                webhook_payload['campaign_timeline'] = campaign_data.get('campaign_timeline', {})
            
            # Ensure valid JSON
            json_payload = json.dumps(webhook_payload)
            
            async with self.session.post(
                self.clay_webhook_url,
                data=json_payload,  # Use data instead of json
                headers={'Content-Type': 'application/json'}
            ) as response:
                if response.status in [200, 201, 202]:
                    self.stats['sent_to_clay'] += 1
                    if campaign_data:
                        print(f"  ✅ Sent to Clay webhook (with emails, LinkedIn, ads)")
                    else:
                        print(f"  ✅ Sent to Clay webhook (analysis only)")
                else:
                    error_text = await response.text()
                    logger.error(f"Clay webhook failed: {response.status} - {error_text}")
                    
        except Exception as e:
            logger.error(f"Clay send error: {e}")
    
    async def process_company(self, company_data: Dict):
        """Process single company with enhanced extraction"""
        
        company_name = company_data['company_name']
        print(f"\n🏢 Processing: {company_name}")
        
        # Step 1: Enhanced website analysis
        print(f"  🔍 Analyzing website with enhanced extraction...")
        
        if self.evidence_extractor:
            # Use synchronous method (not async)
            website_analysis = self.analyze_website_enhanced(company_data['domain'])
            # Process the enhanced evidence
            analysis = self.process_enhanced_evidence(website_analysis)
        else:
            # Use async basic method
            website_analysis = await self.analyze_website_basic(company_data['domain'])
            # Convert basic to standard format
            analysis = self.rule_based_analysis(website_analysis)
        
        # Step 2: GPT enhancement (optional)
        if OPENAI_API_KEY:
            print(f"  🤖 Enhancing with GPT analysis...")
            analysis = self.gpt_analysis_enhanced(company_data, analysis)
        
        # Display results
        print(f"  📊 Tier: {analysis['qualification_tier']}")
        print(f"  📈 PSI Score: {analysis.get('psi_score', 0):.1f}%")
        print(f"  🎯 Primary EDP: {analysis.get('primary_edp', 'unknown')}")
        
        if analysis.get('key_evidence'):
            print(f"  📝 Key Evidence:")
            for evidence in analysis['key_evidence'][:3]:
                print(f"     • {evidence}")
        
        self.stats['processed'] += 1
        
        # Step 3: Save and send if qualified
        if analysis['qualification_tier'] != "NOT_QUALIFIED":
            self.stats['qualified'] += 1
            
            # Save to Supabase
            await self.save_to_supabase_enhanced(company_data, analysis)
            
            # Send comprehensive data to Clay (includes analysis + campaigns)
            await self.send_to_clay_enhanced(company_data, analysis)
            
            return {
                'company': company_name,
                'analysis': analysis,
                'status': 'qualified'
            }
        
        return {
            'company': company_name,
            'analysis': analysis,
            'status': 'not_qualified'
        }
    
    def rule_based_analysis(self, website_analysis: Dict) -> Dict:
        """Fallback analysis for basic extraction"""
        
        evidence = website_analysis.get('evidence', [])
        evidence_str = ' '.join(evidence).lower()
        
        edp_scores = {}
        
        # Sales Enablement
        score = 0
        if "no product search" in evidence_str:
            score += 0.3
        if "pdf" in evidence_str and "catalog" in evidence_str:
            score += 0.3
        if "login" in evidence_str:
            score += 0.2
        if "quote" in evidence_str:
            score += 0.2
        edp_scores['sales_enablement_collapse'] = min(score, 1.0)
        
        # Technology
        score = 0
        if "no ssl" in evidence_str:
            score += 0.4
        if "wordpress" in ' '.join(website_analysis.get('tech_stack', [])).lower():
            score += 0.3
        edp_scores['technology_obsolescence'] = min(score, 1.0)
        
        # Other EDPs (basic scores)
        edp_scores['rep_performance_crisis'] = 0.5 if "dealer" in evidence_str or "rep" in evidence_str else 0.3
        edp_scores['sku_complexity'] = 0.4
        edp_scores['channel_conflict'] = 0.3
        
        # Calculate PSI
        psi_score = sum(score * self.edp_weights[edp] for edp, score in edp_scores.items()) / sum(self.edp_weights.values())
        psi_percentage = psi_score * 100
        
        # Determine tier
        if psi_percentage >= 50:
            tier = "TIER_1_IMMEDIATE"
        elif psi_percentage >= 35:
            tier = "TIER_2_ACTIVE"
        elif psi_percentage >= 25:
            tier = "TIER_3_NURTURE"
        else:
            tier = "NOT_QUALIFIED"
        
        # Primary EDP
        primary_edp = max(edp_scores.items(), key=lambda x: x[1] * self.edp_weights[x[0]])[0]
        
        return {
            'edp_scores': edp_scores,
            'primary_edp': primary_edp,
            'psi_score': psi_percentage,
            'qualification_tier': tier,
            'key_evidence': evidence[:3]
        }
    
    async def process_csv(self, csv_path: str):
        """Process CSV file with enhanced extraction"""
        
        print(f"\n{'='*60}")
        print(f"SUPERCAT ENHANCED PIPELINE")
        print(f"{'='*60}\n")
        
        # Read CSV
        df = pd.read_csv(csv_path)
        df = df.dropna(subset=['company_name', 'domain'])
        
        print(f"📊 Processing {len(df)} companies")
        print(f"🔧 Using: {'Enhanced WebsiteEvidenceExtractor' if self.evidence_extractor else 'Basic extraction'}\n")
        
        # Process each company
        results = []
        async with self:
            for idx, row in df.iterrows():
                company_data = row.to_dict()
                result = await self.process_company(company_data)
                results.append(result)
                
                # Rate limiting
                await asyncio.sleep(2 if self.evidence_extractor else 1)
        
        # Summary
        print(f"\n{'='*60}")
        print(f"PROCESSING COMPLETE")
        print(f"{'='*60}")
        print(f"📊 Total Processed: {self.stats['processed']}")
        print(f"✅ Qualified: {self.stats['qualified']} ({self.stats['qualified']/max(self.stats['processed'],1)*100:.1f}%)")
        print(f"🚀 Sent to Clay: {self.stats['sent_to_clay']}")
        print(f"💾 Saved to Supabase: {self.stats['saved_to_supabase']}")
        
        if self.stats['errors']:
            print(f"⚠️ Errors: {len(self.stats['errors'])}")
        
        # Save results
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        results_file = f"results_enhanced_{timestamp}.json"
        
        with open(results_file, 'w') as f:
            json.dump({
                'stats': self.stats,
                'results': results,
                'timestamp': timestamp,
                'using_enhanced': bool(self.evidence_extractor)
            }, f, indent=2)
        
        print(f"\n📁 Results saved: {results_file}")
        
        # Save qualified companies to CSV
        qualified = [r for r in results if r['status'] == 'qualified']
        if qualified:
            qualified_df = pd.DataFrame([{
                'company': r['company'],
                'tier': r['analysis']['qualification_tier'],
                'psi_score': r['analysis'].get('psi_score', 0),
                'primary_edp': r['analysis'].get('primary_edp', ''),
                'evidence': ', '.join(r['analysis'].get('key_evidence', [])[:2])
            } for r in qualified])
            
            qualified_file = f"qualified_{timestamp}.csv"
            qualified_df.to_csv(qualified_file, index=False)
            print(f"📁 Qualified companies: {qualified_file}")
        
        return results


async def main():
    """Main execution"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python integrated_pipeline.py prospects.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    
    if not Path(csv_file).exists():
        print(f"❌ File not found: {csv_file}")
        sys.exit(1)
    
    processor = IntegratedPipelineProcessor()
    await processor.process_csv(csv_file)


if __name__ == "__main__":
    asyncio.run(main())