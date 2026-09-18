# Risk and Portfolio Analytics *AI Prompts *

7 Quantitative Analyst prompts in Risk and Portfolio Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts · 1 chain. 

## AI prompts in Risk and Portfolio Analytics 
7 prompts Intermediate Single prompt 01 
### Drawdown Analysis 

Conduct a comprehensive drawdown analysis for this strategy or portfolio. Return series: {{returns}} Benchmark (optional): {{benchmark}} 1. Drawdown calculation: - Cumulative we... 
Prompt text Conduct a comprehensive drawdown analysis for this strategy or portfolio.

Return series: {{returns}}
Benchmark (optional): {{benchmark}}

1. Drawdown calculation:
 - Cumulative wealth index: W_t = ∏(1 + r_i) for i = 1 to t
 - Running maximum: M_t = max(W_1, W_2, ..., W_t)
 - Drawdown at time t: DD_t = (W_t - M_t) / M_t
 - Maximum drawdown (MDD): min(DD_t) over full period

2. Drawdown statistics:
 - Maximum drawdown: magnitude and the peak and trough dates
 - Average drawdown: mean of all drawdown episodes
 - Average drawdown duration: average time from peak to trough
 - Average recovery time: average time from trough to new high water mark
 - Number of drawdown episodes exceeding threshold (e.g. >5%, >10%, >20%)
 - Current drawdown: is the strategy currently in a drawdown?

3. Drawdown distribution:
 - Plot all drawdown episodes sorted by severity
 - Are large drawdowns rare events or do they cluster?
 - Drawdown at each percentile (50th, 75th, 90th, 95th) of episode severity

4. Underwater curve analysis:
 - Plot the cumulative return and the underwater curve (time spent in drawdown) on the same chart
 - What fraction of total time was the strategy in a drawdown?
 - Pain index: average drawdown × fraction of time in drawdown

5. Risk-adjusted return ratios involving drawdown:
 - Calmar ratio: annualized return / |MDD|. Higher is better. Benchmark: > 0.5
 - Sterling ratio: annualized return / average of top 3 annual drawdowns
 - Burke ratio: annualized return / sqrt(sum of squared drawdowns)
 - Martin ratio (Ulcer index-based): annualized return / Ulcer_index
 Ulcer index = sqrt(mean(DD²)): penalizes both depth and duration of drawdowns

6. Drawdown comparison to benchmark:
 - Relative drawdown: active drawdown = portfolio DD - benchmark DD
 - Did the strategy protect capital better or worse than the benchmark during major drawdown periods?
 - Maximum relative drawdown and its timing

Return: drawdown statistics table, underwater curve plot, drawdown episode list, ratio comparison, and benchmark relative analysis. Copy prompt Open prompt details Advanced Chain 02 
### Full Risk Analytics Chain 

Step 1: Return data profiling — profile the return data quality. Check for missing dates, zero returns, extreme outliers, survivorship bias, and corporate action contamination.... 
Prompt text Step 1: Return data profiling — profile the return data quality. Check for missing dates, zero returns, extreme outliers, survivorship bias, and corporate action contamination. Compute basic statistics and confirm data is suitable for analysis.
Step 2: Distributional analysis — test for normality, measure skewness and excess kurtosis, estimate tail behavior using EVT (GPD fitting). Determine which risk models are appropriate given the distributional properties.
Step 3: VaR and CVaR — compute using all three methods (historical, parametric, Monte Carlo). Backtest VaR with Kupiec POF test and Christoffersen interval forecast test. Report which method is most appropriate.
Step 4: Drawdown analysis — compute maximum drawdown, average drawdown, recovery time, and the full distribution of drawdown episodes. Report Calmar ratio, Ulcer index, and current drawdown status.
Step 5: Factor decomposition — run factor model regression. Decompose total risk into systematic (factor) and idiosyncratic components. Identify the dominant factor exposures driving portfolio risk.
Step 6: Stress testing — apply at least 3 historical stress scenarios and 3 hypothetical scenarios. For each: P&L impact, VaR comparison, and which positions contribute most to stress loss.
Step 7: Risk report — write a 1-page risk summary: current risk level vs target, factor exposures of concern, tail risk assessment, liquidity profile, and top 3 risk management recommendations. Copy prompt Open prompt details Advanced Single prompt 03 
### Liquidity Risk Assessment 

