# Variance Analysis *AI Prompts *

4 Financial Analyst prompts in Variance Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Variance Analysis 
4 prompts Beginner Single prompt 01 
### Budget vs Actual Variance Analysis 

Analyze the variance between budget and actual results for this period. Budget data: {{budget}} Actual data: {{actuals}} Period: {{period}} 1. Variance calculation: For each P&L... 
Prompt text Analyze the variance between budget and actual results for this period.

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

Return: variance table with F/U flags, decomposed revenue and cost variances, root cause narratives, and updated full-year forecast. Copy prompt Open prompt details Intermediate Single prompt 02 
### Expense Analysis and Optimization 

Analyze the expense structure of this business and identify optimization opportunities. Expense data: {{expense_data}} (by category, department, period) Revenue data: {{revenue_... 
Prompt text Analyze the expense structure of this business and identify optimization opportunities.

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

Return: expense structure table, benchmark comparison, operating leverage analysis, and top 5 optimization opportunities with savings estimates. Copy prompt Open prompt details Intermediate Single prompt 03 
### Margin Bridge Analysis 

Build a margin bridge explaining the change in gross margin or EBITDA margin between two periods. Period A: {{period_a}} margin: {{margin_a}} Period B: {{period_b}} margin: {{ma... 
Prompt text Build a margin bridge explaining the change in gross margin or EBITDA margin between two periods.

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

Return: margin bridge table, waterfall chart description, component commentary, and adjusted margins excluding one-time items. Copy prompt Open prompt details Advanced Single prompt 04 
### Revenue Variance Deep Dive 

Decompose the revenue variance between two periods into price, volume, and mix effects. Period A data: {{period_a_data}} (product/segment, units sold, average price) Period B da... 
Prompt text Decompose the revenue variance between two periods into price, volume, and mix effects.

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

Return: three-way decomposition table, product-level detail, mix shift analysis, and strategic implications. Copy prompt Open prompt details 
## Recommended Variance Analysis workflow 
1 
### Budget vs Actual Variance Analysis 

Start with a focused prompt in Variance Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Expense Analysis and Optimization 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Margin Bridge Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Revenue Variance Deep Dive 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
