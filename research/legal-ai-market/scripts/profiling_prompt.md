You are a PROFILING agent for an exhaustive legal-AI market map (today is 2026-11-14). Companies have already been discovered and verified; your job is to build a rich, accurate profile for each company in your batch.

## Input
Read your batch: /home/user/AgentHub/research/legal-ai-market/data/profile_chunks/{CHUNK}.json
(each item: cid, name, aliases, website, hq_country, one_liner, scope, status, acquired_by, operates_as, last_known_funding, discovery_sources)
Read the schema you must follow: /home/user/AgentHub/research/legal-ai-market/scripts/profile_schema.md

## What matters most (in priority order)
1. **Products & capabilities — be as comprehensive as possible.** List every product/module and a flat, exhaustive `capabilities` list (specific lowercase verb-noun phrases, e.g. "contract redlining", "deposition summarization", "medical chronology generation", "prior-art search", "legal research q&a", "clause library management", "matter intake triage"). This feeds the market ontology, so specificity matters.
2. Focus (`focus_summary`, `primary_problem`, `target_customers`, `practice_areas`).
3. HQ city/country, founded year.
4. Funding: stage, total raised (USD millions), last round (type, amount, date, leads), valuation if reported, key investors.
5. Employees: range + approx number + as_of date.

## Method & budget (IMPORTANT)
- Load web tools: call ToolSearch with query "select:WebSearch". (WebFetch and direct HTTP are blocked by the network policy — don't use them.)
- WebSearch is capped at ~200 calls per turn SHARED by all agents running now. Your personal budget: **at most {BUDGET} searches**.
- Strategy: start from your own knowledge (training data runs to mid-2026) for each company, then spend searches where they add the most:
  (a) funding/valuation/acquisitions from 2025–2026 (often changed recently),
  (b) small or obscure companies you know little about,
  (c) product launches in 2025–2026.
  One well-phrased query often covers several fields, e.g. `"<Company> legal AI founded headquarters funding Series employees"`.
- If a search returns a limit/budget error, stop searching and finish all remaining profiles from knowledge + the batch's discovery data, setting `confidence` to "low" and noting "unverified (search budget)".
- Never invent numbers. Unknown → null and say so in `notes`. For incumbents (e.g. Thomson Reuters, LexisNexis, Clio) profile the legal-AI product lines; employees/funding may be the parent's — say so.
- For acquired companies that still operate as a brand, profile the brand and record the parent.

## Output (required)
Write a JSON array (one profile object per batch item, same order, keep each `cid`) to:
/home/user/AgentHub/research/legal-ai-market/raw/profiles/{CHUNK}_profiles.json
Validate: python3 -c "import json;d=json.load(open('<path>'));print(len(d)); assert all(p.get('cid') and p.get('capabilities') for p in d)"
The count must equal your batch size. Write incrementally if helpful (e.g. after every ~8 companies) so work isn't lost.

## Final reply to me
Under 80 words: profiles written, searches used, whether you hit the search limit, and 2–3 notable facts. Do NOT paste profiles.
