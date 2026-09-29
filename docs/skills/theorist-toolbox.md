<!-- DO NOT EDIT — auto-generated from skills/theorist-toolbox.yml by scripts/build_skills_index.py -->

# Theorist Toolbox

license: `MIT` · 12 skills · last update: 2026-08-09

**Source:** <https://github.com/morankor/theorist-toolbox>

**Maintainers:** Moran Koren (Ben-Gurion University of the Negev, Economics)

**Compatibility:** `claude-code` `codex`

> Shared tooling for doing economic theory with LLMs — three bets on the same problem (machine help on a theorem you cannot already prove, with a trustable answer): math-proof (one careful single-shot pass), codex-math (OpenAI Codex as adversarial co-processor and hostile verifier), and co-math (a multi-agent proof-building project with strict unproven-gap flagging, reviewer sign-off gates, and optional Lean 4 verification, modelled on DeepMind's AI co-mathematician, Zheng et al. 2026). 6 skills + 6 sub-agents; Codex CLI port and ChatGPT prompts included. Companion paper: arXiv:2606.22337 (Koren 2026). Refresh 2026-09-29 (upstream at 2026-08-09): added the second-brain skill (agentic RAG over a local library of theory papers); re-copied the changed texts of math-proof (new proof-strategy planning section), co-math-init (standard workstream pipeline with readability pass), prover, coder and paper-reviewer (new gates against unverified reduction, complexity and integrality claims); corrected the codex-math source path to SKILL.md; nothing was removed. The 5 SKILL.md copies under codex/.agents/skills are the Codex port and are not catalogued separately.


**Source YAML:** [`skills/theorist-toolbox.yml`](https://github.com/bhanneke/RISE/blob/main/skills/theorist-toolbox.yml)

## Skills

### `audit` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/codex-math`](theorist-toolbox/codex-math.md) | economics | `formal-modeling` | Drives OpenAI Codex as an adversarial mathematical co-processor — verify, write, and explore modes; every output is a lead, not a verdict. | [view](theorist-toolbox/codex-math.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/skills/codex-math/SKILL.md) | 2026-07 |
| [`agent:lean-prover`](theorist-toolbox/lean-prover.md) | economics | `formal-modeling` | Formalises a lemma in Lean 4 and verifies it with lake build — a green build is the strongest "proven" the system supports; the reviewer re-runs the build rather than re-checking the mathematics. | [view](theorist-toolbox/lean-prover.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/agents/lean-prover.md) | 2026-07 |

### `code-gen` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`agent:coder`](theorist-toolbox/coder.md) | economics | `code-generation` | Python for computational exploration and numerical verification, with mandatory tests and golden values; cannot complete until tests pass and a reviewer accepts. | [view](theorist-toolbox/coder.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/agents/coder.md) | 2026-07-31 |

### `editing` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/proof-readability`](theorist-toolbox/proof-readability.md) | economics | `revision-editing` | Post-verification exposition pass for already-verified proofs — six layers (architecture, signposting, justification, notation, intuition, grammar) without changing the mathematics. | [view](theorist-toolbox/proof-readability.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/skills/proof-readability/SKILL.md) | 2026-07 |

### `infra` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/co-math-init`](theorist-toolbox/co-math-init.md) | economics | `formal-modeling` | Scaffolds a structured proof-building project (paper.tex, goals, decisions log, workstreams) with strict mode: every gap flagged unproven, nothing complete without reviewer sign-off. | [view](theorist-toolbox/co-math-init.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/skills/co-math-init/SKILL.md) | 2026-07-31 |
| [`/co-math-status`](theorist-toolbox/co-math-status.md) | economics |  | Renders a compact status view of a co-math project — goals, active workstreams, blocked items, pending reviews, recent decisions — as an ASCII diagram. | [view](theorist-toolbox/co-math-status.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/skills/co-math-status/SKILL.md) | 2026-07 |
| [`agent:project-coordinator`](theorist-toolbox/project-coordinator.md) | economics | `formal-modeling` | Front door of a co-math project — reads goals.md, formalises research intent, dispatches and steers workstreams, filters low-level chatter from the user. | [view](theorist-toolbox/project-coordinator.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/agents/project-coordinator.md) | 2026-07 |

### `literature` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`agent:literature-reviewer`](theorist-toolbox/literature-reviewer.md) | economics | `literature-discovery` `literature-synthesis` | Literature searches and verified, cited workstream reports; confirms prior art and validates supporting citations for claims in paper.tex. | [view](theorist-toolbox/literature-reviewer.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/agents/literature-reviewer.md) | 2026-07 |
| [`/second-brain`](theorist-toolbox/second-brain.md) | economics | `literature-synthesis` | Sets up and queries an agentic-RAG second brain over a local library of theory papers, with LaTeX-aware ingestion, theorem and proof lookup, and hybrid search. | [view](theorist-toolbox/second-brain.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/skills/second-brain/SKILL.md) | 2026-07-31 |

### `modeling` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/math-proof`](theorist-toolbox/math-proof.md) | economics | `formal-modeling` | Single-pass discipline for full, gap-free proofs: state what you will show before showing it, sign every term, no "clearly", no overgeneralizing from examples. | [view](theorist-toolbox/math-proof.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/skills/math-proof/SKILL.md) | 2026-07-31 |
| [`agent:prover`](theorist-toolbox/prover.md) | economics | `formal-modeling` | Drafts proofs into paper.tex with strict discipline — every step justified, cited, or explicitly marked unproven; never hand-waves. | [view](theorist-toolbox/prover.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/agents/prover.md) | 2026-07-31 |

### `review` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`agent:paper-reviewer`](theorist-toolbox/paper-reviewer.md) | economics | `referee-simulation` | Adversarial gate — a workstream cannot be marked complete until this agent writes an explicit approval file; cross-checks references, unproven blocks, and code-vs-claim consistency. | [view](theorist-toolbox/paper-reviewer.md) | [origin](https://github.com/morankor/theorist-toolbox/blob/main/agents/paper-reviewer.md) | 2026-07-31 |
