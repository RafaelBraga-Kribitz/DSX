# Price Elasticity and Optimization *AI Prompt *

Analyze price sensitivity and identify optimal pricing for key products. Sales and pricing data: {{pricing_data}} (product, price, units_sold, date) Promotion history: {{promoti... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze price sensitivity and identify optimal pricing for key products.

Sales and pricing data: {{pricing_data}} (product, price, units_sold, date)
Promotion history: {{promotion_data}}
Competitor pricing: {{competitor_prices}} (if available)

1. Price elasticity estimation:
 Price Elasticity of Demand (PED) = % change in quantity / % change in price
 - PED < -1: elastic demand (price decrease drives proportionally more volume)
 - PED > -1: inelastic demand (price changes have limited volume effect)
 - PED = -1: unit elastic

 Estimation approach:
 - Collect price change events (price increases, promotions, sales) for each product
 - Compare volume before and after each price change
 - Control for seasonality by using same period YoY or a holdout comparison

2. Revenue-maximizing price:
 At the estimated elasticity, the revenue-maximizing price is:
 Optimal Price = Marginal Cost / (1 + 1/PED)
 - Calculate for products with reliable elasticity estimates
 - Compare optimal price to current price: are products over or under-priced?

3. Margin-impact analysis:
 - If we raise price by 5%: at what elasticity does revenue decrease?
 - If revenue decreases but volume decreases proportionally less: gross profit may still increase
 - Calculate: (Price lift) x (Volume loss) = Net margin impact at different elasticity assumptions

4. Promotional discount analysis:
 - Which products historically show the highest volume lift from promotions?
 - What discount depth is needed to move volume without destroying margin?
 - Products where discount lift is < 20% volume increase: promotions destroy margin without compensating volume

5. Competitive pricing analysis:
 - Price index: our price / lowest competitor price per product
 - Products where we are more than 15% above the lowest competitor price and showing low conversion
 - Products where we are below average market price: potential for modest price increase

6. Pricing recommendations:
 - Products to test a price increase on (inelastic, below optimal price)
 - Products to review pricing strategy (elastic, above optimal price)
 - Promotional calendar recommendations based on elasticity

Return: elasticity estimates per product, revenue-maximizing price calculations, margin impact analysis, discount effectiveness, and pricing recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin pricing analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Pricing Analytics or the wider Ecommerce Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Price elasticity estimation:, PED < -1: elastic demand (price decrease drives proportionally more volume), PED > -1: inelastic demand (price changes have limited volume effect). The final answer should stay clear, actionable, and easy to review inside a pricing analytics workflow for ecommerce analyst work. 

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

Once you have the first result, continue deeper with related prompts in Pricing Analytics.
