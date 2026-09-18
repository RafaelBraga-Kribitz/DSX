# Attribution *AI Prompts *

4 Marketing Analyst prompts in Attribution. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Attribution 
4 prompts Advanced Chain 01 
### Full Marketing Analytics Chain 

Step 1: Data audit - audit the marketing analytics stack for tracking completeness. Identify missing events, broken tracking, and attribution gaps. Produce a prioritized list of... 
Prompt text Step 1: Data audit - audit the marketing analytics stack for tracking completeness. Identify missing events, broken tracking, and attribution gaps. Produce a prioritized list of data quality fixes.
Step 2: Performance baseline - establish current performance baselines for all key marketing metrics by channel. Compute YoY and MoM trends. Identify which channels are improving and which are declining.
Step 3: Attribution analysis - compare performance across at least three attribution models (last click, first click, linear). Identify which channels are over- or under-credited in the current reporting model. Recommend a more accurate approach.
Step 4: Audience analysis - segment customers into actionable groups using RFM or behavioral clustering. Compute LTV, conversion rate, and CAC by segment. Identify the highest-value underserved segment.
Step 5: Campaign optimization - for each active channel, identify the top optimization opportunity (budget reallocation, audience refinement, creative refresh, landing page improvement). Prioritize by expected revenue impact.
Step 6: Content and organic strategy - audit SEO performance and content effectiveness. Identify top 10 keyword and content opportunities. Build a 90-day content roadmap prioritized by traffic and conversion potential.
Step 7: Marketing plan and measurement - produce a 90-day marketing plan: budget allocation by channel, key initiatives, expected outcomes, and a measurement framework with clear success criteria. Include one incrementality test to run in the quarter. Copy prompt Open prompt details Intermediate Single prompt 02 
### Incrementality Testing Design 

Design an incrementality test to measure the true causal impact of a marketing channel. Channel to test: {{channel}} (e.g. Facebook Ads, email retargeting, TV) Primary metric: {... 
Prompt text Design an incrementality test to measure the true causal impact of a marketing channel.

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

Return: test design recommendation, sample size calculation, measurement plan, and common pitfall mitigations. Copy prompt Open prompt details Advanced Single prompt 03 
### Marketing Mix Modeling 

Design and interpret a marketing mix model (MMM) for this business. Business: {{business}} Sales / conversion data: {{sales_data}} (weekly, 2+ years) Marketing spend data: {{spe... 
Prompt text Design and interpret a marketing mix model (MMM) for this business.

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

Return: MMM methodology explanation, data preparation steps, model output interpretation, contribution table, mROAS by channel, and optimized budget allocation. Copy prompt Open prompt details Intermediate Single prompt 04 
### Multi-Touch Attribution Analysis 

Analyze marketing attribution using multiple models to understand channel contribution. Customer journey data: {{journey_data}} (user_id, touchpoint, timestamp, channel, convert... 
Prompt text Analyze marketing attribution using multiple models to understand channel contribution.

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

Return: model comparison table, path analysis, assisted vs direct breakdown, and budget implications. Copy prompt Open prompt details 
## Recommended Attribution workflow 
1 
### Full Marketing Analytics Chain 

Start with a focused prompt in Attribution so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Incrementality Testing Design 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Marketing Mix Modeling 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Multi-Touch Attribution Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
