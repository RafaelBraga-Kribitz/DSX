# Experimental Design and Methodology *AI Prompts *

10 Research Scientist prompts in Experimental Design and Methodology. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 9 single prompts · 1 chain. 

## AI prompts in Experimental Design and Methodology 
10 prompts Intermediate Single prompt 01 
### Confound Identification 

Systematically identify the confounding variables and alternative explanations that threaten the validity of my study. Study design: {{study_design}} Main relationship of intere... 
Prompt text Systematically identify the confounding variables and alternative explanations that threaten the validity of my study.

Study design: {{study_design}}
Main relationship of interest: {{main_relationship}} (X → Y)
Sample and context: {{sample_context}}

1. What is a confounder:
 A confounder is a variable Z that:
 - Is associated with the exposure/predictor X
 - Is associated with the outcome Y
 - Is NOT on the causal pathway between X and Y (not a mediator)
 If Z is not controlled for, the observed X-Y association will be biased.

2. Confounder brainstorming — work through these categories:
 a. Demographic confounders: age, sex, gender, race/ethnicity, socioeconomic status, education
 b. Behavioral confounders: lifestyle factors, prior behavior, health behaviors, technology use
 c. Temporal confounders: secular trends, seasonality, historical events that coincide with the study
 d. Selection confounders: how participants were recruited, who chose to participate, who dropped out
 e. Measurement confounders: how X was measured (method, instrument, assessor) may differ across levels of Y
 f. Domain-specific confounders: {{field}}-specific factors I should consider

3. For each identified confounder, assess:
 - Direction of bias: does this confounder inflate or deflate the X-Y association?
 - Magnitude of potential bias: is this likely to be a minor or major source of bias?
 - Measurability: can this confounder be measured and controlled?

4. Strategies to address each confounder:
 - Randomization: if using an experiment, randomization balances all confounders in expectation
 - Restriction: limit the sample to a narrow range of the confounder (e.g. study only one age group)
 - Matching: match treatment and control participants on key confounders
 - Statistical adjustment: include confounders as covariates in the model
 - Stratification: analyze subgroups separately
 - Instrumental variables / natural experiments: if confounders are unmeasurable

5. Residual confounding:
 Even after adjustment, some confounding will remain. State explicitly:
 - Which confounders cannot be measured and therefore cannot be controlled
 - The likely direction and magnitude of residual confounding
 - What this means for the causal interpretation of your results

Return: confounder list with bias direction and magnitude assessment, proposed control strategy per confounder, and a residual confounding statement suitable for a limitations section. Copy prompt Open prompt details Intermediate Single prompt 02 
### Control Condition Designer 

Design the appropriate control condition(s) for my experiment. Treatment / intervention: {{treatment}} Outcome of interest: {{outcome}} Study population: {{population}} The choi... 
Prompt text Design the appropriate control condition(s) for my experiment.

Treatment / intervention: {{treatment}}
Outcome of interest: {{outcome}}
Study population: {{population}}

The choice of control condition is one of the most consequential design decisions in an experiment — it determines what your results actually mean.

1. Types of control conditions:

 No-treatment control:
 - Participants receive nothing
 - What it controls for: the natural trajectory of the outcome over time
 - What it does NOT control for: expectancy effects, attention effects, placebo response, demand characteristics
 - Appropriate when: you want to know if treatment outperforms doing nothing at all

 Waitlist control:
 - Participants are told they will receive treatment later
 - Controls for: passive time effects
 - Does not control for: expectancy, attention
 - Appropriate when: it is unethical to permanently withhold treatment; participants need a reason to stay in the study

 Active control (treatment as usual):
 - Participants receive the current standard of care or typical practice
 - Controls for: expectancy, attention, non-specific treatment effects
 - Appropriate when: you want to know if your treatment outperforms what is already available

 Placebo control:
 - Participants receive an inert treatment designed to be indistinguishable from the active treatment
 - Controls for: expectancy, placebo response, non-specific effects
 - Appropriate when: the active treatment has a specific mechanism you want to isolate
 - Requires: a credible placebo that participants cannot distinguish from treatment

 Active component control:
 - A version of the treatment with one component removed
 - Appropriate when: you want to test whether a specific component is the active ingredient

