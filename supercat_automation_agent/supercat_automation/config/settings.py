# config/settings.py
"""
Complete and merged configuration for SuperCat GTM Automation.
Combines detailed application logic with enhanced scraper settings.
"""

import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    """Centralized configuration using Pydantic for validation"""

    # --- Core API Keys (Required) ---
    supabase_url: str = Field(..., env='SUPABASE_URL')
    supabase_key: str = Field(..., env='SUPABASE_KEY')
    openai_api_key: str = Field(..., env='OPENAI_API_KEY')
    
    # --- Clay Configuration (Optional) ---
    clay_webhook_url: str = Field(default="https://api.clay.com/webhook/placeholder", env='CLAY_WEBHOOK_URL')
    clay_api_key: Optional[str] = Field(default=None, env='CLAY_API_KEY')
    clay_table_id: Optional[str] = Field(default=None, env='CLAY_TABLE_ID')

    # --- ENHANCED SCRAPER SETTINGS (Required for Scraping) ---
    twocaptcha_api_key: Optional[str] = Field(default=None, env='TWOCAPTCHA_API_KEY')
    BRIGHT_DATA_WSS_URL: Optional[str] = Field(default=None, env='BRIGHT_DATA_WSS_URL')
    use_proxies: bool = Field(default=False, env='USE_PROXIES')
    proxy_list: List[str] = Field(default_factory=list, env='PROXY_LIST')

    # --- Application Settings ---
    environment: str = Field(default='development', env='ENVIRONMENT')
    debug_mode: bool = Field(default=True, env='DEBUG_MODE')
    log_level: str = Field(default='INFO', env='LOG_LEVEL')
    openai_model: str = Field(default='gpt-4-turbo-preview', env='OPENAI_MODEL')
    
    # --- Rate Limiting ---
    max_daily_enrichments: int = Field(default=500, env='MAX_DAILY_ENRICHMENTS')
    max_concurrent_scrapers: int = Field(default=3, env='MAX_CONCURRENT_SCRAPERS')
    
    # --- Static Application Logic Configuration ---
    # Trade Show Configuration
    trade_shows_config: Dict[str, Any] = {
        'las_vegas_market': {
            'name': 'Las Vegas Market',
            'url': 'https://www.lasvegasmarket.com',
            'exhibitor_url': 'https://www.lasvegasmarket.com/exhibitors',
            'schedule': 'quarterly',
            'next_date': '2025-01-26'
        },
        'high_point_market': {
            'name': 'High Point Market',
            'url': 'https://www.highpointmarket.org',
            'exhibitor_url': 'https://www.highpointmarket.org/exhibitors',
            'schedule': 'bi-annual',
            'next_date': '2025-04-26'
        },
        'americasmart': {
            'name': 'AmericasMart Atlanta',
            'url': 'https://www.americasmart.com',
            'exhibitor_url': 'https://www.americasmart.com/exhibitors',
            'schedule': 'monthly',
            'next_date': '2025-01-14'
        }
    }
    
    # Validated Pain Signals from Won Deals
    validated_pain_signals: Dict[str, Any] = {
        'sales_enablement_collapse': {
            'weight': 1.0,
            'keywords': ['manual', 'hours', 'spreadsheet', 'paper', 'trade show'],
            'threshold': 0.7
        },
        'technology_obsolescence': {
            'weight': 0.93,
            'keywords': ['old', 'legacy', 'CSV', 'FTP', 'outdated'],
            'threshold': 0.6
        },
        'rep_performance_crisis': {
            'weight': 0.71,
            'keywords': ['visibility', 'tracking', 'quota', 'adoption'],
            'threshold': 0.5
        },
        'sku_complexity': {
            'weight': 0.64,
            'keywords': ['SKUs', 'configurations', 'options', 'variants'],
            'threshold': 0.5
        }
    }
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'

# Initialize a single settings object for the application to import
settings = Settings()
