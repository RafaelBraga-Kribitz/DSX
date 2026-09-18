# DCF Valuation Model *AI Prompt *

Build a discounted cash flow (DCF) valuation for this company. Company: {{company}} Financials: {{financial_data}} Forecast horizon: {{horizon}} years Industry: {{industry}} 1.... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a discounted cash flow (DCF) valuation for this company.

Company: {{company}}
Financials: {{financial_data}}
Forecast horizon: {{horizon}} years
Industry: {{industry}}

1. Free Cash Flow (FCF) projection:
 FCF = EBIT x (1 - Tax Rate) + D&A - Capex - Change in Net Working Capital
 - Project each component for {{horizon}} years with explicit assumptions
 - NOPAT margin trajectory: justify the convergence to terminal margin
 - Reinvestment rate: Capex + Change in NWC / NOPAT (higher growth requires more reinvestment)

2. Discount rate (WACC):
 WACC = (E/V) x Ke + (D/V) x Kd x (1-T)
 - Cost of equity (Ke): CAPM = Rf + Beta x ERP
 - Risk-free rate: current 10-year government bond yield
 - Equity risk premium (ERP): use Damodaran's current country ERP
 - Beta: use 2-year weekly regression beta, then Blume-adjusted: Beta_adj = 0.67 x Raw Beta + 0.33
 - Cost of debt (Kd): weighted average yield on existing debt, or credit spread + risk-free rate
 - Capital structure: use target or industry-average leverage, not current (if distorted)

3. Terminal value:
 - Gordon Growth Model: TV = FCF_terminal x (1+g) / (WACC - g)
 - Terminal growth rate: should not exceed long-run GDP growth (typically 2-3%)
 - Sanity check: implied terminal EV/EBITDA multiple vs comparable company multiples
 - Exit multiple method as cross-check: TV = Terminal EBITDA x EV/EBITDA_peer_median

4. Bridge to equity value:
 Enterprise Value = PV of FCFs + PV of Terminal Value
 Equity Value = EV + Cash - Debt - Minority Interest - Preferred Stock
 Per Share Value = Equity Value / Diluted Shares Outstanding

5. Sensitivity analysis:
 - 5x5 table: WACC (range ±100bps) x Terminal Growth Rate (range ±100bps)
 - 5x5 table: WACC x EBITDA Exit Multiple
 - At what assumptions does the stock look cheap vs expensive vs current price?

Return: FCF projection table, WACC calculation, terminal value computation, equity value bridge, and sensitivity tables. 
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

The AI should return a structured result that covers the main requested outputs, such as Free Cash Flow (FCF) projection:, Project each component for {{horizon}} years with explicit assumptions, NOPAT margin trajectory: justify the convergence to terminal margin. The final answer should stay clear, actionable, and easy to review inside a financial modeling workflow for financial analyst work. 

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
