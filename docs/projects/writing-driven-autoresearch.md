<!-- DO NOT EDIT — auto-generated from projects/landscape/writing-driven-autoresearch.yml by scripts/build_indexes.py -->

# Writing-Driven Autoresearch

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/happyhappy-jun/writing-driven-autoresearch>

**Source:** [`projects/landscape/writing-driven-autoresearch.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/writing-driven-autoresearch.yml)

## Positioning

A multi-agent harness that inverts the usual autoresearch order: instead of experimenting and then writing up, it drafts a complete submittable paper first — claims, tables and all, with the numbers standing in as placeholders — and then drives every experiment from the claims in that draft in a modify → measure → verify → revise loop. The founding instruction is "write the paper first, then make it true". Published as the complete run record of the 1st-place entry in the Auto Research track of Ralphthon@ICML 2026, not as an installable framework: three agent personas (master.md, experiment.md, writing.md), the writing guidelines they were held to, 136 timestamped decisions and 53 result JSONs under ralph/, the experiment scripts, and the resulting paper source and PDF, secrets redacted and otherwise exactly as the agents left them.

## Distinctive contribution

Number provenance enforced by tooling rather than trust. Two LaTeX macros split invented numbers (\ph{}) from measured ones (\phm{}); every \phm{} maps to an exact key in a result JSON through a placeholder ledger (ralph/PH-LEDGER.md); verify-phm.py checks each claimed number against those JSONs; and writing-audit.sh fails the build if any unfilled \ph{} survives to submission — so, in the authors' framing, the paper is true because the system was built to make untruth expensive. No other entry in the catalog makes an unverified number a build failure, and none ships its full decision log as the artifact.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Six stages from claim formulation through experiment design, implementation, measurement and revision to a compiled paper — a substantial slice, but with no literature stage and no referee simulation. |
| Autonomy level | 3 | Three agents produced a complete workshop paper in three hours under hackathon rules with minimal human guidance; the integrity checks are scripts in the build, not human approval gates. Evidence is a single run. |
| Architectural transparency | 3 | The repo is the trace: agent persona files, writing guidelines and style guide, the four integrity scripts (verify-phm.py, writing-audit.sh, unwrap-phm.sh, gen-table.py), the 1,100-line plan, all 136 decisions and all 53 result JSONs are published under Apache-2.0. |
| Inputs supported | 0 | One narrow input form — a research task plus a hand-written project spec. No literature retrieval, no dataset connectors; the only data is what the agents' own scripts generate. |
| Outputs / reproducibility | 2 | Unusually strong artifact provenance — every claimed number traces to a named key in a shipped result JSON and is mechanically checkable — but the run itself cannot be re-executed: nothing is packaged, and the models used are not named or pinned. |
| Internal evaluation | 2 | Externally judged: 1st place in the Auto Research track of Ralphthon@ICML 2026 before 11 expert reviewers. That is one run scored in a hackathon, not peer review, and the writing-driven method is never ablated against an experiment-first run. |
| Openness | 2 | Apache-2.0 with the entire run public, but the README states it is not a framework to install, and the experiments needed GPU-scale training plus paid frontier agents — so nothing here is reproducible on commodity hardware. |
| Maturity / traction | 0 | A demonstration by construction: 21 stars, 1 fork, one three-hour run frozen on 2026-07-14, no release, no packaging, and an explicit statement that it is not installable. Scored on installability and adoption, not on quality of the idea. |
| Cross-family policy | 0 | No reviewer role and no model-family policy: verification is deterministic scripts checking numbers against JSONs, and the README does not name which models ran the three personas. |
| Runtime assurance | 3 | The entry's whole point is a gating runtime audit of claim-to-evidence faithfulness: macro-level separation of guessed from measured numbers, a ledger binding each measured value to a result-JSON key, per-number mechanical verification, and a build that fails on any surviving unverified placeholder. Narrower than a full stack — no figure inspection and no proof checking. |
| Cross-platform portability | 1 | The harness is plain Markdown personas plus POSIX shell and Python, so it is portable in form, but nothing is packaged, no runtime or provider is named, and it has been run once — portability is untested. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `code-generation` `data-analysis` `paper-drafting` `revision-editing`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `artifact-versioning`


**Inputs:** `research-task-spec` `project-plan-document`


**Outputs:** `latex-paper-source` `compiled-paper-pdf` `result-jsons` `placeholder-ledger` `decision-log` `experiment-scripts`


**Knowledge sources:** `agent-generated-experiment-results`


## Limitations

- Not an installable framework — the README says so outright. It is one run's record with secrets redacted, so adopting the method means reading the personas and scripts and reimplementing them.
- n = 1. A single three-hour run that won a hackathon track is the entire evidence base: no repeated trials, no ablation against an experiment-first ordering, and no reported failure rate for the placeholder-verification loop.
- The honesty guarantee is narrower than it sounds. It proves a number in the text matches a number in a JSON the agents produced. It says nothing about whether the measurement was the right one — which is where economics claims actually fail, since no ledger key can verify an identification assumption.
- No literature stage: nothing retrieves or cites prior work, so every novelty and positioning claim in the draft is unverified by construction — a serious gap for a method whose first act is asserting the paper's claims.
- Subject matter is ML training (Depth-AR, skipping transformer layers), where the agents wrote both the claim and the measurement script. The provenance mechanism transfers to other fields; the demonstrated competence does not.
- 21 stars, 1 fork, and the models used are unnamed, so the run cannot be priced or re-attempted like-for-like.

## Related projects in this catalog

- [`clo-author`](clo-author.md)
- [`refine-ink`](refine-ink.md)
- [`paper-orchestra`](paper-orchestra.md)
- [`agon`](agon.md)
