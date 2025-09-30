# scrapers/high_point.py
"""
Scraper for High Point Market trade show.
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

class HighPointMarketScraper(BaseTradeshowScraper):
    """Enhanced scraper for High Point Market with multiple strategies."""

    def __init__(self):
        super().__init__(
            trade_show_name="High Point Market",
            base_url="https://www.highpointmarket.org"
        )
        self.exhibitor_list_url = f"{self.base_url}/exhibitor"
        self.exhibitors_collected = set()  # Track unique exhibitors

    async def scrape_trade_show_info(self, page: Page) -> Dict[str, Any]:
        """Scrape High Point Market general information."""
        try:
            logger.info(f"Navigating to High Point Market homepage: {self.base_url}")
            await page.goto(self.base_url, timeout=90000)
            await page.wait_for_load_state('networkidle')
            
            # Try to extract actual dates from the page
            date_info = await self._extract_show_dates(page)
            
            return {
                'name': 'High Point Market',
                'location': 'High Point, NC',
                'venue': 'High Point Market Authority',
                'start_date': date_info.get('start_date', '2025-04-26'),  # Spring 2025 market
                'end_date': date_info.get('end_date', '2025-04-30'),
                'industry': 'Furniture, Home Decor, Lighting',
                'estimated_attendance': 75000,
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
            
            # Navigate with extended timeout
            await page.goto(self.exhibitor_list_url, timeout=120000)
            await page.wait_for_load_state('networkidle')
            
            # Handle any popups or overlays
            await self._handle_overlays(page)
            
            # Wait for initial content to load
            await self._wait_for_exhibitor_content(page)
            
            # Strategy 1: Try to load all exhibitors using the Load More button
            await self._load_all_exhibitors(page)
            
            # Get the page content
            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            
            # Strategy 2: Find exhibitor elements using multiple selectors
            exhibitor_elements = self._find_all_exhibitor_elements(soup)
            logger.info(f"Found {len(exhibitor_elements)} potential exhibitor elements")
            
            # Parse each element
            for elem in exhibitor_elements:
                exhibitor = self._parse_exhibitor_comprehensive(elem)
                if exhibitor and exhibitor.get('company_name'):
                    # Avoid duplicates
                    company_key = exhibitor['company_name'].lower().strip()
                    if company_key not in self.exhibitors_collected:
                        self.exhibitors_collected.add(company_key)
                        exhibitors.append(exhibitor)
            
            logger.info(f"Successfully parsed {len(exhibitors)} unique exhibitors")
            
            # If we got very few results, try alternative strategies
            if len(exhibitors) < 50:
                logger.warning(f"Only found {len(exhibitors)} exhibitors, trying alternative methods...")
                additional = await self._try_alternative_strategies(page)
                for exhibitor in additional:
                    company_key = exhibitor['company_name'].lower().strip()
                    if company_key not in self.exhibitors_collected:
                        self.exhibitors_collected.add(company_key)
                        exhibitors.append(exhibitor)
                
                logger.info(f"Total exhibitors after alternative strategies: {len(exhibitors)}")
            
        except Exception as e:
            logger.error(f"Error in main scraping strategy: {e}")
            # Fallback to JavaScript extraction
            exhibitors = await self._javascript_extraction(page)
        
        return exhibitors

    async def _handle_overlays(self, page: Page):
        """Handle popups, cookie banners, and overlays."""
        overlay_selectors = [
            # Cookie consent
            "button#onetrust-accept-btn-handler",
            "button[id*='accept-cookies']",
            "button[class*='cookie-accept']",
            "button:has-text('Accept')",
            "button:has-text('I Agree')",
            
            # Newsletter/popup close buttons
            "button[aria-label='Close']",
            "button[class*='close']",
            "a[class*='close']",
            "div[class*='modal'] button[class*='close']",
            
            # Skip or dismiss buttons
            "button:has-text('Skip')",
            "button:has-text('No Thanks')",
            "button:has-text('Maybe Later')"
        ]
        
        for selector in overlay_selectors:
            try:
                elements = await page.locator(selector).all()
                for element in elements[:3]:  # Only try first 3 matches
                    if await element.is_visible():
                        await element.click()
                        logger.info(f"Clicked overlay element: {selector}")
                        await asyncio.sleep(1)
            except:
                continue

    async def _wait_for_exhibitor_content(self, page: Page):
        """Wait for exhibitor content to load using multiple strategies."""
        content_selectors = [
            # Known High Point selectors
            "div.exhibitors-list",
            "div.exhibitor-tile",
            "div[class*='exhibitor-card']",
            "article[class*='exhibitor']",
            
            # Generic patterns
            "div[class*='directory']",
            "div[class*='listing']",
            "div[class*='vendor']",
            "div[class*='company-card']",
            
            # Data attributes
            "[data-exhibitor]",
            "[data-vendor]",
            "[data-company]"
        ]
        
        for selector in content_selectors:
            try:
                await page.wait_for_selector(selector, timeout=10000)
                logger.info(f"Found content with selector: {selector}")
                return
            except:
                continue
        
        # If no specific selector worked, wait a bit for any content
        logger.warning("Could not find specific exhibitor content, waiting for general content...")
        await asyncio.sleep(5)

    async def _load_all_exhibitors(self, page: Page):
        """Load all exhibitors using various loading strategies."""
        logger.info("Starting to load all exhibitors...")
        
        # Strategy 1: Click Load More button repeatedly
        load_more_count = await self._click_load_more_buttons(page)
        
        # Strategy 2: Scroll to load lazy-loaded content
        if load_more_count < 5:  # If we didn't find many load more buttons, try scrolling
            await self._infinite_scroll(page)
        
        # Strategy 3: Check for pagination
        await self._handle_pagination(page)

    async def _click_load_more_buttons(self, page: Page) -> int:
        """Click all variations of load more buttons."""
        load_more_selectors = [
            "button.exhibitors-load-more-button",
            "button:has-text('Load More')",
            "button:has-text('Show More')",
            "button:has-text('View More')",
            "a:has-text('Load More')",
            "button[class*='load-more']",
            "button[class*='show-more']",
            "div[class*='load-more'] button",
            "[data-action='load-more']"
        ]
        
        clicks = 0
        max_clicks = 50
        
        for selector in load_more_selectors:
            consecutive_failures = 0
            
            while clicks < max_clicks and consecutive_failures < 3:
                try:
                    button = page.locator(selector).first
                    
                    # Check if button exists and is visible
                    if await button.count() > 0 and await button.is_visible():
                        # Scroll button into view
                        await button.scroll_into_view_if_needed()
                        await asyncio.sleep(0.5)
                        
                        # Click the button
                        await button.click()
                        clicks += 1
                        consecutive_failures = 0
                        
                        logger.info(f"Clicked '{selector}' button (total clicks: {clicks})")
                        
                        # Wait for new content to load
                        await asyncio.sleep(random.uniform(2.0, 4.0))
                    else:
                        consecutive_failures += 1
                        
                except Exception as e:
                    consecutive_failures += 1
                    if consecutive_failures == 1:
                        logger.debug(f"Could not click {selector}: {e}")
        
        logger.info(f"Total load more clicks: {clicks}")
        return clicks

    async def _infinite_scroll(self, page: Page):
        """Perform infinite scrolling to load content."""
        logger.info("Starting infinite scroll...")
        
        last_height = await page.evaluate("document.body.scrollHeight")
        same_height_count = 0
        max_scrolls = 30
        
        for i in range(max_scrolls):
            # Scroll to bottom
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            
            # Wait for content to load
            await asyncio.sleep(random.uniform(2.0, 4.0))
            
            # Check new height
            new_height = await page.evaluate("document.body.scrollHeight")
            
            if new_height == last_height:
                same_height_count += 1
                if same_height_count >= 3:
                    logger.info("Page height unchanged for 3 iterations, stopping scroll")
                    break
            else:
                same_height_count = 0
                logger.info(f"Scroll {i+1}: Height increased from {last_height} to {new_height}")
            
            last_height = new_height
            
            # Also try clicking load more during scroll
            try:
                load_more = page.locator("button:has-text('Load More')").first
                if await load_more.is_visible():
                    await load_more.click()
                    await asyncio.sleep(3)
            except:
                pass

    async def _handle_pagination(self, page: Page):
        """Handle pagination if present."""
        pagination_selectors = [
            "a[class*='pagination']",
            "button[class*='page-next']",
            "a:has-text('Next')",
            "button:has-text('Next')",
            "[aria-label='Next page']"
        ]
        
        pages_loaded = 0
        max_pages = 10
        
        for selector in pagination_selectors:
            while pages_loaded < max_pages:
                try:
                    next_button = page.locator(selector).first
                    if await next_button.is_visible():
                        await next_button.click()
                        pages_loaded += 1
                        logger.info(f"Navigated to page {pages_loaded + 1}")
                        await asyncio.sleep(3)
                    else:
                        break
                except:
                    break

    def _find_all_exhibitor_elements(self, soup: BeautifulSoup) -> List[Tag]:
        """Find exhibitor elements using comprehensive selectors."""
        all_elements = []
        seen_texts = set()
        
        # High Point specific selectors
        selectors = [
            "div.exhibitor-tile",
            "div.exhibitor-card",
            "article.exhibitor",
            "div[class*='exhibitor-item']",
            "div[class*='vendor-card']",
            "div[class*='company-listing']"
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for elem in elements:
                # Check for unique content to avoid duplicates
                text_content = elem.get_text(strip=True)[:100]  # First 100 chars as key
                if text_content and text_content not in seen_texts:
                    seen_texts.add(text_content)
                    all_elements.append(elem)
        
        # Also look for generic patterns
        generic_patterns = [
            {"name": "div", "class": re.compile(r"exhibitor|vendor|company|listing", re.I)},
            {"name": "article", "class": re.compile(r"card|item|tile", re.I)},
            {"name": "li", "class": re.compile(r"exhibitor|vendor|company", re.I)}
        ]
        
        for pattern in generic_patterns:
            elements = soup.find_all(**pattern)
            for elem in elements:
                text_content = elem.get_text(strip=True)[:100]
                if text_content and text_content not in seen_texts:
                    # Verify it looks like an exhibitor (has a name-like element)
                    if elem.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong']):
                        seen_texts.add(text_content)
                        all_elements.append(elem)
        
        logger.info(f"Found {len(all_elements)} unique potential exhibitor elements")
        return all_elements

    def _parse_exhibitor_comprehensive(self, element: Tag) -> Optional[Dict[str, Any]]:
        """Parse exhibitor with multiple extraction strategies."""
        try:
            exhibitor_data = {}
            
            # Extract company name (multiple strategies)
            company_name = self._extract_company_name(element)
            if not company_name:
                return None
            
            exhibitor_data['company_name'] = company_name
            
            # Extract website
            website = self._extract_website(element)
            if website:
                exhibitor_data['website'] = website
            
            # Extract booth information
            booth_info = self._extract_booth_info(element)
            if booth_info:
                exhibitor_data.update(booth_info)
            
            # Extract contact information
            contact_info = self._extract_contact_info(element)
            if contact_info:
                exhibitor_data.update(contact_info)
            
            # Extract categories/products
            categories = self._extract_categories(element)
            if categories:
                exhibitor_data['categories'] = categories
            
            return exhibitor_data
            
        except Exception as e:
            logger.debug(f"Error parsing exhibitor element: {e}")
            return None

    def _extract_company_name(self, element: Tag) -> Optional[str]:
        """Extract company name using multiple strategies."""
        # Strategy 1: Look in headings
        for heading_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            heading = element.find(heading_tag)
            if heading:
                # Get text, excluding nested elements
                name = heading.get_text(strip=True)
                if name and len(name) > 2:
                    return name
        
        # Strategy 2: Look for specific classes
        name_classes = ['exhibitor-name', 'company-name', 'vendor-name', 'title', 'name']
        for class_name in name_classes:
            name_elem = element.find(class_=re.compile(class_name, re.I))
            if name_elem:
                name = name_elem.get_text(strip=True)
                if name and len(name) > 2:
                    return name
        
        # Strategy 3: Look in links
        link = element.find('a', class_=re.compile(r'name|title', re.I))
        if link:
            name = link.get_text(strip=True)
            if name and len(name) > 2:
                return name
        
        # Strategy 4: Look for strong/bold text
        strong = element.find(['strong', 'b'])
        if strong:
            name = strong.get_text(strip=True)
            if name and len(name) > 2 and not any(skip in name.lower() for skip in ['booth', 'location', 'phone']):
                return name
        
        return None

    def _extract_website(self, element: Tag) -> Optional[str]:
        """Extract website URL."""
        # Look for external links
        for link in element.find_all('a', href=True):
            href = link['href']
            
            # Check if it's a website (not internal navigation)
            if href.startswith('http') and 'highpointmarket.org' not in href:
                return href
            elif href.startswith('www.'):
                return f"https://{href}"
            
            # Check for profile/detail links that might contain website info
            if '/exhibitor/' in href or '/vendor/' in href or '/company/' in href:
                # This might be a detail page, store it as a reference
                if href.startswith('/'):
                    return f"{self.base_url}{href}"
        
        return None

    def _extract_booth_info(self, element: Tag) -> Dict[str, Any]:
        """Extract booth number and location information."""
        booth_info = {}
        
        # Look for booth number
        booth_patterns = [
            r'(?:booth|space|stand)[\s:#]*([A-Z0-9\-]+)',
            r'([A-Z]+[\s\-]?\d+)',  # Common format like "C-1055" or "IHFC 209"
            r'(?:showroom|location)[\s:#]*([A-Z0-9\-]+)'
        ]
        
        text_content = element.get_text()
        
        for pattern in booth_patterns:
            match = re.search(pattern, text_content, re.IGNORECASE)
            if match:
                booth_info['booth_number'] = match.group(1).strip()
                break
        
        # Look for building/location
        building_patterns = [
            r'(?:building|hall|wing|floor)[\s:#]*([A-Z0-9\-]+)',
            r'(IHFC|Suites at Market Square|Plaza Suites|Showplace)',  # High Point specific
            r'(?:located in|location)[\s:#]*([^,\n]+)'
        ]
        
        for pattern in building_patterns:
            match = re.search(pattern, text_content, re.IGNORECASE)
            if match:
                booth_info['building'] = match.group(1).strip()
                break
        
        return booth_info

    def _extract_contact_info(self, element: Tag) -> Dict[str, Any]:
        """Extract contact information."""
        contact_info = {}
        
        # Phone number
        phone_pattern = r'(?:phone|tel|p)[\s:#]*\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}'
        phone_match = re.search(phone_pattern, element.get_text(), re.IGNORECASE)
        if phone_match:
            contact_info['phone'] = phone_match.group(0)
        
        # Email
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email_match = re.search(email_pattern, element.get_text())
        if email_match:
            contact_info['email'] = email_match.group(0)
        
        return contact_info

    def _extract_categories(self, element: Tag) -> Optional[str]:
        """Extract product categories."""
        category_indicators = ['category', 'categories', 'products', 'specialties', 'type']
        
        for indicator in category_indicators:
            cat_elem = element.find(class_=re.compile(indicator, re.I))
            if cat_elem:
                return cat_elem.get_text(strip=True)
        
        # Look for tags or labels
        tags = element.find_all(class_=re.compile(r'tag|label|badge', re.I))
        if tags:
            categories = [tag.get_text(strip=True) for tag in tags]
            return ', '.join(categories)
        
        return None

    async def _try_alternative_strategies(self, page: Page) -> List[Dict[str, Any]]:
        """Try alternative strategies if main approach fails."""
        exhibitors = []
        
        # Strategy 1: Look for links to exhibitor profiles
        profile_links = await page.evaluate("""
            () => {
                const links = Array.from(document.querySelectorAll('a[href*="/exhibitor/"], a[href*="/vendor/"], a[href*="/company/"]'));
                return links.map(link => ({
                    name: link.textContent.trim(),
                    url: link.href
                })).filter(item => item.name && item.name.length > 2);
            }
        """)
        
        for link_data in profile_links:
            if link_data['name']:
                exhibitors.append({
                    'company_name': link_data['name'],
                    'profile_url': link_data['url']
                })
        
        logger.info(f"Found {len(exhibitors)} exhibitors from profile links")
        
        return exhibitors

    async def _javascript_extraction(self, page: Page) -> List[Dict[str, Any]]:
        """Fallback JavaScript extraction method."""
        logger.info("Using JavaScript extraction as fallback...")
        
        try:
            exhibitors = await page.evaluate("""
                () => {
                    const results = [];
                    const processedNames = new Set();
                    
                    // Find all potential exhibitor containers
                    const containers = document.querySelectorAll(`
                        div[class*="exhibitor"],
                        div[class*="vendor"],
                        div[class*="company"],
                        article[class*="card"],
                        div[class*="tile"],
                        div[class*="listing"],
                        li[class*="exhibitor"]
                    `);
                    
                    containers.forEach(container => {
                        const data = {};
                        
                        // Find company name
                        const nameElement = container.querySelector('h1, h2, h3, h4, h5, h6, strong, .name, .title, a[class*="name"]');
                        if (nameElement) {
                            const name = nameElement.textContent.trim();
                            if (name && name.length > 2 && !processedNames.has(name.toLowerCase())) {
                                data.company_name = name;
                                processedNames.add(name.toLowerCase());
                                
                                // Find website
                                const linkElement = container.querySelector('a[href*="http"], a[href*="www"]');
                                if (linkElement) {
                                    data.website = linkElement.href;
                                }
                                
                                // Find booth number
                                const text = container.textContent;
                                const boothMatch = text.match(/(?:booth|space|stand)[:\s]*([A-Z0-9\-]+)/i);
                                if (boothMatch) {
                                    data.booth_number = boothMatch[1];
                                }
                                
                                // Find building
                                const buildingMatch = text.match(/(?:building|hall|IHFC|Suites|Plaza)[:\s]*([A-Z0-9\-\s]+)/i);
                                if (buildingMatch) {
                                    data.building = buildingMatch[1].trim();
                                }
                                
                                results.push(data);
                            }
                        }
                    });
                    
                    return results;
                }
            """)
            
            logger.info(f"JavaScript extraction found {len(exhibitors)} exhibitors")
            return exhibitors
            
        except Exception as e:
            logger.error(f"JavaScript extraction failed: {e}")
            return []

    async def _extract_show_dates(self, page: Page) -> Dict[str, str]:
        """Try to extract actual show dates from the page."""
        try:
            dates = await page.evaluate("""
                () => {
                    const text = document.body.innerText;
                    // Look for date patterns like "April 26-30, 2025"
                    const datePattern = /([A-Z][a-z]+)\s+(\d{1,2})[\-–]\s*(\d{1,2}),?\s+(\d{4})/i;
                    const match = text.match(datePattern);
                    
                    if (match) {
                        const month = match[1];
                        const startDay = match[2];
                        const endDay = match[3];
                        const year = match[4];
                        
                        // Convert month name to number
                        const months = {
                            'january': '01', 'february': '02', 'march': '03', 'april': '04',
                            'may': '05', 'june': '06', 'july': '07', 'august': '08',
                            'september': '09', 'october': '10', 'november': '11', 'december': '12'
                        };
                        
                        const monthNum = months[month.toLowerCase()] || '01';
                        
                        return {
                            start_date: `${year}-${monthNum}-${startDay.padStart(2, '0')}`,
                            end_date: `${year}-${monthNum}-${endDay.padStart(2, '0')}`
                        };
                    }
                    
                    return null;
                }
            """)
            
            if dates:
                return dates
                
        except:
            pass
        
        return {}

    def _get_default_show_info(self) -> Dict[str, Any]:
        """Return default show information as fallback."""
        return {
            'name': 'High Point Market',
            'location': 'High Point, NC',
            'venue': 'High Point Market Authority',
            'start_date': '2025-04-26',
            'end_date': '2025-04-30',
            'industry': 'Furniture, Home Decor, Lighting',
            'estimated_attendance': 75000,
            'website_url': self.base_url,
            'exhibitor_list_url': self.exhibitor_list_url,
            'last_scraped': datetime.now().isoformat()
        }