Assess the liquidity risk of this portfolio and estimate the cost and time required for liquidation. Portfolio holdings: {{holdings}} (positions and sizes) Market data: {{market... 
Prompt text Assess the liquidity risk of this portfolio and estimate the cost and time required for liquidation.

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

Return: per-position liquidity metrics, portfolio liquidity distribution, market impact estimates, forced liquidation analysis, and liquidity stress test results. Copy prompt Open prompt details Intermediate Single prompt 04 
### Performance Attribution 

Decompose portfolio performance into its sources using Brinson-Hood-Beebower (BHB) attribution. Portfolio: {{portfolio_weights_and_returns}} Benchmark: {{benchmark_weights_and_r... 
Prompt text Decompose portfolio performance into its sources using Brinson-Hood-Beebower (BHB) attribution.

Portfolio: {{portfolio_weights_and_returns}}
Benchmark: {{benchmark_weights_and_returns}}
Period: {{period}}

1. BHB attribution framework:
 Total active return = Allocation effect + Selection effect + Interaction effect

 For each segment i:
 - Allocation effect: (w_p,i - w_b,i) × (R_b,i - R_b)
 Did we overweight/underweight the right segments?
 - Selection effect: w_b,i × (R_p,i - R_b,i)
 Did we pick better securities within each segment?
 - Interaction effect: (w_p,i - w_b,i) × (R_p,i - R_b,i)
 Did we concentrate in segments where we had good selection?

 Where:
 - w_p,i = portfolio weight in segment i
 - w_b,i = benchmark weight in segment i
 - R_p,i = portfolio return in segment i
 - R_b,i = benchmark return in segment i
 - R_b = total benchmark return

2. Segment definitions:
 Apply attribution at multiple levels:
 - Level 1: by asset class (equity, fixed income, alternatives)
 - Level 2: by sector (within equity: technology, healthcare, financials, etc.)
 - Level 3: by country or region (within global equity)

3. Attribution over time:
 - Monthly attribution: cumulative linking is required (simple addition creates geometric compounding error)
 - Geometric linking method: chain-link the single-period attributions
 - Plot cumulative allocation, selection, and interaction effects over the period

4. Factor attribution (alternative to BHB):
 Regress active returns on factor returns (Barra or Fama-French):
 - Factor contribution: β_factor × factor_return
 - Specific (residual) contribution: unexplained by factors
 - This tells you whether outperformance came from intentional factor tilts or from security selection

5. Risk-adjusted attribution:
 - Information ratio: active_return / tracking_error
 - t-statistic: is active return statistically significant? Require ≥ 3 years to assess significance.
 - Active risk decomposition: which bets contributed most to tracking error?

6. Pitfalls:
 - Currency effects: separate currency contribution from local return contribution for international portfolios
 - Geometric vs arithmetic: be explicit about which convention is used

Return: BHB attribution table by segment, cumulative attribution plots, factor attribution, and information ratio analysis. Copy prompt Open prompt details Intermediate Single prompt 05 
### Portfolio Optimization 

Construct an optimal portfolio from this asset universe using mean-variance optimization and robust alternatives. Assets: {{asset_universe}} Return estimates: {{return_estimates... 
Prompt text Construct an optimal portfolio from this asset universe using mean-variance optimization and robust alternatives.

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

Return: efficient frontier plot, portfolio weights for each method, sensitivity analysis, walk-forward performance comparison. Copy prompt Open prompt details Advanced Single prompt 06 
### Risk Parity Construction 

Construct and analyze a risk parity portfolio from this asset universe. Assets: {{assets}} Covariance matrix: {{covariance}} Target volatility: {{target_vol}} (e.g. 10% annualiz... 
Prompt text Construct and analyze a risk parity portfolio from this asset universe.

Assets: {{assets}}
Covariance matrix: {{covariance}}
Target volatility: {{target_vol}} (e.g. 10% annualized)

1. Risk contribution framework:
 Marginal risk contribution (MRC): MRC_i = (Σw)_i = ∂σ_p/∂w_i
 Total risk contribution (TRC): TRC_i = w_i × MRC_i
 Portfolio variance: σ²_p = w'Σw = Σ_i TRC_i
 Risk contribution percentage: RC%_i = TRC_i / σ²_p

 Risk parity condition: RC%_i = 1/N for all assets i

2. Numerical solution:
 Risk parity has no closed-form solution for N > 2 assets.
 Use gradient-based optimization:
 min Σ_i Σ_j (TRC_i - TRC_j)² subject to w'1 = 1, w ≥ 0

 Or alternatively, use Maillard et al. (2010) iterative algorithm:
 w_i ← w_i × σ_p / (N × MRC_i) → iterate until convergence

3. Risk parity portfolio analysis:
 - Report: asset weights, marginal risk contributions, percentage risk contributions
 - Verify: risk contributions are approximately equal across all assets
 - Compare weights to: equal-weight, min-variance, and 60/40 benchmark

4. Volatility targeting:
 - Scale the risk parity weights by: k = target_vol / σ_rp
 - This may require leverage if σ_rp < target_vol (common with bonds in the portfolio)
 - Report: leverage ratio, cost of leverage assumed (financing rate)

5. Sensitivity analysis:
 - How do weights change if equity volatility doubles? (Bonds get more weight)
 - How do weights change if bond-equity correlation goes from -0.3 to +0.3?
 - Risk parity is most sensitive to: changes in relative volatilities and correlation regime changes

6. Historical performance analysis:
 - Backtest the risk parity portfolio with monthly rebalancing
 - Compare to: equal-weight, 60/40, min-variance
 - Report: Sharpe ratio, Calmar ratio, max drawdown, monthly turnover
 - Notable: risk parity struggled in 2022 when bonds and equities both sold off simultaneously (positive correlation regime)

7. Limitations:
 - Risk parity is a risk-based, not return-based, allocation
 - It is implicitly long duration (bonds dominate in unlevered form)
 - Correlation instability undermines the equal risk contribution in practice

Return: risk parity weights with risk contribution verification, comparison table, sensitivity analysis, and backtest performance. Copy prompt Open prompt details Beginner Single prompt 07 
### VaR and CVaR Calculation 

Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR) for this portfolio using multiple methods. Portfolio returns: {{returns}} Confidence levels: 95% and 99% Holdi... 
Prompt text Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR) for this portfolio using multiple methods.

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

Return: VaR and CVaR table (method × confidence level), method comparison, scaling analysis, and backtesting results. Copy prompt Open prompt details 
## Recommended Risk and Portfolio Analytics workflow 
1 
### Drawdown Analysis 

Start with a focused prompt in Risk and Portfolio Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Full Risk Analytics Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Liquidity Risk Assessment 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Performance Attribution 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
