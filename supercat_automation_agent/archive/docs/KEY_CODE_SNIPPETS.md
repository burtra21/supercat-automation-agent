# Key Code Snippets for MCP Analysis

## 1. Core EDP Detection Logic (pain_detector.py)

```python
class MultiSourcePainDetector:
    """
    Detects and scores all 5 validated EDPs
    Companies can have multiple EDPs (overlapping pain)
    """
    
    def __init__(self):
        # Validated from 14 won deals
        self.edp_definitions = {
            'sales_enablement_collapse': {
                'display_name': 'Sales Enablement System Collapse',
                'weight': 1.0,
                'won_deal_frequency': '100%'
            },
            'technology_obsolescence': {
                'weight': 0.93,
                'won_deal_frequency': '93%'
            },
            'rep_performance_crisis': {
                'weight': 0.71,
                'won_deal_frequency': '71%'
            },
            'sku_complexity': {
                'weight': 0.64,
                'won_deal_frequency': '64%'
            },
            'channel_conflict': {
                'weight': 0.43,
                'won_deal_frequency': '43%'
            }
        }
    
    def analyze_company(self, company_data: Dict) -> Dict:
        """Complete pain analysis with multi-EDP tagging"""
        # Main analysis logic here
```

## 2. Website Evidence Extraction (website_evidence.py)

```python
class WebsiteEvidenceExtractor:
    """
    Extracts specific evidence of the 5 proven EDPs from websites
    Each method maps to validated pain points from 14 won deals
    """
    
    def __init__(self):
        # Map website indicators to proven EDPs
        self.edp_indicators = {
            'sales_enablement_collapse': {
                'indicators': [
                    'no_product_search',
                    'pdf_only_catalog', 
                    'no_mobile_optimization',
                    'manual_quote_process'
                ]
            },
            'technology_obsolescence': {
                'indicators': [
                    'no_ssl_certificate',
                    'slow_page_load',
                    'outdated_cms'
                ]
            }
        }
    
    def extract_evidence(self, url: str) -> Dict:
        """Main extraction method"""
        # Website scraping and analysis logic
```

## 3. Key Questions for Claude Desktop MCP Analysis

### For pain_detector.py:
```
Copy this snippet to Claude Desktop and ask:
"Analyze this EDP detection logic. Are there any issues with the scoring weights? 
Do you see any duplicate logic that could be consolidated?"
```

### For website_evidence.py:
```
Copy this snippet to Claude Desktop and ask:
"Review this website scraping logic. Are there duplicate methods? 
How could the indicator detection be improved?"
```

### For pipeline comparison:
```
"I have 3 pipeline files: full_pipeline.py, mvp_pipeline.py, and run_pipeline.py.
Can you help me determine which one to keep and what the differences are?"
```

## 4. File Paths for Easy MCP Access

**Copy these exact paths to analyze in Claude Desktop:**

### Core Logic Files:
```
/Users/ryanburt/supercat_automation_agent/supercat_automation/analysis/pain_detector.py
/Users/ryanburt/supercat_automation_agent/supercat_automation/scrapers/website_evidence.py
/Users/ryanburt/supercat_automation_agent/supercat_automation/analysis/prospect_processor.py
```

### Pipeline Files (to compare):
```
/Users/ryanburt/supercat_automation_agent/supercat_automation/full_pipeline.py
/Users/ryanburt/supercat_automation_agent/supercat_automation/mvp_pipeline.py  
/Users/ryanburt/supercat_automation_agent/supercat_automation/run_pipeline.py
```

### Message Generation:
```
/Users/ryanburt/supercat_automation_agent/supercat_automation/generation/message_generator.py
/Users/ryanburt/supercat_automation_agent/supercat_automation/generation/linkedin_messages.py
```

## 5. Immediate Issues to Fix

Based on my analysis, here are the top cleanup priorities:

### Duplicate Imports (website_evidence.py):
```python
# PROBLEM: These are duplicated
import logging
import re
import logging  # <-- DUPLICATE
import re       # <-- DUPLICATE
from typing import Dict, List, Any, Optional, Optional  # <-- DUPLICATE Optional
```

### Multiple Pipeline Files:
- Need to choose between full_pipeline.py, mvp_pipeline.py, run_pipeline.py
- Test each to see which works best

### Cleanup Scripts:
- Delete fix_imports.py and fix_type_hints.py (one-time utilities)
- Archive old test files and data files
