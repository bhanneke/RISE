<!-- DO NOT EDIT — auto-copied from skills/aris/details/formula-derivation.md -->

# `formula-derivation`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>modeling</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>formal-modeling</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/formula-derivation/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/formula-derivation/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Formula Derivation: Research Theory Line Construction

Build an honest derivation package, not a fake polished theorem story.

### Constants

- DEFAULT_DERIVATION_DOC = `DERIVATION_PACKAGE.md` in project root
- STATUS = `COHERENT AS STATED | COHERENT AFTER REFRAMING / EXTRA ASSUMPTION | NOT YET COHERENT`

### Context: $ARGUMENTS

### Goal

Produce exactly one of:
1. a coherent derivation package for the original target
2. a reframed derivation package with corrected object / assumptions / scope
3. a blocker report explaining why the current notes cannot yet support a coherent derivation

### Inputs

Extract and normalize:
- the target phenomenon, formula, relation, or theory line
- the intended role of the derivation:
  - exact identity / algebra
  - proposition / local theorem
  - approximation
  - mechanism interpretation
- explicit assumptions
- notation and definitions
- any user-provided formula chain, sketch, messy notes, or current draft
- nearby local theory files if the request points to them
- desired output style if specified:
  - internal alignment note
  - paper-style theory draft
  - blocker report

If the target, object, notation, or assumptions are ambiguous, state the exact interpretation you are using before deriving anything.

### Workflow

#### Step 1: Gather Derivation Context
Determine the target derivation file with this priority:
1. a file path explicitly specified by the user
2. a derivation draft already referenced in local notes
3. `DERIVATION_PACKAGE.md` in project root as the default target

Read the relevant local context:
- the chosen target derivation file, if it already exists
- any local theory notes, formula drafts, appendix notes, or files explicitly mentioned by the user

Extract:
- target formula / theory goal
- current formula chain
- assumptions
- notation
- known blockers
- desired output mode

#### Step 2: Freeze the Target
State explicitly:
- what is being explained, derived, or supported
- whether the immediate goal is:
  - identity / algebra
  - proposition
  - approximation
  - interpretation
- what the derivation is expected to output in the end

Do not start symbolic manipulation before this is fixed.

#### Step 3: Choose the Invariant Object
Identify the single quantity or conceptual object that should organize the derivation.

Typical possibilities include:
- objective / utility / loss
- total cost / energy / welfare
- conserved quantity / state variable
- expected metric / effective rate / effective cost

If the current notes start from a narrower quantity, decide explicitly whether it is:
- the true top-level object
- a proxy
- a local slice
- an approximation

Do not let a convenient proxy silently replace the actual conceptual object.

#### Step 4: Normalize Assumptions and Notation
Restate:
- all assumptions
- all symbols
- regime boundaries or special cases
- which quantities are fixed, adaptive, or state dependent

Identify:
- hidden assumptions
- undefined notation
- scope ambiguities
- whether the current formula chain already mixes exact steps with approximations

Preserve the user's original notation unless a cleanup is necessary for coherence.
If you adopt a cleaner internal formulation, keep that as a derivation device rather than silently replacing the user's target.

#### Step 5: Classify the Derivation Steps
For every nontrivial step, determine whether it is:
- **identity**: exact algebraic reformulation
- **proposition**: a claim requiring conditions
- **approximation**: model simplification or surrogate
- **interpretation**: prose-level meaning of a formula

Never merge these categories without signaling the transition.
If one part is only interpretive, do not present it as if it were mathematically proved.

#### Step 6: Build a Derivation Map
Choose a derivation strategy, for example:
- definition -> substitution -> simplification
- primitive law -> intermediate variable -> target expression
- global quantity -> perturbation -> decomposition
- exact model -> approximation -> interpretable closed form
- general dynamic object -> simplified slice -> local theorem -> return to general case

