# Full Quant Research Chain *AI Prompt *

Step 1: Hypothesis — state the economic or behavioral rationale for why this signal should predict returns. Write it down before looking at any return data. What would falsify t... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Hypothesis — state the economic or behavioral rationale for why this signal should predict returns. Write it down before looking at any return data. What would falsify this hypothesis?
Step 2: Data protocol — define the asset universe with point-in-time construction, the signal computation with exact timing lags, the data sources, and the three-way train/validate/test split. Do not touch the test set.
Step 3: Signal construction and training set IC — compute the signal and evaluate IC, ICIR, and quintile performance on the training set only. If IC is not promising (ICIR < 0.3), return to Step 1 before proceeding.
Step 4: Parameter selection on validation set — select any free parameters (lookback windows, thresholds) on the validation set. Document the parameter search space and all results, not just the best.
Step 5: Multiple testing adjustment — apply Bonferroni or BHY correction given the number of hypotheses tested in your research program. Require t-statistic > 3.0 for a new signal to be considered genuine.
Step 6: Transaction cost and capacity analysis — estimate annualized turnover, total cost per unit of turnover, and net IC after costs. Estimate AUM capacity before market impact exceeds the gross alpha.
Step 7: Final evaluation on test set — evaluate the fully specified signal on the test set exactly once. Report all metrics: IC, ICIR, quintile spreads, net Sharpe. Compare to the validation results — large divergence suggests overfitting.
Step 8: Research report — write a complete research memo: hypothesis and rationale, data and methodology, training and validation results, multiple testing adjustments, transaction cost analysis, test set results, risks and limitations, and recommendation (implement / further research / reject). 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin quantitative research process work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Quantitative Research Process or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that is directly usable in a quantitative research process workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Quantitative Research Process.
