# Comparable Company Analysis *AI Prompt *

Build a comparable company analysis (Comps) to value this company. Subject company: {{subject_company}} Industry: {{industry}} Financials: {{financials}} 1. Select comparable co... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a comparable company analysis (Comps) to value this company.

Subject company: {{subject_company}}
Industry: {{industry}}
Financials: {{financials}}

1. Select comparable companies:
 Criteria for comp selection:
 - Same industry or sub-industry
 - Similar business model (not just SIC code)
 - Similar size: revenue within 0.3x to 3x of subject company
 - Similar growth profile: avoid comparing hypergrowth to mature companies
 - Similar geography if relevant
 Select 6-10 comparable companies. Exclude: companies under M&A processes, in bankruptcy, or with extraordinary items distorting multiples.

2. Compute trading multiples for each comp:
 Enterprise Value (EV) = Market Cap + Net Debt + Minority Interest + Preferred Stock

 EV-based multiples:
 - EV / Revenue (LTM and NTM)
 - EV / Gross Profit (LTM and NTM)
 - EV / EBITDA (LTM and NTM)
 - EV / EBIT (LTM)

 Equity-based multiples:
 - P/E (LTM and NTM)
 - Price / FCF (LTM)

3. Comps table statistics:
 For each multiple: Mean, Median, 25th percentile, 75th percentile
 Flag any outlier that distorts the mean.

4. Apply multiples to subject company:
 - Subject company LTM and NTM financial metrics
 - Implied EV at 25th percentile, median, and 75th percentile of each multiple
 - Equity value = EV - Net Debt
 - Per share value = Equity value / diluted shares

5. Football field chart:
 Show the implied value range from each multiple on a horizontal bar chart.
 Include DCF range for comparison.

6. Multiple selection rationale:
 - Which multiple is most relevant for this industry? (EV/EBITDA for industrials, EV/Revenue for high-growth SaaS, P/E for financials)
 - Does the subject company deserve a premium or discount to the median and why?

Return: comparable company table, multiples statistics, implied valuation ranges, football field chart description, and multiple selection rationale. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin valuation and transactions work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Valuation and Transactions or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Select comparable companies:, Same industry or sub-industry, Similar business model (not just SIC code). The final answer should stay clear, actionable, and easy to review inside a valuation and transactions workflow for financial analyst work. 

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

Once you have the first result, continue deeper with related prompts in Valuation and Transactions.
