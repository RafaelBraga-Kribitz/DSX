# Funnel and Cohort Visualization *AI Prompt *

Design visualizations for funnel analysis and cohort retention. Funnel stages: {{funnel_stages}} Cohort definition: {{cohort_definition}} Metric: {{metric}} (retention rate, rev... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design visualizations for funnel analysis and cohort retention.

Funnel stages: {{funnel_stages}}
Cohort definition: {{cohort_definition}}
Metric: {{metric}} (retention rate, revenue, engagement)

1. Funnel visualization options:

 Standard funnel chart:
 - Trapezoid shapes decreasing in width at each stage
 - Width proportional to the count at that stage
 - Show: absolute count AND conversion rate (%) between each stage
 - Color: use color to highlight the stage with the biggest drop-off
 - Limitation: difficult to compare multiple funnels (e.g. mobile vs desktop)

 Bar-based funnel:
 - Horizontal bars ranked by stage, sorted top to bottom
 - Easier to read exact values than the trapezoid format
 - Add conversion rate labels between bars: '→ 42% converted'
 - Add a secondary bar showing the 'lost' volume in each stage (grey bar)

 Funnel comparison (best for multiple segments):
 - Grouped or overlaid bars for each stage
 - Each group = one stage; bars within = one segment each
 - Better for: mobile vs desktop, new vs returning users, A vs B variant

 Waterfall funnel:
 - Shows how volume flows from one stage to the next
 - Each bar shows: volume entering the stage, volume converting (green), volume lost (red)
 - Good for showing absolute loss at each stage rather than just conversion rate

2. Cohort retention heatmap (standard format):
 - Rows: cohorts (typically by acquisition month/week)
 - Columns: periods since acquisition (Period 0, Period 1, Period 2...)
 - Cell value: retention rate (% of cohort still active in that period)
 - Color: sequential scale — dark = high retention, light = low retention
 - Period 0 is always 100% (the baseline)
 - Reading the diagonal: shows same calendar period across different cohorts (seasonality effect)

3. Retention visualization variants:
 - Line chart overlay: multiple cohort lines on the same chart — shows which cohorts retain better
 - Cumulative retention: useful for subscription products (when does the subscriber cancel?)
 - Retention cliff: annotate the period where the sharpest drop occurs

4. Actionable design:
 - For funnels: highlight the single biggest drop-off stage in red
 - For cohort heatmaps: add reference lines at 30-day and 90-day columns
 - Add a 'benchmark' row to the cohort heatmap showing the company average

Return: funnel chart design (type, labels, color coding), cohort heatmap specification, color scale, and actionability annotations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin advanced visualization types work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Advanced Visualization Types or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Funnel visualization options:, Trapezoid shapes decreasing in width at each stage, Width proportional to the count at that stage. The final answer should stay clear, actionable, and easy to review inside a advanced visualization types workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Advanced Visualization Types.
