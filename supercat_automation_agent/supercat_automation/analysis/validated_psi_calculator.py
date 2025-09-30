"""
Validated PSI Calculator - Dual Methodology Implementation
Based on C2 Supercat Customer Pain Signal Validation Study

Implements both:
1. Weighted methodology (purchase-driven) - for qualification
2. Averaged methodology (operational intelligence) - for account context
"""

import json
import logging
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import math

logger = logging.getLogger(__name__)

class ValidatedPSICalculator:
    """
    Dual methodology PSI calculator based on validation study findings
    
    Weighted Method: EDP7 (35%) + EDP8 (30%) + EDP2 (20%) + EDP1 (10%) + EDP6 (5%)
    Averaged Method: All EDPs weighted equally at 20%
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize with validated weights and thresholds"""
        self.config_path = config_path or "supercat_automation/config/validated_edp_weights.json"
        self.messaging_config_path = "supercat_automation/config/crisis_messaging.json"
        
        # Load validated configuration
        self.config = self._load_config()
        self.messaging_config = self._load_messaging_config()
        
        # Extract weights
        self.weighted_weights = self.config["weighted_methodology"]["weights"]
        self.averaged_weights = self.config["averaged_methodology"]["weights"]
        self.crisis_thresholds = self.config["crisis_thresholds"]
        
        logger.info("Initialized ValidatedPSICalculator with dual methodology")
    
    def _load_config(self) -> Dict[str, Any]:
        """Load validated EDP weights configuration"""
        try:
            config_file = Path(self.config_path)
            if not config_file.exists():
                logger.warning(f"Config file not found: {self.config_path}, using defaults")
                return self._get_default_config()
            
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return self._get_default_config()
    
    def _load_messaging_config(self) -> Dict[str, Any]:
        """Load crisis messaging configuration"""
        try:
            config_file = Path(self.messaging_config_path)
            if not config_file.exists():
                logger.warning(f"Messaging config not found: {self.messaging_config_path}")
                return {}
            
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading messaging config: {e}")
            return {}
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Fallback configuration if files not found"""
        return {
            "weighted_methodology": {
                "weights": {
                    "EDP1_SKU_Complexity": 0.12,
                    "EDP2_Rep_Management": 0.15,
                    "EDP6_Channel_Conflict": 0.05,
                    "EDP7_Sales_Enablement": 0.35,
                    "EDP8_Technology_Obsolescence": 0.33
                }
            },
            "averaged_methodology": {
                "weights": {
                    "EDP1_SKU_Complexity": 0.20,
                    "EDP2_Rep_Management": 0.20,
                    "EDP6_Channel_Conflict": 0.20,
                    "EDP7_Sales_Enablement": 0.20,
                    "EDP8_Technology_Obsolescence": 0.20
                }
            },
            "crisis_thresholds": {
                "tier_a_immediate": {"weighted_psi_min": 70},
                "tier_b_active": {"weighted_psi_min": 40, "weighted_psi_max": 69},
                "tier_c_monitor": {"weighted_psi_max": 39}
            }
        }
    
    def calculate_dual_psi(self, company_data: Dict[str, Any], website_evidence: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate both weighted and averaged PSI scores
        
        Args:
            company_data: Company information (name, domain, rep_count, etc.)
            website_evidence: Website analysis results
            
        Returns:
            Dict containing both methodologies' results
        """
        
        # Calculate individual EDP scores
        edp_scores = self._calculate_edp_scores(company_data, website_evidence)
        
        # Calculate weighted PSI (purchase-driven)
        weighted_psi = self._calculate_weighted_psi(edp_scores)
        
        # Calculate averaged PSI (operational intelligence)
        averaged_psi = self._calculate_averaged_psi(edp_scores)
        
        # Determine primary EDPs for each methodology
        weighted_primary = self._get_primary_edp(edp_scores, self.weighted_weights)
        averaged_primary = self._get_primary_edp(edp_scores, self.averaged_weights)
        
        # Determine tiers
        weighted_tier = self._get_tier(weighted_psi, "weighted")
        averaged_tier = self._get_tier(averaged_psi, "averaged")
        
        # Generate messaging hooks
        messaging = self._generate_messaging_hooks(
            company_data, edp_scores, weighted_primary, averaged_primary, weighted_psi
        )
        
        # Compile results
        results = {
            "methodology": "dual_validated",
            "validation_study_source": "C2 Supercat Customer Pain Signal Validation Study",
            
            # Individual EDP scores (0-100 scale)
            "edp_scores": edp_scores,
            
            # Weighted methodology (primary for qualification)
            "weighted_methodology": {
                "psi_score": round(weighted_psi, 2),
                "primary_edp": weighted_primary,
                "tier": weighted_tier,
                "qualification_decision": weighted_tier in ["TIER_A_IMMEDIATE", "TIER_B_ACTIVE"],
                "purchase_probability": self._get_purchase_probability(weighted_psi, weighted_primary)
            },
            
            # Averaged methodology (intelligence for account context)
            "averaged_methodology": {
                "psi_score": round(averaged_psi, 2),
                "primary_edp": averaged_primary,
                "tier": averaged_tier,
                "operational_intelligence": self._get_operational_intelligence(averaged_primary, edp_scores)
            },
            
            # Messaging and hooks
            "messaging": messaging,
            
            # Evidence and patterns
            "evidence_patterns": self._extract_evidence_patterns(website_evidence, edp_scores),
            
            # Comparison insights
            "methodology_comparison": {
                "primary_edp_match": weighted_primary == averaged_primary,
                "psi_difference": abs(weighted_psi - averaged_psi),
                "strategic_implications": self._get_strategic_implications(
                    weighted_primary, averaged_primary, weighted_psi, averaged_psi
                )
            }
        }
        
        return results
    
    def _calculate_edp_scores(self, company_data: Dict[str, Any], website_evidence: Dict[str, Any]) -> Dict[str, float]:
        """Calculate individual EDP scores (0-100 scale) using actual website evidence"""
        
        # Check if we have v2 website evidence with calculated pain scores
        if 'EDP1_SKU_Complexity_Pain_Score' in website_evidence:
            # Use the calculated pain scores from WebsiteEvidenceExtractorV2
            edp_scores = {
                "EDP1_SKU_Complexity": float(website_evidence.get('EDP1_SKU_Complexity_Pain_Score', 0)),
                "EDP2_Rep_Management": float(website_evidence.get('EDP2_Rep_Performance_Pain_Score', 0)),
                "EDP6_Channel_Conflict": float(website_evidence.get('EDP6_Channel_Conflict_Pain_Score', 0)),
                "EDP7_Sales_Enablement": float(website_evidence.get('EDP7_Sales_Enablement_Pain_Score', 0)),
                "EDP8_Technology_Obsolescence": float(website_evidence.get('EDP8_Tech_Obsolescence_Pain_Score', 0))
            }
        else:
            # Fallback to original logic for v1 compatibility
            evidence = website_evidence.get('evidence', [])
            tech_stack = website_evidence.get('tech_stack', [])
            
            edp_scores = {
                "EDP1_SKU_Complexity": self._calculate_sku_complexity_score(company_data, evidence),
                "EDP2_Rep_Management": self._calculate_rep_management_score(company_data, evidence),
                "EDP6_Channel_Conflict": self._calculate_channel_conflict_score(company_data, evidence),
                "EDP7_Sales_Enablement": self._calculate_sales_enablement_score(company_data, evidence),
                "EDP8_Technology_Obsolescence": self._calculate_technology_obsolescence_score(
                    company_data, evidence, tech_stack
                )
            }
        
        # Cap all scores at 100
        for edp in edp_scores:
            edp_scores[edp] = min(100.0, max(0.0, edp_scores[edp]))
        
        return edp_scores
    
    def _calculate_sku_complexity_score(self, company_data: Dict[str, Any], evidence: List[str]) -> float:
        """Calculate EDP1 SKU Complexity score"""
        score = 0.0
        evidence_str = ' '.join(evidence).lower()
        
        # Catalog format issues
        if 'pdf' in evidence_str and 'catalog' in evidence_str:
            score += 40
        elif 'spreadsheet' in evidence_str:
            score += 30
        
        # Search functionality
        if 'no product search' in evidence_str:
            score += 40
        elif 'limited search' in evidence_str:
            score += 25
        
        # SKU count impact
        sku_count = company_data.get('catalog_sku_count', 0)
        if sku_count > 5000:
            score += 30
        elif sku_count > 2000:
            score += 20
        
        # Configuration complexity
        if 'configurator' in evidence_str:
            score += 20
        
        return score
    
    def _calculate_rep_management_score(self, company_data: Dict[str, Any], evidence: List[str]) -> float:
        """Calculate EDP2 Rep Management score"""
        score = 0.0
        evidence_str = ' '.join(evidence).lower()
        
        # Rep portal existence
        if 'no rep portal' in evidence_str or 'dealer login' in evidence_str:
            score += 50
        
        # Rep count impact
        rep_count = company_data.get('rep_count', 0)
        if rep_count > 50 and 'no portal' in evidence_str:
            score += 30
        elif rep_count > 30:
            score += 20
        
        # Territory management
        if 'territory' in evidence_str and 'complex' in evidence_str:
            score += 20
        
        return score
    
    def _calculate_channel_conflict_score(self, company_data: Dict[str, Any], evidence: List[str]) -> float:
        """Calculate EDP6 Channel Conflict score"""
        score = 0.0
        evidence_str = ' '.join(evidence).lower()
        
        # Channel count
        channel_count = company_data.get('channel_count', 1)
        if channel_count > 2:
            score += (channel_count - 2) * 20
        
        # Pricing transparency
        if 'no pricing' in evidence_str or 'call for price' in evidence_str:
            score += 40
        elif 'login required' in evidence_str and 'pricing' in evidence_str:
            score += 30
        elif 'quote only' in evidence_str:
            score += 20
        
        # Brand complexity
        brand_count = company_data.get('brand_count', 1)
        if brand_count > 1:
            score += brand_count * 15
        
        return score
    
    def _calculate_sales_enablement_score(self, company_data: Dict[str, Any], evidence: List[str]) -> float:
        """Calculate EDP7 Sales Enablement score (primary purchase driver)"""
        score = 0.0
        evidence_str = ' '.join(evidence).lower()
        
        # Product search (critical)
        if 'no product search' in evidence_str:
            score += 40
        elif 'limited search' in evidence_str or 'no filters' in evidence_str:
            score += 25
        
        # Mobile optimization (trade show critical)
        if 'no mobile' in evidence_str or 'mobile failure' in evidence_str:
            score += 35
        
        # Comparison tools
        if 'no comparison' in evidence_str:
            score += 15
        
        # Wishlist/Projects
        if 'no wishlist' in evidence_str:
            score += 15
        
        # Asset availability
        if 'no assets' in evidence_str or 'limited resources' in evidence_str:
            score += 45
        
        # Login requirements (friction)
        if 'requires login' in evidence_str:
            score += 20
        
        return score
    
    def _calculate_technology_obsolescence_score(self, company_data: Dict[str, Any], 
                                               evidence: List[str], tech_stack: List[str]) -> float:
        """Calculate EDP8 Technology Obsolescence score (secondary purchase driver)"""
        score = 0.0
        evidence_str = ' '.join(evidence).lower()
        tech_str = ' '.join(tech_stack).lower()
        
        # SSL certificate (critical)
        if 'no ssl' in evidence_str:
            score += 50
        
        # Page speed
        if 'slow' in evidence_str or 'poor performance' in evidence_str:
            score += 30
        elif 'average speed' in evidence_str:
            score += 15
        
        # Modern features
        modern_feature_count = 0
        modern_features = ['api', 'integration', 'mobile', 'responsive']
        for feature in modern_features:
            if feature in evidence_str or feature in tech_str:
                modern_feature_count += 1
        
        if modern_feature_count < 2:
            score += 35
        
        # Legacy technology indicators
        if 'wordpress' in tech_str:
            score += 20
        if 'old' in evidence_str or 'legacy' in evidence_str:
            score += 40
        
        # Copyright year (outdated maintenance)
        current_year = 2025
        copyright_year = company_data.get('copyright_year', current_year)
        if current_year - copyright_year > 2:
            score += 30
        
        return score
    
    def _calculate_weighted_psi(self, edp_scores: Dict[str, float]) -> float:
        """Calculate weighted PSI score (purchase-driven)"""
        weighted_sum = 0.0
        
        for edp, score in edp_scores.items():
            weight = self.weighted_weights.get(edp, 0.0)
            weighted_sum += (score * weight)
        
        return weighted_sum
    
    def _calculate_averaged_psi(self, edp_scores: Dict[str, float]) -> float:
        """Calculate averaged PSI score (operational intelligence)"""
        if not edp_scores:
            return 0.0
        
        return sum(edp_scores.values()) / len(edp_scores)
    
    def _get_primary_edp(self, edp_scores: Dict[str, float], weights: Dict[str, float]) -> str:
        """Determine primary EDP based on weighted scores"""
        if not edp_scores:
            return "unknown"
        
        weighted_scores = {}
        for edp, score in edp_scores.items():
            weight = weights.get(edp, 0.0)
            weighted_scores[edp] = score * weight
        
        return max(weighted_scores.items(), key=lambda x: x[1])[0]
    
    def _get_tier(self, psi_score: float, methodology: str) -> str:
        """Determine tier based on PSI score"""
        if methodology == "weighted":
            if psi_score >= self.crisis_thresholds["tier_a_immediate"]["weighted_psi_min"]:
                return "TIER_A_IMMEDIATE"
            elif psi_score >= self.crisis_thresholds["tier_b_active"]["weighted_psi_min"]:
                return "TIER_B_ACTIVE"
            else:
                return "TIER_C_MONITOR"
        else:
            # Use same thresholds for averaged methodology
            if psi_score >= 70:
                return "TIER_A_IMMEDIATE"
            elif psi_score >= 40:
                return "TIER_B_ACTIVE"
            else:
                return "TIER_C_MONITOR"
    
    def _get_purchase_probability(self, weighted_psi: float, primary_edp: str) -> float:
        """Calculate purchase probability based on validation study"""
        base_probability = min(0.95, weighted_psi / 100.0)
        
        # Adjust based on primary EDP correlation from validation study
        if primary_edp == "EDP7_Sales_Enablement":
            # 73% of customers, 100% correlation in study
            return min(0.95, base_probability * 1.1)
        elif primary_edp == "EDP8_Technology_Obsolescence":
            # 27% of customers, 93% correlation in study
            return min(0.93, base_probability * 1.05)
        else:
            # Other EDPs have lower purchase correlation
            return base_probability * 0.8
    
    def _get_operational_intelligence(self, primary_edp: str, edp_scores: Dict[str, float]) -> Dict[str, Any]:
        """Generate operational intelligence insights"""
        intelligence = {
            "primary_operational_challenge": primary_edp,
            "severity": "high" if edp_scores.get(primary_edp, 0) > 70 else "medium" if edp_scores.get(primary_edp, 0) > 40 else "low",
            "expansion_opportunities": [],
            "conversation_starters": []
        }
        
        # Add conversation starters from messaging config
        if self.messaging_config and "averaged_methodology_intelligence" in self.messaging_config:
            edp_key = primary_edp.replace("_", "").lower()
            for key, config in self.messaging_config["averaged_methodology_intelligence"].items():
                if edp_key in key.lower():
                    intelligence["conversation_starters"] = config.get("conversation_starters", [])
                    break
        
        # Identify expansion opportunities
        for edp, score in edp_scores.items():
            if score > 50 and edp != primary_edp:
                intelligence["expansion_opportunities"].append({
                    "edp": edp,
                    "score": score,
                    "opportunity": f"Secondary pain point with {score:.1f}% severity"
                })
        
        return intelligence
    
    def _generate_messaging_hooks(self, company_data: Dict[str, Any], edp_scores: Dict[str, float],
                                weighted_primary: str, averaged_primary: str, weighted_psi: float) -> Dict[str, Any]:
        """Generate messaging hooks based on methodology results"""
        
        messaging = {
            "weighted_methodology_hook": "",
            "averaged_methodology_hook": "",
            "crisis_level": "low",
            "urgency_triggers": [],
            "evidence_based_hooks": []
        }
        
        # Determine crisis level
        if weighted_psi >= 70:
            messaging["crisis_level"] = "immediate"
        elif weighted_psi >= 40:
            messaging["crisis_level"] = "active"
        else:
            messaging["crisis_level"] = "monitor"
        
        # Generate weighted methodology hook (for qualification)
        if self.messaging_config and "weighted_methodology_hooks" in self.messaging_config:
            weighted_hooks = self.messaging_config["weighted_methodology_hooks"]
            
            if weighted_primary == "EDP7_Sales_Enablement" and "EDP7_Sales_Enablement" in weighted_hooks:
                messaging["weighted_methodology_hook"] = weighted_hooks["EDP7_Sales_Enablement"]["primary_hook"]
                messaging["urgency_triggers"] = weighted_hooks["EDP7_Sales_Enablement"]["urgency_triggers"]
            elif weighted_primary == "EDP8_Technology_Obsolescence" and "EDP8_Technology_Obsolescence" in weighted_hooks:
                messaging["weighted_methodology_hook"] = weighted_hooks["EDP8_Technology_Obsolescence"]["primary_hook"]
                messaging["urgency_triggers"] = weighted_hooks["EDP8_Technology_Obsolescence"]["urgency_triggers"]
        
        # Generate averaged methodology hook (for intelligence)
        if self.messaging_config and "averaged_methodology_intelligence" in self.messaging_config:
            averaged_intel = self.messaging_config["averaged_methodology_intelligence"]
            
            for key, config in averaged_intel.items():
                if averaged_primary.lower().replace("_", "") in key.lower():
                    messaging["averaged_methodology_hook"] = config.get("intelligence_hook", "")
                    break
        
        # Add evidence-based hooks
        messaging["evidence_based_hooks"] = self._generate_evidence_hooks(company_data, edp_scores)
        
        return messaging
    
    def _generate_evidence_hooks(self, company_data: Dict[str, Any], edp_scores: Dict[str, float]) -> List[str]:
        """Generate specific evidence-based messaging hooks"""
        hooks = []
        
        company_name = company_data.get('company_name', 'your company')
        rep_count = company_data.get('rep_count', 10)
        sku_count = company_data.get('catalog_sku_count', 2000)
        channel_count = company_data.get('channel_count', 1)
        
        # EDP7 hooks
        if edp_scores.get("EDP7_Sales_Enablement", 0) > 60:
            hooks.append(f"No mobile site for High Point Market?")
            hooks.append(f"{company_name}: Manual catalog navigation killing productivity")
        
        # EDP8 hooks
        if edp_scores.get("EDP8_Technology_Obsolescence", 0) > 60:
            hooks.append(f"SSL EXPIRED - customers questioning credibility")
            hooks.append(f"{company_name} 40% slower than digital competitors")
        
        # EDP2 hooks
        if edp_scores.get("EDP2_Rep_Management", 0) > 60:
            hooks.append(f"Your {rep_count} reps have no portal")
        
        # EDP1 hooks
        if edp_scores.get("EDP1_SKU_Complexity", 0) > 60:
            hooks.append(f"{sku_count:,} SKUs but no search function")
        
        # EDP6 hooks
        if edp_scores.get("EDP6_Channel_Conflict", 0) > 60:
            hooks.append(f"{channel_count} channels, zero pricing visibility")
        
        return hooks
    
    def _extract_evidence_patterns(self, website_evidence: Dict[str, Any], edp_scores: Dict[str, float]) -> Dict[str, Any]:
        """Extract evidence patterns that predict purchases"""
        
        evidence = website_evidence.get('evidence', [])
        evidence_str = ' '.join(evidence).lower()
        
        patterns = {
            "digital_failures": [],
            "crisis_indicators": [],
            "competitive_gaps": []
        }
        
        # Digital failures from validation study
        if 'no product search' in evidence_str:
            patterns["digital_failures"].append({
                "pattern": "no_product_search",
                "frequency": "27% of customers",
                "correlation": "EDP7 - 100% correlation",
                "severity": "high"
            })
        
        if 'mobile' in evidence_str and ('fail' in evidence_str or 'no' in evidence_str):
            patterns["digital_failures"].append({
                "pattern": "mobile_optimization_failure", 
                "frequency": "20% of customers",
                "correlation": "EDP7 - 100% correlation",
                "severity": "high"
            })
        
        if 'no ssl' in evidence_str:
            patterns["digital_failures"].append({
                "pattern": "ssl_certificate_missing",
                "frequency": "13% of customers", 
                "correlation": "EDP8 - 93% correlation",
                "severity": "critical"
            })
        
        # Crisis indicators
        for edp, score in edp_scores.items():
            if score > 70:
                patterns["crisis_indicators"].append({
                    "edp": edp,
                    "score": score,
                    "level": "immediate_action_required"
                })
        
        return patterns
    
    def _get_strategic_implications(self, weighted_primary: str, averaged_primary: str, 
                                  weighted_psi: float, averaged_psi: float) -> Dict[str, Any]:
        """Analyze strategic implications of methodology differences"""
        
        implications = {
            "primary_edp_alignment": weighted_primary == averaged_primary,
            "messaging_strategy": "",
            "account_approach": "",
            "expansion_potential": ""
        }
        
        if weighted_primary == averaged_primary:
            implications["messaging_strategy"] = "Unified approach - both methodologies agree on primary pain"
            implications["account_approach"] = "Direct crisis intervention with operational context"
        else:
            implications["messaging_strategy"] = "Dual approach - lead with weighted, acknowledge averaged"
            implications["account_approach"] = "Crisis intervention first, operational efficiency second"
        
        # PSI difference analysis
        psi_diff = abs(weighted_psi - averaged_psi)
        if psi_diff > 20:
            implications["expansion_potential"] = "High - significant operational challenges beyond primary pain"
        elif psi_diff > 10:
            implications["expansion_potential"] = "Medium - some additional operational opportunities"
        else:
            implications["expansion_potential"] = "Low - focused pain point approach recommended"
        
        return implications

    def get_validation_summary(self) -> Dict[str, Any]:
        """Return validation study summary for reference"""
        return {
            "study_source": "C2 Supercat Customer Pain Signal Validation Study",
            "customer_base": "$2.3M portfolio, 15 companies, 89 data points",
            "key_findings": {
                "methodology_differences": "67% of companies show different primary EDPs",
                "weighted_validation": "73% EDP7, 27% EDP8 - validates customer interviews",
                "averaged_insights": "47% EDP6, 33% EDP7, 13% EDP2 - reveals operational challenges",
                "portfolio_health": "67.2% average PSI, 40% in crisis mode"
            },
            "implementation_strategy": {
                "primary_qualification": "Weighted methodology (purchase probability)",
                "intelligence_layer": "Averaged methodology (operational context)",
                "resource_allocation": "90% weighted focus, 10% averaged context"
            }
        }
