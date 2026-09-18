# LLM Infrastructure *AI Prompts *

5 LLM Engineer prompts in LLM Infrastructure. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts · 1 chain. 

## AI prompts in LLM Infrastructure 
5 prompts Advanced Single prompt 01 
### Agentic System Design 

Design a reliable LLM agent system that uses tools to complete multi-step tasks. Agent task: {{task}} Available tools: {{tools}} (web search, code execution, database query, API... 
Prompt text Design a reliable LLM agent system that uses tools to complete multi-step tasks.

Agent task: {{task}}
Available tools: {{tools}} (web search, code execution, database query, API calls, file operations)
Reliability requirement: {{reliability}} (best-effort or guaranteed completion)
Human-in-the-loop: {{hitl}} (yes/no — is human approval required for certain actions?)

1. Agent architecture:

 ReAct loop (Reasoning + Acting):
 - Thought: the agent reasons about what to do next
 - Action: the agent selects and calls a tool
 - Observation: the agent receives the tool result
 - Repeat until the agent decides the task is complete

 Plan-and-execute (more reliable for complex tasks):
 - Planning step: decompose the task into a sequence of sub-tasks
 - Execution: execute each sub-task sequentially (or in parallel where possible)
 - Re-planning: if a step fails, re-plan from the current state

2. Tool design:
 - Each tool has: name, description (the agent reads this to decide when to use it), input schema, output schema
 - Tools must be: idempotent where possible (safe to retry), fast (< 5s for most tools), well-scoped (do one thing well)
 - Tool description quality is critical: the agent's tool selection depends entirely on the description
 - Validation: validate tool outputs before passing to the next step

3. Error handling and retries:
 - Transient failures: retry the tool call up to 3 times with backoff
 - Persistent failures: skip the step and log; reroute to a fallback tool if available
 - Maximum iterations: set a hard limit (e.g., 20 steps) to prevent infinite loops
 - Checkpoint saving: save the agent's state after each completed step; resume from the last checkpoint on failure

4. Safety for agentic systems:
 - Minimal footprint: request only the permissions needed for the current task
 - Human approval gates: require human confirmation before irreversible actions (sending emails, deleting data, making payments)
 - Sandboxed execution: run code in an isolated container (e.g., E2B sandbox)
 - Audit log: log every action the agent takes, every tool it calls, and every decision it makes

5. Frameworks:
 - LangGraph: production-grade graph-based agent framework with state management
 - LlamaIndex Agents: strong for RAG-augmented agents
 - AutoGen (Microsoft): multi-agent conversation framework
 - Pydantic AI: type-safe agent framework with validation
 - Anthropic's computer use: for agents that interact with GUIs

Return: agent architecture selection, tool specification schema, error handling strategy, safety controls, and framework recommendation. Copy prompt Open prompt details Advanced Chain 02 
### Full LLM Application Chain 

Step 1: Requirements and architecture decision - define the task, output format, latency SLA, cost budget, and safety requirements. Decide: prompting only vs RAG vs fine-tuning... 
Prompt text Step 1: Requirements and architecture decision - define the task, output format, latency SLA, cost budget, and safety requirements. Decide: prompting only vs RAG vs fine-tuning vs agent. Document the decision rationale.
Step 2: Prompt design - write the system prompt and user prompt template. Specify the output schema (JSON or structured text). Add grounding and anti-hallucination instructions. Create 20 test cases including 5 adversarial examples.
Step 3: Retrieval design (if RAG) - design the chunking strategy, embedding model selection, and vector database. Configure hybrid search with a cross-encoder re-ranker. Define the retrieval evaluation metrics (precision, recall, faithfulness).
Step 4: Evaluation framework - build the golden test set (100+ examples with verified answers). Define metrics: task accuracy, faithfulness, instruction following, safety. Run the LLM judge pipeline. Establish regression baselines.
Step 5: Safety and guardrails - design input classification (prompt injection, harmful content). Design output validation (PII, content safety, format compliance). Define the human review routing policy for high-risk cases.
Step 6: Infrastructure - design the API integration with retry logic, cost tracking, and caching. Configure the LLM gateway. Set up latency, cost, and error rate monitoring. Define alerting thresholds.
Step 7: Deployment and monitoring - deploy with shadow mode first. Run A/B test vs baseline. Configure production monitoring: latency, cost, guardrail trigger rate, hallucination rate. Define the retraining or re-prompting trigger criteria. Copy prompt Open prompt details Intermediate Single prompt 03 
### LLM API Integration 

Design a robust LLM API integration with error handling, retries, cost control, and observability. Provider: {{provider}} (OpenAI, Anthropic, Google, Azure, self-hosted) Use cas... 
Prompt text Design a robust LLM API integration with error handling, retries, cost control, and observability.

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

Return: API client configuration, retry/backoff strategy, cost tracking design, observability setup, and multi-provider fallback plan. Copy prompt Open prompt details Intermediate Single prompt 04 
### LLM Caching Strategy 

Design a caching strategy to reduce LLM API costs and improve response latency. Use case: {{use_case}} Query volume: {{volume}} per day Expected cache hit rate target: {{target_... 
Prompt text Design a caching strategy to reduce LLM API costs and improve response latency.

Use case: {{use_case}}
Query volume: {{volume}} per day
Expected cache hit rate target: {{target_hit_rate}}
Latency SLA: {{latency}}

1. Exact match caching:
 - Store: hash(prompt) → response
 - Cache backend: Redis with TTL
 - Effective when: many users ask the same question (FAQ bot, search queries)
 - Limitation: does not handle paraphrases or minor wording variations

2. Semantic caching:
 - Embed incoming prompts; retrieve cached responses if cosine similarity > threshold (e.g., 0.95)
 - Store: embedding + response in a vector database (Redis with vector support, Qdrant, pgvector)
 - Handles: paraphrases, minor rewording
 - Trade-off: similarity threshold controls cache hit rate vs risk of returning a wrong cached response
 - A threshold of 0.97 is safe; 0.93-0.95 increases hit rate but risks mismatches
 - GPTCache: open-source library for semantic caching built specifically for LLMs

3. KV (key-value) cache for prompt prefixes:
 - If many requests share a long system prompt prefix: the LLM's KV cache is reused for the prefix
 - Anthropic prompt caching: explicitly mark a static prefix for caching; 90% cost reduction on cached tokens
 - OpenAI prompt caching: automatic for prompts > 1024 tokens with stable prefix content

4. Response TTL strategy:
 - Static content (product FAQs, documentation): TTL = 24 hours
 - Semi-dynamic (news summarization): TTL = 1 hour
 - Dynamic (personalized or real-time): TTL = 0 (do not cache)
 - On data update: invalidate affected cached responses

5. Cache key design:
 - Include in the key: model, version, temperature (cached responses are only valid for the same generation settings)
 - Exclude from the key: request ID, timestamp, user ID (unless personalization is part of the response)

6. Monitoring:
 - Cache hit rate: target > {{target_hit_rate}}
 - Cost savings: estimated $/day saved from caching
 - Staleness incidents: responses served from cache after content changed

Return: exact match and semantic caching design, KV cache utilization, TTL strategy, cache key design, and monitoring metrics. Copy prompt Open prompt details Advanced Single prompt 05 
### LLM Gateway Design 

Design an LLM gateway layer that centralizes model access, controls, and observability for an organization. Organization: {{org_size}} engineers using LLMs Providers in use: {{p... 
Prompt text Design an LLM gateway layer that centralizes model access, controls, and observability for an organization.

Organization: {{org_size}} engineers using LLMs
Providers in use: {{providers}}
Compliance requirements: {{compliance}}
Goals: {{goals}} (cost control, observability, safety, multi-model routing)

1. What an LLM gateway provides:
 - Single access point: all LLM calls from all teams go through the gateway
 - Authentication and authorization: teams have API keys; keys map to budgets and allowed models
 - Rate limiting: per-team, per-user, and per-model limits
 - Logging: centralized log of all requests and responses
 - Routing: send requests to the cheapest capable model; fall back on provider outage
 - Cost allocation: track spend by team, project, and use case

2. Gateway architecture:

 Reverse proxy layer:
 - Accepts LLM API requests (OpenAI-compatible interface)
 - Injects authentication headers to the upstream provider
 - Returns the provider response, adding gateway metadata headers

 Policy engine:
 - Per-request policy: allowed models, max tokens, required safety filters
 - Per-tenant policy: monthly budget cap, rate limit, allowed providers
 - Dynamic routing rules: route based on latency, cost, or model capability

 Logging and analytics:
 - Log: timestamp, tenant ID, user ID, model, input token count, output token count, latency, cost
 - Do NOT log: raw prompt or response if they may contain PII (log hashes only in sensitive contexts)
 - Analytics: daily cost dashboard per team, latency trends, error rates

3. Open-source and commercial options:
 - LiteLLM Proxy: open-source, OpenAI-compatible, supports 100+ providers, includes rate limiting and logging
 - PortKey: commercial gateway with advanced analytics
 - Kong AI Gateway: enterprise-grade API gateway with LLM plugins
 - Azure API Management: enterprise gateway if already on Azure
 - AWS Bedrock API Gateway: for AWS-native deployments

4. PII and compliance:
 - Data residency: route requests to providers in the correct geographic region
 - PII scrubbing: scan and redact PII before logging (not before sending to the model unless required)
 - GDPR / HIPAA: document which providers are used, their DPA status, and data retention policies

5. Reliability:
 - Provider health checks: detect provider outages before they affect users
 - Automatic failover: route to secondary provider if primary is unavailable
 - SLA: gateway adds < 5ms overhead to every request

Return: gateway architecture, policy engine design, logging specification, open-source vs commercial recommendation, and compliance controls. Copy prompt Open prompt details 
## Recommended LLM Infrastructure workflow 
1 
### Agentic System Design 

Start with a focused prompt in LLM Infrastructure so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Full LLM Application Chain 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### LLM API Integration 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### LLM Caching Strategy 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
