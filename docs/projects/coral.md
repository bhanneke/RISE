<!-- DO NOT EDIT — auto-generated from projects/landscape/coral.yml by scripts/build_indexes.py -->

# CORAL

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/Human-Agent-Society/CORAL>

**Source:** [`projects/landscape/coral.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/coral.yml)

## Positioning

Infrastructure (arXiv:2604.01658) for *multi-agent autonomous self-evolution* — organizations of AI agents that run experiments, share knowledge through persistent stores, and continuously improve solutions against a user-supplied grading script. Sits in the *autoresearch infrastructure* layer alongside Aviary and MLGym, but emphasizes evolution and self-improvement rather than benchmarking.

## Distinctive contribution

Treats the *organization* of agents (workspaces, shared knowledge, judges) as a first-class engineering surface, with rubric-based judge packages (race_japan_grader, apex_judge) that themselves spawn Claude Code for evaluation. Natively integrated with Claude Code, OpenCode, Codex, and Cursor.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Four stages spanning design through internal review; oriented to optimization rather than publication. |
| Autonomy level | 3 | Autonomous evolution loop; user supplies task + grader. |
| Architectural transparency | 3 | Open under MIT; arXiv:2604.01658; integrates Claude Code, OpenCode, Codex, Cursor with documented patterns. |
| Inputs supported | 2 | Codebase + grading script inputs; multiple coding-agent back-ends. |
| Outputs / reproducibility | 2 | Isolated workspaces + persistent knowledge stores; LLM nondeterminism limits exact reruns. |
| Internal evaluation | 2 | Rubric-judge packages provide structured internal evaluation; arXiv paper presents systematic results. |
| Openness | 3 | MIT-licensed; uv-installable; broad agent-back-end support. |
| Maturity / traction | 2 | 655 stars; active 2026 development; integrated with major coding agents. |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `research-design` `data-analysis` `code-generation` `referee-simulation`


**Architectural features:** `multi-agent` `persistent-memory` `artifact-versioning` `iterative-loop` `debate-consensus`


**Inputs:** `codebase` `grading-script`


**Outputs:** `evolved-solutions` `shared-knowledge-store` `judge-reports`


**Data sources:** `user-provided`


**Knowledge sources:** `shared-knowledge-store`


## Limitations

- Optimization-focused: best fit for *grade-against-script* tasks, not open-ended scholarly authoring.
- Heavy on coding-agent integration; lighter on literature-layer integration.

## Related projects in this catalog

- [`aviary`](aviary.md)
- [`mlgym`](mlgym.md)
- [`agent-laboratory`](agent-laboratory.md)

## Papers describing this project

- **CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery** — Qu, A., Zheng, H., Zhou, Z., Yan, Y., Tang, Y., Ong, S. Y., et al. (2026). *arXiv*. [arXiv:2604.01658](https://arxiv.org/abs/2604.01658)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
