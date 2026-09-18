# Quantitative Research Process *AI Prompts *

3 Quantitative Analyst prompts in Quantitative Research Process. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts · 1 chain. 

## AI prompts in Quantitative Research Process 
3 prompts Intermediate Single prompt 01 
### Alpha Research Framework 

Design a rigorous alpha research process for evaluating new investment signals. Research question: {{hypothesis}} (e.g. 'Do stocks with improving earnings revision momentum outp... 
Prompt text Design a rigorous alpha research process for evaluating new investment signals.

Research question: {{hypothesis}} (e.g. 'Do stocks with improving earnings revision momentum outperform over the next month?')

1. Hypothesis formation (before looking at data):
 - State the economic intuition: WHY should this signal predict returns?
 - Risk premium explanation: investors demand compensation for bearing this risk
 - Behavioral explanation: systematic investor error that is exploitable
 - Structural explanation: market friction or institutional constraint creates opportunity
 - A signal without economic intuition is more likely to be a false positive
 - Write down the hypothesis before touching the data

2. Universe and data definition:
 - Define the asset universe: which assets, with what inclusion/exclusion criteria?
 - Define the signal: exactly how is it computed? What data inputs? What timing lag?
 - Data sources: where does each input come from? Is it point-in-time?
 - Survivorship bias: is the universe constructed using only assets that existed at each historical date?

3. Research protocol to prevent data snooping:
 - Split data into 3 periods BEFORE any analysis:
 - Training set (50%): hypothesis development, initial signal construction
 - Validation set (25%): parameter selection and signal refinement
 - Test set (25%): final evaluation ONCE, never used before the final test
 - Never look at the test set until the signal is fully specified
 - Document all analysis decisions and the order in which they were made

4. Signal evaluation hierarchy:
 Level 1: Statistical evidence
 - IC, ICIR, t-statistic (require t > 3.0 given prior testing in the field)
 - Quintile portfolio analysis: is the relationship monotonic?

 Level 2: Economic and institutional reality
 - Is the signal implementable? (Available in real time, not too slow to compute)
 - Survives transaction costs? (Net IC > 0 after realistic costs)
 - Capacity: at what AUM level does market impact eliminate the alpha?

 Level 3: Robustness
 - Consistent across time periods, market regimes, geographies?
 - Survives reasonable parameter perturbations?
 - Different from known factors? (Not just a proxy for value, momentum, or quality)

5. The research log:
 - Keep a contemporaneous log of every analysis run, its motivation, and its result
 - Include failed experiments: they constrain the hypothesis space for future work
 - This log is evidence against data snooping allegations

Return: hypothesis statement with economic rationale, data protocol, three-way split design, evaluation criteria, and research log template. Copy prompt Open prompt details Advanced Single prompt 02 
### Factor Crowding Assessment 

Assess whether this factor or strategy is crowded and estimate the associated risks. Factor / strategy: {{factor}} Market data: {{data}} 1. Why crowding matters: A crowded trade... 
Prompt text Assess whether this factor or strategy is crowded and estimate the associated risks.

Factor / strategy: {{factor}}
Market data: {{data}}

1. Why crowding matters:
 A crowded trade occurs when many investors hold similar positions. When they simultaneously unwind — due to redemptions, losses, or regulatory changes — the factor experiences a 'crowding unwind': rapid, correlated losses that are NOT predicted by the factor's historical distribution.

2. Crowding metrics:

 Short interest approach:
 - For a long-short factor: are the 'short' securities heavily short-sold by many investors?
 - Short interest ratio: short_shares / average_daily_volume. High = potential crowding.
 - Change in short interest: rising short interest → increasing crowding

 Institutional ownership concentration:
 - Are the 'long' positions heavily owned by a similar set of quant funds?
 - 13-F filing analysis: overlap in top holdings across quant fund portfolios
 - High overlap = high crowding risk

 Return correlation with known crowded factors:
 - Regress the factor return on returns of known crowded strategies (AQR QMOM, etc.)
 - High correlation → this factor may be susceptible to the same crowding events

 Factor return autocorrelation:
 - Crowding can create short-term momentum in factor returns (everyone piling in)
 - Followed by sharp reversals when the crowd exits
 - Look for: negative autocorrelation at 1-week lag following periods of high positive autocorrelation

3. Crowding risk indicators to monitor:
 - Pairwise correlation among factor-long stocks (rising = crowding)
 - Volatility of factor returns (rising = crowding or unwind in progress)
 - Trading volume in factor-long stocks (spiking = potential unwind)
 - Factor drawdown relative to historical distribution (severe = possible crowding unwind)

4. Historical crowding unwind events:
 - Quant Quake (August 2007): quantitative equity strategies suffered simultaneous drawdowns due to forced deleveraging
 - The unwinding was rapid (3–5 days) and not explained by macro fundamentals
 - August 2007 style analysis: regress this factor's returns on the quant quake period — was it affected?

5. Portfolio implications:
 - Position size adjustment: reduce exposure to highly crowded factors
 - Diversification: ensure the portfolio's factor exposures are not all correlated with the same crowded strategies
 - Stop-loss policy: pre-define the drawdown level at which crowding unwind is suspected and exposure is reduced

Return: crowding metrics for each indicator, comparison to historical crowding events, monitoring dashboard specification, and portfolio adjustment recommendations. Copy prompt Open prompt details Advanced Chain 03 
### Full Quant Research Chain 

Step 1: Hypothesis — state the economic or behavioral rationale for why this signal should predict returns. Write it down before looking at any return data. What would falsify t... 
Prompt text Step 1: Hypothesis — state the economic or behavioral rationale for why this signal should predict returns. Write it down before looking at any return data. What would falsify this hypothesis?
Step 2: Data protocol — define the asset universe with point-in-time construction, the signal computation with exact timing lags, the data sources, and the three-way train/validate/test split. Do not touch the test set.
Step 3: Signal construction and training set IC — compute the signal and evaluate IC, ICIR, and quintile performance on the training set only. If IC is not promising (ICIR < 0.3), return to Step 1 before proceeding.
Step 4: Parameter selection on validation set — select any free parameters (lookback windows, thresholds) on the validation set. Document the parameter search space and all results, not just the best.
Step 5: Multiple testing adjustment — apply Bonferroni or BHY correction given the number of hypotheses tested in your research program. Require t-statistic > 3.0 for a new signal to be considered genuine.
Step 6: Transaction cost and capacity analysis — estimate annualized turnover, total cost per unit of turnover, and net IC after costs. Estimate AUM capacity before market impact exceeds the gross alpha.
Step 7: Final evaluation on test set — evaluate the fully specified signal on the test set exactly once. Report all metrics: IC, ICIR, quintile spreads, net Sharpe. Compare to the validation results — large divergence suggests overfitting.
Step 8: Research report — write a complete research memo: hypothesis and rationale, data and methodology, training and validation results, multiple testing adjustments, transaction cost analysis, test set results, risks and limitations, and recommendation (implement / further research / reject). Copy prompt Open prompt details 
## Recommended Quantitative Research Process workflow 
1 
### Alpha Research Framework 

Start with a focused prompt in Quantitative Research Process so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Factor Crowding Assessment 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Full Quant Research Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
