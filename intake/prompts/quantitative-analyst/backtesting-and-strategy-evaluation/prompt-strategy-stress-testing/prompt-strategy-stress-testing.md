# Strategy Stress Testing *AI Prompt *

Stress test this trading strategy under adverse market conditions to understand its tail behavior. Strategy: {{strategy}} Backtest returns: {{returns}} 1. Historical scenario an... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Stress test this trading strategy under adverse market conditions to understand its tail behavior.

Strategy: {{strategy}}
Backtest returns: {{returns}}

1. Historical scenario analysis:
 For each crisis period, compute strategy performance:
 - Black Monday (Oct 1987): equity crash, volatility spike
 - LTCM crisis (Aug–Oct 1998): liquidity crisis, correlation spike
 - Dot-com crash (Mar 2000 – Oct 2002): prolonged drawdown, tech collapse
 - Global Financial Crisis (Sep 2008 – Mar 2009): systemic risk, credit freeze
 - European Debt Crisis (May 2010, Jul–Oct 2011)
 - Taper Tantrum (May–Jun 2013)
 - COVID crash (Feb 20 – Mar 23, 2020)
 - 2022 rate shock (Jan–Oct 2022): bonds and equities fell simultaneously

 For each scenario report:
 - Strategy return during the crisis window
 - Strategy maximum drawdown during the crisis
 - Sharpe ratio during the crisis period
 - How does strategy performance compare to the market during the crisis?

2. Hypothetical scenario analysis:
 Construct and test these forward-looking scenarios:
 - Volatility spike: all asset volatilities double overnight (test position sizing and risk limits)
 - Correlation crisis: all pairwise correlations spike to 0.9 (diversification disappears)
 - Liquidity crisis: bid-ask spreads widen 5× and ADV drops 70%
 - Rate shock: yield curve shifts +200bps in 3 months
 - Crowded trade unwind: all similar strategies receive simultaneous redemptions and must sell the same positions

3. Worst-case analysis:
 - What single month would have been worst for this strategy historically?
 - What single week? What single day?
 - Are the worst periods concentrated in a specific regime (high vol, risk-off)?

4. Sensitivity to key assumptions:
 - What if the signal IC is 50% lower than assumed? (Alpha decay scenario)
 - What if transaction costs are 2× higher than modeled?
 - What if correlation between assets reverts to a 2008-level regime?
 - What if AUM grows 5× — does capacity constraint degrade performance?

5. Strategy's crash risk profile:
 - Does the strategy make money during crises (crisis alpha) or lose money?
 - Does it suffer from sudden large losses or gradual drawdowns?
 - Are losses correlated with investor redemption risk (liquidity mismatch)?
 - Maximum theoretical loss if all positions go against you simultaneously (sum of individual position max losses)

Return: historical scenario table, hypothetical scenario analysis, worst-case statistics, sensitivity analysis, and crash risk profile. 
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

The AI should return a structured result that covers the main requested outputs, such as Historical scenario analysis:, Black Monday (Oct 1987): equity crash, volatility spike, LTCM crisis (Aug–Oct 1998): liquidity crisis, correlation spike. The final answer should stay clear, actionable, and easy to review inside a backtesting and strategy evaluation workflow for quantitative analyst work. 

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
