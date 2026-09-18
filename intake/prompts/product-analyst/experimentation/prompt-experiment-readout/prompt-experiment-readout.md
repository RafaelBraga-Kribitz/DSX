# Experiment Readout Template *AI Prompt *

Write a complete experiment readout for this concluded A/B test. Experiment: {{experiment_name}} Hypothesis: {{hypothesis}} Results data: {{results}} Audience: product team and... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a complete experiment readout for this concluded A/B test.

Experiment: {{experiment_name}}
Hypothesis: {{hypothesis}}
Results data: {{results}}
Audience: product team and leadership

1. TL;DR (3 sentences):
 - What was tested, what was the result, and what is the recommendation?

2. Background:
 - Problem being solved
 - Hypothesis and expected direction of change
 - Primary metric and guardrail metrics

3. Setup:
 - Variants: control and treatment description
 - Traffic allocation and targeting
 - Test duration and sample size achieved vs required

4. Results:
 - Primary metric: control value, treatment value, absolute difference, % difference, p-value, 95% CI
 - Secondary metrics: same format for each
 - Guardrail metrics: did any degrade significantly?
 - Segment breakdown: results by key segments (mobile/desktop, new/returning, plan type)

5. Interpretation:
 - Is the result statistically significant? Practically significant?
 - Are results consistent across segments or driven by one segment?
 - Any unexpected findings worth investigating?

6. Decision:
 - Ship / Do not ship / Iterate / Run follow-up test
 - If shipping: rollout plan (% of traffic, timeline)
 - If iterating: what specifically changes in the next version?

7. Learnings:
 - What did this test teach us about user behavior?
 - How does this inform future experiments or roadmap decisions?

Return: complete experiment readout document suitable for sharing with the product team. 
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

The AI should return a structured result that covers the main requested outputs, such as TL;DR (3 sentences):, What was tested, what was the result, and what is the recommendation?, Background:. The final answer should stay clear, actionable, and easy to review inside a experimentation workflow for product analyst work. 

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
