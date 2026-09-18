# Revenue Model Builder *AI Prompt *

Build a bottom-up revenue model for this business. Business type: {{business_type}} Revenue streams: {{revenue_streams}} Historical data available: {{historical_data}} Forecast... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a bottom-up revenue model for this business.

Business type: {{business_type}}
Revenue streams: {{revenue_streams}}
Historical data available: {{historical_data}}
Forecast horizon: {{horizon}} years

1. Revenue disaggregation:
 Break total revenue into its most granular meaningful components:
 - For SaaS: ARR = Customers x Average Revenue Per Account (ARPA)
 - New ARR (new logos), Expansion ARR (upsell), Churn ARR (lost customers)
 - Net Revenue Retention (NRR) = (Beginning ARR + Expansion - Churn) / Beginning ARR
 - For transactional: Revenue = Transactions x Average Order Value
 - For subscription: Revenue = Subscribers x Monthly Fee x (1 - Churn Rate)
 - For services: Revenue = Headcount x Utilization Rate x Billing Rate

2. Forecast each driver separately:
 For each revenue driver:
 - Historical trend (last 3 years CAGR)
 - Management guidance or market growth rate
 - Internal capacity constraints
 - Derive the forecast assumption with a clear rationale

3. Bridge from current year to forecast:
 Revenue(year N+1) = Revenue(year N) + New Business + Expansion - Churn + Price Effect
 Show each component explicitly so the forecast is auditable.

4. Scenario analysis:
 - Base case: management guidance or consensus growth rates
 - Bull case: top quartile of peer growth rates
 - Bear case: mean reversion or macro headwind scenario
 - Show the revenue range at each forecast year

5. Sanity checks:
 - Implied market share: does the forecast require unrealistic market share gains?
 - Revenue per employee: does it stay within a reasonable range for the industry?
 - Cohort math: does the model's churn assumption agree with the cohort retention data?

Return: disaggregated revenue model, driver-by-driver assumptions, three-scenario table, and sanity check results. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin financial modeling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Financial Modeling or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Revenue disaggregation:, For SaaS: ARR = Customers x Average Revenue Per Account (ARPA), New ARR (new logos), Expansion ARR (upsell), Churn ARR (lost customers). The final answer should stay clear, actionable, and easy to review inside a financial modeling workflow for financial analyst work. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Financial Modeling.
