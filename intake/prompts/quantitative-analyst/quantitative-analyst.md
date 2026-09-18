# Quantitative Analyst *AI Prompts *

Quantitative Analyst AI prompt library with 27 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Quantitative Analyst prompt categories 
5 categories 
### Risk and Portfolio Analytics 

AI prompts for risk and portfolio analytics, including exposure analysis, scenario testing, allocation diagnostics, and risk-adjusted evaluation. 
7 prompts Drawdown Analysis Full Risk Analytics Chain → 
### Financial Data Analysis 

AI prompts for financial data analysis, including market data profiling, factor exploration, performance decomposition, and signal diagnostics. 
6 prompts Alpha Signal Evaluation Correlation Structure Analysis → 
### Statistical and Econometric Methods 

AI prompts for statistical and econometric methods, including model specification, parameter interpretation, diagnostics, and robustness checks. 
6 prompts Cointegration and Pairs Trading Cross-Sectional Regression → 
### Backtesting and Strategy Evaluation 

AI prompts for backtesting and strategy evaluation, including performance analysis, robustness checks, and practical decision criteria for quantitative workflows. 
5 prompts Backtest Bias Audit Overfitting Detection → 
### Quantitative Research Process 

AI prompts for structured quantitative research processes, from question framing and data preparation to model testing and interpretation. 
3 prompts Alpha Research Framework Factor Crowding Assessment → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 27 Risk and Portfolio Analytics 7 Financial Data Analysis 6 Statistical and Econometric Methods 6 Backtesting and Strategy Evaluation 5 Quantitative Research Process 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **27 **of 27 prompts 
## Risk and Portfolio Analytics 
7 prompt s Risk and Portfolio Analytics Intermediate Prompt 01 
### Drawdown Analysis 
Conduct a comprehensive drawdown analysis for this strategy or portfolio.

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

Return: drawdown statistics table, underwater curve plot, drawdown episode list, ratio comparison, and benchmark relative analysis. Copy prompt View page Show more ↓ Risk and Portfolio Analytics Advanced Chain 02 
### Full Risk Analytics Chain 
Step 1: Return data profiling — profile the return data quality. Check for missing dates, zero returns, extreme outliers, survivorship bias, and corporate action contamination. Compute basic statistics and confirm data is suitable for analysis.
Step 2: Distributional analysis — test for normality, measure skewness and excess kurtosis, estimate tail behavior using EVT (GPD fitting). Determine which risk models are appropriate given the distributional properties.
Step 3: VaR and CVaR — compute using all three methods (historical, parametric, Monte Carlo). Backtest VaR with Kupiec POF test and Christoffersen interval forecast test. Report which method is most appropriate.
Step 4: Drawdown analysis — compute maximum drawdown, average drawdown, recovery time, and the full distribution of drawdown episodes. Report Calmar ratio, Ulcer index, and current drawdown status.
Step 5: Factor decomposition — run factor model regression. Decompose total risk into systematic (factor) and idiosyncratic components. Identify the dominant factor exposures driving portfolio risk.
Step 6: Stress testing — apply at least 3 historical stress scenarios and 3 hypothetical scenarios. For each: P&L impact, VaR comparison, and which positions contribute most to stress loss.
Step 7: Risk report — write a 1-page risk summary: current risk level vs target, factor exposures of concern, tail risk assessment, liquidity profile, and top 3 risk management recommendations. Copy prompt View page Show more ↓ Risk and Portfolio Analytics Advanced Prompt 03 
### Liquidity Risk Assessment 
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

Return: per-position liquidity metrics, portfolio liquidity distribution, market impact estimates, forced liquidation analysis, and liquidity stress test results. Copy prompt View page Show more ↓ Risk and Portfolio Analytics Intermediate Prompt 04 
### Performance Attribution 
Decompose portfolio performance into its sources using Brinson-Hood-Beebower (BHB) attribution.

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

Return: BHB attribution table by segment, cumulative attribution plots, factor attribution, and information ratio analysis. Copy prompt View page Show more ↓ Risk and Portfolio Analytics Intermediate Prompt 05 
### Portfolio Optimization 
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

Return: efficient frontier plot, portfolio weights for each method, sensitivity analysis, walk-forward performance comparison. Copy prompt View page Show more ↓ Risk and Portfolio Analytics Advanced Prompt 06 
### Risk Parity Construction 
Construct and analyze a risk parity portfolio from this asset universe.

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

Return: risk parity weights with risk contribution verification, comparison table, sensitivity analysis, and backtest performance. Copy prompt View page Show more ↓ Risk and Portfolio Analytics Beginner Prompt 07 
### VaR and CVaR Calculation 
Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR) for this portfolio using multiple methods.

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

