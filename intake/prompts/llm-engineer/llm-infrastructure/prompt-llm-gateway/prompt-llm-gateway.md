# LLM Gateway Design *AI Prompt *

Design an LLM gateway layer that centralizes model access, controls, and observability for an organization. Organization: {{org_size}} engineers using LLMs Providers in use: {{p... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an LLM gateway layer that centralizes model access, controls, and observability for an organization.

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

Return: gateway architecture, policy engine design, logging specification, open-source vs commercial recommendation, and compliance controls. 
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

The AI should return a structured result that covers the main requested outputs, such as What an LLM gateway provides:, Single access point: all LLM calls from all teams go through the gateway, Authentication and authorization: teams have API keys; keys map to budgets and allowed models. The final answer should stay clear, actionable, and easy to review inside a llm infrastructure workflow for llm engineer work. 

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
