# Full Forecast Benchmark Chain *AI Prompt *

Full Forecast Benchmark Chain is a advanced chain for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Decompose the time series using STL decomposition. Identify and plot trend, seasonality, and residual components. Note the dominant seasonality period.
Step 2: Test for stationarity using the ADF test. If non-stationary, apply first differencing or log transformation and retest.
Step 3: Train three competing models on the first 80% of the data: (a) ARIMA with auto-selected p,d,q parameters, (b) Facebook Prophet with default settings, (c) Exponential Smoothing (Holt-Winters).
Step 4: Evaluate all three models on the held-out 20% test window. Report MAPE, RMSE, and MAE for each. Declare a winner.
Step 5: Use the winning model to generate a {{forecast_horizon}}-day forecast. Include 80% and 95% confidence intervals. Plot forecast vs actuals.
Step 6: Write a one-paragraph forecast commentary: expected trend, key risks, seasonality effects to watch for, and the confidence level in this forecast. 
```

## When to use this prompt 
Use case 01 
When you need to estimate future values for a key metric. 
Use case 02 
When planning targets, capacity, budgets, or scenario ranges. 
Use case 03 
When comparing simple and advanced forecasting approaches on the same data. 
Use case 04 
When you need forecast assumptions, uncertainty, and commentary alongside the numbers. 

## What the AI should return 

The AI should return forecast outputs in a structured format that includes method, assumptions, projected values, and a short interpretation of the trend. It should compare models or scenarios when requested, and include accuracy metrics or uncertainty intervals where possible. Charts and tables should support the explanation rather than replace it. The final answer should help the user understand both the forecast itself and how much confidence to place in it. 

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
