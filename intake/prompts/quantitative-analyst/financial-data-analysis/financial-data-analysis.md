# Financial Data Analysis *AI Prompts *

6 Quantitative Analyst prompts in Financial Data Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts. 

## AI prompts in Financial Data Analysis 
6 prompts Advanced Single prompt 01 
### Alpha Signal Evaluation 

Rigorously evaluate the statistical and economic validity of this proposed alpha signal. Signal description: {{signal_description}} Signal data: {{signal_data}} Universe: {{univ... 
Prompt text Rigorously evaluate the statistical and economic validity of this proposed alpha signal.

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

Return: IC statistics table, IC decay plot, quintile return analysis, significance tests, overfitting checks, and net-of-cost IC estimate. Copy prompt Open prompt details Intermediate Single prompt 02 
### Correlation Structure Analysis 

Analyze the correlation structure of this multi-asset portfolio and identify instabilities. Assets: {{asset_list}} Return frequency: {{frequency}} Period: {{period}} 1. Static c... 
Prompt text Analyze the correlation structure of this multi-asset portfolio and identify instabilities.

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

Return: correlation matrix heatmap, Ledoit-Wolf estimate, rolling correlation plots, PCA results, instability metrics, and portfolio construction implications. Copy prompt Open prompt details Intermediate Single prompt 03 
### Factor Exposure Analysis 

Analyze the factor exposures of this portfolio or asset using standard risk factor models. Portfolio / asset: {{portfolio}} Factor model: {{factor_model}} (Fama-French 3, Fama-F... 
Prompt text Analyze the factor exposures of this portfolio or asset using standard risk factor models.

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

Return: factor exposure table with CIs, alpha analysis, R², rolling beta plots, return decomposition, and residual analysis. Copy prompt Open prompt details Beginner Single prompt 04 
### Returns Data Profiling 

Profile this financial returns dataset and identify any data quality issues before analysis. Asset class: {{asset_class}} Frequency: {{frequency}} (daily, weekly, monthly) Date... 
Prompt text Profile this financial returns dataset and identify any data quality issues before analysis.

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

Return: summary statistics table, data quality flag list, distribution plots, autocorrelation results, and a data quality verdict (suitable for analysis / needs adjustment / not suitable). Copy prompt Open prompt details Advanced Single prompt 05 
### Tail Risk Analysis 

Conduct a comprehensive tail risk analysis for this return series. Portfolio or asset: {{portfolio}} Return series: {{returns}} 1. Empirical tail analysis: - Left tail: distribu... 
Prompt text Conduct a comprehensive tail risk analysis for this return series.

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

Return: empirical tail analysis, GPD parameter estimates, drawdown metrics, tail correlation analysis, stress test results, and risk model limitation statement. Copy prompt Open prompt details Intermediate Single prompt 06 
### Volatility Regime Analysis 

Analyze volatility regimes in this return series and build a regime classification model. Asset / index: {{asset}} Return series: {{returns}} 1. Realized volatility estimation m... 
Prompt text Analyze volatility regimes in this return series and build a regime classification model.

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

Return: volatility estimator comparison, GARCH results, HMM regime probabilities, regime statistics table, and current regime assessment. Copy prompt Open prompt details 
## Recommended Financial Data Analysis workflow 
1 
### Alpha Signal Evaluation 

Start with a focused prompt in Financial Data Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Correlation Structure Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Factor Exposure Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Returns Data Profiling 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
