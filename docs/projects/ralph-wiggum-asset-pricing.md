<!-- DO NOT EDIT — auto-generated from projects/landscape/ralph-wiggum-asset-pricing.yml by scripts/build_indexes.py -->

# ralph-wiggum-asset-pricing

`external` · status: `active` · focus: `drafting` · discipline: `finance` · started: 2026

**Project page:** <https://github.com/chenandrewy/ralph-wiggum-asset-pricing>

**Licence:** `none`

!!! warning "No licence declared"
    The repository declares no licence, so its code cannot be reused,
    modified or redistributed without the maintainer's permission. RISE
    describes and links to the project; nothing from it is reproduced here.

**Source:** [`projects/landscape/ralph-wiggum-asset-pricing.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ralph-wiggum-asset-pricing.yml)

## Positioning

Geoff Huntley's "Ralph Wiggum" loop applied to an academic asset-pricing paper: the human writes a paper specification (the paper in bullet points), an economic-background file and a test selection; then Claude Code or Codex, running with permissions disabled inside a firewalled dev container, repeats plan → improve → test on the LaTeX paper and R code until every PASS/FAIL test passes. The human stays "on the loop", watching logs and editing the spec between stretches. Sits in the drafting-and-revision layer of RISE for finance theory, next to ape and clo-author on the empirical side.

## Distinctive contribution

The loop's stopping rule is a test suite written for a finance paper: 25 agent-run tests in six families (required elements, fact checks of claims against code output, literature and each other, conformance to the spec, theory-paper quality, figure rendering, writing) plus optional open-ended referee agents. It produced a public case study, "Hedging the Singularity" (arXiv 2604.16997), whose abstract discloses that it was AI-generated and whose human preface reports that the author could not reach "human as Clockmaker" (set up the loop, then accept the output unedited). Every iteration is a git commit, and the full run, a human-written preface and three human referee reports on an earlier paper are kept on separate branches for comparison.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Six stages from model and code through drafting, test-driven revision and optional referee agents; research-question and design choices stay in the human-written spec, and literature is supplied rather than discovered. |
| Autonomy level | 2 | Once the spec, tests and baseline are committed the loop runs unattended, but the human watches, stops and re-steers between stretches and edited the final paper by hand. |
| Architectural transparency | 3 | Loop scripts, agent wrapper, prompts, all 25 test and referee scripts, config and dev container are public, and the full run that produced the paper is kept on its own branch. |
| Inputs supported | 2 | Spec, background file and an optional starting paper/code, with credentialed WRDS access for data; literature is supplied by the user rather than searched. |
| Outputs / reproducibility | 2 | Paper LaTeX, R code, figures and test reports are committed once per iteration (rloop-NN) with per-iteration PDF snapshots; agent runs are not regenerable from the inputs and there is no data manifest. |
| Internal evaluation | 1 | One worked case (Hedging the Singularity) with the author's own preface assessing where the loop fell short; no systematic evaluation across papers and no external review of the output. |
| Openness | 1 | Source is public but no licence is declared, so reuse is not permitted; the case-study run consumed two $200/month Claude Code subscriptions. |
| Maturity / traction | 1 | 17 stars, 0 forks, single author, last push 2026-09-11: an active research prototype. |
| Cross-family policy | 1 | Each author and test script sets its own AGENT (Claude or Codex), so tests can run on a different family from the author, but the shipped default is Claude only. |
| Runtime assurance | 3 | The loop cannot stop until the selected tests pass, and the full suite fact-checks claims against code output, literature and theory, checks spec conformance and inspects rendered figures; main ships a 6-test subset. |
| Cross-platform portability | 1 | Two agent CLIs (Claude Code, Codex) on macOS/Linux or WSL2, recommended inside the project's dev container. |

*Scored on 2026-09-29. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `formal-modeling` `code-generation` `data-analysis` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `tool-use` `human-in-loop` `iterative-loop` `artifact-versioning`


**Inputs:** `paper-specification` `economic-background` `baseline-paper-and-code` `wrds-data`


**Outputs:** `paper-draft` `latex-source` `analysis-code` `figures` `test-reports`


**Data sources:** `wrds` `user-provided`


**Knowledge sources:** `user-supplied-literature`


## Limitations

- No licence declared: the code cannot be reused, modified or redistributed without the maintainer's permission.
- Runs agents with --dangerously-skip-permissions (Claude) or --sandbox danger-full-access (Codex); safety rests on the dev-container firewall, which archival branches implement in a way that can fail open.
- By the author's own account the spec had to be tight and the open-ended referee agents did not work well; the goal of an unedited paper was not reached.
- Built and tested on one asset-pricing theory paper; empirical papers need tests ported from a separate repo (HumanxAI-ChenAY).
- Costly: the full 25-test run used two $200/month Claude Code subscriptions.

## Related projects in this catalog

- [`karpathy-autoresearch`](karpathy-autoresearch.md)
- [`writing-driven-autoresearch`](writing-driven-autoresearch.md)
- [`ape`](ape.md)
- [`clo-author`](clo-author.md)
- [`pai-econ-claude`](pai-econ-claude.md)
