# Add the missing method to website_evidence.py

method_to_add = '''
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
'''

with open('scrapers/website_evidence.py', 'r') as f:
    content = f.read()

# Check if method exists
if '_extract_personalization_data' not in content:
    # Find where to insert (before _identify_tam_tier_indicators)
    insert_pos = content.find('def _identify_tam_tier_indicators')
    if insert_pos > 0:
        # Insert the method
        content = content[:insert_pos] + method_to_add + '\n' + content[insert_pos:]
        
        with open('scrapers/website_evidence.py', 'w') as f:
            f.write(content)
        print("✅ Added _extract_personalization_data method")
else:
    print("✅ Method already exists")
