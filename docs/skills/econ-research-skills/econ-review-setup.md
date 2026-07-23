<!-- DO NOT EDIT — auto-copied from skills/econ-research-skills/details/econ-review-setup.md -->

# `/econ-review-setup`

Prepares, verifies, repairs, or removes the user-owned Python runtime and local Review Desk behind an installed econ-review plugin — dry-run shown first, no silent package downloads or system-software installs.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econ-research-skills/">Econ Research Skills (Hanlu Long)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>PolyForm-Noncommercial-1.0.0 (econ-review); MIT (econ-slides, econ-write)</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hanlulong/econ-paper-review-skill/contents/econ-review/skills/econ-review-setup/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econ-research-skills/econ-review-setup/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hanlulong/econ-paper-review-skill/blob/main/econ-review/skills/econ-review-setup/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hanlulong/econ-paper-review-skill?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Set up Econ Review

Resolve `PLUGIN_ROOT` as the parent directory of the `skills/` directory that
contains this setup skill. Use the standard-library setup tool at
`PLUGIN_ROOT/scripts/setup_econ_review.py`. Do not copy the skill into an agent
home: marketplace installation already supplies it.

1. Find a working Python 3.10 or newer command with `venv` and pip bootstrapping
   support already on the machine. Do not install Python, a package manager, a
   missing `python3-venv` component, or system software on your own.
2. Choose global support setup unless the user explicitly requests one-project
   state. For global setup, run this exact operation first with `--dry-run`:

   ```text
   PYTHON PLUGIN_ROOT/scripts/setup_econ_review.py --support-only --global --with-review-desk --dry-run
   ```

   For project state, replace `--global` with `--local PROJECT_DIRECTORY`.
3. Summarize the dry run in plain language. State that applying it creates or
   refreshes a private econ-review virtual environment, may download the
   version-constrained Python packages declared by the plugin, and installs the
   already bundled, manifest-verified Review Desk. It does not install a second
   skill copy, use administrator access, or upload a manuscript.
4. Apply the same command without `--dry-run` only when the user has explicitly
   asked to install, finish, repair, or refresh setup, or confirms after seeing
   the plan. Do not treat a request merely to review a paper as authorization
   to download packages or change user-level state.
5. Preserve the setup tool's exit distinction. Exit `0` means the core runtime,
   PDF ingestion, and requested Review Desk passed. Exit `2` means the managed
   runtime and Review Desk may be ready but PDF ingestion is still incomplete,
   normally because Poppler is absent. Do not call that a failed plugin install.
6. Never install Poppler, Tesseract, TeX, Pandoc, Node.js, an optional PDF
   backend, or any administrator-managed package automatically. If Poppler is
   missing, report the setup tool's platform-specific user-level options and
   ask separately before running a package-manager command.
7. Verify runtime discovery without changing files:

   ```text
   PYTHON PLUGIN_ROOT/scripts/setup_econ_review.py --runtime-path
   ```

   After project-only setup, pass the same project scope instead:

   ```text
   PYTHON PLUGIN_ROOT/scripts/setup_econ_review.py --runtime-path --local PROJECT_DIRECTORY
   ```

   This read-only resolver verifies and prints only the managed interpreter.
   Preserve the setup command's earlier PDF-doctor result and Review Desk launch
   command or URL when reporting overall readiness. Never expose package-index
   credentials or environment-secret values in the response.

8. When the user asks to uninstall support data, show
   `--cleanup-support --global --dry-run` (or the matching `--local` scope)
   first. Apply the same scope with `--confirm-cleanup` only after explicit
   confirmation. Explain that plugin removal alone retains the runtime,
   descriptor, and Review Desk, while cleanup leaves the plugin and any direct
   skill copy unchanged.
