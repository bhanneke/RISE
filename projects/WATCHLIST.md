# Landscape watch-list

Candidates that do not (yet) meet the inclusion bar, with the reason and
what would change the verdict. Reviewed on every sweep; the monthly
review should re-check each item and move it to the catalog, keep it, or
drop it with a dated note. Inclusion bar: a public artifact (repo,
leaderboard, or hosted system) with real content — papers alone don't
qualify.

_Last reviewed: 2026-10-01._

## Watching

| Item | Source | Why not yet | Would change the verdict |
|---|---|---|---|
| Gemini for Science / Empirical Research Assistance (ERA) | Google DeepMind, `labs.google/science` | ERA has a Nature paper (arXiv:2509.06503) and headline results (expert-level empirical code across genomics, epidemiology, etc.), but as of 2026-10-01 the "Gemini for Science" product bundling it with Co-Scientist/AlphaEvolve/NotebookLM is only a "register your interest" waitlist on Google Labs — no accessible system, no public code (added 2026-10-01) | Public rollout beyond the waitlist, or any usable prototype access |
| OpenAI Dots | OpenAI DevDay, 2026-09-29 | Real, usable always-on agent (Pro/Business Premium users today) with research-capable read-only background tasks, but it is a general-purpose computer-use agent across 4,000+ apps, not a research-specific system with research pipeline stages, inputs, or evaluation (added 2026-10-01) | Evidence of research-specific tooling, benchmarks, or workflows built on top of Dots |
| OpenAI "automated research intern" | OpenAI, 2026-09-06 report | Self-reported internal metric (3.1 agent-workdays/human-workday) describing how OpenAI's own research org uses its coding agents; not an external product, no public artifact (added 2026-10-01) | A named, externally accessible system rather than an internal usage statistic |
| xAI Grok Bot / Grok 4.x multi-agent | xAI, Aug 2026 | Usable always-on computer-use agent (SuperGrok Heavy/Cursor Ultra) with a named multi-agent architecture (Harper = "research" role), but general-purpose, not a research-pipeline system with its own inputs/outputs/evaluation (added 2026-10-01) | A research-specific product or benchmark distinct from the general agent |
| UKP review-feedback agent | `UKPLab/emnlp2026-reviewfeedbackagent` | Re-verified 2026-10-01: still Apache-2.0, 2★, 0 forks — EMNLP reproduction code for LazyReviewPlus, not a usable system | Packaging as an installable tool, or wanting a review-quality-audit sub-branch |
| AgenticDataBench | `AgenticDataBench/AgenticDataBench` (Tsinghua + Ant Group) | Re-verified 2026-10-01: real open-sourced testbed with leaderboard, 15-domain HF datasets, Apache-2.0 — but still measures data-science/business-analytics agents, no hypothesis/identification/write-up dimension | A curator decision to widen RISE to the data-analytics lane |
| AI-Research-SKILLs | `Orchestra-Research` (13.2k★, 933 forks, up from 12.4k★) | Re-verified 2026-10-01, still actively released (v1.7.1, June 2026): real substance but ML-infrastructure how-to (vLLM, Megatron, Instructor), not research methodology | An explicit scope label for engineering-skill packs |
| scientific-agent-skills | `K-Dense-AI` (47.2k★, up from 43.6k★; 181 skills, up from 163) | Re-verified 2026-10-01: ~65 of 181 skills are life-science/cheminformatics/clinical wrappers; the ~50+ general-methodology skills are covered better by catalogued packs | A methodology-only subset, or a scope widening |
| OmniScientist | `tsinghua-fib-lab/OmniScientist` | Re-verified 2026-10-01: repo is still a papers/documentation hub (MIT, 206★, 11 forks, 16 commits) — `/papers` and a README, no `/src` or agent implementation; Deep Ideation and AgentExpt remain paper-only | Constituent systems (Deep Ideation, AgentExpt) shipping their own code |
| aiXiv | `aixiv-org/aixiv-core` | Re-verified 2026-10-01: still a FastAPI submission backend (PDF upload, Postgres, S3) with no review logic; 5★, 0 forks | Review logic landing publicly; venues may need their own category |
| Personalized Auto-Research | arXiv 2608.14881 | Re-verified 2026-10-01: still a position paper only (CC BY-NC-ND); no code found anywhere | Any public artifact — until then it's a citation, not an entry |
| BixBench (v1) | `Future-House/BixBench`, Edison Scientific | Verified 2026-10-01: real repo, HF dataset, maintained v1.0 tag (current work is on v1.5/main) — but it is the explicitly-superseded predecessor of catalogued `bixbench3`, whose own entry already notes the lineage; cataloguing it separately would duplicate that lineage rather than add a distinct artifact | Evidence v1 (not v1.5 or bixbench3) remains the benchmark the field actually reports against |
| ScientistOne (system) | Google Cloud AI Research, arXiv 2605.26340 | Re-verified 2026-10-01: the project site (scientist-one.github.io) and paper remain the only public trace; the only GitHub hit is an unaffiliated third-party `scientistone-codex-plugin`, not the system itself | A public release of the system code |
| Point by Point | Nagaraj, r-r-agent.vercel.app | Verification attempt 2026-10-01 blocked (egress policy blocks the hosting domain; no GitHub repo found under the author's account) — no new evidence either way | An open repo or a stable service |
| SCOPE (experimental-design benchmark) | arXiv 2608.03501 | 300-paper benchmark for LLM experimental-design planning (ICML/NeurIPS/ICLR source papers, rubric-based LLM-as-judge) — no public repo, leaderboard, or dataset link found as of 2026-10-01 (added 2026-10-01) | A public code/data release |
| Agentic Economies for Autonomous Scientific Discovery | Tomašev et al. (Google DeepMind), arXiv 2609.31562 | A resource-management/governance framework paper for AI-agent research economies (markets, credit assignment, accountability) — conceptual position paper, no runnable artifact (added 2026-10-01) | Any reference implementation or testbed release |
| Project2Task | arXiv 2608.05225 | Project-level task-planning layer reporting gains layered on top of AutoResearchClaw — no public repo found as of 2026-10-01 (added 2026-10-01) | A public code release |
| Faraday / Replica | "Training AI Scientists to Replicate Research," arXiv 2608.13331 | 27B fine-tuned "AI Scientist" claiming to beat Opus 4.8/GPT-5.5 on replication tasks; appears to be a closed model (Inherent Labs-style) with an internal benchmark (Replica, n=310 tasks) — no public weights, code, or dataset found (added 2026-10-01) | A public release of Replica data or the model/code |
| Beyond Final Decisions | arXiv 2609.05947 | Process-centric peer-review diagnostic benchmark built from PeerRead/NLPeer-ARR-22/OpenReview-ICLR — no public repo or dataset release found as of 2026-10-01 (added 2026-10-01) | A public code/data release |
| ReplicatorBench | Nguyen et al., arXiv 2602.11354 (KDD 2026, AI-for-Sciences track) | Strong fit for the catalog's social-science emphasis — end-to-end benchmark for AI-agent replication of social/behavioral-science claims, code+data confirmed public — but posted Feb 2026, outside this sweep's July-Sept discovery window; flagging so next sweep scores it properly rather than missing it (added 2026-10-01) | None needed beyond a full scoring pass next cycle |

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
| Automated Alignment Researchers (Anthropic) | 2026-10-01 | `automated-w2s-research` |
| Terminal-Bench-Science | 2026-10-01 | `terminal-bench-science` |
| Econ Writing Skill (`hanlulong`) | 2026-10-01 | `econ-writing-skill` — the "probable duplicate of `econ-research-skills`'s `econ-write` component" claim was checked and found false: no such component exists anywhere in the catalog, and the catalogued `econ-agent-skills` (Weinert) is an unrelated analysis pack, not a writing pack |
| ForeSci | 2026-10-01 | `foresci` — official code release (`roytian1992/ResearchForesight`) now ships the 500-task set, frozen per-domain knowledge bases, and evaluation/judge scripts promised in the paper |
| AI Peer Review (`poldrack/ai-peer-review`) | 2026-10-01 | `ai-peer-review` — verified as a real, actively maintained tool (154★, 25 forks, MIT) distinct from its catalogued Claude-only fork `ai-peer-review-skill`: default six-provider cross-model review panel vs. the fork's single-family subagents |
| PaperDoctor | 2026-10-01 | `paperdoctor` — new (Sept 2026) multi-institution pre-submission diagnostic agent (11 Claude Code skills; evidence-grounded claim/code/theory checks with selective experiment re-execution) |
| LitReview Arena | 2026-10-01 | `litreview-arena` — new (Aug 2026, ICML 2026) battle-style expert benchmark + `LitJudge` evaluator for literature-review-writing agents |
| RECLAIM | 2026-10-01 | `reclaim` — new (Sept 2026) tiered reproducibility benchmark of 100 NeurIPS 2025 papers (Run/Retrain/Reimplement by artifact completeness), full execution traces public |
| ReproAgent | 2026-10-01 | `reproagent` — new (Aug 2026, EMNLP 2026 Findings) contract-guided paper-to-code reproduction agent, beats same-backbone baselines on PaperBench Code-Dev |
