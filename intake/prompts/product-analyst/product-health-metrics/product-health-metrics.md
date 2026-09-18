# Product Health Metrics *AI Prompts *

3 Product Analyst prompts in Product Health Metrics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 2 single prompts · 1 chain. 

## AI prompts in Product Health Metrics 
3 prompts Intermediate Single prompt 01 
### DAU/MAU Ratio Analysis 

Analyze the DAU/MAU ratio (stickiness) for this product and identify improvement opportunities. DAU and MAU data: {{engagement_data}} Product type: {{product_type}} Time period:... 
Prompt text Analyze the DAU/MAU ratio (stickiness) for this product and identify improvement opportunities.

DAU and MAU data: {{engagement_data}}
Product type: {{product_type}}
Time period: {{period}}

1. Stickiness calculation:
 - DAU/MAU ratio: daily_active_users / monthly_active_users x 100%
 - Industry benchmarks by product type:
 - Social/messaging: 40-70% (high daily habit)
 - Productivity/SaaS: 20-40%
 - E-commerce: 5-15% (purchase frequency dependent)
 - Gaming: 20-40%
 - How does this product compare to benchmark?

2. Trend analysis:
 - Plot DAU/MAU over the last 12 months
 - Is stickiness improving, declining, or stable?
 - Is DAU growing faster or slower than MAU? (DAU growing faster = improving stickiness)
 - Identify any inflection points and what caused them

3. Stickiness by segment:
 - DAU/MAU for: new users (< 30 days), established users (30-90 days), power users (> 90 days)
 - DAU/MAU by acquisition channel, plan type, company size
 - Which segment has the highest stickiness? What drives it?

4. Usage pattern analysis:
 - What is the distribution of active days per user per month?
 - Are users clustered into daily users, weekly users, and monthly users?
 - What does the 'weekly user' segment use the product for? (May reveal a different use case)

5. Stickiness drivers:
 - Which features correlate most strongly with daily return visits?
 - Do users who complete {{onboarding_action}} have higher stickiness?
 - Is there a usage threshold that separates sticky from non-sticky users?

Return: stickiness metrics, benchmark comparison, trend analysis, segment breakdown, and stickiness driver analysis. Copy prompt Open prompt details Advanced Chain 02 
### Full Product Analytics Chain 

Step 1: North Star definition - define or validate the North Star Metric for this product. Decompose it into Level 1 and Level 2 input metrics. Assign owners to each leaf metric... 
Prompt text Step 1: North Star definition - define or validate the North Star Metric for this product. Decompose it into Level 1 and Level 2 input metrics. Assign owners to each leaf metric.
Step 2: Growth accounting - apply the growth accounting framework to the last 12 months. Compute the quick ratio trend. Diagnose whether this is a new user, retention, or resurrection problem.
Step 3: Funnel audit - map the full acquisition-to-activation funnel. Identify the top 2 drop-off points. Segment the funnel by device, channel, and cohort.
Step 4: Retention analysis - build the cohort retention matrix. Compute Day 1, Day 7, and Day 30 retention by cohort. Identify whether newer cohorts are improving or declining.
Step 5: Feature adoption - for the top 3 features, compute adoption rates and time-to-first-use. Identify which feature has the strongest correlation with 30-day retention.
Step 6: User segmentation - segment users into at least 4 behavioral groups (Champions, At-risk, Dormant, New). Size each segment and compute its contribution to revenue or activity.
Step 7: Recommendations and roadmap - synthesize findings into a prioritized list of 5 product and analytics recommendations. For each: the problem it addresses, the expected impact, and the measurement plan. Copy prompt Open prompt details Beginner Single prompt 03 
### Product Health Dashboard Design 

Design a product health monitoring framework for {{product_name}}. Product type: {{product_type}} (SaaS, mobile app, marketplace, etc.) Business model: {{business_model}} Curren... 
Prompt text Design a product health monitoring framework for {{product_name}}.

Product type: {{product_type}} (SaaS, mobile app, marketplace, etc.)
Business model: {{business_model}}
Current data available: {{data_sources}}

1. AARRR metrics framework:
 Define the key metric for each stage:
 - Acquisition: how are users finding and signing up for the product? (CAC, sign-up rate, channel mix)
 - Activation: are new users experiencing the core value? (activation rate, time-to-value, onboarding completion)
 - Retention: are users coming back? (Day 1/7/30 retention, MAU/DAU ratio, churn rate)
 - Revenue: are users paying? (ARPU, MRR, conversion to paid, expansion revenue)
 - Referral: are users sharing? (NPS, referral rate, viral coefficient)

2. Leading vs lagging indicators:
 For each AARRR stage: identify one leading indicator (predicts future performance) and one lagging indicator (confirms past performance)

3. North Star Metric:
 - Define the single metric that best captures value delivered to users
 - It should be: measurable, predictive of revenue, influenceable by the team
 - Decompose it: what inputs drive the North Star? (Weekly Active Users x actions per user, for example)

4. Alert thresholds:
 - For each health metric: define the threshold that triggers an alert (e.g. Day 7 retention drops > 5% WoW)
 - Define monitoring frequency: real-time, daily, or weekly per metric

5. Dashboard layout:
 - Top section: North Star Metric + 4 AARRR headline numbers with WoW change
 - Middle section: retention cohort heatmap, funnel conversion rates
 - Bottom section: acquisition channel mix, revenue breakdown

Return: AARRR metric definitions, North Star decomposition, alert thresholds, and dashboard spec. Copy prompt Open prompt details 
## Recommended Product Health Metrics workflow 
1 
### DAU/MAU Ratio Analysis 

Start with a focused prompt in Product Health Metrics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Full Product Analytics Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Product Health Dashboard Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
