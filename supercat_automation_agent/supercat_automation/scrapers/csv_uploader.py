# scrapers/csv_uploader.py
"""
CSV Upload Handler for SuperCat GTM
Processes uploaded account lists through the same pipeline as scraped companies
Updated to match actual CSV headers
"""

import pandas as pd
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path
import uuid

logger = logging.getLogger(__name__)

class CSVAccountUploader:
    """
    Handles CSV uploads of target accounts
    Integrates with existing pain detection and campaign generation pipeline
    """
    
    def __init__(self):
        # Updated to match your actual CSV columns
        self.required_columns = ['company_name', 'domain']
        self.all_columns = [
            'first_name',
            'last_name', 
            'title',
            'company_name',
            'domain',
            'industry',
            'employee_count',
            'LinkedIn Profile',  # Note the space
            'email'
        ]
    
    def validate_csv(self, file_path: str) -> tuple[bool, str]:
        """
        Validate CSV has required columns and data
        """
        try:
            df = pd.read_csv(file_path)
            
            # Check required columns
            missing_cols = [col for col in self.required_columns if col not in df.columns]
            if missing_cols:
                return False, f"Missing required columns: {missing_cols}"
            
            # Check for empty required fields
            if df['company_name'].isna().any() or df['domain'].isna().any():
                return False, "Some rows have empty company_name or domain"
            
            # Validate domains (basic check)
            invalid_domains = df[~df['domain'].str.contains('.', na=False)]
            if not invalid_domains.empty:
                return False, f"Invalid domains found: {invalid_domains['domain'].tolist()[:5]}"
            
            # Count valid rows
            valid_rows = df.dropna(subset=['company_name', 'domain']).shape[0]
            return True, f"Valid CSV with {valid_rows} companies ready to process"
            
        except Exception as e:
            return False, f"Error reading CSV: {str(e)}"
    
    def process_csv(self, file_path: str, limit: int = None) -> List[Dict[str, Any]]:
        """
        Process CSV and return standardized company records
        
        Args:
            file_path: Path to CSV file
            limit: Optional limit on number of companies to process
            
        Returns:
            List of company dictionaries ready for pain analysis
        """
        df = pd.read_csv(file_path)
        
        # Drop rows with missing required fields
        df = df.dropna(subset=['company_name', 'domain'])
        
        # Apply limit if specified
        if limit:
            df = df.head(limit)
        
        companies = []
        for _, row in df.iterrows():
            # Normalize domain
            domain = str(row['domain']).lower().strip()
            if not domain.startswith('http'):
                domain = f"https://{domain}"
            
            # Build company record with your actual columns
            company = {
                'company_id': str(uuid.uuid4()),
                'company_name': str(row['company_name']).strip(),
                'domain': domain,
                'website': domain,
                'source': 'csv_upload',
                'upload_date': datetime.now().isoformat(),
                
                # Contact information from your columns
                'contact_first_name': str(row.get('first_name', '')).strip() if pd.notna(row.get('first_name')) else '',
                'contact_last_name': str(row.get('last_name', '')).strip() if pd.notna(row.get('last_name')) else '',
                'contact_email': str(row.get('email', '')).strip() if pd.notna(row.get('email')) else '',
                'contact_title': str(row.get('title', '')).strip() if pd.notna(row.get('title')) else '',
                'contact_linkedin': str(row.get('LinkedIn Profile', '')).strip() if pd.notna(row.get('LinkedIn Profile')) else '',
                
                # Company information
                'industry': str(row.get('industry', '')).strip() if pd.notna(row.get('industry')) else '',
                'employee_count': str(row.get('employee_count', '')).strip() if pd.notna(row.get('employee_count')) else '',
                
                # Initialize fields for pain analysis
                'edp_scores': {},
                'website_evidence': {},
                'qualification_tier': None,
                'psi_score': 0.0,
                'campaign_status': 'pending_analysis'
            }
            
            companies.append(company)
        
        logger.info(f"Processed {len(companies)} companies from CSV")
        return companies
    
    def export_results(self, companies: List[Dict], output_path: str = None):
        """
        Export processed companies with analysis results
        """
        if not output_path:
            output_path = f"uploads/results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # Create output directory if needed
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Flatten the company dictionaries for CSV export
        flattened = []
        for company in companies:
            flat = {
                'company_name': company['company_name'],
                'domain': company['domain'],
                'first_name': company.get('contact_first_name', ''),
                'last_name': company.get('contact_last_name', ''),
                'email': company.get('contact_email', ''),
                'title': company.get('contact_title', ''),
                'linkedin': company.get('contact_linkedin', ''),
                'industry': company.get('industry', ''),
                'employee_count': company.get('employee_count', ''),
                'qualification_tier': company.get('qualification_tier', ''),
                'psi_score': company.get('psi_score', 0),
                'primary_edp': company.get('primary_edp', ''),
                'campaign_status': company.get('campaign_status', '')
            }
            
            # Add EDP scores
            for edp, score in company.get('edp_scores', {}).items():
                flat[f'edp_{edp}'] = score
            
            flattened.append(flat)
        
        df = pd.DataFrame(flattened)
        df.to_csv(output_path, index=False)
        
        print(f"\n✅ Results exported to: {output_path}")
        return output_path

# Test function for your 72 prospects
def test_with_real_data():
    """Test function to validate your CSV"""
    uploader = CSVAccountUploader()
    
    # Replace with your actual CSV path
    csv_path = "prospects.csv"  # Update this to your file path
    
    # Validate
    valid, message = uploader.validate_csv(csv_path)
    print(f"Validation: {message}")
    
    if valid:
        # Process all 72 prospects
        companies = uploader.process_csv(csv_path)
        print(f"\nProcessed {len(companies)} companies")
        
        # Show first company as example
        if companies:
            first = companies[0]
            print(f"\nFirst company example:")
            print(f"  Company: {first['company_name']}")
            print(f"  Domain: {first['domain']}")
            print(f"  Contact: {first['contact_first_name']} {first['contact_last_name']}")
            print(f"  Title: {first['contact_title']}")
            print(f"  Email: {first['contact_email']}")
            
    return companies

if __name__ == "__main__":
    # Run test with your data
    test_with_real_data()