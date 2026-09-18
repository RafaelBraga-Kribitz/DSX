# Full LLM Application Chain *AI Prompt *

Step 1: Requirements and architecture decision - define the task, output format, latency SLA, cost budget, and safety requirements. Decide: prompting only vs RAG vs fine-tuning... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Requirements and architecture decision - define the task, output format, latency SLA, cost budget, and safety requirements. Decide: prompting only vs RAG vs fine-tuning vs agent. Document the decision rationale.
Step 2: Prompt design - write the system prompt and user prompt template. Specify the output schema (JSON or structured text). Add grounding and anti-hallucination instructions. Create 20 test cases including 5 adversarial examples.
Step 3: Retrieval design (if RAG) - design the chunking strategy, embedding model selection, and vector database. Configure hybrid search with a cross-encoder re-ranker. Define the retrieval evaluation metrics (precision, recall, faithfulness).
Step 4: Evaluation framework - build the golden test set (100+ examples with verified answers). Define metrics: task accuracy, faithfulness, instruction following, safety. Run the LLM judge pipeline. Establish regression baselines.
Step 5: Safety and guardrails - design input classification (prompt injection, harmful content). Design output validation (PII, content safety, format compliance). Define the human review routing policy for high-risk cases.
Step 6: Infrastructure - design the API integration with retry logic, cost tracking, and caching. Configure the LLM gateway. Set up latency, cost, and error rate monitoring. Define alerting thresholds.
Step 7: Deployment and monitoring - deploy with shadow mode first. Run A/B test vs baseline. Configure production monitoring: latency, cost, guardrail trigger rate, hallucination rate. Define the retraining or re-prompting trigger criteria. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin llm infrastructure work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in LLM Infrastructure or the wider LLM Engineer library. 

## What the AI should return 

The AI should return a structured result that is directly usable in a llm infrastructure workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in llm engineer work. 

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

Once you have the first result, continue deeper with related prompts in LLM Infrastructure.
