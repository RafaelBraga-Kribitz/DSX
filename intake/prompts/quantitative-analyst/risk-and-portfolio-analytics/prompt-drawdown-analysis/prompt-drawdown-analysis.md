# Drawdown Analysis *AI Prompt *

Conduct a comprehensive drawdown analysis for this strategy or portfolio. Return series: {{returns}} Benchmark (optional): {{benchmark}} 1. Drawdown calculation: - Cumulative we... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Conduct a comprehensive drawdown analysis for this strategy or portfolio.

Return series: {{returns}}
Benchmark (optional): {{benchmark}}

1. Drawdown calculation:
 - Cumulative wealth index: W_t = ∏(1 + r_i) for i = 1 to t
 - Running maximum: M_t = max(W_1, W_2, ..., W_t)
 - Drawdown at time t: DD_t = (W_t - M_t) / M_t
 - Maximum drawdown (MDD): min(DD_t) over full period

2. Drawdown statistics:
 - Maximum drawdown: magnitude and the peak and trough dates
 - Average drawdown: mean of all drawdown episodes
 - Average drawdown duration: average time from peak to trough
 - Average recovery time: average time from trough to new high water mark
 - Number of drawdown episodes exceeding threshold (e.g. >5%, >10%, >20%)
 - Current drawdown: is the strategy currently in a drawdown?

3. Drawdown distribution:
 - Plot all drawdown episodes sorted by severity
 - Are large drawdowns rare events or do they cluster?
 - Drawdown at each percentile (50th, 75th, 90th, 95th) of episode severity

4. Underwater curve analysis:
 - Plot the cumulative return and the underwater curve (time spent in drawdown) on the same chart
 - What fraction of total time was the strategy in a drawdown?
 - Pain index: average drawdown × fraction of time in drawdown

5. Risk-adjusted return ratios involving drawdown:
 - Calmar ratio: annualized return / |MDD|. Higher is better. Benchmark: > 0.5
 - Sterling ratio: annualized return / average of top 3 annual drawdowns
 - Burke ratio: annualized return / sqrt(sum of squared drawdowns)
 - Martin ratio (Ulcer index-based): annualized return / Ulcer_index
 Ulcer index = sqrt(mean(DD²)): penalizes both depth and duration of drawdowns

6. Drawdown comparison to benchmark:
 - Relative drawdown: active drawdown = portfolio DD - benchmark DD
 - Did the strategy protect capital better or worse than the benchmark during major drawdown periods?
 - Maximum relative drawdown and its timing

Return: drawdown statistics table, underwater curve plot, drawdown episode list, ratio comparison, and benchmark relative analysis. 
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

The AI should return a structured result that covers the main requested outputs, such as Drawdown calculation:, Cumulative wealth index: W_t = ∏(1 + r_i) for i = 1 to t, Running maximum: M_t = max(W_1, W_2, ..., W_t). The final answer should stay clear, actionable, and easy to review inside a risk and portfolio analytics workflow for quantitative analyst work. 

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
