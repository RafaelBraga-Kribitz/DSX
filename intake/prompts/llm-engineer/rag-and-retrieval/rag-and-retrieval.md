# RAG and Retrieval *AI Prompts *

4 LLM Engineer prompts in RAG and Retrieval. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts. 

## AI prompts in RAG and Retrieval 
4 prompts Advanced Single prompt 01 
### Advanced RAG Architectures 

Design advanced RAG patterns to improve performance beyond naive retrieval-augmented generation. Use case: {{use_case}} Corpus characteristics: {{corpus}} (size, structure, upda... 
Prompt text Design advanced RAG patterns to improve performance beyond naive retrieval-augmented generation.

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

Return: architecture recommendation for the specific use case, implementation plan for the chosen pattern, and evaluation approach to verify improvement over naive RAG. Copy prompt Open prompt details Advanced Single prompt 02 
### RAG Evaluation Framework 

Build a systematic evaluation framework for a RAG system. RAG system: {{system_description}} Document corpus: {{corpus}} Query set: {{query_set}} 1. The RAG evaluation triad: A... 
Prompt text Build a systematic evaluation framework for a RAG system.

RAG system: {{system_description}}
Document corpus: {{corpus}}
Query set: {{query_set}}

1. The RAG evaluation triad:
 A RAG system has three components to evaluate:
 - Retrieval quality: are the right chunks being retrieved?
 - Generation quality: is the LLM producing accurate, faithful responses?
 - End-to-end quality: does the final answer satisfy the user's information need?

2. Retrieval metrics:

 Context precision:
 - Of the chunks retrieved, what fraction are actually relevant to the query?
 - Measure: human label or LLM judge (is this chunk relevant to the query?)
 - Target: > 80%

 Context recall:
 - Of all relevant chunks in the corpus, what fraction were retrieved?
 - Requires: knowing which chunks are relevant (golden dataset or LLM judge)
 - Target: > 70%

 MRR (Mean Reciprocal Rank):
 - How highly ranked is the first relevant chunk?
 - MRR = mean(1/rank_of_first_relevant_chunk)

3. Generation metrics:

 Faithfulness:
 - Does every claim in the response actually appear in the retrieved context?
 - LLM judge: 'For each claim in the answer, verify it is supported by the context. Return a faithfulness score between 0 and 1.'
 - Target: > 0.9 (low faithfulness = hallucination from the LLM beyond the context)

 Answer relevance:
 - Does the response actually answer the question asked?
 - LLM judge: 'Does this response directly answer the question? Score 1-5.'

4. End-to-end evaluation:

 RAGAS framework (open-source):
 - Automated RAG evaluation combining context precision, context recall, faithfulness, and answer relevance
 - Uses an LLM judge internally
 - from ragas import evaluate

 Human evaluation:
 - 50-100 questions with golden answers
 - Blind evaluation: raters score responses without seeing the retrieval
 - A/B test: compare RAG system vs baseline (no retrieval)

5. Regression testing:
 - Maintain a golden test set of 100+ queries with expected answers
 - Run after every change (chunking, embedding model, prompt)
 - Accept changes only if no metric drops by > 5%

Return: evaluation framework, metric definitions and targets, RAGAS configuration, golden test set construction, and regression protocol. Copy prompt Open prompt details Intermediate Single prompt 03 
### RAG System Design 

Design a production-grade Retrieval-Augmented Generation (RAG) system for this use case. Use case: {{use_case}} Document corpus: {{corpus_description}} (size, document types, up... 
Prompt text Design a production-grade Retrieval-Augmented Generation (RAG) system for this use case.

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

Return: pipeline architecture, chunking strategy recommendation, embedding model selection, vector DB choice, and RAG prompt template. Copy prompt Open prompt details Intermediate Single prompt 04 
### Retrieval Quality Improvement 

Diagnose and improve retrieval quality in a RAG system. Current retrieval setup: {{retrieval_setup}} Failure modes observed: {{failure_modes}} Corpus type: {{corpus_type}} 1. Re... 
Prompt text Diagnose and improve retrieval quality in a RAG system.

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

Return: failure diagnosis, hybrid search configuration, re-ranking setup, query transformation recommendation, and metadata filtering strategy. Copy prompt Open prompt details 
## Recommended RAG and Retrieval workflow 
1 
### Advanced RAG Architectures 

Start with a focused prompt in RAG and Retrieval so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### RAG Evaluation Framework 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### RAG System Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Retrieval Quality Improvement 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
