# Skills catalog

Curated collections of Markdown-defined research skills (SKILL.md files, plugin commands, MCP servers) shipped by the projects in the [catalog](../projects/index.md).

The pages below are **auto-generated** from `skills/*.yml`. Do not edit by hand — edit the YAML sources.

<!-- AUTO-GENERATED:skills-start -->
*9 skill packs · 160 skills indexed.*

## Pack overview

| Pack | License | Skills | Project | Runtimes |
|---|---|---|---|---|
| [Academic Research Skills (ARS)](academic-research-skills.md) | `CC BY-NC 4.0` | 17 | [academic-research-skills](../projects/academic-research-skills.md) | `claude-code` `codex` `vscode` `jetbrains` |
| [Anthropic Skills (foundational)](anthropic-skills.md) | `MIT` | 8 | — | `claude-code` `agnostic` |
| [ARIS skills](aris.md) | `MIT` | 80 | [aris](../projects/aris.md) | `claude-code` `codex` `cursor` `trae` |
| [AutoResearchClaw skills](autoresearchclaw.md) | `MIT` | 9 | [autoresearchclaw](../projects/autoresearchclaw.md) | `claude-code` `codex` `copilot-cli` `gemini-cli` |
| [Clo-Author skills](clo-author.md) | `none declared` | 14 | [clo-author](../projects/clo-author.md) | `claude-code` |
| [Claude Code for Causal Inference (Scott Cunningham)](cunningham-substack.md) | `all rights reserved (substack essays)` | 7 | — | `claude-code` `agnostic` |
| [EvoSkills](evoskills.md) | `Apache-2.0` | 14 | [evoscientist](../projects/evoscientist.md) | `claude-code` `codex` `agnostic` |
| [Claude Code for Applied Economists (Markus Academy / Eberhardt)](markus-academy.md) | `all rights reserved (substack essays)` | 6 | — | `claude-code` `agnostic` |
| [MCP Marketplace (research-relevant subset)](mcp-marketplace.md) | `varies per skill` | 5 | — | `claude-code` `mcp` |

## All skills (filterable)

<input type="text" id="skillFilter" placeholder="🔍 filter by skill name / pack / field / category / pipeline stage…"
  style="width:100%; padding:0.5em; margin:1em 0; font-size:1em; border:1px solid #ccc; border-radius:4px;"
  oninput="filterSkills(this.value)">

<script>
function filterSkills(q) {
  q = q.toLowerCase().trim();
  document.querySelectorAll('#skillsTable tbody tr').forEach(function(row) {
    row.style.display = (!q || row.textContent.toLowerCase().includes(q)) ? '' : 'none';
  });
}
</script>

