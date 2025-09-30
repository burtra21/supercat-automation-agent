-- Core Tables for SuperCat GTM Automation

-- Companies table
CREATE TABLE IF NOT EXISTS companies (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    domain VARCHAR(255) UNIQUE,
    industry VARCHAR(100),
    employee_count INTEGER,
    revenue_estimate BIGINT,
    current_erp VARCHAR(100),
    trade_shows TEXT[],
    source VARCHAR(50),
    
    -- Pain scoring
    edp_scores JSONB DEFAULT '{}',
    edp_tags TEXT[] DEFAULT '{}',
    tam_tier VARCHAR(50),
    primary_edp VARCHAR(100),
    has_multiple_edps BOOLEAN DEFAULT FALSE,
    edp_count INTEGER DEFAULT 0,
    psi_score FLOAT DEFAULT 0,
    overall_pain_score FLOAT DEFAULT 0,
    
    -- Evidence
    website_evidence JSONB DEFAULT '{}',
    last_website_scan TIMESTAMP,
    
    -- Qualification
    tier_1_qualified BOOLEAN DEFAULT FALSE,
    tier_2_qualified BOOLEAN DEFAULT FALSE,
    qualification_score FLOAT DEFAULT 0,
    disqualified BOOLEAN DEFAULT FALSE,
    
    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Trade shows table
CREATE TABLE IF NOT EXISTS trade_shows (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    venue VARCHAR(255),
    start_date DATE,
    end_date DATE,
    industry VARCHAR(100),
    website_url VARCHAR(500),
    exhibitor_list_url VARCHAR(500),
    estimated_attendance INTEGER,
    last_scraped TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Decision makers table
CREATE TABLE IF NOT EXISTS decision_makers (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    company_id UUID REFERENCES companies(id),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    title VARCHAR(200),
    linkedin_url VARCHAR(500),
    is_champion_persona BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Campaigns table
CREATE TABLE IF NOT EXISTS campaigns (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    company_id UUID REFERENCES companies(id),
    campaign_type VARCHAR(50),
    campaign_status VARCHAR(50) DEFAULT 'draft',
    pain_point_focus VARCHAR(100),
    primary_hook TEXT,
    email_sequence JSONB DEFAULT '[]',
    linkedin_messages JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_companies_tam_tier ON companies(tam_tier);
CREATE INDEX IF NOT EXISTS idx_companies_domain ON companies(domain);
