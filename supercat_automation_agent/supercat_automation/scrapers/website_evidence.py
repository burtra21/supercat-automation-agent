# scrapers/website_evidence.py

import logging
import re
import logging
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from typing import Dict, List, Any, Optional, Optional
from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class WebsiteEvidenceExtractor:
    """
    Extracts specific evidence of the 5 proven EDPs from websites
    Each method maps to validated pain points from 14 won deals
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Map website indicators to proven EDPs
        self.edp_indicators = {
            'sales_enablement_collapse': {
                'indicators': [
                    'no_product_search',
                    'pdf_only_catalog', 
                    'no_mobile_optimization',
                    'no_dealer_portal',
                    'manual_quote_process',
                    'no_inventory_visibility'
                ],
                'weight': 1.0  # 100% of won deals
            },
            'technology_obsolescence': {
                'indicators': [
                    'no_ssl_certificate',
                    'slow_page_load',
                    'outdated_copyright',
                    'flash_required',
                    'no_responsive_design',
                    'no_integrations_visible'
                ],
                'weight': 0.93  # 93% of won deals
            },
            'rep_performance_crisis': {
                'indicators': [
                    'no_rep_locator',
                    'no_rep_portal',
                    'no_territory_info',
                    'no_sales_resources',
                    'complex_territory_structure'
                ],
                'weight': 0.71  # 71% of won deals
            },
            'sku_complexity': {
                'indicators': [
                    'massive_catalog',
                    'no_filtering_options',
                    'complex_configurations',
                    'no_comparison_tool',
                    'confusing_navigation'
                ],
                'weight': 0.64  # 64% of won deals
            },
            'channel_conflict': {
                'indicators': [
                    'multiple_login_portals',
                    'hidden_pricing',
                    'conflicting_information',
                    'multiple_brand_sites',
                    'dealer_only_access'
                ],
                'weight': 0.43  # 43% of won deals
            }
        }
    
    def _get_dynamic_html(self, url: str) -> str:
        """
        Uses Selenium to fetch fully rendered HTML (including JS content)
        """
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        html = driver.page_source
        driver.quit()
        return html

    def analyze_website(self, domain: str) -> Dict[str, Any]:
        """
        Complete website analysis for all 5 EDPs
        Returns evidence mapped to specific pain points
        """
        
        # Ensure proper URL format
        if not domain.startswith('http'):
            domain = f'https://{domain}'
        
        results = {
            'domain': domain,
            'scan_timestamp': datetime.now().isoformat(),
            'edp_evidence': {},
            'specific_findings': [],
            'personalization_hooks': [],
            'tam_indicators': {}
        }
        
        try:
            # Use Selenium to fetch fully rendered HTML
            html = self._get_dynamic_html(domain)
            soup = BeautifulSoup(html, 'html.parser')
            text_content = soup.get_text().lower()

            # Check each EDP
            for edp_name, edp_config in self.edp_indicators.items():
                evidence = self._check_edp_indicators(domain, edp_name, edp_config, soup, text_content)
                results['edp_evidence'][edp_name] = evidence
                # Add specific findings for messaging
                if evidence['score'] > 0.5:
                    results['specific_findings'].extend(evidence['specific_issues'])

            # Extract additional context
            results['personalization_hooks'] = self._extract_personalization_data(soup)
            results['tam_indicators'] = self._identify_tam_tier_indicators(results)

        except Exception as e:
            logger.error(f"Error analyzing {domain}: {e}")
            results['error'] = str(e)

        return results
    
    def _check_edp_indicators(self, domain: str, edp_name: str, config: Dict, soup: BeautifulSoup, text_content: str) -> Dict:
        """
        Check specific indicators for each EDP
        """
        
        evidence = {
            'edp': edp_name,
            'score': 0,
            'indicators_found': [],
            'specific_issues': [],
            'evidence_strength': 'none'
        }
        
        # Check each indicator based on EDP type
        if edp_name == 'sales_enablement_collapse':
            evidence = self._check_sales_enablement_indicators(domain, soup, text_content)
        elif edp_name == 'technology_obsolescence':
            evidence = self._check_technology_indicators(domain, soup, text_content)
        elif edp_name == 'rep_performance_crisis':
            evidence = self._check_rep_indicators(domain, soup, text_content)
        elif edp_name == 'sku_complexity':
            evidence = self._check_catalog_indicators(domain, soup)
        elif edp_name == 'channel_conflict':
            evidence = self._check_channel_indicators(domain, soup)
        
        # Apply weight from won deals
        evidence['weighted_score'] = evidence['score'] * config['weight']
        
        return evidence
    
    def _check_sales_enablement_indicators(self, domain: str, soup: BeautifulSoup, text_content: str) -> Dict:
        """Check for sales enablement collapse indicators"""
        
        evidence = {
            'edp': 'sales_enablement_collapse',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Check for product search
            search_elements = soup.find_all(['input', 'button'], 
                                           attrs={'type': 'search'}) or \
                            soup.find_all(text=lambda t: t and 'search' in t.lower())
            
            if not search_elements:
                evidence['indicators_found'].append('no_product_search')
                evidence['specific_issues'].append('No product search functionality found')
                evidence['score'] += 0.25
            
            # Check for PDF-only resources
            download_links = soup.find_all('a', href=lambda h: h and '.pdf' in h.lower())
            if len(download_links) > 5:
                evidence['indicators_found'].append('pdf_heavy')
                evidence['specific_issues'].append(f'Found {len(download_links)} PDF downloads - indicates manual processes')
                evidence['score'] += 0.20
            
            # Check mobile optimization
            viewport = soup.find('meta', attrs={'name': 'viewport'})
            if not viewport:
                evidence['indicators_found'].append('no_mobile_optimization')
                evidence['specific_issues'].append('Not mobile optimized - critical for trade shows')
                evidence['score'] += 0.30
            
            # Check for dealer/rep portal
            portal_indicators = ['dealer login', 'rep login', 'partner portal', 'sales portal']
            portal_found = any(indicator in text_content for indicator in portal_indicators)
            
            if not portal_found:
                evidence['indicators_found'].append('no_dealer_portal')
                evidence['specific_issues'].append('No dealer/rep portal detected')
                evidence['score'] += 0.25
            
        except Exception as e:
            logger.error(f"Error checking sales enablement: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.7:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.4:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    def _check_technology_indicators(self, domain: str, soup: BeautifulSoup, text_content: str) -> Dict:
        """Check for technology obsolescence indicators"""
        
        evidence = {
            'edp': 'technology_obsolescence',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Check SSL certificate
            if not domain.startswith('https'):
                evidence['indicators_found'].append('no_ssl')
                evidence['specific_issues'].append('No SSL certificate - major security issue')
                evidence['score'] += 0.35

            # Remove misleading page load speed check

            # Check copyright year (search all footer and visible text for year)
            copyright_texts = soup.find_all(string=re.compile(r'©|copyright', re.I))
            found_outdated = False
            for copyright_text in copyright_texts:
                year_match = re.search(r'(\d{4})', copyright_text)
                if year_match:
                    year = int(year_match.group(1))
                    if year < datetime.now().year - 1:
                        evidence['indicators_found'].append('outdated_copyright')
                        evidence['specific_issues'].append(f'Copyright year is {year} - site appears unmaintained')
                        evidence['score'] += 0.20
                        found_outdated = True
                        break

            # Check for modern features
            modern_indicators = ['react', 'vue', 'angular', 'webpack']
            has_modern = any(ind in text_content for ind in modern_indicators)
            
            if not has_modern:
                evidence['indicators_found'].append('no_modern_framework')
                evidence['specific_issues'].append('No modern web framework detected')
                evidence['score'] += 0.20
                
        except Exception as e:
            logger.error(f"Error checking technology: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    def _check_rep_indicators(self, domain: str, soup: BeautifulSoup, text_content: str) -> Dict:
        """Check for rep performance crisis indicators"""
        
        evidence = {
            'edp': 'rep_performance_crisis',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Check for rep locator
            locator_indicators = ['find a rep', 'find a dealer', 'where to buy', 'locate a representative']
            has_locator = any(ind in text_content for ind in locator_indicators)
            
            if not has_locator:
                evidence['indicators_found'].append('no_rep_locator')
                evidence['specific_issues'].append('No rep/dealer locator found')
                evidence['score'] += 0.35
            
            # Check for rep resources
            resource_indicators = ['rep resources', 'sales resources', 'partner resources', 'dealer resources']
            has_resources = any(ind in text_content for ind in resource_indicators)
            
            if not has_resources:
                evidence['indicators_found'].append('no_rep_resources')
                evidence['specific_issues'].append('No dedicated rep resources section')
                evidence['score'] += 0.35
            
            # Check for territory information
            territory_indicators = ['territory', 'territories', 'region', 'coverage area']
            has_territory = any(ind in text_content for ind in territory_indicators)
            
            if not has_territory:
                evidence['indicators_found'].append('no_territory_info')
                evidence['specific_issues'].append('No territory information visible')
                evidence['score'] += 0.30
                
        except Exception as e:
            logger.error(f"Error checking rep indicators: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    def _check_catalog_indicators(self, domain: str, home_soup: BeautifulSoup) -> Dict:
        """Check for SKU complexity indicators"""
        
        evidence = {
            'edp': 'sku_complexity',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        
        try:
            # Dynamically find the product/catalog page instead of guessing URLs
            product_page_url = self._find_page_by_keywords(domain, ['product', 'catalog', 'shop', 'store'], home_soup)

            if not product_page_url:
                evidence['specific_issues'].append('Could not find a product or catalog page.')
                evidence['score'] += 0.10
                return evidence

            # Use Selenium to fetch fully rendered HTML for the catalog/product page
            html = self._get_dynamic_html(product_page_url)
            soup = BeautifulSoup(html, 'html.parser')

            # Check for filtering options (heuristic: less than 3 is poor for B2B)
            filter_elements = soup.find_all(['select', 'input'], 
                                           attrs={'class': lambda c: c and 'filter' in c.lower()})

            if len(filter_elements) < 3:
                evidence['indicators_found'].append('limited_filtering')
                evidence['specific_issues'].append(f'Only {len(filter_elements)} filter options found on catalog page.')
                evidence['score'] += 0.25

            # Check for product count indicators
            product_count_text = soup.find(text=re.compile(r'\d+\s*(products|items|SKUs)', re.I))
            if product_count_text:
                count_match = re.search(r'(\d+)', product_count_text)
                if count_match:
                    count = int(count_match.group(1))
                    if count > 500: # Adjusted threshold
                        evidence['indicators_found'].append('high_sku_count')
                        evidence['specific_issues'].append(f'Over {count} SKUs detected')
                        evidence['score'] += 0.35

            # Check for configurator
            config_indicators = ['configure', 'customize', 'build your', 'options']
            has_configurator = any(ind in html.lower() for ind in config_indicators)

            if has_configurator:
                evidence['indicators_found'].append('complex_configurations')
                evidence['specific_issues'].append('Product configurator detected - high complexity')
                evidence['score'] += 0.40

        except Exception as e:
            logger.error(f"Error checking catalog: {e}")
        
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        
        return evidence
    
    # ...existing code...
    # ...existing code...
        
        hooks = []
        
        try:
            # Extract company name
            title = soup.find('title')
            if title:
                hooks.append({
                    'type': 'company_name',
                    'value': title.text.split('|')[0].strip()
                })
            
            # Look for trade shows mentioned
            text_content = soup.get_text().lower()
            trade_shows = ['High Point Market', 'Vegas Market', 'NeoCon', 'Lightovation']
            for show in trade_shows:
                if show.lower() in text_content:
                    hooks.append({
                        'type': 'trade_show',
                        'value': show
                    })
            
            # Extract product categories
            nav = soup.find('nav') or soup.find('div', class_='navigation')
            if nav:
                categories = [a.text.strip() for a in nav.find_all('a')[:5]]
                if categories:
                    hooks.append({
                        'type': 'product_categories',
                        'value': categories
                    })
                    
        except Exception as e:
            logger.error(f"Error extracting personalization: {e}")
        
        return hooks
    
    def _identify_tam_tier_indicators(self, results: Dict) -> Dict:
        """
        Identify which TAM tier this company belongs to
        Based on number and severity of EDPs
        """
        
        tam_indicators = {
            'tier': None,
            'has_multiple_edps': False,
            'total_pain_score': 0
        }
        
        # Count EDPs with meaningful evidence
        active_edps = []
        for edp_name, evidence in results['edp_evidence'].items():
            if evidence.get('score', 0) > 0.3:
                active_edps.append({
                    'name': edp_name,
                    'score': evidence.get('weighted_score', evidence.get('score', 0))
                })
        
        tam_indicators['edp_count'] = len(active_edps)
        tam_indicators['has_multiple_edps'] = len(active_edps) > 1
        
        if active_edps:
            # Sort by score to find primary
            active_edps.sort(key=lambda x: x['score'], reverse=True)
            tam_indicators['primary_edp'] = active_edps[0]['name']
            tam_indicators['total_pain_score'] = sum(e['score'] for e in active_edps)
        
        # Determine TAM tier
        if tam_indicators['total_pain_score'] >= 2.0 or tam_indicators['edp_count'] >= 3:
            tam_indicators['tier'] = 'TIER_1_HOT'
        elif tam_indicators['total_pain_score'] >= 1.0 or tam_indicators['edp_count'] >= 2:
            tam_indicators['tier'] = 'TIER_2_WARM'
        elif tam_indicators['total_pain_score'] >= 0.5:
            tam_indicators['tier'] = 'TIER_3_COOL'
        else:
            tam_indicators['tier'] = 'TIER_4_COLD'
        
        return tam_indicators
    def _find_page_by_keywords(self, domain: str, keywords: List[str], soup: BeautifulSoup) -> Optional[str]:
        """
        Find a page URL by looking for keywords in links
        """
        for keyword in keywords:
            # Look for links containing the keyword
            links = soup.find_all('a', href=True)
            for link in links:
                href = link.get('href', '').lower()
                text = link.get_text().lower()
                if keyword in href or keyword in text:
                    # Build full URL
                    if href.startswith('http'):
                        return href
                    elif href.startswith('/'):
                        return f"{domain.rstrip('/')}{href}"
                    else:
                        return f"{domain.rstrip('/')}/{href}"
        return None

    def _check_channel_indicators(self, domain: str, soup: BeautifulSoup) -> Dict:
        """
        Check for channel conflict indicators
        """
        evidence = {
            'edp': 'channel_conflict',
            'score': 0,
            'indicators_found': [],
            'specific_issues': []
        }
        try:
            text_content = soup.get_text().lower()
            # Check for multiple login types
            login_types = ['dealer login', 'customer login', 'trade login', 'rep login']
            login_count = sum(1 for login in login_types if login in text_content)
            if login_count >= 2:
                evidence['indicators_found'].append('multiple_portals')
                evidence['specific_issues'].append(f'{login_count} different login portals found')
                evidence['score'] += 0.35
            # Check pricing visibility
            if 'login' in text_content and 'price' in text_content:
                evidence['indicators_found'].append('hidden_pricing')
                evidence['specific_issues'].append('Pricing requires login - channel conflict likely')
                evidence['score'] += 0.30
        except Exception as e:
            logger.error(f"Error in channel check: {e}")
        # Determine evidence strength
        if evidence['score'] >= 0.6:
            evidence['evidence_strength'] = 'strong'
        elif evidence['score'] >= 0.3:
            evidence['evidence_strength'] = 'moderate'
        elif evidence['score'] > 0:
            evidence['evidence_strength'] = 'weak'
        else:
            evidence['evidence_strength'] = 'none'
        return evidence
    def _extract_personalization_data(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract specific data points for message personalization"""
        hooks = []
        
        try:
            # Extract company name from title
            title = soup.find('title')
            if title:
                hooks.append({
                    'type': 'company_name',
                    'value': title.text.split('|')[0].strip()
                })
            
            # Look for trade shows mentioned
            text_content = soup.get_text().lower()
            trade_shows = ['vegas market', 'high point market', 'neocon', 'lightovation']
            for show in trade_shows:
                if show.lower() in text_content:
                    hooks.append({
                        'type': 'trade_show',
                        'value': show
                    })
            
            # Extract product categories from navigation
            nav = soup.find('nav') or soup.find('div', class_='navigation')
            if nav:
                categories = [a.text.strip() for a in nav.find_all('a')[:5]]
                if categories:
                    hooks.append({
                        'type': 'product_categories',
                        'value': categories
                    })
                    
        except Exception as e:
            logger.error(f"Error extracting personalization: {e}")
        
        return hooks