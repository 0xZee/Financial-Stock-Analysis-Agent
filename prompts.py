from pydantic import BaseModel, Field
from typing import List, Dict



class ReportOutput(BaseModel):
    """Financial report model for Streamlit financial agent"""

    recommendation_key: str = Field(..., description="Recommendation for the stock (e.g., Buy, Hold, Sell)")
    risk_profile: str = Field(..., description="Risk level of the investment (e.g., Low, Medium, High)")
    stock_data: Dict[str, float] = Field(..., description="Key financial metrics for the stock, including price, market cap, etc.")
    company_overview: str = Field(..., description="Brief summary of the company's business and market positioning")
    financial_ratios_analysis: str = Field(..., description="Analysis of key financial ratios compared to industry benchmarks")
    market_performance: str = Field(..., description="Analysis of stock trends, valuation metrics, and market comparisons")
    risk_assessment: str = Field(..., description="Evaluation of market, operational, and financial risks")
    investment_recommendation: str = Field(..., description="Buy, Hold, or Sell recommendation with supporting rationale")
    competitive_landscape: str = Field(..., description="Assessment of the company's position relative to competitors")
    recent_news_impact: str = Field(..., description="Impact of recent news, earnings, or industry developments on performance")
    growth_potential: str = Field(..., description="Key growth drivers and opportunities for the company")
    conclusion_key_insights: str = Field(..., description="Summary of significant findings from the analysis")
    conclusion_valuation: str = Field(..., description="Assessment of whether the stock is overvalued, fairly valued, or undervalued")
    conclusion_risk_reward_balance: str = Field(..., description="Analysis of the balance between potential gains and risks")
    conclusion_catalysts: List[str] = Field(..., description="List of key events or developments that could impact performance")
    conclusion_investor_profile_match: str = Field(..., description="Suitable investor profile (e.g., conservative, moderate, aggressive)")
    conclusion_alternative_options: List[str] = Field(..., description="List of peer stocks or ETFs for comparison or diversification")
    conclusion_long_term_outlook: str = Field(..., description="Evaluation of the company's sustainability and strategic plans")
    conclusion_immediate_action: str = Field(..., description="Recommendation for immediate action or specific triggers to monitor")
    conclusion_final_verdict: str = Field(..., description="Restatement of the final Buy, Hold, or Sell recommendation with supporting evidence")


class FINANCE_REPORT(BaseModel):
    recommendation_key: str  # Example: "Buy, Hold, Sell"
    risk_profile: str  # Example: "Low, Medium, High"
    
    company_overview: str  # Brief summary of the company's business and market positioning.
    financial_ratios_analysis: str  # Key financial ratios and comparison to industry benchmarks.
    market_performance: str  # Stock trends, valuation metrics, and market comparisons.
    risk_assessment: str  # Evaluation of market, operational, and financial risks.
    investment_recommendation: str  # Buy/Hold/Sell rating with rationale and insights.
    competitive_landscape: str  # Analysis of the company's position relative to competitors.
    recent_news_impact: str  # Impact of recent news, earnings, or industry developments.
    growth_potential: str  # Key growth drivers and opportunities for the company.

    class ConclusionRecommendations(BaseModel):
        key_insights: str  # Summary of significant findings from the analysis.
        valuation: str  # Assessment of whether the stock is overvalued or undervalued.
        risk_reward_balance: str  # Balance of potential gains vs. risks.
        catalysts: str  # Events or developments that may impact performance.
        investor_profile_match: str  # Suitable investor profile (conservative, moderate, aggressive).
        alternative_options: str  # Peer stocks or ETFs for comparison.
        long_term_outlook: str  # Analysis of the company's sustainability and future plans.
        immediate_action: str  # Recommendation for immediate action or specific triggers to watch.
        final_verdict: str  # Restatement of the Buy/Hold/Sell recommendation with evidence.

    conclusion_recommendations: ConclusionRecommendations


# PROMPTS
REPORTER_TASK_PROMPT = f"""
A detailed financial analysis report with clear sections and supporting data, in markdown format with sections, titles, some tables and emojies, follow this format :

### `Financial Report : Company name | Date`

| date | Recommendation | Risk Level  | Risk Profile  |
|:----------:|:-------------:|:-------------:| :-------------:|
| Ticker | **OVERWEIGHT** / **BUY:** / **HOLD:** / **SELL:** | between 1 and 10 | ** LOW / MEDIUM / HIGH / VERY HIGH (assess based on market, financial, and operational risks). |

---

### `Company Overview`  
> Briefly summarize the company's business, key products/services, recent developments, and market positioning.  

### `Financial Ratios Analysis`  
> Highlight key ratios (profitability, liquidity, leverage, efficiency) and compare them to industry benchmarks.  

### `Market Performance`  
> Discuss stock trends, valuation metrics (e.g., P/E, P/S), and comparisons with industry indices.  

### `Risk Assessment`  
Evaluate market, operational, and financial risks, along with emerging challenges like ESG or technological disruption.  

### `Recent News Impact`  
> Summarize the impact of recent news, earnings reports, or industry developments on the company’s performance.  

### `Growth Potential`  
> Highlight growth drivers such as new markets, products, or strategic partnerships.  

### `Competitive Landscape`  
> Assess the company's position relative to key competitors in terms of market share, innovation, and strategy.  

### `Investment Recommendation`  
> Provide a clear **OVERWEIGHT** / **BUY:** / **HOLD:** / **SELL:** rating with supporting rationale and actionable insights.  

### `Conclusion & Recommendations`
present in 2-columns (Key,Value) table :
1. **Key Insights:** Summarize the most significant findings from the analysis.  
2. **Valuation:** Assess whether the stock is overvalued, fairly valued, or undervalued.  
3. **Risk-Reward Balance:** Weigh potential gains against identified risks.  
4. **Catalysts:** Identify events or developments that could drive short-term or long-term performance.  
5. **Investor Profile Match:** Specify if this investment suits conservative, moderate, or aggressive investors.  
6. **Alternative Options:** Suggest peer stocks or ETFs for comparison or diversification.  
7. **Long-Term Outlook:** Assess the company’s sustainability and strategic plans.  
8. **Immediate Action:** Recommend whether investors should act now or wait for specific triggers.  
9. **Final Verdict:** Restate the **Buy**, **Hold**, or **Sell** recommendation with supporting evidence.  
"""
