# Three-Statement Model Audit *AI Prompt *

Audit this three-statement financial model (Income Statement, Balance Sheet, Cash Flow Statement) for errors and best practices. Model description: {{model_description}} 1. Bala... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit this three-statement financial model (Income Statement, Balance Sheet, Cash Flow Statement) for errors and best practices.

Model description: {{model_description}}

1. Balance sheet balance check:
 - Total Assets = Total Liabilities + Total Equity in every period?
 - If not: identify which line items are likely causing the imbalance

2. Cash flow statement reconciliation:
 - Net income (IS) flows to operating activities (CFS)?
 - Depreciation and amortization is added back in operating activities?
 - Changes in working capital are reflected correctly (increase in current assets = use of cash)?
 - Ending cash (CFS) = Cash line on Balance Sheet for every period?

3. Common modeling errors to check:
 - Circular references: does the model contain circularity (interest expense depends on debt, debt depends on revolver, revolver depends on cash)? Flag and note the resolution method.
 - Hard-coded values in formula cells: all assumptions should be in a dedicated inputs section, not embedded in formulas
 - Inconsistent time periods: are all statements on the same fiscal year/quarter basis?
 - Incorrect sign conventions: revenue positive, costs negative (or vice versa consistently)
 - Missing plug: every balance sheet needs a balancing plug (typically revolver draws or cash sweep)

4. Assumption documentation:
 - Are all key assumptions clearly labeled with their source?
 - Are growth rates, margins, and working capital ratios clearly separated from formulas?
 - Is there a sensitivity table for the most important assumptions?

5. Structural best practices:
 - Color coding: inputs (blue), formulas (black), links from other sheets (green)
 - No merged cells in data areas
 - Row and column headers on every sheet
 - Print-ready formatting: fits on one page per statement per period

Return: error list with severity and location, reconciliation check results, and a model quality score (0-100) with justification. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin financial modeling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Financial Modeling or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Balance sheet balance check:, Total Assets = Total Liabilities + Total Equity in every period?, If not: identify which line items are likely causing the imbalance. The final answer should stay clear, actionable, and easy to review inside a financial modeling workflow for financial analyst work. 

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

Once you have the first result, continue deeper with related prompts in Financial Modeling.
