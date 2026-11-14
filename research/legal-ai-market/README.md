# Legal AI market research (2026-11-14)

Exhaustive map of companies building AI for legal work: who they are, what they build, where they overlap.

**Open the report:** `report/legal-ai-atlas.html` (self-contained; also published as a Claude artifact).
**Quick read:** `report/summary.md` · **Ontology:** `ontology/README.md`

## Numbers
- 696 companies profiled (572 core legal AI, 124 adjacent), 47 HQ countries
- 15 workflow domains, 68 categories
- 36 absorbed/defunct companies (M&A view), 23 excluded candidates (with reasons)

## Folder layout
| Path | What |
|---|---|
| `data/companies.json` | **Main dataset.** One record per company: focus, HQ, founded, funding, headcount, products, capabilities, ontology tags, sources |
| `data/companies.csv` | Same, flattened for spreadsheets |
| `data/companies_verified.json` | Verified universe incl. scope (core/adjacent) and status |
| `data/excluded.json`, `data/excluded_during_profiling.json` | Dropped candidates and why |
| `data/acquired_defunct.json` | Companies folded into acquirers or shut down |
| `data/manual_overrides.json` | The few hand corrections (documented) |
| `ontology/ontology.json` | Ontology: domains → categories (+ customer, practice, model facets) |
| `ontology/mindmap.json` | Mind-map tree, domain overlap matrix, category pairs, category stats |
| `report/` | HTML report, template, takeaways, summary, stats |
| `raw/discovery/` | 10 discovery-agent outputs (1,061 raw records + gap hunt) |
| `raw/verification/` | 4 verification-agent outputs |
| `raw/profiles/` | 24 profiling-agent outputs |
| `raw/tags/` | 4 tagging-agent outputs |
| `scripts/` | Pipeline scripts and the agent briefs used |

## Pipeline (re-run to refresh)
1. Discovery agents → `raw/discovery/*.json`; `python3 scripts/merge_discovery.py`
2. Verification agents → `raw/verification/*.json`; `python3 scripts/consolidate_verified.py`
3. Profiling agents (brief: `scripts/profiling_prompt.md`, schema: `scripts/profile_schema.md`) → `raw/profiles/`
4. Tagging agents (brief: `scripts/tagging_prompt.md`) → `raw/tags/`
5. `python3 scripts/build_dataset.py && python3 scripts/build_artifact.py && python3 scripts/write_docs.py`

## Caveats
- Snapshot as of 2026-11-14. Funding/headcount move fast.
- Web access was search-only and rate-capped; long-tail profiles may rely on model knowledge (see each record's `confidence`).
- Funding = disclosed amounts. Incumbents/PE-owned companies often show none.
- Ontology v1.1–1.3 added 4 categories after tagging (marketing, trial prep, legal translation, AI governance); assignments for those use documented keyword rules in `scripts/build_dataset.py`.
