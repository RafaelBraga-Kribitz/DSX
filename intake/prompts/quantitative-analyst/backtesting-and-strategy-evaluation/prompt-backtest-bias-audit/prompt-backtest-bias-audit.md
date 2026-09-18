# Backtest Bias Audit *AI Prompt *

Audit this backtest for the common biases that cause simulated performance to overstate live performance. Backtest description: {{backtest_description}} Strategy: {{strategy}} C... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit this backtest for the common biases that cause simulated performance to overstate live performance.

Backtest description: {{backtest_description}}
Strategy: {{strategy}}

Check for each bias category:

1. Look-ahead bias (most serious):
 - Is any information used in signal generation that was not available at the time the trade would have been made?
 - Examples:
 - Using closing price to generate the signal AND trade at the same day's closing price
 - Using point-in-time financial data (quarterly earnings) before they were publicly released
 - Using index membership as of today, not as of the trade date
 - Lagged signals: is there a one-day lag between signal and execution?
 - Detection: introduce a 1-day execution lag and see how much performance changes

2. Survivorship bias:
 - Does the asset universe include only entities that survived to the present?
 - Stocks that went bankrupt, funds that closed, companies that were delisted — all excluded?
 - Impact: enormous for long-short equity strategies (shorting future bankruptcies looks easy in hindsight)
 - Fix: use a point-in-time universe that captures all assets that existed at each backtest date

3. Data snooping bias (overfitting):
 - How many parameter combinations were tested before settling on current values?
 - Were the parameters chosen by optimizing in-sample performance?
 - Were multiple strategies tested and only the best reported?
 - Fix: true out-of-sample test; or account for multiple testing via bootstrap

4. Transaction cost bias:
 - Are all transaction costs included: commissions, bid-ask spread, market impact, short borrow cost?
 - Are market impact costs realistic for the strategy's position size relative to ADV?
 - Are short borrow costs included for short positions?
 - Typical costs ignored: overnight financing, currency hedging, taxes

5. Execution bias:
 - Are trades assumed to execute at close-of-day prices? (Unrealistic for large positions)
 - Is partial fill risk modeled? (Large orders may not fully fill)
 - Is slippage modeled?

6. Regime bias:
 - Does the backtest happen to coincide with a favorable regime for the strategy?
 - What is the performance in sub-periods: 2000–2008, 2009–2019, 2020–present?

For each bias: assess severity (Low/Medium/High), estimate the impact on reported Sharpe ratio, and recommend the fix.

Return: bias audit table, estimated total bias impact on Sharpe ratio, and corrected performance estimate. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin backtesting and strategy evaluation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Backtesting and Strategy Evaluation or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Look-ahead bias (most serious):, Is any information used in signal generation that was not available at the time the trade would have been made?, Examples:. The final answer should stay clear, actionable, and easy to review inside a backtesting and strategy evaluation workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Backtesting and Strategy Evaluation.
