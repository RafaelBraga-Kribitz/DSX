# Sensitivity and Scenario Analysis *AI Prompt *

Build a sensitivity and scenario analysis framework for this financial model. Base case model: {{model_description}} Key output metric: {{output}} (e.g. EV, IRR, EBITDA, EPS) Ke... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a sensitivity and scenario analysis framework for this financial model.

Base case model: {{model_description}}
Key output metric: {{output}} (e.g. EV, IRR, EBITDA, EPS)
Key input assumptions: {{inputs}}

1. One-way sensitivity analysis:
 For each key input, vary it across a range while holding all others constant:
 - Range: +/-20%, +/-10%, +/-5% from base case
 - Show output at each input level
 - Tornado chart: rank inputs by their impact on the output (largest impact at top)
 - The top 3 inputs by tornado rank are the most important assumptions to get right

2. Two-way sensitivity table:
 Select the top 2 most impactful inputs from the tornado chart.
 Build a 5x5 table:
 - Rows: Input 1 at 5 levels (base-20% to base+20%)
 - Columns: Input 2 at 5 levels
 - Cell values: output metric at each combination
 - Color code: green = above base case output, red = below

3. Scenario analysis (distinct named scenarios):
 Base case: current assumptions
 Upside scenario: best plausible combination of assumptions (not maximum of each)
 Downside scenario: worst plausible combination (not minimum of each)
 Stress case: severe downside - what happens in a recession or crisis?

 For each scenario:
 - State the 3-5 key assumption changes vs base case
 - Show the output metric range
 - Narrative: what business or macro environment drives this scenario?

4. Break-even analysis:
 - For the primary output metric: at what level of each key input does the output reach breakeven?
 - Example: 'At what revenue growth rate does the IRR reach our minimum threshold of 15%?'

Return: tornado chart description, two-way sensitivity table, scenario comparison table, and break-even levels for each key input. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin financial modeling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Financial Modeling or the wider Financial Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as One-way sensitivity analysis:, Range: +/-20%, +/-10%, +/-5% from base case, Show output at each input level. The final answer should stay clear, actionable, and easy to review inside a financial modeling workflow for financial analyst work. 

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

Once you have the first result, continue deeper with related prompts in Financial Modeling.
