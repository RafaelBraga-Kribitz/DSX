# FastAPI Serving Endpoint *AI Prompt *

This prompt builds a production-oriented FastAPI inference service for an ML model, including request validation, startup model loading, health endpoints, error handling, latency reporting, and concurrency controls. It is intended for real serving environments rather than quick demos. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a production-ready FastAPI model serving endpoint for {{model_name}}.

1. Application structure:
 - Lifespan context manager for model loading at startup (not per-request)
 - Global model object stored in app state, not as a module-level global
 - Separate router for model endpoints

2. Request/response schemas (Pydantic v2):
 - Input schema: {{input_schema}} with field validators and example values
 - Response schema: prediction, confidence, model_version, latency_ms, request_id
 - Error response schema with error code and message

3. Inference endpoint POST /predict:
 - Input validation via Pydantic
 - Preprocessing: replicate exactly the training preprocessing pipeline
 - Inference with torch.no_grad() and model.eval()
 - Postprocessing: convert model output to human-readable format
 - Response with latency measurement

4. Health and readiness:
 - GET /health: returns 200 if service is up
 - GET /ready: returns 200 only if model is loaded and warm
 - GET /metrics: prediction count, p50/p95/p99 latency, error rate

5. Robustness:
 - Input size limits to prevent memory exhaustion
 - Timeout on inference (configurable)
 - Graceful error handling — never return a stack trace to the client

6. Concurrency:
 - For CPU models: use thread pool executor with asyncio.run_in_executor
 - For GPU models: serialize inference with asyncio.Lock or use a request queue

Return: complete FastAPI application code with Dockerfile. 
```

## When to use this prompt 
Use case 01 
when deploying an ML model behind a FastAPI REST endpoint 
Use case 02 
when you need strict request and response schemas with readiness checks 
Use case 03 
when inference preprocessing must mirror training exactly 
Use case 04 
when robustness, concurrency, and observability matter 

## What the AI should return 

Complete FastAPI application code with Pydantic schemas, model loading lifecycle, prediction endpoint, health routes, metrics, and a Dockerfile. 

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

Once you have the first result, continue deeper with related prompts in Model Deployment.
