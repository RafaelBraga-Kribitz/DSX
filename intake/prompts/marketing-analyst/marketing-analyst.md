# Marketing Analyst *AI Prompts *

Marketing Analyst AI prompt library with 30 prompts in 7 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 7 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Marketing Analyst prompt categories 
7 categories 
### Campaign Analytics 

AI prompts for campaign analytics, including performance diagnostics, lift interpretation, spend efficiency, and optimization recommendations. 
6 prompts A/B Test Analysis for Campaigns Campaign Performance Report → 
### Attribution 

AI prompts for attribution analysis across channels and touchpoints, including model choices, assumptions, and decision-ready interpretation. 
4 prompts Full Marketing Analytics Chain Incrementality Testing Design → 
### Audience Segmentation 

AI prompts for audience segmentation workflows, including persona definition, cluster interpretation, and activation-oriented segment recommendations. 
4 prompts Churn Prediction for Marketing Customer Segmentation for Marketing → 
### Brand and Market Analytics 

AI prompts for brand and market analytics, including awareness signals, competitive comparisons, and market-position trend analysis. 
4 prompts Brand Sentiment Analysis Competitor Analysis Framework → 
### CRM and Email Analytics 

AI prompts for CRM and email analytics, including lifecycle performance, engagement diagnostics, segmentation, and retention-oriented messaging impact. 
4 prompts Customer Lifecycle Email Analysis Customer LTV Calculation → 
### SEO and Content Analytics 

AI prompts for SEO and content analytics, including traffic quality, ranking drivers, content performance, and optimization opportunities. 
4 prompts Content Calendar Data Strategy Content Performance Analysis → 
### Web and Digital Analytics 

AI prompts for web and digital analytics, including session behavior, engagement quality, journey diagnostics, and performance monitoring. 
4 prompts Conversion Rate Optimization Analysis GA4 Event Tracking Audit → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 30 Campaign Analytics 6 Attribution 4 Audience Segmentation 4 Brand and Market Analytics 4 CRM and Email Analytics 4 SEO and Content Analytics 4 Web and Digital Analytics 4 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **30 **of 30 prompts 
## Campaign Analytics 
6 prompt s Campaign Analytics Intermediate Prompt 01 
### A/B Test Analysis for Campaigns 
Analyze this marketing A/B test and produce a decision-ready report.

Test description: {{test_description}}
Variants: Control: {{control}} | Treatment: {{treatment}}
Primary metric: {{primary_metric}}
Test data: {{results_data}}

1. Statistical analysis:
 - Control and treatment values for the primary metric
 - Absolute and relative difference
 - Two-proportion z-test (for conversion rates) or t-test (for continuous metrics)
 - p-value and 95% confidence interval
 - Is the result statistically significant at alpha = 0.05?
 - Statistical power: given the observed sample size and effect, what was the test's power?

2. Practical significance:
 - Effect size: Cohen's h (for proportions) or Cohen's d (for means)
 - Business impact: if this effect persists at scale, what is the annual revenue or cost impact?
 - Minimum detectable effect vs observed effect: did we detect what we expected to detect?

3. Secondary metric analysis:
 - Repeat for all secondary metrics
 - Did any guardrail metrics degrade significantly?

4. Segment analysis:
 - Break results by: device, geography, new vs returning, customer tier
 - Is the effect consistent across segments or driven by one?
 - Heterogeneous treatment effects: does the winner differ by segment?

5. Decision:
 - Implement / Do not implement / Run follow-up test
 - If implementing: rollout plan
 - If running follow-up: what specific question does the next test answer?

6. Learnings for future campaigns:
 - What does this test teach us about our audience or message?
 - Should this insight change any other running campaigns?

Return: statistical analysis, effect size calculation, segment breakdown, decision, and learnings. Copy prompt View page Show more ↓ Campaign Analytics Beginner Prompt 02 
### Campaign Performance Report 
Generate a comprehensive campaign performance report for {{campaign_name}}.

Campaign data: {{campaign_data}}
Goal: {{campaign_goal}} (awareness, lead generation, conversion, retention)
Time period: {{period}}

1. Performance summary:
 - Total spend: {{spend}}
 - Total impressions, clicks, conversions
 - Key derived metrics:
 - Click-through rate (CTR): Clicks / Impressions
 - Cost per click (CPC): Spend / Clicks
 - Conversion rate: Conversions / Clicks
 - Cost per acquisition (CPA): Spend / Conversions
 - Return on ad spend (ROAS): Revenue / Spend

2. Performance vs benchmarks:
 - Compare each metric to: campaign target, prior campaign, industry benchmark
 - Flag any metric more than 20% above or below benchmark

3. Channel breakdown:
 - Performance by channel (paid search, paid social, display, email, etc.)
 - Which channel delivered the lowest CPA? The highest ROAS?
 - Channel mix: what % of spend and conversions came from each channel?

4. Creative performance:
 - Top 3 and bottom 3 creative assets by CTR and conversion rate
 - What characteristics do the top performers share? (Format, message, visual style)
 - Recommend pausing the bottom performers

5. Audience performance:
 - Performance by audience segment (demographics, interests, remarketing vs prospecting)
 - Which audience delivered the best conversion rate and CPA?

6. Time performance:
 - Performance by day of week and hour of day
 - Are there peak and trough periods that suggest dayparting optimization?

7. Recommendations:
 - Top 3 optimization actions ranked by expected impact
 - Budget reallocation suggestion: which channels should get more / less?

Return: performance summary table, channel breakdown, creative analysis, audience insights, and top recommendations. Copy prompt View page Show more ↓ Campaign Analytics Intermediate Prompt 03 
### Campaign ROI Analysis 
Calculate the true ROI of this marketing campaign including all costs and revenue attribution.

Campaign: {{campaign_name}}
Spend data: {{spend_data}}
Revenue attribution data: {{revenue_data}}
Product margin: {{gross_margin_pct}}

1. Total cost of campaign:
 - Media spend (by channel)
 - Agency or creative fees
 - Technology platform costs
 - Internal labor cost (estimate: hours x fully-loaded cost per hour)
 - Total cost of campaign

2. Revenue attribution:
 - Direct response revenue: conversions directly attributed to the campaign
 - Assisted revenue: conversions where the campaign appeared in the path but was not the last touch
 - Attribution model used: last click, first click, linear, data-driven
 - Note the sensitivity: how much does attributed revenue change across attribution models?

3. ROI calculation:
 - Gross revenue attributed
 - Gross profit attributed (Revenue x Gross Margin %)
 - Net ROI = (Gross Profit - Total Cost) / Total Cost x 100%
 - ROAS = Gross Revenue / Media Spend (this overstates ROI; use gross profit ROI for real decisions)

4. Payback analysis:
 - For acquisition campaigns: CAC from this campaign
 - LTV of customers acquired: estimated LTV from this campaign's cohort
 - LTV / CAC ratio: is this campaign economically attractive?

5. Comparison to alternatives:
 - ROI vs other campaigns in the same period
 - ROI vs the cost of capital (hurdle rate)
 - Incremental ROI: what additional revenue vs a no-campaign baseline?

6. ROI by channel:
 - Compute net ROI for each channel in the campaign mix
 - Which channel delivered the highest gross profit ROI?
 - Where should budget shift in the next campaign based on this analysis?

Return: total cost breakdown, attribution analysis, net ROI, LTV/CAC, and channel-level ROI comparison. Copy prompt View page Show more ↓ Campaign Analytics Intermediate Prompt 04 
### Demand Generation Funnel Analysis 
Analyze the B2B demand generation funnel from awareness to closed revenue.

