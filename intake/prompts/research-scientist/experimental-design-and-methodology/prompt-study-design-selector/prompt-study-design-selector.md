# Study Design Selector *AI Prompt *

Help me choose the right study design for my research question. Research question: {{research_question}} Available resources: {{resources}} (time, budget, sample access) Field/d... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me choose the right study design for my research question.

Research question: {{research_question}}
Available resources: {{resources}} (time, budget, sample access)
Field/domain: {{field}}

1. Classify my research question:
 - Is this a question about description (what is the prevalence or distribution of X)?
 - Is this a question about association (is X related to Y)?
 - Is this a question about causation (does X cause Y)?
 - Is this a question about mechanism (how or why does X cause Y)?
 The appropriate study design depends critically on this classification.

2. Present the candidate designs:

 For descriptive questions:
 - Cross-sectional survey: snapshot of a population at one point in time. Pros: fast, cheap. Cons: no temporal information, cannot establish causality.
 - Case series / case report: detailed description of a small number of cases. Pros: useful for rare phenomena. Cons: no comparison group, cannot generalize.

 For association questions:
 - Observational cohort: follow a group over time and measure exposures and outcomes. Pros: can assess temporality (X precedes Y). Cons: expensive, slow, confounding.
 - Case-control: compare people who have the outcome to those who do not and look back at exposures. Pros: efficient for rare outcomes. Cons: recall bias, cannot estimate prevalence.
 - Cross-sectional: measure exposure and outcome at the same time. Pros: fast. Cons: cannot determine temporal order.

 For causal questions:
 - Randomized controlled trial (RCT): gold standard for causality. Randomly assign participants to treatment or control. Pros: eliminates confounding. Cons: expensive, ethical constraints, artificial settings.
 - Quasi-experiment: exploit natural variation in treatment assignment (difference-in-differences, regression discontinuity, instrumental variables). Pros: more realistic than RCT. Cons: requires strong assumptions.
 - Natural experiment: an external event creates as-if random assignment. Pros: high external validity. Cons: rare and not controllable.

3. Apply the evidence hierarchy:
 - Rank the feasible designs for my question from strongest to weakest causal inference
 - Identify which designs are feasible given my resources and constraints

4. Recommendation:
 - Recommend the strongest feasible design
 - State clearly: what causal claims can this design support, and what claims it cannot
 - Identify the top 2 threats to validity in the recommended design and how to mitigate them

Return: design recommendation with full rationale, validity threat analysis, and a one-paragraph justification suitable for a methods section. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin experimental design and methodology work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Experimental Design and Methodology or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Classify my research question:, Is this a question about description (what is the prevalence or distribution of X)?, Is this a question about association (is X related to Y)?. The final answer should stay clear, actionable, and easy to review inside a experimental design and methodology workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Experimental Design and Methodology.
