# Ecommerce Analyst *AI Prompts *

Ecommerce Analyst AI prompt library with 20 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Ecommerce Analyst prompt categories 
5 categories 
### Conversion Optimization 

AI prompts for conversion optimization, including funnel diagnostics, friction-point identification, and experiment-ready improvement opportunities. 
5 prompts Checkout Abandonment Recovery E-commerce Conversion Funnel Audit → 
### Customer Analytics 

AI prompts for customer analytics, including behavior patterns, value segmentation, lifecycle analysis, and actionable customer insight generation. 
5 prompts Customer Acquisition Cost Analysis Customer Lifetime Value Analysis → 
### Merchandising Analytics 

AI prompts for merchandising analytics, including assortment performance, pricing dynamics, inventory effects, and category-level optimization. 
4 prompts Cross-Sell and Upsell Analysis Inventory Analytics → 
### Pricing Analytics 

AI prompts for pricing analytics, including elasticity signals, discount impact, margin trade-offs, and pricing strategy recommendations. 
3 prompts Discount and Promotion Analysis Dynamic Pricing Strategy → 
### Traffic and Acquisition Analytics 

AI prompts for traffic and acquisition analytics, including source quality, channel mix, conversion pathways, and budget efficiency. 
3 prompts Affiliate and Influencer Analytics E-commerce Traffic Source Analysis → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 20 Conversion Optimization 5 Customer Analytics 5 Merchandising Analytics 4 Pricing Analytics 3 Traffic and Acquisition Analytics 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **20 **of 20 prompts 
## Conversion Optimization 
5 prompt s Conversion Optimization Intermediate Prompt 01 
### Checkout Abandonment Recovery 
Analyze checkout abandonment and design a recovery strategy.

Checkout data: {{checkout_data}}
CartAbandonment rate: {{abandonment_rate}}
Average order value: {{aov}}

1. Abandonment by checkout step:
 Which steps lose the most customers?
 - Step 1 (Enter email/sign up): high drop here = account creation friction
 - Step 2 (Shipping details): drop here = unexpected shipping cost or complexity
 - Step 3 (Payment details): drop here = trust or payment method issue
 - Step 4 (Order review): drop here = final price concern or last-minute doubt
 Map drop-off rate at each step.

2. Abandonment reasons (from exit surveys or user research):
 - Unexpected shipping costs (primary reason cited in ~50% of cases)
 - Forced account creation
 - Complicated checkout process
 - Payment security concerns
 - Just browsing / not ready to buy
 - Found a better price elsewhere
 Which of these apply based on the data signals?

3. Immediate fix opportunities (no A/B test required):
 - Show shipping cost early: display on product page and cart, before checkout
 - Enable guest checkout: remove account requirement or make it optional after purchase
 - Add trust signals: SSL badge, money-back guarantee, security certifications near payment field
 - Reduce form fields: remove any non-required fields
 - Save progress: if user leaves, preserve their cart and form data

4. Cart abandonment email sequence:
 Email 1 (1 hour after abandonment):
 - Subject: 'You left something behind'
 - Content: items in cart, strong CTA, no discount yet
 - Goal: recapture the 30% who abandoned due to distractions

 Email 2 (24 hours):
 - Subject: 'Your cart is waiting - and here's 10% off'
 - Content: discount offer with urgency (expires in 48 hours)
 - Goal: recapture price-sensitive abandoners

 Email 3 (72 hours):
 - Subject: 'Last chance - your cart expires soon'
 - Content: urgency reminder, social proof on the products

5. Recovery revenue estimate:
 - Current recovered revenue from email sequence (if any)
 - Expected recovery rate with optimized sequence: industry benchmark 10-15% of abandoned carts
 - Annual revenue opportunity: abandonment volume x AOV x expected recovery rate

Return: step-by-step abandonment analysis, root cause hypothesis, immediate fixes, email sequence design, and revenue recovery estimate. Copy prompt View page Show more ↓ Conversion Optimization Beginner Prompt 02 
### E-commerce Conversion Funnel Audit 
Audit the e-commerce conversion funnel from landing to purchase and identify the highest-priority optimization opportunities.

Funnel data: {{funnel_data}}
Platform: {{platform}} (Shopify, WooCommerce, Magento, custom)
Traffic: {{monthly_sessions}} monthly sessions