Funnel data: {{funnel_data}} (leads by stage, conversion rates, time in stage, revenue closed)
Sales cycle: {{avg_sales_cycle}} days
ACV: {{average_contract_value}}

1. Funnel stage definitions and metrics:
 - MQL (Marketing Qualified Lead): lead meeting the scoring threshold
 - SQL (Sales Qualified Lead): MQL accepted by sales
 - Opportunity: SQL with discovery meeting completed
 - Proposal: opportunity with proposal sent
 - Closed-Won: contracted revenue

 For each stage: volume, conversion rate to next stage, average days in stage

2. Conversion rate analysis:
 - MQL to SQL: what % of marketing leads are accepted by sales?
 Below 50% may indicate a lead quality problem
 - SQL to Opportunity: what % of accepted leads convert to active pipeline?
 - Opportunity to Close: win rate against proposals sent
 - Overall funnel conversion: leads to closed-won

3. Revenue forecast from current pipeline:
 - Pipeline by stage: weighted by stage probability
 - Expected revenue in next 90 days from current pipeline
 - Pipeline coverage ratio: pipeline / quota (target > 3x for 90-day quota)

4. Lead source contribution:
 - MQL volume by source (content/SEO, paid, events, outbound, referral)
 - Conversion rates by source: which sources produce the highest quality leads?
 - Revenue contribution by source: where does closed revenue actually come from?
 - Cost per MQL and cost per closed deal by source

5. Sales cycle and velocity:
 - Average days from MQL to close by source and segment
 - Deals stalling in specific stages: which stage has the longest dwell time?
 - Pipeline velocity: (Opportunities x Win Rate x ACV) / Sales Cycle Length

6. Marketing contribution to revenue:
 - Marketing-sourced revenue: deals where marketing generated the first touch
 - Marketing-influenced revenue: deals where marketing contributed at some point
 - Marketing's % contribution to total revenue

Return: funnel conversion table, pipeline forecast, lead source ROI, sales velocity analysis, and marketing revenue attribution. Copy prompt View page Show more ↓ Campaign Analytics Advanced Prompt 05 
### Marketing Performance Dashboard Design 
Design a comprehensive marketing performance dashboard for the CMO and marketing leadership team.

Business model: {{business_model}}
Marketing channels: {{channels}}
Key business goals: {{goals}}
Reporting cadence: weekly and monthly

1. Dashboard sections and metrics:

 SECTION 1 - Revenue and Pipeline Impact:
 - Marketing-sourced revenue (month and YTD vs target)
 - Marketing-influenced revenue
 - Total pipeline value from marketing-sourced leads
 - Pipeline coverage ratio (pipeline / quota)

 SECTION 2 - Demand Generation:
 - MQL volume (week, month, YTD vs target)
 - MQL-to-SQL conversion rate (trend)
 - Cost per MQL by channel
 - Funnel velocity (days MQL to close)

 SECTION 3 - Channel Performance:
 - Spend, conversions, CPA, ROAS by channel
 - Channel mix % (share of spend vs share of conversions)
 - MoM change in CPA by channel

 SECTION 4 - Brand and Organic:
 - Organic traffic (YoY trend)
 - Domain authority and backlink growth
 - Branded search volume trend
 - NPS score (monthly)

 SECTION 5 - Customer Marketing:
 - Email engagement rate (open rate, CTOR)
 - Churn rate trend
 - Expansion revenue from marketing programs
 - Renewal rate (if applicable)

2. Alert conditions for weekly review:
 - MQL volume > 20% below weekly target: investigate channel performance
 - CPA increase > 15% WoW in any channel: bid strategy or competition change
 - Organic traffic > 10% below baseline: potential SEO issue

3. Drill-down structure:
 - Each metric links to a supporting report
 - CMO can click from MQL count to breakdown by channel, source, and sales owner

4. Audience customization:
 - CMO view: pipeline impact + channel efficiency + NPS
 - Channel manager view: their channel only, deep detail
 - CEO view: revenue impact + efficiency ratio only

Return: dashboard sections with metric definitions, alert conditions, drill-down structure, and audience views. Copy prompt View page Show more ↓ Campaign Analytics Advanced Prompt 06 
### Paid Media Budget Optimization 
Optimize paid media budget allocation across channels to maximize return at a given spend level.

Current budget: {{total_budget}}
Current channel allocations: {{current_allocation}}
Performance data by channel: {{performance_data}} (spend, conversions, revenue)

1. Current state analysis:
 For each channel:
 - Current spend and % of total budget
 - Conversions and revenue attributed
 - CPA and ROAS
 - Marginal ROAS: performance of the last incremental dollar spent (from spend vs performance curve)

2. Response curve estimation:
 For each channel, estimate the diminishing returns curve:
 - Collect historical data points: (spend level, performance outcome) per week
 - Fit a saturation curve: Revenue = a x (1 - e^(-b x Spend))
 - Where is the inflection point? Where does marginal ROAS drop below 1?

3. Optimal allocation theory:
 - Budget is optimally allocated when marginal ROAS is equal across all channels
 - If Channel A marginal ROAS (1.8) > Channel B marginal ROAS (0.9): shift budget from B to A
 - Continue reallocation until marginal ROAS equalizes

4. Proposed reallocation:
 - For each channel: recommended new budget
 - Expected change in conversions and revenue vs current allocation
 - Total portfolio ROAS improvement from optimization

5. Constraints to consider:
 - Minimum effective budget per channel (below a threshold, channels stop working)
 - Channel caps from inventory limitations or audience saturation
 - Strategic channels that require funding beyond what pure ROI math suggests
 - Brand safety requirements

6. Testing plan:
 - Do not implement all reallocation at once: risk of performance disruption
 - Phased approach: 20% reallocation per month with measurement between each step

Return: marginal ROAS by channel, response curve parameters, optimal allocation table, revenue uplift estimate, and phased implementation plan. Copy prompt View page Show more ↓ 
## Attribution 
4 prompt s Attribution Advanced Chain 01 
### Full Marketing Analytics Chain 
Step 1: Data audit - audit the marketing analytics stack for tracking completeness. Identify missing events, broken tracking, and attribution gaps. Produce a prioritized list of data quality fixes.
Step 2: Performance baseline - establish current performance baselines for all key marketing metrics by channel. Compute YoY and MoM trends. Identify which channels are improving and which are declining.
Step 3: Attribution analysis - compare performance across at least three attribution models (last click, first click, linear). Identify which channels are over- or under-credited in the current reporting model. Recommend a more accurate approach.
Step 4: Audience analysis - segment customers into actionable groups using RFM or behavioral clustering. Compute LTV, conversion rate, and CAC by segment. Identify the highest-value underserved segment.
Step 5: Campaign optimization - for each active channel, identify the top optimization opportunity (budget reallocation, audience refinement, creative refresh, landing page improvement). Prioritize by expected revenue impact.
Step 6: Content and organic strategy - audit SEO performance and content effectiveness. Identify top 10 keyword and content opportunities. Build a 90-day content roadmap prioritized by traffic and conversion potential.
Step 7: Marketing plan and measurement - produce a 90-day marketing plan: budget allocation by channel, key initiatives, expected outcomes, and a measurement framework with clear success criteria. Include one incrementality test to run in the quarter. Copy prompt View page Show more ↓ Attribution Intermediate Prompt 02 
### Incrementality Testing Design 
Design an incrementality test to measure the true causal impact of a marketing channel.

