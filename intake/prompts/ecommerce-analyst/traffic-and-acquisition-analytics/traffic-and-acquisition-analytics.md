# Traffic and Acquisition Analytics *AI Prompts *

3 Ecommerce Analyst prompts in Traffic and Acquisition Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Traffic and Acquisition Analytics 
3 prompts Intermediate Single prompt 01 
### Affiliate and Influencer Analytics 

Analyze affiliate and influencer channel performance for this e-commerce business. Affiliate data: {{affiliate_data}} (affiliate_id, clicks, orders, revenue, commission) Influen... 
Prompt text Analyze affiliate and influencer channel performance for this e-commerce business.

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

Return: affiliate performance table, quality analysis, influencer performance metrics, commission optimization, and investment recommendations. Copy prompt Open prompt details Intermediate Single prompt 02 
### E-commerce Traffic Source Analysis 

Analyze traffic sources and their contribution to e-commerce revenue. Analytics data: {{analytics_data}} (sessions, source/medium, channel, orders, revenue) Time period: {{perio... 
Prompt text Analyze traffic sources and their contribution to e-commerce revenue.

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

Return: revenue by channel table, conversion rate benchmark comparison, paid channel ROI, organic vs paid balance, new vs returning mix, and traffic quality signals. Copy prompt Open prompt details Advanced Single prompt 03 
### Paid Search Performance Analysis 

Analyze Google Shopping and paid search performance for this e-commerce store. Google Ads data: {{ads_data}} (campaign, ad group, keyword, impressions, clicks, conversions, reve... 
Prompt text Analyze Google Shopping and paid search performance for this e-commerce store.

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

Return: account performance summary, campaign type breakdown, product/keyword analysis, Shopping health check, auction insights, and optimization recommendations. Copy prompt Open prompt details 
## Recommended Traffic and Acquisition Analytics workflow 
1 
### Affiliate and Influencer Analytics 

Start with a focused prompt in Traffic and Acquisition Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### E-commerce Traffic Source Analysis 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Paid Search Performance Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
