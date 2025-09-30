# scrapers/orchestrator.py
"""
Orchestrates all trade show scrapers.
FIXED to use asyncio.gather for running async scrapers concurrently,
resolving the 'coroutine was never awaited' error.
"""

import logging
import asyncio
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path # ADDED for file path operations

from scrapers.vegas_market import VegasMarketScraper
from scrapers.high_point import HighPointMarketScraper
from scrapers.americasmart import AmericasmartScraper
from database.connection import db
from config.settings import settings

logger = logging.getLogger(__name__)

class ScraperOrchestrator:
    """Manages and coordinates all async trade show scrapers."""

    def __init__(self):
        """Initialize the orchestrator with scraper instances."""
        self.scrapers = {
            'vegas_market': VegasMarketScraper(),
            'high_point': HighPointMarketScraper(),
            'americasmart': AmericasmartScraper(),
        }

    async def run_all_scrapers(self) -> List[Dict[str, Any]]:
        """Runs all configured scrapers concurrently using asyncio.gather."""
        logger.info(f"Starting concurrent run for {len(self.scrapers)} scrapers.")
        
        tasks = [instance.run() for name, instance in self.scrapers.items()]
        
        # return_exceptions=True prevents one failed scraper from stopping the others.
        results = await asyncio.gather(*tasks, return_exceptions=True)

        processed_results = []
        for i, result in enumerate(results):
            scraper_name = list(self.scrapers.keys())[i]
            if isinstance(result, Exception):
                logger.error(f"❌ Scraper '{scraper_name}' failed with an exception: {result}")
                processed_results.append({
                    'success': False,
                    'scraper': scraper_name,
                    'error': str(result)
                })
            else:
                logger.info(f"✅ Scraper '{scraper_name}' completed.")
                processed_results.append(result)
                if result.get('success'):
                    self._update_scraping_metrics(result)

        self.generate_scraping_report(processed_results)
        return processed_results

    def _update_scraping_metrics(self, result: Dict[str, Any]):
        """Update database metrics after a successful scrape."""
        try:
            metrics = {'companies_identified': result.get('exhibitors_processed', 0)}
            db.update_daily_metrics(metrics)
        except Exception as e:
            logger.error(f"Error updating metrics: {e}")

    def generate_scraping_report(self, results: List[Dict[str, Any]]):
        """
        Generates a summary report of the scraping results and saves it to a file.
        """
        total_found = sum(r.get('exhibitors_found', 0) for r in results if r.get('success'))
        total_processed = sum(r.get('exhibitors_processed', 0) for r in results if r.get('success'))
        successful_scrapers = sum(1 for r in results if r.get('success'))
        
        report = f"""
        ========================================
        TRADE SHOW SCRAPING REPORT
        ========================================
        Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Summary:
        - Scrapers Run: {len(results)}
        - Successful: {successful_scrapers}
        - Failed: {len(results) - successful_scrapers}
        
        Results:
        - Total Exhibitors Found: {total_found:,}
        - Total Exhibitors Processed & Saved: {total_processed:,}
        ========================================
        """
        logger.info(report)

        # --- ADDED: Save report to a file ---
        try:
            report_dir = Path("output/reports")
            report_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            report_path = report_dir / f"scraping_report_{timestamp}.txt"
            
            with open(report_path, 'w') as f:
                # Adding details of each scraper run to the file version
                detailed_report = report + "\n\n--- Run Details ---\n"
                for result in results:
                    if result.get('success'):
                        detailed_report += f"\n✅ {result.get('trade_show', 'Unknown')}: {result.get('exhibitors_found', 0)} found, {result.get('exhibitors_processed', 0)} processed"
                    else:
                        detailed_report += f"\n❌ {result.get('scraper', 'Unknown')}: {result.get('error', 'Unknown error')}"
                f.write(detailed_report)
            
            logger.info(f"📄 Scraping report saved to: {report_path}")

        except Exception as e:
            logger.error(f"Failed to save scraping report: {e}")
