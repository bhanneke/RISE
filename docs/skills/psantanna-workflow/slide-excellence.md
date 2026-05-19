<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/slide-excellence.md -->

# `/slide-excellence`



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

---
name: slide-excellence
description: Multi-agent comprehensive slide review (visual + pedagogy + proofreading, plus TikZ / parity / substance conditionally). Use when user says "full review", "excellence pass", "comprehensive check", "review everything", "pre-release review", "slide excellence", or before teaching / shipping a deck. Fanout wrapper — for a single lens, use `/visual-audit`, `/pedagogy-review`, or `/proofread` directly.
argument-hint: "[QMD or TEX filename] [--fast] [--skip-substance | --acknowledge-template-domain-reviewer]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Bash", "Task"]
context: fork
---

# Slide Excellence Review

Run a comprehensive multi-dimensional review of lecture slides. Multiple agents analyze the file independently, then results are synthesized.

> **Which slide-review skill do I want?**
>
> - **`/slide-excellence`** (this skill) — multi-agent fanout (visual + pedagogy + proofread, plus TikZ / parity / substance conditionally). Best for **pre-teaching** or **pre-release** checks.
> - **`/visual-audit`** — single lens, layout/overflow/font/spacing only. Fast.
> - **`/pedagogy-review`** — single lens, narrative/prerequisites/worked-examples/notation.
> - **`/proofread`** — single lens, grammar/typos/overflow/terminology.
> - **`/qa-quarto`** — adversarial Beamer ↔ Quarto parity (critic-fixer loop).
> - **`/devils-advocate`** — 5-7 pointed challenges, not a full review.

**Important:** this orchestrator does **conditional** dispatch — it only spawns the subagents that can actually produce useful output for the given file. No more running `tikz-reviewer` on a file with zero TikZ, or `quarto-critic` on a deck without a counterpart.

## Step 1: Identify the File

Parse `$ARGUMENTS` for the filename. Resolve path in `Quarto/` or `Slides/`.

Determine the file type:

- `.tex` → Beamer
- `.qmd` → Quarto
- `.md` → Markdown slides

## Step 2: Pre-flight — Detect Conditions

Before spawning any agent, probe the file to determine which reviews make sense:

