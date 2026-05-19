<!-- DO NOT EDIT — auto-copied from skills/aris/details/patent-novelty-check.md -->

# `patent-novelty-check`



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
name: patent-novelty-check
description: "Assess patent novelty and non-obviousness against prior art. Use when user says \"专利查新\", \"patent novelty\", \"可专利性评估\", \"patentability check\", or wants to evaluate if an invention is patentable."
argument-hint: [invention-description-or-brief-path]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent, WebSearch, WebFetch, mcp__codex__codex
---

# Patent Novelty and Non-Obviousness Check

Assess patentability of: **$ARGUMENTS**

Adapted from `/novelty-check` for patent legal standards. Research novelty is NOT the same as patent novelty.

## Constants

- `REVIEWER_MODEL = gpt-5.5` — Model used via Codex MCP for cross-model examiner verification
- `NOVELTY_STANDARD = patent` — Always use legal patentability standard, not research contribution standard

## Inputs

1. Invention description from `$ARGUMENTS`
2. `patent/PRIOR_ART_REPORT.md` (output of `/prior-art-search`)
3. `patent/INVENTION_BRIEF.md` if exists

## Shared References

Load `../shared-references/patent-writing-principles.md` for novelty/non-obviousness standards.
Load `../shared-references/patent-format-us.md` for 102/103 analysis framework.

## Workflow

### Step 1: Define Claim Elements

From the invention description, extract the key claim elements that would define the invention's scope:
1. List the technical features that make the invention novel
2. Identify which features are known from prior art vs. inventive
3. Draft preliminary claim language for 2-3 independent claims (method + system)

### Step 2: Anticipation Analysis (Novelty)

For each preliminary claim, test against EACH prior art reference in `PRIOR_ART_REPORT.md`:

**Single-reference test**: Does any single reference disclose ALL claim elements?

| Claim Element | Ref 1 | Ref 2 | Ref 3 | ... |
|--------------|-------|-------|-------|-----|
| Feature A | Yes/No + evidence | | | |
| Feature B | Yes/No + evidence | | | |
| Feature C | Yes/No + evidence | | | |
| Feature D | Yes/No + evidence | | | |

**Verdict per reference**:
- ANTICIPATED: One reference discloses every element → claim is not novel
- NOT ANTICIPATED: At least one element missing from every single reference → claim is novel

### Step 3: Obviousness Analysis (Inventive Step)

If the invention is novel (passes Step 2), test for obviousness:

**Two/three-reference combination test**: Can 2-3 references be combined to render the claim obvious?

For each combination of the top references:
1. **Primary reference**: Which reference is closest to the claimed invention?
2. **Secondary reference(s)**: Which reference(s) teach the missing element(s)?
3. **Motivation to combine**: Would a POSITA have reason to combine these references?
   - Explicit suggestion in the references themselves?
   - Same field, same problem?
   - Common design incentive?
   - Known technique for improving similar devices?

Format as a matrix:

| Combination | Primary | Secondary | Missing Elements | Motivation to Combine | Obvious? |
|-------------|---------|-----------|-----------------|----------------------|----------|
| Ref1 + Ref2 | Ref1 | Ref2 | Feature D | Same field, similar problem | Yes/No |

### Step 4: Cross-Model Examiner Verification

Call `REVIEWER_MODEL` via `mcp__codex__codex` with xhigh reasoning:

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are a senior patent examiner at the [USPTO/CNIPA/EPO].
    Examine the following invention for patentability.

    INVENTION: [invention description + preliminary claims]

    PRIOR ART: [prior art references with key teachings]

    Please analyze:
    1. Anticipation (novelty): Does any single reference anticipate any claim?
    2. Obviousness: Can any combination of references render claims obvious?
    3. Claim scope: Are the claims broad enough to be valuable?
    4. Recommended amendments if any claim is rejected.
    Be rigorous and cite specific references.
```

### Step 5: Jurisdiction-Specific Assessment

For each target jurisdiction, provide a patentability assessment:

**Under 35 USC 102/103 (US)**:
- Novelty: PASS / FAIL (cite specific reference if fail)
- Non-obviousness: PASS / FAIL (cite combination if fail)

**Under Article 22 CN Patent Law (CN)**:
- 新颖性 (Novelty): 通过 / 未通过
- 创造性 (Inventive Step): 通过 / 未通过

**Under Article 54/56 EPC (EP)**:
- Novelty: PASS / FAIL
- Inventive step: PASS / FAIL (problem-solution approach)

### Step 6: Output

Write `patent/NOVELTY_ASSESSMENT.md`:

```markdown
## Patentability Assessment

### Invention Summary
[description]

### Overall Assessment
[PATENTABLE / PATENTABLE WITH AMENDMENTS / NOT PATENTABLE]

### Anticipation Analysis
[claim-by-claim matrix against each reference]

### Obviousness Analysis
[combination analysis with motivation to combine]

### Cross-Model Examiner Review
[summary of GPT-5.4 examiner feedback]

### Recommended Claim Amendments
[If claims need modification to overcome prior art, suggest specific amendments]

### Risk Factors
[What could cause rejection during actual prosecution?]
```

## Key Rules

- Patent novelty is absolute: any public disclosure before the priority date counts as prior art, worldwide.
- Research novelty ("has anyone published this?") is NOT the same as patent novelty ("does any single reference teach every claim element?").
- Obviousness requires BOTH: (1) a combination of references AND (2) a motivation to combine them.
- Never assume the invention is patentable just because no identical patent exists.
- The assessment is advisory only -- actual prosecution may reveal different prior art.
- If `mcp__codex__codex` is not available, skip cross-model examiner review and note it in the output.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/patent-novelty-check/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>audit</code></dd>
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/patent-novelty-check/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
