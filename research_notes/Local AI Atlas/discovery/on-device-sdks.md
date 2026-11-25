# On-Device AI Runtimes, SDKs and Engines (segment: on-device-sdks)

Companion to `on-device-sdks.json` (83 entries: 45 tagged `on-device-sdks`, 38 tagged to other segments). Research date 2026-11-25.

**Method and limits.** About 25 web searches before the shared WebSearch budget for this run (200 calls across all agents) ran out. Every WebFetch failed: the sandbox's network rules block hosts such as runanywhere.ai, nobodywho.ai, qualcomm.com and ycombinator.com. So most facts come from search-result summaries, not full pages. The YC directory and Qualcomm AI Hub partner pages could not be enumerated directly. Facts marked [prior knowledge] were not re-verified in this session. For those entries the JSON `sources` field holds only the company's own site or GitHub repo.

## On-device LLM runtimes / SDKs

### Takeaway
A crowded 2024–2026 startup wave (Cactus, RunAnywhere, Mirai, ZETIC.ai, NobodyWho, Fluid Inference, Cephable, TraceWeave) is building SDKs on top of open runtimes (llama.cpp, MLX, ExecuTorch, LiteRT). It is consolidating fast. ggml.ai (llama.cpp) joined Hugging Face in Feb 2026, and Nexa AI was absorbed by Qualcomm in Mar 2026.

