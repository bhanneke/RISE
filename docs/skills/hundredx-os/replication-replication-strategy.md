<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-replication-strategy.md -->

# `replication-strategy`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/replication/replication-strategy.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Skill: Replication Strategy

You are planning the replication of an empirical academic paper.

### Replication Modes

#### Tight Replication
- Use exactly the same data, methods, and specifications
- Goal: reproduce exact numbers (or as close as possible)
- Deviation tolerance: coefficients within 10% or within 1 SE

#### Extended Replication
- Start with tight replication of core results
- Then extend with additional data (more time periods, additional variables)
- Goal: test robustness beyond original sample
- Report both: original replication AND extensions

#### Different Data Replication
- Apply same econometric model to a different dataset
- Goal: test whether findings generalize
- Critical: document all mapping decisions (which variable maps to which)
- Compare patterns (signs, significance) not exact magnitudes

### Data Substitution Logic
When original data is unavailable:
1. Look for the same data source in research DB
2. Look for conceptually similar data (same variable structure, different context)
3. For each substitution, document:
   - What changes (data source, time period, geography, asset class)
   - What stays the same (model, variable definitions, identification)
   - Expected impact on results

### Implementation Search Strategy
1. Check if authors provide replication package (GitHub, journal website, Dataverse)
2. Search for the paper on GitHub (title, DOI, author names)
3. Look for Python packages that implement the specific method
4. Prefer established packages (statsmodels, linearmodels) over custom code
5. For novel methods, check if the originating paper has code

### Risk Assessment
Flag potential issues:
- Weak instruments (F < 10 for IV)
- Small sample sizes (N < 100 for regression)
- Cluster count < 50 for clustered SEs
- Non-convergence risk for GMM/MLE
- Data vintage issues (CRSP corrections, Compustat restated)