Channel to test: {{channel}} (e.g. Facebook Ads, email retargeting, TV)
Primary metric: {{metric}} (conversions, revenue)
Business context: {{context}}

Incrementality testing answers: what revenue would we have generated WITHOUT this channel?
This is the only way to determine true incremental value beyond what would have happened anyway.

1. Test design options:

 Geo holdout test:
 - Split geography into test regions (channel active) and holdout regions (channel paused)
 - Match regions by: historical performance, demographics, market size
 - Duration: minimum 4 weeks (longer for lower-frequency purchase categories)
 - Measure: conversion rate in test regions vs holdout regions

 User holdout (ghost bidding):
 - Randomly assign users: treatment (see ads) vs control (ad slot left empty)
 - Platform-native holdout if available (Facebook Brand Lift, Google Conversion Lift)
 - Best for: digital channels with user-level targeting

 Time-based holdout:
 - Turn off the channel for a period and compare to matched prior period
 - Weakness: seasonal and macro factors can confound results
 - Requires: careful selection of the comparison period

2. Sample size and duration:
 - Required sample: power calculation based on baseline conversion rate and expected lift
 - Minimum detectable effect: if the channel drives < {{mde}}% lift, you need more data
 - Duration: long enough to capture a full purchase cycle

3. Measurement:
 - Lift = (Conversion Rate_test - Conversion Rate_holdout) / Conversion Rate_holdout
 - Incremental conversions = Lift x Holdout user volume
 - True CPA = Channel Spend / Incremental Conversions
 - Compare to attributed CPA: the gap shows how much attribution was overstating the channel

4. Common pitfalls:
 - Spillover: people in the holdout region still see the ads via other means
 - Holdout contamination: test and control groups interact (e.g. via social sharing)
 - Too short a test: brand campaigns need months to show full effect

Return: test design recommendation, sample size calculation, measurement plan, and common pitfall mitigations. Copy prompt View page Show more ↓ Attribution Advanced Prompt 03 
### Marketing Mix Modeling 
Design and interpret a marketing mix model (MMM) for this business.

Business: {{business}}
Sales / conversion data: {{sales_data}} (weekly, 2+ years)
Marketing spend data: {{spend_data}} (by channel, same period)
External factors: {{external_factors}} (macroeconomic data, seasonality, competitor actions)

1. What MMM is and when to use it:
 - MMM uses regression to decompose total sales into: baseline (organic) + each marketing channel's contribution + external factors
 - Unlike attribution (which tracks individual user paths), MMM works at aggregate level
 - Best for: understanding the incremental contribution of each channel, including offline (TV, OOH)
 - Limitation: requires 2+ years of data, is backward-looking, and cannot measure within-campaign personalization

2. Data preparation:
 - Adstock transformation: marketing spend has a delayed and decaying effect
 Adstock_t = Spend_t + decay_rate x Adstock_{t-1}
 - Decay rates by channel: TV (~0.7), Digital display (~0.3), Paid search (~0.1)
 - Saturation curve: diminishing returns on increasing spend (log or S-curve transformation)
 - Control variables: seasonality (Fourier terms or dummy variables), price, distribution, promotions

3. Model specification:
 Sales_t = Baseline + sum(beta_i x Adstock_i_t) + beta_price x Price_t + Seasonal + Error
 - Estimate using Bayesian regression (allows priors on channel effectiveness)
 - Model diagnostics: R-squared, MAPE on holdout period, residual checks

4. Output interpretation:
 - Baseline %: share of sales occurring without any marketing
 - Contribution % per channel: what share of incremental sales each channel drove
 - mROAS (marginal ROAS): the return on the last dollar spent in each channel
 - Saturation point: at what spend level does each channel show diminishing returns?

5. Budget optimization:
 - Using the fitted saturation curves: what budget allocation maximizes total sales at the current total budget?
 - What is the revenue uplift from the optimal allocation vs current allocation?

Return: MMM methodology explanation, data preparation steps, model output interpretation, contribution table, mROAS by channel, and optimized budget allocation. Copy prompt View page Show more ↓ Attribution Intermediate Prompt 04 
### Multi-Touch Attribution Analysis 
Analyze marketing attribution using multiple models to understand channel contribution.

Customer journey data: {{journey_data}} (user_id, touchpoint, timestamp, channel, converted: Y/N)
Conversion event: {{conversion_event}}
Lookback window: {{lookback_window}} days

1. Attribution model comparison:
 Build all five standard models and compare:

 Last click: 100% credit to the final touchpoint
 First click: 100% credit to the first touchpoint
 Linear: equal credit to all touchpoints in the path
 Time decay: more credit to recent touchpoints (decay factor: 0.5 per day)
 Position-based (U-shaped): 40% to first, 40% to last, 20% split across middle

 For each model: credits per channel (absolute and %).

2. Channel contribution shift across models:
 - Which channels gain the most credit in first-click vs last-click?
 - First-click favors awareness channels (social, display); last-click favors intent channels (search)
 - Create a heatmap: channels x attribution models showing credit share

3. Path analysis:
 - Top 10 converting path sequences (e.g. Display → Organic Search → Paid Search → Convert)
 - Average path length (touchpoints) for converting vs non-converting journeys
 - Most common first touchpoints for converters

4. Assisted vs direct conversions:
 - % of conversions with only one touchpoint vs multi-touch paths
 - Channels that primarily assist (appear in paths but not at end) vs channels that primarily close

5. Data-driven attribution (if sample size permits):
 - Shapley value attribution: fair allocation based on marginal contribution of each channel
 - Requires: enough paths where each channel appears with and without others
 - Provides the most theoretically correct attribution

6. Budget implication:
 - If we moved budget based on last-click attribution: which channels would be over or under-invested?
 - Recommended budget allocation change based on the most appropriate model

Return: model comparison table, path analysis, assisted vs direct breakdown, and budget implications. Copy prompt View page Show more ↓ 
## Audience Segmentation 
4 prompt s Audience Segmentation Intermediate Prompt 01 
### Churn Prediction for Marketing 
Build a churn prediction model to identify at-risk customers for proactive marketing intervention.

Customer data: {{customer_data}}
Churn definition: {{churn_definition}}
Marketing interventions available: {{interventions}}

1. Feature engineering:
 Build predictive features for each customer (measured over the last 30/60/90 days):
 - Recency: days since last purchase or login
 - Frequency: purchase count in the last 90 days vs prior 90 days (trend)
 - Monetary: spend in last 90 days vs prior 90 days (trend)
 - Product usage: number of distinct products/features used
 - Engagement: email open rate, app sessions
 - Support signals: number of complaints or returns
 - Payment signals: failed payments, subscription downgrades

2. Churn probability model:
 - Logistic regression for interpretability (preferred for marketing teams)
 - Or gradient boosted trees for accuracy
 - Training: last 6 months of data; validation: most recent 30-60 days
 - Output: probability of churn within the next {{horizon}} days per customer

3. Risk tier definition:
 - High risk: churn probability > 60%
 - Medium risk: churn probability 30-60%
 - Low risk: churn probability < 30%
 - Size each tier: count and revenue at risk

4. Expected value of intervention:
 - For high-risk tier: Expected savings = (customers x churn probability x avg LTV x save rate)
 - Save rate: historical % of at-risk customers who respond to an intervention
 - Compare to intervention cost: is the program economically justified?

