# Volatility Regime Analysis *AI Prompt *

Analyze volatility regimes in this return series and build a regime classification model. Asset / index: {{asset}} Return series: {{returns}} 1. Realized volatility estimation m... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze volatility regimes in this return series and build a regime classification model.

Asset / index: {{asset}}
Return series: {{returns}}

1. Realized volatility estimation methods:
 Compare these estimators and explain when each is appropriate:
 - Close-to-close: std(log returns) × sqrt(252). Simple but uses only end-of-day prices.
 - Parkinson: uses daily high-low range. More efficient than close-to-close.
 - Garman-Klass: uses OHLC prices. More efficient than Parkinson.
 - Yang-Zhang: handles overnight gaps. Best all-around estimator for daily OHLC.
 - Rolling window choice: 21-day (1 month), 63-day (1 quarter), 252-day (1 year) — each captures different features

2. GARCH volatility modeling:
 Fit a GARCH(1,1) model: σ²_t = ω + α ε²_{t-1} + β σ²_{t-1}
 - Report: ω, α, β, and their standard errors
 - Persistence: α + β. If > 0.99, volatility shocks are very long-lived.
 - Half-life of volatility shock: ln(0.5) / ln(α + β)
 - Likelihood ratio test: GARCH vs constant variance (ARCH test)
 - Plot conditional volatility over time

3. Regime detection:
 Method A — Hidden Markov Model (HMM):
 - Fit a 2-state Gaussian HMM to the returns
 - State 1 typically: low volatility, higher mean (bull)
 - State 2 typically: high volatility, lower/negative mean (bear)
 - Report: state means, state variances, transition probability matrix
 - Plot: smoothed state probabilities over time

 Method B — Threshold-based regime classification:
 - Low vol: rolling 21-day vol < 33rd percentile of historical vol
 - Medium vol: 33rd–67th percentile
 - High vol: > 67th percentile
 - Simpler, more transparent, but not probabilistic

4. Regime statistics:
 For each regime, report:
 - Mean return (annualized)
 - Volatility (annualized)
 - Sharpe ratio
 - Average duration (how long do regimes last?)
 - Transition frequency

5. Practical implications:
 - Does the current period appear to be in a high-vol regime?
 - How should portfolio risk management differ across regimes?

Return: volatility estimator comparison, GARCH results, HMM regime probabilities, regime statistics table, and current regime assessment. 
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

The AI should return a structured result that covers the main requested outputs, such as Realized volatility estimation methods:, Close-to-close: std(log returns) × sqrt(252). Simple but uses only end-of-day prices., Parkinson: uses daily high-low range. More efficient than close-to-close.. The final answer should stay clear, actionable, and easy to review inside a financial data analysis workflow for quantitative analyst work. 

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
