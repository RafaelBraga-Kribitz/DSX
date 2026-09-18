# Feature Adoption Analysis *AI Prompt *

Analyze the adoption of this product feature and identify opportunities to increase usage. Feature: {{feature_name}} Adoption data: {{adoption_data}} (user_id, first_use_date, u... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: adoption funnel metrics, time-to-first-use analysis, segment breakdown, retention correlation, and barrier hypothesis. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin feature adoption work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Feature Adoption or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Adoption funnel:, Awareness: % of eligible users who have seen or been exposed to the feature, Activation: % who have used it at least once. The final answer should stay clear, actionable, and easy to review inside a feature adoption workflow for product analyst work. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Feature Adoption.
