# Customer LTV Calculation *AI Prompt *

Calculate Customer Lifetime Value (LTV) using multiple methods and apply it to marketing decisions. Customer data: {{customer_data}} (cohort, revenue history, churn events) Busi... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Calculate Customer Lifetime Value (LTV) using multiple methods and apply it to marketing decisions.

Customer data: {{customer_data}} (cohort, revenue history, churn events)
Business model: {{business_model}}
Discount rate: {{discount_rate}} (cost of capital, typically 10-15%)

1. Simple LTV (for early-stage / approximate use):
 LTV = Average Purchase Value x Purchase Frequency x Customer Lifespan
 - Average Purchase Value: total revenue / total orders
 - Purchase Frequency: total orders / total unique customers per period
 - Customer Lifespan: 1 / Monthly Churn Rate (in months)
 - Gross Profit LTV: multiply by gross margin %

2. Cohort-based LTV (most accurate for historical data):
 - For each acquisition cohort: cumulative revenue per customer through each month of life
 - Plot the cumulative LTV curve: how does LTV grow as cohort ages?
 - LTV at 12 months, 24 months, and steady state
 - Are newer cohorts trending above or below older cohorts? (Improving or declining customer quality)

3. Discounted LTV (for financial decisions):
 Discounted LTV = sum over t: (Expected Cash Flow_t / (1 + r)^t)
 - Where r = monthly discount rate = (1 + annual rate)^(1/12) - 1
 - Cash flow_t = monthly gross profit from the cohort in month t
 - Captures the time value of money: a dollar of LTV received in year 3 is worth less than in year 1

4. LTV by segment:
 - LTV for different acquisition channels, customer segments, product categories, geographies
 - Which segments have 2x or higher LTV than average?
 - This should drive differential CAC targets by segment

5. LTV / CAC framework for marketing decisions:
 - Healthy: LTV / CAC > 3
 - Acceptable: LTV / CAC 1-3 (with path to improvement)
 - Unsustainable: LTV / CAC < 1
 - Maximum CAC by segment = LTV x maximum acceptable CAC ratio

6. LTV improvement levers:
 - Increase average order value (cross-sell, upsell)
 - Increase purchase frequency (engagement, reminder programs)
 - Reduce churn (retention programs)
 - For each lever: estimated impact on LTV

Return: LTV calculation by method, cohort LTV curves, segment LTV comparison, LTV/CAC framework, and LTV improvement lever analysis. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin crm and email analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in CRM and Email Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Simple LTV (for early-stage / approximate use):, Average Purchase Value: total revenue / total orders, Purchase Frequency: total orders / total unique customers per period. The final answer should stay clear, actionable, and easy to review inside a crm and email analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in CRM and Email Analytics.
