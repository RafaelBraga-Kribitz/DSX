# Customer Analytics *AI Prompts *

5 Ecommerce Analyst prompts in Customer Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Customer Analytics 
5 prompts Advanced Single prompt 01 
### Customer Acquisition Cost Analysis 

Analyze customer acquisition costs and LTV/CAC ratios across channels for this e-commerce business. Marketing spend data: {{spend_data}} (by channel, period) New customer data:... 
Prompt text Analyze customer acquisition costs and LTV/CAC ratios across channels for this e-commerce business.

Marketing spend data: {{spend_data}} (by channel, period)
New customer data: {{new_customer_data}} (acquisition date, first order value, acquisition channel)
LTV data: {{ltv_data}}

1. CAC calculation:
 CAC = Total Acquisition Spend / New Customers Acquired
 - Blended CAC: all channels combined
 - Channel CAC: paid search, paid social, email, influencer, affiliate, organic (fully-loaded)
 - Organic CAC: allocate content, SEO, and brand spend to organic-acquired customers
 - New customer only: exclude existing customer marketing spend from the CAC numerator

2. CAC payback period:
 Payback = CAC / (Monthly Gross Profit per New Customer)
 - Target for e-commerce: < 12 months
 - At current gross margin and purchase frequency: how many months to recover the acquisition cost?

3. LTV / CAC ratio by channel:
 - 12-month LTV and 24-month LTV per acquisition channel
 - LTV / CAC ratio per channel
 - Healthy benchmark: > 3x
 - Channels with LTV/CAC < 1: losing money on every customer acquired

4. Cohort-based payback curves:
 - For customers acquired in the last 6 cohorts: cumulative gross profit over time
 - At what month does each cohort recover its CAC?
 - Are newer cohorts recovering faster or slower? (Faster = improving efficiency)

5. Customer quality by channel:
 - Second purchase rate by acquisition channel (% making a second purchase within 90 days)
 - Average order frequency in year 1 by channel
 - Churn rate (no purchase in > 180 days) by channel
 - Channels bringing high-volume but low-quality customers: reconsider spending

6. Budget allocation implications:
 - Which channels should receive more budget based on LTV/CAC?
 - Which channels are over-funded relative to their LTV/CAC?
 - Maximum viable CAC per channel = Target LTV/CAC ratio x 12-month LTV

Return: CAC by channel, payback analysis, LTV/CAC ratios, cohort payback curves, customer quality metrics, and budget allocation recommendations. Copy prompt Open prompt details Beginner Single prompt 02 
### Customer Lifetime Value Analysis 

Calculate and segment Customer Lifetime Value (LTV) for this e-commerce business. Order data: {{order_data}} (customer_id, order_date, order_value, product_category) Time period... 
Prompt text Calculate and segment Customer Lifetime Value (LTV) for this e-commerce business.

Order data: {{order_data}} (customer_id, order_date, order_value, product_category)
Time period: {{period}}
Business model: {{business_model}} (single purchase, subscription, repeat purchase)

1. Basic LTV metrics:
 - Average Order Value (AOV): total revenue / total orders
 - Purchase frequency: orders per customer per year
 - Customer lifespan: average months from first to last purchase (or 1 / annual churn rate)
 - Simple LTV = AOV x Purchase Frequency x Customer Lifespan
 - Gross profit LTV: multiply by gross margin %

2. Cohort-based LTV:
 - Group customers by acquisition month
 - For each cohort: cumulative revenue per customer through months 1, 3, 6, 12, 24
 - LTV curve: how does cumulative revenue grow over time?
 - At what month does the cohort LTV begin to plateau?

3. LTV by acquisition channel:
 - Which channel brings customers with the highest 12-month LTV?
 - Which brings the most orders per customer? Which brings the highest AOV?
 - Compare to CAC by channel: LTV/CAC ratio per channel

