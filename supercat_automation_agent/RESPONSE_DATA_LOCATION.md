# 📊 Where Your EDP Analysis Data Is Located

## 🎯 **DATA STRUCTURE BREAKDOWN**

Your API returns a **200 success** with this structure:

```json
{
  "status": "success",
  "analysis": {
    // ← ALL YOUR EDP DATA IS HERE IN "analysis" section
  },
  "timestamp": "2025-10-03T03:52:36.943979"
}
```

## 📈 **KEY DATA LOCATIONS FOR CLAY**

### **Primary Scores (in `analysis` section):**
```javascript
// Clay can access these fields:
response.analysis.total_pain_score         // = 1.46
response.analysis.weighted_psi_score       // = 36.5  
response.analysis.qualification_tier        // = "TIER_B_ACTIVE"
response.analysis.weighted_primary_edp      // = "rep_performance_crisis"
```

### **EDP Rankings (Top Pain Points):**
```javascript
// Clay can access top EDPs:
response.analysis.edp_rankings[0]           // = ["rep_performance_crisis", 0.71, "strong"]
response.analysis.edp_rankings[1]           // = ["sales_enablement_collapse", 0.50, "moderate"] 
response.analysis.edp_rankings[2]           // = ["technology_obsolescence", 0.186, "weak"]
```

### **Individual EDP Details:**
```javascript
// Clay can access specific EDP analysis:
response.analysis.sales_enablement_collapse.score          // = 0.5
response.analysis.rep_performance_crisis.score             // = 0.71
response.analysis.technology_obsolescence.score             // = 0.186

// Evidence and specific issues:
response.analysis.sales_enablement_collapse.specific_issues
response.analysis.sales_enablement_collapse.indicators_found
```

### **Clay-Ready Summary Fields:**
```javascript
response.analysis.missing_features          // = "no_product_search, no_dealer_portal..."
response.analysis.evidence_hooks            // = "No product search functionality found..."
response.analysis.personalization_hunks      // = [{"type": "company_name", "value": "..."}]
```

## 🎯 **WHAT CLAY RECEIVES**

Clay webhook gets the **complete response** with `status: "success"` and **all data nested under `analysis`**.

### **For Clay Formula Builder:**
- **Total Pain Score**: `analysis.total_pain_score`
- **Qualification Tier**: `analysis.qualification_tier`  
- **Top EDP**: `analysis.edp_rankings[0][0]`
- **Top EDP Score**: `analysis.edp_rankings[0][1]`
- **Evidence Hooks**: `analysis.evidence_hooks`
- **Missing Features**: `analysis.missing_features`

### **Example Clay Formula:**
```
IF(analysis.qualification_tier == "TIER_A_IMMEDIATE", 
   "🚨 IMMEDIATE ACTION - " + analysis.weighted_primary_edp,
   IF(analysis.qualification_tier == "TIER_B_ACTIVE", 
      "⚡ ACTIVE LEAD - " + analysis.edp_rankings[0][0],
      "👀 NURTURE - " + analysis.edp_rankings[0][0]))
```

## 🔍 **DATA FLOW TO CLAY**

1. **Clay sends**: `{"company_name": "Test Corp", "domain": "test.com"}`
2. **Your API returns**: Complete EDP analysis in `analysis` section
3. **Clay accesses**: `response.analysis.total_pain_score`, `response.analysis.edp_rankings`, etc.
4. **Clay uses**: For lead scoring, personalization, routing, etc.

## ✅ **VERIFICATION**

Your current test shows:
- ✅ **200 status** = API working
- ✅ **Complete data** in `analysis` section  
- ✅ **All 5 EDPs** analyzed (sales_enablement_collapse, technology_obsolescence, etc.)
- ✅ **Scoring working** (total_pain_score: 1.46, psi_score: 36.5)
- ✅ **Ready for Clay** integration

**The data IS coming back - it's all nested under `response.analysis`!**

