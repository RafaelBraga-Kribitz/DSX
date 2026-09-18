# Conversion Funnel Audit *AI Prompt *

Audit the conversion funnel for {{product_flow}} and identify the highest-impact drop-off points. Funnel stages provided: {{stages_and_counts}} 1. Compute conversion rates: - St... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: funnel table with conversion rates, drop-off ranking, segment breakdown, and prioritized recommendations. 
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

The AI should return a structured result that covers the main requested outputs, such as Compute conversion rates:, Step-by-step conversion rate: users_at_step_N / users_at_step_N-1, Cumulative conversion rate: users_at_each_step / users_at_top_of_funnel. The final answer should stay clear, actionable, and easy to review inside a funnel analysis workflow for product analyst work. 

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
