# Valuation and Transactions *AI Prompts *

2 Financial Analyst prompts in Valuation and Transactions. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate levels and 2 single prompts. 

## AI prompts in Valuation and Transactions 
2 prompts Intermediate Single prompt 01 
### Comparable Company Analysis 

Build a comparable company analysis (Comps) to value this company. Subject company: {{subject_company}} Industry: {{industry}} Financials: {{financials}} 1. Select comparable co... 
Prompt text Build a comparable company analysis (Comps) to value this company.

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

Return: comparable company table, multiples statistics, implied valuation ranges, football field chart description, and multiple selection rationale. Copy prompt Open prompt details Intermediate Single prompt 02 
### Precedent Transaction Analysis 

Build a precedent transaction analysis to establish acquisition valuation benchmarks. Subject company / target profile: {{target_profile}} Industry: {{industry}} Transaction dat... 
Prompt text Build a precedent transaction analysis to establish acquisition valuation benchmarks.

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

Return: transaction comps table, control premium analysis, implied valuation ranges, and key deal notes affecting multiple selection. Copy prompt Open prompt details 
## Recommended Valuation and Transactions workflow 
1 
### Comparable Company Analysis 

Start with a focused prompt in Valuation and Transactions so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Precedent Transaction Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
