# VaR and CVaR Calculation *AI Prompt *

Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR) for this portfolio using multiple methods. Portfolio returns: {{returns}} Confidence levels: 95% and 99% Holdi... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR) for this portfolio using multiple methods.

Portfolio returns: {{returns}}
Confidence levels: 95% and 99%
Holding period: 1-day and 10-day

1. Definitions:
 - VaR(α): the loss that will not be exceeded with probability α. If 1-day 99% VaR = $1M, there is a 1% chance of losing more than $1M in a single day.
 - CVaR(α) (also called Expected Shortfall, ES): the expected loss given that the loss exceeds VaR. Always ≥ VaR. More coherent risk measure — CVaR is sub-additive, VaR is not.

2. Method 1 — Historical simulation:
 - Sort the return series from worst to best
 - 95% VaR: the 5th percentile of the distribution (5% of worst returns)
 - 99% VaR: the 1st percentile
 - CVaR: mean of returns below the VaR threshold
 - Pros: non-parametric, captures empirical fat tails and asymmetry
 - Cons: limited by historical window length; past scenarios may not reflect future risks

3. Method 2 — Parametric (variance-covariance) approach:
 - Assume returns are normally distributed: VaR = μ - z_α × σ
 - z_{0.95} = 1.645, z_{0.99} = 2.326
 - CVaR = μ - σ × φ(z_α) / (1 - α), where φ is the standard normal PDF
 - Pros: fast, analytical, easy to decompose by position
 - Cons: assumes normality — severely underestimates tail risk for fat-tailed assets

4. Method 3 — Monte Carlo simulation:
 - Fit a distribution to the returns (normal, t, or skew-t)
 - Simulate 100,000 scenarios from the fitted distribution
 - Compute VaR and CVaR from the simulated distribution
 - Pros: flexible distribution; can model complex portfolios
 - Cons: results depend heavily on the assumed distribution and model parameters

5. Scaling to multi-day horizons:
 - Square-root-of-time rule: 10-day VaR ≈ 1-day VaR × sqrt(10)
 - Caveat: this assumes i.i.d. returns. Volatility clustering violates this assumption.
 - Better: simulate 10-day paths and compute VaR directly from path-end P&L

6. Method comparison and recommendation:
 - Report VaR and CVaR from all three methods
 - Where do they differ most? Why?
 - Which method is most appropriate for this portfolio and why?
 - Backtesting VaR: count how many historical days exceeded the VaR. Should be ≈ 5% for 95% VaR.

Return: VaR and CVaR table (method × confidence level), method comparison, scaling analysis, and backtesting results. 
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

The AI should return a structured result that covers the main requested outputs, such as Definitions:, VaR(α): the loss that will not be exceeded with probability α. If 1-day 99% VaR = $1M, there is a 1% chance of losing more than $1M in a single day., CVaR(α) (also called Expected Shortfall, ES): the expected loss given that the loss exceeds VaR. Always ≥ VaR. More coherent risk measure — CVaR is sub-additive, VaR is not.. The final answer should stay clear, actionable, and easy to review inside a risk and portfolio analytics workflow for quantitative analyst work. 

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
