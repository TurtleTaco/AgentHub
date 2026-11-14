You are an ONTOLOGY-TAGGING agent for a legal-AI market map (today is 2026-11-14). No web access is needed — work only from the files.

## Inputs
1. Ontology: /home/user/AgentHub/research/legal-ai-market/ontology/ontology.json
   - Facet A: 15 workflow domains → 64 categories (ids like "CON.review", "LIT.ediscovery"), each with a definition (`def`) and hint keywords (`kw`).
   - Facet B customer values, Facet C practice values, Facet D business models (platform | point | suite | services | infra).
2. Companies: /home/user/AgentHub/research/legal-ai-market/data/tag_inputs/{TAG}.json  (compact profiles: focus, problem, products, capabilities, customers, practice, delivery, differentiators)

## For EACH company produce
- `primary`: the ONE category id that best describes its core focus (where most of its product value sits).
- `categories`: ALL category ids where the company ships a real, substantive capability (include `primary`). Be faithful to the capability list — tag a category only if there is concrete evidence (a product or several capabilities), not a passing mention. Typical: 1–3 for point solutions, 4–10 for platforms/suites.
- `model`: one of platform | point | suite | services | infra (see Facet D definitions; incumbents like Thomson Reuters, LexisNexis, Clio, Filevine = suite; AI-native law firms/ALSPs = services).
- `customers`: normalized list using ONLY Facet B values.
- `practice`: normalized list using ONLY Facet C values (use "General / multi-practice" for horizontal tools).
- `unique_angle`: ≤ 12 words — what is genuinely distinctive about it versus peers in its primary category (e.g. "only player auto-generating SSDI briefs", "owns proprietary Swedish case-law corpus"). Avoid generic phrases like "AI-powered platform".

## Output (required)
Write a JSON array (same order as input) to: /home/user/AgentHub/research/legal-ai-market/raw/tags/{TAG}_tags.json
Item: {"cid": str, "name": str, "primary": str, "categories": [str], "model": str, "customers": [str], "practice": [str], "unique_angle": str}
Validate every id against the ontology:
python3 - <<'PY'
import json
ont=json.load(open('/home/user/AgentHub/research/legal-ai-market/ontology/ontology.json'))
ids={c['id'] for d in ont['facets']['A_domain']['domains'] for c in d['categories']}
t=json.load(open('/home/user/AgentHub/research/legal-ai-market/raw/tags/{TAG}_tags.json'))
inp=json.load(open('/home/user/AgentHub/research/legal-ai-market/data/tag_inputs/{TAG}.json'))
assert len(t)==len(inp), (len(t),len(inp))
bad=[(x['name'],c) for x in t for c in x['categories']+[x['primary']] if c not in ids]
assert not bad, bad[:10]
assert all(x['primary'] in x['categories'] for x in t)
print('ok',len(t))
PY
Work in slices (e.g. 40 companies at a time, appending to the file) so nothing is lost.

## Final reply
Under 60 words: count tagged, validation result, and any category you found under-specified (suggest a split/merge if it would help).
