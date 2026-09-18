# LLM Benchmark and Evaluation Suite *AI Prompt *

Design a comprehensive evaluation suite for this LLM application before production deployment. Application: {{application}} Key capabilities required: {{capabilities}} Risk leve... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a comprehensive evaluation suite for this LLM application before production deployment.

Application: {{application}}
Key capabilities required: {{capabilities}}
Risk level: {{risk_level}}
Stakeholders: {{stakeholders}}

1. Evaluation dimensions:
 A production LLM evaluation must cover:
 - Capability: can the model perform the required tasks?
 - Accuracy / factuality: does the model produce correct outputs?
 - Safety: does the model avoid harmful outputs?
 - Robustness: does the model perform consistently across diverse inputs?
 - Latency and cost: does the model meet operational requirements?

2. Task-specific capability evaluation:
 - Create a golden test set: 200-500 examples with verified ground truth answers
 - Measure: exact match, F1, ROUGE, or human evaluation depending on the task type
 - Segment by difficulty: easy / medium / hard / adversarial

3. Standard benchmark references:
 - General reasoning: MMLU, HellaSwag, ARC, WinoGrande
 - Coding: HumanEval, MBPP, SWE-Bench
 - Math: GSM8K, MATH
 - Safety: TruthfulQA, BBQ (bias benchmark), WinoBias, ToxiGen
 - Long context: SCROLLS, LONGBENCH
 - Custom: build a domain-specific eval set from real user queries

4. Safety evaluation:
 - Refusal appropriateness: does the model correctly refuse harmful requests WITHOUT over-refusing legitimate ones?
 - Harmful content rate: % of responses containing harmful content across 1000+ adversarial prompts
 - Bias audit: test for demographic bias using equivalent prompts differing only in group identity
 - Consistency: does the model give the same answer to paraphrase of the same question?

5. LLM-as-judge meta-evaluation:
 - Use GPT-4 or Claude as an independent judge to score a sample of outputs
 - Validate the LLM judge's scores against human labels on 100 examples (inter-rater reliability)
 - LLM judges are biased toward verbose, confident-sounding responses — account for this

6. A/B evaluation protocol:
 - For each model version change: compare 500+ output pairs using LLM-as-judge
 - Report: win rate, tie rate, loss rate vs baseline
 - Minimum detectable difference: with 500 pairs at alpha = 0.05, can detect 5% difference in win rate

7. Pre-launch checklist:
 ☐ Capability eval: primary metric >= target on golden test set
 ☐ Safety eval: harmful content rate < 0.1% on adversarial prompts
 ☐ Latency: p99 < SLA on realistic load
 ☐ Regression: no capability drop vs baseline > 5%
 ☐ Bias audit: no demographic group has significantly worse outcomes
 ☐ Guardrail stack tested and validated

Return: evaluation suite design, benchmark selection, golden test set construction, safety test plan, and pre-launch checklist. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin evaluation and safety work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Evaluation and Safety or the wider LLM Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Evaluation dimensions:, Capability: can the model perform the required tasks?, Accuracy / factuality: does the model produce correct outputs?. The final answer should stay clear, actionable, and easy to review inside a evaluation and safety workflow for llm engineer work. 

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

Once you have the first result, continue deeper with related prompts in Evaluation and Safety.
