<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/talk.md -->

# `talk`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>slides</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>none declared</code></div><div><b>Updated:</b> 2026-05-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/talk/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/talk/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Talk

Create, audit, or compile presentations (Beamer or Quarto RevealJS).

**Input:** `$ARGUMENTS` — mode and format/path.

---

### Modes

#### `/talk create [format]` — Create Quarto RevealJS Talk (default)
#### `/talk create [format] --beamer` — Create Beamer Talk

Generate a presentation from the paper.

**Agents:** Storyteller (creator) → storyteller-critic (reviewer)

#### Format Constraints

| Format | Slides | Duration | Content Scope |
|--------|--------|----------|---------------|
| job-market | 40-50 | 45-60 min | Full story, all results, mechanism, robustness |
| seminar | 25-35 | 30-45 min | Motivation, main result, 2 robustness, conclusion |
| short | 10-15 | 15 min | Question, method, key result, implication |
| lightning | 3-5 | 5 min | Hook, one result, so-what |

#### Workflow

**Step 1: Parse Arguments**

- **Format** (required): `job-market` | `seminar` | `short` | `lightning`
- **Paper path** (optional): defaults to `paper/main.tex`
- **Engine**: Quarto RevealJS (default) or Beamer (`--beamer`)
- If no format specified, ask the user.

**Step 2: Dispatch Storyteller**

Read the paper and extract: research question, identification strategy, main result, secondary results, robustness checks, key figures/tables, institutional background. Design narrative arc for the chosen format. Build the slide file with shared preamble if available.

The Storyteller follows these design principles:
- **One idea per slide** — never cram two concepts onto one frame
- **Figures over tables; tables in backup** — audiences absorb figures instantly; regression tables belong in backup slides where referees can inspect them during Q&A
- **Build tension** — motivation → question → method → findings → implications
- **Transition slides between major sections** — signal where the talk is going
- **All claims must appear in the paper** — the paper is the single source of truth; never add results or claims that are not in the manuscript

Compile with `quarto render` (Quarto) or XeLaTeX (Beamer).

Save to `paper/quarto/[format]_talk.qmd` (Quarto, default) or `paper/talks/[format]_talk.tex` (Beamer).

**Step 3: Dispatch Storyteller-Critic**

After the Storyteller returns, dispatch the storyteller-critic to review across 5 categories:

| Category | What It Checks |
|----------|---------------|
| **Narrative flow** | Does the story build properly? Is there a clear arc from motivation through results to implications? Are transitions smooth? |
| **Visual quality** | Text overflow, font readability (>= 10pt), figure sizing, consistent formatting, overfull hbox warnings |
| **Content fidelity** | Every claim traceable to the paper — no orphan results, no unsupported statements |
| **Scope for format** | Right amount of content for the duration — not cramming a seminar into a lightning talk, not padding a short talk to seminar length |
| **Compilation** | Does it compile cleanly without errors or warnings? |

Score as advisory (non-blocking). Save report to `quality_reports/[format]_talk_review.md`.

**Step 4: Fix Critical Issues**

If the storyteller-critic finds Critical issues (compilation failures, content not in paper):
1. Re-dispatch Storyteller with specific fixes (max 3 rounds per three-strikes rule)
2. Re-run storyteller-critic to verify

**Step 5: Present Results**

Report to the user:
1. Generated file path
2. Slide count and format compliance
3. Storyteller-critic score (advisory, non-blocking)
4. TODO items (missing figures, tables not yet generated)

---

#### `/talk audit [file]` — Visual Audit

Check existing slides for layout issues.

Run visual quality checks:
- Text overflow on any slide
- Font sizes (>= 10pt for projection)
- Table readability
- Figure sizing and labels
- Consistent formatting
- Overfull hbox warnings

---

#### `/talk compile [file]` — Compile Talk

Automated compilation via latexmk:
```bash
cd paper/talks && latexmk [file]
```

For Quarto:
```bash
cd paper/quarto && quarto render [file]
```

---

### Bundled Resources

| Resource | Path | What It Contains |
|----------|------|-----------------|
| Narrative arcs | `talk/templates/narrative-arcs.md` | Paper-type-specific story structures (reduced-form, structural, theory+empirics, descriptive) with pacing and audience calibration |
| Format constraints | `talk/templates/format-constraints.md` | Slide counts, durations, per-format rules for all 4 formats |
| Quarto scaffold | `talk/templates/quarto-scaffold.qmd` | RevealJS skeleton with YAML config, section dividers, figure/equation slots (default) |
| Beamer scaffold | `talk/templates/beamer-scaffold.tex` | Minimal Beamer skeleton with standard sections (use with `--beamer`) |
| Slide design | `talk/references/slide-design-principles.md` | Visual design principles: font sizes, colors, builds, rhythm |
| Gotchas | `talk/gotchas.md` | Known failure points and edge cases |

The Storyteller agent reads these resources before building slides. The narrative arc determines the slide sequence; the format constraints determine scope.

---

### Principles

- **Paper is authoritative.** Every claim must appear in the paper.
- **Figures over tables.** Audiences absorb figures instantly. Put regression tables in backup slides for Q&A.
- **Less is more.** Especially for short and lightning formats — ruthlessly cut.
- **One idea per slide.** If you need a second point, make a second slide.
- **Audience calibration.** Job market = demonstrate rigor and command of the literature. Seminar = sell the interesting result. Short = method and key finding. Lightning = sell the idea in one breath.
- **Advisory scoring.** Talk scores don't block commits.
- **Worker-critic pairing.** Storyteller creates, storyteller-critic critiques. Never skip the review.
