<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/american-economic-review.md -->

# `american-economic-review`

Venue-fit skill for AER from the English Social-Science Journal bundle — fit, framing, the method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics; exemplar of the one-skill-per-journal breadth-bundle format.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/English-SocialScience-Journal-Skills/skills/american-economic-review/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/american-economic-review/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/English-SocialScience-Journal-Skills/skills/american-economic-review/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## American Economic Review (american-economic-review)

### Journal positioning

AER is the flagship general-interest journal of the American Economic Association and one of the economics "top-5" (with QJE, JPE, Econometrica, REStud). It wants papers of broad interest to economists across fields, with a first-order question, a credible answer, and a result that changes how the profession thinks — not an incremental field paper. The audience is the whole discipline, so the contribution must read as important to someone outside your subfield.

A full lifecycle pack for AER ships separately as `AER-skills` (the `aer-*` skills). This profile is the quick fit / venue-selection layer; route into `aer-workflow` for step-by-step drafting and submission.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AEA site or the editorial-manager submission system.

### When to trigger

- The author names AER (or AER as a stretch target) as the venue.
- A paper has a clean research design and a question of general interest, and the author is choosing between AER and a top field journal.
- A strong field paper needs re-framing so the contribution reads as discipline-wide rather than niche.
- The author needs AER's desk-reject risks and a credible top-5 / top-field alternative list.

### Scope & topic fit

- First-order questions across all fields of economics — micro, macro, labor, public, IO, trade, development, finance-adjacent — judged on general interest.
- Empirical papers with a transparent, defensible identification strategy.
- Theory papers whose results are general and consequential, not a narrow extension.
- Consider the sibling AEJs (`aej-applied-economics`, `aej-macroeconomics`, `aej-microeconomics`, `aej-economic-policy`) and short-format `aer-insights` when the contribution is excellent but narrower than AER's general-interest bar.

### Method & evidence bar

- Identification is the desk filter: naive TWFE on staggered treatment, weak or unjustified instruments, and RDD without density/covariate-smoothness evidence get rejected fast.
- Empirical work is expected to pre-empt the obvious threats (selection, measurement, confounders) with design, not hand-waving; modern DiD estimators, proper inference, and robustness are baseline.
- Structural and theory papers need clearly stated assumptions, identification of structural parameters, and results that generalize.
- Data and code transparency is mandatory; AEA enforces a data and code availability policy with verification.

### Structure & house style

- The introduction must, in its first pages, state the question, the contribution, the approach, and the headline result — and say explicitly why a non-specialist should care.
- Make the marginal contribution non-overlapping: separate the theory/identification advance from the empirical finding from the policy reading.
- AER uses an unstructured abstract, JEL codes, and a tightly disciplined main text with online appendices for everything secondary.
- Exhibits are expected to be self-contained and publication-clean; the headline result should be legible from one table or figure.

### Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Search the live site for "American Economic Review submission guidelines" and the AEA "Data and Code Availability Policy" and follow the current versions.
- Re-check submission fee, formatting, abstract/JEL requirements, anonymization expectations, and figure/table standards on the editorial-manager system.
- Re-check the current data/code deposit and verification workflow (openICPSR / AEA Data Editor) — this is enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

### Pre-submission self-check

- [ ] One sentence stating why an economist outside your field should care about this result.
- [ ] The contribution is stated as identification / theory / measurement, not as statistical significance.
- [ ] The introduction positions the paper against the current top-5 / top-field frontier on this question.
- [ ] Identification threats are addressed by design; inference and DiD/IV/RDD choices are state-of-the-art.
- [ ] Data and code are ready for the AEA availability + verification workflow.

### Common desk-reject triggers

- A well-executed but narrow field paper with no general-interest hook.
- Identification that the profession no longer accepts (TWFE on staggered adoption, weak IV, cosmetic RDD).
- Contribution framed as "first to study X in context Y" without a methodological or conceptual advance.
- Significance treated as the finding; mechanism and external validity left thin.

### Re-routing decision

- Narrower-but-excellent applied → `aej-applied-economics`; macro → `aej-macroeconomics` or `review-of-economic-dynamics`; micro theory → `aej-microeconomics` or `journal-of-economic-theory`; policy → `aej-economic-policy` or `journal-of-public-economics`.
- Short, sharp, single-result papers → `aer-insights`.
- Field-leading specialist work → the relevant top field journal (`journal-of-labor-economics`, `journal-of-development-economics`, `journal-of-public-economics`, `journal-of-finance`, etc.).

### Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] American Economic Review
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / theory clear AER's general-interest bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
