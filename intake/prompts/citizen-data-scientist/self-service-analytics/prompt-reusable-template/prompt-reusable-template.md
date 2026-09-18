# Reusable Analysis Template *AI Prompt *

Help me create a reusable analysis template so I can repeat this analysis quickly each week or month without starting from scratch. Analysis I do repeatedly: {{analysis_descript... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me create a reusable analysis template so I can repeat this analysis quickly each week or month without starting from scratch.

Analysis I do repeatedly: {{analysis_description}}
Data source: {{data_source}}
Outputs needed: {{outputs}}

1. Template structure:
 Design a template that:
 - Has clearly labeled sections I fill in each time (date range, filter criteria, comparison period)
 - Has fixed sections that stay the same every time (the formulas, the chart types, the table structure)
 - Is easy to use for someone who did not create it (my colleague should be able to run this without asking me how)

2. What to parameterize (make easy to change):
 - Date range: make it a single cell reference that all other cells use — change it once, everything updates
 - Comparison period: prior period, same period last year, target
 - Filters: which region, product, or segment to include
 For each parameter: where to put it, how to label it, and what the default value should be

3. What to standardize (keep the same every time):
 - Column names and order
 - Chart types and formatting
 - Metric definitions — write them out once so future-me and colleagues use the same definition
 - The commentary structure (this forces you to answer the same questions every time, which makes period-over-period comparison easier)

4. Documentation to include in the template:
 - A brief description of what this template does
 - Where the data comes from and when it was last refreshed
 - Definitions of each metric
 - Known limitations or caveats
 - Who to contact if something looks wrong

5. The 'can a colleague use this?' test:
 - Could someone with similar skills use this template without any instructions from you?
 - What is the most likely point of confusion? Add a note there.

Return: a step-by-step template design with all the above elements. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin self-service analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Self-Service Analytics or the wider Citizen Data Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Template structure:, Has clearly labeled sections I fill in each time (date range, filter criteria, comparison period), Has fixed sections that stay the same every time (the formulas, the chart types, the table structure). The final answer should stay clear, actionable, and easy to review inside a self-service analytics workflow for citizen data scientist work. 

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

Once you have the first result, continue deeper with related prompts in Self-Service Analytics.
