# Financial Analyst *AI Prompts *

Financial Analyst AI prompt library with 22 prompts in 6 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 6 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Financial Analyst prompt categories 
6 categories 
### Financial Modeling 

AI prompts for financial modeling workflows, including scenario design, assumptions testing, sensitivity analysis, and forecast interpretation. 
5 prompts DCF Valuation Model LBO Model Framework → 
### Financial Analysis 

AI prompts for financial analysis, including trend interpretation, ratio diagnostics, performance decomposition, and decision-support narratives. 
4 prompts Cash Flow Analysis Financial Ratio Analysis → 
### Forecasting 

AI prompts for forecasting, time series analysis, trend detection, seasonality modeling, and future value prediction. 
4 prompts Full Financial Planning Chain Rolling Forecast Design → 
### Variance Analysis 

AI prompts for variance analysis, including plan-vs-actual diagnostics, driver decomposition, and operationally actionable commentary. 
4 prompts Budget vs Actual Variance Analysis Expense Analysis and Optimization → 
### Reporting and Presentation 

AI prompts for reporting and presentation, including executive narrative design, visualization choices, and concise recommendation framing. 
3 prompts Board Financial Package CFO Dashboard Design → 
### Valuation and Transactions 

AI prompts for valuation and transaction analysis, including multiple-based benchmarking, scenario framing, and deal-structure sensitivity. 
2 prompts Comparable Company Analysis Precedent Transaction Analysis → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 22 Financial Modeling 5 Financial Analysis 4 Forecasting 4 Variance Analysis 4 Reporting and Presentation 3 Valuation and Transactions 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **22 **of 22 prompts 
## Financial Modeling 
5 prompt s Financial Modeling Intermediate Prompt 01 
### DCF Valuation Model 
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

Return: FCF projection table, WACC calculation, terminal value computation, equity value bridge, and sensitivity tables. Copy prompt View page Show more ↓ Financial Modeling Advanced Prompt 02 
### LBO Model Framework 
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

Return: Sources and Uses table, debt schedule, FCF projection, exit analysis, returns calculation, and sensitivity tables. Copy prompt View page Show more ↓ Financial Modeling Intermediate Prompt 03 
### Revenue Model Builder 
Build a bottom-up revenue model for this business.

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

Return: disaggregated revenue model, driver-by-driver assumptions, three-scenario table, and sanity check results. Copy prompt View page Show more ↓ Financial Modeling Intermediate Prompt 04 
### Sensitivity and Scenario Analysis 
Build a sensitivity and scenario analysis framework for this financial model.

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

Return: tornado chart description, two-way sensitivity table, scenario comparison table, and break-even levels for each key input. Copy prompt View page Show more ↓ Financial Modeling Beginner Prompt 05 
### Three-Statement Model Audit 
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

Return: error list with severity and location, reconciliation check results, and a model quality score (0-100) with justification. Copy prompt View page Show more ↓ 
## Financial Analysis 
4 prompt s Financial Analysis Intermediate Prompt 01 
### Cash Flow Analysis 
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

Return: cash flow waterfall table, conversion metrics, capex analysis, working capital cash impact, liquidity assessment, and red flag identification. Copy prompt View page Show more ↓ Financial Analysis Beginner Prompt 02 
### Financial Ratio Analysis 
Conduct a comprehensive financial ratio analysis for {{company}}.

Financial statements: {{financial_statements}}
Peer benchmarks: {{benchmarks}}
Periods: {{periods}}

1. Profitability ratios:
 - Gross margin: Gross Profit / Revenue
 - EBITDA margin: EBITDA / Revenue
 - Operating margin: EBIT / Revenue
 - Net margin: Net Income / Revenue
 - Return on equity (ROE): Net Income / Average Equity
 - Return on assets (ROA): Net Income / Average Total Assets
 - Return on invested capital (ROIC): NOPAT / (Equity + Net Debt)

2. Liquidity ratios:
 - Current ratio: Current Assets / Current Liabilities (target > 1.5)
 - Quick ratio: (Cash + Receivables) / Current Liabilities (target > 1.0)
 - Cash ratio: Cash / Current Liabilities

