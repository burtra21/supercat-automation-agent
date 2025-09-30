#!/usr/bin/env python3
"""
Large Batch Processor for SuperCat Pipeline v2
Optimized for processing 900+ prospects with robust error handling and progress tracking
"""

import asyncio
import logging
import json
import pandas as pd
from datetime import datetime
from pathlib import Path
import sys
import os
from typing import Dict, List, Any
import time

# Add current directory to path for imports
sys.path.append(os.path.dirname(__file__))

# Configure logging for large batch processing
def setup_logging(batch_name: str):
    """Setup dedicated logging for large batch processing"""
    log_dir = Path("logs/large_batches")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / f"batch_{batch_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

class LargeBatchProcessor:
    """
    Processes large CSV files (900+ prospects) with:
    - Chunked processing to prevent memory issues
    - Progress tracking and resumption capability
    - Robust error handling and recovery
    - Optimized batch sizes for API rate limits
    """
    
    def __init__(self, batch_name: str):
        self.batch_name = batch_name
        self.logger = setup_logging(batch_name)
        self.session = None
        
        # Optimized settings for large batches
        self.chunk_size = 50  # Process 50 prospects at a time
        self.batch_size = 5   # 5 prospects per API batch (to respect rate limits)
        self.delay_between_chunks = 30  # 30 seconds between chunks
        self.delay_between_batches = 10  # 10 seconds between batches
        
        # Progress tracking
        self.progress_file = Path(f"output/large_batch_results/{batch_name}_progress.json")
        self.results_dir = Path(f"output/large_batch_results/{batch_name}")
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
        # Statistics
        self.stats = {
            'start_time': None,
            'total_prospects': 0,
            'processed': 0,
            'qualified': 0,
            'errors': 0,
            'chunks_completed': 0,
            'estimated_completion': None
        }
    
    def save_progress(self):
        """Save current progress to resume if needed"""
        with open(self.progress_file, 'w') as f:
            json.dump(self.stats, f, indent=2, default=str)
    
    def load_progress(self) -> Dict[str, Any]:
        """Load previous progress if exists"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {}
    
    async def process_large_csv(self, csv_path: str, resume: bool = False):
        """
        Process large CSV file with chunking and progress tracking
        
        Args:
            csv_path: Path to the large CSV file
            resume: Whether to resume from previous progress
        """
        self.logger.info(f"🚀 Starting large batch processing: {self.batch_name}")
        self.logger.info(f"📊 File: {csv_path}")
        
        # Load CSV and validate
        if not Path(csv_path).exists():
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        df = pd.read_csv(csv_path)
        self.stats['total_prospects'] = len(df)
        self.stats['start_time'] = datetime.now()
        
        self.logger.info(f"📋 Total prospects to process: {self.stats['total_prospects']}")
        
        # Resume logic
        start_index = 0
        if resume:
            progress = self.load_progress()
            start_index = progress.get('processed', 0)
            self.logger.info(f"🔄 Resuming from prospect #{start_index}")
        
        # Initialize V2 pipeline
        try:
            from full_pipeline_v2 import SuperCatPipelineV2
            pipeline = SuperCatPipelineV2()
        except ImportError as e:
            self.logger.error(f"Failed to import V2 pipeline: {e}")
            return
        
        # Process in chunks
        for chunk_start in range(start_index, len(df), self.chunk_size):
            chunk_end = min(chunk_start + self.chunk_size, len(df))
            chunk_df = df.iloc[chunk_start:chunk_end]
            
            self.logger.info(f"📦 Processing chunk {chunk_start}-{chunk_end} ({len(chunk_df)} prospects)")
            
            # Process chunk
            try:
                await self.process_chunk(chunk_df, pipeline, chunk_start)
                self.stats['chunks_completed'] += 1
                
                # Save progress after each chunk
                self.stats['processed'] = chunk_end
                self.save_progress()
                
                # Delay between chunks to be respectful of APIs
                if chunk_end < len(df):
                    self.logger.info(f"⏳ Waiting {self.delay_between_chunks}s before next chunk...")
                    await asyncio.sleep(self.delay_between_chunks)
                
            except Exception as e:
                self.logger.error(f"❌ Chunk {chunk_start}-{chunk_end} failed: {e}")
                self.stats['errors'] += 1
                # Continue with next chunk instead of failing entire batch
                continue
        
        # Final summary
        self.generate_final_report()
        self.logger.info(f"✅ Large batch processing completed: {self.batch_name}")
    
    async def process_chunk(self, chunk_df: pd.DataFrame, pipeline, chunk_start: int):
        """Process a single chunk of prospects"""
        chunk_results = []
        
        # Save chunk as temporary CSV
        chunk_csv = self.results_dir / f"chunk_{chunk_start}_input.csv"
        chunk_df.to_csv(chunk_csv, index=False)
        
        try:
            # Process using V2 pipeline with smaller batch size
            results = await pipeline.process_csv_v2(str(chunk_csv), self.batch_size)
            
            # Save chunk results
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            # Save detailed JSON results
            results_file = self.results_dir / f"chunk_{chunk_start}_results_{timestamp}.json"
            with open(results_file, 'w') as f:
                json.dump(results, f, indent=2, default=str)
            
            # Extract qualified prospects for this chunk
            if 'results' in results:
                qualified_prospects = []
                for result in results['results']:
                    if result.get('psi_analysis', {}).get('weighted_methodology', {}).get('qualification_decision'):
                        qualified_prospects.append({
                            'company_name': result.get('company_name'),
                            'domain': result.get('domain'),
                            'qualification_tier': result.get('psi_analysis', {}).get('weighted_methodology', {}).get('tier'),
                            'psi_score': result.get('psi_analysis', {}).get('weighted_methodology', {}).get('psi_score'),
                            'primary_edp': result.get('psi_analysis', {}).get('weighted_methodology', {}).get('primary_edp'),
                            'processed_timestamp': timestamp
                        })
                
                if qualified_prospects:
                    qualified_df = pd.DataFrame(qualified_prospects)
                    qualified_file = self.results_dir / f"chunk_{chunk_start}_qualified_{timestamp}.csv"
                    qualified_df.to_csv(qualified_file, index=False)
                    
                    self.stats['qualified'] += len(qualified_prospects)
            
            self.logger.info(f"✅ Chunk {chunk_start} completed successfully")
            
        except Exception as e:
            self.logger.error(f"❌ Error processing chunk {chunk_start}: {e}")
            raise
        
        finally:
            # Clean up temporary chunk file
            if chunk_csv.exists():
                chunk_csv.unlink()
    
    def generate_final_report(self):
        """Generate comprehensive final report"""
        duration = datetime.now() - self.stats['start_time']
        
        # Consolidate all qualified prospects
        all_qualified = []
        qualified_files = list(self.results_dir.glob("*_qualified_*.csv"))
        
        for file in qualified_files:
            df = pd.read_csv(file)
            all_qualified.append(df)
        
        if all_qualified:
            final_qualified = pd.concat(all_qualified, ignore_index=True)
            final_qualified_file = self.results_dir / f"{self.batch_name}_final_qualified_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            final_qualified.to_csv(final_qualified_file, index=False)
            
            self.logger.info(f"📄 Final qualified prospects saved: {final_qualified_file}")
        
        # Generate summary report
        report = f"""
