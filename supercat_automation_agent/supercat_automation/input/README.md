# Large Batch Processing Guide

## 📋 For Processing 900+ Prospects

### 🗂️ File Organization

#### Input Location
```
/input/large_batches/
├── your_900_prospects.csv          # Your large CSV file
├── backup_900_prospects.csv        # Always keep a backup
└── README.md                       # This guide
```

#### Output Location
```
/output/large_batch_results/
├── {batch_name}/                   # Dedicated folder for your run
│   ├── chunk_*_results_*.json     # Detailed results per chunk
│   ├── chunk_*_qualified_*.csv    # Qualified prospects per chunk
│   ├── {batch_name}_final_qualified_*.csv  # Final consolidated results
│   └── {batch_name}_final_report.md        # Comprehensive report
└── {batch_name}_progress.json     # Progress tracking for resumption
```

## 🚀 How to Run Your 900+ CSV

### Step 1: Prepare Your CSV
1. Save your large CSV in: `/input/large_batches/`
2. Required columns: `company_name`, `domain`
3. Optional columns: `contact_name`, `contact_email`, `industry`

### Step 2: Run the Large Batch Processor
```bash
# Navigate to project directory
cd /Users/ryanburt/supercat_automation_agent/supercat_automation

# Run with your CSV file
python large_batch_processor.py input/large_batches/your_900_prospects.csv production_run_sept2025
```

### Step 3: Monitor Progress
- Check logs in real-time: `tail -f logs/large_batches/batch_production_run_sept2025_*.log`
- Progress saved automatically every 50 prospects
- Can resume if interrupted: `python large_batch_processor.py input/large_batches/your_900_prospects.csv production_run_sept2025 resume`

## ⚙️ Optimized Settings for Large Batches

### Processing Parameters
- **Chunk Size**: 50 prospects per chunk
- **Batch Size**: 5 prospects per API batch
- **Delay Between Chunks**: 30 seconds (API rate limiting)
- **Delay Between Batches**: 10 seconds
- **Estimated Total Time**: ~6-8 hours for 900 prospects

### Memory & Performance
- Chunked processing prevents memory overload
- Progress auto-saved for resumption capability
- Individual chunk results prevent data loss
- Error handling continues processing despite failures

## 📊 Expected Output

### Qualified Prospects Rate
- **Typical**: 35-45% qualification rate
- **900 prospects**: Expect ~315-405 qualified leads
- **Tier Distribution**:
  - Tier A (Immediate): ~15% of qualified
  - Tier B (Active): ~25% of qualified
  - Tier C (Monitor): ~60% of qualified

### Files Generated
1. **Final Qualified CSV**: Ready for Clay import
2. **Detailed JSON Results**: Complete analysis per prospect
3. **Progress Tracking**: For resumption if needed
4. **Comprehensive Report**: Performance metrics and summary

## 🔄 Resumption Capability

If processing is interrupted:
```bash
# Resume from where it left off
python large_batch_processor.py input/large_batches/your_900_prospects.csv production_run_sept2025 resume
```

Progress is saved after every chunk (50 prospects), so minimal re-processing needed.

## 📈 Monitoring & Troubleshooting

### Real-time Monitoring
```bash
# Watch progress logs
tail -f logs/large_batches/batch_production_run_sept2025_*.log

# Check progress file
cat output/large_batch_results/production_run_sept2025_progress.json
```

### Common Issues & Solutions
1. **API Rate Limits**: Built-in delays handle this automatically
2. **Memory Issues**: Chunked processing prevents this
3. **Network Timeouts**: Individual chunk failures don't stop entire batch
4. **Disk Space**: ~2GB needed for 900 prospects with full results

## 🎯 Recommended Approach for 900+ Prospects

### Option 1: Single Large Run (Recommended)
```bash
python large_batch_processor.py input/large_batches/900_prospects.csv production_sept2025
```
- **Pros**: Single consolidated output, comprehensive reporting
- **Cons**: Longer total time (~6-8 hours)
- **Best for**: When you can let it run overnight

### Option 2: Split into Smaller Batches
```bash
# Split your CSV into 3 files of 300 each
python large_batch_processor.py input/large_batches/prospects_batch1.csv batch1_sept2025
python large_batch_processor.py input/large_batches/prospects_batch2.csv batch2_sept2025  
python large_batch_processor.py input/large_batches/prospects_batch3.csv batch3_sept2025
```
- **Pros**: Faster individual runs, more control
- **Cons**: Need to manually consolidate results
- **Best for**: When you need results in phases

## 🔍 Quality Assurance

### Before Running
- [ ] CSV has required columns (`company_name`, `domain`)
- [ ] Backup copy saved
- [ ] Environment variables configured
- [ ] Sufficient disk space (~2GB)

### During Processing
- [ ] Monitor logs for error patterns
- [ ] Check progress file periodically
- [ ] Verify chunk outputs are generating

### After Completion
- [ ] Review final report
- [ ] Validate qualified prospects CSV
- [ ] Import to Clay webhook
- [ ] Archive large batch results

## 💡 Pro Tips

1. **Run Overnight**: Start the batch processing before end of day
2. **Monitor First Hour**: Watch initial chunks to catch any issues early
3. **Backup Results**: Copy final outputs to safe location
4. **Test First**: Run a small sample (50 prospects) to validate setup
5. **Clay Preparation**: Prepare Clay webhook to receive large batch import

## 📞 Support

If issues arise during large batch processing:
1. Check logs in `/logs/large_batches/`
2. Review progress file for resumption point
3. Use `health_monitor.py` to check system status
4. Resume processing with `resume` parameter if needed
