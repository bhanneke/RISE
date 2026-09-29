<!-- DO NOT EDIT — auto-copied from skills/daaf/details/daaf-deploy-smoke-testing.md -->

# `/daaf-deploy-smoke-testing`

Contributor tool that checks a live DAAF install end to end on its configured provider route, from a free preflight through one paid round trip to a six-probe functional battery and a zero-cost deterministic test tier. Requires the DAAF_DEV=1 developer image.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../daaf/">DAAF — Data Analyst Augmentation Framework (Brian Heseung Kim)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>LGPL-3.0-or-later (as declared in the README, badge and CITATION.cff; the repo ships the GPL-3.0 text as LICENSE plus COPYING.LESSER)</code></div><div><b>Updated:</b> 2026-08-08</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/DAAF-Contribution-Community/daaf/contents/.claude/skills/daaf-deploy-smoke-testing/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/daaf/daaf-deploy-smoke-testing/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/DAAF-Contribution-Community/daaf/blob/main/.claude/skills/daaf-deploy-smoke-testing/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/DAAF-Contribution-Community/daaf?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## DAAF Deployment Smoke Testing

Route-aware, in-situ verification that a live DAAF installation actually works, configured exactly as the user set it up. The suite (`scripts/deploy_smoke/`) auto-detects which of DAAF's four provider routes is active from the live environment, then runs tiered probes — from a free no-LLM preflight up through live functional round-trips — and writes an evidence-quoted report with an overall PASS/FAIL. It answers one question: *does this deployment function end-to-end in its configured route?* It is deliberately scoped to deployment/configuration health, not model quality (that is DAAFBench) and not package availability (that is `scripts/smoke_tests/`). This is a development/contributor tool: it assumes the `DAAF_DEV=1` image and is not surfaced in the end-user install guide. Triggers include post-install verification, post-rebuild/update checks, any provider or configuration change, pre-release validation across multiple configurations, and direct requests like "is my install working" or "smoke test the config."

### Critical Disambiguation — Three Smoke Tools, Three Questions

All three exist in the repo; loading the wrong one wastes effort. Route by the *question being asked*:

```
What is being verified?
├─ "Does my DEPLOYMENT work in its provider route?"          → THIS skill
│    (live install health: routing, hooks, dispatch, shim, statuslines)
│    scripts/deploy_smoke/run_deploy_smoke.py
│
├─ "Does a MODEL follow DAAF's rules / adhere behaviorally?" → DAAFBench
│    (scored behavioral-adherence evaluation across a case battery)
│    benchmarks/  — heavyweight, cost-driven, NOT an install check
│
└─ "Does an R/Python LIBRARY load and run?"                  → library smokes
     (per-skill package import/execute checks)
     scripts/smoke_tests/run_all_smoke_tests.sh
```

The deployment suite *reuses* Tier D to run the library smokes and *reuses* DAAFBench's output-parsing helpers, but its purpose is distinct: it is the only tool that verifies the wiring between Claude Code, the configured provider, the hooks, and the subagent machinery is intact for *this* install.

### What It Verifies (by tier)

| Tier | Cost | What it checks | LLM? |
|------|------|----------------|------|
| **0** | free | Route detection + `--route` assertion, `DAAF_DEV=1`, env coherence for the detected route, model-family + ceiling-hook posture, context-window declaration (lane-aware: `DAAF_PROVIDER_SHIM`+`SHIM_BACKEND_MODE` select the ~370k chatgpt-subscription ceiling), CLI liveness, all hooks registered, both statuslines render, shim `/health` (shim routes), chatgpt `auth.json` readable, workspace invariants, R UTF-8 locale (image `LANG`/`LC_ALL=C.UTF-8`) | no |
| **1** | ~cents | One live `claude -p` round-trip + the plumbing around it: response returned, transcript located, audit-log hook fired, context-reporter injection, `/tmp` coordination caches, statusline against the real session, token/cost parsing | 1 call |
| **2** | ~$0.60–3.00 / profile | Six-probe functional battery: subagent dispatch + search, coding agent writes + runs via `run_with_capture`, web access (WebSearch), skill loading, isolation-strip hook (SKIP-tolerant), nested-dispatch deny hook | 6 calls |
| **D** | free | Deterministic battery: a harness self-test first (TD.0 — the suite's own provider-free `unittest` module), then `bats tests/bash`, Pester, `check-daaf-conventions.sh` lint, safety-hook tests, single-command hook tests, and (opt-in) the R/Python library smoke suite. Every Tier D subprocess runs under a sanitized env — the two live-config contaminants `CLAUDE_CODE_MAX_CONTEXT_TOKENS` and `DAAF_BRANCH` are stripped (defense-in-depth atop each battery's own fixture isolation); PATH/HOME/credentials/toolchain are preserved | no |

