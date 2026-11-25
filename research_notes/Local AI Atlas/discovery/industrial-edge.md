# Industrial Edge AI Software, Edge MLOps & Orchestration (segment: industrial-edge)

Companion file: `industrial-edge.json`, with 145 companies (128 industrial-edge plus 17 from other segments).

**How this was researched:** WebSearch only. WebFetch could not resolve the aggregator hosts (newmarketpitch.com, stlpartners.com, shawnhymel.com), so the full market-map pages were never read. About half the rows were verified against a search result. The rest rely on background knowledge, and each of those cites only the company's own homepage. Treat "active" on those homepage-only rows as **likely, not verified** for 2026. Six rows are marked "unknown".

## Edge AI dev platforms / TinyML

### Takeaway
Chip vendors have bought most of the independent TinyML toolchains: Qualcomm, Infineon, TDK, Renesas, Nordic, ST and QuickLogic. The main ones still independent are Latent AI, Plumerai, Xailient, Aizip, Stream Analyze, Neurala and Nota AI. Nota AI went public on KOSDAQ in November 2025.

### Cited Findings
- Qualcomm bought Edge Impulse (San Jose) in March 2025. Edge Impulse had raised $54M before the deal, and terms were not disclosed. — [SiliconANGLE](https://siliconangle.com/2025/03/10/qualcomm-acquires-edge-ai-development-startup-edge-impulse/); [Edge Impulse 2025 review](https://www.edgeimpulse.com/blog/edge-impulse-2025-in-review/)
- Infineon bought Imagimob (Stockholm) on 16 May 2023. Its edge AI tools are now sold under the DEEPCRAFT brand. — [Imagimob](https://www.imagimob.com/news/infineon-strengthens-its-offering-in-embedded-ai-solutions-through-acquisition-of-tinyml-leader-imagimob); [EE Times](https://www.eetimes.com/why-infineon-acquires-tinyml-startup-imagimob/)
- Nordic Semiconductor announced on 17 June 2025 that it was buying all of Neuton.AI's IP and 13 engineers. Neuton builds models under 5 KB. Nordic says the tool will stay free for developers. — [Nordic](https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-accelerates-edge-AI-leadership-with-acquisition-of-Neuton-AI); [Hackster](https://www.hackster.io/news/nordic-semi-dives-deeper-into-tinyml-acquires-sub-5kb-machine-learning-model-platform-neuton-ai-3748378b8c48)
- Voyager Technologies (NYSE: VOYG) **invested in** Latent AI on 18 Aug 2025 to support edge AI for space and defense. One aggregator (Preqin) wrongly lists this as an acquisition. — [Via Satellite](https://www.satellitetoday.com/technology/2025/08/18/voyager-technologies-makes-investment-into-ai-software-company-latent-ai/); [BusinessWire](https://www.businesswire.com/news/home/20250818734194/en/Voyager-and-Latent-AI-Bring-Advanced-AI-to-Orbit)
- Latent AI's CTO chairs the EDGE AI FOUNDATION Defense Working Group, formed in February 2026. Other members include Qualcomm, Wind River, Dell, Syntiant, Expanso and Embedl. — [PR Newswire](https://www.prnewswire.com/news-releases/edge-ai-foundation-launches-first-of-its-kind-working-group-to-advance-mission-critical-ai-capabilities-for-defense-and-government-operations-302691604.html)
- Tracxn lists Plumerai as private, with about $17M raised over 5 rounds. — [Tracxn](https://tracxn.com/d/companies/plumerai/__2Mgv7VbfXQAmHAgHl0iy4xrFAZ5QOwn0QsCcJssSZzg)
- Xailient is still active (on-device face recognition). — [PR Newswire APAC](https://en.prnasia.com/releases/global/xailient-ranks-1-for-face-recognition-accuracy-in-real-world-on-device-ai-556935.shtml)
- Nota AI (maker of NetsPresso) listed on KOSDAQ on 3 Nov 2025. It targeted about 22–26.5B KRW in IPO proceeds and about $10M revenue for 2025. — [PR Newswire](https://tools.prnewswire.com/en-us/live/20813/release/20251104EN12334); [VIR](https://vir.com.vn/nota-ai-gets-fast-track-nod-for-kosdaq-listing-133485.html)
- One secondary source says STMicroelectronics acquired Deeplite (model optimization). The deal date is unverified. — [ABI Research](https://www.abiresearch.com/research-highlight/tiny-machine-learning-ml-software-solutions?hsLang=en)
- The tinyML Foundation renamed itself the EDGE AI FOUNDATION at the end of 2024. In October 2026 it added LF Edge as a strategic partner and launched Physical AI/Robotics, Security and Interoperability working groups. — [PR Newswire](https://www.prnewswire.com/news-releases/edge-ai-foundation-announces-three-new-working-groups-and-strategic-partnership-with-lf-edge-to-accelerate-real-world-ai-deployments-302900935.html)

### Inferences
- Software-only TinyML firms are struggling to stay standalone. MCU vendors want their own model toolchain to win designs, so the remaining independents are likely acquisition targets.
- Qualcomm now holds an edge developer stack built from purchases: Foundries.io (2024), Edge Impulse (2025) and Arduino (2025). This last point comes from background knowledge and is not search-verified.

### Gaps
- None of the 2025–2026 status of Eta Compute, Ekkono, SensiML or Qeexo was verified. The SensiML/QuickLogic 2019, Qeexo/TDK 2023 and Reality AI/Renesas 2022 deal dates come from background knowledge.
- No 2026 list of EDGE AI FOUNDATION members could be retrieved.

## Edge orchestration / fleet management for AI

### Takeaway
ZEDEDA is the best-funded independent edge orchestrator. Barbara, Avassa, Sunlight, Edge Signal, Spectro Cloud and Scale Computing are also still independent. Two notable exits in 2025–2026: AVEVA bought Crosser, and d-Matrix bought Wallaroo.AI.

### Cited Findings
- ZEDEDA raised a $72M Series C led by Smith Point Capital, bringing its total to more than $127M. In January 2026 it said new customer wins had doubled year over year, and that SLB is building ZEDEDA into its Agora Edge AI platform. — [DCD](https://www.datacenterdynamics.com/en/news/edge-orchestration-platform-zededa-raises-72m/); [BusinessWire via Morningstar](https://www.morningstar.com/news/business-wire/20260127258815/zededa-accelerates-enterprise-momentum-doubling-new-customer-acquisition-with-major-fortune-500-wins)
- ZEDEDA and Avassa have a partnership: Avassa Edge Enforcer is sold in the ZEDEDA Marketplace. — [Avassa](https://avassa.io/press-releases/zededa-and-avassa-partner-to-deliver-secure-edge-application-orchestration-for-platform-teams-and-developers/)
- d-Matrix bought Wallaroo.AI (inference deployment and orchestration) in August 2026. It was d-Matrix's second acquisition in four months. — [StorageNewsletter](https://www.storagenewsletter.com/2026/08/11/d-matrix-acquires-wallaroo-ai-to-speed-up-deployment-of-heterogeneous-ai-inference-workloads/); [Dealroom](https://dealroom.co/news/142752-d-matrix-buys-wallaroo-ai-in-second-acquisition-in-four-months/)
- AVEVA bought Crosser, the Swedish edge analytics/DataOps company. It is now "Flows" in CONNECT, and the standalone product no longer takes new customers. Reported value is SEK 500M–1B. Mainsights reported the deal in December 2025; ARC calls it an April 2026 acquisition. — [Crosser](https://crosser.io/blog/crosser-has-been-acquired-by-aveva/); [AVEVA](https://www.aveva.com/en/connect-experience/about-connect/crosser-transition/); [ARC](https://www.arcweb.com/node/163625)
- Litmus says it is still independent. It partnered with InfluxData in April 2026 to run AI agents at the edge. Litmus's blog also claims that Schneider agreed on 30 June 2026 to buy Cognite for $3.1B. That claim is unverified and comes from a competitor's blog. — [BusinessWire](https://www.businesswire.com/news/home/20260420837867/en/InfluxData-and-Litmus-Partner-to-Power-Scalable-Industrial-AI-at-the-Edge); [Litmus blog](https://litmus.io/blog/compare-best-industrial-ai-platforms)
- Aggregator only: Barbara raised about $5.1–5.3M in February 2026 (investors include Aramco Ventures and Iberdrola), and Edgify raised a $9M Series A in August 2026. Armada raised a $230M Series B in May 2026 for modular edge AI data centers. — [newmarketpitch](https://newmarketpitch.com/blogs/news/edge-ai-funding-analysis) (page could not be fetched; figures conflict across its own pages)

### Inferences
- Edge orchestration is splitting into two camps. Infrastructure players (ZEDEDA, Scale, Sunlight, Spectro, Dell NativeEdge) manage the hardware and OS. AI-specific players (Barbara, Edge Signal, Wallaroo before its sale) manage model deployment. Large industrial software vendors are buying the second camp.

### Gaps
- No acquisition news turned up for Sunlight, Scale Computing, Avassa or Barbara. Funding amounts for Barbara and Edgify rely on one aggregator that was not fetched.

## Edge computer vision / video AI platforms running on-prem

### Takeaway
This is the largest sub-segment. It covers:
- Video-security AI startups: Spot AI, Coram, Lumana and Ambient.ai.
- Developer platforms: Network Optix/Nx AI Manager, Lumeo, viso.ai, alwaysAI, Roboflow and Chooch.
- Industrial inspection: Landing AI, Elementary, Mariner, Overview.ai, UnitX and Cognex.

New 2026 factory-vision raises include Tristar AI, Maneva and Almetra.

### Cited Findings
- Coram AI raised a $13.8M Series A led by Battery Ventures in January 2025. It adds AI search to existing IP cameras without needing specific hardware. — [VCA](https://www.vcaonline.com/news/2025011603/coram-ai-raises-13-8-million-in-series-a-funding-to-bring-ai-to-video-security-boosting-workplace-safety-and-efficiency/)
- Lumana raised a $40M Series A led by Wing VC in July 2025. — [Lumana](https://www.lumana.ai/blog/lumana-secures-40-million-to-lead-the-next-era-of-ai-powered-video-intelligence)
- Spot AI raised $31M in October 2024, bringing its total to about $93M, and launched Video AI Agents. Later rounds in 2025–2026 appear only on aggregators and conflict. — [Business Standard](https://business-standard.com/companies/start-ups/spot-ai-secures-31-mn-launches-video-ai-agents-for-enhanced-surveillance-124103101229_1.html); [KMWorld](https://www.kmworld.com/Articles/News/News/Spot-AI-debuts-Video-AI-Agents-transforming-camera-footage-into-a-proactive-valuable-data-source--166681.aspx)
- Tristar AI raised a $12.4M Series A led by Isogon Ventures on 12 Nov 2026. It does edge-stack visual inspection and says it runs on more than 500 production lines. — [PR Newswire](https://www.prnewswire.com/news-releases/tristar-ai-raises-12-4m-series-a-to-give-manufacturers-a-quality-inspector-that-never-blinks-302937353.html)
- Aggregator only:
  - Maneva: $27M Series A, June 2026 (factory video agents on NVIDIA edge devices).
  - Almetra, formerly Deltia (Berlin): €16.3M Series A, June 2026.
  - Hazen.ai: $8M, September 2026.
  - Surveily: $2.9M, March 2026.
  - SwitchOn (India, DeepInspect): $8M pre-Series B, July 2026.
  - Sources: [newmarketpitch](https://newmarketpitch.com/blogs/news/edge-ai-list-deals); [WoodenScale](https://www.woodenscale.ai/blogs/switchon-funding-8m-for-deepinspect-expansion/)
- Chooch's last disclosed round was a $20.1M Series A in November 2022. No acquisitions were found for Chooch, Cogniac, Neurala, alwaysAI or Lumeo. — [Dealroom](https://app.dealroom.co/companies/chooch_ai)

### Inferences
- "Video AI agents" built on VLMs are being added to camera fleets. Most vendors run a hybrid setup: detection on an on-site appliance, with LLM search in the cloud. Verkada and Rhombus are included but marked hybrid/cloud-managed because they qualify only borderline.

### Gaps
- The Specter "100+ video intelligence startups" landscape could not be fetched. It would likely add many more names.
- Status is unverified for Invisible AI, Drishti and Sixgill (marked "unknown").
- Background-knowledge deals not search-verified: Network Optix/Scailable (2024), Siemens/Inspekto (2024), Metropolis/Oosto (2024).

## Robotics / physical-AI edge inference software stacks

### Takeaway
Most of the money goes to robot foundation-model labs and chips, not to deployment software. The included edge-software stacks are Viam, Formant, Brain Corp, Field AI, Mujin, Micropsi, Intrinsic, Applied Intuition, Wind River and Sonatus.

### Cited Findings
- Aggregators say robotics startups raised about $18.8B in 2026. SiMa.ai raised a $150M Series C (September 2026), and D-Robotics a $150M Series B (April 2026). — [newmarketpitch](https://newmarketpitch.com/blogs/news/physical-ai-funding-news)
- Axelera AI raised a Series C of more than $250M in February 2026. Its Metis chips come with the Voyager SDK for vision and robotics inference. — [Wikipedia](https://en.wikipedia.org/wiki/Axelera_AI)
- The EDGE AI FOUNDATION's Physical AI/Robotics working group is led by NXP and includes AWS, Arduino, Analog Devices and DeepX. — [PR Newswire](https://www.prnewswire.com/news-releases/edge-ai-foundation-announces-three-new-working-groups-and-strategic-partnership-with-lf-edge-to-accelerate-real-world-ai-deployments-302900935.html)

### Inferences
- Robot foundation-model labs (Physical Intelligence, Skild AI) were left out of the JSON. Their models are not mainly sold as deployment software for customer-run edge hardware.

### Gaps
- The robotics edge stacks are drawn from background knowledge. None of them had funding or status checked by search.

## Acquisitions in this space, 2022–2026

### Takeaway
There were about 20 deals. Semiconductor companies bought TinyML and toolchain firms; industrial software companies bought edge data and orchestration firms.

### Cited Findings
- **2022:** Johnson Controls bought FogHorn; Renesas bought Reality AI; Aptiv bought Wind River; Intrinsic bought Vicarious; Zebra bought Matrox Imaging. All from background knowledge.
- **2023:** Infineon bought Imagimob ([source](https://www.imagimob.com/news/infineon-strengthens-its-offering-in-embedded-ai-solutions-through-acquisition-of-tinyml-leader-imagimob)). TDK bought Qeexo, IFS bought Falkonry, and NVIDIA bought OmniML (all background knowledge).
- **2024:** Qualcomm bought Foundries.io; NVIDIA bought Deci; Network Optix bought Scailable; Siemens bought Inspekto; Metropolis bought Oosto; Almaviva bought Iteris. All from background knowledge.
- **2025:**
  - Qualcomm bought Edge Impulse ([source](https://siliconangle.com/2025/03/10/qualcomm-acquires-edge-ai-development-startup-edge-impulse/)) and Arduino (background knowledge).
  - Nordic bought Neuton.AI ([source](https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-accelerates-edge-AI-leadership-with-acquisition-of-Neuton-AI)).
  - NXP bought Kinara, reported at $307M (secondary source).
  - AVEVA bought Crosser ([source](https://crosser.io/blog/crosser-has-been-acquired-by-aveva/)).
- **2026:**
  - d-Matrix bought Wallaroo.AI ([source](https://www.storagenewsletter.com/2026/08/11/d-matrix-acquires-wallaroo-ai-to-speed-up-deployment-of-heterogeneous-ai-inference-workloads/)).
  - An EE Times headline says Microchip is acquiring Hailo; the date is unclear ([source](https://www.eetimes.com/microchip-acquires-edge-ai-chip-startup-hailo/)).
  - Schneider buying Cognite is unverified ([Litmus blog](https://litmus.io/blog/compare-best-industrial-ai-platforms)).
- **Not acquisitions:** Voyager made a minority investment in Latent AI ([source](https://www.satellitetoday.com/technology/2025/08/18/voyager-technologies-makes-investment-into-ai-software-company-latent-ai/)). SparkCognition renamed itself Avathon in 2024 (background knowledge).

### Inferences
- Over 2023–2025, five MCU/SoC vendors each bought a TinyML or edge-ML toolchain. This suggests the model toolchain is now treated as a standard part of selling edge silicon.

### Gaps
- The deals listed above as background knowledge, and ST/Deeplite, need checking against press releases.
- Out-of-segment companies seen and added to the JSON:
  - edge-silicon: SiMa.ai, Axelera, Hailo, Kinara, DEEPX, EdgeCortix, Syntiant
  - efficient-models: Embedl, Deeplite, Deci, OmniML, Ultralytics
  - on-device-sdks: Picovoice
  - onprem-hardware: Armada
  - selfhosted-inference-llmops: Gcore
  - private-ai-platforms: Clarifai
  - consumer-local-apps: Frigate
- Seen but not added: Acrab (claimed $350M+ edge agentic AI stack; aggregator only), Era ($11M, AI-gadget software), Callosum, Mobilint, BrainChip, Physical Intelligence, Skild AI, Mind Robotics.
