# Product Experiment Prioritization *AI Prompt *

Prioritize this backlog of product experiments for the next quarter. Experiment ideas: {{experiment_list}} Current traffic: {{daily_active_users}} DAU Team capacity: {{capacity}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Prioritize this backlog of product experiments for the next quarter.

Experiment ideas: {{experiment_list}}
Current traffic: {{daily_active_users}} DAU
Team capacity: {{capacity}} experiments per quarter

1. Score each experiment on ICE framework:
 - Impact (1-10): how much will this move the primary metric if it works?
 - Confidence (1-10): how sure are we the hypothesis is correct? (prior evidence, user research)
 - Ease (1-10): how quickly and cheaply can this be built and measured?
 - ICE score = (Impact + Confidence + Ease) / 3

2. Feasibility check:
 - For each experiment: calculate required sample size at 80% power, alpha=0.05, and the team's stated MDE
 - Calculate required duration: sample_size / (DAU x traffic_allocation_rate)
 - Flag experiments requiring > 8 weeks as impractical for the quarter

3. Dependency and conflict check:
 - Are any experiments testing overlapping UI elements or user flows? (Cannot run simultaneously)
 - Does any experiment depend on another being completed first?
 - Map experiment conflicts and dependencies

4. Learning value:
 - Even if a test is negative, what do we learn?
 - Prioritize experiments that resolve fundamental product questions over marginal optimizations

5. Recommended quarter plan:
 - Select experiments that fit within capacity, avoid conflicts, and maximize learning
 - Sequence them: which experiments must run first to unblock others?
 - Reserve 20% capacity for urgent or opportunistic tests

Return: ICE scoring table, feasibility check, conflict map, and recommended quarter experiment plan with sequencing. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin experimentation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Experimentation or the wider Product Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Score each experiment on ICE framework:, Impact (1-10): how much will this move the primary metric if it works?, Confidence (1-10): how sure are we the hypothesis is correct? (prior evidence, user research). The final answer should stay clear, actionable, and easy to review inside a experimentation workflow for product analyst work. 

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

Once you have the first result, continue deeper with related prompts in Experimentation.
