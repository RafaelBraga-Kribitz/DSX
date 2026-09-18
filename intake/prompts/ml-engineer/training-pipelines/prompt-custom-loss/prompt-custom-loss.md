# Custom Loss Function *AI Prompt *

This prompt builds a custom PyTorch loss function that is differentiable, numerically stable, and testable. It includes unit tests, gradient checks, reduction modes, and edge-case handling so the loss can be trusted in real training workloads. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a custom loss function for this problem with full PyTorch autograd compatibility.

Problem: {{problem_description}}
Loss requirements: {{loss_requirements}}

1. Implementation requirements:
 - Subclass torch.nn.Module or implement as a function
 - Fully differentiable — use only PyTorch tensor operations, no NumPy inside forward()
 - Support batched inputs of arbitrary batch size
 - Handle edge cases: empty batches, all-same-class batches, NaN/Inf inputs

2. For composite losses (combining multiple terms):
 - Implement each term as a separate method for testability
 - Use learnable or fixed weighting between terms
 - Log each term's contribution separately during training

3. Numerical stability:
 - Use log-sum-exp trick for log probabilities
 - Apply clipping to prevent log(0) or division by zero
 - Test with fp16 — ensure no overflow with half precision

4. Testing the loss:
 - Unit test: verify loss = 0 for perfect predictions
 - Unit test: verify loss > 0 for wrong predictions
 - Gradient check: torch.autograd.gradcheck to verify analytical gradients match numerical approximation
 - Verify loss is lower for better predictions (sanity check)

5. Reduction modes: support 'mean', 'sum', and 'none' as in standard PyTorch losses

Return: loss implementation, unit tests, gradient check, and integration example in a training loop. 
```

## When to use this prompt 
Use case 01 
when a standard loss does not fit the problem requirements 
Use case 02 
when implementing composite or problem-specific objectives in PyTorch 
Use case 03 
when autograd compatibility and numerical stability are critical 
Use case 04 
when you need tests and gradcheck before using a custom loss in production 

## What the AI should return 

Custom loss implementation, supporting tests, gradient checks, reduction mode support, and an example of integration into training. 

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

Once you have the first result, continue deeper with related prompts in Training Pipelines.
