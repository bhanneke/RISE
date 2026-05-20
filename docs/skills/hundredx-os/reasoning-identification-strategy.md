<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/reasoning-identification-strategy.md -->

# `identification-strategy`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/reasoning/identification-strategy.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Identification Strategy Evaluation

### Purpose

Empirical credibility in economics rests on identification -- how convincingly the paper isolates the causal effect it claims to measure. This procedure provides a systematic framework for evaluating whether an identification strategy is convincing, what its vulnerabilities are, and what tests would strengthen it.

---

### Step 1: Identify the Estimand

Before evaluating the strategy, be precise about what the paper is trying to estimate:

- **ATE** (Average Treatment Effect): Effect across the entire population. Requires strong assumptions.
- **ATT** (Average Treatment Effect on the Treated): Effect on those who actually received treatment. Weaker assumptions but narrower claim.
- **LATE** (Local Average Treatment Effect): Effect on compliers in an IV framework. Valid but applies to a specific subpopulation.
- **Structural parameter**: A deep parameter (elasticity, preference parameter) estimated via a model. Depends on model assumptions.

**Key question**: Does the paper clearly state what it estimates? If the paper uses IV but discusses results as if they are ATE, flag this.

---

### Step 2: Classify the Framework

#### 2a. Difference-in-Differences (DiD)

**Required assumptions:**
- Parallel trends: treatment and control groups would have followed the same trend absent treatment
- No anticipation: units don't change behavior before treatment
- SUTVA: treatment of one unit doesn't affect outcomes of other units
- Stable composition: the groups don't change composition around treatment

**Tests to check:**
- [ ] Pre-treatment trends plotted and discussed (not just p-values)
- [ ] Event study specification showing lead coefficients near zero
- [ ] Robustness to different pre-treatment windows
- [ ] Placebo tests with fake treatment dates
- [ ] Treatment doesn't correlate with pre-existing trends
- [ ] If staggered treatment: appropriate estimator used (not TWFE with heterogeneous effects)

**Common failures:**
- Showing parallel pre-trends in levels but estimating in logs (or vice versa)
- Ignoring that parallel trends can hold mechanically in short pre-periods
- Using TWFE with staggered adoption without discussing negative weights
- Not addressing potential spillovers to control group

#### 2b. Instrumental Variables (IV)

**Required assumptions:**
- Relevance: instrument predicts the endogenous variable (first stage)
- Exclusion restriction: instrument affects outcome ONLY through the endogenous variable
- Independence: instrument is as-good-as-randomly assigned (conditional on controls)
- Monotonicity: instrument affects treatment in the same direction for all units (for LATE interpretation)

**Tests to check:**
- [ ] First-stage F-statistic reported (>10 for single instrument; use effective F for multiple)
- [ ] Exclusion restriction defended with economic reasoning (not just asserted)
- [ ] Reduced form shown (does instrument predict outcome directly?)
- [ ] Balance tests: instrument uncorrelated with observables
- [ ] Overidentification test if multiple instruments (but understand its limitations)
- [ ] Discussion of who the compliers are (LATE interpretation)

**Common failures:**
- Weak instruments dressed up with robust standard errors
- Exclusion restriction "defended" by saying "we assume it holds"
- Multiple instruments without discussing why they're all valid
- Ignoring that instrument may affect outcome through channels other than claimed

#### 2c. Regression Discontinuity (RD)

**Required assumptions:**
- Continuity: potential outcomes are continuous at the cutoff
- No manipulation: units cannot precisely control the running variable
- Local randomization: units just above and below cutoff are comparable

**Tests to check:**
- [ ] McCrary/density test for manipulation of running variable
- [ ] Balance of covariates at the cutoff
- [ ] Sensitivity to bandwidth choice (show results for multiple bandwidths)
- [ ] Correct polynomial order (avoid overfitting with high-order polynomials)
- [ ] Visualization: raw data plotted with the discontinuity visible
- [ ] If fuzzy RD: first stage at cutoff shown and discussed

**Common failures:**
- Using global polynomial fits instead of local linear
- Not showing the raw data -- only showing fitted lines
- Bandwidth chosen to maximize significance
- Ignoring that RD estimate is valid only at the cutoff

#### 2d. Randomized Controlled Trial (RCT)

**Required assumptions:**
- Random assignment actually achieved
- No selective attrition
- No spillovers between treatment and control
- SUTVA holds

**Tests to check:**
- [ ] Balance table across treatment and control
- [ ] Attrition rates by group and analysis of attrition bias
- [ ] ITT and LATE both reported
- [ ] Pre-registration referenced (or justified why not)
- [ ] Power calculations (ex ante or ex post)
- [ ] Multiple hypothesis testing correction if many outcomes

#### 2e. Structural Estimation

**Required evaluation criteria:**
- [ ] Model assumptions clearly stated and discussed
- [ ] Which parameters are identified and which are calibrated?
- [ ] Goodness of fit: does the model match key data moments?
- [ ] Counterfactual exercises: are they sensitive to functional form?
- [ ] Model validation: does the model predict out-of-sample moments?

---

### Step 3: Evaluate Threats to Identification

For each framework, enumerate:

1. **What could violate the key assumption?** Be specific: "Firms near the treatment cutoff might have lobbied for the policy" not "there might be endogeneity."

2. **What is the most damaging alternative explanation?** If a hostile referee wanted to dismiss the paper, what would they argue?

3. **Has the paper addressed this threat?** Three levels:
   - **Tested and survived**: The paper runs a formal test and the threat is ruled out
   - **Discussed with reasoning**: The paper argues why the threat is unlikely, with evidence
   - **Acknowledged but unresolved**: The paper mentions it but doesn't address it
   - **Not discussed**: The paper ignores this threat entirely

---

### Step 4: Rate Threats

For each unaddressed or partially addressed threat:

| Threat | Plausibility | Damage if true | Addressable? | Suggested test |
|--------|-------------|---------------|-------------|----------------|

- **Plausibility**: How likely is this threat to actually matter? (low/medium/high)
- **Damage if true**: If this threat is real, does it invalidate the result, attenuate it, or change interpretation? (fatal/serious/minor)
- **Addressable**: Can the author address this with available data/methods? (yes/partially/no)
- **Suggested test**: What specific test or analysis would address this threat?

---

### Step 5: Overall Credibility Assessment

Synthesize into a single assessment:

- **Credible**: Identification strategy is standard for the question, key assumptions are defensible, main threats are tested. Reasonable referee would accept.
- **Credible with caveats**: Strategy is sound but some threats remain. Paper should acknowledge limitations clearly. Acceptable at most outlets with proper discussion.
- **Questionable**: Key assumption is hard to defend or major threat is unaddressed. Paper needs additional analysis to be convincing.
- **Not credible**: Fundamental identification problem that cannot be fixed with additional tests. Paper needs a different approach.

---

### Decision Rules for Referee Perspective

- A paper does NOT need to address every conceivable threat. It needs to address the most plausible and damaging ones.
- A transparently discussed limitation is far better than an ignored one. Flag papers that oversell their identification.
- The standard varies by outlet: top-5 journals demand near-airtight identification; field journals accept reasonable strategies with acknowledged limitations.
- Novel identification strategies get more scrutiny than established ones. If using a new approach, the paper must convince the reader it's valid.