1. Funnel stages and current conversion rates:
 - Session to Product View rate: sessions that viewed at least one product page
 - Product View to Add-to-Cart rate
 - Add-to-Cart to Checkout Initiation rate
 - Checkout Initiation to Purchase rate (checkout completion)
 - Overall session-to-purchase conversion rate

 Benchmark comparison by device:
 - Desktop: typical e-commerce CVR 2-4%
 - Mobile: typical e-commerce CVR 1-2%
 - How does this store compare?

2. Cart abandonment analysis:
 - Cart abandonment rate: (add-to-cart - purchases) / add-to-cart
 - Industry average: ~70%. If > 80%, significant optimization opportunity.
 - Checkout abandonment rate: where in the checkout flow do users leave?
 - Most common exit pages during checkout

3. Device and traffic source breakdown:
 - Conversion rate by device (desktop, mobile, tablet)
 - Conversion rate by traffic source (organic, paid, email, direct, social)
 - Which combination (source x device) has the highest and lowest CVR?
 - Mobile CVR vs desktop CVR gap: if > 50% lower on mobile, mobile UX is the priority

4. Product page conversion rate:
 - Add-to-cart rate by product category
 - Products with high traffic but low add-to-cart rate (< 5%): page or product issue?
 - Products with high add-to-cart but low purchase rate: cart abandonment issue for specific products

5. Checkout friction analysis:
 - How many steps in the checkout? (Target: 1-2 pages)
 - Is guest checkout available? (Forced account creation kills mobile conversions)
 - Payment options: does the store offer the top payment methods for its audience?
 - Form fields: any unnecessary fields that slow completion?

6. Priority recommendations:
 - Top 3 interventions by expected revenue impact
 - Expected lift in CVR for each intervention
 - Estimated annual revenue gain from each 0.1% CVR improvement at current traffic

Return: funnel metrics table, abandonment analysis, device breakdown, product page analysis, checkout friction assessment, and prioritized recommendations. Copy prompt View page Show more ↓ Conversion Optimization Advanced Chain 03 
### Full E-commerce Analytics Chain 
Step 1: Revenue attribution audit - review the attribution model in use. Identify if it is accurately crediting channels, including the impact of dark social and direct traffic. Recommend attribution improvements.
Step 2: Conversion funnel audit - map the full conversion funnel from session to purchase. Identify the top 3 drop-off points. Segment the funnel by device, traffic source, and new vs returning.
Step 3: Customer segmentation - build RFM segments for the full customer base. Size each segment, compute revenue contribution, and define the marketing action for each tier. Identify the At-Risk and Can't Lose Them segments as top priority.
Step 4: Product analytics - apply the product performance matrix (traffic vs conversion). Identify the top 10 Hidden Gems to promote and the top 5 high-traffic, low-conversion pages to fix.
Step 5: Pricing and promotion review - compute the revenue and margin impact of the last 3 promotions. Test whether any products are candidates for a price increase based on elasticity signals. Review discount addiction indicators.
Step 6: Retention strategy - compute the second-purchase conversion rate and the average time between orders by category. Design a post-purchase email flow with specific timing and content for the top 3 product categories.
Step 7: 90-day growth plan - synthesize findings into a prioritized growth plan: top 3 conversion improvements, top 3 retention actions, and top 2 acquisition efficiency improvements. For each: expected revenue impact, required investment, and measurement plan. Copy prompt View page Show more ↓ Conversion Optimization Advanced Prompt 04 
### Personalization Opportunity Analysis 
Identify and prioritize personalization opportunities to improve conversion and customer experience.

Customer data: {{customer_data}}
Behavioral data: {{behavioral_data}}
Current personalization capabilities: {{current_capabilities}}

1. Personalization opportunity inventory:
 Where can personalization improve the experience?
 - Homepage hero: show category or product relevant to the visitor's history
 - Product recommendations: 'Recommended for you' based on browse/purchase history
 - Search results: personalized ranking based on category preferences
 - Email content: dynamically insert products based on browse history
 - Pricing/offer: segment-specific offers (first-time buyer discount vs loyalty reward)
 - Category landing: reorder products based on the visitor's likely preferences

2. Personalization value estimation:
 For each opportunity:
 - Baseline performance of the non-personalized version
 - Expected lift from personalization (cite studies or similar implementations)
 - Traffic volume affected
 - Estimated incremental revenue = Traffic x Baseline CVR x Expected Lift x AOV

