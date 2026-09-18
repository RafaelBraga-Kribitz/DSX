# Financial Modeling *AI Prompts *

5 Financial Analyst prompts in Financial Modeling. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Financial Modeling 
5 prompts Intermediate Single prompt 01 
### DCF Valuation Model 

Build a discounted cash flow (DCF) valuation for this company. Company: {{company}} Financials: {{financial_data}} Forecast horizon: {{horizon}} years Industry: {{industry}} 1.... 
Prompt text Build a discounted cash flow (DCF) valuation for this company.

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

Return: FCF projection table, WACC calculation, terminal value computation, equity value bridge, and sensitivity tables. Copy prompt Open prompt details Advanced Single prompt 02 
### LBO Model Framework 

Build a leveraged buyout (LBO) model framework for evaluating this acquisition. Target company: {{target}} Financials: {{financials}} Entry assumptions: {{entry_assumptions}} Ho... 
Prompt text Build a leveraged buyout (LBO) model framework for evaluating this acquisition.

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

Return: Sources and Uses table, debt schedule, FCF projection, exit analysis, returns calculation, and sensitivity tables. Copy prompt Open prompt details Intermediate Single prompt 03 
### Revenue Model Builder 

Build a bottom-up revenue model for this business. Business type: {{business_type}} Revenue streams: {{revenue_streams}} Historical data available: {{historical_data}} Forecast... 
Prompt text Build a bottom-up revenue model for this business.

Business type: {{business_type}}
Revenue streams: {{revenue_streams}}
Historical data available: {{historical_data}}
Forecast horizon: {{horizon}} years

1. Revenue disaggregation:
 Break total revenue into its most granular meaningful components:
 - For SaaS: ARR = Customers x Average Revenue Per Account (ARPA)
 - New ARR (new logos), Expansion ARR (upsell), Churn ARR (lost customers)
 - Net Revenue Retention (NRR) = (Beginning ARR + Expansion - Churn) / Beginning ARR
 - For transactional: Revenue = Transactions x Average Order Value
 - For subscription: Revenue = Subscribers x Monthly Fee x (1 - Churn Rate)
 - For services: Revenue = Headcount x Utilization Rate x Billing Rate

2. Forecast each driver separately:
 For each revenue driver:
 - Historical trend (last 3 years CAGR)
 - Management guidance or market growth rate
 - Internal capacity constraints
 - Derive the forecast assumption with a clear rationale

3. Bridge from current year to forecast:
 Revenue(year N+1) = Revenue(year N) + New Business + Expansion - Churn + Price Effect
 Show each component explicitly so the forecast is auditable.

4. Scenario analysis:
 - Base case: management guidance or consensus growth rates
 - Bull case: top quartile of peer growth rates
 - Bear case: mean reversion or macro headwind scenario
 - Show the revenue range at each forecast year

5. Sanity checks:
 - Implied market share: does the forecast require unrealistic market share gains?
 - Revenue per employee: does it stay within a reasonable range for the industry?
 - Cohort math: does the model's churn assumption agree with the cohort retention data?

Return: disaggregated revenue model, driver-by-driver assumptions, three-scenario table, and sanity check results. Copy prompt Open prompt details Intermediate Single prompt 04 
### Sensitivity and Scenario Analysis 

Build a sensitivity and scenario analysis framework for this financial model. Base case model: {{model_description}} Key output metric: {{output}} (e.g. EV, IRR, EBITDA, EPS) Ke... 
Prompt text Build a sensitivity and scenario analysis framework for this financial model.

Base case model: {{model_description}}
Key output metric: {{output}} (e.g. EV, IRR, EBITDA, EPS)
Key input assumptions: {{inputs}}

1. One-way sensitivity analysis:
 For each key input, vary it across a range while holding all others constant:
 - Range: +/-20%, +/-10%, +/-5% from base case
 - Show output at each input level
 - Tornado chart: rank inputs by their impact on the output (largest impact at top)
 - The top 3 inputs by tornado rank are the most important assumptions to get right

2. Two-way sensitivity table:
 Select the top 2 most impactful inputs from the tornado chart.
 Build a 5x5 table:
 - Rows: Input 1 at 5 levels (base-20% to base+20%)
 - Columns: Input 2 at 5 levels
 - Cell values: output metric at each combination
 - Color code: green = above base case output, red = below

3. Scenario analysis (distinct named scenarios):
 Base case: current assumptions
 Upside scenario: best plausible combination of assumptions (not maximum of each)
 Downside scenario: worst plausible combination (not minimum of each)
 Stress case: severe downside - what happens in a recession or crisis?

 For each scenario:
 - State the 3-5 key assumption changes vs base case
 - Show the output metric range
 - Narrative: what business or macro environment drives this scenario?

4. Break-even analysis:
 - For the primary output metric: at what level of each key input does the output reach breakeven?
 - Example: 'At what revenue growth rate does the IRR reach our minimum threshold of 15%?'

Return: tornado chart description, two-way sensitivity table, scenario comparison table, and break-even levels for each key input. Copy prompt Open prompt details Beginner Single prompt 05 
### Three-Statement Model Audit 

Audit this three-statement financial model (Income Statement, Balance Sheet, Cash Flow Statement) for errors and best practices. Model description: {{model_description}} 1. Bala... 
Prompt text Audit this three-statement financial model (Income Statement, Balance Sheet, Cash Flow Statement) for errors and best practices.

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

Return: error list with severity and location, reconciliation check results, and a model quality score (0-100) with justification. Copy prompt Open prompt details 
## Recommended Financial Modeling workflow 
1 
### DCF Valuation Model 

Start with a focused prompt in Financial Modeling so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### LBO Model Framework 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Revenue Model Builder 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Sensitivity and Scenario Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
