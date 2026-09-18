# Performance Attribution *AI Prompt *

Decompose portfolio performance into its sources using Brinson-Hood-Beebower (BHB) attribution. Portfolio: {{portfolio_weights_and_returns}} Benchmark: {{benchmark_weights_and_r... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Decompose portfolio performance into its sources using Brinson-Hood-Beebower (BHB) attribution.

Portfolio: {{portfolio_weights_and_returns}}
Benchmark: {{benchmark_weights_and_returns}}
Period: {{period}}

1. BHB attribution framework:
 Total active return = Allocation effect + Selection effect + Interaction effect

 For each segment i:
 - Allocation effect: (w_p,i - w_b,i) × (R_b,i - R_b)
 Did we overweight/underweight the right segments?
 - Selection effect: w_b,i × (R_p,i - R_b,i)
 Did we pick better securities within each segment?
 - Interaction effect: (w_p,i - w_b,i) × (R_p,i - R_b,i)
 Did we concentrate in segments where we had good selection?

 Where:
 - w_p,i = portfolio weight in segment i
 - w_b,i = benchmark weight in segment i
 - R_p,i = portfolio return in segment i
 - R_b,i = benchmark return in segment i
 - R_b = total benchmark return

2. Segment definitions:
 Apply attribution at multiple levels:
 - Level 1: by asset class (equity, fixed income, alternatives)
 - Level 2: by sector (within equity: technology, healthcare, financials, etc.)
 - Level 3: by country or region (within global equity)

3. Attribution over time:
 - Monthly attribution: cumulative linking is required (simple addition creates geometric compounding error)
 - Geometric linking method: chain-link the single-period attributions
 - Plot cumulative allocation, selection, and interaction effects over the period

4. Factor attribution (alternative to BHB):
 Regress active returns on factor returns (Barra or Fama-French):
 - Factor contribution: β_factor × factor_return
 - Specific (residual) contribution: unexplained by factors
 - This tells you whether outperformance came from intentional factor tilts or from security selection

5. Risk-adjusted attribution:
 - Information ratio: active_return / tracking_error
 - t-statistic: is active return statistically significant? Require ≥ 3 years to assess significance.
 - Active risk decomposition: which bets contributed most to tracking error?

6. Pitfalls:
 - Currency effects: separate currency contribution from local return contribution for international portfolios
 - Geometric vs arithmetic: be explicit about which convention is used

Return: BHB attribution table by segment, cumulative attribution plots, factor attribution, and information ratio analysis. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin risk and portfolio analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Risk and Portfolio Analytics or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as BHB attribution framework:, Allocation effect: (w_p,i - w_b,i) × (R_b,i - R_b), Selection effect: w_b,i × (R_p,i - R_b,i). The final answer should stay clear, actionable, and easy to review inside a risk and portfolio analytics workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Risk and Portfolio Analytics.