3. Leverage ratios:
 - Net debt / EBITDA (target < 3x for investment grade)
 - Interest coverage: EBITDA / Interest Expense (target > 3x)
 - Debt / Equity ratio
 - Debt / Total Capital

4. Efficiency ratios:
 - Days Sales Outstanding (DSO): Receivables / (Revenue / 365)
 - Days Inventory Outstanding (DIO): Inventory / (COGS / 365)
 - Days Payable Outstanding (DPO): Payables / (COGS / 365)
 - Cash Conversion Cycle: DSO + DIO - DPO

5. Per ratio: provide:
 - Value for each historical period
 - Trend: improving or deteriorating?
 - Peer median comparison: above or below benchmark?
 - Commentary: what is driving the trend?

6. DuPont decomposition of ROE:
 ROE = Net Margin x Asset Turnover x Financial Leverage
 Which component is driving ROE? Is the source of returns healthy (operating efficiency) or concerning (excessive leverage)?

Return: ratio table across periods, peer benchmark comparison, trend assessment, DuPont decomposition, and key findings. Copy prompt View page Show more ↓ Financial Analysis Advanced Prompt 03 
### Unit Economics Analysis 
Analyze the unit economics of this business and assess its scalability.

Business model: {{business_model}}
Data: {{unit_economics_data}}

1. Customer Acquisition Cost (CAC):
 CAC = Total Sales and Marketing Spend / New Customers Acquired
 - Blended CAC: all channels combined
 - By-channel CAC: paid acquisition, organic, referral, outbound
 - CAC payback period: CAC / Monthly Gross Profit per Customer
 Target: < 12 months for SaaS, < 6 months for e-commerce

2. Customer Lifetime Value (LTV):
 LTV = Average Revenue per Customer / Churn Rate (for SaaS)
 Or: LTV = Average Order Value x Purchase Frequency x Gross Margin / Churn Rate
 - Gross margin LTV: multiply by gross margin to get profit-basis LTV
 - LTV should account for the expected customer tenure, not assume infinite life

3. LTV / CAC ratio:
 - LTV / CAC > 3: business is generating healthy returns on acquisition spend
 - LTV / CAC < 1: acquiring customers at a loss (sustainable only during investment phase)
 - Trend: is LTV/CAC improving or deteriorating as the business scales?

4. Cohort economics:
 - By acquisition cohort: cumulative gross profit per customer over time
 - CAC recovery curve: at what month does the cohort recover its acquisition cost?
 - Cohort comparison: are newer cohorts recovering CAC faster or slower?

5. Contribution margin per unit/customer:
 Revenue - Variable COGS - Variable Sales and Marketing = Contribution Margin
 - At what volume does the business reach contribution margin breakeven per unit?

6. Scalability assessment:
 - Does CAC increase as the business scales? (Channel saturation)
 - Does LTV increase as the business scales? (Network effects, pricing power)
 - What is the implied steady-state margin when the business reaches maturity?

Return: CAC and LTV calculations, LTV/CAC ratio, cohort recovery curves, contribution margin analysis, and scalability assessment. Copy prompt View page Show more ↓ Financial Analysis Intermediate Prompt 04 
### Working Capital Analysis 
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

