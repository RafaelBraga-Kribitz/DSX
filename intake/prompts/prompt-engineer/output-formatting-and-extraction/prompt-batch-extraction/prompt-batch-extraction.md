# Batch Extraction at Scale *AI Prompt *

Design a prompt and system for efficiently extracting structured data from thousands of documents using LLMs at scale. Target: extract {{schema}} from {{num_documents}} document... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a prompt and system for efficiently extracting structured data from thousands of documents using LLMs at scale.

Target: extract {{schema}} from {{num_documents}} documents at a cost of < {{target_cost_per_doc}} per document.

1. Prompt efficiency for batch workloads:

 a. Minimize token count:
 - System prompt: put stable instructions (schema, rules) in the system prompt — reused across calls without re-tokenizing
 - User prompt: only the document text and a minimal task reminder
 - Omit examples from the user prompt (they are in the system prompt)
 - Compress the schema: use a compact field list instead of verbose JSON Schema

 b. Multi-document batching:
 - Process multiple short documents in a single API call by separating them with delimiters
 - 'Below are N documents separated by ---DOCUMENT_BREAK---. Extract the schema from each and return a JSON array with one object per document in the same order.'
 - Optimal batch size: experiment with 3–10 documents per call; larger batches reduce API overhead but increase error blast radius

 c. Document chunking for long documents:
 - If a document exceeds the context window: split into overlapping chunks
 - Extract from each chunk independently
 - Merge: for each field, take the value from whichever chunk had the clearest signal

2. Quality vs cost tradeoffs:
 - Tier 1 (high importance documents): full prompt + self-critique + validation = highest quality, highest cost
 - Tier 2 (standard documents): full prompt + schema validation = balanced
 - Tier 3 (bulk/archival): compact prompt + spot-check validation = lowest cost

3. Error handling at scale:
 - Track parse failure rate per batch
 - If failure rate > 5%: halt and investigate prompt or input quality
 - Retry failures with a longer, more explicit prompt before flagging for human review
 - Log every failure with the input document and error for post-hoc analysis

4. Cost monitoring:
 - Track tokens in and out per document type
 - Alert if cost per document exceeds budget
 - Identify document types that are disproportionately expensive (too long, too complex)

Return: system prompt for batch extraction, batching implementation, chunking strategy, tier routing logic, and cost monitoring dashboard spec. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin output formatting and extraction work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Output Formatting and Extraction or the wider Prompt Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Prompt efficiency for batch workloads:, System prompt: put stable instructions (schema, rules) in the system prompt — reused across calls without re-tokenizing, User prompt: only the document text and a minimal task reminder. The final answer should stay clear, actionable, and easy to review inside a output formatting and extraction workflow for prompt engineer work. 

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

Once you have the first result, continue deeper with related prompts in Output Formatting and Extraction.
