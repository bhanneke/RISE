<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-submission.md -->

# `qje-submission`

Final pre-submission preflight for QJE via Editorial Express — single-PDF format, double-blind anonymization, author-date references, the no-fee policy, and supplementary files.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-submission/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-submission/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-submission/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Submission Preflight (qje-submission)

### When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Express
- Unsure which files Editorial Express expects at the initial-submission stage
- Confirming the single-PDF format, double-blind anonymization, and author-date style are QJE-compliant
- Checking declarations and supplementary-materials requirements

### Process facts (verified; re-confirm specifics on the official page)

- QJE is published by **Oxford University Press** and **edited at Harvard University's Department of Economics** — the oldest English-language economics journal (founded **1886**) and one of the top-5. Source: academic.oup.com/qje; Wikipedia.
- Submission is through **Editorial Express** at `editorialexpress.com/qje` — the same Express platform used by several econ journals, *not* OUP's ScholarOne. Admin contact: `qje_admin@editorialexpress.com`.
- **There is no submission fee.** This is unusual among top-5 journals (AER, JPE, REStud all charge); do not budget for one. QJE is hybrid open access, so an optional OA charge applies only *after* acceptance if you choose it.
- **Initial submission is a single PDF** containing the full manuscript, tables, figures, and appendices. **No Word files, no LaTeX source, no separate figure files** at this stage — source files are requested only after acceptance.
- QJE uses **double-blind refereeing** — the manuscript must be fully anonymized.
- The editorial team — **five Editors, all at Harvard** (Robert J. Barro, Lawrence F. Katz, Nathan Nunn, Andrei Shleifer, and Stefanie Stantcheva, masthead re-verified 2026-06-22; re-check before submitting) — makes **fast desk decisions (roughly two weeks)**, the quickest among the top-5 flagships, so a clean, complete submission is part of clearing the first screen. (Acceptance runs ~1-4%; desk-reject ~60%+.)

### Preflight checklist

#### Format & style

- [ ] One **single PDF** with manuscript, tables, figures, and appendices embedded (no Word, no separate figure files)
- [ ] References in **author-date (Chicago)** style; reference list alphabetical by surname
- [ ] Abstract is short (target **~150 words**)
- [ ] Tables and figures numbered, called out in order, with self-contained notes
- [ ] Long manuscripts are fine (no hard page limit); an extensive **online appendix** is expected
- [ ] PDF compiles cleanly; figures legible at print resolution

#### Anonymization (double-blind — required)

- [ ] No author names, affiliations, or acknowledgments in the PDF
- [ ] Self-citations phrased neutrally ("Smith (2020) shows", not "in our earlier work")
- [ ] PDF metadata/properties scrubbed of author identity
- [ ] Acknowledgments and funding info kept out of the body, supplied separately

#### Files for Editorial Express

- [ ] Main manuscript as a single PDF (figures/tables/appendix embedded)
- [ ] Cover letter (concise: question, design, headline result, general-interest fit)
- [ ] Suggested / excluded referees prepared (expert, fair, conflict-free)
- [ ] Replication materials staged for the accepted stage (see qje-replication-package)

#### Declarations

- [ ] Conflict-of-interest / disclosure statement consistent with the **AEA Disclosure Policy**
- [ ] Funding and data-source disclosures prepared
- [ ] Confirmed the paper is not under review elsewhere

#### Final content sanity

- [ ] Abstract states the finding with a number (see qje-writing-style)
- [ ] Identification diagnostics complete (see qje-identification, qje-robustness)
- [ ] No over-claiming beyond what the design supports

### Anti-patterns

- Uploading a Word file or separate figure files at initial submission (QJE wants one PDF)
- Mixed/inconsistent reference styles instead of clean author-date
- Leaving author identity in self-citations or PDF metadata under double-blind review
- Budgeting for a submission fee that does not exist at QJE
- A defensive, multi-page cover letter instead of a tight pitch the editors can read in two weeks
- Submitting a thin appendix to a journal that expects an extensive one

### Output format

```
【Single PDF】one file, all exhibits + appendix embedded? [Y/N]
【Reference style】author-date (Chicago), consistent? [Y/N]
【Anonymization】body + PDF metadata clean (double-blind)? [Y/N]
【Files staged】PDF / cover letter / referees? [Y/N each]
【Declarations】AEA disclosure / funding prepared? [Y/N]
【Content sanity】abstract states finding; identification complete? [Y/N]
【Next step】await ~2-week desk decision → qje-rebuttal on R&R
```

### Supplementary resources

- `templates/manuscript_template.md` — QJE-oriented manuscript skeleton (abstract, intro arc, design, exhibits, author-date references)
- `templates/checklist.md` — 8-section pre-submission self-check
- `../../resources/external_tools.md` — data sources and Stata/R/Python packages for credible-design empirical micro
- `../../resources/official-source-map.md` — official QJE URLs behind every fact in this pack
