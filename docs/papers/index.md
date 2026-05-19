# Papers catalog

> Regenerated from `papers/references.bib` (the **single source of truth** for
> citations) plus `docs/papers/notes/*.md` (curator analysis + status) by
> `scripts/build_indexes.py`. Do not edit by hand.

Each entry's *citation data* (title, authors, year, venue, DOI/arXiv) comes
from [`papers/references.bib`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib);
*themes and analysis* come from per-paper structured notes in
[`docs/papers/notes/`](https://github.com/bhanneke/RISE/tree/main/docs/papers/notes).

<!-- AUTO-GENERATED:papers-table-start -->
*65 bibliographic entries; 56 have curator notes (40 fully read).*

<input type="text" id="paperFilter" placeholder="🔍 filter by author / title / venue / theme / year / citekey…"
  style="width:100%; padding:0.5em; margin:1em 0; font-size:1em; border:1px solid #ccc; border-radius:4px;"
  oninput="filterPapers(this.value)">

<script>
function filterPapers(q) {
  q = q.toLowerCase().trim();
  document.querySelectorAll('#papersTable tbody tr').forEach(function(row) {
    row.style.display = (!q || row.textContent.toLowerCase().includes(q)) ? '' : 'none';
  });
}
</script>

<table id="papersTable" markdown>
<thead>
<tr><th>Year</th><th>Authors</th><th>Title</th><th>Venue</th><th>Link</th><th>Themes</th><th>Citekey</th><th>Note</th></tr>
</thead>
<tbody markdown>
<tr><td>2012</td><td>Aral et al.</td><td><a href="notes/aral2012itproductivity/">Information, Technology, and Information Worker Productivity</a></td><td>Information Systems Research</td><td><a href="https://doi.org/10.1287/isre.1110.0408">doi</a></td><td><code>research-productivity</code> <code>is-methodology</code> <code>sociotechnical</code></td><td><code>aral2012itproductivity</code></td><td>read</td></tr>
<tr><td>2019</td><td>Sarker & others</td><td><a href="notes/sarker2019sociotechnical/">The Sociotechnical Axis of Cohesion for the IS Discipline: Its Historical Legacy and Its Continued Relevance</a></td><td>MIS Quarterly</td><td>—</td><td><code>sociotechnical</code> <code>is-methodology</code></td><td><code>sarker2019sociotechnical</code></td><td>read</td></tr>
<tr><td>2020</td><td>Maynez & others</td><td><a href="notes/maynez2020faithfulness/">On Faithfulness and Factuality in Abstractive Summarization</a></td><td>Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics</td><td>—</td><td><code>hallucination</code> <code>reasoning-faithfulness</code> <code>evaluation-of-ai-research</code></td><td><code>maynez2020faithfulness</code></td><td>read</td></tr>
<tr><td>2023</td><td>Ji & others</td><td><a href="notes/ji2023hallucination/">Survey of Hallucination in Natural Language Generation</a></td><td>ACM Computing Surveys</td><td>—</td><td><code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>ji2023hallucination</code></td><td>read</td></tr>
<tr><td>2023</td><td>Mitchell & Krakauer</td><td><a href="notes/mitchell2023understanding/">The Debate over Understanding in AI's Large Language Models</a></td><td>Proceedings of the National Academy of Sciences</td><td>—</td><td><code>llm-cognition</code> <code>sociotechnical</code></td><td><code>mitchell2023understanding</code></td><td>read</td></tr>
<tr><td>2023</td><td>Noy & Zhang</td><td><a href="notes/noy2023experimental/">Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence</a></td><td>Science</td><td><a href="https://doi.org/10.1126/science.adh2586">doi</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code></td><td><code>noy2023experimental</code></td><td>read</td></tr>
<tr><td>2023</td><td>Park & others</td><td><a href="notes/park2023generative/">Generative Agents: Interactive Simulacra of Human Behavior</a></td><td>Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology</td><td>—</td><td><code>autonomous-research-agents</code> <code>sociotechnical</code> <code>llm-cognition</code></td><td><code>park2023generative</code></td><td>read</td></tr>
<tr><td>2023</td><td>Schick & others</td><td><a href="notes/schick2023toolformer/">Toolformer: Language Models Can Teach Themselves to Use Tools</a></td><td>Advances in Neural Information Processing Systems</td><td>—</td><td><code>agentic-tool-use</code></td><td><code>schick2023toolformer</code></td><td>read</td></tr>
<tr><td>2023</td><td>Susarla et al.</td><td><a href="notes/susarla2023janus/">The Janus Effect of Generative AI: Charting the Path for Responsible Conduct of Scholarly Activities in Information Systems</a></td><td>Information Systems Research</td><td><a href="https://doi.org/10.1287/isre.2023.ed.v34.n2">doi</a></td><td><code>is-methodology</code> <code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>susarla2023janus</code></td><td>read</td></tr>
<tr><td>2024</td><td>?</td><td>Agentic Research and AI-Assisted Peer Review Experiments</td><td>arXiv</td><td><a href="https://arxiv.org/abs/2406.06009">arXiv</a></td><td></td><td><code>anon2024agenticpeer</code></td><td>—</td></tr>
<tr><td>2024</td><td>?</td><td>Results of the NeurIPS 2024 Experiment on the Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers</td><td>NeurIPS Blog</td><td><a href="https://blog.neurips.cc/2024/12/10/results-of-the-neurips-2024-experiment-on-the-usefulness-of-llms-as-an-author-checklist-assistant-for-scientific-papers/">link</a></td><td></td><td><code>neurips2024checklist</code></td><td>—</td></tr>
<tr><td>2024</td><td>Agrawal et al.</td><td><a href="notes/agrawal2024aiscience/">AI in Science</a></td><td>National Bureau of Economic Research</td><td><a href="https://www.nber.org/papers/w34953">link</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>llm-cognition</code> <code>sociotechnical</code></td><td><code>agrawal2024aiscience</code></td><td>read</td></tr>
<tr><td>2024</td><td>Alavi et al.</td><td><a href="notes/alavi2024kmperspective/">A Knowledge Management Perspective of Generative Artificial Intelligence</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00859">doi</a></td><td><code>sociotechnical</code> <code>is-methodology</code></td><td><code>alavi2024kmperspective</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Avital</td><td><a href="notes/avital2024decentralization/">Digital Transformation of Academic Publishing: A Call for the Decentralization and Democratization of Academic Journals</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00873">doi</a></td><td><code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>avital2024decentralization</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Benbya et al.</td><td><a href="notes/benbya2024navigating/">Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00861">doi</a></td><td><code>sociotechnical</code> <code>research-productivity</code></td><td><code>benbya2024navigating</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Drori & Te'eni</td><td><a href="notes/drori2024humanloop/">Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00867">doi</a></td><td><code>ai-peer-review</code> <code>human-ai-research-collaboration</code></td><td><code>drori2024humanloop</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Gregor</td><td><a href="notes/gregor2024responsible/">Responsible Artificial Intelligence and Journal Publishing</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00863">doi</a></td><td><code>ai-peer-review</code> <code>sociotechnical</code> <code>is-methodology</code></td><td><code>gregor2024responsible</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Ifargan et al.</td><td>Autonomous LLM-Driven Research --- from Data to Human-Verifiable Research Papers</td><td>NEJM AI</td><td><a href="https://doi.org/10.1056/AIoa2400555">doi</a></td><td></td><td><code>ifargan2024datatopaper</code></td><td>—</td></tr>
<tr><td>2024</td><td>Ifargan et al.</td><td>Autonomous LLM-driven research from data to human-verifiable research papers</td><td>arXiv</td><td><a href="https://arxiv.org/abs/2404.17605">arXiv</a></td><td></td><td><code>ifargan2024datatopaperarxiv</code></td><td>—</td></tr>
<tr><td>2024</td><td>Jarvenpaa & Klein</td><td><a href="notes/jarvenpaa2024theorizing/">New Frontiers in Information Systems Theorizing: Human-gAI Collaboration</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00868">doi</a></td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code></td><td><code>jarvenpaa2024theorizing</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Kankanhalli</td><td><a href="notes/kankanhalli2024peerreview/">Peer Review in the Age of Generative AI</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00865">doi</a></td><td><code>ai-peer-review</code> <code>sociotechnical</code></td><td><code>kankanhalli2024peerreview</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Liang et al.</td><td><a href="notes/liang2024mapping/">Mapping the Increasing Use of LLMs in Scientific Papers</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2404.01268">arXiv</a></td><td><code>research-productivity</code> <code>evaluation-of-ai-research</code></td><td><code>liang2024mapping</code></td><td>read</td></tr>
<tr><td>2024</td><td>Liang et al.</td><td><a href="notes/liang2024monitoring/">Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2403.07183">arXiv</a></td><td><code>ai-peer-review</code> <code>evaluation-of-ai-research</code> <code>sociotechnical</code></td><td><code>liang2024monitoring</code></td><td>read</td></tr>
<tr><td>2024</td><td>Ngwenyama & Rowe</td><td><a href="notes/ngwenyama2024literature/">Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00869">doi</a></td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code> <code>evaluation-of-ai-research</code></td><td><code>ngwenyama2024literature</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Novy-Marx & Velikov</td><td><a href="notes/novymarx2024aifinance/">AI-Powered (Finance) Scholarship</a></td><td>National Bureau of Economic Research</td><td><a href="https://www.nber.org/papers/w33363">link</a></td><td><code>autonomous-research-agents</code> <code>research-productivity</code> <code>evaluation-of-ai-research</code> <code>hallucination</code></td><td><code>novymarx2024aifinance</code></td><td>read</td></tr>
<tr><td>2024</td><td>Riemer & Peter</td><td><a href="notes/riemer2024styleengines/">Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications</a></td><td>International Journal of Information Management</td><td>—</td><td><code>style-engines</code> <code>is-methodology</code> <code>sociotechnical</code></td><td><code>riemer2024styleengines</code></td><td>read</td></tr>
<tr><td>2024</td><td>Russo Latona et al.</td><td><a href="notes/russo2024reviewlottery/">The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2405.02150">arXiv</a></td><td><code>ai-peer-review</code> <code>evaluation-of-ai-research</code> <code>ai-publishing-ecosystems</code></td><td><code>russo2024reviewlottery</code></td><td>read</td></tr>
<tr><td>2024</td><td>Sabherwal & Grover</td><td><a href="notes/sabherwal2024societal/">The Societal Impacts of Generative Artificial Intelligence: A Balanced Perspective</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00860">doi</a></td><td><code>sociotechnical</code></td><td><code>sabherwal2024societal</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Sarker et al.</td><td><a href="notes/sarker2024democratizing/">Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00872">doi</a></td><td><code>ai-peer-review</code> <code>is-methodology</code> <code>human-ai-research-collaboration</code></td><td><code>sarker2024democratizing</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Schwartz & Te'eni</td><td><a href="notes/schwartz2024kcc/">AI for Knowledge Creation, Curation, and Consumption in Context</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00862">doi</a></td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code> <code>ai-publishing-ecosystems</code></td><td><code>schwartz2024kcc</code></td><td>read</td></tr>
<tr><td>2024</td><td>Shmueli & Ray</td><td><a href="notes/shmueli2024editorial/">Reimagining the Journal Editorial Process: An AI-Augmented Versus an AI-Driven Future</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00864">doi</a></td><td><code>ai-peer-review</code> <code>is-methodology</code></td><td><code>shmueli2024editorial</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Watson et al.</td><td><a href="notes/watson2024causal/">Extending the Foresight of Phillip Ein-Dor: Causal Knowledge Analytics</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00871">doi</a></td><td><code>is-methodology</code> <code>evaluation-of-ai-research</code></td><td><code>watson2024causal</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Weber</td><td><a href="notes/weber2024roboreviewer/">The Other Reviewer: RoboReviewer</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00866">doi</a></td><td><code>ai-peer-review</code> <code>sociotechnical</code></td><td><code>weber2024roboreviewer</code></td><td>skimmed</td></tr>
<tr><td>2024</td><td>Yoo</td><td><a href="notes/yoo2024epistemic/">Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI</a></td><td>Journal of the Association for Information Systems</td><td><a href="https://doi.org/10.17705/1jais.00870">doi</a></td><td><code>is-methodology</code> <code>sociotechnical</code> <code>evaluation-of-ai-research</code></td><td><code>yoo2024epistemic</code></td><td>skimmed</td></tr>
<tr><td>2025</td><td>Bapna et al.</td><td><a href="notes/bapna2025analytics/">Agentic AI and Managers' Analytics Capabilities: An Exploration</a></td><td>SSRN Working Paper</td><td><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5293722">link</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>agentic-tool-use</code></td><td><code>bapna2025analytics</code></td><td>read</td></tr>
<tr><td>2025</td><td>Bick et al.</td><td><a href="notes/bick2025rapidadoption/">The Rapid Adoption of Generative AI</a></td><td>Management Science</td><td><a href="https://doi.org/10.1287/mnsc.2025.02523">doi</a></td><td><code>research-productivity</code> <code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>bick2025rapidadoption</code></td><td>read</td></tr>
<tr><td>2025</td><td>Brodeur et al.</td><td><a href="notes/brodeur2025reproducibility/">Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis</a></td><td>National Bureau of Economic Research</td><td><a href="https://www.nber.org/papers/w33753">link</a></td><td><code>replication-infrastructure</code> <code>evaluation-of-ai-research</code></td><td><code>brodeur2025reproducibility</code></td><td>read</td></tr>
<tr><td>2025</td><td>Brynjolfsson et al.</td><td><a href="notes/brynjolfsson2025genaiwork/">Generative AI at Work</a></td><td>Quarterly Journal of Economics</td><td><a href="https://doi.org/10.1093/qje/qjae044">doi</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>sociotechnical</code></td><td><code>brynjolfsson2025genaiwork</code></td><td>read</td></tr>
<tr><td>2025</td><td>Chen & others</td><td><a href="notes/chen2025reasoning/">Reasoning Models Don't Always Say What They Think</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2505.05410">arXiv</a></td><td><code>reasoning-faithfulness</code> <code>agentic-reasoning</code> <code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>chen2025reasoning</code></td><td>read</td></tr>
<tr><td>2025</td><td>Cunningham</td><td>Claude Code for Causal Inference</td><td>Causal Inference Substack</td><td><a href="https://causalinf.substack.com/s/claude-code">link</a></td><td></td><td><code>cunningham2025claudecode</code></td><td>—</td></tr>
<tr><td>2025</td><td>Eberhardt</td><td>Claude Code for Applied Economists</td><td>Markus Academy Substack</td><td><a href="https://markusacademy.substack.com/p/claude-code-for-applied-economists">link</a></td><td></td><td><code>eberhardt2025claudecode</code></td><td>—</td></tr>
<tr><td>2025</td><td>Editorial</td><td><a href="notes/naturePeerReview2025editorial/">Transparent Peer Review to Be Extended to All Research Papers</a></td><td>Nature Editorial, d41586-025-01880-9</td><td><a href="https://www.nature.com/articles/d41586-025-01880-9">link</a></td><td><code>ai-peer-review</code> <code>ai-publishing-ecosystems</code> <code>sociotechnical</code></td><td><code>naturePeerReview2025editorial</code></td><td>read</td></tr>
<tr><td>2025</td><td>Filimonovic et al.</td><td><a href="notes/filimonovic2025genai/">Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2510.02408">arXiv</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>evaluation-of-ai-research</code></td><td><code>filimonovic2025genai</code></td><td>read</td></tr>
<tr><td>2025</td><td>Gopal & others</td><td><a href="notes/gopal2025inventing/">Inventing with Machines: Generative AI and the Evolving Landscape of IS Research</a></td><td>Information Systems Research</td><td>—</td><td><code>is-methodology</code> <code>human-ai-research-collaboration</code> <code>autonomous-research-agents</code> <code>sociotechnical</code></td><td><code>gopal2025inventing</code></td><td>read</td></tr>
<tr><td>2025</td><td>Gridach et al.</td><td><a href="notes/gridach2025agenticsurvey/">Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2503.08979">arXiv</a></td><td><code>autonomous-research-agents</code> <code>evaluation-of-ai-research</code></td><td><code>gridach2025agenticsurvey</code></td><td>skimmed</td></tr>
<tr><td>2025</td><td>Keuper</td><td><a href="notes/keuper2025promptinjection/">Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2509.10248">arXiv</a></td><td><code>ai-peer-review</code> <code>hallucination</code></td><td><code>keuper2025promptinjection</code></td><td>read</td></tr>
<tr><td>2025</td><td>Kwon & Yang</td><td><a href="notes/kwon2025inequality/">Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality</a></td><td>Proceedings of the International Conference on Information Systems (ICIS)</td><td><a href="https://aisel.aisnet.org/icis2025/gen_ai/gen_ai/2">link</a></td><td><code>research-productivity</code> <code>sociotechnical</code></td><td><code>kwon2025inequality</code></td><td>skimmed</td></tr>
<tr><td>2025</td><td>Matton & others</td><td><a href="notes/matton2025walkthetalk/">Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations</a></td><td>International Conference on Learning Representations (ICLR)</td><td>—</td><td><code>reasoning-faithfulness</code> <code>hallucination</code> <code>evaluation-of-ai-research</code></td><td><code>matton2025walkthetalk</code></td><td>read</td></tr>
<tr><td>2025</td><td>Mikalef et al.</td><td><a href="notes/mikalef2025responsible/">Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research</a></td><td>European Journal of Information Systems</td><td><a href="https://doi.org/10.1080/0960085X.2025.2506875">doi</a></td><td><code>sociotechnical</code> <code>is-methodology</code> <code>evaluation-of-ai-research</code></td><td><code>mikalef2025responsible</code></td><td>read</td></tr>
<tr><td>2025</td><td>Naddaf</td><td><a href="notes/naddaf2025aipeer/">AI Is Transforming Peer Review --- and Many Scientists Are Worried</a></td><td>Nature</td><td>—</td><td><code>ai-peer-review</code> <code>ai-publishing-ecosystems</code> <code>sociotechnical</code></td><td><code>naddaf2025aipeer</code></td><td>read</td></tr>
<tr><td>2025</td><td>Peter et al.</td><td><a href="notes/peter2025anthropomorphic/">The Benefits and Dangers of Anthropomorphic Conversational Agents</a></td><td>Proceedings of the National Academy of Sciences</td><td>—</td><td><code>sociotechnical</code> <code>llm-cognition</code></td><td><code>peter2025anthropomorphic</code></td><td>read</td></tr>
<tr><td>2025</td><td>Tie et al.</td><td><a href="notes/tie2025aiscientistsurvey/">A Survey of AI Scientists</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2510.23045">arXiv</a></td><td><code>autonomous-research-agents</code> <code>evaluation-of-ai-research</code></td><td><code>tie2025aiscientistsurvey</code></td><td>read</td></tr>
<tr><td>2025</td><td>Wu & others</td><td><a href="notes/wu2025agenticreasoning/">Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools</a></td><td>Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)</td><td>—</td><td><code>agentic-reasoning</code> <code>agentic-tool-use</code></td><td><code>wu2025agenticreasoning</code></td><td>read</td></tr>
<tr><td>2025</td><td>Zhang & others</td><td><a href="notes/zhang2025aixiv/">aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2508.15126">arXiv</a></td><td><code>ai-publishing-ecosystems</code> <code>autonomous-research-agents</code> <code>ai-peer-review</code> <code>sociotechnical</code></td><td><code>zhang2025aixiv</code></td><td>read</td></tr>
<tr><td>2026</td><td>Abbasi & others</td><td>ISR Special Issue: Generative AI and New Methods of Inquiry in Information Systems Research</td><td>INFORMS Information Systems Research, Call for Papers</td><td><a href="https://pubsonline.informs.org/page/isre/calls-for-papers">link</a></td><td></td><td><code>abbasi2026isr</code></td><td>—</td></tr>
<tr><td>2026</td><td>Acemoglu et al.</td><td><a href="notes/acemoglu2026collapse/">AI, Human Cognition and Knowledge Collapse</a></td><td>SSRN Working Paper</td><td><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6326698">link</a></td><td><code>sociotechnical</code> <code>evaluation-of-ai-research</code> <code>llm-cognition</code></td><td><code>acemoglu2026collapse</code></td><td>read</td></tr>
<tr><td>2026</td><td>Collu et al.</td><td><a href="notes/collu2026misleading/">Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2508.20863">arXiv</a></td><td><code>ai-peer-review</code> <code>hallucination</code> <code>sociotechnical</code></td><td><code>collu2026misleading</code></td><td>read</td></tr>
<tr><td>2026</td><td>Dell'Acqua et al.</td><td><a href="notes/dellacqua2026jagged/">Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality</a></td><td>Organization Science</td><td><a href="https://doi.org/10.1287/orsc.2025.21838">doi</a></td><td><code>research-productivity</code> <code>human-ai-research-collaboration</code> <code>evaluation-of-ai-research</code></td><td><code>dellacqua2026jagged</code></td><td>read</td></tr>
<tr><td>2026</td><td>Gartenberg et al.</td><td><a href="notes/gartenberg2026morebetter/">More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review</a></td><td>Organization Science</td><td><a href="https://doi.org/10.1287/orsc.2026.ed.v37.n3">doi</a></td><td><code>ai-peer-review</code> <code>ai-publishing-ecosystems</code> <code>research-productivity</code></td><td><code>gartenberg2026morebetter</code></td><td>read</td></tr>
<tr><td>2026</td><td>Jarzębowicz et al.</td><td><a href="notes/jarzebowicz2026landscape/">The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2603.11842">arXiv</a></td><td><code>is-methodology</code> <code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>jarzebowicz2026landscape</code></td><td>read</td></tr>
<tr><td>2026</td><td>Kumar et al.</td><td><a href="notes/kumar2025agenticadoption/">Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities</a></td><td>Information \& Management</td><td><a href="https://doi.org/10.1016/j.im.2026.104317">doi</a></td><td><code>autonomous-research-agents</code> <code>is-methodology</code> <code>sociotechnical</code></td><td><code>kumar2025agenticadoption</code></td><td>read</td></tr>
<tr><td>2026</td><td>Laban et al.</td><td><a href="notes/laban2026llmscorrupt/">LLMs Corrupt Your Documents When You Delegate</a></td><td>arXiv</td><td><a href="https://arxiv.org/abs/2604.15597">arXiv</a></td><td><code>agentic-tool-use</code> <code>hallucination</code> <code>evaluation-of-ai-research</code> <code>reasoning-faithfulness</code></td><td><code>laban2026llmscorrupt</code></td><td>read</td></tr>
<tr><td>2026</td><td>Ngwenyama et al.</td><td><a href="notes/ngwenyama2026platform/">Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor</a></td><td>European Journal of Information Systems</td><td><a href="https://doi.org/10.1080/0960085X.2026.2642660">doi</a></td><td><code>sociotechnical</code> <code>ai-publishing-ecosystems</code></td><td><code>ngwenyama2026platform</code></td><td>read</td></tr>
<tr><td>2026</td><td>Yang et al.</td><td>ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration</td><td>arXiv</td><td><a href="https://arxiv.org/abs/2605.03042">arXiv</a></td><td></td><td><code>yang2026aris</code></td><td>—</td></tr>
<tr><td>2026</td><td>team</td><td>EvoScientist Technical Report</td><td>arXiv</td><td><a href="https://arxiv.org/abs/2603.08127">arXiv</a></td><td></td><td><code>evoscientist2026techreport</code></td><td>—</td></tr>
</tbody>
</table>

