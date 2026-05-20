<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/latex-tables.md -->

# `latex-tables`

Generate publication-ready regression tables in LaTeX.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/writing/latex-tables/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/latex-tables/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/writing/latex-tables/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## LaTeX Tables

### Purpose

This skill creates clean, publication-ready tables in LaTeX for regression results and summary statistics, using standard academic formatting.

### When to Use

- Converting model output into LaTeX tables
- Standardizing table style across a paper
- Adding notes, significance stars, and labels

### Instructions

Follow these steps to complete the task:

#### Step 1: Understand the Context

Before generating any code, ask the user:

- What type of table is needed (regression, summary stats, balance)?
- What software produced the results (Stata, R, Python)?
- Which formatting style is required (journal-specific, AEA, etc.)?

#### Step 2: Generate the Output

Based on the context, generate LaTeX code that:

1. **Uses `booktabs`** for clean horizontal rules
2. **Includes labels and captions** for referencing in the paper
3. **Adds notes** for standard errors and significance
4. **Aligns numeric columns** for readability

#### Step 3: Verify and Explain

After generating output:

- Explain how to compile the table
- Highlight any assumptions in the formatting
- Suggest refinements for journal submission

### Example Prompts

- "Create a regression table with three models in LaTeX"
- "Format summary statistics with mean and sd columns"
- "Add significance stars and standard error notes"

### Example Output

```latex
% ============================================
% Regression Table
% ============================================
\begin{table}[htbp]\centering
\caption{Effect of Treatment on Outcome}
\label{tab:main_results}
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
\midrule
Treatment & 0.125*** & 0.118*** & 0.102** \\
 & (0.041) & (0.039) & (0.046) \\
Controls & No & Yes & Yes \\
Fixed Effects & No & Yes & Yes \\
\midrule
Observations & 2,145 & 2,145 & 2,145 \\
R-squared & 0.18 & 0.24 & 0.31 \\
\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Notes: Standard errors in parentheses. * p<0.10, ** p<0.05, *** p<0.01.
\end{tablenotes}
\end{table}
```

### Requirements

#### Software

- LaTeX distribution (TeX Live or MikTeX)

#### Packages

- `booktabs`
- `threeparttable` (optional for notes)

### Best Practices

1. **Keep tables compact** and readable
2. **Use consistent notation** for standard errors and stars
3. **Provide clear captions and labels**

### Common Pitfalls

- Overly wide tables that do not fit the page
- Missing notes for standard errors
- Inconsistent labeling across tables

### References

- [LaTeX booktabs documentation](https://ctan.org/pkg/booktabs)
- [AEA Author Guidelines](https://www.aeaweb.org/journals/policies/author-instructions)

### Changelog

#### v1.0.0

- Initial release
