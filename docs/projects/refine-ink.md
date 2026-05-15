<!-- DO NOT EDIT — auto-generated from projects/landscape/refine-ink.yml by scripts/build_indexes.py -->

# refine.ink

`external` · status: `active` · focus: `revision` · discipline: `general` · started: 2026

**Project page:** <https://www.refine.ink/>

**Source:** [`projects/landscape/refine-ink.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/refine-ink.yml)

## Positioning

Academic prose tooling focused on the revision/editing stage of the RISE pipeline. Does not produce papers end-to-end; consumes drafts and produces refined prose.

## Distinctive contribution

Targeted product surface for academic-style revision, distinct from general-purpose AI writing assistants; positions itself within the scholarly-writing workflow rather than as a generic chat tool.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (revision-editing). |
| Autonomy level | 1 | Copilot: author reviews each suggestion. |
| Architectural transparency | 0 | Commercial product; internals not publicly documented. |
| Inputs supported | 1 | Accepts drafts; limited external integration. |
| Outputs / reproducibility | 1 | Persists revisions; not designed for run-to-run determinism. |
| Internal evaluation | 0 | No public systematic evaluation. |
| Openness | 0 | Closed commercial product. |
| Maturity / traction | 1 | Active commercial offering; adoption scope unclear from public info. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `revision-editing`


**Architectural features:** `single-llm` `tool-use`


**Inputs:** `paper-draft`


**Outputs:** `revised-prose`


## Limitations

- Single-stage tool; not a RISE system on its own.
- Closed implementation; cannot be audited or extended.

## Related projects in this catalog

- [`coarse-ink`](coarse-ink.md)

## Related references (literature catalog)

- Riemer, K. et al. (2024). [*Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications*](../papers/notes/riemer2024styleengines.md) `riemer2024styleengines`
