# LLM API Integration *AI Prompt *

Design a robust LLM API integration with error handling, retries, cost control, and observability. Provider: {{provider}} (OpenAI, Anthropic, Google, Azure, self-hosted) Use cas... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a robust LLM API integration with error handling, retries, cost control, and observability.

Provider: {{provider}} (OpenAI, Anthropic, Google, Azure, self-hosted)
Use case: {{use_case}}
Expected volume: {{volume}} requests per day
Latency SLA: {{latency}}

1. Client configuration:
 - Timeout: set request timeout to {{timeout}} seconds (default is often None — always set it)
 - Max retries: 3 retries with exponential backoff (1s, 2s, 4s)
 - Retry conditions: 429 (rate limit), 500, 502, 503 (transient server errors)
 - Do NOT retry: 400 (bad request), 401 (auth error), 400 context length exceeded

2. Rate limit handling:
 - Track token usage per request (prompt tokens + completion tokens)
 - Implement a token budget per user or per tenant
 - Exponential backoff with jitter on 429: avoid thundering herd
 - Circuit breaker: if error rate > 50% for > 60 seconds, stop sending requests and alert

3. Context window management:
 - Truncate long inputs to stay within the model's context limit
 - Strategy: truncate from the middle (preserve start and end of documents)
 - Or: chunk and summarize long documents before including in the context
 - Track: prompt token count per request, alert if approaching the limit

4. Cost control:
 - Log: input tokens, output tokens, model, cost per request
 - Aggregate: daily and monthly cost by use case, user, and model
 - Alert: when daily cost > {{cost_threshold}}
 - Optimization: use cheaper models for lower-stakes tasks (GPT-4o-mini instead of GPT-4o)
 - Cache: responses for identical or near-identical requests (semantic caching with Redis + embedding similarity)

5. Observability:
 - Log every request: prompt hash (not the full prompt if sensitive), model, latency, tokens, status
 - Trace: request ID allows linking the LLM call to the originating application request
 - Dashboard: latency p50/p95/p99, error rate, cost per hour, cache hit rate

6. Multi-provider resilience:
 - Define a fallback chain: primary → secondary → tertiary provider
 - LiteLLM: unified interface to 100+ LLM providers; handles failover transparently
 - Fall back to a smaller, self-hosted model as the last resort

Return: API client configuration, retry/backoff strategy, cost tracking design, observability setup, and multi-provider fallback plan. 
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

The AI should return a structured result that covers the main requested outputs, such as Client configuration:, Timeout: set request timeout to {{timeout}} seconds (default is often None — always set it), Max retries: 3 retries with exponential backoff (1s, 2s, 4s). The final answer should stay clear, actionable, and easy to review inside a llm infrastructure workflow for llm engineer work. 

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
