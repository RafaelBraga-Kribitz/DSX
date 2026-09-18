# Retrieval Quality Improvement *AI Prompt *

Diagnose and improve retrieval quality in a RAG system. Current retrieval setup: {{retrieval_setup}} Failure modes observed: {{failure_modes}} Corpus type: {{corpus_type}} 1. Re... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Diagnose and improve retrieval quality in a RAG system.

Current retrieval setup: {{retrieval_setup}}
Failure modes observed: {{failure_modes}}
Corpus type: {{corpus_type}}

1. Retrieval failure diagnosis:

 Low recall (the right chunk is not retrieved):
 - Vocabulary mismatch: the query uses different words than the document
 - Chunk too large: relevant sentence is diluted in a large chunk
 - Embedding model weakness: try a higher-quality embedding model
 - Insufficient k: increase top-k and use re-ranking to filter

 Low precision (wrong chunks retrieved):
 - Chunks are too similar to each other (duplicate information)
 - Embedding model does not discriminate well for this domain
 - Query is ambiguous: use query expansion or clarification

2. Hybrid search:
 - Combine dense (vector) retrieval with sparse (BM25/TF-IDF) retrieval
 - Dense: captures semantic similarity (same meaning, different words)
 - Sparse: captures exact keyword match (critical for proper nouns, technical terms, codes)
 - Reciprocal Rank Fusion (RRF): combine rankings from both retrieval methods
 - Hybrid consistently outperforms either method alone for most real-world corpora

3. Re-ranking with a cross-encoder:
 - First-stage retrieval: top-k=50 chunks (optimized for recall, not precision)
 - Cross-encoder re-ranking: score all 50 (query, chunk) pairs jointly, re-rank
 - Return top-5 after re-ranking (much higher precision)
 - Cross-encoder models: Cohere rerank-english-v3, BGE-reranker-large (open-source)
 - Cross-encoders are too slow for first-stage retrieval (O(k) inference vs O(1) for bi-encoders)

4. Query transformation:
 - HyDE (Hypothetical Document Embeddings): generate a hypothetical answer to the query, embed it, and use it to retrieve documents (often outperforms direct query embedding)
 - Step-back prompting: ask a more general question before the specific one
 - Query expansion: generate 3-5 query variants, retrieve for each, deduplicate results
 - Multi-query: decompose compound questions into sub-questions, retrieve for each

5. Metadata filtering:
 - Add structured metadata to each chunk: source, date, section, author, product, language
 - Filter before retrieval: only search within the relevant date range, product, or section
 - Dramatically improves precision when the user's query has clear scope constraints

Return: failure diagnosis, hybrid search configuration, re-ranking setup, query transformation recommendation, and metadata filtering strategy. 
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

The AI should return a structured result that covers the main requested outputs, such as Retrieval failure diagnosis:, Vocabulary mismatch: the query uses different words than the document, Chunk too large: relevant sentence is diluted in a large chunk. The final answer should stay clear, actionable, and easy to review inside a rag and retrieval workflow for llm engineer work. 

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
