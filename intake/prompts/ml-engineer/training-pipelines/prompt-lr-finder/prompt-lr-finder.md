# Learning Rate Finder *AI Prompt *

This prompt implements a learning rate range test and uses its results to configure an effective learning rate schedule, including a 1-cycle policy. It is meant to replace guesswork with a data-driven way to pick a stable and performant learning rate. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a learning rate range test (LR finder) to find the optimal learning rate for this model.

Based on the Smith (2017) cyclical learning rate paper approach:

1. LR range test implementation:
 - Start with a very small LR (1e-7) and exponentially increase to a large LR (10) over 100–200 iterations
 - Log loss at each step
 - Stop early if loss explodes (> 4× minimum loss)

2. Plot the LR finder curve:
 - x-axis: learning rate (log scale)
 - y-axis: smoothed loss (EMA smoothing factor=0.05)
 - Annotate: the point of steepest descent (best LR), the point where loss starts diverging (max LR)

3. Recommended LR selection rules:
 - For standard training: use the LR at steepest loss descent ÷ 10
 - For 1-cycle policy: use the LR at steepest descent as max_lr, and max_lr ÷ 10 as initial_lr

4. Implement 1-cycle LR scheduler using the found LR:
 - Warmup: linear increase from max_lr/10 to max_lr over 30% of training
 - Decay: cosine anneal from max_lr to max_lr/10000 over remaining 70%

5. Reset model weights after the LR finder (do not use weights from the search)

Return: LR finder code, plot code, and 1-cycle scheduler setup using the found optimal LR. 
```

## When to use this prompt 
Use case 01 
when you want to tune learning rate systematically instead of guessing 
Use case 02 
when training is unstable or converges too slowly 
Use case 03 
when you want a Smith-style LR finder and 1-cycle schedule 
Use case 04 
when you need plots and clear LR selection rules 

## What the AI should return 

LR finder code, plotting code, recommended LR selection guidance, and a 1-cycle scheduler configured from the discovered range. 

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