Return: working capital table across periods, CCC calculation, benchmark comparison, cash impact analysis, and optimization opportunities with cash value estimates. Copy prompt View page Show more ↓ 
## Forecasting 
4 prompt s Forecasting Advanced Chain 01 
### Full Financial Planning Chain 
Step 1: Business driver identification - identify the 5-8 key drivers that determine financial outcomes for this business. For each driver: current value, historical trend, and forecast assumption with rationale.
Step 2: Revenue model - build a bottom-up revenue model from the key drivers. Disaggregate revenue into its components (new business, existing customer growth, churn). Build three scenarios: base, bull, and bear.
Step 3: Cost model - forecast each major cost category as either a fixed cost, a variable cost tied to a revenue driver, or a headcount-driven cost. Identify operating leverage: at what revenue level does EBITDA turn positive or reach the target margin?
Step 4: Cash flow model - build the FCF model from EBITDA to free cash flow. Include working capital movements, capex, interest, and taxes. Compute cash runway under each scenario.
Step 5: Balance sheet build - project the balance sheet for each period. Verify it balances. Identify any periods where the company needs additional financing.
Step 6: Sensitivity and scenario analysis - build a tornado chart of the top inputs by impact. Create a 5x5 sensitivity table for the two most impactful inputs. Present the three scenarios with narrative.
Step 7: Management presentation - produce a one-page financial summary: revenue, EBITDA, and FCF for each period with actuals and forecast. Include key assumptions, risks, and the single most important financial question the team needs to answer in the next 90 days. Copy prompt View page Show more ↓ Forecasting Intermediate Prompt 02 
### Rolling Forecast Design 
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

Return: rolling forecast architecture, driver identification worksheet, submission workflow calendar, accuracy tracking framework, and comparison to annual budget approach. Copy prompt View page Show more ↓ Forecasting Intermediate Prompt 03 
### Scenario Planning Framework 
Build a scenario planning framework for this business.

Company: {{company}}
Key uncertainties: {{key_uncertainties}}
Planning horizon: {{horizon}}

1. Identify the key uncertainties:
 From the provided list, select 2 dimensions with:
 - High impact on business outcomes
 - High uncertainty (we do not know which way they will go)
 - Independence from each other (orthogonal axes)

 Example axes: (Market growth: fast vs slow) x (Competitive intensity: high vs low)

2. Build four scenarios on a 2x2 matrix:
 Each quadrant = a different future world
 - Scenario 1 (best case): favorable on both axes
 - Scenario 2 (growth challenge): favorable market, unfavorable competitive position
 - Scenario 3 (volume challenge): unfavorable market, favorable competitive position
 - Scenario 4 (stress case): unfavorable on both axes

3. Financial model per scenario:
 For each scenario:
 - Revenue assumption (growth rate and trajectory)
 - Margin assumption (impact on gross and EBITDA margin)
 - Cash flow and liquidity position at end of horizon
 - Key financial metrics: revenue, EBITDA, FCF, net debt/EBITDA

4. Trigger indicators:
 For each scenario: what early data would signal we are moving into that scenario?
 - Revenue indicators: order intake, pipeline coverage, churn rate
 - Market indicators: competitor pricing, industry PMI, macro data
 - Operational indicators: hiring plan, supply chain lead times

5. Strategic responses:
 For each scenario: what actions would management take?
 - Scenario 1: accelerate investment, hire aggressively
 - Scenario 4: cost containment, preserve cash, renegotiate debt
 Pre-committing to responses removes decision delay when a scenario materializes.

Return: 2x2 scenario matrix, financial model per scenario, trigger indicator dashboard, and pre-committed strategic responses. Copy prompt View page Show more ↓ Forecasting Advanced Prompt 04 
### Time Series Revenue Forecasting 
Build a statistical time series forecast for this revenue or financial metric.

Metric: {{metric}}
Historical data: {{data}} (at least 24 periods)
Forecast horizon: {{horizon}} periods
Seasonality: {{seasonality}} (yes/no, and period: weekly/monthly/quarterly)

1. Exploratory analysis:
 - Plot the series: trend, seasonality, and irregular components visible?
 - Decompose using STL or classical decomposition: trend + seasonal + residual
 - Autocorrelation function (ACF) and Partial ACF (PACF): identify autoregressive and moving average structure
 - ADF test: is the series stationary? If not, difference and retest.

2. Model candidates:

 Holt-Winters (ETS):
 - Triple exponential smoothing: handles trend and seasonality
 - Parameters: alpha (level), beta (trend), gamma (seasonality)
 - Best for: smooth trends with regular seasonality, limited data (< 5 years)

 SARIMA:
 - Seasonal ARIMA (p,d,q)(P,D,Q)[m]
 - Select parameters using auto.arima (AIC/BIC minimization)
 - Best for: data with complex autocorrelation structure

 Prophet (Facebook/Meta):
 - Handles multiple seasonalities, holiday effects, and trend changepoints
 - Best for: monthly or daily data with irregular events and holidays

