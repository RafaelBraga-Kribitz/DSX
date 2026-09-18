# Revenue Variance Deep Dive *AI Prompt *

Decompose the revenue variance between two periods into price, volume, and mix effects. Period A data: {{period_a_data}} (product/segment, units sold, average price) Period B da... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Decompose the revenue variance between two periods into price, volume, and mix effects.

Period A data: {{period_a_data}} (product/segment, units sold, average price)
Period B data: {{period_b_data}}

1. Total revenue variance:
 Total Variance = Revenue_B - Revenue_A (absolute and % change)

2. Three-way variance decomposition:

 Volume variance:
 = (Total Volume_B - Total Volume_A) x Average Price_A
 What revenue would have changed if only volume changed (price and mix held constant)?

 Price variance:
 = (Average Price_B - Average Price_A) x Total Volume_B
 What revenue changed because we charged more or less per unit?

 Mix variance:
 = (Actual mix revenue at Period A prices) - (Expected mix revenue at Period A prices)
 What revenue changed because the product/segment mix shifted toward higher or lower value items?

 Verify: Volume Variance + Price Variance + Mix Variance = Total Revenue Variance

3. Product/segment level detail:
 For each product or segment:
 - Revenue Period A, Period B
 - Volume change, price change
 - Contribution to total volume/price/mix variance

4. Mix analysis:
 - Which products gained share of revenue mix? Which lost share?
 - Did mix shift toward higher-margin or lower-margin products?
 - Revenue at period A prices if mix were held constant: how much did mix cost or add?

5. Strategic implications:
 - Is revenue growth coming from volume (sustainable, market share driven) or price (possible unsustainable if it drives churn)?
 - Is the mix shift favorable (premiumization) or unfavorable (commoditization)?

Return: three-way decomposition table, product-level detail, mix shift analysis, and strategic implications. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin variance analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Variance Analysis or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Total revenue variance:, Three-way variance decomposition:, Product/segment level detail:. The final answer should stay clear, actionable, and easy to review inside a variance analysis workflow for financial analyst work. 

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

Once you have the first result, continue deeper with related prompts in Variance Analysis.
