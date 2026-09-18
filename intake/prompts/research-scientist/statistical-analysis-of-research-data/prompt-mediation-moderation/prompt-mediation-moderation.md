# Mediation and Moderation Analysis *AI Prompt *

Design and analyze a mediation or moderation analysis for my study. Conceptual model: {{conceptual_model}} (e.g. 'X → M → Y' or 'X × W → Y') Hypotheses: {{hypotheses}} Data avai... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and analyze a mediation or moderation analysis for my study.

Conceptual model: {{conceptual_model}} (e.g. 'X → M → Y' or 'X × W → Y')
Hypotheses: {{hypotheses}}
Data available: {{data}}

1. Clarify the conceptual question:

 Mediation (X → M → Y):
 - Asks: does X affect Y through its effect on M?
 - M is the mechanism through which X influences Y
 - Example: does a training intervention (X) improve job performance (Y) by increasing self-efficacy (M)?

 Moderation (X × W → Y):
 - Asks: does the effect of X on Y depend on the level of W?
 - W is the boundary condition that strengthens or weakens the X-Y relationship
 - Example: does the training effect on performance (X → Y) differ by employee tenure (W)?

 Moderated mediation (the indirect effect is moderated):
 - Asks: does the mediated pathway (X → M → Y) operate differently at different levels of W?

2. Mediation analysis — using Hayes PROCESS or lavaan:

 Requirements:
 - Temporal precedence: X must precede M must precede Y in time
 - Causal inference requires ruling out reverse causation and confounding of M-Y relationship
 - Distinguish between mediation (mechanism) and moderation (boundary condition)

 Steps:
 a. Test total effect of X on Y (path c)
 b. Test effect of X on M (path a)
 c. Test effect of M on Y controlling for X (path b)
 d. Test direct effect of X on Y controlling for M (path c')
 e. Calculate indirect effect = a × b with bootstrap CI (5000 bootstraps; 95% CI not crossing 0 = significant mediation)

 Note: Baron and Kenny's causal steps approach (requiring significant c path) is outdated. Use bootstrap indirect effects.

3. Moderation analysis:
 - Center continuous predictors before computing interaction terms
 - Test the interaction term (X × W)
 - If significant: probe the interaction with simple slopes at W = mean ± 1SD (or for binary W, at each level)
 - Plot the interaction: fitted values of Y across the range of X, separately for levels of W
 - Report: interaction coefficient, simple slopes with SEs and p-values, region of significance (Johnson-Neyman technique)

4. Common errors to avoid:
 - Do not interpret partial mediation as a finding — it is just incomplete mediation
 - Do not conclude mediation from cross-sectional data without acknowledging this is assumed, not demonstrated
 - Do not probe an interaction that is not statistically significant

Return: analysis code, results interpretation, interaction plot, and a methods paragraph. 
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

The AI should return a structured result that covers the main requested outputs, such as Clarify the conceptual question:, Asks: does X affect Y through its effect on M?, M is the mechanism through which X influences Y. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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