5. Intervention strategy by tier:
 - High risk: highest-value offer, personal outreach from CSM or account manager
 - Medium risk: automated personalized email with value reminder + soft incentive
 - Low risk: monitor; include in standard engagement program

6. Measurement plan:
 - Control group: randomly hold out 10% of at-risk customers from interventions
 - Measure: 60-day churn rate in treated vs control group
 - Calculate: incremental save rate and revenue impact

Return: feature engineering spec, model approach, risk tier definitions, intervention strategy, expected value calculation, and measurement plan. Copy prompt View page Show more ↓ Audience Segmentation Intermediate Prompt 02 
### Customer Segmentation for Marketing 
Build and operationalize customer segments for targeted marketing.

Customer data: {{customer_data}} (demographics, behavioral, transactional, engagement)
Marketing goals: {{goals}}
Channels available: {{channels}}

1. Segmentation approach selection:

 Demographic segmentation:
 - Age, gender, location, income, job title
 - Pros: easy to understand and action
 - Cons: weak predictor of behavior for most products

 Behavioral segmentation:
 - Purchase history, product usage, channel preferences, engagement frequency
 - Pros: directly tied to marketing-relevant actions
 - Best for: personalization, cross-sell, win-back

 RFM (Recency, Frequency, Monetary):
 - Recency: how recently did they purchase?
 - Frequency: how often do they purchase?
 - Monetary: how much do they spend?
 - Quintile score (1-5) on each dimension; combine into segment labels

 Psychographic / attitudinal:
 - Values, motivations, lifestyle
 - Pros: powerful for brand messaging
 - Cons: requires survey data, harder to operationalize

2. RFM segmentation execution:
 For each customer, compute R, F, M scores (1-5):
 - Champions: RFM = 5,5,5 (buy often, recently, high value)
 - Loyal customers: 4+,4+,3+
 - At-risk: previously high RFM but R has dropped
 - Potential loyalists: recent but low frequency
 - Win-back: low R, previously decent F and M
 - Lost: low on all three dimensions

3. Segment sizing and value:
 - Size (count and % of customers)
 - Average order value, purchase frequency, LTV by segment
 - Total revenue contribution by segment

4. Segment-to-channel mapping:
 For each segment: which channels and messages are most appropriate?
 - Champions: VIP program, referral program, early access
 - At-risk: re-engagement email, win-back offer
 - Potential loyalists: loyalty nudge, second purchase incentive

5. Personalization rules:
 - What content, offer, and message should each segment receive?
 - Build a segment x message matrix

Return: RFM segment definitions and scoring logic, segment sizing table, revenue contribution, channel mapping, and personalization rules. Copy prompt View page Show more ↓ Audience Segmentation Advanced Prompt 03 
### Lookalike Audience Analysis 
Build a lookalike audience strategy based on best-customer characteristics.

Seed audience: {{seed_audience}} (your best customers by LTV or conversion)
Available platforms: {{platforms}} (Meta, Google, LinkedIn, programmatic DSP)
Campaign goal: {{goal}}

1. Seed audience definition and quality:
 - Define 'best customers': top 10% by LTV, or converted within 30 days, or completed {{action}}
 - Minimum seed size: 1,000 users for reliable lookalike modeling (500 minimum, 5,000+ recommended)
 - Seed quality check: are seed customers actually your most profitable? (Not just most active)

2. First-party data preparation:
 - Match rate optimization: use email, phone, MAIDS for highest match rates
 - Hashed PII: never pass unhashed emails to platforms
 - Audience freshness: use customers acquired in the last 6 months for best results
 - Exclude: existing customers from prospecting lookalike campaigns

3. Platform-specific lookalike construction:

 Meta Lookalike Audiences:
 - Similarity range: 1% (most similar) to 10% (broader reach, less similar)
 - Recommendation: 1-2% for highest intent, 3-5% for broader prospecting
 - Layer with interest targeting for higher precision

 Google Similar Audiences / Customer Match:
 - Smart Bidding automatically adjusts bids for similar audiences
 - Customer Match can be used for similar segments via automatically created lists

 LinkedIn Lookalikes:
 - Most valuable for B2B: match on company, industry, job title characteristics
 - Seed with MQL or customer list from CRM

4. Testing framework:
 - A/B test: lookalike 1% vs lookalike 3% vs interest targeting vs no audience filter
 - Measure: CPA and conversion rate per audience type
 - Duration: minimum 2 weeks, 50+ conversions per variant for statistical reliability

5. Performance benchmarks:
 - Lookalike audiences should outperform broad targeting by 20-40% on CPA
 - If lookalike is not outperforming: seed audience may not be differentiated enough

Return: seed audience definition, data preparation checklist, platform construction guide, testing framework, and performance benchmarks. Copy prompt View page Show more ↓ Audience Segmentation Intermediate Prompt 04 
### Persona Development from Data 
Develop data-driven marketing personas for {{product}}.

Data sources: {{data_sources}} (CRM, survey, behavioral analytics, interviews)
Existing customer base: {{customer_count}} customers

1. Quantitative customer profiling:
 From CRM and analytics data, compute for each customer:
 - Company size, industry, geography (for B2B)
 - Demographics: age, gender, job title (for B2C or B2B)
 - Behavioral: acquisition channel, feature usage, purchase frequency
 - Value: LTV, plan/product tier, churn risk score

2. Cluster analysis:
 - Apply k-means clustering (k=3 to 5) on the behavioral and firmographic features
 - For each cluster: profile using the mean values of each feature
 - Name each cluster based on its defining characteristics

3. Qualitative enrichment:
 - For each cluster, pull the top 10% by LTV and review their CRM notes, support tickets, and survey responses
 - Identify: primary use case, main problem solved, key decision criteria, objections to purchase
 - Add the 'voice of the customer' to each persona: direct quotes from reviews or interviews

4. Persona template per cluster:
 - Name and title: a memorable label (e.g. 'The Efficiency-Focused Ops Manager')
 - Demographics/firmographics: size, role, industry
 - Primary goal: the main outcome they are trying to achieve
 - Pain points: the problems your product solves for them
 - Decision criteria: how they evaluate solutions
 - Information sources: where they get industry information
 - Objections: their most common reasons not to buy

5. Persona sizing and value:
 - What % of current customers does each persona represent?
 - What % of revenue does each persona account for?
 - Which persona is under-represented in the customer base vs addressable market?

6. Marketing application:
 - Recommended messaging for each persona
 - Recommended channels to reach each persona
 - Recommended content type for each persona

Return: cluster analysis, persona template for each cluster, sizing table, and marketing application guide. Copy prompt View page Show more ↓ 
## Brand and Market Analytics 
4 prompt s Brand and Market Analytics Intermediate Prompt 01 
### Brand Sentiment Analysis 
Analyze brand sentiment from customer reviews, social mentions, and survey data.

Data sources: {{data_sources}} (reviews, social listening, NPS survey, support tickets)
Time period: {{period}}
Competitors to compare: {{competitors}}

1. Sentiment scoring:
 For each text data source:
 - Classify each item as: Positive, Neutral, Negative
 - Sentiment score: (Positive - Negative) / Total
 - Track sentiment score over time
 - Volume by sentiment category per period

2. Theme extraction:
 - Use topic modeling or keyword clustering to identify the main themes in reviews/mentions
 - For each theme: count of mentions, sentiment split, trend over time
 - Positive themes: what do customers love most? (Product quality, service, value, ease of use)
 - Negative themes: what are the biggest complaints? (Price, reliability, support, missing features)

