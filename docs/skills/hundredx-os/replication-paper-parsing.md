<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-paper-parsing.md -->

# `paper-parsing`



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

# Skill: Paper Parsing

You are extracting structured content from an academic paper. Follow these rules:

## Section Identification
- Look for numbered sections (1., 2., 1.1, etc.) or named headings
- Common structure: Abstract, Introduction, Literature Review, Data, Methodology, Results, Discussion, Conclusion
- Some papers use "Empirical Strategy" or "Identification" instead of "Methodology"
- Appendices are separate sections — capture them

## Table Extraction
- Academic tables have: number (Table 1), caption, column headers, data rows, notes
- Notes typically contain: SE format ("Standard errors in parentheses"), significance stars, sample info
- Regression tables: dependent variable in column header, regressors in rows
- Summary statistics tables: Variable, N, Mean, SD, Min, Max

## Equation Extraction
- Look for numbered equations: (1), (2), etc.
- Convert to LaTeX notation: subscripts, superscripts, Greek letters
- Capture the context: what the equation represents

## Figure Identification
- Capture figure number, caption, and what the figure depicts
- For time series plots: note the axes and time range
- For scatter plots: note the variables
- You cannot see the actual figure content from text — describe based on caption and surrounding text

## Reference Extraction
- Extract from the bibliography/references section
- Format: Author(s) (Year). Title. Journal, Volume(Issue), Pages.
- Note DOIs when present


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/replication/paper-parsing.md</pre>
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/replication-paper-parsing/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
