# Product Analyst *AI Prompts *

Product Analyst AI prompt library with 16 prompts in 7 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 7 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Product Analyst prompt categories 
7 categories 
### Funnel Analysis 

AI prompts for funnel analysis, including stage conversion diagnostics, dropout root causes, and prioritized opportunities for improvement. 
3 prompts Conversion Funnel Audit Funnel Segmentation Deep Dive → 
### Product Health Metrics 

AI prompts for product health metrics, including engagement quality, reliability indicators, retention outcomes, and metric framework design. 
3 prompts DAU/MAU Ratio Analysis Full Product Analytics Chain → 
### Experimentation 

AI prompts for experimentation workflows in machine learning, iterative testing, hypothesis validation, and model improvement cycles. 
2 prompts Experiment Readout Template Product Experiment Prioritization → 
### Feature Adoption 

AI prompts for feature adoption analysis, including activation patterns, usage cohorts, stickiness signals, and product opportunity identification. 
2 prompts Feature Adoption Analysis Feature Impact Assessment → 
### Growth Analytics 

AI prompts for growth analytics, including acquisition performance, activation health, retention drivers, and scalable growth strategy insights. 
2 prompts Growth Accounting Framework North Star Metric Decomposition → 
### Retention Analysis 

AI prompts for retention analysis, including cohort behavior, churn patterns, reactivation opportunities, and lifecycle optimization insights. 
2 prompts Churn Prediction Indicators User Retention Cohort Analysis → 
### User Segmentation 

AI prompts for user segmentation, including behavioral grouping, profile interpretation, and targeted product or messaging strategies. 
2 prompts Behavioral User Segmentation Power User Analysis → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 16 Funnel Analysis 3 Product Health Metrics 3 Experimentation 2 Feature Adoption 2 Growth Analytics 2 Retention Analysis 2 User Segmentation 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **16 **of 16 prompts 
## Funnel Analysis 
3 prompt s Funnel Analysis Beginner Prompt 01 
### Conversion Funnel Audit 
Audit the conversion funnel for {{product_flow}} and identify the highest-impact drop-off points.

Funnel stages provided: {{stages_and_counts}}

1. Compute conversion rates:
 - Step-by-step conversion rate: users_at_step_N / users_at_step_N-1
 - Cumulative conversion rate: users_at_each_step / users_at_top_of_funnel
 - Overall funnel conversion: bottom_of_funnel / top_of_funnel

2. Identify the biggest drop-offs:
 - Rank steps by absolute user loss (not just % drop)
 - Rank steps by % conversion rate (lowest = most leaky)
 - Flag any step with conversion rate below {{threshold}}%

3. Benchmark against industry standards:
 - What is a typical conversion rate for each step in {{industry}}?
 - Which steps are performing below benchmark?

4. Segment the funnel:
 - Break conversion rates by: new vs returning users, device (mobile/desktop), traffic source, user cohort
 - Which segments have the lowest conversion at the biggest drop-off step?
 - Are any segments converting exceptionally well? (Best practice to replicate)

5. Qualitative context:
 - For the top 2 drop-off steps: list 3 possible reasons users are leaving
 - What data would confirm or rule out each reason?

6. Prioritized recommendations:
 - Top 3 interventions ranked by expected impact on overall funnel conversion
 - For each: hypothesis, test design, and expected lift

Return: funnel table with conversion rates, drop-off ranking, segment breakdown, and prioritized recommendations. Copy prompt View page Show more ↓ Funnel Analysis Intermediate Prompt 02 
### Funnel Segmentation Deep Dive 
Analyze how conversion rates differ across key user segments in this funnel.

Funnel data: {{funnel_data}}
Segmentation dimensions: {{dimensions}} (e.g. acquisition channel, device, plan type, geography, user tenure)

1. Per-segment funnel tables:
 For each dimension, produce a funnel table showing conversion at every step broken out by segment value.
 Highlight: which segment has the highest overall conversion? Which has the lowest?

2. Segment-step interaction:
 - Are drop-off patterns consistent across segments, or does one segment struggle at a specific step?
 - Example: mobile users may convert well at sign-up but drop at payment entry
 - Identify any step where segment A converts at more than 2x segment B

