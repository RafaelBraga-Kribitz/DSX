# Chain-of-Thought for Analysis *AI Prompts *

4 Prompts Engineer prompts in Chain-of-Thought for Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Chain-of-Thought for Analysis 
4 prompts Intermediate Single prompt 01 
### Comparative Analysis CoT 

Design a chain-of-thought prompt for rigorous comparative analysis — comparing two or more entities, time periods, or segments in data. Comparative questions ('is A better than... 
Prompt text Design a chain-of-thought prompt for rigorous comparative analysis — comparing two or more entities, time periods, or segments in data.

Comparative questions ('is A better than B?', 'what changed between Q1 and Q2?') are prone to cherry-picking evidence and confirmation bias without structured reasoning.

1. Comparative analysis CoT structure:

 Step 1 — Define what is being compared:
 'State explicitly: what are the entities being compared (A and B)? Over what time period? On what metrics?'

 Step 2 — Establish the comparison framework:
 'Before looking at the numbers, list all the metrics relevant to this comparison. This prevents cherry-picking only favorable metrics.'

 Step 3 — Gather facts for each metric:
 'For each metric: state the value for A, the value for B, the absolute difference, and the percentage difference. No interpretation yet — just facts.'

 Step 4 — Context and normalization:
 'Are the metrics comparable as-is, or do they need normalization? (e.g. revenue needs to be adjusted for market size, conversion rate needs same traffic source)'

 Step 5 — Statistical significance check:
 'For each difference: is the sample size large enough to be confident in this difference? State if sample sizes are too small to draw conclusions.'

 Step 6 — Balanced interpretation:
 'Where does A outperform B? Where does B outperform A? Are there metrics where they are effectively equal?'

 Step 7 — Synthesis:
 'Given the complete picture, what is the overall conclusion? On balance, which is better and why? What are the conditions under which this conclusion might reverse?'

2. Common mistakes to guard against (include in the prompt):
 - 'Do not declare an overall winner based on only 1–2 metrics while ignoring others.'
 - 'Do not interpret noise as signal. Differences smaller than X% on samples smaller than N should be treated as inconclusive.'
 - 'Do not use relative changes that obscure absolute differences. Always state both.'

3. Output format:
 - Comparison table: metric | A value | B value | difference | significance | winner
 - Written summary: balanced narrative, 2–3 paragraphs
 - Bottom line: one sentence conclusion with appropriate caveats

Return: the comparative analysis CoT prompt, a sample comparison scenario with data, expected CoT reasoning, and the comparison table output. Copy prompt Open prompt details Beginner Single prompt 02 
### Data Analysis CoT Prompt 

Design a chain-of-thought (CoT) prompt that guides an LLM to analyze a dataset systematically rather than jumping to conclusions. Without CoT, LLMs often pattern-match to the mo... 
Prompt text Design a chain-of-thought (CoT) prompt that guides an LLM to analyze a dataset systematically rather than jumping to conclusions.

Without CoT, LLMs often pattern-match to the most likely answer rather than reasoning through the data. CoT forces step-by-step reasoning that catches more errors and produces more reliable analysis.

1. The CoT trigger phrase:
 - End your analysis instruction with: 'Think through this step by step before giving your final answer.'
 - Alternative: 'Before answering, work through your reasoning in a <scratchpad> block.'
 - The scratchpad approach separates reasoning from the final answer, making the output cleaner

2. Analysis CoT structure to enforce:

 Instruct the model to reason through these steps explicitly:

 Step 1 — Understand the question:
 'Restate the analysis question in your own words. What exactly is being asked?'

 Step 2 — Identify what data is needed:
 'What columns, filters, or aggregations are needed to answer this question?'

 Step 3 — Check for data quality issues:
 'Before computing, scan for: missing values in key columns, outliers that could skew results, date range coverage.'

 Step 4 — Compute:
 'Perform the calculation. Show intermediate steps for any non-trivial computation.'

 Step 5 — Sanity check the result:
 'Does this result make intuitive sense? Is it in the expected order of magnitude? If it seems surprising, explain why.'

 Step 6 — Answer the question:
 'State the answer clearly in one sentence. Include the key number and appropriate context.'

3. When to use CoT vs direct prompting:
 - Use CoT for: multi-step calculations, comparisons across multiple groups, trend analysis, root cause questions
 - Use direct prompting for: simple lookups, single-step aggregations, formatting tasks
 - CoT adds tokens (cost and latency) — only use it when reasoning quality matters

4. Zero-shot CoT vs few-shot CoT:
 - Zero-shot: just add 'Think step by step' — works surprisingly well for moderate complexity
 - Few-shot: provide 2–3 complete reasoning examples — significantly better for complex or domain-specific analysis

Return: a zero-shot CoT data analysis prompt, a few-shot version with 2 complete reasoning examples, and a comparison of outputs with and without CoT on a sample analysis question. Copy prompt Open prompt details Intermediate Single prompt 03 
### Root Cause CoT Prompt 

Design a chain-of-thought prompt that guides an LLM through a data-driven root cause analysis. Context: given a metric deviation and supporting data, the LLM must reason through... 
Prompt text Design a chain-of-thought prompt that guides an LLM through a data-driven root cause analysis.

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

Return: the root cause CoT prompt, 2 test cases with complete data inputs, expected reasoning chains, and evaluation rubric. Copy prompt Open prompt details Advanced Single prompt 04 
### Self-Critique Analysis Prompt 

Design a self-critique prompt pattern where the LLM generates an initial data analysis and then critiques and improves its own output. Self-critique significantly improves analy... 
Prompt text Design a self-critique prompt pattern where the LLM generates an initial data analysis and then critiques and improves its own output.

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

Return: the three-pass prompt sequence, a test case showing how critique improved a flawed initial analysis, and a decision guide for when to use 2 vs 3 passes. Copy prompt Open prompt details 
## Recommended Chain-of-Thought for Analysis workflow 
1 
### Comparative Analysis CoT 

Start with a focused prompt in Chain-of-Thought for Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Analysis CoT Prompt 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Root Cause CoT Prompt 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Self-Critique Analysis Prompt 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
