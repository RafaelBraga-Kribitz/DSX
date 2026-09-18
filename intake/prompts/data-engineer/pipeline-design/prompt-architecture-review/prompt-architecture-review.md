# Pipeline Architecture Review *AI Prompt *

This prompt reviews a pipeline design as a production system rather than just a diagram. It helps uncover reliability, idempotency, observability, scalability, and maintainability risks before they become outages or expensive rebuilds. It is especially useful when a team has a proposed architecture but needs a structured technical critique. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Review this data pipeline architecture and identify weaknesses.

Pipeline description: {{pipeline_description}}

Evaluate across these dimensions and flag each as Critical / Warning / Info:

1. Reliability:
 - Is there a single point of failure? What happens if any one component goes down?
 - Are retries implemented with exponential backoff and jitter?
 - Is there a dead-letter queue or error sink for failed records?
 - Are downstream consumers protected from upstream failures (circuit breaker)?

2. Idempotency:
 - Can the pipeline be safely re-run without producing duplicate data?
 - Is the write operation upsert/merge rather than append-only?
 - If append-only, is there a deduplication step downstream?

3. Observability:
 - Are row counts logged at every stage (source, after transformation, at sink)?
 - Is there alerting on pipeline failure, SLA breach, and anomalous record counts?
 - Can you trace a single record from source to destination?

4. Scalability:
 - Will the design hold at 10× current data volume?
 - Are there any sequential bottlenecks that cannot be parallelized?

5. Maintainability:
 - Is business logic separated from infrastructure concerns?
 - Are transformations testable in isolation?

Return: issue list with severity, impact, and specific remediation for each finding. 
```

## When to use this prompt 
Use case 01 
When you want a design review before implementation begins. 
Use case 02 
When a pipeline has recurring failures and you suspect architectural weaknesses. 
Use case 03 
When preparing for a design review, architecture board, or readiness assessment. 
Use case 04 
When you need a prioritized remediation list instead of generic feedback. 

## What the AI should return 

Return a structured review with findings grouped by dimension, each labeled Critical, Warning, or Info. For every finding, include the affected component, business or operational impact, why it matters, and a concrete remediation. End with a short summary of the top architectural risks and the first fixes to prioritize. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Design.
