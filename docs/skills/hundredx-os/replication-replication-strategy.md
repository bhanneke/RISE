<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-replication-strategy.md -->

# `replication-strategy`



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

# Skill: Replication Strategy

You are planning the replication of an empirical academic paper.

## Replication Modes

### Tight Replication
- Use exactly the same data, methods, and specifications
- Goal: reproduce exact numbers (or as close as possible)
- Deviation tolerance: coefficients within 10% or within 1 SE

### Extended Replication
- Start with tight replication of core results
- Then extend with additional data (more time periods, additional variables)
- Goal: test robustness beyond original sample
- Report both: original replication AND extensions

### Different Data Replication
- Apply same econometric model to a different dataset
- Goal: test whether findings generalize
- Critical: document all mapping decisions (which variable maps to which)
- Compare patterns (signs, significance) not exact magnitudes

## Data Substitution Logic
When original data is unavailable:
1. Look for the same data source in research DB
2. Look for conceptually similar data (same variable structure, different context)
3. For each substitution, document:
   - What changes (data source, time period, geography, asset class)
   - What stays the same (model, variable definitions, identification)
   - Expected impact on results

## Implementation Search Strategy
1. Check if authors provide replication package (GitHub, journal website, Dataverse)
2. Search for the paper on GitHub (title, DOI, author names)
3. Look for Python packages that implement the specific method
4. Prefer established packages (statsmodels, linearmodels) over custom code
5. For novel methods, check if the originating paper has code

## Risk Assessment
Flag potential issues:
- Weak instruments (F < 10 for IV)
- Small sample sizes (N < 100 for regression)
- Cluster count < 50 for clustered SEs
- Non-convergence risk for GMM/MLE
- Data vintage issues (CRSP corrections, Compustat restated)


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/replication/replication-strategy.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>replication</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>replication</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/replication-replication-strategy/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