<!-- AUTO-GENERATED:papers-table-end -->

??? note "Browse by theme"

    <!-- AUTO-GENERATED:papers-by-theme-start -->

### `agentic-reasoning`

- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Wu & others. [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`

### `agentic-tool-use`

- **2023** — Schick & others. [*Toolformer: Language Models Can Teach Themselves to Use Tools*](notes/schick2023toolformer.md) `schick2023toolformer`
- **2025** — Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- **2025** — Wu & others. [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`

### `ai-peer-review`

- **2024** — Drori & Te'eni. [*Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks*](notes/drori2024humanloop.md) `drori2024humanloop` · skimmed
- **2024** — Gregor. [*Responsible Artificial Intelligence and Journal Publishing*](notes/gregor2024responsible.md) `gregor2024responsible` · skimmed
- **2024** — Kankanhalli. [*Peer Review in the Age of Generative AI*](notes/kankanhalli2024peerreview.md) `kankanhalli2024peerreview` · skimmed
- **2024** — Liang et al.. [*Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*](notes/liang2024monitoring.md) `liang2024monitoring`
- **2024** — Russo Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/russo2024reviewlottery.md) `russo2024reviewlottery`
- **2024** — Sarker et al.. [*Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review*](notes/sarker2024democratizing.md) `sarker2024democratizing` · skimmed
- **2024** — Shmueli & Ray. [*Reimagining the Journal Editorial Process: An AI-Augmented Versus an AI-Driven Future*](notes/shmueli2024editorial.md) `shmueli2024editorial` · skimmed
- **2024** — Weber. [*The Other Reviewer: RoboReviewer*](notes/weber2024roboreviewer.md) `weber2024roboreviewer` · skimmed
- **2025** — Keuper. [*Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications*](notes/keuper2025promptinjection.md) `keuper2025promptinjection`
- **2025** — Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- **2025** — Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2026** — Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2026misleading.md) `collu2026misleading`
- **2026** — Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`

### `ai-publishing-ecosystems`

- **2023** — Susarla et al.. [*The Janus Effect of Generative AI: Charting the Path for Responsible Conduct of Scholarly Activities in Information Systems*](notes/susarla2023janus.md) `susarla2023janus`
- **2024** — Avital. [*Digital Transformation of Academic Publishing: A Call for the Decentralization and Democratization of Academic Journals*](notes/avital2024decentralization.md) `avital2024decentralization` · skimmed
- **2024** — Russo Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/russo2024reviewlottery.md) `russo2024reviewlottery`
- **2024** — Schwartz & Te'eni. [*AI for Knowledge Creation, Curation, and Consumption in Context*](notes/schwartz2024kcc.md) `schwartz2024kcc`
- **2025** — Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2025rapidadoption.md) `bick2025rapidadoption`
- **2025** — Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- **2025** — Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2026** — Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`
- **2026** — Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- **2026** — Ngwenyama et al.. [*Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor*](notes/ngwenyama2026platform.md) `ngwenyama2026platform`

