# MCP Analysis Guide for SuperCat

## How to Use Your MCP Setup to Analyze SuperCat

### 1. **Core Files for MCP Analysis** (Copy these to Claude Desktop)

**Start with these 4 files - they're the heart of SuperCat:**

```bash
# Copy these file paths to analyze in Claude Desktop:
/Users/ryanburt/supercat_automation_agent/supercat_automation/analysis/pain_detector.py
/Users/ryanburt/supercat_automation_agent/supercat_automation/scrapers/website_evidence.py  
/Users/ryanburt/supercat_automation_agent/supercat_automation/analysis/prospect_processor.py
/Users/ryanburt/supercat_automation_agent/supercat_automation/generation/message_generator.py
```

### 2. **MCP Analysis Workflow**

**Step 1: Open Claude Desktop**
- Your MCP servers are already configured
- Ask: "Can you analyze this file and tell me what it does?" 
- Paste the file path

**Step 2: Use Clay MCP for Data Analysis**
- Ask: "Use Clay to analyze the prospect data structure"
- Your clay-mcp server can help understand data flow

**Step 3: Use N8N MCP for Workflow Analysis**  
- Ask: "Use N8N to map the automation workflow"
- Your n8n-mcp server can help visualize the pipeline

### 3. **Key Questions to Ask Claude Desktop**

**For pain_detector.py:**
```
"Analyze this file and tell me:
1. What are the 5 EDPs it detects?
2. Are there any duplicate functions?
3. What's the scoring algorithm?"
```

**For website_evidence.py:**
```
"Analyze this file and tell me:
1. What website indicators does it look for?
2. Are there duplicate methods?
3. How does the scraping work?"
```

**For pipeline files:**
```
"Compare these 3 pipeline files and tell me:
1. Which one is most complete?
2. What are the differences?
3. Which should I keep?"
```

### 4. **MCP Commands to Try**

**Using your configured MCP servers:**

```
# In Claude Desktop, try these commands:
"Use clay-mcp to analyze the prospect data structure"
"Use n8n-mcp to create a workflow diagram of the pipeline"  
"Use smartlead to review the email sequence logic"
"Use notion-mcp to create a project cleanup plan"
```

### 5. **File Size Limits for MCP**

**If files are too large:**
- Copy just the class definitions and key methods
- Focus on the main functions (like `detect_edp()` or `extract_evidence()`)
- Ask Claude to analyze function by function

**Example:**
Instead of the whole website_evidence.py, copy just:
```python
class WebsiteEvidenceExtractor:
    def __init__(self):
        # initialization code
    
    def detect_sales_enablement_collapse(self, url):
        # main detection logic
```

### 6. **Expected MCP Benefits**

**Clay MCP:** 
- Understand data enrichment flow
- Analyze prospect scoring logic

**N8N MCP:**
- Map automation workflows  
- Identify bottlenecks

**Smartlead MCP:**
- Review email sequence effectiveness
- Optimize message generation

**Notion MCP:**
- Create organized cleanup documentation
- Track progress on fixes
