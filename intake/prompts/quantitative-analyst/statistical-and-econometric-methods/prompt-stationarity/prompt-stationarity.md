# Time Series Stationarity *AI Prompt *

Test for stationarity in this financial time series and apply appropriate transformations. Time series: {{time_series}} (price, spread, ratio, yield, etc.) 1. Why stationarity m... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: ADF, KPSS, and PP test results, transformation recommendation, and ACF/PACF plots for the original and transformed series. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical and econometric methods work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical and Econometric Methods or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why stationarity matters:, Visual inspection:, Plot the raw series: does it appear to trend or drift?. The final answer should stay clear, actionable, and easy to review inside a statistical and econometric methods workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Statistical and Econometric Methods.
