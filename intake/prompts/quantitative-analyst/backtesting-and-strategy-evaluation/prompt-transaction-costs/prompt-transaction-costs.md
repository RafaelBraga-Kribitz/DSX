# Transaction Cost Modeling *AI Prompt *

Build a realistic transaction cost model for this trading strategy and assess its impact on performance. Strategy: {{strategy}} Asset class: {{asset_class}} Typical position siz... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a realistic transaction cost model for this trading strategy and assess its impact on performance.

Strategy: {{strategy}}
Asset class: {{asset_class}}
Typical position size vs ADV: {{position_vs_adv}}

1. Components of total transaction cost:

 a. Explicit costs:
 - Commission: broker fee per share or per dollar traded
 - SEC fee (US equities): $8 per $1M of sales
 - Exchange fees and rebates (maker/taker model)

 b. Implicit costs:
 - Bid-ask spread: cost of crossing the spread = 0.5 × (ask - bid) / midprice per trade
 - Market impact: additional cost of moving the market when executing large orders
 - Timing risk: price moves against you between decision and execution

 c. Short sale costs:
 - Short borrow rate: typically 0.5–2% annualized for easy-to-borrow stocks; can be >10% for hard-to-borrow
 - Locate fee: cost of finding shares to borrow before shorting

2. Bid-ask spread estimation:
 - Use quoted spread for liquid assets: (ask - bid) / midprice
 - Half-spread per one-way trip: 0.5 × quoted_spread
 - Historical spread data if available; otherwise estimate from Roll's model or Corwin-Schultz

3. Market impact model:
 Square-root impact model (Almgren-Chriss):
 Impact = η × σ × (Q / ADV)^0.5
 Where: η ≈ 0.1 (empirical constant), σ = daily vol, Q = trade size as fraction of ADV

 Linear impact model (simpler):
 Impact = κ × (Q / ADV)
 Where κ typically 0.005–0.02 depending on asset liquidity

 Apply at each trade and aggregate over the holding period.

4. Turnover-cost relationship:
 - Annualized one-way turnover rate from the strategy
 - Total annualized cost = turnover × (commission + half_spread + market_impact)
 - Drag on annual return: total_annualized_cost as % of AUM
 - Break-even Sharpe: what gross Sharpe is needed to achieve a net Sharpe of 0.5 after costs?

5. Sensitivity analysis:
 - Net performance at: 0× costs, 0.5× costs, 1× costs, 2× costs (stress test)
 - At what cost multiplier does net Sharpe fall below 0.5?
 - Which cost component has the largest impact: spread, market impact, or borrow?

6. Cost reduction strategies:
 - Reduce turnover: wider signal thresholds before rebalancing
 - Use limit orders instead of market orders to reduce spread cost (adds execution risk)
 - Optimal execution: stagger large trades over multiple days to reduce market impact
 - Netting: trade only the net change in position when multiple signals conflict

Return: cost model for each component, annualized total cost estimate, net performance table at different cost levels, and break-even analysis. 
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

The AI should return a structured result that covers the main requested outputs, such as Components of total transaction cost:, Commission: broker fee per share or per dollar traded, SEC fee (US equities): $8 per $1M of sales. The final answer should stay clear, actionable, and easy to review inside a backtesting and strategy evaluation workflow for quantitative analyst work. 

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
