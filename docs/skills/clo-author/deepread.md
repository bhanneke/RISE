<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/deepread.md -->

# `deepread`

Deep technical read of a near-final draft run on Codex: commenters per section, adversarial verification of each comment, merged into referee-grade comments anchored to exact quotes.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT (LICENSE file, "Copyright (c) 2026 Hugo Sant'Anna"; portions derived from claude-code-my-workflow, also MIT)</code></div><div><b>Updated:</b> 2026-10-15</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/deepread/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/deepread/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Deep Read

A full technical reading of the manuscript. Every section is read by multiple
commenters with different priors; every comment must survive an attempt to
refute it before it reaches the author.

**Every model call runs on Codex** (`codex exec`), so a full run costs no Claude
tokens. The orchestration is a plain Python script — no agent dispatch, no
workflow engine.

**Input:** `$ARGUMENTS` — flags, or a section path to scope the run.

---

### Usage

```bash
python3 scripts/deepread.py --dry-run          # projection only, no calls
python3 scripts/deepread.py --segment seg06    # one section
python3 scripts/deepread.py                    # full paper
```

Run from the project root. Defaults are `--root .` and `--paper paper`.
Output: `quality_reports/deepread/YYYY-MM-DD_report.md`.

**Always run `--dry-run` first.** It prints the segment list, the agent count,
and the projected token cost, and warns above the 2.5M budget.

| Flag | Effect |
|---|---|
| `--dry-run` | Print the projection and stop |
| `--segment segNN` | One section only |
| `--skeptic` | Add the adversarial twin reader (~+50% cost) |
| `--min-segment-words N` | Merge sections below N words (default 300) |
| `--jobs N` | Parallel Codex calls (default 6) |
| `--debug DIR` | Dump raw Codex transcripts for diagnosis |
| `--out PATH` | Report destination |

#### Prerequisites

- `codex` CLI on PATH (`brew install codex`), authenticated
- `scripts/paper_coherence.py` beside it — the script calls it to segment
- A `paper/` directory with a `main.tex` that `\input`s its sections

The script runs Codex with `--sandbox read-only`. It cannot modify the paper.

---

### What this is, and what it is not

| | `/deepread` | `/coherence` | `/review --peer` |
|---|---|---|---|
| Reads | The whole paper, section by section | Nothing — it compares files | The paper, as a journal would |
| Finds | Argument gaps, unsupported claims, derivation errors, confounds | Stale numbers, broken refs | Contribution, fit, novelty |
| Output | Comments anchored to quotes | A pass/fail list | A decision letter |
| Engine | Codex | Python, no model | Claude agents |
| Cost | ~2.4M Codex tokens, ~30 min | Free, seconds | Minutes |
| When | Near-final draft | Every commit | Before submitting |

Run `/coherence` **first**. It clears the mechanical layer for free, and the
consolidator is told to drop any comment that merely restates a finding the
deterministic engine already reported.

---

### Pipeline

```
paper_coherence.py --segments        one file per section, carrying the tables,
        │                            notes, figures and equations it cites
        ▼
  ┌─────┴──────┬──────────┬─────────┐
general      rigor     evidence   skeptic          PARALLEL, per segment
(always)   (if eqs)   (if tables) (--skeptic)
  └─────┬──────┴──────────┴─────────┘
        ▼
  one verifier per segment           refutes what it can, collapses duplicates
        ▼
  consolidator                       dedup across readers, rank
        ▼
  overall assessment
```

#### Why each stage

**Segments, not the whole paper.** A commenter given 8,000 words reads the first
section and skims the rest. One given a 400-word segment with its two tables
attached reads all of it.

**Multiple readers per segment.** `general` asks whether the argument holds;
`skeptic` assumes the result is spurious and looks for why. Same text, opposite
prior. `rigor` and `evidence` are conditional on the segment having equations or
tables.

**Adversarial verification.** Fan-out produces comments faster than good ones.
Each segment's comments are handed to one verifier prompted to refute them,
defaulting to refuted when uncertain. Observed: 4 raised → 1 survived.

**Consolidation.** Readers over the same segment produce the same defect from
different angles. Without a merge stage the fan-out yields a longer report, not
a better one.

---

### Cost discipline

These defaults are not preferences. The first Claude-agent version of this
pipeline burned **6.9M tokens on an 8,800-word paper and exhausted the session
before producing any verified output.**

| Rule | Why |
|---|---|
| **One verifier per segment, not per comment** | 403 comments meant ~300 verifier agents. Batched, the same job is 24. |
| **Readers cap at 3 comments** | Uncapped readers produced ~17 per section. The cap lives in each reader's agent file. |
| **Skeptic is opt-in** | Doubles the reading pass and produces the most-refuted comments. |
| **Sections under 300 words merge** | A 54-word subsection is not worth its own reader. |

Measured on a 14-segment paper: 39 agents, ~2.4M Codex tokens, ~30 min.
One segment: ~290k, ~10 min.

The projection constants in `deepread.py` are calibrated from real runs
(37k/reader, 106k/verifier, 56k/merge). Re-measure and update them if the model
or prompts change — a projection that drifts from reality is worse than none.

---

### Report

`quality_reports/deepread/YYYY-MM-DD_report.md`:

1. **Funnel** — segments, readers, comments raised, survived, tokens actually
   spent vs projected. The spend-vs-projection line is how you know the estimate
   still holds.
2. **Overall assessment** — the argument, what has to hold, the two or three
   things that most threaten it.
3. **Comments** — grouped by section, ranked, each with its exact quote, the
   problem, why it matters, and a specific fix.

---

### Principles

- **Every comment quotes the text it is about.** A comment that cannot quote its
  target is dropped.
- **No praise, no summary, no generic advice.** "Consider expanding the
  discussion" is the failure mode this pipeline exists to avoid.
- **An empty result is a real result.** A sound section produces no comments.
- **Verification is not optional.** Skipping the refutation pass turns a fan-out
  into a comment generator.
- **No score, no verdict.** `/review --peer` produces the decision letter; this
  produces the technical reading.
- **Never edits the paper.** Read-only sandbox, comments only.

---

### Troubleshooting

| Symptom | Cause |
|---|---|
| `codex CLI not found` | `brew install codex`, then authenticate |
| `0 comments` everywhere | Run with `--debug DIR` and inspect a transcript; the JSON extractor may need updating if Codex changes its output framing |
| `0 tokens` reported | Codex writes its usage footer to stderr; the script reads both streams |
| Projection far from actual | Re-measure and update the constants in `project()` |
| Segmentation finds nothing | `main.tex` must `\input` its sections; check `paper_coherence.py --segments` alone |
