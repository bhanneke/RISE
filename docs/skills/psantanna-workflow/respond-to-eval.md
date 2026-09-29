<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/respond-to-eval.md -->

# `/respond-to-eval`

Turns student course evaluations into a teaching-improvement plan: clusters comments into themes and classifies each as Keep, Change or Investigate.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>revision</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-27</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/respond-to-eval/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/respond-to-eval/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/respond-to-eval/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Respond to Evaluations

Convert a semester's course evaluations into a defensible teaching-improvement plan. Cluster free-text comments into themes, weight each theme by how many independent students raised it, classify what to do about it, and draft specific changes pointed at the syllabus and deck — so next semester's revision is a checklist, not a vibe.

**Posture (echoes `/respond-to-referees`):** one angry comment is not a trend, and a comment you disagree with is a signal to *investigate*, not a license to ignore or to auto-act. A single student's frustration may be the only one willing to say what twenty felt — frequency weights the theme, it does not gate it. Ground truth here is a process: the plan records *why* a theme was kept or changed, so the reasoning survives to the next round.

### When to use

- End of term, when numeric scores + open-text comments land and you want a revision plan, not a mood.
- Assembling a teaching dossier / tenure file where you must *show* you acted on feedback.
- Mid-stream (early-semester feedback) to course-correct before the term ends.

Not for: writing the syllabus from scratch (use `/syllabus`), or reviewing one deck's pedagogy (use `/pedagogy-review`).

### Inputs

