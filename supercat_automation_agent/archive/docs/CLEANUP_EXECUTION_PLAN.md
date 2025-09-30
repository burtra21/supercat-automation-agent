# 🧹 PROJECT CLEANUP PLAN

## 📧 FILES TO MODIFY FOR COPY CHANGES

### **Core Files for Email/LinkedIn/Ads Copy:**
1. **`supercat_automation/generation/message_generator.py`** ⭐ **PRIMARY**
   - `CustomerValidatedMessageGenerator` class
   - All 7 email generation methods
   - LinkedIn message methods
   - GPT-4 prompts and templates

2. **`supercat_automation/generation/pvp_ad_generator.py`**
   - Ad copy generation logic
   - Google/Meta ad templates

3. **`supercat_automation/orchestration/clay_webhook.py`**
   - Webhook payload formatting

### **Specific Methods to Change:**
- `generate_problem_agitation_email()` - Email 1
- `generate_social_proof_email()` - Email 2  
- `generate_roi_email()` - Email 3
- `generate_competitive_email()` - Email 4
- `generate_case_study_email()` - Email 5
- `generate_urgency_email()` - Email 6
- `generate_breakup_email()` - Email 7
- `generate_linkedin_connection()` - LinkedIn outreach
- `generate_linkedin_followup()` - LinkedIn follow-up
- `generate_meta_ad_copy()` - Facebook/Meta ads

---

## 🗑️ FILES TO DELETE

### **Test Files (Safe to Delete):**
- `test_webhook_samples.py`
- `direct_message_test.py` 
- `simple_webhook_test.py`
- `test_campaign_generation.py`
- `test_mcp_setup.py`
- `test_webhook_structure.py`
- `upload_prospects.py` (empty file)
- `supercat_automation/tests/test_pain_detection.py`
- `supercat_automation/simple_test.py`

### **Backup Files (Safe to Delete):**
- `supercat_automation/generation/pvp_message_generator_backup.py`

### **Documentation Files (Can Archive):**
- `ARCHITECTURE_SEPARATION_AUDIT.md`
- `CODE_CLEANUP_PLAN.md` 
- `EDP_detection.txt`
- `evidence_based_EDP.txt`
- `KEY_CODE_SNIPPETS.md`
- `MCP_ANALYSIS_GUIDE.md`
- `PIPELINE_FIX_COMPLETE.md`
- `PROJECT_CONTEXT_FULL.md`
- `project_context.txt`
- `STRATEGIC_GAPS_ANALYSIS.md`
- `STRATEGY_ALIGNMENT_AUDIT.md`
- `SUPERCAT_ALIGNMENT_AUDIT.md`
- `SUPERCAT_MCP_STRATEGY.md`
- `SUPERCAT_OVERVIEW.md`

### **Result Files (Can Archive/Delete):**
- All `qualified_*.csv` files
- All `results_enhanced_*.json` files

### **Unused Generation Files:**
- `supercat_automation/generation/evidence_based_messages.py`
- `supercat_automation/generation/email_sequences.py`
- `supercat_automation/generation/linkedin_messages.py`
- `supercat_automation/generation/ad_copy_generator.py`
- `supercat_automation/generation/pvp_message_generator.py`

---

## 🏗️ CORE PRODUCTION FILES TO KEEP

### **Essential Pipeline:**
- `supercat_automation/full_pipeline.py` ⭐
- `supercat_automation/generation/message_generator.py` ⭐
- `supercat_automation/orchestration/clay_webhook.py` ⭐
- `supercat_automation/generation/pvp_ad_generator.py` ⭐

### **Configuration:**
- `supercat_automation/config/settings.py`
- `supercat_automation/config/credentials.py`
- `supercat_automation/config/__init__.py`

### **Database:**
- `supercat_automation/database/connection.py`
- `supercat_automation/database/__init__.py`

### **Core Modules:**
- `supercat_automation/analysis/` (all files)
- `supercat_automation/scrapers/` (all files)
- `supercat_automation/utils/` (all files)

### **Data:**
- `supercat_automation/prospects.csv`
- `supercat_automation/companies_to_analyze.csv`

---

## 📁 RECOMMENDED FOLDER STRUCTURE AFTER CLEANUP

```
supercat_automation_agent/
├── supercat_automation/
│   ├── full_pipeline.py                    # Main entry point
│   ├── prospects.csv                       # Input data
│   ├── config/                            # Configuration
│   ├── database/                          # DB connection
│   ├── analysis/                          # EDP detection
│   ├── scrapers/                          # Website scraping
│   ├── generation/                        # Content generation
│   │   ├── message_generator.py           # ⭐ Email/LinkedIn copy
│   │   └── pvp_ad_generator.py           # ⭐ Ad copy
│   ├── orchestration/                     
│   │   └── clay_webhook.py               # ⭐ Webhook integration
│   └── utils/                            # Utilities
├── output/                               # Generated files
├── logs/                                # Log files
├── .venv/                               # Python environment
└── README.md                           # Documentation
```

---

## 🚀 CLEANUP EXECUTION PLAN

1. **Archive Documentation** - Move *.md and *.txt to `/archive/`
2. **Delete Test Files** - Remove all test_*.py files
3. **Delete Result Files** - Remove qualified_*.csv and results_*.json
4. **Remove Unused Generators** - Delete redundant generation files
5. **Clean Root Directory** - Keep only essential files
6. **Update .gitignore** - Ignore output/, logs/, results files

This will reduce project size by ~80% while keeping all functional code!
