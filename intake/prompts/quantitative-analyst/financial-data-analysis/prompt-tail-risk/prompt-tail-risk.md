# Tail Risk Analysis *AI Prompt *

Conduct a comprehensive tail risk analysis for this return series. Portfolio or asset: {{portfolio}} Return series: {{returns}} 1. Empirical tail analysis: - Left tail: distribu... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a comprehensive tail risk analysis for this return series.

Portfolio or asset: {{portfolio}}
Return series: {{returns}}

1. Empirical tail analysis:
 - Left tail: distribution of returns below the 5th and 1st percentile
 - Right tail: distribution of returns above the 95th and 99th percentile
 - Tail asymmetry: is the left tail heavier than the right? (Typical for equity strategies)
 - Comparison to normal: at the 1% quantile, how does the empirical loss compare to the normal distribution prediction?

2. Extreme Value Theory (EVT) for tail estimation:
 Peaks Over Threshold (POT) method:
 - Choose threshold u at the 95th percentile of losses
 - Fit Generalized Pareto Distribution (GPD) to exceedances: F(x) = 1 - (1 + ξx/σ)^(-1/ξ)
 - Report: shape parameter ξ (> 0 = heavy tail, = 0 = exponential, < 0 = bounded tail), scale σ
 - ξ > 0.5 indicates very heavy tails — normal-based risk measures severely underestimate risk
 - Use GPD to estimate VaR and CVaR at extreme quantiles (99.9%) beyond the data

3. Maximum Drawdown analysis:
 - Maximum drawdown (MDD): largest peak-to-trough decline
 - Average drawdown
 - Drawdown duration distribution: how long do drawdowns last?
 - Recovery time distribution: how long does it take to recover to prior peak?
 - Calmar ratio: annualized return / |MDD|
 - Pain index: integral of drawdown curve over time

4. Tail correlation (co-tail risk):
 - For a multi-asset portfolio: does the portfolio tail loss exceed what uncorrelated risks would imply?
 - Tail dependence coefficient: probability that both assets suffer extreme losses simultaneously
 - Clayton copula for lower tail dependence: captures asymmetric dependence in down markets

5. Stress test scenarios:
 Apply historical stress scenarios:
 - 2008 financial crisis (Sept–Nov 2008)
 - COVID crash (Feb–Mar 2020)
 - 2020 interest rate spike (Q1 2022)
 - Dot-com crash (2000–2002)
 For each: what was the portfolio loss? How does it compare to VaR predictions?

6. Reporting:
 - At what loss level does your risk model break down? (Where does the normal approximation stop being conservative?)
 - What tail risk is not captured by standard VaR?

Return: empirical tail analysis, GPD parameter estimates, drawdown metrics, tail correlation analysis, stress test results, and risk model limitation statement. 
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

The AI should return a structured result that covers the main requested outputs, such as Empirical tail analysis:, Left tail: distribution of returns below the 5th and 1st percentile, Right tail: distribution of returns above the 95th and 99th percentile. The final answer should stay clear, actionable, and easy to review inside a financial data analysis workflow for quantitative analyst work. 

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
