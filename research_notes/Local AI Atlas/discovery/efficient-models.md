# Efficient Models (segment key: efficient-models)

Companion to `efficient-models.json` (158 entries: 109 efficient-models, 25 bigtech, 24 out-of-segment). Method note: 15 web searches were run before the shared web-search budget for this turn was used up. WebFetch could not reach scmp.com, siliconangle.com, dealroom.co or storagenewsletter.com because the session network blocks them. Many entries therefore rest on training knowledge (cutoff mid-2026). For those, the cited source is the company's official site, GitHub or Hugging Face page, not a news article. Facts I could not re-verify are listed under Gaps.

## Optimization / compression / compilation companies

### Takeaway
Big chip vendors have bought up most of the first wave of model-optimization startups: NVIDIA took OmniML, Deci, OctoAI and CentML; AMD took Nod.ai, Mipsology, Brium and Silo AI; Red Hat took Neural Magic; Rebellions took SqueezeBits; Qualcomm took Edge Impulse. Independent capital has concentrated in Multiverse Computing, alongside a new 2026 wave of compression and low-bit startups: PrismML, Ora Computing and Refiant AI.

### Cited Findings
- Multiverse Computing (Spain) announced a Series C of up to $570M (€500M) on 27 Jul 2026, at a $1.7B pre-money valuation. Its CompactifAI product uses tensor networks to compress models. Its Series B was €189M (~$215M) in Jun 2025. Sources disagree on the post-money valuation: Sifted reports €2B and Sacra $2.3B. — [Multiverse](https://multiversecomputing.com/resources/multiverse-computing-announces-series-c-fundraising-targeting-up-to-usd570m-eur500m-to-power); [Quantum Insider](https://thequantuminsider.com/2026/07/27/multiverse-computing-announces-series-c-fundraising-targeting-up-to-570-million/); [TechCrunch 2025](https://techcrunch.com/2025/06/12/multiverse-computing-raises-215m-for-tech-that-could-radically-slim-ai-costs); [Sacra](https://sacra.com/c/multiverse-computing/); [Sifted](https://sifted.eu/articles/multiverse-computing-series-c-unicorn/)
- PrismML is a Caltech spinout backed by Khosla Ventures. It came out of stealth on 31 Mar 2026 with 1-bit Bonsai open-weight LLMs (8B/4B/1.7B, Apache 2.0); the 8B model is about 1.15 GB. Ternary Bonsai (1.58-bit) followed on 16 Apr 2026. Reported seed figures vary: $16.25M in one report, $22.25M in another. — [PrismML](https://prismml.com/news/prismml-launches-worlds-first-1-bit-ai-model); [PrismML ternary](https://prismml.com/news/ternary-bonsai); [The Register](https://www.theregister.com/2026/04/04/prismml_1bit_llm/); [TechCrunch](https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/)
- Ora Computing (Vienna) raised a €3.5M seed in Jun 2026, led by Constructor Capital and Greencode Ventures, for model optimization and compression. — [tech.eu](https://tech.eu/2026/06/24/ora-computing-raises-eur35m-to-build-the-efficiency-layer-of-the-ai-stack/)
- Refiant AI raised a $5M seed in Apr 2026, led by VoLo Earth, for "nature-inspired" compression that it says cuts energy use by more than 80%. Its HQ and website were not confirmed. — [SiliconANGLE (search snippet)](https://siliconangle.com/?p=737911)
- Rebellions, the Korean NPU maker, acquired SqueezeBits, a quantization and optimization startup. The coverage is dated Jul 2026. — [cloudnews.tech](https://cloudnews.tech/rebellions-acquires-squeezebits-to-complete-the-ai-inference-cycle/); [StorageNewsletter](https://www.storagenewsletter.com/2026/07/10/rebellions-acquires-ai-inference-optimization-leader-squeezebits-to-deliver-full-stack-ai-infrastructure/)
- AMD acquired Brium (AI software optimization across hardware) in Jun 2025. — [TechCrunch](https://techcrunch.com/2025/06/04/amd-takes-aim-at-nvidias-ai-hardware-dominance-with-brium-acquisition)
- NVIDIA acquired OmniML, which compressed models for edge hardware. — [DCD](https://datacenterdynamics.com/en/news/nvidia-acquires-omniml-for-ai-edge-workloads)
- Pruna AI raised a $6.5M seed led by EQT Ventures in Nov 2024 and open-sourced its optimization framework in Mar 2025. It also sells an enterprise tier that includes an optimization agent. — [TechCrunch](https://techcrunch.com/2025/03/20/pruna-ai-open-sources-its-ai-model-optimization-framework); [Munich Startup](https://www.munich-startup.de/en/106164/pruna-ai-seed-round/)
- Embedl (Sweden) raised a €5.5M pre-Series A in Jun 2025 to launch Embedl Hub. Its Model Optimization SDK targets defence, automotive and robotics. — [tech.eu](https://tech.eu/2025/06/18/embedl-raises-eur55m-to-boost-ai-efficiency-in-embedded-systems/)
- Fastino raised a $17.5M seed led by Khosla in May 2025, on top of a $7M pre-seed led by M12 and Insight. It builds task-specific models trained on gaming GPUs. — [TechCrunch](https://techcrunch.com/2025/05/07/fastino-trains-ai-models-on-cheap-gaming-gpus-and-just-raised-17-5m-led-by-khosla)
- ThirdAI's last recorded round is a $6M seed from Aug 2021. A CB Insights item dated Feb 2026 quotes its CEO, which suggests the company still operates. — [TechCrunch](https://techcrunch.com/2021/08/13/thirdai-raises-6m-to-democratize-ai-to-any-hardware); [CB Insights](https://www.cbinsights.com/company/third-ai)
- Unsloth was founded in 2023 and is backed by Lightspeed. It is an open-source tool for local fine-tuning and quantization. PitchBook lists a Jul 2026 round with no amount disclosed. — [Lightspeed](https://lsvp.com/company/unsloth/); [PitchBook](https://pitchbook.com/profiles/company/590107-78)
- Distil Labs (Berlin) turns a prompt plus a few dozen examples into a fine-tuned small model. — [WeAreDevelopers](https://www.wearedevelopers.com/videos/1654-distil-labs-small-model-training-made-simple)
- EdgeRunner AI (SF) raised a $5.5M seed for offline, task-specific "ultra-efficient language models". — [VMblog](https://vmblog.com/bylines/edgerunner-ai-emerges-from-stealth-with-5-5m-seed-funding-to-build-generative-ai-for-the-edge/)

### Inferences
- The optimization layer is consolidating into hardware vendors, who want models tuned for their own silicon. The independents left either have very large rounds (Multiverse), give away an open-source core (Pruna, Unsloth) or sell into defence and embedded markets (Embedl, Latent AI, EdgeRunner).
- Low-bit work is moving from post-training quantization to natively trained 1-bit and ternary models: PrismML, Microsoft BitNet, TII Falcon-E and ModelBest BitCPM.

### Gaps
- No 2026 information was found for CLIKA, Deeplite, ENOT or Nyun AI. CLIKA's and ENOT's HQ countries are left null. I have an unverified recollection that STMicroelectronics acquired Deeplite; its status is marked "unknown".
- Nota AI's possible KOSDAQ listing (2025) is unverified, so it is typed as scaleup.
- I believe TitanML rebranded as Doubleword, but did not re-verify it this session.
- I did not re-verify the following acquisitions this session: CentML by NVIDIA (2025), Neuton.ai by Nordic (2025), Edge Impulse by Qualcomm (2025), Jina AI by Elastic (2025) and Predibase by Rubrik (2025).
- The Taalas acquisition by AMD rests on one aiweekly.co alert and is marked "reported; unverified".
- Mobius Labs (HQQ), Nolano AI and deepgrove (ternary models) have status "unknown".

## Efficient-architecture and small-model labs

### Takeaway
The main architecture bets for local AI are hybrid SSM/Mamba models (Liquid, Zyphra, Cartesia, AI21 Jamba, TII Falcon-H1, IBM Granite 4, NVIDIA Nemotron), diffusion LLMs (Inception, Celeris, Google DiffusionGemma), and tiny recursive or brain-inspired models (Sapient HRM, Samsung TRM). Arcee and Reflection AI became US open-weight standard-bearers in 2026.

### Cited Findings
- Liquid AI raised $250M led by AMD in Dec 2024. Search snippets also report LFM2.5 (Jan 2026), LFM2.5-8B-A1B (Aug 2026), LFM3 (Oct 2026) and a Mercedes-Benz MBUX partnership; the LFM3 details and the Qualcomm deal are unverified. — [Liquid AI](https://www.liquid.ai/blog/we-raised-250m-to-scale-capable-and-efficient-general-purpose-ai); [SiliconANGLE](https://siliconangle.com/2024/12/13/liquid-ai-raises-250m-led-amd-build-new-type-generative-ai-model)
- Zyphra released Zamba2-VL vision-language models (1.2B/2.7B/7B, Mamba2 backbone). A digest reports ZAYA1-8B (May 2026), an SSM-MoE hybrid. — [Zyphra](https://www.zyphra.com/post/zamba2-vl)
- TII's Falcon-H1R 7B is a hybrid Mamba-Transformer model. Falcon-E is a 1.58-bit edge model family. — [VentureBeat](https://venturebeat.com/technology/tiis-falcon-h1r-7b-can-out-reason-models-up-to-7x-its-size-and-its-mostly); [Falcon blog](https://falcon-lm.github.io/blog/falcon-edge)
- Inception raised $50M in Nov 2025 and launched Mercury 2, a reasoning diffusion LLM, in Feb 2026. Its weights appear to be closed, so it is borderline for this scope. — [TechCrunch](https://techcrunch.com/2025/11/06/inception-raises-50-million-to-build-diffusion-models-for-code-and-text); [The Decoder](https://the-decoder.com/inception-launches-mercury-2-the-first-diffusion-based-language-reasoning-model/)
- Celeris came out of stealth on 24 Jul 2026 with the Celeris-1 diffusion LLM; its licence is unknown. Google's DiffusionGemma is open under Apache 2.0. — [Dealroom](https://app.dealroom.co/news/note/celeris-launches-celeris-1-a-diffusion-llm-built-for-speed-1); [The Decoder](https://the-decoder.com/googles-new-open-model-diffusiongemma-generates-text-from-noise-instead-of-word-by-word/)
- Arcee released the Trinity family (Nano/Mini/Large) under Apache-2.0. A Sept 2026 round reportedly valued it above $1B. — [VentureBeat](https://venturebeat.com/ai/arcee-aims-to-reboot-u-s-open-source-ai-with-new-trinity-models-released); [TechCrunch](https://www.techcrunch.com/2026/01/28/tiny-startup-arcee-ai-built-a-400b-open-source-llm-from-scratch-to-best-metas-llama/)
- Reflection AI released Beam 1.0 open weights in Oct 2026. Reported dates differ between 5 and 16 Oct. — [AI Business](https://aibusiness.com/foundation-models/reflection-s-beam-model-signals-deepening-split)
- Deep Cogito's Cogito v2.1 (671B) is built on a DeepSeek base. — [TechCrunch](https://techcrunch.com/2025/04/08/deep-cogito-emerges-from-stealth-with-hybrid-ai-reasoning-models)
- ModelBest released BitCPM-CANN, 1.58-bit models trained on Ascend 910B. — [DEV](https://dev.to/gentic_news/modelbest-drops-bitcpm-cann-first-158-bit-llm-on-ascend-910b-3llf)
- Microsoft's BitNet b1.58 2B4T was the first open native 1-bit LLM at 2B scale. — [arXiv](https://arxiv.org/html/2504.12285v1)

### Inferences
- Most "local-first" labs pair open small weights with a paid edge SDK or enterprise deployment, for example Liquid LEAP, Cartesia Edge and Moondream. Open weights act as distribution, and revenue comes from enterprise or OEM licensing.

### Gaps
- Several models and claims rest on training knowledge only: Essential AI's open model (Rnj-1), Manifest AI's Brumby / power retention, Pathway's BDH, Sapient's HRM, Kyutai's Pocket TTS, Trillion Labs, Motif, TildeOpen, Bielik and Velvet.
- I recall Zhipu and MiniMax listing in Hong Kong in early 2026, but could not verify it; both are typed as scaleup.
- Aleph Alpha's 2025–26 corporate changes were not checked.
- No list of Chinese on-device small-model startups was compiled beyond ModelBest, because the SCMP article was blocked.

## Open-weight vendors widely self-hosted (big tech and Chinese labs)

### Takeaway
Big tech is the main source of open weights that run locally. Meta Llama, Google Gemma (including Gemma 3n on-device and DiffusionGemma), Microsoft Phi and BitNet, IBM Granite 4, OpenAI gpt-oss, NVIDIA Nemotron, Apple and Alibaba Qwen are tagged "bigtech". Chinese labs that are not big tech are tagged efficient-models: DeepSeek, Moonshot, Zhipu, MiniMax, StepFun, 01.AI and Baichuan.

### Cited Findings
- A May 2026 digest reports that Qwen 3.5 includes hybrid state-space layers, Upstage Solar Open 2 is a 250B-A15B hybrid, OLMo 3 is a hybrid, and NVIDIA's Nemotron 3 Super is a 120B hybrid Mamba MoE. — [open-weight digest](https://ice-ice-bear.github.io/posts/2026-05-10-open-weight-models-digest/); [Raschka](https://sebastianraschka.com/blog/2026/notable-open-weight-models-this-week.html)
- Mistral released Voxtral TTS, an open-weight ~4B model, in Mar 2026. — [VentureBeat](https://venturebeat.com/ai/mistral-ai-just-released-a-text-to-speech-model-it-says-beats-elevenlabs-and)

### Inferences
- Big-tech small models (Gemma 3n, Phi, Llama 3.2 1B/3B, Qwen3 0.6–4B, Granite 4 Nano, gpt-oss-20b) set the baseline that small-model startups must beat.

### Gaps
- Release details for each big-tech model were not re-verified this session; the sources are official model hubs.

## 1-bit/sparse startups, small speech/TTS models and embedding companies

### Takeaway
Most open on-device TTS is coming from small teams: hexgrad Kokoro, KittenML, Neuphonic, Gradium Phonon, Supertone Supertonic, Kyutai, Canopy, Nari, Resemble Chatterbox and Sesame CSM. For local RAG embeddings, Nomic, Mixedbread, BAAI BGE and Qwen3-Embedding are the default open choices, while Jina has licensing caveats and is now owned by Elastic.

### Cited Findings
- Gradium, a Paris spinout of Kyutai, open-sourced Phonon. The 31M English model is Apache 2.0 and the 40M multilingual model is CC BY-NC. Both run on phones, laptops, boards and browsers. — [Gradium](https://gradium.ai/blog/release-phonon-open-weight); [MarkTechPost](https://www.marktechpost.com/2026/10/22/gradium-phonon-31m-on-device-tts/)
- Supertone's Supertonic 3 runs on-device through ONNX in 31 languages. One source gives 99M parameters; this is unconfirmed. KittenTTS is under 25 MB. NeuTTS ships GGUF models for on-device use. — [mer.vin](https://mer.vin/2026/06/supertonic-3-99m-on-device-tts-with-onnx-31-languages-and-1200-chars-sec/); [NYU RITS](https://rits.shanghai.nyu.edu/ai/kittentts-state-of-the-art-voice-synthesis-in-under-25-mb/); [Pinggy](https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/)
- nomic-embed-text (Apache-2.0, ~0.3 GB) installs from Ollama, and v2-moe is fully open. Jina v3 is CC-BY-NC. Practical guides call BGE-M3 and Qwen3-Embedding strong local choices. — [PromptQuorum](https://www.promptquorum.com/power-local-llm/best-embedding-models-local-rag-2026); [SurrealDB](https://surrealdb.com/blog/embedding-models-comparison); [Zilliz](https://www.zilliz.com/blog/choose-embedding-model-rag-2026)
- NobodyWho (Copenhagen) raised a €2M pre-seed in Dec 2025 for running small models locally on laptops and phones. — [tech.eu](https://tech.eu/2025/12/17/nobodywho-raises-eur2m-to-challenge-big-techs-cloud-ai-with-slms-for-local-devices/)
- Mirai raised a $10M seed led by Uncork in Feb 2026 for an on-device inference layer. — [Pulse 2.0](https://pulse2.com/mirai-10-million-seed-funding-raised-for-building-ai-capability-layer/amp/)

### Inferences
- In speech, sub-100M open models are now good enough for production on-device use, which squeezes API-only TTS vendors at the edge.

### Gaps
- Sparse-model startups are thin: ThirdAI and Numenta have unclear status, and Neural Magic now sits inside Red Hat. Cerebras REAP-pruned MoE checkpoints were noted but left out, since Cerebras is a cloud and hardware company.
- Several companies were seen but excluded or not added. Voyage AI (bought by MongoDB, 2025) is API-centric and was excluded. Smallest.ai is cloud voice AI and was excluded. InVerse, reportedly acquired by OpenVenture in Sept 2025, was left out because the reports conflict. Domyn/iGenius, Krutrim, Writer (Palmyra), Katanemo, Oumi, Axolotl, Radical Numerics and Adaption Labs could not be verified and were not added. Community quantizers (TheBloke, bartowski) are individuals, not companies.
- HQ is null for several entries: Mirai, Tiiny AI, Conway, Celeris, Refiant, Cactus, Fish Audio, KittenML, hexgrad, deepgrove, Nolano, ENOT, CLIKA, Neuton.ai and the RWKV/Recursal project.
- Out-of-segment entries added with their best-fit keys: Cohere, Aleph Alpha and Prem AI (private-ai-platforms); Predibase, Modular and ggml.ai (selfhosted-inference-llmops); Nexa AI, Mirai, Cactus, NobodyWho, Zetic.ai, Picovoice and Argmax (on-device-sdks); Menlo/Jan, Tether QVAC and Conway (consumer-local-apps); Tiiny AI (onprem-hardware); Taalas (edge-silicon); Edge Impulse, Neuton.ai, Xailient and Roboflow (industrial-edge); and G42 Inception/Jais (international).