# Large Batch Processing Report: {self.batch_name}

## Summary
- **Start Time**: {self.stats['start_time']}
- **Duration**: {duration}
- **Total Prospects**: {self.stats['total_prospects']}
- **Successfully Processed**: {self.stats['processed']}
- **Qualified Prospects**: {self.stats['qualified']}
- **Chunks Completed**: {self.stats['chunks_completed']}
- **Errors**: {self.stats['errors']}
- **Success Rate**: {(self.stats['processed'] / self.stats['total_prospects'] * 100):.1f}%
- **Qualification Rate**: {(self.stats['qualified'] / max(self.stats['processed'], 1) * 100):.1f}%

## Files Generated
- **Results Directory**: {self.results_dir}
- **Individual Chunk Results**: {len(list(self.results_dir.glob('chunk_*_results_*.json')))} files
- **Qualified Prospects**: {len(list(self.results_dir.glob('*_qualified_*.csv')))} files
- **Final Consolidated**: {self.batch_name}_final_qualified_*.csv

## Performance Metrics
- **Average Processing Speed**: {(self.stats['processed'] / duration.total_seconds() * 60):.1f} prospects/minute
- **Estimated API Calls**: {self.stats['processed'] * 3} (website analysis, PSI calculation, campaign generation)
- **Chunks Processed**: {self.stats['chunks_completed']}

## Next Steps
1. Review qualified prospects in final CSV
2. Import qualified prospects to Clay webhook
3. Launch campaigns for Tier A/B prospects
4. Set up monitoring for Tier C prospects
        """
        
        report_file = self.results_dir / f"{self.batch_name}_final_report.md"
        with open(report_file, 'w') as f:
            f.write(report)
        
        self.logger.info(f"📊 Final report saved: {report_file}")

async def main():
    """Main execution function for large batch processing"""
    if len(sys.argv) < 3:
        print("Usage: python large_batch_processor.py <csv_file> <batch_name> [resume]")
        print("Example: python large_batch_processor.py input/large_batches/900_prospects.csv production_run_sept2025")
        print("Resume: python large_batch_processor.py input/large_batches/900_prospects.csv production_run_sept2025 resume")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    batch_name = sys.argv[2]
    resume = len(sys.argv) > 3 and sys.argv[3] == "resume"
    
    processor = LargeBatchProcessor(batch_name)
    await processor.process_large_csv(csv_file, resume)

if __name__ == "__main__":
    asyncio.run(main())