### `autonomous-research-agents`

- **2023** — Park & others. [*Generative Agents: Interactive Simulacra of Human Behavior*](notes/park2023generative.md) `park2023generative`
- **2024** — Novy-Marx & Velikov. [*AI-Powered (Finance) Scholarship*](notes/novymarx2024aifinance.md) `novymarx2024aifinance`
- **2025** — Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- **2025** — Gridach et al.. [*Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions*](notes/gridach2025agenticsurvey.md) `gridach2025agenticsurvey` · skimmed
- **2025** — Tie et al.. [*A Survey of AI Scientists*](notes/tie2025aiscientistsurvey.md) `tie2025aiscientistsurvey`
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2026** — Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`

### `evaluation-of-ai-research`

- **2020** — Maynez & others. [*On Faithfulness and Factuality in Abstractive Summarization*](notes/maynez2020faithfulness.md) `maynez2020faithfulness`
- **2023** — Ji & others. [*Survey of Hallucination in Natural Language Generation*](notes/ji2023hallucination.md) `ji2023hallucination`
- **2024** — Liang et al.. [*Mapping the Increasing Use of LLMs in Scientific Papers*](notes/liang2024mapping.md) `liang2024mapping`
- **2024** — Liang et al.. [*Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*](notes/liang2024monitoring.md) `liang2024monitoring`
- **2024** — Ngwenyama & Rowe. [*Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World*](notes/ngwenyama2024literature.md) `ngwenyama2024literature` · skimmed
- **2024** — Novy-Marx & Velikov. [*AI-Powered (Finance) Scholarship*](notes/novymarx2024aifinance.md) `novymarx2024aifinance`
- **2024** — Russo Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/russo2024reviewlottery.md) `russo2024reviewlottery`
- **2024** — Watson et al.. [*Extending the Foresight of Phillip Ein-Dor: Causal Knowledge Analytics*](notes/watson2024causal.md) `watson2024causal` · skimmed
- **2024** — Yoo. [*Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI*](notes/yoo2024epistemic.md) `yoo2024epistemic` · skimmed
- **2025** — Brodeur et al.. [*Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis*](notes/brodeur2025reproducibility.md) `brodeur2025reproducibility`
- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- **2025** — Gridach et al.. [*Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions*](notes/gridach2025agenticsurvey.md) `gridach2025agenticsurvey` · skimmed
- **2025** — Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- **2025** — Mikalef et al.. [*Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research*](notes/mikalef2025responsible.md) `mikalef2025responsible`
- **2025** — Tie et al.. [*A Survey of AI Scientists*](notes/tie2025aiscientistsurvey.md) `tie2025aiscientistsurvey`
- **2026** — Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`
- **2026** — Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`

### `hallucination`

- **2020** — Maynez & others. [*On Faithfulness and Factuality in Abstractive Summarization*](notes/maynez2020faithfulness.md) `maynez2020faithfulness`
- **2023** — Ji & others. [*Survey of Hallucination in Natural Language Generation*](notes/ji2023hallucination.md) `ji2023hallucination`
- **2024** — Novy-Marx & Velikov. [*AI-Powered (Finance) Scholarship*](notes/novymarx2024aifinance.md) `novymarx2024aifinance`
- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Keuper. [*Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications*](notes/keuper2025promptinjection.md) `keuper2025promptinjection`
- **2025** — Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- **2026** — Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2026misleading.md) `collu2026misleading`
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`

