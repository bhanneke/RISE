<!-- DO NOT EDIT — auto-generated from projects/landscape/ai-researcher.yml by scripts/build_indexes.py -->

# AI-Researcher (HKUDS)

`external` · status: `dormant` · focus: `end-to-end` · discipline: `computer-science` · started: 2025

**Project page:** <https://github.com/HKUDS/AI-Researcher>

**Licence:** `none`

!!! warning "No licence declared"
    The repository declares no licence, so its code cannot be reused,
    modified or redistributed without the maintainer's permission. RISE
    describes and links to the project; nothing from it is reproduced here.

**Source:** [`projects/landscape/ai-researcher.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ai-researcher.yml)

## Positioning

An autonomous multi-agent system for ML research (arXiv 2505.18705, NeurIPS 2025 spotlight) that takes either a detailed idea (Level 1) or only a set of reference papers (Level 2) and runs resource collection from arXiv, GitHub and Hugging Face, idea generation, algorithm design, implementation and experiments inside a Docker container, an iterative validate-and-refine cycle, and hierarchical paper writing. Sits beside sakana-ai-scientist, agent-laboratory and deepscientist in the computer-science end-to-end cluster; a hosted successor runs at novix.science.

## Distinctive contribution

Scientist-Bench, released with the system: tasks built from state-of-the-art papers in CV, NLP, data mining and information retrieval, with the human-written paper as ground truth, split into guided (Level 1) and open-ended (Level 2) tasks and scored by evaluator agents on novelty, experimental comprehensiveness, theoretical foundation, result analysis and writing quality. The benchmark data and its construction pipeline are published in the repo, so other AI scientists can be run against the same tasks.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Seven stages from literature collection through implementation, experiments and paper writing; review exists only as Scientist-Bench evaluator agents scoring finished outputs, not as a stage inside the research pipeline. |
| Autonomy level | 3 | Runs from an idea or a list of reference papers to a full manuscript without per-step approval; the README and paper describe it as fully autonomous. |
| Architectural transparency | 3 | Agent code, prompts, Docker environment, run scripts and the Scientist-Bench data and collection pipeline are all public in the repo. |
| Inputs supported | 2 | Two input forms (detailed idea, reference-paper list) with literature, code and dataset collection from arXiv, GitHub and Hugging Face; no private corpus or user data connector. |
| Outputs / reproducibility | 2 | Persists code, experiment logs and a LaTeX paper in the agent workplace; LLM-driven runs are not regenerable from declared inputs and there is no artifact manifest. |
| Internal evaluation | 3 | Peer-reviewed at NeurIPS 2025 (spotlight) with a purpose-built benchmark; a third-party audit (ScientistOne, arXiv 2605.26340) found that every audited baseline system had at least one systematic integrity failure. |
| Openness | 1 | Source is public but no licence is declared, so reuse is not permitted; runs also need paid LLM API keys and a GPU container. |
| Maturity / traction | 2 | About 5.8k stars and 724 forks with a hosted product (novix.science), but no tagged releases and no push since 2025-10-16, so the open-source line is dormant. |
| Cross-family policy | 0 | Separate COMPLETION_MODEL and CHEEP_MODEL settings pick a strong and a cheap model, but no role reviews another's work across model families. |
| Runtime assurance | 1 | The implementation phase executes and tests code and refines on the results; there is no in-pipeline citation, claim or method-code audit before the paper is written. |
| Cross-platform portability | 2 | LiteLLM routing supports several providers (Claude, OpenAI, DeepSeek, Gemini via OpenRouter), but execution is tied to the project's own Docker image. |

*Scored on 2026-09-29. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `hypothesis-generation` `research-design` `code-generation` `data-analysis` `paper-drafting`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop`


**Inputs:** `research-idea` `reference-papers`


**Outputs:** `paper-draft` `code` `experiment-results`


**Data sources:** `benchmark-datasets` `hugging-face`


**Knowledge sources:** `arxiv` `github` `hugging-face`


## Limitations

- No licence declared: the code cannot be reused, modified or redistributed without the maintainer's permission.
- Dormant: last push 2025-10-16 and 65 open issues; development appears to have moved to the hosted novix.science service.
- The ScientistOne CoE Audit (arXiv 2605.26340) covered 75 papers from five systems, AI-Researcher among the four baselines, and reports that every baseline showed at least one systematic failure mode (hallucinated reference rates up to 21%, score verification passing in as few as 42% of papers, method-code alignment between 20% and 80%); the abstract gives these as ranges across baselines, not per system.
- Scope is ML/AI research (CV, NLP, data mining, IR); no evidence in economics, finance or the social sciences.
- Scientist-Bench quality scores come from LLM evaluator agents, not human referees.
- The README's paper-writing example contains a literal OPENAI_API_KEY value, a secrets-hygiene problem in the published instructions.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`deepscientist`](deepscientist.md)
- [`autoresearchclaw`](autoresearchclaw.md)
- [`zochi`](zochi.md)

## Papers describing this project

- **AI-Researcher: Autonomous Scientific Innovation** — Tang, J., Xia, L., Li, Z., Huang, C. (2025). *NeurIPS 2025*. [arXiv:2505.18705](https://arxiv.org/abs/2505.18705)

## Related references (literature catalog)

- Tang, J. et al. (2025). [*AI-Researcher: Autonomous Scientific Innovation*](../papers/notes/tang2025airesearcher.md) `tang2025airesearcher`
- Meng, R. et al. (2026). [*ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence*](../papers/notes/meng2026scientistone.md) `meng2026scientistone`
