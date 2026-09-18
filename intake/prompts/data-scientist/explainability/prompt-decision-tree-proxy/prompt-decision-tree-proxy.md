# Decision Tree Proxy *AI Prompt *

This prompt builds a shallow decision tree that approximates a complex model for interpretability. It is useful when the real model is hard to explain but stakeholders still want simplified rules of thumb. The key idea is fidelity: the tree should mimic the complex model as well as possible while staying readable. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a simple decision tree that approximates the behavior of this complex model.

1. Generate predictions from the complex model on the full training set
2. Train a decision tree on those predictions (use model outputs as the new target)
3. Limit the tree depth to 4 levels maximum for interpretability
4. Tune: find the depth (1–6) that maximizes fidelity (agreement with the complex model) while staying interpretable
5. Visualize the decision tree using graphviz or a text representation
6. Extract the top 5 decision rules as plain-English if-then statements
7. Report fidelity: what percentage of predictions does the proxy tree agree with the complex model?

Note: this is a surrogate model, not the real model. Flag where the proxy disagrees most with the original. 
```

## When to use this prompt 
Use case 01 
The production model is too complex for direct explanation. 
Use case 02 
Stakeholders want simple if-then rules approximating model behavior. 
Use case 03 
You need a surrogate explanation with measurable fidelity. 
Use case 04 
You want to know where the simplified proxy breaks down. 

## What the AI should return 

A tuned shallow surrogate tree, fidelity score, key extracted rules in plain English, visualization or text representation of the tree, and notes on where the proxy disagrees with the original model. 

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

Once you have the first result, continue deeper with related prompts in Explainability.
