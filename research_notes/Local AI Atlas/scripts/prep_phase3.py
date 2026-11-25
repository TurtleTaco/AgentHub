"""Prepare classification chunks and fact-check chunks from profiles.
Usage: python3 prep_phase3.py <notes_dir> <n_class_chunks> <n_fc_chunks> <fc_per_chunk>
"""
import json, glob, os, sys
notes, ncc, nfc, per = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
P = lambda *a: os.path.join(notes, *a)
prof, seen = [], set()
for f in sorted(glob.glob(P("profiles", "batch-*.json"))):
    for p in json.load(open(f)):
        if p.get("id") in seen: continue
        seen.add(p.get("id")); prof.append(p)
ins = [p for p in prof if p.get("verdict") in ("in", "borderline")]
print("profiles", len(prof), "in/borderline", len(ins))
os.makedirs(P("data", "classify-input"), exist_ok=True)
size = -(-len(ins) // ncc)
for i in range(ncc):
    with open(P("data", "classify-input", f"chunk-{i+1}.jsonl"), "w") as fh:
        for p in ins[i*size:(i+1)*size]:
            fh.write(json.dumps({"id": p["id"], "name": p.get("name"), "focus": p.get("focus"), "problem": p.get("problem"),
                "products": [f'{x.get("name")} ({x.get("category")}): {x.get("description")}' for x in (p.get("products") or []) if isinstance(x, dict)][:8],
                "layers": p.get("layers"), "deployment": p.get("deployment"), "modalities": p.get("modalities"), "customers": p.get("customers"),
                "differentiator": p.get("differentiator")}, ensure_ascii=False) + "\n")
    print("class chunk", i+1, len(ins[i*size:(i+1)*size]))
# fact-check selection: independent or recently-acquired non-public companies not already high-confidence searched
def indep(p): return (p.get("org_type") in ("startup", "scaleup", "open-source-company") or (p.get("org_type") not in ("public", "big-tech", "subsidiary")))
cand = [p for p in ins if indep(p) and not (p.get("basis") == "searched" and (p.get("confidence") or {}).get("funding") == "high")]
def score(p):
    f = p.get("total_funding_usd_m") or 0
    e = p.get("employees") or 0
    return (1 if p.get("verdict") == "in" else 0, f + e / 5)
cand.sort(key=score, reverse=True)
pick = cand[: nfc * per]
os.makedirs(P("verification", "input"), exist_ok=True)
keys = ["id", "name", "website", "hq_city", "hq_country", "founded", "status", "status_detail", "funding_stage", "total_funding_usd_m", "last_round", "valuation_usd_m", "employees", "employees_band", "confidence", "basis"]
for i in range(nfc):
    chunk = pick[i::nfc]  # interleave so each chunk mixes big and small
    with open(P("verification", "input", f"fc-{i+1}.jsonl"), "w") as fh:
        for p in chunk: fh.write(json.dumps({k: p.get(k) for k in keys}, ensure_ascii=False) + "\n")
    print("fc chunk", i+1, len(chunk))
print("fact-check candidates", len(cand), "picked", len(pick))
