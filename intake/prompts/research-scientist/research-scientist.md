# Research Scientist *AI Prompts *

Research Scientist AI prompt library with 32 prompts in 3 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 3 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Research Scientist prompt categories 
3 categories 
### Reproducibility and Open Science 

AI prompts for reproducibility and open science practices, including experiment tracking, transparent reporting, and repeatable research outputs. 
11 prompts Code Review for Reproducibility Data Sharing Plan → 
### Statistical Analysis of Research Data 

AI prompts for statistical analysis of research data, including descriptive summaries, inferential tests, assumptions checks, and interpretation. 
11 prompts Analysis Plan Chain Bayesian vs Frequentist Analysis → 
### Experimental Design and Methodology 

AI prompts for experimental design and research methodology, including hypothesis framing, controls, bias reduction, and analysis planning. 
10 prompts Confound Identification Control Condition Designer → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 32 Reproducibility and Open Science 11 Statistical Analysis of Research Data 11 Experimental Design and Methodology 10 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **32 **of 32 prompts 
## Reproducibility and Open Science 
11 prompt s Reproducibility and Open Science Intermediate Prompt 01 
### Code Review for Reproducibility 
Review my analysis code for reproducibility and identify problems that would prevent another researcher from replicating my results.

Code: {{analysis_code}}
Language: {{language}}

Check for each category of reproducibility problem:

1. Environment problems (code may run differently on another machine):
 - Absolute paths: any path starting with /Users/ or C:\Users\ will fail on another machine. Replace with relative paths from the project root.
 - Missing package/library declarations: list all library() or import statements at the top of the script.
 - Undeclared package versions: are package versions recorded? Different versions may produce different results.
 - System-specific code: any code that depends on OS-specific behavior.
 - Missing random seeds: any analysis using randomization must set a seed for reproducibility.

2. Ordering problems (code must run from top to bottom without manual steps):
 - Objects used before they are defined: will cause errors if run sequentially.
 - External file dependencies not created by earlier code: scripts that depend on files that another analyst must manually provide.
 - Hidden state: code that relies on objects in the global environment from a previous session.
 - Manual steps: any step that requires human intervention (e.g. 'run this block first, then that block').

3. Data provenance problems:
 - Raw data modified in place: raw data files should never be overwritten.
 - Missing data source documentation: where did the raw data come from? How was it obtained?
 - Undocumented exclusions: data filtered or excluded without comment explaining why.

4. Documentation problems:
 - Uncommented analytical decisions: if a choice was made (which covariates to include, how to handle outliers), a comment should explain why.
 - Variable names that require knowledge of the project: use descriptive variable names.
 - No description of what the script does at the top.

5. Output stability:
 - Does the code produce the same output when run twice with the same inputs?
 - Are intermediate results saved so the full pipeline does not need to re-run to get the final results?

For each problem found:
- Line number or code section
- Description of the problem
- Corrected code

Return: annotated code review, corrected code, and a reproducibility score (0–100) with justification. Copy prompt View page Show more ↓ Reproducibility and Open Science Intermediate Prompt 02 
### Data Sharing Plan 
Help me create a data sharing plan that maximizes openness while addressing legal, ethical, and practical constraints.

Data type: {{data_type}}
Participant population: {{population}}
Funder requirements: {{funder}} (e.g. NIH, NSF, Wellcome Trust, EU Horizon)
Journal requirements: {{journal}}

1. Determine the appropriate level of data sharing:

 Fully open (preferred when possible):
 - Data deposited in a public repository with no access controls
 - Appropriate when: data contains no identifying information and poses no re-identification risk
 - Repositories: OSF, Zenodo, Figshare, domain-specific repositories (ICPSR, UKDA, GenBank, etc.)

 Restricted access:
 - Data available to qualified researchers upon request or through an application process
 - Appropriate when: data contains sensitive information but de-identification is not sufficient
 - Repositories: UKDA, ICSPR Restricted Access, institutional data repository

 Available on request:
 - Data available by contacting the authors
 - Least preferred: frequently data becomes unavailable after author changes institution
 - Appropriate only when: repository deposit is genuinely not possible

 Not shared:
 - Appropriate only when: legal or ethical prohibitions exist (classified data, legally protected patient records)
 - Must provide a clear statement of why data cannot be shared

2. De-identification requirements:
 - Apply Safe Harbor method (HIPAA): remove the 18 specified identifiers
 - Apply Expert Determination: a qualified expert certifies re-identification risk is very small
 - For small or unusual populations: even 'de-identified' data may be re-identifiable — consider restricted access
 - Synthetic data: generate synthetic data that preserves statistical properties without individual records

3. Metadata and documentation:
 - Data without documentation is nearly unusable
 - Provide: a codebook for every variable (name, label, values, missing codes), a data collection instrument, and a processing log describing all transformations from raw to analysis-ready data

4. Consent language (for future studies):
 - Consent forms should include explicit language about data sharing
 - Recommended language: 'De-identified data from this study may be shared with other researchers via a secure repository to enable verification of results and future research.'

5. Funder-specific requirements:
 - NIH: Data Management and Sharing Plan required for all funded studies
 - NSF: similar requirements, check program-specific guidance
 - EU Horizon: 'open by default' requirement with possibility of exceptions
 Write the data management plan text appropriate for {{funder}}.

Return: data sharing recommendation, de-identification procedure, repository selection, metadata checklist, and data management plan text for the funder. Copy prompt View page Show more ↓ Reproducibility and Open Science Advanced Prompt 03 
### Meta-Analysis Readiness 
Prepare my study to maximize its contribution to future meta-analyses of this research area.

Study details: {{study_details}}
Field: {{field}}

Meta-analyses synthesize evidence across studies, but are only as good as the data provided by individual studies. Most studies are meta-analysis-unfriendly due to incomplete reporting.

1. Effect size reporting requirements:
 Report ALL of the following for every primary and secondary outcome:
 - Sample size per group (or total N for correlational studies)
 - Means and standard deviations per group (for continuous outcomes)
 - The correlation between time points (for pre-post designs without a control group)
 - Cell frequencies (for categorical outcomes)
 - The exact test statistic (t, F, z, χ²) and degrees of freedom
 - Exact p-value
 - Effect size (d, r, OR, RR) with 95% CI
 These allow meta-analysts to compute any effect size metric from your data.

