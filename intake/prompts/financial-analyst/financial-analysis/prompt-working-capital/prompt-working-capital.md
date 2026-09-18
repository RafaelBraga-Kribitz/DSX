# Working Capital Analysis *AI Prompt *

Analyze the working capital dynamics and cash conversion efficiency of this business. Balance sheet and P&L data: {{financial_data}} Periods: {{periods}} Industry: {{industry}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the working capital dynamics and cash conversion efficiency of this business.

Balance sheet and P&L data: {{financial_data}}
Periods: {{periods}}
Industry: {{industry}}

1. Working capital components:
 Net Working Capital = Current Operating Assets - Current Operating Liabilities
 - Operating current assets: Accounts Receivable + Inventory + Prepaid Expenses
 - Operating current liabilities: Accounts Payable + Accrued Expenses + Deferred Revenue
 - Exclude: cash and short-term investments (financing items)

2. Days metrics (DSO, DIO, DPO):
 - DSO = AR / (Revenue / 365): how quickly do customers pay?
 - DIO = Inventory / (COGS / 365): how long does inventory sit?
 - DPO = AP / (COGS / 365): how long before we pay suppliers?
 - CCC = DSO + DIO - DPO: net days of cash tied up in operations
 A negative CCC (e.g. Amazon, Costco) means the business is funded by its customers.

3. Trend analysis:
 - Plot DSO, DIO, DPO, and CCC over {{periods}}
 - Is the CCC improving (shortening) or worsening (lengthening)?
 - Are individual components driving the change?

4. Cash impact of working capital changes:
 - Change in NWC = NWC(end) - NWC(beginning)
 - Positive change = use of cash, negative change = source of cash
 - If revenue is growing fast: working capital will likely consume cash even if days metrics are stable

5. Industry benchmark comparison:
 - DSO, DIO, DPO vs industry median
 - Which components are out of line? (High DSO suggests collection problems; low DPO may mean supplier leverage is low)

6. Optimization opportunities:
 - DSO reduction: invoicing process, early payment discounts, collections follow-up
 - DIO reduction: inventory management, just-in-time ordering
 - DPO extension: negotiate longer payment terms with suppliers
 - For each lever: estimate the one-time cash release from a 5-day improvement

Return: working capital table across periods, CCC calculation, benchmark comparison, cash impact analysis, and optimization opportunities with cash value estimates. 
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

The AI should return a structured result that covers the main requested outputs, such as Working capital components:, Operating current assets: Accounts Receivable + Inventory + Prepaid Expenses, Operating current liabilities: Accounts Payable + Accrued Expenses + Deferred Revenue. The final answer should stay clear, actionable, and easy to review inside a financial analysis workflow for financial analyst work. 

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
