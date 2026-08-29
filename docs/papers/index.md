# Papers catalog

> Regenerated from `papers/references.bib` (the **single source of truth** for
> citations) plus `docs/papers/notes/*.md` (curator analysis + status) by
> `scripts/build_indexes.py`. Do not edit by hand.

Each entry's *citation data* (title, authors, year, venue, DOI/arXiv) comes
from [`papers/references.bib`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib);
*themes and analysis* come from per-paper structured notes in
[`docs/papers/notes/`](https://github.com/bhanneke/RISE/tree/main/docs/papers/notes).

<!-- AUTO-GENERATED:papers-table-start -->
*101 bibliographic entries; 96 have curator notes (48 fully read). Filter via the column headers or the search box.*

<div style="margin:1em 0; display:flex; gap:0.5em; align-items:center;">
  <input type="text" id="paperFilter" placeholder="🔍 search author / title / venue / theme / citekey…"
    style="flex:1; padding:0.5em; font-size:1em; border:1px solid #ccc; border-radius:4px;"
    oninput="applyPaperFilters()">
  <button type="button" onclick="resetPaperFilters()"
    style="padding:0.5em 1em; border:1px solid #ccc; border-radius:4px; background:#f5f5f5; cursor:pointer;">
    Reset
  </button>
  <span id="paperCount" style="white-space:nowrap; color:#666; font-size:0.9em;"></span>
</div>

<script>
function applyPaperFilters() {
  var q = (document.getElementById('paperFilter').value || '').toLowerCase().trim();
  var sels = document.querySelectorAll('#papersTable select[data-filter-col]');
  var facets = {};
  sels.forEach(function(s){ if (s.value) facets[s.dataset.filterCol] = s.value; });
  var rows = document.querySelectorAll('#papersTable tbody tr');
  var shown = 0;
  rows.forEach(function(row){
    var ok = true;
    Object.keys(facets).forEach(function(col){
      var cell = row.getAttribute('data-' + col) || '';
      if (col === 'themes') {
        if (cell.split('|').indexOf(facets[col]) === -1) ok = false;
      } else if (cell !== facets[col]) {
        ok = false;
      }
    });
    if (ok && q) {
      if (row.textContent.toLowerCase().indexOf(q) === -1) ok = false;
    }
    row.style.display = ok ? '' : 'none';
    if (ok) shown++;
  });
  var c = document.getElementById('paperCount');
  if (c) c.textContent = shown + ' / ' + rows.length + ' papers';
}
function resetPaperFilters() {
  document.getElementById('paperFilter').value = '';
  document.querySelectorAll('#papersTable select[data-filter-col]').forEach(function(s){ s.value = ''; });
  applyPaperFilters();
}
document.addEventListener('DOMContentLoaded', applyPaperFilters);
</script>

<table id="papersTable" markdown>
<thead>
<tr><th>Year</th><th>Authors</th><th>Title</th><th>Venue</th><th>Link</th><th>Themes</th><th>Citekey</th><th>Note</th></tr>
<tr><th><select data-filter-col="year" onchange="applyPaperFilters()" style="width:100%; padding:0.2em; font-size:0.85em; border:1px solid #ccc; border-radius:3px; background:white; font-weight:normal;"><option value="">— any —</option><option value="2026">2026</option>
<option value="2025">2025</option>
<option value="2024">2024</option>
<option value="2023">2023</option>
<option value="2020">2020</option>
<option value="2019">2019</option>
<option value="2012">2012</option></select></th><th></th><th></th><th><select data-filter-col="venue" onchange="applyPaperFilters()" style="width:100%; padding:0.2em; font-size:0.85em; border:1px solid #ccc; border-radius:3px; background:white; font-weight:normal;"><option value="">— any —</option><option value="ACM Computing Surveys">ACM Computing Surveys</option>
<option value="Advances in Neural Information Processing Systems">Advances in Neural Information Processing Systems</option>
<option value="Advances in Neural Information Processing Systems 37 (NeurIPS 2024)">Advances in Neural Information Processing Systems 37 (NeurIPS 2024)</option>
<option value="Causal Inference Substack">Causal Inference Substack</option>
<option value="European Journal of Information Systems">European Journal of Information Systems</option>
<option value="German Conference on Artificial Intelligence (K\"unstliche Intelligenz)">German Conference on Artificial Intelligence (K\"unstliche Intelligenz)</option>
<option value="INFORMS Information Systems Research, Call for Papers">INFORMS Information Systems Research, Call for Papers</option>
<option value="Information Systems Research">Information Systems Research</option>
<option value="Information \& Management">Information \& Management</option>
<option value="International Conference on Learning Representations (ICLR)">International Conference on Learning Representations (ICLR)</option>
<option value="International Journal of Information Management">International Journal of Information Management</option>
<option value="Journal of Economic Literature">Journal of Economic Literature</option>
<option value="Journal of the Association for Information Systems">Journal of the Association for Information Systems</option>
<option value="MIS Quarterly">MIS Quarterly</option>
<option value="Management Science">Management Science</option>
<option value="Markus Academy Substack">Markus Academy Substack</option>
<option value="NEJM AI">NEJM AI</option>
<option value="National Bureau of Economic Research">National Bureau of Economic Research</option>
<option value="Nature">Nature</option>
<option value="Nature Biotechnology">Nature Biotechnology</option>
<option value="Nature Editorial, d41586-025-01880-9">Nature Editorial, d41586-025-01880-9</option>
<option value="Organization Science">Organization Science</option>
<option value="Proceedings of EMNLP 2024">Proceedings of EMNLP 2024</option>
<option value="Proceedings of NAACL 2024">Proceedings of NAACL 2024</option>
<option value="Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology">Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology</option>
<option value="Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)">Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)</option>
<option value="Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics">Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics</option>
<option value="Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)">Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</option>
<option value="Proceedings of the International Conference on Information Systems (ICIS)">Proceedings of the International Conference on Information Systems (ICIS)</option>
<option value="Proceedings of the National Academy of Sciences">Proceedings of the National Academy of Sciences</option>
<option value="Quarterly Journal of Economics">Quarterly Journal of Economics</option>
<option value="SSRN Working Paper">SSRN Working Paper</option>
<option value="Science">Science</option>
<option value="arXiv">arXiv</option></select></th><th></th><th><select data-filter-col="themes" onchange="applyPaperFilters()" style="width:100%; padding:0.2em; font-size:0.85em; border:1px solid #ccc; border-radius:3px; background:white; font-weight:normal;"><option value="">— any —</option><option value="agentic-pipelines">agentic-pipelines</option>
<option value="agentic-reasoning">agentic-reasoning</option>
<option value="agentic-tool-use">agentic-tool-use</option>
<option value="ai-peer-review">ai-peer-review</option>
<option value="ai-publishing-ecosystems">ai-publishing-ecosystems</option>
<option value="autonomous-research-agents">autonomous-research-agents</option>
<option value="end-to-end-research">end-to-end-research</option>
<option value="evaluation-of-ai-research">evaluation-of-ai-research</option>
<option value="evaluation-rigor">evaluation-rigor</option>
<option value="hallucination">hallucination</option>
<option value="harness-engineering">harness-engineering</option>
<option value="human-ai-research-collaboration">human-ai-research-collaboration</option>
<option value="is-methodology">is-methodology</option>
<option value="llm-cognition">llm-cognition</option>
<option value="memory-systems">memory-systems</option>
<option value="multi-agent-systems">multi-agent-systems</option>
<option value="peer-review">peer-review</option>
<option value="reasoning-faithfulness">reasoning-faithfulness</option>
<option value="replication-infrastructure">replication-infrastructure</option>
<option value="research-ethics">research-ethics</option>
<option value="research-productivity">research-productivity</option>
<option value="self-improvement">self-improvement</option>
<option value="sociotechnical">sociotechnical</option>
<option value="style-engines">style-engines</option>
<option value="traceability-verifiability">traceability-verifiability</option></select></th><th></th><th><select data-filter-col="status" onchange="applyPaperFilters()" style="width:100%; padding:0.2em; font-size:0.85em; border:1px solid #ccc; border-radius:3px; background:white; font-weight:normal;"><option value="">— any —</option><option value="read">read</option>
<option value="skimmed">skimmed</option>
<option value="—">—</option></select></th></tr>
</thead>
<tbody markdown>
<tr data-year="2012" data-venue="Information Systems Research" data-themes="research-productivity|is-methodology|sociotechnical" data-status="read"><td>2012</td><td>Aral et al.</td><td><a href="notes/aral2012itproductivity/">Information, Technology, and Information Worker Productivity</a></td><td>Information Systems Research</td><td><a href="https://doi.org/10.1287/isre.1110.0408" target="_blank" rel="noopener">doi</a></td><td><code>research-productivity</code> <code>is-methodology</code> <code>sociotechnical</code></td><td><code>aral2012itproductivity</code></td><td>read</td></tr>
<tr data-year="2019" data-venue="MIS Quarterly" data-themes="sociotechnical|is-methodology" data-status="read"><td>2019</td><td>Sarker & others</td><td><a href="notes/sarker2019sociotechnical/">The Sociotechnical Axis of Cohesion for the IS Discipline: Its Historical Legacy and Its Continued Relevance</a></td><td>MIS Quarterly</td><td><a href="https://doi.org/10.25300/misq/2019/13747" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code> <code>is-methodology</code></td><td><code>sarker2019sociotechnical</code></td><td>read</td></tr>
<tr data-year="2020" data-venue="Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics" data-themes="hallucination|reasoning-faithfulness|evaluation-of-ai-research" data-status="read"><td>2020</td><td>Maynez & others</td><td><a href="notes/maynez2020faithfulness/">On Faithfulness and Factuality in Abstractive Summarization</a></td><td>Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics</td><td><a href="https://doi.org/10.18653/v1/2020.acl-main.173" target="_blank" rel="noopener">doi</a></td><td><code>hallucination</code> <code>reasoning-faithfulness</code> <code>evaluation-of-ai-research</code></td><td><code>maynez2020faithfulness</code></td><td>read</td></tr>
<tr data-year="2023" data-venue="ACM Computing Surveys" data-themes="hallucination|evaluation-of-ai-research" data-status="read"><td>2023</td><td>Ji & others</td><td><a href="notes/ji2023hallucination/">Survey of Hallucination in Natural Language Generation</a></td><td>ACM Computing Surveys</td><td><a href="https://doi.org/10.1145/3571730" target="_blank" rel="noopener">doi</a></td><td><code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>ji2023hallucination</code></td><td>read</td></tr>
<tr data-year="2023" data-venue="arXiv" data-themes="hallucination|agentic-tool-use|evaluation-of-ai-research" data-status="skimmed"><td>2023</td><td>Lála et al.</td><td><a href="notes/lala2023paperqa/">PaperQA: Retrieval-Augmented Generative Agent for Scientific Research</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2312.07559" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>hallucination</code> <code>agentic-tool-use</code> <code>evaluation-of-ai-research</code></td><td><code>lala2023paperqa</code></td><td>skimmed</td></tr>
<tr data-year="2023" data-venue="Proceedings of the National Academy of Sciences" data-themes="llm-cognition|sociotechnical" data-status="read"><td>2023</td><td>Mitchell & Krakauer</td><td><a href="notes/mitchell2023understanding/">The Debate over Understanding in AI's Large Language Models</a></td><td>Proceedings of the National Academy of Sciences</td><td><a href="https://doi.org/10.1073/pnas.2215907120" target="_blank" rel="noopener">doi</a></td><td><code>llm-cognition</code> <code>sociotechnical</code></td><td><code>mitchell2023understanding</code></td><td>read</td></tr>
<tr data-year="2023" data-venue="Science" data-themes="research-productivity|human-ai-research-collaboration" data-status="read"><td>2023</td><td>Noy & Zhang</td><td><a href="notes/noy2023experimental/">Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence</a></td><td>Science</td><td><a href="https://doi.org/10.1126/science.adh2586" target="_blank" rel="noopener">doi</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code></td><td><code>noy2023experimental</code></td><td>read</td></tr>
<tr data-year="2023" data-venue="Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology" data-themes="autonomous-research-agents|sociotechnical|llm-cognition" data-status="read"><td>2023</td><td>Park & others</td><td><a href="notes/park2023generative/">Generative Agents: Interactive Simulacra of Human Behavior</a></td><td>Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology</td><td><a href="https://doi.org/10.1145/3586183.3606763" target="_blank" rel="noopener">doi</a></td><td><code>autonomous-research-agents</code> <code>sociotechnical</code> <code>llm-cognition</code></td><td><code>park2023generative</code></td><td>read</td></tr>
<tr data-year="2023" data-venue="Advances in Neural Information Processing Systems" data-themes="agentic-tool-use" data-status="read"><td>2023</td><td>Schick & others</td><td><a href="notes/schick2023toolformer/">Toolformer: Language Models Can Teach Themselves to Use Tools</a></td><td>Advances in Neural Information Processing Systems</td><td><a href="https://doi.org/10.48550/arXiv.2302.04761" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-tool-use</code></td><td><code>schick2023toolformer</code></td><td>read</td></tr>
<tr data-year="2023" data-venue="Information Systems Research" data-themes="is-methodology|sociotechnical|ai-publishing-ecosystems" data-status="read"><td>2023</td><td>Susarla et al.</td><td><a href="notes/susarla2023janus/">The Janus Effect of Generative AI: Charting the Path for Responsible Conduct of Scholarly Activities in Information Systems</a></td><td>Information Systems Research</td><td><a href="https://doi.org/10.1287/isre.2023.ed.v34.n2" target="_blank" rel="noopener">doi</a></td><td><code>is-methodology</code> <code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>susarla2023janus</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="National Bureau of Economic Research" data-themes="research-productivity|human-ai-research-collaboration|llm-cognition|sociotechnical" data-status="read"><td>2024</td><td>Agrawal et al.</td><td><a href="notes/agrawal2024aiscience/">AI in Science</a></td><td>National Bureau of Economic Research</td><td><a href="https://www.nber.org/papers/w34953" target="_blank" rel="noopener">link</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>llm-cognition</code> <code>sociotechnical</code></td><td><code>agrawal2024aiscience</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="sociotechnical|is-methodology" data-status="skimmed"><td>2024</td><td>Alavi et al.</td><td><a href="notes/alavi2024kmperspective/">A Knowledge Management Perspective of Generative Artificial Intelligence</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00859" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code> <code>is-methodology</code></td><td><code>alavi2024kmperspective</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="hallucination|evaluation-of-ai-research|agentic-reasoning" data-status="skimmed"><td>2024</td><td>Asai et al.</td><td><a href="notes/asai2024openscholar/">OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2411.14199" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>hallucination</code> <code>evaluation-of-ai-research</code> <code>agentic-reasoning</code></td><td><code>asai2024openscholar</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="sociotechnical|ai-publishing-ecosystems" data-status="skimmed"><td>2024</td><td>Avital</td><td><a href="notes/avital2024decentralization/">Digital Transformation of Academic Publishing: A Call for the Decentralization and Democratization of Academic Journals</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00873" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>avital2024decentralization</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="autonomous-research-agents|ai-peer-review|human-ai-research-collaboration" data-status="skimmed"><td>2024</td><td>Baek et al.</td><td><a href="notes/baek2024researchagent/">ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2404.07738" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>ai-peer-review</code> <code>human-ai-research-collaboration</code></td><td><code>baek2024researchagent</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="sociotechnical|research-productivity" data-status="skimmed"><td>2024</td><td>Benbya et al.</td><td><a href="notes/benbya2024navigating/">Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00861" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code> <code>research-productivity</code></td><td><code>benbya2024navigating</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="ai-peer-review|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>D'Arcy et al.</td><td><a href="notes/darcy2024marg/">MARG: Multi-Agent Review Generation for Scientific Papers</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2401.04259" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>ai-peer-review</code> <code>evaluation-of-ai-research</code></td><td><code>darcy2024marg</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="ai-peer-review|human-ai-research-collaboration" data-status="skimmed"><td>2024</td><td>Drori & Te'eni</td><td><a href="notes/drori2024humanloop/">Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00867" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>human-ai-research-collaboration</code></td><td><code>drori2024humanloop</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="peer-review|ai-publishing-ecosystems|evaluation-rigor" data-status="read"><td>2024</td><td>Goldberg et al.</td><td><a href="notes/neurips2024checklist/">Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers: NeurIPS'24 Experiment</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2411.03417" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>peer-review</code> <code>ai-publishing-ecosystems</code> <code>evaluation-rigor</code></td><td><code>neurips2024checklist</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="ai-peer-review|sociotechnical|is-methodology" data-status="skimmed"><td>2024</td><td>Gregor</td><td><a href="notes/gregor2024responsible/">Responsible Artificial Intelligence and Journal Publishing</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00863" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>sociotechnical</code> <code>is-methodology</code></td><td><code>gregor2024responsible</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="is-methodology|human-ai-research-collaboration" data-status="skimmed"><td>2024</td><td>Jarvenpaa & Klein</td><td><a href="notes/jarvenpaa2024theorizing/">New Frontiers in Information Systems Theorizing: Human-gAI Collaboration</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00868" target="_blank" rel="noopener">doi</a></td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code></td><td><code>jarvenpaa2024theorizing</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Proceedings of EMNLP 2024" data-themes="human-ai-research-collaboration|agentic-reasoning|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Jiang et al.</td><td><a href="notes/jiang2024costorm/">Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations</a></td><td>Proceedings of EMNLP 2024</td><td><a href="https://doi.org/10.48550/arXiv.2408.15232" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>human-ai-research-collaboration</code> <code>agentic-reasoning</code> <code>evaluation-of-ai-research</code></td><td><code>jiang2024costorm</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="ai-peer-review|sociotechnical" data-status="skimmed"><td>2024</td><td>Kankanhalli</td><td><a href="notes/kankanhalli2024peerreview/">Peer Review in the Age of Generative AI</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00865" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>sociotechnical</code></td><td><code>kankanhalli2024peerreview</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="ai-peer-review|evaluation-of-ai-research|ai-publishing-ecosystems" data-status="read"><td>2024</td><td>Latona et al.</td><td><a href="notes/latona2024reviewlottery/">The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2405.02150" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>ai-peer-review</code> <code>evaluation-of-ai-research</code> <code>ai-publishing-ecosystems</code></td><td><code>latona2024reviewlottery</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="research-productivity|evaluation-of-ai-research" data-status="read"><td>2024</td><td>Liang et al.</td><td><a href="notes/liang2024mapping/">Mapping the Increasing Use of LLMs in Scientific Papers</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2404.01268" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>research-productivity</code> <code>evaluation-of-ai-research</code></td><td><code>liang2024mapping</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="ai-peer-review|evaluation-of-ai-research|sociotechnical" data-status="read"><td>2024</td><td>Liang et al.</td><td><a href="notes/liang2024monitoring/">Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2403.07183" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>ai-peer-review</code> <code>evaluation-of-ai-research</code> <code>sociotechnical</code></td><td><code>liang2024monitoring</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="autonomous-research-agents|ai-peer-review|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Lu et al.</td><td><a href="notes/lu2024aiscientist/">The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2408.06292" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>ai-peer-review</code> <code>evaluation-of-ai-research</code></td><td><code>lu2024aiscientist</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="ai-publishing-ecosystems|research-ethics|peer-review" data-status="read"><td>2024</td><td>Lund et al.</td><td><a href="notes/lund2024aiacademic/">The Impact of AI on Academic Research and Publishing</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2406.06009" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>ai-publishing-ecosystems</code> <code>research-ethics</code> <code>peer-review</code></td><td><code>lund2024aiacademic</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="agentic-tool-use|agentic-reasoning|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Narayanan et al.</td><td><a href="notes/narayanan2024aviary/">Aviary: training language agents on challenging scientific tasks</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2412.21154" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-tool-use</code> <code>agentic-reasoning</code> <code>evaluation-of-ai-research</code></td><td><code>narayanan2024aviary</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="is-methodology|human-ai-research-collaboration|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Ngwenyama & Rowe</td><td><a href="notes/ngwenyama2024literature/">Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00869" target="_blank" rel="noopener">doi</a></td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code> <code>evaluation-of-ai-research</code></td><td><code>ngwenyama2024literature</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="International Journal of Information Management" data-themes="style-engines|is-methodology|sociotechnical" data-status="read"><td>2024</td><td>Riemer & Peter</td><td><a href="notes/riemer2024styleengines/">Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications</a></td><td>International Journal of Information Management</td><td><a href="https://doi.org/10.1016/j.ijinfomgt.2024.102824" target="_blank" rel="noopener">doi</a></td><td><code>style-engines</code> <code>is-methodology</code> <code>sociotechnical</code></td><td><code>riemer2024styleengines</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="sociotechnical" data-status="skimmed"><td>2024</td><td>Sabherwal & Grover</td><td><a href="notes/sabherwal2024societal/">The Societal Impacts of Generative Artificial Intelligence: A Balanced Perspective</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00860" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code></td><td><code>sabherwal2024societal</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="ai-peer-review|is-methodology|human-ai-research-collaboration" data-status="skimmed"><td>2024</td><td>Sarker et al.</td><td><a href="notes/sarker2024democratizing/">Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00872" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>is-methodology</code> <code>human-ai-research-collaboration</code></td><td><code>sarker2024democratizing</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="is-methodology|human-ai-research-collaboration|ai-publishing-ecosystems" data-status="read"><td>2024</td><td>Schwartz & Te'eni</td><td><a href="notes/schwartz2024kcc/">AI for Knowledge Creation, Curation, and Consumption in Context</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00862" target="_blank" rel="noopener">doi</a></td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code> <code>ai-publishing-ecosystems</code></td><td><code>schwartz2024kcc</code></td><td>read</td></tr>
<tr data-year="2024" data-venue="Proceedings of NAACL 2024" data-themes="agentic-reasoning|hallucination|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Shao et al.</td><td><a href="notes/shao2024storm/">Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models</a></td><td>Proceedings of NAACL 2024</td><td><a href="https://doi.org/10.48550/arXiv.2402.14207" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-reasoning</code> <code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>shao2024storm</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="ai-peer-review|is-methodology" data-status="skimmed"><td>2024</td><td>Shmueli & Ray</td><td><a href="notes/shmueli2024editorial/">Reimagining the Journal Editorial Process: An AI-Augmented Versus an AI-Driven Future</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00864" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>is-methodology</code></td><td><code>shmueli2024editorial</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="arXiv" data-themes="hallucination|agentic-tool-use|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Skarlinski et al.</td><td><a href="notes/skarlinski2024paperqa2/">Language agents achieve superhuman synthesis of scientific knowledge</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2409.13740" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>hallucination</code> <code>agentic-tool-use</code> <code>evaluation-of-ai-research</code></td><td><code>skarlinski2024paperqa2</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Advances in Neural Information Processing Systems 37 (NeurIPS 2024)" data-themes="autonomous-research-agents|evaluation-of-ai-research|agentic-reasoning" data-status="skimmed"><td>2024</td><td>Wang et al.</td><td><a href="notes/wang2024autosurvey/">AutoSurvey: Large Language Models Can Automatically Write Surveys</a></td><td>Advances in Neural Information Processing Systems 37 (NeurIPS 2024)</td><td><a href="https://doi.org/10.48550/arXiv.2406.10252" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>evaluation-of-ai-research</code> <code>agentic-reasoning</code></td><td><code>wang2024autosurvey</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="is-methodology|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Watson et al.</td><td><a href="notes/watson2024causal/">Extending the Foresight of Phillip Ein-Dor: Causal Knowledge Analytics</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00871" target="_blank" rel="noopener">doi</a></td><td><code>is-methodology</code> <code>evaluation-of-ai-research</code></td><td><code>watson2024causal</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="ai-peer-review|sociotechnical" data-status="skimmed"><td>2024</td><td>Weber</td><td><a href="notes/weber2024roboreviewer/">The Other Reviewer: RoboReviewer</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00866" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>sociotechnical</code></td><td><code>weber2024roboreviewer</code></td><td>skimmed</td></tr>
<tr data-year="2024" data-venue="Journal of the Association for Information Systems" data-themes="is-methodology|sociotechnical|evaluation-of-ai-research" data-status="skimmed"><td>2024</td><td>Yoo</td><td><a href="notes/yoo2024epistemic/">Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00870" target="_blank" rel="noopener">doi</a></td><td><code>is-methodology</code> <code>sociotechnical</code> <code>evaluation-of-ai-research</code></td><td><code>yoo2024epistemic</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="autonomous-research-agents|agentic-reasoning|evaluation-of-ai-research" data-status="skimmed"><td>2025</td><td>Agarwal et al.</td><td><a href="notes/agarwal2025autodiscovery/">AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2507.00310" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>agentic-reasoning</code> <code>evaluation-of-ai-research</code></td><td><code>agarwal2025autodiscovery</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="SSRN Working Paper" data-themes="research-productivity|human-ai-research-collaboration|agentic-tool-use" data-status="read"><td>2025</td><td>Bapna et al.</td><td><a href="notes/bapna2025analytics/">Agentic AI and Managers' Analytics Capabilities: An Exploration</a></td><td>SSRN Working Paper</td><td><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5293722" target="_blank" rel="noopener">link</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>agentic-tool-use</code></td><td><code>bapna2025analytics</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="evaluation-of-ai-research|autonomous-research-agents|agentic-tool-use" data-status="skimmed"><td>2025</td><td>Bragg et al.</td><td><a href="notes/bragg2025astabench/">AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2510.21652" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>evaluation-of-ai-research</code> <code>autonomous-research-agents</code> <code>agentic-tool-use</code></td><td><code>bragg2025astabench</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="National Bureau of Economic Research" data-themes="replication-infrastructure|evaluation-of-ai-research" data-status="read"><td>2025</td><td>Brodeur et al.</td><td><a href="notes/brodeur2025reproducibility/">Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis</a></td><td>National Bureau of Economic Research</td><td><a href="https://www.nber.org/papers/w33753" target="_blank" rel="noopener">link</a></td><td><code>replication-infrastructure</code> <code>evaluation-of-ai-research</code></td><td><code>brodeur2025reproducibility</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="Quarterly Journal of Economics" data-themes="research-productivity|human-ai-research-collaboration|sociotechnical" data-status="read"><td>2025</td><td>Brynjolfsson et al.</td><td><a href="notes/brynjolfsson2025genaiwork/">Generative AI at Work</a></td><td>Quarterly Journal of Economics</td><td><a href="https://doi.org/10.1093/qje/qjae044" target="_blank" rel="noopener">doi</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>sociotechnical</code></td><td><code>brynjolfsson2025genaiwork</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="reasoning-faithfulness|agentic-reasoning|hallucination|evaluation-of-ai-research" data-status="read"><td>2025</td><td>Chen & others</td><td><a href="notes/chen2025reasoning/">Reasoning Models Don't Always Say What They Think</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2505.05410" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>reasoning-faithfulness</code> <code>agentic-reasoning</code> <code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>chen2025reasoning</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="ai-peer-review|hallucination|sociotechnical" data-status="read"><td>2025</td><td>Collu et al.</td><td><a href="notes/collu2025misleading/">Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2508.20863" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>ai-peer-review</code> <code>hallucination</code> <code>sociotechnical</code></td><td><code>collu2025misleading</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="Causal Inference Substack" data-themes="" data-status="—"><td>2025</td><td>Cunningham</td><td>Claude Code for Causal Inference</td><td>Causal Inference Substack</td><td><a href="https://causalinf.substack.com/s/claude-code" target="_blank" rel="noopener">link</a></td><td></td><td><code>cunningham2025claudecode</code></td><td>—</td></tr>
<tr data-year="2025" data-venue="Markus Academy Substack" data-themes="" data-status="—"><td>2025</td><td>Eberhardt</td><td>Claude Code for Applied Economists</td><td>Markus Academy Substack</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists" target="_blank" rel="noopener">link</a></td><td></td><td><code>eberhardt2025claudecode</code></td><td>—</td></tr>
<tr data-year="2025" data-venue="Nature Editorial, d41586-025-01880-9" data-themes="ai-peer-review|ai-publishing-ecosystems|sociotechnical" data-status="read"><td>2025</td><td>Editorial</td><td><a href="notes/naturePeerReview2025editorial/">Transparent Peer Review to Be Extended to All Research Papers</a></td><td>Nature Editorial, d41586-025-01880-9</td><td><a href="https://www.nature.com/articles/d41586-025-01880-9" target="_blank" rel="noopener">link</a></td><td><code>ai-peer-review</code> <code>ai-publishing-ecosystems</code> <code>sociotechnical</code></td><td><code>naturePeerReview2025editorial</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="research-productivity|human-ai-research-collaboration|evaluation-of-ai-research" data-status="read"><td>2025</td><td>Filimonovic et al.</td><td><a href="notes/filimonovic2025genai/">Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2510.02408" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>evaluation-of-ai-research</code></td><td><code>filimonovic2025genai</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="agentic-tool-use|autonomous-research-agents" data-status="skimmed"><td>2025</td><td>Gao et al.</td><td><a href="notes/gao2025tooluniverse/">ToolUniverse: An open platform for democratizing AI scientists</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2509.23426" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-tool-use</code> <code>autonomous-research-agents</code></td><td><code>gao2025tooluniverse</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="" data-status="—"><td>2025</td><td>Georgiev et al.</td><td>Mathematical Exploration and Discovery at Scale</td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2511.02864" target="_blank" rel="noopener">doi (arXiv)</a></td><td></td><td><code>georgiev2025alphaevolvemath</code></td><td>—</td></tr>
<tr data-year="2025" data-venue="Information Systems Research" data-themes="is-methodology|human-ai-research-collaboration|autonomous-research-agents|sociotechnical" data-status="read"><td>2025</td><td>Gopal & others</td><td><a href="notes/gopal2025inventing/">Inventing with Machines: Generative AI and the Evolving Landscape of IS Research</a></td><td>Information Systems Research</td><td><a href="https://doi.org/10.1287/isre.2025.editorial.v36.n4" target="_blank" rel="noopener">doi</a></td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code> <code>autonomous-research-agents</code> <code>sociotechnical</code></td><td><code>gopal2025inventing</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="autonomous-research-agents|evaluation-of-ai-research" data-status="skimmed"><td>2025</td><td>Gridach et al.</td><td><a href="notes/gridach2025agenticsurvey/">Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2503.08979" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>evaluation-of-ai-research</code></td><td><code>gridach2025agenticsurvey</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="NEJM AI" data-themes="agentic-pipelines|traceability-verifiability|end-to-end-research" data-status="read"><td>2025</td><td>Ifargan et al.</td><td><a href="notes/ifargan2024datatopaper/">Autonomous LLM-Driven Research — from Data to Human-Verifiable Research Papers</a></td><td>NEJM AI</td><td><a href="https://doi.org/10.1056/AIoa2400555" target="_blank" rel="noopener">doi</a></td><td><code>agentic-pipelines</code> <code>traceability-verifiability</code> <code>end-to-end-research</code></td><td><code>ifargan2024datatopaper</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="ai-peer-review|hallucination" data-status="read"><td>2025</td><td>Keuper</td><td><a href="notes/keuper2025promptinjection/">Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2509.10248" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>ai-peer-review</code> <code>hallucination</code></td><td><code>keuper2025promptinjection</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="Proceedings of the International Conference on Information Systems (ICIS)" data-themes="research-productivity|sociotechnical" data-status="skimmed"><td>2025</td><td>Kwon & Yang</td><td><a href="notes/kwon2025inequality/">Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality</a></td><td>Proceedings of the International Conference on Information Systems (ICIS)</td><td><a href="https://aisel.aisnet.org/icis2025/gen_ai/gen_ai/2" target="_blank" rel="noopener">link</a></td><td><code>research-productivity</code> <code>sociotechnical</code></td><td><code>kwon2025inequality</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="autonomous-research-agents|evaluation-of-ai-research|hallucination" data-status="skimmed"><td>2025</td><td>Liang et al.</td><td><a href="notes/liang2025surveyx/">SurveyX: Academic Survey Automation via Large Language Models</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2502.14776" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>evaluation-of-ai-research</code> <code>hallucination</code></td><td><code>liang2025surveyx</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="International Conference on Learning Representations (ICLR)" data-themes="reasoning-faithfulness|hallucination|evaluation-of-ai-research" data-status="read"><td>2025</td><td>Matton & others</td><td><a href="notes/matton2025walkthetalk/">Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations</a></td><td>International Conference on Learning Representations (ICLR)</td><td><a href="https://doi.org/10.48550/arXiv.2504.14150" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>reasoning-faithfulness</code> <code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>matton2025walkthetalk</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="European Journal of Information Systems" data-themes="sociotechnical|is-methodology|evaluation-of-ai-research" data-status="read"><td>2025</td><td>Mikalef et al.</td><td><a href="notes/mikalef2025responsible/">Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research</a></td><td>European Journal of Information Systems</td><td><a href="https://doi.org/10.1080/0960085X.2025.2506875" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code> <code>is-methodology</code> <code>evaluation-of-ai-research</code></td><td><code>mikalef2025responsible</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="autonomous-research-agents|hallucination|research-productivity|evaluation-of-ai-research" data-status="skimmed"><td>2025</td><td>Mitchener et al.</td><td><a href="notes/mitchener2025kosmos/">Kosmos: An AI Scientist for Autonomous Discovery</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2511.02824" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>hallucination</code> <code>research-productivity</code> <code>evaluation-of-ai-research</code></td><td><code>mitchener2025kosmos</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="Nature" data-themes="ai-peer-review|ai-publishing-ecosystems|sociotechnical" data-status="read"><td>2025</td><td>Naddaf</td><td><a href="notes/naddaf2025aipeer/">AI Is Transforming Peer Review — and Many Scientists Are Worried</a></td><td>Nature</td><td><a href="https://doi.org/10.1038/d41586-025-00894-7" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>ai-publishing-ecosystems</code> <code>sociotechnical</code></td><td><code>naddaf2025aipeer</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="evaluation-of-ai-research|autonomous-research-agents|agentic-tool-use" data-status="skimmed"><td>2025</td><td>Nathani et al.</td><td><a href="notes/nathani2025mlgym/">MLGym: A New Framework and Benchmark for Advancing AI Research Agents</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2502.14499" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>evaluation-of-ai-research</code> <code>autonomous-research-agents</code> <code>agentic-tool-use</code></td><td><code>nathani2025mlgym</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="" data-status="—"><td>2025</td><td>Novikov et al.</td><td>AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery</td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2506.13131" target="_blank" rel="noopener">doi (arXiv)</a></td><td></td><td><code>novikov2025alphaevolve</code></td><td>—</td></tr>
<tr data-year="2025" data-venue="Proceedings of the National Academy of Sciences" data-themes="sociotechnical|llm-cognition" data-status="read"><td>2025</td><td>Peter et al.</td><td><a href="notes/peter2025anthropomorphic/">The Benefits and Dangers of Anthropomorphic Conversational Agents</a></td><td>Proceedings of the National Academy of Sciences</td><td><a href="https://doi.org/10.1073/pnas.2415898122" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code> <code>llm-cognition</code></td><td><code>peter2025anthropomorphic</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="autonomous-research-agents|human-ai-research-collaboration|evaluation-of-ai-research" data-status="skimmed"><td>2025</td><td>Schmidgall et al.</td><td><a href="notes/schmidgall2025agentlaboratory/">Agent Laboratory: Using LLM Agents as Research Assistants</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2501.04227" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>human-ai-research-collaboration</code> <code>evaluation-of-ai-research</code></td><td><code>schmidgall2025agentlaboratory</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="replication-infrastructure|autonomous-research-agents" data-status="skimmed"><td>2025</td><td>Seo et al.</td><td><a href="notes/seo2025paper2code/">Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2504.17192" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>replication-infrastructure</code> <code>autonomous-research-agents</code></td><td><code>seo2025paper2code</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="agentic-reasoning|agentic-tool-use" data-status="skimmed"><td>2025</td><td>Team</td><td><a href="notes/tongyi2025deepresearch/">Tongyi DeepResearch Technical Report</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2510.24701" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-reasoning</code> <code>agentic-tool-use</code></td><td><code>tongyi2025deepresearch</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="autonomous-research-agents|evaluation-of-ai-research" data-status="read"><td>2025</td><td>Tie et al.</td><td><a href="notes/tie2025aiscientistsurvey/">A Survey of AI Scientists</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2510.23045" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>evaluation-of-ai-research</code></td><td><code>tie2025aiscientistsurvey</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)" data-themes="agentic-reasoning|agentic-tool-use" data-status="read"><td>2025</td><td>Wu & others</td><td><a href="notes/wu2025agenticreasoning/">Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools</a></td><td>Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</td><td><a href="https://doi.org/10.18653/v1/2025.acl-long.1383" target="_blank" rel="noopener">doi</a></td><td><code>agentic-reasoning</code> <code>agentic-tool-use</code></td><td><code>wu2025agenticreasoning</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="autonomous-research-agents|ai-peer-review|evaluation-of-ai-research" data-status="skimmed"><td>2025</td><td>Yamada et al.</td><td><a href="notes/yamada2025aiscientistv2/">The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2504.08066" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>ai-peer-review</code> <code>evaluation-of-ai-research</code></td><td><code>yamada2025aiscientistv2</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)" data-themes="autonomous-research-agents|ai-peer-review|sociotechnical|evaluation-of-ai-research" data-status="skimmed"><td>2025</td><td>Yu et al.</td><td><a href="notes/yu2025researchtown/">ResearchTown: Simulator of Human Research Community</a></td><td>Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)</td><td><a href="https://doi.org/10.48550/arXiv.2412.17767" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>ai-peer-review</code> <code>sociotechnical</code> <code>evaluation-of-ai-research</code></td><td><code>yu2025researchtown</code></td><td>skimmed</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="ai-publishing-ecosystems|autonomous-research-agents|ai-peer-review|sociotechnical" data-status="read"><td>2025</td><td>Zhang & others</td><td><a href="notes/zhang2025aixiv/">aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2508.15126" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>ai-publishing-ecosystems</code> <code>autonomous-research-agents</code> <code>ai-peer-review</code> <code>sociotechnical</code></td><td><code>zhang2025aixiv</code></td><td>read</td></tr>
<tr data-year="2025" data-venue="arXiv" data-themes="agentic-tool-use|agentic-reasoning|hallucination" data-status="skimmed"><td>2025</td><td>Zheng et al.</td><td><a href="notes/zheng2025deepresearcher/">DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2504.03160" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-tool-use</code> <code>agentic-reasoning</code> <code>hallucination</code></td><td><code>zheng2025deepresearcher</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="INFORMS Information Systems Research, Call for Papers" data-themes="" data-status="—"><td>2026</td><td>Abbasi & others</td><td>ISR Special Issue: Generative AI and New Methods of Inquiry in Information Systems Research</td><td>INFORMS Information Systems Research, Call for Papers</td><td><a href="https://pubsonline.informs.org/page/isre/calls-for-papers" target="_blank" rel="noopener">link</a></td><td></td><td><code>abbasi2026isr</code></td><td>—</td></tr>
<tr data-year="2026" data-venue="SSRN Working Paper" data-themes="sociotechnical|evaluation-of-ai-research|llm-cognition" data-status="read"><td>2026</td><td>Acemoglu et al.</td><td><a href="notes/acemoglu2026collapse/">AI, Human Cognition and Knowledge Collapse</a></td><td>SSRN Working Paper</td><td><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6326698" target="_blank" rel="noopener">link</a></td><td><code>sociotechnical</code> <code>evaluation-of-ai-research</code> <code>llm-cognition</code></td><td><code>acemoglu2026collapse</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="Management Science" data-themes="research-productivity|sociotechnical|ai-publishing-ecosystems" data-status="read"><td>2026</td><td>Bick et al.</td><td><a href="notes/bick2026rapidadoption/">The Rapid Adoption of Generative AI</a></td><td>Management Science</td><td><a href="https://doi.org/10.1287/mnsc.2025.02523" target="_blank" rel="noopener">doi</a></td><td><code>research-productivity</code> <code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>bick2026rapidadoption</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="German Conference on Artificial Intelligence (K\"unstliche Intelligenz)" data-themes="is-methodology|human-ai-research-collaboration" data-status="read"><td>2026</td><td>Br\^\incoveanu et al.</td><td><a href="notes/brincoveanu2026augmenting/">Augmenting Systematic Literature Reviews: A Human-AI Collaborative Framework</a></td><td>German Conference on Artificial Intelligence (K\"unstliche Intelligenz)</td><td>—</td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code></td><td><code>brincoveanu2026augmenting</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="Organization Science" data-themes="research-productivity|human-ai-research-collaboration|evaluation-of-ai-research" data-status="read"><td>2026</td><td>Dell'Acqua et al.</td><td><a href="notes/dellacqua2026jagged/">Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality</a></td><td>Organization Science</td><td><a href="https://doi.org/10.1287/orsc.2025.21838" target="_blank" rel="noopener">doi</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>evaluation-of-ai-research</code></td><td><code>dellacqua2026jagged</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="Organization Science" data-themes="ai-peer-review|ai-publishing-ecosystems|research-productivity" data-status="read"><td>2026</td><td>Gartenberg et al.</td><td><a href="notes/gartenberg2026morebetter/">More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review</a></td><td>Organization Science</td><td><a href="https://doi.org/10.1287/orsc.2026.ed.v37.n3" target="_blank" rel="noopener">doi</a></td><td><code>ai-peer-review</code> <code>ai-publishing-ecosystems</code> <code>research-productivity</code></td><td><code>gartenberg2026morebetter</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="Nature" data-themes="agentic-pipelines|multi-agent-systems|autonomous-research-agents|end-to-end-research" data-status="read"><td>2026</td><td>Ghareeb et al.</td><td><a href="notes/ghareeb2026robin/">A Multi-Agent System for Automating Scientific Discovery</a></td><td>Nature</td><td><a href="https://doi.org/10.1038/s41586-026-10652-y" target="_blank" rel="noopener">doi</a> · <a href="https://arxiv.org/abs/2505.13400" target="_blank" rel="noopener">arXiv</a></td><td><code>agentic-pipelines</code> <code>multi-agent-systems</code> <code>autonomous-research-agents</code> <code>end-to-end-research</code></td><td><code>ghareeb2026robin</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="Nature" data-themes="autonomous-research-agents|agentic-reasoning|human-ai-research-collaboration" data-status="skimmed"><td>2026</td><td>Gottweis et al.</td><td><a href="notes/gottweis2026coscientist/">Accelerating scientific discovery with Co-Scientist</a></td><td>Nature</td><td><a href="https://doi.org/10.1038/s41586-026-10644-y" target="_blank" rel="noopener">doi</a> · <a href="https://arxiv.org/abs/2502.18864" target="_blank" rel="noopener">arXiv</a></td><td><code>autonomous-research-agents</code> <code>agentic-reasoning</code> <code>human-ai-research-collaboration</code></td><td><code>gottweis2026coscientist</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="is-methodology|sociotechnical|ai-publishing-ecosystems" data-status="read"><td>2026</td><td>Jarzębowicz et al.</td><td><a href="notes/jarzebowicz2026landscape/">The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2603.11842" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>is-methodology</code> <code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>jarzebowicz2026landscape</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="autonomous-research-agents|agentic-reasoning|evaluation-of-ai-research" data-status="skimmed"><td>2026</td><td>Jin et al.</td><td><a href="notes/jin2026arbor/">Toward Generalist Autonomous Research via Hypothesis-Tree Refinement</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2606.11926" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>agentic-reasoning</code> <code>evaluation-of-ai-research</code></td><td><code>jin2026arbor</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="replication-infrastructure|evaluation-of-ai-research" data-status="skimmed"><td>2026</td><td>Kohler et al.</td><td><a href="notes/kohler2026agenticreproduction/">Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2604.21965" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>replication-infrastructure</code> <code>evaluation-of-ai-research</code></td><td><code>kohler2026agenticreproduction</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="Information \& Management" data-themes="autonomous-research-agents|is-methodology|sociotechnical" data-status="read"><td>2026</td><td>Kumar et al.</td><td><a href="notes/kumar2025agenticadoption/">Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities</a></td><td>Information \& Management</td><td><a href="https://doi.org/10.1016/j.im.2026.104317" target="_blank" rel="noopener">doi</a></td><td><code>autonomous-research-agents</code> <code>is-methodology</code> <code>sociotechnical</code></td><td><code>kumar2025agenticadoption</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="agentic-tool-use|hallucination|evaluation-of-ai-research|reasoning-faithfulness" data-status="read"><td>2026</td><td>Laban et al.</td><td><a href="notes/laban2026llmscorrupt/">LLMs Corrupt Your Documents When You Delegate</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2604.15597" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-tool-use</code> <code>hallucination</code> <code>evaluation-of-ai-research</code> <code>reasoning-faithfulness</code></td><td><code>laban2026llmscorrupt</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="Nature Biotechnology" data-themes="agentic-pipelines|multi-agent-systems|autonomous-research-agents|sociotechnical" data-status="read"><td>2026</td><td>Li et al.</td><td><a href="notes/li2026agenticbiomedical/">Agentic AI and the Rise of in silico Team Science in Biomedical Research</a></td><td>Nature Biotechnology</td><td><a href="https://doi.org/10.1038/s41587-026-03035-1" target="_blank" rel="noopener">doi</a></td><td><code>agentic-pipelines</code> <code>multi-agent-systems</code> <code>autonomous-research-agents</code> <code>sociotechnical</code></td><td><code>li2026agenticbiomedical</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="replication-infrastructure|evaluation-of-ai-research" data-status="skimmed"><td>2026</td><td>Li et al.</td><td><a href="notes/li2026reprorepo/">ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2606.18237" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>replication-infrastructure</code> <code>evaluation-of-ai-research</code></td><td><code>li2026reprorepo</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="autonomous-research-agents|human-ai-research-collaboration|hallucination|evaluation-of-ai-research" data-status="skimmed"><td>2026</td><td>Liu et al.</td><td><a href="notes/liu2026autoresearchclaw/">AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2605.20025" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>human-ai-research-collaboration</code> <code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>liu2026autoresearchclaw</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="evaluation-of-ai-research|autonomous-research-agents" data-status="skimmed"><td>2026</td><td>Lupidi et al.</td><td><a href="notes/lupidi2026airsbench/">AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2602.06855" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>evaluation-of-ai-research</code> <code>autonomous-research-agents</code></td><td><code>lupidi2026airsbench</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="agentic-pipelines|multi-agent-systems|self-improvement|memory-systems" data-status="read"><td>2026</td><td>Lyu et al.</td><td><a href="notes/evoscientist2026techreport/">EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2603.08127" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-pipelines</code> <code>multi-agent-systems</code> <code>self-improvement</code> <code>memory-systems</code></td><td><code>evoscientist2026techreport</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="European Journal of Information Systems" data-themes="sociotechnical|ai-publishing-ecosystems" data-status="read"><td>2026</td><td>Ngwenyama et al.</td><td><a href="notes/ngwenyama2026platform/">Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor</a></td><td>European Journal of Information Systems</td><td><a href="https://doi.org/10.1080/0960085X.2026.2642660" target="_blank" rel="noopener">doi</a></td><td><code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>ngwenyama2026platform</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="Journal of Economic Literature" data-themes="autonomous-research-agents|research-productivity|evaluation-of-ai-research|hallucination" data-status="read"><td>2026</td><td>Novy-Marx & Velikov</td><td><a href="notes/novymarx2026aifinance/">Artificial Intelligence–Powered (Finance) Scholarship</a></td><td>Journal of Economic Literature</td><td><a href="https://doi.org/10.1257/jel.20251821" target="_blank" rel="noopener">doi</a> · <a href="https://www.nber.org/papers/w33363" target="_blank" rel="noopener">NBER</a></td><td><code>autonomous-research-agents</code> <code>research-productivity</code> <code>evaluation-of-ai-research</code> <code>hallucination</code></td><td><code>novymarx2026aifinance</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="autonomous-research-agents|agentic-reasoning" data-status="skimmed"><td>2026</td><td>Qu et al.</td><td><a href="notes/qu2026coral/">CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2604.01658" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>autonomous-research-agents</code> <code>agentic-reasoning</code></td><td><code>qu2026coral</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="evaluation-of-ai-research|autonomous-research-agents|agentic-reasoning" data-status="skimmed"><td>2026</td><td>Wang et al.</td><td><a href="notes/wang2026aarribench/">Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2606.07462" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>evaluation-of-ai-research</code> <code>autonomous-research-agents</code> <code>agentic-reasoning</code></td><td><code>wang2026aarribench</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="evaluation-of-ai-research|replication-infrastructure|autonomous-research-agents" data-status="skimmed"><td>2026</td><td>Wang et al.</td><td><a href="notes/wang2026naturebench/">NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2606.24530" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>evaluation-of-ai-research</code> <code>replication-infrastructure</code> <code>autonomous-research-agents</code></td><td><code>wang2026naturebench</code></td><td>skimmed</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="agentic-pipelines|multi-agent-systems|evaluation-rigor|harness-engineering" data-status="read"><td>2026</td><td>Yang et al.</td><td><a href="notes/yang2026aris/">ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2605.03042" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>agentic-pipelines</code> <code>multi-agent-systems</code> <code>evaluation-rigor</code> <code>harness-engineering</code></td><td><code>yang2026aris</code></td><td>read</td></tr>
<tr data-year="2026" data-venue="arXiv" data-themes="human-ai-research-collaboration|autonomous-research-agents|agentic-tool-use" data-status="skimmed"><td>2026</td><td>Zheng et al.</td><td><a href="notes/zheng2026comathematician/">AI co-mathematician: Accelerating mathematicians with agentic AI</a></td><td>arXiv</td><td><a href="https://doi.org/10.48550/arXiv.2605.06651" target="_blank" rel="noopener">doi (arXiv)</a></td><td><code>human-ai-research-collaboration</code> <code>autonomous-research-agents</code> <code>agentic-tool-use</code></td><td><code>zheng2026comathematician</code></td><td>skimmed</td></tr>
</tbody>
</table>

