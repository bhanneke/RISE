<!-- DO NOT EDIT — auto-generated from projects/e2er.yml by scripts/build_indexes.py -->

# E2ER — End-to-End Research

`owned` · status: `active` · focus: `end-to-end` · discipline: `economics` · started: 2025

**Project page:** <https://github.com/bhanneke/E2ER-project>

**Source:** [`projects/e2er.yml`](https://github.com/bhanneke/RISE/blob/main/projects/e2er.yml)

## Positioning

E2ER is a strategist-driven agentic research pipeline that takes a research idea (human- or agent-supplied) and carries it through literature synthesis, identification, data acquisition, analysis, and paper drafting. It targets the full inputs → knowledge production → outputs arc of the RISE diagram, with explicit data and knowledge side-inputs.

## Distinctive contribution

Strategist-orchestrated multi-agent design with persona-rich review loops; emphasizes durable artifact production over chat output, and treats methodological skills (econometrics, replication, referee simulation) as first-class reusable modules.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Covers ideation through referee simulation — 12 of 14 canonical stages. |
| Autonomy level | 2 | Supervised agent — human sets up the task and reviews final artifacts; intermediate steps are autonomous. |
| Architectural transparency | 2 | Architecture, prompts, and skills published on GitHub; some orchestration internals still evolving. |
| Inputs supported | 3 | Accepts ideas, RQs, prior papers; integrates literature corpora and live data sources. |
| Outputs / reproducibility | 2 | Versioned artifacts persisted; full end-to-end reproducibility from inputs still in progress. |
| Internal evaluation | 1 | Reviewer-simulation loops provide internal evaluation; no external benchmark or peer-reviewed publication yet. |
| Openness | 2 | Public repository under permissive license; some examples reproducible without proprietary credentials. |
| Maturity / traction | 1 | Active research prototype; single-team use as of 2026-05. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `literature-discovery` `literature-synthesis` `research-design` `data-acquisition` `data-analysis` `formal-modeling` `code-generation` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `rag-knowledge-base` `persistent-memory` `dag-orchestration` `iterative-loop` `artifact-versioning`


**Inputs:** `human-idea` `agentic-idea` `research-question` `prior-paper`


**Outputs:** `paper-draft` `figures` `tables` `code` `referee-reports` `replication-package`


**Data sources:** `fred` `yfinance` `ssrn` `openalex`


**Knowledge sources:** `arxiv` `ssrn` `openalex` `semantic-scholar`


## Limitations

- End-to-end reproducibility from inputs not yet demonstrated on a public test case.
- Domain coverage currently focused on economics/finance; portability to other fields untested.
- External evaluation (peer review, third-party replication) pending.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`zeropaper`](zeropaper.md)
- [`social-science-replicability`](social-science-replicability.md)

## References

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
- `cao2025aifinance` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `cunningham2025claudecode` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `eberhardt2025claudecode` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
