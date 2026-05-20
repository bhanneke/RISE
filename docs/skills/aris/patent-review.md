<!-- DO NOT EDIT — auto-copied from skills/aris/details/patent-review.md -->

# `patent-review`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/patent-review/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/patent-review/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Patent Examiner Review via Codex MCP (xhigh reasoning)

Get a multi-round patent examiner review of the patent application based on: **$ARGUMENTS**

Adapted from `/research-review`. The reviewer persona is a patent examiner, not a paper reviewer.

### Constants

- `REVIEWER_MODEL = gpt-5.5` — Model used via Codex MCP
- `REVIEW_ROUNDS = 2` — Number of review rounds
- `EXAMINER_PERSONA = "patent-examiner"` — GPT-5.4 persona

### Prerequisites

- Codex MCP Server configured:
  ```bash
  claude mcp add codex -s user -- codex mcp-server
  ```

### Inputs

1. `patent/CLAIMS.md` — all drafted claims
2. `patent/specification/` — all specification sections
3. `patent/figures/numeral_index.md` — reference numeral mapping
4. `patent/PRIOR_ART_REPORT.md` — known prior art
5. `patent/INVENTION_DISCLOSURE.md` — invention structure

### Workflow

#### Step 1: Gather Patent Context

Before calling the external reviewer, compile a comprehensive briefing:
1. Read all claims (independent + dependent)
2. Read specification sections (at least summary and detailed description)
3. Read prior art report for context
4. Identify: core inventive concept, claim scope, known prior art, target jurisdiction

#### Step 2: Round 1 — Full Examiner Review

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

#### Step 3: Implement Fixes (Round 1)

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

#### Step 4: Round 2 — Follow-Up Review

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

#### Step 5: Generate Improvement Report

Write `patent/PATENT_REVIEW.md`:

```markdown
### Patent Review Report

#### Application Summary
[Title, claims count, jurisdiction]

#### Review Round 1
#### Office Action Summary
[Key findings from examiner]

#### Issues Found
| # | Type | Severity | Claim/Section | Issue | Citation | Fix Applied |
|---|------|----------|--------------|-------|----------|-------------|
| 1 | Clarity | CRITICAL | Claim 3 | Indefinite term "rapid" | 112(b) | Defined in spec |
| 2 | Novelty | MAJOR | Claim 1 | Ref X anticipates element C | 102 | Amended claim |

#### Score After Round 1: [X]/10

#### Review Round 2
#### Follow-Up Assessment
[Are previous rejections overcome?]

#### Remaining Issues
[Any issues still outstanding]

#### Score After Round 2: [X]/10

#### Recommendations
[Final recommendations before proceeding to jurisdiction formatting]
- [ ] All CRITICAL issues resolved
- [ ] All MAJOR issues resolved or argued
- [ ] Specification supports all claim amendments
- [ ] Ready for jurisdiction formatting
```

### Key Rules

- The reviewer persona must be a patent examiner, not a paper reviewer or academic.
- Always use `model_reasoning_effort: "xhigh"` for maximum analysis depth.
- Address CRITICAL and MAJOR issues before proceeding to the next phase.
- Document all changes in the review report for traceability.
- If the patentability score is below 5/10 after Round 2, recommend significant rework before filing.
- The review is advisory -- actual prosecution may proceed differently.