2. Complete reporting for non-significant results:
 - Non-significant results are as important to meta-analysis as significant ones
 - Report exact statistics even for null results — 'p = .42' is far more informative than 'ns'
 - Null results suppressed by publication bias cause meta-analyses to overestimate effects

3. Moderator variables:
 Report participant characteristics that are common moderators in {{field}}:
 - Demographic variables: age (mean, SD, range), sex/gender (proportions), relevant clinical characteristics
 - Study characteristics: setting, assessor training, duration, intensity
 - These allow meta-analysts to test heterogeneity and identify moderators

4. PRISMA / CONSORT reporting:
 - Clinical trials: follow CONSORT checklist for complete reporting
 - Observational studies: follow STROBE checklist
 - Systematic reviews: follow PRISMA checklist
 - These checklists ensure all information needed for meta-analysis is reported

5. Data and code sharing for meta-analytic use:
 - Provide participant-level data when possible (allows individual-patient-data meta-analysis)
 - At minimum: provide a summary statistics table with all the values in point 1 above
 - Share in a format compatible with meta-analysis software (metafor in R, Comprehensive Meta-Analysis, RevMan)

6. Registered in a trials registry:
 - Clinical trials: PROSPERO, ClinicalTrials.gov
 - Psychological studies: OSF, AsPredicted
 - Registry number must appear in the paper for inclusion in high-quality meta-analyses

Return: meta-analysis reporting checklist, summary statistics table template, CONSORT/STROBE/PRISMA compliance check, and data sharing format recommendation. Copy prompt View page Show more ↓ Reproducibility and Open Science Intermediate Prompt 04 
### Open Materials Preparation 
Prepare my study materials for open sharing so other researchers can replicate and build on my work.

Materials to share: {{materials_list}} (stimuli, surveys, experimental scripts, coding schemes, etc.)
Repository: {{repository}} (OSF, GitHub, institutional repository, etc.)

1. What to share:
 - Stimuli: all experimental stimuli in their original form (images, audio, video, text)
 - Survey instruments: the exact survey or questionnaire as presented to participants, including all instructions
 - Experimental scripts: code for computerized experiments (PsychoPy, jsPsych, Qualtrics export)
 - Coding schemes: rubrics for rating or coding qualitative data, with training examples
 - Pilot materials: any materials from pilot testing that informed the final design

2. Documentation to accompany each material:
 - What it is: a plain-language description of what this material is and what it does
 - When it was used: at what point in the study protocol was this used?
 - How it was scored or coded: if the material produces data, how are responses scored or coded?
 - Adaptations: if this material was adapted from an existing source, what was changed and why?
 - License: under what terms may other researchers use this material?

3. Licensing:
 - For original materials: use Creative Commons CC-BY (others may use with attribution)
 - For adapted materials: check the license of the original — some restrict derivatives
 - For code: use an open source license (MIT, Apache 2.0, GPL)
 - For data: use CC-BY or CC0 (public domain dedication)
 - Never share materials under restrictive licenses that prevent replication

4. README for the materials repository:
 - What this repository contains
 - How materials correspond to the published paper
 - Any materials that could not be shared and why
 - Contact information for questions
 - How to cite the materials

5. Getting a persistent identifier:
 - DOI for materials enables citation tracking
 - OSF and Zenodo provide free DOIs for deposited materials
 - Include the materials DOI in the published paper

6. What you cannot or should not share:
 - Materials under copyright that you do not own
 - Materials that would allow identification of participants
 - Commercially licensed instruments — instead, provide the name and where to obtain them

Return: materials inventory checklist, documentation template per material type, license recommendations, and README template. Copy prompt View page Show more ↓ Reproducibility and Open Science Advanced Chain 05 
### Open Science Practices Chain 
Step 1: Preregistration — write and submit a complete preregistration before data collection begins. Include: research question, hypotheses, design, measures, sample size justification, primary analysis plan, secondary analyses, assumption checks, missing data plan, and exclusion criteria. Timestamp it.
Step 2: Registered Report submission (if applicable) — if the target journal offers Registered Reports, format the Stage 1 submission. Submit before data collection for an In-Principle Acceptance.
Step 3: Research compendium setup — initialize the project directory structure with separate raw data, processed data, code, and output folders. Set up version control (Git). Record the computing environment (renv, requirements.txt). Write the README.
Step 4: Data collection and contemporaneous documentation — document all protocol deviations, unexpected events, and unplanned decisions in a study log as they occur. Do not rely on memory after the fact.
Step 5: Analysis — run the pre-specified analyses exactly as registered. Any deviation from the plan must be explicitly noted with a reason. Additional exploratory analyses may be conducted but must be clearly labeled as unregistered.
Step 6: Open materials, data, and code — prepare all study materials for sharing. De-identify the data. Finalize the analysis code so it runs from raw data to paper tables and figures with a single command. Deposit to a repository with a DOI.
Step 7: Transparent reporting — write the paper with transparent reporting: report all pre-registered outcomes (not just significant ones), label exploratory analyses, include the preregistration DOI, materials DOI, and data DOI. Complete the relevant reporting checklist (CONSORT, STROBE, etc.). Copy prompt View page Show more ↓ Reproducibility and Open Science Advanced Prompt 06 
### P-hacking and HARKing Audit 
Audit my analysis and reporting for practices that inflate false positive rates, even unintentionally.

Analysis history: {{analysis_history}}
Final results: {{results}}

Researchers often engage in questionable research practices inadvertently. This audit helps identify and correct them.

