<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/verify-claims.md -->

# `/verify-claims`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/verify-claims/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/verify-claims/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/verify-claims/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## /verify-claims — Chain-of-Verification on a Draft

Fact-check a draft using the **Post-Flight Verification protocol** (`.claude/rules/post-flight-verification.md`).

**Input:** `$ARGUMENTS` — path to a file containing the draft (markdown, .qmd, .tex, .md) or a shorthand pointer. Optional flags:

- `--source <path-or-url>` — one or more source-material pointers (repeat for multiple). If omitted, the skill infers from context (e.g., papers referenced, cited arXiv URLs).
- `--no-fail-closed` — downgrade FAIL outcomes to warnings without regeneration. Use sparingly.

### When to pick this skill

- **`/verify-claims`** (this skill) — ad-hoc fact-checking on any draft or text block the user hands you. One-shot, user-invoked.
- **Other skills that auto-run Post-Flight internally** (`/lit-review`, `/research-ideation`, `/respond-to-referees`, `/review-paper --peer`) — no need to call this separately; they already run it.
- **`/proofread`** — grammar, typos, overflow. Different lens.
- **`/review-paper`** (default mode) — full manuscript review, not just claim verification.
- **`/validate-bib`** — checks citations *exist* and are well-formed (structural + DOI). This skill checks they *hold* (the cited paper supports the attributed claim). Complementary — run both before submission.

### How it works

