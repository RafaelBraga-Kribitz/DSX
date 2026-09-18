# Bayesian Methods *AI Prompts *

2 Statistician prompts in Bayesian Methods. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in Bayesian Methods 
2 prompts Advanced Single prompt 01 
### Bayesian Hierarchical Model 

Specify and interpret a Bayesian hierarchical (multilevel) model for this data. Data structure: {{data_structure}} (units nested in groups: students in schools, measurements in... 
Prompt text Specify and interpret a Bayesian hierarchical (multilevel) model for this data.

Data structure: {{data_structure}} (units nested in groups: students in schools, measurements in subjects)
Outcome: {{outcome}}
Level-1 predictors: {{l1_predictors}} (measured at the unit level)
Level-2 predictors: {{l2_predictors}} (measured at the group level)
Group variable: {{group_variable}}
Number of groups: {{n_groups}}

1. Why hierarchical models:
 - Observations within groups are not independent (ICC > 0)
 - Using a single-level model underestimates standard errors (overestimates precision)
 - Hierarchical models borrow strength across groups (partial pooling):
 - Complete pooling: ignores group membership (too simple)
 - No pooling: estimates each group separately (too noisy for small groups)
 - Partial pooling: shrinks group estimates toward the overall mean (optimal)

2. Model specification:
 Level 1 (within groups):
 y_ij = alpha_j + beta_j * x_ij + epsilon_ij
 epsilon_ij ~ Normal(0, sigma^2)

 Level 2 (between groups):
 alpha_j ~ Normal(mu_alpha, tau_alpha^2) [random intercepts]
 beta_j ~ Normal(mu_beta, tau_beta^2) [random slopes, if specified]

 Hyperpriors (Bayesian):
 mu_alpha ~ Normal(0, 10)
 tau_alpha ~ HalfNormal(0, 1) [must be positive; HalfNormal is a good weakly informative prior]

3. Intraclass correlation coefficient (ICC):
 ICC = tau^2 / (tau^2 + sigma^2)
 - ICC = 0: no clustering; single-level model is fine
 - ICC = 0.10: 10% of variance is at the group level; standard errors inflated by DEFF = 1 + (m-1) x 0.10
 - ICC > 0.20: strong clustering; hierarchical model is essential

4. Cross-level interactions:
 - Does the effect of x_ij (Level 1) vary with w_j (Level 2)?
 - Include: beta_j = gamma_10 + gamma_11 * w_j + u_1j
 - This is the hallmark of hierarchical modeling: testing whether context moderates individual-level effects

5. Convergence diagnostics (for MCMC estimation):
 - R-hat (Gelman-Rubin): should be < 1.01 for all parameters
 - Effective sample size (ESS): should be > 100 (preferably > 400) for each parameter
 - Trace plots: chains should mix well, with no trends or stuck periods
 - Posterior predictive check: does the model reproduce the observed data distribution?

Return: hierarchical model specification, ICC calculation, cross-level interaction interpretation, and MCMC convergence assessment. Copy prompt Open prompt details Intermediate Single prompt 02 
### Bayesian Hypothesis Testing 

Perform a Bayesian analysis as an alternative or complement to frequentist hypothesis testing. Hypothesis: {{hypothesis}} Data: {{data}} Prior information: {{prior_info}} (liter... 
Prompt text Perform a Bayesian analysis as an alternative or complement to frequentist hypothesis testing.

Hypothesis: {{hypothesis}}
Data: {{data}}
Prior information: {{prior_info}} (literature values, expert knowledge, or 'weakly informative')

1. The Bayesian framework:
 - Prior: P(theta) — your belief about the parameter before seeing the data
 - Likelihood: P(data | theta) — how probable is the data at each value of theta?
 - Posterior: P(theta | data) ∝ P(data | theta) x P(theta)
 - The posterior combines prior belief with the evidence from the data

2. Prior specification:

 Informative prior:
 - Based on previous studies or expert knowledge
 - Example: beta(8, 4) for a success probability believed to be around 0.67
 - Must be documented and justified

 Weakly informative prior:
 - Provides mild regularization without dominating the data
 - Example: Normal(0, 2.5) on logistic regression coefficients (Gelman's recommendation)
 - Prevents extreme estimates while allowing the data to speak

 Non-informative / reference prior:
 - Jeffreys prior: invariant under reparameterization
 - Flat prior: uniform over all values (often improper and not recommended)

3. Bayes factor:
 BF = P(data | H1) / P(data | H0)
 - BF > 10: strong evidence for H1
 - BF 3-10: moderate evidence
 - BF 1-3: weak evidence
 - BF < 1: evidence favors H0
 - BF 1/10 to 1/3: moderate evidence for H0
 - Interpretation: the Bayes factor is how much more probable the data is under H1 vs H0

4. Posterior credible interval:
 - The 95% credible interval contains the true parameter with 95% posterior probability
 - Contrast with frequentist CI: the frequentist CI does NOT have a probability interpretation for the parameter
 - Highest Density Interval (HDI): the shortest interval containing 95% of the posterior mass

5. Decision making under uncertainty:
 - Region of Practical Equivalence (ROPE): define a range of effect sizes that are practically negligible
 - If the posterior is entirely within the ROPE: accept H0 as practically equivalent
 - If the posterior is entirely outside the ROPE: reject H0
 - If the posterior overlaps the ROPE: suspend judgment

Return: posterior distribution, Bayes factor, 95% credible interval, and ROPE-based decision. Copy prompt Open prompt details 
## Recommended Bayesian Methods workflow 
1 
### Bayesian Hierarchical Model 

Start with a focused prompt in Bayesian Methods so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Bayesian Hypothesis Testing 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
