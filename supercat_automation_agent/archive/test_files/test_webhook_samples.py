#!/usr/bin/env python3
"""
Generate sample webhook payloads for all 4 specialized Clay endpoints
"""

import sys
import os
import json
from datetime import datetime

sys.path.append('supercat_automation')

def create_sample_company_data():
    """Create realistic test company data for different EDPs"""
    
    companies = [
        {
            'company_name': 'Premier Furniture Solutions',
            'domain': 'premierfurniture.com',
            'id': 'comp_001',
            'primary_edp': 'rep_performance_crisis',
            'catalog_sku_count': 8500,
            'tam_tier': 'TIER_2_ACTIVE',
            'psi_score': 42.3,
            'key_evidence': [
                'No dealer/rep portal detected',
                'No modern web framework detected',
                'No rep/dealer locator found'
            ],
            'decision_makers': [
                {
                    'id': 'dm_001',
                    'name': 'Sarah Johnson',
                    'title': 'VP Sales Operations',
                    'email': 'sarah.johnson@premierfurniture.com'
                },
                {
                    'id': 'dm_002',
                    'name': 'Mike Chen',
                    'title': 'Director of Sales',
                    'email': 'mike.chen@premierfurniture.com'
                }
            ]
        },
        {
            'company_name': 'Apex Manufacturing Corp',
            'domain': 'apexmfg.com',
            'id': 'comp_002',
            'primary_edp': 'sku_complexity',
            'catalog_sku_count': 15000,
            'tam_tier': 'TIER_1_PRIME',
            'psi_score': 67.8,
            'key_evidence': [
                'Complex product configurations detected',
                'Manual order processing identified',
                'Legacy ERP system in use'
            ],
            'decision_makers': [
                {
                    'id': 'dm_003',
                    'name': 'David Rodriguez',
                    'title': 'Chief Operations Officer',
                    'email': 'david.rodriguez@apexmfg.com'
                }
            ]
        },
        {
            'company_name': 'TechCorp Industries',
            'domain': 'techcorp.com',
            'id': 'comp_003',
            'primary_edp': 'technology_obsolescence',
            'catalog_sku_count': 3200,
            'tam_tier': 'TIER_2_ACTIVE',
            'psi_score': 38.9,
            'key_evidence': [
                'Outdated web technology stack',
                'No mobile optimization',
                'Legacy database systems'
            ],
            'decision_makers': [
                {
                    'id': 'dm_004',
                    'name': 'Jennifer Walsh',
                    'title': 'CTO',
                    'email': 'jennifer.walsh@techcorp.com'
                }
            ]
        },
        {
            'company_name': 'Global Trade Solutions',
            'domain': 'globaltradesolutions.com',
            'id': 'comp_004',
            'primary_edp': 'sales_enablement_collapse',
            'catalog_sku_count': 12000,
            'tam_tier': 'TIER_1_PRIME',
            'psi_score': 71.2,
            'key_evidence': [
                'No sales enablement tools detected',
                'Manual quote processes',
                'No CRM integration visible'
            ],
            'decision_makers': [
                {
                    'id': 'dm_005',
                    'name': 'Robert Kim',
                    'title': 'VP Sales',
                    'email': 'robert.kim@globaltradesolutions.com'
                }
            ]
        }
    ]
    
    return companies

def generate_webhook_samples():
    """Generate sample webhook payloads for all 4 endpoints"""
    
    try:
        from supercat_automation.orchestration.clay_webhook import CampaignGenerator
        
        generator = CampaignGenerator()
        companies = create_sample_company_data()
        
        print("🎯 Generating sample webhook payloads...")
        print("=" * 60)
        
        all_samples = {}
        
        for i, company in enumerate(companies, 1):
            print(f"\n📊 Company {i}: {company['company_name']}")
            print(f"   EDP: {company['primary_edp']}")
            print(f"   TAM Tier: {company['tam_tier']}")
            
            # Generate campaign
            try:
                campaign = generator.generate_campaign(company)
                
                if campaign:
                    print(f"   ✅ Campaign generated: {len(campaign.get('message_variants', {}).get('email', []))} emails")
                    
                    # Prepare the 4 specialized webhook payloads
                    webhooks = generator.prepare_specialized_webhooks(company, campaign)
                    
                    print(f"   📡 Generated {len(webhooks)} specialized webhooks:")
                    
                    for webhook in webhooks:
                        webhook_type = webhook['webhook_type']
                        print(f"      - {webhook_type}: {len(webhook['data'])} data fields")
                        
                        # Store sample
                        if webhook_type not in all_samples:
                            all_samples[webhook_type] = []
                        all_samples[webhook_type].append(webhook)
                
                else:
                    print(f"   ❌ No campaign generated")
                    
            except Exception as e:
                print(f"   ⚠️ Error generating campaign: {e}")
        
        # Save samples to files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        print(f"\n💾 Saving webhook samples...")
        
        for webhook_type, samples in all_samples.items():
            filename = f"webhook_samples_{webhook_type}_{timestamp}.json"
            filepath = f"output/{filename}"
            
            # Ensure output directory exists
            os.makedirs("output", exist_ok=True)
            
            with open(filepath, 'w') as f:
                json.dump(samples, f, indent=2, default=str)
            
            print(f"   📄 {webhook_type}: {len(samples)} samples → {filename}")
        
        # Create a comprehensive summary
        summary = {
            'generation_timestamp': timestamp,
            'total_companies_tested': len(companies),
            'webhook_types_generated': list(all_samples.keys()),
            'samples_per_type': {k: len(v) for k, v in all_samples.items()},
            'sample_structure': {
                webhook_type: {
                    'fields': list(samples[0]['data'].keys()) if samples else [],
                    'sample_count': len(samples)
                }
                for webhook_type, samples in all_samples.items()
            }
        }
        
        summary_file = f"output/webhook_samples_summary_{timestamp}.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n📋 Summary saved to: {summary_file}")
        print(f"🎉 Generated {sum(len(samples) for samples in all_samples.values())} total webhook samples!")
        
        return all_samples
        
    except Exception as e:
        print(f"❌ Error in webhook sample generation: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("🚀 Starting webhook sample generation...")
    samples = generate_webhook_samples()
    
    if samples:
        print("\n✅ Webhook sample generation completed successfully!")
        print("\nSample webhook types generated:")
        for webhook_type, sample_list in samples.items():
            print(f"  - {webhook_type}: {len(sample_list)} samples")
    else:
        print("\n❌ Webhook sample generation failed!")