```bash
FILE="$resolved_path"

# Has TikZ diagrams?
has_tikz=$(grep -c '\\begin{tikzpicture}' "$FILE" 2>/dev/null); has_tikz=${has_tikz:-0}

# For .qmd: is there a paired .tex in Slides/?
has_tex_pair="false"
if [[ "$FILE" == *.qmd ]]; then
  base="$(basename "$FILE" .qmd)"
  # Common Beamer suffixes: _Topic, _Lecture, exact match
  for candidate in "Slides/${base}.tex" "Slides/Lecture${base}.tex"; do
    if [ -f "$candidate" ]; then
      has_tex_pair="true"
      tex_pair="$candidate"
      break
    fi
  done
fi

# For .tex: is there a paired .qmd in Quarto/?
has_qmd_pair="false"
if [[ "$FILE" == *.tex ]]; then
  base="$(basename "$FILE" .tex)"
  for candidate in "Quarto/${base}.qmd" "Quarto/${base#Lecture}.qmd"; do
    if [ -f "$candidate" ]; then
      has_qmd_pair="true"
      qmd_pair="$candidate"
      break
    fi
  done
fi

# Has R code chunks or referenced R scripts?
has_r="false"
if grep -qE '```\{r|source\(.*\.R\)' "$FILE" 2>/dev/null; then
  has_r="true"
fi
```

Report the detection:

```
File:         path/to/file.tex
Type:         Beamer (.tex)
TikZ blocks:  3
Quarto pair:  Quarto/Lecture2.qmd (found)
R chunks:     none
```

## Step 3: Domain-reviewer customization check (MANDATORY for .tex)

Before spawning the substance-review agent on a `.tex` file, verify `.claude/agents/domain-reviewer.md` has been customized for this project. The ship-state domain-reviewer is a **template** — running it unmodified produces generic "are assumptions stated?" feedback, not real domain review.

Detection heuristic (any of these → still template):

- Contains the marker token `AUTO-DETECT-TEMPLATE-MARKER` anywhere in the file (present in the shipped template; removed/replaced when customized). Detection is a substring match — the marker can span lines.
- Contains any `<!-- Customize: ... -->` or `[Customize: ...]` placeholder (both forms are checked).
- The five lenses are identical to the shipped template's wording (diff against `.claude/agents/domain-reviewer.md` on the v1.3.0 tag — if zero lines changed, it's still template).

If the template marker is present:

```
⚠️  domain-reviewer.md has not been customized for your field.

Running it in its shipped state produces generic checks ("are assumptions
stated?") rather than field-specific review. Options:

  1. Customize .claude/agents/domain-reviewer.md — replace the 5 lenses
     with checks for your field. The /configure-project skill will scaffold
     this interactively (coming in PR D of the plan).
  2. Run slide-excellence with --skip-substance to proceed without the
     substance-review agent. Other reviewers still run.
  3. Run slide-excellence with --acknowledge-template-domain-reviewer to
     proceed anyway (you'll get generic feedback from the substance agent).

What would you like to do?
```

Wait for user input. Do NOT silently run domain-reviewer on a template.

## Step 4: Run Review Agents in Parallel

Spawn only the agents whose conditions hold:

**Always-on for slides (`.tex` or `.qmd`):**

- **Agent A: Visual Audit** (`slide-auditor`)
  Overflow, font consistency, box fatigue, spacing, images.
  Save: `quality_reports/[FILE]_visual_audit.md`.

- **Agent B: Pedagogical Review** (`pedagogy-reviewer`)
  13 pedagogical patterns, narrative, pacing, notation.
  Save: `quality_reports/[FILE]_pedagogy_report.md`.

- **Agent C: Proofreading** (`proofreader`)
  Grammar, typos, consistency, academic quality, citations.
  Save: `quality_reports/[FILE]_proofread_report.md`.

**Conditional:**

- **Agent D: TikZ Review** (`tikz-reviewer`) — only if `has_tikz > 0`.
  Measurement-based collision audit (Bézier, gaps, boundaries, margins).
  Save: `quality_reports/[FILE]_tikz_review.md`.

- **Agent E: Content Parity** (`quarto-critic`) — only if the file has a counterpart (`has_tex_pair` or `has_qmd_pair`).
  Frame count comparison, environment parity, content drift between `.tex` ↔ `.qmd`.
  Save: `quality_reports/[FILE]_parity_report.md`.

- **Agent F: R Code Review** (`r-reviewer`) — only if `has_r == true`.
  Code correctness for any embedded R chunks or referenced scripts.
  Save: `quality_reports/[FILE]_r_review.md`.

- **Agent G: Substance Review** (`domain-reviewer`) — MANDATORY for `.tex`, OPTIONAL for `.qmd`, GATED by Step 3.
  Domain correctness via the 5-lens framework.
  Save: `quality_reports/[FILE]_substance_review.md`.

**De-duplication:** if the user has already run one of these skills on this file in the current session (e.g., ran `/proofread` first, now running `/slide-excellence`), ask whether to reuse the existing report or re-run. Default: reuse (saves tokens).

## Step 5: Synthesize Combined Summary

Only include sections for agents that actually ran.

```markdown
# Slide Excellence Review: [Filename]

**File:** [path]
**Type:** [Beamer / Quarto / Markdown]
**Detected:** TikZ=N | pair=[path or none] | R=[yes/no]
**Agents spawned:** [A, B, C, D, G] (skipped: E [no pair], F [no R])

## Overall Quality Score: [EXCELLENT / GOOD / NEEDS WORK / POOR]

| Dimension | Critical | Medium | Low |
|-----------|----------|--------|-----|
| Visual/Layout | | | |
| Pedagogical | | | |
| Proofreading | | | |
| TikZ (if ran) | | | |
| Substance (if ran) | | | |

### Critical Issues (Immediate Action Required)
### Medium Issues (Next Revision)
### Recommended Next Steps
```

## Step 6: Report Token/Time Budget

After completion, print an estimate:

```
Spawned N agents; approx token usage ~XXk. Sequential fallback
(one agent at a time) would cost ~XXk but take ~5× longer. For
cost-conscious reviews, run individual subagent skills directly
(/proofread, /visual-audit, /pedagogy-review).
```

## Flag Reference

| Flag | Effect |
|---|---|
| `--skip-substance` | Don't spawn Agent G (domain-reviewer). Useful if you haven't customized domain-reviewer.md yet. |
| `--acknowledge-template-domain-reviewer` | Proceed with the un-customized domain-reviewer anyway; you accept that the substance review will be generic. |
| `--fast` | Spawn a single synthesis agent reading the file directly, rather than parallel subagents. Cheaper (~8k vs ~50k tokens) but less thorough. |

## Quality Score Rubric

| Score | Critical | Medium | Meaning |
|-------|----------|--------|---------|
| Excellent | 0-2 | 0-5 | Ready to present |
| Good | 3-5 | 6-15 | Minor refinements |
| Needs Work | 6-10 | 16-30 | Significant revision |
| Poor | 11+ | 31+ | Major restructuring |

## Why conditional dispatch matters

The previous version of this orchestrator spawned **all 6** subagents regardless of file type. Running `tikz-reviewer` on a TikZ-free deck produced an empty report (wasted tokens). Running `quarto-critic` without a counterpart file produced a "no pair to compare" report (wasted tokens). And running `domain-reviewer` without customization produced generic "are assumptions stated?" feedback that authors learned to ignore (eroded trust in the whole orchestrator).

Conditional dispatch cuts token cost roughly in half on typical `.qmd`-only files and doubles trust by never running a reviewer that can't produce useful output.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/slide-excellence/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>slides</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>dissemination</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/slide-excellence/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/slide-excellence/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
