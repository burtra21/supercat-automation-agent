#!/usr/bin/env python3
"""
Test script for validated integration system
Tests the dual methodology PSI calculator and enhanced message generator
"""

import json
import sys
import os
from pathlib import Path

# Add supercat_automation to path
sys.path.append('supercat_automation')

from supercat_automation.analysis.validated_psi_calculator import ValidatedPSICalculator
from supercat_automation.generation.validated_message_generator import ValidatedMessageGenerator

def test_dual_psi_calculation():
    """Test the dual methodology PSI calculator"""
    
    print("🧪 Testing Dual Methodology PSI Calculator")
    print("=" * 50)
    
    # Initialize calculator
    calculator = ValidatedPSICalculator()
    
    # Sample company data (based on validation study examples)
    test_companies = [
        {
            "company_name": "Test Furniture Co",
            "domain": "testfurniture.com",
            "rep_count": 15,
            "catalog_sku_count": 3500,
            "channel_count": 2,
            "brand_count": 1,
            "annual_revenue": 8000000
        },
        {
            "company_name": "Crisis Lighting LLC", 
            "domain": "crisislighting.com",
            "rep_count": 25,
            "catalog_sku_count": 8000,
            "channel_count": 3,
            "brand_count": 2,
            "annual_revenue": 15000000
        }
    ]
    
    # Sample website evidence (simulating different crisis levels)
    test_evidence = [
        {
            "evidence": [
                "No product search functionality",
                "Mobile optimization failure",
                "PDF-only catalogs detected",
                "No SSL certificate"
            ],
            "tech_stack": ["WordPress", "Legacy PHP"]
        },
        {
            "evidence": [
                "No product search functionality", 
                "Mobile optimization failure",
                "Manual dealer/rep login system",
                "No SSL certificate",
                "Request quote process only"
            ],
            "tech_stack": ["Custom CMS", "Legacy infrastructure"]
        }
    ]
    
    # Test each company
    for i, (company, evidence) in enumerate(zip(test_companies, test_evidence)):
        print(f"\n📊 Testing Company {i+1}: {company['company_name']}")
        print("-" * 40)
        
        # Calculate dual PSI
        results = calculator.calculate_dual_psi(company, evidence)
        
        # Display results
        print(f"Weighted PSI: {results['weighted_methodology']['psi_score']:.1f}%")
        print(f"Averaged PSI: {results['averaged_methodology']['psi_score']:.1f}%")
        print(f"Weighted Primary EDP: {results['weighted_methodology']['primary_edp']}")
        print(f"Averaged Primary EDP: {results['averaged_methodology']['primary_edp']}")
        print(f"Qualification Tier: {results['weighted_methodology']['tier']}")
        print(f"Purchase Probability: {results['weighted_methodology']['purchase_probability']:.1%}")
        
        # Show methodology comparison
        comparison = results['methodology_comparison']
        print(f"Primary EDP Match: {comparison['primary_edp_match']}")
        print(f"PSI Difference: {comparison['psi_difference']:.1f}%")
        
        # Show messaging hooks
        messaging = results['messaging']
        print(f"Crisis Level: {messaging['crisis_level']}")
        print(f"Weighted Hook: {messaging['weighted_methodology_hook']}")
        if messaging['evidence_based_hooks']:
            print(f"Evidence Hooks: {messaging['evidence_based_hooks'][:2]}")
    
    print("\n✅ PSI Calculator test completed")
    return True

