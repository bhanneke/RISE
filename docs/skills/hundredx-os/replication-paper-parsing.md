<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-paper-parsing.md -->

# `paper-parsing`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/replication/paper-parsing.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Skill: Paper Parsing

You are extracting structured content from an academic paper. Follow these rules:

### Section Identification
- Look for numbered sections (1., 2., 1.1, etc.) or named headings
- Common structure: Abstract, Introduction, Literature Review, Data, Methodology, Results, Discussion, Conclusion
- Some papers use "Empirical Strategy" or "Identification" instead of "Methodology"
- Appendices are separate sections — capture them

### Table Extraction
- Academic tables have: number (Table 1), caption, column headers, data rows, notes
- Notes typically contain: SE format ("Standard errors in parentheses"), significance stars, sample info
- Regression tables: dependent variable in column header, regressors in rows
- Summary statistics tables: Variable, N, Mean, SD, Min, Max

### Equation Extraction
- Look for numbered equations: (1), (2), etc.
- Convert to LaTeX notation: subscripts, superscripts, Greek letters
- Capture the context: what the equation represents

### Figure Identification
- Capture figure number, caption, and what the figure depicts
- For time series plots: note the axes and time range
- For scatter plots: note the variables
- You cannot see the actual figure content from text — describe based on caption and surrounding text

### Reference Extraction
- Extract from the bibliography/references section
- Format: Author(s) (Year). Title. Journal, Volume(Issue), Pages.
- Note DOIs when present
