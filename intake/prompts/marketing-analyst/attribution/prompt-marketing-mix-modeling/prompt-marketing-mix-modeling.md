# Marketing Mix Modeling *AI Prompt *

Design and interpret a marketing mix model (MMM) for this business. Business: {{business}} Sales / conversion data: {{sales_data}} (weekly, 2+ years) Marketing spend data: {{spe... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and interpret a marketing mix model (MMM) for this business.

Business: {{business}}
Sales / conversion data: {{sales_data}} (weekly, 2+ years)
Marketing spend data: {{spend_data}} (by channel, same period)
External factors: {{external_factors}} (macroeconomic data, seasonality, competitor actions)

1. What MMM is and when to use it:
 - MMM uses regression to decompose total sales into: baseline (organic) + each marketing channel's contribution + external factors
 - Unlike attribution (which tracks individual user paths), MMM works at aggregate level
 - Best for: understanding the incremental contribution of each channel, including offline (TV, OOH)
 - Limitation: requires 2+ years of data, is backward-looking, and cannot measure within-campaign personalization

2. Data preparation:
 - Adstock transformation: marketing spend has a delayed and decaying effect
 Adstock_t = Spend_t + decay_rate x Adstock_{t-1}
 - Decay rates by channel: TV (~0.7), Digital display (~0.3), Paid search (~0.1)
 - Saturation curve: diminishing returns on increasing spend (log or S-curve transformation)
 - Control variables: seasonality (Fourier terms or dummy variables), price, distribution, promotions

3. Model specification:
 Sales_t = Baseline + sum(beta_i x Adstock_i_t) + beta_price x Price_t + Seasonal + Error
 - Estimate using Bayesian regression (allows priors on channel effectiveness)
 - Model diagnostics: R-squared, MAPE on holdout period, residual checks

4. Output interpretation:
 - Baseline %: share of sales occurring without any marketing
 - Contribution % per channel: what share of incremental sales each channel drove
 - mROAS (marginal ROAS): the return on the last dollar spent in each channel
 - Saturation point: at what spend level does each channel show diminishing returns?

5. Budget optimization:
 - Using the fitted saturation curves: what budget allocation maximizes total sales at the current total budget?
 - What is the revenue uplift from the optimal allocation vs current allocation?

Return: MMM methodology explanation, data preparation steps, model output interpretation, contribution table, mROAS by channel, and optimized budget allocation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin attribution work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Attribution or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as What MMM is and when to use it:, MMM uses regression to decompose total sales into: baseline (organic) + each marketing channel's contribution + external factors, Unlike attribution (which tracks individual user paths), MMM works at aggregate level. The final answer should stay clear, actionable, and easy to review inside a attribution workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Attribution.
