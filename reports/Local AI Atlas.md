# Local AI Atlas

*Market map of companies that run AI on customer-controlled hardware · as of Nov 2026*

Interactive version: the **Local AI Atlas** artifact (built from `reports/local-ai-atlas/`).

## Key takeaways

- **760 companies, 8 domains, 50 niches.** Local AI is a full stack, from NPUs to personal apps, not one market.
- **On-prem beats on-device.** 439 companies target customer datacenters vs 119 for phones. "Local" mostly means private infrastructure.
- **Silicon is crowded and mature; software is young.** 74 of 110 model companies and 35 of 45 personal-AI players were founded 2020+, vs 20 of 135 chip firms.
- **Money follows physical AI.** Among core (non-borderline) independents, Vertical & Physical AI raised the most ($19B, led by Anduril Industries, Shield AI, Field AI); personal local AI the least ($0.6B).
- **NVIDIA is the gravity well.** Top acquirer (8 deals incl. Run:ai, Deci, OctoAI) and co-builder of Palantir's Sovereign AI OS: five joint launches in 11 months.
- **Chipmakers are buying the software layer.** NVIDIA 8, AMD 6, Qualcomm 5 of 85 tracked deals: runtimes, compilers, dev platforms (Edge Impulse, Modular, Nexa AI, Silo AI).
- **Biggest overlaps: Models × Runtimes (30) and Runtimes × Ops (22).** Model makers ship their own engines. Serving engines grow into cluster ops.
- **Focus is the norm.** 390 of 760 companies sit in a single niche; the multi-domain players are mostly big tech.
- **White space:** portable & web runtimes, local creative tools, healthcare & life sciences, personal AI servers & home AI each have fewer than 10 companies.
- **Shakudo's niche (private AI OS) has 23 players**, from Dataiku, Domino and Cloudera to Kamiwaza, webAI and Zylon. The battle is open-source breadth plus run-anywhere Kubernetes.

## Ontology: 8 domains → niches

| Domain | Problem it solves | Main | Niches |
|---|---|---|---|
| **1. Edge & Device Silicon** | Make AI computable inside small, power-limited devices | 135 | 1a Edge AI accelerators (34); 1b Ultra-low-power & TinyML chips (41); 1c In-memory, analog & neuromorphic (28); 1d NPU & AI processor IP (25); 1e PC, mobile & auto SoCs (21); 1f Embedded & vision SoCs (46) |
| **2. On-prem Compute & Systems** | Give organisations their own AI compute instead of renting cloud GPUs | 85 | 2a Datacenter inference accelerators (38); 2b AI servers & AI factory stacks (31); 2c Workstations & AI mini-PCs (21); 2d Private AI appliances (21); 2e Storage & data for on-prem AI (15); 2f AI integrators & services (4); 2g Hyperscaler on-prem & disconnected clouds (4) |
| **3. Models & Efficiency** | Make capable models small and open enough to run locally | 110 | 3a Compression & compilers (32); 3b Efficient-architecture model labs (20); 3c Open-weight model makers (62); 3d Compact speech & audio models (26); 3e Compact vision & multimodal models (14); 3f Fine-tuning & distillation tools (11); 3g Embedding & retrieval models (5) |
| **4. Inference Runtimes & SDKs** | Run any model fast on whatever hardware is at hand | 53 | 4a On-device GenAI SDKs (21); 4b Local inference engines (32); 4c On-device voice engines (19); 4d Self-hosted serving engines (43); 4e Portable & web runtimes (6) |
| **5. Infrastructure & Edge Ops** | Deploy, scale and manage AI across owned clusters and edge fleets | 85 | 5a GPU orchestration & private AI cloud (40); 5b Enterprise private-AI infrastructure (16); 5c Edge orchestration & fleet management (39); 5d Edge MLOps & TinyML platforms (24); 5e Distributed & federated compute (10) |
| **6. Private & Sovereign AI Platforms** | Let enterprises and states use GenAI without data leaving their control | 124 | 6a Private AI operating systems (23); 6b Private ChatGPT & enterprise RAG (44); 6c Self-hostable agent & workflow builders (31); 6d Enterprise LLMs with private deployment (26); 6e Sovereign & national AI stacks (41); 6f Self-hosted coding assistants (12); 6g Confidential & privacy-preserving AI (12) |
| **7. Vertical & Physical AI** | Solve sector problems where data, latency or connectivity rule out the cloud | 123 | 7a Video analytics & security (39); 7b Industrial vision & inspection (29); 7c Robotics, drones & autonomy (18); 7d Defense & national security (24); 7e Healthcare & life sciences (8); 7f Smart infrastructure, retail & mobility (23); 7g On-prem speech & conversational AI (17); 7h Regulated document, language & finance AI (15) |
| **8. Personal & Developer Local AI** | Let individuals own and run AI on their own machines | 45 | 8a Local LLM apps (20); 8b Local creative tools (7); 8c Personal memory & assistants (16); 8d Personal AI servers & home AI (8); 8e Developer tools for local models (16) |

