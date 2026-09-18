# Process Map *AI Prompt *

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It documents a business process in a structured, role-based format that is easy to review and improve. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create a structured process map for: {{process_name}}

Based on the provided process description or interview notes:

1. Document the process in a standard swim-lane format:
 - Identify the actors/roles involved (each gets a swim lane)
 - List each step in sequence
 - Show decision points (diamonds) with Yes/No branches
 - Show where inputs enter and outputs leave the process
 - Show system touchpoints at each step

2. Since this is text-based, represent the process map as:
 - A numbered step list with the actor, action, system, and decision/output for each step
 - Indented sub-steps for branches

3. Add metadata per step:
 - Average time to complete
 - Who is responsible (RACI: Responsible, Accountable, Consulted, Informed)
 - System or tool used
 - Common errors or exceptions

4. Summarize: total end-to-end time, total number of handoffs, and total number of decision points

Return: structured process map, step metadata table, and summary statistics. 
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
