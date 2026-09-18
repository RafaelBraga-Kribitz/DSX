# Overfitting Detection *AI Prompt *

Detect and quantify overfitting in this quantitative strategy or model. Strategy / model: {{strategy}} Backtest results: {{backtest_results}} Number of parameters: {{n_params}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Detect and quantify overfitting in this quantitative strategy or model.

Strategy / model: {{strategy}}
Backtest results: {{backtest_results}}
Number of parameters: {{n_params}}
In-sample period: {{is_period}}
Out-of-sample period: {{oos_period}}

1. The overfitting problem in quantitative finance:
 - Financial time series are noisy with low signal-to-noise ratios
 - The probability of backtest overfitting (PBO) is high even with careful methodology
 - Bailey, Borwein, Lopez de Prado, Zhu (2014): with 45 backtests, random chance will produce one Sharpe > 1.5 even if there is no true alpha

2. Deflated Sharpe Ratio (DSR):
 DSR accounts for the number of trials and the statistical properties of the backtest:
 DSR = PSR(SR*) where PSR is the Probabilistic Sharpe Ratio
 SR* = SR_benchmark × sqrt(1 - ρ + N × ρ × (1 - 1/N)) ← effective benchmark adjusted for N trials
 - Report: number of trials N, assumed independent trials, DSR value
 - DSR < 0.95 after accounting for N trials: likely overfit

3. Probabilistic Sharpe Ratio (PSR):
 PSR(SR*) = Φ[(SR - SR*) × sqrt(T-1) / sqrt(1 - γ₃SR + (γ₄-1)/4 × SR²)]
 Where γ₃ = skewness, γ₄ = kurtosis of returns
 - PSR measures the probability that the true Sharpe exceeds a benchmark (e.g. 0 or 0.5)
 - PSR < 0.95 at benchmark SR = 0: cannot rule out that true SR ≤ 0

4. Minimum Backtest Length (MinBTL):
 MinBTL = (SR / SR_hat)² × (1 - ρ + N × ρ) × (1 + (1 - γ₃SR + (γ₄-1)/4 × SR²) / (T-1))⁻¹
 - Given N trials and observed SR, what minimum backtest length is needed to be 95% confident the strategy is not overfit?
 - If actual backtest length < MinBTL: almost certainly overfit

5. Combinatorial Purged Cross-Validation (CPCV):
 - Split data into T non-overlapping folds
 - Generate all C(T, 2) combinations of training/test splits (each combination is one path)
 - Compute performance on each test path
 - PBO: fraction of test paths where OOS performance is worse than expected
 - Advantage: uses all data for both training and testing; robust to regime selection

6. Parameter sensitivity check:
 - Perturb each parameter by ±10% and ±25% from optimal value
 - Plot performance surface around the optimal point
 - Robust strategy: flat performance surface around optimal (many local parameter combinations work)
 - Overfit strategy: sharp performance spike at optimal (only exact values work)

Return: DSR calculation, PSR, MinBTL, CPCV results, parameter sensitivity surface, and overfitting probability assessment. 
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

The AI should return a structured result that covers the main requested outputs, such as The overfitting problem in quantitative finance:, Financial time series are noisy with low signal-to-noise ratios, The probability of backtest overfitting (PBO) is high even with careful methodology. The final answer should stay clear, actionable, and easy to review inside a backtesting and strategy evaluation workflow for quantitative analyst work. 

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
