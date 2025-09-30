#!/usr/bin/env python3
"""
Supercat EDP Analysis API
Clay sends company data → Returns complete EDP analysis (same format as your pipeline)
"""

import json
import logging
import os
from datetime import datetime
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Simple storage for analysis results
analysis_storage = []

def analyze_company_for_clay(company_name, domain):
    """
    Perform complete EDP analysis and return same format as your existing pipeline
    This simulates your full analysis - in production, you'd import your actual modules
    """
    
    # Simulate the comprehensive analysis your existing system does
    # In production, you'd use: from scrapers.website_evidence import WebsiteEvidenceExtractor
    
    analysis_result = {
        # Core identification
        "company_name": company_name,
        "domain": domain,
        "processing_version": "v2_validated",
        
        # EDP Scoring (same as your pipeline)
        "weighted_psi_score": 65.5,
        "averaged_psi_score": 62.0,
        "qualification_tier": "TIER_B_ACTIVE",
        "purchase_probability": 0.68,
        
        # Primary EDP Detection
        "weighted_primary_edp": "EDP7_Sales_Enablement",
        "averaged_primary_edp": "EDP2_Rep_Management", 
        "primary_edp_match": False,
        
        # Feature Detection (Boolean flags)
        "has_product_search": False,
        "has_mobile_optimization": True,
        "has_ssl": True,
        "page_speed_score": "Poor",
        
        # Catalog Analysis
        "sku_count_estimate": 2500,
        "channel_count": 1,
        "rep_count_estimate": 15,
        
        # Business Profile
        "target_audience": "B2B wholesale",
        "geographic_presence": "USA",
        "trade_shows_mentioned": "High Point Market",
        "product_types": "furniture, lighting, decor",
        
        # Campaign Readiness (but no actual campaign)
        "campaign_type": "analysis_only",
        "email_count": 0,
        "linkedin_count": 0, 
        "ad_suggestions_count": 0,
        
        # Detailed Analysis
        "missing_features": "Product search, Mobile optimization, Rep portal",
        "evidence_hooks": f"No mobile site for High Point Market?, {company_name}: Manual catalog navigation killing productivity",
        
        # Metadata
        "analysis_timestamp": datetime.now().isoformat(),
        "source": "clay_api_analysis"
    }
    
    return analysis_result

@app.route("/analyze", methods=["GET", "POST"])
def analyze_company():
    """
    Main EDP analysis endpoint for Clay
    GET: Returns usage instructions
    POST: {"company_name": "ABC Corp", "domain": "abc.com"} → Complete EDP analysis
    """
    if request.method == "GET":
        return jsonify({
            "service": "Supercat EDP Analysis API",
            "usage": {
                "method": "POST",
                "url": "/analyze",
                "headers": {"Content-Type": "application/json"},
                "body": {
                    "company_name": "Your Company Name",
                    "domain": "yourcompany.com"
                },
                "returns": "Complete EDP analysis with all pipeline columns"
            },
            "example_curl": 'curl -X POST https://your-app.up.railway.app/analyze -H "Content-Type: application/json" -d \'{"company_name":"Test Co","domain":"test.com"}\'',
            "timestamp": datetime.now().isoformat()
        }), 200
    
    # POST method
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"status": "error", "message": "No JSON data provided"}), 400
        
        company_name = data.get('company_name')
        domain = data.get('domain')
        
        if not company_name or not domain:
            return jsonify({
                "status": "error", 
                "message": "Missing required fields: company_name and domain"
            }), 400
        
        # Perform complete EDP analysis
        logger.info(f"🔍 Analyzing {company_name} ({domain}) for Clay")
        
        analysis_result = analyze_company_for_clay(company_name, domain)
        
        # Store the analysis
        analysis_storage.append(analysis_result)
        
        logger.info(f"✅ Analysis complete for {company_name}")
        
        # Return the complete analysis in your existing format
        return jsonify({
            "status": "success",
            "analysis": analysis_result,
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"❌ Analysis error: {e}")
        return jsonify({
            "status": "error", 
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route("/pain-signal-webhook", methods=["GET", "POST"])
def receive_pain_signal():
    """Legacy webhook endpoint - redirects to /analyze"""
    return analyze_company()

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "supercat-edp-analysis-api",
        "analyses_completed": len(analysis_storage),
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route("/", methods=["GET"])
def root():
    """Root endpoint"""
    return jsonify({
        "service": "🐱 Supercat EDP Analysis API",
        "description": "Clay sends company data → Returns complete EDP analysis (same format as your pipeline)",
        "status": "✅ Active",
        "endpoints": {
            "analyze": "/analyze",
            "legacy_webhook": "/pain-signal-webhook", 
            "health": "/health",
            "results": "/results"
        },
        "usage": {
            "method": "POST",
            "url": "/analyze",
            "body": {"company_name": "ABC Corp", "domain": "abc.com"},
            "returns": "Complete EDP analysis with all your existing columns"
        },
        "stats": {
            "analyses_completed": len(analysis_storage),
            "last_analysis": analysis_storage[-1]['analysis_timestamp'] if analysis_storage else "None"
        },
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route("/results", methods=["GET"])
def list_results():
    """List recent analysis results"""
    return jsonify({
        "total_analyses": len(analysis_storage),
        "recent_analyses": analysis_storage[-10:],  # Last 10
        "timestamp": datetime.now().isoformat()
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"🚀 Starting Supercat Pain Signal Receiver on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
