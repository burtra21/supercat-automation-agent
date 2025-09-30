# scrapers/base_scraper.py
"""
Base scraper class that all trade show scrapers inherit from.
UPDATED to support connecting to a remote Scraping Browser (e.g., Bright Data)
via a WebSocket URL for maximum stealth and reliability.
"""

import asyncio
import logging
import random
from typing import Dict, List, Any, Optional
from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps

from playwright.async_api import async_playwright, Page, Browser, Playwright, TimeoutError as PlaywrightTimeoutError
from twocaptcha import TwoCaptcha

from database.connection import db
from config.settings import settings

logger = logging.getLogger(__name__)

def retry_async(retries=3, delay=5, backoff=2):
    """
    An async decorator to retry a function on failure with exponential backoff.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            _retries, _delay = retries, delay
            while _retries > 0:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    _retries -= 1
                    if _retries == 0:
                        logger.error(f"Function {func.__name__} failed after {retries} retries.")
                        raise
                    logger.warning(f"Function {func.__name__} failed with {e}. Retrying in {_delay} seconds...")
                    await asyncio.sleep(_delay)
                    _delay *= backoff
        return wrapper
    return decorator


class BaseTradeshowScraper(ABC):
    """Base class for all trade show scrapers using Playwright."""

    def __init__(self, trade_show_name: str, base_url: str):
        """Initialize the scraper."""
        self.trade_show_name = trade_show_name
        self.base_url = base_url
        self.trade_show_id: Optional[str] = None
        self.captcha_solver = TwoCaptcha(settings.twocaptcha_api_key) if settings.twocaptcha_api_key else None

    @abstractmethod
    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape general trade show information - must be implemented by child class."""
        pass

    @abstractmethod
    async def scrape_exhibitor_list(self, page: Page) -> List[Dict[str, Any]]:
        """Scrape the list of exhibitors - must be implemented by child class."""
        pass

    def validate_exhibitor_data(self, exhibitor: Dict) -> bool:
        """Validate that exhibitor data has required fields."""
        return 'company_name' in exhibitor and exhibitor['company_name']

    def clean_company_name(self, name: str) -> str:
        """Clean and standardize company name."""
        if not name: return ""
        suffixes = ['Inc.', 'LLC', 'Ltd.', 'Corp.', 'Corporation', 'Company', 'Co.']
        name = name.strip()
        for suffix in suffixes:
            if name.endswith(suffix):
                name = name[:-len(suffix)].strip()
        return name

    async def _save_and_link_exhibitor(self, exhibitor: Dict):
        """Saves a company and links it to the trade show as an exhibitor."""
        if self.validate_exhibitor_data(exhibitor):
            exhibitor['company_name'] = self.clean_company_name(exhibitor['company_name'])
            company_data = {
                'company_name': exhibitor['company_name'],
                'domain': exhibitor.get('website', ''),
                'source': f"{self.trade_show_name}_exhibitor"
            }
            company_record = db.upsert_company(company_data)

            if company_record and self.trade_show_id:
                exhibitor_link = {
                    'trade_show_id': self.trade_show_id,
                    'company_id': company_record['id'],
                    'booth_number': exhibitor.get('booth_number'),
                }
                db.link_exhibitor_to_show(exhibitor_link)
                return True
        return False

    @retry_async(retries=2, delay=10)
    async def run(self) -> Dict[str, Any]:
        """Main execution method using Playwright."""
        async with async_playwright() as p:
            browser = await self._get_browser(p)
            if not browser:
                return {'success': False, 'error': 'Failed to launch or connect to browser.'}
            
            try:
                context = await browser.new_context(
                    user_agent=self._get_random_user_agent(),
                    viewport={'width': 1920, 'height': 1080},
                    locale='en-US'
                )
                page = await context.new_page()
                await self._apply_stealth(page)

                logger.info(f"🚀 Starting scraper for {self.trade_show_name}")

                trade_show_data = await self.scrape_trade_show_info(page)
                if trade_show_data:
                    trade_show_record = db.upsert_trade_show(trade_show_data)
                    if trade_show_record:
                        self.trade_show_id = trade_show_record['id']

                exhibitors_raw = await self.scrape_exhibitor_list(page)

                processed_count = 0
                for exhibitor in exhibitors_raw:
                    if await self._save_and_link_exhibitor(exhibitor):
                        processed_count += 1
                
                logger.info(f"✅ Processed and saved {processed_count} exhibitors for {self.trade_show_name}")

                return {
                    'success': True,
                    'trade_show': self.trade_show_name,
                    'exhibitors_found': len(exhibitors_raw),
                    'exhibitors_processed': processed_count
                }

            except Exception as e:
                logger.error(f"❌ Scraper run failed for {self.trade_show_name}: {e}", exc_info=True)
                return {'success': False, 'error': str(e)}
            finally:
                if browser.is_connected():
                    await browser.close()

    async def _get_browser(self, p: Playwright) -> Optional[Browser]:
        """
        Connects to a remote scraping browser if WSS_URL is set, otherwise
        launches a local browser with a standard proxy.
        """
        if settings.BRIGHT_DATA_WSS_URL:
            logger.info("Connecting to Bright Data Scraping Browser...")
            return await p.chromium.connect_over_cdp(settings.BRIGHT_DATA_WSS_URL)
        else:
            logger.info("Launching local Playwright browser...")
            proxy_config = self._get_http_proxy()
            launch_options = {"headless": True}
            if proxy_config:
                launch_options["proxy"] = proxy_config
                logger.info(f"Using HTTP proxy: {proxy_config['server']}")
            return await p.chromium.launch(**launch_options)

    def _get_http_proxy(self) -> Optional[Dict[str, str]]:
        """
        Fetches standard HTTP proxy configuration for local browser fallback.
        """
        if settings.use_proxies and settings.proxy_list:
            proxy_url = random.choice(settings.proxy_list)
            try:
                auth, endpoint = proxy_url.split('@')
                user, password = auth.replace('http://', '').split(':')
                server = f"http://{endpoint}"
                return {"server": server, "username": user, "password": password}
            except ValueError:
                return {"server": proxy_url}
        return None

    async def _apply_stealth(self, page: Page):
        """Applies techniques to make Playwright harder to detect."""
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def _get_random_user_agent(self) -> str:
        """Provides a random, realistic User-Agent string."""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        ]
        return random.choice(user_agents)

    async def _simulate_human_behavior(self, page: Page):
        """Performs small, randomized actions to mimic a human user."""
        await asyncio.sleep(random.uniform(0.5, 1.5))
        await page.mouse.move(random.randint(50, 150), random.randint(50, 150))
        await asyncio.sleep(random.uniform(0.5, 1.0))

    async def _solve_captcha_if_present(self, page: Page) -> bool:
        """Detects and solves a reCAPTCHA if one is found on the page."""
        if not self.captcha_solver:
            return False
        try:
            captcha_frame = page.frame_locator('iframe[src*="recaptcha"]')
            await captcha_frame.locator('body').wait_for(timeout=5000)
            site_key_element = await captcha_frame.locator('.g-recaptcha').get_attribute('data-sitekey')
            if site_key_element:
                logger.info(f"reCAPTCHA detected with site key: {site_key_element}")
                result = self.captcha_solver.recaptcha(sitekey=site_key_element, url=page.url)
                if result and 'code' in result:
                    logger.info("CAPTCHA solved successfully. Submitting token.")
                    await page.evaluate(f'document.getElementById("g-recaptcha-response").innerHTML="{result["code"]}";')
                    await asyncio.sleep(3)
                    return True
                else:
                    logger.error("CAPTCHA solving failed.")
                    return False
        except PlaywrightTimeoutError:
            return False
        except Exception as e:
            logger.error(f"An error occurred during CAPTCHA solving: {e}")
            return False
