<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-robustness.md -->

# `qje-robustness`

Plans and prioritizes the robustness suite and online appendix QJE referees expect, exploiting the journal's no-page-limit norm, without changing the core identification design.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-robustness/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-robustness/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-robustness/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Robustness & Online Appendix (qje-robustness)

### When to trigger

- The main result exists but the robustness section / online appendix is thin
- You want to pre-empt the "what about X?" referee report
- You are unsure which checks are load-bearing vs. padding
- The appendix is a pile of tables with no organizing logic

### QJE expectation: an exhaustive, organized appendix

QJE imposes **no hard page limit** and the modern QJE empirical paper carries a **very extensive online appendix** — the Chetty–Hendren neighborhoods papers (QJE 2018) and Chetty–Hendren–Kline–Saez (QJE 2014) are the genre standard, with online appendices dwarfing the printed text. A short robustness section signals an unfinished paper. But volume is not the goal — *anticipation* is. The appendix should answer, in advance, every serious threat a smart referee would raise, organized so the handling Editor can find each answer fast. Note: at submission everything ships in **one PDF** (no separate appendix file at the initial stage), so the appendix must be cleanly sectioned within that document. Lead with the checks that defend the **identifying assumption**, then **measurement**, then **specification**.

### Robustness priority ladder (defend in this order)

1. **Identification threats first.** The checks that defend exogeneity: pre-trends, placebo timing/outcomes, falsification where the channel is absent, alternative control groups, donor-pool / synthetic checks. These are not optional.
2. **Selection & sample.** Attrition, sample-definition sensitivity, alternative inclusion windows, trimming/winsorizing, outlier robustness.
3. **Measurement.** Alternative outcome/treatment definitions, alternative data sources, measurement-error bounds.
4. **Specification.** Functional form, fixed-effects structure, controls in/out (and a discussion that the estimate is not control-sensitive), clustering alternatives.
5. **Inference.** Wild-cluster bootstrap with few clusters, randomization inference, multiple-hypothesis corrections across outcomes/subgroups.
6. **Magnitude & external validity.** Benchmark the effect size against the literature; show where the result does and does not extend.

### What goes in the body vs. the appendix

| Goes in the main text                                  | Goes in the online appendix (same PDF at submission)     |
|--------------------------------------------------------|----------------------------------------------------------|
| The one or two checks that *make or break* the design  | The full battery of alternative specs                    |
| The headline robustness figure (e.g., event study)     | All variant tables, by category                          |
| A sentence summarizing each appendix result            | Data construction, variable definitions, extra proofs    |

### Execution bridge (StatsPAI / Stata MCP)

Run the robustness battery, don't just enumerate it. Full map:
`shared-resources/empirical-methods/execution-with-mcp.md`. QJE instantiation:

- **Many outcomes / specifications:** `romano_wolf` (step-down, FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold, not
  a grid of naive stars.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — quantify the confounder strength
  that would overturn the headline.
- **Inference:** `wild_cluster_bootstrap` with few clusters; `twoway_cluster` /
  `conley` where the dependence structure demands it.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` to run for each — no guessing the battery.
- **Emit appendix-ready exhibits** with `etable` / `did_summary_to_latex`.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix; preserve the scripts for `qje-replication-package`.

### Checklist

- [ ] Every identification threat has a corresponding check, named and reported
- [ ] Pre-trends / placebo / falsification evidence is in the body, not buried
- [ ] Estimate shown to be insensitive to reasonable specification choices
- [ ] Few-cluster / multiple-hypothesis inference handled
- [ ] Appendix is organized by threat category, not dumped chronologically
- [ ] Appendix is cleanly sectioned within the single submission PDF
- [ ] Each appendix result is referenced and one-line-summarized in the main text
- [ ] Magnitudes benchmarked against prior estimates in the literature

### Anti-patterns

- A two-paragraph robustness section in a paper claiming a causal effect (QJE's no-page-limit norm leaves no excuse)
- Appendix tables with no narrative linking them to specific threats
- Reporting only the checks that pass; hiding the fragile specification
- "Results are robust to a battery of checks (see Appendix)" with no specifics in text
- Padding the appendix with redundant specifications instead of addressing real threats

### Output format

```
【Identification checks】[pre-trends, placebo, falsification, alt controls, ...]
【Selection/sample checks】[...]
【Measurement checks】[...]
【Specification checks】[...]
【Inference checks】[wild-cluster, RI, MHT, ...]
【Body vs. appendix split】what stays in text
【Gaps to close】[...]
【Next step】qje-tables-figures
```