### `human-ai-research-collaboration`

- **2023** — Noy & Zhang. [*Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*](notes/noy2023experimental.md) `noy2023experimental`
- **2024** — Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- **2024** — Drori & Te'eni. [*Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks*](notes/drori2024humanloop.md) `drori2024humanloop` · skimmed
- **2024** — Jarvenpaa & Klein. [*New Frontiers in Information Systems Theorizing: Human-gAI Collaboration*](notes/jarvenpaa2024theorizing.md) `jarvenpaa2024theorizing` · skimmed
- **2024** — Ngwenyama & Rowe. [*Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World*](notes/ngwenyama2024literature.md) `ngwenyama2024literature` · skimmed
- **2024** — Sarker et al.. [*Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review*](notes/sarker2024democratizing.md) `sarker2024democratizing` · skimmed
- **2024** — Schwartz & Te'eni. [*AI for Knowledge Creation, Curation, and Consumption in Context*](notes/schwartz2024kcc.md) `schwartz2024kcc`
- **2025** — Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- **2025** — Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- **2025** — Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- **2025** — Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- **2026** — Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`

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
- **2026** — Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- **2026** — Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`

### `llm-cognition`

- **2023** — Mitchell & Krakauer. [*The Debate over Understanding in AI's Large Language Models*](notes/mitchell2023understanding.md) `mitchell2023understanding`
- **2023** — Park & others. [*Generative Agents: Interactive Simulacra of Human Behavior*](notes/park2023generative.md) `park2023generative`
- **2024** — Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- **2025** — Peter et al.. [*The Benefits and Dangers of Anthropomorphic Conversational Agents*](notes/peter2025anthropomorphic.md) `peter2025anthropomorphic`
- **2026** — Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`

### `reasoning-faithfulness`

- **2020** — Maynez & others. [*On Faithfulness and Factuality in Abstractive Summarization*](notes/maynez2020faithfulness.md) `maynez2020faithfulness`
- **2025** — Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- **2025** — Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- **2026** — Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`

### `replication-infrastructure`

- **2025** — Brodeur et al.. [*Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis*](notes/brodeur2025reproducibility.md) `brodeur2025reproducibility`

### `research-productivity`

- **2012** — Aral et al.. [*Information, Technology, and Information Worker Productivity*](notes/aral2012itproductivity.md) `aral2012itproductivity`
- **2023** — Noy & Zhang. [*Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*](notes/noy2023experimental.md) `noy2023experimental`
- **2024** — Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- **2024** — Benbya et al.. [*Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work*](notes/benbya2024navigating.md) `benbya2024navigating` · skimmed
- **2024** — Liang et al.. [*Mapping the Increasing Use of LLMs in Scientific Papers*](notes/liang2024mapping.md) `liang2024mapping`
- **2024** — Novy-Marx & Velikov. [*AI-Powered (Finance) Scholarship*](notes/novymarx2024aifinance.md) `novymarx2024aifinance`
- **2025** — Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- **2025** — Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2025rapidadoption.md) `bick2025rapidadoption`
- **2025** — Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- **2025** — Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- **2025** — Kwon & Yang. [*Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality*](notes/kwon2025inequality.md) `kwon2025inequality` · skimmed
- **2026** — Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`
- **2026** — Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`

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
- **2025** — Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2025rapidadoption.md) `bick2025rapidadoption`
- **2025** — Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- **2025** — Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- **2025** — Kwon & Yang. [*Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality*](notes/kwon2025inequality.md) `kwon2025inequality` · skimmed
- **2025** — Mikalef et al.. [*Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research*](notes/mikalef2025responsible.md) `mikalef2025responsible`
- **2025** — Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- **2025** — Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- **2025** — Peter et al.. [*The Benefits and Dangers of Anthropomorphic Conversational Agents*](notes/peter2025anthropomorphic.md) `peter2025anthropomorphic`
- **2025** — Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`
- **2026** — Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`
- **2026** — Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2026misleading.md) `collu2026misleading`
- **2026** — Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- **2026** — Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`
- **2026** — Ngwenyama et al.. [*Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor*](notes/ngwenyama2026platform.md) `ngwenyama2026platform`

### `style-engines`

- **2024** — Riemer & Peter. [*Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications*](notes/riemer2024styleengines.md) `riemer2024styleengines`

<!-- AUTO-GENERATED:papers-by-theme-end -->

??? note "Browse by year"

    <!-- AUTO-GENERATED:papers-by-year-start -->
*56/56 notes have been filled with abstract-grounded summaries; 0 remain as stubs marked ⚠️ (front-matter verified, but Summary / Contribution / Method / Critique not yet written).*

### 2026

- Acemoglu et al.. [*AI, Human Cognition and Knowledge Collapse*](notes/acemoglu2026collapse.md) `acemoglu2026collapse`
- Collu et al.. [*Misleading Large Language Models Used (or Misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks*](notes/collu2026misleading.md) `collu2026misleading`
- Dell'Acqua et al.. [*Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*](notes/dellacqua2026jagged.md) `dellacqua2026jagged`
- Gartenberg et al.. [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`
- Jarzębowicz et al.. [*The Landscape of Generative AI in Information Systems: A Synthesis of Secondary Reviews and Research Agendas*](notes/jarzebowicz2026landscape.md) `jarzebowicz2026landscape`
- Kumar et al.. [*Agentic Artificial Intelligence as a New Frontier in Information Systems: Promise, Peril, and Research Opportunities*](notes/kumar2025agenticadoption.md) `kumar2025agenticadoption`
- Laban et al.. [*LLMs Corrupt Your Documents When You Delegate*](notes/laban2026llmscorrupt.md) `laban2026llmscorrupt`
- Ngwenyama et al.. [*Platform Capture of Scientific Knowledge Production: Publishers' Dominance, Generative AI and Subsumption of Academic Labor*](notes/ngwenyama2026platform.md) `ngwenyama2026platform`

### 2025

- Bapna et al.. [*Agentic AI and Managers' Analytics Capabilities: An Exploration*](notes/bapna2025analytics.md) `bapna2025analytics`
- Bick et al.. [*The Rapid Adoption of Generative AI*](notes/bick2025rapidadoption.md) `bick2025rapidadoption`
- Brodeur et al.. [*Assessing Reproducibility in Economics Using Standardized Crowd-Sourced Analysis*](notes/brodeur2025reproducibility.md) `brodeur2025reproducibility`
- Brynjolfsson et al.. [*Generative AI at Work*](notes/brynjolfsson2025genaiwork.md) `brynjolfsson2025genaiwork`
- Chen & others. [*Reasoning Models Don't Always Say What They Think*](notes/chen2025reasoning.md) `chen2025reasoning`
- Filimonovic et al.. [*Can GenAI Improve Academic Performance? Evidence from the Social and Behavioral Sciences*](notes/filimonovic2025genai.md) `filimonovic2025genai`
- Gopal & others. [*Inventing with Machines: Generative AI and the Evolving Landscape of IS Research*](notes/gopal2025inventing.md) `gopal2025inventing`
- Gridach et al.. [*Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions*](notes/gridach2025agenticsurvey.md) `gridach2025agenticsurvey` · skimmed
- Keuper. [*Prompt Injection Attacks on LLM Generated Reviews of Scientific Publications*](notes/keuper2025promptinjection.md) `keuper2025promptinjection`
- Kwon & Yang. [*Large Language Models in Academia: Boosting Productivity but Reinforcing Inequality*](notes/kwon2025inequality.md) `kwon2025inequality` · skimmed
- Matton & others. [*Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations*](notes/matton2025walkthetalk.md) `matton2025walkthetalk`
- Mikalef et al.. [*Responsible AI Starts with the Artifact: Challenging the Concept of Responsible AI in IS Research*](notes/mikalef2025responsible.md) `mikalef2025responsible`
- Naddaf. [*AI Is Transforming Peer Review --- and Many Scientists Are Worried*](notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- Nature Editorial. [*Transparent Peer Review to Be Extended to All Research Papers*](notes/naturePeerReview2025editorial.md) `naturePeerReview2025editorial`
- Peter et al.. [*The Benefits and Dangers of Anthropomorphic Conversational Agents*](notes/peter2025anthropomorphic.md) `peter2025anthropomorphic`
- Tie et al.. [*A Survey of AI Scientists*](notes/tie2025aiscientistsurvey.md) `tie2025aiscientistsurvey`
- Wu & others. [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Zhang & others. [*aiXiv: A Next-Generation Open Access Ecosystem for Scientific Discovery Generated by AI Scientists*](notes/zhang2025aixiv.md) `zhang2025aixiv`

### 2024

- Agrawal et al.. [*AI in Science*](notes/agrawal2024aiscience.md) `agrawal2024aiscience`
- Alavi et al.. [*A Knowledge Management Perspective of Generative Artificial Intelligence*](notes/alavi2024kmperspective.md) `alavi2024kmperspective` · skimmed
- Avital. [*Digital Transformation of Academic Publishing: A Call for the Decentralization and Democratization of Academic Journals*](notes/avital2024decentralization.md) `avital2024decentralization` · skimmed
- Benbya et al.. [*Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work*](notes/benbya2024navigating.md) `benbya2024navigating` · skimmed
- Drori & Te'eni. [*Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks*](notes/drori2024humanloop.md) `drori2024humanloop` · skimmed
- Gregor. [*Responsible Artificial Intelligence and Journal Publishing*](notes/gregor2024responsible.md) `gregor2024responsible` · skimmed
- Jarvenpaa & Klein. [*New Frontiers in Information Systems Theorizing: Human-gAI Collaboration*](notes/jarvenpaa2024theorizing.md) `jarvenpaa2024theorizing` · skimmed
- Kankanhalli. [*Peer Review in the Age of Generative AI*](notes/kankanhalli2024peerreview.md) `kankanhalli2024peerreview` · skimmed
- Liang et al.. [*Mapping the Increasing Use of LLMs in Scientific Papers*](notes/liang2024mapping.md) `liang2024mapping`
- Liang et al.. [*Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews*](notes/liang2024monitoring.md) `liang2024monitoring`
- Ngwenyama & Rowe. [*Should We Collaborate with AI to Conduct Literature Reviews? Changing Epistemic Values in a Flattening World*](notes/ngwenyama2024literature.md) `ngwenyama2024literature` · skimmed
- Novy-Marx & Velikov. [*AI-Powered (Finance) Scholarship*](notes/novymarx2024aifinance.md) `novymarx2024aifinance`
- Riemer & Peter. [*Conceptualizing Generative AI as Style Engines: Application Archetypes and Implications*](notes/riemer2024styleengines.md) `riemer2024styleengines`
- Russo Latona et al.. [*The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates*](notes/russo2024reviewlottery.md) `russo2024reviewlottery`
- Sabherwal & Grover. [*The Societal Impacts of Generative Artificial Intelligence: A Balanced Perspective*](notes/sabherwal2024societal.md) `sabherwal2024societal` · skimmed
- Sarker et al.. [*Democratizing Knowledge Creation Through Human-AI Collaboration in Academic Peer Review*](notes/sarker2024democratizing.md) `sarker2024democratizing` · skimmed
- Schwartz & Te'eni. [*AI for Knowledge Creation, Curation, and Consumption in Context*](notes/schwartz2024kcc.md) `schwartz2024kcc`
- Shmueli & Ray. [*Reimagining the Journal Editorial Process: An AI-Augmented Versus an AI-Driven Future*](notes/shmueli2024editorial.md) `shmueli2024editorial` · skimmed
- Watson et al.. [*Extending the Foresight of Phillip Ein-Dor: Causal Knowledge Analytics*](notes/watson2024causal.md) `watson2024causal` · skimmed
- Weber. [*The Other Reviewer: RoboReviewer*](notes/weber2024roboreviewer.md) `weber2024roboreviewer` · skimmed
- Yoo. [*Evolving Epistemic Infrastructure: The Role of Scientific Journals in the Age of Generative AI*](notes/yoo2024epistemic.md) `yoo2024epistemic` · skimmed

### 2023

- Ji & others. [*Survey of Hallucination in Natural Language Generation*](notes/ji2023hallucination.md) `ji2023hallucination`
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