3. Volume-weighted impact:
 - A segment with 5% conversion but only 2% of volume has low total impact
 - Compute: (segment volume %) x (conversion gap vs best segment) = impact score
 - Rank segments by impact score to prioritize where improvement matters most

4. Cohort conversion analysis:
 - Do users acquired in recent months convert better or worse than older cohorts?
 - Is there a trend suggesting the product is getting easier or harder to convert?

5. Statistical significance:
 - For the largest conversion gap between segments: run a proportion z-test
 - Is the difference significant (p < 0.05) or within random variation?

6. Recommendations:
 - Which segment should be targeted for conversion improvement first and why?
 - What product or UX change would most help the lowest-converting high-volume segment?

Return: per-segment funnel tables, segment-step interaction analysis, impact scores, significance test, and top recommendations. Copy prompt View page Show more ↓ Funnel Analysis Advanced Prompt 03 
### Multi-Touch Attribution for Product 
Analyze which in-product touchpoints and features most contribute to conversion or activation.

User journey data: {{journey_data}} (user_id, touchpoint_type, touchpoint_timestamp, converted: Y/N)
Conversion event: {{conversion_event}} (e.g. first purchase, plan upgrade, feature activation)

1. Touchpoint inventory:
 - List all unique touchpoints users encounter before the conversion event
 - Count how often each appears in converting vs non-converting journeys
 - What % of converters touched each touchpoint?

2. Attribution models - compare all three:

 First touch:
 - 100% credit to the first touchpoint the user interacted with
 - Best for: understanding what initiates the conversion journey

 Last touch:
 - 100% credit to the touchpoint immediately before conversion
 - Best for: understanding what closes the conversion

 Linear:
 - Equal credit to all touchpoints in the path
 - Best for: understanding overall touchpoint contribution

3. Path analysis:
 - What are the top 10 most common touchpoint sequences for converters?
 - What sequences do non-converters follow? Where do they diverge?
 - Is there a specific touchpoint combination that strongly predicts conversion?

4. Time-to-conversion by path:
 - Do users with certain touchpoint paths convert faster?
 - Is there a touchpoint that accelerates conversion when added to the path?

5. Recommendations:
 - Which touchpoints should be promoted (high attribution, currently under-used)?
 - Which touchpoints appear to delay or interrupt conversion?
 - What is the optimal path to guide new users through?

Return: touchpoint attribution table (all three models), top conversion paths, path divergence analysis, and recommendations. Copy prompt View page Show more ↓ 
## Product Health Metrics 
3 prompt s Product Health Metrics Intermediate Prompt 01 
### DAU/MAU Ratio Analysis 
Analyze the DAU/MAU ratio (stickiness) for this product and identify improvement opportunities.

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

Return: stickiness metrics, benchmark comparison, trend analysis, segment breakdown, and stickiness driver analysis. Copy prompt View page Show more ↓ Product Health Metrics Advanced Chain 02 
### Full Product Analytics Chain 
Step 1: North Star definition - define or validate the North Star Metric for this product. Decompose it into Level 1 and Level 2 input metrics. Assign owners to each leaf metric.
Step 2: Growth accounting - apply the growth accounting framework to the last 12 months. Compute the quick ratio trend. Diagnose whether this is a new user, retention, or resurrection problem.
Step 3: Funnel audit - map the full acquisition-to-activation funnel. Identify the top 2 drop-off points. Segment the funnel by device, channel, and cohort.
Step 4: Retention analysis - build the cohort retention matrix. Compute Day 1, Day 7, and Day 30 retention by cohort. Identify whether newer cohorts are improving or declining.
Step 5: Feature adoption - for the top 3 features, compute adoption rates and time-to-first-use. Identify which feature has the strongest correlation with 30-day retention.
Step 6: User segmentation - segment users into at least 4 behavioral groups (Champions, At-risk, Dormant, New). Size each segment and compute its contribution to revenue or activity.
Step 7: Recommendations and roadmap - synthesize findings into a prioritized list of 5 product and analytics recommendations. For each: the problem it addresses, the expected impact, and the measurement plan. Copy prompt View page Show more ↓ Product Health Metrics Beginner Prompt 03 
### Product Health Dashboard Design 
Design a product health monitoring framework for {{product_name}}.

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