3. Data requirements per opportunity:
 - What data is needed? (Purchase history, browse history, declared preferences, segment membership)
 - Is this data available and accessible in real-time?
 - Any privacy or consent requirements? (GDPR, CCPA)

4. Quick wins (no ML required):
 - New vs returning: show a 'welcome back' message and recently viewed products for returning users
 - Geo-based: show regionally relevant products or shipping estimates based on IP location
 - Cart-based: upsell products based on cart contents (highest affinity pair from market basket analysis)
 - Email click-based: if user clicked category X in last email, show category X products next time

5. Advanced personalization (requires ML or CDP):
 - Collaborative filtering: 'customers like you also bought'
 - Propensity scoring: predict likelihood to buy each product and rank recommendations accordingly
 - Churn prediction-based offers: detect at-risk customers and trigger a personalized retention offer

6. Measurement plan:
 For each personalization implementation:
 - Control group: show non-personalized version to 10-20% of users
 - Measure: CVR, AOV, and revenue per visitor
 - Minimum duration: 2 weeks, minimum conversions per variant: 100

Return: personalization opportunity map, value estimates, data requirements, quick win implementations, and measurement framework. Copy prompt View page Show more ↓ Conversion Optimization Intermediate Prompt 05 
### Product Page Optimization 
Analyze product page performance and identify conversion optimization opportunities.

Product page data: {{product_page_data}} (traffic, add-to-cart rate, purchase rate, heatmap data)
Top products to analyze: {{product_list}}

1. Product page conversion hierarchy:
 - Views to Add-to-Cart rate by product (benchmark: 5-15% for most categories)
 - Add-to-Cart to Purchase rate (measures checkout conversion for this specific product)
 - Page exit rate before any engagement

2. Above-the-fold analysis:
 - Do the primary product images load quickly? (LCP < 2.5 seconds)
 - Is the price visible without scrolling?
 - Is the primary CTA (Add to Cart) visible without scrolling?
 - Is the product name and key value proposition immediately clear?
 - What does the heatmap show for click and scroll distribution?

3. Product image quality signals:
 - Number of images: research shows > 3 images increases conversion
 - Image types: do they include: hero shot, lifestyle image, detail/zoom, 360/video?
 - Mobile image display: do images load quickly and display correctly on mobile?

4. Product description analysis:
 - Is the primary benefit stated in the first sentence?
 - Are technical specifications separated from benefits?
 - Is social proof (review count, rating) prominently displayed near the CTA?
 - Is shipping information and return policy visible on the product page?

5. Social proof signals:
 - Review count and average rating visible near Add-to-Cart
 - User-generated content (UGC) or customer photos
 - 'X people are viewing this' or 'Only 3 left in stock' urgency signals
 - Are these signals accurate and trustworthy? (Fake scarcity damages trust)

6. Low-performing product deep dive:
 For each product with add-to-cart rate < 3%:
 - Is the price competitive vs comparable products?
 - Is the primary concern a product quality issue or a page presentation issue?
 - What do the top 10 reviews say? Any consistent complaints?

7. A/B test backlog for product pages:
 - 5 specific tests ranked by expected impact on add-to-cart rate

Return: product page metrics table, above-the-fold assessment, image and content analysis, social proof audit, and A/B test backlog. Copy prompt View page Show more ↓ 
## Customer Analytics 
5 prompt s Customer Analytics Advanced Prompt 01 
### Customer Acquisition Cost Analysis 
Analyze customer acquisition costs and LTV/CAC ratios across channels for this e-commerce business.

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

Return: CAC by channel, payback analysis, LTV/CAC ratios, cohort payback curves, customer quality metrics, and budget allocation recommendations. Copy prompt View page Show more ↓ Customer Analytics Beginner Prompt 02 
### Customer Lifetime Value Analysis 
Calculate and segment Customer Lifetime Value (LTV) for this e-commerce business.

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

Return: LTV metrics table, cohort curves, channel LTV comparison, category LTV analysis, segment breakdown, and second-purchase insights. Copy prompt View page Show more ↓ Customer Analytics Intermediate Prompt 03 
### Repeat Purchase and Retention Analysis 
Analyze repeat purchase behavior and design a retention improvement strategy.

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