2. For my specific experiment:
 - Which control type is most appropriate? Why?
 - What does each plausible control condition tell me vs what it leaves confounded?
 - Are multiple control arms warranted to answer more than one question?

3. Blinding considerations:
 - Can participants be blinded to their condition? If not, how will expectancy effects be minimized?
 - Can assessors be blinded? Can analysts be blinded?
 - What are the risks of unblinding (participants guessing their condition)?

4. Ethical considerations:
 - Is it ethical to withhold treatment from the control group?
 - What happens to control participants after the study ends?

Return: recommended control condition(s), rationale, what each controls for and does not, and a blinding plan. Copy prompt Open prompt details Advanced Chain 03 
### Full Study Design Chain 

Step 1: Sharpen the research question — convert the broad research area into a specific, answerable, PICO-structured research question with clearly operationalized constructs an... 
Prompt text Step 1: Sharpen the research question — convert the broad research area into a specific, answerable, PICO-structured research question with clearly operationalized constructs and a defined unit of analysis.
Step 2: Select the study design — identify the strongest feasible design given the research question and available resources. State what causal claims the chosen design can and cannot support.
Step 3: Design the control condition — specify the comparison condition, what it controls for, and what it leaves uncontrolled. Design the blinding procedure.
Step 4: Confound analysis — systematically identify all potential confounders by category. Specify the control strategy for each. Acknowledge what residual confounding remains.
Step 5: Measurement plan — specify the operationalization of each construct. Provide psychometric evidence for each instrument. Identify measurement invariance requirements.
Step 6: Validity audit — audit the design for threats to internal, construct, statistical conclusion, and external validity. Document mitigation strategies.
Step 7: Pre-mortem — assume the study failed and identify the most likely causes. Modify the protocol to prevent or detect each failure mode.
Step 8: Write the methods section — produce a complete methods section covering: participants (eligibility, recruitment, sample size), design, procedure, measures, and analysis plan. Write with sufficient detail for independent replication. Copy prompt Open prompt details Intermediate Single prompt 04 
### Measurement Instrument Evaluation 

Evaluate the measurement instruments I plan to use and identify potential measurement problems. Constructs to measure: {{constructs}} Proposed instruments: {{instruments}} Popul... 
Prompt text Evaluate the measurement instruments I plan to use and identify potential measurement problems.

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

Return: instrument evaluation table, reliability and validity evidence summary, measurement invariance plan, and recommendations for any instruments with inadequate psychometric evidence. Copy prompt Open prompt details Advanced Single prompt 05 
### Pilot Study Design 

