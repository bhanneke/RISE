<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/chemistry-rdkit.md -->

# `chemistry-rdkit`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../autoresearchclaw/">AutoResearchClaw skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/chemistry-rdkit/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/autoresearchclaw/chemistry-rdkit/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/aiming-lab/AutoResearchClaw" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

### RDKit Cheminformatics Best Practice

#### Molecular I/O
1. Create molecules from SMILES: `mol = Chem.MolFromSmiles('CCO')`
2. Always check for None: `MolFromSmiles` returns None on invalid input
3. Convert to canonical SMILES: `Chem.MolToSmiles(mol)`
4. Read SDF files: `suppl = Chem.SDMolSupplier('file.sdf')`
5. Read SMILES files: `suppl = Chem.SmilesMolSupplier('file.smi')`
6. Write molecules: `writer = Chem.SDWriter('output.sdf')`

#### Molecular Descriptors
1. Molecular weight: `Descriptors.MolWt(mol)`
2. LogP (lipophilicity): `Descriptors.MolLogP(mol)`
3. TPSA (polar surface area): `Descriptors.TPSA(mol)`
4. H-bond donors/acceptors: `Descriptors.NumHDonors(mol)`, `Descriptors.NumHAcceptors(mol)`
5. Rotatable bonds: `Descriptors.NumRotatableBonds(mol)`
6. Lipinski Rule of 5: MW <= 500, LogP <= 5, HBD <= 5, HBA <= 10

#### Fingerprints and Similarity
1. Morgan (circular) fingerprints: `AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)`
2. RDKit fingerprints: `Chem.RDKFingerprint(mol)`
3. MACCS keys: `MACCSkeys.GenMACCSKeys(mol)`
4. Tanimoto similarity: `DataStructs.TanimotoSimilarity(fp1, fp2)`
5. Use radius=2 (ECFP4 equivalent) as default for most applications
6. For virtual screening, Tanimoto > 0.7 suggests structural similarity

#### Substructure Search
1. SMARTS patterns: `pattern = Chem.MolFromSmarts('[OH]')`
2. Check match: `mol.HasSubstructMatch(pattern)`
3. Get all matches: `mol.GetSubstructMatches(pattern)`
4. Common SMARTS: `[#6](=O)[OH]` (carboxylic acid), `[NH2]` (primary amine)
5. Filter compound libraries by functional group presence

#### Property Calculation Patterns
1. Batch processing: iterate over SDMolSupplier, skip None entries
2. Use `Chem.Descriptors.descList` for all available descriptors
3. For ADMET filtering, calculate Lipinski, Veber, and PAINS filters
4. Generate 3D coordinates: `AllChem.EmbedMolecule(mol, AllChem.ETKDG())`
5. Minimize energy: `AllChem.MMFFOptimizeMolecule(mol)`

#### Common Pitfalls
1. Always sanitize molecules (default behavior) — disable only when needed
2. Add hydrogens explicitly for 3D work: `Chem.AddHs(mol)`
3. Handle stereochemistry: use `Chem.AssignStereochemistry(mol)`
4. Large SDF files: use `ForwardSDMolSupplier` for memory efficiency
5. Kekulization errors usually indicate invalid SMILES input
