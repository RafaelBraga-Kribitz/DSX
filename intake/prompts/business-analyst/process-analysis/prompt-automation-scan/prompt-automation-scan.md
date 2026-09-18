# Automation Opportunity Scan *AI Prompt *

This prompt helps analyze how work flows through a business process and where that process can be improved. It is useful for documenting current ways of working, finding waste, identifying constraints, and designing better future-state operations. The output should support both diagnosis and action, not just description. It evaluates which process steps are the best candidates for automation and why. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Scan this process for automation opportunities and build an automation prioritization plan.

Process description and step data provided.

For each process step, evaluate automation potential:
1. Rule-based: is the logic clear, consistent, and documentable? (High automation potential)
2. Volume: how many times per day/week is this step executed? (Higher volume = higher ROI)
3. Frequency of exceptions: how often does the step require human judgment? (High exceptions = lower automation potential)
4. Data availability: is the input data digital and structured? (Yes = automatable, No = requires data capture first)
5. Regulatory risk: are there compliance reasons a human must be in the loop?

Score each step: Automation Potential (High/Medium/Low) and Automation ROI (High/Medium/Low)

For high-potential steps, specify:
- Recommended automation type: RPA, workflow automation, API integration, ML model, or full end-to-end BPA
- Estimated time savings per week
- Implementation effort in person-days
- Payback period

Return: automation opportunity matrix, prioritized automation roadmap, and estimated total time savings. 
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
