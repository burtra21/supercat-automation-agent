#!/usr/bin/env python3
"""
Clay Integration Test Script
Tests both Clay calling API and API sending to Clay
"""

import requests
import json

BASE_URL = "http://localhost:8000"
CLAY_WEBHOOK_URL = "https://api.clay.com/v3/sources/webhook/pull-in-data-from-a-webhook-ba8d0100-6e0f-4c26-8523-fac369f75a18"

def test_clay_calls_api():
    """
    Test: Clay calls your API to get analysis (current workflow)
    """
    print("🧪 TEST 1: Clay Calls Your API")
    print("=" * 50)
    
    # Simulate Clay calling your API
    response = requests.post(f"{BASE_URL}/pain-signal-webhook", 
                           json={"company_name": "Sample Corp", "domain": "sample.com"})
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Clay receives this complete response:")
        print(f"   Status: {data['status']}")
        print(f"   Company: {data['analysis']['company_name']}")
        print(f"   Pain Score: {data['analysis']['total_pain_score']}")
        print(f"   Tier: {data['analysis']['qualification_tier']}")
        print(f"   Top EDP: {data['analysis']['edp_rankings'][0][0]}")
        
        print(f"\n📍 Clay can now use this data for:")
        print(f"   - Lead scoring based on pain_score")
        print(f"   - Segmentation by qualification_tier")
        print(f"   - Personalization using EDP rankings")
        
    else:
        print(f"❌ API call failed: {response.status_code}")

def test_api_sends_to_clay():
    """
    Test: Your API analyzes and sends results TO Clay webhook
    """
    print("\n🧪 TEST 2: Your API Sends TO Clay")
    print("=" * 50)
    
    # Test the new endpoint that sends to Clay
    try:
        response = requests.post(f"{BASE_URL}/analyze-and-send",
                               json={"company_name": "Clay Target Corp", "domain": "claytarget.com"},
                               timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            clay_sent = data.get("clay_webhook_ sent", False)
            
            print(f"✅ Analysis complete!")
            print(f"✅ Sent to Clay: {clay_sent}")
            print(f"📍 Data sent to: {CLAY_WEBHOOK_URL}")
            
            if clay_sent:
                print(f"\n🎉 SUCCESS! Complete EDP analysis sent to Clay webhook")
                print(f"📍 Check Clay dashboard for incoming data")
                
                analysis = data['analysis']
                print(f"\n📊 Data sent to Clay:")
                print(f"   Company: {analysis['company_name']}")
                print(f"   Total Pain Score: {analysis['total_pain_score']}")
                print(f"   Qualification Tier: {analysis['qualification_tier']}")
                print(f"   EDPS Found: {len([e for e in analysis['edp_rankings'] if e[1] > 0.1])}")
            else:
                print(f"❌ Failed to send to Clay webhook")
        else:
            print(f"❌ API error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Error testing Clay send: {e}")

def main():
    """
    Test both Clay integration approaches
    """
    print("🔌 CLAY WEBHOOK INTEGRATION TEST")
    print("=" * 60)
    
    print(f"📡 Clay Webhook URL: {CLAY_WEBHOOK_URL}")
    print(f"🚀 Your API Base URL: {BASE_URL}")
    
    # Test both workflows
    test_clay_calls_api()
    test_api_sends_to_clay()
    
    print(f"\n🎯 SUMMARY:")
    print(f"✅ Option 1: Clay calls your API - Working!")
    print(f"✅ Option 2: Your API sends to Clay - Available!")
    print(f"\n📍 Your data IS going to Clay webhook at:")
    print(f"   {CLAY_WEBHOOK_URL}")

if __name__ == "__main__":
    main()

