# Consumer & Developer Local AI Apps, Local-First Personal AI, and Personal/Home AI Hardware (segment: consumer-local-apps)

Output file: `consumer-local-apps.json`, 103 organizations (93 tagged consumer-local-apps, 10 tagged other segments: bigtech x3, on-device-sdks x3, private-ai-platforms x2, selfhosted-inference-llmops x1, efficient-models x1).

Method note: the shared web-search budget ran out after about 25 searches. Entries with a 2025–2026 event (funding, acquisition, launch, rename) were checked against search results or primary pages in this session. Many long-standing open-source projects and indie apps (e.g., KoboldCpp, SillyTavern, Upscayl, Aider, Zed, Frigate, PhotoPrism, FUTO, GMKtec, Minisforum, Beelink, Corsair, Start9) are listed from prior knowledge. For those I cite their canonical GitHub repo or homepage and did not re-verify them this session. The Opera and Brave entries cite homepages because their blog domains could not be reached.

## Local LLM apps and tools: who is behind each

### Takeaway
The desktop local-LLM layer has consolidated around a few venture-backed companies: Ollama Inc. ($65M Series B, Jul 2026), Element Labs/LM Studio (bought Locally AI, Apr 2026) and Comfy Org on the media side. Around them sits a long tail of indie and open-source apps, most built on llama.cpp. ggml.ai, the company behind llama.cpp, joined Hugging Face in Feb 2026.