Tier 2 cost scales with the configured model. Tiers 0 and D run once; Tiers 1 and 2 run once *per profile*. Each Tier 2 run operates inside its own per-run, UUID-owned sandbox (`scripts/deploy_smoke/_sandbox/run_<uuid>/`) that it self-cleans on exit, so no fixture from a prior run can satisfy a later one; correspondingly, the T2.2 coding probe PASSes only on freshly captured execution evidence, not on source text or a stale log (see `references/interpreting-results.md`).

### When to Run

- **After a fresh install or a rebuild/update** — confirm the deployment still routes, dispatches, and enforces hooks.
- **After any provider or configuration change** — a new API key, a model remap (`ANTHROPIC_DEFAULT_*`), a shim backend switch, a base-URL change.
- **Before a release** — validate across each configuration you support (Anthropic, OpenRouter with multiple model families, the shim routes).
- **When something feels off** — statusline shows the wrong window, subagents behave oddly, a hook seems not to fire.

### Invocation

Run from anywhere (the CLI resolves the repo root itself). All commands are single Bash calls.

```bash
## Free preflight only — no API cost, good first check after any change:
python3 /daaf/scripts/deploy_smoke/run_deploy_smoke.py --tiers 0 --yes

## Default run (Tiers 0,1,2) on the auto-detected route, with the cost confirmation prompt:
python3 /daaf/scripts/deploy_smoke/run_deploy_smoke.py

## Assert the expected route — detection mismatch is a FAIL (catches a mis-set env):
python3 /daaf/scripts/deploy_smoke/run_deploy_smoke.py --route anthropic-subscription --tiers 0

## Everything, including the deterministic battery and the (slow) library smokes:
python3 /daaf/scripts/deploy_smoke/run_deploy_smoke.py --tiers 0,1,2,D --include-r-smoke --yes
```

**Flags** (verified against `--help`):

| Flag | Effect |
|------|--------|
| `--route ROUTE` | Assert the expected route; a detection mismatch is a FAIL instead of a silent override. Values: `anthropic-subscription`, `openrouter`, `chatgpt-subscription`, `openai-api`. |
| `--profiles A,B,C` | Comma-separated profile names from `profiles.yaml` (OpenRouter route — see below). |
| `--tiers 0,1,2,D` | Which tiers to run. Default `0,1,2`. Add `D` for the deterministic battery. |
| `--include-r-smoke` | Include the slow R/Python library smoke suite inside Tier D. |
| `--timeout N` | Per-probe timeout seconds (0 = per-tier defaults: 180/300/600). |
| `--yes` | Skip the pre-launch cost/summary confirmation (needed for non-interactive runs). |
| `--report-dir DIR` | Override the report output directory. |

The suite omits `--model` on its `claude -p` probes by default, so it tests the model **as configured** (from `settings.json` / `ANTHROPIC_MODEL` / the profile overlay) — exactly what a real session would resolve.

### OpenRouter Multi-Profile Runs

The OpenRouter route can talk to multiple model families. `--profiles` runs Tiers 1–2 once per named profile (Tiers 0 and D run once), applying each profile's env overlay to the probe subprocess only:

```bash
python3 /daaf/scripts/deploy_smoke/run_deploy_smoke.py --route openrouter \
    --profiles openrouter-claude,openrouter-gpt,openrouter-glm --yes
```

Profiles are defined in `scripts/deploy_smoke/profiles.yaml` (the three above are working examples — adapt the model slugs to models your OpenRouter account can reach). For non-Claude models a profile sets `ANTHROPIC_DEFAULT_OPUS_MODEL` / `ANTHROPIC_DEFAULT_SONNET_MODEL` (keeps subagents model-pure and makes `enforce-model-ceiling.sh` stand down) and `CLAUDE_CODE_MAX_CONTEXT_TOKENS` (declares the real window so context reporting is accurate).

