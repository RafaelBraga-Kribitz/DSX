# Repeat Purchase and Retention Analysis *AI Prompt *

Analyze repeat purchase behavior and design a retention improvement strategy. Order data: {{order_data}} Customer base: {{customer_count}} total customers Business goal: {{goal}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze repeat purchase behavior and design a retention improvement strategy.

Order data: {{order_data}}
Customer base: {{customer_count}} total customers
Business goal: {{goal}} (increase purchase frequency or reduce time between orders)

1. Repeat purchase metrics:
 - First-time buyer %: customers with only 1 order
 - Repeat buyer %: customers with 2+ orders
 - Loyal buyer %: customers with 5+ orders
 - % of revenue from repeat vs first-time buyers
 - If > 70% of revenue is from first-time buyers: the business depends on constant acquisition (expensive)

2. Time between purchases:
 - Median days between order 1 and order 2
 - Median days between order 2 and order 3
 - Does the inter-purchase interval increase or decrease with order number?
 - Purchase interval by product category (frequency-based categories vs occasion-based)

3. Second purchase conversion:
 - % of first-time buyers who make a second purchase within 30, 60, 90, 180 days
 - Second purchase conversion rate by acquisition channel
 - Second purchase conversion rate by first product category purchased
 - The single most important metric for retention: getting the first repeat purchase

4. Replenishment cycle analysis:
 - For consumable products: average repurchase interval per SKU
 - Products with predictable repurchase cycles (coffee, supplements, skincare)
 - These products are candidates for subscription programs

5. Churn definition and rate:
 - Define active customer: purchased in last {{active_window}} days
 - Churn: not active by this definition
 - Monthly churn rate: (customers at risk of churning who actually churn) / at-risk customers

6. Retention program recommendations:
 - Post-purchase email: trigger {{days}} days before expected next purchase based on category interval
 - Loyalty points: reward repeat purchases to incentivize second order
 - Subscription upsell: offer subscribe-and-save for products with predictable repurchase cycles
 - Win-back: at {{days}} days since last purchase, trigger win-back with incentive

Return: repeat purchase metrics, time-to-repurchase analysis, second purchase conversion, churn rate, and retention program recommendations. 
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

The AI should return a structured result that covers the main requested outputs, such as Repeat purchase metrics:, First-time buyer %: customers with only 1 order, Repeat buyer %: customers with 2+ orders. The final answer should stay clear, actionable, and easy to review inside a customer analytics workflow for ecommerce analyst work. 

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