Return: repeat purchase metrics, time-to-repurchase analysis, second purchase conversion, churn rate, and retention program recommendations. Copy prompt View page Show more ↓ Customer Analytics Intermediate Prompt 04 
### Returns and Refunds Analysis 
Analyze product returns and refunds to identify root causes and financial impact.

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

Return: returns overview, product/category return rates, reason analysis, financial impact, prevention opportunities, and policy analysis. Copy prompt View page Show more ↓ Customer Analytics Intermediate Prompt 05 
### RFM Segmentation for E-commerce 
Build an RFM (Recency, Frequency, Monetary) segmentation model for this e-commerce customer base.

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

Return: RFM scoring methodology, segment definitions and sizes, revenue contribution table, marketing actions per segment, and migration tracking plan. Copy prompt View page Show more ↓ 
## Merchandising Analytics 
4 prompt s Merchandising Analytics Intermediate Prompt 01 
### Cross-Sell and Upsell Analysis 
Analyze cross-sell and upsell opportunities to increase average order value and customer LTV.

Order data: {{order_data}} (order_id, customer_id, product_ids, quantities, values)
Product catalog: {{catalog}}

1. Market basket analysis:
 Compute product affinity using association rules:
 - Support: % of orders containing both product A and product B
 - Confidence: given product A, what % of those orders also contain product B?
 - Lift: how much more likely is product B in the basket given product A (vs random chance)?
 Lift > 1: products are bought together more than by chance

 Find the top 20 product pairs by lift score (minimum support = 1% of orders, minimum confidence = 20%)

2. Category cross-sell patterns:
 - Which pairs of product categories are most frequently purchased together?
 - Which categories are under-crosssold? (Frequently ordered independently but rarely together)
 - Are there natural product bundles the data suggests?

3. Sequential purchase analysis:
 - After purchasing product A, what does the customer buy in their next order?
 - Time between purchase A and related purchase B: how long do we have to suggest the cross-sell?
 - This drives post-purchase email timing and content

4. Upsell opportunities:
 - Products where customers frequently upgrade to a higher-priced variant after initial purchase
 - Product categories where the second purchase is at a higher price point than the first
 - Which products serve as 'entry points' that lead to higher-value subsequent purchases?

5. Bundle creation recommendations:
 - Based on affinity analysis: top 5 product bundle opportunities
 - For each bundle: expected AOV lift, current % of customers who buy both individually
 - Bundle pricing strategy: slight discount vs individual sum (3-7% discount typical)

6. Implementation recommendations:
 - Product page 'Frequently Bought Together': use top affinity pairs
 - Cart page 'Add to your order': show the highest-confidence cross-sell for items in cart
 - Post-purchase email: trigger with the sequential purchase insight (timing and product)
 - Bundle listings: create bundles for top affinity pairs

Return: top association rules table, category cross-sell matrix, sequential purchase analysis, upsell patterns, bundle recommendations, and implementation priorities. Copy prompt View page Show more ↓ Merchandising Analytics Advanced Prompt 02 
### Inventory Analytics 
Analyze inventory performance and identify stock-out and overstock risks.

Inventory data: {{inventory_data}} (SKU, units_on_hand, daily_sales_rate, lead_time_days, reorder_point)
Sales data: {{sales_data}}

1. Inventory coverage analysis:
 - Days of Inventory Outstanding (DIO): units_on_hand / average_daily_sales_rate
 - Flag: DIO > 90 days = likely overstock
 - Flag: DIO < 14 days = reorder urgently (below safety stock for most lead times)
 - Distribution of DIO across the catalog

2. Stock-out risk assessment:
 - Products with DIO < lead_time_days: will stock out before reorder arrives
 - Products currently at zero inventory: lost sales occurring now
 - Lost revenue estimate from out-of-stocks:
 Out-of-stock loss = (days_out_of_stock x average_daily_revenue_when_in_stock)

3. Overstock identification:
 - Products with DIO > 90 days: cash and storage tied up unproductively
 - Total overstock value: units_excess x unit_cost (units_excess = inventory - 90 days supply)
 - Products with declining sales trend: overstock risk is growing over time

4. Reorder point calculation:
 Reorder Point = (Average Daily Sales x Lead Time) + Safety Stock
 Safety Stock = Z x Standard Deviation of Demand x sqrt(Lead Time)
 - Z = 1.65 for 95% service level, 2.05 for 98%
 - Compare current reorder points to calculated optimal reorder points

