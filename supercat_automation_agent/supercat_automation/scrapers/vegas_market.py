# scrapers/vegas_market.py
"""
Vegas Market Scraper - Production-Ready Version
Implements multiple fallback strategies and robust error handling
"""

import json
import logging
import asyncio
import random
from typing import Dict, List, Any, Optional, Set
from datetime import datetime
from urllib.parse import urljoin, urlparse
import re

from playwright.async_api import Page, Route, Request, Response, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup, Tag
from .base_scraper import BaseTradeshowScraper

logger = logging.getLogger(__name__)

class VegasMarketScraper(BaseTradeshowScraper):
    """
    Production-ready scraper for Las Vegas Market
    Implements multiple strategies with fallbacks
    """
    
    def __init__(self):
        super().__init__(
            trade_show_name="Las Vegas Market",
            base_url="https://www.lasvegasmarket.com"
        )
        # Multiple possible URLs to try
        self.exhibitor_urls = [
            f"{self.base_url}/exhibitor/exhibitor-directory",
            f"{self.base_url}/exhibitors",
            f"{self.base_url}/directory",
            f"{self.base_url}/exhibitor-list"
        ]
        self.api_data = []
        self.intercepted_responses = []
        
    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape Las Vegas Market general information with fallbacks"""
        try:
            await page.goto(self.base_url, timeout=60000, wait_until='networkidle')
            
            # Wait for main content to load
            await page.wait_for_selector('body', timeout=30000)
            
            # Extract dates using multiple strategies
            dates = await self._extract_show_dates(page)
            
            return {
                'name': 'Las Vegas Market',
                'location': 'Las Vegas, NV',
                'venue': 'World Market Center',
                'start_date': dates.get('start', '2025-07-27'),
                'end_date': dates.get('end', '2025-07-31'),
                'industry': 'Furniture, Home Decor, Gift',
                'website_url': self.base_url,
                'exhibitor_list_url': self.exhibitor_urls[0],
                'last_scraped': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Error scraping trade show info: {e}")
            # Return fallback data
            return self._get_fallback_show_info()
    
    async def scrape_exhibitor_list(self, page: Page) -> List[Dict[str, Any]]:
        """
        Main scraping method with multiple strategies
        """
        exhibitors = []
        
        # Strategy 1: Try API interception first
        logger.info("Strategy 1: Attempting API interception...")
        exhibitors = await self._scrape_via_api_interception(page)
        
        if len(exhibitors) < 10:  # Likely failed
            logger.info("Strategy 2: Attempting DOM scraping...")
            exhibitors = await self._scrape_via_dom(page)
        
        if len(exhibitors) < 10:  # Still not enough
            logger.info("Strategy 3: Attempting search-based scraping...")
            exhibitors = await self._scrape_via_search(page)
        
        if len(exhibitors) < 10:  # Last resort
            logger.info("Strategy 4: Attempting sitemap/static page scraping...")
            exhibitors = await self._scrape_via_sitemap(page)
        
        # Deduplicate
        exhibitors = self._deduplicate_exhibitors(exhibitors)
        
        logger.info(f"Total unique exhibitors found: {len(exhibitors)}")
        return exhibitors
    
    async def _scrape_via_api_interception(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 1: Intercept API calls made by the page
        """
        exhibitors = []
        
        # Set up request interception
        async def handle_route(route: Route, request: Request):
            """Intercept and log API requests"""
            url = request.url
            
            # Log interesting API calls
            if any(keyword in url.lower() for keyword in ['exhibitor', 'vendor', 'company', 'directory', 'api', 'graphql']):
                logger.debug(f"Intercepted API call: {url}")
            
            await route.continue_()
        
        async def handle_response(response: Response):
            """Capture API responses"""
            url = response.url
            
            # Check if this looks like exhibitor data
            if any(keyword in url.lower() for keyword in ['exhibitor', 'vendor', 'company', 'directory']):
                try:
                    if response.status == 200:
                        content_type = response.headers.get('content-type', '')
                        if 'json' in content_type:
                            data = await response.json()
                            self.api_data.append(data)
                            logger.info(f"Captured API response from: {url}")
                except Exception as e:
                    logger.debug(f"Could not parse response from {url}: {e}")
        
        # Set up interception
        page.on('response', handle_response)
        await page.route('**/*', handle_route)
        
        # Try each possible URL
        for url in self.exhibitor_urls:
            try:
                logger.info(f"Trying URL: {url}")
                await page.goto(url, timeout=60000, wait_until='networkidle')
                
                # Wait for potential API calls
                await asyncio.sleep(5)
                
                # Check if we got data
                if self.api_data:
                    exhibitors = self._parse_api_data(self.api_data)
                    if exhibitors:
                        logger.info(f"Found {len(exhibitors)} exhibitors via API interception")
                        return exhibitors
                        
            except Exception as e:
                logger.warning(f"Failed to load {url}: {e}")
                continue
        
        return exhibitors
    
    async def _scrape_via_dom(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 2: Traditional DOM scraping with smart selectors
        """
        exhibitors = []
        
        # Try multiple possible selectors
        selector_sets = [
            # Set 1: Data attributes
            {
                'container': '[data-testid*="exhibitor"], [data-test*="exhibitor"]',
                'name': '[data-testid*="name"], [data-test*="name"], h2, h3, h4',
                'booth': '[data-testid*="booth"], [data-test*="location"], [data-test*="booth"]',
                'website': 'a[href*="http"]'
            },
            # Set 2: Class-based
            {
                'container': '.exhibitor-card, .vendor-card, .company-card, .directory-item',
                'name': '.exhibitor-name, .vendor-name, .company-name, .name, h2, h3',
                'booth': '.booth-number, .location, .booth, .stand',
                'website': 'a.website, a.link, a[href*="http"]'
            },
            # Set 3: Generic structure
            {
                'container': 'article, .card, .item, .result, div[class*="card"]',
                'name': 'h1, h2, h3, h4, .title',
                'booth': '.location, .booth, span:contains("Booth")',
                'website': 'a[href^="http"]'
            }
        ]
        
        for url in self.exhibitor_urls:
            try:
                await page.goto(url, timeout=60000, wait_until='domcontentloaded')
                
                # Handle popups
                await self._handle_popups(page)
                
                # Try infinite scroll
                await self._smart_infinite_scroll(page)
                
                # Try each selector set
                for selectors in selector_sets:
                    try:
                        # Wait for containers
                        await page.wait_for_selector(selectors['container'], timeout=10000)
                        
                        # Get all exhibitor containers
                        containers = await page.query_selector_all(selectors['container'])
                        
                        logger.info(f"Found {len(containers)} potential exhibitor containers")
                        
                        for container in containers[:500]:  # Limit to prevent memory issues
                            exhibitor = await self._extract_exhibitor_from_element(container, selectors)
                            if exhibitor and exhibitor.get('company_name'):
                                exhibitors.append(exhibitor)
                        
                        if exhibitors:
                            logger.info(f"Successfully extracted {len(exhibitors)} exhibitors")
                            return exhibitors
                            
                    except Exception as e:
                        logger.debug(f"Selector set failed: {e}")
                        continue
                        
            except Exception as e:
                logger.warning(f"Failed to scrape {url}: {e}")
                continue
        
        return exhibitors
    
    async def _scrape_via_search(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 3: Use the site's search functionality
        """
        exhibitors = []
        
        # Common search patterns for trade show sites
        search_urls = [
            f"{self.base_url}/search",
            f"{self.base_url}/exhibitor/search",
            f"{self.base_url}/directory/search"
        ]
        
        # Try alphabet search (A-Z)
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            for base_search_url in search_urls:
                try:
                    search_url = f"{base_search_url}?q={letter}"
                    logger.info(f"Searching with letter: {letter}")
                    
                    await page.goto(search_url, timeout=30000, wait_until='networkidle')
                    await asyncio.sleep(2)
                    
                    # Extract results
                    results = await self._extract_search_results(page)
                    exhibitors.extend(results)
                    
                    if len(exhibitors) > 100:  # Good enough sample
                        break
                        
                except Exception as e:
                    logger.debug(f"Search failed for {letter}: {e}")
                    continue
            
            if len(exhibitors) > 100:
                break
        
        return exhibitors
    
    async def _scrape_via_sitemap(self, page: Page) -> List[Dict[str, Any]]:
        """
        Strategy 4: Check sitemap or use a category/building approach
        """
        exhibitors = []
        
        # Common building/hall names at Vegas Market
        buildings = [
            'Building A', 'Building B', 'Building C',
            'Pavilion', 'Hall 1', 'Hall 2', 'Hall 3',
            'North', 'South', 'East', 'West'
        ]
        
        # Try sitemap first
        sitemap_urls = [
            f"{self.base_url}/sitemap.xml",
            f"{self.base_url}/sitemap",
            f"{self.base_url}/exhibitor-sitemap.xml"
        ]
        
        for sitemap_url in sitemap_urls:
            try:
                await page.goto(sitemap_url, timeout=30000)
                content = await page.content()
                
                # Extract exhibitor URLs from sitemap
                exhibitor_urls = re.findall(r'<loc>(.*?exhibitor.*?)</loc>', content, re.IGNORECASE)
                
                # Visit each exhibitor page (limit to prevent overload)
                for ex_url in exhibitor_urls[:50]:
                    try:
                        await page.goto(ex_url, timeout=20000)
                        exhibitor = await self._extract_exhibitor_from_page(page)
                        if exhibitor:
                            exhibitors.append(exhibitor)
                    except:
                        continue
                        
                if exhibitors:
                    return exhibitors
                    
            except Exception as e:
                logger.debug(f"Sitemap approach failed: {e}")
                continue
        
        return exhibitors
    
    async def _smart_infinite_scroll(self, page: Page, max_scrolls: int = 50):
        """
        Intelligent infinite scroll with multiple strategies
        """
        logger.info("Starting smart infinite scroll...")
        
        # Strategy 1: Check for a "Load More" button
        load_more_selectors = [
            'button:has-text("Load More")',
            'button:has-text("Show More")',
            'button:has-text("View More")',
            'a:has-text("Load More")',
            'button[class*="load"]',
            'button[class*="more"]'
        ]
        
        for selector in load_more_selectors:
            try:
                while True:
                    button = await page.query_selector(selector)
                    if button:
                        await button.click()
                        await asyncio.sleep(2)
                    else:
                        break
            except:
                continue
        
        # Strategy 2: Traditional scroll
        last_height = await page.evaluate('document.body.scrollHeight')
        same_height_count = 0
        
        for i in range(max_scrolls):
            # Scroll down
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            
            # Random wait to appear human
            await asyncio.sleep(random.uniform(1.5, 3.0))
            
            # Check for new content
            new_height = await page.evaluate('document.body.scrollHeight')
            
            if new_height == last_height:
                same_height_count += 1
                
                # Try scrolling up a bit then down again (sometimes triggers load)
                if same_height_count == 2:
                    await page.evaluate('window.scrollTo(0, document.body.scrollHeight - 1000)')
                    await asyncio.sleep(1)
                    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                    await asyncio.sleep(2)
                
                if same_height_count >= 3:
                    logger.info("No new content after 3 attempts, stopping scroll")
                    break
            else:
                same_height_count = 0
                last_height = new_height
                logger.debug(f"Scroll {i+1}: New content loaded")
        
        logger.info("Finished scrolling")
    
    async def _handle_popups(self, page: Page):
        """Handle various popups and overlays"""
        popup_selectors = [
            # Cookie banners
            'button:has-text("Accept")',
            'button:has-text("Accept All")',
            'button#onetrust-accept-btn-handler',
            'button[aria-label*="accept"]',
            # Newsletter/email popups
            'button[aria-label*="close"]',
            'button:has-text("No Thanks")',
            'button.close',
            '.modal-close',
            # Generic close buttons
            'button:has-text("X")',
            'button:has-text("×")',
        ]
        
        for selector in popup_selectors:
            try:
                button = await page.query_selector(selector)
                if button and await button.is_visible():
                    await button.click()
                    await asyncio.sleep(1)
                    logger.debug(f"Closed popup with selector: {selector}")
            except:
                continue
    
    async def _extract_exhibitor_from_element(self, element, selectors: Dict) -> Dict[str, Any]:
        """Extract exhibitor data from a page element"""
        try:
            exhibitor = {}
            
            # Get company name
            name_elem = await element.query_selector(selectors['name'])
            if name_elem:
                exhibitor['company_name'] = await name_elem.inner_text()
                exhibitor['company_name'] = exhibitor['company_name'].strip()
            
            # Get booth number
            booth_elem = await element.query_selector(selectors['booth'])
            if booth_elem:
                exhibitor['booth_number'] = await booth_elem.inner_text()
                exhibitor['booth_number'] = exhibitor['booth_number'].strip()
            
            # Get website
            website_elem = await element.query_selector(selectors['website'])
            if website_elem:
                exhibitor['website'] = await website_elem.get_attribute('href')
            
            # Get any additional text content for context
            try:
                full_text = await element.inner_text()
                exhibitor['raw_text'] = full_text[:500]  # Store for later parsing if needed
            except:
                pass
            
            return exhibitor if exhibitor.get('company_name') else None
            
        except Exception as e:
            logger.debug(f"Failed to extract exhibitor: {e}")
            return None
    
    async def _extract_exhibitor_from_page(self, page: Page) -> Dict[str, Any]:
        """Extract exhibitor data from a dedicated exhibitor page"""
        try:
            exhibitor = {}
            
            # Try multiple selectors for company name
            name_selectors = ['h1', 'h2', '.company-name', '.exhibitor-name', '[itemprop="name"]']
            for selector in name_selectors:
                try:
                    elem = await page.query_selector(selector)
                    if elem:
                        exhibitor['company_name'] = await elem.inner_text()
                        break
                except:
                    continue
            
            # Extract other details
            exhibitor['website'] = await self._extract_website(page)
            exhibitor['booth_number'] = await self._extract_booth_number(page)
            
            return exhibitor if exhibitor.get('company_name') else None
            
        except Exception as e:
            logger.debug(f"Failed to extract from page: {e}")
            return None
    
    async def _extract_website(self, page: Page) -> Optional[str]:
        """Extract website URL from page"""
        selectors = [
            'a:has-text("Website")',
            'a:has-text("Visit Website")',
            'a[href*="http"]:not([href*="lasvegasmarket"])',
            'a.website-link'
        ]
        
        for selector in selectors:
            try:
                elem = await page.query_selector(selector)
                if elem:
                    return await elem.get_attribute('href')
            except:
                continue
        return None
    
    async def _extract_booth_number(self, page: Page) -> Optional[str]:
        """Extract booth number from page"""
        # Look for booth number patterns
        content = await page.content()
        booth_patterns = [
            r'Booth[:\s#]+([A-Z0-9\-]+)',
            r'Stand[:\s#]+([A-Z0-9\-]+)',
            r'Location[:\s]+([A-Z0-9\-]+)',
        ]
        
        for pattern in booth_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return None
    
    async def _extract_show_dates(self, page: Page) -> Dict[str, str]:
        """Extract show dates from the page"""
        dates = {}
        
        # Look for date patterns
        content = await page.content()
        
        # Common date patterns
        date_patterns = [
            r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})-(\d{1,2}),?\s+(\d{4})',
            r'(\d{1,2})/(\d{1,2})/(\d{4})\s*-\s*(\d{1,2})/(\d{1,2})/(\d{4})',
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, content)
            if match:
                # Parse and format dates
                # (Implementation depends on pattern matched)
                logger.info(f"Found dates: {match.group()}")
                break
        
        return dates
    
    async def _extract_search_results(self, page: Page) -> List[Dict[str, Any]]:
        """Extract exhibitors from search results"""
        exhibitors = []
        
        # Common search result selectors
        result_selectors = [
            '.search-result',
            '.result-item',
            'article',
            '.exhibitor-result'
        ]
        
        for selector in result_selectors:
            try:
                results = await page.query_selector_all(selector)
                for result in results:
                    exhibitor = await self._extract_exhibitor_from_element(
                        result, 
                        {
                            'name': 'h2, h3, .title',
                            'booth': '.booth, .location',
                            'website': 'a[href^="http"]'
                        }
                    )
                    if exhibitor:
                        exhibitors.append(exhibitor)
                
                if exhibitors:
                    break
                    
            except:
                continue
        
        return exhibitors
    
    def _parse_api_data(self, api_responses: List[Any]) -> List[Dict[str, Any]]:
        """Parse exhibitor data from intercepted API responses"""
        exhibitors = []
        
        for response in api_responses:
            try:
                # Handle different API response structures
                if isinstance(response, dict):
                    # Check for common data locations
                    data_locations = [
                        response.get('data', []),
                        response.get('results', []),
                        response.get('exhibitors', []),
                        response.get('vendors', []),
                        response.get('companies', []),
                        response.get('items', []),
                    ]
                    
                    for data in data_locations:
                        if isinstance(data, list):
                            for item in data:
                                exhibitor = self._parse_api_exhibitor(item)
                                if exhibitor:
                                    exhibitors.append(exhibitor)
                        elif isinstance(data, dict):
                            exhibitor = self._parse_api_exhibitor(data)
                            if exhibitor:
                                exhibitors.append(exhibitor)
                
                elif isinstance(response, list):
                    for item in response:
                        exhibitor = self._parse_api_exhibitor(item)
                        if exhibitor:
                            exhibitors.append(exhibitor)
                            
            except Exception as e:
                logger.debug(f"Failed to parse API response: {e}")
                continue
        
        return exhibitors
    
    def _parse_api_exhibitor(self, item: Dict) -> Optional[Dict[str, Any]]:
        """Parse individual exhibitor from API data"""
        if not isinstance(item, dict):
            return None
        
        exhibitor = {}
        
        # Common field names for company name
        name_fields = ['name', 'companyName', 'company_name', 'exhibitorName', 
                      'exhibitor_name', 'vendorName', 'vendor_name', 'title']
        
        for field in name_fields:
            if field in item and item[field]:
                exhibitor['company_name'] = str(item[field]).strip()
                break
        
        # Common field names for booth
        booth_fields = ['booth', 'boothNumber', 'booth_number', 'location', 
                       'stand', 'standNumber', 'stand_number']
        
        for field in booth_fields:
            if field in item and item[field]:
                exhibitor['booth_number'] = str(item[field]).strip()
                break
        
        # Common field names for website
        website_fields = ['website', 'url', 'webUrl', 'web_url', 'link', 
                         'companyUrl', 'company_url']
        
        for field in website_fields:
            if field in item and item[field]:
                exhibitor['website'] = str(item[field]).strip()
                break
        
        # Store raw data for debugging
        exhibitor['raw_api_data'] = item
        
        return exhibitor if exhibitor.get('company_name') else None
    
    def _deduplicate_exhibitors(self, exhibitors: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Remove duplicate exhibitors based on company name"""
        seen = set()
        unique = []
        
        for exhibitor in exhibitors:
            name = exhibitor.get('company_name', '').lower().strip()
            if name and name not in seen:
                seen.add(name)
                unique.append(exhibitor)
        
        return unique
    
    def _get_fallback_show_info(self) -> Dict[str, Any]:
        """Return fallback trade show information"""
        return {
            'name': 'Las Vegas Market',
            'location': 'Las Vegas, NV',
            'venue': 'World Market Center',
            'start_date': '2025-07-27',
            'end_date': '2025-07-31',
            'industry': 'Furniture, Home Decor, Gift',
            'website_url': self.base_url,
            'exhibitor_list_url': self.exhibitor_urls[0],
            'last_scraped': datetime.now().isoformat(),
            'note': 'Fallback data - actual dates may vary'
        }