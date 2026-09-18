# Product Catalog Performance Analysis *AI Prompt *

Analyze the performance of the product catalog to identify best sellers, underperformers, and merchandising opportunities. Product data: {{product_data}} (product_id, category,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the performance of the product catalog to identify best sellers, underperformers, and merchandising opportunities.

Product data: {{product_data}} (product_id, category, views, add-to-cart, orders, revenue, margin, inventory)
Time period: {{period}}

1. Revenue and margin contribution:
 - Pareto analysis: what % of products generate 80% of revenue? (Typically 20%)
 - Top 20 products by revenue contribution and their % of total
 - Top 20 products by gross margin contribution
 - Products where high revenue rank and high margin rank diverge: investigate

2. Product performance matrix (2x2):
 X-axis: Conversion rate (add-to-cart to purchase)
 Y-axis: Traffic (product page views)

 - High traffic, high conversion (Stars): protect and feature prominently
 - High traffic, low conversion (Opportunities): fix the page or review the product offering
 - Low traffic, high conversion (Hidden Gems): increase visibility, promote more
 - Low traffic, low conversion (Dogs): review for discontinuation or significant improvement

3. Category-level analysis:
 - Revenue, orders, and AOV by category
 - Category conversion rate (add-to-cart from category page)
 - Category growth: which categories are growing YoY? Which are declining?
 - Cross-category purchase patterns: which categories are most frequently bought together?

4. Inventory vs demand alignment:
 - Out-of-stock rate per product: % of time in stock-out during the period
 - Stock-out revenue impact: estimated lost sales from stock-outs on high-demand products
 - Overstock: products with > 90 days of inventory coverage at current sell rate

5. New vs established product performance:
 - Products launched in the last 90 days: are they ramping or stalling?
 - Products > 180 days old with declining traffic: content refresh or markdown needed?

6. Pricing analysis:
 - Products with lowest conversion rate in their category: is price a factor?
 - Price elasticity signals: any products where a discount drove disproportionate volume increase?

Return: Pareto analysis, product performance matrix, category analysis, inventory alignment, and pricing insights. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin merchandising analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Merchandising Analytics or the wider Ecommerce Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Revenue and margin contribution:, Pareto analysis: what % of products generate 80% of revenue? (Typically 20%), Top 20 products by revenue contribution and their % of total. The final answer should stay clear, actionable, and easy to review inside a merchandising analytics workflow for ecommerce analyst work. 

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

Once you have the first result, continue deeper with related prompts in Merchandising Analytics.
