# RAG Evaluation Framework *AI Prompt *

Build a systematic evaluation framework for a RAG system. RAG system: {{system_description}} Document corpus: {{corpus}} Query set: {{query_set}} 1. The RAG evaluation triad: A... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a systematic evaluation framework for a RAG system.

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

Return: evaluation framework, metric definitions and targets, RAGAS configuration, golden test set construction, and regression protocol. 
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

The AI should return a structured result that covers the main requested outputs, such as The RAG evaluation triad:, Retrieval quality: are the right chunks being retrieved?, Generation quality: is the LLM producing accurate, faithful responses?. The final answer should stay clear, actionable, and easy to review inside a rag and retrieval workflow for llm engineer work. 

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
