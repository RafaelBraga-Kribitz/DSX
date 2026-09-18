# Self-Critique Analysis Prompt *AI Prompt *

Design a self-critique prompt pattern where the LLM generates an initial data analysis and then critiques and improves its own output. Self-critique significantly improves analy... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a self-critique prompt pattern where the LLM generates an initial data analysis and then critiques and improves its own output.

Self-critique significantly improves analysis quality by catching errors, unsupported conclusions, and missing context that the initial generation missed.

1. The two-pass pattern:

 Pass 1 — Initial analysis:
 Use a standard analysis prompt to generate an initial response.
 Do not add self-critique instructions yet — let the model generate its natural first response.

 Pass 2 — Self-critique (separate prompt call):
 Feed the initial analysis back to the model with this critique prompt:

 'Review the following data analysis. Critique it on these specific dimensions:

 1. Factual accuracy: Are all numbers and statistics correctly stated? Check each claim against the source data.
 2. Unsupported claims: Are any conclusions drawn that go beyond what the data supports? Flag each one.
 3. Missing context: What important context was omitted that would change the interpretation?
 4. Confounding factors: What alternative explanations were not considered?
 5. Misleading framing: Is any language used that could lead a reader to a wrong conclusion?
 6. Precision: Are confidence levels stated where appropriate? Is uncertainty acknowledged?

 For each issue found: quote the problematic text, explain the issue, and provide the corrected version.'

 Pass 3 — Revised analysis:
 'Now write a revised version of the analysis that incorporates all the corrections from your critique.'

2. When self-critique is most valuable:
 - High-stakes analyses that will be presented to leadership
 - Analyses that will inform a significant business decision
 - Any analysis containing causal claims (correlation ≠ causation)
 - Analyses where the conclusion is surprising — surprising results deserve extra scrutiny

3. Efficiency tip:
 - For most analyses, the two-pass pattern (initial + critique) is sufficient
 - Three passes (initial + critique + revised) adds quality but also cost and latency
 - Use three passes only when the stakes are high enough to justify it

4. Automated critique checklist integration:
 - Convert the critique dimensions into a checklist that runs automatically after every analysis
 - Flag outputs that trigger any checklist item for human review before distribution

Return: the three-pass prompt sequence, a test case showing how critique improved a flawed initial analysis, and a decision guide for when to use 2 vs 3 passes. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin chain-of-thought for analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Chain-of-Thought for Analysis or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The two-pass pattern:, Factual accuracy: Are all numbers and statistics correctly stated? Check each claim against the source data., Unsupported claims: Are any conclusions drawn that go beyond what the data supports? Flag each one.. The final answer should stay clear, actionable, and easy to review inside a chain-of-thought for analysis workflow for prompts engineer work. 

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
