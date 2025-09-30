#!/usr/bin/env python3
"""
Simple webhook sample generator - runs pipeline logic directly
"""

import sys
import os
import json
from datetime import datetime

# Add current directory to path
sys.path.insert(0, '/Users/ryanburt/supercat_automation_agent/supercat_automation')

def generate_webhook_samples():
    """Generate real webhook samples using the campaign generator"""
    
    try:
        # Import after path setup
        from orchestration.clay_webhook import CompleteClayWebhookOrchestrator
        
        print("🎯 Generating webhook samples...")
        
        # Create realistic test companies
        test_companies = [
            {
                'company_name': '9to5 Seating',
                'domain': '9to5seating.com',
                'primary_edp': 'rep_performance_crisis',
                'catalog_sku_count': 850,
                'tam_tier': 'TIER_2_ACTIVE',
                'psi_score': 42.3,
                'key_evidence': [
                    'No dealer/rep portal detected',
                    'No modern web framework detected'
                ],
                'decision_makers': [
                    {
                        'id': 'dm_001',
                        'name': 'Ed Lachman',
                        'title': 'Chief Operating Officer',
                        'email': 'ed.lachman@9to5seating.com'
                    }
                ]
            },
            {
                'company_name': 'Abbott Collection',
                'domain': 'abbottcollection.com', 
                'primary_edp': 'sku_complexity',
                'catalog_sku_count': 3200,
                'tam_tier': 'TIER_1_PRIME',
                'psi_score': 67.8,
                'key_evidence': [
                    'Complex product catalog structure',
                    'Manual configuration processes'
                ],
                'decision_makers': [
                    {
                        'id': 'dm_002',
                        'name': 'Lee Abbott',
                        'title': 'Vice President',
                        'email': 'lee.a@abbottcollection.com'
                    }
                ]
            }
        ]
        
        # Initialize generator
        generator = CompleteClayWebhookOrchestrator()
        
        # Generate samples for each company
        all_samples = []
        
        for i, company in enumerate(test_companies, 1):
            print(f"\n📊 Company {i}: {company['company_name']}")
            print(f"   Domain: {company['domain']}")
            print(f"   EDP: {company['primary_edp']}")
            
            try:
                # Generate campaign using the message generator
                campaign = generator.message_generator.generate_campaign(
                    company_data=company,
                    pain_signals={'primary_pain': company['primary_edp']},
                    decision_makers=company['decision_makers']
                )
                
                if campaign:
                    print(f"   ✅ Campaign generated")
                    
                    # Create outreach data structure
                    outreach_data = {
                        'company': company,
                        'analysis': {
                            'primary_edp': company['primary_edp'],
                            'tam_tier': company['tam_tier'],
                            'key_evidence': company['key_evidence']
                        },
                        'campaign': campaign
                    }
                    
                    # Generate webhook payload
                    webhook_payload = generator.prepare_complete_payload(outreach_data)
                    
                    if webhook_payload:
                        print(f"   📡 Webhook payload generated")
                        
                        # Extract key data
                        data = webhook_payload['data']
                        email_count = len(json.loads(data.get('email_sequence', '[]')))
                        linkedin_count = len(json.loads(data.get('linkedin_messages', '[]')))
                        
                        print(f"   📧 Emails: {email_count}")
                        print(f"   💼 LinkedIn: {linkedin_count}")
                        
                        # Store sample
                        sample = {
                            'company_name': company['company_name'],
                            'domain': company['domain'],
                            'primary_edp': company['primary_edp'],
                            'webhook_payload': webhook_payload,
                            'generation_timestamp': datetime.now().isoformat()
                        }
                        all_samples.append(sample)
                    else:
                        print(f"   ❌ No webhook payload generated")
                else:
                    print(f"   ❌ No campaign generated")
                    
            except Exception as e:
                print(f"   ⚠️ Error: {e}")
        
        # Save samples
        if all_samples:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"/Users/ryanburt/supercat_automation_agent/output/webhook_samples_{timestamp}.json"
            
            # Ensure output directory exists
            os.makedirs("/Users/ryanburt/supercat_automation_agent/output", exist_ok=True)
            
            with open(filename, 'w') as f:
                json.dump(all_samples, f, indent=2, default=str)
            
            print(f"\n💾 Saved {len(all_samples)} webhook samples to:")
            print(f"   {filename}")
            
            # Print summary
            print(f"\n📋 Summary:")
            for sample in all_samples:
                data = sample['webhook_payload']['data']
                email_count = len(json.loads(data.get('email_sequence', '[]')))
                linkedin_count = len(json.loads(data.get('linkedin_messages', '[]')))
                print(f"   • {sample['company_name']}: {email_count} emails, {linkedin_count} LinkedIn")
            
            return all_samples
        else:
            print(f"\n❌ No samples generated")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("🚀 Starting webhook sample generation...")
    samples = generate_webhook_samples()
    
    if samples:
        print(f"\n🎉 Successfully generated {len(samples)} webhook samples!")
    else:
        print(f"\n💥 Webhook sample generation failed!")
