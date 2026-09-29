<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/capture-environment.md -->

# `/capture-environment`

Snapshots the computational environment (R, Stata or Python) for a replication package and writes the matching lockfiles and version records.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/capture-environment/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/capture-environment/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/capture-environment/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## `/capture-environment` — snapshot the computational environment

A replication package that runs on the author's laptop in 2026 and nowhere else in 2029 is not reproducible. This skill captures the *exact* computational environment — language versions, package versions, seeds, RNG kind, and (optionally) the OS layer — so a referee, the AEA Data Editor, or future-you can reconstruct it. It detects which stack the project uses and emits the artifacts that stack's ecosystem expects, then verifies the lockfile installs clean.

**Core principle:** Pin everything a result depends on. Display rounding aside, a re-run on a pinned environment should reproduce the paper to the `replication-protocol.md` tolerances — *byte-identical* when the optional Dockerfile is used.

### When to use

- **Before releasing a replication package** to openICPSR, Zenodo, Dataverse, or a journal archive — the AEA Data Editor / DCAS standard expects a documented, version-pinned environment.
- **Before submission**, alongside `/audit-reproducibility` — that skill checks the *numbers*; this one captures the *environment* those numbers were produced in (its `sessionInfo.txt` requirement is satisfied by this skill).
- **After adding or upgrading a package** mid-project — re-snapshot so the lockfile doesn't drift from what the code actually loads.
- **When handing a project to a co-author or RA** who needs to reconstruct your stack.

### Inputs

- `$0` — project directory. Defaults to the repo root. The skill looks under `scripts/R/`, `scripts/stata/`, `scripts/python/`.
- `--docker` — also emit a `Dockerfile` pinning OS + language version + system libraries for byte-identical reproduction.
- `--no-verify` — skip Phase 3 (the best-effort clean-install check). Useful in CI or when the toolchain isn't installed locally.

### Workflow

#### Phase 0: Detect the stack

Glob for stack signals and decide which capture paths to run (a project may be multi-language — DiD in R, an IV robustness check in Stata):

| Signal | Stack | Capture path |
|---|---|---|
| `scripts/R/*.R`, `DESCRIPTION`, `renv/`, `*.Rproj` | **R** | renv + sessionInfo |
| `scripts/python/*.py`, `*.ipynb`, `pyproject.toml`, `requirements.txt`, `environment.yml`, `uv.lock` | **Python** | pip / conda / uv |
| `scripts/stata/*.do` | **Stata** | version + ado list |

If no signal is found, report and stop — there is no environment to capture.

#### Phase 1: Capture per language