<!-- AUTO-GENERATED:papers-table-end -->

??? note "Browse by theme"

    <!-- AUTO-GENERATED:papers-by-theme-start -->

### `agentic-pipelines`

- **2025** — Ifargan et al.. [*Autonomous LLM-Driven Research --- from Data to Human-Verifiable Research Papers*](notes/ifargan2024datatopaper.md) `ifargan2024datatopaper`
- **2026** — Lyu et al.. [*EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery*](notes/evoscientist2026techreport.md) `evoscientist2026techreport`
- **2026** — Ghareeb et al.. [*A Multi-Agent System for Automating Scientific Discovery*](notes/ghareeb2026robin.md) `ghareeb2026robin`
- **2026** — Li et al.. [*Agentic AI and the Rise of in silico Team Science in Biomedical Research*](notes/li2026agenticbiomedical.md) `li2026agenticbiomedical`
- **2026** — Yang et al.. [*ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration*](notes/yang2026aris.md) `yang2026aris`

### `agentic-reasoning`

- **2024** — Asai et al.. [*OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs*](notes/asai2024openscholar.md) `asai2024openscholar` · skimmed
- **2024** — Jiang et al.. [*Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations*](notes/jiang2024costorm.md) `jiang2024costorm` · skimmed
- **2024** — Narayanan et al.. [*Aviary: training language agents on challenging scientific tasks*](notes/narayanan2024aviary.md) `narayanan2024aviary` · skimmed
- **2024** — Shao et al.. [*Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models*](notes/shao2024storm.md) `shao2024storm` · skimmed
- **2024** — Wang et al.. [*AutoSurvey: Large Language Models Can Automatically Write Surveys*](notes/wang2024autosurvey.md) `wang2024autosurvey` · skimmed
- **2025** — Agarwal et al.. [*AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise*](notes/agarwal2025autodiscovery.md) `agarwal2025autodiscovery` · skimmed
- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Team. [*Tongyi DeepResearch Technical Report*](notes/tongyi2025deepresearch.md) `tongyi2025deepresearch` · skimmed
- **2025** — Wu & others. [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- **2025** — Zheng et al.. [*DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments*](notes/zheng2025deepresearcher.md) `zheng2025deepresearcher` · skimmed
- **2026** — Gottweis et al.. [*Accelerating scientific discovery with Co-Scientist*](notes/gottweis2026coscientist.md) `gottweis2026coscientist` · skimmed
- **2026** — Jin et al.. [*Toward Generalist Autonomous Research via Hypothesis-Tree Refinement*](notes/jin2026arbor.md) `jin2026arbor` · skimmed
- **2026** — Qu et al.. [*CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery*](notes/qu2026coral.md) `qu2026coral` · skimmed
- **2026** — Wang et al.. [*Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle*](notes/wang2026aarribench.md) `wang2026aarribench` · skimmed

### `agentic-tool-use`

- **2023** — Lála et al.. [*PaperQA: Retrieval-Augmented Generative Agent for Scientific Research*](notes/lala2023paperqa.md) `lala2023paperqa` · skimmed
- **2023** — Schick & others. [*Toolformer: Language Models Can Teach Themselves to Use Tools*](notes/schick2023toolformer.md) `schick2023toolformer`
- **2024** — Narayanan et al.. [*Aviary: training language agents on challenging scientific tasks*](notes/narayanan2024aviary.md) `narayanan2024aviary` · skimmed
- **2024** — Skarlinski et al.. [*Language agents achieve superhuman synthesis of scientific knowledge*](notes/skarlinski2024paperqa2.md) `skarlinski2024paperqa2` · skimmed
- **2025** — Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- **2025** — Bragg et al.. [*AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite*](notes/bragg2025astabench.md) `bragg2025astabench` · skimmed
- **2025** — Gao et al.. [*ToolUniverse: An open platform for democratizing AI scientists*](notes/gao2025tooluniverse.md) `gao2025tooluniverse` · skimmed
- **2025** — Nathani et al.. [*MLGym: A New Framework and Benchmark for Advancing AI Research Agents*](notes/nathani2025mlgym.md) `nathani2025mlgym` · skimmed
- **2025** — Team. [*Tongyi DeepResearch Technical Report*](notes/tongyi2025deepresearch.md) `tongyi2025deepresearch` · skimmed
- **2025** — Wu & others. [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- **2025** — Zheng et al.. [*DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments*](notes/zheng2025deepresearcher.md) `zheng2025deepresearcher` · skimmed
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`
- **2026** — Zheng et al.. [*AI co-mathematician: Accelerating mathematicians with agentic AI*](notes/zheng2026comathematician.md) `zheng2026comathematician` · skimmed

### `ai-peer-review`

- **2024** — Baek et al.. [*ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models*](notes/baek2024researchagent.md) `baek2024researchagent` · skimmed
- **2024** — D'Arcy et al.. [*MARG: Multi-Agent Review Generation for Scientific Papers*](notes/darcy2024marg.md) `darcy2024marg` · skimmed
- **2024** — Drori & Te'eni. [*Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks*](notes/drori2024humanloop.md) `drori2024humanloop` · skimmed
- **2024** — Gregor. [*Responsible Artificial Intelligence and Journal Publishing*](notes/gregor2024responsible.md) `gregor2024responsible` · skimmed
- **2024** — Kankanhalli. [*Peer Review in the Age of Generative AI*](notes/kankanhalli2024peerreview.md) `kankanhalli2024peerreview` · skimmed
- **2024** — Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/latona2024reviewlottery.md) `latona2024reviewlottery`
- **2024** — Liang et al.. [*Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*](notes/liang2024monitoring.md) `liang2024monitoring`
- **2024** — Lu et al.. [*The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*](notes/lu2024aiscientist.md) `lu2024aiscientist` · skimmed
- **2024** — Sarker et al.. [*Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review*](notes/sarker2024democratizing.md) `sarker2024democratizing` · skimmed
- **2024** — Shmueli & Ray. [*Reimagining the Journal Editorial Process: An AI-Augmented Versus an AI-Driven Future*](notes/shmueli2024editorial.md) `shmueli2024editorial` · skimmed
- **2024** — Weber. [*The Other Reviewer: RoboReviewer*](notes/weber2024roboreviewer.md) `weber2024roboreviewer` · skimmed
- **2025** — Keuper. [*Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications*](notes/keuper2025promptinjection.md) `keuper2025promptinjection`
- **2025** — Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- **2025** — Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- **2025** — Yamada et al.. [*The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*](notes/yamada2025aiscientistv2.md) `yamada2025aiscientistv2` · skimmed
- **2025** — Yu et al.. [*ResearchTown: Simulator of Human Research Community*](notes/yu2025researchtown.md) `yu2025researchtown` · skimmed
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2025** — Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2025misleading.md) `collu2025misleading`
- **2026** — Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`

### `ai-publishing-ecosystems`

- **2023** — Susarla et al.. [*The Janus Effect of Generative AI: Charting the Path for Responsible Conduct of Scholarly Activities in Information Systems*](notes/susarla2023janus.md) `susarla2023janus`
- **2024** — Avital. [*Digital Transformation of Academic Publishing: A Call for the Decentralization and Democratization of Academic Journals*](notes/avital2024decentralization.md) `avital2024decentralization` · skimmed
- **2024** — Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/latona2024reviewlottery.md) `latona2024reviewlottery`
- **2024** — Lund et al.. [*The Impact of AI on Academic Research and Publishing*](notes/lund2024aiacademic.md) `lund2024aiacademic`
- **2024** — Goldberg et al.. [*Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers: NeurIPS'24 Experiment*](notes/neurips2024checklist.md) `neurips2024checklist`
- **2024** — Schwartz & Te'eni. [*AI for Knowledge Creation, Curation, and Consumption in Context*](notes/schwartz2024kcc.md) `schwartz2024kcc`
- **2026** — Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2026rapidadoption.md) `bick2026rapidadoption`
- **2025** — Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- **2025** — Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2026** — Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`
- **2026** — Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- **2026** — Ngwenyama et al.. [*Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor*](notes/ngwenyama2026platform.md) `ngwenyama2026platform`

### `autonomous-research-agents`

- **2023** — Park & others. [*Generative Agents: Interactive Simulacra of Human Behavior*](notes/park2023generative.md) `park2023generative`
- **2024** — Baek et al.. [*ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models*](notes/baek2024researchagent.md) `baek2024researchagent` · skimmed
- **2024** — Lu et al.. [*The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*](notes/lu2024aiscientist.md) `lu2024aiscientist` · skimmed
- **2026** — Novy-Marx & Velikov. [*Artificial Intelligence--Powered (Finance) Scholarship*](notes/novymarx2026aifinance.md) `novymarx2026aifinance`
- **2024** — Wang et al.. [*AutoSurvey: Large Language Models Can Automatically Write Surveys*](notes/wang2024autosurvey.md) `wang2024autosurvey` · skimmed
- **2025** — Agarwal et al.. [*AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise*](notes/agarwal2025autodiscovery.md) `agarwal2025autodiscovery` · skimmed
- **2025** — Bragg et al.. [*AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite*](notes/bragg2025astabench.md) `bragg2025astabench` · skimmed
- **2025** — Gao et al.. [*ToolUniverse: An open platform for democratizing AI scientists*](notes/gao2025tooluniverse.md) `gao2025tooluniverse` · skimmed
- **2025** — Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- **2025** — Gridach et al.. [*Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions*](notes/gridach2025agenticsurvey.md) `gridach2025agenticsurvey` · skimmed
- **2025** — Liang et al.. [*SurveyX: Academic Survey Automation via Large Language Models*](notes/liang2025surveyx.md) `liang2025surveyx` · skimmed
- **2025** — Mitchener et al.. [*Kosmos: An AI Scientist for Autonomous Discovery*](notes/mitchener2025kosmos.md) `mitchener2025kosmos` · skimmed
- **2025** — Nathani et al.. [*MLGym: A New Framework and Benchmark for Advancing AI Research Agents*](notes/nathani2025mlgym.md) `nathani2025mlgym` · skimmed
- **2025** — Schmidgall et al.. [*Agent Laboratory: Using LLM Agents as Research Assistants*](notes/schmidgall2025agentlaboratory.md) `schmidgall2025agentlaboratory` · skimmed
- **2025** — Seo et al.. [*Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning*](notes/seo2025paper2code.md) `seo2025paper2code` · skimmed
- **2025** — Tie et al.. [*A Survey of AI Scientists*](notes/tie2025aiscientistsurvey.md) `tie2025aiscientistsurvey`
- **2025** — Yamada et al.. [*The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*](notes/yamada2025aiscientistv2.md) `yamada2025aiscientistv2` · skimmed
- **2025** — Yu et al.. [*ResearchTown: Simulator of Human Research Community*](notes/yu2025researchtown.md) `yu2025researchtown` · skimmed
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2026** — Ghareeb et al.. [*A Multi-Agent System for Automating Scientific Discovery*](notes/ghareeb2026robin.md) `ghareeb2026robin`
- **2026** — Gottweis et al.. [*Accelerating scientific discovery with Co-Scientist*](notes/gottweis2026coscientist.md) `gottweis2026coscientist` · skimmed
- **2026** — Jin et al.. [*Toward Generalist Autonomous Research via Hypothesis-Tree Refinement*](notes/jin2026arbor.md) `jin2026arbor` · skimmed
- **2026** — Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`
- **2026** — Li et al.. [*Agentic AI and the Rise of in silico Team Science in Biomedical Research*](notes/li2026agenticbiomedical.md) `li2026agenticbiomedical`
- **2026** — Liu et al.. [*AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration*](notes/liu2026autoresearchclaw.md) `liu2026autoresearchclaw` · skimmed
- **2026** — Lupidi et al.. [*AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents*](notes/lupidi2026airsbench.md) `lupidi2026airsbench` · skimmed
- **2026** — Qu et al.. [*CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery*](notes/qu2026coral.md) `qu2026coral` · skimmed
- **2026** — Wang et al.. [*Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle*](notes/wang2026aarribench.md) `wang2026aarribench` · skimmed
- **2026** — Wang et al.. [*NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?*](notes/wang2026naturebench.md) `wang2026naturebench` · skimmed
- **2026** — Zheng et al.. [*AI co-mathematician: Accelerating mathematicians with agentic AI*](notes/zheng2026comathematician.md) `zheng2026comathematician` · skimmed

### `end-to-end-research`

- **2025** — Ifargan et al.. [*Autonomous LLM-Driven Research --- from Data to Human-Verifiable Research Papers*](notes/ifargan2024datatopaper.md) `ifargan2024datatopaper`
- **2026** — Ghareeb et al.. [*A Multi-Agent System for Automating Scientific Discovery*](notes/ghareeb2026robin.md) `ghareeb2026robin`

### `evaluation-of-ai-research`

- **2020** — Maynez & others. [*On Faithfulness and Factuality in Abstractive Summarization*](notes/maynez2020faithfulness.md) `maynez2020faithfulness`
- **2023** — Ji & others. [*Survey of Hallucination in Natural Language Generation*](notes/ji2023hallucination.md) `ji2023hallucination`
- **2023** — Lála et al.. [*PaperQA: Retrieval-Augmented Generative Agent for Scientific Research*](notes/lala2023paperqa.md) `lala2023paperqa` · skimmed
- **2024** — Asai et al.. [*OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs*](notes/asai2024openscholar.md) `asai2024openscholar` · skimmed
- **2024** — D'Arcy et al.. [*MARG: Multi-Agent Review Generation for Scientific Papers*](notes/darcy2024marg.md) `darcy2024marg` · skimmed
- **2024** — Jiang et al.. [*Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations*](notes/jiang2024costorm.md) `jiang2024costorm` · skimmed
- **2024** — Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/latona2024reviewlottery.md) `latona2024reviewlottery`
- **2024** — Liang et al.. [*Mapping the Increasing Use of LLMs in Scientific Papers*](notes/liang2024mapping.md) `liang2024mapping`
- **2024** — Liang et al.. [*Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*](notes/liang2024monitoring.md) `liang2024monitoring`
- **2024** — Lu et al.. [*The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*](notes/lu2024aiscientist.md) `lu2024aiscientist` · skimmed
- **2024** — Narayanan et al.. [*Aviary: training language agents on challenging scientific tasks*](notes/narayanan2024aviary.md) `narayanan2024aviary` · skimmed
- **2024** — Ngwenyama & Rowe. [*Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World*](notes/ngwenyama2024literature.md) `ngwenyama2024literature` · skimmed
- **2026** — Novy-Marx & Velikov. [*Artificial Intelligence--Powered (Finance) Scholarship*](notes/novymarx2026aifinance.md) `novymarx2026aifinance`
- **2024** — Shao et al.. [*Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models*](notes/shao2024storm.md) `shao2024storm` · skimmed
- **2024** — Skarlinski et al.. [*Language agents achieve superhuman synthesis of scientific knowledge*](notes/skarlinski2024paperqa2.md) `skarlinski2024paperqa2` · skimmed
- **2024** — Wang et al.. [*AutoSurvey: Large Language Models Can Automatically Write Surveys*](notes/wang2024autosurvey.md) `wang2024autosurvey` · skimmed
- **2024** — Watson et al.. [*Extending the Foresight of Phillip Ein-Dor: Causal Knowledge Analytics*](notes/watson2024causal.md) `watson2024causal` · skimmed
- **2024** — Yoo. [*Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI*](notes/yoo2024epistemic.md) `yoo2024epistemic` · skimmed
- **2025** — Agarwal et al.. [*AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise*](notes/agarwal2025autodiscovery.md) `agarwal2025autodiscovery` · skimmed
- **2025** — Bragg et al.. [*AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite*](notes/bragg2025astabench.md) `bragg2025astabench` · skimmed
- **2025** — Brodeur et al.. [*Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis*](notes/brodeur2025reproducibility.md) `brodeur2025reproducibility`
- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- **2025** — Gridach et al.. [*Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions*](notes/gridach2025agenticsurvey.md) `gridach2025agenticsurvey` · skimmed
- **2025** — Liang et al.. [*SurveyX: Academic Survey Automation via Large Language Models*](notes/liang2025surveyx.md) `liang2025surveyx` · skimmed
- **2025** — Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- **2025** — Mikalef et al.. [*Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research*](notes/mikalef2025responsible.md) `mikalef2025responsible`
- **2025** — Mitchener et al.. [*Kosmos: An AI Scientist for Autonomous Discovery*](notes/mitchener2025kosmos.md) `mitchener2025kosmos` · skimmed
- **2025** — Nathani et al.. [*MLGym: A New Framework and Benchmark for Advancing AI Research Agents*](notes/nathani2025mlgym.md) `nathani2025mlgym` · skimmed
- **2025** — Schmidgall et al.. [*Agent Laboratory: Using LLM Agents as Research Assistants*](notes/schmidgall2025agentlaboratory.md) `schmidgall2025agentlaboratory` · skimmed
- **2025** — Tie et al.. [*A Survey of AI Scientists*](notes/tie2025aiscientistsurvey.md) `tie2025aiscientistsurvey`
- **2025** — Yamada et al.. [*The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*](notes/yamada2025aiscientistv2.md) `yamada2025aiscientistv2` · skimmed
- **2025** — Yu et al.. [*ResearchTown: Simulator of Human Research Community*](notes/yu2025researchtown.md) `yu2025researchtown` · skimmed
- **2026** — Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`
- **2026** — Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`
- **2026** — Jin et al.. [*Toward Generalist Autonomous Research via Hypothesis-Tree Refinement*](notes/jin2026arbor.md) `jin2026arbor` · skimmed
- **2026** — Kohler et al.. [*Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results*](notes/kohler2026agenticreproduction.md) `kohler2026agenticreproduction` · skimmed
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`
- **2026** — Li et al.. [*ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues*](notes/li2026reprorepo.md) `li2026reprorepo` · skimmed
- **2026** — Liu et al.. [*AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration*](notes/liu2026autoresearchclaw.md) `liu2026autoresearchclaw` · skimmed
- **2026** — Lupidi et al.. [*AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents*](notes/lupidi2026airsbench.md) `lupidi2026airsbench` · skimmed
- **2026** — Wang et al.. [*Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle*](notes/wang2026aarribench.md) `wang2026aarribench` · skimmed
- **2026** — Wang et al.. [*NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?*](notes/wang2026naturebench.md) `wang2026naturebench` · skimmed

### `evaluation-rigor`

- **2024** — Goldberg et al.. [*Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers: NeurIPS'24 Experiment*](notes/neurips2024checklist.md) `neurips2024checklist`
- **2026** — Yang et al.. [*ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration*](notes/yang2026aris.md) `yang2026aris`

### `hallucination`

- **2020** — Maynez & others. [*On Faithfulness and Factuality in Abstractive Summarization*](notes/maynez2020faithfulness.md) `maynez2020faithfulness`
- **2023** — Ji & others. [*Survey of Hallucination in Natural Language Generation*](notes/ji2023hallucination.md) `ji2023hallucination`
- **2023** — Lála et al.. [*PaperQA: Retrieval-Augmented Generative Agent for Scientific Research*](notes/lala2023paperqa.md) `lala2023paperqa` · skimmed
- **2024** — Asai et al.. [*OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs*](notes/asai2024openscholar.md) `asai2024openscholar` · skimmed
- **2026** — Novy-Marx & Velikov. [*Artificial Intelligence--Powered (Finance) Scholarship*](notes/novymarx2026aifinance.md) `novymarx2026aifinance`
- **2024** — Shao et al.. [*Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models*](notes/shao2024storm.md) `shao2024storm` · skimmed
- **2024** — Skarlinski et al.. [*Language agents achieve superhuman synthesis of scientific knowledge*](notes/skarlinski2024paperqa2.md) `skarlinski2024paperqa2` · skimmed
- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Keuper. [*Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications*](notes/keuper2025promptinjection.md) `keuper2025promptinjection`
- **2025** — Liang et al.. [*SurveyX: Academic Survey Automation via Large Language Models*](notes/liang2025surveyx.md) `liang2025surveyx` · skimmed
- **2025** — Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- **2025** — Mitchener et al.. [*Kosmos: An AI Scientist for Autonomous Discovery*](notes/mitchener2025kosmos.md) `mitchener2025kosmos` · skimmed
- **2025** — Zheng et al.. [*DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments*](notes/zheng2025deepresearcher.md) `zheng2025deepresearcher` · skimmed
- **2025** — Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2025misleading.md) `collu2025misleading`
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`
- **2026** — Liu et al.. [*AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration*](notes/liu2026autoresearchclaw.md) `liu2026autoresearchclaw` · skimmed

