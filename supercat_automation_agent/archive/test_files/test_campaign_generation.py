#!/usr/bin/env python3
"""
Quick test to isolate campaign generation issue
"""

import sys
import os
sys.path.append('supercat_automation')

from generation.pvp_message_generator import PVPMessageGenerator

def test_campaign_generation():
    """Test the campaign generation with minimal data"""
    
    generator = PVPMessageGenerator()
    
    # Create a simple test analysis matching our pipeline structure
    test_analysis = {
        'company_name': 'Test Company',
        'domain': 'test.com',
        'primary_edp': 'rep_performance_crisis',
        'qualification_tier': 'TIER_2_ACTIVE',
        'psi_score': 38.7,
        'key_evidence': [
            'No dealer/rep portal detected',
            'No modern web framework detected',
            'No rep/dealer locator found'
        ],
        'detailed_evidence': {
            'specific_findings': [
                'No dealer/rep portal detected',
                'No modern web framework detected'
            ],
            'personalization_hooks': [
                {'type': 'catalog', 'value': 'furniture catalog'}
            ]
        },
        'website_evidence': {
            'specific_findings': [
                'No dealer/rep portal detected',
                'No modern web framework detected'
            ],
            'personalization_hooks': [
                {'type': 'catalog', 'value': 'furniture catalog'}
            ]
        }
    }
    
    print("Testing campaign generation...")
    print(f"Company: {test_analysis['company_name']}")
    print(f"Primary EDP: {test_analysis['primary_edp']}")
    
    try:
        # Test evidence extraction first
        evidence = generator._extract_all_evidence(test_analysis)
        print(f"\n✅ Evidence extraction successful:")
        print(f"   Website findings: {len(evidence['website_findings'])}")
        print(f"   Personalization hooks: {len(evidence['personalization_hooks'])}")
        print(f"   Has sufficient evidence: {evidence['has_sufficient_evidence']}")
        
        # Test campaign generation
        campaign = generator.generate_pvp_campaign(test_analysis)
        print(f"\n✅ Campaign generation successful:")
        print(f"   Campaign type: {campaign.get('campaign_type')}")
        print(f"   Email sequence: {len(campaign.get('email_sequence', []))} emails")
        print(f"   LinkedIn messages: {len(campaign.get('linkedin_messages', []))} messages")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_campaign_generation()
    if success:
        print("\n🎉 Campaign generation test passed!")
    else:
        print("\n💥 Campaign generation test failed!")
