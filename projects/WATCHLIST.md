# Landscape watch-list

Candidates that do not (yet) meet the inclusion bar, with the reason and
what would change the verdict. Reviewed on every sweep; the monthly
review should re-check each item and move it to the catalog, keep it, or
drop it with a dated note. Inclusion bar: a public artifact (repo,
leaderboard, or hosted system) with real content — papers alone don't
qualify.

_Last reviewed: 2026-09-08._

## Watching

| Item | Source | Why not yet | Would change the verdict |
|---|---|---|---|
| UKP review-feedback agent | `UKPLab/emnlp2026-reviewfeedbackagent` | Public, Apache-2.0, ships LazyReviewPlus — but EMNLP reproduction code, not a usable system (2★, 0 forks) | Packaging as an installable tool, or wanting a review-quality-audit sub-branch |
| AgenticDataBench | Tsinghua + Ant Group | Solid artifact (Apache-2.0, leaderboard, HF datasets) but measures data-science/business-analytics agents — no hypothesis, identification, or write-up dimension | A curator decision to widen RISE to the data-analytics lane |
| AI-Research-SKILLs | `Orchestra-Research` (12.4k★) | Real substance but ML-infrastructure how-to (vLLM, Megatron, Instructor), not research methodology | An explicit scope label for engineering-skill packs |
| scientific-agent-skills | `K-Dense-AI` (43.6k★) | ~150 of 163 skills are life-science/cheminformatics tool wrappers; the ~13 methodology skills are covered better by catalogued packs | A methodology-only subset, or a scope widening |
| econ-writing-skill | `hanlulong` (589★) | Probable duplicate: already catalogued inside `econ-research-skills` as its `econ-write` component | Confirmation that it diverged into distinct content |
| OmniScientist | `tsinghua-fib-lab` | Paper hub for a research programme, not a runnable system | Constituent systems (Deep Ideation, AgentExpt) shipping their own code |
| aiXiv | `aixiv-org/aixiv-core` | The claim (AI-authored venue with agentic review) is not evidenced — repo is a FastAPI submission backend without review logic | Review logic landing publicly; venues may need their own category |
| ForeSci | arXiv 2606.00644 | Best benchmark *idea* found (leakage-controlled forecasting of research directions) but no code, data, or leaderboard | Any public artifact |
| Personalized Auto-Research | arXiv 2608.14881 | Position paper only (CC BY-NC-ND); no code | Any public artifact — until then it's a citation, not an entry |
| poldrack/ai-peer-review | github.com/poldrack | Upstream of the catalogued `ai-peer-review-skill`; not independently verified yet | A verification pass — may be the stronger entry |
| BixBench (v1) | Edison Scientific / FutureHouse | Predecessor of catalogued `bixbench3`; not independently verified yet | A verification pass if v1 remains the more-used baseline |

## Dropped (with date and reason)

| Item | Dropped | Reason |
|---|---|---|
| AI Economist Agent (arXiv 2606.20041) | 2026-09-08 | Code confirmed absent ~3 months post-posting (not on the abs page, in the HTML, or on the author's GitHub); single-author framework paper |
| econ-auto-research (`hanlulong`) | 2026-09-08 | Still a stub ("there is no code here yet"), 22★ on the pitch alone; same maintainer is catalogued via `openecon-data`, so it resurfaces if it ships |
| IV Co-Scientist (arXiv 2602.07943) | 2026-09-08 | CLeaR 2026 paper is real but no artifact 7 months on; the only candidate repo (`ivaxi0s/iv-llm`, 1★) is unconfirmable and below the bar |
| Sakana Marlin / Fugu Ultra | 2026-09-08 | Closed commercial products, no public artifact to verify; Fugu Ultra's paper-reproduction claims unverifiable |

## Graduated to the catalog

| Item | Added | As |
|---|---|---|
| ResearchClawBench | 2026-09-08 | `researchclaw-bench` |
| PARNESS | 2026-09-08 | `parness` |
| SwarmResearch | 2026-09-08 | `swarmresearch` |
