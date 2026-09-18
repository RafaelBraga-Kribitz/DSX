# Alpha Signal Evaluation *AI Prompt *

Rigorously evaluate the statistical and economic validity of this proposed alpha signal. Signal description: {{signal_description}} Signal data: {{signal_data}} Universe: {{univ... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Rigorously evaluate the statistical and economic validity of this proposed alpha signal.

Signal description: {{signal_description}}
Signal data: {{signal_data}}
Universe: {{universe}}
Look-ahead period: {{horizon}}

1. Information coefficient (IC) analysis:
 IC = Spearman rank correlation(signal_t, return_{t+h})
 - Compute IC for each cross-section (each time period)
 - Mean IC: expected predictive power per period. IC > 0.05 is economically meaningful for daily signals.
 - IC standard deviation (ICSD): consistency of the signal
 - Information ratio of the signal: IC_mean / IC_std
 IR > 0.5: strong signal. IR > 1.0: exceptional.
 - % of periods with positive IC: > 55% indicates consistent directionality

2. IC decay analysis:
 - Compute IC at horizons h = 1, 5, 10, 21, 63, 126 trading days
 - Plot IC vs horizon: how quickly does predictive power decay?
 - The horizon where IC crosses zero defines the signal's natural holding period
 - Fast decay → short-term signal (high turnover). Slow decay → longer-term signal.

3. Quintile / decile portfolio analysis:
 - Each period: sort universe by signal into 5 (or 10) portfolios
 - Equal-weight each portfolio and compute forward returns
 - Report for each quintile: mean return, std, Sharpe, % periods positive
 - Key test: monotonic relationship from Q1 (low signal) to Q5 (high signal)?
 - Spread return: Q5 − Q1 long-short portfolio
 - Spread Sharpe ratio, drawdown, and turnover

4. Statistical significance testing:
 - t-test on mean IC: H₀: IC_mean = 0. Reject if |t| > 2.0.
 - Account for autocorrelation in IC series: Newey-West standard errors
 - Multiple testing concern: if this signal is one of many tested, apply Bonferroni or BHY correction
 - Bootstrap test: reshuffle signal vs returns 10,000 times and check if observed IC exceeds 95th percentile of null

5. Signal decay and overfitting checks:
 - In-sample vs out-of-sample IC: if in-sample IC >> out-of-sample IC, likely overfitting
 - Publication decay: has this signal's IC declined over time? (Sign of arbitrage)
 - Stability: does IC remain consistent across different market regimes?

6. Practical implementation costs:
 - Turnover rate of the long-short portfolio
 - Effective spread cost at current turnover: does signal survive round-trip transaction costs?
 - Break-even cost: max cost at which signal still generates positive net IC

Return: IC statistics table, IC decay plot, quintile return analysis, significance tests, overfitting checks, and net-of-cost IC estimate. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin financial data analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Financial Data Analysis or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Information coefficient (IC) analysis:, Compute IC for each cross-section (each time period), Mean IC: expected predictive power per period. IC > 0.05 is economically meaningful for daily signals.. The final answer should stay clear, actionable, and easy to review inside a financial data analysis workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Financial Data Analysis.
