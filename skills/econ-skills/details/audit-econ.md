---
name: audit-econ
description: Audit economics research for correctness — math, econometrics, code, data, proofs, model derivations. Dispatches independent Opus sub-agents, orchestrates Delphi consensus, presents severity-sorted findings, and manages fix workflow.
argument-hint: <target_path> [--agents N] [--effort max|high|medium]
---

# Audit Economics Research

Rigorous, multi-agent audit of economics research work. Enforces Econometrica-level standards across mathematics, econometrics, code, and data.

## Trigger conditions

Invoke this skill when the user asks to:
- Audit, check, verify, or validate research work
- Review math, derivations, proofs, or theorems for correctness
- Check whether a model's assumptions and results are consistent
- Verify data construction, regression implementation, or code correctness
- Confirm that results are replicable from raw data

## Defaults and configuration

| Setting | Default | Override |
|---------|---------|----------|
| Sub-agents | 3 | `--agents N` or specify after invocation |
| Model | Latest Opus | Always Opus for audit sub-agents |
| Effort | High | `--effort max\|high\|medium` |

If the user specifies overrides (e.g., "use 5 agents" or "max effort"), apply them. Otherwise use defaults.

## Arguments

Target and configuration: $ARGUMENTS

Parse:
- **target_path**: the file(s) to audit (.md, .tex, .py, .ipynb, .do, .jl, etc.)
- **--agents N**: number of independent audit sub-agents (default 3)
- **--effort**: thinking effort level (default high)

If no target is given, ask the user what to audit.

## Phase 1: Scope and dispatch

### Step 1.1: Determine audit type

Read the target file(s). Classify the audit domain(s):

| Content detected | Audit type |
|-----------------|------------|
| Equations, proofs, derivations, model sections | Math/Model |
| Data loading, merging, filtering, variable construction | Data Pipeline |
| Regression calls, estimation, standard errors, treatment effects | Econometrics |
| Plotting, figure generation | Graph |
| Mixed (model + data + regressions in one file) | General |

A single file may trigger multiple audit types. Use the **General** template if the file spans domains.

### Step 1.2: Identify the data lineage

If the target involves data or regressions:
1. Identify ALL data files referenced (read the code to find file paths)
2. Trace backwards: if the code loads an intermediate file, find the notebook/script that created it
3. Continue tracing until you reach the raw original data files
4. Build the full lineage: raw data → intermediate files → final analysis
5. ALL files in the lineage are in scope for the audit

### Step 1.3: Dispatch audit sub-agents

Launch N independent sub-agents (Agent tool, model: "opus") in a SINGLE message with multiple tool calls.

Each sub-agent receives:
- The target file path(s) and data lineage paths
- The appropriate prompt template from `references/subagent-prompts.md`
- Instructions to return a structured report

**Sub-agents must be independent** — they do not see each other's work during the audit phase. This ensures genuine independent review.

Each sub-agent must return findings in this format per issue:
```
FINDING:
- Name: [short descriptive name]
- Severity: [Critical / High / Mid / Low]
- Location: [file:line or section reference]
- Problem: [one sentence]
- Proposed fix: [one sentence]
- Evidence: [the specific math, code, or data that is wrong, with explanation]
```

## Phase 2: Delphi consensus

### Step 2.1: Collect reports

Wait for all sub-agents to return. Read each report.

### Step 2.2: Compare findings

Build a unified list of all findings across all agents:
- **Unanimous**: all agents flagged the same issue → confirmed finding
- **Majority**: most agents flagged it → likely real, but verify
- **Singleton**: only one agent flagged it → needs discussion

### Step 2.3: Resolve disagreements

For each non-unanimous finding:
1. Send a follow-up to the dissenting agent(s): "Agent X flagged [issue] with this evidence: [evidence]. You did not flag this. Is this a real issue? Explain why or why not."
2. Send a follow-up to the flagging agent: "Agents Y and Z did not flag [your issue]. Here is their reasoning: [reasoning]. Do you maintain your finding? Provide additional evidence or retract."
3. Continue until convergence — either the dissenter is persuaded or persuades the others.

### Step 2.4: Finalize

Discard retracted findings. Confirm all remaining findings with consensus severity levels.

## Phase 3: Present findings

### Step 3.1: Build the findings table

Sort findings: Critical → High → Mid → Low.

Present using the table format from `references/response-templates.md` — Template A:

