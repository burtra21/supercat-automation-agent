# database/migrations.py
"""
SQL migrations for EDP scoring system
Run these in your Supabase SQL editor
"""

migrations = """
-- Add EDP scoring columns to companies table
ALTER TABLE companies ADD COLUMN IF NOT EXISTS edp_scores JSONB DEFAULT '{}';
ALTER TABLE companies ADD COLUMN IF NOT EXISTS edp_tags TEXT[] DEFAULT '{}';
ALTER TABLE companies ADD COLUMN IF NOT EXISTS tam_tier VARCHAR(10);
ALTER TABLE companies ADD COLUMN IF NOT EXISTS website_evidence JSONB DEFAULT '{}';
ALTER TABLE companies ADD COLUMN IF NOT EXISTS last_website_scan TIMESTAMP;
ALTER TABLE companies ADD COLUMN IF NOT EXISTS psi_score FLOAT DEFAULT 0;

-- Create indexes for faster queries
CREATE INDEX IF NOT EXISTS idx_companies_tam_tier ON companies(tam_tier);
CREATE INDEX IF NOT EXISTS idx_companies_psi_score ON companies(psi_score DESC);
CREATE INDEX IF NOT EXISTS idx_companies_edp_tags ON companies USING GIN(edp_tags);

-- Add composite scoring
ALTER TABLE companies ADD COLUMN IF NOT EXISTS has_multiple_edps BOOLEAN DEFAULT FALSE;
ALTER TABLE companies ADD COLUMN IF NOT EXISTS primary_edp VARCHAR(50);
ALTER TABLE companies ADD COLUMN IF NOT EXISTS edp_count INTEGER DEFAULT 0;
"""

print("Copy and run these migrations in Supabase SQL editor:")
print(migrations)