1. P-hacking: flexibility in data analysis that increases the probability of a false positive

 Check for each practice:

 Outcome switching:
 - Was the primary outcome changed after seeing results?
 - Are results reported selectively — only outcomes that reached significance?
 - Test: compare reported outcomes to outcomes listed in the preregistration or methods section

 Optional stopping:
 - Was data collection stopped when significance was reached?
 - Was additional data collected after a non-significant result?
 - Impact: stopping when p < .05 inflates Type I error to ~14% for a nominal 5% test

 Covariate inclusion decisions:
 - Were covariates added or removed based on whether they changed the p-value?
 - Are different covariates used for different outcomes without pre-specification?

 Outlier exclusion decisions:
 - Were outlier exclusion rules determined after seeing how they affected results?
 - Were different exclusion rules applied to different outcomes?

 Subgroup analysis:
 - Were significant subgroup effects reported without pre-specification?
 - Was the overall non-significant result followed by searching for a significant subgroup?

2. HARKing: Hypothesizing After Results are Known

 Signs of HARKing:
 - Hypotheses in the paper perfectly predict the pattern of results, including null findings for control variables
 - The Introduction has an unusual post-hoc quality — theory exactly matches what was found
 - Exploratory results are presented as if they were predicted
 - No inconsistencies between the hypotheses and the results

3. For each identified practice:
 - Impact: how does this inflate Type I error?
 - Correction: what is the correct analysis or reporting approach?
 - If this was done inadvertently: how to report results honestly now

4. The correction path:
 - If analyses were done that were not pre-specified: label them as exploratory
 - If the primary outcome was changed: report results for the original primary outcome as well
 - If the result depends on a specific outlier rule: report a robustness check with the alternative rule
 - Never delete analyses that were run; include all in supplementary materials

Return: audit findings per practice, severity assessment, correction recommendations, and a transparency statement suitable for inclusion in the paper. Copy prompt View page Show more ↓ Reproducibility and Open Science Beginner Prompt 07 
### Preregistration Writer 
Help me write a complete preregistration for my study.

Study overview: {{study_overview}}
Platform: {{platform}} (OSF, AsPredicted, ClinicalTrials.gov, PROSPERO)

Preregistration locks in your hypotheses, design, and analysis plan before data collection, preventing HARKing and p-hacking.

1. Hypotheses:
 - State each hypothesis precisely and in a way that is clearly falsifiable
 - Specify directionality: 'X will be higher than Y' not 'X and Y will differ'
 - Distinguish confirmatory hypotheses (tested with pre-specified alpha) from exploratory questions
 - Number each hypothesis: H1, H2, H3

2. Design:
 - Study type and design (RCT, observational, within-subjects, etc.)
 - Manipulations and their operationalization
 - Measures: name and description of each instrument
 - Primary outcome: specify exactly one primary outcome
 - Secondary outcomes: list all, in priority order

3. Participants:
 - Target population and eligibility criteria (inclusion and exclusion)
 - Recruitment source and procedure
 - Sample size and power analysis justification
 - Stopping rule: will data collection stop at a fixed N or at a fixed date?

4. Analysis plan:
 - Primary analysis: exact test, model specification, covariates, alpha level
 - Secondary analyses: same level of specificity
 - Handling of assumption violations: specify in advance what you will do
 - Missing data approach
 - Exclusion criteria for the analytic sample (different from eligibility)
 - Multiple comparison correction

5. What happens if:
 - Recruitment falls short of target?
 - Primary outcome has excessive missing data?
 - A key assumption is violated?
 Pre-specify contingency plans for foreseeable problems.

6. Transparency commitments:
 - Will data be shared? Where and under what conditions?
 - Will analysis code be shared?
 - Will materials be shared?

Return: complete preregistration text formatted for the chosen platform, with each section written at the level of specificity required to make it a meaningful constraint. Copy prompt View page Show more ↓ Reproducibility and Open Science Advanced Prompt 08 
### Registered Report Design 
Help me structure my study as a Registered Report to eliminate publication bias for my research.

Study overview: {{study_overview}}
Target journal: {{journal}}

1. What is a Registered Report:
 A Registered Report (RR) is a publication format where peer review occurs in two stages:
 - Stage 1 (before data collection): the introduction, hypotheses, methods, and analysis plan are peer reviewed. If accepted, the journal issues an In-Principle Acceptance (IPA) — a commitment to publish regardless of results, conditional on following the approved protocol.
 - Stage 2 (after data collection and analysis): the completed manuscript is reviewed for adherence to the approved protocol. Results cannot cause rejection.
 - Key benefit: eliminates publication bias and incentivizes rigorous methods over positive results.

2. Stage 1 manuscript components:

 Introduction:
 - Comprehensive literature review demonstrating that the research question is important and unanswered
 - Clear theoretical rationale for the predicted effects
 - Explicit a priori hypotheses that follow from the theory

 Methods:
 - Participants: eligibility criteria, recruitment, sample size with power analysis, stopping rule
 - Design and procedure: sufficient detail for independent replication
 - Measures: full description of all instruments with psychometric evidence
 - Analysis plan: pre-specified primary and secondary analyses, assumption checks, missing data, exclusion criteria
 - Timeline and feasibility: evidence that the study is feasible

3. Handling deviations from the protocol:
 - Minor deviations (e.g. slightly fewer participants than planned): disclose transparently; usually does not affect IPA
 - Unanticipated events: document contemporaneously; discuss with editor before proceeding
 - If a major assumption of the analysis plan turns out to be violated: the pre-specified contingency plan applies
 - Post-hoc analyses: any analysis not in the approved plan must be clearly labeled as 'unregistered' or 'exploratory'

4. Distinguishing confirmatory from exploratory in the Stage 2 paper:
 - Use clear labeling: confirmatory (pre-registered) vs exploratory (not pre-registered)
 - Exploratory results are not second-class — they are hypothesis-generating for future registered studies
 - Never present exploratory results as if they were confirmatory

5. Finding Registered Report journals:
 - The Center for Open Science maintains a list of journals offering RR format
 - Consider whether the target journal's RR guidelines match the study timeline

Return: Stage 1 manuscript outline, analysis plan formatted for RR review, and guidance on handling anticipated deviations. Copy prompt View page Show more ↓ Reproducibility and Open Science Advanced Prompt 09 
### Replication Failure Diagnosis 
My replication attempt did not reproduce the original finding. Help me diagnose why and what conclusions to draw.

