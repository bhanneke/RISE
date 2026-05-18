<!-- DO NOT EDIT — auto-generated from projects/landscape/ape.yml by scripts/build_indexes.py -->

# Project APE

`external` · status: `active` · focus: `end-to-end` · discipline: `economics` · started: 2026

**Project page:** <https://ape.socialcatalystlab.org/>

**Source:** [`projects/landscape/ape.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ape.yml)

## Positioning

An autonomous system that generates empirical economic policy research papers end-to-end from publicly available data, then scores them via a TrueSkill tournament in which AI-generated papers compete head-to-head against peer-reviewed human benchmarks from AER and AEJ:Policy (judged by Gemini 3.1 Flash Lite). The motivating problem: "Most policies — probably millions of them globally — are never rigorously evaluated."

## Distinctive contribution

*Combines* autonomous research generation with an explicit human-benchmark tournament — most catalog projects do one or the other. The TrueSkill ranking + AER/AEJ:Policy benchmark set is a reusable evaluation harness; everything (papers, code, data, failures) is published transparently. The project explicitly disclaims policy use: "None of the generated papers have been peer-reviewed and should not be used for evidence-based policy making."

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Eight stages from hypothesis through replication-verification; full end-to-end loop. |
| Autonomy level | 3 | Generates papers autonomously without per-step human approval. |
| Architectural transparency | 3 | Stated commitment: 'everything is public — papers, code, data, failures.' TrueSkill scoring + benchmark set are open. |
| Inputs supported | 2 | Policy-question inputs; integrates public-data sources; uses AER / AEJ:Policy corpus as benchmark. |
| Outputs / reproducibility | 3 | Replication-verification step: 'Checks whether code executes and outputs match.' Full artifact transparency by design. |
| Internal evaluation | 3 | Tournament evaluation against peer-reviewed human-benchmark papers from top economics journals — strongest internal-eval design in the catalog. |
| Openness | 3 | Fully open: papers, code, data, failures. |
| Maturity / traction | 1 | Active hosted project in 2026; adoption / external use signals not yet clear. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-acquisition` `data-analysis` `code-generation` `paper-drafting` `referee-simulation` `replication`


**Architectural features:** `multi-agent` `tool-use` `artifact-versioning` `debate-consensus`


**Inputs:** `policy-question`


**Outputs:** `paper` `code` `data` `tournament-ranking`


**Data sources:** `public-policy-data`


**Knowledge sources:** `aer` `aej-policy`


## Limitations

- Explicit author disclaimer that outputs should not be used for evidence-based policy making.
- Tournament judge (Gemini 3.1 Flash Lite) may itself be biased — meta-evaluation question.
- Economics-policy scope by design; portability to other empirical fields untested.
- Maintainer identity (Social Catalyst Lab) and funding model not publicly detailed.

## Related projects in this catalog

- [`e2er`](e2er.md)
- [`clo-author`](clo-author.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`social-science-replicability`](social-science-replicability.md)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- `cao2025aifinance` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
