# Annotation and Labeling Guide *AI Prompt *

Design the annotation and labeling strategy for this chart. Chart type: {{chart_type}} Key insight to communicate: {{key_insight}} Audience: {{audience}} 1. Title and subtitle s... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design the annotation and labeling strategy for this chart.

Chart type: {{chart_type}}
Key insight to communicate: {{key_insight}}
Audience: {{audience}}

1. Title and subtitle strategy:
 - Title: state the insight, not the data. 'Revenue grew 34% in Q3' beats 'Quarterly Revenue.'
 - Title should be answerable by 'so what?' — not just 'what is this?'
 - Subtitle: add essential context (time period, geography, unit, data source)
 - Format: title bold and prominent, subtitle smaller and lighter

2. Axis labels:
 - Label axes only when the unit is not obvious from the title or context
 - Remove redundant axis label if values are labeled on the chart directly
 - Rotate x-axis labels only as a last resort — prefer angled labels or flipping to horizontal bar chart
 - Units belong on the axis label or in parentheses, NOT repeated on every tick

3. Data labels (value annotations on data points):
 Guideline: use data labels OR axis + gridlines, not both.
 - Use data labels when: there are few data points and exact values matter
 - Use gridlines when: there are many data points and relative position matters more than exact values
 - For bar charts: place labels inside the bar (for long bars) or just outside (for short bars), left-aligned
 - For line charts: label only the final value, or highlight specific notable points
 - Format: use the same number formatting as the axis (1 decimal place if axis uses 1)

4. Callout annotations (highlighting specific insight):
 - Use sparingly: maximum 2–3 annotations per chart
 - Format: brief text (5–10 words) + arrow pointing to the relevant data point or region
 - Content: explain WHY this point is notable, not just WHAT the value is
 - Example: 'Spike caused by holiday campaign (Dec 15–Jan 3)' is better than 'Peak value: 42,000'

5. Reference lines and bands:
 - Target / goal line: show with a dashed line, labeled directly on the line
 - Historical average: light dashed line
 - Confidence interval or forecast range: semi-transparent shaded band, not heavy borders
 - Crisis or event periods: shaded background band with a text label at the top

6. Legend placement:
 - Prefer: direct labeling at the end of each line / top of each series (no separate legend)
 - If legend is needed: place inside the plot area (top-right or bottom-right)
 - Never: use a legend positioned below a wide chart that requires eye travel

7. What NOT to annotate:
 - Every data point (creates noise, defeats the purpose)
 - Obvious features the viewer can see clearly
 - Multiple overlapping annotations in the same chart region

Return: title and subtitle for this specific chart, axis label specification, data label strategy, callout annotation text, and legend placement decision. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin chart design principles work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Chart Design Principles or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Title and subtitle strategy:, Title: state the insight, not the data. 'Revenue grew 34% in Q3' beats 'Quarterly Revenue.', Title should be answerable by 'so what?' — not just 'what is this?'. The final answer should stay clear, actionable, and easy to review inside a chart design principles workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Chart Design Principles.