5. ABC classification:
 - A items: top 20% of products by revenue (80% of revenue) - high control
 - B items: next 30% of products (15% of revenue) - moderate control
 - C items: bottom 50% of products (5% of revenue) - minimal control
 - A items should never stock out; C items can have lower service levels

6. Inventory optimization actions:
 - Immediate: order products in stock-out risk category
 - Short term: markdown or bundle overstock items to release cash
 - Medium term: revise reorder points and safety stock levels for top-50 SKUs

Return: DIO distribution, stock-out risk list with lost revenue, overstock list with excess value, optimized reorder points, ABC classification, and action priorities. Copy prompt View page Show more ↓ Merchandising Analytics Intermediate Prompt 03 
### Product Catalog Performance Analysis 
Analyze the performance of the product catalog to identify best sellers, underperformers, and merchandising opportunities.

Product data: {{product_data}} (product_id, category, views, add-to-cart, orders, revenue, margin, inventory)
Time period: {{period}}

1. Revenue and margin contribution:
 - Pareto analysis: what % of products generate 80% of revenue? (Typically 20%)
 - Top 20 products by revenue contribution and their % of total
 - Top 20 products by gross margin contribution
 - Products where high revenue rank and high margin rank diverge: investigate

2. Product performance matrix (2x2):
 X-axis: Conversion rate (add-to-cart to purchase)
 Y-axis: Traffic (product page views)

 - High traffic, high conversion (Stars): protect and feature prominently
 - High traffic, low conversion (Opportunities): fix the page or review the product offering
 - Low traffic, high conversion (Hidden Gems): increase visibility, promote more
 - Low traffic, low conversion (Dogs): review for discontinuation or significant improvement

3. Category-level analysis:
 - Revenue, orders, and AOV by category
 - Category conversion rate (add-to-cart from category page)
 - Category growth: which categories are growing YoY? Which are declining?
 - Cross-category purchase patterns: which categories are most frequently bought together?

4. Inventory vs demand alignment:
 - Out-of-stock rate per product: % of time in stock-out during the period
 - Stock-out revenue impact: estimated lost sales from stock-outs on high-demand products
 - Overstock: products with > 90 days of inventory coverage at current sell rate

5. New vs established product performance:
 - Products launched in the last 90 days: are they ramping or stalling?
 - Products > 180 days old with declining traffic: content refresh or markdown needed?

6. Pricing analysis:
 - Products with lowest conversion rate in their category: is price a factor?
 - Price elasticity signals: any products where a discount drove disproportionate volume increase?

Return: Pareto analysis, product performance matrix, category analysis, inventory alignment, and pricing insights. Copy prompt View page Show more ↓ Merchandising Analytics Intermediate Prompt 04 
### Search and Discovery Analysis 
Analyze on-site search behavior and product discovery patterns to improve findability and merchandising.

Search data: {{search_data}} (search_term, frequency, click-through, add-to-cart, purchase)
Navigation data: {{navigation_data}}

1. Search usage metrics:
 - % of sessions using the search bar
 - Search users vs non-search users: conversion rate comparison
 - If search users convert at > 2x non-search users: search is a high-value entry point to optimize

2. Top search terms analysis:
 - Top 50 search terms by frequency
 - Click-through rate per search term: did the user find what they were looking for?
 - Add-to-cart rate per search term
 - Zero-results searches: searches that returned no results (high-priority fixes)

3. Zero-result and low-result searches:
 - What are customers searching for that the store does not carry?
 - Which zero-result searches represent a product gap opportunity?
 - Which low-result searches are caused by poor search configuration (typos, synonyms)?
 - Example: 'sneakers' returns 0 results but 'trainers' returns 200 (synonym issue)

4. Search-to-purchase funnel:
 - For the top 20 search terms: click rate, add-to-cart rate, and purchase rate
 - High search frequency but low purchase rate: search results not matching intent
 - Products receiving many searches but with low stock: restock priority

5. Category navigation analysis:
 - Which category pages have the highest bounce rate?
 - Click distribution on category pages: are users clicking the right products?
 - Category sort order: is the default sort (best sellers, new arrivals, featured) working?

6. Discovery optimization recommendations:
 - Add synonyms to search engine for top zero-result queries
 - Promote 'Hidden Gem' products (high conversion, low traffic) in search results and category pages
 - Create product collections or gift guides based on common search intent clusters
 - Improve autocomplete suggestions for top search terms

