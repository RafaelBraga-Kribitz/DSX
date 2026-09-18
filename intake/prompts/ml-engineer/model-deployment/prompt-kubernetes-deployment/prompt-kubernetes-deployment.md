# Kubernetes Deployment *AI Prompt *

This prompt writes Kubernetes manifests for running an ML serving service at production scale, including Deployment, HPA, Service, Ingress, ConfigMap, and PodDisruptionBudget. It focuses on safe rollout behavior, readiness, autoscaling, and operational resilience. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write Kubernetes manifests for deploying this ML model serving application at production scale.

1. Deployment manifest:
 - Replicas: {{min_replicas}} initial
 - Resource requests and limits:
 - CPU: request={{cpu_request}}, limit={{cpu_limit}}
 - Memory: request={{memory_request}}, limit={{memory_limit}}
 - GPU: nvidia.com/gpu: 1 (if GPU-based)
 - Rolling update strategy: maxUnavailable=0, maxSurge=1 (zero-downtime deploys)
 - Liveness probe: GET /health every 10s, failure threshold 3
 - Readiness probe: GET /ready every 5s (only route traffic when model is loaded)
 - Startup probe: GET /ready with longer timeout for slow model loading

2. Horizontal Pod Autoscaler (HPA):
 - Scale based on: CPU utilization target {{cpu_target}}% or custom metric (requests per second)
 - Min replicas: {{min_replicas}}, max replicas: {{max_replicas}}
 - Scale-down stabilization: 5 minutes to prevent thrashing

3. Service and Ingress:
 - ClusterIP Service for internal traffic
 - Ingress with TLS termination, rate limiting, and timeout settings

4. ConfigMap and Secret management:
 - Non-sensitive config in ConfigMap (model path, log level, batch size)
 - Sensitive config in Secrets (API keys, database credentials)
 - Mount secrets as environment variables, not files

5. Pod disruption budget:
 - minAvailable: {{min_available}} to prevent all pods being evicted simultaneously

6. Namespace and RBAC:
 - Dedicated namespace for ML serving
 - ServiceAccount with minimal permissions

Return: Deployment, HPA, Service, Ingress, ConfigMap, and PodDisruptionBudget manifests. 
```

## When to use this prompt 
Use case 01 
when deploying model serving workloads to Kubernetes 
Use case 02 
when readiness, liveness, and startup behavior must be explicitly managed 
Use case 03 
when autoscaling and zero-downtime rolling updates are required 
Use case 04 
when configuration and disruption controls should be separated cleanly 

## What the AI should return 

Production-oriented Kubernetes manifests for deployment, scaling, traffic exposure, configuration, and disruption management. 

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
