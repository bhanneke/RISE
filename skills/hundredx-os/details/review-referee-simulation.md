# Referee Simulation

## Purpose

This skill describes how to simulate a tough but fair referee report for an academic
paper. The goal is to anticipate what a knowledgeable, critical reviewer would say,
so the author can address weaknesses before submission. A good simulated referee
is honest, specific, and constructive.

---

## Step 0: Scope Check

Before writing anything, identify the paper's **stated scope**:

1. Read the abstract, introduction (especially the contribution paragraph), and the
   Research Strategy Document (RSD) if available.
2. Write down: (a) the core question the paper claims to answer, (b) the stated
   contribution, and (c) the identification strategy or methodology.

Throughout the review, **classify every concern** as one of:

- **In-scope**: threatens the paper's stated contribution. For example, the
  identification strategy is flawed for the question the paper actually asks, or
  the evidence does not support the claim the paper actually makes.
- **Out-of-scope**: suggests a different or additional paper. For example, "you
  should also study X" or "this methodology could be applied to Y" when X and Y are
  not part of the stated contribution.

**Rules:**
- Only in-scope concerns can be MAJOR. An out-of-scope concern is MINOR by default,
  unless ignoring it would make the in-scope contribution actively misleading (e.g.,
  a known confound that the paper fails to even mention).
- Do not penalise the paper for not being a different paper. The question is whether
  the paper answers **its own** question convincingly, not whether it answers the
  question you wish it had asked.
- Flag the streetlight effect: is the paper studying what is easy to measure rather
  than what matters? Does it link the phenomenon to an archetypal economic problem,
  or just document "this happened"? Ask explicitly: "Is the answer derivative?" — i.e.
  could a reader have predicted this finding without new evidence?
- Flag scope miscalibration: is the paper trying to answer a question that is too
  narrow to be interesting, or too diffuse to be answered convincingly?
- Flag solution-driven research: is the paper pushing a particular method or theory
  and then searching for a problem to apply it to, rather than starting from a
  compelling economic question?

---

## Step 1: Prove You Understood the Paper

Start the report with a one-paragraph summary of the paper. This serves two functions:
it demonstrates that you engaged seriously with the work, and it reveals whether the
paper communicates its contribution clearly. If the summary is hard to write, the
paper likely has a clarity problem.

The summary should cover:
- The research question the paper asks
- The method used to answer it (data, identification strategy, or theoretical approach)
- The main finding, stated quantitatively where possible
- The claimed contribution relative to existing work

**Do not** pad the summary with background or motivation. A referee has read the paper.
The summary should be tight -- four to six sentences.

**Example:**
"This paper estimates the effect of DAO governance participation on protocol token
returns using a difference-in-differences design around governance proposal votes
on Ethereum. The authors exploit variation in voting deadlines across 47 protocols
to construct treatment and control windows. They find that tokens of protocols
with active governance earn 2.3 percentage points higher weekly returns in the
two weeks following contested votes, relative to protocols without active votes in
the same period. The paper argues this reflects an information revelation channel
rather than a governance premium."

---

## Step 2: Evaluate the Contribution

Ask: Is this genuinely new?

- Does the paper clearly state what it adds beyond existing work?
- Are the 3-5 closest prior papers identified and differentiated from?
- Is the contribution incremental (same method, slightly different setting) or
  substantive (new fact, new mechanism, new identification)?
- Would a specialist in this area, upon reading the abstract, think "I didn't
  know that" or "I already knew that"?

**Specific questions to address:**
- What is the single most important thing the reader learns from this paper?
- Could this finding have been anticipated from existing work without new evidence?
- Is the contribution primarily empirical (new fact), methodological (new tool),
  or theoretical (new framework)?

If the contribution is unclear or incremental, say so directly. This is a major
concern, not a minor one.

---

## Step 3: Evaluate Identification

Ask: Is the causal claim credible?

This is typically the most important section of a referee report for empirical papers.
Evaluate the identification strategy against its own standards:

### For difference-in-differences:
- Is the parallel trends assumption plausible? Is evidence provided?
- Are pre-treatment trends shown in an event study plot?
- Is there a concern about staggered treatment timing? If so, is an appropriate
  estimator used?
- Could there be anticipation effects?

### For instrumental variables:
- Is the instrument relevant? (Report the first-stage F-statistic.)
- Is the exclusion restriction plausible? Can the instrument affect the outcome
  through channels other than the endogenous variable?
- Who are the compliers? Is the LATE interpretable?

### For regression discontinuity:
- Is there evidence of manipulation at the cutoff?
- Are covariates balanced at the cutoff?
- Is the result robust to bandwidth choice?

### For randomized experiments:
- Was randomization properly implemented? Is there balance?
- Is there selective attrition?
- Are there spillover concerns?

### For all designs:
- What is the most damaging alternative explanation? Has the paper addressed it?
- If a hostile referee wanted to dismiss the result, what would they argue?

---

## Step 4: Evaluate Evidence-Claim Alignment

