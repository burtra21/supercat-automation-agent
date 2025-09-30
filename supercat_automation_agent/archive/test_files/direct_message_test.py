#!/usr/bin/env python3
"""
Direct test of CustomerValidatedMessageGenerator
"""

import sys
import os
import json
from datetime import datetime

# Add current directory to path
sys.path.insert(0, '/Users/ryanburt/supercat_automation_agent/supercat_automation')

def test_message_generator():
    """Test the CustomerValidatedMessageGenerator directly"""
    
    try:
        # Import after path setup
        from generation.message_generator import CustomerValidatedMessageGenerator
        
        print("🎯 Testing CustomerValidatedMessageGenerator...")
        
        # Create test company
        company_data = {
            'company_name': '9to5 Seating',
            'domain': '9to5seating.com',
            'id': 'comp_001',
            'catalog_sku_count': 850
        }
        
        pain_signals = {
            'primary_pain': 'rep_performance_crisis'
        }
        
        decision_makers = [
            {
                'id': 'dm_001',
                'name': 'Ed Lachman',
                'title': 'Chief Operating Officer',
                'email': 'ed.lachman@9to5seating.com'
            }
        ]
        
        # Initialize generator
        generator = CustomerValidatedMessageGenerator()
        
        print(f"\n📊 Company: {company_data['company_name']}")
        print(f"   Pain: {pain_signals['primary_pain']}")
        print(f"   Decision makers: {len(decision_makers)}")
        
        # Generate campaign
        campaign = generator.generate_campaign(
            company_data=company_data,
            pain_signals=pain_signals,
            decision_makers=decision_makers
        )
        
        if campaign:
            print(f"\n✅ Campaign generated successfully!")
            print(f"   Type: {campaign.get('campaign_type')}")
            print(f"   Pain focus: {campaign.get('pain_point_focus')}")
            
            # Check message variants
            variants = campaign.get('message_variants', {})
            emails = variants.get('email', [])
            linkedin = variants.get('linkedin', [])
            ads = variants.get('ads', [])
            
            print(f"\n📧 Email sequence: {len(emails)} emails")
            for i, email in enumerate(emails, 1):
                print(f"   Email {i}: {email.get('subject', 'No subject')}")
            
            print(f"\n💼 LinkedIn messages: {len(linkedin)} messages")
            for i, msg in enumerate(linkedin, 1):
                print(f"   Message {i}: {msg.get('type', 'Unknown type')}")
            
            print(f"\n📱 Ad suggestions: {len(ads)} ads")
            
            # Save the campaign
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"/Users/ryanburt/supercat_automation_agent/output/campaign_sample_{timestamp}.json"
            
            # Ensure output directory exists
            os.makedirs("/Users/ryanburt/supercat_automation_agent/output", exist_ok=True)
            
            with open(filename, 'w') as f:
                json.dump(campaign, f, indent=2, default=str)
            
            print(f"\n💾 Campaign saved to: {filename}")
            
            return campaign
        else:
            print(f"\n❌ No campaign generated")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    print("🚀 Starting direct message generator test...")
    campaign = test_message_generator()
    
    if campaign:
        print(f"\n🎉 Message generator test successful!")
    else:
        print(f"\n💥 Message generator test failed!")
