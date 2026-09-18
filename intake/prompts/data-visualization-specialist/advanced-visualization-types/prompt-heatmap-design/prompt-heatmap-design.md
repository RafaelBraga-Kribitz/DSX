# Heatmap Design Guide *AI Prompt *

Design an effective heatmap for this data. Data: {{data_description}} Rows: {{row_dimension}} Columns: {{column_dimension}} Values: {{value_metric}} 1. When to use a heatmap: -... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an effective heatmap for this data.

Data: {{data_description}}
Rows: {{row_dimension}}
Columns: {{column_dimension}}
Values: {{value_metric}}

1. When to use a heatmap:
 - When the combination of two categorical or ordinal dimensions determines an outcome
 - When there are too many cells for individual bar charts
 - When the pattern across the full matrix is the insight (not individual values)
 - Classic uses: hour-of-day × day-of-week, correlation matrix, cohort retention

2. Color scale selection:
 - Sequential (one direction): light = low, dark = high. Use for: volume, count, positive metrics.
 - Diverging (two directions from midpoint): use for: correlation (-1 to +1), deviation from target (negative to positive), profit/loss.
 - Categorical: only if cells represent categories, not values

 Color scale specifics:
 - For retention or positive rates: white/light → brand color
 - For correlation matrices: blue → white → red (standard in statistics)
 - For profit/loss: red → white → green
 - Always: make the color scale legend visible with clear breakpoints labeled

3. Ordering rows and columns:
 - Do NOT use alphabetical order unless that is meaningful
 - Order by: magnitude (row total descending), natural order (Mon–Sun, Jan–Dec), or hierarchical clustering
 - Hierarchical clustering: groups similar rows and columns together, revealing pattern blocks

4. Cell annotations:
 - Add the value in each cell when: precision matters AND the matrix is small (< 100 cells)
 - For large matrices: use color only, with hover tooltips for exact values
 - Number format: 1 decimal for percentages; abbreviate large numbers (1.2M)
 - Text color: use dark text on light cells, light text on dark cells (auto-switch at midpoint)

5. Size and aspect ratio:
 - Square cells: ideal for correlation matrices where both dimensions are the same concept
 - Rectangular cells: for matrices where row and column dimensions differ substantially
 - Target: cells large enough to read the annotation (minimum 30×30px for annotated cells)

6. Marginal summaries:
 - Add row totals (right side) and column totals (bottom)
 - Use a lighter shade or a bar chart strip for marginals
 - This helps interpret relative importance of each row/column

Return: color scale specification, ordering recommendation, annotation rules, and marginal summary design. 
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

The AI should return a structured result that covers the main requested outputs, such as When to use a heatmap:, When the combination of two categorical or ordinal dimensions determines an outcome, When there are too many cells for individual bar charts. The final answer should stay clear, actionable, and easy to review inside a advanced visualization types workflow for data visualization specialist work. 

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
