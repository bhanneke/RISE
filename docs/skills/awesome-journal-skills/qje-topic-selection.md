<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-topic-selection.md -->

# `qje-topic-selection`

Scopes and pressure-tests a research question for QJE — fit, the "big idea" bar, and breadth of the takeaway for QJE's general-interest readership.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>ideation</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>rq-formulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-topic-selection/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-topic-selection/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-topic-selection/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Topic Selection & Fit (qje-topic-selection)

### When to trigger

- You have data or a result but the "so what?" is unclear
- You are unsure whether the idea is top-5 material or a field-journal paper
- The question is narrow, technical, or interesting only to specialists
- You can describe what you *did* but not the *broad lesson* it teaches

### The QJE bar: a big question with a broad answer

QJE is a general-interest journal covering all of economics, published by OUP and edited at Harvard since **1886** (the oldest English-language economics journal). Its comparative advantage is the **compelling question + credible empirics + a conceptual takeaway with broad implications** — the journal that ran Akerlof's "Market for 'Lemons'" (QJE 1970) and Mankiw, Romer & Weil's "Contribution to the Empirics of Economic Growth" (QJE 1992) rewards papers that *change how a wide audience thinks*, not just precise estimates. Editorial reality reinforces this: five Harvard-based Editors desk-screen in ~2 weeks, so the big idea must be visible immediately. Force the idea through three filters:

1. **The question filter** — Would a smart economist outside your subfield want to know the answer? State the question in one sentence a labor economist, a macroeconomist, and a development economist would all find interesting.
2. **The answer filter** — Is the *answer* (not the method) surprising, important, or settling of a long-standing debate? A precise estimate of something nobody disputes is a field-journal paper.
3. **The breadth filter** — Does the result generalize beyond the specific setting? QJE rewards a clean local result that *teaches a general lesson* (e.g., Chetty–Hendren–Kline–Saez on the geography of intergenerational mobility, QJE 2014).

### Scope fit decision table

| Your paper is...                                              | QJE fit          | Better home if not              |
|---------------------------------------------------------------|------------------|---------------------------------|
| Big empirical-micro question + clean natural experiment       | Strong           | —                               |
| Novel large-scale data answering an old question              | Strong           | —                               |
| New econometric estimator / asymptotic theory                 | Weak             | Econometrica, JoE               |
| Structural IO / quantitative-macro led by a calibrated model  | Possible         | JPE, Econometrica, AEJ:Macro    |
| Field-specific incremental estimate                           | Weak             | Top field journal (JOLE, JPubE) |
| Pure theory with no empirical or policy payoff                | Weak             | TE, JET, RAND                   |
| Descriptive paper with genuinely new facts/data               | Possible         | Needs exceptional, first-order novelty |

QJE-vs-siblings taste note: relative to JPE (more sympathetic to a strong calibrated/structural model carrying the paper) and Econometrica (method and theory), QJE leans toward **reduced-form, idea-driven empirical work with a memorable lesson**. A pure-method paper that AER or JPE might consider for a methods slot is a weak QJE fit.

### Sharpening the contribution

- Write the **one-sentence hook**: "We show that [surprising answer] using [clean source of variation]." If you cannot fill both brackets, the project is not ready.
- Identify the **broad lesson**: finish the sentence "Beyond this setting, our result implies ..."
- Name the **debate you move**: which prior belief does your answer overturn, quantify, or reconcile?
- Stress-test against desk rejection: QJE desk-rejects fast (~2 weeks). If the editor cannot see the big idea in the first paragraph of the intro, the paper is gone.

### Checklist

- [ ] One-sentence hook with both a surprising answer and a clean source of variation
- [ ] A "broad lesson" sentence that travels beyond the specific setting
- [ ] The question is legible to a non-specialist top-5 reader
- [ ] The answer (not the technique) is what makes the paper interesting
- [ ] You can name the prior belief or debate the paper moves
- [ ] Not better suited to Econometrica (method) or a top field journal (incremental)

### Anti-patterns

- A precise causal estimate of something no one doubted ("more education raises wages, again")
- Leading with the *method* ("we apply the Callaway–Sant'Anna estimator to ...") instead of the *question*
- A purely descriptive paper with no exceptional, first-order data novelty
- "Interesting only to people who study X" — fails the general-interest filter
- Over-claiming generality the design cannot support (a single-county RDD billed as a universal law)

### Output format

```
【Question】one sentence a non-specialist would care about
【Surprising answer】...
【Source of variation】...
【Broad lesson】Beyond this setting, ...
【Debate moved】prior belief → our result
【QJE fit verdict】strong / possible / weak (+ better home if weak)
【Next step】qje-literature-positioning
```
