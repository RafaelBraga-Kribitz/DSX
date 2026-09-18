# Statistical and Econometric Methods *AI Prompts *

6 Quantitative Analyst prompts in Statistical and Econometric Methods. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 6 single prompts. 

## AI prompts in Statistical and Econometric Methods 
6 prompts Intermediate Single prompt 01 
### Cointegration and Pairs Trading 

Test for cointegration between two assets and build a pairs trading model. Asset 1: {{asset_1}} Asset 2: {{asset_2}} Price series: {{price_series}} 1. Cointegration testing: Eng... 
Prompt text Test for cointegration between two assets and build a pairs trading model.

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

Return: cointegration test results, spread construction and statistics, OU parameter estimates, backtest performance, and stability analysis. Copy prompt Open prompt details Intermediate Single prompt 02 
### Cross-Sectional Regression 

Run and interpret a cross-sectional regression of asset returns on characteristics for factor research. Universe: {{universe}} (N assets) Dependent variable: {{horizon}}-day for... 
Prompt text Run and interpret a cross-sectional regression of asset returns on characteristics for factor research.

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

Return: Fama-MacBeth regression table, Newey-West t-statistics, standalone vs joint premium comparison, premium stability plots. Copy prompt Open prompt details Advanced Single prompt 03 
### High-Frequency Data Analysis 

Analyze this high-frequency (intraday) financial data and estimate microstructure-aware statistics. Data: {{hf_data}} (tick or bar data with timestamps, prices, volumes) Frequen... 
Prompt text Analyze this high-frequency (intraday) financial data and estimate microstructure-aware statistics.

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

Return: data quality report, realized volatility estimates with signature plot, bid-ask spread estimates, intraday seasonality plots, and jump detection results. Copy prompt Open prompt details Intermediate Single prompt 04 
### Multiple Testing in Finance 

Address the multiple testing problem in this quantitative research context. Research context: {{context}} (number of strategies tested, signals screened, parameters optimized) N... 
Prompt text Address the multiple testing problem in this quantitative research context.

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

Return: adjusted p-values under each correction method, required t-statistics for significance, and multiple testing corrections applied to my specific results. Copy prompt Open prompt details Advanced Single prompt 05 
### Regime Detection and Switching 

Detect and model market regime switches in this financial time series. Time series: {{time_series}} Regime definition goal: {{goal}} (vol regimes, trend/mean-reversion, risk-on/... 
Prompt text Detect and model market regime switches in this financial time series.

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

Return: HMM parameter estimates, smoothed regime probabilities, regime-conditional statistics, regime-conditional strategy performance, and current regime assessment. Copy prompt Open prompt details Intermediate Single prompt 06 
### Time Series Stationarity 

Test for stationarity in this financial time series and apply appropriate transformations. Time series: {{time_series}} (price, spread, ratio, yield, etc.) 1. Why stationarity m... 
Prompt text Test for stationarity in this financial time series and apply appropriate transformations.

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

Return: ADF, KPSS, and PP test results, transformation recommendation, and ACF/PACF plots for the original and transformed series. Copy prompt Open prompt details 
## Recommended Statistical and Econometric Methods workflow 
1 
### Cointegration and Pairs Trading 

Start with a focused prompt in Statistical and Econometric Methods so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Cross-Sectional Regression 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### High-Frequency Data Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Multiple Testing in Finance 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
