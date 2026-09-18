# Audience Segmentation *AI Prompts *

4 Marketing Analyst prompts in Audience Segmentation. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts. 

## AI prompts in Audience Segmentation 
4 prompts Intermediate Single prompt 01 
### Churn Prediction for Marketing 

Build a churn prediction model to identify at-risk customers for proactive marketing intervention. Customer data: {{customer_data}} Churn definition: {{churn_definition}} Market... 
Prompt text Build a churn prediction model to identify at-risk customers for proactive marketing intervention.

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

Return: feature engineering spec, model approach, risk tier definitions, intervention strategy, expected value calculation, and measurement plan. Copy prompt Open prompt details Intermediate Single prompt 02 
### Customer Segmentation for Marketing 

Build and operationalize customer segments for targeted marketing. Customer data: {{customer_data}} (demographics, behavioral, transactional, engagement) Marketing goals: {{goal... 
Prompt text Build and operationalize customer segments for targeted marketing.

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

Return: RFM segment definitions and scoring logic, segment sizing table, revenue contribution, channel mapping, and personalization rules. Copy prompt Open prompt details Advanced Single prompt 03 
### Lookalike Audience Analysis 

Build a lookalike audience strategy based on best-customer characteristics. Seed audience: {{seed_audience}} (your best customers by LTV or conversion) Available platforms: {{pl... 
Prompt text Build a lookalike audience strategy based on best-customer characteristics.

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

Return: seed audience definition, data preparation checklist, platform construction guide, testing framework, and performance benchmarks. Copy prompt Open prompt details Intermediate Single prompt 04 
### Persona Development from Data 

Develop data-driven marketing personas for {{product}}. Data sources: {{data_sources}} (CRM, survey, behavioral analytics, interviews) Existing customer base: {{customer_count}}... 
Prompt text Develop data-driven marketing personas for {{product}}.

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

Return: cluster analysis, persona template for each cluster, sizing table, and marketing application guide. Copy prompt Open prompt details 
## Recommended Audience Segmentation workflow 
1 
### Churn Prediction for Marketing 

Start with a focused prompt in Audience Segmentation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Customer Segmentation for Marketing 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Lookalike Audience Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Persona Development from Data 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
