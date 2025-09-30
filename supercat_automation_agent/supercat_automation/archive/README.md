# Archive Directory

## 📁 Contents

### `/test_files/` - Test Data & Development Files
- `test_*.csv` - Various test CSV files used during development
- `sample_prospects.csv` - Sample data for testing
- `companies_to_analyze.csv` - Test company data

### `/v1_results/` - Legacy Pipeline Results
- `results_enhanced_*.json` - V1 pipeline results (deprecated)
- `qualified_20250826_*.csv` - V1 qualified prospects (deprecated)

## ⚠️ Important Notes

- **Test Files**: Used for development and testing - not production data
- **V1 Results**: Legacy pipeline results using single methodology PSI
- **Deprecated**: V1 files use outdated qualification methodology

## 🔄 Migration Notes

All current production should use:
- V2 pipeline (`full_pipeline_v2.py`)
- Validated PSI calculator
- Enhanced message generation
- Files moved from root directory on 2025-09-01

## 🗑️ Safe to Remove

These archived files can be safely deleted after confirming V2 pipeline is working correctly in production.