3. NPS driver analysis:
 - Promoters (9-10): what do they consistently praise?
 - Passives (7-8): what would convert them to promoters?
 - Detractors (0-6): what are the primary complaint themes?
 - For each NPS segment: top 3 verbatim themes

4. Competitive sentiment comparison:
 - Overall sentiment score vs competitors
 - Which themes does our brand win on vs competitors?
 - Which themes do competitors win on? (Areas to improve)

5. Sentiment anomalies:
 - Any spikes in negative sentiment? What triggered them? (Product issue, PR event, policy change)
 - Any unexpected positive spikes? What can we replicate?

6. Marketing implications:
 - Which proven positive themes should be amplified in marketing messages?
 - Which negative themes represent reputation risks that marketing must address?

Return: sentiment score trends, theme analysis, NPS driver breakdown, competitive comparison, and marketing implications. Copy prompt View page Show more ↓ Brand and Market Analytics Intermediate Prompt 02 
### Competitor Analysis Framework 
Build a competitive marketing intelligence framework for {{company}}.

Competitors: {{competitor_list}}
Analysis dimensions: {{dimensions}}

1. Digital presence benchmarking:
 For each competitor:
 - Website traffic estimate (SimilarWeb, SEMrush)
 - Organic keyword ranking count and estimated traffic
 - Paid search spend estimate (SEMrush, SpyFu)
 - Social media followers and engagement rate by platform
 - App store ratings and review count (if applicable)

2. SEO competitive analysis:
 - Keyword gap: keywords competitors rank for that we do not
 - Content gap: topics competitors have content on that we do not
 - Backlink comparison: domain authority and linking root domains
 - Top content by traffic for each competitor

3. Paid advertising analysis:
 - Estimated monthly paid search spend per competitor
 - Ad copy analysis: what messages and value propositions are they using?
 - Landing page analysis: what does their conversion experience look like?
 - Facebook Ad Library: active social ad creative and messaging

4. Messaging and positioning:
 - For each competitor: primary value proposition (from homepage)
 - Target audience stated or implied
 - Key differentiators claimed
 - Pricing tier and model (if visible)
 - Create a positioning map: plot competitors on 2 axes (e.g. price vs feature depth)

5. Share of voice:
 - Estimated organic search share of voice for target keyword set
 - Social mention volume comparison
 - PR and news coverage volume

6. Competitive threats and opportunities:
 - Where are competitors investing heavily? (Threat)
 - Where are competitors weak? (Opportunity)
 - What positioning gaps exist that no competitor is occupying?

Return: competitor benchmarking table, SEO gap analysis, paid ad insights, positioning map, share of voice, and threat/opportunity matrix. Copy prompt View page Show more ↓ Brand and Market Analytics Intermediate Prompt 03 
### Market Sizing Analysis 
Estimate the Total Addressable Market (TAM), Serviceable Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for this business.

Business: {{business_description}}
Product/service: {{product}}
Geography: {{geography}}

1. TAM (Total Addressable Market):
 The total market demand if the product captured 100% of the market.

 Top-down approach:
 - Start with a published industry market size (from Gartner, IDC, IBISWorld, etc.)
 - Narrow to the specific segment relevant to this product
 - Adjust for the geographic scope

 Bottom-up approach:
 - Count the number of potential customers (from public data, census, industry directories)
 - Estimate average annual spend per customer
 - TAM = customer count x average spend
 - Use both approaches and triangulate

2. SAM (Serviceable Addressable Market):
 The portion of TAM that can realistically be served given product scope, geography, and channel.
 - Exclude segments the product is not designed for
 - Exclude geographies where the company does not or cannot operate
 - Exclude customer sizes that do not match the go-to-market motion

3. SOM (Serviceable Obtainable Market):
 The realistic market share the business can capture in 3-5 years.
 - Benchmark against comparable companies at similar stages
 - Consider: competitive intensity, sales capacity, brand awareness, capital available
 - Typical SOM = 1-10% of SAM in year 3-5 for venture-stage companies

4. Market growth rate:
 - Historical CAGR of the market
 - Forward-looking drivers: what is accelerating or decelerating market growth?
 - TAM in 5 years at current growth rate

5. Sanity check:
 - Revenue target / SOM: what market share does the business plan imply?
 - Is that market share realistic given competitors and market dynamics?

Return: TAM, SAM, and SOM estimates with both top-down and bottom-up methodology, market growth rate, and sanity check on business plan assumptions. Copy prompt View page Show more ↓ Brand and Market Analytics Intermediate Prompt 04 
### Survey Analysis for Marketing Insights 
Analyze this marketing survey and extract actionable insights.

Survey data: {{survey_data}}
Survey type: {{survey_type}} (NPS, CSAT, brand awareness, customer effort, market research)
Respondents: {{n_respondents}}

1. Response quality check:
 - Response rate and completion rate
 - Speeders: respondents who completed the survey in < 30% of median time (unreliable data)
 - Straightliners: respondents who gave the same answer to every scale question
 - Recommend excluding speeders and straightliners from analysis

2. Quantitative analysis:
 - For each closed-ended question: frequency distribution (count and % per response option)
 - For scale questions (1-10 NPS, 1-5 satisfaction): mean, median, standard deviation
 - Cross-tabulation: how do responses differ by key demographic or segment?

3. NPS analysis (if applicable):
 - Promoters (9-10), Passives (7-8), Detractors (0-6): count and %
 - NPS = % Promoters - % Detractors
 - NPS by segment: which customer group has the highest / lowest NPS?
 - NPS trend vs prior survey wave

4. Open-text analysis:
 - Theme extraction: top 10 themes from open-ended responses
 - Sentiment per theme: positive, neutral, negative
 - Volume and sentiment for: Promoters vs Detractors vs Passives
 - Most actionable verbatims: select 5 representative quotes per theme

5. Correlation with behavior:
 - Match survey respondents to CRM/behavioral data
 - Do high-NPS customers actually have higher retention rates?
 - Do customers who cite price as a concern have higher churn rates?

6. Marketing implications:
 - Promoter themes to amplify in marketing messaging
 - Detractor themes that are reputation risks to address
 - Awareness and perception gaps revealed by the survey

Return: response quality check, quantitative summary, NPS calculation, theme analysis, behavioral correlation, and marketing implications. Copy prompt View page Show more ↓ 
## CRM and Email Analytics 
4 prompt s CRM and Email Analytics Intermediate Prompt 01 
### Customer Lifecycle Email Analysis 
Analyze the effectiveness of lifecycle email sequences and identify gaps in the program.

Lifecycle data: {{lifecycle_data}} (email type, trigger event, send date, open, click, conversion)
Customer journey stages: {{stages}} (onboarding, activation, engagement, expansion, retention, win-back)

1. Lifecycle email inventory:
 Map every automated email to the customer journey stage:
 - Trigger: what event sends this email?
 - Goal: what action should the recipient take?
 - Metric: how is success measured?

2. Coverage gaps:
 - Which stages have no automated email coverage?
 - Are there high-value moments in the customer journey with no triggered email?
 - Common gaps: post-onboarding engagement, pre-renewal reminder, post-cancellation win-back

3. Sequence performance:
 For each lifecycle sequence:
 - Open rate by email position (Email 1, 2, 3...): how quickly does engagement decay?
 - Click rate by position
 - Completion rate: what % of recipients receive all emails in the sequence?
 - Conversion rate: what % take the desired action?

4. Time-to-convert analysis:
 - From lifecycle email send to conversion: how long does it take?
 - Is there an optimal timing window? (Some emails may be sent too early or too late)