3. Model evaluation:
 - Split data: train on first 80%, test on last 20%
 - Metrics: MAPE, MAE, RMSE on the test set
 - Select the model with lowest MAPE on holdout

4. Forecast output:
 - Point forecast for each future period
 - 80% and 95% prediction intervals
 - Is the interval width reasonable given the metric's historical variance?

5. Forecast decomposition:
 - How much of the forecast is trend vs seasonal vs baseline?
 - What is the year-over-year growth implied by the forecast?

Return: model comparison table, selected model diagnostics, forecast with prediction intervals, and decomposition of forecast components. Copy prompt View page Show more ↓ 
## Variance Analysis 
4 prompt s Variance Analysis Beginner Prompt 01 
### Budget vs Actual Variance Analysis 
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

Return: variance table with F/U flags, decomposed revenue and cost variances, root cause narratives, and updated full-year forecast. Copy prompt View page Show more ↓ Variance Analysis Intermediate Prompt 02 
### Expense Analysis and Optimization 
Analyze the expense structure of this business and identify optimization opportunities.

Expense data: {{expense_data}} (by category, department, period)
Revenue data: {{revenue_data}}
Benchmarks: {{industry_benchmarks}}

1. Expense categorization:
 - Fixed vs variable costs: which expenses are truly fixed regardless of revenue?
 - Discretionary vs non-discretionary: which can be reduced without impacting operations?
 - Direct vs indirect: which are directly tied to revenue generation?

2. Expense as % of revenue trend:
 For each major expense category:
 - Expense / Revenue % for each of the last {{n}} periods
 - Is the ratio improving (declining) or worsening (rising) over time?
 - At what revenue level should expenses show significant operating leverage?

3. Benchmark comparison:
 - Compare each major expense line to industry median % of revenue
 - Categories above benchmark: potential over-investment or inefficiency
 - Categories below benchmark: potential under-investment or competitive advantage

4. Headcount and productivity analysis:
 - Revenue per employee: trend and benchmark comparison
 - Expense per employee: which departments have the highest cost per head?
 - Is headcount growth outpacing revenue growth? (Operating leverage going in wrong direction)

5. Top 5 optimization opportunities:
 For each opportunity:
 - Expense category
 - Current spend vs benchmark
 - Estimated annual savings
 - Implementation risk (Low/Medium/High)
 - Required action

6. Scenario: what if we reduce expense category X by Y%?
 - Impact on EBITDA margin
 - Impact on annual EBITDA in dollars
 - Any revenue risk from the reduction?

Return: expense structure table, benchmark comparison, operating leverage analysis, and top 5 optimization opportunities with savings estimates. Copy prompt View page Show more ↓ Variance Analysis Intermediate Prompt 03 
### Margin Bridge Analysis 
Build a margin bridge explaining the change in gross margin or EBITDA margin between two periods.

Period A: {{period_a}} margin: {{margin_a}}
Period B: {{period_b}} margin: {{margin_b}}
P&L data for both periods: {{pnl_data}}

1. Margin bridge components:
 Total margin change = Volume effect + Price/Rate effect + Mix effect + Cost efficiency effect + One-time items

 Volume effect:
 - If revenue grew, fixed costs spread over a larger base, improving margin
 - Volume effect = (Revenue_B - Revenue_A) / Revenue_B x Fixed Cost Ratio_A

 Price/Rate effect:
 - Change in average selling price x revenue volume
 - Change in input cost rates x cost volume

 Mix effect:
 - Did the revenue mix shift toward higher or lower margin products/customers/channels?
 - Mix effect = (Current mix margin - Prior mix margin) x Revenue_B

 Cost efficiency:
 - Productivity improvements, procurement savings, or headcount efficiency
 - Efficiency effect = (Cost_A % of revenue - Cost_B % of revenue) x Revenue_B

 One-time items:
 - Identify and isolate non-recurring items in both periods
 - Adjusted margins excluding one-time items

