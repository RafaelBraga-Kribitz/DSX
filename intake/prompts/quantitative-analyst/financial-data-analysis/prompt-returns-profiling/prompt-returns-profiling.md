# Returns Data Profiling *AI Prompt *

Profile this financial returns dataset and identify any data quality issues before analysis. Asset class: {{asset_class}} Frequency: {{frequency}} (daily, weekly, monthly) Date... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Profile this financial returns dataset and identify any data quality issues before analysis.

Asset class: {{asset_class}}
Frequency: {{frequency}} (daily, weekly, monthly)
Date range: {{date_range}}

1. Basic return statistics:
 - Count of observations and date range coverage
 - Mean, median, standard deviation, min, max
 - Annualized return: mean_daily × 252 (or ×52 weekly, ×12 monthly)
 - Annualized volatility: std_daily × sqrt(252)
 - Skewness and excess kurtosis — financial returns typically show negative skewness and excess kurtosis (fat tails)

2. Data quality checks specific to returns:
 - Zero returns: flag consecutive zero returns (>3 in a row often indicates a data freeze or illiquid asset, not a flat market)
 - Extreme returns: flag returns beyond ±10σ — likely data errors, corporate actions, or extreme events requiring investigation
 - Missing dates: check against the expected trading calendar. Missing dates should be explained (holidays, halts)
 - Stale prices: if using prices, identical consecutive closing prices for liquid assets signal a data problem
 - Survivorship bias check: is this a historical dataset? Were assets included only if they survived to the present?

3. Distribution analysis:
 - Plot return distribution vs normal distribution overlay
 - Jarque-Bera test for normality: JB = n/6 × (S² + K²/4) where S=skewness, K=excess kurtosis
 - Report: skewness (negative is left-skewed — bad tails), kurtosis (>3 indicates fat tails)
 - Quantile-Quantile plot: visual check for tail behavior relative to normal

4. Autocorrelation check:
 - Ljung-Box test for serial autocorrelation in returns (should be near zero for efficient markets)
 - Ljung-Box test on squared returns (should show autocorrelation — volatility clustering is expected)
 - Plot ACF and PACF for returns and squared returns

5. Corporate actions and outliers:
 - Flag dates with |return| > 3σ as requiring investigation
 - For each flagged date: check if the return aligns with a known event (earnings, index rebalance, dividend)
 - Adjust for dividends and splits if working with raw prices

Return: summary statistics table, data quality flag list, distribution plots, autocorrelation results, and a data quality verdict (suitable for analysis / needs adjustment / not suitable). 
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

The AI should return a structured result that covers the main requested outputs, such as Basic return statistics:, Count of observations and date range coverage, Mean, median, standard deviation, min, max. The final answer should stay clear, actionable, and easy to review inside a financial data analysis workflow for quantitative analyst work. 

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
