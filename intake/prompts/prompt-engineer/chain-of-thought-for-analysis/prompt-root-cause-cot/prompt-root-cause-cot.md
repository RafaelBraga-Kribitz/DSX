# Root Cause CoT Prompt *AI Prompt *

Design a chain-of-thought prompt that guides an LLM through a data-driven root cause analysis. Context: given a metric deviation and supporting data, the LLM must reason through... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a chain-of-thought prompt that guides an LLM through a data-driven root cause analysis.

Context: given a metric deviation and supporting data, the LLM must reason through possible causes systematically rather than anchoring on the first plausible explanation.

1. The anchoring bias problem:
 - Without explicit CoT, LLMs tend to latch onto the first plausible cause and construct evidence to support it
 - The prompt must force the model to generate and evaluate multiple hypotheses before selecting one

2. Root cause CoT structure:

 Phase 1 — Problem characterization:
 'Before investigating causes, fully characterize the problem:
 - What changed? (metric, direction, magnitude)
 - When did it change? (onset, duration, pattern: sudden vs gradual)
 - Where is it concentrated? (which segments, regions, or products account for the most deviation)
 - What did NOT change? (other metrics that are stable, ruling out systemic causes)'

 Phase 2 — Hypothesis generation (before looking at evidence):
 'Generate 5 possible causes for this deviation WITHOUT evaluating likelihood yet.
 Force yourself to consider: seasonal effects, data pipeline issues, product changes, external events, and measurement errors.'

 Phase 3 — Evidence evaluation:
 'For each hypothesis, evaluate the evidence FOR and AGAINST it from the provided data.
 Be explicit about what evidence would be needed to confirm or rule out each hypothesis.'

 Phase 4 — Hypothesis ranking:
 'Rank the 5 hypotheses from most to least likely. Justify each ranking with specific evidence.'

 Phase 5 — Conclusion:
 'State the most likely root cause. State your confidence level (High/Medium/Low). State the key assumption that, if wrong, would change your conclusion.'

3. Anti-hallucination guardrails:
 - 'Do not cite data that was not provided in the input. If you need data you do not have, say so.'
 - 'If the available data is insufficient to determine the root cause, say so explicitly rather than speculating.'

4. Structured output:
 - The scratchpad contains the full CoT reasoning
 - The final answer is a concise summary: root cause, confidence, key evidence, and next diagnostic step

Return: the root cause CoT prompt, 2 test cases with complete data inputs, expected reasoning chains, and evaluation rubric. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin chain-of-thought for analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Chain-of-Thought for Analysis or the wider Prompt Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The anchoring bias problem:, Without explicit CoT, LLMs tend to latch onto the first plausible cause and construct evidence to support it, The prompt must force the model to generate and evaluate multiple hypotheses before selecting one. The final answer should stay clear, actionable, and easy to review inside a chain-of-thought for analysis workflow for prompt engineer work. 

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

Once you have the first result, continue deeper with related prompts in Chain-of-Thought for Analysis.