Check whether the evidence actually supports the claims made:

- Does the paper claim causation when it has only established correlation?
- Are effect sizes interpreted correctly and in economically meaningful units?
- Are robustness checks addressing the most important threats, or just easy ones?
- Does the paper overclaim in the abstract or conclusion relative to what the
  evidence actually shows?
- Are heterogeneity results pre-specified or the result of data mining?
- Do the mechanism tests actually identify mechanisms, or just document correlations
  with other outcomes?

---

## Step 5: Check for Common Econometric Issues

- **Standard errors:** Are they clustered at the right level? Is the number of
  clusters sufficient (at least 30-50)?
- **Multiple testing:** If the paper tests many hypotheses, is there a correction
  for multiple comparisons?
- **Sample selection:** Is the sample representative of the population the paper
  claims to study?
- **Measurement error:** Could measurement error in key variables bias results?
  In which direction?
- **Functional form:** Are results sensitive to log vs. level specifications?
  Linear vs. nonlinear models?
- **Outliers:** Could a few extreme observations drive the results?
- **Power:** Is the study adequately powered to detect effects of the size claimed?
  A null result with wide confidence intervals is uninformative.

---

## Step 6: Separate Major from Minor Concerns

### Major concerns

These are issues that, if unresolved, would prevent publication:

- The identification strategy has a fundamental flaw
- The contribution is not clearly differentiated from existing work
- The evidence does not support the main claim
- There is a data or coding error that affects the main result
- The paper tries to answer a question that the available data cannot address

### Minor concerns

These are issues that should be fixed but do not threaten the paper's core contribution:

- Missing robustness checks that the author can easily run
- Presentation issues (unclear writing, poor table formatting)
- Missing references that should be cited
- Minor inconsistencies in notation or variable definitions
- Suggestions for additional analyses that would strengthen (but are not required for)
  the paper

**Always distinguish these categories explicitly.** A report that lists 15 concerns
without prioritizing them is unhelpful. The author needs to know what must be fixed
versus what would be nice to fix.

---

## Step 7: Be Constructive

For every criticism, suggest a specific fix when possible:

| Bad | Good |
|-----|------|
| "The identification is weak" | "The parallel trends assumption would be more convincing with an event study plot showing lead coefficients. Additionally, a placebo test using [specific outcome] as a falsification check would address the concern that [specific confounder] drives the result." |
| "The writing is unclear" | "The contribution paragraph (p. 3) lists four contributions but does not signal which is the main one. Restructuring to lead with the primary contribution and subordinating the others would sharpen the paper's message." |
| "More robustness is needed" | "The result should be shown to be robust to (1) dropping the top and bottom 1% of [variable], (2) using [alternative clustering level], and (3) restricting the sample to [relevant subsample]." |

---

## Step 8: Assign a Rating

Use the following scale, applying the standards of the target outlet:

| Rating | Meaning |
|--------|---------|
| **Strong reject** | Fundamental problems that cannot be fixed. Wrong question, wrong method for the question, or a contribution that does not exist. |
| **Reject** | Significant problems that would require a substantially different paper to address. Major identification concerns, unclear contribution, or evidence that does not support claims. Potentially publishable elsewhere with major revisions. |
| **Weak reject** | The paper has merit but important concerns remain. Could be publishable at this outlet with substantial revisions, but it is not certain the revisions would be successful. |
| **Weak accept** | The paper makes a contribution and the identification is broadly credible, but some concerns need to be addressed. Revisions are likely to be successful. |
| **Accept** | Strong paper with minor issues only. Contribution is clear, identification is convincing, evidence supports claims. |
| **Strong accept** | Exceptional paper. Important question, convincing evidence, clear contribution. Publishable as-is or with trivial changes. Rare. |

### Consider the target outlet's standards

- **Top-5 journals (AER, Econometrica, QJE, JPE, REStud):** The bar is high. The
  question must be first-order important, the identification must be near-airtight,
  and the contribution must be substantial and clearly differentiated.
- **Top field journals (JFE, RFS, JME for finance; JDE, JHR for development/labor):**
  The question should be important to the field. Execution and identification matter
  more than novelty.
- **Good field journals and general interest outlets:** Solid execution of established
  methods on relevant questions. Clear contribution within the subfield.
- **Working paper / pre-submission review:** Apply the standards of the intended
  target outlet, but also flag whether the paper is aimed at the right outlet.

---

## Output Format

Structure the referee report as follows:

```
SUMMARY
[One paragraph proving you understood the paper]

MAJOR CONCERNS
1. [Concern title]
   [Specific description of the problem]
   [Suggested fix]

2. [Concern title]
   ...

MINOR CONCERNS
1. [Concern]
2. [Concern]
...

OVERALL ASSESSMENT
[Rating: strong reject / reject / weak reject / weak accept / accept / strong accept]
[One paragraph justifying the rating and summarizing the key issue(s) that
determine whether this paper is publishable at the target outlet]
```
