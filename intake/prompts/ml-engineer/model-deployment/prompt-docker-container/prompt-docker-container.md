# Docker Container for ML *AI Prompt *

This prompt produces an optimized Docker packaging setup for a model serving application, including a multi-stage Dockerfile, .dockerignore, and docker-compose example. It emphasizes secure and minimal runtime images, pinned dependencies, health checks, and configurable runtime behavior. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write an optimized Dockerfile for deploying this ML model serving application.

Requirements:
- Base image: appropriate CUDA + Python base for GPU, or slim Python for CPU
- Framework: {{framework}} (PyTorch / TensorFlow / ONNX Runtime)

1. Multi-stage build:
 - Builder stage: install build dependencies, compile any C extensions
 - Runtime stage: copy only what is needed for serving (no build tools, no test files)

2. Dependency installation:
 - Copy requirements.txt first, install dependencies before copying code (layer caching)
 - Pin all dependency versions
 - Use --no-cache-dir to reduce image size
 - Install only inference dependencies, not training ones

3. Security best practices:
 - Run as non-root user (create appuser)
 - Read-only filesystem where possible
 - No secrets in the image — use environment variables or mounted secrets

4. Model artifact handling:
 - Bake model weights into image for simplicity (smaller models <500MB)
 - OR load from object storage at startup using environment variable for path

5. Health check:
 - HEALTHCHECK instruction hitting the /health endpoint

6. Image size optimization:
 - Remove pip cache, apt cache, and __pycache__ directories
 - Use .dockerignore to exclude notebooks, tests, data, and .git

7. Runtime configuration:
 - ENV variables for: model path, port, log level, num workers
 - ENTRYPOINT with CMD for override flexibility

Return: Dockerfile, .dockerignore, and docker-compose.yml for local testing. 
```

## When to use this prompt 
Use case 01 
when containerizing an ML inference service for local or production deployment 
Use case 02 
when image size, security, and dependency hygiene matter 
Use case 03 
when you need separate builder and runtime stages 
Use case 04 
when local testing should be supported with docker-compose 

## What the AI should return 

An optimized Dockerfile, matching .dockerignore, and docker-compose.yml for local serving and health-check-based testing. 

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