Then write a derivation map:
- target formula or theory line
- required intermediate identities or lemmas
- which assumptions each nontrivial step uses
- where approximations enter
- where special-case and general-case regimes diverge or collapse

If the derivation needs a decomposition, derive it from the chosen global quantity.
Do not make a split appear magically from one local variable itself.

#### Step 7: Write the Derivation Document
Write to the chosen target derivation file.

If the target derivation file already exists:
- read it first
- update the relevant section
- do not blindly duplicate prior content

If the user does not specify a target, default to `DERIVATION_PACKAGE.md` in project root.

Do NOT write directly into paper sections or appendix `.tex` files unless the user explicitly asks for that target.

The derivation package must include:
- target
- status
- invariant object
- assumptions
- notation
- derivation strategy
- derivation map
- main derivation steps
- remarks / interpretations
- boundaries and non-claims

Writing rules:
- do not hide gaps with words like "clearly", "obviously", or "similarly"
- define every symbol before use
- mark approximations explicitly
- separate derivation body from remarks
- if the true object is dynamic or state dependent but a simpler slice is analyzed, say so explicitly
- if a formula line is only heuristic, label it honestly

#### Step 8: Final Verification
Before finishing the target derivation file, verify:
- the target is explicit
- the invariant object is stable across the derivation
- every assumption used is stated
- each formula step is correctly labeled as identity / proposition / approximation / interpretation
- the derivation does not silently switch objects
- special cases and general cases still belong to one theory line
- boundaries and non-claims are stated

If the derivation still lacks a coherent object, stable assumptions, or an honest path from premises to result, downgrade the status and write a blocker report instead of forcing a clean story.

### Required File Structure

Write the target derivation file using this structure:

```md
## Derivation Package

### Target
[what is being derived or explained]

### Status
COHERENT AS STATED / COHERENT AFTER REFRAMING / NOT YET COHERENT

### Invariant Object
[top-level quantity organizing the derivation]

### Assumptions
- ...

### Notation
- ...

### Derivation Strategy
[chosen route and why]

### Derivation Map
1. Target depends on ...
2. Intermediate step A uses ...
3. Approximation enters at ...

### Main Derivation
Step 1. ...
Step 2. ...
...

### Remarks and Interpretation
- ...

### Boundaries and Non-Claims
- ...

### Open Risks
- ...
```

### Output Modes

#### If the derivation is coherent as stated
Write the full structure above with a clean derivation package.

#### If the notes are close but not coherent yet
Write:
- the exact mismatch
- the corrected invariant object, assumption, or scope
- the reframed derivation package

#### If the derivation cannot be made coherent honestly
Write:
- `Status: NOT YET COHERENT`
- the exact blocker:
  - missing object
  - unstable assumptions
  - notation conflict
  - unsupported approximation
  - theorem-level claim without enough conditions
- what extra assumption, reframe, or intermediate derivation would be needed

### Relationship to `proof-writer`

Use `formula-derivation` when the user says things like:
- “我不知道怎么起这条推导主线”
- “这个公式到底该从哪个量出发”
- “帮我把理论搭顺”
- “把说明文档变成可写进论文的公式文档”
- “这几段公式之间逻辑不通”

Use `proof-writer` only after:
- the exact claim is fixed
- the assumptions are stable
- the notation is settled
- and the task is now to prove or refute that claim rigorously

### Chat Response

After writing the target derivation file, respond briefly with:
- status
- whether the target survived unchanged or had to be reframed
- what file was updated

### Key Rules

- Never fabricate a coherent derivation if the object, assumptions, or scope do not support one.
- Prefer reframing the derivation over overclaiming.
- Separate assumptions, identities, propositions, approximations, and interpretations.
- Keep one invariant object across special and general cases whenever possible.
- Treat simplified constant-parameter cases as analysis slices, not as the conceptual main object.
- If uncertainty remains, mark it explicitly in `Open Risks`; do not hide it in polished prose.
- Coherence matters more than elegance.
