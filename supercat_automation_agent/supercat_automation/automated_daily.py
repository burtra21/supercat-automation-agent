# automated_daily.py
'''Automated daily runner for SuperCat GTM'''

import schedule
import time
import logging
from datetime import datetime
import asyncio
from full_orchestrator import SupercatFullOrchestrator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/daily_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DailyAutomation:
    '''Runs SuperCat automation on schedule'''
    
    def __init__(self):
        self.orchestrator = SupercatFullOrchestrator()
        self.run_count = 0
    
    def morning_run(self):
        '''Morning pipeline run - full analysis'''
        logger.info("=" * 60)
        logger.info("🌅 MORNING RUN STARTING")
        logger.info(f"Run #{self.run_count + 1} at {datetime.now()}")
        
        try:
            asyncio.run(self.orchestrator.run_complete_pipeline(mode='full'))
            self.run_count += 1
            logger.info("✅ Morning run completed successfully")
        except Exception as e:
            logger.error(f"❌ Morning run failed: {e}")
    
    def afternoon_run(self):
        '''Afternoon run - campaigns only'''
        logger.info("=" * 60)
        logger.info("🌆 AFTERNOON RUN STARTING")
        
        try:
            asyncio.run(self.orchestrator.run_complete_pipeline(mode='campaign_only'))
            logger.info("✅ Afternoon run completed successfully")
        except Exception as e:
            logger.error(f"❌ Afternoon run failed: {e}")
    
    def health_check(self):
        '''Hourly health check'''
        logger.info(f"💓 Health check - System running - Runs completed: {self.run_count}")
    
    def start(self):
        '''Start the scheduler'''
        
        # Schedule runs
        schedule.every().day.at("09:00").do(self.morning_run)
        schedule.every().day.at("14:00").do(self.afternoon_run)
        schedule.every().hour.do(self.health_check)
        
        # Run immediately on start
        logger.info("🚀 Daily Automation Started")
        logger.info("Scheduled:")
        logger.info("  - Morning run: 9:00 AM")
        logger.info("  - Afternoon run: 2:00 PM")
        logger.info("  - Health checks: Every hour")
        
        # Run once immediately
        self.morning_run()
        
        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    automation = DailyAutomation()
    automation.start()
