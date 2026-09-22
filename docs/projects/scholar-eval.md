<!-- DO NOT EDIT — auto-generated from projects/landscape/scholar-eval.yml by scripts/build_indexes.py -->

# ScholarEval

`external` · status: `dormant` · focus: `review` · discipline: `general` · started: 2025

**Project page:** <https://github.com/skai-research/ScholarEval>

**Source:** [`projects/landscape/scholar-eval.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/scholar-eval.yml)

## Positioning

A retrieval-augmented system that reviews a *research idea* before any work is done, along two declared dimensions — Soundness (are the proposed methods empirically valid given what the literature already establishes?) and Contribution (does it advance on prior work?) — with every judgement grounded in papers retrieved via the Semantic Scholar API under a user-declared literature cutoff date rather than in model priors. Ships as both a system (Streamlit app, CLI pipeline, and a hosted web app at go.osu.edu/scholar-eval) and a benchmark: ScholarIdeas, an expert-annotated set of 117 research ideas across AI, neuroscience, biochemistry and ecology carrying 1,076 review rubrics. It occupies the one slot the RISE review layer was missing — appraisal at the idea stage, upstream of drafting, where `reviewer`, `marg` and the referee-simulation entries all act on finished manuscripts.

## Distinctive contribution

It separates *soundness* from *contribution* and makes the second falsifiable by construction: the cutoff date fixes what the system is allowed to have read, so a novelty verdict can be checked against a defined corpus rather than asserted from a model's training data. The companion evaluation covers more of the expert-annotated rubric set than baselines including OpenAI's o4-mini-deep-research, and a user study reports gains in literature engagement and idea refinement — the closest thing in the catalog to a measured pre-work triage tool.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three adjacent stages — literature discovery, synthesis, and referee-style appraisal of an idea; no research design, analysis, drafting or revision. |
| Autonomy level | 2 | The user submits an idea file and a cutoff date and the pipeline retrieves, reasons and returns a structured review without per-step approval — supervised agent, reviewed at the artifact. |
| Architectural transparency | 3 | MIT-licensed repo publishes the system (`ScholarEval/`), the dataset-construction code (`dataset_creation/`), the benchmark harness (`evaluation/`), the ScholarIdeas rubrics, and the GROBID config — architecture plus prompts plus evaluation code. |
| Inputs supported | 1 | A single input form (a research-idea text file plus a cutoff date) with literature access only — no dataset, no manuscript, no private-corpus ingestion. |
| Outputs / reproducibility | 1 | Outputs are prose reviews plus their retrieved reference lists written to an output folder; there is no versioning, seeding or run manifest, and re-running the same idea against the live Semantic Scholar index need not reproduce the review. |
| Internal evaluation | 2 | Systematic benchmarking on the authors' own ScholarIdeas (117 ideas, 1,076 expert rubrics) against baselines including o4-mini-deep-research, plus a user study; arXiv-only (v1 2025-10-17, v2 2026-02-28) with no venue in the comments field and no third-party replication. |
| Openness | 2 | MIT licence with code, dataset (HuggingFace `hananour/ScholarIdeas`) and three documented deployment paths, but a run needs a LiteLLM API endpoint plus a Semantic Scholar key, and the hosted app is metered at $15 of free academic credit — permissive, not free-tier reproducible. |
| Maturity / traction | 1 | 21 stars, 2 forks, 32 commits, no push since 2025-10-28 even though the paper was revised in February 2026; a hosted OSU-linked web app exists but no evidence of sustained external use. |
| Cross-family policy | 1 | The LLM engine is a per-run flag with both gpt-4o and claude-sonnet-4 documented, so a cross-family setup is possible, but the soundness and contribution agents run on whichever single engine is passed — nothing pairs families. |
| Runtime assurance | 2 | Grounding is the mechanism, not an afterthought: claims are tied to Semantic Scholar retrievals with an enforced literature cutoff and GROBID-parsed full text, i.e. RAG citation grounding as an in-pipeline check on both review dimensions. |
| Cross-platform portability | 2 | LiteLLM as the model layer means many providers behind one config, and there are three execution paths (local Streamlit, CLI script, hosted web app). |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `referee-simulation`


**Architectural features:** `multi-agent` `rag-knowledge-base` `tool-use`


**Inputs:** `research-idea` `literature-cutoff-date`


**Outputs:** `soundness-review` `contribution-review` `retrieved-citations`


**Knowledge sources:** `semantic-scholar` `unpaywall` `grobid-parsed-pdfs`


## Limitations

- No code push since 2025-10-28 while the paper reached v2 in February 2026 — the repo may lag the evaluated system.
- Reviews inherit their coverage from Semantic Scholar and Unpaywall: anything paywalled, unindexed or after the declared cutoff is invisible to the soundness verdict.
- ScholarIdeas spans AI, neuroscience, biochemistry and ecology — no economics, finance or information-systems ideas, so rubric transfer to Björn's own fields is untested.
- Both the system and the benchmark it is scored on come from the same team; no third-party evaluation, and the arXiv page carries no venue as of scoring date.
- Requires a LiteLLM endpoint and a Semantic Scholar API key; the free hosted route is credit-metered.
- Appraises ideas only — it does not check executed work, data, or a manuscript, and gives no verdict a referee could be held to.

## Related projects in this catalog

- [`reviewer`](reviewer.md)
- [`marg`](marg.md)
- [`ai-research-feedback`](ai-research-feedback.md)
- [`open-scholar`](open-scholar.md)

## Papers describing this project

- **ScholarEval: Research Idea Evaluation Grounded in Literature** — Moussa, H. N., Da Silva, P. Q., Adu-Ampratwum, D., East, A., Lu, Z., Puccetti, N., Xue, M., Sun, H., Majumder, B. P., Kumar, S. (2025). *arXiv*. [arXiv:2510.16234](https://arxiv.org/abs/2510.16234)

## Related references (literature catalog)

- `moussa2025scholareval` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
