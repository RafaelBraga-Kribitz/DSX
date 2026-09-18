# Precedent Transaction Analysis *AI Prompt *

Build a precedent transaction analysis to establish acquisition valuation benchmarks. Subject company / target profile: {{target_profile}} Industry: {{industry}} Transaction dat... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a precedent transaction analysis to establish acquisition valuation benchmarks.

Subject company / target profile: {{target_profile}}
Industry: {{industry}}
Transaction data available: {{transaction_data}}

1. Transaction selection criteria:
 - Same industry as target
 - Completed M&A transactions (not rumors or cancelled deals)
 - Comparable deal structure (acquisition of control)
 - Time relevance: weight recent transactions more (last 5 years preferred, last 10 years for reference)
 - Size comparability: deal value within 0.2x to 5x of expected deal size
 Exclude: distressed/bankruptcy sales, minority investments, transactions with no disclosed financials

2. Transaction multiple computation:
 For each transaction:
 - Transaction EV = equity consideration + assumed debt + minority interest
 - EV / LTM Revenue (at time of announcement)
 - EV / LTM EBITDA
 - EV / LTM EBIT
 - Premium to unaffected share price (% above 30-day pre-announcement price)

3. Control premium analysis:
 - Transactions typically include a control premium over public market trading values
 - Average acquisition premium in this industry over comparable period
 - Implied control premium vs current trading multiples of comparable public companies

4. Transaction multiple statistics:
 - Mean, median, 25th percentile, 75th percentile for each multiple
 - Note: transaction multiples are typically higher than trading multiples (control premium)

5. Apply to subject company:
 - Implied EV range at 25th/median/75th percentile transaction multiples
 - Equity value range after adjusting for net debt

6. Key transaction details to note:
 - Any strategic rationale that drove premium multiples (synergies, competitive bid)
 - Any discounts due to distress, minority positions, or transition risk

Return: transaction comps table, control premium analysis, implied valuation ranges, and key deal notes affecting multiple selection. 
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

The AI should return a structured result that covers the main requested outputs, such as Transaction selection criteria:, Same industry as target, Completed M&A transactions (not rumors or cancelled deals). The final answer should stay clear, actionable, and easy to review inside a valuation and transactions workflow for financial analyst work. 

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