Return: AARRR metric definitions, North Star decomposition, alert thresholds, and dashboard spec. Copy prompt View page Show more ↓ 
## Experimentation 
2 prompt s Experimentation Advanced Prompt 01 
### Experiment Readout Template 
Write a complete experiment readout for this concluded A/B test.

Experiment: {{experiment_name}}
Hypothesis: {{hypothesis}}
Results data: {{results}}
Audience: product team and leadership

1. TL;DR (3 sentences):
 - What was tested, what was the result, and what is the recommendation?

2. Background:
 - Problem being solved
 - Hypothesis and expected direction of change
 - Primary metric and guardrail metrics

3. Setup:
 - Variants: control and treatment description
 - Traffic allocation and targeting
 - Test duration and sample size achieved vs required

4. Results:
 - Primary metric: control value, treatment value, absolute difference, % difference, p-value, 95% CI
 - Secondary metrics: same format for each
 - Guardrail metrics: did any degrade significantly?
 - Segment breakdown: results by key segments (mobile/desktop, new/returning, plan type)

5. Interpretation:
 - Is the result statistically significant? Practically significant?
 - Are results consistent across segments or driven by one segment?
 - Any unexpected findings worth investigating?

6. Decision:
 - Ship / Do not ship / Iterate / Run follow-up test
 - If shipping: rollout plan (% of traffic, timeline)
 - If iterating: what specifically changes in the next version?

7. Learnings:
 - What did this test teach us about user behavior?
 - How does this inform future experiments or roadmap decisions?

Return: complete experiment readout document suitable for sharing with the product team. Copy prompt View page Show more ↓ Experimentation Intermediate Prompt 02 
### Product Experiment Prioritization 
Prioritize this backlog of product experiments for the next quarter.

Experiment ideas: {{experiment_list}}
Current traffic: {{daily_active_users}} DAU
Team capacity: {{capacity}} experiments per quarter

1. Score each experiment on ICE framework:
 - Impact (1-10): how much will this move the primary metric if it works?
 - Confidence (1-10): how sure are we the hypothesis is correct? (prior evidence, user research)
 - Ease (1-10): how quickly and cheaply can this be built and measured?
 - ICE score = (Impact + Confidence + Ease) / 3

2. Feasibility check:
 - For each experiment: calculate required sample size at 80% power, alpha=0.05, and the team's stated MDE
 - Calculate required duration: sample_size / (DAU x traffic_allocation_rate)
 - Flag experiments requiring > 8 weeks as impractical for the quarter

3. Dependency and conflict check:
 - Are any experiments testing overlapping UI elements or user flows? (Cannot run simultaneously)
 - Does any experiment depend on another being completed first?
 - Map experiment conflicts and dependencies

4. Learning value:
 - Even if a test is negative, what do we learn?
 - Prioritize experiments that resolve fundamental product questions over marginal optimizations

5. Recommended quarter plan:
 - Select experiments that fit within capacity, avoid conflicts, and maximize learning
 - Sequence them: which experiments must run first to unblock others?
 - Reserve 20% capacity for urgent or opportunistic tests

Return: ICE scoring table, feasibility check, conflict map, and recommended quarter experiment plan with sequencing. Copy prompt View page Show more ↓ 
## Feature Adoption 
2 prompt s Feature Adoption Beginner Prompt 01 
### Feature Adoption Analysis 
Analyze the adoption of this product feature and identify opportunities to increase usage.

Feature: {{feature_name}}
Adoption data: {{adoption_data}} (user_id, first_use_date, usage_frequency, user_segment)
Launch date: {{launch_date}}

1. Adoption funnel:
 - Awareness: % of eligible users who have seen or been exposed to the feature
 - Activation: % who have used it at least once
 - Adoption: % who have used it more than {{n_times}} times
 - Habit: % who use it regularly (at least once per {{period}})

2. Time to first use:
 - How long after account creation do users first try the feature?
 - Median and distribution of time-to-first-use
 - What % of eventual adopters used it within: 1 day, 7 days, 30 days of account creation?

3. Adoption by segment:
 - Which user segments have the highest adoption rates? (by plan, role, company size, acquisition channel)
 - Which segments are significantly below average? These are the opportunity segments.

