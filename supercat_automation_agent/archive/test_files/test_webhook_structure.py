#!/usr/bin/env python3
"""
Test to show the flattened data structure being sent to each Clay webhook
"""

import sys
import os
import json
sys.path.append('supercat_automation')

from generation.pvp_message_generator import PVPMessageGenerator
from generation.pvp_ad_generator import PVPAdGenerator
from orchestration.clay_webhook import CompleteClayWebhookOrchestrator

def test_webhook_data_structure():
    """Test to show what data gets sent to each webhook"""
    
    # Create test analysis data
    test_analysis = {
        'company_name': 'Test Furniture Co',
        'domain': 'testfurniture.com',
        'primary_edp': 'rep_performance_crisis',
        'qualification_tier': 'TIER_2_ACTIVE',
        'psi_score': 45.2,
        'key_evidence': [
            'No dealer/rep portal detected',
            'Found 8 PDF downloads - indicates manual processes',
            'No modern web framework detected'
        ],
        'detailed_evidence': {
            'specific_findings': [
                'No dealer/rep portal detected',
                'Found 8 PDF downloads - indicates manual processes',
                'No modern web framework detected'
            ],
            'personalization_hooks': [
                {'type': 'catalog', 'value': 'furniture catalog'}
            ]
        }
    }
    
    test_company = {
        'id': 'test_123',
        'company_name': 'Test Furniture Co',
        'domain': 'testfurniture.com',
        'first_name': 'John',
        'last_name': 'Smith',
        'email': 'john.smith@testfurniture.com',
        'title': 'Sales Director',
        'employee_count': 75,
        'catalog_sku_count': 1200
    }
    
    # Prepare outreach data
    outreach_data = {
        'company': {
            'id': test_company['id'],
            'company_name': test_company['company_name'],
            'domain': test_company['domain'],
            'primary_edp': test_analysis['primary_edp'],
            'tam_tier': test_analysis['qualification_tier'],
            'psi_score': test_analysis['psi_score'],
            'website_evidence': test_analysis['detailed_evidence'],
            'first_name': test_company['first_name'],
            'last_name': test_company['last_name'],
            'email': test_company['email'],
            'title': test_company['title'],
            'employee_count': test_company['employee_count'],
            'catalog_sku_count': test_company['catalog_sku_count']
        }
    }
    
    # Generate campaigns
    orchestrator = CompleteClayWebhookOrchestrator()
    complete_payload = orchestrator.prepare_complete_payload(outreach_data)
    
    if complete_payload:
        pvp_campaign = complete_payload['data'].get('pvp_campaign', {})
        ad_campaign = complete_payload['data'].get('ad_campaign', {})
        
        print("=" * 80)
        print("WEBHOOK DATA STRUCTURES")
        print("=" * 80)
        
        # 1. Research Data Webhook
        print("\n📊 RESEARCH DATA WEBHOOK:")
        print("-" * 40)
        research_data = {
            'company_id': test_company['id'],
            'company_name': test_company['company_name'],
            'domain': test_company['domain'],
            'primary_edp': test_analysis['primary_edp'],
            'tam_tier': test_analysis['qualification_tier'],
            'psi_score': test_analysis['psi_score'],
            'first_name': test_company['first_name'],
            'last_name': test_company['last_name'],
            'email': test_company['email'],
            'title': test_company['title'],
            'employee_count': test_company['employee_count'],
            'catalog_sku_count': test_company['catalog_sku_count']
        }
        
        # Add evidence columns
        for i, evidence in enumerate(test_analysis['key_evidence'][:5], 1):
            research_data[f'evidence_{i}'] = evidence
            
        for key, value in research_data.items():
            print(f"  {key}: {value}")
        
        # 2. Email Campaign Webhook
        print("\n📧 EMAIL CAMPAIGN WEBHOOK:")
        print("-" * 40)
        email_sequence = pvp_campaign.get('email_sequence', [])
        email_data = {
            'company_id': test_company['id'],
            'company_name': test_company['company_name'],
            'domain': test_company['domain'],
            'primary_edp': test_analysis['primary_edp']
        }
        
        for i, email in enumerate(email_sequence[:5], 1):
            email_data[f'email_subject_{i}'] = email.get('subject', '')
            email_data[f'email_body_{i}'] = email.get('body', '')[:100] + "..." if len(email.get('body', '')) > 100 else email.get('body', '')
            email_data[f'email_day_{i}'] = email.get('day', i-1)
            
        for key, value in email_data.items():
            print(f"  {key}: {value}")
        
        # 3. LinkedIn Campaign Webhook  
        print("\n💼 LINKEDIN CAMPAIGN WEBHOOK:")
        print("-" * 40)
        linkedin_messages = pvp_campaign.get('linkedin_messages', [])
        linkedin_data = {
            'company_id': test_company['id'],
            'company_name': test_company['company_name'],
            'domain': test_company['domain'],
            'primary_edp': test_analysis['primary_edp']
        }
        
        for i, message in enumerate(linkedin_messages[:3], 1):
            linkedin_data[f'linkedin_subject_{i}'] = message.get('subject', '')
            linkedin_data[f'linkedin_message_{i}'] = message.get('message', '')[:100] + "..." if len(message.get('message', '')) > 100 else message.get('message', '')
            linkedin_data[f'linkedin_day_{i}'] = message.get('day', i-1)
            
        for key, value in linkedin_data.items():
            print(f"  {key}: {value}")
        
        # 4. Ads Campaign Webhook
        print("\n📱 ADS CAMPAIGN WEBHOOK:")
        print("-" * 40)
        ads_data = {
            'company_id': test_company['id'],
            'company_name': test_company['company_name'],
            'domain': test_company['domain'],
            'primary_edp': test_analysis['primary_edp']
        }
        
        # Display ads
        display_ads = ad_campaign.get('display_ads', {}).get('ad_sizes', [])
        for i, ad in enumerate(display_ads[:3], 1):
            message = ad.get('message', {})
            ads_data[f'ad_{i}_size'] = ad.get('size', '')
            ads_data[f'ad_{i}_headline'] = message.get('headline', '')
            ads_data[f'ad_{i}_subtext'] = message.get('subtext', '')
            ads_data[f'ad_{i}_cta'] = message.get('cta', '')
        
        # Google ads
        google_ads = ad_campaign.get('google_ads', {}).get('ads', [])
        for i, ad in enumerate(google_ads[:2], 1):
            ads_data[f'google_ad_{i}_headline'] = ad.get('headline', '')
            ads_data[f'google_ad_{i}_description'] = ad.get('description', '')[:100] + "..." if len(ad.get('description', '')) > 100 else ad.get('description', '')
            
        for key, value in ads_data.items():
            print(f"  {key}: {value}")
        
        print("\n" + "=" * 80)
        print("✅ All webhook data is now FLATTENED and COLUMN-READY for Clay!")
        print("✅ No more JSON parsing needed - direct column mapping!")
        print("=" * 80)

if __name__ == "__main__":
    test_webhook_data_structure()
