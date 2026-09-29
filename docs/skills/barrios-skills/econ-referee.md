<!-- DO NOT EDIT — auto-copied from skills/barrios-skills/details/econ-referee.md -->

# `econ-referee`

A short pre-submission referee workflow for accounting, finance and economics papers. Its iron law is that every major comment cites a page, table or figure, and any claim the manuscript cannot support is marked Unverified, never invented. It classifies the paper, locates the contribution sentence, and audits in a fixed order that stops early only on a fatal flaw. It adds accounting- and finance-specific flags and venue checklists (JAR/TAR/JAE, JF/JFE/RFS, AEA) and always delivers three outputs: substance comments, separate editing notes and a prioritized revision plan. Self-declared original rather than a fork of the PolyForm-noncommercial OpenEcon referee.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../barrios-skills/">Barrios Skills (John Manuel Barrios)</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> accounting</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2026 John Barrios"). The vendored third-party skills keep their own terms: the Anthropic document skills say "Proprietary. LICENSE.txt has complete terms", and the K-Dense skills carry per-library licence lines.</code></div><div><b>Updated:</b> 2026-07-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Barrios88/barrios-skills/contents/skills/writing-and-review/econ-referee/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/barrios-skills/econ-referee/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Barrios88/barrios-skills/blob/main/skills/writing-and-review/econ-referee/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Barrios88/barrios-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Barrios Skills** — John Barrios's curated workflow for economists and accountants. Prioritize reproducible empirical work, clear identification language, and journal-ready output.

## Econ / finance / accounting pre-submission referee

John Barrios's compact referee workflow. Inspired by the *idea* of verified, revision-ready AI refereeing in the OpenEcon ecosystem, but written for this collection (MIT) with an accounting and finance lens — **not** a fork of the PolyForm-Noncommercial `econ-paper-review-skill`.

### When to use

- Stress-test a working paper before journal submission
- Produce a referee-style report the author can act on
- Separate **substance** (identification, inference, contribution) from **editing** (clarity, typos)

**After** the judgment is settled, use `econ-write` + `econ-humanizer` to implement revisions.

### Iron law: every major comment cites evidence

Do not invent table numbers, coefficients, or sample sizes. If the PDF/manuscript does not support the claim, mark **Unverified** and ask for the exhibit.

Format substance comments as:

```text
[Severity: Critical|Major|Minor] [Topic: Identification|Inference|Data|Contribution|Clarity]
Location: §X / Table Y / Figure Z (p. N if known)
Issue: ...
Why it matters for this literature: ...
Concrete fix: ...
```

### Workflow

#### 1. Classify the paper

- Empirical reduced-form / archival accounting / asset pricing / banking / macro / theory / structural / mixed
- Claimed identification (DiD, IV, RDD, bunching, event study, disclosure mandate, etc.)
- Target venue band if the user names one (e.g. JAR vs JAE vs JF)

#### 2. Read for the contribution sentence

Write the paper's one-sentence contribution *in the author's terms*, then in your own skeptical terms. If these diverge, that is Comment #1.

#### 3. Audit in this order (stop early only if fatal)

1. **Research integrity** — results match text; no silent sample changes across tables
2. **Design / identification** — parallel trends, exclusion, bandwidth, disclosure timing, etc.
3. **Inference** — clustering, multiple testing, weak IV, staggered DiD estimator choice
4. **Data construction** — Compustat filters, winsorization, look-ahead, delisting, CIK merges
5. **Economic magnitude** — is the effect sized in interpretable units?
6. **Literature / novelty** — relative to the frontier the paper cites
7. **Presentation** — only after substance

#### 4. Accounting- and finance-specific flags

| Field | Recurring issues |
|-------|------------------|
| Archival accounting | Measurement of accruals/quality; within-GAAP discretion vs real effects; disclosure vs recognition; auditor/office clustering |
| Corporate finance | Endogenous policy; bad controls (collider); industry×year FE debates; CEO vs firm clustering |
| Asset pricing | Multiple testing; tradability; microstructure; anomaly t-stats vs Sharpe |
| Banking / intermediation | Regulatory timing; call-report breaks; call vs market data mismatch |
| Governance / ESG | Construct validity; boilerplate NLP; selection into disclosure |

#### 5. Deliverables (always produce all three)

**A. Referee report** (1–2 pages)

- Summary paragraph (contribution + verdict tone)
- Main comments (numbered, verified)
- Minor comments
- Overall recommendation language suitable for *private* pre-submission use (Accept/R&R/Reject *as a forecast*, clearly labeled as advisory)

**B. Editing notes** (separate)

- Clarity, structure, notation — not mixed into substance comments

**C. Revision plan**

| Priority | Comment # | Action | Depends on |
|----------|-----------|--------|------------|
| P0 | … | … | … |

### Red lines

- Do not accuse fraud without documentary support; ask for clarification instead
- Do not demand citations to papers you cannot name accurately
- Do not rewrite the paper's contribution into a different paper
- Do not rubber-stamp: if identification is weak, say so plainly

### Optional journal-fit paragraph

Only if the user asks. Map claims to venue norms (identification bar, magnitude, mechanism evidence) without pretending to know editorial boards' private thresholds.

### Venue checklists (accounting & finance)

Use when the user names a target outlet. These are *pre-submission stress tests*, not editorial promises.

#### JAR / TAR / JAE (archival accounting)

- [ ] Research question is about **accounting** (measurement, disclosure, assurance, real effects of GAAP/IFRS) — not a generic corporate-finance paper with an accounting covariate
- [ ] Construct validity: accruals / AQ / conservatism / disclosure indices defined and defended against alternatives
- [ ] Identification threat named in accounting terms (discretion, concurrent standards changes, auditor change, XBRL mandate timing, etc.)
- [ ] Sample filters: Compustat `indfmt/datafmt/popsrc/consol`; fiscal-year alignment; winsorization / truncation disclosed
- [ ] Clustering: firm at minimum; auditor/office or state when the shock lives there
- [ ] Mechanism / channel evidence expected at top journals (not only reduced-form ATE)
- [ ] Economic magnitude in accounting units (pp of ROA, days of accruals, basis points of spread) — not only t-stats
- [ ] Parallel-trends / pre-trends or placebo around disclosure/effective dates when DiD-like

#### JF / JFE / RFS (finance)

- [ ] Contribution vs asset-pricing / corporate-finance / banking frontier is explicit in one sentence
- [ ] Endogeneity: policy, leverage, and governance designs state the exclusion story without hand-waving
- [ ] Fixed effects match the variation (firm + year; industry×year when industry shocks are the threat)
- [ ] Clustering justified (firm vs CEO vs deal); no silent switch across tables
- [ ] For pricing papers: multiple testing, tradability, and microstructure addressed or scoped out
- [ ] Magnitudes in return space (bps, abnormal returns, Sharpe-relevant units) with horizon clear
- [ ] Staggered shocks: not only TWFE when adoption timing varies

#### AEA / general interest econ

- [ ] External validity and mechanism get more weight than accounting-construct debates
- [ ] Identification section could stand alone for a non-specialist empirical reader
- [ ] Tables emphasize main claim; appendices hold robustness forests

If the paper straddles accounting and finance, say which literature's bar you are applying and why.