5. Optimization opportunities:
 - Sequences with lowest conversion rate: content or timing issue?
 - High open but low click sequences: strong subject line but weak email body
 - Low open sequences: timing, subject line, or sender name issue

6. Recommended additions:
 Based on the gap analysis, propose 3 new lifecycle automations:
 - Trigger event
 - Goal
 - Message approach
 - Expected impact on activation/retention/revenue metric

Return: lifecycle email inventory, coverage gap analysis, sequence performance table, and 3 recommended new automations. Copy prompt View page Show more ↓ CRM and Email Analytics Advanced Prompt 02 
### Customer LTV Calculation 
Calculate Customer Lifetime Value (LTV) using multiple methods and apply it to marketing decisions.

Customer data: {{customer_data}} (cohort, revenue history, churn events)
Business model: {{business_model}}
Discount rate: {{discount_rate}} (cost of capital, typically 10-15%)

1. Simple LTV (for early-stage / approximate use):
 LTV = Average Purchase Value x Purchase Frequency x Customer Lifespan
 - Average Purchase Value: total revenue / total orders
 - Purchase Frequency: total orders / total unique customers per period
 - Customer Lifespan: 1 / Monthly Churn Rate (in months)
 - Gross Profit LTV: multiply by gross margin %

2. Cohort-based LTV (most accurate for historical data):
 - For each acquisition cohort: cumulative revenue per customer through each month of life
 - Plot the cumulative LTV curve: how does LTV grow as cohort ages?
 - LTV at 12 months, 24 months, and steady state
 - Are newer cohorts trending above or below older cohorts? (Improving or declining customer quality)

3. Discounted LTV (for financial decisions):
 Discounted LTV = sum over t: (Expected Cash Flow_t / (1 + r)^t)
 - Where r = monthly discount rate = (1 + annual rate)^(1/12) - 1
 - Cash flow_t = monthly gross profit from the cohort in month t
 - Captures the time value of money: a dollar of LTV received in year 3 is worth less than in year 1

4. LTV by segment:
 - LTV for different acquisition channels, customer segments, product categories, geographies
 - Which segments have 2x or higher LTV than average?
 - This should drive differential CAC targets by segment

5. LTV / CAC framework for marketing decisions:
 - Healthy: LTV / CAC > 3
 - Acceptable: LTV / CAC 1-3 (with path to improvement)
 - Unsustainable: LTV / CAC < 1
 - Maximum CAC by segment = LTV x maximum acceptable CAC ratio

6. LTV improvement levers:
 - Increase average order value (cross-sell, upsell)
 - Increase purchase frequency (engagement, reminder programs)
 - Reduce churn (retention programs)
 - For each lever: estimated impact on LTV

Return: LTV calculation by method, cohort LTV curves, segment LTV comparison, LTV/CAC framework, and LTV improvement lever analysis. Copy prompt View page Show more ↓ CRM and Email Analytics Beginner Prompt 03 
### Email Campaign Analysis 
Analyze the performance of this email campaign and identify optimization opportunities.

Email data: {{email_data}}
Campaign type: {{type}} (newsletter, promotional, lifecycle, transactional)
Audience: {{audience_size}} recipients

1. Deliverability metrics:
 - Delivery rate: delivered / sent (target > 98%)
 - Bounce rate: hard + soft bounces / sent
 - Spam complaint rate: spam reports / delivered (target < 0.1%)
 - List health: what % of the list is engaged (opened at least once in 90 days)?

2. Engagement metrics:
 - Open rate: unique opens / delivered (benchmark varies by industry, typically 20-40%)
 - Click-to-open rate (CTOR): clicks / opens (measures email content quality, target > 10%)
 - Click rate: clicks / delivered
 - Unsubscribe rate: unsubscribes / delivered (target < 0.2%)

3. Conversion metrics:
 - Conversion rate: desired action completions / delivered
 - Revenue per email: total revenue attributed / emails delivered
 - Compare to target and prior campaigns

4. Timing analysis:
 - What day of week and time of day were emails sent?
 - Compare open rate and click rate at different send times (if A/B tested)
 - Industry best practice send times for this audience segment

5. Subject line analysis:
 - If A/B tested: winning subject line and the open rate lift
 - Characteristics of high-performing subject lines: length, personalization, urgency, question vs statement
 - Recommendation for next campaign

6. Segment performance:
 - Break engagement metrics by: customer segment, tenure, geography, prior engagement level
 - Which segment has the highest CTOR? Should receive more targeted sends.
 - Which segment has the lowest open rate? Review frequency, relevance, send time.

7. Optimization recommendations:
 - Top 3 actions to improve performance in the next send

Return: deliverability metrics, engagement analysis, conversion results, segment breakdown, and optimization recommendations. Copy prompt View page Show more ↓ CRM and Email Analytics Intermediate Prompt 04 
### Email List Health Audit 
Audit the health of this email list and build a re-engagement and list hygiene plan.

List data: {{list_data}} (subscriber_id, subscribe_date, last_open_date, last_click_date, email_type)
List size: {{list_size}}
Current engagement rate: {{engagement_rate}}

1. Engagement segmentation:
 Classify every subscriber into engagement tiers:
 - Active: opened or clicked in the last 90 days
 - Warming: opened or clicked 90-180 days ago
 - At-risk: last engaged 180-365 days ago
 - Inactive: no engagement in > 365 days
 - Never engaged: subscribed but never opened a single email

 Size and % of list in each tier.

2. List decay rate:
 - How quickly is the active tier shrinking as a % of total?
 - Monthly new subscribers vs monthly subscribers moving to inactive
 - If inactive subscribers > 30% of list: email deliverability is at risk

3. Impact on deliverability:
 - High inactive rates signal to ISPs that your emails are unwanted
 - Gmail, Outlook, and Apple Mail track engagement heavily
 - Estimated deliverability risk: at current inactive %, what is the projected impact on inbox placement?

4. Re-engagement campaign design:
 For the 'At-risk' tier:
 - Trigger: 180 days since last open
 - Sequence: 3-email re-engagement series
 - Email 1: 'We miss you' + best recent content
 - Email 2: Incentive offer or value reminder
 - Email 3: 'Last chance' + explicit opt-down/unsubscribe option
 - Success criteria: any open or click = move back to 'Warming' tier

5. Sunset policy:
 - After the re-engagement sequence: move non-responders to suppression list
 - Do NOT delete: keep suppressed for compliance (unsubscribe proof)
 - Expected list size reduction and engagement rate improvement from sunset

6. List growth quality:
 - Which acquisition sources are producing the highest-engagement subscribers?
 - Which sources produce low-engagement (likely purchased or low-intent) subscribers?
 - Stop acquiring from low-quality sources even if it slows list growth

Return: engagement tier breakdown, list decay analysis, re-engagement sequence, sunset policy, and acquisition source quality assessment. Copy prompt View page Show more ↓ 
## SEO and Content Analytics 
4 prompt s SEO and Content Analytics Advanced Prompt 01 
### Content Calendar Data Strategy 
Build a data-driven content calendar strategy for the next quarter.

Business goals: {{goals}}
Current content performance data: {{performance_data}}
Keyword research: {{keyword_data}}
Budget and capacity: {{capacity}} content pieces per month

1. Content audit and baseline:
 - Total content inventory: how many pieces exist?
 - Distribution by type: blog, video, infographic, case study, guide, etc.
 - Performance distribution: top 20% of content drives what % of traffic?
 - Underperformers: content with < 100 organic sessions per month despite 90+ days live

