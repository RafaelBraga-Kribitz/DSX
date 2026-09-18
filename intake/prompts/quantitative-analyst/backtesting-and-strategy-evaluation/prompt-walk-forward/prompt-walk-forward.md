# Walk-Forward Validation *AI Prompt *

Design and execute a walk-forward validation framework to assess strategy robustness out-of-sample. Strategy: {{strategy}} Total data period: {{period}} Parameters to optimize:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and execute a walk-forward validation framework to assess strategy robustness out-of-sample.

Strategy: {{strategy}}
Total data period: {{period}}
Parameters to optimize: {{parameters}}

1. Walk-forward validation framework:
 - Training window: {{training_length}} months (used for parameter optimization)
 - Test window: {{test_length}} months (out-of-sample evaluation)
 - Step: {{step_size}} months (how often to re-optimize)
 - Total OOS periods: (total_months - training_months) / step_size

 Process for each fold:
 1. Train: optimize parameters on training window to maximize {{objective}} (e.g. Sharpe)
 2. Freeze: lock the optimal parameters from the training window
 3. Test: evaluate the frozen strategy on the next test window
 4. Step: advance both windows by the step size
 5. Repeat until the end of data

2. Walk-forward variants:
 - Anchored (expanding window): training window grows over time. More data but may include stale regimes.
 - Rolling (fixed window): training window moves with a fixed length. Adapts to regime changes but discards old data.
 - Recommendation: compare both; if they diverge significantly, parameters are regime-dependent.

3. Concatenated OOS performance:
 - Concatenate all test period results into a single OOS return series
 - This is the most realistic performance estimate: uses only OOS data
 - Report: Sharpe, Calmar, max drawdown, win rate, and turnover on the OOS series

4. In-sample vs out-of-sample performance ratio:
 - IS Sharpe / OOS Sharpe: if > 2, significant overfitting
 - Minimum OOS Sharpe ≥ 50% of IS Sharpe: rough guideline for acceptable overfitting
 - If OOS performance is dramatically worse: the strategy is overfit, not robust

5. Parameter stability analysis:
 - Plot the optimal parameter value chosen at each training step over time
 - Are optimal parameters stable across windows or do they oscillate?
 - High instability → the strategy is sensitive to parameter choice → not robust
 - A strategy with robust parameters will show similar optimal values across training windows

6. Number of OOS periods required:
 - Need at least 30 OOS periods (folds) for statistical inference on OOS performance
 - With 30 periods at monthly frequency: 2.5 years of OOS data
 - With 3-month test windows: need 7.5 years of OOS data — this is a significant requirement

Return: walk-forward performance table (IS vs OOS per fold), concatenated OOS Sharpe and drawdown, parameter stability plots, and overfitting assessment. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin backtesting and strategy evaluation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Backtesting and Strategy Evaluation or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Walk-forward validation framework:, Training window: {{training_length}} months (used for parameter optimization), Test window: {{test_length}} months (out-of-sample evaluation). The final answer should stay clear, actionable, and easy to review inside a backtesting and strategy evaluation workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Backtesting and Strategy Evaluation.
