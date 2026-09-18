# Time Series Revenue Forecasting *AI Prompt *

Build a statistical time series forecast for this revenue or financial metric. Metric: {{metric}} Historical data: {{data}} (at least 24 periods) Forecast horizon: {{horizon}} p... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a statistical time series forecast for this revenue or financial metric.

Metric: {{metric}}
Historical data: {{data}} (at least 24 periods)
Forecast horizon: {{horizon}} periods
Seasonality: {{seasonality}} (yes/no, and period: weekly/monthly/quarterly)

1. Exploratory analysis:
 - Plot the series: trend, seasonality, and irregular components visible?
 - Decompose using STL or classical decomposition: trend + seasonal + residual
 - Autocorrelation function (ACF) and Partial ACF (PACF): identify autoregressive and moving average structure
 - ADF test: is the series stationary? If not, difference and retest.

2. Model candidates:

 Holt-Winters (ETS):
 - Triple exponential smoothing: handles trend and seasonality
 - Parameters: alpha (level), beta (trend), gamma (seasonality)
 - Best for: smooth trends with regular seasonality, limited data (< 5 years)

 SARIMA:
 - Seasonal ARIMA (p,d,q)(P,D,Q)[m]
 - Select parameters using auto.arima (AIC/BIC minimization)
 - Best for: data with complex autocorrelation structure

 Prophet (Facebook/Meta):
 - Handles multiple seasonalities, holiday effects, and trend changepoints
 - Best for: monthly or daily data with irregular events and holidays

3. Model evaluation:
 - Split data: train on first 80%, test on last 20%
 - Metrics: MAPE, MAE, RMSE on the test set
 - Select the model with lowest MAPE on holdout

4. Forecast output:
 - Point forecast for each future period
 - 80% and 95% prediction intervals
 - Is the interval width reasonable given the metric's historical variance?

5. Forecast decomposition:
 - How much of the forecast is trend vs seasonal vs baseline?
 - What is the year-over-year growth implied by the forecast?

Return: model comparison table, selected model diagnostics, forecast with prediction intervals, and decomposition of forecast components. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin forecasting work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Forecasting or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Exploratory analysis:, Plot the series: trend, seasonality, and irregular components visible?, Decompose using STL or classical decomposition: trend + seasonal + residual. The final answer should stay clear, actionable, and easy to review inside a forecasting workflow for financial analyst work. 

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

Once you have the first result, continue deeper with related prompts in Forecasting.
