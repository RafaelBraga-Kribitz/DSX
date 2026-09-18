# Cash Flow Analysis *AI Prompt *

Analyze the cash flow quality and sustainability of this business. Cash flow statement: {{cash_flow_data}} Periods: {{periods}} 1. Cash flow waterfall: EBITDA - Interest paid -... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the cash flow quality and sustainability of this business.

Cash flow statement: {{cash_flow_data}}
Periods: {{periods}}

1. Cash flow waterfall:
 EBITDA
 - Interest paid
 - Taxes paid
 - Capex
 - Change in working capital
 = Free Cash Flow (FCF)

 FCF to equity = FCF - Debt repayments + New borrowings
 Show the waterfall for each period.

2. Cash conversion quality:
 - FCF conversion: FCF / Net Income (target > 80% for high-quality earnings)
 - If FCF < Net Income: accrual accounting is inflating net income (working capital build, non-cash charges)
 - EBITDA to cash conversion: FCF / EBITDA
 - Recurring FCF: strip out one-time items and non-recurring capex

3. Capex analysis:
 - Maintenance capex vs growth capex: what portion is necessary to maintain the asset base?
 - Capex / Revenue %: trending up or down?
 - Capex / Depreciation: ratio < 1 may indicate underinvestment

4. Working capital cash consumption:
 - Is working capital consuming cash as the business grows?
 - For each $1 of revenue growth: how many cents of working capital investment are required?

5. Liquidity and sustainability:
 - Cash runway: current cash / monthly net cash burn
 - Debt service coverage: FCF / (Interest + Required debt amortization)
 - At current FCF: how many years to pay off net debt?

6. Red flags in cash flow:
 - Growing receivables outpacing revenue (customers paying slower or revenue recognition issues)
 - Capex consistently below depreciation (asset base deteriorating)
 - Significant gap between net income and OCF (earnings quality concern)
 - Negative FCF with no clear path to positive (sustainability concern)

Return: cash flow waterfall table, conversion metrics, capex analysis, working capital cash impact, liquidity assessment, and red flag identification. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin financial analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Financial Analysis or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Cash flow waterfall:, Interest paid, Taxes paid. The final answer should stay clear, actionable, and easy to review inside a financial analysis workflow for financial analyst work. 

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

Once you have the first result, continue deeper with related prompts in Financial Analysis.
