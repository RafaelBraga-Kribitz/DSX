# Pricing Analytics *AI Prompts *

3 Ecommerce Analyst prompts in Pricing Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Pricing Analytics 
3 prompts Intermediate Single prompt 01 
### Discount and Promotion Analysis 

Analyze the effectiveness of discounts and promotions and optimize the promotional strategy. Promotion data: {{promotion_data}} (promotion type, discount %, products, period, or... 
Prompt text Analyze the effectiveness of discounts and promotions and optimize the promotional strategy.

Promotion data: {{promotion_data}} (promotion type, discount %, products, period, orders, revenue)
Baseline data: {{baseline_data}} (same period last year or non-promotional baseline)

1. Promotion performance metrics:
 For each promotion:
 - Revenue during promotion vs baseline (lift)
 - Gross margin during promotion vs baseline (margin impact)
 - Orders count and AOV during vs baseline
 - New vs returning customer mix during promotion

2. Revenue vs margin trade-off:
 - Revenue lift (%) from promotion
 - Gross profit change (%) from promotion (may be negative even if revenue is up)
 - Break-even volume: how much incremental volume is needed to offset the margin give-away?
 Break-even lift = Discount % / (Gross Margin % - Discount %)
 Example: 20% discount on a 40% margin product requires 100% volume increase to maintain gross profit

3. Promotion types comparison:
 - % off: drives broadest participation, margins most exposed
 - BOGO (Buy One Get One): volume driver, effective for high-margin products
 - Free shipping threshold: AOV driver (set threshold at 30% above current AOV)
 - Gift with purchase: drives specific product trial, protects revenue
 - Flash sale (time-limited): urgency driver, but trains customers to wait for discounts

4. Customer behavior post-promotion:
 - Are customers acquired during promotions at lower LTV than non-promotion customers?
 - Do promotional buyers return at similar or lower rates than full-price buyers?
 - Are existing customers simply shifting their planned purchases to discount periods?

5. Discount addiction signals:
 - Is there a trend toward increasing discount frequency to maintain revenue?
 - What % of revenue is generated at a discount?
 - Are customers waiting for promotions before purchasing? (Signal: conversion rate declines in weeks before promotions)

6. Optimized promotional calendar:
 - Based on analysis: which promotion types drive the best net margin impact?
 - Recommended promotional cadence: how often and at what depth?
 - Products that should never be promoted (inelastic, premium positioning)

Return: promotion performance table, break-even analysis, type comparison, post-promotion behavior analysis, discount addiction signals, and promotional calendar recommendation. Copy prompt Open prompt details Advanced Single prompt 02 
### Dynamic Pricing Strategy 

Design a data-driven dynamic pricing framework for this e-commerce business. Product catalog: {{catalog}} Demand data: {{demand_data}} Competitor pricing feed: {{competitor_pric... 
Prompt text Design a data-driven dynamic pricing framework for this e-commerce business.

Product catalog: {{catalog}}
Demand data: {{demand_data}}
Competitor pricing feed: {{competitor_prices}} (if available)
Objective: {{objective}} (maximize revenue, maximize margin, protect market share)

1. Dynamic pricing applicability:
 Not all products are suitable for dynamic pricing. Score each category:
 - High suitability: commodity products, seasonal products, high price sensitivity, active competitor pricing changes
 - Low suitability: branded products, luxury, items where price stability builds trust

2. Demand-based pricing rules:
 Adjust price based on current demand signals:
 - High demand (sell-through rate > target): small price increase to protect margin
 - Low demand (sell-through rate < target): small price decrease to drive velocity
 - Near out-of-stock: price increase to ration remaining inventory
 - Overstock: price decrease to accelerate sell-through

3. Competitive pricing rules (if competitor data available):
 - Price matching rule: stay within 5% of the lowest verified competitor price for A-category products
 - Price leadership rule: for unique or differentiated products, ignore competitor pricing
 - Floor price: never go below the minimum margin threshold (cost + minimum margin %)

4. Time-based pricing:
 - Day-of-week elasticity: are there purchase patterns that suggest different price sensitivity by day?
 - Seasonal pricing: pre-season vs peak season vs clearance pricing for each category
 - End-of-season markdown schedule: structured markdown cadence as season ends

5. Guardrails and controls:
 - Maximum price change per day: ± 10% to avoid customer perception issues
 - Price floor per SKU: ensures margin is never destroyed
 - Minimum price stability: some products (premium, gift) should not fluctuate frequently
 - Human review threshold: any suggested price change > 20% requires human approval

6. Testing and measurement:
 - A/B test dynamic pricing vs static: randomize products into test and control
 - Measure: revenue per visit, gross margin %, sell-through rate
 - Be aware: customers on the same product may see different prices (manage perception risk)

Return: product category suitability matrix, demand-based and competitive pricing rules, time-based strategy, guardrails, and testing framework. Copy prompt Open prompt details Intermediate Single prompt 03 
### Price Elasticity and Optimization 

Analyze price sensitivity and identify optimal pricing for key products. Sales and pricing data: {{pricing_data}} (product, price, units_sold, date) Promotion history: {{promoti... 
Prompt text Analyze price sensitivity and identify optimal pricing for key products.

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

Return: elasticity estimates per product, revenue-maximizing price calculations, margin impact analysis, discount effectiveness, and pricing recommendations. Copy prompt Open prompt details 
## Recommended Pricing Analytics workflow 
1 
### Discount and Promotion Analysis 

Start with a focused prompt in Pricing Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Dynamic Pricing Strategy 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Price Elasticity and Optimization 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
