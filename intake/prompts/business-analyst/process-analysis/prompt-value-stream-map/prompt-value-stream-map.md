# Value Stream Mapping *AI Prompt *

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It separates value-adding work from waste so the team can redesign the process around flow and efficiency. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create a value stream map for the process: {{process_name}}

Value stream mapping distinguishes between value-adding and non-value-adding steps to identify waste.

1. Map the current state:
 - List every step from trigger to final output
 - For each step, classify:
 - Value-adding (VA): customer would pay for this step
 - Non-value-adding but necessary (NNVA): required by regulation, system constraint, etc.
 - Pure waste (NVA): adds no value and can be eliminated
 - Record cycle time and wait time per step

2. Calculate waste metrics:
 - Total lead time (end-to-end)
 - Total value-adding time
 - Process efficiency = VA time / Total lead time × 100%
 - Typical processes are 5–15% efficient — how does this one compare?

3. Identify the 8 Lean wastes present:
 Defects, Overproduction, Waiting, Non-utilized talent, Transportation, Inventory, Motion, Extra-processing

4. Design the future state:
 - Eliminate or reduce the top 3 waste categories
 - What would the process look like without those wastes?
 - What would the new process efficiency be?

Return: current state VSM table, waste inventory, process efficiency metrics, and future state design. 
```

## When to use this prompt 
Use case 01 
Use when you need to document how a process works from end to end. 
Use case 02 
Use when cycle time, quality, handoffs, or workload issues suggest process inefficiency. 
Use case 03 
Use during operations reviews, transformation projects, or automation assessments. 
Use case 04 
Use when you want a practical improvement plan, not only a description of the current state. 

## What the AI should return 

The AI should return a structured process analysis with steps, findings, bottlenecks or waste points, and practical recommendations. It should make roles, timings, handoffs, and decision points easy to follow, and it should clearly separate current-state observations from future-state recommendations. Where calculations are requested, include them in a readable table or summary. 

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

Once you have the first result, continue deeper with related prompts in Process Analysis.
