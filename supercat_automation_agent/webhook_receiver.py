#!/usr/bin/env python3
"""
Pain Signal Receiver API - Standalone Railway Version
Flask API endpoint to receive webhook data from Clay
Simplified version for deployment without complex module dependencies
"""

import json
import logging
import os
from datetime import datetime
from typing import Dict, Any
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Simple in-memory storage for demo (in production, you'd connect to your database)
webhook_storage = []

class PainSignalReceiver:
    """
    Handles incoming webhook data from Clay
    Simplified version for Railway deployment
    """
    
    def __init__(self):
        logger.info("✅ Initialized Pain Signal Receiver")
    
    def process_webhook_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process incoming webhook data from Clay
        """
        try:
            # Extract key fields from Clay webhook
            company_name = data.get('company_name', 'Unknown')
            domain = data.get('domain', '')
            webhook_type = data.get('webhook_type', 'pain_signal_response')
            
            logger.info(f"📥 Received webhook for {company_name} ({domain})")
            
            # Store webhook data (simplified for deployment)
            webhook_record = self._save_webhook_data(data)
            
            # Process based on webhook type
            if webhook_type == 'pain_signal_response':
                return self._handle_pain_signal_response(data, webhook_record)
            elif webhook_type == 'campaign_status':
                return self._handle_campaign_status(data, webhook_record)
            else:
                return self._handle_generic_webhook(data, webhook_record)
                
        except Exception as e:
            logger.error(f"❌ Error processing webhook data: {e}")
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def _save_webhook_data(self, data: Dict[str, Any]) -> Dict:
        """
        Save incoming webhook for audit trail (simplified storage)
        """
        try:
            # Prepare webhook record
            webhook_record = {
                'id': len(webhook_storage) + 1,
                'webhook_source': 'clay',
                'webhook_type': data.get('webhook_type', 'unknown'),
                'company_name': data.get('company_name'),
                'domain': data.get('domain'),
                'payload': data,
                'received_at': datetime.now().isoformat(),
                'status': 'received'
            }
            
            # Store in memory (for production, use your Supabase connection)
            webhook_storage.append(webhook_record)
            
            logger.info(f"💾 Saved webhook data: ID {webhook_record['id']}")
            return webhook_record
                
        except Exception as e:
            logger.error(f"❌ Error saving webhook: {e}")
            return {}
    
    def _handle_pain_signal_response(self, data: Dict, webhook_record: Dict) -> Dict[str, Any]:
        """
        Handle response to pain signal analysis
        """
        logger.info(f"🎯 Processing pain signal response for {data.get('company_name')}")
        
        try:
            return {
                'status': 'processed',
                'type': 'pain_signal_response',
                'company': data.get('company_name'),
                'webhook_id': webhook_record.get('id'),
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Error handling pain signal response: {e}")
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def _handle_campaign_status(self, data: Dict, webhook_record: Dict) -> Dict[str, Any]:
        """
        Handle campaign status updates from Clay
        """
        logger.info(f"📧 Processing campaign status for {data.get('company_name')}")
        
        try:
            return {
                'status': 'processed',
                'type': 'campaign_status',
                'company': data.get('company_name'),
                'webhook_id': webhook_record.get('id'),
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Error handling campaign status: {e}")
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def _handle_generic_webhook(self, data: Dict, webhook_record: Dict) -> Dict[str, Any]:
        """
        Handle generic webhook data
        """
        logger.info(f"📦 Processing generic webhook for {data.get('company_name')}")
        
        return {
            'status': 'received',
            'type': 'generic',
            'webhook_id': webhook_record.get('id'),
            'data_keys': list(data.keys()),
            'timestamp': datetime.now().isoformat()
        }

# Initialize receiver
receiver = PainSignalReceiver()

@app.route("/pain-signal-webhook", methods=["POST"])
def receive_pain_signal():
    """
    Main webhook endpoint for receiving data from Clay
    """
    try:
        # Get JSON data
        data = request.get_json()
        
        if not data:
            logger.warning("⚠️ Received webhook with no JSON data")
            return jsonify({
                "status": "error",
                "message": "No JSON data received"
            }), 400
        
        logger.info(f"📥 Webhook received from Clay: {json.dumps(data, indent=2)}")
        
        # Process the webhook data
        result = receiver.process_webhook_data(data)
        
        # Return success response
        return jsonify({
            "status": "received",
            "result": result,
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"❌ Error in webhook endpoint: {e}")
        return jsonify({
            "status": "error",
            "message": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint for Railway deployment
    """
    return jsonify({
        "status": "healthy",
        "service": "pain-signal-receiver",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "webhooks_received": len(webhook_storage)
    }), 200

@app.route("/", methods=["GET"])
def root():
    """
    Root endpoint with service information
    """
    return jsonify({
        "service": "Supercat Pain Signal Receiver",
        "description": "Receives webhook data from Clay for pain signal processing",
        "endpoints": {
            "webhook": "/pain-signal-webhook",
            "health": "/health",
            "webhooks": "/webhooks"
        },
        "timestamp": datetime.now().isoformat(),
        "webhooks_received": len(webhook_storage)
    }), 200

@app.route("/webhooks", methods=["GET"])
def list_webhooks():
    """
    List received webhooks (for testing/debugging)
    """
    return jsonify({
        "total_webhooks": len(webhook_storage),
        "webhooks": webhook_storage[-10:],  # Last 10 webhooks
        "timestamp": datetime.now().isoformat()
    }), 200

if __name__ == "__main__":
    """
    Run the Flask app
    For Railway deployment, this will be called by the start command
    """
    # Get port from environment (Railway sets this)
    port = int(os.environ.get("PORT", 8000))
    
    logger.info(f"🚀 Starting Pain Signal Receiver API on port {port}")
    
    # Run the app
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False  # Set to False for production
    )
