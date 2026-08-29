---
citekey: jiang2024costorm
title: 'Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations'
authors:
- Jiang, Y.
- Shao, Y.
- Ma, D.
- Semnani, S. J.
- Lam, M. S.
year: 2024
venue: EMNLP 2024
doi: ''
url: https://arxiv.org/abs/2408.15232
kind: paper
themes:
- human-ai-research-collaboration
- agentic-reasoning
- evaluation-of-ai-research
methods:
- system-design
- benchmark-evaluation
- human-evaluation
relates_to_projects:
- storm
status: skimmed
arxiv_id: '2408.15232'
---

## Summary

Co-STORM (Collaborative STORM) targets the "unknown unknowns"
problem: chatbots and generative search engines answer concrete
queries well, but users struggle to discover what they do not know to
ask. Modeled on children learning by listening to and joining adult
conversations, Co-STORM lets a user observe and occasionally steer a
discourse among several LM agents that ask questions on the user's
behalf. A dynamic mind map organizes the information uncovered, and
the system produces a comprehensive report as takeaways. For
automatic evaluation the authors build WildSeek from real
information-seeking records with user goals; Co-STORM outperforms
baselines on discourse-trace and report quality. In a human
evaluation, 70% of participants preferred Co-STORM to a search
engine and 78% to a RAG chatbot. EMNLP 2024 main conference (arXiv
v2, October 2024).

## Contribution

Claimed: a new interaction paradigm for serendipitous information
discovery; the mind map as a discourse-tracking aid; the WildSeek
dataset; superiority over baselines and user preference over search
and RAG chat.

What the abstract supports: the two preference percentages are given;
"outperforms baseline methods" on discourse trace and report quality
is not quantified and the baselines are unnamed. The title promises
"engaged human learning", but the abstract reports preference, not
learning outcomes.

## Method

Design: multi-agent discourse with intermittent user steering; a
dynamic mind map; report generation.

Evaluation: WildSeek (real information-seeking records with user
goals) for automatic evaluation of discourse-trace and report
quality; human evaluation as preference against a search engine and
a RAG chatbot.

Not specified in the abstract: the number of participants and task
design, the LLM(s), how agent roles are assigned, session length,
how often users actually steered, and whether report factuality was
evaluated.

## Relevance to RISE

Informs `literature-discovery` and `literature-synthesis`. Catalog
slug: `storm` (the catalog scores STORM/Co-STORM as one project; its
autonomy score of 2 reflects Co-STORM's collaborative steering, and
`human-in-loop` is among its architectural tags). Predecessor:
[shao2024storm](shao2024storm.md). The paper is a concrete
division-of-labor design for human–AI research collaboration: agents
generate the questions, the human observes and intervenes.

Multi-agent structure / aggregation: Co-STORM's collaborative
discourse — several LM agents in a shared conversation with
intermittent human steering, aggregated through a dynamic mind map
into a final report — is a multi-agent structure with an explicit
aggregation artifact, and the abstract reports gains on
discourse-trace and report quality over baselines; it does not
separate the effect of multi-agent discourse from that of human
steering or of the mind map.

## Critique / open questions

- Preference over a search engine and a RAG chatbot is a modest bar
  for a research tool; effect on what users learn is not reported in
  the abstract.
- Report factuality is not mentioned in the abstract.
- "Occasionally steer" is not quantified; the balance between
  observation and intervention is unknown from the abstract.
- The educational analogy motivates the design but is not itself
  tested.
- The abstract concedes no limitations.

## Key quotes

> "Unlike QA systems that require users to ask all the questions,
> Co-STORM lets users observe and occasionally steer the discourse
> among several LM agents." (abstract)

> "To facilitate user interaction, Co-STORM assists users in tracking
> the discourse by organizing the uncovered information into a
> dynamic mind map, ultimately generating a comprehensive report as
> takeaways." (abstract)

> "In a further human evaluation, 70% of participants prefer Co-STORM
> over a search engine, and 78% favor it over a RAG chatbot."
> (abstract)
