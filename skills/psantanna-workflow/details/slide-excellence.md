---
name: slide-excellence
description: Multi-agent comprehensive slide review (visual + pedagogy + proofreading, plus TikZ / parity / substance conditionally). Use when user says "full review", "excellence pass", "comprehensive check", "review everything", "pre-release review", "slide excellence", or before teaching / shipping a deck. Fanout wrapper — for a single lens, use `/visual-audit`, `/pedagogy-review`, or `/proofread` directly.
argument-hint: "[QMD or TEX filename] [--fast] [--skip-substance | --acknowledge-template-domain-reviewer]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Bash", "Agent", "Task"]
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

**Important:** this orchestrator does **conditional** dispatch — it only spawns the subagents that can actually produce useful output for the given file. It does not run `tikz-reviewer` on a file with zero TikZ, or `quarto-critic` on a deck without a counterpart.

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

# Measure the Quarto render once — the file itself, or a .tex file's Quarto pair.
# The report goes to Agents A and E. slide-qa exits 0 (clean) or 1 (a finding:
# overflow, clipped content, or a broken asset) with a fresh report, 2 if it could
# not run (it deletes old reports first).
qa_report=""; qa_target=""
if [[ "$FILE" == *.qmd ]]; then qa_target="$FILE"
elif [ "$has_qmd_pair" = "true" ]; then qa_target="$qmd_pair"; fi
if [ -n "$qa_target" ]; then
  quarto render "$qa_target" >/dev/null 2>&1
  "${SLIDE_QA_PYTHON:-python3}" scripts/slide-qa.py "$qa_target"
  if [ $? -ne 2 ]; then
    qa_report="quality_reports/audits/slide-qa/$(basename "$qa_target" .qmd)/report.md"
  fi
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
Slide QA:     quality_reports/audits/slide-qa/Lecture2/report.md (or: could not run — reason)
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
     with checks for your field (the file's EXAMPLES block shows two
     disciplines to copy from).
  2. Run slide-excellence with --skip-substance to proceed without the
     substance-review agent. Other reviewers still run.
  3. Run slide-excellence with --acknowledge-template-domain-reviewer to
     proceed anyway (you'll get generic feedback from the substance agent).

```

Stop here and return these options — this skill runs in a forked context and cannot wait for an answer. Do not run `domain-reviewer` on the uncustomized template; the user re-invokes with the flag they choose.

## Step 4: Run Review Agents in Parallel

Spawn only the agents whose conditions hold:

**Always-on for slides (`.tex` or `.qmd`):**

- **Agent A: Visual Audit** (`slide-auditor`)
  Overflow, font consistency, box fatigue, spacing, images. When `$qa_report` is set (a `.qmd`, or a `.tex` with a Quarto pair), pass it — measured overflow plus screenshots; if slide-qa could not run, say so in the summary.
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
  Frame count comparison, environment parity, content drift between `.tex` ↔ `.qmd`. Pass `$qa_report` when there is one.
  Save: `quality_reports/[FILE]_parity_report.md`.

- **Agent F: R Code Review** (`r-reviewer`) — only if `has_r == true`.
  Code correctness for any embedded R chunks or referenced scripts.
  Save: `quality_reports/[FILE]_r_review.md`.

- **Agent G: Substance Review** (`domain-reviewer`) — MANDATORY for `.tex`, OPTIONAL for `.qmd`, GATED by Step 3.
  Domain correctness via the 5-lens framework.
  Save: `quality_reports/[FILE]_substance_review.md`.

**De-duplication:** if one of these skills already produced a report for this file in the current session (e.g. `/proofread` ran first), reuse that report when it is newer than the file and list which reports were reused — this skill runs in a forked context and cannot stop to ask. To force a fresh pass, move the old report out of `quality_reports/` (or touch the deck so it is newer) and re-invoke.

## Step 5: Synthesize Combined Summary (reduce typed findings)

This is **fan-out → reduce** ([`orchestrator-protocol.md`](../../rules/orchestrator-protocol.md)): each agent returns `FINDING`s + a `SCORECARD` in the shared schema ([`orchestration-schemas.md`](../../references/orchestration-schemas.md)), and this step **stacks the typed scorecards** rather than re-reading each report by eye. The Overall Quality Score is the gate predicate over summed CRITICAL/MAJOR/MINOR counts. (Conditional dispatch means a skipped lens contributes no findings, not zeros to average.)

Only include sections for agents that actually ran.

```markdown
# Slide Excellence Review: [Filename]

**File:** [path]
**Type:** [Beamer / Quarto / Markdown]
**Detected:** TikZ=N | pair=[path or none] | R=[yes/no]
**Agents spawned:** [A, B, C, D, G] (skipped: E [no pair], F [no R])

## Overall Quality Score: [EXCELLENT / GOOD / NEEDS WORK / POOR]

| Dimension | Critical (`blocker`) | Major | Minor | Score/10 |
|-----------|----------|--------|-----|-----|
| Visual/Layout | | | | |
| Pedagogical | | | | |
| Proofreading | | | | |
| TikZ (if ran) | | | | |
| Substance (if ran) | | | | |

### Critical Issues (Immediate Action Required)
### Major Issues (Next Revision)
### Recommended Next Steps
```

## Step 6: Report Token/Time Budget

After completion, print what was spawned:

```
Spawned N agents[; token usage: actual figure, if the harness reports it].
For cost-conscious reviews, run individual subagent skills directly
(/proofread, /visual-audit, /pedagogy-review).
```

## Flag Reference

| Flag | Effect |
|---|---|
| `--skip-substance` | Don't spawn Agent G (domain-reviewer). Useful if you haven't customized domain-reviewer.md yet. |
| `--acknowledge-template-domain-reviewer` | Proceed with the un-customized domain-reviewer anyway; you accept that the substance review will be generic. |
| `--fast` | Spawn a single synthesis agent reading the file directly, rather than parallel subagents. Cheaper but less thorough. |

## Quality Score Rubric

| Score | Critical (`blocker`) | Major | Meaning |
|-------|----------|--------|---------|
| Excellent | 0 | 0 | Ready to present |
| Good | 0 | 1-5 | Revise the majors first (the gate reads this as REVISE) |
| Needs Work | 0-5 | 6+, or any with criticals | Significant revision — the gate blocks while any critical remains |
| Poor | 6+ | any | Major restructuring |

Any critical finding blocks, whatever the other counts — the same gate predicate as [`orchestration-schemas.md`](../../references/orchestration-schemas.md) §3.

## Why conditional dispatch matters

A reviewer that cannot produce useful output costs tokens and trust: `tikz-reviewer` on a TikZ-free deck returns nothing, `quarto-critic` without a counterpart file has no pair to compare, and an uncustomized `domain-reviewer` returns generic "are assumptions stated?" feedback that authors learn to ignore. Spawn only the lenses the file can use.

## Findings are validated, not just written (v2.5)

This skill's reviewers emit findings under the machine-checked contract in
[`finding-schema.json`](../../references/finding-schema.json). Reports are JSON **arrays**.

**Smoke-test the harness before spending review effort** — a run that fans out reviewers and
then cannot write a valid report has wasted the whole pass:

```bash
echo '[]' | python3 scripts/validate-findings.py
```

Reviewer agents are read-only, so **this skill writes the files**. For each reviewer's final
response: save the prose report to this skill's report path for that reviewer, copy its closing fenced `json` block
to a scratch file, and fill the ids while validating:

```bash
python3 scripts/validate-findings.py --fill-ids block.json > <report>.json.tmp \
  && mv <report>.json.tmp <report>.json || rm -f <report>.json.tmp   # exit 0 required; a failed run keeps no file
python3 scripts/validate-findings.py --check-quotes <report>.json   # each quote must be the file's own text (orchestration-schemas.md §1)
```

A reviewer that returned no `json` block, or a block that does not validate, has not reviewed:
re-dispatch it once with the validator's error text, then report the lens as missing rather
than reducing without it.

What the contract forces, and why:

- **`rule`** — the documented rule or standard violated. A finding citing no rule is an
  opinion, and opinions do not gate a commit.
- **`failing_case`** — a concrete configuration under which the claim breaks, or the exact
  missing hypothesis. *"This could be clearer"* does not validate.
- **`id = sha1("<file>:<line>:<locus>")`** — deterministic, so dedup across rounds is
  exact and the two-strikes rule is checkable rather than eyeballed.
- **`mechanical`** — `true` only for fixes that cannot change a result (typo, cross-reference,
  formatting, label). **Never** for an estimand, assumption, specification, inference
  procedure, sample definition, or reporting language: those return to the researcher.

Apply the **per-lens evidence burdens** and the **"does NOT count" filters** in
[`orchestration-schemas.md` §7](../../references/orchestration-schemas.md) *before*
verification, so known false alarms never reach the judge. The verifier pass is
**refute-biased** and sets each finding's `verdict` (reviewers leave it unset): only `verdict: "confirmed"` findings ship; anything it cannot ground is
dropped, not downgraded to a warning.
