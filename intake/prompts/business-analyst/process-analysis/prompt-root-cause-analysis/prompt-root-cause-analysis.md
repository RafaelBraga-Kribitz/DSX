# Root Cause Analysis *AI Prompt *

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It uses proven problem-solving methods to move from symptoms to a changeable root cause. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a structured root cause analysis (RCA) for this problem: {{problem_statement}}

Use the following structured approach:

1. Problem definition:
 - What exactly happened? (Specific, measurable)
 - When did it start? Is it recurring?
 - What is the business impact? (Quantify: cost, time, customer impact)

2. Five Whys analysis:
 - Why did the problem occur? [Answer 1]
 - Why did [Answer 1] occur? [Answer 2]
 - Continue until you reach the root cause (usually 4–6 levels deep)
 - Stop when the answer is a system, process, or policy that can be changed

3. Fishbone (Ishikawa) analysis:
 - Categorize potential causes under: People, Process, Technology, Data, Environment
 - For each category, list 2–3 contributing factors
 - Mark which are confirmed, suspected, or ruled out

4. Root cause confirmation:
 - Which cause, if fixed, would prevent the problem from recurring?
 - What evidence supports this as the root cause?

5. Corrective actions:
 - Immediate containment: stop the bleeding now
 - Root cause fix: prevent recurrence
 - Systemic improvement: prevent similar problems elsewhere

Return: Five Whys chain, fishbone diagram (text format), confirmed root cause, and action plan. 
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
