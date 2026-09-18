# Experiment Roadmap Builder *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It helps sequence experiment ideas into a realistic roadmap that balances impact, confidence, and effort. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a 90-day experimentation roadmap for {{product_area}} based on the provided business objectives and backlog of ideas.

Idea backlog: {{ideas_list}}

1. Score each experiment idea on:
 - Expected impact: how much could this move the primary metric? (1–5)
 - Confidence in hypothesis: how strong is the evidence this will work? (1–5)
 - Implementation effort: engineering days to build (1=<3 days, 5=>20 days)
 - Sample size required: how many weeks at current traffic?
 - Learning value: even if negative, what will we learn? (1–5)

2. Score each idea using ICE score: (Impact × Confidence) / Effort

3. Apply scheduling constraints:
 - Maximum 2 experiments running simultaneously on the same surface
 - Avoid overlapping experiments that share user populations
 - Schedule quick tests (high ICE) first to build velocity

4. Produce a week-by-week experiment calendar for 90 days

5. Identify the top learning that each 30-day block is designed to answer

Return: scored idea table, ICE rankings, experiment calendar, and 30-day learning objectives. 
```

## When to use this prompt 
Use case 01 
Use when a product, growth, or operations team wants to test a change rigorously. 
Use case 02 
Use before launch to design an experiment or after launch to interpret results. 
Use case 03 
Use when you need to calculate sample size, validate significance, or diagnose weak tests. 
Use case 04 
Use when a decision depends on evidence rather than intuition or stakeholder opinion. 

## What the AI should return 

The AI should return a decision-ready experiment output with the requested calculations, assumptions, and interpretation clearly labeled. Statistical reasoning should be explained in plain language, and the response should distinguish significance, practical impact, risks, and next steps. Any recommendation should be explicit, defensible, and tied to the evidence provided. 

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

Once you have the first result, continue deeper with related prompts in AB Testing and Experimentation.
