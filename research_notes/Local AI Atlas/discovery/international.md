# International (non-US) Local AI Companies — Discovery Notes

Dataset: `international.json` (204 companies; Europe 73, China 40, South Korea 18, Japan 13, Canada 12, Israel 11, India 9, Taiwan 8, Middle East 7, Southeast Asia 6, Australia 3, Latin America 2, Africa 2). By segment: efficient-models 49, edge-silicon 42, private-ai-platforms 27, onprem-hardware 26, selfhosted-inference-llmops 17, bigtech 14, on-device-sdks 11, vertical-regulated 8, industrial-edge 7, consumer-local-apps 3.

Method note: about 25 web searches this session (sifted.eu would not fetch, and the shared search budget ran out). Roughly 60 entries have a 2025–2026 news source found this session. The rest are well-known companies sourced to their own websites from prior knowledge; their status was **not re-checked this session** and should be spot-checked before publication.

## Canada

### Takeaway
Canada's local-AI strength is enterprise private LLMs (Cohere), AI silicon (Tenstorrent, Taalas, Blumind, ABR), and on-device voice (Picovoice). Its best-known edge-chip startup, Untether AI, shut down in 2025.

### Cited Findings
- Cohere and Aleph Alpha announced a combination in April 2026 and signed a definitive agreement on 16 Sept 2026. It is subject to regulatory and shareholder approval. Schwarz Group committed US$600M to lead the merged firm's Series E. Reported value is about $20B. HQ is reported as Toronto + Berlin; earlier reports said Canada only — [TNW](https://thenextweb.com/news/cohere-aleph-alpha-definitive-agreement-transatlantic-sovereign-ai); [SiliconANGLE](https://siliconangle.com/2026/09/16/cohere-and-aleph-alpha-agree-to-merge-in-reported-20b-deal/); [TechCrunch](https://techcrunch.com/2026/04/25/why-cohere-is-merging-with-aleph-alpha/)
- Cohere reported $240M ARR in 2025, per merger coverage — [The Logic](https://thelogic.co/news/cohere-aleph-alpha-merger-sovereign-ai/)
- AMD acqui-hired Untether AI's whole engineering team (June 2025). Untether ended support for its speedAI products and imAIgine SDK — [Tom's Hardware](https://www.tomshardware.com/tech-industry/amd-scoops-entire-untether-ai-chip-team-canada-ai-inference-outfit-will-cease-product-support); [HPCwire](https://www.hpcwire.com/off-the-wire/untether-ai-team-acquired-by-amd-product-support-discontinued/)
- Blumind (Ottawa) makes analog ultra-low-power AI chips. A BM110 eval kit was reported in Nov 2026, from a single less-established source — [TechSoda](https://techsoda.substack.com/p/canadian-startup-blumind-to-release); [tech-insider](https://tech-insider.org/ca/blumind-bm110-evaluation-kit-analog-ai-chip-ottawa-2026/)
- Applied Brain Research (Waterloo) raised a seed round led by Two Small Fish to sell its TSP1 speech chip, which runs under 35mW. This comes from a secondary profile — [yespress](https://yespress.io/applied-brain-research)
- Picovoice's on-device voice + LLM stack — [DigiTimes PR](https://www.digitimes.com/news/a20250505PR208.html?chid=9)

### Inferences
- Once it closes, the Cohere–Aleph Alpha merger would create the largest non-US "sovereign/private enterprise LLM" vendor. That could make it the default non-US alternative for regulated buyers in both North America and the EU.

### Gaps
- Tenstorrent's headquarters is listed as Canada (Toronto), but the company also runs large Santa Clara operations; the primary HQ was not checked.
- Status not checked: Taalas details and funding, Deeplite, Fluent.ai. LōD Technologies (Vancouver, from a BetaKit article) and PolarGrid were found but left out: LōD's product isn't clear, and PolarGrid is network-side edge.

## Europe

### Takeaway
Europe is the biggest non-US cluster. It has sovereign LLM platforms (Mistral, Aleph Alpha, LightOn, Zylon, deepset), model compression (Multiverse, Pruna, Embedl, Nota-style), edge silicon (Axelera, Innatera, GreenWaves, SEMRON, STMicro, NXP, Infineon), and a wave of 2026 inference-chip money (Fractile, Euclyd, VSORA).

### Cited Findings
- European chip startups had raised €3.25bn in equity in 2026 at the time of writing, against €827m in all of 2025. About three-quarters went to AI processors, including Fractile, Euclyd and Axelera — [Sifted](https://sifted.eu/articles/european-chips-funding-almost-quadruples-as-investors-back-nvidias-inference-challengers/). Sifted also mapped 113 European AI-hardware startups, but the page could not be fetched — [Sifted map](https://sifted.eu/articles/europes-chips-startups-mapped-113-companies-building-the-hardware-behind-ai/)
- Axelera AI raised $250M (Feb 2026) for edge inference chips. It has a €61.6M grant for its Titania chiplet — [Dealroom](https://dealroom.co/news/126111-axelera-ai-raises-250m-to-scale-energy-efficient-edge-ai-chips-in-europe/)
- Euclyd (Eindhoven, ASML alumni) is seeking €100M or more for its CRAFTWERK inference chip — [IO+](https://ioplus.nl/en/posts/euclyd-wants-to-raise-100-million-and-take-on-nvidia)
- Fractile raised a $220M Series B — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/uk-chip-startup-fractile-raises-090729157.html)
- Multiverse Computing (Spain) raised $570M at a $1.7B valuation (July 2026). It launched the offline CompactifAI app (Mar 2026) and an edge partnership with Axelera (Mar 2026) — [SiliconANGLE](https://siliconangle.com/2026/07/28/ai-model-compression-startup-multiverse-raises-570m-1-7b-valuation/); [GlobeNewswire](https://www.globenewswire.com/news-release/2026/03/03/3248035/0/en/multiverse-computing-launches-compactifai-app-bringing-offline-ai-to-edge-devices.html); [Multiverse](https://multiversecomputing.com/resources/multiverse-computing-and-axelera-ai-launch-strategic-collaboration-to-bring-next-generation-ai)
- Mistral sells on-prem deployments that run on customer GPU clusters — [Sacra](https://sacra.com/chat/h/1df259c3-0150-468a-bb1d-e6db821d0663/). Mistral and HUMAIN announced a sovereign-AI collaboration (Aug 2026) — [Intelligent CIO](https://www.intelligentcio.com/me/2026/08/25/mistral-and-humain-announce-strategic-collaboration-to-advance-sovereign-ai-in-saudi-arabia/)
- 2026 UK raises:
  - Locai: £1M pre-seed for off-cloud, on-user-hardware inference — [UKTN](https://www.uktech.news/ai/locai-raises-1m-to-develop-its-off-cloud-ai-infrastructure-20260422)
  - Stanhope AI: $8M seed for on-device adaptive AI — [TNW](https://thenextweb.com/news/stanhope-ai-raises-8m-to-build-adaptive-ai-for-robotics-and-defence)
  - Edgify: $9M for in-store edge AI — [Dealroom](https://dealroom.co/news/143996-edgify-raises-9m-to-run-ai-inside-store-checkouts-and-cameras/)
  - Plumerai: $8.7M Series A (2025) — [Tech.eu](https://tech.eu/2025/09/16/plumerai-raises-87m-series-a-to-scale-tiny-ai-for-cameras/)
- German and Austrian sovereign/on-prem startups:
  - amber: €7M — [TNW](https://thenextweb.com/news/amber-series-a-7m-ventech-nrw-bank-ai-data-layer)
  - INXM: €5.7M pre-seed — [AI-Radar](https://ai-radar.it/article/inxm-raccoglie-57-milioni-di-euro-per-l-automazione-ai-on-premise-nelle-imprese-europee?lang=en)
  - Blockbrain: €17.5M — [BeBeez](https://bebeez.eu/2026/02/12/german-genai-startup-blockbrain-lands-e17-5-million-to-advance-enterprise-grade-ai-agents/)
  - Xayn/Noxtua: €80M — [Tech.eu](https://tech.eu/2025/04/25/xayn-secures-80m-to-build-europe-s-privacy-first-legal-ai-backed-by-c-h-beck/)
  - Ablatic AI (Talos LLM) — [JKU](https://www.jku.at/en/quanta/detail/news/jku-spin-off-ablatic-ai-develops-european-ai-language-model/)
- Nordics:
  - Berget AI (Sweden): €2.1M for sovereign inference — [Tech.eu](https://tech.eu/2026/02/02/swedish-startup-berget-ai-lands-2-1m-as-demand-grows-for-sovereign-ai-in-europe/)
  - NobodyWho (Copenhagen): €2M for on-device SLMs — [Tech.eu](https://tech.eu/2025/12/17/nobodywho-raises-eur2m-to-challenge-big-techs-cloud-ai-with-slms-for-local-devices/)
- OpenEuroLLM is an EU-funded consortium that includes Aleph Alpha and ellamind — [Computerwoche](https://www.computerwoche.de/article/3815387/openeurollm-soll-europas-ki-souveranitat-starken.html)

### Inferences
- Two European theses look strong enough to survive: compression (Multiverse) paired with edge silicon (Axelera), and confidential or on-prem enterprise platforms. Frontier pre-training is consolidating, as the Aleph Alpha → Cohere deal shows.

### Gaps
- The Sifted 113-company hardware map could not be read, so it is the best next source to mine.
- Not checked this session:
  - ggml.ai/llama.cpp: possible 2026 corporate tie-up
  - iGenius → Domyn rebrand
  - nyonic status
  - LeapMind-like small players
- Lumai (Oxford optical compute) is listed without a source URL.
- Thin or missing coverage: Poland (only Bielik), Italy (Domyn, LocalAI), Baltics, CEE edge-AI startups. Russian vendors (e.g., Sber GigaChat on-prem) were deliberately left out.

## Israel

### Takeaway
Israel contributes edge GenAI silicon (Hailo-10H), on-prem inference systems (NeuReality, Pliops), and air-gapped enterprise AI (Tabnine, AI21). Several notable exits went to NVIDIA (Run:ai, Deci).

### Cited Findings
- Hailo-10H is described as the first discrete edge accelerator built for on-device generative AI — [Ynet](https://www.ynetnews.com/tech-and-digital/article/skpxw508lx); [eeNews](https://www.eenewseurope.com/en/hailo-10h-edge-ai-accelerator-with-on-device-generative-ai)
- NeuReality's NR1 appliance ships preloaded with Llama, Mistral, Qwen and Granite for private GenAI clouds and on-prem clusters — [insideHPC](https://insidehpc.com/2025/05/neureality-announces-inference-appliance-is-preloaded-with-ai-models/)
- Impala AI raised an $11M seed (Viola, NFX) for inference inside the customer's VPC — [Ynet](https://www.ynetnews.com/tech-and-digital/article/h1ux03jjwx)
- Inferize's technology is moving into Nebius Token Factory, which is cloud-side, so it was excluded — [Calcalist](https://www.calcalistech.com/tags/Inferize)

### Inferences
- Israeli local-AI value is concentrated in silicon and infrastructure software rather than models.

### Gaps
- Not re-checked this session: Run:ai and Deci acquisition years (2024), and Pliops LightningAI product details.

## Middle East (UAE, Saudi Arabia)

### Takeaway
Gulf "sovereign AI" is mostly state-backed in-country cloud and compute (Core42, HUMAIN), plus open-weight models (Falcon, Jais, K2). The first on-prem "AI-in-a-Box" appliances are emerging.

### Cited Findings
- Core42 was formed in 2023 from G42 Cloud, Inception and Injazat. It partners with e& on sovereign AI compute — [Zawya](https://www.zawya.com/en/business/e-uae-and-core42-partner-to-deliver-sovereign-ai-infrastructure-at-scale-403213); [Computer Weekly](https://www.computerweekly.com/news/366642883/Core42-partners-with-Solutions-on-Mubadala-sovereign-AI)
- HUMAIN and AMD launched "AI in a Box" for Saudi enterprises — [Arab News](https://backup.arabnews.com/node/2656424/business-economy). HUMAIN also partners with Cohere on a 50MW compute deal — [CryptoBriefing](https://cryptobriefing.com/humain-cohere-sovereign-ai-compute/) — and with Mistral — [YourStory](https://yourstory.com/ai-story/mistral-ai-humain-sovereign-ai-saudi-arabia)
- Kerno and SAAL.ai unveiled a UAE-built Sovereign AI-in-a-Box — [Gulf News](https://gulfnews.com/business/corporate-news/kerno-and-saalai-unveil-uae-built-sovereign-ai-in-a-box-1.500704548)

### Gaps
- No specs or pricing found for the Gulf appliances. Qatar (QCRI Fanar), Turkey and Egypt were not covered.

## India

### Takeaway
India's local-AI activity centres on Sarvam's offline edge stack and a fresh crop of edge-AI chip startups (Netrasemi, Mindgrove, HrdWyr, Sensesemi). Ziroh Labs pitches running LLMs on CPUs only.

### Cited Findings
- Sarvam Edge (Feb 2026) runs speech recognition, translation and TTS offline on phones. Sarvam also works with HMD on feature phones — [NewsBytes](https://www.newsbytesapp.com/news/science/sarvam-ai-pushes-offline-models-to-reduce-cloud-spending/story); [Beebom](https://gadgets.beebom.com/news/hmd-sarvam-ai-join-hands-for-conversational-ai-in-feature-phones)
- Netrasemi brought up its 12nm A2000 edge AI SoC — [AIM](https://analyticsindiamag.com/ai-features/from-chip-talent-to-chipmaker-netrasemi-bets-on-indias-semiconductor-future); [YourStory](https://yourstory.com/2025/08/netrasemi-semiconductor-startup-edge-ai-chips)
- HrdWyr raised $13M (May 2026) — [Business Standard](https://business-standard.com/companies/start-ups/hrdwyr-raises-13-mn-to-scale-ai-native-chips-for-edge-devices-globally-126051200964_1.html)
- Sensesemi raised a ₹25 Cr seed — [AIM](https://analyticsindiamag.com/ai-news-updates/sensesemi-bags-₹25-cr-seed-funding-to-build-edge-ai-chips)
- An Indian startup showed LLMs running without GPUs. This is believed to be Ziroh Labs' Kompact AI, but the company was not confirmed from the snippet — [AIM](https://analyticsindiamag.com/ai-startups/this-indian-ai-startup-proves-llms-no-longer-need-expensive-gpus/)

### Gaps
- Inc42 coverage was not surfaced. Gnani.ai, CoRover/BharatGPT, Neysa and Vicharak were not verified, so they were left out.

## China

### Takeaway
China dominates open-weight models used for local deployment: DeepSeek, Qwen, GLM, Kimi, MiniMax, MiniCPM. It also has a deep edge-silicon bench (Horizon, Black Sesame, Axera, SOPHGO, Rockchip, Houmo) and an on-prem LLM "all-in-one appliance" market of about 100 vendors.

### Cited Findings
- IDC counts nearly 100 vendors selling LLM all-in-one appliances. Named examples include China Telecom Xirang on Ascend, JD Cloud, H3C LinSeer Cube and IEIT/Inspur. Prices range from hundreds of thousands to millions of RMB — [DigiTimes](https://www.digitimes.com/news/a20250212PD230.html); [IDC](https://www.idc.com/?p=104159)
- Appliance uptake has been "shallow, narrow and slow", mostly SOEs and local governments — [ChinAI](https://chinai.substack.com/p/chinai-321-deepseek-spreads-across)
- Axera listed on HKEX on 10 Feb 2026 as China's "first edge AI chip stock" — [Qiming](https://qimingvc.com/en/news/chinese-edge-ai-chip-leader-axera-lists-hong-kong-stock-exchange)
- ModelBest's MiniCPM is in production cars (Changan Mazda EZ-60). Its funding reportedly passed a $1B valuation (single source) — [Pandaily](https://pandaily.com/model-best-raises-tens-of-millions-of-dollars-to-advance-edge-optimized-large-models); [SMM](https://news.metal.com/newscontent/103690673-modelbest-secures-fresh-funding-to-accelerate-on-device-ai-deployment)
- Chinese AI-chip startups are pivoting to edge devices as cloud competition heats up — [Caixin](https://www.caixinglobal.com/2026-07-21/chinese-ai-chip-startups-look-beyond-the-cloud-to-edge-devices-102466338.html)
- Houmo's M50 compute-in-memory chip — [KrASIA](https://kr-asia.com/beyond-the-cloud-houmo-ai-sees-ai-compute-shifting-to-the-edge)
- On-device model start-ups StepFun and Benzhi (SmallThinker) — [SCMP](https://www.scmp.com/tech/tech-trends/article/3360820/giant-models-grab-headlines-some-chinese-start-ups-bet-smaller-phone-ready-ai)
- Om AI's edge VLX model — [TechNode](https://technode.com/2026/05/27/from-video-understanding-to-edge-deployment-om-ai-targets-real-world-ai/)
- Enflame's US$900M IPO — [SCMP](https://scmp.com/tech/big-tech/article/3366025/enflames-us900m-ipo-tests-appetite-chinas-little-dragon-ai-chipmakers)

### Gaps
- Not checked: possible 2026 HK IPOs of Zhipu and MiniMax (both are listed as "scaleup").
- Jiuwanli, an edge inference chip startup founded in May 2026 by an ex-HiSilicon executive, came from a search summary only and was left out.
- Few appliance vendors are listed individually: Sugon, JD Cloud and China Telecom were left out.

## South Korea

### Takeaway
Korea has the densest NPU ecosystem outside the US and China. Edge chips: DeepX, Mobilint. On-prem chips: Rebellions, FuriosaAI, HyperAccel. Compression: Nota, SqueezeBits, ENERZAi. Sovereign LLMs: Upstage, LG EXAONE, Naver, all run by a national sovereign-AI program.

### Cited Findings
- DeepX confirmed IPO plans (Apr 2026) and is building DX-M2 on Samsung 2nm. Reported valuations conflict: $2.2bn per TNW vs more than ₩1T per JoongAng — [Asiae](https://www.asiae.co.kr/en/article/2026041412075569608); [TNW](https://thenextweb.com/news/deepx-series-d-2-2bn-edge-ai-chips-robotics); [JoongAng](https://www.koreajoongangdaily.com/business/deepx-to-produce-next-ai-chip-using-samsung-foundrys-2-nanometer-process/12597950)
- Mobilint is in mass production with 490+ supported models. It claims the only Korean NPU that runs LLMs at the edge (company claim) — [DigitalToday](https://www.digitaltoday.co.kr/en/view/44811/mobilint-poscodx-npu-based-industrial-ai-joint-development)
- Nota cut Upstage Solar 100B memory use by 72% under the national Sovereign AI Foundation Model Project — [Nota](https://blog.nota.ai/newsroom/nota-ai-upstage-solar-llm-memory-reduction)
- Upstage offers on-prem deployment and released the open-weight Solar Open 2 (Jul 2026) — [Upstage](https://upstage.ai/pricing/on-premises); [Korea Times](https://www.koreatimes.co.kr/business/companies/20260723/upstage-unveils-solar-open-2-open-weight-ai-model-built-for-autonomous-tasks)

### Gaps
- Not re-checked: Nota AI's KOSDAQ listing (marked public), and HyperAccel, ENERZAi, Lablup and Moreh, which come from prior knowledge. Kakao Kanana and SKT A.X were left out.

## Japan

### Takeaway
Japan pairs edge silicon (EdgeCortix, Sony IMX500, Renesas) with lightweight domestic LLMs built for on-prem use (NTT tsuzumi, NEC cotomi, Fujitsu Takane, PFN PLaMo Lite, ELYZA, Sakana).

### Cited Findings
- EdgeCortix won a ¥3B NEDO award for its NovaEdge GenAI chiplet — [Evertiq](https://evertiq.com/news/2025-06-02-edgecortix-secures-21m-to-develop-energy-efficient-ai-chiplet)
- PLaMo Lite (1B) and Rakuten AI 2.0 mini are aimed at edge and mobile use (third-party survey) — [codenote](https://codenote.net/en/posts/japanese-local-llm-development-case-studies/)

### Gaps
- No Nikkei sources surfaced. Status not checked: LeapMind (possibly wound down) and AI inside Cube.

## Taiwan

### Takeaway
Taiwan's local-AI players are MediaTek (on-device GenAI SoCs) and on-prem LLM hardware: Skymizer HTX301, Neuchips, and Phison aiDAPTIV+.

### Cited Findings
- Skymizer's HTX301 claims to run 700B-parameter models on a single PCIe card for on-prem use. It is partnered with III — [TechNode Global](https://technode.global/prnasia/skymizer-taiwan-inc-unveils-breakthrough-architecture-enabling-ultra-large-llm-inference-on-a-single-card/); [TechNews](https://technews.tw/2026/05/29/skymizer-htx301-the-worlds-first-edge-ai-inference-chip/)

### Gaps
- Kneron's corporate HQ is San Diego, with big operations in Taiwan; it is marked "Taiwan / USA". Appier was excluded because it is cloud-based.

## Southeast Asia, Australia, Latin America, Africa

### Takeaway
These regions mostly offer sovereign open models (SEA-LION, Typhoon, Sahabat-AI, Latam-GPT, InkubaLM) and sovereign inference infrastructure (SCX.ai). Notable exceptions are Singapore's Acrab (edge SoC + Agent Box) and Menlo Research (Jan, an offline desktop app).

### Cited Findings
- Acrab came out of stealth having raised $350M+ in total. Its GΞLIX 1 edge SoC powers an Agent Box desktop for local LLMs — [Unite.AI](https://www.unite.ai/acrabs-edge-chip-aims-to-run-100b-ai-models-locally/); [e27](https://e27.co/acrabs-us130m-raise-signals-seas-deeper-push-into-ai-hardware-20260807/)
- SCX.ai: Sydney sovereign inference node (Jan 2026), ASX listing after a A$40M IPO, A$6.5M contracted ARR — [HPCwire](https://www.hpcwire.com/aiwire/2026/01/30/scx-ai-launches-australias-1st-sovereign-ai-inference-node-in-sydney/); [Dealroom](https://dealroom.co/news/140248-scx-ai-seeks-aud-40m-in-asx-float-for-local-ai-inference/)
- Latam-GPT: 60 institutions across 15 countries; its training data is smaller than global models' — [Brookings](https://www.brookings.edu/articles/latam-gpt-and-the-search-for-ai-sovereignty/)
- Saptiva (Mexico) offers air-gapped sovereign LLM stacks (promotional source) — [Mexico Business News](https://mexicobusiness.news/cloudanddata/news/sovereign-ai-when-protocol-product)

### Gaps
- No Australian on-device startups found. BrainChip is ASX-listed but runs its main operations in California.
- Thin coverage in Latin America and Africa: not verified were Maritaca AI and WideLabs (Brazil) and Awarri/N-ATLaS (Nigeria). An unnamed Zambian sovereign-AI venture was also found but not identified.
- Vietnam and Malaysia are not covered.
