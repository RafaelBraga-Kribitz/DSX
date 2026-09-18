# Bottleneck Identification *AI Prompt *

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It finds the process step that most constrains flow and prioritizes fixes based on business impact. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Identify and prioritize the bottlenecks in this business process using the data provided.

A bottleneck is a step where work accumulates, throughput is constrained, or cycle time is disproportionately long.

1. For each process step, analyze:
 - Average cycle time (how long does this step take?)
 - Wait time before this step (how long does work sit waiting to be processed?)
 - Volume (how many units pass through this step per day/week?)
 - Error rate and rework rate at this step
 - Utilization rate of the resource at this step (% of time actively working)

2. Calculate total cycle time vs total value-add time: what % of end-to-end time actually adds value?

3. Apply the Theory of Constraints: identify the single biggest constraint. Everything else is secondary until this is resolved.

4. For each bottleneck identified:
 - Root cause: is it a people, process, system, or data problem?
 - Business impact: what is the cost of this bottleneck in time, money, or customer experience?
 - Recommended fix: quick win vs longer-term solution

Return: bottleneck analysis table, constraint identification, and prioritized improvement actions. 
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
