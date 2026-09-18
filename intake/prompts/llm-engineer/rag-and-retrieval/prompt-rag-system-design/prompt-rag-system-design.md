# RAG System Design *AI Prompt *

Design a production-grade Retrieval-Augmented Generation (RAG) system for this use case. Use case: {{use_case}} Document corpus: {{corpus_description}} (size, document types, up... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a production-grade Retrieval-Augmented Generation (RAG) system for this use case.

Use case: {{use_case}}
Document corpus: {{corpus_description}} (size, document types, update frequency)
Query type: {{query_type}} (factual Q&A, summarization, comparison, synthesis)
Latency requirement: {{latency}} ms end-to-end

1. RAG pipeline stages:

 Indexing (offline):
 - Document loading: PDF, HTML, Markdown, Word — use appropriate parsers (pypdf, markdownify, etc.)
 - Chunking: split documents into chunks for embedding (see chunking strategies below)
 - Embedding: convert chunks to dense vectors using an embedding model
 - Vector storage: store vectors in a vector database with metadata

 Retrieval (online, per query):
 - Embed the user query using the same embedding model
 - Retrieve top-k most similar chunks by cosine similarity
 - Optional: re-rank retrieved chunks using a cross-encoder
 - Construct the context window from the top chunks

 Generation:
 - Construct the augmented prompt: system instruction + retrieved context + user query
 - Generate the response using the LLM
 - Optionally: cite sources in the response

2. Chunking strategies:

 Fixed-size with overlap:
 - chunk_size = 512 tokens, overlap = 50-100 tokens
 - Simple, predictable chunk size
 - Overlap prevents information loss at chunk boundaries

 Semantic chunking:
 - Split at natural boundaries: paragraphs, sections, sentences
 - Produces more coherent chunks but variable size
 - Better for: structured documents with clear sections

 Hierarchical chunking:
 - Store both document-level and chunk-level embeddings
 - Retrieve document-level first, then chunk-level within the selected document
 - Better for: navigating long documents

3. Embedding model selection:
 - OpenAI text-embedding-3-large: strong performance, hosted, $
 - Cohere embed-v3: strong multilingual, reranking support
 - BGE-M3 / E5-large: strong open-source options for self-hosting
 - For code: use code-specific embedding models
 - MTEB benchmark: the standard leaderboard for retrieval embedding models

4. Vector database selection:
 - Pinecone: fully managed, production-ready, easy setup
 - Weaviate: open-source + managed, supports hybrid search
 - Qdrant: open-source, high performance, rich filter support
 - pgvector: Postgres extension, simple stack if you already use Postgres
 - Chroma: easiest to start with for prototyping

5. RAG prompt template:
 'Answer the user's question using only the information provided in the context below. If the answer is not found in the context, say "I don't have enough information to answer this question."

 Context:
 {{retrieved_chunks}}

 Question: {{user_question}}
 Answer:'

Return: pipeline architecture, chunking strategy recommendation, embedding model selection, vector DB choice, and RAG prompt template. 
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

The AI should return a structured result that covers the main requested outputs, such as RAG pipeline stages:, Document loading: PDF, HTML, Markdown, Word — use appropriate parsers (pypdf, markdownify, etc.), Chunking: split documents into chunks for embedding (see chunking strategies below). The final answer should stay clear, actionable, and easy to review inside a rag and retrieval workflow for llm engineer work. 

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
