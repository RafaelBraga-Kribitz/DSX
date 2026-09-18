# PSI Implementation *AI Prompt *

This prompt implements Population Stability Index for numeric and categorical features in a production-ready way, including edge cases, vectorization, and tests. It is best when PSI needs to be a reusable library component rather than a one-off notebook calculation. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a production-grade Population Stability Index (PSI) calculation for both numeric and categorical features.

1. PSI formula:
 PSI = Σ (Actual% - Expected%) × ln(Actual% / Expected%)
 Where bins are defined on the reference (expected) distribution

2. Numeric feature PSI:
 - Define bins on the reference distribution (use quantile-based bins for robustness to outliers)
 - Number of bins: 10 for PSI (more bins = more sensitive but noisier)
 - Bin definition: [min, q10, q20, ..., q90, max] from the reference distribution
 - For the current distribution: count observations falling into each reference bin
 - Edge cases:
 - Empty bin in reference: replace with a small value (0.001) to avoid division by zero
 - Empty bin in current: replace with a small value (0.001) to avoid log(0)
 - Values outside reference range: assign to the first or last bin

3. Categorical feature PSI:
 - Each category is a bin
 - Reference frequencies: category counts / total reference rows
 - Current frequencies: category counts / total current rows
 - New categories (in current but not in reference): assign to an 'OTHER' bin
 - Missing categories (in reference but not in current): use 0.001 floor

4. Batch PSI computation (for multiple features at once):
 - Vectorized implementation using pandas or NumPy
 - Return a DataFrame: feature_name | psi_score | num_bins | reference_date | current_date | status

5. Validation:
 - Unit test: PSI of identical distributions should be ≈ 0
 - Unit test: PSI of completely different distributions should be > 0.5
 - Smoke test: PSI is always ≥ 0

6. Performance:
 - For large datasets (>10M rows): compute PSI on a random 10% sample — PSI is stable with sampling
 - Benchmark: should compute PSI for 100 features in < 30 seconds

Return: PSI implementation for numeric and categorical features, unit tests, batch computation function, and performance benchmark. 
```

## When to use this prompt 
Use case 01 
when you need a robust PSI utility for production pipelines 
Use case 02 
when numeric and categorical features must both be supported 
Use case 03 
when batch PSI over many features should be fast and testable 
Use case 04 
when edge cases such as empty bins and unseen categories matter 

## What the AI should return 

A production-grade PSI implementation with numeric and categorical support, batch computation, unit tests, and basic benchmarking. 

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

Once you have the first result, continue deeper with related prompts in Drift Detection.
