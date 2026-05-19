<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/new-project.md -->

# `new-project`



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
name: new-project
description: Full research pipeline from idea to paper. Orchestrates all phases — discovery, strategy, analysis, writing, peer review, and submission. Use when starting a new research project from scratch.
argument-hint: "[research topic or 'interactive' for guided start]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task,WebSearch,WebFetch
---

# New Project

Launch a full research pipeline from idea to paper, orchestrated through the dependency graph.

**Input:** `$ARGUMENTS` — a research topic or `interactive` for a guided start via `/discover interview`.

---

## Pipeline Overview

This skill orchestrates the full dependency graph. Each phase activates when its dependencies are met. The orchestrator manages agent dispatch, three-strikes escalation, and quality gates.

```
Phase 1: Discovery
  ├── /discover interview → Research Spec + Domain Profile
  ├── /discover lit → Literature Synthesis + BibTeX
  └── /discover data → Data Assessment

Phase 2: Strategy (depends on Phase 1)
  ├── /strategize → Strategy Memo + Robustness Plan
  └── /strategize theory → Theory Section (conditional — econometric methods, theory+empirics, structural, methodological reduced-form)

Phase 3: Execution (depends on Phase 2)
  ├── /analyze → Scripts + Tables + Figures
  └── /write → Paper Sections

Phase 4: Peer Review (depends on Phase 3)
  ├── /review --all → Comprehensive Quality Score
  └── /review --peer → domain-referee + methods-referee Reports

Phase 5: Submission (depends on Phase 4, score >= 95)
  ├── /submit target → Journal Recommendations
  ├── /submit package → Replication Package
  └── /submit final → Final Verification
```

---

## Workflow

### Step 0: Enter Plan Mode

Before any work begins:
1. **Enter plan mode** — use `EnterPlanMode`
2. **Create the project folder structure** — `data/raw/`, `data/cleaned/`, `scripts/R/`, `paper/sections/`, `paper/figures/`, `paper/tables/`, etc.
3. **Draft a high-level plan** — what phases are needed, estimated scope
4. **Save to disk** — `quality_reports/plans/YYYY-MM-DD_new-project.md`
5. **Present to user** — wait for approval before proceeding
6. **Exit plan mode** — only after approval

### Step 1: Discovery Phase

1. **If `interactive` or no research spec exists:**
   Run `/discover interview` to produce:
   - Research specification (`quality_reports/research_spec_*.md`)
   - Domain profile (`.claude/references/domain-profile.md`) — if still template

2. **Run `/discover lit`** with the research topic:
   - Librarian collects literature
   - librarian-critic reviews coverage
   - Output: literature synthesis + BibTeX entries

3. **Run `/discover data`** to find datasets:
   - Explorer searches for data sources
   - explorer-critic assesses data quality

**Gate:** Research spec and literature review must exist before proceeding.

### Step 2: Strategy Phase

4. **Run `/strategize`** to design the empirical strategy:
   - Strategist proposes identification strategy
   - strategist-critic validates the design

4b. **If paper type is econometric methods, theory+empirics, structural, or methodological reduced-form:**
   **Run `/strategize theory`** to produce the formal theory section:
   - Theorist drafts assumptions, theorems, proofs
   - theorist-critic audits proof validity (4 phases, early-stop on critical gaps)
   - Theorist-critic score contributes 20% to the weighted aggregate when present (see `quality.md`)

   Skip this step for applied papers using off-the-shelf estimators.

**Gate:** Strategy memo must pass strategist-critic review (score >= 80). If theory section exists, theorist-critic must also pass (score >= 80).

### Step 3: Execution Phase

5. **Run `/analyze`** to implement the strategy:
   - Data-engineer cleans data and creates figures
   - Coder writes analysis scripts
   - coder-critic reviews code

6. **Run `/write`** to draft the paper:
   - Writer drafts sections
   - Humanizer pass strips AI patterns

**Gate:** Code must pass coder-critic review. Paper sections must exist.

### Step 4: Peer Review Phase

7. **Run `/review --all`** for comprehensive review:
   - strategist-critic + coder-critic + writer-critic + Verifier in parallel
   - Weighted aggregate score computed

8. **Run `/review --peer`** for simulated peer review:
   - domain-referee (subject expertise) + methods-referee (econometrics)
   - Independent, blind reports
   - Orchestrator synthesizes editorial decision

**Gate:** Aggregate score >= 80 (commit-ready). Score >= 90 for submission.

### Step 5: Submission Phase (optional, user-triggered)

9. **Run `/submit target`** for journal recommendations
10. **Run `/submit package`** for replication package
11. **Run `/submit final`** for final verification

---

## User Interaction Points

The pipeline pauses for user input at these points:
- After interview (approve research spec)
- After strategy memo (approve identification strategy)
- After data analysis (review results before paper drafting)
- After peer review (review feedback before revision)
- Before submission (approve journal choice)

Between pauses, the orchestrator runs autonomously per `workflow.md`.

---

## Bundled Resources (Level 3)

| Resource | Path | When |
|----------|------|------|
| Quality gates | `config/quality-gates.json` | Phase transitions — score thresholds |
| Gotchas | `gotchas.md` | Always — known failure points |

---

## Principles

- **This is always orchestrated.** Unlike other skills, `/new-project` always runs through the full pipeline.
- **Dependency-driven.** Phases activate by dependency, not forced sequence.
- **Quality-gated.** Each phase transition requires passing quality checks.
- **User retains control.** Pipeline pauses at key decision points.
- **Resumable.** If interrupted, the pipeline resumes from the last completed phase.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/new-project/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>hugosantanna/clo-author</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../clo-author.md">Clo-Author skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>none declared</dd>
<dt><b>Last update</b></dt><dd>2026-05-11</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/hugosantanna/clo-author">⭐ hugosantanna/clo-author</a><br><img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/hugosantanna/clo-author" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/clo-author/new-project/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/clo-author.yml">edit on GitHub</a>.</p>
</div>

</div>
