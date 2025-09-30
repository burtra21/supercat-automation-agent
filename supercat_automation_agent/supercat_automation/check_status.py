import sys
print("🔍 Checking SuperCat GTM System Status...\n")

# Check imports
modules = {
    "Database": "database.connection",
    "Pain Detector": "analysis.pain_detector", 
    "Message Generator": "generation.evidence_based_messages",
    "Website Analyzer": "scrapers.website_evidence"
}

for name, module in modules.items():
    try:
        __import__(module)
        print(f"✅ {name}: OK")
    except SyntaxError as e:
        print(f"❌ {name}: Syntax error - {e}")
    except Exception as e:
        print(f"❌ {name}: {e}")

# Check settings
try:
    from config.settings import settings
    print(f"\n📋 Configuration:")
    print(f"  Environment: {settings.environment}")
    print(f"  Debug Mode: {settings.debug_mode}")
    
    # Check which services are configured
    services = {
        "Supabase": 'placeholder' not in settings.supabase_url,
        "OpenAI": 'placeholder' not in settings.openai_api_key,
        "Clay": 'placeholder' not in settings.clay_webhook_url
    }
    
    for service, configured in services.items():
        status = "✅ Configured" if configured else "⚠️  Using placeholder"
        print(f"  {service}: {status}")
        
except Exception as e:
    print(f"❌ Settings error: {e}")

print("\n🎯 Ready to:")
print("  1. Analyze companies for pain signals")
print("  2. Generate personalized campaigns")
print("  3. Process prospect lists")
print("\nRun: python run_pipeline.py to see it in action!")
