# Alpha Research Framework *AI Prompt *

Design a rigorous alpha research process for evaluating new investment signals. Research question: {{hypothesis}} (e.g. 'Do stocks with improving earnings revision momentum outp... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a rigorous alpha research process for evaluating new investment signals.

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

Return: hypothesis statement with economic rationale, data protocol, three-way split design, evaluation criteria, and research log template. 
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

The AI should return a structured result that covers the main requested outputs, such as Hypothesis formation (before looking at data):, State the economic intuition: WHY should this signal predict returns?, Risk premium explanation: investors demand compensation for bearing this risk. The final answer should stay clear, actionable, and easy to review inside a quantitative research process workflow for quantitative analyst work. 

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