## Big-tech collaborations

- **NVIDIA × Palantir** (Oct 2025 → Sep 2026): Five joint launches: AIP on NVIDIA's stack, a Sovereign AI OS reference architecture, Nemotron in air-gapped US agencies.
- **Dell × Palantir × NVIDIA** (May 2026): Palantir Foundry/AIP ships on-prem inside Dell AI Factory.
- **NVIDIA AI Factory for Government** (Oct 2025): Reference design for federal on-prem AI with Dell, HPE, Cisco and others.
- **NVIDIA × 7 PC makers** (Oct 2025): DGX Spark-class desktops (Acer, ASUS, Dell, GIGABYTE, HP, Lenovo, MSI) put a petaflop on the desk.
- **Microsoft Sovereign Private Cloud** (Feb 2026): Azure Local + Foundry Local run large models fully disconnected.
- **Google Distributed Cloud × NVIDIA / Cirrascale** (Apr 2026): Gemini offered on-prem, including air-gapped.
- **Qualcomm × Humain** (Oct 2025): 200 MW of AI200/AI250 inference racks for Saudi sovereign AI.
- **Microsoft × Qualcomm, Intel, AMD** (2024 →): Copilot+ PCs set the 40-TOPS NPU bar for AI PCs.
- **Meta × Arm** (Oct 2025): ExecuTorch 1.0 with Arm backends for on-device Llama.
- **Huawei × DeepSeek** (2025–2026): Open models tuned for Ascend chips: China's domestic local stack.

## Consolidation

- 85 acquisitions tracked; top buyers: NVIDIA (8), AMD (6), Qualcomm (5), IBM (2), SoftBank Group (2), Analog Devices (2), Nordic Semiconductor (2), GlobalFoundries (2)

## Method & caveats

1. **Discover**: 11 research agents swept market maps, partner directories and funding news, one segment each: 1389 mentions, 893 unique candidates.
2. **Curate**: Merged duplicates; removed community projects, consortia and generic tooling: 792 candidates.
3. **Verify & profile**: 21 agent batches confirmed scope and status, then profiled each company: 760 in scope, 45 rejected.
4. **Fact-check**: 10 independent agents re-checked funding, status, founding, HQ and headcount for 400 key independents: 101 confirmed, 224 corrected, 75 unverifiable.
5. **Build the ontology**: 8 problem-framed domains and 50 niches derived from what companies do. Agents mapped every company (1 main + up to 3 secondary niches); weak fits drove v2.
6. **Map overlaps**: Overlap = a company active in 2+ domains. Crowding and white space = companies per niche. Everything is saved as JSON/CSV.

- **Scope**: Inference on hardware the customer controls: device, edge, on-prem, private cloud, air-gapped, sovereign. Cloud-API-only vendors excluded.
- **Borderline**: 331 companies where local AI is a secondary line are kept and labelled borderline.
- **Funding**: Total disclosed equity in USD for independent companies, all purposes (not only local AI). Public and big-tech firms show 'Public'.
- **Headcount**: Estimates from LinkedIn and aggregator snippets; treat as ±30%.
- **Confidence**: Each profile carries per-field confidence and a basis. 536 of 760 profiles used live web search; the rest rely on model knowledge and are flagged low/medium.
- **Freshness**: As of 25 Nov 2026. Events after mid-2026 depend on web search coverage and may be incomplete.
- **Files**: research_notes/Local AI Atlas/: data/companies.json & .csv, ontology.json, deals.json, profiles/, verification/, discovery/.

## Files

- `research_notes/Local AI Atlas/data/companies.json`: master dataset (all fields)
- `research_notes/Local AI Atlas/data/companies.csv`: spreadsheet version
- `research_notes/Local AI Atlas/data/directory.md`: every company by niche
- `research_notes/Local AI Atlas/data/ontology.json`, `deals.json`, `narrative.json`
- `research_notes/Local AI Atlas/profiles/`, `verification/`, `discovery/`: raw agent outputs and notes
