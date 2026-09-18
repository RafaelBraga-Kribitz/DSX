# Forecasting *AI Prompts *

7 Data Analyst prompts in Forecasting. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts · 1 chain · 2 templates. 

## AI prompts in Forecasting 
7 prompts Advanced Template 01 
### Demand Forecast with External Factors 

Demand Forecast with External Factors is a advanced template for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Build a demand forecast that incorporates external factors:

1. Base model: fit a Prophet or ARIMA model on historical {{target_metric}} alone. Record baseline MAPE.
2. Add external regressors: {{external_factors}} (e.g. price, promotions, marketing spend, economic index). Fit a new model including these.
3. Compare accuracy: does adding external factors improve MAPE by more than 5%? If yes, use the richer model.
4. Identify which external factor has the highest predictive power (use feature importance or correlation with residuals)
5. Generate a {{forecast_horizon}}-day forecast with three scenarios: optimistic, base, pessimistic — varying the {{key_lever}} assumption.

Return: accuracy comparison table, feature importance chart, and the 3-scenario forecast plot. Copy prompt Open prompt details Advanced Chain 02 
### Full Forecast Benchmark Chain 

Full Forecast Benchmark Chain is a advanced chain for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Step 1: Decompose the time series using STL decomposition. Identify and plot trend, seasonality, and residual components. Note the dominant seasonality period.
Step 2: Test for stationarity using the ADF test. If non-stationary, apply first differencing or log transformation and retest.
Step 3: Train three competing models on the first 80% of the data: (a) ARIMA with auto-selected p,d,q parameters, (b) Facebook Prophet with default settings, (c) Exponential Smoothing (Holt-Winters).
Step 4: Evaluate all three models on the held-out 20% test window. Report MAPE, RMSE, and MAE for each. Declare a winner.
Step 5: Use the winning model to generate a {{forecast_horizon}}-day forecast. Include 80% and 95% confidence intervals. Plot forecast vs actuals.
Step 6: Write a one-paragraph forecast commentary: expected trend, key risks, seasonality effects to watch for, and the confidence level in this forecast. Copy prompt Open prompt details Intermediate Single prompt 03 
### Growth Rate Analysis 

Growth Rate Analysis is a intermediate prompt for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Calculate and analyze growth rates for the primary metric in this dataset:

1. Compute week-over-week (WoW), month-over-month (MoM), and year-over-year (YoY) growth rates for each time period
2. Plot all three growth rate series on a single chart with a zero reference line
3. Identify the periods of fastest and slowest growth
4. Calculate whether growth is accelerating or decelerating — fit a trend to the MoM growth rate itself
5. Compare growth rates across segments if a segment column exists
6. Project where the metric will be in 90 days if the current growth trajectory continues unchanged

Return a growth rate table and a plain-English summary: is the business growing faster or slower than before, and is the trend improving or deteriorating? Copy prompt Open prompt details Intermediate Single prompt 04 
### Prophet Forecast with Seasonality 

Prophet Forecast with Seasonality is a intermediate prompt for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Build a time series forecast using Facebook Prophet on this dataset.

1. Prepare the data: rename the date column to 'ds' and the target column to 'y'
2. Configure Prophet with:
 - Yearly seasonality: auto-detect
 - Weekly seasonality: enabled if data frequency is daily
 - Country holidays: {{country_code}} if applicable
3. Split: use the last 20% of data as a test set
4. Fit the model on the training set and evaluate on the test set: report MAPE, MAE, and RMSE
5. Generate a forecast for the next {{forecast_horizon}} days with 80% and 95% uncertainty intervals
6. Plot: actual vs forecast, trend component, and seasonality components separately Copy prompt Open prompt details Intermediate Template 05 
### Scenario Planning Forecast 

Scenario Planning Forecast is a intermediate template for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Generate a 3-scenario forecast for {{metric}} over the next {{forecast_horizon}}:

Scenario definitions:
- Pessimistic: assume {{pessimistic_assumption}} (e.g. growth slows to half the current rate, churn increases by 20%)
- Base case: continue current trend with normal seasonality
- Optimistic: assume {{optimistic_assumption}} (e.g. growth accelerates by 50%, a new product launch captures additional market)

For each scenario:
- Plot the forecast line with a distinct color
- Show the projected value at 30, 60, and 90 days
- State the key assumption driving each scenario

Highlight the range between pessimistic and optimistic as a shaded uncertainty band.
Add a plain-English paragraph explaining what would need to be true for the optimistic scenario to materialize. Copy prompt Open prompt details Intermediate Single prompt 06 
### Seasonality Decomposition 

Seasonality Decomposition is a intermediate prompt for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Decompose this time series to understand its underlying components:

1. Apply STL (Seasonal-Trend decomposition using LOESS) to separate the series into trend, seasonality, and residual components
2. Plot all three components with the original series
3. Quantify the strength of the seasonal component: what percentage of variance does it explain?
4. Identify the dominant seasonality period (daily, weekly, monthly, annual)
5. Check the residual component — does it look like white noise or does it contain unexplained structure?
6. Describe in plain English: what is the underlying growth trend, what is the seasonal pattern, and are there any unusual residuals that need investigation? Copy prompt Open prompt details Beginner Single prompt 07 
### Trend Projection 

Trend Projection is a beginner prompt for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Project the future trend of the primary metric in this dataset.

1. Fit both a linear and a polynomial (degree 2) trend line. Compare R² values — which fits better?
2. Calculate the compound growth rate (CAGR) over the full observed period
3. Project the metric 30, 60, and 90 days into the future using the better-fitting model
4. Check for seasonal patterns and, if found, describe how they affect the projection
5. State the 3 key assumptions behind this forecast and one external factor that could invalidate it Copy prompt Open prompt details 
## Recommended Forecasting workflow 
1 
### Demand Forecast with External Factors 

Start with a focused prompt in Forecasting so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Full Forecast Benchmark Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Growth Rate Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Prophet Forecast with Seasonality 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
