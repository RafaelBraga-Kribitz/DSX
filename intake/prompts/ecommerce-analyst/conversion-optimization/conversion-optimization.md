# Conversion Optimization *AI Prompts *

5 Ecommerce Analyst prompts in Conversion Optimization. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts · 1 chain. 

## AI prompts in Conversion Optimization 
5 prompts Intermediate Single prompt 01 
### Checkout Abandonment Recovery 

Analyze checkout abandonment and design a recovery strategy. Checkout data: {{checkout_data}} CartAbandonment rate: {{abandonment_rate}} Average order value: {{aov}} 1. Abandonm... 
Prompt text Analyze checkout abandonment and design a recovery strategy.

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

Return: step-by-step abandonment analysis, root cause hypothesis, immediate fixes, email sequence design, and revenue recovery estimate. Copy prompt Open prompt details Beginner Single prompt 02 
### E-commerce Conversion Funnel Audit 

Audit the e-commerce conversion funnel from landing to purchase and identify the highest-priority optimization opportunities. Funnel data: {{funnel_data}} Platform: {{platform}}... 
Prompt text Audit the e-commerce conversion funnel from landing to purchase and identify the highest-priority optimization opportunities.

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

Return: funnel metrics table, abandonment analysis, device breakdown, product page analysis, checkout friction assessment, and prioritized recommendations. Copy prompt Open prompt details Advanced Chain 03 
### Full E-commerce Analytics Chain 

Step 1: Revenue attribution audit - review the attribution model in use. Identify if it is accurately crediting channels, including the impact of dark social and direct traffic.... 
Prompt text Step 1: Revenue attribution audit - review the attribution model in use. Identify if it is accurately crediting channels, including the impact of dark social and direct traffic. Recommend attribution improvements.
Step 2: Conversion funnel audit - map the full conversion funnel from session to purchase. Identify the top 3 drop-off points. Segment the funnel by device, traffic source, and new vs returning.
Step 3: Customer segmentation - build RFM segments for the full customer base. Size each segment, compute revenue contribution, and define the marketing action for each tier. Identify the At-Risk and Can't Lose Them segments as top priority.
Step 4: Product analytics - apply the product performance matrix (traffic vs conversion). Identify the top 10 Hidden Gems to promote and the top 5 high-traffic, low-conversion pages to fix.
Step 5: Pricing and promotion review - compute the revenue and margin impact of the last 3 promotions. Test whether any products are candidates for a price increase based on elasticity signals. Review discount addiction indicators.
Step 6: Retention strategy - compute the second-purchase conversion rate and the average time between orders by category. Design a post-purchase email flow with specific timing and content for the top 3 product categories.
Step 7: 90-day growth plan - synthesize findings into a prioritized growth plan: top 3 conversion improvements, top 3 retention actions, and top 2 acquisition efficiency improvements. For each: expected revenue impact, required investment, and measurement plan. Copy prompt Open prompt details Advanced Single prompt 04 
### Personalization Opportunity Analysis 

Identify and prioritize personalization opportunities to improve conversion and customer experience. Customer data: {{customer_data}} Behavioral data: {{behavioral_data}} Curren... 
Prompt text Identify and prioritize personalization opportunities to improve conversion and customer experience.

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

Return: personalization opportunity map, value estimates, data requirements, quick win implementations, and measurement framework. Copy prompt Open prompt details Intermediate Single prompt 05 
### Product Page Optimization 

Analyze product page performance and identify conversion optimization opportunities. Product page data: {{product_page_data}} (traffic, add-to-cart rate, purchase rate, heatmap... 
Prompt text Analyze product page performance and identify conversion optimization opportunities.

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

Return: product page metrics table, above-the-fold assessment, image and content analysis, social proof audit, and A/B test backlog. Copy prompt Open prompt details 
## Recommended Conversion Optimization workflow 
1 
### Checkout Abandonment Recovery 

Start with a focused prompt in Conversion Optimization so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### E-commerce Conversion Funnel Audit 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Full E-commerce Analytics Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Personalization Opportunity Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