2. Waterfall chart specification:
 - Start bar: Period A margin %
 - Each bridge item: positive = green bar up, negative = red bar down
 - End bar: Period B margin %
 - All bars sum to the total margin change

3. Commentary for each bridge item:
 - Why did this component move? (Specific cause)
 - Is it structural (durable) or temporary?
 - Expected trajectory going forward

Return: margin bridge table, waterfall chart description, component commentary, and adjusted margins excluding one-time items. Copy prompt View page Show more ↓ Variance Analysis Advanced Prompt 04 
### Revenue Variance Deep Dive 
Decompose the revenue variance between two periods into price, volume, and mix effects.

Period A data: {{period_a_data}} (product/segment, units sold, average price)
Period B data: {{period_b_data}}

1. Total revenue variance:
 Total Variance = Revenue_B - Revenue_A (absolute and % change)

2. Three-way variance decomposition:

 Volume variance:
 = (Total Volume_B - Total Volume_A) x Average Price_A
 What revenue would have changed if only volume changed (price and mix held constant)?

 Price variance:
 = (Average Price_B - Average Price_A) x Total Volume_B
 What revenue changed because we charged more or less per unit?

 Mix variance:
 = (Actual mix revenue at Period A prices) - (Expected mix revenue at Period A prices)
 What revenue changed because the product/segment mix shifted toward higher or lower value items?

 Verify: Volume Variance + Price Variance + Mix Variance = Total Revenue Variance

3. Product/segment level detail:
 For each product or segment:
 - Revenue Period A, Period B
 - Volume change, price change
 - Contribution to total volume/price/mix variance

4. Mix analysis:
 - Which products gained share of revenue mix? Which lost share?
 - Did mix shift toward higher-margin or lower-margin products?
 - Revenue at period A prices if mix were held constant: how much did mix cost or add?

5. Strategic implications:
 - Is revenue growth coming from volume (sustainable, market share driven) or price (possible unsustainable if it drives churn)?
 - Is the mix shift favorable (premiumization) or unfavorable (commoditization)?

Return: three-way decomposition table, product-level detail, mix shift analysis, and strategic implications. Copy prompt View page Show more ↓ 
## Reporting and Presentation 
3 prompt s Reporting and Presentation Intermediate Prompt 01 
### Board Financial Package 
Prepare the financial section of a board of directors package for {{period}}.

Company: {{company}}
Financial results: {{results}}
Board audience: {{board_composition}}

Board packages require: strategic framing, not operational detail. Every number must be compared to something. Recommendations must be specific.

1. Executive financial summary (1 page):
 - Period highlights in 3 bullet points (specific numbers, not vague statements)
 - Financial scorecard: 6 key metrics vs budget and prior year
 - Full-year forecast update: are we tracking to plan?
 - Top financial risk: one specific concern with mitigation actions

2. P&L review (1 page):
 - Income statement: actual vs budget vs prior year (columns)
 - All variances > 5% flagged with a brief explanation in footnotes
 - Bridge chart: explain the EBITDA change from prior year in 4-5 components

3. Balance sheet and cash flow (1 page):
 - Balance sheet: period end vs prior year end with key ratio changes
 - Cash flow bridge: beginning cash + operations + investing + financing = ending cash
 - Liquidity runway: months of cash at current burn rate
 - Debt profile: maturity schedule and covenant headroom

4. Forecast and outlook (1 page):
 - Full-year revenue and EBITDA: budget vs current forecast vs prior year
 - Scenario analysis: base, bull, bear case for the remainder of the year
 - Key assumptions that could cause the forecast to be wrong

5. Decisions required (if any):
 - Any financial decisions or approvals needed from the board?
 - Present options with recommendation and rationale

Return: board package outline with specific content for each page, key metrics table, and bridge chart description. Copy prompt View page Show more ↓ Reporting and Presentation Beginner Prompt 02 
### CFO Dashboard Design 
Design a CFO-level financial dashboard for {{company}}.

