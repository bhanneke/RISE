<!-- DO NOT EDIT — auto-copied from skills/aris/details/patent-review.md -->

# `patent-review`



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
name: patent-review
description: "Get an external patent examiner review of a patent application. Use when user says \"专利审查\", \"patent review\", \"审查意见\", \"examiner review\", or wants critical feedback on patent claims and specification."
argument-hint: [patent-directory-or-scope]
allowed-tools: Bash(*), Read, Grep, Glob, Write, Edit, Agent, mcp__codex__codex, mcp__codex__codex-reply
---

# Patent Examiner Review via Codex MCP (xhigh reasoning)

Get a multi-round patent examiner review of the patent application based on: **$ARGUMENTS**

Adapted from `/research-review`. The reviewer persona is a patent examiner, not a paper reviewer.

## Constants

- `REVIEWER_MODEL = gpt-5.5` — Model used via Codex MCP
- `REVIEW_ROUNDS = 2` — Number of review rounds
- `EXAMINER_PERSONA = "patent-examiner"` — GPT-5.4 persona

## Prerequisites

- Codex MCP Server configured:
  ```bash
  claude mcp add codex -s user -- codex mcp-server
  ```

## Inputs

1. `patent/CLAIMS.md` — all drafted claims
2. `patent/specification/` — all specification sections
3. `patent/figures/numeral_index.md` — reference numeral mapping
4. `patent/PRIOR_ART_REPORT.md` — known prior art
5. `patent/INVENTION_DISCLOSURE.md` — invention structure

## Workflow

### Step 1: Gather Patent Context

Before calling the external reviewer, compile a comprehensive briefing:
1. Read all claims (independent + dependent)
2. Read specification sections (at least summary and detailed description)
3. Read prior art report for context
4. Identify: core inventive concept, claim scope, known prior art, target jurisdiction

### Step 2: Round 1 — Full Examiner Review

Send to `REVIEWER_MODEL` via `mcp__codex__codex` with xhigh reasoning:

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are a senior patent examiner at the [USPTO/CNIPA/EPO].
    Examine this patent application and issue a detailed office action.

    CLAIMS:
    [all claims]

    SPECIFICATION SUMMARY:
    [key sections: title, technical field, background, summary, abstract]

    PRIOR ART KNOWN:
    [prior art references]

    PATENTABILITY STANDARDS TO APPLY:
    [US: 35 USC 101/102/103/112 | CN: Articles 22, 26 | EP: Articles 54, 56, 83, 84]

    Please issue an office action covering:

    1. CLAIM CLARITY (112(b)/Art 84):
       - Are all terms definite?
       - Any indefinite functional language?
       - Antecedent basis issues?

    2. WRITTEN DESCRIPTION (112(a)/Art 83 first para):
       - Does the spec support ALL claim scope?
       - Any claim elements without spec support?

    3. ENABLEMENT (112(a)/Art 83):
       - Can a POSITA practice the invention?
       - Any missing algorithm/structure for functional claims?

    4. NOVELTY (102/Art 54):
       - Would any known reference anticipate any claim?
       - Identify the closest single reference.

    5. NON-OBVIOUSNESS (103/Art 56):
       - Would any combination render claims obvious?
       - What is the motivation to combine?

    6. CLAIM SCOPE:
       - Are independent claims broad enough to be commercially valuable?
       - Do dependent claims provide meaningful fallback positions?
       - Any claims that are too broad (likely rejected) or too narrow (not valuable)?

    7. SPECIFICATION QUALITY:
       - Language issues (subjective terms, relative terms, result-to-be-achieved)
       - Reference numeral consistency
       - Missing embodiments

    Format your response as a formal office action with:
    - GROUNDS OF REJECTION for each issue (cite statute)
    - SUGGESTED AMENDMENTS for each issue
    - OVERALL PATENTABILITY SCORE: 1-10

    Be rigorous and specific. This is a real examination.
```

### Step 3: Implement Fixes (Round 1)

Based on the examiner's office action:

1. **CRITICAL issues** (102 rejection, 112 indefiniteness, missing enablement):
   - Must be fixed before proceeding
   - Amend claims or add specification support

2. **MAJOR issues** (103 obviousness, weak claim scope, missing support):
   - Should be fixed or argued
   - Consider claim amendments or specification additions

3. **MINOR issues** (language quality, numeral consistency, formatting):
   - Fix if time permits
   - Document in output for later cleanup

For each fix:
- Show the specific change (old claim -> new claim)
- Explain how the fix addresses the examiner's concern

### Step 4: Round 2 — Follow-Up Review

Use `mcp__codex__codex` with the threadId from Round 1:

```
mcp__codex__codex:
  threadId: [from Round 1]
  prompt: |
    Here is the revised patent application after addressing your office action.

    CHANGES MADE:
    [list of all changes with rationale]

    REVISED CLAIMS:
    [updated claims]

    REVISED SPECIFICATION EXCERPTS:
    [changed sections]

    Please re-examine:
    1. Are the previous rejections overcome?
    2. Are there new issues introduced by the amendments?
    3. What is the updated patentability score?
    4. Any remaining grounds for rejection?
```

### Step 5: Generate Improvement Report

Write `patent/PATENT_REVIEW.md`:

```markdown
## Patent Review Report

### Application Summary
[Title, claims count, jurisdiction]

### Review Round 1
#### Office Action Summary
[Key findings from examiner]

#### Issues Found
| # | Type | Severity | Claim/Section | Issue | Citation | Fix Applied |
|---|------|----------|--------------|-------|----------|-------------|
| 1 | Clarity | CRITICAL | Claim 3 | Indefinite term "rapid" | 112(b) | Defined in spec |
| 2 | Novelty | MAJOR | Claim 1 | Ref X anticipates element C | 102 | Amended claim |

#### Score After Round 1: [X]/10

### Review Round 2
#### Follow-Up Assessment
[Are previous rejections overcome?]

#### Remaining Issues
[Any issues still outstanding]

#### Score After Round 2: [X]/10

### Recommendations
[Final recommendations before proceeding to jurisdiction formatting]
- [ ] All CRITICAL issues resolved
- [ ] All MAJOR issues resolved or argued
- [ ] Specification supports all claim amendments
- [ ] Ready for jurisdiction formatting
```

## Key Rules

- The reviewer persona must be a patent examiner, not a paper reviewer or academic.
- Always use `model_reasoning_effort: "xhigh"` for maximum analysis depth.
- Address CRITICAL and MAJOR issues before proceeding to the next phase.
- Document all changes in the review report for traceability.
- If the patentability score is below 5/10 after Round 2, recommend significant rework before filing.
- The review is advisory -- actual prosecution may proceed differently.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/patent-review/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>review</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/patent-review/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