- `$0` — the evaluation file(s): a CSV/TSV export, `.txt`/`.md` of pasted comments, or a `.pdf`/`.docx` report.
- `$1` (optional) — the **prior** improvement plan, so this round is a diff (did last term's changes land?).

| Format | How to read |
| --- | --- |
| `.csv`, `.tsv`, `.txt`, `.md` | `Read` directly; for CSV, note which column is numeric vs free-text. |
| `.pdf` | `TMP=$(mktemp -d)/evals.txt && pdftotext "$0" "$TMP"` (poppler). Read/grep `"$TMP"`. |
| `.docx` | `TMP=$(mktemp -d)/evals.txt && pandoc "$0" -t plain -o "$TMP"`. |

If extraction fails or a tool is missing, ask for a plain-text export and stop. A scanned or partly scanned PDF extracts with exit 0 and blank pages, so also compare `pdfinfo "$0" | grep Pages` with the pages that returned text (`awk 'BEGIN{RS="\f"} NF{n++} END{print n+0}' "$TMP"`); read any blank pages directly with Read, or ask for a text version, and if you go on without them, say which pages were not read. When you are done, delete the extracted copy (`rm -rf "$(dirname "$TMP")"`): it is a plaintext copy of the document.

### Phases

#### Phase 0: Load evals + prior plan (Pre-Flight)

Read the eval file(s) and the prior plan (if given). Produce a short Pre-Flight block before clustering:

```markdown
### Pre-Flight Report
**Evals loaded:** N responses (M with free-text), instrument: [name/term]
**Numeric items:** [list each scale item + mean, and the institution/department mean if present]
**Prior plan:** [path, or "none — first round"] — changes promised last term: [bullet list]
**Course artifacts in scope:** [syllabus path] · [deck(s) under Slides/ or Quarto/]
```

Numbers anchor the read but do not override text: a 4.2/5 with ten "I was lost by week 6" comments is a problem the mean is hiding.

#### Phase 1: Theme-cluster + weight by frequency

1. Split free-text into atomic comments (one student may raise several themes; one comment may belong to several themes).
2. Cluster into themes (e.g., *pacing*, *problem-set difficulty*, *grading clarity*, *real-world relevance*, *office hours*, *prerequisite gaps*). Name each theme in the instructor's words, not the student's.
3. For each theme record: **mention count** (distinct students), **representative verbatim quote** (~25 words, anonymized — strip names/identifying detail), **valence** (positive / negative / mixed), and **numeric corroboration** (which scale item, if any, moves with it).
4. **Signal vs noise:** a theme with `< --min-mentions` (default 2) distinct students is tagged **low-frequency**, not dropped — it carries to Phase 2 for a Keep/Investigate call. Frequency weights; it never silences.

#### Phase 2: Classify + propose changes

Assign each theme exactly one label (the teaching analogue of `/respond-to-referees`' coverage matrix):

| Label | Meaning | Drives |
| --- | --- | --- |
| **Keep** | Working well; protect it from collateral damage when you change other things. | A "do not break" note. |
| **Change** | Clear, agreed problem with a concrete fix you can name. | A specific syllabus/deck edit. |
| **Investigate** | Real signal but root cause unclear, or you disagree with the proposed remedy — gather evidence (a mid-term pulse poll, a look at the grade distribution, peer observation) before acting. | An investigation step, not an edit. |
| **Out-of-scope** | Outside your control (room, time slot, required textbook, prerequisite course) or contrary to a deliberate pedagogical choice you stand behind. | A documented rationale, not a change. |

For each **Change**, write a concrete revision mapped to a target: `syllabus §X` / `Slides/LectureNN.tex slide K` / a new worked example / an assessment reweighting — the same point-to-the-location discipline `/respond-to-referees` uses for "we added X on page Y". For **Investigate**, name the evidence you'll collect and the decision rule. For **Out-of-scope**, write the one-sentence rationale you'd stand behind in a dossier.

Disagreement is explicit and reasoned: "Students asked to drop proofs; retained because the course's stated objective is derivation fluency — added two scaffolded worked examples (LectureNN slide K) to ease the on-ramp instead" is a Keep-with-mitigation, not an Out-of-scope dismissal.

#### Phase 3: Save the improvement plan

Write the plan to `quality_reports/teaching/YYYY-MM-DD_[course]_improvement-plan.md`. Structure:

1. **Header** — course, term, instrument, response rate, numeric summary vs benchmark.
2. **Prior-plan retrospective** (if `$1` given) — for each change promised last term: Landed / Partial / Not done, with the evidence from this term's evals.
3. **Theme matrix** — one row per theme: theme · mentions · valence · numeric corroboration · classification · target (syllabus §/deck slide) · representative quote.
4. **Change list** — the concrete edits, ordered by mention count then severity, each pointing at a syllabus section or deck/slide.
5. **Investigate list** — open questions + the evidence to collect next.

The plan is a deliverable, not a transient report, so it lives under `quality_reports/teaching/` and feeds next term's `$1`.

#### Phase 3.5: Post-Flight Verification (quotes + targets)

The plan's hallucination-prone content is (a) verbatim quotes attributed to students and (b) "edit syllabus §X / LectureNN slide K" targets that must actually exist. Run the fresh-context verifier protocol in `.claude/rules/post-flight-verification.md`: spawn `claim-verifier` (fresh context, never a conversation fork) with the quotes + the eval source and the edit-targets + the syllabus/deck paths. Reconcile — a quote that isn't in the source, or a "slide K" that doesn't exist, is corrected or dropped before the plan is final. Opt-out: `--no-verify` (not recommended).

### Output / Report

After writing the plan, surface this in your **final chat message** (not inside the plan file):

```
### Teaching-improvement summary — [course], [term]
Themes: K total — C Change · I Investigate · P Keep · O Out-of-scope
Top 3 changes (by mentions): 1) … 2) … 3) …
Open investigations: …
Prior plan: x of y promised changes landed.
```

If all themes are classified and every Change names a target, say `All themes classified; every Change mapped to a syllabus or deck target.`

### Exit behavior

- A theme with no classification halts the report — there are no orphans, exactly as `/respond-to-referees` admits no unclassified concern.
- Read-only on the syllabus and decks: this skill **plans** edits and writes the plan file; it does not edit teaching materials. Apply changes deliberately afterward (with `/create-lecture` or direct edits).
- Numbers never auto-override text and text never auto-overrides numbers; conflicts become **Investigate**, not a silent winner.

### Flags

- `--min-mentions` — distinct-student threshold below which a theme is tagged *low-frequency* (default `2`). Lowering it surfaces more singletons; it never drops them.
- `--no-verify` — skip Phase 3.5 Post-Flight Verification of quotes and edit-targets. Not recommended for a dossier-bound plan.

### Cross-references

- `.claude/skills/respond-to-referees/SKILL.md` — the research analogue; this skill borrows its map-classify-respond shape and "signal to investigate, not auto-act" posture.
- `.claude/skills/pedagogy-review/SKILL.md` — once a **Change** targets a specific deck, run pedagogy-review on it before re-teaching.
- `.claude/skills/create-lecture/SKILL.md` — to execute deck-level changes the plan proposes.
- `.claude/rules/post-flight-verification.md` — the fresh-context verifier protocol Phase 3.5 reuses.
- `templates/skill-template.md` — house style for skills.

### What this skill does NOT do

- It does **not** edit the syllabus or any deck — it produces a plan; you (or `/create-lecture`) apply it.
- It does **not** compute new numeric scores or re-weight the instrument; it reads the institution's numbers as given.
- It does **not** identify students or attempt to de-anonymize comments — quotes are stripped of identifying detail.
- It does **not** auto-act on disagreement or on a single comment; both route to **Investigate** or a documented rationale.
