# Metric Decomposition Tree *AI Prompt *

This prompt helps define, evaluate, and organize the metrics a business should use to measure success. It is useful when teams need stronger alignment between strategy, performance measurement, and operational actions. The goal is to create KPIs that are meaningful, measurable, and connected to outcomes rather than vanity reporting. It breaks a top-level KPI into the smaller levers that teams can understand and influence. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a full metric decomposition tree for the top-level metric: {{top_metric}}

A decomposition tree breaks a top-level metric into its component parts, making it possible to diagnose exactly which lever to pull when the metric moves.

1. Level 1 decomposition: break {{top_metric}} into its arithmetic components
 - Example: Revenue = Users × Conversion Rate × Average Order Value
2. Level 2 decomposition: break each Level 1 component further
 - Example: Users = New Users + Returning Users
3. Level 3 decomposition where meaningful
4. For each leaf node in the tree:
 - Current value (if available)
 - Which team or person owns it
 - How quickly it can realistically change
 - What specific actions move it
5. Identify which leaf nodes have the highest leverage — a 10% improvement in which node would move the top metric the most?
6. Identify which leaf nodes are currently unmeasured

Return: full decomposition tree (text format), leverage analysis table, and measurement gap list. 
```

## When to use this prompt 
Use case 01 
Use when a team needs better metrics tied to strategy and business outcomes. 
Use case 02 
Use when existing KPIs feel noisy, redundant, or hard to act on. 
Use case 03 
Use during planning cycles, OKR setting, dashboard redesign, or metric reviews. 
Use case 04 
Use when you need clear ownership, targets, definitions, and measurement logic. 

## What the AI should return 

The AI should return a structured metric framework with clear definitions, ownership, formulas, and decision logic. The response should distinguish strategic outcomes from operational drivers, call out data gaps, and explain recommended choices in plain business language. The final output should be something a team could review and adopt, not just a brainstorm. 

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

Once you have the first result, continue deeper with related prompts in KPI Design and Strategy.
