# Lambda vs Kappa Architecture *AI Prompt *

This prompt compares Lambda and Kappa architectures for use cases that combine historical processing with low-latency needs. It helps teams avoid choosing an architecture based on buzzwords rather than processing logic, replay needs, and operational complexity. The answer should clearly apply the trade-offs to the specific use case. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Evaluate whether this use case calls for a Lambda architecture or a Kappa architecture.

Use case: {{use_case_description}}
Latency requirements: {{latency}}
Historical reprocessing need: {{reprocessing_need}}
Team size and complexity tolerance: {{team_constraints}}

1. Lambda architecture:
 - Two separate pipelines: batch (accurate, slow) and speed (fast, approximate)
 - Serving layer merges batch and speed views
 - Pros: handles historical reprocessing naturally, speed layer can be simpler
 - Cons: two codebases for the same logic (duplication and drift risk), higher operational complexity
 - When to choose: if batch and streaming have genuinely different business logic, or if batch accuracy is non-negotiable and streaming is additive

2. Kappa architecture:
 - Single streaming pipeline for everything
 - Reprocessing = replay from beginning of the message log with a new consumer group
 - Pros: single codebase, simpler operations, no view merging
 - Cons: requires a long-retention message log, streaming system must handle batch-scale replay, stateful processing is more complex
 - When to choose: when batch and streaming logic are identical, team wants to minimize operational surface area

3. Decision framework:
 - Is the processing logic identical for batch and streaming? → Kappa
 - Do you need to reprocess years of history frequently? → Check if Kappa replay is cost-effective
 - Is your team small? → Kappa (less to maintain)
 - Do you have complex, different historical vs real-time logic? → Lambda
 - Is latency requirement < 1 minute AND accuracy is critical? → Lambda with micro-batch

4. Recommended architecture for this use case:
 - State the recommendation clearly with rationale
 - Identify the top 2 risks of the chosen approach and mitigations

Return: architecture comparison, decision framework applied to this use case, recommendation, and risk register. 
```

## When to use this prompt 
Use case 01 
When evaluating architecture options for mixed batch and streaming workloads. 
Use case 02 
When deciding whether one code path can serve both real-time and replay scenarios. 
Use case 03 
When your team is small and operational complexity matters. 
Use case 04 
When preparing an architecture recommendation with risks and trade-offs. 

## What the AI should return 

Return a side-by-side comparison of Lambda and Kappa for the stated use case, then make a clear recommendation. Include the decision criteria applied, key assumptions, and the top risks of the chosen approach with mitigations. The result should help a team defend the architecture choice in review discussions. 

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
