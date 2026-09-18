# Dynamic Pricing Strategy *AI Prompt *

Design a data-driven dynamic pricing framework for this e-commerce business. Product catalog: {{catalog}} Demand data: {{demand_data}} Competitor pricing feed: {{competitor_pric... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a data-driven dynamic pricing framework for this e-commerce business.

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

Return: product category suitability matrix, demand-based and competitive pricing rules, time-based strategy, guardrails, and testing framework. 
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

The AI should return a structured result that covers the main requested outputs, such as Dynamic pricing applicability:, High suitability: commodity products, seasonal products, high price sensitivity, active competitor pricing changes, Low suitability: branded products, luxury, items where price stability builds trust. The final answer should stay clear, actionable, and easy to review inside a pricing analytics workflow for ecommerce analyst work. 

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
