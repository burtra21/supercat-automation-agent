# src/scrapers/trade_show_scraper.py
"""
Trade show scraper for identifying target companies
Focus on furniture, lighting, and home decor shows
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import logging
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class TradeshowScraper:
    """Scrapes major trade shows for exhibitor lists"""
    
    def __init__(self, supabase_client):
        self.supabase = supabase_client
        self.trade_shows = [
            {
                'name': 'Las Vegas Market',
                'url': 'https://www.lasvegasmarket.com',
                'exhibitor_path': '/exhibitors',
                'industry': 'furniture_lighting_home_decor',
                'frequency': 'bi-annual',
                'next_dates': ['2025-01-26', '2025-07-27']
            },
            {
                'name': 'High Point Market',
                'url': 'https://www.highpointmarket.org',
                'exhibitor_path': '/exhibitors',
                'industry': 'furniture',
                'frequency': 'bi-annual',
                'next_dates': ['2025-04-26', '2025-10-25']
            },
            {
                'name': 'AmericasMart Atlanta',
                'url': 'https://www.americasmart.com',
                'exhibitor_path': '/markets/gift-home',
                'industry': 'gift_home_decor',
                'frequency': 'quarterly',
                'next_dates': ['2025-01-14', '2025-07-15']
            },
            {
                'name': 'Dallas Market Center',
                'url': 'https://www.dallasmarketcenter.com',
                'exhibitor_path': '/markets/lightovation',
                'industry': 'lighting',
                'frequency': 'bi-annual',
                'next_dates': ['2025-01-08', '2025-06-18']
            }
        ]
    
    async def scrape_all_shows(self) -> List[Dict]:
        """Scrape all configured trade shows"""
        all_exhibitors = []
        
        for show in self.trade_shows:
            try:
                exhibitors = await self.scrape_show(show)
                all_exhibitors.extend(exhibitors)
                logger.info(f"Scraped {len(exhibitors)} exhibitors from {show['name']}")
            except Exception as e:
                logger.error(f"Failed to scrape {show['name']}: {e}")
                continue
        
        return all_exhibitors
    
    async def scrape_show(self, show: Dict) -> List[Dict]:
        """Scrape individual trade show for exhibitors"""
        exhibitors = []
        
        try:
            async with aiohttp.ClientSession() as session:
                url = show['url'] + show['exhibitor_path']
                async with session.get(url) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Parse exhibitor listings (simplified - needs customization per site)
                    exhibitor_elements = soup.find_all(['div', 'article'], class_=['exhibitor', 'vendor', 'company'])
                    
                    for elem in exhibitor_elements:
                        exhibitor = self._parse_exhibitor(elem, show)
                        if exhibitor:
                            exhibitors.append(exhibitor)
        
        except Exception as e:
            logger.error(f"Error scraping {show['name']}: {e}")
        
        return exhibitors
    
    def _parse_exhibitor(self, element, show: Dict) -> Optional[Dict]:
        """Parse individual exhibitor element"""
        try:
            # Extract company name
            name_elem = element.find(['h2', 'h3', 'h4', 'a'], class_=['name', 'title', 'company-name'])
            if not name_elem:
                return None
            
            company_name = name_elem.get_text(strip=True)
            
            # Extract booth number
            booth_elem = element.find(['span', 'div'], class_=['booth', 'location', 'booth-number'])
            booth_number = booth_elem.get_text(strip=True) if booth_elem else None
            
            # Extract website/domain
            link_elem = element.find('a', href=True)
            website = link_elem['href'] if link_elem else None
            
            # Calculate urgency based on show date
            next_show_date = datetime.strptime(show['next_dates'][0], '%Y-%m-%d')
            days_until_show = (next_show_date - datetime.now()).days
            urgency_score = self._calculate_urgency(days_until_show)
            
            return {
                'company_name': company_name,
                'trade_show': show['name'],
                'booth_number': booth_number,
                'website': website,
                'industry': show['industry'],
                'show_date': show['next_dates'][0],
                'days_until_show': days_until_show,
                'urgency_score': urgency_score,
                'source': 'trade_show_scrape',
                'scraped_at': datetime.now().isoformat()
            }
        
        except Exception as e:
            logger.debug(f"Failed to parse exhibitor: {e}")
            return None
    
    def _calculate_urgency(self, days_until_show: int) -> float:
        """Calculate urgency score based on days until show"""
        if days_until_show <= 30:
            return 1.0
        elif days_until_show <= 60:
            return 0.8
        elif days_until_show <= 90:
            return 0.6
        elif days_until_show <= 120:
            return 0.4
        else:
            return 0.2


# src/scrapers/industry_directory_scraper.py
"""
Industry directory scraper for furniture/lighting manufacturers
"""

class IndustryDirectoryScraper:
    """Scrapes industry directories for target companies"""
    
    def __init__(self, supabase_client):
        self.supabase = supabase_client
        self.directories = [
            {
                'name': 'Furniture Today Top 100',
                'url': 'https://www.furnituretoday.com/research/',
                'industry': 'furniture_manufacturing'
            },
            {
                'name': 'Home Furnishings Association',
                'url': 'https://www.myhfa.org/members/',
                'industry': 'home_furnishings'
            },
            {
                'name': 'American Lighting Association',
                'url': 'https://www.americanlightingassoc.com/members/',
                'industry': 'lighting'
            },
            {
                'name': 'International Home Furnishings Representatives Association',
                'url': 'https://www.ihfra.org/manufacturers/',
                'industry': 'home_furnishings_reps'
            }
        ]
    
    async def scrape_directories(self) -> List[Dict]:
        """Scrape all configured directories"""
        all_companies = []
        
        for directory in self.directories:
            try:
                companies = await self.scrape_directory(directory)
                all_companies.extend(companies)
                logger.info(f"Scraped {len(companies)} companies from {directory['name']}")
            except Exception as e:
                logger.error(f"Failed to scrape {directory['name']}: {e}")
                continue
        
        return all_companies
    
    async def scrape_directory(self, directory: Dict) -> List[Dict]:
        """Scrape individual directory"""
        companies = []
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(directory['url']) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Parse company listings
                    company_elements = soup.find_all(['div', 'li', 'article'], 
                                                    class_=['member', 'company', 'listing'])
                    
                    for elem in company_elements:
                        company = self._parse_company(elem, directory)
                        if company:
                            companies.append(company)
        
        except Exception as e:
            logger.error(f"Error scraping {directory['name']}: {e}")
        
        return companies
    
    def _parse_company(self, element, directory: Dict) -> Optional[Dict]:
        """Parse individual company element"""
        try:
            # Extract company details
            name = element.find(['h2', 'h3', 'a']).get_text(strip=True)
            
            # Look for website
            website_elem = element.find('a', href=lambda x: x and 'http' in x)
            website = website_elem['href'] if website_elem else None
            
            # Extract additional details
            details = {
                'company_name': name,
                'website': website,
                'industry': directory['industry'],
                'source': f"directory_{directory['name']}",
                'directory_listing': True,
                'scraped_at': datetime.now().isoformat()
            }
            
            return details
        
        except Exception as e:
            logger.debug(f"Failed to parse company: {e}")
            return None