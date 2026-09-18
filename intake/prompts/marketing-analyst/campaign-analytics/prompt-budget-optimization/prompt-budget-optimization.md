# Paid Media Budget Optimization *AI Prompt *

Optimize paid media budget allocation across channels to maximize return at a given spend level. Current budget: {{total_budget}} Current channel allocations: {{current_allocati... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Optimize paid media budget allocation across channels to maximize return at a given spend level.

Current budget: {{total_budget}}
Current channel allocations: {{current_allocation}}
Performance data by channel: {{performance_data}} (spend, conversions, revenue)

1. Current state analysis:
 For each channel:
 - Current spend and % of total budget
 - Conversions and revenue attributed
 - CPA and ROAS
 - Marginal ROAS: performance of the last incremental dollar spent (from spend vs performance curve)

2. Response curve estimation:
 For each channel, estimate the diminishing returns curve:
 - Collect historical data points: (spend level, performance outcome) per week
 - Fit a saturation curve: Revenue = a x (1 - e^(-b x Spend))
 - Where is the inflection point? Where does marginal ROAS drop below 1?

3. Optimal allocation theory:
 - Budget is optimally allocated when marginal ROAS is equal across all channels
 - If Channel A marginal ROAS (1.8) > Channel B marginal ROAS (0.9): shift budget from B to A
 - Continue reallocation until marginal ROAS equalizes

4. Proposed reallocation:
 - For each channel: recommended new budget
 - Expected change in conversions and revenue vs current allocation
 - Total portfolio ROAS improvement from optimization

5. Constraints to consider:
 - Minimum effective budget per channel (below a threshold, channels stop working)
 - Channel caps from inventory limitations or audience saturation
 - Strategic channels that require funding beyond what pure ROI math suggests
 - Brand safety requirements

6. Testing plan:
 - Do not implement all reallocation at once: risk of performance disruption
 - Phased approach: 20% reallocation per month with measurement between each step

Return: marginal ROAS by channel, response curve parameters, optimal allocation table, revenue uplift estimate, and phased implementation plan. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin campaign analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Campaign Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Current state analysis:, Current spend and % of total budget, Conversions and revenue attributed. The final answer should stay clear, actionable, and easy to review inside a campaign analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Campaign Analytics.
