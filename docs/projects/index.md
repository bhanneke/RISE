# Projects catalog

> This page is regenerated from `projects/*.yml` and
> `projects/landscape/*.yml` by `scripts/build_indexes.py`.
> Do not edit by hand — edit the YAML sources.

The catalog evaluates agentic-research systems against the
[standard rubric](../../projects/EVALUATION.md). Vocabularies for
stages, architectural features, and disciplinary scope are defined
in [`projects/VOCABULARY.md`](../../projects/VOCABULARY.md).

## Featured

- **[E2ER](../../projects/e2er.yml)** — End-to-End Research project
  (owned; deep-dive page).

## Landscape

<!-- AUTO-GENERATED:projects-start -->

### Comparison matrix

| Project | Type | LC | AUT | ARC | IN | OUT | EVAL | OPEN | MAT | Discipline |
|---|---|---|---|---|---|---|---|---|---|---|
| [E2ER — End-to-End Research](../../projects/e2er.yml) | owned | 3 | 2 | 2 | 3 | 2 | 1 | 2 | 1 | economics |
| [APE — Automated Peer Evaluator](../../projects/landscape/ape.yml) | external | 0 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | general |
| [coarse.ink](../../projects/landscape/coarse-ink.yml) | external | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | general |
| [refine.ink](../../projects/landscape/refine-ink.yml) | external | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | general |
| [Sakana AI Scientist v2](../../projects/landscape/sakana-ai-scientist.yml) | external | 2 | 3 | 3 | 1 | 2 | 2 | 3 | 2 | computer-science |
| [Social Science Replicability Infrastructure](../../projects/landscape/social-science-replicability.yml) | external | 1 | 2 | 2 | 2 | 2 | 1 | 3 | 1 | social-sciences |
| [zeropaper](../../projects/landscape/zeropaper.yml) | external | 1 | 2 | 2 | 1 | 1 | 0 | 3 | 1 | general |

*Score columns: LC = lifecycle coverage, AUT = autonomy, ARC = architectural transparency, IN = inputs supported, OUT = outputs/reproducibility, EVAL = internal evaluation, OPEN = openness, MAT = maturity/traction. Scale 0–3. See [`projects/EVALUATION.md`](../../projects/EVALUATION.md).*

### Entries

#### [E2ER — End-to-End Research](../../projects/e2er.yml)

E2ER is a strategist-driven agentic research pipeline that takes a research idea (human- or agent-supplied) and carries it through literature synthesis, identification, data acquisition, analysis, and paper drafting. It targets the full inputs → knowledge production → outputs arc of the RISE diagram, with explicit data and knowledge side-inputs.

#### [APE — Automated Peer Evaluator](../../projects/landscape/ape.yml)

A focused tool for automated peer evaluation of submitted papers, sitting at the *referee-simulation* stage of the RISE pipeline. Does not produce papers itself; consumes them and produces structured reviews.

#### [coarse.ink](../../projects/landscape/coarse-ink.yml)

Research-workflow tooling that supports upstream stages of writing and project management. Sits in the research-design / drafting portion of the RISE pipeline as a workspace rather than an autonomous pipeline.

#### [refine.ink](../../projects/landscape/refine-ink.yml)

Academic prose tooling focused on the revision/editing stage of the RISE pipeline. Does not produce papers end-to-end; consumes drafts and produces refined prose.

#### [Sakana AI Scientist v2](../../projects/landscape/sakana-ai-scientist.yml)

An autonomous "AI scientist" pipeline that ideates, runs experiments (primarily ML), drafts a paper, and self-reviews. Targets the full RISE arc end-to-end with minimal human oversight per task.

#### [Social Science Replicability Infrastructure](../../projects/landscape/social-science-replicability.yml)

Infrastructure aimed at the replication stage of the RISE pipeline: given a published paper, attempt to reproduce its empirical results in an automated or semi-automated fashion. Sits squarely in the replication block of the RISE diagram.

#### [zeropaper](../../projects/landscape/zeropaper.yml)

An autonomous paper-writing pipeline that takes a research topic and produces a written paper with minimal user input. Sits firmly in the paper-drafting / revision portion of the RISE pipeline with light upstream ideation.

<!-- AUTO-GENERATED:projects-end -->

## How to add a project

1. Copy `projects/landscape/sakana-ai-scientist.yml` as a template.
2. Fill in fields per [`projects/schema.md`](../../projects/schema.md).
3. Score it against [`projects/EVALUATION.md`](../../projects/EVALUATION.md).
4. Open a pull request.
