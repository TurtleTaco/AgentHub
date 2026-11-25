"""Curate merged candidates: manual merges, exclusions, additions, batching.
Usage: python3 curate.py <notes_dir> <batch_size>
"""
import json, sys, os, re
notes, bs = sys.argv[1], int(sys.argv[2])
d = json.load(open(os.path.join(notes, "data", "candidates.json")))
by = {r["name"]: r for r in d}

MERGE = {  # target name -> names folded into it
    "Meta Platforms": ["Meta (Llama)"],
    "Samsung Electronics": ["Samsung (SAIL Montreal TRM)"],
    "NAVER Cloud (HyperCLOVA X)": ["Naver (HyperCLOVA X SEED)"],
    "Tensordyne (formerly Recogni)": ["Recogni"],
    "Sony Group": ["Sony AITRIOS"],
    "Bosch": ["Bosch Sensortec"],
    "Alibaba Qwen": ["T-Head (Alibaba)"],
    "Huawei": ["HiSilicon"],
    "Inferact": ["vLLM (vllm-project)"],
}
RENAME = {"Alibaba Qwen": "Alibaba Group", "Siemens Industrial Edge": "Siemens",
          "Meta Platforms": "Meta", "NAVER Cloud (HyperCLOVA X)": "NAVER"}
EXCLUDE_COMMUNITY = """Edge AI and Vision Alliance|EDGE AI FOUNDATION (formerly tinyML Foundation)|LF Edge|KServe|llm-d|RWKV Project|SillyTavern (open-source community)|KoboldCpp (LostRuins, open-source)|oobabooga (text-generation-webui)|AUTOMATIC1111 (Stable Diffusion WebUI)|lllyasviel (Fooocus / Forge / ControlNet)|Page Assist (n4ze3m, open-source)|Alpaca (Jeffser, open-source)|Enchanted (open-source, gluonfield)|Leon AI (open-source)|Reor (open-source project)|Krita AI Diffusion (Acly)|Pinokio (cocktailpeanut)|Buzz (Chidi Williams)|Aider (Paul Gauthier)|k2-fsa (sherpa-onnx / Next-gen Kaldi)|EuroLLM (Unbabel-led consortium)|Swiss AI Initiative (Apertus)|Latam-GPT (CENIA)|AI Singapore (SEA-LION)|BAAI (Beijing Academy of AI)|Shanghai AI Laboratory (InternLM)|MBZUAI Institute of Foundation Models|EleutherAI|TAIDE|BharatGen|Open Home Foundation|Frigate|Upscayl|DiffusionBee (Divam Gupta)|VoiceInk (Prakash Joshi Pax)|PocketPal AI (Asghar Ghorbani)|MLC (MLC LLM project)|Sahabat-AI|OpenClaw Foundation|hexgrad (Kokoro)|Coqui|Xnor.ai|Mainframe (fullmoon)|Enclave AI (Piotr Gorzelany)|Chatbox AI (Bin Huang)|Draw Things (Liu Liu)|Jacaranda Health (UlizaLlama)|Layla Network|Sanctum (desktop app; publisher reportedly QXYZ Labs)|Good Snooze (MacWhisper)""".split("|")
EXCLUDE_GENERIC = """LangChain|LlamaIndex|CrewAI|Langfuse|Galileo|Arize AI (Phoenix)|Comet|Portkey|TensorZero|Outerbounds|Union.ai|ZenML|Weights & Biases|MosaicML|Glean|Snowflake (Arctic Embed)|Salesforce (xLAM)|Teradata|Fireworks AI|Cast AI|Verkada|Determined AI|BerriAI (LiteLLM)|Activepieces|Weaviate|MinIO|Intrinsic (Alphabet)|Vicarious|Tesla|Skydio|Rhombus|Yellow.ai|ServiceNow|SAP|C3 AI|Kilo Code|Roo Code, Inc.|Zed Industries|Anomaly (OpenCode)|Glass Devtools (Void)|Open Interpreter, Inc.|Cline Bot Inc.""".split("|")
ADD = [{"name": "Lambda", "website": "https://lambda.ai", "hq_country": "United States", "type": "scaleup",
        "status": "active", "segments": ["onprem-hardware"], "found_by": ["coordinator"],
        "one_liners": ["GPU cloud plus on-prem clusters and workstations for AI"], "local_ai_angles": ["Sells private, customer-owned GPU clusters"], "sources": ["https://lambda.ai"], "aliases": []}]

def get(n):
    if n not in by:
        print("MISSING", n); return None
    return by[n]

for tgt, srcs in MERGE.items():
    t = get(tgt)
    for s in srcs:
        r = get(s)
        if not (t and r): continue
        t["aliases"] = sorted(set(t["aliases"]) | {r["name"]} | set(r["aliases"]))
        for k in ("segments", "found_by"):
            t[k] = sorted(set(t[k]) | set(r[k]))
        for k in ("one_liners", "local_ai_angles", "sources"):
            t[k] = list(dict.fromkeys(t[k] + r[k]))[:8]
        r["_drop"] = "merged into " + tgt

excluded = []
for n in EXCLUDE_COMMUNITY:
    r = get(n)
    if r: r["_drop"] = "community/individual project, consortium or non-company"
for n in EXCLUDE_GENERIC:
    r = get(n)
    if r: r["_drop"] = "generic tooling or cloud-first; local AI not a core offering"

keep = []
for r in d:
    if r.get("_drop"):
        excluded.append({"name": r["name"], "reason": r["_drop"], "website": r.get("website")})
    else:
        if r["name"] in RENAME:
            r["aliases"] = sorted(set(r["aliases"]) | {r["name"]}); r["name"] = RENAME[r["name"]]
        keep.append(r)
keep += ADD
for r in keep:
    r["id"] = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
    segs = [s for s in r["segments"] if s != "international"] or r["segments"]
    r["primary_segment"] = segs[0] if len(segs) == 1 else max(segs, key=lambda s: sum(1 for f in r["found_by"] if f == s) or 0.5)
ids = [r["id"] for r in keep]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]

order = ["bigtech", "onprem-hardware", "edge-silicon", "selfhosted-inference-llmops", "private-ai-platforms",
         "vertical-regulated", "efficient-models", "on-device-sdks", "consumer-local-apps", "industrial-edge", "international"]
keep.sort(key=lambda r: (order.index(r["primary_segment"]) if r["primary_segment"] in order else 99, r["name"].lower()))
json.dump(keep, open(os.path.join(notes, "data", "curated_candidates.json"), "w"), indent=1, ensure_ascii=False)
json.dump(excluded, open(os.path.join(notes, "data", "excluded_at_curation.json"), "w"), indent=1, ensure_ascii=False)

os.makedirs(os.path.join(notes, "profiles", "input"), exist_ok=True)
batches = [keep[i:i + bs] for i in range(0, len(keep), bs)]
for i, b in enumerate(batches, 1):
    slim = [{"id": r["id"], "name": r["name"], "aliases": r["aliases"], "website": r["website"], "hq_country": r["hq_country"],
             "discovery_status": r["status"], "segments": r["segments"], "discovery_notes": r["one_liners"] + r["local_ai_angles"],
             "discovery_sources": r["sources"][:4]} for r in b]
    json.dump(slim, open(os.path.join(notes, "profiles", "input", f"batch-{i:02d}.json"), "w"), indent=1, ensure_ascii=False)
    segs = sorted(set(r["primary_segment"] for r in b))
    print(f"batch-{i:02d}: {len(b)} [{', '.join(segs)}] {b[0]['name']} .. {b[-1]['name']}")
print("kept", len(keep), "excluded", len(excluded))
