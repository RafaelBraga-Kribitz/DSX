# Reproducibility and Open Science *AI Prompts *

11 Research Scientist prompts in Reproducibility and Open Science. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 10 single prompts · 1 chain. 

## AI prompts in Reproducibility and Open Science 
11 prompts Intermediate Single prompt 01 
### Code Review for Reproducibility 

Review my analysis code for reproducibility and identify problems that would prevent another researcher from replicating my results. Code: {{analysis_code}} Language: {{language... 
Prompt text Review my analysis code for reproducibility and identify problems that would prevent another researcher from replicating my results.

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

Return: annotated code review, corrected code, and a reproducibility score (0–100) with justification. Copy prompt Open prompt details Intermediate Single prompt 02 
### Data Sharing Plan 

Help me create a data sharing plan that maximizes openness while addressing legal, ethical, and practical constraints. Data type: {{data_type}} Participant population: {{populat... 
Prompt text Help me create a data sharing plan that maximizes openness while addressing legal, ethical, and practical constraints.

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

Return: data sharing recommendation, de-identification procedure, repository selection, metadata checklist, and data management plan text for the funder. Copy prompt Open prompt details Advanced Single prompt 03 
### Meta-Analysis Readiness 

Prepare my study to maximize its contribution to future meta-analyses of this research area. Study details: {{study_details}} Field: {{field}} Meta-analyses synthesize evidence... 
Prompt text Prepare my study to maximize its contribution to future meta-analyses of this research area.

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

Return: meta-analysis reporting checklist, summary statistics table template, CONSORT/STROBE/PRISMA compliance check, and data sharing format recommendation. Copy prompt Open prompt details Intermediate Single prompt 04 
### Open Materials Preparation 

Prepare my study materials for open sharing so other researchers can replicate and build on my work. Materials to share: {{materials_list}} (stimuli, surveys, experimental scrip... 
Prompt text Prepare my study materials for open sharing so other researchers can replicate and build on my work.

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

Return: materials inventory checklist, documentation template per material type, license recommendations, and README template. Copy prompt Open prompt details Advanced Chain 05 
### Open Science Practices Chain 

Step 1: Preregistration — write and submit a complete preregistration before data collection begins. Include: research question, hypotheses, design, measures, sample size justif... 
Prompt text Step 1: Preregistration — write and submit a complete preregistration before data collection begins. Include: research question, hypotheses, design, measures, sample size justification, primary analysis plan, secondary analyses, assumption checks, missing data plan, and exclusion criteria. Timestamp it.
Step 2: Registered Report submission (if applicable) — if the target journal offers Registered Reports, format the Stage 1 submission. Submit before data collection for an In-Principle Acceptance.
Step 3: Research compendium setup — initialize the project directory structure with separate raw data, processed data, code, and output folders. Set up version control (Git). Record the computing environment (renv, requirements.txt). Write the README.
Step 4: Data collection and contemporaneous documentation — document all protocol deviations, unexpected events, and unplanned decisions in a study log as they occur. Do not rely on memory after the fact.
Step 5: Analysis — run the pre-specified analyses exactly as registered. Any deviation from the plan must be explicitly noted with a reason. Additional exploratory analyses may be conducted but must be clearly labeled as unregistered.
Step 6: Open materials, data, and code — prepare all study materials for sharing. De-identify the data. Finalize the analysis code so it runs from raw data to paper tables and figures with a single command. Deposit to a repository with a DOI.
Step 7: Transparent reporting — write the paper with transparent reporting: report all pre-registered outcomes (not just significant ones), label exploratory analyses, include the preregistration DOI, materials DOI, and data DOI. Complete the relevant reporting checklist (CONSORT, STROBE, etc.). Copy prompt Open prompt details Advanced Single prompt 06 
### P-hacking and HARKing Audit 

Audit my analysis and reporting for practices that inflate false positive rates, even unintentionally. Analysis history: {{analysis_history}} Final results: {{results}} Research... 
Prompt text Audit my analysis and reporting for practices that inflate false positive rates, even unintentionally.

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

Return: audit findings per practice, severity assessment, correction recommendations, and a transparency statement suitable for inclusion in the paper. Copy prompt Open prompt details Beginner Single prompt 07 
### Preregistration Writer 

Help me write a complete preregistration for my study. Study overview: {{study_overview}} Platform: {{platform}} (OSF, AsPredicted, ClinicalTrials.gov, PROSPERO) Preregistration... 
Prompt text Help me write a complete preregistration for my study.

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

Return: complete preregistration text formatted for the chosen platform, with each section written at the level of specificity required to make it a meaningful constraint. Copy prompt Open prompt details Advanced Single prompt 08 
### Registered Report Design 

Help me structure my study as a Registered Report to eliminate publication bias for my research. Study overview: {{study_overview}} Target journal: {{journal}} 1. What is a Regi... 
Prompt text Help me structure my study as a Registered Report to eliminate publication bias for my research.

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

Return: Stage 1 manuscript outline, analysis plan formatted for RR review, and guidance on handling anticipated deviations. Copy prompt Open prompt details Advanced Single prompt 09 
### Replication Failure Diagnosis 

My replication attempt did not reproduce the original finding. Help me diagnose why and what conclusions to draw. Original finding: {{original_finding}} (effect size: {{original... 
Prompt text My replication attempt did not reproduce the original finding. Help me diagnose why and what conclusions to draw.

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

Return: discrepancy quantification, ranked candidate explanations with supporting evidence, and recommended next steps. Copy prompt Open prompt details Intermediate Single prompt 10 
### Replication Study Design 

Design a high-quality replication study of the following original finding. Original finding: {{original_finding}} Original study: {{original_study_citation}} Replication goal: {... 
Prompt text Design a high-quality replication study of the following original finding.

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

Return: replication protocol, power analysis, pre-specified success criteria, and a comparison table of original vs replication design. Copy prompt Open prompt details Beginner Single prompt 11 
### Research Compendium Builder 

Help me organize my research project into a reproducible research compendium that another researcher could use to replicate my findings. Project type: {{project_type}} Tools use... 
Prompt text Help me organize my research project into a reproducible research compendium that another researcher could use to replicate my findings.

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

Return: directory structure for my project, README template, dependency setup instructions, and coding standards checklist. Copy prompt Open prompt details 
## Recommended Reproducibility and Open Science workflow 
1 
### Code Review for Reproducibility 

Start with a focused prompt in Reproducibility and Open Science so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Sharing Plan 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Meta-Analysis Readiness 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Open Materials Preparation 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