Return: search usage metrics, top and zero-result analysis, search-to-purchase funnel, category navigation insights, and discovery optimization recommendations. Copy prompt View page Show more ↓ 
## Pricing Analytics 
3 prompt s Pricing Analytics Intermediate Prompt 01 
### Discount and Promotion Analysis 
Analyze the effectiveness of discounts and promotions and optimize the promotional strategy.

Promotion data: {{promotion_data}} (promotion type, discount %, products, period, orders, revenue)
Baseline data: {{baseline_data}} (same period last year or non-promotional baseline)

1. Promotion performance metrics:
 For each promotion:
 - Revenue during promotion vs baseline (lift)
 - Gross margin during promotion vs baseline (margin impact)
 - Orders count and AOV during vs baseline
 - New vs returning customer mix during promotion

2. Revenue vs margin trade-off:
 - Revenue lift (%) from promotion
 - Gross profit change (%) from promotion (may be negative even if revenue is up)
 - Break-even volume: how much incremental volume is needed to offset the margin give-away?
 Break-even lift = Discount % / (Gross Margin % - Discount %)
 Example: 20% discount on a 40% margin product requires 100% volume increase to maintain gross profit

3. Promotion types comparison:
 - % off: drives broadest participation, margins most exposed
 - BOGO (Buy One Get One): volume driver, effective for high-margin products
 - Free shipping threshold: AOV driver (set threshold at 30% above current AOV)
 - Gift with purchase: drives specific product trial, protects revenue
 - Flash sale (time-limited): urgency driver, but trains customers to wait for discounts

4. Customer behavior post-promotion:
 - Are customers acquired during promotions at lower LTV than non-promotion customers?
 - Do promotional buyers return at similar or lower rates than full-price buyers?
 - Are existing customers simply shifting their planned purchases to discount periods?

5. Discount addiction signals:
 - Is there a trend toward increasing discount frequency to maintain revenue?
 - What % of revenue is generated at a discount?
 - Are customers waiting for promotions before purchasing? (Signal: conversion rate declines in weeks before promotions)

6. Optimized promotional calendar:
 - Based on analysis: which promotion types drive the best net margin impact?
 - Recommended promotional cadence: how often and at what depth?
 - Products that should never be promoted (inelastic, premium positioning)

Return: promotion performance table, break-even analysis, type comparison, post-promotion behavior analysis, discount addiction signals, and promotional calendar recommendation. Copy prompt View page Show more ↓ Pricing Analytics Advanced Prompt 02 
### Dynamic Pricing Strategy 
Design a data-driven dynamic pricing framework for this e-commerce business.

Product catalog: {{catalog}}
Demand data: {{demand_data}}
Competitor pricing feed: {{competitor_prices}} (if available)
Objective: {{objective}} (maximize revenue, maximize margin, protect market share)

1. Dynamic pricing applicability:
 Not all products are suitable for dynamic pricing. Score each category:
 - High suitability: commodity products, seasonal products, high price sensitivity, active competitor pricing changes
 - Low suitability: branded products, luxury, items where price stability builds trust

2. Demand-based pricing rules:
 Adjust price based on current demand signals:
 - High demand (sell-through rate > target): small price increase to protect margin
 - Low demand (sell-through rate < target): small price decrease to drive velocity
 - Near out-of-stock: price increase to ration remaining inventory
 - Overstock: price decrease to accelerate sell-through

3. Competitive pricing rules (if competitor data available):
 - Price matching rule: stay within 5% of the lowest verified competitor price for A-category products
 - Price leadership rule: for unique or differentiated products, ignore competitor pricing
 - Floor price: never go below the minimum margin threshold (cost + minimum margin %)

4. Time-based pricing:
 - Day-of-week elasticity: are there purchase patterns that suggest different price sensitivity by day?
 - Seasonal pricing: pre-season vs peak season vs clearance pricing for each category
 - End-of-season markdown schedule: structured markdown cadence as season ends

5. Guardrails and controls:
 - Maximum price change per day: ± 10% to avoid customer perception issues
 - Price floor per SKU: ensures margin is never destroyed
 - Minimum price stability: some products (premium, gift) should not fluctuate frequently
 - Human review threshold: any suggested price change > 20% requires human approval