Design a pilot study to test the feasibility of my planned main study before committing full resources. Main study plan: {{main_study_plan}} Key feasibility concerns: {{feasibil... 
Prompt text Design a pilot study to test the feasibility of my planned main study before committing full resources.

Main study plan: {{main_study_plan}}
Key feasibility concerns: {{feasibility_concerns}}

A pilot study is NOT a small version of the main study. It is a feasibility study with specific objectives that go beyond collecting preliminary effect size estimates.

1. Define the pilot's specific objectives:
 Tick each relevant objective for my study:
 - Recruitment feasibility: can I enroll participants at the required rate? What is the actual enrollment rate per week?
 - Randomization fidelity: does the randomization procedure work correctly in practice?
 - Protocol adherence: do participants and experimenters follow the protocol as written?
 - Attrition rate: what proportion of enrolled participants complete the study? Is this acceptable?
 - Treatment fidelity: is the treatment delivered as intended? Manipulation check performance?
 - Instrument performance: do the measures work well in this population? (Floor/ceiling effects, internal consistency, completion time)
 - Data quality: are there data entry errors, missing items, technical failures?
 - Procedure timing: how long does each study session actually take?
 - Acceptability: do participants find the study burdensome or the treatment acceptable?

2. What a pilot should NOT be used for:
 - Estimating effect sizes for power calculation (pilots are too small and estimates are unreliable)
 - Conducting statistical hypothesis tests on outcomes (severely underpowered)
 - Drawing any inferential conclusions about the intervention's efficacy
 These are common misuses of pilot data that inflate Type I error in subsequent studies.

3. Sample size for the pilot:
 - Typical guidance: 12–30 participants per arm for assessing feasibility
 - Size is driven by precision of feasibility estimates, not power for outcome effects
 - Example: to estimate a 50% completion rate within ±15%, you need approximately 40 participants

4. Progression criteria:
 - Define in advance the criteria that must be met for the main study to proceed
 - Example: 'Proceed if: (a) enrollment rate ≥ 5 participants/week, (b) protocol adherence ≥ 80%, (c) attrition ≤ 20%'
 - 'Stop-go-modify' criteria: proceed, modify protocol and re-pilot, or abandon

5. Reporting the pilot:
 - Report all feasibility metrics, not just those that look favorable
 - Be explicit that hypothesis testing on outcomes was not an objective

Return: pilot objectives checklist, sample size justification, progression criteria, and a pilot study protocol outline. Copy prompt Open prompt details Advanced Single prompt 06 
### Pre-Mortem Analysis 

Conduct a pre-mortem analysis of my planned study — assume the study has failed and work backwards to identify what went wrong. Study plan: {{study_plan}} A pre-mortem is a pros... 
Prompt text Conduct a pre-mortem analysis of my planned study — assume the study has failed and work backwards to identify what went wrong.

Study plan: {{study_plan}}

A pre-mortem is a prospective failure analysis. Instead of optimistically planning for success, you assume the study produced null or uninterpretable results and identify the most likely causes.

1. The failure scenarios:

 Scenario A — Null results (no effect found):
 - Was the effect truly absent? Or was the study underpowered to detect it?
 - Was the treatment inadequately implemented (low treatment fidelity)?
 - Was the outcome measured too soon (insufficient follow-up)?
 - Were participants not the right population (wrong target group, too heterogeneous)?
 - Was there contamination between conditions?

 Scenario B — Uninterpretable results (effect found but meaning is unclear):
 - Did the manipulation check fail? (We do not know if the treatment changed the intended mechanism)
 - Did demand characteristics drive results? (Participants responded as they thought we wanted)
 - Was there differential attrition? (The groups who remained are systematically different)
 - Did an unmeasured third variable explain the result?

 Scenario C — Methodological failure:
 - Recruitment shortfall: could not enroll enough participants
 - Protocol deviations: participants or experimenters did not follow the protocol
 - Instrument problems: scale showed poor psychometric properties in this sample
 - Data loss: technical failures, missing data beyond acceptable thresholds

 Scenario D — External invalidity:
 - Results replicate in the lab but not in field settings
 - Results hold for the study sample but not for the target population
 - Results are highly context-specific and do not generalize

2. For each failure scenario:
 - Probability: how likely is this scenario to occur?
 - Impact: if this happens, can the study be salvaged or must it be abandoned?
 - Prevention: what can be done NOW, before data collection, to prevent or detect this?
 - Detection: how would you know during or after the study that this scenario occurred?

3. Protocol modifications from the pre-mortem:
 - List the specific changes to the study protocol that the pre-mortem analysis suggests
 - Include: manipulation checks, fidelity monitoring, attrition tracking, pilot testing

Return: failure scenario analysis, prevention and detection measures, and a revised protocol checklist. Copy prompt Open prompt details Beginner Single prompt 07 
### Research Question Sharpener 

Help me sharpen my research question into one that is specific, answerable, and well-scoped. My current research question: {{research_question}} Field: {{field}} 1. Diagnose the... 
Prompt text Help me sharpen my research question into one that is specific, answerable, and well-scoped.

My current research question: {{research_question}}
Field: {{field}}

1. Diagnose the current question:
 Evaluate it on these dimensions:
 - Specificity: is it clear exactly what is being measured, in whom, under what conditions?
 - Answerability: can empirical data actually answer this question?
 - Scope: is it too broad (requires 10 studies to answer) or too narrow (trivial to answer)?
 - Novelty: has this been answered already? What would a new answer add?
 - Feasibility: can this be studied with available methods, data, and resources?

2. Apply the PICO / PECO framework:
 For clinical/experimental research use PICO:
 - Population (P): who are the participants? Define inclusion and exclusion criteria.
 - Intervention / Exposure (I/E): what is being done to or observed about the participants?
 - Comparator (C): what is the comparison condition? (active control, placebo, no treatment, alternative exposure level)
 - Outcome (O): what is being measured? Specify primary outcome and key secondary outcomes.

 For non-clinical research, adapt:
 - Sample: who or what are the units of analysis?
 - Variable of interest: what is the key predictor, exposure, or condition?
 - Comparison: is there a meaningful baseline or contrast?
 - Measure: how will the outcome be operationalized?

3. Operationalize the key constructs:
 - For each key term in the research question: how will it be measured or defined?
 - Are there multiple valid operationalizations? Which will you choose and why?
 - What is the unit of analysis: individual, group, organization, country, time point?

4. Write 3 refined versions:
 - Version A: most conservative scope (definitely answerable with one study)
 - Version B: target scope (the version you should aim for)
 - Version C: ambitious scope (if the study goes well and you can extend it)

5. The one-sentence research question:
 Write the final research question as a single sentence suitable for the introduction of a paper: 'This study examines whether/how/what [relationship] between [variable X] and [variable Y] in [population] under [conditions].' Copy prompt Open prompt details Intermediate Single prompt 08 
### Sample Representativeness Audit 

Evaluate the representativeness of my sample and the generalizability of my findings. Study sample: {{sample_description}} Target population: {{target_population}} Recruitment m... 
Prompt text Evaluate the representativeness of my sample and the generalizability of my findings.

Study sample: {{sample_description}}
Target population: {{target_population}}
Recruitment method: {{recruitment_method}}

1. Define the population hierarchy:
 - Target population: the full population to which you want to generalize
 - Accessible population: the population you can realistically recruit from
 - Sampling frame: the list or mechanism from which you draw participants
 - Study sample: who actually participated
 - At each level: identify who is systematically excluded and why

2. WEIRD problem assessment:
 Assess whether your sample is WEIRD (Western, Educated, Industrialized, Rich, Democratic):
 - Western: is the sample from Western countries only? Many behavioral findings do not replicate cross-culturally.
 - Educated: what is the educational distribution? Is it higher than the target population?
 - Industrialized: is the sample from urban, industrialized settings? Rural or lower-resource populations may differ.
 - Rich: what is the income distribution? Is convenience sampling overrepresenting higher-income individuals?
 - Democratic: is the sample from stable democracies? Political context affects many research constructs.
 For each dimension: how different is your sample from your target population?

3. Volunteer bias:
 - People who volunteer for research differ systematically from those who do not
 - Volunteers tend to be more educated, more conscientious, more open to new experiences
 - Assess: in what ways might your volunteers differ from the target population on theoretically relevant variables?

4. Attrition bias:
 - Who dropped out? Compare completers vs dropouts on baseline characteristics.
 - Is dropout related to treatment condition or outcome severity?
 - What does differential attrition do to the representativeness of your final analytic sample?

5. Generalizability statement:
 - Write an honest, specific generalizability statement for the paper: 'Results are most likely to generalize to [specific population]. Caution is warranted in applying findings to [different groups] because [specific reason].'

Return: population hierarchy analysis, WEIRD assessment, volunteer and attrition bias evaluation, and generalizability statement. Copy prompt Open prompt details Beginner Single prompt 09 
### Study Design Selector 

Help me choose the right study design for my research question. Research question: {{research_question}} Available resources: {{resources}} (time, budget, sample access) Field/d... 
Prompt text Help me choose the right study design for my research question.

Research question: {{research_question}}
Available resources: {{resources}} (time, budget, sample access)
Field/domain: {{field}}

1. Classify my research question:
 - Is this a question about description (what is the prevalence or distribution of X)?
 - Is this a question about association (is X related to Y)?
 - Is this a question about causation (does X cause Y)?
 - Is this a question about mechanism (how or why does X cause Y)?
 The appropriate study design depends critically on this classification.

2. Present the candidate designs:

 For descriptive questions:
 - Cross-sectional survey: snapshot of a population at one point in time. Pros: fast, cheap. Cons: no temporal information, cannot establish causality.
 - Case series / case report: detailed description of a small number of cases. Pros: useful for rare phenomena. Cons: no comparison group, cannot generalize.

 For association questions:
 - Observational cohort: follow a group over time and measure exposures and outcomes. Pros: can assess temporality (X precedes Y). Cons: expensive, slow, confounding.
 - Case-control: compare people who have the outcome to those who do not and look back at exposures. Pros: efficient for rare outcomes. Cons: recall bias, cannot estimate prevalence.
 - Cross-sectional: measure exposure and outcome at the same time. Pros: fast. Cons: cannot determine temporal order.

 For causal questions:
 - Randomized controlled trial (RCT): gold standard for causality. Randomly assign participants to treatment or control. Pros: eliminates confounding. Cons: expensive, ethical constraints, artificial settings.
 - Quasi-experiment: exploit natural variation in treatment assignment (difference-in-differences, regression discontinuity, instrumental variables). Pros: more realistic than RCT. Cons: requires strong assumptions.
 - Natural experiment: an external event creates as-if random assignment. Pros: high external validity. Cons: rare and not controllable.

3. Apply the evidence hierarchy:
 - Rank the feasible designs for my question from strongest to weakest causal inference
 - Identify which designs are feasible given my resources and constraints

4. Recommendation:
 - Recommend the strongest feasible design
 - State clearly: what causal claims can this design support, and what claims it cannot
 - Identify the top 2 threats to validity in the recommended design and how to mitigate them

Return: design recommendation with full rationale, validity threat analysis, and a one-paragraph justification suitable for a methods section. Copy prompt Open prompt details Intermediate Single prompt 10 
### Validity Threat Audit 

Audit my study design for threats to internal and external validity. Study description: {{study_description}} Apply the four validity frameworks systematically. 1. Internal vali... 
Prompt text Audit my study design for threats to internal and external validity.

Study description: {{study_description}}

Apply the four validity frameworks systematically.

1. Internal validity (did the treatment really cause the observed outcome?):
 Check for each threat:
 - History: did any external event occur during the study that could explain the outcome?
 - Maturation: could participants have changed naturally over the study period independent of the treatment?
 - Testing: could repeated measurement itself change participants' responses?
 - Instrumentation: did the measurement tools or procedures change during the study?
 - Regression to the mean: were extreme scorers selected? Their scores would likely move toward the mean naturally.
 - Selection bias: were treatment and control groups systematically different at baseline?
 - Attrition / mortality: did participants drop out differentially across conditions?
 - Contamination: did control participants receive elements of the treatment inadvertently?

2. Construct validity (are you measuring and manipulating what you think you are?):
 - Construct underrepresentation: does your operationalization miss important aspects of the construct?
 - Construct-irrelevant variance: does your measure capture things other than the construct of interest?
 - Manipulation check: how do you know the treatment actually changed what it was intended to change?

3. Statistical conclusion validity (are your statistical inferences correct?):
 - Low statistical power: are you likely to detect a real effect if it exists?
 - Multiple comparisons: are you testing many outcomes without adjustment?
 - Assumption violations: do the data meet the assumptions of your planned analyses?
 - Fishing and flexibility in data analysis: are analysis decisions made post-hoc after seeing results?

4. External validity (do results generalize?):
 - Population validity: how similar is your sample to the population of interest?
 - Ecological validity: how similar are your study conditions to real-world conditions?
 - Temporal validity: are results likely to hold at other time points?
 - Treatment variation: does your treatment represent how it would actually be delivered in practice?

5. For each identified threat:
 - Severity: how likely is this threat to bias results and in what direction?
 - Mitigation: what design features address this threat?
 - Residual risk: what threat remains after mitigation?
 - Disclosure: how will this be acknowledged in the limitations section?

Return: validity audit table (threat, severity, mitigation, residual risk), overall validity assessment, and limitations section draft. Copy prompt Open prompt details 
## Recommended Experimental Design and Methodology workflow 
1 
### Confound Identification 

Start with a focused prompt in Experimental Design and Methodology so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Control Condition Designer 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Full Study Design Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Measurement Instrument Evaluation 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
