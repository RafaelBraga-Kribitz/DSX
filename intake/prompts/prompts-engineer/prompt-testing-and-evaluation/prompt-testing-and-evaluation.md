# Prompt Testing and Evaluation *AI Prompts *

3 Prompts Engineer prompts in Prompt Testing and Evaluation. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Prompt Testing and Evaluation 
3 prompts Advanced Single prompt 01 
### LLM-as-Judge Evaluation 

Design a reliable LLM-as-judge system to evaluate the quality of data analysis outputs at scale. Human evaluation is the gold standard but does not scale. LLM-as-judge enables a... 
Prompt text Design a reliable LLM-as-judge system to evaluate the quality of data analysis outputs at scale.

Human evaluation is the gold standard but does not scale. LLM-as-judge enables automated quality evaluation across thousands of outputs — if done correctly.

1. When LLM-as-judge is appropriate:
 - When human evaluation is too expensive or slow to run at scale
 - For outputs where correctness has a nuanced, rubric-based definition
 - As a first-pass filter before human review of borderline cases
 - NOT appropriate as a sole quality gate for high-stakes outputs

2. Judge prompt design (critical — garbage in, garbage out):

 a. Role and task:
 'You are an expert data analyst evaluating the quality of an AI-generated data analysis. Your evaluation must be objective and based only on the criteria below.'

 b. Evaluation rubric (specific dimensions with clear descriptions):
 'Score the analysis on each dimension from 1 to 5:
 - Factual accuracy (1–5): Are all numbers and statistics correctly stated? Does the analysis accurately describe the data?
 - Logical reasoning (1–5): Does the analysis reason correctly from data to conclusions? Are any logical leaps unjustified?
 - Completeness (1–5): Does the analysis address the question fully? Are important insights missing?
 - Clarity (1–5): Is the analysis clearly written and easy for a business audience to understand?
 - Actionability (1–5): Does the analysis lead to a clear, specific recommended action?'

 c. Output format:
 'Return a JSON object: {"factual_accuracy": N, "logical_reasoning": N, "completeness": N, "clarity": N, "actionability": N, "overall": N, "key_issues": ["issue 1", "issue 2"], "strengths": ["strength 1"]}'

3. Reliability safeguards:
 - Reference answer: provide the correct answer alongside the candidate output so the judge can compare
 - Position bias mitigation: if comparing two outputs, run the judge twice with A/B order swapped; average the scores
 - Calibration: measure judge agreement with human evaluators on 50 calibration examples; adjust if disagreement > 20%

4. Judge validation:
 - Test the judge on known good outputs (should score > 4 on all dimensions)
 - Test on known bad outputs (should score < 2 on accuracy when factual errors are present)
 - Measure consistency: run the same input through the judge 5 times and check score variance (should be < 0.5 std)

Return: judge prompt, calibration procedure, consistency test, and a dashboard for tracking judge-assessed quality over time. Copy prompt Open prompt details Intermediate Single prompt 02 
### Prompt Evaluation Dataset Builder 

Build a systematic evaluation dataset for measuring the quality of a data-focused LLM prompt. A good eval dataset is the foundation of prompt engineering — without it, you are g... 
Prompt text Build a systematic evaluation dataset for measuring the quality of a data-focused LLM prompt.

A good eval dataset is the foundation of prompt engineering — without it, you are guessing whether your prompt improvements are real.

1. Evaluation dataset requirements:
 - Minimum size: 50–200 examples (fewer → high variance in measurements, more → diminishing returns)
 - Distribution: representative of real production inputs, not just easy cases
 - Coverage: includes rare but important edge cases
 - Ground truth: each example has a verified correct output (human-labeled or programmatically verifiable)