4. LTV by first product category:
 - Do customers who first purchase from category A have higher LTV than category B?
 - Category with highest LTV first purchase: prioritize in acquisition marketing

5. LTV by customer segment:
 - One-time buyers (only 1 order): how many and what % of customers? What is their share of revenue?
 - Repeat buyers (2-4 orders): their LTV vs one-time buyers
 - Loyal customers (5+ orders): their LTV, AOV, and frequency vs average

6. Second purchase conversion:
 - What % of first-time buyers make a second purchase within 90 days?
 - Time to second purchase distribution
 - The second purchase is the most predictive event for long-term retention
 - What drives second purchase? (Category, time since first, email trigger)

Return: LTV metrics table, cohort curves, channel LTV comparison, category LTV analysis, segment breakdown, and second-purchase insights. Copy prompt Open prompt details Intermediate Single prompt 03 
### Repeat Purchase and Retention Analysis 

Analyze repeat purchase behavior and design a retention improvement strategy. Order data: {{order_data}} Customer base: {{customer_count}} total customers Business goal: {{goal}... 
Prompt text Analyze repeat purchase behavior and design a retention improvement strategy.

Order data: {{order_data}}
Customer base: {{customer_count}} total customers
Business goal: {{goal}} (increase purchase frequency or reduce time between orders)

1. Repeat purchase metrics:
 - First-time buyer %: customers with only 1 order
 - Repeat buyer %: customers with 2+ orders
 - Loyal buyer %: customers with 5+ orders
 - % of revenue from repeat vs first-time buyers
 - If > 70% of revenue is from first-time buyers: the business depends on constant acquisition (expensive)

2. Time between purchases:
 - Median days between order 1 and order 2
 - Median days between order 2 and order 3
 - Does the inter-purchase interval increase or decrease with order number?
 - Purchase interval by product category (frequency-based categories vs occasion-based)

3. Second purchase conversion:
 - % of first-time buyers who make a second purchase within 30, 60, 90, 180 days
 - Second purchase conversion rate by acquisition channel
 - Second purchase conversion rate by first product category purchased
 - The single most important metric for retention: getting the first repeat purchase

4. Replenishment cycle analysis:
 - For consumable products: average repurchase interval per SKU
 - Products with predictable repurchase cycles (coffee, supplements, skincare)
 - These products are candidates for subscription programs

5. Churn definition and rate:
 - Define active customer: purchased in last {{active_window}} days
 - Churn: not active by this definition
 - Monthly churn rate: (customers at risk of churning who actually churn) / at-risk customers

6. Retention program recommendations:
 - Post-purchase email: trigger {{days}} days before expected next purchase based on category interval
 - Loyalty points: reward repeat purchases to incentivize second order
 - Subscription upsell: offer subscribe-and-save for products with predictable repurchase cycles
 - Win-back: at {{days}} days since last purchase, trigger win-back with incentive

Return: repeat purchase metrics, time-to-repurchase analysis, second purchase conversion, churn rate, and retention program recommendations. Copy prompt Open prompt details Intermediate Single prompt 04 
### Returns and Refunds Analysis 

Analyze product returns and refunds to identify root causes and financial impact. Returns data: {{returns_data}} (order_id, product_id, return_reason, return_date, refund_amount... 
Prompt text Analyze product returns and refunds to identify root causes and financial impact.

Returns data: {{returns_data}} (order_id, product_id, return_reason, return_date, refund_amount)
Order data: {{order_data}}

1. Returns overview:
 - Return rate: returns / orders (by units and by order value)
 - Industry average by category: apparel 20-30%, electronics 5-10%, home goods 5-8%
 - How does this store compare?
 - Cost of returns: shipping + processing + inventory write-down as % of revenue

2. Return rate by product and category:
 - Products with highest return rates
 - Are certain categories structurally high-return? (Size/fit issues in apparel)
 - Products with increasing return rates: product quality issue or misleading listing?

3. Return reason analysis:
 - Classify return reasons: wrong size, defective/damaged, not as described, changed mind, arrived late
 - Volume and % for each reason
 - Controllable vs uncontrollable returns:
 - Controllable: not as described, wrong item sent, defective → operational fix
 - Uncontrollable: changed mind, wrong size ordered → policy and content optimization

4. Financial impact:
 - Gross return rate: returns / gross revenue
 - Net revenue = gross revenue - refunds
 - Contribution margin impact: for each return, the contribution margin of that order is lost, plus return cost
 - Annual cost of returns in dollars

5. Return prevention opportunities:
 - 'Not as described' returns → improve product descriptions, add more images, size guides
 - 'Wrong size' returns → add size recommendation feature or chat assistant
 - 'Defective' returns → supplier quality review
 - Products with > 25% return rate: review listing accuracy and product quality

6. Return policy analysis:
 - Does the current return policy drive returns? (e.g. free returns may incentivize 'bracket buying')
 - What would be the financial impact of moving from 30-day to 14-day return window?

Return: returns overview, product/category return rates, reason analysis, financial impact, prevention opportunities, and policy analysis. Copy prompt Open prompt details Intermediate Single prompt 05 
### RFM Segmentation for E-commerce 

Build an RFM (Recency, Frequency, Monetary) segmentation model for this e-commerce customer base. Order data: {{order_data}} (customer_id, order_date, order_value) Analysis date... 
Prompt text Build an RFM (Recency, Frequency, Monetary) segmentation model for this e-commerce customer base.

Order data: {{order_data}} (customer_id, order_date, order_value)
Analysis date: {{analysis_date}}
Total customers: {{customer_count}}

1. RFM metric computation:
 For each customer:
 - Recency (R): days since most recent purchase
 - Frequency (F): total number of orders
 - Monetary (M): total revenue generated

2. Quintile scoring:
 - Rank all customers on each dimension from 1 (worst) to 5 (best)
 - R score: 5 = purchased most recently, 1 = purchased least recently
 - F score: 5 = highest order frequency
 - M score: 5 = highest total spend
 - Combined RFM score: concatenate the three scores (e.g. '555', '411', '123')

3. Segment definition:
 - Champions (RFM 444-555): bought recently, buy often, high spend
 - Loyal Customers (R3-5, F3-5, M3-5): frequent but not cutting-edge recency
 - Potential Loyalists (R4-5, F1-2, M1-3): recent but low frequency - new customers showing promise
 - At-Risk (R1-2, F3-5, M3-5): used to be great customers but haven't bought recently
 - Can't Lose Them (R1, F4-5, M4-5): previously highest-value, now gone
 - Hibernating (R1-2, F1-2, M1-2): low on all dimensions
 - Lost (R1, F1, M1): low on all, no recent activity

4. Segment sizing and value:
 - Count and % of customers in each segment
 - Total revenue and % of revenue per segment
 - Average AOV and purchase frequency per segment

5. Marketing actions per segment:
 - Champions: VIP treatment, loyalty program invitation, referral ask
 - At-Risk: re-engagement campaign, exclusive offer, personal outreach for high-value
 - Can't Lose Them: win-back campaign with strong offer, survey why they left
 - Hibernating: last-chance reactivation email before sunset
 - Potential Loyalists: second-purchase nurture, loyalty points accelerator

6. Segment migration tracking:
 - Run the RFM model monthly
 - Track how many customers move between segments
 - Net migration to Champions: leading indicator of business health

Return: RFM scoring methodology, segment definitions and sizes, revenue contribution table, marketing actions per segment, and migration tracking plan. Copy prompt Open prompt details 
## Recommended Customer Analytics workflow 
1 
### Customer Acquisition Cost Analysis 

Start with a focused prompt in Customer Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Customer Lifetime Value Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Repeat Purchase and Retention Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Returns and Refunds Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
