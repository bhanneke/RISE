<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/submission-disclosures.md -->

# `/submission-disclosures`

Generates the submission-time disclosure block: AI-use statement matched to the target journal policy, CRediT roles, conflict-of-interest and data-availability statements.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-06-10</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/submission-disclosures/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/submission-disclosures/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/submission-disclosures/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## /submission-disclosures — The Submission-Time Disclosure Block

Draft the four statements journals now require (or strongly expect) at submission, in one pass: **AI-use disclosure**, **CRediT contributor roles**, **conflict-of-interest**, and **data availability**. Journals tightened AI-use policies through 2025–2026; an undisclosed-AI finding at a top journal is now a research-integrity problem, not a formatting one — so the statement should be drafted *deliberately*, not improvised in the submission portal at midnight.

**This skill is about the author's disclosures TO the journal.** It is unrelated to `/disclosure-check`, which screens restricted-data *outputs* for statistical-disclosure risk (small cells, PII). Same word, different worlds.

### When to use

- Preparing a submission or resubmission package and the portal asks for AI-use / COI / data-availability statements.
- A revise-and-resubmit at a journal that adopted an AI policy since the original submission.
- A coauthor asks "do we need to say we used Claude/Copilot/ChatGPT on this?"

### Phases

#### Phase 1 — Resolve the journal's actual policy

1. If a journal short-name is given, read its profile in `journal-profiles.md` (top-5 econ + AEA-imprint policy notes + poli-sci top-3).
2. **Verify the current policy on the journal's own site** (`WebSearch`/`WebFetch`: "<journal> artificial intelligence policy authors", the journal's submission guidelines page). Policies moved fast in 2025–2026; a cached or remembered policy is not good enough for a submission. Record the URL and retrieval date in the output.
3. If no explicit AI policy exists, default to the strictest common denominator (disclose tools, scope of use, and human responsibility) — over-disclosure is free; under-disclosure is not.

#### Phase 2 — Inventory what was actually used

Interview briefly (or infer from the repo when evident — e.g. `quality_reports/`, session logs, a CLAUDE.md):

- **Which tools** (Claude Code, Copilot, ChatGPT, Grammarly-class) and **for what**: writing/editing prose, code authoring, code review, literature search, data analysis, translation.
- **What stayed human**: research design, identification choices, interpretation, final verification of every number and citation (tie to the repo's own verification story — `/audit-reproducibility`, `/verify-claims` — when true, *say so*: "all AI-assisted numbers were independently verified against code" is a strength, not a confession).
- **What AI was NOT used for** when the journal cares (e.g., most policies bar AI as a listed author and bar undisclosed AI-generated images/data).

#### Phase 3 — Draft the four statements

Write `quality_reports/submission_disclosures_[manuscript-slug].md` containing:

1. **AI-use disclosure** — journal-matched wording: tools + versions, scope of use, the affirmation that authors take full responsibility for all content and verified all AI-assisted output. Honest and specific; never boilerplate that overclaims ("no AI was used") when the repo's own logs say otherwise.
2. **CRediT roles** — the 14-role taxonomy mapped to each author (interview for the mapping; flag roles no author holds).
3. **Conflict-of-interest** — funding sources, paid/unpaid positions, data-provider relationships (IRB/data-use agreements often constrain what must be stated; cross-ref `confidential-data.md`).
4. **Data availability** — aligned with the replication deposit: openICPSR/DCAS language when the target is an AEA-imprint journal (delegate the deposit itself to `/replication-package`; restricted-data access language per `confidential-data.md`).

With `--statements-only`, emit the statements to chat without writing the file. With `--no-ai`, skip statement 1 (the user asserts no AI assistance — note in chat that the repo's own session logs may contradict this, if they visibly do).

#### Phase 4 — Parity check against the manuscript

Grep the manuscript for an existing acknowledgments/disclosure section; flag contradictions (e.g., the paper thanks "research assistance" that the COI omits, or an existing AI statement that the new one contradicts). Do not silently overwrite — surface the diff.

### Exit behavior

- **Statements drafted, policy verified:** write the file, print the four statements + the policy URL/date, and remind the user the statements are drafts for *author* review — sign-off is theirs.
- **Journal policy unverifiable** (site unreachable, no policy found): emit the strict-default statements, clearly marked "default wording — verify against the journal's current author guidelines before submission."
- **Inventory contradicts `--no-ai`:** stop and surface the contradiction; never produce a false "no AI" statement.

### Flags

- `--no-ai` — Skip the AI-use statement (user asserts none was used). The skill still warns if repo evidence visibly contradicts the assertion.
- `--statements-only` — Print the statements to chat; write no file.

### Cross-references

- `.claude/skills/disclosure-check/SKILL.md` — statistical-disclosure screening of restricted-data outputs (the other "disclosure"; unrelated).
- `.claude/skills/replication-package/SKILL.md` — the deposit the data-availability statement must match.
- `.claude/references/journal-profiles.md` — per-journal calibration, incl. the AEA DCAS policy note.
- `.claude/rules/confidential-data.md` — restricted-data constraints on what the statements can say.
- `.claude/skills/humanize/SKILL.md` — detecting AI-voice in prose; disclosure and voice are separate obligations.

### What this skill does NOT do

- **Screen outputs for statistical disclosure risk** — that is `/disclosure-check`.
- **Build the replication deposit** — that is `/replication-package`; this skill only writes the statement that points at it.
- **Decide your ethics.** It drafts honest statements from what you report and what the repo shows; whether a use *needed* disclosing under a vague policy is the author's call — the skill defaults to disclosure when in doubt.
- **Submit anything.** Statements go in the user's submission package by the user's hand.
