# Project evaluation rubric (v0.2)

Every entry in `projects/e2er.yml` and `projects/landscape/*.yml` is
scored against the eight dimensions below.

**Scoring**: each dimension takes an integer score `0–3` with a
one-line *justification* string. Scores are descriptive, not normative;
the goal is to make the landscape navigable, not to rank winners.

A radar chart per project and a comparison matrix are rendered from
these scores by `scripts/build_indexes.py`.

---

## The eight dimensions

### 1. Lifecycle coverage

How much of the inputs → knowledge-production → outputs pipeline does
the system touch? Counted from the project's declared `pipeline_stages`
(see [`VOCABULARY.md`](VOCABULARY.md)).

| Score | Meaning |
|-------|---------|
| 0 | Touches one stage only (e.g., literature search only). |
| 1 | Touches 2–3 adjacent stages. |
| 2 | Covers a substantial slice (4–7 stages) but with gaps. |
| 3 | End-to-end: 8+ stages including paper-drafting *and* a validation/review stage. |

### 2. Autonomy level

How much human oversight per task is required for the system to deliver
its declared output?

| Score | Meaning |
|-------|---------|
| 0 | Tool: human drives every step; system only assists. |
| 1 | Copilot: human approves each significant step. |
| 2 | Supervised agent: human sets up the task and reviews the final artifact. |
| 3 | Autonomous: system runs end-to-end without per-task human approval (society-of-agents included). |

### 3. Architectural transparency

Is the agent topology, prompts, and orchestration logic publicly
documented at a level that enables understanding, critique, or reuse?

| Score | Meaning |
|-------|---------|
| 0 | Closed; only marketing-level description. |
| 1 | High-level architecture published, no prompts or code. |
| 2 | Architecture + prompts published; code partial. |
| 3 | Full transparency: code, prompts, configs, evaluation harness. |

### 4. Inputs supported

Variety of acceptable inputs and the data + knowledge sources the
system can access.

| Score | Meaning |
|-------|---------|
| 0 | One narrow input form, no data/knowledge access. |
| 1 | One input form, plus literature *or* data access. |
| 2 | Multiple input forms (idea, RQ, paper, dataset) and at least one of {literature corpus, data sources}. |
| 3 | Multiple input forms with both literature *and* data-source access, including private corpora. |

### 5. Outputs and artifact reproducibility

What durable outputs does the system produce, and are they reproducible
from inputs?

| Score | Meaning |
|-------|---------|
| 0 | Ephemeral chat output only; no persisted artifacts. |
| 1 | Persists prose drafts only. |
| 2 | Persists prose + code/figures, but no end-to-end reproducibility. |
| 3 | Versioned artifacts (paper + code + data manifest) reproducible from declared inputs. |

### 6. Internal evaluation

Does the project evaluate its own outputs against external standards
(benchmarks, human review, replication)?

| Score | Meaning |
|-------|---------|
| 0 | No reported evaluation. |
| 1 | Anecdotal demos / cherry-picked examples. |
| 2 | Systematic internal evaluation (e.g., scored against a benchmark). |
| 3 | External validation: peer-reviewed publication, third-party replication, or sustained real-world adoption with reported outcomes. |

### 7. Openness and reproducibility (of the system itself)

Distinct from output reproducibility — this scores the *project as
software*.

| Score | Meaning |
|-------|---------|
| 0 | Closed-source, no free tier. |
| 1 | Source available but non-permissive license, or free tier with heavy gating. |
| 2 | Permissive license; examples partially reproducible. |
| 3 | Permissive license; demonstrated examples reproducible end-to-end on commodity hardware. |

### 8. Maturity and traction

| Score | Meaning |
|-------|---------|
| 0 | Demo / abandoned (no activity >12 months) / vapor. |
| 1 | Research prototype: active but pre-1.0, single-team use. |
| 2 | Alpha / beta: external users, regular releases. |
| 3 | Production: sustained external adoption, citations, or commercial deployment. |

---

## v0.2 additions — architectural dimensions

Added in v0.2 (2026-05-18) to make the catalog directly comparable with
the architectural feature matrix in Yang, Li, Li (2026) "ARIS"
(arXiv:2605.03042, Table 4). These dimensions sit alongside the
original 8 methodological dimensions.

### 9. Cross-family policy

Does the system *require, default to, or merely allow* cross-model-family
review (executor and reviewer from different model families)? Motivated
by ARIS's argument that same-model self-refinement falls into local
minima — see [@yang2026aris].

| Score | Meaning |
|-------|---------|
| 0 | None — single-LLM by design, or multi-agent within one model family only. |
| 1 | Optional — cross-family setup is supported via config but not the default path. |
| 2 | Default — cross-family is the recommended / out-of-the-box configuration. |
| 3 | Required — system cannot function without two different model families. |

### 10. Runtime assurance

In-flight integrity mechanisms that catch failure *as the pipeline
runs*, distinct from post-hoc evaluation. Includes claim-faithfulness
checks, hallucinated-citation detection, math-proof verification,
runtime fact-checking, visual artifact inspection, adversarial gates.

| Score | Meaning |
|-------|---------|
| 0 | None — outputs pass through without runtime integrity checks. |
| 1 | Light — logging, basic schema validation, or single-pass review. |
| 2 | Moderate — multiple in-pipeline gates (e.g., math auditor + novelty checker, or RAG citation grounding). |
| 3 | Heavy — full runtime audit stack (evidence verification + claim audit + math proof + figure inspection) with gating on failure. |

Note: this dimension is **about runtime mechanisms only**, not about
benchmark results or peer-review acceptance — those belong under
dimension 6 (`internal_evaluation`).

### 11. Cross-platform portability

How many distinct execution environments / model providers / agent
runtimes can the system be deployed against without rewriting it?

| Score | Meaning |
|-------|---------|
| 0 | Single platform — locked to one IDE / one provider / one runtime. |
| 1 | Limited — 2 backends or a known small adapter set. |
| 2 | Multiple — 3+ LLM providers OR 2+ IDEs / runtimes. |
| 3 | Framework-agnostic — 5+ supported execution environments, deliberately portable design (skills-as-Markdown, protocol-based). |

---

## Required narrative sections

In addition to the eight scores, each entry includes free-text fields:

- **`positioning`** *(1–3 sentences)* — Where the project sits on the
  inputs → knowledge production → outputs diagram. What flows it
  implements.
- **`distinctive_contribution`** *(1–3 sentences)* — What this project
  does that others on the landscape don't.
- **`limitations`** *(bullet list)* — Known limitations or risks.
- **`related`** *(list of project slugs)* — Sibling / competitor /
  predecessor projects in this catalog.

---

## Re-scoring policy

- Scores carry a `scored_on` date (YYYY-MM-DD).
- Re-score when the project has a significant release, or annually at minimum.
- Old scores are preserved in git history; we do not maintain inline change logs.

---

## Versioning

This rubric is **v0.2** (2026-05-18). v0.2 added three architectural
dimensions (cross_family_policy, assurance_runtime,
cross_platform_portability) derived from ARIS Table 4
[@yang2026aris]. Material changes (new dimension, redefinition of a
score band) bump the minor version and require a re-scoring pass
across the catalog.

### Change log

- **v0.2** (2026-05-18) — Added dimensions 9–11 from ARIS Table 4 analogy. Re-scored all 34 existing projects + 3 new ARIS-flagged additions (data-to-paper, AutoResearchClaw, EvoScientist).
- **v0.1** (2026-05-14) — Initial 8 dimensions.
