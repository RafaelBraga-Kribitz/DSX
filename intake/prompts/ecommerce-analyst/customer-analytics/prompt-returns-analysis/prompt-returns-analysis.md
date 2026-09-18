# Returns and Refunds Analysis *AI Prompt *

Analyze product returns and refunds to identify root causes and financial impact. Returns data: {{returns_data}} (order_id, product_id, return_reason, return_date, refund_amount... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze product returns and refunds to identify root causes and financial impact.

Returns data: {{returns_data}} (order_id, product_id, return_reason, return_date, refund_amount)
Order data: {{order_data}}

1. Returns overview:
 - Return rate: returns / orders (by units and by order value)
 - Industry average by category: apparel 20-30%, electronics 5-10%, home goods 5-8%
 - How does this store compare?
 - Cost of returns: shipping + processing + inventory write-down as % of revenue

2. Return rate by product and category:
 - Products with highest return rates
 - Are certain categories structurally high-return? (Size/fit issues in apparel)
 - Products with increasing return rates: product quality issue or misleading listing?

3. Return reason analysis:
 - Classify return reasons: wrong size, defective/damaged, not as described, changed mind, arrived late
 - Volume and % for each reason
 - Controllable vs uncontrollable returns:
 - Controllable: not as described, wrong item sent, defective → operational fix
 - Uncontrollable: changed mind, wrong size ordered → policy and content optimization

4. Financial impact:
 - Gross return rate: returns / gross revenue
 - Net revenue = gross revenue - refunds
 - Contribution margin impact: for each return, the contribution margin of that order is lost, plus return cost
 - Annual cost of returns in dollars

5. Return prevention opportunities:
 - 'Not as described' returns → improve product descriptions, add more images, size guides
 - 'Wrong size' returns → add size recommendation feature or chat assistant
 - 'Defective' returns → supplier quality review
 - Products with > 25% return rate: review listing accuracy and product quality

6. Return policy analysis:
 - Does the current return policy drive returns? (e.g. free returns may incentivize 'bracket buying')
 - What would be the financial impact of moving from 30-day to 14-day return window?

Return: returns overview, product/category return rates, reason analysis, financial impact, prevention opportunities, and policy analysis. 
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

The AI should return a structured result that covers the main requested outputs, such as Returns overview:, Return rate: returns / orders (by units and by order value), Industry average by category: apparel 20-30%, electronics 5-10%, home goods 5-8%. The final answer should stay clear, actionable, and easy to review inside a customer analytics workflow for ecommerce analyst work. 

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
