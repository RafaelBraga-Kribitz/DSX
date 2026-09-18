# Portfolio Optimization *AI Prompt *

Construct an optimal portfolio from this asset universe using mean-variance optimization and robust alternatives. Assets: {{asset_universe}} Return estimates: {{return_estimates... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Construct an optimal portfolio from this asset universe using mean-variance optimization and robust alternatives.

Assets: {{asset_universe}}
Return estimates: {{return_estimates}}
Covariance matrix: {{covariance_matrix}}
Constraints: {{constraints}}

1. Classical mean-variance optimization (Markowitz):
 Solve: min w'Σw subject to w'μ = target_return, w'1 = 1, w ≥ 0
 - Efficient frontier: trace the set of portfolios minimizing variance for each target return
 - Identify: minimum variance portfolio (MVP), maximum Sharpe ratio portfolio (tangency)
 - Report for each portfolio: weights, expected return, volatility, Sharpe ratio

2. The problem with classical MVO:
 - Estimation error: small changes in expected returns produce large weight changes
 - Input sensitivity: MVO is an 'error maximizer' — it concentrates in assets with the most overestimated returns
 - Demonstrate: perturb expected returns by ±1% and show how weights change

3. Robust optimization alternatives:

 Maximum Sharpe Ratio with shrinkage:
 - Shrink expected returns toward a common prior (e.g. equal returns for all assets or CAPM-implied returns)
 - Ledoit-Wolf shrinkage on the covariance matrix

 Minimum Variance Portfolio:
 - Avoids using expected return estimates entirely (which are the most error-prone input)
 - min w'Σw subject to w'1 = 1, w ≥ 0
 - Historically outperforms on a risk-adjusted basis in many markets

 Risk Parity:
 - Each asset contributes equally to total portfolio variance
 - RC_i = w_i × (Σw)_i = Portfolio_variance / N
 - Implicit long duration bias (bonds are low vol); often levered to achieve return targets

 Maximum Diversification:
 - Maximize the ratio: w'σ / sqrt(w'Σw) where σ is the vector of individual asset volatilities
 - Maximizes diversification benefit relative to a weighted average of individual volatilities

4. Practical constraints:
 - Long-only: w ≥ 0
 - Weight bounds: w_i ∈ [0, 0.20] (max 20% in any single asset)
 - Turnover constraints: |w_new - w_old| ≤ budget
 - Sector constraints: sum of sector weights within bounds

5. Out-of-sample evaluation:
 - Walk-forward portfolio construction: reoptimize annually, evaluate on the following year
 - Compare all methods: realized Sharpe, realized volatility, maximum drawdown, turnover

Return: efficient frontier plot, portfolio weights for each method, sensitivity analysis, walk-forward performance comparison. 
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

The AI should return a structured result that covers the main requested outputs, such as Classical mean-variance optimization (Markowitz):, Efficient frontier: trace the set of portfolios minimizing variance for each target return, Identify: minimum variance portfolio (MVP), maximum Sharpe ratio portfolio (tangency). The final answer should stay clear, actionable, and easy to review inside a risk and portfolio analytics workflow for quantitative analyst work. 

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