### `harness-engineering`

- **2026** — Yang et al.. [*ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration*](notes/yang2026aris.md) `yang2026aris`

### `human-ai-research-collaboration`

- **2023** — Noy & Zhang. [*Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*](notes/noy2023experimental.md) `noy2023experimental`
- **2024** — Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- **2024** — Baek et al.. [*ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models*](notes/baek2024researchagent.md) `baek2024researchagent` · skimmed
- **2024** — Drori & Te'eni. [*Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks*](notes/drori2024humanloop.md) `drori2024humanloop` · skimmed
- **2024** — Jarvenpaa & Klein. [*New Frontiers in Information Systems Theorizing: Human-gAI Collaboration*](notes/jarvenpaa2024theorizing.md) `jarvenpaa2024theorizing` · skimmed
- **2024** — Jiang et al.. [*Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations*](notes/jiang2024costorm.md) `jiang2024costorm` · skimmed
- **2024** — Ngwenyama & Rowe. [*Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World*](notes/ngwenyama2024literature.md) `ngwenyama2024literature` · skimmed
- **2024** — Sarker et al.. [*Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review*](notes/sarker2024democratizing.md) `sarker2024democratizing` · skimmed
- **2024** — Schwartz & Te'eni. [*AI for Knowledge Creation, Curation, and Consumption in Context*](notes/schwartz2024kcc.md) `schwartz2024kcc`
- **2025** — Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- **2025** — Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- **2025** — Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- **2025** — Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- **2025** — Schmidgall et al.. [*Agent Laboratory: Using LLM Agents as Research Assistants*](notes/schmidgall2025agentlaboratory.md) `schmidgall2025agentlaboratory` · skimmed
- **2026** — Br\^\incoveanu et al.. [*Augmenting Systematic Literature Reviews: A Human-AI Collaborative Framework*](notes/brincoveanu2026augmenting.md) `brincoveanu2026augmenting`
- **2026** — Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`
- **2026** — Gottweis et al.. [*Accelerating scientific discovery with Co-Scientist*](notes/gottweis2026coscientist.md) `gottweis2026coscientist` · skimmed
- **2026** — Liu et al.. [*AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration*](notes/liu2026autoresearchclaw.md) `liu2026autoresearchclaw` · skimmed
- **2026** — Zheng et al.. [*AI co-mathematician: Accelerating mathematicians with agentic AI*](notes/zheng2026comathematician.md) `zheng2026comathematician` · skimmed

### `is-methodology`

- **2012** — Aral et al.. [*Information, Technology, and Information Worker Productivity*](notes/aral2012itproductivity.md) `aral2012itproductivity`
- **2019** — Sarker & others. [*The Sociotechnical Axis of Cohesion for the IS Discipline: Its Historical Legacy and Its Continued Relevance*](notes/sarker2019sociotechnical.md) `sarker2019sociotechnical`
- **2023** — Susarla et al.. [*The Janus Effect of Generative AI: Charting the Path for Responsible Conduct of Scholarly Activities in Information Systems*](notes/susarla2023janus.md) `susarla2023janus`
- **2024** — Alavi et al.. [*A Knowledge Management Perspective of Generative Artificial Intelligence*](notes/alavi2024kmperspective.md) `alavi2024kmperspective` · skimmed
- **2024** — Gregor. [*Responsible Artificial Intelligence and Journal Publishing*](notes/gregor2024responsible.md) `gregor2024responsible` · skimmed
- **2024** — Jarvenpaa & Klein. [*New Frontiers in Information Systems Theorizing: Human-gAI Collaboration*](notes/jarvenpaa2024theorizing.md) `jarvenpaa2024theorizing` · skimmed
- **2024** — Ngwenyama & Rowe. [*Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World*](notes/ngwenyama2024literature.md) `ngwenyama2024literature` · skimmed
- **2024** — Riemer & Peter. [*Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications*](notes/riemer2024styleengines.md) `riemer2024styleengines`
- **2024** — Sarker et al.. [*Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review*](notes/sarker2024democratizing.md) `sarker2024democratizing` · skimmed
- **2024** — Schwartz & Te'eni. [*AI for Knowledge Creation, Curation, and Consumption in Context*](notes/schwartz2024kcc.md) `schwartz2024kcc`
- **2024** — Shmueli & Ray. [*Reimagining the Journal Editorial Process: An AI-Augmented Versus an AI-Driven Future*](notes/shmueli2024editorial.md) `shmueli2024editorial` · skimmed
- **2024** — Watson et al.. [*Extending the Foresight of Phillip Ein-Dor: Causal Knowledge Analytics*](notes/watson2024causal.md) `watson2024causal` · skimmed
- **2024** — Yoo. [*Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI*](notes/yoo2024epistemic.md) `yoo2024epistemic` · skimmed
- **2025** — Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- **2025** — Mikalef et al.. [*Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research*](notes/mikalef2025responsible.md) `mikalef2025responsible`
- **2026** — Br\^\incoveanu et al.. [*Augmenting Systematic Literature Reviews: A Human-AI Collaborative Framework*](notes/brincoveanu2026augmenting.md) `brincoveanu2026augmenting`
- **2026** — Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- **2026** — Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`

