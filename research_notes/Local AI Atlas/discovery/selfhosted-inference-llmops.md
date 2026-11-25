# Self-hosted inference, LLMOps and on-prem AI infrastructure software (segment: selfhosted-inference-llmops)

Companion dataset: `selfhosted-inference-llmops.json` (154 entries: 123 in this segment, 31 out-of-segment local-AI companies tagged with their best-fit segment).

**How this was researched, and how far to trust it.** The shared web-search budget ran out after 12 queries in this session, and WebFetch could not reach any company site, because the sandbox's network allowlist blocks those hosts. So only the facts in the "Cited Findings" bullets below were checked live this session. Everything else in the JSON comes from the researcher's prior knowledge (training data through about mid-2026). That covers most one-liners, HQ countries and pre-2026 acquisitions. Those entries cite the company homepage or GitHub repo, not a news article. Status strings marked `[UNVERIFIED]` or `[prior knowledge, not re-verified]` should be fact-checked before they go into the final report.

## (a) Inference engines and model-serving companies

### Takeaway
Inference engines consolidated around two open-source projects in 2025–2026: vLLM and SGLang. Each now has a well-funded commercial company behind it (Inferact for vLLM, RadixArk for SGLang). A KV-cache layer company, TensorMesh (LMCache), sits next to them. Modular is consolidating the serving layer: it acquired BentoML in February 2026.

