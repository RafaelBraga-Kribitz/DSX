# Experimental Design *AI Prompts *

3 Statistician prompts in Experimental Design. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Experimental Design 
3 prompts Advanced Single prompt 01 
### Factorial and Adaptive Designs 

Design a factorial or adaptive experimental design for this study. Research question: {{research_question}} Factors: {{factors}} (each factor and its levels) Adaptive elements n... 
Prompt text Design a factorial or adaptive experimental design for this study.

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

Return: factorial design specification (factors, combinations, sample size), interaction test plan, adaptive design choice with stopping boundaries, and analysis approach. Copy prompt Open prompt details Intermediate Single prompt 02 
### Observational Study Design 

Design an observational study and plan the appropriate analysis to control for confounding. Exposure of interest: {{exposure}} Outcome of interest: {{outcome}} Available data: {... 
Prompt text Design an observational study and plan the appropriate analysis to control for confounding.

Exposure of interest: {{exposure}}
Outcome of interest: {{outcome}}
Available data: {{data_description}}
Study type: {{study_type}} (cross-sectional, case-control, cohort)

1. Study design selection:

 Cross-sectional:
 - Exposure and outcome measured at the same time
 - Pros: fast, cheap, good for prevalence estimation
 - Cons: cannot establish temporality; prone to reverse causation
 - Best for: estimating associations and generating hypotheses

 Case-control:
 - Sample based on outcome (cases vs controls), then measure past exposure
 - Pros: efficient for rare outcomes
 - Cons: recall bias; selection of controls is critical
 - Analysis: conditional or unconditional logistic regression; effect measure = odds ratio

 Prospective cohort:
 - Sample based on exposure status, follow forward to measure outcomes
 - Pros: can measure incidence, multiple outcomes, avoids recall bias
 - Cons: expensive, slow; loss to follow-up threatens validity
 - Analysis: survival analysis (Cox model), incidence rate ratio; effect measure = hazard ratio, RR

 Retrospective cohort:
 - Historical data used to construct a cohort; follow forward in time using existing records
 - Faster than prospective; subject to data quality of historical records

2. Confounding control methods:

 Design-stage:
 - Restriction: limit study to a homogeneous subgroup (removes confounding from that variable)
 - Matching: match cases and controls (or exposed and unexposed) on potential confounders
 - Advantage: guaranteed balance; disadvantage: cannot study matched variables as exposures

 Analysis-stage:
 - Multivariable regression: include confounders as covariates
 - Propensity score methods (see propensity score prompt)
 - Stratification: estimate effect within strata of the confounder, then pool with Mantel-Haenszel

3. Bias assessment:
 - Selection bias: is the study sample representative of the target population?
 - Information bias: are exposure and outcome measured accurately?
 - Confounding: have all major confounders been measured and controlled?
 - Use a directed acyclic graph (DAG) to identify the minimal sufficient adjustment set

4. Directed Acyclic Graph (DAG):
 - Draw the causal diagram: nodes = variables, arrows = direct causal effects
 - Identify confounders: common causes of exposure and outcome
 - Identify colliders: common effects of two variables (do NOT adjust for colliders — this opens a non-causal path)
 - Use the backdoor criterion to identify the adjustment set

Return: study design recommendation, confounding control plan, DAG specification, and bias assessment. Copy prompt Open prompt details Intermediate Single prompt 03 
### Randomized Controlled Trial Design 

Design a randomized controlled trial (RCT) to answer this research question. Research question: {{research_question}} Intervention: {{intervention}} Primary outcome: {{primary_o... 
Prompt text Design a randomized controlled trial (RCT) to answer this research question.

Research question: {{research_question}}
Intervention: {{intervention}}
Primary outcome: {{primary_outcome}}
Population: {{population}}
Practical constraints: {{constraints}} (budget, timeline, ethical restrictions)

1. Randomization design:

 Simple randomization:
 - Each participant independently assigned with probability p = 0.5
 - Works well for large n (> 200); may produce imbalanced groups in small trials

 Block randomization:
 - Participants randomized in blocks of fixed size (e.g. blocks of 4 or 6)
 - Guarantees approximately equal group sizes throughout the trial
 - Use when enrollment is sequential and interim analyses are planned

 Stratified randomization:
 - Randomize separately within strata of key prognostic variables (age group, site, disease severity)
 - Prevents chance imbalance on important covariates
 - Combine with block randomization within strata

 Cluster randomization:
 - Randomize groups (clinics, schools, communities) rather than individuals
 - Use when individual randomization causes contamination
 - Requires larger sample size (inflate by design effect = 1 + (m-1) x ICC)

2. Blinding:
 - Open-label: neither participants nor assessors are blinded (highest risk of bias)
 - Single-blind: participants are blinded to treatment assignment
 - Double-blind: both participants and outcome assessors are blinded (gold standard for efficacy)
 - Triple-blind: includes the data analysts
 - Is blinding feasible for this intervention? If not: use blinded outcome assessment at minimum

3. Sample size and allocation:
 - Calculate required n based on primary outcome (see power analysis prompt)
 - Equal allocation (50/50) is most efficient when costs per participant are equal
 - Unequal allocation: use if one arm is more costly or to expose fewer to the control

4. Analysis plan (pre-specified):
 - Primary analysis: intention-to-treat (ITT) — analyze participants as randomized, regardless of adherence
 - Per-protocol analysis: sensitivity analysis for those who completed the protocol
 - Handling missing data: specify imputation method in advance
 - Pre-register the primary outcome and analysis plan (ClinicalTrials.gov, OSF)

5. Validity threats:
 - Selection bias: only randomization fully controls this
 - Attrition: track dropout rate by arm; > 20% differential dropout threatens validity
 - Contamination: control group receives elements of the intervention
 - CONSORT checklist: use for reporting

Return: randomization design recommendation, blinding plan, sample size, ITT analysis plan, and validity threat assessment. Copy prompt Open prompt details 
## Recommended Experimental Design workflow 
1 
### Factorial and Adaptive Designs 

Start with a focused prompt in Experimental Design so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Observational Study Design 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Randomized Controlled Trial Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
