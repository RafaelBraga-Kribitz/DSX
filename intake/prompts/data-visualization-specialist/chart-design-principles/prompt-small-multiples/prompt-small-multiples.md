# Small Multiples Design *AI Prompt *

Design a small multiples layout for this dataset instead of a cluttered single chart. Dataset: {{dataset_description}} Dimension to facet by: {{facet_dimension}} (region, produc... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a small multiples layout for this dataset instead of a cluttered single chart.

Dataset: {{dataset_description}}
Dimension to facet by: {{facet_dimension}} (region, product, segment, etc.)
Number of facets: {{n_facets}}
Key metric: {{metric}}

Small multiples (trellis charts, faceted charts) show the same chart type repeated for each value of a dimension. They enable comparison across groups while keeping each individual panel clean and readable.

1. When to use small multiples vs overlaid series:
 Use small multiples when:
 - More than 4–5 series on a single chart becomes tangled (spaghetti chart)
 - The comparison is across rather than within the dimension
 - Patterns within each panel are more important than the exact values between panels

 Use overlaid series (single chart) when:
 - You need exact value comparison between series at the same time point
 - There are only 2–3 series and they don't overlap heavily

2. Layout design:
 - Grid arrangement: prefer rows × columns that are wider than tall (landscape orientation)
 - Panel count guideline: 4–12 panels is the readable range. > 20 panels requires a different approach.
 - Panel size: large enough to show the pattern clearly, small enough that all panels fit on one screen/page
 - Aspect ratio: each panel should follow the banking to 45° rule — line slopes close to 45° are most readable

3. Shared axes (critical for comparability):
 - ALL panels must share the same x and y axis scales unless explicitly communicating within-panel patterns
 - Do NOT use independent (free) scales unless the goal is to show pattern shape, not magnitude
 - If scales differ substantially between panels: use a log scale or explicitly label each panel's scale range

4. Ordering of panels:
 - By magnitude: sort panels by the most meaningful summary statistic (e.g. total revenue)
 - Alphabetically: only if magnitude order is not meaningful
 - By natural order: time, geography, hierarchy
 - Never: random order

5. Labeling in small multiples:
 - Panel titles: short and above each panel (not below)
 - Remove x-axis labels from all but the bottom row
 - Remove y-axis labels from all but the leftmost column
 - Shared axis titles: one title spanning the entire grid edge, not repeated per panel
 - Highlight a reference pattern: add a light grey copy of the overall average/total in each panel for reference

6. Highlighting across panels:
 - Use the same highlight color in each panel to emphasize the same element (e.g. the current period)
 - Add a reference line at the overall average in each panel so viewers can see which panels are above or below

Return: layout specification (rows × columns, panel size), axis sharing rules, panel ordering recommendation, and labeling specification. 
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

The AI should return a structured result that covers the main requested outputs, such as When to use small multiples vs overlaid series:, More than 4–5 series on a single chart becomes tangled (spaghetti chart), The comparison is across rather than within the dimension. The final answer should stay clear, actionable, and easy to review inside a chart design principles workflow for data visualization specialist work. 

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
