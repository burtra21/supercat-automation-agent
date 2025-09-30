#!/usr/bin/env python3
"""
Simple Flask webhook receiver for Railway deployment
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

# Simple storage for webhooks
webhook_storage = []

@app.route("/pain-signal-webhook", methods=["POST"])
def receive_pain_signal():
    """Main webhook endpoint for Clay"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"status": "error", "message": "No JSON data"}), 400
        
        # Store webhook
        webhook_record = {
            'id': len(webhook_storage) + 1,
            'company_name': data.get('company_name', 'Unknown'),
            'domain': data.get('domain', ''),
            'payload': data,
            'received_at': datetime.now().isoformat()
        }
        
        webhook_storage.append(webhook_record)
        logger.info(f"📥 Received webhook for {webhook_record['company_name']}")
        
        return jsonify({
            "status": "received",
            "webhook_id": webhook_record['id'],
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "supercat-pain-signal-receiver",
        "webhooks_received": len(webhook_storage),
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route("/", methods=["GET"])
def root():
    """Root endpoint"""
    return jsonify({
        "service": "Supercat Pain Signal Receiver",
        "description": "Receives webhook data from Clay",
        "endpoints": {
            "webhook": "/pain-signal-webhook",
            "health": "/health",
            "webhooks": "/webhooks"
        },
        "webhooks_received": len(webhook_storage),
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route("/webhooks", methods=["GET"])
def list_webhooks():
    """List received webhooks"""
    return jsonify({
        "total_webhooks": len(webhook_storage),
        "webhooks": webhook_storage[-10:],  # Last 10
        "timestamp": datetime.now().isoformat()
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"🚀 Starting Supercat Pain Signal Receiver on port {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