2. Dataset construction methods:

 a. Sample from production (best for real-world relevance):
 - Sample 200 recent production inputs randomly
 - Stratify by input complexity: simple / medium / complex
 - Have domain experts label the expected output for each

 b. Programmatic generation (best for edge cases):
 - Generate inputs algorithmically to cover specific scenarios
 - Example for an extraction prompt: generate documents with 0 fields, 1 field, all fields, conflicting fields, malformed values
 - Use a template + parameter grid to generate all combinations

 c. Adversarial examples (best for robustness):
 - Inputs designed to trigger failure modes: very long text, unusual formatting, ambiguous cases
 - Include examples where the correct output is 'no information found' rather than a value

3. Ground truth creation:
 - For extraction tasks: human annotators label expected fields and values
 - Inter-annotator agreement: have 2 annotators label the same 20% of examples; measure agreement; resolve disagreements
 - For SQL generation: execute the SQL and compare results to expected results
 - For analysis tasks: define a rubric and have domain experts score outputs 1–5

4. Eval metrics per task type:
 - Extraction: field-level precision and recall
 - Classification: accuracy, F1 per class
 - SQL generation: execution accuracy (does the SQL run and return correct results?)
 - Analysis: rubric score (factual accuracy, clarity, completeness)

5. Dataset maintenance:
 - Add 5 new examples per month from production failures
 - Re-label examples when the ground truth definition changes
 - Track dataset version alongside prompt version

Return: dataset construction procedure, annotation guide, inter-annotator agreement calculation, metric implementations per task type, and dataset versioning schema. Copy prompt Open prompt details Intermediate Single prompt 03 
### Prompt Regression Test Suite 

Build a regression test suite to detect when prompt changes break existing behavior. Prompts are code. When you change a prompt, you need to verify that all previously working c... 
Prompt text Build a regression test suite to detect when prompt changes break existing behavior.

Prompts are code. When you change a prompt, you need to verify that all previously working cases still work — just like software regression testing.

1. Test case structure:
 Each test case has:
 - test_id: unique identifier
 - description: what this test verifies
 - input: the exact input to the prompt
 - expected_output: the exact expected output (for exact match tests) OR
 - expected_properties: properties the output must satisfy (for semantic tests)
 - tags: categories for running subsets (e.g. 'edge_case', 'high_priority', 'numeric')

2. Test types for data prompts:

 a. Exact match tests:
 - For deterministic outputs (extraction, formatting, SQL generation with temperature=0)
 - output == expected_output
 - Run with temperature=0 for reproducibility

 b. Schema validation tests:
 - Output must conform to the expected JSON schema
 - Use jsonschema.validate()

 c. Semantic equivalence tests:
 - For analysis outputs where wording may vary but meaning must be the same
 - Use a judge LLM: 'Does this output convey the same information as the expected output? Answer yes or no and explain.'
 - Or use sentence similarity (cosine similarity of embeddings > 0.9)

 d. Property tests:
 - Check specific properties: 'revenue value is a positive number', 'date is in ISO 8601 format', 'no fields are missing'
 - More robust than exact match for outputs with variability

3. Test execution:
 - Run the full suite before every prompt change is deployed
 - Track pass rate over time — a declining pass rate indicates prompt drift
 - Run with multiple seeds (temperature > 0) for stochastic tests to measure variance

4. Building the initial test set:
 - Start with 20–30 representative cases covering the main input patterns
 - Add an edge case test every time a bug is found and fixed
 - Prioritize: 5 critical tests that must always pass (core functionality), 20 standard tests, N edge case tests

5. CI/CD integration:
 - Run critical tests on every PR that touches the prompt
 - Run the full suite before every production deployment
 - Block deployment if critical test pass rate < 100% or overall pass rate < 90%

Return: test case schema, test runner implementation, judge LLM integration for semantic tests, and CI/CD configuration. Copy prompt Open prompt details 
## Recommended Prompt Testing and Evaluation workflow 
1 
### LLM-as-Judge Evaluation 

Start with a focused prompt in Prompt Testing and Evaluation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Prompt Evaluation Dataset Builder 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Prompt Regression Test Suite 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