4. Correlation with retention:
 - Do users who adopt this feature have higher 30-day and 90-day retention?
 - Compute retention rates for: adopters vs non-adopters (note: correlation, not causation)
 - If adopters retain significantly better: this feature is a potential activation lever

5. Usage depth:
 - Among adopters: how often do they use it? (sessions per week distribution)
 - Are there power users using it far more than average? What do they have in common?
 - At what usage frequency does the feature become 'sticky' (correlated with long-term retention)?

6. Barriers to adoption:
 - In the adoption funnel, which step has the biggest drop-off?
 - For low-adoption segments: what are 3 likely barriers (awareness, discoverability, complexity, value clarity)?

Return: adoption funnel metrics, time-to-first-use analysis, segment breakdown, retention correlation, and barrier hypothesis. Copy prompt View page Show more ↓ Feature Adoption Intermediate Prompt 02 
### Feature Impact Assessment 
Assess the business impact of this recently launched feature.

Feature: {{feature_name}}
Launch date: {{launch_date}}
Primary success metric: {{primary_metric}}
Data available: {{data}}

1. Pre/post comparison:
 - Define the pre-period (same length as post, ending at launch date)
 - Compare primary metric: pre-period average vs post-period average
 - Absolute change and % change
 - Account for trends: was the metric already trending up/down before launch?

2. Confound check:
 - What else changed during the post-period? (Seasonality, marketing campaigns, other feature launches)
 - How might these confounds explain the observed change?
 - Can any confounds be controlled for or isolated?

3. Adoption-outcome correlation:
 - Segment users by adoption level: non-adopters, light adopters, heavy adopters
 - Compare primary metric across adoption segments
 - Does heavier feature usage correlate with better outcomes?

4. Counterfactual estimation:
 - If possible: use a holdout group (users who did not have access to the feature) as a control
 - Difference-in-differences: compare the change in metric for treatment vs control groups
 - If no holdout: use synthetic control (similar product/market as proxy)

5. Secondary effects:
 - Did the feature have any unintended effects on other metrics?
 - Check: session length, support tickets, error rates, other feature usage

6. ROI estimate:
 - Translate the metric impact into business value: what is the estimated annual impact in revenue or cost?
 - How does this compare to the development cost of the feature?

Return: pre/post comparison, confound analysis, adoption-outcome correlation, counterfactual estimate, and ROI. Copy prompt View page Show more ↓ 
## Growth Analytics 
2 prompt s Growth Analytics Intermediate Prompt 01 
### Growth Accounting Framework 
Apply a growth accounting framework to decompose MAU growth into its constituent components.

User activity data: {{activity_data}} (user_id, active_month)
Time period: {{period}}

1. User state classification:
 For each user in each month, classify their state:
 - New: first month of activity
 - Retained: active this month AND last month
 - Resurrected: active this month but NOT last month (but active at some prior point)
 - Churned: active last month but NOT this month (not visible in current month counts)

2. Growth accounting equation:
 MAU(t) = MAU(t-1) + New(t) + Resurrected(t) - Churned(t)
 - Verify this equation balances in the data

3. Monthly trend of each component:
 - Plot New, Retained, Resurrected, and Churned users over time
 - Quick ratio = (New + Resurrected) / Churned
 Quick ratio > 1: growing. < 1: shrinking. = 1: flat.
 - What is the trend in the quick ratio?

4. Component deep dive:
 - New users: growing or declining? What is driving acquisition?
 - Churn: is the churn count growing as MAU grows? (Structural churn problem if yes)
 - Resurrection: what brings users back? Is resurrection a meaningful growth driver?
 - Retention: what % of users are retained month over month? Is it improving?

5. Diagnosis:
 - Is this a new user problem (top of funnel), a retention problem, or both?
 - If the quick ratio < 1: which component needs improvement most?
 - If the quick ratio > 1 but slowing: is churn keeping pace with new user growth?

Return: monthly growth accounting table, quick ratio trend, component analysis, and growth diagnosis. Copy prompt View page Show more ↓ Growth Analytics Advanced Prompt 02 
### North Star Metric Decomposition 
Decompose the North Star Metric into its input metrics and build a measurement tree.

