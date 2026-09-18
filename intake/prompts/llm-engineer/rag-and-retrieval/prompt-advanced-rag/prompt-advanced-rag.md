# Advanced RAG Architectures *AI Prompt *

Design advanced RAG patterns to improve performance beyond naive retrieval-augmented generation. Use case: {{use_case}} Corpus characteristics: {{corpus}} (size, structure, upda... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design advanced RAG patterns to improve performance beyond naive retrieval-augmented generation.

Use case: {{use_case}}
Corpus characteristics: {{corpus}} (size, structure, update frequency, domain)
Performance gap: {{gap}} (precision, recall, multi-hop reasoning, conflicting information)

1. Corrective RAG (CRAG):
 - After retrieval: evaluate the relevance of retrieved chunks using a lightweight relevance classifier
 - If all chunks are low-relevance: fall back to web search or a broader retrieval strategy
 - Corrective step prevents the LLM from generating based on irrelevant context

2. Self-RAG:
 - The LLM generates special tokens deciding: whether to retrieve, whether the retrieved context is relevant, whether the generated sentence is supported
 - Requires training or prompting the model to produce these critique tokens
 - More reliable than always retrieving regardless of whether the query needs external knowledge

3. Multi-hop RAG (for complex reasoning):
 - Simple RAG retrieves once. Multi-hop retrieves iteratively:
 Step 1: retrieve for the original query
 Step 2: based on the first retrieval, formulate a follow-up query and retrieve again
 - Handles: questions requiring synthesizing information from multiple documents
 - IRCoT (Interleaved Retrieval with Chain-of-Thought): alternate retrieval and reasoning steps

4. Fusion RAG:
 - Generate multiple query reformulations from the original question
 - Retrieve for each reformulation independently
 - Fuse all retrieved chunks (deduplicate, rank, select top-k)
 - Better recall than single-query retrieval

5. GraphRAG:
 - Build a knowledge graph from the corpus (entities and relationships)
 - Retrieve from the graph (entity-centric) in addition to or instead of chunk-based retrieval
 - Effective for: queries about relationships between entities, entity-centric Q&A
 - Microsoft GraphRAG: open-source implementation with community detection

6. Long context vs RAG trade-off:
 - Very long context models (128K+ tokens) can sometimes ingest entire documents without retrieval
 - When to prefer long context: when the entire document is needed, retrieval precision is low
 - When to prefer RAG: corpus too large for any context window, cost of long-context inference is prohibitive, retrieval quality is high

Return: architecture recommendation for the specific use case, implementation plan for the chosen pattern, and evaluation approach to verify improvement over naive RAG. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin rag and retrieval work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in RAG and Retrieval or the wider LLM Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Corrective RAG (CRAG):, After retrieval: evaluate the relevance of retrieved chunks using a lightweight relevance classifier, If all chunks are low-relevance: fall back to web search or a broader retrieval strategy. The final answer should stay clear, actionable, and easy to review inside a rag and retrieval workflow for llm engineer work. 

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

Once you have the first result, continue deeper with related prompts in RAG and Retrieval.
