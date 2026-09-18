# Multiple Testing in Finance *AI Prompt *

Address the multiple testing problem in this quantitative research context. Research context: {{context}} (number of strategies tested, signals screened, parameters optimized) N... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Address the multiple testing problem in this quantitative research context.

Research context: {{context}} (number of strategies tested, signals screened, parameters optimized)
Number of tests performed: {{n_tests}}

1. The multiple testing problem in finance:
 - With 100 independent tests at α = 0.05, expect 5 false positives by chance alone
 - Finance researchers test thousands of factors, strategies, and parameter combinations
 - Harvey, Liu, and Zhu (2016): with 315 published factors by 2012, the minimum t-statistic needed for significance should be 3.0, not 2.0
 - Most published factor premiums may be false discoveries

2. Family-wise error rate (FWER) corrections:
 Controls the probability of ANY false positive:

 Bonferroni correction:
 - α_adjusted = α / n_tests
 - For 100 tests at α = 0.05: α_adjusted = 0.0005 (t-stat ≈ 3.5 required)
 - Conservative: assumes all tests are independent (they rarely are)

 Holm-Bonferroni (step-down):
 - Less conservative than Bonferroni while still controlling FWER
 - Sort p-values: p(1) ≤ p(2) ≤ ... ≤ p(m)
 - Reject H(i) if p(i) ≤ α / (m - i + 1)

3. False Discovery Rate (FDR) corrections:
 Controls the expected proportion of false positives among rejections:
 More powerful than FWER methods when many tests are truly non-null.

 Benjamini-Hochberg (BH) procedure:
 - Sort p-values: p(1) ≤ p(2) ≤ ... ≤ p(m)
 - Find largest k such that p(k) ≤ (k/m) × q (target FDR = q, e.g. q = 0.10)
 - Reject all H(1) through H(k)
 - Appropriate when you have many tests and can tolerate some false positives

 Storey's q-value:
 - Adaptive FDR: estimates the proportion of true null hypotheses π₀ and adjusts
 - More powerful than BH when many tests are truly non-null

4. Bootstrap-based multiple testing:
 - White's Reality Check: tests whether the best-performing strategy outperforms after accounting for selection
 - Romano-Wolf stepdown procedure: controls FWER while being less conservative than Bonferroni
 - Procedure: permute returns to create null distribution of max performance statistics

5. Adjusting t-statistics for multiple comparisons:
 Following Harvey et al. (2016):
 - Minimum t-statistic for significance given M prior tests: t_min ≈ sqrt(log(M/2) × 2 × (1 + log(1/q)))
 - For M = 100, q = 0.05: t_min ≈ 3.0
 - For M = 1000, q = 0.05: t_min ≈ 3.5

6. Practical recommendations:
 - Pre-specify tests before looking at data
 - Report all tests performed, not just significant ones
 - Apply BH or Romano-Wolf correction to all reported results
 - Require t > 3.0 as a baseline for any factor claiming to be new

Return: adjusted p-values under each correction method, required t-statistics for significance, and multiple testing corrections applied to my specific results. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical and econometric methods work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical and Econometric Methods or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The multiple testing problem in finance:, With 100 independent tests at α = 0.05, expect 5 false positives by chance alone, Finance researchers test thousands of factors, strategies, and parameter combinations. The final answer should stay clear, actionable, and easy to review inside a statistical and econometric methods workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Statistical and Econometric Methods.
