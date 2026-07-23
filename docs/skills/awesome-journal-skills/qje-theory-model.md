<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-theory-model.md -->

# `qje-theory-model`

Adds the model or conceptual framework that turns a credible empirical coefficient into a lesson with broad implications — the frame QJE expects around a headline result.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>modeling</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>formal-modeling</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-theory-model/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-theory-model/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-theory-model/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Theory & Conceptual Frame (qje-theory-model)

### When to trigger

- The empirics are clean but the paper reads as "a coefficient with no story"
- Referees would ask "what is the economic mechanism / model behind this?"
- There is a verbal mechanism but no formalization tying estimates to parameters
- The result is interesting but its broad implication is not articulated

### Why QJE wants a frame, not necessarily heavy theory

QJE rewards a **clear conceptual takeaway with broad implications** — it is, after all, the journal that published Akerlof's "Market for 'Lemons'" (QJE 1970) and Spence's "Job Market Signaling" (QJE 1973), papers carried by a sharp idea rather than heavy machinery. That does *not* mean every paper needs a structural model. Many of QJE's most influential empirical-micro papers carry a *light* conceptual framework whose role is to (1) organize what is being estimated, (2) make the mechanism legible, and (3) map reduced-form estimates to an economically meaningful quantity (the sufficient-statistic style of Chetty-school QJE papers is the template). This is a real QJE-vs-sibling distinction: a paper whose contribution *is* a calibrated structural model often fits JPE or Econometrica better; QJE prizes the idea-plus-clean-evidence combination. Match the weight of theory to the question; do not bolt on a model the empirics cannot speak to.

### Choosing the right level of formalization

| Level                        | Use when...                                                        | Risk if misused                          |
|------------------------------|--------------------------------------------------------------------|------------------------------------------|
| Verbal conceptual frame      | The mechanism is intuitive and the estimate is the contribution    | Reads as undertheorized; "so what?"      |
| Stylized model (1–3 results) | You need to show *what parameter* the design identifies            | Best default for empirical-micro QJE     |
| Sufficient-statistic frame   | A few estimable objects map to welfare/policy                      | Powerful and parsimonious when it fits   |
| Full structural model        | Counterfactuals/welfare require out-of-sample extrapolation        | Often a better fit for JPE/ECMA than QJE |

### The framing moves

1. **Define the object.** State precisely what economic quantity the empirical estimate corresponds to (an elasticity, a treatment effect on a welfare-relevant margin, a structural parameter).
2. **Make the mechanism a proposition.** Even a two-equation model that yields "the sign/size of β reveals mechanism M" disciplines the interpretation and tells referees what the test is.
3. **Connect to welfare or policy.** Where possible, use a sufficient-statistic or envelope argument to translate estimates into a quantity decision-makers care about.
4. **State the broad lesson.** Close the loop with the topic-selection hook: the model should make the "beyond this setting" sentence rigorous and legible to a general-interest reader.

### Checklist

- [ ] The estimated object is defined in terms of an economic primitive
- [ ] The model (verbal or formal) generates a testable prediction the data address
- [ ] Theory weight is matched to the question (no gratuitous structural model)
- [ ] Mapping from reduced-form estimates to the conceptual quantity is explicit
- [ ] A welfare / policy interpretation is offered where feasible
- [ ] The frame makes the "broad lesson" rigorous, not decorative
- [ ] Assumptions of the frame are stated and their plausibility discussed

### Anti-patterns

- A standalone theory section disconnected from what the data can test
- A heavy structural model whose key parameters the design cannot identify (and that pushes the paper toward JPE/ECMA territory)
- "Mechanism" asserted verbally with no prediction that the empirics confirm/reject
- Theory that merely restates the regression rather than disciplining it
- A model so general it predicts any sign of the estimate (unfalsifiable)

### Output format

```
【Estimated object】what economic primitive the coefficient maps to
【Frame level】verbal / stylized model / sufficient-statistic / structural
【Key prediction】the testable implication the data address
【Welfare/policy mapping】... (or "not applicable, by design")
【Broad lesson, made rigorous】...
【Next step】qje-robustness
```