Original finding: {{original_finding}} (effect size: {{original_es}})
Replication finding: {{replication_finding}} (effect size: {{replication_es}})
Design differences: {{design_differences}}

1. First: quantify the discrepancy
 - Is the replication effect size significantly different from the original? Use a test of heterogeneity (Q statistic or equivalence test)
 - What is the 95% CI of the replication effect size? Does it exclude the original effect size?
 - Could the discrepancy be explained by sampling variation alone? (Both studies may be sampling from the same distribution)

2. Candidate explanations for replication failure:

 a. Statistical explanation (most common for small original studies):
 - The original effect was a false positive (Type I error)
 - The original effect size was inflated by publication bias and the original study was underpowered
 - Both the original and replication are sampling a real effect with high variance
 Evidence for: p-value just below .05 in original; small original N; effect not replicated across multiple attempts

 b. Methodological differences:
 - The replication differed from the original in a consequential way
 - Which specific differences between original and replication could plausibly moderate the effect?
 - A moderator variable was different between studies (population, context, time, operationalization)
 Evidence for: specific, theoretically justified moderator that differed between studies

 c. Context effects:
 - The effect is real but context-dependent
 - The original study was conducted in a specific context that does not generalize
 - Time effects: the phenomenon may have changed since the original study (technology, cultural change)
 Evidence for: original and replication differ in context in a way consistent with a known moderator

 d. Fraud or QRP in the original:
 - The original data were fabricated or p-hacked
 Evidence for: statistical anomalies in the original (GRIM test, SPRITE test, p-curve analysis)

3. What replication failure does and does not tell us:
 - Does NOT tell us: the original finding was definitely wrong, that the original authors did anything improper
 - DOES tell us: the original finding may not be reliable, the effect size is likely smaller than originally reported, the conditions under which the effect occurs need further investigation

4. Recommended next steps:
 - Conduct a mini meta-analysis of all available replications including your own
 - Design a well-powered study explicitly testing the hypothesized moderator
 - Contact the original authors for a collaborative adversarial replication

Return: discrepancy quantification, ranked candidate explanations with supporting evidence, and recommended next steps. Copy prompt View page Show more ↓ Reproducibility and Open Science Intermediate Prompt 10 
### Replication Study Design 
Design a high-quality replication study of the following original finding.

Original finding: {{original_finding}}
Original study: {{original_study_citation}}
Replication goal: {{goal}} (direct/close replication, conceptual replication, or adversarial replication)

1. Clarify the type of replication:

 Direct / close replication:
 - Reproduces the original procedure as closely as possible
 - Tests whether the original finding holds in a new sample from the same population
 - Most informative about the reliability of the original finding
 - Design challenge: the original paper may not describe the procedure in enough detail

 Conceptual replication:
 - Tests the same theoretical claim using different operationalizations
 - Different measures, different manipulations, different population
 - More informative about the generalizability of the theoretical claim
 - Does not tell you whether the original finding itself replicates

 Adversarial replication:
 - Collaborative replication where original authors and skeptics jointly design the study
 - Both parties agree in advance that the result will be accepted as definitive
 - Most credible form of replication but requires cooperation

2. Obtain the original materials:
 - Contact the original authors for: stimuli, exact measures, randomization procedure, analysis code
 - If unavailable: document what is known from the paper and what was reconstructed
 - Differences between original materials and reconstructed materials must be reported

