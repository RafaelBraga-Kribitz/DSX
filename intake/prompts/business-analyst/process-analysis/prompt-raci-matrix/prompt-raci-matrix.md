# RACI Matrix Builder *AI Prompt *

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It clarifies who does the work, who owns the result, and where accountability gaps exist. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a RACI matrix for the process or project: {{process_or_project}}

RACI definitions:
- R (Responsible): does the work
- A (Accountable): owns the outcome, approves deliverables. Only one A per task.
- C (Consulted): provides input before the task is done
- I (Informed): notified after the task is done

1. List all tasks or decisions in the process as rows
2. List all roles (not people) involved as columns
3. For each task × role intersection, assign R, A, C, I, or blank

4. Check for RACI anti-patterns and flag:
 - Multiple A for a single task: accountability ambiguity — assign one owner
 - No R for a task: who is actually doing this work?
 - R without A: work with no accountability — add an owner
 - Too many C or I on one task: decision-making will be slow — trim the list
 - A role with no tasks: are they needed?

5. Highlight the top 3 process risks revealed by the RACI analysis

Return: formatted RACI matrix, anti-pattern flags with recommended fixes, and process risk summary. 
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
