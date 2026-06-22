# Customer Churn Analysis - Detailed Report

## Executive Summary

**Overall Churn Rate: 38.6%** (193 out of 500 customers)

This analysis identifies the major drivers of customer churn for the streaming service using statistical testing, machine learning feature importance, and correlation analysis.

---

## Major Churn Drivers (Ranked by Importance)

### 1. **LOW ENGAGEMENT - Viewing Hours** ⭐⭐⭐ (CRITICAL)
- **Feature Importance: 23.8%** (Highest)
- **Impact**: Churned customers watch **20.0% fewer hours** (66.6h vs 83.2h)
- **Statistical Significance**: p < 0.0001 (highly significant)
- **Insight**: Low viewing hours is the single strongest predictor of churn

### 2. **LOW ENGAGEMENT - Session Duration** ⭐⭐⭐ (CRITICAL)
- **Feature Importance: 21.6%** (Second highest)
- **Impact**: Churned customers have **14.4% shorter sessions** (49.4 min vs 57.8 min)
- **Statistical Significance**: p < 0.0001 (highly significant)
- **Insight**: Customers who spend less time per session are more likely to leave

### 3. **CUSTOMER SERVICE INTERACTIONS** ⭐⭐⭐ (CRITICAL)
- **Feature Importance: 9.1%**
- **Impact**: Churned customers had **27.7% more service interactions** (3.18 vs 2.49)
- **Correlation**: +0.28 (strongest positive correlation)
- **Statistical Significance**: p < 0.0001 (highly significant)
- **Insight**: More service calls indicate dissatisfaction and technical issues

### 4. **CONTENT VARIETY - Unique Titles Watched** ⭐⭐
- **Feature Importance: 15.9%** (Third highest)
- **Impact**: Churned customers watched **18.1% fewer unique titles** (19.5 vs 23.7)
- **Statistical Significance**: p < 0.0001 (highly significant)
- **Insight**: Limited content exploration indicates lack of engagement

### 5. **BINGE WATCHING BEHAVIOR** ⭐⭐
- **Feature Importance: 11.2%**
- **Impact**: Churned customers had **19.7% fewer binge sessions** (6.2 vs 7.7)
- **Statistical Significance**: p < 0.0001 (highly significant)
- **Insight**: Binge watching indicates strong engagement and loyalty

### 6. **SUBSCRIPTION TIER** ⭐⭐
- **Feature Importance: 3.5%**
- **Churn Rates by Tier**:
  - **Basic**: 43.5% churn (207 customers) - HIGHEST RISK
  - **Standard**: 39.5% churn (210 customers)
  - **Premium**: 24.1% churn (83 customers) - LOWEST RISK
- **Statistical Significance**: p = 0.0086 (significant)
- **Insight**: Basic tier customers are nearly **2x more likely** to churn than Premium

### 7. **MONTHLY COST** ⭐
- **Feature Importance: 3.6%**
- **Impact**: Churned customers pay **7.7% less** on average ($11.18 vs $12.11)
- **Statistical Significance**: p = 0.0047 (significant)
- **Insight**: Lower-paying customers show higher churn, related to tier

### 8. **GENRE PREFERENCE**
- **Feature Importance: 11.4%**
- **Highest Churn Genres**:
  - Horror: 52.3% churn rate
  - Thriller: 48.3% churn rate
  - Action: 44.6% churn rate
- **Lowest Churn Genres**:
  - Documentary: 25.9% churn rate
  - Comedy: 33.0% churn rate
  - Drama: 35.3% churn rate
- **Statistical Significance**: p = 0.12 (marginally significant)
- **Insight**: Genre preferences show patterns but are less predictive

---

## Statistical Analysis Summary

### Univariate Analysis (T-tests)
All numerical features showed **highly significant differences** between churned and retained customers (p < 0.001):

