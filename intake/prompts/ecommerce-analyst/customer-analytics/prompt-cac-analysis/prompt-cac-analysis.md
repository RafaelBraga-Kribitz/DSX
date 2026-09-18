# Customer Acquisition Cost Analysis *AI Prompt *

Analyze customer acquisition costs and LTV/CAC ratios across channels for this e-commerce business. Marketing spend data: {{spend_data}} (by channel, period) New customer data:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze customer acquisition costs and LTV/CAC ratios across channels for this e-commerce business.

Marketing spend data: {{spend_data}} (by channel, period)
New customer data: {{new_customer_data}} (acquisition date, first order value, acquisition channel)
LTV data: {{ltv_data}}

1. CAC calculation:
 CAC = Total Acquisition Spend / New Customers Acquired
 - Blended CAC: all channels combined
 - Channel CAC: paid search, paid social, email, influencer, affiliate, organic (fully-loaded)
 - Organic CAC: allocate content, SEO, and brand spend to organic-acquired customers
 - New customer only: exclude existing customer marketing spend from the CAC numerator

2. CAC payback period:
 Payback = CAC / (Monthly Gross Profit per New Customer)
 - Target for e-commerce: < 12 months
 - At current gross margin and purchase frequency: how many months to recover the acquisition cost?

3. LTV / CAC ratio by channel:
 - 12-month LTV and 24-month LTV per acquisition channel
 - LTV / CAC ratio per channel
 - Healthy benchmark: > 3x
 - Channels with LTV/CAC < 1: losing money on every customer acquired

4. Cohort-based payback curves:
 - For customers acquired in the last 6 cohorts: cumulative gross profit over time
 - At what month does each cohort recover its CAC?
 - Are newer cohorts recovering faster or slower? (Faster = improving efficiency)

5. Customer quality by channel:
 - Second purchase rate by acquisition channel (% making a second purchase within 90 days)
 - Average order frequency in year 1 by channel
 - Churn rate (no purchase in > 180 days) by channel
 - Channels bringing high-volume but low-quality customers: reconsider spending

6. Budget allocation implications:
 - Which channels should receive more budget based on LTV/CAC?
 - Which channels are over-funded relative to their LTV/CAC?
 - Maximum viable CAC per channel = Target LTV/CAC ratio x 12-month LTV

Return: CAC by channel, payback analysis, LTV/CAC ratios, cohort payback curves, customer quality metrics, and budget allocation recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin customer analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Customer Analytics or the wider Ecommerce Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as CAC calculation:, Blended CAC: all channels combined, Channel CAC: paid search, paid social, email, influencer, affiliate, organic (fully-loaded). The final answer should stay clear, actionable, and easy to review inside a customer analytics workflow for ecommerce analyst work. 

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

Once you have the first result, continue deeper with related prompts in Customer Analytics.
