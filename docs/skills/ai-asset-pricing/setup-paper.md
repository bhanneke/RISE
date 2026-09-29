<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/setup-paper.md -->

# `/setup-paper`

Starts a new paper from the repo's LaTeX boilerplate, filling title, authors and affiliations, inserting tagged placeholder text and compiling a test PDF.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-24</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/setup-paper/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/setup-paper/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/setup-paper/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Setup Paper

Scaffold a new academic paper from the repo's LaTeX boilerplate template. The
template includes 6 table exemplars, 1 figure, and 2 equation styles — all
tagged `[REMOVE]` — so Claude has maximum context on formatting conventions.

### Examples

- `/setup-paper "My Paper Title"` — basic scaffold with placeholder authors
- `/setup-paper "My Paper Title" --authors "John Smith (MIT), Jane Doe (LSE)"` — with authors
- `/setup-paper "My Paper Title" --authors "John Smith (MIT)" --topic "asset pricing anomalies"` — with topic-aware filler

### Workflow

#### Phase 1: Parse Arguments

Extract from `$ARGUMENTS`:
- **Title** (required): first quoted string or all text before `--`
- **`--authors`** (optional): comma-separated `"Name (Affiliation)"` pairs
- **`--topic`** (optional): one-line description for smarter filler generation

If title is missing, use `AskUserQuestion` to prompt.

#### Phase 2: Resolve Target Directory

Determine where to write `main.tex` and `references.bib`:

1. If cwd is inside `projects/<name>/` (any depth), target = `projects/<name>/latex/`
2. If cwd already ends with `/latex/`, target = cwd
3. Otherwise, ask the user which project to target or whether to write to cwd

Create the target directory if it does not exist.

#### Phase 3: Locate Boilerplate

Find the repo root by walking up from cwd looking for `boilerplate/template_main.tex`.
The boilerplate lives at:

```
<repo_root>/boilerplate/template_main.tex
<repo_root>/boilerplate/template_references.bib
```

If the boilerplate files are not found, stop and tell the user.

#### Phase 4: Copy and Transform

1. Read `boilerplate/template_main.tex`
2. Read `boilerplate/template_references.bib`
3. Write both to the target directory as `main.tex` and `references.bib`
4. Update the `\bibliography{}` line: replace `template_references` with `references`

#### Phase 5: Replace Placeholders

Find and replace these `[REMOVE]` placeholders in `main.tex`:

| Find | Replace with |
|------|-------------|
| `[REMOVE] Your Paper Title Here` | User's title |
| `[REMOVE] First Author\thanks{...}` block | Generated from `--authors` (see below) |
| `[REMOVE] Second Author\thanks{...}` block | Remove if only one author, or replace |
| `[REMOVE] We gratefully acknowledge...` | `[REMOVE] Acknowledgments go here.` (keep tag) |
| `[REMOVE] This paper studies...` (abstract) | Topic-aware filler if `--topic`, else keep |
| `[REMOVE] Keyword One; ...` | `[REMOVE] Keyword One; Keyword Two; Keyword Three.` (keep tag) |
| `[REMOVE] G12; C12.` | `[REMOVE] G12; C12.` (keep tag) |

Also replace the Internet Appendix title:
| `[REMOVE] Your Paper Title Here` (in IA section) | User's title |

**Author block generation** from `--authors "Name1 (Affil1), Name2 (Affil2)"`:

```latex
\author{
{\normalsize Name1\thanks{{\scriptsize
Affil1; \url{name1@university.edu}}}}
\and
{\normalsize Name2\thanks{{\scriptsize
Affil2; \url{name2@university.edu}}}}
}
```

If no `--authors` provided, leave the template's placeholder authors intact.

#### Phase 6: Write Filler Content

If `--topic` is provided, rewrite the introduction filler (~250 words) to:
- Open with a concrete claim about the topic
- Follow motivation → gap → contribution → roadmap structure
- Cite `\citet{FamaFrench_1992}`, `\citet{FamaFrench_1993}`, and `\citet{FamaFrench_2015}`
- Tag every sentence with `[REMOVE]`

Also write 2–3 sentence `[REMOVE]`-tagged filler for Data, Methodology, Results, and Conclusion sections that references the topic.

If no `--topic`, leave the template's default filler intact.

**Do NOT remove the example tables, figures, or equations.** These serve as formatting exemplars.

#### Phase 7: Compile

Run the standard build cycle using the pdflatex path from canonical local state reported by `tools/bootstrap.py audit`:

```bash
cd {target_dir} && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```

Report any errors or warnings. If pdflatex is not available, skip compilation
and note it in the summary.

#### Phase 8: Summary

Print the structured summary below.

### Table Exemplar Index

The template includes 7 table styles for reference:

| Label | Archetype | Location | Pattern |
|-------|-----------|----------|---------|
| `tab:example_panel` | Panel results + t-stats | Data | `\scalebox{0.75}`, 2 panels, `\cmidrule`, `\addlinespace` |
| `tab:example_descriptive` | Summary statistics | Data | `\scalebox{0.85}`, no panels, percentiles |
| `tab:example_definitions` | Lookup / definitions | Data | `p{6cm}` text column, `\texttt{}` mnemonics |
| `tab:example_decomposition` | Multi-leg decomposition | Results | `\scalebox{0.72}`, Long/Short/L-S groups |
| `tab:example_comparison` | Compact comparison | Results | `\scalebox{0.78}`, Mean + Alpha side-by-side |
| `tab:example_summary` | Appendix summary | Appendix A | No scaling, counts + aggregate stats |
| `tab:ia_example` | IA subsample results | Internet Appendix | `\scalebox{0.80}`, Roman numeral numbering (IA.I) |

### Output

```
PAPER SETUP COMPLETE
====================

Title: {title}
Authors: {author list or "template placeholders (replace [REMOVE] tags)"}
Topic: {topic or "none"}
Target: {target_dir}
Files created:
  {target_dir}/main.tex       (from boilerplate/template_main.tex)
  {target_dir}/references.bib (from boilerplate/template_references.bib)

Compile: SUCCESS / FAILED / SKIPPED (pdflatex not available)
Pages: {N}

Section keys (for /write-section):
  introduction, data, methodology, results, conclusion, appendix-a, internet-appendix

Table exemplars (7):
  tab:example_panel, tab:example_descriptive, tab:example_definitions,
  tab:example_decomposition, tab:example_comparison, tab:example_summary,
  tab:ia_example

[REMOVE] items: {count} across {N} sections

Next steps:
  1. Search for [REMOVE] and replace all filler content with your text
  2. Add your .bib entries to references.bib (FF 1992/1993/2015 included as demos)
  3. Keep example tables as formatting reference until you replace with your own
  4. Run /build-paper to recompile after edits
```
