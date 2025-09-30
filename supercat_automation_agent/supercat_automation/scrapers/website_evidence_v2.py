"""
Enhanced Website Evidence Extractor v2
Captures detailed EDP analysis matching SuperCat_EDP_Analysis.csv structure
Integrates with validated PSI calculator and message generator
"""

import logging
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from typing import Dict, List, Any, Optional
from datetime import datetime
import time

logger = logging.getLogger(__name__)

class WebsiteEvidenceExtractorV2:
    """
    Enhanced website evidence extractor for comprehensive EDP analysis
    Matches the detailed structure from SuperCat_EDP_Analysis.csv
    """
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # Trade shows to detect
        self.trade_shows = {
            'High Point Market': ['high point market', 'hpmkt', 'highpoint'],
            'Vegas Market': ['vegas market', 'las vegas market'],
            'Lightovation': ['lightovation', 'dallas market'],
            'NeoCon': ['neocon', 'neo con'],
            'Casual Market': ['casual market'],
            'HD Expo': ['hd expo', 'hdexpo']
        }
        
        # JavaScript frameworks to detect
        self.js_frameworks = [
            'react', 'vue', 'angular', 'angularjs', 'jquery', 'next.js', 
            'backbone.js', 'ember', 'svelte', 'webpack', 'typescript'
        ]
        
        # Modern features to detect
        self.modern_features = [
            'service worker', 'intersection observer', 'viewport meta',
            'html5', 'es modules', 'webauthn', 'progressive web app'
        ]
    
    def analyze_website_comprehensive(self, domain: str) -> Dict[str, Any]:
        """
        Comprehensive website analysis matching CSV structure
        """
        
        if not domain.startswith('http'):
            domain = f'https://{domain}'
        
        results = {
            'domain': domain,
            'scan_timestamp': datetime.now().isoformat(),
            
            # EDP1: SKU Complexity Analysis
            'EDP1_SKU_Count_Estimate': 0,
            'EDP1_Product_Categories': [],
            'EDP1_Category_Count': 0,
            'EDP1_Configuration_Options': False,
            'EDP1_Has_Configurator': False,
            'EDP1_Catalog_Format': 'Unknown',
            'EDP1_Has_Search': False,
            'EDP1_Search_Sophistication': 'None',
            'EDP1_Filter_Options': [],
            'EDP1_Filter_Count': 0,
            'EDP1_SKU_Complexity_Pain_Score': 0,
            
            # EDP2: Rep Management Analysis
            'EDP2_Has_Rep_Locator': False,
            'EDP2_Rep_Portal_Exists': False,
            'EDP2_Rep_Resources_Accessible': False,
            'EDP2_Territory_Structure_Visible': False,
            'EDP2_Rep_Count_Estimate': 0,
            'EDP2_Territory_Complexity': 'Unknown',
            'EDP2_Rep_Login_Keywords': [],
            'EDP2_Rep_Performance_Pain_Score': 0,
            
            # EDP6: Channel Conflict Analysis
            'EDP6_Channels_Detected': [],
            'EDP6_Channel_Count': 0,
            'EDP6_Has_Direct_Sales': False,
            'EDP6_Has_Dealer_Network': False,
            'EDP6_Has_Ecommerce': False,
            'EDP6_Has_Trade_Program': False,
            'EDP6_Has_Contract_Sales': False,
            'EDP6_Pricing_Transparency': 'Unknown',
            'EDP6_Brand_Count': 0,
            'EDP6_Multi_Brand_Detected': False,
            'EDP6_Channel_Conflict_Pain_Score': 0,
            
            # EDP7: Sales Enablement Analysis
            'EDP7_Has_Product_Search': False,
            'EDP7_Has_Advanced_Filters': False,
            'EDP7_Has_Comparison_Tool': False,
            'EDP7_Has_Wishlist_Quotes': False,
            'EDP7_Has_Project_Boards': False,
            'EDP7_Has_Mobile_Optimization': False,
            'EDP7_Has_Downloadable_Assets': False,
            'EDP7_Resource_Formats': [],
            'EDP7_Resource_Format_Count': 0,
            'EDP7_Requires_Login_Resources': False,
            'EDP7_Missing_Tools': [],
            'EDP7_Sales_Enablement_Pain_Score': 0,
            
            # EDP8: Technology Obsolescence Analysis
            'EDP8_Has_SSL': False,
            'EDP8_Page_Speed_Score': 'Unknown',
            'EDP8_Load_Time_Seconds': 0,
            'EDP8_Modern_Features': [],
            'EDP8_Modern_Feature_Count': 0,
            'EDP8_Integration_Signals': [],
            'EDP8_Integration_Count': 0,
            'EDP8_Has_API': False,
            'EDP8_CMS_Detected': 'Unknown',
            'EDP8_Uses_CDN': False,
            'EDP8_Copyright_Year': datetime.now().year,
            'EDP8_Staleness_Score': 0,
            'EDP8_Has_Legacy_Tech': False,
            'EDP8_Legacy_Tech_Found': [],
            'EDP8_Tech_Obsolescence_Pain_Score': 0,
            
            # Additional Context
            'Trade_Shows_Mentioned': [],
            'Trade_Show_Count': 0,
            'Next_Trade_Show': None,
            'Weeks_To_Next_Show': None,
            'Product_Types': [],
            'Target_Audience': 'Unknown',
            'Geographic_Presence': 'Unknown',
            'Key_Differentiators': [],
            'Specific_Missing_Features': [],
            
            # Technical Details
            'Mobile_Viewport_Meta': False,
            'Has_Modern_JS_Framework': False,
            'JavaScript_Frameworks': [],
            'Has_Search_Endpoint': False,
            'Has_Resources_Page': False,
            'Has_Events_Page': False,
            'Broken_Links_Count': 0,
            'Uses_Modern_CSS': False,
            'Website_Tech_Stack': []
        }
        
        try:
            # Get page content with timing
            start_time = time.time()
            html = self._get_dynamic_html(domain)
            load_time = time.time() - start_time
            results['EDP8_Load_Time_Seconds'] = round(load_time, 1)
            
            soup = BeautifulSoup(html, 'html.parser')
            text_content = soup.get_text().lower()
            
            # Analyze each EDP category
            self._analyze_edp1_sku_complexity(soup, text_content, results)
            self._analyze_edp2_rep_management(soup, text_content, results)
            self._analyze_edp6_channel_conflict(soup, text_content, results)
            self._analyze_edp7_sales_enablement(soup, text_content, results)
            self._analyze_edp8_technology(domain, soup, text_content, results)
            
            # Extract additional context
            self._extract_trade_shows(text_content, results)
            self._extract_product_context(soup, text_content, results)
            self._extract_technical_details(soup, html, results)
            
            # Calculate pain scores
            self._calculate_pain_scores(results)
            
        except Exception as e:
            logger.error(f"Error analyzing {domain}: {e}")
            results['error'] = str(e)
        
        return results
    
    def _get_dynamic_html(self, url: str) -> str:
        """Get fully rendered HTML using Selenium"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--log-level=3')
        
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), 
            options=chrome_options
        )
        
        try:
            driver.get(url)
            time.sleep(3)  # Wait for dynamic content
            html = driver.page_source
        finally:
            driver.quit()
        
        return html
    
    def _analyze_edp1_sku_complexity(self, soup: BeautifulSoup, text_content: str, results: Dict):
        """Analyze EDP1: SKU Complexity indicators"""
        
        # Product search detection
        search_elements = soup.find_all(['input'], attrs={'type': 'search'}) or \
                         soup.find_all(['input'], attrs={'placeholder': lambda x: x and 'search' in x.lower()}) or \
                         soup.find_all(['button'], string=lambda x: x and 'search' in x.lower())
        
        results['EDP1_Has_Search'] = len(search_elements) > 0
        
        if results['EDP1_Has_Search']:
            results['EDP1_Search_Sophistication'] = 'Advanced' if len(search_elements) > 2 else 'Basic'
        
        # Product categories detection
        nav_elements = soup.find_all(['nav', 'ul', 'div'], class_=lambda x: x and any(
            term in x.lower() for term in ['nav', 'menu', 'category', 'product']
        ))
        
        categories = []
        for nav in nav_elements:
            links = nav.find_all('a')
            for link in links[:10]:  # Limit to avoid noise
                text = link.get_text().strip()
                if len(text) > 2 and len(text) < 50:
                    categories.append(text)
        
        results['EDP1_Product_Categories'] = list(set(categories))[:20]  # Limit and dedupe
        results['EDP1_Category_Count'] = len(results['EDP1_Product_Categories'])
        
        # Filter options detection
        filter_elements = soup.find_all(['select', 'input'], attrs={
            'class': lambda x: x and any(term in x.lower() for term in ['filter', 'sort', 'refine'])
        })
        
        filter_options = []
        for element in filter_elements:
            if element.name == 'select':
                options = element.find_all('option')
                if len(options) > 1:
                    filter_options.append(f"Select: {element.get('name', 'unknown')}")
            else:
                filter_options.append(f"Input: {element.get('name', 'unknown')}")
        
        results['EDP1_Filter_Options'] = filter_options
        results['EDP1_Filter_Count'] = len(filter_options)
        
        # Configurator detection
        config_keywords = ['configure', 'customize', 'build your', 'options', 'configurator']
        results['EDP1_Has_Configurator'] = any(keyword in text_content for keyword in config_keywords)
        results['EDP1_Configuration_Options'] = results['EDP1_Has_Configurator']
        
        # Catalog format detection
        pdf_links = soup.find_all('a', href=lambda x: x and '.pdf' in x.lower())
        if len(pdf_links) > 5:
            results['EDP1_Catalog_Format'] = 'PDF-heavy'
        elif results['EDP1_Has_Search']:
            results['EDP1_Catalog_Format'] = 'Interactive catalog'
        else:
            results['EDP1_Catalog_Format'] = 'Basic website'
        
        # SKU count estimation (heuristic)
        product_indicators = soup.find_all(string=re.compile(r'\d+\s*(products|items|SKUs)', re.I))
        if product_indicators:
            for indicator in product_indicators:
                match = re.search(r'(\d+)', indicator)
                if match:
                    results['EDP1_SKU_Count_Estimate'] = max(results['EDP1_SKU_Count_Estimate'], int(match.group(1)))
        
        # If no explicit count, estimate from categories and complexity
        if results['EDP1_SKU_Count_Estimate'] == 0:
            if results['EDP1_Category_Count'] > 15:
                results['EDP1_SKU_Count_Estimate'] = 5000
            elif results['EDP1_Category_Count'] > 8:
                results['EDP1_SKU_Count_Estimate'] = 2000
            elif results['EDP1_Category_Count'] > 4:
                results['EDP1_SKU_Count_Estimate'] = 800
            else:
                results['EDP1_SKU_Count_Estimate'] = 500
    
    def _analyze_edp2_rep_management(self, soup: BeautifulSoup, text_content: str, results: Dict):
        """Analyze EDP2: Rep Management indicators"""
        
        # Rep locator detection
        locator_keywords = ['find a rep', 'find a dealer', 'where to buy', 'locate a representative', 'rep locator']
        results['EDP2_Has_Rep_Locator'] = any(keyword in text_content for keyword in locator_keywords)
        
        # Rep portal detection
        portal_keywords = ['rep login', 'dealer login', 'partner portal', 'sales portal', 'rep portal']
        rep_login_found = []
        for keyword in portal_keywords:
            if keyword in text_content:
                rep_login_found.append(keyword)
        
        results['EDP2_Rep_Portal_Exists'] = len(rep_login_found) > 0
        results['EDP2_Rep_Login_Keywords'] = rep_login_found
        
        # Rep resources detection
        resource_keywords = ['rep resources', 'sales resources', 'partner resources', 'dealer resources', 'sales tools']
        results['EDP2_Rep_Resources_Accessible'] = any(keyword in text_content for keyword in resource_keywords)
        
        # Territory structure detection
        territory_keywords = ['territory', 'territories', 'region', 'coverage area', 'sales territory']
        results['EDP2_Territory_Structure_Visible'] = any(keyword in text_content for keyword in territory_keywords)
        
        if results['EDP2_Territory_Structure_Visible']:
            results['EDP2_Territory_Complexity'] = 'High' if 'complex' in text_content else 'Medium'
        else:
            results['EDP2_Territory_Complexity'] = 'Low'
        
        # Rep count estimation (heuristic based on company indicators)
        if 'nationwide' in text_content or 'national' in text_content:
            results['EDP2_Rep_Count_Estimate'] = 100
        elif 'regional' in text_content or len(rep_login_found) > 1:
            results['EDP2_Rep_Count_Estimate'] = 50
        elif results['EDP2_Has_Rep_Locator']:
            results['EDP2_Rep_Count_Estimate'] = 20
        else:
            results['EDP2_Rep_Count_Estimate'] = 10
    
    def _analyze_edp6_channel_conflict(self, soup: BeautifulSoup, text_content: str, results: Dict):
        """Analyze EDP6: Channel Conflict indicators"""
        
        channels = []
        
        # Direct sales detection
        if any(term in text_content for term in ['direct sales', 'buy direct', 'factory direct']):
            channels.append('Direct Sales')
            results['EDP6_Has_Direct_Sales'] = True
        
        # Dealer network detection
        if any(term in text_content for term in ['dealer', 'authorized dealer', 'showroom', 'retailer']):
            channels.append('Dealer Network')
            results['EDP6_Has_Dealer_Network'] = True
        
        # E-commerce detection
        if any(term in text_content for term in ['add to cart', 'buy now', 'shop online', 'e-commerce', 'online store']):
            channels.append('E-commerce')
            results['EDP6_Has_Ecommerce'] = True
        
        # Trade program detection
        if any(term in text_content for term in ['trade program', 'trade only', 'to the trade', 'designer program']):
            channels.append('Trade Program')
            results['EDP6_Has_Trade_Program'] = True
        
        # Contract sales detection
        if any(term in text_content for term in ['contract sales', 'hospitality', 'commercial', 'project sales']):
            channels.append('Contract Sales')
            results['EDP6_Has_Contract_Sales'] = True
        
        results['EDP6_Channels_Detected'] = channels
        results['EDP6_Channel_Count'] = len(channels)
        
        # Pricing transparency analysis
        if 'call for price' in text_content or 'request quote' in text_content:
            results['EDP6_Pricing_Transparency'] = 'None'
        elif 'login' in text_content and 'price' in text_content:
            results['EDP6_Pricing_Transparency'] = 'Login required'
        elif any(term in text_content for term in ['$', 'price', 'cost']):
            results['EDP6_Pricing_Transparency'] = 'Public pricing'
        else:
            results['EDP6_Pricing_Transparency'] = 'Quote only'
        
        # Brand detection (simplified)
        brand_indicators = soup.find_all(['div', 'section'], class_=lambda x: x and 'brand' in x.lower())
        results['EDP6_Brand_Count'] = min(len(brand_indicators), 10)  # Cap at reasonable number
        results['EDP6_Multi_Brand_Detected'] = results['EDP6_Brand_Count'] > 1
    
    def _analyze_edp7_sales_enablement(self, soup: BeautifulSoup, text_content: str, results: Dict):
        """Analyze EDP7: Sales Enablement indicators"""
        
        # Product search (already analyzed in EDP1)
        results['EDP7_Has_Product_Search'] = results['EDP1_Has_Search']
        
        # Advanced filters
        results['EDP7_Has_Advanced_Filters'] = results['EDP1_Filter_Count'] > 3
        
        # Comparison tool detection
        comparison_keywords = ['compare', 'comparison', 'compare products', 'side by side']
        results['EDP7_Has_Comparison_Tool'] = any(keyword in text_content for keyword in comparison_keywords)
        
        # Wishlist/quotes detection
        wishlist_keywords = ['wishlist', 'favorites', 'save', 'quote', 'request quote']
        results['EDP7_Has_Wishlist_Quotes'] = any(keyword in text_content for keyword in wishlist_keywords)
        
        # Project boards detection
        project_keywords = ['project', 'mood board', 'inspiration', 'collection', 'project board']
        results['EDP7_Has_Project_Boards'] = any(keyword in text_content for keyword in project_keywords)
        
        # Mobile optimization detection
        viewport_meta = soup.find('meta', attrs={'name': 'viewport'})
        results['EDP7_Has_Mobile_Optimization'] = viewport_meta is not None
        results['Mobile_Viewport_Meta'] = results['EDP7_Has_Mobile_Optimization']
        
        # Downloadable assets detection
        download_links = soup.find_all('a', href=lambda x: x and any(
            ext in x.lower() for ext in ['.pdf', '.zip', '.doc', '.xls', '.dwg', '.cad']
        ))
        results['EDP7_Has_Downloadable_Assets'] = len(download_links) > 0
        
        # Resource formats
        resource_formats = []
        for link in download_links[:10]:  # Limit check
            href = link.get('href', '').lower()
            if '.pdf' in href:
                resource_formats.append('PDF')
            elif '.zip' in href:
                resource_formats.append('ZIP')
            elif any(ext in href for ext in ['.doc', '.docx']):
                resource_formats.append('DOC')
            elif any(ext in href for ext in ['.xls', '.xlsx']):
                resource_formats.append('XLS')
            elif any(ext in href for ext in ['.dwg', '.cad']):
                resource_formats.append('CAD')
        
        results['EDP7_Resource_Formats'] = list(set(resource_formats))
        results['EDP7_Resource_Format_Count'] = len(results['EDP7_Resource_Formats'])
        
        # Login requirements for resources
        results['EDP7_Requires_Login_Resources'] = 'login' in text_content and len(download_links) > 0
        
        # Missing tools identification
        missing_tools = []
        if not results['EDP7_Has_Product_Search']:
            missing_tools.append('Product search')
        if not results['EDP7_Has_Comparison_Tool']:
            missing_tools.append('Comparison tool')
        if not results['EDP7_Has_Wishlist_Quotes']:
            missing_tools.append('Quote builder')
        if not results['EDP7_Has_Project_Boards']:
            missing_tools.append('Project boards')
        if not results['EDP7_Has_Mobile_Optimization']:
            missing_tools.append('Mobile site')
        
        results['EDP7_Missing_Tools'] = missing_tools
    
    def _analyze_edp8_technology(self, domain: str, soup: BeautifulSoup, text_content: str, results: Dict):
        """Analyze EDP8: Technology Obsolescence indicators"""
        
        # SSL detection
        results['EDP8_Has_SSL'] = domain.startswith('https')
        
        # Page speed scoring (simplified)
        load_time = results['EDP8_Load_Time_Seconds']
        if load_time < 2:
            results['EDP8_Page_Speed_Score'] = 'Good'
        elif load_time < 4:
            results['EDP8_Page_Speed_Score'] = 'Average'
        else:
            results['EDP8_Page_Speed_Score'] = 'Poor'
        
        # Modern features detection
        modern_features_found = []
        html_content = str(soup).lower()
        
        for feature in self.modern_features:
            if feature in html_content or feature in text_content:
                modern_features_found.append(feature)
        
        results['EDP8_Modern_Features'] = modern_features_found
        results['EDP8_Modern_Feature_Count'] = len(modern_features_found)
        
        # JavaScript frameworks detection
        js_frameworks_found = []
        for framework in self.js_frameworks:
            if framework in html_content:
                js_frameworks_found.append(framework)
        
        results['JavaScript_Frameworks'] = js_frameworks_found
        results['Has_Modern_JS_Framework'] = len(js_frameworks_found) > 0
        
        # Integration signals detection
        integration_signals = []
        integration_keywords = ['api', 'integration', 'webhook', 'rest', 'graphql', 'oauth']
        for keyword in integration_keywords:
            if keyword in text_content:
                integration_signals.append(keyword)
        
        results['EDP8_Integration_Signals'] = integration_signals
        results['EDP8_Integration_Count'] = len(integration_signals)
        results['EDP8_Has_API'] = 'api' in integration_signals
        
        # CMS detection
        cms_indicators = {
            'wordpress': ['wp-content', 'wordpress'],
            'shopify': ['shopify', 'myshopify'],
            'magento': ['magento'],
            'drupal': ['drupal'],
            'squarespace': ['squarespace'],
            'wix': ['wix.com']
        }
        
        for cms, indicators in cms_indicators.items():
            if any(indicator in html_content for indicator in indicators):
                results['EDP8_CMS_Detected'] = cms.title()
                break
        
        # CDN detection
        cdn_indicators = ['cdn', 'cloudflare', 'amazonaws', 'fastly', 'maxcdn']
        results['EDP8_Uses_CDN'] = any(indicator in html_content for indicator in cdn_indicators)
        
        # Copyright year detection
        copyright_matches = re.findall(r'©?\s*(\d{4})', text_content)
        if copyright_matches:
            years = [int(year) for year in copyright_matches if 2000 <= int(year) <= datetime.now().year]
            if years:
                results['EDP8_Copyright_Year'] = max(years)
        
        # Staleness score calculation
        current_year = datetime.now().year
        year_diff = current_year - results['EDP8_Copyright_Year']
        results['EDP8_Staleness_Score'] = min(year_diff * 20, 100)  # 20 points per year, max 100
        
        # Legacy technology detection
        legacy_tech = []
        legacy_indicators = {
            'flash': ['flash', 'swf'],
            'old_jquery': ['jquery-1.', 'jquery/1.'],
            'old_wordpress': ['wp-content/themes/twentyten', 'wp-content/themes/twentyeleven'],
            'old_bootstrap': ['bootstrap-2.', 'bootstrap/2.'],
            'ie_specific': ['<!--[if IE', 'filter:progid']
        }
        
        for tech, indicators in legacy_indicators.items():
            if any(indicator in html_content for indicator in indicators):
                legacy_tech.append(tech)
        
        results['EDP8_Legacy_Tech_Found'] = legacy_tech
        results['EDP8_Has_Legacy_Tech'] = len(legacy_tech) > 0
        
        # Website tech stack (simplified)
        tech_stack = []
        tech_stack.extend(js_frameworks_found)
        if results['EDP8_CMS_Detected'] != 'Unknown':
            tech_stack.append(results['EDP8_CMS_Detected'])
        if results['EDP8_Uses_CDN']:
            tech_stack.append('CDN')
        
        results['Website_Tech_Stack'] = tech_stack
    
    def _extract_trade_shows(self, text_content: str, results: Dict):
        """Extract trade show mentions and dates"""
        
        trade_shows_found = []
        for show_name, keywords in self.trade_shows.items():
            if any(keyword in text_content for keyword in keywords):
                trade_shows_found.append(show_name)
        
        results['Trade_Shows_Mentioned'] = trade_shows_found
        results['Trade_Show_Count'] = len(trade_shows_found)
        
        # Simple next show detection (would need more sophisticated date parsing in production)
        if 'high point market' in text_content:
            results['Next_Trade_Show'] = 'High Point Market'
            results['Weeks_To_Next_Show'] = 9  # Example - would calculate from actual dates
    
    def _extract_product_context(self, soup: BeautifulSoup, text_content: str, results: Dict):
        """Extract product types and business context"""
        
        # Product types detection
        product_keywords = {
            'furniture': ['furniture', 'seating', 'tables', 'chairs', 'sofas', 'beds'],
            'lighting': ['lighting', 'lamps', 'fixtures', 'chandeliers', 'sconces'],
            'outdoor': ['outdoor', 'patio', 'garden', 'exterior'],
            'decor': ['decor', 'accessories', 'art', 'mirrors', 'rugs']
        }
        
        product_types = []
        for category, keywords in product_keywords.items():
            if any(keyword in text_content for keyword in keywords):
                product_types.append(category)
        
        results['Product_Types'] = product_types
        
        # Target audience detection
        if any(term in text_content for term in ['trade only', 'to the trade', 'designer']):
            results['Target_Audience'] = 'Trade only'
        elif any(term in text_content for term in ['b2b', 'wholesale', 'dealer']):
            results['Target_Audience'] = 'B2B wholesale'
        elif any(term in text_content for term in ['retail', 'consumer', 'buy now']):
            results['Target_Audience'] = 'B2C retail'
        else:
            results['Target_Audience'] = 'Mixed'
        
        # Geographic presence
        if any(term in text_content for term in ['worldwide', 'international', 'global']):
            results['Geographic_Presence'] = 'Worldwide'
        elif any(term in text_content for term in ['nationwide', 'national', 'usa', 'america']):
            results['Geographic_Presence'] = 'USA'
        elif any(term in text_content for term in ['regional', 'local']):
            results['Geographic_Presence'] = 'Regional'
        else:
            results['Geographic_Presence'] = 'Unknown'
    
    def _extract_technical_details(self, soup: BeautifulSoup, html: str, results: Dict):
        """Extract additional technical details"""
        
        # Search endpoint detection
        forms = soup.find_all('form')
        for form in forms:
            action = form.get('action', '').lower()
            if any(term in action for term in ['search', 'query', 'find']):
                results['Has_Search_Endpoint'] = True
                break
        
        # Resources page detection
        links = soup.find_all('a', href=True)
        for link in links:
            href = link.get('href', '').lower()
            text = link.get_text().lower()
            if any(term in href or term in text for term in ['resource', 'download', 'library']):
                results['Has_Resources_Page'] = True
                break
        
        # Events page detection
        for link in links:
            href = link.get('href', '').lower()
            text = link.get_text().lower()
            if any(term in href or term in text for term in ['event', 'show', 'trade', 'calendar']):
                results['Has_Events_Page'] = True
                break
        
        # Modern CSS detection
        css_links = soup.find_all('link', rel='stylesheet')
        results['Uses_Modern_CSS'] = len(css_links) > 0
        
        # Broken links detection (simplified - just count 404-prone patterns)
        broken_patterns = ['#', 'javascript:void', 'mailto:']
        broken_count = 0
        for link in links[:50]:  # Limit check for performance
            href = link.get('href', '')
            if any(pattern in href for pattern in broken_patterns):
                broken_count += 1
        
        results['Broken_Links_Count'] = broken_count
    
    def _calculate_pain_scores(self, results: Dict):
        """Calculate pain scores for each EDP based on indicators found"""
        
        # EDP1: SKU Complexity Pain Score
        score = 0
        if not results['EDP1_Has_Search']:
            score += 40
        if results['EDP1_SKU_Count_Estimate'] > 2000:
            score += 30
        if results['EDP1_Filter_Count'] < 3:
            score += 20
        if results['EDP1_Has_Configurator']:
            score += 10
        results['EDP1_SKU_Complexity_Pain_Score'] = min(score, 100)
        
        # EDP2: Rep Performance Pain Score
        score = 0
        if not results['EDP2_Has_Rep_Locator']:
            score += 35
        if not results['EDP2_Rep_Portal_Exists']:
            score += 50
        if not results['EDP2_Rep_Resources_Accessible']:
            score += 15
        results['EDP2_Rep_Performance_Pain_Score'] = min(score, 100)
        
        # EDP6: Channel Conflict Pain Score
        score = 0
        if results['EDP6_Channel_Count'] > 2:
            score += (results['EDP6_Channel_Count'] - 2) * 20
        if results['EDP6_Pricing_Transparency'] in ['None', 'Quote only']:
            score += 40
        if results['EDP6_Multi_Brand_Detected']:
            score += 20
        results['EDP6_Channel_Conflict_Pain_Score'] = min(score, 100)
        
        # EDP7: Sales Enablement Pain Score
        score = 0
        if not results['EDP7_Has_Product_Search']:
            score += 40
        if not results['EDP7_Has_Mobile_Optimization']:
            score += 35
        if not results['EDP7_Has_Comparison_Tool']:
            score += 15
        if not results['EDP7_Has_Downloadable_Assets']:
            score += 10
        results['EDP7_Sales_Enablement_Pain_Score'] = min(score, 100)
        
        # EDP8: Technology Obsolescence Pain Score
        score = 0
        if not results['EDP8_Has_SSL']:
            score += 50
        if results['EDP8_Page_Speed_Score'] == 'Poor':
            score += 30
        elif results['EDP8_Page_Speed_Score'] == 'Average':
            score += 15
        if results['EDP8_Modern_Feature_Count'] < 2:
            score += 20
        if results['EDP8_Has_Legacy_Tech']:
            score += 25
        results['EDP8_Tech_Obsolescence_Pain_Score'] = min(score, 100)
        
        # Add specific missing features summary
        missing_features = []
        missing_features.extend(results['EDP7_Missing_Tools'])
        if not results['EDP8_Has_SSL']:
            missing_features.append('SSL certificate')
        if not results['EDP2_Rep_Portal_Exists']:
            missing_features.append('Rep portal')
        
        results['Specific_Missing_Features'] = missing_features
