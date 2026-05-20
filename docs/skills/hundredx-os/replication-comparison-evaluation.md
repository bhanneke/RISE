<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-comparison-evaluation.md -->

# `comparison-evaluation`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/replication/comparison-evaluation.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Skill: Comparison & Evaluation

You are evaluating whether a replication successfully reproduces the original results.

### Match Quality Categories

#### Direction and Significance Match
- Same sign of coefficient AND same significance level
- This is a "successful replication" even if magnitudes differ
- Deviation in magnitude is expected with different data/period

#### Direction Only Match
- Same sign but different significance (e.g., *** becomes * or n.s.)
- This is a "partial replication" — the effect exists but is weaker
- Investigate: smaller sample? less variation? different period?

#### No Match
- Different sign OR completely insignificant when original was highly significant
- This is a "failed replication" — requires careful analysis
- Do NOT immediately blame the replication — the original might be fragile

### Deviation Analysis Framework

#### Expected Deviations (planned)
- Different sample period → expect magnitude differences
- Different winsorization → affects outlier-sensitive estimates
- Different data source → expect level differences, same patterns
- Package differences → minor numerical differences (< 1%)

#### Unexpected Deviations (investigate)
- Sign flips → check variable construction, coding errors
- Large magnitude differences (> 50%) → check sample selection
- Significance changes → check SE computation, clustering

### Assumption Testing
For each key assumption:
1. Can it be tested? (parallel trends → yes; exclusion restriction → usually no)
2. Was it tested in the original? How?
3. Does it hold in the replication data?
4. If violated, what does that imply for the results?

### Overall Assessment Criteria
- **Successful**: >80% of primary results replicate in direction and significance
- **Partial**: 50-80% of primary results replicate, or all replicate in direction only
- **Failed**: <50% of primary results replicate

### Robustness Assessment of Original
After all comparisons:
- Are results robust to different data? → Strong external validity
- Are results robust to different specifications? → Strong internal validity
- Do results depend on specific coding choices? → Fragile