Return: VaR and CVaR table (method × confidence level), method comparison, scaling analysis, and backtesting results. Copy prompt View page Show more ↓ 
## Financial Data Analysis 
6 prompt s Financial Data Analysis Advanced Prompt 01 
### Alpha Signal Evaluation 
Rigorously evaluate the statistical and economic validity of this proposed alpha signal.

Signal description: {{signal_description}}
Signal data: {{signal_data}}
Universe: {{universe}}
Look-ahead period: {{horizon}}

1. Information coefficient (IC) analysis:
 IC = Spearman rank correlation(signal_t, return_{t+h})
 - Compute IC for each cross-section (each time period)
 - Mean IC: expected predictive power per period. IC > 0.05 is economically meaningful for daily signals.
 - IC standard deviation (ICSD): consistency of the signal
 - Information ratio of the signal: IC_mean / IC_std
 IR > 0.5: strong signal. IR > 1.0: exceptional.
 - % of periods with positive IC: > 55% indicates consistent directionality

2. IC decay analysis:
 - Compute IC at horizons h = 1, 5, 10, 21, 63, 126 trading days
 - Plot IC vs horizon: how quickly does predictive power decay?
 - The horizon where IC crosses zero defines the signal's natural holding period
 - Fast decay → short-term signal (high turnover). Slow decay → longer-term signal.

3. Quintile / decile portfolio analysis:
 - Each period: sort universe by signal into 5 (or 10) portfolios
 - Equal-weight each portfolio and compute forward returns
 - Report for each quintile: mean return, std, Sharpe, % periods positive
 - Key test: monotonic relationship from Q1 (low signal) to Q5 (high signal)?
 - Spread return: Q5 − Q1 long-short portfolio
 - Spread Sharpe ratio, drawdown, and turnover

4. Statistical significance testing:
 - t-test on mean IC: H₀: IC_mean = 0. Reject if |t| > 2.0.
 - Account for autocorrelation in IC series: Newey-West standard errors
 - Multiple testing concern: if this signal is one of many tested, apply Bonferroni or BHY correction
 - Bootstrap test: reshuffle signal vs returns 10,000 times and check if observed IC exceeds 95th percentile of null

5. Signal decay and overfitting checks:
 - In-sample vs out-of-sample IC: if in-sample IC >> out-of-sample IC, likely overfitting
 - Publication decay: has this signal's IC declined over time? (Sign of arbitrage)
 - Stability: does IC remain consistent across different market regimes?

6. Practical implementation costs:
 - Turnover rate of the long-short portfolio
 - Effective spread cost at current turnover: does signal survive round-trip transaction costs?
 - Break-even cost: max cost at which signal still generates positive net IC

Return: IC statistics table, IC decay plot, quintile return analysis, significance tests, overfitting checks, and net-of-cost IC estimate. Copy prompt View page Show more ↓ Financial Data Analysis Intermediate Prompt 02 
### Correlation Structure Analysis 
Analyze the correlation structure of this multi-asset portfolio and identify instabilities.

Assets: {{asset_list}}
Return frequency: {{frequency}}
Period: {{period}}

1. Static correlation matrix:
 - Compute Pearson correlation matrix
 - Visualize as heatmap with hierarchical clustering (assets with similar correlations grouped together)
 - Report the range: minimum and maximum pairwise correlations
 - Flag pairs with correlation > 0.9 (potential redundancy) and < -0.5 (potential hedge)

2. Robust correlation estimation:
 Pearson correlation is sensitive to outliers. Apply:
 - Spearman rank correlation: robust to outliers, captures monotonic relationships
 - Ledoit-Wolf shrinkage: regularized covariance matrix — critical for portfolio optimization with many assets
 - Minimum covariance determinant (MCD): downweights outliers automatically
 Compare: how much do robust estimates differ from Pearson for each pair?

3. Rolling correlation analysis:
 - 63-day rolling pairwise correlations for all pairs
 - Plot selected pairs over time
 - Identify correlation regime changes: periods when correlations were notably higher or lower
 - Crisis correlation: do correlations spike during market stress? (Diversification typically fails when needed most)

4. Principal Component Analysis (PCA):
 - Apply PCA to the correlation matrix
 - Report: variance explained by each PC (scree plot)
 - How many PCs explain 80% of variance? (Indicates effective dimensionality of the portfolio)
 - PC1 loadings: usually the 'market factor' — uniform positive loadings on all assets
 - PC2 onward: often sector or style tilts
 - Track PC1 explained variance over time: rising explained variance indicates increasing co-movement (correlation risk)