2. Opportunity prioritization matrix:
 Score each content opportunity on:
 - Search volume: how many monthly searches for the target keyword?
 - Keyword difficulty: how competitive is ranking for this keyword?
 - Business relevance: how closely does this keyword relate to our product/service?
 - Content gap: is there a piece already ranking well for this? (Avoid cannibalization)

 Priority score = (Search Volume x Business Relevance) / Keyword Difficulty

3. Content type strategy:
 Based on funnel stage goals:
 - Awareness (top of funnel): educational blog posts, infographics, videos
 - Consideration (middle): comparison guides, case studies, how-tos, webinars
 - Decision (bottom): testimonials, ROI calculators, free trials, demos
 What % of capacity should go to each stage?

4. Content calendar structure:
 - Month 1: focus on top 3 quick-win keyword opportunities
 - Month 2: focus on top 3 competitor gap opportunities
 - Month 3: focus on top 3 brand / thought leadership pieces
 For each piece: keyword target, content type, author, publish date, promotion plan

5. Distribution plan per piece:
 - SEO: internal linking to new content from existing high-traffic pages
 - Email: segment of subscribers most relevant to each topic
 - Social: platform and format most appropriate for each content type
 - Paid amplification: boost pieces with high conversion potential

6. Measurement plan:
 - 30-day: social shares, initial traffic
 - 90-day: organic ranking position, organic traffic
 - 180-day: conversions attributed, backlinks earned

Return: content audit summary, priority scoring table, type strategy, quarterly calendar, distribution plan, and measurement framework. Copy prompt View page Show more ↓ SEO and Content Analytics Intermediate Prompt 02 
### Content Performance Analysis 
Analyze the performance of content assets and identify the content strategy that drives the most business value.

Content data: {{content_data}} (URL, traffic, engagement, conversions, publication date, content type)
Business goals: {{goals}} (lead generation, organic traffic, brand awareness)

1. Content performance metrics:
 For each content piece:
 - Organic sessions (and YoY trend)
 - Average time on page
 - Bounce rate
 - Conversion rate to {{goal_action}} (CTA click, form submit, sign-up)
 - Backlinks acquired
 - Social shares

2. Content ROI:
 - Organic traffic value: (monthly organic sessions) x (CPC equivalent for those keywords)
 - Conversion value: conversions x average order value or LTV
 - Cost to produce: estimated hours x fully-loaded cost per hour
 - Content ROI = (traffic value + conversion value - production cost) / production cost

3. Content categorization analysis:
 Group content by type (how-to, comparison, case study, thought leadership, etc.):
 - Which content type drives the most traffic?
 - Which content type has the highest conversion rate?
 - Which content type earns the most backlinks?
 - Recommendation: what type to produce more of?

4. Content decay analysis:
 - For posts older than 12 months: is traffic growing, stable, or declining?
 - High-traffic posts with declining trend: prioritize for refresh
 - Low-traffic posts despite strong keyword intent: SEO or content quality issue

5. Content gap analysis:
 - Which target keywords have no content?
 - Which content pieces rank for keywords outside their intended topic? (Keyword cannibalization risk)

6. Top 10 content pieces to invest in:
 - Ranked by: potential traffic uplift if refreshed or expanded
 - Each with: current status, recommended action, and expected traffic gain

Return: content performance table, content ROI estimates, type analysis, decay list, gap analysis, and top 10 investment priorities. Copy prompt View page Show more ↓ SEO and Content Analytics Intermediate Prompt 03 
### Keyword Opportunity Analysis 
Identify and prioritize keyword opportunities for organic growth.

Current keyword rankings: {{current_rankings}}
Keyword research data: {{keyword_research}} (from Semrush, Ahrefs, or similar)
Competitor domains: {{competitors}}
Business focus: {{business_focus}}

1. Keyword opportunity matrix:
 Segment all target keywords by:
 - Current position: ranking (1-3), ranking (4-10), ranking (11-20), not ranking
 - Search volume: high (> 1000/month), medium (100-1000), low (< 100)
 - Keyword difficulty: easy (< 30), medium (30-60), hard (> 60)
 - Business relevance: core (direct product/service match), adjacent (related problem), awareness (broad topic)

2. Quick win keywords:
 - Currently ranking 4-10 for high-volume, high-relevance keywords
 - Small position improvements (e.g. from 7 to 3) can double traffic
 - For each: current page, specific optimization needed, expected traffic gain from top-3

3. Competitor gap analysis:
 - Keywords where competitors rank in top 10 but we have no content
 - Filter by: high volume + medium difficulty + high business relevance
 - These are the highest-priority new content creation opportunities

4. Long-tail keyword clusters:
 - Group related keywords by topic cluster (not just individual keywords)
 - A single piece of comprehensive content can rank for multiple related long-tail terms
 - Identify the 5 most valuable topic clusters we are not yet covering

5. Search intent classification:
 For the top 50 opportunity keywords, classify intent:
 - Informational: user wants to learn (blog, guide content)
 - Commercial investigation: user is comparing options (comparison, review content)
 - Transactional: user is ready to buy (product page, landing page)
 - Match content type to search intent: mismatched content will not rank

6. Prioritized keyword roadmap:
 Quarter 1: quick wins (optimize existing content for 4-10 position keywords)
 Quarter 2: new content for the top 5 competitor gap opportunities
 Quarter 3: build topic authority clusters for the highest-value themes

Return: keyword opportunity matrix, quick win list, competitor gap analysis, topic clusters, and quarterly roadmap. Copy prompt View page Show more ↓ SEO and Content Analytics Beginner Prompt 04 
### SEO Performance Audit 
Conduct a data-driven SEO performance audit for {{website}}.

Search Console data: {{search_console_data}}
GA4 data: {{ga4_data}}
Audit period: {{period}}

1. Overall organic performance:
 - Total organic sessions: trend over {{period}}
 - Total impressions, clicks, average CTR, average position (from Search Console)
 - YoY change in organic sessions
 - Organic share of total traffic mix

2. Top pages analysis:
 - Top 20 pages by organic sessions
 - For each: impressions, clicks, CTR, average position
 - Pages with high impressions but low CTR (< 2%): title/meta description optimization opportunity
 - Pages with good CTR but low position (4-10): close to page 1, worth optimizing content
 - Pages with declining sessions YoY: potential ranking drops or content decay

3. Keyword analysis:
 - Top 50 keywords by clicks
 - Keyword categorization: branded vs non-branded
 - Non-branded keyword performance: positions 1-3, 4-10, 11-20
 - Keyword opportunities: high impression, low click keywords (position 4-10) = quick win optimization targets

4. Technical SEO signals:
 - Core Web Vitals: LCP, FID/INP, CLS from Search Console
 - Mobile vs desktop impressions and CTR comparison
 - Index coverage: excluded pages and their reasons
 - Any manual actions or security issues flagged

5. Content decay identification:
 - Pages where organic traffic has declined > 20% YoY
 - Likely causes: algorithm update, increased competition, outdated content
 - Priority for content refresh based on traffic loss volume

6. Opportunity matrix:
 - Quick wins (1-4 weeks): CTR optimization, internal linking, title tag updates
 - Medium term (1-3 months): content expansion for position 4-10 keywords
 - Long term (3-12 months): new content creation for strategic keyword gaps

