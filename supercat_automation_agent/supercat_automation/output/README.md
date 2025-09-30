# SuperCat Output Directory Organization

## 📁 Directory Structure

### `/results/` - Pipeline Results
- **`v2_production/`** - V2 pipeline enhanced results (JSON format)
- **`qualified_prospects/`** - V2 qualified prospect exports (CSV format)
- **`prospects.csv`** - Original prospect input files
- **`prospects2.csv`** - Additional prospect input files
- **`prospects_*.csv`** - Legacy pipeline outputs

### `/reports/` - Analysis Reports
- Executive summaries
- Scraping reports
- Orchestrator reports

### `/exports/` - Campaign Exports
- Generated campaign materials
- Message sequences
- Ad suggestions

### `/ads/` - Advertisement Assets
- Generated ad copy
- Campaign suggestions
- Creative assets

### `/large_batch_results/` - Large Batch Processing (900+ prospects)
- **`{batch_name}/`** - Dedicated folder per large batch run
- **`chunk_*_results_*.json`** - Detailed results per processing chunk
- **`chunk_*_qualified_*.csv`** - Qualified prospects per chunk
- **`{batch_name}_final_qualified_*.csv`** - Final consolidated qualified prospects
- **`{batch_name}_final_report.md`** - Comprehensive batch processing report
- **`{batch_name}_progress.json`** - Progress tracking for resumption

## 🗂️ File Naming Convention

### V2 Production Results
- Format: `results_v2_enhanced_YYYYMMDD_HHMMSS.json`
- Contains: Complete pipeline analysis, PSI scores, campaigns

### Qualified Prospects
- Format: `qualified_v2_YYYYMMDD_HHMMSS.csv`
- Contains: Qualified prospects ready for outreach

### Reports
- Format: `[type]_report_YYYYMMDD_HHMMSS.txt`
- Types: scraping, orchestrator, executive_summary

### Large Batch Results
- Format: `{batch_name}_final_qualified_YYYYMMDD_HHMMSS.csv`
- Contains: Consolidated qualified prospects from large batch processing
- Progress: `{batch_name}_progress.json` for resumption capability

## 📊 Current Production Files

### Latest V2 Results (Production Ready)
- `results_v2_enhanced_20250901_035103.json` - Most recent production run
- `qualified_v2_20250901_035103.csv` - Latest qualified prospects

### Historical V2 Results
- Multiple dated files from August 28 - September 1, 2025
- All contain validated PSI calculations and campaign generation

## 🔍 How to Use

1. **For Analysis**: Check `v2_production/` for detailed JSON results
2. **For Outreach**: Use CSV files in `qualified_prospects/`
3. **For Reporting**: Reference files in `reports/` directory
4. **For Campaigns**: Check `exports/` for campaign materials
5. **For Large Batches**: Use `large_batch_results/` for 900+ prospect processing

## 🚨 Important Notes

- V2 pipeline results use validated PSI calculator
- All files after 2025-08-28 use production-ready methodology
- Archived test files and v1 results moved to `/archive/` directory