**R** — emit two artifacts:
- `renv.lock` via `renv::snapshot()` (run `renv::init(bare = TRUE)` first if the project isn't renv-managed; snapshot records every package + version + source/remote and the R version). Honors the seed conventions in `r-code-conventions.md`.
- `sessionInfo.txt` via `Rscript -e "writeLines(capture.output(sessionInfo()), 'output/sessionInfo.txt')"` — the human-readable companion `/audit-reproducibility` looks for.

**Python** — emit whichever matches the project's existing tooling (do not invent a new one):
- `uv.lock` (preferred when `pyproject.toml` + `uv` present — fully-resolved, hashed, cross-platform): `uv lock` / `uv export --format requirements-txt > requirements.txt`.
- `requirements.txt` via `pip freeze` (or `python -m pip freeze`) for a venv/pip project — pin `==` exactly.
- `environment.yml` via `conda env export --no-builds` for a conda project.
Always also record the interpreter version (`python --version`) in the report.

**Stata** — Stata has no lockfile, so capture the closest equivalents (mirrors `stata-code-conventions.md` §3):
- The pinned `version` line each `.do` file declares (e.g. `version 18`) — grep `scripts/stata/*.do` and report the version actually pinned.
- An ado/plus package inventory: a small `.do` that runs `which` on the user-installed commands the pipeline uses (`reghdfe`, `ivreg2`, `estout`/`esttab`, `rdrobust`, `csdid`, …) plus `ado dir` and `about`, logged to `output/sessionInfo_stata.txt`.
- A note that Stata version pinning is *semantic* (`version 18` fixes command behavior), not a binary pin — the Dockerfile (Phase 2) cannot help here because Stata is licensed and not redistributable; record the exact Stata version + flavor (SE/MP/IC) + update level in the report so a replicator can match it.

#### Phase 1b: Record seeds and RNG

Grep the analysis scripts for the master seed and RNG kind so the "Computational requirements" block can state them:
- **R**: `set.seed(YYYYMMDD)`, and `RNGkind()` — flag `"L'Ecuyer-CMRG"` if parallel/Monte Carlo work is present (see `simulation-conventions.md`).
- **Stata**: `set seed` and `set sortseed`.
- **Python**: `numpy.random.default_rng(seed)` / `random.seed()` / framework seeds.

If the pipeline does randomized work (bootstrap, MC, RCT re-randomization, permutation inference) and **no** seed is found, surface it as a WARNING — an unseeded random result is not reproducible.

#### Phase 2: Dockerfile (only with `--docker`)

Emit a `Dockerfile` that pins the OS + language version + system libraries for byte-identical reproduction:
- **R** → `FROM rocker/r-ver:<X.Y.Z>` (Rocker pins the R version), `COPY renv.lock`, `RUN R -e "renv::restore()"`, plus `apt-get install` for system libs the packages need (e.g. `libcurl4-openssl-dev`, `libgdal-dev` for spatial work).
- **Python** → `FROM python:<X.Y.Z>-slim`, `COPY requirements.txt` / `uv.lock`, `RUN pip install -r requirements.txt` (or `uv sync --frozen`).
- **Stata** → cannot pin the licensed binary; emit a `Dockerfile` stub that documents the expected Stata version + flavor and leaves the `stata` install/license step to the replicator (with a comment pointing at the AEA's guidance on Stata images).

Pin a digest where possible (`FROM image@sha256:…`) so the base image can't drift.

#### Phase 3: Verify the lockfile installs clean (best-effort; skip with `--no-verify`)

Attempt a clean restore in a throwaway location and report PASS / FAIL — never overwrite the working environment:
- **R**: `renv::restore()` into a temp library, or `Rscript -e "renv::status()"` for a dry check.
- **Python**: `uv sync --frozen` / `pip install --dry-run -r requirements.txt` into a fresh venv.
- **Docker** (if `--docker`): `docker build` the image.

A FAIL here means the lockfile references a package version that can't be resolved (yanked release, private remote, platform-specific wheel). Report it; do not auto-edit the lockfile.

#### Phase 4: Report

Print a paste-ready block and write it to `output/computational_requirements.md`:

```markdown
### Computational requirements

**Software:** R 4.4.1 (or: Stata 18.0 SE, update 2026-01-15; Python 3.12.3)
**OS used:** macOS 15.5 (arm64) — Dockerfile pins Ubuntu 24.04 for portability
**Key packages:** fixest 0.12.1, did 2.1.2 (full list in renv.lock)
**Random seeds:** set.seed(20260609); RNGkind("L'Ecuyer-CMRG") for the bootstrap
**Approx. runtime:** [author confirms — e.g. ~12 min, 8 cores]
**Lockfiles in package:** renv.lock, output/sessionInfo.txt[, Dockerfile]
```

Pre-fill software/package/seed lines from the captured artifacts; leave runtime for the author to confirm.

### Output / artifacts

| Stack | Files written |
|---|---|
| R | `renv.lock`, `output/sessionInfo.txt` |
| Python | `requirements.txt` *or* `environment.yml` *or* `uv.lock` (matching project tooling) |
| Stata | `output/sessionInfo_stata.txt` (version + ado list; named so it does not overwrite R's in a mixed project) |
| Any (`--docker`) | `Dockerfile` |
| Always | `output/computational_requirements.md` (the paste-ready block) |

### Exit behavior

- **All captures succeeded, verify PASS (or `--no-verify`):** exit 0, requirements block printed.
- **A missing-seed WARNING on a randomized pipeline:** exit 0 with the warning surfaced — reproducibility is compromised but the snapshot still wrote.
- **Verify FAIL (lockfile won't resolve):** exit 1, so the skill can gate a pre-release `/commit`. Report the unresolvable package; do not silently "fix" the lockfile.
- **No stack detected in Phase 0:** exit 1 with the directories searched.

### Cross-references

- `.claude/rules/replication-protocol.md` — the tolerance contract a pinned environment is meant to reproduce.
- `.claude/rules/r-code-conventions.md` — R seeding + output-path conventions this skill reads.
- `.claude/rules/stata-code-conventions.md` — §3 `sessionInfo_stata.txt` + `version`-pinning the Stata path mirrors.
- `.claude/rules/simulation-conventions.md` — L'Ecuyer streams for reproducible parallel/MC work.
- `.claude/rules/confidential-data.md` — when raw data is restricted, the *environment* still ships even though the data does not; coordinate the README's "data availability" section with this block.
- `/audit-reproducibility` — consumes the `sessionInfo.txt` this skill produces; run it after.
- `/data-analysis`, `/stata-replication`, `/simulation-study` — the pipelines whose environment this snapshots.
- [AEA Data Editor checklist](https://aeadataeditor.github.io/) / [openICPSR](https://www.openicpsr.org/) / DCAS — the external standards this skill targets.

### What this skill does NOT do

- **Re-run your analysis or check your numbers.** It captures the environment; `/audit-reproducibility` verifies the manuscript's numeric claims against the outputs.
- **Package or de-identify data.** Lockfiles describe software, not data. Disclosure avoidance, de-identification, and data-availability statements are out of scope — see `confidential-data.md`.
- **Upgrade or "fix" your dependencies.** It records what the code currently uses. If a verify FAIL surfaces a yanked version, you decide whether to pin an alternative.
- **Pin a Stata binary.** Stata is licensed and not redistributable; the skill records the exact version/flavor/update so a replicator can match it, but cannot containerize it.
