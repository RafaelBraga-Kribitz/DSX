# LBO Model Framework *AI Prompt *

Build a leveraged buyout (LBO) model framework for evaluating this acquisition. Target company: {{target}} Financials: {{financials}} Entry assumptions: {{entry_assumptions}} Ho... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a leveraged buyout (LBO) model framework for evaluating this acquisition.

Target company: {{target}}
Financials: {{financials}}
Entry assumptions: {{entry_assumptions}}
Holding period: {{holding_period}} years

1. Sources and Uses of Funds:
 Sources: Senior debt + Mezzanine debt + Sponsor equity = Total
 Uses: Purchase price (EV) + Transaction fees + Financing fees = Total
 Sources must equal Uses.

 Entry multiples:
 - Entry EV/EBITDA: {{entry_multiple}}x
 - Purchase price = Entry EV/EBITDA x LTM EBITDA
 - Debt/EBITDA: {{leverage}}x (split between senior secured and subordinated)

2. Debt schedule:
 For each debt tranche:
 - Beginning balance, interest expense, cash sweep / amortization, ending balance
 - Cash sweep: excess cash flow used to pay down highest-cost debt first
 - Revolver: drawn when operating cash flow is insufficient to meet obligations
 - PIK vs cash interest: PIK increases principal (compounds), cash interest reduces free cash

3. Free cash flow and debt paydown:
 EBITDA - Interest - Taxes - Capex - Change in NWC = FCF available for debt paydown
 - Project EBITDA with operating improvement thesis assumptions
 - Tax shield: interest expense x tax rate reduces cash taxes
 - Debt paydown waterfall: senior debt first, then mezz, then any remaining

4. Exit analysis:
 Exit EV = Exit EBITDA x Exit Multiple
 Exit Equity Value = Exit EV - Remaining Debt
 Sponsor proceeds = Exit Equity Value x Sponsor ownership %

5. Returns calculation:
 - Money-on-Money Multiple (MoM): Proceeds / Equity invested
 - IRR: solve for the rate that makes NPV of cash flows = 0
 - Target returns: MoM > 2.5x, IRR > 20% for typical PE
 - Returns bridge: attribute IRR to EBITDA growth, multiple expansion, leverage, and dividends

6. Sensitivity tables:
 - IRR and MoM: entry multiple vs exit multiple (3x3 or 5x5)
 - IRR and MoM: entry multiple vs EBITDA growth rate

Return: Sources and Uses table, debt schedule, FCF projection, exit analysis, returns calculation, and sensitivity tables. 
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

The AI should return a structured result that covers the main requested outputs, such as Sources and Uses of Funds:, Entry EV/EBITDA: {{entry_multiple}}x, Purchase price = Entry EV/EBITDA x LTM EBITDA. The final answer should stay clear, actionable, and easy to review inside a financial modeling workflow for financial analyst work. 

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
