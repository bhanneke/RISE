<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-comparison-evaluation.md -->

# `comparison-evaluation`



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

# Skill: Comparison & Evaluation

You are evaluating whether a replication successfully reproduces the original results.

## Match Quality Categories

### Direction and Significance Match
- Same sign of coefficient AND same significance level
- This is a "successful replication" even if magnitudes differ
- Deviation in magnitude is expected with different data/period

### Direction Only Match
- Same sign but different significance (e.g., *** becomes * or n.s.)
- This is a "partial replication" — the effect exists but is weaker
- Investigate: smaller sample? less variation? different period?

### No Match
- Different sign OR completely insignificant when original was highly significant
- This is a "failed replication" — requires careful analysis
- Do NOT immediately blame the replication — the original might be fragile

## Deviation Analysis Framework

### Expected Deviations (planned)
- Different sample period → expect magnitude differences
- Different winsorization → affects outlier-sensitive estimates
- Different data source → expect level differences, same patterns
- Package differences → minor numerical differences (< 1%)

### Unexpected Deviations (investigate)
- Sign flips → check variable construction, coding errors
- Large magnitude differences (> 50%) → check sample selection
- Significance changes → check SE computation, clustering

## Assumption Testing
For each key assumption:
1. Can it be tested? (parallel trends → yes; exclusion restriction → usually no)
2. Was it tested in the original? How?
3. Does it hold in the replication data?
4. If violated, what does that imply for the results?

## Overall Assessment Criteria
- **Successful**: >80% of primary results replicate in direction and significance
- **Partial**: 50-80% of primary results replicate, or all replicate in direction only
- **Failed**: <50% of primary results replicate

## Robustness Assessment of Original
After all comparisons:
- Are results robust to different data? → Strong external validity
- Are results robust to different specifications? → Strong internal validity
- Do results depend on specific coding choices? → Fragile


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/replication/comparison-evaluation.md</pre>
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/replication-comparison-evaluation/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
