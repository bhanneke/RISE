<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/causal-inference-natural-experiments.md -->

# `natural-experiments`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

# Natural Experiments: Taxonomy and Evaluation

## What Makes a Natural Experiment

An exogenous event, institutional rule, or policy change assigns units to
treatments as-if randomly, without researcher control. Credibility depends on:
- Clear identification of the source of exogenous variation
- Plausible independence from potential outcomes
- Institutional knowledge of the assignment mechanism
- Empirical support (balance tests, placebo tests, density tests)

## Categories

| Category | Source of Variation | Key Concern |
|----------|-------------------|-------------|
| Policy changes | Cross-jurisdictional or over-time law/regulation variation | Policy endogeneity, anticipation effects |
| Geographic discontinuities | Borders, boundaries, spatial features | Endogenous sorting near boundaries |
| Weather/environmental | Rainfall, temperature, natural disasters | Multiple channels (exclusion restriction) |
| Lotteries | Draft, school admission, housing voucher | Imperfect compliance (fuzzy design, LATE) |
| Institutional assignment | Judge/examiner, date cutoffs, queue position | Conditional random assignment validity |
| Historical variation | Colonial institutions, historical infrastructure | Long causal chains, exclusion restriction |

## Evaluating Natural Experiments

### Internal Validity
- Is the variation truly exogenous? Can agents sort or select?
- Does the identifying assumption have testable implications?
- Are there confounding contemporaneous changes?
- Is the treatment well-defined or a bundle of changes?

### External Validity
- Does the design estimate a LATE for a specific subpopulation?
- How representative is the affected population?
- Does the setting generalize to other contexts?

### Reporting Standards
1. Clearly state the source of identifying variation.
2. Present the first stage (if IV) or treatment-control comparison.
3. Show balance on pre-treatment covariates.
4. Present reduced-form evidence.
5. Discuss threats explicitly.
6. Conduct robustness and placebo analyses.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/causal-inference/natural-experiments.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>analysis</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>data-analysis</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/causal-inference-natural-experiments/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
