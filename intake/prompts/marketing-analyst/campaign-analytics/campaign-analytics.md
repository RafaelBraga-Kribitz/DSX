# Campaign Analytics *AI Prompts *

6 Marketing Analyst prompts in Campaign Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 6 single prompts. 

## AI prompts in Campaign Analytics 
6 prompts Intermediate Single prompt 01 
### A/B Test Analysis for Campaigns 

Analyze this marketing A/B test and produce a decision-ready report. Test description: {{test_description}} Variants: Control: {{control}} | Treatment: {{treatment}} Primary met... 
Prompt text Analyze this marketing A/B test and produce a decision-ready report.

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

Return: statistical analysis, effect size calculation, segment breakdown, decision, and learnings. Copy prompt Open prompt details Beginner Single prompt 02 
### Campaign Performance Report 

Generate a comprehensive campaign performance report for {{campaign_name}}. Campaign data: {{campaign_data}} Goal: {{campaign_goal}} (awareness, lead generation, conversion, ret... 
Prompt text Generate a comprehensive campaign performance report for {{campaign_name}}.

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

Return: performance summary table, channel breakdown, creative analysis, audience insights, and top recommendations. Copy prompt Open prompt details Intermediate Single prompt 03 
### Campaign ROI Analysis 

Calculate the true ROI of this marketing campaign including all costs and revenue attribution. Campaign: {{campaign_name}} Spend data: {{spend_data}} Revenue attribution data: {... 
Prompt text Calculate the true ROI of this marketing campaign including all costs and revenue attribution.

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

Return: total cost breakdown, attribution analysis, net ROI, LTV/CAC, and channel-level ROI comparison. Copy prompt Open prompt details Intermediate Single prompt 04 
### Demand Generation Funnel Analysis 

Analyze the B2B demand generation funnel from awareness to closed revenue. Funnel data: {{funnel_data}} (leads by stage, conversion rates, time in stage, revenue closed) Sales c... 
Prompt text Analyze the B2B demand generation funnel from awareness to closed revenue.

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

Return: funnel conversion table, pipeline forecast, lead source ROI, sales velocity analysis, and marketing revenue attribution. Copy prompt Open prompt details Advanced Single prompt 05 
### Marketing Performance Dashboard Design 

Design a comprehensive marketing performance dashboard for the CMO and marketing leadership team. Business model: {{business_model}} Marketing channels: {{channels}} Key busines... 
Prompt text Design a comprehensive marketing performance dashboard for the CMO and marketing leadership team.

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

Return: dashboard sections with metric definitions, alert conditions, drill-down structure, and audience views. Copy prompt Open prompt details Advanced Single prompt 06 
### Paid Media Budget Optimization 

Optimize paid media budget allocation across channels to maximize return at a given spend level. Current budget: {{total_budget}} Current channel allocations: {{current_allocati... 
Prompt text Optimize paid media budget allocation across channels to maximize return at a given spend level.

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

Return: marginal ROAS by channel, response curve parameters, optimal allocation table, revenue uplift estimate, and phased implementation plan. Copy prompt Open prompt details 
## Recommended Campaign Analytics workflow 
1 
### A/B Test Analysis for Campaigns 

Start with a focused prompt in Campaign Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Campaign Performance Report 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Campaign ROI Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Demand Generation Funnel Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