6. Testing and measurement:
 - A/B test dynamic pricing vs static: randomize products into test and control
 - Measure: revenue per visit, gross margin %, sell-through rate
 - Be aware: customers on the same product may see different prices (manage perception risk)

Return: product category suitability matrix, demand-based and competitive pricing rules, time-based strategy, guardrails, and testing framework. Copy prompt View page Show more ↓ Pricing Analytics Intermediate Prompt 03 
### Price Elasticity and Optimization 
Analyze price sensitivity and identify optimal pricing for key products.

Sales and pricing data: {{pricing_data}} (product, price, units_sold, date)
Promotion history: {{promotion_data}}
Competitor pricing: {{competitor_prices}} (if available)

1. Price elasticity estimation:
 Price Elasticity of Demand (PED) = % change in quantity / % change in price
 - PED < -1: elastic demand (price decrease drives proportionally more volume)
 - PED > -1: inelastic demand (price changes have limited volume effect)
 - PED = -1: unit elastic

 Estimation approach:
 - Collect price change events (price increases, promotions, sales) for each product
 - Compare volume before and after each price change
 - Control for seasonality by using same period YoY or a holdout comparison

2. Revenue-maximizing price:
 At the estimated elasticity, the revenue-maximizing price is:
 Optimal Price = Marginal Cost / (1 + 1/PED)
 - Calculate for products with reliable elasticity estimates
 - Compare optimal price to current price: are products over or under-priced?

3. Margin-impact analysis:
 - If we raise price by 5%: at what elasticity does revenue decrease?
 - If revenue decreases but volume decreases proportionally less: gross profit may still increase
 - Calculate: (Price lift) x (Volume loss) = Net margin impact at different elasticity assumptions

4. Promotional discount analysis:
 - Which products historically show the highest volume lift from promotions?
 - What discount depth is needed to move volume without destroying margin?
 - Products where discount lift is < 20% volume increase: promotions destroy margin without compensating volume

5. Competitive pricing analysis:
 - Price index: our price / lowest competitor price per product
 - Products where we are more than 15% above the lowest competitor price and showing low conversion
 - Products where we are below average market price: potential for modest price increase

6. Pricing recommendations:
 - Products to test a price increase on (inelastic, below optimal price)
 - Products to review pricing strategy (elastic, above optimal price)
 - Promotional calendar recommendations based on elasticity

Return: elasticity estimates per product, revenue-maximizing price calculations, margin impact analysis, discount effectiveness, and pricing recommendations. Copy prompt View page Show more ↓ 
## Traffic and Acquisition Analytics 
3 prompt s Traffic and Acquisition Analytics Intermediate Prompt 01 
### Affiliate and Influencer Analytics 
Analyze affiliate and influencer channel performance for this e-commerce business.

Affiliate data: {{affiliate_data}} (affiliate_id, clicks, orders, revenue, commission)
Influencer data: {{influencer_data}} (creator_id, platform, post_date, promo_code, orders, revenue)
Commission rates: {{commission_rates}}

1. Affiliate performance metrics:
 For each affiliate:
 - Clicks, orders, conversion rate, revenue
 - Commission paid and commission rate
 - Net revenue = Revenue - Commission
 - ROAS (net): Net Revenue / Commission
 - Average order value from this affiliate's referrals
 - New vs returning customers referred

2. Affiliate quality analysis:
 - Affiliates with high click volume but low conversion: traffic quality issue (incentivized or misaligned audience)
 - Affiliates with high CVR and high AOV: premium partners, worth higher commission rates
 - Coupon code affiliates vs content affiliates: which generate higher new customer rates?
 - Coupon affiliates often capture customers who would have bought anyway (low incrementality)

3. Influencer performance:
 For each influencer post:
 - Impressions, reach, clicks (if tracked), orders attributed (promo code)
 - Revenue, EMV (Earned Media Value)
 - Cost per acquisition from influencer: fee / orders
 - Compare CPA to paid social CPA as a benchmark

4. Influencer content effectiveness:
 - Which content formats drove the most orders? (Reel vs story vs feed post vs YouTube)
 - Which platforms performed best for this product category?
 - Timing: how quickly do influencer-driven orders arrive? (Typically 48-72 hours peak, then decay)

5. Commission structure optimization:
 - Are commission rates optimized per affiliate tier?
 - Which affiliates would respond to a higher commission and generate enough incremental revenue?
 - Are any affiliates receiving high commissions without driving incremental customers?

