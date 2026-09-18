# Budget vs Actual Variance Analysis *AI Prompt *

Analyze the variance between budget and actual results for this period. Budget data: {{budget}} Actual data: {{actuals}} Period: {{period}} 1. Variance calculation: For each P&L... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the variance between budget and actual results for this period.

Budget data: {{budget}}
Actual data: {{actuals}}
Period: {{period}}

1. Variance calculation:
 For each P&L line item:
 - Budget amount
 - Actual amount
 - Absolute variance: Actual - Budget
 - Percentage variance: (Actual - Budget) / |Budget| x 100%
 - Favorable (F) or Unfavorable (U): revenue above budget = F, cost above budget = U

2. Materiality threshold:
 - Define materiality: variances > {{threshold}}% or > ${{amount}} warrant explanation
 - Flag all variances exceeding the threshold

3. Revenue variance decomposition:
 Total Revenue Variance = Volume Variance + Price/Mix Variance
 - Volume variance: (Actual Volume - Budget Volume) x Budget Price
 - Price variance: (Actual Price - Budget Price) x Actual Volume
 - Mix variance: if applicable (multiple products/services)

4. Cost variance decomposition:
 Total Cost Variance = Volume Variance + Efficiency Variance + Rate Variance
 - Volume variance: expected cost at actual volume - budget cost
 - Efficiency variance: actual hours/units x budget rate - expected at actual volume
 - Rate variance: (Actual Rate - Budget Rate) x Actual hours/units

5. Root cause narrative:
 For the top 5 variances by magnitude:
 - Explain what drove the variance
 - Is it a one-time item or ongoing?
 - Is it within the business's control?
 - What is the forecast impact for the rest of the year?

6. Year-to-date and full-year implications:
 - YTD variance as % of full-year budget
 - Updated full-year forecast based on current run rate

Return: variance table with F/U flags, decomposed revenue and cost variances, root cause narratives, and updated full-year forecast. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin variance analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Variance Analysis or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Variance calculation:, Budget amount, Actual amount. The final answer should stay clear, actionable, and easy to review inside a variance analysis workflow for financial analyst work. 

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

Once you have the first result, continue deeper with related prompts in Variance Analysis.
