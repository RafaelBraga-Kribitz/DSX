# Multiple Testing Correction *AI Prompt *

Apply appropriate multiple testing corrections to this set of hypothesis tests. Number of tests: {{n_tests}} Raw p-values: {{p_values}} Test context: {{context}} (exploratory an... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Apply appropriate multiple testing corrections to this set of hypothesis tests.

Number of tests: {{n_tests}}
Raw p-values: {{p_values}}
Test context: {{context}} (exploratory analysis, confirmatory study, family of related tests)
Error rate to control: {{error_rate}} (FWER or FDR)

1. The multiple testing problem:
 If you run k independent tests each at alpha = 0.05, the probability of at least one false positive is:
 FWER = 1 - (1 - 0.05)^k
 For k=20: FWER = 64%. For k=100: FWER = 99.4%.
 Uncorrected p-values in a multiple testing setting are misleading.

2. Family-wise error rate (FWER) methods:
 Controls the probability of ANY false positive across all tests.

 Bonferroni:
 - Adjusted alpha = original alpha / k
 - Reject H0 if p_i < alpha/k
 - Conservative: assumes all tests are independent
 - Best for: small number of pre-specified tests (k < 10) with strong family-wise control needed

 Holm-Bonferroni (uniformly more powerful than Bonferroni):
 - Sort p-values from smallest to largest: p(1) <= p(2) <= ... <= p(k)
 - Reject H0(i) if p(j) < alpha / (k - j + 1) for all j <= i
 - Rejects at least as many as Bonferroni, never fewer
 - Recommended over plain Bonferroni in almost all cases

3. False discovery rate (FDR) methods:
 Controls the expected proportion of false positives among rejected tests.
 Appropriate when making many tests in an exploratory context (genomics, imaging, marketing).

 Benjamini-Hochberg (BH):
 - Sort p-values from smallest to largest: p(1) <= p(2) <= ... <= p(k)
 - Find the largest i such that p(i) <= (i/k) x alpha
 - Reject all H0(j) for j <= i
 - BH guarantees E[FDP] <= alpha (under independence or positive correlation)
 - Typical FDR threshold: q = 0.05 (expect 5% of rejected hypotheses to be false positives)

4. Apply to provided p-values:
 - List all raw p-values
 - Apply Holm-Bonferroni: which tests survive?
 - Apply BH at q = 0.05: which tests survive?
 - Compare: how many more discoveries does BH yield vs Holm-Bonferroni?

5. Recommendation:
 - For confirmatory studies with strong false positive cost: FWER control (Holm-Bonferroni)
 - For exploratory studies where false negatives are costly: FDR control (BH)
 - For data-driven analysis with thousands of tests: BH or Storey's q-value

Return: FWER and FDR calculations applied to the provided p-values, comparison table, and method recommendation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin hypothesis testing work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Hypothesis Testing or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The multiple testing problem:, Family-wise error rate (FWER) methods:, Adjusted alpha = original alpha / k. The final answer should stay clear, actionable, and easy to review inside a hypothesis testing workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Hypothesis Testing.