Business model: {{business_model}}
Data sources: {{data_sources}}
Review cadence: {{cadence}} (weekly / monthly)

1. Dashboard structure (top to bottom):

 Row 1 - P&L Headlines:
 - Revenue: actual vs budget vs prior period (with % variance)
 - Gross Margin %: actual vs budget vs prior period
 - EBITDA: actual vs budget vs prior period
 - Net Income: actual vs budget vs prior period

 Row 2 - Cash and Liquidity:
 - Cash balance: current vs prior month vs minimum covenant
 - Operating cash flow: LTM actual vs budget
 - Free cash flow: LTM
 - Net debt / EBITDA: current vs covenant threshold

 Row 3 - Revenue Quality:
 - ARR / MRR trend (for recurring revenue businesses)
 - New vs expansion vs churn waterfall (if SaaS)
 - Customer count and net adds
 - Revenue concentration: top 10 customer % of total

 Row 4 - Expense and Margin:
 - Opex by category as % of revenue: actual vs budget
 - Headcount: actual vs budget
 - Revenue per employee: trend

2. Alert conditions:
 - Revenue > 10% below budget: red flag
 - Gross margin < {{threshold}}%: red flag
 - Cash runway < 12 months: critical alert
 - Net debt / EBITDA > covenant level: critical alert

3. Drill-down links:
 - Each headline metric links to a detailed supporting schedule
 - Revenue headline: links to revenue by segment and geography
 - Headcount: links to department-level headcount report

Return: dashboard layout specification, metric definitions, alert thresholds, and drill-down structure. Copy prompt View page Show more ↓ Reporting and Presentation Advanced Prompt 03 
### Investor Presentation Financial Section 
Write the financial section of an investor presentation for {{company}}.

Audience: {{audience}} (institutional investors, analysts, debt investors)
Company stage: {{stage}} (public, pre-IPO, Series C, etc.)
Financial highlights: {{highlights}}

1. Financial highlights slide (headline metrics):
 - Choose 4-6 metrics that best represent the financial health and growth story
 - Each metric: current value + trend arrow + key comparison (YoY or vs peers)
 - For SaaS: ARR, NRR, Gross Margin, Rule of 40 score
 - For e-commerce: GMV, Take Rate, Gross Margin, Customer Acquisition Cost
 - For traditional business: Revenue, EBITDA Margin, FCF, ROIC

2. Revenue story slide:
 - Revenue by period with growth rates labeled
 - Revenue quality: recurring vs non-recurring
 - Revenue by segment or product: showing mix shift toward higher-value streams
 - Forward-looking: at least one slide showing the path to the long-term revenue target

3. Unit economics slide:
 - LTV / CAC for customer-acquisition businesses
 - Gross margin by cohort or segment
 - Payback period trend
 - Clear statement: 'We acquire customers profitably and they generate [X]x their acquisition cost'

4. Path to profitability slide (for unprofitable companies):
 - Current cash burn and runway
 - Key milestones to reach EBITDA breakeven
 - Bridge from current EBITDA margin to long-term target margin with specific drivers
 - Conservative and base case timeline

5. Balance sheet and liquidity slide:
 - Current cash position and runway
 - Debt profile: total debt, maturity, covenants
 - Capital allocation plan: how will cash be deployed?

6. Financial credibility signals:
 - Beat-and-raise history (if public)
 - Auditor and quality of earnings
 - Any restatements or accounting changes: address proactively

Return: slide-by-slide outline with specific data points, chart types, key messages per slide, and narrative arc for the full financial section. Copy prompt View page Show more ↓ 
## Valuation and Transactions 
2 prompt s Valuation and Transactions Intermediate Prompt 01 
### Comparable Company Analysis 
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

Return: comparable company table, multiples statistics, implied valuation ranges, football field chart description, and multiple selection rationale. Copy prompt View page Show more ↓ Valuation and Transactions Intermediate Prompt 02 
### Precedent Transaction Analysis 
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

Return: transaction comps table, control premium analysis, implied valuation ranges, and key deal notes affecting multiple selection. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
