# Customer Lifetime Value Analysis *AI Prompt *

Calculate and segment Customer Lifetime Value (LTV) for this e-commerce business. Order data: {{order_data}} (customer_id, order_date, order_value, product_category) Time period... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Calculate and segment Customer Lifetime Value (LTV) for this e-commerce business.

Order data: {{order_data}} (customer_id, order_date, order_value, product_category)
Time period: {{period}}
Business model: {{business_model}} (single purchase, subscription, repeat purchase)

1. Basic LTV metrics:
 - Average Order Value (AOV): total revenue / total orders
 - Purchase frequency: orders per customer per year
 - Customer lifespan: average months from first to last purchase (or 1 / annual churn rate)
 - Simple LTV = AOV x Purchase Frequency x Customer Lifespan
 - Gross profit LTV: multiply by gross margin %

2. Cohort-based LTV:
 - Group customers by acquisition month
 - For each cohort: cumulative revenue per customer through months 1, 3, 6, 12, 24
 - LTV curve: how does cumulative revenue grow over time?
 - At what month does the cohort LTV begin to plateau?

3. LTV by acquisition channel:
 - Which channel brings customers with the highest 12-month LTV?
 - Which brings the most orders per customer? Which brings the highest AOV?
 - Compare to CAC by channel: LTV/CAC ratio per channel

4. LTV by first product category:
 - Do customers who first purchase from category A have higher LTV than category B?
 - Category with highest LTV first purchase: prioritize in acquisition marketing

5. LTV by customer segment:
 - One-time buyers (only 1 order): how many and what % of customers? What is their share of revenue?
 - Repeat buyers (2-4 orders): their LTV vs one-time buyers
 - Loyal customers (5+ orders): their LTV, AOV, and frequency vs average

6. Second purchase conversion:
 - What % of first-time buyers make a second purchase within 90 days?
 - Time to second purchase distribution
 - The second purchase is the most predictive event for long-term retention
 - What drives second purchase? (Category, time since first, email trigger)

Return: LTV metrics table, cohort curves, channel LTV comparison, category LTV analysis, segment breakdown, and second-purchase insights. 
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

The AI should return a structured result that covers the main requested outputs, such as Basic LTV metrics:, Average Order Value (AOV): total revenue / total orders, Purchase frequency: orders per customer per year. The final answer should stay clear, actionable, and easy to review inside a customer analytics workflow for ecommerce analyst work. 

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