### Cited Findings
- Ollama Inc. raised a $65M Series B led by Theory Ventures, bringing total funding to $88M. It has nearly 9M users and did not disclose a valuation. Sources disagree on headcount (14 vs 62) and on the lead investor (one outlet says Benchmark) — [TechCrunch](https://techcrunch.com/2026/07/09/popular-open-source-ai-developer-tool-ollama-raises-65m-grows-to-nearly-9m-users/); [SiliconANGLE](https://siliconangle.com/2026/07/09/open-source-ai-developer-tool-ollama-raises-65m-grow-platform/); [valueaddvc](https://valueaddvc.com/blog/ollama-65m-series-b-theory-ventures-14-employees-8-9m-developers)
- LM Studio (Element Labs) acquired Locally AI, Adrien Grondin's iPhone app, in April 2026. Grondin now leads native AI across devices. On June 4, 2026, Locally relaunched as LM Studio's mobile app with LM Link — [LM Studio blog](https://lmstudio.ai/blog/locally-ai-joins-lm-studio); [LM Studio blog – Locally/LM Link](https://lmstudio.ai/blog/locally-lm-link); [Gigazine](https://gigazine.net/gsc_news/en/20260410-lm-studio-acquired-locally-ai)
- ggml.ai (Georgi Gerganov's company, llama.cpp/ggml) joined Hugging Face on Feb 20, 2026. Projects stay open source and no terms were disclosed — [Simon Willison](https://simonwillison.net/2026/Feb/20/ggmlai-joins-hugging-face/); [gihyo.jp](https://gihyo.jp/article/2026/02/ggml-join-hugging-face)
- Jan is made by Menlo Research Pte. Ltd. (Singapore), formerly "Homebrew"; the rename was announced Mar 25, 2025. Its funding is unclear: one directory says bootstrapped. Menlo is also moving into humanoid robotics (Asimov) — [Menlo HackMD](https://hackmd.io/@menlo); [everydev](https://www.everydev.ai/developers/open-superintelligence)
- Open WebUI incorporated as Open WebUI, Inc. Funding data conflicts: CB Insights shows $40K from the Mozilla Builders and GitHub accelerators, while another site claims $2.5M — [CB Insights](https://www.cbinsights.com/company/open-webui); [PitchBook](https://pitchbook.com/profiles/company/608052-61)
- Msty is made by CloudStack, LLC of Powell, Ohio, founded 2024 with about 10 employees. CEO Ashok Gelal; products are Msty Studio, Msty Go (formerly Msty Claw) and Msty Nexus. The app is closed source with no telemetry — [promptquorum review](https://www.promptquorum.com/power-local-llm/msty-review); [msty.ai](https://msty.ai/blog/introducing-msty-nexus)
- Osaurus is an open-source Apple-silicon LLM server with MCP support from Dinoki Labs (Terence Pae, Sam Yoo). It grew out of the Dinoki desktop companion; TechCrunch covered it in May 2026 — [TechCrunch](https://techcrunch.com/2026/05/15/osaurus-brings-both-local-and-cloud-ai-models-to-your-mac/)
- Kolosal AI's code is under the Genta-Technology GitHub org (commercial contact at genta.tech). One listing gives its HQ as Canada (founded 2025), which conflicts with Genta's Indonesian identity, so HQ is left null — [ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2FGenta-Technology%2FKolosal); [i-programmer](https://i-programmer.info/news/105-artificial-intelligence/17976-kolosal-ai-run-llms-locally-on-your-workstation-or-edge-devices-.html)
- Sanctum's legal entity is unverified. The Product Hunt maker is Tyler Scott Ward, and a download aggregator lists the publisher as "QXYZ Labs". It is not the same as the business-focused "Sanctum AI" covered by VentureBeat — [Product Hunt](https://www.producthunt.com/products/sanctum); [nero publisher page](https://get.nero.com/publishers/QXYZLabs/Sanctum\Sanctum.html)
- Hyperlink is Nexa AI's on-device file-search agent ("Perplexity for local files"). NVIDIA has promoted it for RTX PCs since Nov 2025, and AMD for Ryzen AI. Nexa also sells NexaSDK — [NVIDIA blog](https://blogs.nvidia.com/blog/rtx-ai-garage-nexa-hyperlink-local-agent); [AMD](https://www.amd.com/en/ecosystem/isv/consumer-partners/nexa.html)
- Mobile apps:
  - Private LLM is made by Numen Technologies.
  - Enclave's App Store developer is Piotr Gorzelany.
  - PocketPal AI (open source) is the most-recommended free app on iOS and Android.
  - Layla appears in Android lists.
  - fullmoon (Mainframe) is rarely updated.
  - MLC Chat is the speed pick (about 22 tok/s on a Snapdragon NPU).
  - Sources: [App Store – Enclave](https://apps.apple.com/us/app/enclave-local-ai-assistant/id6476614556); [promptquorum Android](https://www.promptquorum.com/power-local-llm/best-local-llm-apps-android-2026); [modelfit iPhone](https://modelfit.io/guides/best-llm-for-iphone/)
- Liquid AI acquired the Apollo private on-device chat app (2025 launch coverage) and rebuilt it on its LEAP model library. The price is undisclosed, and the original developer (reportedly Aaron Ng) is not confirmed by a primary source — [Liquid AI press](https://www.liquid.ai/press/liquid-ai-launches-leap-and-apollo-a-new-era-for-edge-ai-deployment-begins); [VentureBeat](https://venturebeat.com/ai/finally-a-dev-kit-for-designing-on-device-mobile-ai-apps-is-here-liquid-ais-leap)
- OpenClaw, the viral open-source personal agent created by Peter Steinberger, is now stewarded by the OpenClaw Foundation, an independent 501(c)(3). It has about 395k GitHub stars and supports local model providers as plugins — [GitHub](https://github.com/openclaw/openclaw)

### Inferences
- The likely M&A pattern for 2026–27 is platform companies (LM Studio, Hugging Face, Liquid AI) buying single-developer mobile or desktop apps and core runtime teams.
- Most consumer apps are thin layers on llama.cpp or MLX. Owning the runtime (ggml at HF, MLX at Apple) is strategically more valuable than owning the UI.

### Gaps
- Legal entities and HQs were not confirmed for: Pinokio, PocketPal, Enclave, fullmoon/Mainframe, Sanctum, Kolosal, Chatbox, LobeHub, Layla, BoltAI, Elephas and Backyard AI.
- The LibreChat acquisition by ClickHouse (Nov 2025) comes from prior knowledge. The search budget ran out and clickhouse.com was unreachable, so verify it.
- Backyard AI (formerly Faraday.dev): its current status, and whether the desktop local app was discontinued, is not verified.
- Funding for Open WebUI, Mintplex Labs, Nomic AI and Element Labs was not checked this session.

## Local image, video and audio generation tools

### Takeaway
Comfy Org is the scaled leader: $30M at a $500M valuation in Apr 2026, $48M raised in total and 4M+ users. Adobe has been absorbing local-first creative AI teams: the Invoke team (Oct 2025) and Topaz Labs (acquisition completed Sept 2026).

### Cited Findings
- ComfyUI raised $30M at a $500M valuation (Apr 24, 2026), reportedly led by Craft, for $48M total. An earlier $17M round was announced Sep 2025. Comfy has about 65 staff (Quebec City plus remote), and Netflix, Apple and Ubisoft are customers. Aggregators conflict on earlier round sizes — [TechCrunch](https://techcrunch.com/2026/04/24/comfyui-hits-500m-valuation-as-creators-seek-more-control-over-ai-generated-media/); [Comfy blog](https://blog.comfy.org/p/comfyui-raises-30m-to-scale-open); [Comfy blog $17M](https://blog.comfy.org/p/comfy-raises-17m-funding)
- The Invoke team joined Adobe Firefly Foundry (announced at Adobe MAX, Oct 28, 2025). The commercial Invoke platform shut down while open-source InvokeAI continues. A "$3.8M" figure on Dealroom appears to be seed funding, not a purchase price — [Adobe](https://news.adobe.com/news/2025/10/adobe-max-2025-firefly-foundry); [Dealroom](https://app.dealroom.co/news/feed/adobe-acquires-invoke-ai-for-3-8m)
- Adobe announced the Topaz Labs acquisition in Jun 2026 and completed it Sept 23, 2026. Topaz Photo/Video AI run locally — [Adobe blog](https://blog.adobe.com/en/publish/2026/09/23/adobe-completes-acquisition-of-topaz-labs); [CMSWire](https://www.cmswire.com/digital-experience/adobe-to-acquire-topaz-labs-to-boost-ai-video-image-tools/)
- Local meeting notes: Hyprnote (fastrepl) is now "anarlog". It briefly used the name "char", which is now a separate app. It runs on-device transcription and stores data in local SQLite — [GitHub](https://github.com/fastrepl/hyprnote)

### Inferences
- Local creative tools are being commercialized through cloud add-ons (Comfy Cloud) or absorbed by incumbents (Adobe), rather than as standalone local licenses.

### Gaps
- Not checked in 2026 sources: whether DiffusionBee and AUTOMATIC1111 are still maintained, Draw Things' corporate entity, and TensorStack/Amuse's HQ.
- Local video tools (Wan2GP, LTX desktop tools) and local music tools were not researched.

## Local-first personal AI, memory and assistants

### Takeaway
The flagship of the category, Rewind/Limitless, was absorbed by Meta (Dec 2025) and its local Mac app wound down. Screenpipe (Mediar) is now the leading open-source, local-first screen-memory company (YC S26). Khoj continues as a self-hostable open-source "second brain".

### Cited Findings
- Meta acquired Limitless (formerly Rewind) in Dec 2025. Pendant sales stopped and the Rewind desktop software is being wound down; the team moves to Reality Labs wearables — [TechCrunch](https://www.techcrunch.com/2025/12/05/meta-acquires-ai-device-startup-limitless/); [Engadget](https://www.engadget.com/ai/metas-latest-acquisition-suggests-hardware-plans-beyond-glasses-and-headsets-212930339.html)
- Screenpipe is made by Mediar, Inc. It is in YC's Summer 2026 batch, and reports raised about $2.8M (seed/pre-seed, 2025, led by Founders, Inc.; details conflict). Claimed traction is 200k+ installs and 18k GitHub stars (Mar 2026), with a $400 lifetime license — [YC](https://www.ycombinator.com/companies/screenpipe); [Crunchbase](https://www.crunchbase.com/organization/mediar-6241); [dev.to](https://dev.to/tekmag/screenpipe-the-open-source-screen-recorder-that-gives-ai-agents-persistent-memory-of-your-work-3l2e)
- Khoj is AGPL-3.0 and can run in the cloud, on-prem or hybrid. Its v2.0 beta series is ongoing, and the team also promotes Pipali, "open-source AI coworker that runs on your computer" — [GitHub](https://github.com/khoj-ai/khoj); [dev.to review](https://dev.to/jovan_chan_9500711396d4e6/khoj-review-2026-your-self-hosted-ai-second-brain-28mi)

### Inferences
- Big tech's moves (Meta–Limitless, Microsoft Recall, Apple Intelligence) squeeze independent lifelogging startups. Open-source plus local-first is the main remaining differentiation.

### Gaps
- Personal AI (personal.ai) is excluded because its product appears cloud-hosted; it was not verified.
- Omi (Based Hardware) is excluded as mostly cloud, although it is open source and self-hostable.
- The status of Reor and Kin, and Pieces' current local-LLM features, were not verified this session.

## Personal AI hardware, home servers and AI mini-PCs

### Takeaway
2025–26 brought crowdfunded personal AI boxes:
- **Olares One:** Kickstarter $2.3M, backed by a reported $45M Series A plus a later $55M "ByteFuture" round.
- **Tiiny AI Pocket Lab:** $3M+ on Kickstarter, Mar–Apr 2026, and certified by Guinness.

Alongside them, AMD Ryzen AI Max+ 395 mini-PCs (Framework, GMKtec, Minisforum, Beelink, Corsair) became the default "local LLM PC", and Apple Macs are being clustered with EXO.

### Cited Findings
- Olares One has an RTX 5090 Mobile GPU, 96GB RAM and was priced at $2,999 on Kickstarter. It passed $1M in its first week and ran a $2.3M campaign (Jan 2026). Funding:
  - A $45M Series A was led by SIG.
  - A 2026 report says ByteFuture raised $55M for Olares One and Olares OS, with all Kickstarter orders delivered (single source).
  - An Aug 2026 release claims $100M total.
  - Sources: [SiliconANGLE](https://siliconangle.com/2025/12/09/olares-launches-personal-ai-computer-turns-local-files-smart-assistant/); [TechPowerUp](https://www.techpowerup.com/342779/olares-to-launch-a-personal-ai-device-bringing-cloud-level-performance-home); [Dealroom news](https://dealroom.co/news/150432-bytefuture-raises-55m-to-scale-local-ai-hardware-and-os/)
- Tiiny AI Pocket Lab runs LLMs up to 120B parameters on-device. It passed $1M within 5 hours of its Mar 11, 2026 Kickstarter launch, and Kicktraq shows $3M+ funded by Apr 10. Its super-early-bird price was $1,399 — [VIR](https://vir.com.vn/tiiny-ai-pocket-lab-raises-1-million-in-five-hours-on-kickstarter-148369.html); [Kicktraq](https://www.kicktraq.com/projects/tiinyai/tiiny-ai-pocket-lab/); [Live Science](https://www.livescience.com/technology/computing/meet-the-worlds-smallest-ai-supercomputer-it-packs-doctorate-level-intelligence-its-makers-say-and-can-fit-into-your-pocket)
- EXO Labs released exo 1.0 with RDMA over Thunderbolt 5, and Apple reportedly integrated the clustering protocol into macOS 26.2. Its funding is undisclosed ("private investors"). Apple's "Harbor" Mac private-inference app reportedly appeared briefly in the App Store on Nov 10, 2026 — [heise](https://heise.de/-11085716); [Digital Trends](https://digitaltrends.com/computing/apple-wants-to-turn-your-mac-into-a-private-ai-server-without-making-you-touch-the-terminal); [Tom's Hardware](https://www.tomshardware.com/software/two-nvidia-dgx-spark-systems-combined-with-m3-ultra-mac-studio-to-create-blistering-llm-system-exo-labs-demonstrates-disaggregated-ai-inference-and-achieves-a-2-8-benchmark-boost)
- Other plug-and-play boxes noted in a 2026 buyer's guide: "ClawBox" (67 TOPS, 15W) and an unnamed $1,899 "Compact Local AI Server" sold on Amazon. These are weak sources and the makers are unidentified, so they are not in the JSON — [GitHub gist](https://gist.github.com/yalexx/8f22e96f5309a29f1892056ff66b35a3)

### Inferences
- The consumer local-AI hardware market is splitting three ways: prosumer GPU boxes (Olares, tinybox), low-power pocket or NPU devices (Tiiny), and commodity unified-memory mini-PCs (AMD Strix Halo OEMs, Mac mini/Studio).

### Gaps
- Not verified: HQ and legal entity for Olares/ByteFuture and Tiiny AI, Umbrel's AI-specific products, and tiny corp's 2026 tinybox lineup and pricing.
- Not added (unverified): AI NAS makers (Zettlab, UGREEN NASync AI), the Sarvam AI device (India, planned May 2026) and OpenVoiceOS. Mycroft AI (defunct 2023) was considered but omitted.

## Local coding assistants for individuals

### Takeaway
Most open-source coding agents (Continue, Cline, Roo Code, Kilo Code, Aider, OpenCode, goose, Zed) are bring-your-own-model and work with Ollama or LM Studio. Tabby and Refact are explicitly self-hosted servers. Void (Glass Devtools, YC) has paused development.

### Cited Findings
- Void IDE development is "temporarily paused" (announced around Jan 2025) while the team explores new ideas. It supports Ollama and local models — [OpenAlternative](https://openalternative.co/void); [everydev](https://www.everydev.ai/developers/glass-devtools); [YC](https://www.ycombinator.com/companies/void)
- Entries for Continue, Cline, Roo Code, Kilo Code, TabbyML, Aider, Refact, Zed, goose (Block) and OpenCode (Anomaly/SST) cite their GitHub repos. Their local-model support was not re-verified this session.

### Inferences
- Local coding usage is mostly a configuration option inside cloud-first agents, not a standalone business. Tabby and Tabnine are the vendors that monetize self-hosting directly.

### Gaps
- 2025–26 funding for Cline (reported $32M in 2025, prior knowledge), Kilo Code, Continue and Roo Code was not verified because the search budget ran out and cline.bot was unreachable.
- JetBrains (local Mellum/full-line completion) and Sourcegraph were not added.

### Out-of-segment local-AI companies seen (added to JSON with other segment keys)
- **ggml.ai** (on-device-sdks): acquired by Hugging Face, 2026.
- **MLC** (on-device-sdks).
- **Cactus Compute** (on-device-sdks).
- **Liquid AI** (efficient-models).
- **Zylon/PrivateGPT** (private-ai-platforms).
- **Tabnine** (private-ai-platforms).
- **Docker Model Runner** (selfhosted-inference-llmops).
- **AMD** (bigtech): Lemonade/GAIA.
- **Apple** (bigtech): MLX/Harbor.
- **NVIDIA** (bigtech): ChatRTX/DGX Spark.

Also seen but not added: Hugging Face, Intel AI Playground, Microsoft Foundry Local, Google AI Edge Gallery, Red Hat RamaLama, h2o.ai (h2oGPT), and the DGX Spark OEMs (ASUS, Dell, MSI).