### Cited Findings
- Inferact, founded by vLLM maintainers, raised a $150M seed round at an $800M valuation on Jan 22, 2026. Sources name a16z and Lightspeed as co-leads (ZoomInfo names Altimeter instead). CEO Simon Mo is one of vLLM's creators. Inferact plans a paid serverless vLLM, and the upstream project stays open source. — [TechCrunch](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/); [SiliconANGLE](https://siliconangle.com/2026/01/22/inferact-launches-150m-funding-commercialize-vllm/); [a16z](https://a16z.com/announcement/investing-in-inferact/)
- RadixArk, the commercial spinout of SGLang, launched on May 5, 2026 with a $100M seed at a $400M post-money valuation. Accel led, Spark co-led, and NVentures (NVIDIA) participated. Founders are Ying Sheng and Banghua Zhu. SGLang began in Ion Stoica's lab at UC Berkeley in 2023. RadixArk keeps SGLang free and plans to make money from managed hosting and from tools built on SGLang and its Miles project. — [SiliconANGLE](https://siliconangle.com/2026/05/05/nvidia-amd-back-100m-round-ai-tooling-startup-radixark/); [TechCrunch (Jan 2026)](https://techcrunch.com/2026/01/21/sources-project-sglang-spins-out-as-radixark-with-400m-valuation-as-inference-market-explodes)
- The January 2026 TechCrunch report on RadixArk ("upwards of $160M at about $1B") does not match the round announced in May ($100M at $400M). — [TechCrunch](https://techcrunch.com/2026/01/21/sources-project-sglang-spins-out-as-radixark-with-400m-valuation-as-inference-market-explodes)
- Modular acquired BentoML, announced Feb 10, 2026. BentoML stays Apache-2.0, Modular says it is used by more than 10,000 organizations, and BentoML calls the deal a "strategic product acquisition". — [Modular blog](https://www.modular.com/blog/bentoml-joins-modular); [BentoML blog](https://bentoml.com/blog/bentoml-is-joining-modular)
- One low-reliability source claims Qualcomm closed an all-stock acquisition of Modular around July 2026. No other source confirms it. — [usagepricing.com](https://www.usagepricing.com/blueprint/activity/bentoml-2026-07-29-qualcomm-modular-acquisition)
- AMD completed its acquisition of MK1 (Mountain View, CA), announced Nov 10, 2025. MK1's Flywheel inference engine processes more than 1T tokens per day and is built for the memory architecture of AMD Instinct GPUs. Co-founders are Paul Merolla (a Neuralink co-founder) and Thong Wei Koh. — [AMD blog](https://www.amd.com/en/blogs/2025/amd-acquires-mk1-to-advance-ai-inference-performance.html)

### Inferences
- Other companies in this layer (from prior knowledge, not re-verified): Neural Magic, Red Hat AI Inference Server, llm-d, KServe, FriendliAI, Doubleword (formerly TitanML), Clarifai Local Runners, Baseten self-hosted, the Together and Fireworks VPC offerings, Hugging Face (TGI/HUGS/Dell Enterprise Hub), Ollama, llama.cpp/ggml, LocalAI, Xinference, GPUStack, Exo, Kalavai, ZML, Kog, Pipeshift, Simplismart, TrueFoundry, Tensorfuse, Beam/beta9, Gimlet Labs, SiliconFlow, Infinigence, Moreh, Seldon, Wallaroo and Gcore Everywhere Inference.
- The pattern: the open-source engine becomes a company, then GPU vendors acquire or invest. NVIDIA bought OctoAI, Deci, Lepton and CentML. AMD bought Nod.ai, Silo AI, Brium and MK1. NVentures invested in RadixArk. Chip vendors increasingly own the software layer that self-hosting customers depend on.

### Gaps
- Not verified this session: the status of Lamini (prior knowledge says founder Sharon Zhou joined AMD in 2025; whether the company was acquired is unknown), Inferless, Mystic AI and Mako (website and HQ also unconfirmed). The same goes for websites and HQs of Inferact, RadixArk and dstack.
- The Qualcomm–Modular report needs primary confirmation. Status in the JSON is flagged `[UNVERIFIED]`.
- Funding figures for Modular, Baseten, Fireworks, TensorMesh, Doubleword, Pipeshift and Simplismart were not re-checked, so none are in the JSON.

## (b) GPU orchestration and private AI infrastructure software

### Takeaway
NVIDIA now owns the most widely used schedulers for customer-owned GPU clusters: Run:ai (Kubernetes) and SchedMD's Slurm (HPC). Independent options include Rafay, Mirantis k0rdent, Spectro Cloud, dstack, SkyPilot, Exostellar, ClearML, Lablup Backend.AI and GPUStack. The rest of the market is platform vendors (Nutanix, VMware/Broadcom, Red Hat, SUSE, Canonical) and AI data platforms (VAST, WEKA, Hammerspace, NetApp, DDN, MinIO).

### Cited Findings
- NVIDIA acquired SchedMD, the developer of Slurm, announced Dec 15, 2025, with undisclosed terms. NVIDIA committed to keeping Slurm open source and vendor-neutral. SchedMD was founded in 2010 in Livermore, CA, has about 40 employees, and counts CoreWeave and the Barcelona Supercomputing Center as customers. — [NVIDIA blog](https://blogs.nvidia.com/blog/nvidia-acquires-schedmd); [Network World](https://www.networkworld.com/article/4106930/nvidia-moves-deeper-into-ai-infrastructure-with-schedmd-acquisition.html)
- Analysts quoted by Network World expect NVIDIA to steer Slurm toward features like tighter NCCL integration, but not toward immediate lock-in. — [Network World](https://www.networkworld.com/article/4106930/nvidia-moves-deeper-into-ai-infrastructure-with-schedmd-acquisition.html)

### Inferences
- From prior knowledge, not re-verified: NVIDIA completed the Run:ai acquisition around the end of 2024 and later open-sourced the KAI Scheduler ([GitHub](https://github.com/NVIDIA/KAI-Scheduler)). Bright Computing (2022) became NVIDIA Base Command Manager. With Run:ai, Bright and Slurm, NVIDIA controls the main cluster-management layers for on-prem GPU fleets.
- Storage and memory vendors (WEKA Augmented Memory Grid, VAST, Hammerspace, Kove software-defined memory) increasingly sell themselves as KV-cache and inference accelerators. This overlaps with LMCache/TensorMesh.

### Gaps
- Product names are from prior knowledge and were not re-checked: Mirantis k0rdent AI, Spectro Cloud PaletteAI, Nutanix Enterprise AI, Canonical inference snaps, SUSE AI, Cast AI AI Enabler, Avesha Elastic GPU Service, Fixstars AIBooster and Rapt AI.
- The CNCF landscape, a16z and Menlo market maps, and the NVIDIA and Red Hat partner pages could not be fetched (network blocked), so this list has not been cross-checked against them.

## (c) Foundation-model vendors selling VPC, on-prem or air-gapped deployment

### Takeaway
Sovereignty is driving consolidation among private-deployment model vendors. Cohere is combining with Aleph Alpha (announced Apr 2026, definitive agreement Sep 2026). Mistral, LightOn, Upstage, Sakana, Writer, AI21, Reka, Contextual AI, Arcee, Poolside, Tabnine, Deepgram and Speechmatics also sell private deployments.

### Cited Findings
- Cohere agreed on Apr 24, 2026 to acquire Aleph Alpha. The FT valued the combined company at about $20B. Cohere's shareholders would hold about 90% and Aleph Alpha's about 10%. Schwarz Group committed $600M to Cohere's Series E. — [Dealroom](https://dealroom.co/news/127656-cohere-acquires-aleph-alpha-and-raises-600-million-from-its-top-backer/); [Reuters via Yahoo](https://finance.yahoo.com/sectors/technology/articles/canadas-cohere-germanys-aleph-alpha-052106831.html)
- The definitive business combination agreement was signed Sep 16, 2026. It still needed regulatory approval and was expected to close later in 2026. The combined company keeps the Cohere name, has dual HQs in Berlin and Toronto, keeps Heidelberg as a research center, and will have more than 1,000 employees. — [TNW](https://thenextweb.com/news/cohere-aleph-alpha-definitive-agreement-transatlantic-sovereign-ai); [Dealroom](https://dealroom.co/news/154731-cohere-and-aleph-alpha-agree-to-combine-announced-2026/)
- The stated rationale is a sovereign alternative to US providers for regulated sectors and governments. Aleph Alpha brings customers such as SAP, Bosch and Deutsche Bank. TechCrunch called it "not an alliance between equals". — [Constellation Research](https://www.constellationr.com/insights/news/cohere-acquires-aleph-alpha-form-us-ai-counterweight); [TechCrunch](https://techcrunch.com/2026/04/25/why-cohere-is-merging-with-aleph-alpha/)

### Inferences
- From prior knowledge, not re-verified: AMD acquired Silo AI (2024) and Databricks acquired MosaicML (2023), so private-deployment model talent is also being absorbed by chip and data-platform companies. Late-2025 reports said NVIDIA was in talks to acquire AI21 and Intel was in talks to acquire SambaNova. Neither outcome was verified, so both are recorded as "active" with a note.

### Gaps
- No live confirmation this session of each vendor's current on-prem or air-gapped offering (Writer, Reka, Inflection, Arcee, Contextual, Poolside, Upstage, Sakana).
- It is still unknown whether Cohere–Aleph Alpha has closed as of 2026-11-25.

## Acquisitions summary, and out-of-segment companies seen

### Takeaway
NVIDIA is the dominant acquirer: Run:ai, OctoAI, Deci, Lepton, CentML, SchedMD and Bright Computing. AMD is next: Nod.ai, Silo AI, Brium and MK1. Other notable deals are Red Hat–Neural Magic, Rubrik–Predibase, Modular–BentoML, Cohere–Aleph Alpha, CoreWeave–Weights & Biases, HPE–Determined AI, Intel–cnvrg.io and Databricks–MosaicML.

### Cited Findings
- Verified this session: NVIDIA–SchedMD, Dec 2025 ([NVIDIA](https://blogs.nvidia.com/blog/nvidia-acquires-schedmd)); AMD–MK1, Nov 2025 ([AMD](https://www.amd.com/en/blogs/2025/amd-acquires-mk1-to-advance-ai-inference-performance.html)); Modular–BentoML, Feb 2026 ([Modular](https://www.modular.com/blog/bentoml-joins-modular)); Cohere–Aleph Alpha, Apr/Sep 2026 ([TNW](https://thenextweb.com/news/cohere-aleph-alpha-definitive-agreement-transatlantic-sovereign-ai)).

### Inferences
- Acquisitions from prior knowledge, recorded in the JSON but not re-verified: Red Hat–Neural Magic (closed early 2025); NVIDIA–Run:ai (2024), OctoAI (2024), Deci (2024), Lepton (2025), CentML (2025) and Bright Computing (2022); AMD–Nod.ai (2023), Silo AI (2024) and Brium (2025); Rubrik–Predibase (2025); CoreWeave–W&B (2025); HPE–Determined AI (2021); Intel–cnvrg.io (2020); Databricks–MosaicML (2023).
- Lower confidence, flagged in the JSON: Hugging Face–ggml.ai/llama.cpp (2026), ClickHouse–Langfuse (2026), Cisco–NeuralFabric (2025).
- Seen but left out of the JSON: Mistral–Koyeb (early 2026, Koyeb is a serverless cloud); Cloudflare–Replicate (late 2025, cloud API); Elastic–Jina AI (2025); Cognition–Windsurf (2025). All are prior knowledge and unverified.
- Out-of-segment local-AI companies added to the JSON with their best-fit segment:
  - bigtech: NVIDIA, AMD, IBM, Cisco.
  - onprem-hardware: HPE, Dell, DDN, Pure Storage, Penguin Solutions, Liqid, GigaIO, SambaNova, Groq.
  - private-ai-platforms: Shakudo, Palantir, Domino, Dataiku, H2O.ai, Cloudera, DataRobot, Katonic, Prem AI, Zylon.
  - international: Zhipu, Sarvam.
  - vertical-regulated: Domyn.
  - efficient-models: Liquid AI, Multiverse, Pruna.
  - on-device-sdks: Nexa AI.
  - consumer-local-apps: LM Studio.

### Gaps
- Coverage is weakest on 2026 seed-stage inference startups beyond Inferact and RadixArk, on Chinese, Japanese and Korean on-prem inference vendors, and on the sovereign-AI infrastructure software vendors in Europe and the Gulf. All of these need live search.
- Excluded on purpose as cloud-only or GPU rental: Modal, RunPod, Cerebrium, Replicate, DeepInfra, Lambda cloud, CoreWeave, Nebius, Crusoe and Banana.dev (defunct 2024).
