# Feature Adoption *AI Prompts *

2 Product Analyst prompts in Feature Adoption. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → intermediate levels and 2 single prompts. 

## AI prompts in Feature Adoption 
2 prompts Beginner Single prompt 01 
### Feature Adoption Analysis 

Analyze the adoption of this product feature and identify opportunities to increase usage. Feature: {{feature_name}} Adoption data: {{adoption_data}} (user_id, first_use_date, u... 
Prompt text Analyze the adoption of this product feature and identify opportunities to increase usage.

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

Return: adoption funnel metrics, time-to-first-use analysis, segment breakdown, retention correlation, and barrier hypothesis. Copy prompt Open prompt details Intermediate Single prompt 02 
### Feature Impact Assessment 

Assess the business impact of this recently launched feature. Feature: {{feature_name}} Launch date: {{launch_date}} Primary success metric: {{primary_metric}} Data available: {... 
Prompt text Assess the business impact of this recently launched feature.

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

Return: pre/post comparison, confound analysis, adoption-outcome correlation, counterfactual estimate, and ROI. Copy prompt Open prompt details 
## Recommended Feature Adoption workflow 
1 
### Feature Adoption Analysis 

Start with a focused prompt in Feature Adoption so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Feature Impact Assessment 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