North Star Metric: {{nsm}} (e.g. 'Weekly Active Engaged Users' or 'Messages Sent per Month')
Product context: {{product_description}}

1. Level 1 decomposition:
 Break the NSM into 2-3 multiplicative or additive components.
 Example: Weekly Active Engaged Users = Weekly Active Users x Engagement Rate
 Example: Revenue = Users x Conversion Rate x Average Order Value

2. Level 2 decomposition:
 Break each Level 1 component further.
 Example: Weekly Active Users = New Users + Retained Users + Resurrected Users
 Example: Engagement Rate = % Users Completing Core Action

3. Level 3 decomposition (where meaningful):
 Continue decomposing into actionable leaf metrics that specific teams own.

4. For each leaf metric:
 - Current value
 - Owner: which team or squad controls this metric?
 - Lever: what specific action moves this metric?
 - Effort to improve by 10%: Low / Medium / High

5. Sensitivity analysis:
 - If each leaf metric improves by 10%, which has the largest impact on the NSM?
 - This identifies the highest-leverage improvement opportunity

6. Metric tree dashboard spec:
 - Top level: NSM with trend
 - Second level: Level 1 components with trend
 - Third level: Level 2 components with owner labeled
 - Color coding: green = above target, yellow = near target, red = below target

Return: metric tree (all three levels), owner assignment, sensitivity analysis, and dashboard specification. Copy prompt View page Show more ↓ 
## Retention Analysis 
2 prompt s Retention Analysis Intermediate Prompt 01 
### Churn Prediction Indicators 
Identify the leading behavioral indicators that predict user churn before it happens.

User behavior data: {{behavior_data}}
Churn definition: {{churn_definition}} (e.g. no activity for 30 days, subscription cancelled)
Observation window: {{observation_window}} (behavioral features measured in the N days before churn)

1. Feature engineering for churn prediction:
 Compute these behavioral features for each user in the observation window:
 - Login frequency: sessions per week
 - Days since last active
 - Core action completion rate: % of sessions where {{core_action}} was completed
 - Feature breadth: number of distinct features used
 - Engagement trend: comparing last 7 days vs prior 7 days
 - Support contacts: number of support tickets or error events
 - Billing events: failed payments, plan downgrades

2. Univariate analysis:
 For each feature, compare the distribution between:
 - Users who churned within {{horizon}} days
 - Users who did not churn
 Compute: mean, median, and statistical significance of the difference (Mann-Whitney U test)

3. Predictive ranking:
 - Which features show the largest and most statistically significant difference between churners and non-churners?
 - Rank features by predictive power (use AUC of a simple logistic regression per feature)

4. Early warning thresholds:
 - For the top 3 features: what threshold value separates high-churn-risk from low-churn-risk users?
 - Example: users with > 14 days since last login have a 3x higher churn rate than average

5. Churn risk segmentation:
 - Combine the top 3 indicators into a simple churn risk score (Low / Medium / High)
 - What % of users currently fall into each risk tier?
 - What intervention should each tier receive?

Return: feature importance table, threshold analysis, risk tier definitions, and intervention recommendations. Copy prompt View page Show more ↓ Retention Analysis Beginner Prompt 02 
### User Retention Cohort Analysis 
Build and interpret a user retention cohort analysis.

Event data: {{event_data}} (user_id, event_date, acquisition_date or cohort_date)
Retention definition: {{retention_definition}} (e.g. any login, completed core action, purchase)
Cohort granularity: {{granularity}} (weekly / monthly)

1. Build the retention matrix:
 - Rows: cohorts defined by {{cohort_period}} of first use or acquisition
 - Columns: periods since acquisition (Period 0, 1, 2, ... N)
 - Cell value: % of cohort still active in that period
 - Period 0 = 100% by definition (the acquisition period)

2. Key retention metrics:
 - Day 1 retention: % of users returning the day after first use
 - Day 7 retention: % returning in the first week
 - Day 30 retention: % returning within the first month
 - Long-term retention: at what period does the retention curve flatten? This is the product's natural retention floor.

3. Cohort comparison:
 - Are newer cohorts retaining better or worse than older ones?
 - Which cohort has the best Day 30 retention? What was happening during that acquisition period?
 - Plot cohort curves on the same chart: diverging curves indicate improving or worsening product health

