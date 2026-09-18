# Novelty Effect Check *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It checks whether an experiment lift is real and durable or just an early reaction to something new. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Check whether this A/B test result is driven by a novelty effect rather than a genuine sustained improvement.

A novelty effect occurs when users behave differently simply because something is new — the effect fades over time as users habituate.

1. Plot the primary metric for treatment and control groups over time (day by day or week by week)
2. Check for the novelty effect pattern:
 - Large early treatment lift that narrows or disappears over time
 - Treatment performance converges toward control in later weeks
3. Segment analysis by user tenure:
 - Compare treatment effect for new users (first 30 days) vs established users (>90 days)
 - A novelty effect typically only appears in established users, not new ones
4. Compute the treatment effect for the first half vs second half of the experiment
 - If first-half effect is significantly larger than second-half, novelty effect is likely
5. Extrapolate: if the novelty effect is confirmed, what is the expected long-term steady-state lift?

Return: time series plot of treatment vs control, novelty effect diagnosis, user tenure breakdown, and long-term lift estimate. 
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
