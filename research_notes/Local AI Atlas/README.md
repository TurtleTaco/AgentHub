# Local AI Atlas: research workspace

Market research on companies enabling local AI (on-device, edge, on-prem, private cloud, air-gapped, sovereign). As of Nov 2026.

## Pipeline

1. `discovery/`: 11 segment sweeps (JSON + notes) → `scripts/merge_discovery.py` → `data/candidates.json`
2. `scripts/curate.py` → `data/curated_candidates.json`, `data/excluded_at_curation.json`, `profiles/input/`
3. `profiles/batch-*.json|md`: verification + profile per company (prompt: `scripts/profile_prompt.txt`)
4. `verification/factcheck-*.json`: independent fact-checks (prompt: `scripts/factcheck_prompt.txt`)
5. `data/ontology.json` + `data/classification-*.json` (prompt: `scripts/classify_prompt.txt`; overrides in `classification-overrides.json`)
6. `scripts/build_atlas.py` → `data/companies.json|csv`, `data/out_of_scope.json`, `data/deals.json`, `reports/local-ai-atlas/atlas-data.json`
7. `scripts/make_narrative.py` → `data/narrative.json`; `scripts/make_report.py` → `reports/Local AI Atlas.md`, `data/directory.md`

## Rebuild

```bash
cd "research_notes/Local AI Atlas"
python3 scripts/build_atlas.py . ../../reports/local-ai-atlas/atlas-data.json
python3 scripts/make_narrative.py . ../../reports/local-ai-atlas/atlas-data.json
python3 scripts/build_atlas.py . ../../reports/local-ai-atlas/atlas-data.json
python3 scripts/make_report.py . ../../reports/local-ai-atlas/atlas-data.json "../../reports/Local AI Atlas.md"
```

## Record fields (data/companies.json)

id, name, legalName, verdict (in/borderline), web, city, country, region, founded, type, status, statusDetail, parent, stage, fund (USD M), lastRound, val, mcap, investors, emp, empBand, focus, problem, diff, products [name, category, description], dep (deployment targets), layers, mod (modalities), cust (customer segments), partners, customers, primary/secondary (niche ids), conf (per-field confidence), basis, src, factchecked (fields corrected by fact-check)
