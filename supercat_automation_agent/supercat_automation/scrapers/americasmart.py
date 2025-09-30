# scrapers/americasmart.py
"""
Scraper for AmericasMart Atlanta trade show.
Enhanced version with robust loading strategies and multiple fallback approaches.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import asyncio
import random
import re
from bs4 import BeautifulSoup, Tag
from playwright.async_api import Page, TimeoutError as PlaywrightTimeoutError
from .base_scraper import BaseTradeshowScraper

logger = logging.getLogger(__name__)

class AmericasmartScraper(BaseTradeshowScraper):
    """Enhanced scraper for AmericasMart Atlanta with multiple strategies."""

    def __init__(self):
        super().__init__(
            trade_show_name="AmericasMart Atlanta",
            base_url="https://www.americasmart.com"
        )
        self.exhibitor_list_url = f"{self.base_url}/exhibitor/exhibitor-directory"
        self.exhibitors_collected = set()  # Track unique exhibitors

    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape AmericasMart Atlanta general information."""
        try:
            logger.info(f"Navigating to AmericasMart homepage: {self.base_url}")
            await page.goto(self.base_url, timeout=90000)
            await page.wait_for_load_state('networkidle')
            
            date_info = await self._extract_show_dates(page)
            
            return {
                'name': 'AmericasMart Atlanta',
                'location': 'Atlanta, GA',
                'venue': 'AmericasMart',
                'start_date': date_info.get('start_date', '2026-01-13'),
                'end_date': date_info.get('end_date', '2026-01-19'),
                'industry': 'Gift, Home, Rug',
                'website_url': self.base_url,
                'exhibitor_list_url': self.exhibitor_list_url,
                'last_scraped': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error scraping trade show info: {e}")
            return self._get_default_show_info()

    async def scrape_exhibitor_list(self, page: Page) -> List[Dict[str, Any]]:
        """Enhanced exhibitor scraping with multiple strategies."""
        exhibitors = []
        
        try:
            logger.info(f"Navigating to exhibitor directory: {self.exhibitor_list_url}")
            await page.goto(self.exhibitor_list_url, timeout=120000)
            await page.wait_for_load_state('networkidle')
            
            await self._handle_overlays(page)
            await self._wait_for_exhibitor_content(page)
            
            # Primary Strategy: Paginate through all pages
            await self._handle_pagination(page, exhibitors)
            
            logger.info(f"Successfully parsed {len(exhibitors)} unique exhibitors")
            
        except Exception as e:
            logger.error(f"Error in main scraping strategy: {e}")
        
        return exhibitors

    async def _handle_overlays(self, page: Page):
        """Handle popups, cookie banners, and overlays."""
        overlay_selectors = [
            "button#onetrust-accept-btn-handler", "button:has-text('Accept')",
            "button[aria-label='Close']", "button[class*='close']"
        ]
        for selector in overlay_selectors:
            try:
                elements = await page.locator(selector).all()
                for element in elements:
                    if await element.is_visible():
                        await element.click(timeout=2000)
                        logger.info(f"Clicked overlay element: {selector}")
                        await asyncio.sleep(1)
            except:
                continue

    async def _wait_for_exhibitor_content(self, page: Page):
        """Wait for exhibitor content to load."""
        content_selectors = [
            "div[data-testid='exhibitor-card']", "div.imc-exhibitor-card",
            "div[class*='directory']", "div[class*='listing']"
        ]
        for selector in content_selectors:
            try:
                await page.wait_for_selector(selector, timeout=10000)
                logger.info(f"Found content with selector: {selector}")
                return
            except:
                continue
        logger.warning("Could not find specific exhibitor content, waiting...")
        await asyncio.sleep(5)

    async def _handle_pagination(self, page: Page, exhibitors: List[Dict[str, Any]]):
        """Handle pagination by repeatedly clicking the 'Next' button."""
        next_page_selector = "a[aria-label='Next Page']"
        max_pages = 50

        for i in range(max_pages):
            logger.info(f"Scraping page {i + 1}...")
            await self._parse_page_content(page, exhibitors)
            
            try:
                next_button = page.locator(next_page_selector)
                if await next_button.is_disabled(timeout=5000):
                    logger.info("Next button is disabled. Reached the last page.")
                    break
                
                await self._simulate_human_behavior(page)
                await next_button.click()
                await page.wait_for_load_state('networkidle', timeout=30000)
            except Exception:
                logger.info("Could not find or click 'Next Page' button. Assuming end of list.")
                break

    async def _parse_page_content(self, page: Page, exhibitors: List[Dict[str, Any]]):
        """Parse the content of the current page for exhibitors."""
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        exhibitor_elements = self._find_all_exhibitor_elements(soup)
        
        for elem in exhibitor_elements:
            exhibitor = self._parse_exhibitor_comprehensive(elem)
            if exhibitor and exhibitor.get('company_name'):
                company_key = exhibitor['company_name'].lower().strip()
                if company_key not in self.exhibitors_collected:
                    self.exhibitors_collected.add(company_key)
                    exhibitors.append(exhibitor)

    def _find_all_exhibitor_elements(self, soup: BeautifulSoup) -> List[Tag]:
        """Find exhibitor elements using comprehensive selectors."""
        selectors = [
            "div[data-testid='exhibitor-card']", "div.imc-exhibitor-card",
            "div[class*='exhibitor-item']", "div[class*='vendor-card']"
        ]
        all_elements = []
        for selector in selectors:
            all_elements.extend(soup.select(selector))
        return all_elements

    def _parse_exhibitor_comprehensive(self, element: Tag) -> Optional[Dict[str, Any]]:
        """Parse exhibitor with multiple extraction strategies."""
        try:
            company_name = self._extract_company_name(element)
            if not company_name:
                return None
            
            return {
                'company_name': company_name,
                'website': self._extract_website(element),
                'booth_number': self._extract_booth_info(element).get('booth_number'),
                'building': self._extract_booth_info(element).get('building'),
                'categories': self._extract_categories(element)
            }
        except Exception as e:
            logger.debug(f"Error parsing exhibitor element: {e}")
            return None

    def _extract_company_name(self, element: Tag) -> Optional[str]:
        """Extract company name using multiple strategies."""
        name_selectors = [
            "h3[data-testid='exhibitor-name'] a", "h3.imc-exhibitor-card__name a",
            "div[class*='-name']", "div[class*='-title']"
        ]
        for selector in name_selectors:
            tag = element.select_one(selector)
            if tag and tag.text.strip():
                return tag.text.strip()
        return None

    def _extract_website(self, element: Tag) -> Optional[str]:
        """Extract website URL."""
        for link in element.find_all('a', href=True):
            href = link['href']
            if href.startswith('http') and 'americasmart.com' not in href:
                return href
        return None

    def _extract_booth_info(self, element: Tag) -> Dict[str, Any]:
        """Extract booth number and location information."""
        booth_info = {}
        location_tag = element.select_one("p[data-testid='exhibitor-location']")
        if location_tag:
            booth_info['booth_number'] = location_tag.text.strip()
        return booth_info

    def _extract_categories(self, element: Tag) -> Optional[str]:
        """Extract product categories."""
        categories_tag = element.select_one("p[data-testid='exhibitor-categories']")
        if categories_tag:
            return categories_tag.text.strip()
        return None

    async def _extract_show_dates(self, page: Page) -> Dict[str, str]:
        """Try to extract actual show dates from the page."""
        # This is a placeholder; a real implementation would need a robust date-finding logic
        return {}

    def _get_default_show_info(self) -> Dict[str, Any]:
        """Return default show information as fallback."""
        return {
            'name': 'AmericasMart Atlanta',
            'location': 'Atlanta, GA',
            'venue': 'AmericasMart',
            'start_date': '2026-01-13',
            'end_date': '2026-01-19',
            'industry': 'Gift, Home, Rug',
            'website_url': self.base_url,
            'exhibitor_list_url': self.exhibitor_list_url,
            'last_scraped': datetime.now().isoformat()
        }
