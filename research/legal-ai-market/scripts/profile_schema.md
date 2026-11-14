# Company profile schema (one JSON object per company)

```json
{
  "cid": "C0123",                       // from candidates list — keep as given
  "name": "Harvey",
  "website": "https://www.harvey.ai",
  "status": "active | acquired | defunct",
  "acquired_by": null,                  // or "Thomson Reuters (2023)"
  "parent_company": null,               // e.g. "LexisNexis (RELX)" for product lines of incumbents
  "hq_city": "San Francisco",
  "hq_country": "United States",
  "other_offices": ["New York", "London"],
  "founded_year": 2022,
  "founders": ["Winston Weinberg", "Gabe Pereyra"],
  "employees": {
    "range": "501-1000",                // one of: 1-10, 11-50, 51-200, 201-500, 501-1000, 1001-5000, 5001+
    "approx": 650,                      // best numeric estimate or null
    "as_of": "2026-09",
    "source": "LinkedIn / press"
  },
  "funding": {
    "stage": "Series F",                // Bootstrapped | Pre-seed | Seed | Series A | Series B | Series C | Series D | Series E | Series F+ | Growth/PE | Public | Acquired | Subsidiary | Non-profit | Unknown
    "total_raised_usd_m": 1200,         // number in USD millions, or null if unknown
    "total_raised_text": "~$1.2B total",
    "last_round": {"type": "Series F", "amount_usd_m": 200, "date": "2026-xx", "lead_investors": ["GIC", "Sequoia"]},
    "valuation_usd_m": 11000,           // latest reported, or null
    "key_investors": ["Sequoia", "Kleiner Perkins", "OpenAI Startup Fund"]
  },
  "focus_summary": "<= 30 words: what they do and for whom",
  "primary_problem": "<= 20 words: the core pain they solve",
  "target_customers": ["Large law firms", "In-house legal"],   // pick from list below
  "practice_areas": ["Corporate/M&A", "Litigation", "Tax"],     // or ["General"]
  "jurisdictions": ["US", "UK", "EU"],
  "products": [
    {"name": "Assistant", "description": "<= 25 words", "capabilities": ["legal Q&A", "drafting", "document analysis"]},
    {"name": "Vault", "description": "...", "capabilities": ["bulk document review", "tabular extraction"]}
  ],
  "capabilities": ["legal research", "contract review", "due diligence", "..."],   // flat, lowercase, specific verb-noun phrases; be exhaustive
  "delivery": ["Web app", "Word add-in", "Outlook add-in", "API", "Mobile", "Integrations"],
  "ai_approach": "<= 25 words (own models? which LLM vendors? agentic? RAG over proprietary content?)",
  "key_integrations": ["iManage", "NetDocuments", "Microsoft 365"],
  "notable_customers": ["A&O Shearman", "PwC"],
  "differentiators": ["<= 12 words each", "..."],
  "recent_news": ["2026-06: <= 15 words", "..."],
  "confidence": "high | medium | low",
  "sources": ["https://...", "https://..."],
  "notes": "<= 30 words: caveats, conflicting numbers, etc."
}
```

## Allowed `target_customers` values
Large law firms · Mid-size law firms · Small firms & solos · Plaintiff/PI firms · In-house legal · Business teams (non-lawyers) · Compliance teams · Consumers/individuals · SMBs · Government/courts · Legal aid/non-profits · Insurers/claims · Financial institutions · Private equity/funds · IP/patent professionals · ALSPs/legal service providers · Law students/academia

## Rules
- Never invent numbers. Unknown → null, and say so in `notes`.
- For incumbents (e.g. Thomson Reuters, LexisNexis, Clio) describe the LEGAL AI product lines; employees/funding can be for the parent, note that.
- Prefer sources from 2025–2026. Note the date for employees/funding.
- `capabilities` must be exhaustive across all products — this feeds the ontology.
