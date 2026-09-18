# Discount and Promotion Analysis *AI Prompt *

Analyze the effectiveness of discounts and promotions and optimize the promotional strategy. Promotion data: {{promotion_data}} (promotion type, discount %, products, period, or... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the effectiveness of discounts and promotions and optimize the promotional strategy.

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

Return: promotion performance table, break-even analysis, type comparison, post-promotion behavior analysis, discount addiction signals, and promotional calendar recommendation. 
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

The AI should return a structured result that covers the main requested outputs, such as Promotion performance metrics:, Revenue during promotion vs baseline (lift), Gross margin during promotion vs baseline (margin impact). The final answer should stay clear, actionable, and easy to review inside a pricing analytics workflow for ecommerce analyst work. 

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
