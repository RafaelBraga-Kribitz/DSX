# LLM-as-Judge Evaluation *AI Prompt *

Design a reliable LLM-as-judge system to evaluate the quality of data analysis outputs at scale. Human evaluation is the gold standard but does not scale. LLM-as-judge enables a... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a reliable LLM-as-judge system to evaluate the quality of data analysis outputs at scale.

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

Return: judge prompt, calibration procedure, consistency test, and a dashboard for tracking judge-assessed quality over time. 
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

The AI should return a structured result that covers the main requested outputs, such as When LLM-as-judge is appropriate:, When human evaluation is too expensive or slow to run at scale, For outputs where correctness has a nuanced, rubric-based definition. The final answer should stay clear, actionable, and easy to review inside a prompt testing and evaluation workflow for prompt engineer work. 

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