def test_validated_message_generation():
    """Test the validated message generator"""
    
    print("\n🧪 Testing Validated Message Generator")
    print("=" * 50)
    
    # Initialize message generator (without OpenAI for testing)
    generator = ValidatedMessageGenerator()
    
    # Test company data
    company_data = {
        "company_name": "Sample Furniture Inc",
        "domain": "samplefurniture.com", 
        "rep_count": 20,
        "catalog_sku_count": 5000,
        "channel_count": 2,
        "annual_revenue": 12000000
    }
    
    # Test website evidence (high crisis scenario)
    website_evidence = {
        "evidence": [
            "No product search functionality",
            "Mobile optimization failure", 
            "No SSL certificate",
            "Manual order processing",
            "PDF-only catalogs detected"
        ],
        "tech_stack": ["WordPress", "Legacy systems"]
    }
    
    print(f"📧 Generating campaign for: {company_data['company_name']}")
    print("-" * 40)
    
    # Generate validated campaign
    campaign = generator.generate_validated_campaign(company_data, website_evidence)
    
    # Display campaign overview
    print(f"Campaign Type: {campaign['campaign_type']}")
    print(f"Qualification Tier: {campaign['qualification_tier']}")
    print(f"Primary Methodology: {campaign['primary_methodology']}")
    
    # Show validation context
    validation = campaign['validation_context']
    print(f"Validation Source: {validation['study_source']}")
    print(f"Weighted PSI: {validation['weighted_psi']:.1f}%")
    print(f"Averaged PSI: {validation['averaged_psi']:.1f}%")
    print(f"Purchase Probability: {validation['purchase_probability']:.1%}")
    
    # Show email sequence overview
    email_sequence = campaign['email_sequence']
    print(f"\n📧 Email Sequence ({len(email_sequence)} emails):")
    for email in email_sequence:
        print(f"  Day {email['send_day']}: {email['email_type']} - {email['subject'][:60]}...")
    
    # Show LinkedIn sequence
    linkedin_sequence = campaign['linkedin_sequence']
    print(f"\n💼 LinkedIn Sequence ({len(linkedin_sequence)} messages):")
    for msg in linkedin_sequence:
        print(f"  Day {msg['send_day']}: {msg['type']}")
    
    # Show ad suggestions
    ad_suggestions = campaign['ad_suggestions']
    print(f"\n📢 Ad Suggestions ({len(ad_suggestions)} platforms):")
    for ad in ad_suggestions:
        print(f"  {ad['platform']}: {ad.get('headlines', [''])[0][:50]}...")
    
    # Show operational intelligence (if qualified)
    if 'operational_intelligence' in campaign:
        intel = campaign['operational_intelligence']
        print(f"\n🧠 Operational Intelligence:")
        print(f"  Averaged Primary EDP: {intel['averaged_primary_edp']}")
        print(f"  Expansion Opportunities: {len(intel['expansion_opportunities'])}")
        if intel['conversation_starters']:
            print(f"  Conversation Starters: {len(intel['conversation_starters'])}")
    
    print("\n✅ Message Generator test completed")
    return True

def test_configuration_loading():
    """Test configuration file loading"""
    
    print("\n🧪 Testing Configuration Loading")
    print("=" * 50)
    
    # Test validated weights config
    weights_path = Path("supercat_automation/config/validated_edp_weights.json")
    if weights_path.exists():
        with open(weights_path, 'r') as f:
            weights_config = json.load(f)
        
        print("✅ Validated EDP weights loaded")
        print(f"  Weighted methodology weights: {len(weights_config['weighted_methodology']['weights'])}")
        print(f"  Averaged methodology weights: {len(weights_config['averaged_methodology']['weights'])}")
        print(f"  Crisis thresholds defined: {len(weights_config['crisis_thresholds'])}")
    else:
        print("❌ Validated EDP weights config not found")
        return False
    
    # Test crisis messaging config
    messaging_path = Path("supercat_automation/config/crisis_messaging.json")
    if messaging_path.exists():
        with open(messaging_path, 'r') as f:
            messaging_config = json.load(f)
        
        print("✅ Crisis messaging config loaded")
        print(f"  Weighted methodology hooks: {len(messaging_config['weighted_methodology_hooks'])}")
        print(f"  Averaged methodology intelligence: {len(messaging_config['averaged_methodology_intelligence'])}")
        print(f"  Evidence patterns: {len(messaging_config['evidence_based_patterns']['digital_failures_that_predict_purchases'])}")
    else:
        print("❌ Crisis messaging config not found")
        return False
    
    print("\n✅ Configuration loading test completed")
    return True

def test_validation_study_integration():
    """Test integration of validation study findings"""
    
    print("\n🧪 Testing Validation Study Integration")
    print("=" * 50)
    
    calculator = ValidatedPSICalculator()
    
    # Get validation summary
    validation_summary = calculator.get_validation_summary()
    
    print("📊 Validation Study Summary:")
    print(f"  Source: {validation_summary['study_source']}")
    print(f"  Customer Base: {validation_summary['customer_base']}")
    
    key_findings = validation_summary['key_findings']
    print(f"  Methodology Differences: {key_findings['methodology_differences']}")
    print(f"  Weighted Validation: {key_findings['weighted_validation']}")
    print(f"  Averaged Insights: {key_findings['averaged_insights']}")
    print(f"  Portfolio Health: {key_findings['portfolio_health']}")
    
    implementation = validation_summary['implementation_strategy']
    print(f"  Primary Qualification: {implementation['primary_qualification']}")
    print(f"  Intelligence Layer: {implementation['intelligence_layer']}")
    print(f"  Resource Allocation: {implementation['resource_allocation']}")
    
    print("\n✅ Validation study integration test completed")
    return True

def main():
    """Run all tests"""
    
    print("🚀 SuperCat Validated Integration Test Suite")
    print("=" * 60)
    
    tests = [
        ("Configuration Loading", test_configuration_loading),
        ("Dual PSI Calculation", test_dual_psi_calculation),
        ("Validated Message Generation", test_validated_message_generation),
        ("Validation Study Integration", test_validation_study_integration)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("🏁 Test Results Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {test_name}")
    
    print(f"\nOverall: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 All tests passed! Integration is ready for deployment.")
        return 0
    else:
        print(f"\n⚠️ {total-passed} test(s) failed. Please review and fix issues.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