### Cited Findings
- Cactus (YC S25) runs local inference on phones, wearables and other low-power devices. Its v1 SDK adds an optional cloud fallback. — [InfoQ](https://www.infoq.com/news/2025/12/cactus-on-device-inference/); [HF blog](https://huggingface.co/blog/rshemet/cactus-on-device-inference)
- Cactus claims 70+ tok/s on iPhone 17 and Galaxy S25 Ultra and supports any GGUF model. It ships React Native, Flutter, Kotlin and Swift bindings (vendor claim). — [YC](https://ycombinator.com/companies/cactus)
- RunAnywhere (YC W26) offers one open-source SDK for multimodal on-device AI plus a control plane for model rollouts. It covers iOS, Android and React Native and has about 10.1k GitHub stars. — [YC Launch](https://www.ycombinator.com/launches/PFB-runanywhere-the-default-way-to-run-on-device-ai-at-scale)
- RunAnywhere's own blog ranks on-device SDK competitors. Those rankings are self-interested. — [RunAnywhere blog](https://www.runanywhere.ai/blog/best-ai-sdks-on-device-inference-2026)
- Nexa AI was acquired by Qualcomm. Its 12-person team joined in mid-March 2026, and the Nexa SDK continues under Qualcomm's GenieX framework. — [Qualcomm dev blog](https://www.qualcomm.com/developer/blog/2026/06/geniex-developer-preview); [Sina interview](https://t.cj.sina.com.cn/articles/view/2833534593/a8e44e8102001cuqe)
- Before the acquisition, Nexa SDK ran GPT-OSS-20B entirely on Snapdragon phones with 16GB+ RAM. — [Qualcomm blog](https://www.qualcomm.com/developer/blog/2025/11/nexa-ai-for-android-simple-way-to-bring-on-device-ai-to-smartphones-with-snapdragon)
- Mirai was founded by the creators of Reface and Prisma (Dima Shvets, Alexey Moiseenkov) and raised a $10M seed led by Uncork in Feb 2026. It builds a Rust inference engine (uzu) for Apple Silicon. It claims up to 37% faster generation and 59% faster prefill than MLX (vendor claim). HQ is reported as London by press and as San Francisco by Dealroom. — [TechCrunch](https://techcrunch.com/2026/02/19/co-founders-behind-reface-and-prisma-join-hands-to-improve-on-device-model-inference-with-mirai/); [Uncork](https://uncorkcapital.com/blog/to-the-edge-again-welcoming-mirai-to-the-uncork-portfolio); [GitHub](https://github.com/trymirai/uzu)
- Liquid AI launched LEAP v0 (Liquid Edge-AI Platform) and the Apollo app on 2025-07-15. Developers can add LFM2 models (from about 300MB) in roughly 10 lines of code. LEAP added AMD Ryzen AI laptop support in Aug 2025. — [Liquid blog](https://www.liquid.ai/en/blog/liquid-ai-launches-leap-and-apollo-bringing-edge-ai-to-every-developer); [BusinessWire](https://www.businesswire.com/news/home/20250818260821/en/Liquid%E2%80%99s-Edge-AI-Platform-LEAP-Expands-Support-to-Laptops-With-Best-in-Class-Performance-on-AMD-Ryzen%E2%84%A2-and-Ryzen-AI%E2%84%A2-Processors)
- ZETIC.ai (Korea, founded 2024) raised a seed round from Korea Investment Accelerator and TheVentures in May 2024. Its Melange platform, rebranded MLange at TechCrunch Disrupt 2025, converts models into NPU libraries and claims up to 60x over mobile CPU. — [Wowtale](https://en.wowtale.net/2024/05/21/76988); [Pulse](https://www.pulse.bot/b2b-growth/news/zeticai-launches-mlange-the-first-one-stop-on-device-ai-app-development-platform-2e95e1f9-3839-4707-bdd1-eb0fa9a472cc/)
- ggml.ai (Georgi Gerganov's team behind llama.cpp) joined Hugging Face on 2026-02-20. ggml.ai's site says it "was acquired by Hugging Face in 2026", while HF frames it as "joining". llama.cpp stays open source. — [Simon Willison](https://simonwillison.net/2026/Feb/20/ggmlai-joins-hugging-face/); [gihyo.jp](https://gihyo.jp/article/2026/02/ggml-join-hugging-face)
- Tether launched the open-source QVAC SDK in April 2026. It is built on QVAC Fabric (a llama.cpp fork) plus whisper.cpp, Parakeet and Bergamot, and targets phones, desktops and servers. — [Decrypt](https://decrypt.co/363809/stablecoin-giant-tether-launches-toolkit-for-building-local-offline-ai-apps); [QVAC README](https://raw.githubusercontent.com/tetherto/qvac/main/README.md)
- Exo Labs builds exo, open-source peer-to-peer software that clusters home devices for local inference. Aggregators disagree on HQ (CB Insights: Seattle; Crunchbase: London) and report about $2.98M raised (unverified). — [exolabs.net](https://www.exolabs.net/); [CB Insights](https://www.cbinsights.com/company/exo-labs)
- NobodyWho is an open-source, llama.cpp-based on-device LLM engine with iOS and Android demos and game-engine integrations. — [Product Hunt](https://www.producthunt.com/posts/nobodywho)
- Several new 2026 seed rounds went to on-device agent and model startups:
  - Cephable: $7M, Nov 2026 — [Axios](https://www.axios.com/pro/climate-deals/2026/11/03/cephable-mass-mutual-ventures)
  - TraceWeave (Korea): $2.3M, Oct 2026 — [Wowtale](https://en.wowtale.net/2026/10/21/235665/)
  - Out of Set (Korea, speech) — [Wowtale](https://en.wowtale.net/2026/05/21/234111/)
  - PrismML: $22.25M from Khosla, Cerberus and Caltech for small reasoning LLMs on phones and PCs — [Dealroom](https://dealroom.co/news/152150-prismml-raises-22m-seed-to-shrink-ai-models-onto-your-phone/)
- Aizip builds Gizmo small language models (300M–2B parameters) for edge devices and demoed them with Renesas on Arm MPUs in July 2024. — [BusinessWire](https://www.businesswire.com/news/home/20240723463718/en)
- Software Mansion sells on-device AI app development services and maintains React Native ExecuTorch. — [Software Mansion](https://swmansion.com/services/on-device-ai-and-local-ai-development/)

### Inferences
- Value is shifting from raw runtimes, which are commoditized open source (llama.cpp, MLX, ExecuTorch), toward developer experience, NPU-specific compilation and fleet management (OTA model updates, analytics). Chip vendors are buying SDK teams to win developers: Qualcomm took Nexa AI (2026) and, [prior knowledge], Edge Impulse (2025).
- Hugging Face now owns a large share of the open local stack: ggml/llama.cpp, Transformers.js and SmolLM.

### Gaps
- The YC company directory could not be fetched, so other YC 2024–2026 on-device startups were probably missed.
- No independent benchmarks compare Cactus, RunAnywhere, Mirai and Nexa. All performance figures are vendor claims.
- HQ is unverified for RunAnywhere, Fluid Inference, NobodyWho, PrismML and Second State.
- Funding is unverified for Fluid Inference, NobodyWho, Cactus and RunAnywhere.
- Mozilla.ai's ownership of llamafile, and whether Second State and GaiaNet are still active, are [prior knowledge] only.

## On-device speech / voice

### Takeaway
On-device voice is the most mature local-AI niche. It ranges from veteran embedded vendors (Sensory, Picovoice, Cerence, SoundHound) to Apple-focused startups (Argmax, Fluid Inference) and a 2025–2026 wave of tiny open TTS models (Kyutai Pocket TTS, Gradium Phonon, Neuphonic NeuTTS, Kitten TTS).

### Cited Findings
- Argmax open-sources WhisperKit, SpeakerKit and TTSKit for Apple platforms and sells a Pro SDK, including an Android SDK on LiteRT. It raised an $8M seed in Nov 2024. Sources conflict on the lead: Argmax and Salesforce Ventures name Salesforce Ventures; Wilson Sonsini names General Catalyst. — [Argmax](https://www.argmaxinc.com/blog/seed); [Salesforce Ventures](https://salesforceventures.com/perspectives/welcome-argmax); [WSGR](https://wsgr.com/en/insights/wilson-sonsini-advises-argmax-on-seed-round.html)
- Picovoice offers on-device wake word, VAD, intent, STT, speaker recognition and picoLLM. Audio is processed entirely on-device; the network is used only for AccessKey validation. picoLLM also runs in browsers via WebAssembly. — [GitHub](https://github.com/Picovoice/picovoice); [Picovoice blog](https://picovoice.ai/blog/cross-browser-local-llm-inference-using-webassembly/)
- Moonshine AI (CEO Pete Warden, co-founder of Useful Sensors) raised an undisclosed round from Wing VC and IQT in Jul/Aug 2025 to advance on-device voice AI. CB Insights reports about $5M total (unverified). — [BusinessWire](https://www.businesswire.com/news/home/20250731017792/en/Moonshine-AI-Secures-Funding-to-Advance-On-Device-Voice-AI); [HF model](https://huggingface.co/UsefulSensors/moonshine)
- Fluid Inference maintains FluidAudio, an open Swift SDK for ASR, TTS (Kokoro, PocketTTS), diarization and VAD on the Apple Neural Engine. Apps built on it include Spokenly and Hedy. — [GitHub](https://github.com/FluidInference/FluidAudio)
- Speechmatics On-Device runs ASR on the end-user device and claims to come within 5% of cloud accuracy. It reports 3.9x real time and 0.94GB RAM on a Windows CPU (vendor claim). — [Speechmatics](https://www.speechmatics.com/company/articles-and-news/on-device-speech-to-text-in-10-questions)
- Cartesia released Edge, an Apache-2.0 SSM library for on-device use starting with Apple M-series chips. It also has Rene (a 1.3B model) and Sonic On-Device TTS (private beta). — [Cartesia](https://www.cartesia.ai/on-device); [TechCrunch](https://techcrunch.com/2024/12/12/cartesia-claims-its-ai-is-efficient-enough-to-run-pretty-much-anywhere/)
- Kyutai's Pocket TTS is a 100M-parameter model that runs in real time on CPUs. — [GitHub](https://github.com/kyutai-labs/pocket-tts)
- Gradium, a Kyutai spinout, raised a $70M seed in Dec 2025 led by FirstMark and Eurazeo; Goodwin reports it as €60M. NVIDIA led an extension of about $30M in Jul 2026, taking the seed past $100M. Gradium released Phonon (31M/40M), an open on-device TTS model. — [TechCrunch](https://techcrunch.com/2025/12/02/paris-based-ai-voice-startup-gradium-nabs-70m-seed); [Sifted](https://sifted.eu/articles/gradium-nvidia-30m-extension-seed); [Gradium](https://gradium.ai/blog/release-phonon-open-weight)
- Neuphonic's NeuTTS are open on-device TTS models with voice cloning. Kitten TTS models are 15M–80M parameters (25–80MB). — [GitHub](https://github.com/neuphonic/neuTTS); [Stream](https://getstream.io/blog/best-on-device-tts-models/)

### In-car and edge assistants
- Cerence CaLLM Edge (Nov 2024) is a 3.8B model fine-tuned from Phi-3 and quantized to 4-bit. It runs in the head unit offline or as a hybrid backup. Arm Kleidi accelerates it, and a multimodal version runs on MediaTek/NVIDIA. — [Cerence PR](https://investors.cerence.com/news-events/press-releases/detail/114/cerence-introduces-pioneering-embedded-small-language-model-purpose-built-for-automotive); [MediaTek/NVIDIA PR](https://investors.cerence.com/news-events/press-releases/detail/98/cerence-ai-and-mediatek-partner-to-introduce-multi-modal-language-models-running-on-the-edge-built-on-nvidia)
- SoundHound runs an on-device LLM (Chat AI) on NVIDIA DRIVE with no connectivity required. It was announced 2024-03-18. — [SpeechTech](https://www.speechtechmag.com/Articles/News/Speech-Technology-News/SoundHound-to-Offer-On-Chip-Voice-AI-with-NVIDIA-163116.aspx)
- Kardome deploys spatial-hearing voice models on edge hardware (NVIDIA AGX), partnered with SoundHound in Jun 2025, and demoed at CES 2026. — [TWICE](https://www.twice.com/the-wire/kardome-demonstrates-edge-based-voice-ai-at-ces-2026); [Kardome](https://kardome.com/blog-posts/kardome-soundhound-ai-team-up-transform-in-car-voice-ui-multi-zone-conversational-ai)
- Sensory pitches 100% on-device wake word and STT with under 60ms latency, plus LLM handoff to the cloud for complex queries. — [Sensory](https://www.sensory.com/automotive/)

### Inferences
- In-car assistants are converging on hybrid designs: an embedded SLM handles core commands and the cloud handles open-domain queries (Cerence, Sensory, SoundHound).
- Open tiny TTS models (under 100M parameters) became a competitive category in 2025–2026, with vendor blind tests disputing which is best.

### Gaps
- Status was not checked for Fluent.ai, Snips (Sonos 2019) or Speechly (Roblox 2023); they were left out.
- Chinese in-car voice vendors (iFlytek, AISpeech, Unisound) and paragon semvox were not researched.
- Coqui's shutdown (early 2024) and Alpha Cephei/Vosk details are [prior knowledge].
- Kardome's HQ (Israel) is [prior knowledge].

## On-device vision / multimodal

### Takeaway
Fewer pure-play startups here. Moondream (tiny VLMs) and Nota AI (model optimization, KOSDAQ-listed Nov 2025) are the anchors, with Korean optimization firms (ENERZAi, SqueezeBits, ZETIC) and tinyML vision firms (Plumerai) around them.

### Cited Findings
- M87 Labs (Moondream) raised a $4.5M pre-seed led by Felicis, M12 GitHub Fund and Ascend in Oct 2024. Moondream 0.5B is built for edge devices, and Moondream 3.0 Preview came out in Sep 2025. — [VentureBeat](https://venturebeat.com/ai/moondream-raises-4-5m-to-prove-that-smaller-ai-models-can-still-pack-a-punch); [GitHub](https://github.com/m87-labs/moondream)
- Nota AI (Daejeon, founded 2015) makes the NetsPresso optimization platform and listed on KOSDAQ on 2025-11-03 (ticker 486990). It collaborates with Qualcomm AI Hub. — [TechNode](https://technode.global/prnasia/nota-ai-seeks-kosdaq-listing-as-the-first-ai-optimization-tech-startup/); [Edge AI Vision](https://www.edge-ai-vision.com/2025/05/nota-ai-demonstrates-on-device-ai-breakthrough-at-embedded-vision-summit-2025-in-collaboration-with-qualcomm-ai-hub/)
- ENERZAi describes itself as a full-stack on-device AI solution company doing model compression and compiler optimization. — [embedded world](https://www.embedded-world.de/en/exhibitors/enerzai-inc-2611214)

### Inferences
- Vision-on-device value has largely moved into silicon-vendor toolchains (Qualcomm AI Hub, MediaTek NeuroPilot, Hailo). Independent vision SDK startups tend to be optimization or compression plays.

### Gaps
- No verified sources this session for Plumerai, Xnor.ai (Apple 2020), Embedl, Clika or SqueezeBits. Their entries are [prior knowledge] with only the company site as source.

## Browser / WebGPU inference and big-tech platforms

### Takeaway
In-browser inference is dominated by open-source projects (MLC WebLLM, Transformers.js, wllama) and browser vendors (Chrome built-in Gemini Nano). Picovoice picoLLM is the clearest commercial cross-browser SDK. No funded browser-inference pure-play startup was found.

### Cited Findings
- WebLLM is MLC's in-browser engine. It uses WebGPU and WASM, offers an OpenAI-compatible API, and compiles kernels with MLC-LLM. — [MLC blog](https://blog.mlc.ai/2024/06/13/webllm-a-high-performance-in-browser-llm-inference-engine); [arXiv](https://arxiv.org/html/2412.15803v1)
- Microsoft Research published WebGPU LLM inference work ("Llamas on the Web"). — [MSR](https://www.microsoft.com/en-us/research/?p=1173686)
- Intel's guide covers in-browser LLM options including Transformers.js, WebLLM and wllama. — [Intel](https://www.intel.com/content/www/us/en/developer/articles/technical/web-developers-guide-to-in-browser-llms.html)
- Google Firebase AI Logic offers hybrid on-device/cloud inference for Android apps. — [Firebase](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started)

### Gaps
- Big-tech runtime entries (Apple Core ML/MLX/Foundation Models/Private Cloud Compute, Meta ExecuTorch, Microsoft Foundry Local/Windows ML, Intel OpenVINO, AMD Lemonade, Alibaba MNN, Tencent ncnn) use repo or official-site sources. Their feature descriptions are partly [prior knowledge].
- Browser vendors with local LLM features (Opera, Brave, Firefox) were not researched.

## Hybrid on-device/cloud routers

### Takeaway
No standalone, funded startup focused purely on routing between on-device and cloud was found. Hybrid routing ships as a feature of on-device SDKs (Cactus cloud fallback, RunAnywhere hybrid routing), of platforms (Google Firebase AI Logic hybrid, Apple Intelligence with Private Cloud Compute) and of automotive stacks (Cerence, Sensory LLM handoff).

### Cited Findings
- Cactus v1 adds optional cloud fallback; its hybrid routing and fleet features are a paid tier. — [InfoQ](https://www.infoq.com/news/2025/12/cactus-on-device-inference/)
- Firebase AI Logic hybrid inference covers on-device and cloud-hosted models. — [Firebase](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started)
- Cerence CaLLM Edge can serve as a backup when connectivity drops. — [Cerence PR](https://investors.cerence.com/news-events/press-releases/detail/114/cerence-introduces-pioneering-embedded-small-language-model-purpose-built-for-automotive)
- The closest "router" startup found, TrustedRouter, routes between cloud models using confidential computing, not on-device execution. It is excluded as out of scope. — [Dealroom](https://dealroom.co/news/163714-ai-router-trustedrouter-raises-6m-seed-to-keep-prompts-private/)

### Inferences
- Hybrid routing looks like it is becoming a standard SDK feature rather than a standalone company category.

### Gaps
- The search budget ran out before a dedicated "local-first router" search could finish, so small open-source or seed-stage routers may exist that were not found.

## Out-of-segment local-AI companies seen (included in JSON with their best-fit segment)

- **edge-silicon:** Qualcomm (also acquirer of Nexa AI), Arm, MediaTek, Quadric ($30M Series C — [Edge AI Vision](https://www.edge-ai-vision.com/?p=56520)), Axelera AI, Syntiant.
- **bigtech:** Google, Apple, Meta, Microsoft, Intel, AMD, NVIDIA, Alibaba MNN, Tencent ncnn.
- **efficient-models:** PrismML, Deci (NVIDIA 2024), Embedl, SqueezeBits, Clika, Pruna AI, Multiverse Computing.
- **industrial-edge:** Edge Impulse (Qualcomm 2025), Imagimob (Infineon 2023), Roboflow, Latent AI, DeGirum.
- **selfhosted-inference-llmops:** OctoAI (NVIDIA 2024), Neural Magic (Red Hat 2025), GaiaNet.
- **consumer-local-apps:** Ollama, LM Studio, Jan, Locally AI, Open Home Foundation.
- **private-ai-platforms:** webAI. **vertical-regulated:** Edgerunner AI. **international:** ThunderSoft.
- **Excluded (cloud-only):** TrustedRouter and OpenRouter (cloud routers).
- **Excluded (out of scope here):** Iconic is included as an on-device game-AI engine.
- **Seen but not added for lack of detail:** SiMa.ai (edge silicon, runs Cerence CaLLM Edge), Callstack (react-native-ai), Useful Sensors (Moonshine parent/predecessor, Torre translator).
