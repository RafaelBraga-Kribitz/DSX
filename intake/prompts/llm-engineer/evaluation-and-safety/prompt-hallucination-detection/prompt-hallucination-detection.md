# LLM Hallucination Detection *AI Prompt *

Design a hallucination detection and mitigation strategy for this LLM application. Application type: {{app_type}} (RAG Q&A, text generation, summarization, data extraction) Mode... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a hallucination detection and mitigation strategy for this LLM application.

Application type: {{app_type}} (RAG Q&A, text generation, summarization, data extraction)
Model: {{model}}
Risk level: {{risk_level}} (low, medium, high, safety-critical)

1. Types of LLM hallucination:
 - Factual hallucination: generating plausible but false facts (invented statistics, incorrect dates, wrong attributions)
 - Faithfulness hallucination: in RAG, generating claims not supported by the retrieved context
 - Instruction hallucination: failing to follow the specified format or constraints
 - Entity hallucination: generating realistic-sounding but non-existent names, citations, URLs

2. Detection methods:

 Self-consistency check:
 - Ask the same question multiple times (temperature > 0)
 - If answers are inconsistent across samples: likely hallucination
 - High consistency does NOT guarantee correctness (the model can be consistently wrong)

 Entailment-based detection:
 - Use an NLI (Natural Language Inference) model to check: does the source context entail the generated claim?
 - For each sentence in the response: classify as entailed, neutral, or contradicted by the context
 - Flag sentences classified as 'neutral' or 'contradicted'
 - Tools: TRUE metric, MiniCheck, AlignScore

 LLM self-evaluation:
 'Review the following response and identify any claims that are not supported by the provided context. For each unsupported claim, flag it as [UNSUPPORTED].

 Context: {{context}}
 Response: {{response}}'

 External fact-checking:
 - For factual claims: retrieve supporting evidence from a trusted source
 - Check: does the evidence confirm or contradict the claim?

3. Mitigation strategies:

 System-level:
 - RAG with source citations: ground all responses in retrieved documents
 - Retrieval confidence: if no relevant document is found, respond with 'I don't have information about this'
 - Response grounding instruction: 'Only state facts present in the provided context. If you are uncertain, say so.'

 Post-generation:
 - Hedging injection: automatically add 'According to the provided sources' where claims are made
 - Source attribution: cite the specific document for each claim in the response
 - Human review trigger: route low-confidence or high-stakes responses to human review

4. Calibration and confidence:
 - Ask the model to express its confidence: 'How confident are you in this answer? (High/Medium/Low)'
 - LLMs are poorly calibrated: high expressed confidence does not reliably predict accuracy
 - For safety-critical applications: require external verification regardless of expressed confidence

Return: hallucination typology, detection method selection, mitigation strategy, and human review routing policy. 
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

The AI should return a structured result that covers the main requested outputs, such as Types of LLM hallucination:, Factual hallucination: generating plausible but false facts (invented statistics, incorrect dates, wrong attributions), Faithfulness hallucination: in RAG, generating claims not supported by the retrieved context. The final answer should stay clear, actionable, and easy to review inside a evaluation and safety workflow for llm engineer work. 

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
