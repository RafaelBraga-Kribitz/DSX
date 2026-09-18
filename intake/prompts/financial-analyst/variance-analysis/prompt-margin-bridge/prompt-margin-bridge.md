# Margin Bridge Analysis *AI Prompt *

Build a margin bridge explaining the change in gross margin or EBITDA margin between two periods. Period A: {{period_a}} margin: {{margin_a}} Period B: {{period_b}} margin: {{ma... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a margin bridge explaining the change in gross margin or EBITDA margin between two periods.

Period A: {{period_a}} margin: {{margin_a}}
Period B: {{period_b}} margin: {{margin_b}}
P&L data for both periods: {{pnl_data}}

1. Margin bridge components:
 Total margin change = Volume effect + Price/Rate effect + Mix effect + Cost efficiency effect + One-time items

 Volume effect:
 - If revenue grew, fixed costs spread over a larger base, improving margin
 - Volume effect = (Revenue_B - Revenue_A) / Revenue_B x Fixed Cost Ratio_A

 Price/Rate effect:
 - Change in average selling price x revenue volume
 - Change in input cost rates x cost volume

 Mix effect:
 - Did the revenue mix shift toward higher or lower margin products/customers/channels?
 - Mix effect = (Current mix margin - Prior mix margin) x Revenue_B

 Cost efficiency:
 - Productivity improvements, procurement savings, or headcount efficiency
 - Efficiency effect = (Cost_A % of revenue - Cost_B % of revenue) x Revenue_B

 One-time items:
 - Identify and isolate non-recurring items in both periods
 - Adjusted margins excluding one-time items

2. Waterfall chart specification:
 - Start bar: Period A margin %
 - Each bridge item: positive = green bar up, negative = red bar down
 - End bar: Period B margin %
 - All bars sum to the total margin change

3. Commentary for each bridge item:
 - Why did this component move? (Specific cause)
 - Is it structural (durable) or temporary?
 - Expected trajectory going forward

Return: margin bridge table, waterfall chart description, component commentary, and adjusted margins excluding one-time items. 
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

The AI should return a structured result that covers the main requested outputs, such as Margin bridge components:, If revenue grew, fixed costs spread over a larger base, improving margin, Volume effect = (Revenue_B - Revenue_A) / Revenue_B x Fixed Cost Ratio_A. The final answer should stay clear, actionable, and easy to review inside a variance analysis workflow for financial analyst work. 

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
