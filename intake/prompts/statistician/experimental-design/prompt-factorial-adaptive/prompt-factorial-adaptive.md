# Factorial and Adaptive Designs *AI Prompt *

Design a factorial or adaptive experimental design for this study. Research question: {{research_question}} Factors: {{factors}} (each factor and its levels) Adaptive elements n... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a factorial or adaptive experimental design for this study.

Research question: {{research_question}}
Factors: {{factors}} (each factor and its levels)
Adaptive elements needed: {{adaptive_needs}} (interim analysis, arm dropping, response-adaptive randomization)

1. Factorial designs:

 Full factorial:
 - All combinations of factor levels are tested
 - 2^k design: k factors each at 2 levels → 2^k treatment combinations
 - Advantages: tests main effects AND interactions simultaneously
 - Sample size: same n needed per cell as a one-factor design, but tests many more questions
 - Key output: interaction plot — does the effect of factor A depend on the level of factor B?

 Fractional factorial:
 - Test only a fraction of all 2^k combinations (e.g. 2^(k-p) design)
 - Aliasing: main effects are confounded with high-order interactions
 - Use when: k is large and high-order interactions are assumed negligible
 - Resolution III: main effects aliased with 2-way interactions (minimum for screening)
 - Resolution V: main effects and 2-way interactions estimable (preferred for confirmatory)

2. Adaptive designs:

 Group sequential design:
 - Pre-planned interim analyses at specified information fractions (e.g. at 50% and 100% of n)
 - Spending functions control Type I error across looks:
 - O'Brien-Fleming: strict early stopping, liberal late (good when early stopping is rare)
 - Pocock: equal thresholds at each look (more liberal early)
 - Stopping rules: stop for efficacy (p < boundary), futility (conditional power < 20%), or safety

 Response-adaptive randomization:
 - Allocation probabilities update based on accumulating outcome data
 - More participants assigned to the arm showing better performance
 - Pros: ethical (fewer participants in inferior arm)
 - Cons: increases bias risk, complicates inference; FDA skepticism in confirmatory trials

 Platform trials:
 - Multiple interventions tested simultaneously on a shared control arm
 - Arms can enter and exit the platform based on interim results
 - Efficient for rapid testing of many treatments (COVID-19 trials used this)

3. Analysis for adaptive designs:
 - Naive p-values from adaptive designs are invalid (inflation of Type I error)
 - Use: conditional power, stagewise p-values (combination function), or Bayesian posterior probabilities
 - Closed testing principle: preserves familywise error rate when multiple hypotheses are tested

Return: factorial design specification (factors, combinations, sample size), interaction test plan, adaptive design choice with stopping boundaries, and analysis approach. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin experimental design work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Experimental Design or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Factorial designs:, All combinations of factor levels are tested, 2^k design: k factors each at 2 levels → 2^k treatment combinations. The final answer should stay clear, actionable, and easy to review inside a experimental design workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Experimental Design.