### `llm-cognition`

- **2023** — Mitchell & Krakauer. [*The Debate over Understanding in AI's Large Language Models*](notes/mitchell2023understanding.md) `mitchell2023understanding`
- **2023** — Park & others. [*Generative Agents: Interactive Simulacra of Human Behavior*](notes/park2023generative.md) `park2023generative`
- **2024** — Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- **2025** — Peter et al.. [*The Benefits and Dangers of Anthropomorphic Conversational Agents*](notes/peter2025anthropomorphic.md) `peter2025anthropomorphic`
- **2026** — Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`

### `memory-systems`

- **2026** — Lyu et al.. [*EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery*](notes/evoscientist2026techreport.md) `evoscientist2026techreport`

### `multi-agent-systems`

- **2026** — Lyu et al.. [*EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery*](notes/evoscientist2026techreport.md) `evoscientist2026techreport`
- **2026** — Ghareeb et al.. [*A Multi-Agent System for Automating Scientific Discovery*](notes/ghareeb2026robin.md) `ghareeb2026robin`
- **2026** — Li et al.. [*Agentic AI and the Rise of in silico Team Science in Biomedical Research*](notes/li2026agenticbiomedical.md) `li2026agenticbiomedical`
- **2026** — Yang et al.. [*ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration*](notes/yang2026aris.md) `yang2026aris`

### `peer-review`

- **2024** — Lund et al.. [*The Impact of AI on Academic Research and Publishing*](notes/lund2024aiacademic.md) `lund2024aiacademic`
- **2024** — Goldberg et al.. [*Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers: NeurIPS'24 Experiment*](notes/neurips2024checklist.md) `neurips2024checklist`

### `reasoning-faithfulness`

- **2020** — Maynez & others. [*On Faithfulness and Factuality in Abstractive Summarization*](notes/maynez2020faithfulness.md) `maynez2020faithfulness`
- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`

### `replication-infrastructure`

- **2025** — Brodeur et al.. [*Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis*](notes/brodeur2025reproducibility.md) `brodeur2025reproducibility`
- **2025** — Seo et al.. [*Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning*](notes/seo2025paper2code.md) `seo2025paper2code` · skimmed
- **2026** — Kohler et al.. [*Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results*](notes/kohler2026agenticreproduction.md) `kohler2026agenticreproduction` · skimmed
- **2026** — Li et al.. [*ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues*](notes/li2026reprorepo.md) `li2026reprorepo` · skimmed
- **2026** — Wang et al.. [*NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?*](notes/wang2026naturebench.md) `wang2026naturebench` · skimmed

### `research-ethics`

- **2024** — Lund et al.. [*The Impact of AI on Academic Research and Publishing*](notes/lund2024aiacademic.md) `lund2024aiacademic`

### `research-productivity`

- **2012** — Aral et al.. [*Information, Technology, and Information Worker Productivity*](notes/aral2012itproductivity.md) `aral2012itproductivity`
- **2023** — Noy & Zhang. [*Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*](notes/noy2023experimental.md) `noy2023experimental`
- **2024** — Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- **2024** — Benbya et al.. [*Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work*](notes/benbya2024navigating.md) `benbya2024navigating` · skimmed
- **2024** — Liang et al.. [*Mapping the Increasing Use of LLMs in Scientific Papers*](notes/liang2024mapping.md) `liang2024mapping`
- **2026** — Novy-Marx & Velikov. [*Artificial Intelligence--Powered (Finance) Scholarship*](notes/novymarx2026aifinance.md) `novymarx2026aifinance`
- **2025** — Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- **2026** — Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2026rapidadoption.md) `bick2026rapidadoption`
- **2025** — Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- **2025** — Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- **2025** — Kwon & Yang. [*Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality*](notes/kwon2025inequality.md) `kwon2025inequality` · skimmed
- **2025** — Mitchener et al.. [*Kosmos: An AI Scientist for Autonomous Discovery*](notes/mitchener2025kosmos.md) `mitchener2025kosmos` · skimmed
- **2026** — Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`
- **2026** — Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`

