<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/causal-inference-natural-experiments.md -->

# `natural-experiments`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/causal-inference/natural-experiments.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Natural Experiments: Taxonomy and Evaluation

### What Makes a Natural Experiment

An exogenous event, institutional rule, or policy change assigns units to
treatments as-if randomly, without researcher control. Credibility depends on:
- Clear identification of the source of exogenous variation
- Plausible independence from potential outcomes
- Institutional knowledge of the assignment mechanism
- Empirical support (balance tests, placebo tests, density tests)

### Categories

| Category | Source of Variation | Key Concern |
|----------|-------------------|-------------|
| Policy changes | Cross-jurisdictional or over-time law/regulation variation | Policy endogeneity, anticipation effects |
| Geographic discontinuities | Borders, boundaries, spatial features | Endogenous sorting near boundaries |
| Weather/environmental | Rainfall, temperature, natural disasters | Multiple channels (exclusion restriction) |
| Lotteries | Draft, school admission, housing voucher | Imperfect compliance (fuzzy design, LATE) |
| Institutional assignment | Judge/examiner, date cutoffs, queue position | Conditional random assignment validity |
| Historical variation | Colonial institutions, historical infrastructure | Long causal chains, exclusion restriction |

### Evaluating Natural Experiments

#### Internal Validity
- Is the variation truly exogenous? Can agents sort or select?
- Does the identifying assumption have testable implications?
- Are there confounding contemporaneous changes?
- Is the treatment well-defined or a bundle of changes?

#### External Validity
- Does the design estimate a LATE for a specific subpopulation?
- How representative is the affected population?
- Does the setting generalize to other contexts?

#### Reporting Standards
1. Clearly state the source of identifying variation.
2. Present the first stage (if IV) or treatment-control comparison.
3. Show balance on pre-treatment covariates.
4. Present reduced-form evidence.
5. Discuss threats explicitly.
6. Conduct robustness and placebo analyses.
