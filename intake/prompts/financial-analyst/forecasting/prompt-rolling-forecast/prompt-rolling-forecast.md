# Rolling Forecast Design *AI Prompt *

Design and build a rolling forecast process to replace or supplement the annual budget. Company context: {{company_context}} Forecast horizon: {{horizon}} quarters ahead (always... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and build a rolling forecast process to replace or supplement the annual budget.

Company context: {{company_context}}
Forecast horizon: {{horizon}} quarters ahead (always maintained)
Update frequency: {{frequency}} (monthly or quarterly)

1. Rolling forecast architecture:
 - Horizon: always maintain {{horizon}} quarters forward regardless of fiscal year
 - Lock periods: actuals replace forecast as months close
 - Driver-based: forecast built from business drivers, not top-down targets
 Revenue = {{driver_1}} x {{driver_2}} (not 'last year + 10%')

2. Key drivers to forecast:
 Identify the 5-8 leading indicators that drive financial results:
 - Revenue drivers: new customer count, pipeline conversion rate, average deal size, renewal rate
 - Cost drivers: headcount plan, average cost per hire, usage-based costs, inflation
 - Working capital drivers: DSO, DPO, inventory turns
 For each driver: who owns the forecast input? What is the data source?

3. Forecast submission workflow:
 - Week 1: close actuals and update models
 - Week 2: business unit managers submit driver updates
 - Week 3: FP&A consolidates and runs scenarios
 - Week 4: review with senior leadership, finalize

4. Rolling forecast vs budget comparison:
 Rather than budget vs actual, track:
 - Forecast vs actual (how accurate was the rolling forecast?)
 - Forecast revision history: is the forecast converging or diverging as we approach the period?
 - Bias analysis: is the team consistently optimistic or pessimistic?

5. Accuracy tracking:
 - MAPE (Mean Absolute Percentage Error) per forecast vintage and per line item
 - Target: < 5% MAPE for 1-quarter-ahead forecast
 - Which business units have the least accurate forecasts? (Requires coaching or process improvement)

Return: rolling forecast architecture, driver identification worksheet, submission workflow calendar, accuracy tracking framework, and comparison to annual budget approach. 
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

The AI should return a structured result that covers the main requested outputs, such as Rolling forecast architecture:, Horizon: always maintain {{horizon}} quarters forward regardless of fiscal year, Lock periods: actuals replace forecast as months close. The final answer should stay clear, actionable, and easy to review inside a forecasting workflow for financial analyst work. 

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
