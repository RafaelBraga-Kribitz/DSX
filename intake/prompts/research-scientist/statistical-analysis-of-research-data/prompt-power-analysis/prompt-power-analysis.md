# Power Analysis *AI Prompt *

Conduct a power analysis to determine the sample size needed for my study. Study design: {{design}} Primary statistical test: {{test}} Effect size: {{effect_size_estimate}} and... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a power analysis to determine the sample size needed for my study.

Study design: {{design}}
Primary statistical test: {{test}}
Effect size: {{effect_size_estimate}} and its source (prior study, meta-analysis, minimum clinically/practically important difference)
Desired power: 0.80 (conventional minimum) or {{desired_power}}
Alpha level: 0.05 (two-tailed) or {{alpha}}

1. Choose the effect size input correctly:

 Priority order for effect size estimation:
 a. Minimum effect size of practical/clinical importance: 'What is the smallest effect that would matter for practice or policy?' Use this if you have domain knowledge.
 b. Meta-analytic estimate: if a meta-analysis of similar studies exists, use its pooled effect size.
 c. Well-powered prior study: a single prior study estimate is noisy; treat it with caution and consider using a smaller estimate.
 d. Cohen's benchmarks (d = 0.2/0.5/0.8): use only as a last resort — these are not field-specific and lead to widely varying conclusions.

 Common mistake: using an effect size from a small pilot study. Small studies overestimate effect sizes (winner's curse). If using a pilot estimate, shrink it by 50%.

2. Run the power analysis:
 - Calculate required N for power = 0.80 and power = 0.90
 - Calculate the minimum detectable effect size at the available N
 - For the recommended design, account for: attrition (inflate N by expected dropout rate), multiple testing (if testing multiple outcomes), clustering (design effect for clustered samples)

3. Sensitivity analysis:
 - Show how required N changes if the true effect size is 50%, 75%, 100%, and 125% of the assumed effect size
 - This illustrates how sensitive the study is to assumptions about effect size

4. Present the power analysis transparently:
 Report: assumed effect size and its source, alpha level, desired power, calculated N, attrition adjustment, final recommended N. State the software/package used.

5. What to do if the required N is not feasible:
 - Use a larger alpha (0.10) only if pre-specified and justified
 - Accept lower power (0.70) only for preliminary studies
 - Narrow the target population to increase homogeneity (reduces within-group variance, increases power)
 - Use a within-subjects design (more efficient than between-subjects)
 - Use a more sensitive primary outcome
 - Abandon and redesign if power cannot exceed 0.50 — an underpowered study is usually not worth running

Return: power analysis results at multiple power levels, sensitivity analysis table, sample size recommendation with attrition adjustment, and methods text. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical analysis of research data work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical Analysis of Research Data or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Choose the effect size input correctly:, Run the power analysis:, Calculate required N for power = 0.80 and power = 0.90. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Statistical Analysis of Research Data.
