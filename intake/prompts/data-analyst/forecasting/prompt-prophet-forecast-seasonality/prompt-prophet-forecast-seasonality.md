# Prophet Forecast with Seasonality *AI Prompt *

Prophet Forecast with Seasonality is a intermediate prompt for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a time series forecast using Facebook Prophet on this dataset.

1. Prepare the data: rename the date column to 'ds' and the target column to 'y'
2. Configure Prophet with:
 - Yearly seasonality: auto-detect
 - Weekly seasonality: enabled if data frequency is daily
 - Country holidays: {{country_code}} if applicable
3. Split: use the last 20% of data as a test set
4. Fit the model on the training set and evaluate on the test set: report MAPE, MAE, and RMSE
5. Generate a forecast for the next {{forecast_horizon}} days with 80% and 95% uncertainty intervals
6. Plot: actual vs forecast, trend component, and seasonality components separately 
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