5. Instability metrics:
 - Correlation instability index: average change in pairwise correlations across rolling windows
 - Lowest-correlation period vs highest-correlation period: what drove the change?
 - Correlation between asset pairs during down markets vs up markets (asymmetric correlation)

6. Implications for portfolio construction:
 - Which correlations are most unstable? (Least reliable for diversification)
 - What is the maximum theoretical diversification benefit given current correlations?

Return: correlation matrix heatmap, Ledoit-Wolf estimate, rolling correlation plots, PCA results, instability metrics, and portfolio construction implications. Copy prompt View page Show more ↓ Financial Data Analysis Intermediate Prompt 03 
### Factor Exposure Analysis 
Analyze the factor exposures of this portfolio or asset using standard risk factor models.

Portfolio / asset: {{portfolio}}
Factor model: {{factor_model}} (Fama-French 3, Fama-French 5, Carhart 4, Barra, or custom factors)
Time period: {{period}}

1. Factor model regression:
 Run OLS regression of excess returns on factor returns:
 R_i - R_f = α + β₁F₁ + β₂F₂ + ... + βₙFₙ + ε

 For Fama-French 3-factor:
 R_i - R_f = α + β_MKT(R_M - R_f) + β_SMB(SMB) + β_HML(HML) + ε

 Report for each factor:
 - Beta (exposure): with 95% confidence interval
 - t-statistic and p-value
 - Economic significance: what does a 1-unit factor shock imply for portfolio return?