<table id="skillsTable">
<thead><tr><th>Skill</th><th>Pack</th><th>Field</th><th>Category</th><th>Stages</th><th>Description</th><th>Source</th><th>Updated</th></tr></thead>
<tbody>
<tr><td><code>Development-econometrics workflows with Claude</code></td><td><a href="markus-academy.md">Claude Code for Applied Economists (Markus Academy / Eberhardt)</a></td><td>economics</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>Pattern for cross-country / sub-national development-econometrics work (technology adoption, growth empirics).</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists">link</a></td><td>2025</td></tr>
<tr><td><code>Difference-in-Differences with Claude</code></td><td><a href="cunningham-substack.md">Claude Code for Causal Inference (Scott Cunningham)</a></td><td>econometrics</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>Pattern for running DID workflows (parallel-trends checks, event-study plots, Callaway-Sant'Anna) with Claude Code as the coder.</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td>2025</td></tr>
<tr><td><code>Instrumental Variables with Claude</code></td><td><a href="cunningham-substack.md">Claude Code for Causal Inference (Scott Cunningham)</a></td><td>econometrics</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>Pattern for IV estimation, weak-instrument checks (Anderson-Rubin, AR-LM), local-IV interpretation.</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td>2025</td></tr>
<tr><td><code>Panel-data analysis with Claude</code></td><td><a href="markus-academy.md">Claude Code for Applied Economists (Markus Academy / Eberhardt)</a></td><td>econometrics</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>Pattern for FE/RE panel estimation, cluster-robust SEs, dynamic panel (Arellano-Bond) workflows.</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists">link</a></td><td>2025</td></tr>
<tr><td><code>Regression Discontinuity with Claude</code></td><td><a href="cunningham-substack.md">Claude Code for Causal Inference (Scott Cunningham)</a></td><td>econometrics</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>Pattern for RD designs: bandwidth selection, McCrary tests, robust SEs, donut RD.</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td>2025</td></tr>
<tr><td><code>Synthetic Control with Claude</code></td><td><a href="cunningham-substack.md">Claude Code for Causal Inference (Scott Cunningham)</a></td><td>econometrics</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>Pattern for synthetic-control estimation, placebo tests, and inference.</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td>2025</td></tr>
<tr><td><code>analyze</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>analyze-results</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>statistical-reporting</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>analysis</code></td><td><code>data-analysis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-anti-leakage</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>Anti-leakage protocol for sensitive data</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-claim-audit</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>v3.8 claim-faithfulness audit pass with 5 HIGH-WARN classes</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-cross-model</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>Cross-model verification harness (ARS_CROSS_MODEL)</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-quality-check</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>Writing-quality check catches machine-generated patterns</td><td>—</td><td>—</td></tr>
<tr><td><code>citation-audit</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>claims-drafting</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>experiment-audit</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>novelty-check</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-claim-audit</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>patent-novelty-check</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>result-to-claim</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>audit</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>experiment-bridge</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>code-gen</code></td><td><code>code-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>experiment-craft</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>code-gen</code></td><td><code>code-generation</code></td><td>Experiment design and code crafting</td><td>—</td><td>—</td></tr>
<tr><td><code>experiment-iterative-coder</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>code-gen</code></td><td><code>code-generation</code></td><td>Iterative coding loop for experimentation</td><td>—</td><td>—</td></tr>
<tr><td><code>experiment-pipeline</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>code-gen</code></td><td><code>code-generation</code></td><td>End-to-end experiment pipeline orchestration</td><td>—</td><td>—</td></tr>
<tr><td><code>experiment-queue</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>code-gen</code></td><td><code>code-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>skills-codex</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>code-gen</code></td><td><code>code-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>Macro data pipelines (FRED / World Bank)</code></td><td><a href="markus-academy.md">Claude Code for Applied Economists (Markus Academy / Eberhardt)</a></td><td>economics</td><td><code>data-handling</code></td><td><code>data-acquisition</code> <code>data-analysis</code></td><td>Pattern for assembling macro panels from FRED / World Bank / Penn World Table sources.</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists">link</a></td><td>2025</td></tr>
<tr><td><code>xlsx</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>data-handling</code></td><td><code>data-acquisition</code></td><td>Excel spreadsheet generation</td><td>—</td><td>—</td></tr>
<tr><td><code>Claude Code for Applied Economists (overview)</code></td><td><a href="markus-academy.md">Claude Code for Applied Economists (Markus Academy / Eberhardt)</a></td><td>economics</td><td><code>design</code></td><td><code>research-design</code></td><td>Series-opening essay laying out the case for Claude Code as an applied-economics research tool.</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists">link</a></td><td>2025</td></tr>
<tr><td><code>Claude Code for Causal Inference (overview)</code></td><td><a href="cunningham-substack.md">Claude Code for Causal Inference (Scott Cunningham)</a></td><td>econometrics</td><td><code>design</code></td><td><code>research-design</code> <code>data-analysis</code></td><td>Series-opening essay introducing the use of Claude Code for causal-identification workflows in applied economics.</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td>2025</td></tr>
<tr><td><code>ablation-planner</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>design</code></td><td><code>research-design</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>experiment-plan</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>design</code></td><td><code>research-design</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-plan</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>design</code></td><td><code>research-design</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-planning</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>design</code></td><td><code>research-design</code></td><td>Paper structure + research plan</td><td>—</td><td>—</td></tr>
<tr><td><code>Academic Research Writer</code></td><td><a href="mcp-marketplace.md">MCP Marketplace (research-relevant subset)</a></td><td>humanities</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>Humanities-focused academic writing with archive search, verbatim-quote retrieval with verified page numbers, and strict citation enforcement.</td><td><a href="https://mcpmarket.com/tools/skills/academic-research-writer">link</a></td><td>2025</td></tr>
<tr><td><code>LaTeX tables from Stata/R output</code></td><td><a href="markus-academy.md">Claude Code for Applied Economists (Markus Academy / Eberhardt)</a></td><td>economics</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>Pattern for converting Stata/R regression output into journal-formatted LaTeX tables.</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists">link</a></td><td>2025</td></tr>
<tr><td><code>a-evolve</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-latex-harden</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>LaTeX hardening for journal compliance</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-plan</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>Socratic dialogue to map paper chapter structure</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-write</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>Draft paper sections</td><td>—</td><td>—</td></tr>
<tr><td><code>biology-biopython</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>careful</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>checkpoint</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>chemistry-rdkit</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>dashboard</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>doc-coauthoring</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>Long-document coauthoring workflow</td><td>—</td><td>—</td></tr>
<tr><td><code>docx</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>Microsoft Word document generation</td><td>—</td><td>—</td></tr>
<tr><td><code>dse-loop</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>embodiment-description</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>freeze</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>grant-proposal</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>interview-cheatsheet</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>invention-structuring</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>jurisdiction-format</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>kill-argument</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>monitor-experiment</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>new-project</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-compile</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-illustration</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-illustration-image2</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-poster</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-write</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-writing</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-writing</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>Paper drafting pipeline</td><td>—</td><td>—</td></tr>
<tr><td><code>patent-pipeline</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>pdf</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>PDF document generation</td><td>—</td><td>—</td></tr>
<tr><td><code>pixel-art</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>qzcli</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>render-html</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>revise</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>run-experiment</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>scientific-writing</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>serverless-modal</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>shared-references</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>specification-writing</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>strategize</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>system-profile</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>tools</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>training-check</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>vast-gpu</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>write</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>writing-systems-papers</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>drafting</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-citation-convert</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>editing</code></td><td><code>revision-editing</code></td><td>Citation format conversion across styles</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-style-calibration</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>editing</code></td><td><code>revision-editing</code></td><td>Learns user's writing voice from past work</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-vlm-figure</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>figures</code></td><td><code>paper-drafting</code></td><td>VLM figure verification</td><td>—</td><td>—</td></tr>
<tr><td><code>figure-description</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>figures</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>figure-spec</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>figures</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>mermaid-diagram</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>figures</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>nano-banana</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>figures</code></td><td><code>paper-drafting</code></td><td>AI-generated inline figures (Google Gemini Nano Banana)</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-figure</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>figures</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>scientific-visualization</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>figures</code></td><td><code>paper-drafting</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>discover</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>ideation</code></td><td><code>rq-formulation</code> <code>hypothesis-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>hypothesis-formulation</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>ideation</code></td><td><code>rq-formulation</code> <code>hypothesis-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>idea-creator</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>ideation</code></td><td><code>rq-formulation</code> <code>hypothesis-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>idea-discovery</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>ideation</code></td><td><code>rq-formulation</code> <code>hypothesis-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>idea-discovery-robot</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>ideation</code></td><td><code>rq-formulation</code> <code>hypothesis-generation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>research-ideation</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>ideation</code></td><td><code>rq-formulation</code> <code>hypothesis-generation</code></td><td>Research idea generation</td><td>—</td><td>—</td></tr>
<tr><td><code>claude-api</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>infra</code></td><td></td><td>Build apps with the Claude API + Anthropic SDK</td><td>—</td><td>—</td></tr>
<tr><td><code>evo-memory</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>infra</code></td><td></td><td>Persistent memory layer for EvoScientist sessions</td><td>—</td><td>—</td></tr>
<tr><td><code>feishu-notify</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>infra</code></td><td></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>Academic Paper Search</code></td><td><a href="mcp-marketplace.md">MCP Marketplace (research-relevant subset)</a></td><td>general</td><td><code>literature</code></td><td><code>literature-discovery</code></td><td>Search across major scholarly databases (Scopus, Semantic Scholar) for preprints, peer-reviewed journals, and conference proceedings.</td><td><a href="https://mcpmarket.com/tools/skills/academic-paper-search">link</a></td><td>2025</td></tr>
<tr><td><code>Academic Research Assistant</code></td><td><a href="mcp-marketplace.md">MCP Marketplace (research-relevant subset)</a></td><td>general</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>Search and synthesize millions of scholarly articles via combined database access.</td><td><a href="https://mcpmarket.com/tools/skills/academic-research-assistant">link</a></td><td>2025</td></tr>
<tr><td><code>Academic Research Assistant (variant)</code></td><td><a href="mcp-marketplace.md">MCP Marketplace (research-relevant subset)</a></td><td>general</td><td><code>literature</code></td><td><code>literature-discovery</code></td><td>Alternative implementation of an academic-research assistant skill on the MCP marketplace.</td><td><a href="https://mcpmarket.com/tools/skills/academic-research-assistant-1">link</a></td><td>2025</td></tr>
<tr><td><code>Academic Research Citation Search</code></td><td><a href="mcp-marketplace.md">MCP Marketplace (research-relevant subset)</a></td><td>general</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>AI-powered literature search across arXiv, PubMed, Semantic Scholar, and Google Scholar with citation extraction.</td><td><a href="https://mcpmarket.com/tools/skills/academic-research-citation-search">link</a></td><td>2025</td></tr>
<tr><td><code>alphaxiv</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-lit-review</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>13-agent literature-review team with Socratic guided mode</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-prisma</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>PRISMA systematic-review workflow</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-semantic-scholar</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>Semantic Scholar API verification</td><td>—</td><td>—</td></tr>
<tr><td><code>arxiv</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>deepxiv</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>exa-search</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>gemini-search</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>literature-search</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>openalex</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-navigator</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>Navigate literature with persistent memory</td><td>—</td><td>—</td></tr>
<tr><td><code>prior-art-search</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>research-lit</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>research-pipeline</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>research-refine</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>research-refine-pipeline</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>research-survey</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>Survey/literature review generation</td><td>—</td><td>—</td></tr>
<tr><td><code>research-wiki</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>researchclaw</code></td><td><a href="autoresearchclaw.md">AutoResearchClaw skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>semantic-scholar</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>literature</code></td><td><code>literature-discovery</code> <code>literature-synthesis</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>Teaching Causal Inference with Claude</code></td><td><a href="cunningham-substack.md">Claude Code for Causal Inference (Scott Cunningham)</a></td><td>econometrics</td><td><code>meta</code></td><td></td><td>Pattern for using Claude Code to scaffold teaching materials, exercises, and lecture notes for causal-inference courses.</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td>2025</td></tr>
<tr><td><code>auto-paper-improvement-loop</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>meta</code></td><td></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>mcp-builder</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>meta</code></td><td></td><td>Build MCP servers (Anthropic spec)</td><td>—</td><td>—</td></tr>
<tr><td><code>meta-optimize</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>meta</code></td><td></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>skill-creator</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>meta</code></td><td></td><td>Meta-skill for building new skills from scratch</td><td>—</td><td>—</td></tr>
<tr><td><code>evomath-tao</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>modeling</code></td><td><code>formal-modeling</code></td><td>Mathematical derivation skill in the spirit of Tao-style proof reasoning</td><td>—</td><td>—</td></tr>
<tr><td><code>formula-derivation</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>modeling</code></td><td><code>formal-modeling</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>proof-checker</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>modeling</code></td><td><code>formal-modeling</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>proof-writer</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>modeling</code></td><td><code>formal-modeling</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>Replication Package for Causal Papers</code></td><td><a href="cunningham-substack.md">Claude Code for Causal Inference (Scott Cunningham)</a></td><td>econometrics</td><td><code>replication</code></td><td><code>replication</code></td><td>Pattern for assembling a reproducible replication package after a causal-inference paper draft.</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td>2025</td></tr>
<tr><td><code>ars-review</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>Multi-perspective peer review (EIC + 3 dynamic reviewers + Devil's Advocate)</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-review-rubric</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>0-100 quality rubrics</td><td>—</td><td>—</td></tr>
<tr><td><code>auto-review-loop</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>auto-review-loop-llm</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>auto-review-loop-minimax</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>comm-lit-review</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-review</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>Multi-perspective peer review</td><td>—</td><td>—</td></tr>
<tr><td><code>patent-review</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>research-review</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>review</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>skills-codex-claude-review</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>skills-codex-gemini-review</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>review</code></td><td><code>referee-simulation</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>Referee-response drafting for econ journals</code></td><td><a href="markus-academy.md">Claude Code for Applied Economists (Markus Academy / Eberhardt)</a></td><td>economics</td><td><code>revision</code></td><td><code>revision-editing</code></td><td>Pattern for structuring R&R responses (point-by-point reply, what-changed-in-paper, robustness additions).</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists">link</a></td><td>2025</td></tr>
<tr><td><code>ars-review-rr</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>revision</code></td><td><code>revision-editing</code></td><td>R&R traceability matrix</td><td>—</td><td>—</td></tr>
<tr><td><code>ars-revision-coach</code></td><td><a href="academic-research-skills.md">Academic Research Skills (ARS)</a></td><td>—</td><td><code>revision</code></td><td><code>revision-editing</code></td><td>Revision coaching with reviewer-comment routing</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-rebuttal</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>revision</code></td><td><code>revision-editing</code></td><td>Rebuttal pipeline for reviewer comments</td><td>—</td><td>—</td></tr>
<tr><td><code>rebuttal</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>revision</code></td><td><code>revision-editing</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>academic-slides</code></td><td><a href="evoskills.md">EvoSkills</a></td><td>—</td><td><code>slides</code></td><td><code>dissemination</code></td><td>Academic slide deck generation</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-slides</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>slides</code></td><td><code>dissemination</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>paper-talk</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>slides</code></td><td><code>dissemination</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>pptx</code></td><td><a href="anthropic-skills.md">Anthropic Skills (foundational)</a></td><td>—</td><td><code>slides</code></td><td><code>dissemination</code></td><td>PowerPoint deck generation</td><td>—</td><td>—</td></tr>
<tr><td><code>slides-polish</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>slides</code></td><td><code>dissemination</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>talk</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>slides</code></td><td><code>dissemination</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>overleaf-sync</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>submission</code></td><td><code>dissemination</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>resubmit-pipeline</code></td><td><a href="aris.md">ARIS skills</a></td><td>—</td><td><code>submission</code></td><td><code>dissemination</code></td><td>—</td><td>—</td><td>—</td></tr>
<tr><td><code>submit</code></td><td><a href="clo-author.md">Clo-Author skills</a></td><td>—</td><td><code>submission</code></td><td><code>dissemination</code></td><td>—</td><td>—</td><td>—</td></tr>
</tbody></table>

## Skill count by category (across packs)

| Category | Count |
|---|---:|
| `drafting` | 48 |
| `literature` | 24 |
| `review` | 12 |
| `audit` | 11 |
| `analysis` | 9 |
| `figures` | 7 |
| `code-gen` | 6 |
| `design` | 6 |
| `ideation` | 6 |
| `slides` | 6 |
| `meta` | 5 |
| `revision` | 5 |
| `modeling` | 4 |
| `infra` | 3 |
| `submission` | 3 |
| `data-handling` | 2 |
| `editing` | 2 |
| `replication` | 1 |

<!-- AUTO-GENERATED:skills-end -->
