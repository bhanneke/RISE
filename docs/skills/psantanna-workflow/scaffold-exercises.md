<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/scaffold-exercises.md -->

# `/scaffold-exercises`

Scaffolds a graded problem set with worked solutions and short why-this-matters explainers across analytical, empirical and coding problem types.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/scaffold-exercises/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/scaffold-exercises/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/scaffold-exercises/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## `/scaffold-exercises` — Problem Set Scaffolder

Generate a graded problem set as two files: a clean **student set** (problems only) and a **solution key** (worked solutions + a one-line explainer per problem). Pattern imported from `mattpocock/skills`, adapted for economics teaching — the primary lens is graded coursework that mixes derivation, estimation, and code.

**Input:** `$ARGUMENTS` — a topic (e.g., "instrumental variables", "consumer theory", "quantile regression") and optional flags. See [Flags](#flags).

---

### When to use

- You have a lecture or reading and want a matching assignment with an answer key.
- You want a mix of problem types (derive, estimate, code) at a controlled difficulty, with solutions emitted **separately** so the student file stays clean.

Do **not** use this to grade submissions, auto-check answers, or build a timed exam — it scaffolds *practice/graded* material, not assessment infrastructure.

---

### Problem types

| Type | What the student does | Solution artifact |
| --- | --- | --- |
| **analytical** | Derive / prove / characterize (theory: optimization, identification, comparative statics) | Step-by-step derivation with the key lemma named |
| **empirical** | Estimate + interpret on a provided or simulated dataset | Expected estimate, sign/magnitude reasoning, common-mistake note |
| **coding** | Implement an estimator or simulation in R or Stata | Runnable reference snippet + expected output shape |

If no dataset is supplied for an empirical problem, generate a small **simulated** one with a fixed seed (YYYYMMDD) so the answer key is deterministic and reproducible.

---

### Workflow

#### Phase 0: Set topic, difficulty, counts, types (Pre-Flight)

Read any source material the user points at (lecture `.tex`/`.qmd`, a paper, a dataset header) and produce a Pre-Flight Report **before** generating problems:

```markdown
### Pre-Flight Report — Problem Set

**Topic:** [topic]
**Source(s) read:** [lecture/paper/dataset — one-line takeaway each]
**Difficulty:** intro | core | advanced
**Counts by type:** analytical=N, empirical=N, coding=N  (total = `--count`)
**Dataset:** [provided path | simulated with seed YYYYMMDD | none]
**Learning objectives:** [2-4 bullets the set should exercise]
```

Resolve every flag here (interactive choices are gathered before generation, not mid-run). If the topic is too vague to write objectives, ask one clarifying question and stop. Otherwise proceed.

#### Phase 1: Generate problems

For each problem, write a number, a section heading, the prompt, and any data/notation it needs. Conventions:

- **Motivation before mechanics** — one sentence on why the problem is worth solving, matching `create-lecture`'s pedagogy.
- **Notation reuse** — match symbols to the source lecture; never introduce a clashing symbol for an already-defined object.
- **Difficulty calibration** — *intro* checks one concept; *core* chains 2-3 steps; *advanced* requires a non-obvious insight or identification argument.
- **Self-contained** — each problem states its own assumptions; no "as in lecture 4" dangling references.

#### Phase 2: Generate worked solutions + explainers

For every problem, write:

1. A **worked solution** — full derivation, expected estimate, or runnable code (depending on type). Coding solutions must actually run; if `Bash` + R/Stata are available, execute the snippet and paste real output.
2. A **"why this matters" explainer** — 1-2 sentences linking the answer to the broader concept (the imported pattern's signature: every problem ships with a short rationale, not just a number).

#### Phase 3: Write student set + solution key

Emit two files (paths configurable; default under `quality_reports/teaching/`, beside `/respond-to-eval`'s teaching plans. A new top-level directory such as `exercises/` fails `scripts/check-repo-hygiene.py` once committed, unless it is added to that script's `ROOT_ALLOW_DIRS`):

- `quality_reports/teaching/<topic-slug>_problems.md` — the **student set**: sections, problems, any data, NO answers.
- `quality_reports/teaching/<topic-slug>_solutions.md` — the **solution key**: each problem restated, its worked solution, and its explainer.

The split is load-bearing: never leak a solution into the student file. With `--no-solutions`, write only the student set and stop.

---

### Output / Report format

Student set:

```markdown
## Problem Set: [Topic]  (Difficulty: core)

### Section 1 — Analytical
**1.** [Motivation sentence.] [Prompt.]

### Section 2 — Empirical
**2.** Using `data/<file>` (vars: ...), [estimate + interpret prompt].

### Section 3 — Coding (R)
**3.** [Implement-X prompt.]
```

Solution key mirrors the numbering, adding `### Solution` and `> Why this matters:` blocks per problem. Close your chat reply with a one-line manifest: files written, problem count by type, and whether code solutions were executed or only drafted.

---

### Exit behavior

- Print the two output paths (absolute), the per-type counts, and the seed if a dataset was simulated.
- If a coding solution could not be executed (no R/Stata, or it errored), flag it as **DRAFTED — NOT RUN** rather than implying it was verified.
- If any empirical problem references variables not present in the supplied dataset, stop and surface the mismatch instead of inventing columns.

---

### Flags

- `--difficulty` — `intro` | `core` | `advanced` (default `core`); calibrates step depth as in Phase 1.
- `--count` — total number of problems (default 6); split across types per the Pre-Flight counts.
- `--types` — comma-separated subset of `analytical,empirical,coding` (default all three).
- `--dataset` — path to a real dataset for empirical problems; omit to simulate one with a seeded DGP.
- `--no-solutions` — write only the student set; skip the solution key (Phase 2/3 key file).

---

### Cross-references

- `.claude/skills/create-lecture/SKILL.md` — build the lecture these exercises practice; shares notation-reuse + motivation-first conventions.
- `.claude/skills/data-analysis/SKILL.md` — for empirical problems whose reference solution needs a full R estimation pipeline.
- `.claude/skills/simulation-study/SKILL.md` — when a problem demonstrates an estimator's finite-sample behavior; reuse its seeded-DGP discipline.
- `.claude/skills/lit-review/SKILL.md` — source advanced problems from current papers on the topic.
- `.claude/skills/interview-me/SKILL.md` — turn a fuzzy "I want a set on…" into concrete learning objectives first.
- `templates/skill-template.md` — house style for authoring/extending this skill.

---

### What this skill does NOT do

- **Does not grade** student submissions or auto-check answers against a key.
- **Does not run a timed exam** or enforce assessment policy (point weights, rubrics, proctoring).
- **Does not invent data** — empirical problems use a supplied dataset or an explicitly seeded simulation, never fabricated numbers.
- **Does not leak solutions** into the student file, and does not deploy/publish anything (no `/deploy`).
- **Does not auto-invoke** other skills — it references siblings; it does not call them.
