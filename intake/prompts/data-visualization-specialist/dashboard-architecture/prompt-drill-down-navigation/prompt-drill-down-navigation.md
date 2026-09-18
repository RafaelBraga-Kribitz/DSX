# Drill-Down Navigation Design *AI Prompt *

Design a drill-down navigation structure for this dashboard so users can move from summary to detail without losing context. Dashboard: {{dashboard_name}} Data hierarchy: {{hier... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a drill-down navigation structure for this dashboard so users can move from summary to detail without losing context.

Dashboard: {{dashboard_name}}
Data hierarchy: {{hierarchy}} (e.g. Region → Country → Store → Product)
User journey: {{user_journey}} (what questions do users typically ask in sequence?)

1. The drill-down mental model:
 Users start at a high-level summary and need to progressively answer:
 Level 1: Is everything okay? (KPI overview)
 Level 2: Where is the problem? (Dimensional breakdown)
 Level 3: Why is it happening? (Root cause detail)
 Level 4: Which specific items? (Row-level detail table)

 Design each level to naturally lead to the next.

2. Navigation patterns:

 Click-through drill-down:
 - Clicking a bar/point navigates to a lower-level page filtered to that value
 - User knows they are drilling by the breadcrumb trail: All Regions > EMEA > UK
 - Back button returns to parent level
 - Best for: hierarchical data with many levels

 Tooltip drill-down:
 - Hovering reveals a mini chart or additional metrics in a tooltip
 - No navigation required
 - Best for: quick context without leaving the current view

 Filter-driven drill-down:
 - Clicking a dimension value filters all charts on the page
 - Charts update in place rather than navigating to a new page
 - Best for: exploratory analysis where users want to compare across the drill dimension

 Expandable rows (table drill-down):
 - Summary rows expand to show sub-rows
 - Best for: tabular hierarchies (product category → subcategory → SKU)

3. Breadcrumb design:
 - Always show the current position in the hierarchy: Home > Sales > EMEA > UK
 - Each level is clickable to navigate back
 - Current level is not a link (it is where you are)
 - Place breadcrumb at the top of the page, below the header

4. Preserving filter context:
 - When drilling down, carry all existing filters to the lower level
 - Clearly show which filters are active at all times
 - Provide a 'Reset all filters' option
 - If a filter is incompatible with the drill-down target, warn the user

5. Back navigation:
 - Always provide a back button or breadcrumb link
 - Browser back button should also work (no JavaScript state navigation that breaks back button)
 - Return to parent level with the same view state the user left

6. Mobile drill-down:
 - Tap a chart element to reveal a details panel (not navigate away)
 - Full-screen detail view for tables on mobile

Return: navigation pattern recommendation, breadcrumb design specification, filter persistence rules, and mobile navigation approach. 
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

The AI should return a structured result that covers the main requested outputs, such as The drill-down mental model:, Navigation patterns:, Clicking a bar/point navigates to a lower-level page filtered to that value. The final answer should stay clear, actionable, and easy to review inside a dashboard architecture workflow for data visualization specialist work. 

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
