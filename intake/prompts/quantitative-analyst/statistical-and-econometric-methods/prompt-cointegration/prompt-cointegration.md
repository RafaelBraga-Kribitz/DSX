# Cointegration and Pairs Trading *AI Prompt *

Test for cointegration between two assets and build a pairs trading model. Asset 1: {{asset_1}} Asset 2: {{asset_2}} Price series: {{price_series}} 1. Cointegration testing: Eng... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Test for cointegration between two assets and build a pairs trading model.

Asset 1: {{asset_1}}
Asset 2: {{asset_2}}
Price series: {{price_series}}

1. Cointegration testing:

 Engle-Granger two-step approach:
 Step 1: Run OLS: P1_t = α + β × P2_t + ε_t
 Step 2: Test residuals ε_t for stationarity using ADF
 - If residuals are stationary: the pair is cointegrated
 - Cointegrating coefficient β: the hedge ratio (how much of asset 2 to hold per unit of asset 1)
 - Limitation: only tests one cointegrating vector; sensitive to which asset is on the left-hand side

 Johansen test (preferred for robustness):
 - Tests for multiple cointegrating relationships
 - Trace statistic and Max-Eigenvalue statistic
 - Null H₀(r=0): no cointegrating vectors. Reject at p < 0.05.
 - Reports the cointegrating vector and loading coefficients (speed of adjustment)

2. Spread construction:
 Spread_t = P1_t - β × P2_t
 - Plot the spread over time: should look mean-reverting if cointegrated
 - Compute: mean of spread, std of spread, half-life of mean reversion
 - Half-life: from Ornstein-Uhlenbeck fit: dS = κ(μ - S)dt + σdW
 Half-life = ln(2) / κ
 - Very short half-life (<5 days): crowded, may not survive transaction costs
 - Very long half-life (>120 days): too slow, requires significant capital commitment

3. Trading signals:
 Standardized spread (z-score): z_t = (Spread_t - μ) / σ
 - Entry long: z < -2 (spread below mean by 2σ: buy asset 1, sell asset 2)
 - Entry short: z > +2 (spread above mean: sell asset 1, buy asset 2)
 - Exit: z crosses zero (or ±0.5)
 - Stop-loss: z > ±3 or ±4 (spread has diverged beyond tolerable levels)

4. Backtest the pairs strategy:
 - Signal generation as above
 - Dollar-neutral: equal dollar value in each leg
 - Transaction costs: round-trip spread + market impact
 - Report: Sharpe ratio, Calmar, turnover, avg holding period, win rate, drawdown

5. Stability checks:
 - Is the cointegrating relationship stable over time? Rolling Engle-Granger test
 - Does the hedge ratio drift? Rolling OLS hedge ratio over 252-day window
 - Structural break tests (CUSUM, Bai-Perron): has the relationship broken down?

Return: cointegration test results, spread construction and statistics, OU parameter estimates, backtest performance, and stability analysis. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical and econometric methods work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical and Econometric Methods or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Cointegration testing:, If residuals are stationary: the pair is cointegrated, Cointegrating coefficient β: the hedge ratio (how much of asset 2 to hold per unit of asset 1). The final answer should stay clear, actionable, and easy to review inside a statistical and econometric methods workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Statistical and Econometric Methods.
