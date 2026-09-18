# Observational Study Design *AI Prompt *

Design an observational study and plan the appropriate analysis to control for confounding. Exposure of interest: {{exposure}} Outcome of interest: {{outcome}} Available data: {... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an observational study and plan the appropriate analysis to control for confounding.

Exposure of interest: {{exposure}}
Outcome of interest: {{outcome}}
Available data: {{data_description}}
Study type: {{study_type}} (cross-sectional, case-control, cohort)

1. Study design selection:

 Cross-sectional:
 - Exposure and outcome measured at the same time
 - Pros: fast, cheap, good for prevalence estimation
 - Cons: cannot establish temporality; prone to reverse causation
 - Best for: estimating associations and generating hypotheses

 Case-control:
 - Sample based on outcome (cases vs controls), then measure past exposure
 - Pros: efficient for rare outcomes
 - Cons: recall bias; selection of controls is critical
 - Analysis: conditional or unconditional logistic regression; effect measure = odds ratio

 Prospective cohort:
 - Sample based on exposure status, follow forward to measure outcomes
 - Pros: can measure incidence, multiple outcomes, avoids recall bias
 - Cons: expensive, slow; loss to follow-up threatens validity
 - Analysis: survival analysis (Cox model), incidence rate ratio; effect measure = hazard ratio, RR

 Retrospective cohort:
 - Historical data used to construct a cohort; follow forward in time using existing records
 - Faster than prospective; subject to data quality of historical records

2. Confounding control methods:

 Design-stage:
 - Restriction: limit study to a homogeneous subgroup (removes confounding from that variable)
 - Matching: match cases and controls (or exposed and unexposed) on potential confounders
 - Advantage: guaranteed balance; disadvantage: cannot study matched variables as exposures

 Analysis-stage:
 - Multivariable regression: include confounders as covariates
 - Propensity score methods (see propensity score prompt)
 - Stratification: estimate effect within strata of the confounder, then pool with Mantel-Haenszel

3. Bias assessment:
 - Selection bias: is the study sample representative of the target population?
 - Information bias: are exposure and outcome measured accurately?
 - Confounding: have all major confounders been measured and controlled?
 - Use a directed acyclic graph (DAG) to identify the minimal sufficient adjustment set

4. Directed Acyclic Graph (DAG):
 - Draw the causal diagram: nodes = variables, arrows = direct causal effects
 - Identify confounders: common causes of exposure and outcome
 - Identify colliders: common effects of two variables (do NOT adjust for colliders — this opens a non-causal path)
 - Use the backdoor criterion to identify the adjustment set

Return: study design recommendation, confounding control plan, DAG specification, and bias assessment. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin experimental design work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Experimental Design or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Study design selection:, Exposure and outcome measured at the same time, Pros: fast, cheap, good for prevalence estimation. The final answer should stay clear, actionable, and easy to review inside a experimental design workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Experimental Design.