3. Power the replication:
 - A replication should be powered at 90% (not 80%) to detect the original effect size
 - But: original effect sizes are likely inflated (winner's curse from small original studies)
 - Recommended: power to detect 75% of the original effect size, giving a more realistic target
 - A replication powered at 90% for 75% of the original effect size typically requires 2–4× the original N

4. Replication success criteria (specify in advance):
 - Narrow criterion: same direction AND p < .05 (most commonly used, but problematic)
 - Recommended criterion: the original effect size falls within the replication's 95% CI
 - Bayesian criterion: Bayes factor > 3 in favor of the original hypothesis
 - Pre-specify which criterion will be used

5. Regardless of outcome, report:
 - Original effect size and replication effect size with CIs
 - Whether the replication effect size is significantly smaller than the original (test of heterogeneity)
 - All procedural differences from the original study

Return: replication protocol, power analysis, pre-specified success criteria, and a comparison table of original vs replication design. Copy prompt View page Show more ↓ Reproducibility and Open Science Beginner Prompt 11 
### Research Compendium Builder 
Help me organize my research project into a reproducible research compendium that another researcher could use to replicate my findings.

Project type: {{project_type}}
Tools used: {{tools}} (R, Python, Stata, SPSS, etc.)

1. What is a research compendium:
 A research compendium is a structured collection of files that contains the data, code, and text associated with a research project, organized so that anyone can reproduce the reported results.

2. Recommended directory structure:
```
project_name/
├── README.md # Overview, how to reproduce results
├── DESCRIPTION # Dependencies and environment info
├── data/
│ ├── raw/ # Original, unmodified data (read-only)
│ ├── processed/ # Cleaned, analysis-ready data
│ └── codebook.md # Variable definitions and coding
├── code/ (or R/, scripts/)
│ ├── 00_data_cleaning.R # Data cleaning script
│ ├── 01_analysis.R # Main analysis
│ ├── 02_figures.R # Figure generation
│ └── functions/ # Custom functions used by scripts
├── output/
│ ├── figures/ # Generated figures
│ └── tables/ # Generated tables
├── paper/
│ ├── manuscript.Rmd # Paper manuscript (ideally dynamic)
│ └── references.bib # Bibliography
└── tests/ # Tests for analysis code
```

3. README content requirements:
 - Project title, authors, and contact
 - One-paragraph project description
 - How to install dependencies
 - How to reproduce the main results (step by step)
 - Brief description of each directory
 - Data availability statement
 - License

4. Dependency management:
 - R: use renv to capture package versions. Commit renv.lock.
 - Python: use a requirements.txt or conda environment.yml
 - Document the R/Python version used
 - Ideally: provide a Dockerfile or Binder link for complete environment reproducibility

5. Coding standards for reproducibility:
 - Set random seeds at the top of every script that uses randomization
 - Use relative paths (never absolute paths like /Users/YourName/...)
 - Do not modify raw data files — always create new processed versions
 - Write scripts that run from top to bottom without manual intervention
 - Comment code to explain analytical decisions, not just what the code does

6. Dynamic documents:
 - Ideal: R Markdown or Quarto document that generates the paper by running the analysis inline
 - Results in the paper update automatically when data or code changes
 - Eliminates copy-paste errors between analysis output and paper text

Return: directory structure for my project, README template, dependency setup instructions, and coding standards checklist. Copy prompt View page Show more ↓ 
## Statistical Analysis of Research Data 
11 prompt s Statistical Analysis of Research Data Advanced Chain 01 
### Analysis Plan Chain 
Step 1: Primary analysis specification — specify the primary outcome, primary predictor, and the exact statistical test with its parameters (test type, alpha level, directionality). Specify this before seeing data.
Step 2: Secondary analyses — list all secondary outcomes and exploratory analyses in priority order. Specify multiple comparison correction strategy. Distinguish confirmatory from exploratory analyses clearly.
Step 3: Assumption checks — for each planned analysis, list all statistical assumptions and the procedure to test them. Specify in advance what will be done if each assumption is violated.
Step 4: Missing data plan — specify the expected missing data mechanism, the primary handling strategy, and sensitivity analyses for alternative mechanisms.
Step 5: Power analysis — calculate required sample size for the primary analysis at 80% and 90% power. Account for expected attrition. Run sensitivity analysis showing N required across a range of effect sizes.
Step 6: Subgroup analyses — specify any pre-planned subgroup analyses. State the interaction test that will be used. Explicitly flag all unplanned post-hoc subgroup analyses as exploratory.
Step 7: Write the statistical analysis plan (SAP) — produce a complete, timestamped statistical analysis plan that will be preregistered before data collection begins. Include: primary estimand, all analysis specifications, assumption checks, missing data plan, and planned reporting format. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Advanced Prompt 02 
### Bayesian vs Frequentist Analysis 
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

Return: recommendation with rationale, prior specification for Bayesian approach, sensitivity analysis plan, and code in R (brms) or Python (PyMC). Copy prompt View page Show more ↓ Statistical Analysis of Research Data Beginner Prompt 03 
### Effect Size Interpretation 
Help me calculate, report, and interpret effect sizes for my study.

Study type: {{study_type}}
Statistical results: {{results}}
Field norms: {{field}} (what are typical effect sizes in this field?)

1. Why effect sizes matter more than p-values:
 - A p-value tells you whether an effect exists (given sufficient sample size)
 - An effect size tells you HOW LARGE the effect is
 - With large enough samples, trivially small effects become statistically significant
 - Effect sizes allow comparison across studies and meta-analysis
 - Always report both: the p-value for the inference decision, the effect size for the magnitude interpretation

2. Effect size families and when to use each:

 Standardized mean difference family:
 - Cohen's d: difference between two means divided by pooled standard deviation. For independent groups.
 - Glass's Δ: uses only the control group SD in the denominator. Preferred when SDs differ substantially.
 - Hedges' g: small-sample correction of Cohen's d. Use when n < 20 per group.
 - Interpretation: d = 0.2 (small), 0.5 (medium), 0.8 (large) — but these are field-agnostic; use field norms when available.

 Correlation family:
 - Pearson r: linear association between two continuous variables. r = 0.1 (small), 0.3 (medium), 0.5 (large).
 - R²: proportion of variance explained. Report alongside r.
 - Partial eta squared (η²p): proportion of variance in the outcome explained by the predictor, removing other effects. For ANOVA designs.
 - Omega squared (ω²): less biased estimator of η²p. Prefer over η²p for small samples.

 Odds ratio and relative risk:
 - Odds ratio (OR): for logistic regression and case-control studies. OR = 1 means no effect.
 - Relative risk (RR): for cohort studies with binary outcomes. More interpretable than OR.
 - Number needed to treat (NNT): 1 / absolute risk reduction. Most clinically interpretable.

3. Calculate effect sizes from my results:
 - Apply the appropriate formula to my specific results
 - Include confidence intervals around each effect size estimate

4. Contextualizing the effect size:
 - Compare to typical effect sizes in {{field}}
 - Compare to effect sizes in related prior studies
 - Translate to practical significance: what does an effect of this size mean in the real world?

Return: calculated effect sizes with CIs, interpretation against field benchmarks, and a practical significance statement. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Intermediate Prompt 04 
### Mediation and Moderation Analysis 
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

Return: analysis code, results interpretation, interaction plot, and a methods paragraph. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Intermediate Prompt 05 
### Missing Data Handler 
Analyze the missing data in my study and implement the appropriate handling strategy.

Dataset description: {{dataset}}
Missingness pattern: {{missingness_description}}
Analysis plan: {{analysis_plan}}

1. Classify the missing data mechanism:

 MCAR (Missing Completely At Random):
 - Missingness is unrelated to any variable in the dataset, observed or unobserved
 - Test: Little's MCAR test; compare characteristics of completers vs incomplete cases
 - Consequence: complete case analysis is unbiased but loses power
 - Implication: any missing data method gives unbiased results; simple methods are acceptable

 MAR (Missing At Random):
 - Missingness depends on OBSERVED variables but not on the missing values themselves
 - Example: older participants are more likely to miss a follow-up assessment, and age is recorded
 - Cannot be tested definitively (requires knowledge of unobserved data)
 - Most common practical assumption; required for multiple imputation and maximum likelihood
 - Implication: multiple imputation or FIML is valid; complete case analysis is biased

 MNAR (Missing Not At Random):
 - Missingness depends on the missing values themselves
 - Example: depressed participants are more likely to drop out, and depression is the outcome
 - Most problematic; no standard method fully corrects for MNAR
 - Implication: sensitivity analyses required; results are provisional

2. Evaluate and recommend a handling strategy:

 Complete case analysis (listwise deletion):
 - Valid only under MCAR; biased under MAR
 - Appropriate if: missingness rate < 5% AND MCAR is plausible

 Multiple imputation (MI):
 - Valid under MAR
 - Procedure: impute M datasets (M = 20–100 depending on missingness rate), analyze each separately, pool using Rubin's rules
 - Include all analysis variables, auxiliary variables correlated with outcome or missingness, and the outcome in the imputation model
 - Report: number of imputations, imputation model specification, convergence diagnostics

 Full Information Maximum Likelihood (FIML):
 - Valid under MAR; for structural equation models and mixed models
 - Preferred over MI for SEM and when the analysis model is well-specified

 Sensitivity analysis for MNAR:
 - Pattern-mixture models
 - Selection models
 - Delta adjustment: perturb imputed values systematically and check how much results change

3. Reporting:
 - Report the amount and pattern of missing data for every variable
 - Report the assumed mechanism and justification
 - Report the handling method and software
 - If MI: report number of imputations and imputation model

Return: missing data analysis, mechanism assessment, recommended strategy with implementation code, and reporting text. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Advanced Prompt 06 
### Multiverse Analysis 
Design and execute a multiverse analysis to assess the robustness of my findings across reasonable analytical choices.

Main finding: {{main_finding}}
Analysis pipeline: {{analysis_pipeline}}

A multiverse analysis reports results across all defensible combinations of analytical decisions, rather than cherry-picking one analysis path.

1. Map the decision nodes in my analysis:

 For each step in the pipeline, identify all defensible alternatives:

 Data processing decisions:
 - Outlier exclusion: none, ±2 SD, ±3 SD, Winsorization at 5th/95th percentile
 - Missing data: complete case, single imputation, multiple imputation (5 datasets, 20 datasets)
 - Variable transformation: raw, log, square root, z-score
 - Covariate inclusion: minimal (pre-specified), expanded (additional theoretically relevant covariates)

 Analytical decisions:
 - Model family: OLS, robust regression, mixed model
 - Predictor operationalization: continuous vs dichotomized vs categorical
 - Outcome operationalization: if multiple measures of the same construct, which one is primary?
 - Control variables: which covariates to include

 Sampling decisions:
 - Exclusion criteria: strict application vs lenient (e.g. include vs exclude participants who missed >20% of items)
 - Subpopulation: full sample vs specific age range vs specific subgroup

2. Execute the multiverse:
 - Define all combinations of decisions: this produces the 'multiverse' of analyses
 - Run the primary test across all combinations
 - Extract: effect size, p-value, and confidence interval for each universe

3. Summarize and visualize:
 - Specification curve: plot all effect sizes sorted from smallest to largest, with indicator strips showing which decisions each specification used
 - Proportion of specifications showing a statistically significant effect in the expected direction
 - Proportion of specifications showing a significant effect in the unexpected direction

4. Interpretation:
 - Robust finding: significant and in the expected direction in the large majority of specifications (> 80%)
 - Fragile finding: result depends heavily on specific analytical choices
 - Which specific decisions drive the result? Are those the more or less defensible choices?

5. Reporting:
 - Report the main analysis AND the multiverse results
 - Never use the multiverse to find the significant result — preregister the primary analysis

Return: decision node mapping, analysis code, specification curve plot, robustness interpretation, and reporting text. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Intermediate Prompt 07 
### Peer Review Statistics Critique 
Critically evaluate the statistical methods and reporting in this paper I am reviewing.

Paper abstract/methods/results: {{paper_content}}

Systematically check for the following statistical issues:

1. Study design and causal inference:
 - Does the study design support the causal claims made in the discussion?
 - Are observational data used to support causal conclusions without adequate justification?
 - Is confounding adequately addressed?

2. Sample size and power:
 - Was a power analysis reported? Does the achieved sample size match the power analysis?
 - Is the study adequately powered for the primary outcome? (Effect size and sample size allow calculation)
 - Is the study appropriately cautious about null results given potential underpowering?

3. Multiple comparisons:
 - How many outcomes were tested? Were corrections for multiple comparisons applied?
 - Are results from exploratory analyses clearly labeled as such?
 - Is there evidence of outcome switching (primary outcome appears to have been changed post-hoc)?

4. Effect sizes and practical significance:
 - Are effect sizes reported for all main findings?
 - Are confidence intervals reported?
 - Is the distinction between statistical significance and practical significance made?

5. Specific red flags:
 - p-hacking indicators: p-values clustered just below 0.05, unusual number of 'marginally significant' results (p = .06, .07, .08)
 - HARKing (Hypothesizing After Results are Known): post-hoc hypotheses presented as a priori
 - Selective reporting: were all pre-specified outcomes reported? Are non-significant results reported?
 - Base rate neglect: does the probability of a true finding justify the strength of the conclusion?
 - Overfitting: in predictive models, is there a held-out test set? Is in-sample fit used to claim out-of-sample performance?

6. For each issue identified:
 - Severity: does this issue invalidate the conclusions, weaken them, or require clarification?
 - Recommended author action: specific request for analysis, reporting, or language change
 - Reviewer language: suggest wording appropriate for a peer review

Return: structured peer review critique organized by issue, severity ratings, and specific revision requests. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Intermediate Prompt 08 
### Power Analysis 
Conduct a power analysis to determine the sample size needed for my study.

Study design: {{design}}
Primary statistical test: {{test}}
Effect size: {{effect_size_estimate}} and its source (prior study, meta-analysis, minimum clinically/practically important difference)
Desired power: 0.80 (conventional minimum) or {{desired_power}}
Alpha level: 0.05 (two-tailed) or {{alpha}}

1. Choose the effect size input correctly:

 Priority order for effect size estimation:
 a. Minimum effect size of practical/clinical importance: 'What is the smallest effect that would matter for practice or policy?' Use this if you have domain knowledge.
 b. Meta-analytic estimate: if a meta-analysis of similar studies exists, use its pooled effect size.
 c. Well-powered prior study: a single prior study estimate is noisy; treat it with caution and consider using a smaller estimate.
 d. Cohen's benchmarks (d = 0.2/0.5/0.8): use only as a last resort — these are not field-specific and lead to widely varying conclusions.

 Common mistake: using an effect size from a small pilot study. Small studies overestimate effect sizes (winner's curse). If using a pilot estimate, shrink it by 50%.

2. Run the power analysis:
 - Calculate required N for power = 0.80 and power = 0.90
 - Calculate the minimum detectable effect size at the available N
 - For the recommended design, account for: attrition (inflate N by expected dropout rate), multiple testing (if testing multiple outcomes), clustering (design effect for clustered samples)

3. Sensitivity analysis:
 - Show how required N changes if the true effect size is 50%, 75%, 100%, and 125% of the assumed effect size
 - This illustrates how sensitive the study is to assumptions about effect size

4. Present the power analysis transparently:
 Report: assumed effect size and its source, alpha level, desired power, calculated N, attrition adjustment, final recommended N. State the software/package used.

5. What to do if the required N is not feasible:
 - Use a larger alpha (0.10) only if pre-specified and justified
 - Accept lower power (0.70) only for preliminary studies
 - Narrow the target population to increase homogeneity (reduces within-group variance, increases power)
 - Use a within-subjects design (more efficient than between-subjects)
 - Use a more sensitive primary outcome
 - Abandon and redesign if power cannot exceed 0.50 — an underpowered study is usually not worth running

Return: power analysis results at multiple power levels, sensitivity analysis table, sample size recommendation with attrition adjustment, and methods text. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Intermediate Prompt 09 
### Results Reporting Checklist 
Review my results section for completeness and adherence to best practices in statistical reporting.

Results draft: {{results_draft}}
Analyses used: {{analyses}}

Apply the following reporting standards to every statistical result:

1. Descriptive statistics:
 - Report M and SD (not SEM, which is rarely interpretable) for continuous variables
 - Report frequencies and proportions for categorical variables
 - Report the sample size at each analysis step, accounting for missing data
 - Use APA format for numbers: two decimal places for statistics, three for p-values

2. Inferential statistics — every result must include:
 - The test statistic and its degrees of freedom: t(48) = 2.34 or F(2, 145) = 8.91
 - Exact p-value (not 'p < .05' or 'ns'): p = .023 or p = .412
 - Effect size with 95% confidence interval: d = 0.48 [0.12, 0.84]
 - Do not use asterisks (*, **, ***) as a substitute for reporting exact p-values

3. Common reporting deficiencies to flag:
 - Reporting only p-values without effect sizes
 - Reporting 'p < .05' instead of the exact p-value
 - Reporting SEM instead of SD for descriptive statistics
 - Missing confidence intervals on effect size estimates
 - Reporting results for tests on violated assumptions without acknowledging violations
 - Claiming nonsignificance as evidence of no effect
 - Failing to report results for non-significant outcomes (selective reporting)
 - Rounding to fewer than 2 decimal places for key statistics

4. Specific test reporting standards:

 t-test: t(df) = X.XX, p = .XXX, d = X.XX [95% CI: X.XX, X.XX]
 ANOVA: F(df_effect, df_error) = X.XX, p = .XXX, ω² = .XX [95% CI]
 Chi-squared: χ²(df, N = XX) = X.XX, p = .XXX, φ = .XX
 Correlation: r(df) = .XX, p = .XXX, 95% CI [.XX, .XX]
 Regression coefficient: B = X.XX, SE = X.XX, β = .XX, t(df) = X.XX, p = .XXX
 Mediation indirect effect: ab = X.XX, 95% bootstrap CI [X.XX, X.XX]

5. Tables and figures:
 - Every table must be interpretable standalone with a complete caption
 - Figures must include error bars with a caption specifying what they represent (SD, SE, 95% CI)
 - Raw data or aggregated data sufficient for meta-analysis should be available

Return: annotated results section with specific corrections, reporting deficiencies flagged by line, and a corrected version of the results. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Intermediate Prompt 10 
### Statistical Assumption Checker 
Check the statistical assumptions underlying my planned analyses and recommend how to handle any violations.

Planned analyses: {{analyses}}
Data characteristics: {{data_description}}

For each planned analysis, check the following assumptions:

1. Linear regression assumptions:
 - Linearity: is the relationship between predictors and outcome linear? Check: scatter plot, residual vs fitted plot. Violation: use polynomial terms, transformations, or GAM.
 - Independence: are observations independent? Check: study design. Violation: use clustered standard errors, mixed models, or GEE.
 - Homoscedasticity (constant variance): does residual variance remain constant across fitted values? Check: scale-location plot. Violation: use robust standard errors (HC3) or transform the outcome.
 - Normality of residuals: are residuals approximately normally distributed? Check: Q-Q plot, Shapiro-Wilk (for small n). Note: normality of RESIDUALS is required, not of the outcome itself. Violation: with n > 30, Central Limit Theorem generally protects. For small n: use robust or nonparametric methods.
 - No perfect multicollinearity: Check: VIF. VIF > 10 is problematic. Violation: drop or combine predictors, use ridge regression.

2. ANOVA assumptions:
 - Normality of group distributions (robust with large n)
 - Homogeneity of variance: Levene's test. Violation: Welch's ANOVA does not require equal variances — use by default.
 - Independence: same as above.

3. Chi-squared test assumptions:
 - Expected cell frequencies ≥ 5 in all cells. Violation: use Fisher's exact test, combine categories, or use exact tests.
 - Independence of observations.

4. Logistic regression assumptions:
 - No perfect separation: if a predictor perfectly predicts the outcome, estimates become unstable. Check: examine cross-tabs of predictors with outcome.
 - Linearity of log-odds: continuous predictors should have a linear relationship with the log-odds. Check: Box-Tidwell transformation test.
 - No influential outliers: Check: Cook's distance, leverage statistics.

5. For each violated assumption:
 - State the likely impact on results (conservative? anti-conservative? biased estimates?)
 - Provide the specific code or procedure to implement the appropriate remedy
 - Explain how to report the assumption check and its handling in the paper

Return: assumption checklist per analysis, violation assessment, remedies with implementation guidance, and reporting language. Copy prompt View page Show more ↓ Statistical Analysis of Research Data Beginner Prompt 11 
### Statistical Test Selector 
Help me choose the correct statistical test for my research question and data.

Research question: {{research_question}}
Outcome variable type: {{outcome_type}} (continuous, binary, count, ordinal, time-to-event)
Predictor/grouping variable: {{predictor}} (categorical with N groups, continuous)
Study design: {{design}} (between-subjects, within-subjects, mixed, longitudinal)
Sample size: {{n}}

1. Decision tree for test selection:

 Comparing means or distributions:
 - 2 independent groups, continuous outcome → Independent samples t-test (if normal) or Mann-Whitney U (if not)
 - 2 related groups / repeated measures, continuous outcome → Paired t-test (if normal) or Wilcoxon signed-rank
 - 3+ independent groups, continuous outcome → One-way ANOVA (if normal) or Kruskal-Wallis
 - 3+ groups with covariates → ANCOVA
 - Repeated measures with 3+ time points → Repeated measures ANOVA or linear mixed model

 Associations:
 - Two continuous variables → Pearson correlation (if both normal) or Spearman (if not)
 - Continuous outcome, multiple predictors → Multiple linear regression
 - Binary outcome → Logistic regression
 - Count outcome → Poisson regression (or negative binomial if overdispersed)
 - Time-to-event outcome → Cox proportional hazards regression
 - Ordinal outcome → Ordinal logistic regression

 Categorical associations:
 - Two categorical variables → Chi-squared test (if expected cell counts ≥ 5) or Fisher's exact (if small cells)

2. Check the assumptions of the recommended test:
 - State each assumption
 - Explain how to test whether each assumption is met
 - For each violated assumption: state the appropriate alternative or robust version

3. The model-based alternative:
 For most research questions, a regression model is preferable to a simple test because:
 - It accommodates covariates and confounders
 - It provides effect size estimates with confidence intervals
 - It handles unbalanced designs gracefully
 - It generalizes to more complex designs
 Recommend the regression equivalent of the chosen test.

4. Multiple outcomes:
 If testing more than one outcome, explain:
 - The multiple comparisons problem
 - Whether a family-wise correction (Bonferroni, Holm) or false discovery rate approach is appropriate
 - How to designate a primary outcome to preserve Type I error rate

Return: recommended test and its regression equivalent, assumptions and how to test them, multiple comparisons guidance. Copy prompt View page Show more ↓ 
## Experimental Design and Methodology 
10 prompt s Experimental Design and Methodology Intermediate Prompt 01 
### Confound Identification 
Systematically identify the confounding variables and alternative explanations that threaten the validity of my study.

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

Return: confounder list with bias direction and magnitude assessment, proposed control strategy per confounder, and a residual confounding statement suitable for a limitations section. Copy prompt View page Show more ↓ Experimental Design and Methodology Intermediate Prompt 02 
### Control Condition Designer 
Design the appropriate control condition(s) for my experiment.

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

Return: recommended control condition(s), rationale, what each controls for and does not, and a blinding plan. Copy prompt View page Show more ↓ Experimental Design and Methodology Advanced Chain 03 
### Full Study Design Chain 
Step 1: Sharpen the research question — convert the broad research area into a specific, answerable, PICO-structured research question with clearly operationalized constructs and a defined unit of analysis.
Step 2: Select the study design — identify the strongest feasible design given the research question and available resources. State what causal claims the chosen design can and cannot support.
Step 3: Design the control condition — specify the comparison condition, what it controls for, and what it leaves uncontrolled. Design the blinding procedure.
Step 4: Confound analysis — systematically identify all potential confounders by category. Specify the control strategy for each. Acknowledge what residual confounding remains.
Step 5: Measurement plan — specify the operationalization of each construct. Provide psychometric evidence for each instrument. Identify measurement invariance requirements.
Step 6: Validity audit — audit the design for threats to internal, construct, statistical conclusion, and external validity. Document mitigation strategies.
Step 7: Pre-mortem — assume the study failed and identify the most likely causes. Modify the protocol to prevent or detect each failure mode.
Step 8: Write the methods section — produce a complete methods section covering: participants (eligibility, recruitment, sample size), design, procedure, measures, and analysis plan. Write with sufficient detail for independent replication. Copy prompt View page Show more ↓ Experimental Design and Methodology Intermediate Prompt 04 
### Measurement Instrument Evaluation 
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

Return: instrument evaluation table, reliability and validity evidence summary, measurement invariance plan, and recommendations for any instruments with inadequate psychometric evidence. Copy prompt View page Show more ↓ Experimental Design and Methodology Advanced Prompt 05 
### Pilot Study Design 
Design a pilot study to test the feasibility of my planned main study before committing full resources.

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

Return: pilot objectives checklist, sample size justification, progression criteria, and a pilot study protocol outline. Copy prompt View page Show more ↓ Experimental Design and Methodology Advanced Prompt 06 
### Pre-Mortem Analysis 
Conduct a pre-mortem analysis of my planned study — assume the study has failed and work backwards to identify what went wrong.

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

Return: failure scenario analysis, prevention and detection measures, and a revised protocol checklist. Copy prompt View page Show more ↓ Experimental Design and Methodology Beginner Prompt 07 
### Research Question Sharpener 
Help me sharpen my research question into one that is specific, answerable, and well-scoped.

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
 Write the final research question as a single sentence suitable for the introduction of a paper: 'This study examines whether/how/what [relationship] between [variable X] and [variable Y] in [population] under [conditions].' Copy prompt View page Show more ↓ Experimental Design and Methodology Intermediate Prompt 08 
### Sample Representativeness Audit 
Evaluate the representativeness of my sample and the generalizability of my findings.

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

Return: population hierarchy analysis, WEIRD assessment, volunteer and attrition bias evaluation, and generalizability statement. Copy prompt View page Show more ↓ Experimental Design and Methodology Beginner Prompt 09 
### Study Design Selector 
Help me choose the right study design for my research question.

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

Return: design recommendation with full rationale, validity threat analysis, and a one-paragraph justification suitable for a methods section. Copy prompt View page Show more ↓ Experimental Design and Methodology Intermediate Prompt 10 
### Validity Threat Audit 
Audit my study design for threats to internal and external validity.

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

Return: validity audit table (threat, severity, mitigation, residual risk), overall validity assessment, and limitations section draft. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
