# Backtesting and Strategy Evaluation *AI Prompts *

5 Quantitative Analyst prompts in Backtesting and Strategy Evaluation. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Backtesting and Strategy Evaluation 
5 prompts Beginner Single prompt 01 
### Backtest Bias Audit 

Audit this backtest for the common biases that cause simulated performance to overstate live performance. Backtest description: {{backtest_description}} Strategy: {{strategy}} C... 
Prompt text Audit this backtest for the common biases that cause simulated performance to overstate live performance.

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

Return: bias audit table, estimated total bias impact on Sharpe ratio, and corrected performance estimate. Copy prompt Open prompt details Advanced Single prompt 02 
### Overfitting Detection 

Detect and quantify overfitting in this quantitative strategy or model. Strategy / model: {{strategy}} Backtest results: {{backtest_results}} Number of parameters: {{n_params}}... 
Prompt text Detect and quantify overfitting in this quantitative strategy or model.

Strategy / model: {{strategy}}
Backtest results: {{backtest_results}}
Number of parameters: {{n_params}}
In-sample period: {{is_period}}
Out-of-sample period: {{oos_period}}

1. The overfitting problem in quantitative finance:
 - Financial time series are noisy with low signal-to-noise ratios
 - The probability of backtest overfitting (PBO) is high even with careful methodology
 - Bailey, Borwein, Lopez de Prado, Zhu (2014): with 45 backtests, random chance will produce one Sharpe > 1.5 even if there is no true alpha

2. Deflated Sharpe Ratio (DSR):
 DSR accounts for the number of trials and the statistical properties of the backtest:
 DSR = PSR(SR*) where PSR is the Probabilistic Sharpe Ratio
 SR* = SR_benchmark × sqrt(1 - ρ + N × ρ × (1 - 1/N)) ← effective benchmark adjusted for N trials
 - Report: number of trials N, assumed independent trials, DSR value
 - DSR < 0.95 after accounting for N trials: likely overfit

3. Probabilistic Sharpe Ratio (PSR):
 PSR(SR*) = Φ[(SR - SR*) × sqrt(T-1) / sqrt(1 - γ₃SR + (γ₄-1)/4 × SR²)]
 Where γ₃ = skewness, γ₄ = kurtosis of returns
 - PSR measures the probability that the true Sharpe exceeds a benchmark (e.g. 0 or 0.5)
 - PSR < 0.95 at benchmark SR = 0: cannot rule out that true SR ≤ 0

4. Minimum Backtest Length (MinBTL):
 MinBTL = (SR / SR_hat)² × (1 - ρ + N × ρ) × (1 + (1 - γ₃SR + (γ₄-1)/4 × SR²) / (T-1))⁻¹
 - Given N trials and observed SR, what minimum backtest length is needed to be 95% confident the strategy is not overfit?
 - If actual backtest length < MinBTL: almost certainly overfit

5. Combinatorial Purged Cross-Validation (CPCV):
 - Split data into T non-overlapping folds
 - Generate all C(T, 2) combinations of training/test splits (each combination is one path)
 - Compute performance on each test path
 - PBO: fraction of test paths where OOS performance is worse than expected
 - Advantage: uses all data for both training and testing; robust to regime selection

6. Parameter sensitivity check:
 - Perturb each parameter by ±10% and ±25% from optimal value
 - Plot performance surface around the optimal point
 - Robust strategy: flat performance surface around optimal (many local parameter combinations work)
 - Overfit strategy: sharp performance spike at optimal (only exact values work)

Return: DSR calculation, PSR, MinBTL, CPCV results, parameter sensitivity surface, and overfitting probability assessment. Copy prompt Open prompt details Advanced Single prompt 03 
### Strategy Stress Testing 

Stress test this trading strategy under adverse market conditions to understand its tail behavior. Strategy: {{strategy}} Backtest returns: {{returns}} 1. Historical scenario an... 
Prompt text Stress test this trading strategy under adverse market conditions to understand its tail behavior.

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

Return: historical scenario table, hypothetical scenario analysis, worst-case statistics, sensitivity analysis, and crash risk profile. Copy prompt Open prompt details Intermediate Single prompt 04 
### Transaction Cost Modeling 

Build a realistic transaction cost model for this trading strategy and assess its impact on performance. Strategy: {{strategy}} Asset class: {{asset_class}} Typical position siz... 
Prompt text Build a realistic transaction cost model for this trading strategy and assess its impact on performance.

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

Return: cost model for each component, annualized total cost estimate, net performance table at different cost levels, and break-even analysis. Copy prompt Open prompt details Intermediate Single prompt 05 
### Walk-Forward Validation 

Design and execute a walk-forward validation framework to assess strategy robustness out-of-sample. Strategy: {{strategy}} Total data period: {{period}} Parameters to optimize:... 
Prompt text Design and execute a walk-forward validation framework to assess strategy robustness out-of-sample.

Strategy: {{strategy}}
Total data period: {{period}}
Parameters to optimize: {{parameters}}

1. Walk-forward validation framework:
 - Training window: {{training_length}} months (used for parameter optimization)
 - Test window: {{test_length}} months (out-of-sample evaluation)
 - Step: {{step_size}} months (how often to re-optimize)
 - Total OOS periods: (total_months - training_months) / step_size

 Process for each fold:
 1. Train: optimize parameters on training window to maximize {{objective}} (e.g. Sharpe)
 2. Freeze: lock the optimal parameters from the training window
 3. Test: evaluate the frozen strategy on the next test window
 4. Step: advance both windows by the step size
 5. Repeat until the end of data

2. Walk-forward variants:
 - Anchored (expanding window): training window grows over time. More data but may include stale regimes.
 - Rolling (fixed window): training window moves with a fixed length. Adapts to regime changes but discards old data.
 - Recommendation: compare both; if they diverge significantly, parameters are regime-dependent.

3. Concatenated OOS performance:
 - Concatenate all test period results into a single OOS return series
 - This is the most realistic performance estimate: uses only OOS data
 - Report: Sharpe, Calmar, max drawdown, win rate, and turnover on the OOS series

4. In-sample vs out-of-sample performance ratio:
 - IS Sharpe / OOS Sharpe: if > 2, significant overfitting
 - Minimum OOS Sharpe ≥ 50% of IS Sharpe: rough guideline for acceptable overfitting
 - If OOS performance is dramatically worse: the strategy is overfit, not robust

5. Parameter stability analysis:
 - Plot the optimal parameter value chosen at each training step over time
 - Are optimal parameters stable across windows or do they oscillate?
 - High instability → the strategy is sensitive to parameter choice → not robust
 - A strategy with robust parameters will show similar optimal values across training windows

6. Number of OOS periods required:
 - Need at least 30 OOS periods (folds) for statistical inference on OOS performance
 - With 30 periods at monthly frequency: 2.5 years of OOS data
 - With 3-month test windows: need 7.5 years of OOS data — this is a significant requirement

Return: walk-forward performance table (IS vs OOS per fold), concatenated OOS Sharpe and drawdown, parameter stability plots, and overfitting assessment. Copy prompt Open prompt details 
## Recommended Backtesting and Strategy Evaluation workflow 
1 
### Backtest Bias Audit 

Start with a focused prompt in Backtesting and Strategy Evaluation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Overfitting Detection 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Strategy Stress Testing 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Transaction Cost Modeling 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
