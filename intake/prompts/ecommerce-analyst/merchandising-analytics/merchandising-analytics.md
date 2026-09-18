# Merchandising Analytics *AI Prompts *

4 Ecommerce Analyst prompts in Merchandising Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts. 

## AI prompts in Merchandising Analytics 
4 prompts Intermediate Single prompt 01 
### Cross-Sell and Upsell Analysis 

Analyze cross-sell and upsell opportunities to increase average order value and customer LTV. Order data: {{order_data}} (order_id, customer_id, product_ids, quantities, values)... 
Prompt text Analyze cross-sell and upsell opportunities to increase average order value and customer LTV.

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

Return: top association rules table, category cross-sell matrix, sequential purchase analysis, upsell patterns, bundle recommendations, and implementation priorities. Copy prompt Open prompt details Advanced Single prompt 02 
### Inventory Analytics 

Analyze inventory performance and identify stock-out and overstock risks. Inventory data: {{inventory_data}} (SKU, units_on_hand, daily_sales_rate, lead_time_days, reorder_point... 
Prompt text Analyze inventory performance and identify stock-out and overstock risks.

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

Return: DIO distribution, stock-out risk list with lost revenue, overstock list with excess value, optimized reorder points, ABC classification, and action priorities. Copy prompt Open prompt details Intermediate Single prompt 03 
### Product Catalog Performance Analysis 

Analyze the performance of the product catalog to identify best sellers, underperformers, and merchandising opportunities. Product data: {{product_data}} (product_id, category,... 
Prompt text Analyze the performance of the product catalog to identify best sellers, underperformers, and merchandising opportunities.

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

Return: Pareto analysis, product performance matrix, category analysis, inventory alignment, and pricing insights. Copy prompt Open prompt details Intermediate Single prompt 04 
### Search and Discovery Analysis 

Analyze on-site search behavior and product discovery patterns to improve findability and merchandising. Search data: {{search_data}} (search_term, frequency, click-through, add... 
Prompt text Analyze on-site search behavior and product discovery patterns to improve findability and merchandising.

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

Return: search usage metrics, top and zero-result analysis, search-to-purchase funnel, category navigation insights, and discovery optimization recommendations. Copy prompt Open prompt details 
## Recommended Merchandising Analytics workflow 
1 
### Cross-Sell and Upsell Analysis 

Start with a focused prompt in Merchandising Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Inventory Analytics 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Product Catalog Performance Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Search and Discovery Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
