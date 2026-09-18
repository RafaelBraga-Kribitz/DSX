# Multiple Testing Correction *AI Prompt *

This prompt helps design, size, analyze, or govern experiments in a structured way. It is useful when a team wants to make product or process decisions based on evidence instead of opinion. The output should balance statistical rigor with practical business judgment so stakeholders can act confidently. It adjusts significance decisions when many metrics or variants were tested at once. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply multiple testing corrections to this experiment that tested multiple metrics or multiple variants simultaneously.

Test data provided includes {{num_metrics}} metrics and/or {{num_variants}} variants.

1. Explain the multiple testing problem:
 - With {{num_tests}} independent tests at α=0.05, the probability of at least one false positive is {{familywise_error_rate}}%
 - Without correction, we are likely to see spurious significant results

2. Apply and compare three correction methods:
 a. Bonferroni correction: α_adjusted = 0.05 / number of tests
 b. Holm-Bonferroni (step-down): less conservative than Bonferroni
 c. Benjamini-Hochberg (FDR): controls false discovery rate at 5%

3. For each metric, show: raw p-value | Bonferroni adjusted | Holm adjusted | BH adjusted | significant after each correction?

4. Recommend which correction method to use for this specific test and why

5. Re-state the decision recommendation after applying the correction — does it change?

Return: corrected p-value table, method comparison, and final decision recommendation. 
```

## When to use this prompt 
Use case 01 
Use when a product, growth, or operations team wants to test a change rigorously. 
Use case 02 
Use before launch to design an experiment or after launch to interpret results. 
Use case 03 
Use when you need to calculate sample size, validate significance, or diagnose weak tests. 
Use case 04 
Use when a decision depends on evidence rather than intuition or stakeholder opinion. 

## What the AI should return 

The AI should return a decision-ready experiment output with the requested calculations, assumptions, and interpretation clearly labeled. Statistical reasoning should be explained in plain language, and the response should distinguish significance, practical impact, risks, and next steps. Any recommendation should be explicit, defensible, and tied to the evidence provided. 

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

Once you have the first result, continue deeper with related prompts in AB Testing and Experimentation.