### `self-improvement`

- **2026** — Lyu et al.. [*EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery*](notes/evoscientist2026techreport.md) `evoscientist2026techreport`

### `sociotechnical`

- **2012** — Aral et al.. [*Information, Technology, and Information Worker Productivity*](notes/aral2012itproductivity.md) `aral2012itproductivity`
- **2019** — Sarker & others. [*The Sociotechnical Axis of Cohesion for the IS Discipline: Its Historical Legacy and Its Continued Relevance*](notes/sarker2019sociotechnical.md) `sarker2019sociotechnical`
- **2023** — Mitchell & Krakauer. [*The Debate over Understanding in AI's Large Language Models*](notes/mitchell2023understanding.md) `mitchell2023understanding`
- **2023** — Park & others. [*Generative Agents: Interactive Simulacra of Human Behavior*](notes/park2023generative.md) `park2023generative`
- **2023** — Susarla et al.. [*The Janus Effect of Generative AI: Charting the Path for Responsible Conduct of Scholarly Activities in Information Systems*](notes/susarla2023janus.md) `susarla2023janus`
- **2024** — Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- **2024** — Alavi et al.. [*A Knowledge Management Perspective of Generative Artificial Intelligence*](notes/alavi2024kmperspective.md) `alavi2024kmperspective` · skimmed
- **2024** — Avital. [*Digital Transformation of Academic Publishing: A Call for the Decentralization and Democratization of Academic Journals*](notes/avital2024decentralization.md) `avital2024decentralization` · skimmed
- **2024** — Benbya et al.. [*Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work*](notes/benbya2024navigating.md) `benbya2024navigating` · skimmed
- **2024** — Gregor. [*Responsible Artificial Intelligence and Journal Publishing*](notes/gregor2024responsible.md) `gregor2024responsible` · skimmed
- **2024** — Kankanhalli. [*Peer Review in the Age of Generative AI*](notes/kankanhalli2024peerreview.md) `kankanhalli2024peerreview` · skimmed
- **2024** — Liang et al.. [*Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*](notes/liang2024monitoring.md) `liang2024monitoring`
- **2024** — Riemer & Peter. [*Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications*](notes/riemer2024styleengines.md) `riemer2024styleengines`
- **2024** — Sabherwal & Grover. [*The Societal Impacts of Generative Artificial Intelligence: A Balanced Perspective*](notes/sabherwal2024societal.md) `sabherwal2024societal` · skimmed
- **2024** — Weber. [*The Other Reviewer: RoboReviewer*](notes/weber2024roboreviewer.md) `weber2024roboreviewer` · skimmed
- **2024** — Yoo. [*Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI*](notes/yoo2024epistemic.md) `yoo2024epistemic` · skimmed
- **2026** — Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2026rapidadoption.md) `bick2026rapidadoption`
- **2025** — Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- **2025** — Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- **2025** — Kwon & Yang. [*Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality*](notes/kwon2025inequality.md) `kwon2025inequality` · skimmed
- **2025** — Mikalef et al.. [*Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research*](notes/mikalef2025responsible.md) `mikalef2025responsible`
- **2025** — Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- **2025** — Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- **2025** — Peter et al.. [*The Benefits and Dangers of Anthropomorphic Conversational Agents*](notes/peter2025anthropomorphic.md) `peter2025anthropomorphic`
- **2025** — Yu et al.. [*ResearchTown: Simulator of Human Research Community*](notes/yu2025researchtown.md) `yu2025researchtown` · skimmed
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2026** — Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`
- **2025** — Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2025misleading.md) `collu2025misleading`
- **2026** — Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- **2026** — Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`
- **2026** — Li et al.. [*Agentic AI and the Rise of in silico Team Science in Biomedical Research*](notes/li2026agenticbiomedical.md) `li2026agenticbiomedical`
- **2026** — Ngwenyama et al.. [*Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor*](notes/ngwenyama2026platform.md) `ngwenyama2026platform`

