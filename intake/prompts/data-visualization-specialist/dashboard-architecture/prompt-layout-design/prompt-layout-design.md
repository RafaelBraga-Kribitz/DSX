# Dashboard Layout Design *AI Prompt *

Design the layout and information hierarchy for this dashboard. Dashboard purpose: {{purpose}} Audience: {{audience}} Key decisions it supports: {{decisions}} Available metrics:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design the layout and information hierarchy for this dashboard.

Dashboard purpose: {{purpose}}
Audience: {{audience}}
Key decisions it supports: {{decisions}}
Available metrics: {{metrics}}
Tool: {{tool}} (Tableau, Power BI, Looker, Grafana, custom web)

1. F-pattern and Z-pattern reading order:
 - Eyes enter top-left and move right, then sweep left and down
 - Most important information: top-left
 - Secondary importance: top-right and left side
 - Supporting detail: bottom and center
 - Apply this: place the single most important KPI top-left, supporting context bottom-right

2. Dashboard sections (top to bottom):

 Row 1 — Header KPIs (always visible):
 - 3–5 key numbers with period-over-period change and direction indicator
 - These answer 'is everything okay?' at a glance
 - Format: large number + small label + change % + arrow color

 Row 2 — Trend overview:
 - Primary time series chart showing the main metric over the full period
 - Answers: 'what is the trend?'

 Row 3 — Breakdown charts:
 - How does the main metric break down by the most important dimension?
 - Typically 2–3 charts side by side (by region, by product, by channel)

 Row 4 — Supporting detail:
 - Tables, secondary metrics, drill-down content
 - Content that contextualizes the summary above

3. Filter placement:
 - Global filters (date range, region, segment): top of dashboard, always visible
 - Local filters (applying only to one section): near the section they affect
 - Filter defaults: set to the most common use case, not blank

4. Whitespace:
 - Sufficient padding between charts (minimum 16px)
 - Grouped charts have smaller internal padding, larger padding from other groups
 - Do not compress charts to fit more — whitespace is not wasted space

5. Responsive considerations:
 - Will this be viewed on mobile? Design for the smallest screen first.
 - Vertical stacking for mobile: the top KPI row must be fully visible without scrolling

6. Number of charts:
 - Rule of thumb: ≤ 8 charts on a single screen without scrolling
 - More than 8: split into multiple dashboard pages or tabs
 - Each chart must be independently interpretable — no 'see chart 3 for context'

Return: sketch layout description (rows, columns, chart assignments), filter specification, whitespace guidelines, and mobile adaptation notes. 
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

The AI should return a structured result that covers the main requested outputs, such as F-pattern and Z-pattern reading order:, Eyes enter top-left and move right, then sweep left and down, Most important information: top-left. The final answer should stay clear, actionable, and easy to review inside a dashboard architecture workflow for data visualization specialist work. 

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