| # | Name | Severity | Problem | Proposed Fix |
|---|------|----------|---------|--------------|

No verbose commentary. Just the table.

### Step 3.2: Ask for fix mode

Ask the user exactly one of:

> How would you like to proceed?
> 1. **Autofix all** — I dispatch agents to fix everything, verify each fix, then run a final audit
> 2. **Fix subset** — tell me which numbers to fix (e.g., "fix 1-3, skip 4, I'll handle 5")
> 3. **Sequential** — we go through each one together, discuss the fix, then move to the next

If the user doesn't want to fix anything, stop here.

## Phase 3.5: Build the dependency graph (mandatory before any fix)

Most cascade failures in formal modeling come from changing one equation without updating every downstream consumer of that equation. The discipline that prevents this: **map the dependency graph of the model before applying any fix**, and brief every fix and verification agent with the graph so changes propagate explicitly.

### Step 3.5.1: Dispatch a single dependency-mapping agent

Dispatch ONE Opus sub-agent using Template 8 from `references/subagent-prompts.md`. The output is a markdown propagation table with one row per finding and columns: `# | Affected object | Direct consumers | Indirect consumers | Cross-cuts | Form-sensitive derivations`.

Critical points to ensure the agent captures:
- For renames: enumerate every existing use of the new symbol elsewhere.
- For functional-form changes (e.g., from linear to Cobb-Douglas): list every guess-and-verify or closed-form derivation that depends on the original form.
- For parameter changes: list every BGP / homogeneity argument that uses the original parameter restrictions.

This step runs SEQUENTIALLY before any fix agent — never in parallel.

### Step 3.5.2: Brief fix agents with the propagation map

When dispatching each fix agent (Mode A) or moving to each finding (Mode C), include in the prompt:
- The affected object and its direct/indirect consumers.
- Explicit instruction: *"After applying the fix, examine every consumer in the propagation list and update it if it has become inconsistent. Treat consumer updates as part of this same fix, not a separate follow-up."*
- For renames and notation collisions: enumerate every existing use of the new symbol elsewhere in the document.
- For form-sensitive derivations: instruct the agent to re-derive the consuming derivation from scratch under the new form.

### Step 3.5.3: Brief verification agents with the propagation map

Verification agents (per-fix and at the final audit) receive the propagation map and explicitly check that all listed consumers are still consistent — not just that the local fix landed. A fix that lands locally but breaks a downstream consumer is a failed fix.

### Step 3.5.4: Update the graph after the final audit

If the final comprehensive audit (after all fixes) returns new issues, rebuild the dependency graph for the new findings before repeating Phase 4. Do not re-use the prior graph — the document state has changed.

## Phase 4: Fix execution

### Mode A: Autofix all

1. **Phase 3.5 dependency graph must be built first.** Do not skip.
2. For each finding, dispatch a sub-agent (Opus) to implement the fix, **with the propagation map for that finding included in the prompt**.
3. After each fix, dispatch a verification sub-agent (Template 6) that checks both (a) the local fix landed and (b) every consumer in the propagation map is still consistent with the new state.
4. If verification fails → iterate the fix until it passes.
5. After ALL fixes are implemented and verified → run a **final comprehensive audit** (Phase 1-2 again, using Template 7) to ensure no fix broke something else.
6. If the final audit finds new issues → present them, **rebuild the dependency graph for the new findings (Phase 3.5)**, and repeat from Phase 3.

### Mode B: Fix subset

1. **Build the Phase 3.5 dependency graph for the selected subset** (skip rows for findings the user opted out of).
2. User specifies which findings to fix (by number).
3. Apply Mode A process only to the specified findings.
4. Run final comprehensive audit on the entire document after all specified fixes.

### Mode C: Sequential

1. **Build the Phase 3.5 dependency graph upfront** so each fix can reference the propagation map.
2. Present the first finding: "We are now on #X: [name]. The problem is [problem]. My proposed fix: [fix]. **Propagation: [list of consumers]**. What do you think?"
3. Wait for user input. Discuss until convergence.
4. Implement the agreed fix, propagating to all consumers in the map. Verify with a sub-agent that checks both local fix and propagation.
5. Move to the next finding. Repeat.
6. After all findings are addressed → run final comprehensive audit.

### Final audit (all modes)

