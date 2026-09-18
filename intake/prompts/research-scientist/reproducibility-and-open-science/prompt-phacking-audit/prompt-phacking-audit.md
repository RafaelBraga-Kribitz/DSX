# P-hacking and HARKing Audit *AI Prompt *

Audit my analysis and reporting for practices that inflate false positive rates, even unintentionally. Analysis history: {{analysis_history}} Final results: {{results}} Research... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit my analysis and reporting for practices that inflate false positive rates, even unintentionally.

Analysis history: {{analysis_history}}
Final results: {{results}}

Researchers often engage in questionable research practices inadvertently. This audit helps identify and correct them.

1. P-hacking: flexibility in data analysis that increases the probability of a false positive

 Check for each practice:

 Outcome switching:
 - Was the primary outcome changed after seeing results?
 - Are results reported selectively — only outcomes that reached significance?
 - Test: compare reported outcomes to outcomes listed in the preregistration or methods section

 Optional stopping:
 - Was data collection stopped when significance was reached?
 - Was additional data collected after a non-significant result?
 - Impact: stopping when p < .05 inflates Type I error to ~14% for a nominal 5% test

 Covariate inclusion decisions:
 - Were covariates added or removed based on whether they changed the p-value?
 - Are different covariates used for different outcomes without pre-specification?

 Outlier exclusion decisions:
 - Were outlier exclusion rules determined after seeing how they affected results?
 - Were different exclusion rules applied to different outcomes?

 Subgroup analysis:
 - Were significant subgroup effects reported without pre-specification?
 - Was the overall non-significant result followed by searching for a significant subgroup?

2. HARKing: Hypothesizing After Results are Known

 Signs of HARKing:
 - Hypotheses in the paper perfectly predict the pattern of results, including null findings for control variables
 - The Introduction has an unusual post-hoc quality — theory exactly matches what was found
 - Exploratory results are presented as if they were predicted
 - No inconsistencies between the hypotheses and the results

3. For each identified practice:
 - Impact: how does this inflate Type I error?
 - Correction: what is the correct analysis or reporting approach?
 - If this was done inadvertently: how to report results honestly now

4. The correction path:
 - If analyses were done that were not pre-specified: label them as exploratory
 - If the primary outcome was changed: report results for the original primary outcome as well
 - If the result depends on a specific outlier rule: report a robustness check with the alternative rule
 - Never delete analyses that were run; include all in supplementary materials

Return: audit findings per practice, severity assessment, correction recommendations, and a transparency statement suitable for inclusion in the paper. 
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

The AI should return a structured result that covers the main requested outputs, such as P-hacking: flexibility in data analysis that increases the probability of a false positive, Was the primary outcome changed after seeing results?, Are results reported selectively — only outcomes that reached significance?. The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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
