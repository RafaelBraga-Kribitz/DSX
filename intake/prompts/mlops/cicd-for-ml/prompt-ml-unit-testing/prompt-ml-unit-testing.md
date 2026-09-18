# ML Unit Testing *AI Prompt *

This prompt writes a comprehensive unit test suite for ML code, covering preprocessing, feature engineering, models, losses, metrics, and smoke tests. It is best for improving code reliability in projects where data and training logic are more complex than standard application code. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a comprehensive unit test suite for this ML codebase.

ML code has unique testing challenges: stochasticity, large data dependencies, and complex multi-step pipelines. These patterns address them.

1. Preprocessing tests:
 - Test each transformation function with a minimal synthetic DataFrame
 - Test edge cases: all-null column, single row, empty DataFrame, columns with extreme values
 - Test idempotency: applying the transformation twice produces the same result as applying it once
 - Test dtype contracts: output dtypes match expectations regardless of input variation

2. Feature engineering tests:
 - Test each feature computation function independently
 - Assert feature values are within expected ranges
 - Test for data leakage: features computed on a single row must not access other rows' data
 - Test lag/rolling features: verify the correct temporal offset is applied

3. Model architecture tests:
 - Test forward pass: model accepts the expected input shape and returns the expected output shape
 - Test output range: for classifiers, softmax outputs sum to 1; probabilities are in [0,1]
 - Test gradient flow: loss.backward() does not produce NaN or Inf gradients
 - Test model save/load: saved model produces identical outputs to the original model

4. Loss function tests:
 - Perfect predictions → loss = 0 (or near zero)
 - Random predictions → loss is within the expected range for the problem
 - Gradient check: torch.autograd.gradcheck passes

5. Metric tests:
 - Test each metric function: verify output equals a hand-calculated expected value on a small example
 - Test edge cases: all-same-class predictions, perfect predictions, all-wrong predictions

6. No-train test (smoke test for the training loop):
 - Run 1 training step on a tiny synthetic dataset
 - Assert: loss decreases after the first step, model parameters change, no errors thrown

Return: test suite covering all categories, with fixtures for synthetic data and a pytest configuration. 
```

## When to use this prompt 
Use case 01 
when an ML codebase lacks strong automated tests 
Use case 02 
when preprocessing and feature engineering need precise correctness checks 
Use case 03 
when model save-load, gradient flow, and metric correctness should be tested 
Use case 04 
when you want pytest fixtures and a practical ML testing structure 

## What the AI should return 

A structured ML unit test suite with synthetic fixtures, category-specific tests, smoke checks, and pytest configuration. 

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

Once you have the first result, continue deeper with related prompts in CI/CD for ML.
