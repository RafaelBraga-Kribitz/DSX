# Risk Parity Construction *AI Prompt *

Construct and analyze a risk parity portfolio from this asset universe. Assets: {{assets}} Covariance matrix: {{covariance}} Target volatility: {{target_vol}} (e.g. 10% annualiz... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Construct and analyze a risk parity portfolio from this asset universe.

Assets: {{assets}}
Covariance matrix: {{covariance}}
Target volatility: {{target_vol}} (e.g. 10% annualized)

1. Risk contribution framework:
 Marginal risk contribution (MRC): MRC_i = (Σw)_i = ∂σ_p/∂w_i
 Total risk contribution (TRC): TRC_i = w_i × MRC_i
 Portfolio variance: σ²_p = w'Σw = Σ_i TRC_i
 Risk contribution percentage: RC%_i = TRC_i / σ²_p

 Risk parity condition: RC%_i = 1/N for all assets i

2. Numerical solution:
 Risk parity has no closed-form solution for N > 2 assets.
 Use gradient-based optimization:
 min Σ_i Σ_j (TRC_i - TRC_j)² subject to w'1 = 1, w ≥ 0

 Or alternatively, use Maillard et al. (2010) iterative algorithm:
 w_i ← w_i × σ_p / (N × MRC_i) → iterate until convergence

3. Risk parity portfolio analysis:
 - Report: asset weights, marginal risk contributions, percentage risk contributions
 - Verify: risk contributions are approximately equal across all assets
 - Compare weights to: equal-weight, min-variance, and 60/40 benchmark

4. Volatility targeting:
 - Scale the risk parity weights by: k = target_vol / σ_rp
 - This may require leverage if σ_rp < target_vol (common with bonds in the portfolio)
 - Report: leverage ratio, cost of leverage assumed (financing rate)

5. Sensitivity analysis:
 - How do weights change if equity volatility doubles? (Bonds get more weight)
 - How do weights change if bond-equity correlation goes from -0.3 to +0.3?
 - Risk parity is most sensitive to: changes in relative volatilities and correlation regime changes

6. Historical performance analysis:
 - Backtest the risk parity portfolio with monthly rebalancing
 - Compare to: equal-weight, 60/40, min-variance
 - Report: Sharpe ratio, Calmar ratio, max drawdown, monthly turnover
 - Notable: risk parity struggled in 2022 when bonds and equities both sold off simultaneously (positive correlation regime)

7. Limitations:
 - Risk parity is a risk-based, not return-based, allocation
 - It is implicitly long duration (bonds dominate in unlevered form)
 - Correlation instability undermines the equal risk contribution in practice

Return: risk parity weights with risk contribution verification, comparison table, sensitivity analysis, and backtest performance. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin risk and portfolio analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Risk and Portfolio Analytics or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Risk contribution framework:, Numerical solution:, Risk parity portfolio analysis:. The final answer should stay clear, actionable, and easy to review inside a risk and portfolio analytics workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Risk and Portfolio Analytics.