4. Retention curve shape interpretation:
 - Sharp early drop then flat: high initial churn but strong core user base
 - Gradual continuous decline: no engaged user base, product is not habit-forming
 - Bump at specific period: seasonal return or notification-driven re-engagement

5. Retention by acquisition channel:
 - Which acquisition channels produce the highest Day 30 retention?
 - Are there channels bringing volume but low retention? (Wasted acquisition spend)

6. Recommendations:
 - At which period does the biggest retention drop occur? What is the likely cause?
 - What single change would most improve the retention curve shape?

Return: retention matrix, key metrics table, cohort comparison chart description, curve interpretation, and top recommendations. Copy prompt View page Show more ↓ 
## User Segmentation 
2 prompt s User Segmentation Intermediate Prompt 01 
### Behavioral User Segmentation 
Segment users based on behavioral patterns in this product.

Behavioral data: {{behavior_data}} (event logs: user_id, event_type, timestamp, session_id)
Segmentation goal: {{goal}} (personalization, intervention targeting, resource allocation)

1. Feature engineering for segmentation:
 Create behavioral features per user over the last {{window}} days:
 - Recency: days since last active
 - Frequency: sessions per week
 - Depth: average actions per session
 - Breadth: number of distinct features used
 - Tenure: days since account creation
 - Core action rate: % of sessions with {{core_action}}

2. RFM-style segmentation (rule-based, interpretable):
 Apply percentile-based segmentation on Recency, Frequency, and Depth:
 - Champions: recent, frequent, deep engagement
 - At-risk: previously frequent but declining
 - Dormant: not active in > 30 days
 - New users: tenure < 14 days
 - Casual: low frequency, low depth

3. Cluster-based segmentation (data-driven):
 - Apply k-means clustering on the behavioral features
 - Test k = 3, 4, 5, 6 clusters; select using silhouette score
 - Profile each cluster: mean values for each behavioral feature
 - Name each cluster with a business-friendly label based on its profile

4. Segment stability:
 - How stable are segments over time? (Do users move between segments frequently?)
 - A good segment is both meaningful and stable

5. Segment sizing and value:
 - Count and % of users in each segment
 - Revenue, retention, or other outcome metric per segment
 - Which segment represents the highest business value?

6. Recommended actions per segment:
 - Champions: retain and leverage as advocates
 - At-risk: trigger a win-back flow
 - Dormant: re-engagement campaign or sunset
 - New users: accelerate activation

Return: feature engineering code/SQL, RFM segment definitions, cluster profiles, segment sizing table, and recommended actions. Copy prompt View page Show more ↓ User Segmentation Intermediate Prompt 02 
### Power User Analysis 
Identify and analyze the power users of this product to understand what drives exceptional engagement.

Engagement data: {{engagement_data}}
Power user definition: {{definition}} (top 10% by usage frequency, or specific behavior threshold)

1. Power user identification:
 - Define power users quantitatively: users who {{criterion}} in the last 30 days
 - What % of total users are power users?
 - What % of total activity or revenue do power users account for? (Often 80% of value from 20% of users)

2. Power user profile:
 - Demographics: tenure, acquisition channel, plan type, company size (if B2B)
 - Behavioral fingerprint: which features do they use most? What is their typical session pattern?
 - Onboarding: did they complete onboarding differently? How quickly did they activate?
 - First week behavior: what did power users do in their first 7 days that non-power users did not?

3. The aha moment:
 - Is there a specific action in the first week that strongly predicts becoming a power user?
 - Compute: % of power users who completed {{action}} in week 1 vs % of all users
 - This is the aha moment candidate - the action to optimize for in onboarding

4. Power user journey:
 - Map the typical sequence of feature adoption for power users
 - At what tenure do most users reach power user status?
 - Is there a specific feature or workflow that accelerates the journey?

5. Implications for product and growth:
 - How can onboarding be redesigned to guide more users toward the power user path?
 - Which acquisition channels produce the most power users? (Not just the most users)
 - What does retaining power users require? (Are they at risk of churning for any reason?)

Return: power user definition and sizing, behavioral profile, aha moment analysis, journey map, and product/growth implications. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
