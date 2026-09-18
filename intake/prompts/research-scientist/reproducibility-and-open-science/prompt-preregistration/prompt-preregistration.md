# Preregistration Writer *AI Prompt *

Help me write a complete preregistration for my study. Study overview: {{study_overview}} Platform: {{platform}} (OSF, AsPredicted, ClinicalTrials.gov, PROSPERO) Preregistration... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me write a complete preregistration for my study.

Study overview: {{study_overview}}
Platform: {{platform}} (OSF, AsPredicted, ClinicalTrials.gov, PROSPERO)

Preregistration locks in your hypotheses, design, and analysis plan before data collection, preventing HARKing and p-hacking.

1. Hypotheses:
 - State each hypothesis precisely and in a way that is clearly falsifiable
 - Specify directionality: 'X will be higher than Y' not 'X and Y will differ'
 - Distinguish confirmatory hypotheses (tested with pre-specified alpha) from exploratory questions
 - Number each hypothesis: H1, H2, H3

2. Design:
 - Study type and design (RCT, observational, within-subjects, etc.)
 - Manipulations and their operationalization
 - Measures: name and description of each instrument
 - Primary outcome: specify exactly one primary outcome
 - Secondary outcomes: list all, in priority order

3. Participants:
 - Target population and eligibility criteria (inclusion and exclusion)
 - Recruitment source and procedure
 - Sample size and power analysis justification
 - Stopping rule: will data collection stop at a fixed N or at a fixed date?

4. Analysis plan:
 - Primary analysis: exact test, model specification, covariates, alpha level
 - Secondary analyses: same level of specificity
 - Handling of assumption violations: specify in advance what you will do
 - Missing data approach
 - Exclusion criteria for the analytic sample (different from eligibility)
 - Multiple comparison correction

5. What happens if:
 - Recruitment falls short of target?
 - Primary outcome has excessive missing data?
 - A key assumption is violated?
 Pre-specify contingency plans for foreseeable problems.

6. Transparency commitments:
 - Will data be shared? Where and under what conditions?
 - Will analysis code be shared?
 - Will materials be shared?

Return: complete preregistration text formatted for the chosen platform, with each section written at the level of specificity required to make it a meaningful constraint. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin reproducibility and open science work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Reproducibility and Open Science or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Hypotheses:, State each hypothesis precisely and in a way that is clearly falsifiable, Specify directionality: 'X will be higher than Y' not 'X and Y will differ'. The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Reproducibility and Open Science.
