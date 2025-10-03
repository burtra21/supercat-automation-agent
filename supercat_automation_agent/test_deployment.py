#!/usr/bin/env python3
"""
Deployment Test Script for Railway EDP Analysis API
Tests the deployed API endpoint to ensure complete EDP analysis is working
"""

import requests
import json
import sys
from typing import Dict, Any

def test_api_deployment(base_url: str) -> bool:
    """
    Test the deployed API endpoint with a sample company
    """
    print(f"🚀 Testing deployed API at: {base_url}")
    
    # Test payload
    test_data = {
        "company_name": "Test Corp",
        "domain": "test.com"
    }
    
    try:
        # Test multiple endpoints
        endpoints = [
            "/pain-signal-webhook",
            "/analyze", 
            "/"
        ]
  
        for endpoint in endpoints:
            url = f"{base_url.rstrip('/')}{endpoint}"
            print(f"\n🔍 Testing endpoint: {endpoint}")
            
            response = requests.post(
                url,
                json=test_data,
                timeout=30,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate response structure
                if validate_edp_response(data):
                    print(f"✅ {endpoint} - API working correctly!")
                    print_response_summary(data)
                    return True
                else:
                    print(f"❌ {endpoint} - Invalid response format")
                    
            else:
                print(f"❌ {endpoint} - HTTP {response.status_code}: {response.text}")
        
        return False
        
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

def validate_edp_response(data: Dict[str, Any]) -> bool:
    """
    Validate that the response contains complete EDP analysis
    """
    try:
        # Check for required structure
        if "status" not in data or data["status"] != "success":
            return False
            
        if "analysis" not in data:
            return False
            
        analysis = data["analysis"]
        
        # Check for EDP analysis components
        required_fields = [
            "total_pain_score",
            "weighted_psi_score", 
            "qualification_tier",
            "edp_rankings",
            "edp_analysis"
        ]
        
        for field in required_fields:
            if field not in analysis:
                print(f"❌ Missing field: {field}")
                return False
        
        # Check that EDP rankings is populated
        edp_rankings = analysis.get("edp_rankings", [])
        if not edp_rankings or len(edp_rankings) == 0:
            print("❌ EDP rankings empty")
            return False
            
        # Check that edp_analysis contains all 5 EDPs
        edp_analysis = analysis.get("edp_analysis", {})
        expected_edps = [
            "sales_enablement_collapse",
            "technology_obsolescence", 
            "rep_performance_crisis",
            "sku_complexity",
            "channel_conflict"
        ]
        
        for edp in expected_edps:
            if edp not in edp_analysis:
                print(f"❌ Missing EDP: {edp}")
                return False
        
        print("✅ All EDP validation checks passed!")
        return True
        
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False

def print_response_summary(data: Dict[str, Any]) -> None:
    """
    Print a summary of the EDP analysis response
    """
    analysis = data.get("analysis", {})
    
    print(f"\n📊 EDP Analysis Summary:")
    print(f"   Company: {analysis.get('company_name', 'Unknown')}")
    print(f"   Domain: {analysis.get('domain', 'Unknown')}")
    print(f"   Total Pain Score: {analysis.get('total_pain_score', 0)}")
    print(f"   Weighted PSI Score: {analysis.get(' weighted_psi_score', 0)}")
    print(f"   Qualification Tier: {analysis.get('qualification_tier', 'Unknown')}")
    
    # Show top EDP rankings
    rankings = analysis.get("edp_rankings", [])
    if rankings:
        print(f"\n🎯 Top EDP Rankings:")
        for i, (edp, score, strength) in enumerate(rankings[:3], 1):
            print(f"   {i}. {edp.replace('_', ' ').title()}: {score:.3f} ({strength})")

def main():
    """
    Main test function
    """
    if len(sys.argv) < 2:
        print("Usage: python test_deployment.py <API_BASE_URL>")
        print("Example: python test_deployment.py https://your-app.up.railway.app")
        sys.exit(1)
    
    base_url = sys.argv[1]
    
    print("🧪 Railway EDP Analysis API Deployment Test")
    print("=" * 50)
    
    success = test_api_deployment(base_url)
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 DEPLOYMENT TEST SUCCESSFUL!")
        print("✅ API is working correctly and returning complete EDP analysis")
        print("✅ Ready for Clay webhook integration")
    else:
        print("❌ DEPLOYMENT TEST FAILED!")
        print("❌ Check deployment logs and fix issues before Clay integration")
        sys.exit(1)

if __name__ == "__main__":
    main()
