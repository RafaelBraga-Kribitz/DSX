# Confound Identification *AI Prompt *

Systematically identify the confounding variables and alternative explanations that threaten the validity of my study. Study design: {{study_design}} Main relationship of intere... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Systematically identify the confounding variables and alternative explanations that threaten the validity of my study.

Study design: {{study_design}}
Main relationship of interest: {{main_relationship}} (X → Y)
Sample and context: {{sample_context}}

1. What is a confounder:
 A confounder is a variable Z that:
 - Is associated with the exposure/predictor X
 - Is associated with the outcome Y
 - Is NOT on the causal pathway between X and Y (not a mediator)
 If Z is not controlled for, the observed X-Y association will be biased.

2. Confounder brainstorming — work through these categories:
 a. Demographic confounders: age, sex, gender, race/ethnicity, socioeconomic status, education
 b. Behavioral confounders: lifestyle factors, prior behavior, health behaviors, technology use
 c. Temporal confounders: secular trends, seasonality, historical events that coincide with the study
 d. Selection confounders: how participants were recruited, who chose to participate, who dropped out
 e. Measurement confounders: how X was measured (method, instrument, assessor) may differ across levels of Y
 f. Domain-specific confounders: {{field}}-specific factors I should consider

3. For each identified confounder, assess:
 - Direction of bias: does this confounder inflate or deflate the X-Y association?
 - Magnitude of potential bias: is this likely to be a minor or major source of bias?
 - Measurability: can this confounder be measured and controlled?

4. Strategies to address each confounder:
 - Randomization: if using an experiment, randomization balances all confounders in expectation
 - Restriction: limit the sample to a narrow range of the confounder (e.g. study only one age group)
 - Matching: match treatment and control participants on key confounders
 - Statistical adjustment: include confounders as covariates in the model
 - Stratification: analyze subgroups separately
 - Instrumental variables / natural experiments: if confounders are unmeasurable

5. Residual confounding:
 Even after adjustment, some confounding will remain. State explicitly:
 - Which confounders cannot be measured and therefore cannot be controlled
 - The likely direction and magnitude of residual confounding
 - What this means for the causal interpretation of your results

Return: confounder list with bias direction and magnitude assessment, proposed control strategy per confounder, and a residual confounding statement suitable for a limitations section. 
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

The AI should return a structured result that covers the main requested outputs, such as What is a confounder:, Is associated with the exposure/predictor X, Is associated with the outcome Y. The final answer should stay clear, actionable, and easy to review inside a experimental design and methodology workflow for research scientist work. 

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
