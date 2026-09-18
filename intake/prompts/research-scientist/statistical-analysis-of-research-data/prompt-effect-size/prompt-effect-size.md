# Effect Size Interpretation *AI Prompt *

Help me calculate, report, and interpret effect sizes for my study. Study type: {{study_type}} Statistical results: {{results}} Field norms: {{field}} (what are typical effect s... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me calculate, report, and interpret effect sizes for my study.

Study type: {{study_type}}
Statistical results: {{results}}
Field norms: {{field}} (what are typical effect sizes in this field?)

1. Why effect sizes matter more than p-values:
 - A p-value tells you whether an effect exists (given sufficient sample size)
 - An effect size tells you HOW LARGE the effect is
 - With large enough samples, trivially small effects become statistically significant
 - Effect sizes allow comparison across studies and meta-analysis
 - Always report both: the p-value for the inference decision, the effect size for the magnitude interpretation

2. Effect size families and when to use each:

 Standardized mean difference family:
 - Cohen's d: difference between two means divided by pooled standard deviation. For independent groups.
 - Glass's Δ: uses only the control group SD in the denominator. Preferred when SDs differ substantially.
 - Hedges' g: small-sample correction of Cohen's d. Use when n < 20 per group.
 - Interpretation: d = 0.2 (small), 0.5 (medium), 0.8 (large) — but these are field-agnostic; use field norms when available.

 Correlation family:
 - Pearson r: linear association between two continuous variables. r = 0.1 (small), 0.3 (medium), 0.5 (large).
 - R²: proportion of variance explained. Report alongside r.
 - Partial eta squared (η²p): proportion of variance in the outcome explained by the predictor, removing other effects. For ANOVA designs.
 - Omega squared (ω²): less biased estimator of η²p. Prefer over η²p for small samples.

 Odds ratio and relative risk:
 - Odds ratio (OR): for logistic regression and case-control studies. OR = 1 means no effect.
 - Relative risk (RR): for cohort studies with binary outcomes. More interpretable than OR.
 - Number needed to treat (NNT): 1 / absolute risk reduction. Most clinically interpretable.

3. Calculate effect sizes from my results:
 - Apply the appropriate formula to my specific results
 - Include confidence intervals around each effect size estimate

4. Contextualizing the effect size:
 - Compare to typical effect sizes in {{field}}
 - Compare to effect sizes in related prior studies
 - Translate to practical significance: what does an effect of this size mean in the real world?

Return: calculated effect sizes with CIs, interpretation against field benchmarks, and a practical significance statement. 
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

The AI should return a structured result that covers the main requested outputs, such as Why effect sizes matter more than p-values:, A p-value tells you whether an effect exists (given sufficient sample size), An effect size tells you HOW LARGE the effect is. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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
