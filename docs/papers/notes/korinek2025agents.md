---
citekey: korinek2025agents
title: 'AI Agents for Economic Research: August 2025 Update of "Generative AI for Economic Research: Use Cases and Implications for Economists"'
authors:
- 'Korinek, A.'
year: 2025
venue: 'Update to Journal of Economic Literature 61(4)'
doi: ''
url: https://www.genaiforecon.org/JEL-2025-Aug-AIAgents.pdf
kind: survey
themes:
- autonomous-research-agents
- agentic-tool-use
- research-productivity
methods:
- survey
- tutorial
relates_to_projects: []
status: skimmed
---

## Summary

The mid-2025 instalment of the semi-annual updates Korinek committed
to when his December 2023 JEL article ([korinek2023genai]) was
published. This update is new in its entirety and is about agents:
LLM-based systems that plan, use tools, keep memory and execute
multi-step research tasks. Its stated aim is to demystify them and to
let economists without programming expertise build their own, using
"vibe coding" and agentic frameworks such as LangGraph. Worked
examples and complete code cover agents that run literature reviews
across many sources, write and debug econometric code, fetch and
analyse economic data, and coordinate multi-step research workflows.
Earlier material is not repeated: the December 2024 update covers
reasoning and collaboration with several dozen use cases, and the 2023
original covers LLM basics and longer-term implications for the
profession.

## Contribution

A practitioner's bridge rather than new evidence: conceptual framing of
agents for an economics audience plus runnable implementations. Its
weight in the field comes from where it sits — a living JEL survey by
an author who also serves (unpaid, as disclosed) on Anthropic's
Economic Advisory board — which makes it the reference economists are
most likely to have read on the topic.

## Method

Survey and tutorial with working code. No evaluation of the agents it
builds; claims about what they can do rest on the demonstrations.

## Relevance to RISE

The most widely read on-ramp to agentic research in economics, and
the natural citation when RISE describes how the discipline itself
frames these systems. Its building blocks (literature review, code
generation, data acquisition, workflow coordination) map onto the
`literature-discovery`, `code-generation`, `data-acquisition` and
orchestration stages of the pipeline anatomy. Because it teaches
economists to assemble their own agents, it is also the upstream of
many home-built systems that never become catalogue entries — a
useful caution when reading the landscape as the full population.

## Critique / open questions

Build-your-own emphasis without an evaluation layer: the paper shows
how to make an agent run, not how to know whether its output is right,
which is the gap the verification literature in this knowledge base
keeps returning to. Being a living document it will date quickly; cite
the specific update.

## Key quotes

> "The objective of this paper is to demystify AI agents—autonomous
> LLM-based systems that plan, use tools, and execute multi-step
> research tasks—and to provide hands-on instructions for economists
> to build their own, even if they do not have programming expertise."
> (abstract)

> "The paper demonstrates that by 'vibe coding' (programming through
> natural language) and building on modern agentic frameworks like
> LangGraph, any economist can build sophisticated research assistants
> and other autonomous tools in minutes." (abstract)
