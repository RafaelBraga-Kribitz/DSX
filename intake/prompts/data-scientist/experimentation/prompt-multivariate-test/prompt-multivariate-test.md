# Multivariate Test Analysis *AI Prompt *

This prompt evaluates A/B/n tests where multiple variants compete simultaneously. It is useful when you need a disciplined workflow that first checks for any overall difference and then controls false positives during pairwise comparisons. It also highlights outright harmful variants. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the results of this multivariate (A/B/n) test with {{num_variants}} variants.

1. Check for sample ratio mismatch across all variants
2. Run omnibus test first: is there any significant difference across all variants? (chi-squared or ANOVA)
3. If significant, run pairwise comparisons between all variant pairs using:
 - Bonferroni correction for multiple comparisons
 - Report adjusted p-values and whether each pair is significant at α=0.05 after correction
4. Compute the effect size for each variant vs control: Cohen's d (continuous) or relative lift (proportions)
5. Plot: mean metric value per variant with 95% confidence intervals
6. Identify the winning variant — highest metric value with statistical significance vs control
7. Flag any variants that are significantly worse than control (degradation alert) 
```

## When to use this prompt 
Use case 01 
You ran more than two variants in one experiment. 
Use case 02 
You need omnibus and pairwise testing with correction. 
Use case 03 
You want effect sizes and confidence intervals by variant. 
Use case 04 
You need a clear winner and degradation alerts. 

## What the AI should return 

A multivariate experiment report including SRM results, omnibus test outcome, corrected pairwise comparisons, effect sizes, confidence-interval plot, winning variant decision, and any degradation warnings. 

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