The final audit uses Template 7 from `references/subagent-prompts.md`. It re-audits the entire document from scratch to confirm:
- All fixes are correctly implemented
- No fix introduced a new error
- The document is internally consistent

If new issues are found, present them and ask the user how to proceed (same Phase 3 flow).

## Domain-specific audit checklists

These checklists are embedded in the sub-agent prompt templates. They are listed here for reference — the sub-agents receive them via `references/subagent-prompts.md`.

### Math / Model

- Every assumption is explicitly stated — not buried in derivations or implied
- Derivations are step-by-step: no skipped algebra, no "it follows that" without showing why
- No contradictions between assumptions and results
- Economic nuances are correctly handled:
  - How do firms enter? Free entry vs. fixed number?
  - Competition: perfect, monopolistic, Cournot, Bertrand?
  - Are agents atomistic (measure zero) or discrete?
  - Price-takers vs. price-setters?
  - What is the timing? Static, dynamic, overlapping generations?
  - Open vs. closed economy? Trade in goods, capital, labor?
- Results are derived from assumptions, not assumed and reverse-engineered
- Notation is consistent throughout (same symbol means the same thing everywhere)
- Boundary conditions and corner solutions are addressed
- Existence and uniqueness of equilibrium are discussed where relevant

### Data Pipeline

- Trace from raw original data files through ALL intermediate transformations to final analysis
- Check for suspicious filtering: dropping observations, restricting samples, excluding outliers
- Flag any hardcoded values in tables or results — everything must be computed at runtime
- Verify correct data version, correct years, correct variable definitions
- If multiple datasets are merged: check harmonization (units, definitions, time periods)
- Check for dropped observations from merges (inner vs. outer join consequences)
- Ensure full replicability: pressing "run all" from raw data produces identical output
- Flag any fabricated or hand-entered results — this is an ethics violation

### Regressions / Econometrics

- Standard packages must be used: pyfixest, statsmodels, linearmodels (Python); reghdfe, ivregress (Stata); fixest (R)
- NEVER trust hand-computed standard errors, treatment effects, or test statistics
- Flag arbitrary specification choices: time windows, panel balance, control variables
- Preferred specification = the one that would get least objection from unfriendly referees
- If using difference-in-differences: check parallel trends, staggered treatment handling (Sun & Abraham, Callaway & Sant'Anna)
- If using IV: check first stage, exclusion restriction discussion, weak instrument tests
- If clustering: verify cluster level is appropriate for the variation exploited
- Check that the reported specification matches what the code actually runs

### Graphs

- Data flows correctly from source to figure — no intermediate manipulation that distorts
- No visual tricks: truncated axes, misleading scales, cherry-picked time windows
- Axis labels, titles, and legends are accurate
- Source data is cited

### Code

- Everything runs end-to-end from raw data without manual intervention
- No fabricated results: every number in every table comes from a computed variable
- Variable names match between data construction and analysis
- No stale intermediate files that could mask errors
- Error handling doesn't silently swallow problems

## Important rules

- **Wrong math is worse than no math.** Every equation must be verified. Never approve a derivation you cannot confirm step by step.
- **Never assume results — derive them.** If a result "looks right," that is not evidence. Show the algebra.
- **Never trust hand-computed statistics.** Standard errors, p-values, treatment effects — always from a validated package.
- **Always trace data to original raw files.** If you can't trace it, flag it.
- **Flag suspicious filtering as potential ethics violation.** Dropping observations that change results is academic fraud. Flag it loudly.
- **Standard specification = least referee objection.** When multiple specifications are defensible, prefer the one most commonly used in top-5 publications.
- **Sub-agents must be Opus by default.** This audit requires the strongest available model.
- **Final audit is mandatory after any fix.** No exceptions.
- **Map the dependency graph before fixing (Phase 3.5).** Cascade failures happen when fixing one equation silently invalidates downstream consumers of that equation. Build the propagation map first; brief every fix and verification agent with the consumers of each affected object; require fixes to update consumers as part of the same edit (not as a follow-up). A fix that lands locally but breaks a consumer is a failed fix. Form-sensitive derivations (e.g., a value-function guess that assumes a specific functional form of an equation that just got changed) are the most common cascade vector — flag and re-derive them explicitly.
- **Spend tokens freely on correctness.** This is not the place to economize. Prefer thorough, expensive, correct audits over fast, cheap, wrong ones.
- **Report format is sacred.** Findings table only. No verbose commentary. The table speaks.
