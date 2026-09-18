# Funnel Segmentation Deep Dive *AI Prompt *

Analyze how conversion rates differ across key user segments in this funnel. Funnel data: {{funnel_data}} Segmentation dimensions: {{dimensions}} (e.g. acquisition channel, devi... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: per-segment funnel tables, segment-step interaction analysis, impact scores, significance test, and top recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin funnel analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Funnel Analysis or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Per-segment funnel tables:, Segment-step interaction:, Are drop-off patterns consistent across segments, or does one segment struggle at a specific step?. The final answer should stay clear, actionable, and easy to review inside a funnel analysis workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in Funnel Analysis.