**Shim routes are different.** On `openai-api` / `chatgpt-subscription` the shim *daemon* state (`SHIM_SANITIZE_TOOLS`, `backend_mode`) is fixed at daemon startup and cannot be changed per run — env overlays reach the CLI session, not the running shim. `--profiles` on a shim route emits a WARNING; verify daemon state read-only via Tier 0's shim `/health` probe instead.

### Reading the Output

Each run writes `scripts/deploy_smoke/reports/{YYYYMMDD_HHMMSS}_{route}/`:

- **`report.md`** — human audit: per-probe verdict with quoted evidence, grouped by tier, plus a redacted env fingerprint.
- **`report.json`** — machine-readable: git SHA, route, model family, redacted env fingerprint, per-probe results.
- **`evidence/`** — discrete audit-snapshot files: `shim_health.json` (shim routes only) and `env_fingerprint.json`. The `/tmp` coordination-cache reads a Tier 1 probe performs are embedded inline in that probe's `report.md`/`report.json` evidence — they are *not* written as separate files under `evidence/`.
- **`evidence/tier_d/`** — Tier D failure artifacts (present when Tier D runs): the COMPLETE scrubbed output of any FAILed or timed-out battery is persisted at `evidence/tier_d/{probe_id}.log`, and Pester's NUnit `testResults.xml` is written here (report-local) rather than at the repository root. On a PASS the report keeps only a concise final excerpt; the full log is persisted only on FAIL/timeout.

Verdicts are `PASS | FAIL | WARN | SKIP | INFO`. Only **FAIL** flips the overall result and the exit code (nonzero), matching the `run_all_smoke_tests.sh` contract. A route-appropriate SKIP (e.g. shim `/health` on a non-shim route) or a tolerant WARN never breaks the run.

**Interpreting individual probes — verdicts are not always self-explanatory.** Some WARN/INFO signals are expected mechanics of a headless probe, not install defects (notably the Tier 1 context-reporter and `/tmp`-cache probes on short runs), and each route has its own known failure modes with documented fixes. For probe-by-probe interpretation, route-conditional expectations, and failure-mode → fix routing, read `references/interpreting-results.md`.

### Route Auto-Detection (summary)

Detection reads the live environment (no LLM, no subprocess):

| Live env signal | Detected route |
|-----------------|----------------|
| `DAAF_PROVIDER_SHIM=openai` + `SHIM_BACKEND_MODE=chatgpt` | `chatgpt-subscription` (shim) |
| `DAAF_PROVIDER_SHIM=openai` (otherwise) | `openai-api` (shim) |
| `ANTHROPIC_BASE_URL` contains `openrouter.ai` | `openrouter` |
| none of the above | `anthropic-subscription` |

The shim gate is checked before the OpenRouter base-URL test because shim routes point `ANTHROPIC_BASE_URL` at the localhost shim, not at openrouter.ai. `--route` turns your *expectation* into an assertion so a silently mis-set env surfaces as a FAIL.

### Boundaries

- **Requires `DAAF_DEV=1`.** The deployment smoke suite is intentionally restricted to development images as a contributor tool; the Tier 0 policy gate applies even to `--tiers 0`. Tier D additionally relies on development-only deterministic/test tooling, although an unavailable Tier-D tool can produce a probe-level SKIP. Codex itself ships in every image. Shim routing and `codex login` are separate explicit opt-ins and do not require a development image. The suite remains intentionally absent from the end-user install guide.
- **Secrets never leak.** The env fingerprint redacts any var whose name contains `KEY`/`TOKEN`/`SECRET`/`AUTH`, but preserves the load-bearing empty-vs-unset distinction (e.g. OpenRouter needs `ANTHROPIC_API_KEY` present-and-empty).
- **Reads `/tmp` caches, never writes them.** Reading DAAF's coordination caches is the sanctioned pattern; the suite writes only inside the project.
- **Do not confuse tiers with cost tiers.** Tier 0 and Tier D are free; Tiers 1 and 2 make live API calls billed to your configured provider. The pre-launch summary quotes the call count before any live tier runs (skip it with `--yes`).

### Reference Files

| File | When to read |
|------|--------------|
| `references/interpreting-results.md` | Reading a report: probe-by-probe meaning, route-conditional expectations, headless-mode nuances, and known failure-mode → documented-fix routing per route |
