<!-- DO NOT EDIT — auto-generated from projects/landscape/autora.yml by scripts/build_indexes.py -->

# AutoRA (Automated Research Assistant)

`external` · status: `dormant` · focus: `end-to-end` · discipline: `social-sciences` · started: 2020

**Project page:** <https://github.com/autoresearch/autora>

**Source:** [`projects/landscape/autora.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/autora.yml)

## Positioning

A Python framework for closing the empirical research loop in the behavioural and brain sciences: an *experimentalist* proposes novel experimental conditions, an *experiment runner* collects the corresponding observations from participants or a synthetic generator, and a *theorist* fits a model that explains the data — then the cycle repeats with the new evidence, all coordinated through a serializable `StandardState` object. Declared scope is model discovery, experimental design, data collection and open-science documentation. It sits in the RISE closed-loop-discovery layer with Coral, Arbor and Robin, and is the only entry there aimed at human-subject social science.

## Distinctive contribution

It is the catalog's one closed-loop *empirical* discovery system for behavioural science — the social-science analogue of a self-driving lab, where the experiment being designed and run has human participants in it — and it is also the catalog's one pre-LLM entry: the theorist is a symbolic model-discovery method such as the Bayesian Machine Scientist, not a language model. Everything that makes it work is a documented component contract rather than a prompt, which means the loop is deterministic where the rest of the landscape is stochastic, and it runs with no API key and no inference cost.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five stages covering the whole empirical core — condition proposal, experimental design, data collection, analysis and symbolic model discovery — with the entire communication half absent: no literature stage, no drafting, no review. The README's 'open-science documentation' scope does not extend to journal formatting or submission packaging, so `dissemination` is not claimed. |
| Autonomy level | 3 | Autonomous once configured: the propose-conditions → run-experiment → fit-model cycle iterates without per-cycle human approval, which is the point of the closed loop. Human judgment lives in the initial variable-space and runner specification, not in the loop. |
| Architectural transparency | 3 | MIT license, 3,104 commits of fully public code, documented interface contracts for the experimentalist/runner/theorist components and the StandardState object, and a complete documentation site with runnable tutorials at autoresearch.github.io/autora. No prompts to publish — there is no LLM. |
| Inputs supported | 1 | Essentially one input form: a programmatic specification of the variable space and the runner. Data access is genuine (real-participant or synthetic experiment runners), but there is no literature ingestion, no PDF or free-text idea intake, and no bibliographic connector at all. |
| Outputs / reproducibility | 2 | Persists experimental conditions, collected datasets and models in symbolic form through a serializable state object, with versioned PyPI releases and tutorials that run end to end; short of band 3 because there is no manuscript artifact and no declared data manifest tying a published result to a run. |
| Internal evaluation | 2 | Peer-reviewed at JOSS in 2024 (9(104):6839) — editorial software review plus worked closed-loop demonstrations such as the Bayesian Machine Scientist recovering synthetic equations. Not band 3 because JOSS review certifies the software, not the quality of the discoveries: no benchmark of discovery accuracy against a standard and no third-party replication is reported in the repo. |
| Openness | 3 | MIT license, pip-installable, and the synthetic-runner tutorials reproduce end to end on a laptop with no API key, no paid model and no inference cost — one of the few entries in the catalog where a demonstrated example is genuinely reproducible on commodity hardware. |
| Maturity / traction | 2 | Deep and credible — 3,104 commits since 2020, JOSS-published, funded by Schmidt Science Fellows, Schmidt Sciences, Brown's Carney BRAINSTORM and VISS — but adoption is modest (101 stars, 13 forks, 38 open issues) and nothing has been pushed since 2025-11-27, so it reads as stable-and-quiet rather than growing. |
| Cross-family policy | 0 | Not applicable and scored 0: there is no LLM anywhere in the system, so there are no model families to cross. The theorist is a symbolic discovery algorithm. |
| Runtime assurance | 1 | Light, but of a kind no other entry has: each proposed model is confronted with freshly collected observations every cycle, so a wrong model is contradicted by new data rather than by a reviewer agent. There is no audit stack, no gating on failure, and nothing to check because no prose or citation is generated. |
| Cross-platform portability | 1 | A single Python runtime, but with a deliberate plugin architecture (separate autora-experimentalist-*, autora-theorist-* and autora-experiment-runner-* packages) that functions as a small documented adapter set. No model providers or agent runtimes to swap. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-acquisition` `data-analysis` `formal-modeling`


**Architectural features:** `iterative-loop` `persistent-memory`


**Inputs:** `variable-space-specification` `experiment-runner-configuration`


**Outputs:** `experimental-conditions` `collected-datasets` `symbolic-models`


**Data sources:** `human-participant-experiments` `synthetic-generators`


## Limitations

- Dormant: last pushed 2025-11-27, roughly nine months before scoring, with 38 open issues.
- No LLM and no natural-language interface: the researcher must express the problem as a variable space and a component pipeline in Python, which is a much higher barrier to entry than a prompt.
- No literature stage whatsoever — the loop cannot tell you whether the model it discovered is already known.
- Produces no prose: models, conditions and data only, so the write-up remains entirely manual.
- The theorist components are symbolic-regression-class methods; discovered models are only as interpretable as those methods allow, and nothing in the framework assesses whether a recovered equation is theoretically meaningful.
- Real-participant loops inherit every ethics, consent and IRB obligation of ordinary human-subject research, and the framework does not manage those.
- Modest traction (101 stars) means few external plugins beyond the group's own, so a new domain likely requires writing a runner and a theorist from scratch.

## Related projects in this catalog

- [`coral`](coral.md)
- [`arbor`](arbor.md)
- [`robin`](robin.md)

## Papers describing this project

- **AutoRA: Automated Research Assistant for Closed-Loop Empirical Research** — Musslick, S., Andrew, B., Williams, C., Hewson, J., Li, S., Marinescu, I., Dubova, M., Dang, G., Strittmatter, Y., Holland, J. (2024). *Journal of Open Source Software 9(104):6839*. [doi](https://doi.org/10.21105/joss.06839)

## Related references (literature catalog)

- `musslick2024autora` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
