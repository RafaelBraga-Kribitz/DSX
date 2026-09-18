# KPI Card Design *AI Prompt *

Design KPI summary cards for the top section of this dashboard. Metrics to display: {{metrics}} Comparison periods: {{comparisons}} (vs last week, vs last year, vs target) Audie... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design KPI summary cards for the top section of this dashboard.

Metrics to display: {{metrics}}
Comparison periods: {{comparisons}} (vs last week, vs last year, vs target)
Audience: {{audience}}

1. KPI card anatomy:
 Each card should contain:
 - Metric name: short, plain English (not internal code names)
 - Current value: large, prominent, formatted appropriately
 - Change indicator: absolute and % change vs comparison period
 - Direction arrow: ↑ or ↓
 - Color coding: green (positive) / red (negative) — but ONLY if direction = good/bad is unambiguous
 - Sparkline (optional): tiny trend line showing last 30 days of history

2. Value formatting rules:
 - Revenue: $1.2M not $1,234,567 (abbreviate at thousands/millions)
 - Percentages: 23.4% (one decimal), not 23.4567%
 - Ratios: 2.3× not 2.3x (typographically correct)
 - Counts: 12,345 with comma separator
 - Duration: 4m 23s not 263 seconds
 - Never use more decimal places than the measurement precision warrants

3. Change formatting:
 - Show BOTH absolute and percentage change where meaningful
 - Example: '+$42K (+8.3%) vs last month'
 - For metrics where % change is misleading (small denominators): show absolute only
 - Time period label must be explicit: 'vs last month' not just 'MoM'

4. Color coding — apply carefully:
 - Only use red/green when the direction of 'better' is universally agreed
 - Revenue up → green ✓. Cost up → red ✓. Refund rate up → red ✓.
 - Customer support tickets up → could be red OR green depending on context → use neutral
 - When in doubt: use blue/grey for the value, let the arrow indicate direction without color judgment
 - Always provide an alternative indicator beyond color (arrow shape, +/- sign) for colorblind accessibility

5. Card sizing and hierarchy:
 - Primary KPI: largest card, most prominent position
 - Secondary KPIs: equal-sized cards in a row below or beside
 - Supporting context: smaller, lower visual weight
 - Do not show more than 5 KPI cards in the top row — choose the most important ones

6. Sparkline design:
 - No axis labels or gridlines — the shape is what matters
 - Highlight the most recent point with a dot
 - Use the same color as the metric
 - Width: sufficient to show 4 weeks or 12 months of history at a glance

7. What to omit:
 - Percentage change without the baseline value (uninformative)
 - Three comparison periods on the same card (confusing)
 - Conditional formatting that changes the card color (distracting)

Return: KPI card specification for each metric, formatting rules, color coding decisions, and sparkline design. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dashboard architecture work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Dashboard Architecture or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as KPI card anatomy:, Metric name: short, plain English (not internal code names), Current value: large, prominent, formatted appropriately. The final answer should stay clear, actionable, and easy to review inside a dashboard architecture workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Dashboard Architecture.