### `style-engines`

- **2024** — Riemer & Peter. [*Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications*](notes/riemer2024styleengines.md) `riemer2024styleengines`

### `traceability-verifiability`

- **2025** — Ifargan et al.. [*Autonomous LLM-Driven Research --- from Data to Human-Verifiable Research Papers*](notes/ifargan2024datatopaper.md) `ifargan2024datatopaper`

<!-- AUTO-GENERATED:papers-by-theme-end -->

??? note "Browse by year"

    <!-- AUTO-GENERATED:papers-by-year-start -->
*96/96 notes have been filled with abstract-grounded summaries; 0 remain as stubs marked ⚠️ (front-matter verified, but Summary / Contribution / Method / Critique not yet written).*

### 2026

- Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`
- Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2026rapidadoption.md) `bick2026rapidadoption`
- Br\^\incoveanu et al.. [*Augmenting Systematic Literature Reviews: A Human-AI Collaborative Framework*](notes/brincoveanu2026augmenting.md) `brincoveanu2026augmenting`
- Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`
- Lyu et al.. [*EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery*](notes/evoscientist2026techreport.md) `evoscientist2026techreport`
- Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`
- Ghareeb et al.. [*A Multi-Agent System for Automating Scientific Discovery*](notes/ghareeb2026robin.md) `ghareeb2026robin`
- Gottweis et al.. [*Accelerating scientific discovery with Co-Scientist*](notes/gottweis2026coscientist.md) `gottweis2026coscientist` · skimmed
- Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- Jin et al.. [*Toward Generalist Autonomous Research via Hypothesis-Tree Refinement*](notes/jin2026arbor.md) `jin2026arbor` · skimmed
- Kohler et al.. [*Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results*](notes/kohler2026agenticreproduction.md) `kohler2026agenticreproduction` · skimmed
- Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`
- Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`
- Li et al.. [*Agentic AI and the Rise of in silico Team Science in Biomedical Research*](notes/li2026agenticbiomedical.md) `li2026agenticbiomedical`
- Li et al.. [*ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues*](notes/li2026reprorepo.md) `li2026reprorepo` · skimmed
- Liu et al.. [*AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration*](notes/liu2026autoresearchclaw.md) `liu2026autoresearchclaw` · skimmed
- Lupidi et al.. [*AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents*](notes/lupidi2026airsbench.md) `lupidi2026airsbench` · skimmed
- Ngwenyama et al.. [*Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor*](notes/ngwenyama2026platform.md) `ngwenyama2026platform`
- Novy-Marx & Velikov. [*Artificial Intelligence--Powered (Finance) Scholarship*](notes/novymarx2026aifinance.md) `novymarx2026aifinance`
- Qu et al.. [*CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery*](notes/qu2026coral.md) `qu2026coral` · skimmed
- Wang et al.. [*Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle*](notes/wang2026aarribench.md) `wang2026aarribench` · skimmed
- Wang et al.. [*NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?*](notes/wang2026naturebench.md) `wang2026naturebench` · skimmed
- Yang et al.. [*ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration*](notes/yang2026aris.md) `yang2026aris`
- Zheng et al.. [*AI co-mathematician: Accelerating mathematicians with agentic AI*](notes/zheng2026comathematician.md) `zheng2026comathematician` · skimmed

### 2025

- Agarwal et al.. [*AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise*](notes/agarwal2025autodiscovery.md) `agarwal2025autodiscovery` · skimmed
- Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- Bragg et al.. [*AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite*](notes/bragg2025astabench.md) `bragg2025astabench` · skimmed
- Brodeur et al.. [*Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis*](notes/brodeur2025reproducibility.md) `brodeur2025reproducibility`
- Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2025misleading.md) `collu2025misleading`
- Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- Gao et al.. [*ToolUniverse: An open platform for democratizing AI scientists*](notes/gao2025tooluniverse.md) `gao2025tooluniverse` · skimmed
- Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- Gridach et al.. [*Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions*](notes/gridach2025agenticsurvey.md) `gridach2025agenticsurvey` · skimmed
- Ifargan et al.. [*Autonomous LLM-Driven Research --- from Data to Human-Verifiable Research Papers*](notes/ifargan2024datatopaper.md) `ifargan2024datatopaper`
- Keuper. [*Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications*](notes/keuper2025promptinjection.md) `keuper2025promptinjection`
- Kwon & Yang. [*Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality*](notes/kwon2025inequality.md) `kwon2025inequality` · skimmed
- Liang et al.. [*SurveyX: Academic Survey Automation via Large Language Models*](notes/liang2025surveyx.md) `liang2025surveyx` · skimmed
- Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- Mikalef et al.. [*Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research*](notes/mikalef2025responsible.md) `mikalef2025responsible`
- Mitchener et al.. [*Kosmos: An AI Scientist for Autonomous Discovery*](notes/mitchener2025kosmos.md) `mitchener2025kosmos` · skimmed
- Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- Nathani et al.. [*MLGym: A New Framework and Benchmark for Advancing AI Research Agents*](notes/nathani2025mlgym.md) `nathani2025mlgym` · skimmed
- Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- Peter et al.. [*The Benefits and Dangers of Anthropomorphic Conversational Agents*](notes/peter2025anthropomorphic.md) `peter2025anthropomorphic`
- Schmidgall et al.. [*Agent Laboratory: Using LLM Agents as Research Assistants*](notes/schmidgall2025agentlaboratory.md) `schmidgall2025agentlaboratory` · skimmed
- Seo et al.. [*Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning*](notes/seo2025paper2code.md) `seo2025paper2code` · skimmed
- Tie et al.. [*A Survey of AI Scientists*](notes/tie2025aiscientistsurvey.md) `tie2025aiscientistsurvey`
- Team. [*Tongyi DeepResearch Technical Report*](notes/tongyi2025deepresearch.md) `tongyi2025deepresearch` · skimmed
- Wu & others. [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Yamada et al.. [*The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search*](notes/yamada2025aiscientistv2.md) `yamada2025aiscientistv2` · skimmed
- Yu et al.. [*ResearchTown: Simulator of Human Research Community*](notes/yu2025researchtown.md) `yu2025researchtown` · skimmed
- Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- Zheng et al.. [*DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments*](notes/zheng2025deepresearcher.md) `zheng2025deepresearcher` · skimmed

### 2024

- Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- Alavi et al.. [*A Knowledge Management Perspective of Generative Artificial Intelligence*](notes/alavi2024kmperspective.md) `alavi2024kmperspective` · skimmed
- Asai et al.. [*OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs*](notes/asai2024openscholar.md) `asai2024openscholar` · skimmed
- Avital. [*Digital Transformation of Academic Publishing: A Call for the Decentralization and Democratization of Academic Journals*](notes/avital2024decentralization.md) `avital2024decentralization` · skimmed
- Baek et al.. [*ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models*](notes/baek2024researchagent.md) `baek2024researchagent` · skimmed
- Benbya et al.. [*Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work*](notes/benbya2024navigating.md) `benbya2024navigating` · skimmed
- D'Arcy et al.. [*MARG: Multi-Agent Review Generation for Scientific Papers*](notes/darcy2024marg.md) `darcy2024marg` · skimmed
- Drori & Te'eni. [*Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks*](notes/drori2024humanloop.md) `drori2024humanloop` · skimmed
- Gregor. [*Responsible Artificial Intelligence and Journal Publishing*](notes/gregor2024responsible.md) `gregor2024responsible` · skimmed
- Jarvenpaa & Klein. [*New Frontiers in Information Systems Theorizing: Human-gAI Collaboration*](notes/jarvenpaa2024theorizing.md) `jarvenpaa2024theorizing` · skimmed
- Jiang et al.. [*Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations*](notes/jiang2024costorm.md) `jiang2024costorm` · skimmed
- Kankanhalli. [*Peer Review in the Age of Generative AI*](notes/kankanhalli2024peerreview.md) `kankanhalli2024peerreview` · skimmed
- Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/latona2024reviewlottery.md) `latona2024reviewlottery`
- Liang et al.. [*Mapping the Increasing Use of LLMs in Scientific Papers*](notes/liang2024mapping.md) `liang2024mapping`
- Liang et al.. [*Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*](notes/liang2024monitoring.md) `liang2024monitoring`
- Lu et al.. [*The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery*](notes/lu2024aiscientist.md) `lu2024aiscientist` · skimmed
- Lund et al.. [*The Impact of AI on Academic Research and Publishing*](notes/lund2024aiacademic.md) `lund2024aiacademic`
- Narayanan et al.. [*Aviary: training language agents on challenging scientific tasks*](notes/narayanan2024aviary.md) `narayanan2024aviary` · skimmed
- Goldberg et al.. [*Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers: NeurIPS'24 Experiment*](notes/neurips2024checklist.md) `neurips2024checklist`
- Ngwenyama & Rowe. [*Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World*](notes/ngwenyama2024literature.md) `ngwenyama2024literature` · skimmed
- Riemer & Peter. [*Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications*](notes/riemer2024styleengines.md) `riemer2024styleengines`
- Sabherwal & Grover. [*The Societal Impacts of Generative Artificial Intelligence: A Balanced Perspective*](notes/sabherwal2024societal.md) `sabherwal2024societal` · skimmed
- Sarker et al.. [*Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review*](notes/sarker2024democratizing.md) `sarker2024democratizing` · skimmed
- Schwartz & Te'eni. [*AI for Knowledge Creation, Curation, and Consumption in Context*](notes/schwartz2024kcc.md) `schwartz2024kcc`
- Shao et al.. [*Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models*](notes/shao2024storm.md) `shao2024storm` · skimmed
- Shmueli & Ray. [*Reimagining the Journal Editorial Process: An AI-Augmented Versus an AI-Driven Future*](notes/shmueli2024editorial.md) `shmueli2024editorial` · skimmed
- Skarlinski et al.. [*Language agents achieve superhuman synthesis of scientific knowledge*](notes/skarlinski2024paperqa2.md) `skarlinski2024paperqa2` · skimmed
- Wang et al.. [*AutoSurvey: Large Language Models Can Automatically Write Surveys*](notes/wang2024autosurvey.md) `wang2024autosurvey` · skimmed
- Watson et al.. [*Extending the Foresight of Phillip Ein-Dor: Causal Knowledge Analytics*](notes/watson2024causal.md) `watson2024causal` · skimmed
- Weber. [*The Other Reviewer: RoboReviewer*](notes/weber2024roboreviewer.md) `weber2024roboreviewer` · skimmed
- Yoo. [*Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI*](notes/yoo2024epistemic.md) `yoo2024epistemic` · skimmed

### 2023

- Ji & others. [*Survey of Hallucination in Natural Language Generation*](notes/ji2023hallucination.md) `ji2023hallucination`
- Lála et al.. [*PaperQA: Retrieval-Augmented Generative Agent for Scientific Research*](notes/lala2023paperqa.md) `lala2023paperqa` · skimmed
- Mitchell & Krakauer. [*The Debate over Understanding in AI's Large Language Models*](notes/mitchell2023understanding.md) `mitchell2023understanding`
- Noy & Zhang. [*Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*](notes/noy2023experimental.md) `noy2023experimental`
- Park & others. [*Generative Agents: Interactive Simulacra of Human Behavior*](notes/park2023generative.md) `park2023generative`
- Schick & others. [*Toolformer: Language Models Can Teach Themselves to Use Tools*](notes/schick2023toolformer.md) `schick2023toolformer`
- Susarla et al.. [*The Janus Effect of Generative AI: Charting the Path for Responsible Conduct of Scholarly Activities in Information Systems*](notes/susarla2023janus.md) `susarla2023janus`

### 2020

- Maynez & others. [*On Faithfulness and Factuality in Abstractive Summarization*](notes/maynez2020faithfulness.md) `maynez2020faithfulness`

### 2019

- Sarker & others. [*The Sociotechnical Axis of Cohesion for the IS Discipline: Its Historical Legacy and Its Continued Relevance*](notes/sarker2019sociotechnical.md) `sarker2019sociotechnical`

### 2012

- Aral et al.. [*Information, Technology, and Information Worker Productivity*](notes/aral2012itproductivity.md) `aral2012itproductivity`

<!-- AUTO-GENERATED:papers-by-year-end -->

## How to add a paper

1. Add the BibTeX entry to `papers/references.bib` with a citekey of the form
   `lastnameYEARword` (lowercase, no punctuation).
2. Create `docs/papers/notes/<citekey>.md` from the schema template at
   [`papers/schema.md`](https://github.com/bhanneke/RISE/blob/main/papers/schema.md).
3. Fill in the structured summary sections.
4. Open a pull request.
