---
citekey: ji2023hallucination
title: "Survey of Hallucination in Natural Language Generation"
authors: ["Ji, Z.", "et al."]
year: 2023
venue: "ACM Computing Surveys"
doi: ""
url: ""
kind: survey
themes:
  - hallucination
  - evaluation-of-ai-research
methods:
  - survey
relates_to_projects:
  - paper-qa
  - open-scholar
  - storm
  - gpt-researcher
status: read
rating: 4
---

## Summary

A comprehensive survey of hallucination in natural-language
generation — defining the phenomenon, distinguishing *intrinsic*
(contradicts the source) from *extrinsic* (unverifiable against the
source) hallucination, mapping causes (training data, modeling,
inference, decoding), and cataloging detection and mitigation
techniques task by task (summarization, dialogue, MT, QA, data-to-text).

## Contribution

The reference taxonomy that subsequent work in factuality,
faithfulness, and grounded generation has built on. By organizing
hallucination type × cause × task, it makes interventions comparable
and exposes that "hallucination" is not a single phenomenon.

## Method

Literature survey covering work through 2022. Categorizes papers by
task and intervention class; tabulates detection metrics; identifies
open problems.

## Relevance to RISE

A RISE pipeline that drafts papers, retrieves literature, or
generates citations is inherently exposed to both intrinsic and
extrinsic hallucination — and many of the catalog's projects
([`paper-qa`](../../projects/paper-qa.md),
[`open-scholar`](../../projects/open-scholar.md),
[`storm`](../../projects/storm.md)) cite citation-grounding and
retraction-awareness as core selling points precisely because of the
failure modes catalogued here. The taxonomy is also useful for
*evaluating* RISE systems: distinguishing fabricated results from
unfaithful summaries from outdated facts requires the type × task
breakdown.

## Critique / open questions

- Predates the agentic turn — does not address compounding
  hallucination across multi-agent loops, or hallucination injected
  via tool outputs.
- The survey treats hallucination as undesirable; the framing does
  not engage with cases (e.g., hypothesis generation) where
  *generating beyond the source* is the point — relevant for RISE
  ideation stages.

## Key quotes

*To be added on re-read with page references.*
