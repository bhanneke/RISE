<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-rebuttal.md -->

# `qje-rebuttal`

Structures the revision and response letter when a QJE decision letter arrives (R&R or reject-and-resubmit); routes re-analysis to the relevant qje-* skill rather than redoing it.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>revision</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-rebuttal/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-rebuttal/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-rebuttal/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Rebuttal & Revision (qje-rebuttal)

### When to trigger

- A QJE decision letter arrived: revise-and-resubmit, or a conditional/major revision
- You have referee reports and need a response strategy
- You are unsure how to prioritize conflicting referee demands
- The revised manuscript exists and you need to draft the response letter

### QJE reality: few rounds, high stakes

At an unconditional acceptance rate of only **~1-4%**, an R&R from one of QJE's five Harvard-based Editors is a rare and valuable signal — treat it as a near-final opportunity and address everything substantive in this round rather than negotiating across many. The **handling Editor's letter is the contract**: at QJE a single Editor (not a co-editor + AE layer) owns the decision, so that letter tells you which referee points are binding and which are optional. Read it first and let it set priorities.

### Triage protocol

1. **Decode the Editor.** The Editor's letter ranks the issues. A point the Editor underscores is binding; a point only one referee raised and the Editor ignored is lower priority (but still answer it).
2. **Classify every comment.** For each referee point, tag it: *fundamental* (must add analysis), *clarification* (rewrite/explain), or *disagreement* (you will push back, politely, with evidence).
3. **Sequence the work.** Do the analysis first (route fundamentals to `qje-identification` / `qje-robustness` / `qje-theory-model`), update exhibits, *then* write the letter — never write the letter before the manuscript reflects the changes.
4. **Never pick a fight you can win with a robustness check.** If a check settles it, run the check; reserve disagreement for points where the referee is genuinely mistaken.

### Response-letter structure

- **Opening**: thank the Editor and referees; summarize the main changes in a short paragraph.
- **Point-by-point**: quote each comment, then respond. Each response = what you did + where in the revised paper it now appears (section/table/figure/page).
- **Disagreements**: state the referee's point fairly, then give the evidence-based reason you respectfully differ; offer a compromise (e.g., added to the appendix) where possible.
- **Tone**: gracious, concrete, never defensive. Show the referees made the paper better.
- **Change log**: optionally include a brief summary of all changes up front for the Editor's convenience.

### Checklist

- [ ] Editor's priorities decoded and used to rank responses
- [ ] Every referee comment classified (fundamental / clarification / disagreement)
- [ ] All fundamental requests resolved with actual new analysis, not promises
- [ ] Each response cites the exact location of the change in the revised paper
- [ ] Disagreements are evidence-based, fair, and offer a compromise
- [ ] Tone is gracious and concrete throughout
- [ ] Revised manuscript updated *before* the letter was written
- [ ] No new over-claiming introduced while answering reviewers

### Anti-patterns

- Writing the response letter before the manuscript actually reflects the changes
- Promising future work instead of doing the analysis this round (rounds are scarce at ~1-4% acceptance)
- Arguing with a referee where a quick robustness check would settle it
- Defensive or curt tone; treating reports as attacks rather than help
- Answering only the easy points and hand-waving the hard one the Editor flagged
- Vague responses ("we have addressed this") with no location in the paper

### Output format

```
【Decision】R&R / major / conditional
【Editor's binding points】[...]
【Comment classification】fundamental: [...] / clarification: [...] / disagreement: [...]
【Analysis routed to】qje-identification / qje-robustness / qje-theory-model (as needed)
【Letter status】point-by-point with locations? [Y/N]
【Tone check】gracious + concrete? [Y/N]
【Next step】resubmit the single PDF via Editorial Express (qje-submission for file checks)
```