2. Alpha (Jensen's alpha):
 - Report α with standard error and t-statistic
 - Annualized alpha = daily_alpha × 252
 - Is alpha statistically significant (t > 2.0)? Is it economically meaningful?
 - Caveat: alpha depends heavily on which factors are included in the model

3. Model fit:
 - R² and Adjusted R²: what % of return variation is explained by the factors?
 - Information ratio: α / tracking_error (annualized)
 - Residual autocorrelation: Durbin-Watson test on residuals

4. Rolling factor exposures:
 - 252-day rolling betas for each factor
 - Plot over time: are exposures stable or do they drift significantly?
 - Significant beta drift may indicate strategy drift, market regime change, or reconstitution

5. Factor contribution to return:
 - Decompose total return into: factor contribution + alpha + unexplained
 - Factor contribution_i = β_i × Factor_return_i
 - Which factors contributed most positively and negatively over the period?

6. Residual analysis:
 - Is the idiosyncratic risk (residual std) large relative to systematic risk?
 - High idiosyncratic risk suggests security-specific risks not captured by the factor model

Return: factor exposure table with CIs, alpha analysis, R², rolling beta plots, return decomposition, and residual analysis. Copy prompt View page Show more ↓ Financial Data Analysis Beginner Prompt 04 
### Returns Data Profiling 
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

Return: summary statistics table, data quality flag list, distribution plots, autocorrelation results, and a data quality verdict (suitable for analysis / needs adjustment / not suitable). Copy prompt View page Show more ↓ Financial Data Analysis Advanced Prompt 05 
### Tail Risk Analysis 
Conduct a comprehensive tail risk analysis for this return series.

Portfolio or asset: {{portfolio}}
Return series: {{returns}}

1. Empirical tail analysis:
 - Left tail: distribution of returns below the 5th and 1st percentile
 - Right tail: distribution of returns above the 95th and 99th percentile
 - Tail asymmetry: is the left tail heavier than the right? (Typical for equity strategies)
 - Comparison to normal: at the 1% quantile, how does the empirical loss compare to the normal distribution prediction?

2. Extreme Value Theory (EVT) for tail estimation:
 Peaks Over Threshold (POT) method:
 - Choose threshold u at the 95th percentile of losses
 - Fit Generalized Pareto Distribution (GPD) to exceedances: F(x) = 1 - (1 + ξx/σ)^(-1/ξ)
 - Report: shape parameter ξ (> 0 = heavy tail, = 0 = exponential, < 0 = bounded tail), scale σ
 - ξ > 0.5 indicates very heavy tails — normal-based risk measures severely underestimate risk
 - Use GPD to estimate VaR and CVaR at extreme quantiles (99.9%) beyond the data

3. Maximum Drawdown analysis:
 - Maximum drawdown (MDD): largest peak-to-trough decline
 - Average drawdown
 - Drawdown duration distribution: how long do drawdowns last?
 - Recovery time distribution: how long does it take to recover to prior peak?
 - Calmar ratio: annualized return / |MDD|
 - Pain index: integral of drawdown curve over time

4. Tail correlation (co-tail risk):
 - For a multi-asset portfolio: does the portfolio tail loss exceed what uncorrelated risks would imply?
 - Tail dependence coefficient: probability that both assets suffer extreme losses simultaneously
 - Clayton copula for lower tail dependence: captures asymmetric dependence in down markets

5. Stress test scenarios:
 Apply historical stress scenarios:
 - 2008 financial crisis (Sept–Nov 2008)
 - COVID crash (Feb–Mar 2020)
 - 2020 interest rate spike (Q1 2022)
 - Dot-com crash (2000–2002)
 For each: what was the portfolio loss? How does it compare to VaR predictions?

6. Reporting:
 - At what loss level does your risk model break down? (Where does the normal approximation stop being conservative?)
 - What tail risk is not captured by standard VaR?

Return: empirical tail analysis, GPD parameter estimates, drawdown metrics, tail correlation analysis, stress test results, and risk model limitation statement. Copy prompt View page Show more ↓ Financial Data Analysis Intermediate Prompt 06 
### Volatility Regime Analysis 
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

Return: volatility estimator comparison, GARCH results, HMM regime probabilities, regime statistics table, and current regime assessment. Copy prompt View page Show more ↓ 
## Statistical and Econometric Methods 
6 prompt s Statistical and Econometric Methods Intermediate Prompt 01 
### Cointegration and Pairs Trading 
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

Return: cointegration test results, spread construction and statistics, OU parameter estimates, backtest performance, and stability analysis. Copy prompt View page Show more ↓ Statistical and Econometric Methods Intermediate Prompt 02 
### Cross-Sectional Regression 
Run and interpret a cross-sectional regression of asset returns on characteristics for factor research.

Universe: {{universe}} (N assets)
Dependent variable: {{horizon}}-day forward returns
Characteristics: {{characteristics}} (value, momentum, quality, size, etc.)
Period: {{period}}

1. Fama-MacBeth two-step procedure:
 This is the standard approach for cross-sectional factor research:

 Step 1 — Cross-sectional regressions (each period t):
 R_{i,t+h} = α_t + γ_{1,t} X_{1,i,t} + γ_{2,t} X_{2,i,t} + ... + ε_{i,t}
 Run this regression for each time period t → get a time series of γ_{k,t} for each characteristic k

 Step 2 — Time series inference:
 - Mean γ_k: average return premium for characteristic k
 - Std of γ_k: variation in premium over time
 - t-statistic: γ̄_k / (std_k / sqrt(T)) — adjust for autocorrelation with Newey-West
 - Reject H₀ (no premium) if |t| > 2.0; prefer t > 3.0 (Harvey et al. 2016) given multiple testing

2. Data preparation for cross-sectional regression:
 - Winsorize characteristics at 1st and 99th percentile: prevents extreme values from dominating
 - Rank-normalize characteristics: rank each characteristic within each cross-section, then scale to [-1, 1] or [0, 1]
 - Industry/sector neutralization: demean within each industry to remove sector bias
 - Standardize (z-score within each cross-section): ensures γ is interpretable as return per unit of normalized characteristic

3. Multi-characteristic regression:
 - Joint regression: controls for the correlation between characteristics
 - Standalone vs joint premium: a characteristic with a strong standalone premium may become insignificant after controlling for other characteristics (it was proxying for something else)
 - Check VIF: multicollinearity is common between related characteristics (value measures, for example)

4. Economic interpretation:
 - γ_k × 252 / h: annualized return premium for a 1-unit characteristic tilt
 - Economic significance: if γ_k is statistically significant but implies only 0.2% annualized premium, is it worth implementing?

5. Stability analysis:
 - Plot γ_{k,t} over time: is the premium stable or cyclical?
 - Pre-publication vs post-publication premium: has the premium decayed?
 - Bull vs bear market performance: does the premium hold in all market conditions?

Return: Fama-MacBeth regression table, Newey-West t-statistics, standalone vs joint premium comparison, premium stability plots. Copy prompt View page Show more ↓ Statistical and Econometric Methods Advanced Prompt 03 
### High-Frequency Data Analysis 
Analyze this high-frequency (intraday) financial data and estimate microstructure-aware statistics.

Data: {{hf_data}} (tick or bar data with timestamps, prices, volumes)
Frequency: {{frequency}} (tick, 1-second, 1-minute)

1. Data cleaning for HF data:
 - Remove pre-market and post-market trades if analyzing regular session
 - Remove trades outside the bid-ask spread (erroneous prints)
 - Remove trades flagged with conditions (correction, cancel, out-of-sequence)
 - Handle auction prices: opening and closing auctions have different microstructure
 - Timestamps: ensure microsecond timestamps are in the same timezone

2. Realized volatility estimation:
 - Realized variance: RV_t = Σ r²_{t,i} (sum of squared high-frequency returns)
 - Optimal sampling frequency: avoid microstructure noise (bid-ask bounce) at very high frequency
 - Signature plot: plot RV as a function of sampling frequency → select the frequency where RV stabilizes
 - Bias-Variance tradeoff: higher frequency → more observations but more noise
 - Two-Scale Realized Variance (TSRV): subsampling estimator robust to microstructure noise
 - Realized kernel estimator (Barndorff-Nielsen): state-of-the-art for noisy tick data

3. Bid-ask spread estimation:
 If only trade prices are available (no quote data):
 - Roll's implied spread: 2 × sqrt(-cov(ΔP_t, ΔP_{t-1}))
 Under the model: trades alternate between bid and ask, creating negative autocovariance
 - Corwin-Schultz estimator: uses daily high-low prices

4. Market impact and order flow:
 - Order imbalance: (buy volume - sell volume) / total volume
 - Order flow toxicity (VPIN): volume-synchronized probability of informed trading
 - Amihud illiquidity ratio at intraday frequency: |return| / dollar_volume_per_bar

5. Intraday seasonality:
 - Plot average volume by time of day: U-shaped pattern typical for equities (high at open and close)
 - Plot average volatility by time of day: similar U-shape
 - Normalize statistics for seasonality before strategy analysis

6. Jump detection:
 - Barndorff-Nielsen & Shephard (BNS) test: separates continuous volatility from jumps
 - Bipower variation: BV_t = (π/2) Σ |r_{t,i}| × |r_{t,i+1}| (robust to jumps)
 - Jump statistic: (RV - BV) / RV → fraction of total variance due to jumps
 - Detect individual jumps: flag returns exceeding 3σ_BV (jump threshold)

Return: data quality report, realized volatility estimates with signature plot, bid-ask spread estimates, intraday seasonality plots, and jump detection results. Copy prompt View page Show more ↓ Statistical and Econometric Methods Intermediate Prompt 04 
### Multiple Testing in Finance 
Address the multiple testing problem in this quantitative research context.

Research context: {{context}} (number of strategies tested, signals screened, parameters optimized)
Number of tests performed: {{n_tests}}

1. The multiple testing problem in finance:
 - With 100 independent tests at α = 0.05, expect 5 false positives by chance alone
 - Finance researchers test thousands of factors, strategies, and parameter combinations
 - Harvey, Liu, and Zhu (2016): with 315 published factors by 2012, the minimum t-statistic needed for significance should be 3.0, not 2.0
 - Most published factor premiums may be false discoveries

2. Family-wise error rate (FWER) corrections:
 Controls the probability of ANY false positive:

 Bonferroni correction:
 - α_adjusted = α / n_tests
 - For 100 tests at α = 0.05: α_adjusted = 0.0005 (t-stat ≈ 3.5 required)
 - Conservative: assumes all tests are independent (they rarely are)

 Holm-Bonferroni (step-down):
 - Less conservative than Bonferroni while still controlling FWER
 - Sort p-values: p(1) ≤ p(2) ≤ ... ≤ p(m)
 - Reject H(i) if p(i) ≤ α / (m - i + 1)

3. False Discovery Rate (FDR) corrections:
 Controls the expected proportion of false positives among rejections:
 More powerful than FWER methods when many tests are truly non-null.

 Benjamini-Hochberg (BH) procedure:
 - Sort p-values: p(1) ≤ p(2) ≤ ... ≤ p(m)
 - Find largest k such that p(k) ≤ (k/m) × q (target FDR = q, e.g. q = 0.10)
 - Reject all H(1) through H(k)
 - Appropriate when you have many tests and can tolerate some false positives

 Storey's q-value:
 - Adaptive FDR: estimates the proportion of true null hypotheses π₀ and adjusts
 - More powerful than BH when many tests are truly non-null

4. Bootstrap-based multiple testing:
 - White's Reality Check: tests whether the best-performing strategy outperforms after accounting for selection
 - Romano-Wolf stepdown procedure: controls FWER while being less conservative than Bonferroni
 - Procedure: permute returns to create null distribution of max performance statistics

5. Adjusting t-statistics for multiple comparisons:
 Following Harvey et al. (2016):
 - Minimum t-statistic for significance given M prior tests: t_min ≈ sqrt(log(M/2) × 2 × (1 + log(1/q)))
 - For M = 100, q = 0.05: t_min ≈ 3.0
 - For M = 1000, q = 0.05: t_min ≈ 3.5

6. Practical recommendations:
 - Pre-specify tests before looking at data
 - Report all tests performed, not just significant ones
 - Apply BH or Romano-Wolf correction to all reported results
 - Require t > 3.0 as a baseline for any factor claiming to be new

Return: adjusted p-values under each correction method, required t-statistics for significance, and multiple testing corrections applied to my specific results. Copy prompt View page Show more ↓ Statistical and Econometric Methods Advanced Prompt 05 
### Regime Detection and Switching 
Detect and model market regime switches in this financial time series.

Time series: {{time_series}}
Regime definition goal: {{goal}} (vol regimes, trend/mean-reversion, risk-on/risk-off, etc.)

1. Hidden Markov Model (HMM) regime detection:

 Specification for 2-state HMM:
 - State S_t ∈ {1, 2} (hidden, not directly observable)
 - Emission distribution: R_t | S_t = k ~ N(μ_k, σ²_k)
 - Transition matrix: P = [[p_{11}, p_{12}], [p_{21}, p_{22}]]
 p_{11} = P(stay in state 1 | currently in state 1)

 Estimation via EM algorithm (Baum-Welch):
 - Report: μ_1, σ_1, μ_2, σ_2, transition matrix P
 - Viterbi algorithm: most likely state sequence
 - Smoothed probabilities: P(S_t = k | all data) — softer than Viterbi

 Model selection:
 - 2 vs 3 states: compare BIC or AIC
 - 2-state typically: bull (high μ, low σ) and bear (low/negative μ, high σ)
 - 3-state may add: transition (moderate μ, rising σ)

2. Markov-Switching Regression:
 R_t = μ_{S_t} + φ_{S_t} R_{t-1} + ε_{S_t}
 - Different AR(1) coefficient in each regime
 - Captures mean-reversion in some regimes and momentum in others
 - Hamilton (1989) filter for real-time regime probability

3. Threshold and SETAR models:
 SETAR (Self-Exciting Threshold AR):
 - Regime is determined by whether a variable exceeds a threshold
 - R_t = α_1 + φ_1 R_{t-1} + ε_t if R_{t-d} ≤ threshold (regime 1)
 - R_t = α_2 + φ_2 R_{t-1} + ε_t if R_{t-d} > threshold (regime 2)
 - Self-exciting: the lagged return itself determines the regime
 - Suptest (Andrews) for the threshold location

4. Practical regime classification:
 Simple rule-based approach for transparency:
 - Regime = function of: trailing volatility, VIX level, credit spreads, or trend indicator
 - Pros: interpretable, auditable, does not require re-estimation
 - Cons: less statistically rigorous than HMM

5. Using regimes for portfolio management:
 - Regime-conditional strategy performance: does the alpha strategy perform differently across regimes?
 - Regime-conditional asset allocation: what is the historically optimal allocation in each regime?
 - Real-time regime probabilities: current P(S_t = bear) — use as a risk aversion dial
 - Transition probability: P(bear next month | bull this month) — forward-looking risk indicator

Return: HMM parameter estimates, smoothed regime probabilities, regime-conditional statistics, regime-conditional strategy performance, and current regime assessment. Copy prompt View page Show more ↓ Statistical and Econometric Methods Intermediate Prompt 06 
### Time Series Stationarity 
Test for stationarity in this financial time series and apply appropriate transformations.

Time series: {{time_series}} (price, spread, ratio, yield, etc.)

1. Why stationarity matters:
 Most statistical models assume stationarity — constant mean, variance, and autocorrelation structure over time. Non-stationary series cause spurious regressions: two unrelated trending series will appear correlated. In finance: prices are almost never stationary; returns usually are.

2. Visual inspection:
 - Plot the raw series: does it appear to trend or drift?
 - Plot the ACF: for a stationary series, ACF decays quickly to zero. For non-stationary, ACF decays slowly.
 - Plot first differences: does differencing remove the apparent trend?

3. Unit root tests:

 Augmented Dickey-Fuller (ADF) test:
 - H₀: series has a unit root (non-stationary)
 - H₁: series is stationary
 - Choose lag order: AIC or BIC criterion
 - Check critical values: ADF t-statistic vs MacKinnon critical values (-2.86 at 5% for no trend)
 - Reject H₀ (series is stationary) if ADF t-stat < critical value

 KPSS test (complementary):
 - H₀: series is stationary
 - H₁: series has a unit root
 - Use both ADF and KPSS: agreement strengthens the conclusion
 - ADF fails to reject + KPSS rejects → strong evidence for unit root
 - ADF rejects + KPSS fails to reject → strong evidence for stationarity

 Phillips-Perron (PP) test:
 - Non-parametric correction for autocorrelation and heteroscedasticity
 - More robust than ADF when errors are not i.i.d.

4. Handling non-stationarity:
 - Level I(1) series (random walk): take first differences → returns are stationary
 - Log transformation first: reduces heteroscedasticity and makes multiplicative effects additive
 - For spreads or ratios that should be mean-reverting: test stationarity of the spread directly
 - Trend stationarity (deterministic trend): detrend by regressing on time → residuals may be stationary

5. Cointegration (for multiple non-stationary series):
 - If two I(1) series are cointegrated, a linear combination is stationary
 - Engle-Granger test: run OLS, test residuals for unit root
 - Johansen test: allows testing for multiple cointegrating vectors
 - Implication: can model the long-run relationship even in non-stationary series

Return: ADF, KPSS, and PP test results, transformation recommendation, and ACF/PACF plots for the original and transformed series. Copy prompt View page Show more ↓ 
## Backtesting and Strategy Evaluation 
5 prompt s Backtesting and Strategy Evaluation Beginner Prompt 01 
### Backtest Bias Audit 
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

Return: bias audit table, estimated total bias impact on Sharpe ratio, and corrected performance estimate. Copy prompt View page Show more ↓ Backtesting and Strategy Evaluation Advanced Prompt 02 
### Overfitting Detection 
Detect and quantify overfitting in this quantitative strategy or model.

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

Return: DSR calculation, PSR, MinBTL, CPCV results, parameter sensitivity surface, and overfitting probability assessment. Copy prompt View page Show more ↓ Backtesting and Strategy Evaluation Advanced Prompt 03 
### Strategy Stress Testing 
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

Return: historical scenario table, hypothetical scenario analysis, worst-case statistics, sensitivity analysis, and crash risk profile. Copy prompt View page Show more ↓ Backtesting and Strategy Evaluation Intermediate Prompt 04 
### Transaction Cost Modeling 
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

Return: cost model for each component, annualized total cost estimate, net performance table at different cost levels, and break-even analysis. Copy prompt View page Show more ↓ Backtesting and Strategy Evaluation Intermediate Prompt 05 
### Walk-Forward Validation 
Design and execute a walk-forward validation framework to assess strategy robustness out-of-sample.

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

Return: walk-forward performance table (IS vs OOS per fold), concatenated OOS Sharpe and drawdown, parameter stability plots, and overfitting assessment. Copy prompt View page Show more ↓ 
## Quantitative Research Process 
3 prompt s Quantitative Research Process Intermediate Prompt 01 
### Alpha Research Framework 
Design a rigorous alpha research process for evaluating new investment signals.

Research question: {{hypothesis}} (e.g. 'Do stocks with improving earnings revision momentum outperform over the next month?')

1. Hypothesis formation (before looking at data):
 - State the economic intuition: WHY should this signal predict returns?
 - Risk premium explanation: investors demand compensation for bearing this risk
 - Behavioral explanation: systematic investor error that is exploitable
 - Structural explanation: market friction or institutional constraint creates opportunity
 - A signal without economic intuition is more likely to be a false positive
 - Write down the hypothesis before touching the data

2. Universe and data definition:
 - Define the asset universe: which assets, with what inclusion/exclusion criteria?
 - Define the signal: exactly how is it computed? What data inputs? What timing lag?
 - Data sources: where does each input come from? Is it point-in-time?
 - Survivorship bias: is the universe constructed using only assets that existed at each historical date?

3. Research protocol to prevent data snooping:
 - Split data into 3 periods BEFORE any analysis:
 - Training set (50%): hypothesis development, initial signal construction
 - Validation set (25%): parameter selection and signal refinement
 - Test set (25%): final evaluation ONCE, never used before the final test
 - Never look at the test set until the signal is fully specified
 - Document all analysis decisions and the order in which they were made

4. Signal evaluation hierarchy:
 Level 1: Statistical evidence
 - IC, ICIR, t-statistic (require t > 3.0 given prior testing in the field)
 - Quintile portfolio analysis: is the relationship monotonic?

 Level 2: Economic and institutional reality
 - Is the signal implementable? (Available in real time, not too slow to compute)
 - Survives transaction costs? (Net IC > 0 after realistic costs)
 - Capacity: at what AUM level does market impact eliminate the alpha?

 Level 3: Robustness
 - Consistent across time periods, market regimes, geographies?
 - Survives reasonable parameter perturbations?
 - Different from known factors? (Not just a proxy for value, momentum, or quality)

5. The research log:
 - Keep a contemporaneous log of every analysis run, its motivation, and its result
 - Include failed experiments: they constrain the hypothesis space for future work
 - This log is evidence against data snooping allegations

Return: hypothesis statement with economic rationale, data protocol, three-way split design, evaluation criteria, and research log template. Copy prompt View page Show more ↓ Quantitative Research Process Advanced Prompt 02 
### Factor Crowding Assessment 
Assess whether this factor or strategy is crowded and estimate the associated risks.

Factor / strategy: {{factor}}
Market data: {{data}}

1. Why crowding matters:
 A crowded trade occurs when many investors hold similar positions. When they simultaneously unwind — due to redemptions, losses, or regulatory changes — the factor experiences a 'crowding unwind': rapid, correlated losses that are NOT predicted by the factor's historical distribution.

2. Crowding metrics:

 Short interest approach:
 - For a long-short factor: are the 'short' securities heavily short-sold by many investors?
 - Short interest ratio: short_shares / average_daily_volume. High = potential crowding.
 - Change in short interest: rising short interest → increasing crowding

 Institutional ownership concentration:
 - Are the 'long' positions heavily owned by a similar set of quant funds?
 - 13-F filing analysis: overlap in top holdings across quant fund portfolios
 - High overlap = high crowding risk

 Return correlation with known crowded factors:
 - Regress the factor return on returns of known crowded strategies (AQR QMOM, etc.)
 - High correlation → this factor may be susceptible to the same crowding events

 Factor return autocorrelation:
 - Crowding can create short-term momentum in factor returns (everyone piling in)
 - Followed by sharp reversals when the crowd exits
 - Look for: negative autocorrelation at 1-week lag following periods of high positive autocorrelation

3. Crowding risk indicators to monitor:
 - Pairwise correlation among factor-long stocks (rising = crowding)
 - Volatility of factor returns (rising = crowding or unwind in progress)
 - Trading volume in factor-long stocks (spiking = potential unwind)
 - Factor drawdown relative to historical distribution (severe = possible crowding unwind)

4. Historical crowding unwind events:
 - Quant Quake (August 2007): quantitative equity strategies suffered simultaneous drawdowns due to forced deleveraging
 - The unwinding was rapid (3–5 days) and not explained by macro fundamentals
 - August 2007 style analysis: regress this factor's returns on the quant quake period — was it affected?

5. Portfolio implications:
 - Position size adjustment: reduce exposure to highly crowded factors
 - Diversification: ensure the portfolio's factor exposures are not all correlated with the same crowded strategies
 - Stop-loss policy: pre-define the drawdown level at which crowding unwind is suspected and exposure is reduced

Return: crowding metrics for each indicator, comparison to historical crowding events, monitoring dashboard specification, and portfolio adjustment recommendations. Copy prompt View page Show more ↓ Quantitative Research Process Advanced Chain 03 
### Full Quant Research Chain 
Step 1: Hypothesis — state the economic or behavioral rationale for why this signal should predict returns. Write it down before looking at any return data. What would falsify this hypothesis?
Step 2: Data protocol — define the asset universe with point-in-time construction, the signal computation with exact timing lags, the data sources, and the three-way train/validate/test split. Do not touch the test set.
Step 3: Signal construction and training set IC — compute the signal and evaluate IC, ICIR, and quintile performance on the training set only. If IC is not promising (ICIR < 0.3), return to Step 1 before proceeding.
Step 4: Parameter selection on validation set — select any free parameters (lookback windows, thresholds) on the validation set. Document the parameter search space and all results, not just the best.
Step 5: Multiple testing adjustment — apply Bonferroni or BHY correction given the number of hypotheses tested in your research program. Require t-statistic > 3.0 for a new signal to be considered genuine.
Step 6: Transaction cost and capacity analysis — estimate annualized turnover, total cost per unit of turnover, and net IC after costs. Estimate AUM capacity before market impact exceeds the gross alpha.
Step 7: Final evaluation on test set — evaluate the fully specified signal on the test set exactly once. Report all metrics: IC, ICIR, quintile spreads, net Sharpe. Compare to the validation results — large divergence suggests overfitting.
Step 8: Research report — write a complete research memo: hypothesis and rationale, data and methodology, training and validation results, multiple testing adjustments, transaction cost analysis, test set results, risks and limitations, and recommendation (implement / further research / reject). Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