| Feature | Churned Mean | Retained Mean | Difference | P-value |
|---------|-------------|---------------|------------|---------|
| Viewing Hours | 66.6 | 83.2 | -20.0% | < 0.0001*** |
| Binge Sessions | 6.2 | 7.7 | -19.7% | < 0.0001*** |
| Unique Titles | 19.5 | 23.7 | -18.1% | < 0.0001*** |
| Session Duration | 49.4 min | 57.8 min | -14.4% | < 0.0001*** |
| CS Interactions | 3.18 | 2.49 | +27.7% | < 0.0001*** |
| Monthly Cost | $11.18 | $12.11 | -7.7% | 0.0047** |

### Logistic Regression Coefficients (Standardized)
Largest positive effects (increase churn):
1. Customer Service Interactions: +0.461
2. Subscription Tier (Basic): +0.230

Largest negative effects (reduce churn):
1. Monthly Cost (Premium): -0.350
2. Total Viewing Hours: -0.262

---

## Key Insights & Patterns

### 🔴 High-Risk Customer Profile
- Basic or Standard subscription tier
- < 70 hours viewing per month
- < 50 minutes average session duration
- < 20 unique titles watched
- ≥ 3 customer service interactions
- Prefers Horror, Thriller, or Action genres
- **Predicted Churn Risk: 50-70%**

### 🟢 Low-Risk Customer Profile
- Premium subscription tier
- > 90 hours viewing per month
- > 60 minutes average session duration
- > 25 unique titles watched
- ≤ 2 customer service interactions
- Prefers Documentary or Comedy genres
- **Predicted Churn Risk: 15-25%**

---

## Root Cause Analysis

### Primary Cause: **Lack of Engagement**
Combined viewing hours, session duration, and content variety account for **~60% of predictive power**. This suggests:
- Content library may not meet user needs
- User experience issues reducing engagement
- Lack of compelling content discovery

### Secondary Cause: **Service Quality Issues**
Higher customer service interactions correlate strongly with churn, indicating:
- Technical problems (streaming quality, login issues)
- Billing or account issues
- Poor customer support experience

### Tertiary Cause: **Value Perception**
Basic tier shows highest churn, suggesting:
- Lower perceived value at lower price points
- Premium features create stickiness
- Price sensitivity less important than engagement

---

## Strategic Recommendations

### Immediate Actions (0-30 days)
1. **Identify At-Risk Customers**
   - Flag customers with < 70 viewing hours last month
   - Monitor customers with > 2 service interactions
   - Create early intervention program

2. **Improve Customer Service**
   - Analyze root causes of service interactions
   - Implement proactive support for technical issues
   - Reduce response times

### Short-Term Actions (1-3 months)
3. **Boost Engagement Programs**
   - Personalized content recommendations
   - "What to watch next" campaigns
   - Gamification and viewing challenges

4. **Premium Tier Promotion**
   - Highlight value of Premium features
   - Offer limited-time upgrades for Basic users
   - A/B test pricing and feature bundles

### Long-Term Actions (3-6 months)
5. **Content Strategy**
   - Expand Documentary and Comedy offerings (low churn)
   - Improve Horror/Thriller content quality or reduce focus
   - Create binge-worthy series and collections

6. **User Experience Enhancement**
   - Improve content discovery algorithms
   - Reduce friction in viewing experience
   - Mobile and multi-device optimization

---

## Monitoring Metrics

Track these KPIs weekly/monthly:
- Average viewing hours per customer
- Average session duration
- Customer service interaction rate
- Tier distribution and migration
- Binge session frequency
- Content diversity index (unique titles per user)

---

## Conclusion

Churn is primarily driven by **low engagement** rather than price sensitivity. Customers who watch less content, spend less time per session, and explore fewer titles are the most likely to leave. Customer service issues compound this problem. 

**The solution is not price reduction but engagement enhancement and service quality improvement.**

Focus on:
1. ✅ Increasing viewing hours through better content discovery
2. ✅ Reducing customer service issues through proactive support
3. ✅ Promoting Premium tier to improve value perception
4. ✅ Creating binge-worthy content and personalized recommendations
