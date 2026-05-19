<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/chemistry-rdkit.md -->

# `chemistry-rdkit`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

---
name: chemistry-rdkit
description: Computational chemistry with RDKit for molecular analysis, descriptors, fingerprints, and substructure search. Use when working with SMILES, drug discovery, or cheminformatics tasks.
metadata:
  category: domain
  trigger-keywords: "molecule,SMILES,chemical,drug,rdkit,fingerprint,molecular,compound,reaction,cheminformatics"
  applicable-stages: "9,10,12"
  priority: "4"
  version: "1.0"
  author: researchclaw
  references: "adapted from K-Dense-AI/claude-scientific-skills"
---

## RDKit Cheminformatics Best Practice

### Molecular I/O
1. Create molecules from SMILES: `mol = Chem.MolFromSmiles('CCO')`
2. Always check for None: `MolFromSmiles` returns None on invalid input
3. Convert to canonical SMILES: `Chem.MolToSmiles(mol)`
4. Read SDF files: `suppl = Chem.SDMolSupplier('file.sdf')`
5. Read SMILES files: `suppl = Chem.SmilesMolSupplier('file.smi')`
6. Write molecules: `writer = Chem.SDWriter('output.sdf')`

### Molecular Descriptors
1. Molecular weight: `Descriptors.MolWt(mol)`
2. LogP (lipophilicity): `Descriptors.MolLogP(mol)`
3. TPSA (polar surface area): `Descriptors.TPSA(mol)`
4. H-bond donors/acceptors: `Descriptors.NumHDonors(mol)`, `Descriptors.NumHAcceptors(mol)`
5. Rotatable bonds: `Descriptors.NumRotatableBonds(mol)`
6. Lipinski Rule of 5: MW <= 500, LogP <= 5, HBD <= 5, HBA <= 10

### Fingerprints and Similarity
1. Morgan (circular) fingerprints: `AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)`
2. RDKit fingerprints: `Chem.RDKFingerprint(mol)`
3. MACCS keys: `MACCSkeys.GenMACCSKeys(mol)`
4. Tanimoto similarity: `DataStructs.TanimotoSimilarity(fp1, fp2)`
5. Use radius=2 (ECFP4 equivalent) as default for most applications
6. For virtual screening, Tanimoto > 0.7 suggests structural similarity

### Substructure Search
1. SMARTS patterns: `pattern = Chem.MolFromSmarts('[OH]')`
2. Check match: `mol.HasSubstructMatch(pattern)`
3. Get all matches: `mol.GetSubstructMatches(pattern)`
4. Common SMARTS: `[#6](=O)[OH]` (carboxylic acid), `[NH2]` (primary amine)
5. Filter compound libraries by functional group presence

### Property Calculation Patterns
1. Batch processing: iterate over SDMolSupplier, skip None entries
2. Use `Chem.Descriptors.descList` for all available descriptors
3. For ADMET filtering, calculate Lipinski, Veber, and PAINS filters
4. Generate 3D coordinates: `AllChem.EmbedMolecule(mol, AllChem.ETKDG())`
5. Minimize energy: `AllChem.MMFFOptimizeMolecule(mol)`

### Common Pitfalls
1. Always sanitize molecules (default behavior) — disable only when needed
2. Add hydrogens explicitly for 3D work: `Chem.AddHs(mol)`
3. Handle stereochemistry: use `Chem.AssignStereochemistry(mol)`
4. Large SDF files: use `ForwardSDMolSupplier` for memory efficiency
5. Kekulization errors usually indicate invalid SMILES input


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/chemistry-rdkit/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>aiming-lab/AutoResearchClaw</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../autoresearchclaw.md">AutoResearchClaw skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04-23</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw">⭐ aiming-lab/AutoResearchClaw</a><br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/autoresearchclaw/chemistry-rdkit/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/autoresearchclaw.yml">edit on GitHub</a>.</p>
</div>

</div>
