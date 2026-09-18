# Measurement Instrument Evaluation *AI Prompt *

Evaluate the measurement instruments I plan to use and identify potential measurement problems. Constructs to measure: {{constructs}} Proposed instruments: {{instruments}} Popul... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Evaluate the measurement instruments I plan to use and identify potential measurement problems.

Constructs to measure: {{constructs}}
Proposed instruments: {{instruments}}
Population: {{population}}

1. Reliability (consistency of measurement):

 Internal consistency:
 - For multi-item scales: Cronbach's alpha should be ≥ 0.70 for research, ≥ 0.80 for applied decisions
 - Omega (ω) is preferred over alpha when items are not tau-equivalent
 - Danger: high alpha does not mean the scale measures a single construct (it may have high interitem correlations for other reasons)

 Test-retest reliability:
 - How stable is the measure over time? Appropriate stability period depends on whether the construct is trait-like (stable) or state-like (variable)
 - Intraclass correlation coefficient (ICC) for continuous measures; Kappa for categorical

 Inter-rater reliability:
 - For observational or rating measures: how consistently do different raters score the same material?
 - ICC ≥ 0.75 is generally acceptable

2. Validity (does the instrument measure what it claims to?):

 Content validity: do the items comprehensively cover the construct domain?
 Criterion validity: does the instrument correlate appropriately with a gold-standard measure?
 Construct validity: does the instrument behave as theory predicts?
 - Convergent validity: correlates with theoretically related measures
 - Discriminant validity: does NOT correlate with theoretically unrelated measures

3. Measurement invariance:
 - Does the instrument measure the same construct in the same way across demographic groups?
 - Without invariance, group comparisons are invalid
 - How will you test for invariance?

4. Practical considerations:
 - Burden: how long does the instrument take? Is this feasible in my study context?
 - Floor and ceiling effects: will many participants score at the extreme ends of the scale?
 - Translation and adaptation: if using with a different language/culture than the instrument was validated on, what adaptation is needed?

5. For each instrument in my study:
 - Evidence quality: is reliability and validity evidence strong, moderate, or weak?
 - Population match: was it validated on a population similar to mine?
 - Known limitations: what are the documented weaknesses of this instrument?
 - Alternative: if this instrument is inadequate, what would be better?

Return: instrument evaluation table, reliability and validity evidence summary, measurement invariance plan, and recommendations for any instruments with inadequate psychometric evidence. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin experimental design and methodology work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Experimental Design and Methodology or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Reliability (consistency of measurement):, For multi-item scales: Cronbach's alpha should be ≥ 0.70 for research, ≥ 0.80 for applied decisions, Omega (ω) is preferred over alpha when items are not tau-equivalent. The final answer should stay clear, actionable, and easy to review inside a experimental design and methodology workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Experimental Design and Methodology.
