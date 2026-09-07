<!-- DO NOT EDIT — auto-copied from skills/ai-research-feedback/details/audit-analysis.md -->

# `/audit-analysis`

Hands a diff of changed empirical code to an isolated subagent instructed to break it: N before and after every filter, merge, and collapse taken from logs; merge keys, uniqueness, and the fate of unmatched observations; variable units, logs versus levels, deflation, lag alignment; silent failures such as missings coerced to zero, `destring ... force`, and `fillna(0)`; and the clustering level and what the fixed effects absorb. Every finding must quote a file and line and is tagged CONFIRMED or SUSPECTED; nothing is written to the repository.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-research-feedback/">AI Research Feedback (Claes Bäckman)</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-08-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>code-generation</code> · <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/claesbackman/AI-research-feedback/contents/Skills/audit-analysis/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-research-feedback/audit-analysis/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/audit-analysis/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/claesbackman/AI-research-feedback?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Audit Analysis Code

Find errors in changed empirical code before a referee does.

The audit runs in a subagent with a clean context. That isolation is the point: whoever wrote the code — including this session, if it helped — must not be able to steer the findings. Do not read the changed files yourself before launching, do not form a view, and do not answer the auditor's questions mid-run.

### Phase 1: Establish scope

Set `BASE` from `$ARGUMENTS` if given, otherwise `main`.

Run, and stop with a short explanation if any of the first three fail:

- `git rev-parse --git-dir` — must be a repository
- `git rev-parse --verify BASE` — the base ref must exist
- `git diff --stat BASE` — if empty, there is nothing to audit
- `git log BASE..HEAD --oneline` — may legitimately be empty when the work is uncommitted, or when HEAD is BASE and only the working tree has changed. Note it and drop the commit-message check from the audit.

Report to the user in two or three lines: base ref, number of changed files, number of changed lines, and whether commit messages are available. Then launch immediately.

### Phase 2: Launch the auditor

One `Agent` call, `subagent_type: "general-purpose"`. Substitute `BASE` and pass this verbatim:

> Review empirical research code adversarially. The author wants it broken now
> rather than by a referee. Read `git log BASE..HEAD` and `git diff BASE`, then
> the changed files in full. Follow variables built outside the diff.
>
> Check, and report on each of:
> - Claims vs. code: do comments and commit messages match what runs? Quote
>   both sides of any disagreement.
> - Sample: N before and after every filter, merge, and collapse. Take N from
>   logs; write "N unverified" where there is no log. Flag undocumented drops.
> - Merges: key, uniqueness on the side that needs it, fate of unmatched
>   observations, whether `_merge` is inspected, duplicate id-period pairs after.
> - Variables: trace every regressor and outcome. Units, logs vs. levels,
>   deflation, lag alignment. Does construction match the name?
> - Silent failures: missings coerced to zero, `if x > 0` true on missing,
>   `destring ... force`, `replace` that changes nothing, loops that skip.
>   In Python, `fillna(0)`, silent dtype coercion, chained assignment.
> - Estimation: clustering level and cluster count, what the fixed effects
>   absorb, weights, whether estimation N matches the sample traced above.
>
> Each finding: file, line, quoted excerpt, what is wrong, consequence for the
> results. Tag CONFIRMED (visible in the code) or SUSPECTED (needs the data).
> Style and naming are not findings. Order by consequence, worst first, ten max.
> Then one line per category: what you found, or that you found nothing. Close
> with the one thing you could not check without the data. Change nothing.

If the diff exceeds roughly 1,500 changed lines, run two auditors in parallel instead — one taking claims, sample, and merges, the other taking variables, silent failures, and estimation — and concatenate their findings. Do not split a smaller diff; the categories inform each other.

### Phase 3: Relay without softening

Pass the findings through in the order returned, worst first. Do not reclassify a SUSPECTED finding as fine, do not add reassurance, and do not open with what the code gets right. The user asked for errors.

Drop any finding that lacks a file, a line, and a quoted excerpt, and tell the user how many you dropped. Unanchored findings are the failure mode this design exists to catch — an auditor told to find errors will manufacture them if nothing forces it to point at code.

Reproduce the per-category coverage lines verbatim, including the categories that came back clean, and the closing line about what could not be checked without the data. A clean category is a claim the auditor is on the record for.

Fix nothing. If the user wants repairs, that is a separate request.
