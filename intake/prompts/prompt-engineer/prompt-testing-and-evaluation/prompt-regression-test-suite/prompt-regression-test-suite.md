# Prompt Regression Test Suite *AI Prompt *

Build a regression test suite to detect when prompt changes break existing behavior. Prompts are code. When you change a prompt, you need to verify that all previously working c... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a regression test suite to detect when prompt changes break existing behavior.

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

Return: test case schema, test runner implementation, judge LLM integration for semantic tests, and CI/CD configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin prompt testing and evaluation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Prompt Testing and Evaluation or the wider Prompt Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Test case structure:, test_id: unique identifier, description: what this test verifies. The final answer should stay clear, actionable, and easy to review inside a prompt testing and evaluation workflow for prompt engineer work. 

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

Once you have the first result, continue deeper with related prompts in Prompt Testing and Evaluation.
