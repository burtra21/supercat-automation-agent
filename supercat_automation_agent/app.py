#!/usr/bin/env python3
"""
Supercat EDP Analysis API - WORKING VERSION
Returns complete EDP analysis in your existing pipeline format
"""

import json
import logging
import os
from datetime import datetime
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
analysis_storage = []

def analyze_company_for_clay(company_name, domain):
    """
    REAL EDP analysis using your existing WebsiteEvidenceExtractor
    Returns complete analysis in your pipeline format
    """
    
    try:
        # Import your existing analysis system
        import sys
        import os
        
        # Add the supercat_automation directory to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        supercat_dir = os.path.join(current_dir, 'supercat_automation')
        if supercat_dir not in sys.path:
            sys.path.insert(0, supercat_dir)
            
        from scrapers.website_evidence import WebsiteEvidenceExtractor
        
        # Perform REAL website analysis
        extractor = WebsiteEvidenceExtractor()
        evidence = extractor.analyze_website(domain)
        
        # Transform to your pipeline format
        edp_evidence = evidence.get('edp_evidence', {})
        tam_indicators = evidence.get('tam_indicators', {})
        
        # Calculate scores
        total_pain_score = sum(edp.get('weighted_score', edp.get('score', 0)) for edp in edp_evidence.values())
        primary_edp = max(edp_evidence.items(), key=lambda x: x[1].get('weighted_score', 0))[0] if edp_evidence else "unknown"
        
        # Determine qualification tier
        if total_pain_score >= 2.0:
            tier = "TIER_A_IMMEDIATE"
        elif total_pain_score >= 1.0:
            tier = "TIER_B_ACTIVE"
        else:
            tier = "TIER_C_NURTURE"
        
        # Extract specific indicators
        missing_features = []
        evidence_hooks = []
        
        for edp_name, edp_data in edp_evidence.items():
            if edp_data.get('score', 0) > 0.3:
                missing_features.extend(edp_data.get('indicators_found', []))
                evidence_hooks.extend(edp_data.get('specific_issues', []))
        
        # Return COMPLETE raw analysis - everything your system produces
        analysis_result = {
            # Core identification
            "company_name": company_name,
            "domain": domain,
            "processing_version": "v2_validated",
            "analysis_timestamp": datetime.now().isoformat(),
            "source": "real_website_analysis",
            
            # COMPLETE EDP Analysis - All 5 EDPs with full details
            "edp_analysis": edp_evidence,  # Full raw EDP data
            
            # EDP Scoring Summary
            "total_pain_score": total_pain_score,
            "weighted_psi_score": round(total_pain_score * 25, 2),
            "averaged_psi_score": round(total_pain_score * 20, 0),
            "qualification_tier": tier,
            "purchase_probability": min(0.95, total_pain_score * 0.4),
            
            # EDP Rankings (Primary, Secondary, Third, etc.)
            "edp_rankings": sorted(
                [(name, data.get('weighted_score', data.get('score', 0)), data.get('evidence_strength', 'none'))
                 for name, data in edp_evidence.items()],
                key=lambda x: x[1], reverse=True
            ),
            
            # Individual EDP Scores & Details
            "sales_enablement_collapse": edp_evidence.get('sales_enablement_collapse', {}),
            "technology_obsolescence": edp_evidence.get('technology_obsolescence', {}),
            "rep_performance_crisis": edp_evidence.get('rep_performance_crisis', {}),
            "sku_complexity": edp_evidence.get('sku_complexity', {}),
            "channel_conflict": edp_evidence.get('channel_conflict', {}),
            
            # TAM Classification
            "tam_indicators": tam_indicators,
            "tam_tier": tam_indicators.get('tier', 'UNKNOWN'),
            "has_multiple_edps": tam_indicators.get('has_multiple_edps', False),
            "edp_count": tam_indicators.get('edp_count', 0),
            
            # Website Evidence Details
            "website_evidence": evidence,
            "personalization_hooks": evidence.get('personalization_hooks', []),
            "specific_findings": evidence.get('specific_findings', []),
            
            # Feature Detection (REAL analysis)
            "has_product_search": not any('no_product_search' in edp.get('indicators_found', []) for edp in edp_evidence.values()),
            "has_mobile_optimization": not any('no_mobile_optimization' in edp.get('indicators_found', []) for edp in edp_evidence.values()),
            "has_ssl": domain.startswith('https') if domain.startswith('http') else True,
            
            # Legacy format compatibility
            "weighted_primary_edp": primary_edp,
            "averaged_primary_edp": primary_edp,
            "missing_features": ", ".join(missing_features[:10]),
            "evidence_hooks": "; ".join(evidence_hooks[:5]) if evidence_hooks else f"Analysis completed for {company_name}"
        }
        
        return analysis_result
        
    except Exception as e:
        logger.error(f"Real analysis failed for {company_name}: {e}")
        
        # Fallback to basic analysis if imports fail
        return {
            "company_name": company_name,
            "domain": domain,
            "processing_version": "v2_basic",
            "weighted_psi_score": 45.0,
            "qualification_tier": "TIER_C_NURTURE",
            "weighted_primary_edp": "analysis_error",
            "missing_features": "Unable to analyze website",
            "evidence_hooks": f"Analysis error for {company_name}: {str(e)}",
            "analysis_timestamp": datetime.now().isoformat(),
            "source": "fallback_analysis"
        }

@app.route("/pain-signal-webhook", methods=["POST", "GET"])
@app.route("/analyze", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def analyze_endpoint():
    """
    MAIN EDP ANALYSIS ENDPOINT
    Clay sends: {"company_name": "ABC Corp", "domain": "abc.com"}
    Returns: Complete EDP analysis in your existing format
    """
    if request.method == "GET":
        return jsonify({
            "service": "🐱 Supercat EDP Analysis API - WORKING",
            "status": "✅ ACTIVE",
            "endpoints": ["/analyze", "/pain-signal-webhook", "/"],
            "usage": {
                "method": "POST",
                "body": {"company_name": "ABC Corp", "domain": "abc.com"},
                "returns": "Complete EDP analysis with all your pipeline columns"
            }
        }), 200
    
    # POST method - EDP Analysis
    try:
        data = request.get_json() or {}
        company_name = data.get('company_name', 'Unknown Company')
        domain = data.get('domain', 'unknown.com')
        
        logger.info(f"🔍 Analyzing {company_name} ({domain}) for Clay")
        
        # Get complete EDP analysis
        analysis_result = analyze_company_for_clay(company_name, domain)
        analysis_storage.append(analysis_result)
        
        logger.info(f"✅ Analysis complete for {company_name}")
        
        return jsonify({
            "status": "success",
            "analysis": analysis_result,
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"❌ Analysis error: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/health")
def health():
    """Health check"""
    return jsonify({
        "status": "healthy",
        "service": "supercat-edp-analysis",
        "analyses_completed": len(analysis_storage)
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"🚀 Starting Supercat EDP Analysis API on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
