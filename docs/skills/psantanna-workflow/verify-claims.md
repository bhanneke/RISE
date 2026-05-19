<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/verify-claims.md -->

# `/verify-claims`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

---
name: verify-claims
description: Run Chain-of-Verification (CoVe) on a draft or a block of text with factual claims. Spawns the `claim-verifier` agent in a forked (fresh) context so it never sees the draft — then reports which claims are supported, contradicted, or unverifiable. Use when user says "verify these citations", "check the claims in X", "did I hallucinate anything", "fact-check this draft", "run CoVe on this", or after any text generation that asserts facts about papers, datasets, or numerical results. NOT for style/grammar review (use `/proofread`) or substance review (use `/review-paper`).
argument-hint: "[file-or-text-path] [--source <path-or-url>] [--no-fail-closed]"
allowed-tools: ["Read", "Grep", "Glob", "Task", "Write"]
---

# /verify-claims — Chain-of-Verification on a Draft

Fact-check a draft using the **Post-Flight Verification protocol** ([`.claude/rules/post-flight-verification.md`](../../rules/post-flight-verification.md)).

**Input:** `$ARGUMENTS` — path to a file containing the draft (markdown, .qmd, .tex, .md) or a shorthand pointer. Optional flags:

- `--source <path-or-url>` — one or more source-material pointers (repeat for multiple). If omitted, the skill infers from context (e.g., papers referenced, cited arXiv URLs).
- `--no-fail-closed` — downgrade FAIL outcomes to warnings without regeneration. Use sparingly.

## When to pick this skill

- **`/verify-claims`** (this skill) — ad-hoc fact-checking on any draft or text block the user hands you. One-shot, user-invoked.
- **Other skills that auto-run Post-Flight internally** (`/lit-review`, `/research-ideation`, `/respond-to-referees`, `/review-paper --peer`) — no need to call this separately; they already run it.
- **`/proofread`** — grammar, typos, overflow. Different lens.
- **`/review-paper`** (default mode) — full manuscript review, not just claim verification.

## How it works

Implements the 4-step CoVe loop from Dhuliawala et al. 2023 ([arXiv:2309.11495](https://arxiv.org/abs/2309.11495)), with architectural enforcement of the fresh-context independence trick.

### Phase 0 — Pre-Flight

Confirm:
- Draft file exists and is readable
- At least one source pointer available (either `--source` or auto-detected from draft)
- `claim-verifier` agent file exists at `.claude/agents/claim-verifier.md`

If any fail → surface the failure, do NOT proceed.

### Phase 1 — Extract claims

Read the draft. Identify factual assertions of these types:

| Type | Example |
|------|---------|
| Citation | "Smith (2019, *JEL*) shows X" |
| Numerical fact | "N = 10,000", "ATT = 0.42" |
| Negative literature | "No prior work studies X" |
| Named entity | researcher, paper title, venue, package, estimator name |
| Dataset claim | "The CPS contains field `educ_attain`" |

Skip: opinions, forward-looking suggestions, definitions the draft introduces.

Output a claims table:

```markdown
| ID | Claim | Source hint |
|----|-------|-------------|
| C1 | ... | ... |
```

### Phase 2 — Generate verification questions

One question per claim. Make it specific and answerable from the source alone.

### Phase 3 — Spawn `claim-verifier` (forked, fresh context)

```
Task: subagent_type=claim-verifier, context=fork
Prompt: hand over claims table + verification questions + source material pointers.
        Do NOT include the draft text.
```

The forked agent runs the CoVe independent-answer step. It has never seen the draft and cannot confirm-bias. It returns a structured verification report.

### Phase 4 — Reconcile

Based on the report:

- **PASS** (all claims match source): produce a green Post-Flight block and return.
- **PARTIAL** (unverifiable claims remain): produce a yellow block flagging which claims need manual review.
- **FAIL** (at least one contradiction): produce a red block listing discrepancies with evidence. If the draft is writeable and the user asked for auto-correction, regenerate the affected sections using the verifier's evidence. Otherwise return the report and let the user decide.

Respect `--no-fail-closed`: on FAIL, produce the warning but do not regenerate.

## Example

```
/verify-claims quality_reports/lit-review_staggered-did.md --source master_supporting_docs/callaway_santanna_2021.pdf --source master_supporting_docs/dechaisemartin_dhaultfoeuille_2020.pdf
```

Expected output (abridged):

```markdown
## Post-Flight Verification — lit-review_staggered-did.md

**Claims extracted:** 14
**Verified independently:** 14 (forked claim-verifier)
**Outcome:** PARTIAL — 12 verified, 1 discrepancy, 1 unverifiable

### Discrepancies

- **C7** — draft claims "de Chaisemartin & D'Haultfœuille (2020) *propose* a DR estimator." Source Section 4 shows they propose a weighting estimator, not DR. Recommend correction.

### Unverifiable

- **C12** — draft cites "Borusyak et al. 2024 (working paper)". No canonical URL in provided sources. Recommend user supply DOI or arXiv link.

### Verified

| ID | Claim | Evidence |
|----|-------|----------|
| C1 | "Callaway & Sant'Anna 2021 use group-time ATT" | p. 5, eq. (3) |
| ... | ... | ... |
```

## Fail modes and recovery

**Verifier times out:** surface a warning block, return draft as provisional. Do not silently ship.

**Source material inaccessible** (paywall, 404): report the specific claims that hinge on it, flag as `cannot-verify`, recommend user supply an alternative source.

**Draft contains only opinions / forward-looking text:** report "no verifiable factual claims extracted — nothing to check" and return.

## Cross-references

- [`.claude/agents/claim-verifier.md`](../../agents/claim-verifier.md) — the forked verifier.
- [`.claude/rules/post-flight-verification.md`](../../rules/post-flight-verification.md) — the protocol.
- MEMORY.md `[LEARN:pattern]` on Chain-of-Verification vs critic-fixer vs cross-artifact review.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/verify-claims/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>audit</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/verify-claims/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/verify-claims/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