6. Recommendations:
 - Top 5 affiliates to invest more in (performance-based tiering)
 - Affiliates to pause or restructure (low quality, possible fraud signals)
 - Influencer categories to scale based on performance analysis

Return: affiliate performance table, quality analysis, influencer performance metrics, commission optimization, and investment recommendations. Copy prompt View page Show more ↓ Traffic and Acquisition Analytics Intermediate Prompt 02 
### E-commerce Traffic Source Analysis 
Analyze traffic sources and their contribution to e-commerce revenue.

Analytics data: {{analytics_data}} (sessions, source/medium, channel, orders, revenue)
Time period: {{period}}
Marketing spend by channel: {{spend_data}}

1. Revenue by channel:
 - Revenue attributed by channel: organic search, paid search, direct, email, paid social, organic social, referral, affiliate
 - Each channel: sessions, orders, conversion rate, AOV, revenue
 - Revenue per session by channel (best efficiency metric for cross-channel comparison)

2. Channel conversion rate comparison:
 - Email typically converts at 2-5%: highest-converting channel
 - Organic search: 1-3%
 - Paid search (branded): 3-8%
 - Paid search (non-branded): 1-2%
 - Social (paid): 0.5-1.5%
 - Direct: 2-4%
 - How does each channel compare to these benchmarks?

3. Paid channel ROI:
 - For each paid channel: spend, attributed revenue, ROAS
 - True ROI (gross profit basis): (Revenue x Gross Margin - Spend) / Spend
 - Which paid channels have ROAS above the threshold to justify continued investment?

4. Organic vs paid balance:
 - Organic revenue as % of total: is the business too dependent on paid traffic?
 - Paid traffic shut-off risk: if all paid channels stopped tomorrow, what would revenue be?
 - Cost of revenue: what % of revenue is consumed by marketing spend?

5. New customer vs returning customer by channel:
 - Which channels drive new customers vs returning customers?
 - Channels bringing primarily returning customers: potential attribution issue (assisting role) or wasted prospecting spend

6. Traffic quality signals:
 - Bounce rate by channel
 - Pages per session by channel
 - Session duration by channel
 - Low-quality channels (high bounce, low engagement): review targeting and landing page alignment

Return: revenue by channel table, conversion rate benchmark comparison, paid channel ROI, organic vs paid balance, new vs returning mix, and traffic quality signals. Copy prompt View page Show more ↓ Traffic and Acquisition Analytics Advanced Prompt 03 
### Paid Search Performance Analysis 
Analyze Google Shopping and paid search performance for this e-commerce store.

Google Ads data: {{ads_data}} (campaign, ad group, keyword, impressions, clicks, conversions, revenue, spend)
Time period: {{period}}

1. Account-level performance:
 - Total spend, revenue, ROAS, and CPA
 - ROAS target: {{target_roas}} (typically 4-8x for e-commerce)
 - Is the account meeting the ROAS target? Overall and by campaign type?

2. Campaign type breakdown:
 - Branded search: keywords containing the brand name
 - Non-branded search: generic product and category keywords
 - Shopping campaigns: Google Shopping product listing ads
 - Performance Max: automated campaign type
 - ROAS and CPA per campaign type
 - Branded terms typically have very high ROAS (5-15x) but limited incrementality

3. Product/keyword performance:
 - Top 20 keywords/products by revenue
 - Bottom 20 keywords/products by ROAS (candidates for bid reduction or pause)
 - ROAS distribution: what % of spend is above / below the ROAS target?

4. Shopping campaign analysis:
 - Product feed health: any products disapproved or not showing?
 - Impression share: what % of available impressions are we capturing?
 - Lost impression share: due to budget vs due to rank
 - Top products by Shopping revenue and their Shopping CPA

5. Auction insights:
 - Who are the top auction competitors?
 - Impression share comparison vs competitors
 - Are we winning or losing on top-of-page rate?

6. Optimization opportunities:
 - Budget allocation: which campaigns are limited by budget but have high ROAS? Increase budget.
 - Bid adjustment: keywords with ROAS > 2x target: consider raising bids to capture more volume
 - Negative keywords: terms generating clicks but no conversions: add as negatives
 - Product feed improvements: products with high impressions but low CTR need title/image optimization

Return: account performance summary, campaign type breakdown, product/keyword analysis, Shopping health check, auction insights, and optimization recommendations. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
