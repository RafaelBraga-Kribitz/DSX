# Demand Forecast with External Factors *AI Prompt *

Demand Forecast with External Factors is a advanced template for forecasting. This prompt focuses on projecting future outcomes based on historical patterns in the data. It guides the AI to compare methods, state assumptions, and present forecasts with appropriate context and uncertainty. Use it when you need forward-looking estimates for planning, monitoring, or scenario analysis. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a demand forecast that incorporates external factors:

1. Base model: fit a Prophet or ARIMA model on historical {{target_metric}} alone. Record baseline MAPE.
2. Add external regressors: {{external_factors}} (e.g. price, promotions, marketing spend, economic index). Fit a new model including these.
3. Compare accuracy: does adding external factors improve MAPE by more than 5%? If yes, use the richer model.
4. Identify which external factor has the highest predictive power (use feature importance or correlation with residuals)
5. Generate a {{forecast_horizon}}-day forecast with three scenarios: optimistic, base, pessimistic — varying the {{key_lever}} assumption.

Return: accuracy comparison table, feature importance chart, and the 3-scenario forecast plot. 
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