Implements the 4-step CoVe loop from Dhuliawala et al. 2023 ([arXiv:2309.11495](https://arxiv.org/abs/2309.11495)), with architectural enforcement of the fresh-context independence trick.

#### Phase 0 — Pre-Flight

Confirm:
- Draft file exists and is readable
- At least one source pointer available (either `--source` or auto-detected from draft)
- `claim-verifier` agent file exists at `.claude/agents/claim-verifier.md`

If any fail → surface the failure, do NOT proceed.

#### Phase 1 — Extract claims

Read the draft. Identify factual assertions of these types:

| Type | Example |
|------|---------|
| Citation | "Smith (2019, *JEL*) shows X" |
| Numerical fact | "N = 10,000", "ATT = 0.42" |
| Negative literature | "No prior work studies X" |
| Named entity | researcher, paper title, venue, package, estimator name |
| Dataset claim | "The CPS contains field `educ_attain`" |

Skip: opinions, forward-looking suggestions, definitions the draft introduces.

**For citation-type claims, extract the claim↔citation PAIR — not just the citation.** Capture *what* the draft attributes to *which* work, so the verifier checks **appropriateness** (does Smith 2019 actually *show* X?), not merely existence. "Smith (2019) shows a positive wage effect" becomes `{cite: Smith2019, attributed: "positive wage effect"}`. This is the layer `/validate-bib` explicitly defers here: validate-bib confirms the citation *exists and is well-formed*; this skill confirms it *holds*. A mis-citation (the paper exists but says something else, or the opposite) is exactly a numeric/directional contradiction → HIGH-WARN unless a concrete `author_alternative` is recorded (then EXPLAINED).

Output a claims table:

```markdown
| ID | Claim | Source hint |
|----|-------|-------------|
| C1 | ... | ... |
```

#### Phase 2 — Generate verification questions

One question per claim. Make it specific and answerable from the source alone.

#### Phase 3 — Spawn `claim-verifier` (fresh context — never a conversation fork)

```
Agent: subagent_type=claim-verifier   # a named subagent starts fresh; a /fork copy would inherit the draft
Prompt: hand over claims table + verification questions + source material pointers.
        Do NOT include the draft text.
```

The forked agent runs the CoVe independent-answer step. It has never seen the draft and cannot confirm-bias. It returns a structured verification report.

#### Phase 4 — Reconcile

The verifier returns a per-claim verdict in one of these severity tiers:

- **HIGH-WARN** — fabricated reference (the cited paper doesn't exist at the named venue/year), draft claim directly contradicted by the source, or `not_found` retrieval that the verifier interprets as a hallucinated citation. **Fail closed** — surface these first and never present the draft as verified while one stands. This is a reporting rule, not a mechanical gate: nothing in `/commit` or the pre-commit hook reads these verdicts, so the author decides, and a HIGH-WARN left in place is stated in the report the user sees.
- **MED-WARN** — transient infrastructure / retrieval failure (paywall the verifier can normally bypass via cached metadata; DOI resolver timeout; partial PDF read). Surface for the author; do not gate-refuse.
- **LOW-WARN** — source genuinely inaccessible (paywalled and not in cache; private dataset; pre-print server transient). Surface with `cannot-verify` flag; do not gate-refuse.
- **EXPLAINED** (v2.0) — a numeric/directional contradiction the author has *pre-justified* with a concrete named alternative (different defensible edition, specification, sample, or rounding convention), passed to the verifier via the claim's `author_alternative` field. Surfaced with the evidence and the recorded reason; **non-gating**. The hard floor holds: a *fabricated* citation is never EXPLAINED, and a blank/vague alternative stays HIGH-WARN. This mirrors `audit-reproducibility`'s EXPLAINED disposition for numeric claims — a mismatch is not always a failure when a defensible alternative is named.

Verdict aggregation by tier across all extracted claims (EXPLAINED counts as non-gating, like LOW):

| Tier counts | Outcome | What the report says |
|---|---|---|
| 0 HIGH, 0 MED, ≥ 0 LOW/EXPLAINED | **PASS** (green block) | draft verified |
| 0 HIGH, ≥ 1 MED, any LOW/EXPLAINED | **PARTIAL** (yellow block) | verified with warnings |
| ≥ 1 HIGH | **FAIL** (red block) | **never reported as verified** while a HIGH-WARN stands (unless `--no-fail-closed`) |

`--no-fail-closed` reports HIGH-WARN verdicts as ordinary warnings instead of failing closed. Use sparingly — it's there for offline / hallucination-sensitive contexts where the user accepts the risk in writing.

If the draft is writeable and the user asked for auto-correction, regenerate the affected sections using the verifier's evidence. Otherwise return the report and let the user decide.

### Example

```
/verify-claims quality_reports/lit-review_measurement-error.md --source master_supporting_docs/author_2021_method.pdf --source master_supporting_docs/coauthor_2020_survey.pdf
```

Expected output (abridged):

```markdown
### Post-Flight Verification — lit-review_measurement-error.md

**Claims extracted:** 14
**Verified independently:** 14 (fresh-context claim-verifier)
**Outcome:** FAIL — 12 verified, 1 contradicted by its source (HIGH-WARN), 1 unverifiable (LOW-WARN); the draft is not reported as verified until C7 is corrected

#### Discrepancies

- **C7** — draft claims "Coauthor (2020) *proposes* a bias-corrected estimator." Source Section 4 shows they propose a weighting estimator, not a bias-corrected one. Recommend correction.

#### Unverifiable

- **C12** — draft cites "Third Author et al. 2024 (working paper)". No canonical URL in provided sources. Recommend user supply DOI or arXiv link.

#### Verified

| ID | Claim | Evidence |
|----|-------|----------|
| C1 | "Author 2021 defines the calibration constant as a ratio of moments" | p. 5, eq. (3) |
| ... | ... | ... |
```

### Fail modes and recovery

**Verifier times out:** surface a warning block, return draft as provisional. Do not silently ship.

**Source material inaccessible** (paywall, 404): report the specific claims that hinge on it, flag as `cannot-verify`, recommend user supply an alternative source.

**Draft contains only opinions / forward-looking text:** report "no verifiable factual claims extracted — nothing to check" and return.

### Cross-references

- `.claude/agents/claim-verifier.md` — the fresh-context verifier.
- `.claude/rules/post-flight-verification.md` — the protocol.
- MEMORY.md `[LEARN:pattern]` on Chain-of-Verification vs critic-fixer vs cross-artifact review.