Return: performance summary, top page and keyword analysis, technical issues, content decay list, and opportunity matrix. Copy prompt View page Show more ↓ 
## Web and Digital Analytics 
4 prompt s Web and Digital Analytics Intermediate Prompt 01 
### Conversion Rate Optimization Analysis 
Identify conversion rate optimization (CRO) opportunities across this website.

Analytics data: {{analytics_data}}
Heatmap and session recording data: {{heatmap_data}} (if available)
Key conversion goal: {{conversion_goal}}

1. Funnel visualization:
 Map the steps from landing to conversion:
 - Step 1: landing page entry
 - Step 2: [next step]
 - ...
 - Final step: conversion complete
 - Drop-off rate at each step
 - Identify the single biggest drop-off: this is the priority for CRO

2. Page-level analysis for priority pages:
 For each high-traffic, high-drop-off page:
 - Exit rate: what % leave the site from this page?
 - Time on page: are users engaging or bouncing quickly?
 - Scroll depth: how far down the page do users scroll?
 - Click distribution (from heatmap): are users clicking the right elements?

3. Form analysis (if applicable):
 - Form abandonment rate: started but not submitted
 - Which form field has the highest abandonment rate? (Indicates friction or required information concerns)
 - Time to complete the form
 - Error rate per field

4. Mobile vs desktop conversion gap:
 - Mobile conversion rate vs desktop conversion rate
 - If mobile is significantly lower: mobile UX is a priority
 - Page speed on mobile: Core Web Vitals for mobile specifically

5. Traffic source conversion rate comparison:
 - Conversion rate by acquisition channel
 - If paid traffic converts much lower than organic: landing page relevance may be poor
 - Are paid campaign landing pages dedicated pages or generic product pages?

6. Prioritized CRO test backlog:
 - Generate 10 specific test hypotheses
 - Each with: page, element to test, hypothesis, expected lift, effort (Low/Medium/High)
 - Score by ICE and prioritize

Return: funnel drop-off analysis, page-level insights, form analysis, mobile gap, source conversion comparison, and prioritized CRO test backlog. Copy prompt View page Show more ↓ Web and Digital Analytics Intermediate Prompt 02 
### GA4 Event Tracking Audit 
Audit the Google Analytics 4 event tracking implementation for completeness and data quality.

GA4 property: {{property}}
Business goals: {{goals}}
Current events tracked: {{events_list}}

1. Key events audit:
 For each business goal, is the corresponding key event being tracked?
 - Lead generation: form_submit event with form_id, form_type parameters
 - E-commerce: purchase event with transaction_id, value, currency, items array
 - Engagement: video_start, video_complete, scroll depth (75% minimum), file_download
 - Account actions: sign_up, login, subscription_start, subscription_cancel
 - Content: outbound_click, internal_search, search_results_viewed

2. Data quality checks:
 - Are event parameters consistently named? (purchase vs Purchase vs PURCHASE = three separate events)
 - Are revenue events double-counting? (Both client-side and server-side firing)
 - Are null values appearing in required parameters? (item_id = null in purchase events)
 - Are session and user counts plausible given actual traffic?

3. Conversion tracking verification:
 - Test each key event in DebugView: fires at the right moment, with correct parameters?
 - Compare GA4 conversions to CRM / payment processor records: within 10% variance?
 - Are conversions cross-device (GA4 uses Google Signals)? Is cross-device linking enabled?

4. Audience building for remarketing:
 - Are the right events configured as key events for audience building?
 - Recommended audiences: all visitors, product viewers, cart abandoners, past purchasers, high-value customers

5. Data retention settings:
 - Event data retention: set to 14 months (not the default 2 months for comparative analysis)
 - User data: review for GDPR/CCPA compliance

6. Missing event recommendations:
 Based on the audit, list the top 5 events that are missing or misconfigured, with:
 - Event name and parameters
 - Implementation priority
 - Business value of tracking this event

Return: key events audit table, data quality findings, conversion verification results, and top 5 missing event recommendations. Copy prompt View page Show more ↓ Web and Digital Analytics Advanced Prompt 03 
### Marketing Analytics Stack Audit 
Audit the marketing analytics stack for this organization and identify gaps, redundancies, and improvement opportunities.

Current tools: {{tools_list}}
Data flows: {{data_flows}}
Team capability: {{team_capability}}

1. Analytics stack layers:
 Map the current stack against these layers:
 - Data collection: (pixels, SDKs, server-side tagging, webhooks)
 - Data transport: (tag management, event streaming, APIs)
 - Data storage: (data warehouse, CDP, CRM, platform-native storage)
 - Data transformation: (dbt, Fivetran, custom ETL)
 - Analytics and reporting: (BI tool, platform dashboards, spreadsheets)
 - Activation: (email platform, ad platforms, personalization engine)

2. Data quality assessment per layer:
 - Collection: are all key events tracked? Are there data gaps?
 - Storage: is there a single source of truth or multiple conflicting sources?
 - Transformation: is business logic documented and version-controlled?
 - Reporting: do different teams use different definitions for the same metric?

3. Redundancy identification:
 - Are multiple tools doing the same job? (Two CDPs, two email platforms)
 - Can any tools be consolidated without loss of capability?
 - What is the total annual cost of the current stack?

4. Critical gaps:
 - Multi-touch attribution: is there a cross-channel attribution solution beyond platform-reported ROAS?
 - Customer identity resolution: can you link the same person across devices and channels?
 - Offline-to-online: is offline (store, call center) data connected to digital behavior?
 - Incrementality measurement: is there any program to measure true causal marketing impact?

5. Priority improvements:
 - Top 3 gaps with highest impact on marketing decision quality
 - For each: recommended solution, estimated implementation effort, expected ROI

6. Data governance:
 - Is there a marketing data dictionary? (Agreed definitions for all metrics)
 - Who owns each data source and is responsible for its quality?

Return: stack layer map, quality assessment, redundancy analysis, critical gaps, priority improvements, and governance recommendations. Copy prompt View page Show more ↓ Web and Digital Analytics Beginner Prompt 04 
### Website Traffic Analysis 
Analyze website traffic data and identify key trends and opportunities.

GA4 or analytics data: {{analytics_data}}
Time period: {{period}}
Business goal: {{goal}}

1. Traffic overview:
 - Total sessions, users, and page views
 - YoY and MoM trend for each
 - Sessions per user: how often do users return?
 - Average session duration and pages per session

2. Traffic source breakdown:
 - Sessions by channel: organic search, paid search, direct, referral, social, email, other
 - % of sessions by channel (channel mix)
 - YoY change in each channel's share: which channels are growing or shrinking?
 - Are we over-reliant on any single channel (> 40% from one source = concentration risk)?

3. Engagement quality by channel:
 - Bounce rate (or engagement rate in GA4) by channel
 - Session duration by channel
 - Pages per session by channel
 - Conversion rate by channel
 - Which channel drives the most engaged visitors? The least engaged?

4. Landing page analysis:
 - Top 20 landing pages by entry sessions
 - Bounce/engagement rate per landing page
 - Landing pages with high traffic but low engagement: content-traffic mismatch

5. Device and geography:
 - Mobile vs desktop vs tablet: sessions, engagement rate, conversion rate
 - Mobile share trend: is mobile growing? Does mobile convert at a lower rate?
 - Top geographies by traffic: any unexpected sources or gaps?

6. Conversion funnel from traffic:
 - Traffic to lead/sign-up/purchase conversion rate overall and by channel
 - Which pages are the top conversion exit points?

Return: traffic overview, channel mix analysis, engagement quality table, landing page insights, and conversion funnel summary. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
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
