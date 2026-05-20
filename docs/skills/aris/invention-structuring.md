<!-- DO NOT EDIT — auto-copied from skills/aris/details/invention-structuring.md -->

# `invention-structuring`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/invention-structuring/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/invention-structuring/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Invention Structuring

Structure the invention into a formal disclosure based on: **$ARGUMENTS**

Adapted from the refinement pattern in `/research-refine` for patent invention decomposition.

### Constants

- `REVIEWER_MODEL = gpt-5.5` — External reviewer for invention decomposition validation
- `MAX_REFINEMENT_ROUNDS = 3` — Maximum structuring iterations

### Inputs

1. Invention description from `$ARGUMENTS`
2. `patent/INVENTION_BRIEF.md` if exists
3. `patent/PRIOR_ART_REPORT.md` — prior art landscape
4. `patent/NOVELTY_ASSESSMENT.md` — novelty analysis

### Shared References

Load `../shared-references/patent-writing-principles.md` for the Problem-Solution-Advantage framework and claimable subject matter guidelines.

### Workflow

#### Step 1: Problem-Solution-Advantage Framework

Structure the invention using the universal patent framework:

**Technical Problem (要解决的技术问题)**:
- Derived from prior art deficiencies identified in NOVELTY_ASSESSMENT.md
- Must be a specific, technical problem (not a commercial or social problem)
- Statement format: "The technical problem to be solved is how to [specific technical objective] given [specific technical constraint]."

**Technical Solution (技术方案)**:
- The invention's specific technical contribution
- Focus on the mechanism, not the result
- Must be described at a level that matches the intended claim scope
- Identify which features are known vs. inventive

**Advantages (有益效果)**:
- Measurable or quantifiable improvements over prior art
- Must result from the inventive features, not just good engineering
- Include specific technical effects if known (e.g., "reduces processing time by 40%")

#### Step 2: Invention Decomposition

Break the invention into three layers:

**Core Inventive Concept (核心发明构思)**:
- The minimal set of features that make the invention patentable
- This maps to the independent claim scope
- Test: if you remove this feature, the invention is no longer novel

**Supporting Features (支撑性特征)**:
- Features that make the invention work well in practice
- These become dependent claim material
- They narrow the scope but add practical value

**Optional Features (可选特征)**:
- Implementation details, preferred parameters, alternatives
- These become embodiment material
- They support broader claim interpretation

#### Step 3: Claimable Subject Matter Identification

For the core inventive concept, determine what categories of claims to draft:

| Category | Applicability | Content |
|----------|-------------|---------|
| Method/process | If invention involves steps | Process flow, algorithm, workflow |
| System/apparatus | If invention involves components | Hardware structure, modules, connections |
| Product | If invention is a physical device | Shape, structure, composition |
| Computer-readable medium | If software invention (US) | Stored instructions, non-transitory medium |
| Product-by-process | If structure is hard to define | Product defined by how it is made |

#### Step 4: Drawing Plan

Plan what figures are needed to support the claims and specification:

| Figure | Type | Shows | Supports Claim Elements |
|--------|------|-------|------------------------|
| FIG. 1 | Block diagram | System architecture | System claim components |
| FIG. 2 | Flowchart | Method steps | Method claim steps |
| FIG. 3 | Sequence diagram | Interaction between components | Specific implementation details |

If user has provided figures, reference them here. If figures are missing, note what is needed.

#### Step 5: Dependency Mapping

Map feature dependencies to plan the claim hierarchy:

```
Independent Claim 1 (method, broadest scope)
├── Core inventive feature A
├── Core inventive feature B
└── Known feature C (for context)

Dependent Claim 2 → narrows feature A with specific implementation
Dependent Claim 3 → narrows feature B with specific parameters
Dependent Claim 4 → depends on 2, adds optional feature D
Dependent Claim 5 → alternative implementation of feature A
```

#### Step 6: Cross-Model Validation

Call `REVIEWER_MODEL` via `mcp__codex__codex` with xhigh reasoning:

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are a patent attorney reviewing an invention disclosure.
    Evaluate the structuring choices:

    INVENTION: [Problem-Solution-Advantage summary]
    DECOMPOSITION: [Core/Supporting/Optional features]
    CLAIM PLAN: [intended claim categories and hierarchy]

    Please assess:
    1. Is the Problem-Solution-Advantage framework correctly applied?
    2. Is the core inventive concept correctly identified? Are there features that should be core but are listed as supporting (or vice versa)?
    3. Are the planned claim categories sufficient to protect the invention?
    4. Is the drawing plan adequate for enablement?
    5. Are there any claimable aspects being missed?
```

#### Step 7: Output

Write `patent/INVENTION_DISCLOSURE.md`:

```markdown
### Invention Disclosure

#### Title
[invention title]

#### Technical Problem
[formal problem statement]

#### Technical Solution
[formal solution description]

#### Advantages
[measurable advantages]

#### Feature Decomposition

#### Core Inventive Concept
[features that define independent claim scope]

#### Supporting Features
[features for dependent claims]

#### Optional Features
[features for embodiments]

#### Claimable Subject Matter
[method, system, product, medium claims planned]

#### Drawing Plan
[figures needed, what each shows]

#### Dependency Map
[claim hierarchy plan]

#### Inventor Information
[names, contributions]

#### Target Jurisdiction
[CN/US/EP/ALL]
```

### Key Rules

- The Problem must come from prior art deficiencies, not from commercial needs.
- The Solution must describe the technical mechanism, not just the result.
- The core inventive concept must be the minimum set of features for patentability.
- Supporting features should be independently valuable -- each should provide a meaningful technical benefit even if other supporting features are removed.
- Never invent embodiments that do not correspond to the actual invention or user-provided materials.
- If `mcp__codex__codex` is not available, skip cross-model validation and note it in the output.
