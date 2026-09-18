# Bayesian vs Frequentist Analysis *AI Prompt *

Help me decide between a frequentist and Bayesian analysis approach for my study, and implement the chosen approach. Study context: {{study_context}} Prior knowledge available:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Help me decide between a frequentist and Bayesian analysis approach for my study, and implement the chosen approach.

Study context: {{study_context}}
Prior knowledge available: {{prior_knowledge}}
Inference goal: {{inference_goal}}

1. Key conceptual differences:

 Frequentist:
 - Probability = long-run frequency of events in repeated experiments
 - Parameters are fixed (unknown) constants; data are random
 - Inference: p-value (probability of data at least as extreme as observed, given H0 is true)
 - Output: point estimate, confidence interval (if experiment repeated 100 times, 95% of CIs would contain the true value)
 - No prior knowledge formally incorporated

 Bayesian:
 - Probability = degree of belief
 - Parameters are random variables with probability distributions; data are fixed once observed
 - Inference: posterior distribution (updated beliefs after seeing data)
 - Output: posterior mean/median, credible interval (probability that parameter falls in this interval given the data)
 - Prior knowledge explicitly incorporated through prior distribution

2. When to prefer each approach:

 Prefer frequentist when:
 - Strong prior knowledge is not available or hard to justify publicly
 - Results need to be communicated to a broadly frequentist audience
 - Simple hypothesis testing with a clear alpha level is the goal
 - Regulatory context requires NHST (e.g. clinical trial primary endpoint)

 Prefer Bayesian when:
 - Informative prior knowledge exists (previous studies, domain expertise) that should influence inference
 - You want to quantify evidence for the null hypothesis (Bayes factor)
 - Sequential/adaptive designs where interim analyses are needed
 - Complex hierarchical models where priors regularize unstable estimates
 - Small samples where priors stabilize estimates
 - Direct probability statements about parameters are needed ('there is a 92% probability the effect is positive')

3. If using Bayesian analysis:
 - Specify priors: weakly informative priors (regularizing) vs strongly informative priors (based on prior studies)
 - Sensitivity analysis: show results under different prior specifications
 - Report: prior distribution, posterior distribution, posterior mean with 95% credible interval, Bayes factor if testing hypotheses
 - Software: Stan / brms (R), PyMC (Python), JASP (GUI)

4. Bayes Factor interpretation:
 - BF > 100: decisive evidence for H1
 - BF 30–100: very strong evidence for H1
 - BF 10–30: strong evidence for H1
 - BF 3–10: moderate evidence for H1
 - BF 1–3: anecdotal evidence for H1
 - BF = 1: no evidence either way
 - BF < 1/3: moderate evidence for H0

Return: recommendation with rationale, prior specification for Bayesian approach, sensitivity analysis plan, and code in R (brms) or Python (PyMC). 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical analysis of research data work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical Analysis of Research Data or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Key conceptual differences:, Probability = long-run frequency of events in repeated experiments, Parameters are fixed (unknown) constants; data are random. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Statistical Analysis of Research Data.
