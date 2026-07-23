<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/mgsci-workflow.md -->

# `mgsci-workflow`

Router for the 12-skill Management Science depth pack (mgsci-*) — topic selection through rebuttal, including picking the right INFORMS Department lane (analytical vs empirical).

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Management-Science-Skills/skills/mgsci-workflow/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/mgsci-workflow/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Management-Science-Skills/skills/mgsci-workflow/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Management Science Workflow (mgsci-workflow)

### Overview

This is the router. It does not replace any specialized skill; it tells you **which mgsci-* skill to use right now** for your Management Science manuscript.

Default assumption: unless the user says otherwise, treat the target as **Management Science** — the **INFORMS** flagship established in **1954** by the precursor Institute of Management Sciences (TIMS). It is deliberately **bimethodological**: it places rigorous **analytical/quantitative** work (operations research, optimization, stochastic processes, game and economic theory) **side by side** with **empirical** work (econometrics, lab/field experiments, behavioral studies, data science), across **every functional business area** — accounting, finance, marketing, operations, information systems, strategy, entrepreneurship, organizations, behavioral economics. There is **no single dominant method by design**; each **Department** sets its own field-appropriate rigor bar. The unifying test is rigor **plus** a decision-relevant management/business contribution that travels across departments.

> Editor-in-Chief Christoph H. Loch (term Jan 1, 2024 - Dec 31, 2026). Submissions are routed into a specific **Department** (e.g., Accounting; Behavioral Economics and Decision Analysis; Data Science; Entrepreneurship and Innovation; Finance; Healthcare Management; Information Systems; Market Design, Platform, and Demand Analytics; Marketing; Operations Management; Optimization and Decision Analytics; Organizations; Stochastic Models and Simulation; Strategy; Sustainability). Verify the current masthead and department set on INFORMS PubsOnline before submission.

### When to trigger

- "What should I do next?" with a half-built Management Science manuscript
- You are unsure which **Department** your paper belongs to, or whether it fits Management Science vs a sister INFORMS journal (Operations Research, M&SOM, Marketing Science)
- A model exists but the managerial insight is thin, or data exist but the contribution is unclear
- A Department Editor desk-rejected on "fit" or "better suited elsewhere" and you need to re-aim
- You received a decision letter (R&R or reject) and need to switch into response mode

### Routing table

| Current symptom                                                          | Next skill                    |
|--------------------------------------------------------------------------|-------------------------------|
| Idea is vague; unsure of Department fit or Management Science vs sister journal | `mgsci-topic-selection`  |
| Model/hypotheses lack a sharp mechanism or testable proposition          | `mgsci-theory-development`     |
| Front end reads as gap-spotting; the relevant conversation isn't engaged | `mgsci-literature-positioning` |
| Method (analytical model or empirical design) may not match the question | `mgsci-methods`               |
| Have data/numerics; unsure on identification, validity, or robustness    | `mgsci-data-analysis`         |
| Results exist but the cross-department "so what for decisions" is thin   | `mgsci-contribution-framing`  |
| Exhibits cluttered, notation-heavy, or not self-explanatory              | `mgsci-tables-figures`        |
| Prose is notation-dense, passive, or buries the result                   | `mgsci-writing-style`         |
| Ready to submit; need the ScholarOne + fee + disclosure preflight        | `mgsci-submission`            |
| Want to understand desk-screen / Department Editor / review mechanics    | `mgsci-review-process`        |
| Received an R&R; need to plan and draft the response                     | `mgsci-rebuttal`              |

### Default order

```
mgsci-topic-selection → mgsci-theory-development → mgsci-literature-positioning →
mgsci-methods → mgsci-data-analysis → mgsci-contribution-framing →
mgsci-tables-figures → mgsci-writing-style → mgsci-submission →
mgsci-review-process → mgsci-rebuttal
```

Skip stages that are already solid; loop back when a Department Editor or reviewer pushes.

### Desk-reject early-warning router

Most Management Science deaths are fit and contribution failures caught at the desk, not deep methodological flaws. Route on the symptom before investing more.

| Early-warning symptom | Likely desk verdict | Route to |
|-----------------------|---------------------|----------|
| Cannot name a single home department | "Off fit / better elsewhere" | `mgsci-topic-selection` |
| Method is a polished algorithm, thin managerial reading | Redirect toward Operations Research | `mgsci-topic-selection` / `mgsci-methods` |
| Result is correct but no decision changes | "So what" reject | `mgsci-contribution-framing` |
| Empirical causal claim with selection unaddressed | Identification reject | `mgsci-methods` / `mgsci-data-analysis` |
| Insight confined to one application area | Reads as a sister-journal paper | `mgsci-contribution-framing` |

### Worked routing micro-example (illustrative)

A user has a solved queueing model of hospital ED diversion and "some data." Because the journal is the multidisciplinary INFORMS flagship, the router first asks the department question: this is Stochastic Models / Operations Management, not a generic OR submission, so the managerial lever (a diversion policy a hospital manager would adopt) must be explicit. The model exists, so skip theory-development; the gap is that the comparative statics carry no decision reading and the empirical test is observational. Route: `mgsci-contribution-framing` to sharpen the decision lever, then `mgsci-methods` to upgrade identification before any polishing. Polishing prose first would be wasted effort against a desk that screens on fit and contribution.

### Calibration anchor

The flagship spans analytical-to-behavioral across many departments; the router's job is to surface the department and the cross-department travel early, because those — not formatting — decide most outcomes. Confirm the current department roster and masthead on INFORMS PubsOnline.

### Output format

```
【Where you are】[stage]
【Department / lane】analytical vs empirical; candidate Department
【Fit risk】Management Science vs sister INFORMS journal
【Next skill】mgsci-...
```
