# Financial Analysis *AI Prompts *

4 Financial Analyst prompts in Financial Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Financial Analysis 
4 prompts Intermediate Single prompt 01 
### Cash Flow Analysis 

Analyze the cash flow quality and sustainability of this business. Cash flow statement: {{cash_flow_data}} Periods: {{periods}} 1. Cash flow waterfall: EBITDA - Interest paid -... 
Prompt text Analyze the cash flow quality and sustainability of this business.

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

Return: cash flow waterfall table, conversion metrics, capex analysis, working capital cash impact, liquidity assessment, and red flag identification. Copy prompt Open prompt details Beginner Single prompt 02 
### Financial Ratio Analysis 

Conduct a comprehensive financial ratio analysis for {{company}}. Financial statements: {{financial_statements}} Peer benchmarks: {{benchmarks}} Periods: {{periods}} 1. Profitab... 
Prompt text Conduct a comprehensive financial ratio analysis for {{company}}.

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

Return: ratio table across periods, peer benchmark comparison, trend assessment, DuPont decomposition, and key findings. Copy prompt Open prompt details Advanced Single prompt 03 
### Unit Economics Analysis 

Analyze the unit economics of this business and assess its scalability. Business model: {{business_model}} Data: {{unit_economics_data}} 1. Customer Acquisition Cost (CAC): CAC... 
Prompt text Analyze the unit economics of this business and assess its scalability.

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

Return: CAC and LTV calculations, LTV/CAC ratio, cohort recovery curves, contribution margin analysis, and scalability assessment. Copy prompt Open prompt details Intermediate Single prompt 04 
### Working Capital Analysis 

Analyze the working capital dynamics and cash conversion efficiency of this business. Balance sheet and P&L data: {{financial_data}} Periods: {{periods}} Industry: {{industry}}... 
Prompt text Analyze the working capital dynamics and cash conversion efficiency of this business.

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

Return: working capital table across periods, CCC calculation, benchmark comparison, cash impact analysis, and optimization opportunities with cash value estimates. Copy prompt Open prompt details 
## Recommended Financial Analysis workflow 
1 
### Cash Flow Analysis 

Start with a focused prompt in Financial Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Financial Ratio Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Unit Economics Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Working Capital Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
