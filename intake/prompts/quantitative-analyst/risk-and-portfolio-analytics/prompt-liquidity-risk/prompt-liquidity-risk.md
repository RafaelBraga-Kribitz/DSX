# Liquidity Risk Assessment *AI Prompt *

Assess the liquidity risk of this portfolio and estimate the cost and time required for liquidation. Portfolio holdings: {{holdings}} (positions and sizes) Market data: {{market... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Assess the liquidity risk of this portfolio and estimate the cost and time required for liquidation.

Portfolio holdings: {{holdings}} (positions and sizes)
Market data: {{market_data}} (average daily volume, bid-ask spreads)
Liquidation scenario: {{scenario}}

1. Liquidity metrics per position:
 - Average Daily Volume (ADV): 20-day and 60-day trailing ADV
 - Days-to-liquidate (DTL): position_size / (participation_rate × ADV)
 Standard assumption: participate at 20% of ADV to avoid significant market impact
 - Bid-ask spread cost: size × (ask - bid) / midprice
 - Amihud illiquidity ratio: |return| / dollar_volume. Higher = more illiquid.

2. Portfolio-level liquidity:
 - Asset-weighted average DTL for the full portfolio
 - DTL percentile distribution: what % of the portfolio can be liquidated in 1 day, 3 days, 1 week, 2 weeks?
 - Illiquid tail: which positions have DTL > 20 days? These are the most problematic under stress.

3. Market impact modeling:
 The square-root market impact model:
 Impact = η × σ × sqrt(Q / ADV)
 Where η ≈ 0.1 for equities, σ = daily volatility, Q = shares to trade, ADV = average daily volume
 - Estimate market impact for each position at 100% liquidation
 - Total liquidation cost = bid-ask spread cost + market impact cost
 - Liquidity-adjusted VaR: add expected liquidation cost to standard VaR

4. Stress scenario — forced liquidation:
 Scenario: forced to liquidate {{pct}}% of portfolio in {{days}} trading days
 - Which positions can be liquidated within the constraint?
 - What market impact will the liquidation create?
 - What is the expected slippage cost in dollars and as % of portfolio NAV?
 - Which positions will require extended liquidation beyond the constraint?

5. Liquidity mismatch risk:
 - If managing a fund: compare portfolio liquidity profile to fund redemption terms
 - What fraction of the portfolio could be liquidated within the fund's redemption notice period?
 - What are the implications if redemptions exceed the liquid portion?

6. Liquidity stress testing:
 - Scenario: ADV drops 50% (typical in a crisis). How does the DTL profile change?
 - Scenario: bid-ask spreads widen 5×. How does total liquidation cost change?

Return: per-position liquidity metrics, portfolio liquidity distribution, market impact estimates, forced liquidation analysis, and liquidity stress test results. 
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

The AI should return a structured result that covers the main requested outputs, such as Liquidity metrics per position:, Average Daily Volume (ADV): 20-day and 60-day trailing ADV, Days-to-liquidate (DTL): position_size / (participation_rate × ADV). The final answer should stay clear, actionable, and easy to review inside a risk and portfolio analytics workflow for quantitative analyst work. 

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
