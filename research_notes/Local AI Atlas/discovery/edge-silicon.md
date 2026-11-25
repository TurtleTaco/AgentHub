# Edge AI Silicon (segment: edge-silicon) — discovery notes

Dataset: `edge-silicon.json`, 153 entries. 128 are edge-silicon. The other 25 were seen out of segment: onprem-hardware 10, bigtech 9, on-device-sdks 4, efficient-models 1, industrial-edge 1.

**Method caveat (read first):** the shared WebSearch budget ran out after 13 searches. WebFetch to newmarketpitch.com, edge-ai-vision.com and edgeaifoundation.org was blocked by the session network allowlist, so the member/exhibitor lists (Edge AI and Vision Alliance, Edge AI Foundation) could not be read. Only the facts cited below with URLs were checked this session. Every other entry comes from prior knowledge (cutoff around mid-2026); its JSON `sources` field holds only the company homepage. Treat statuses and details not cited here as unverified until the profiling pass checks them.

## Edge AI accelerator startups: who they are and their current status

### Takeaway
The independent edge-accelerator field has consolidated around a few well-funded leaders: Hailo, Axelera AI, SiMa.ai, DEEPX, EnCharge AI and Mythic. Around them sits a long tail of ultra-low-power, analog/in-memory and neuromorphic startups. Several 2019–2021-era players failed or were absorbed in 2024–2025: Kinara, Untether AI, Esperanto, Rain AI and Perceive.

### Cited Findings
- Mythic closed a $125M round led by DCVC (announced Dec 17, 2025). It claims its analog processing units are 100x more energy-efficient than GPUs; that figure comes from the company and has not been independently tested. It had previously raised $13M in Mar 2023 — [Business Wire](https://www.businesswire.com/news/home/20251217546249/en/Mythic-to-Challenge-AIs-GPU-Pantheon-with-100x-Energy-Advantage-and-Oversubscribed-$125M-Raise); [DCVC](https://www.dcvc.com/news-insights/mythic-raises-125m-to-break-through-ais-power-wall/)
- DEEPX confirmed preparations for a public share offering in April 2026 — [tech-insider.org](https://tech-insider.org/deepx-ipo-2026-korean-edge-ai-chip-700-million/)
- Axelera AI's Metis chip targets edge inference such as computer vision and robotics — [Wikipedia](https://en.wikipedia.org/wiki/Axelera_AI)
- The newmarketpitch.com aggregator reported several 2026 rounds. These could not be fetched or checked against primary sources: Axelera Series C (>$250M, Feb 24, 2026), SiMa.ai $150M Series C (Sep 28, 2026), Quadric Series C ($30M Jan 2026 + $16M Jul 2026), DEEPX Series D+ (conflicting $67.6M vs $29M), and "iHW" $37.5M Series A for analog compute-in-memory. The aggregator also named "VisiNextek" and "HrdWyr"; I could not verify they exist, so I left them out of the JSON. Aggregator URL: https://newmarketpitch.com/blogs/news/edge-ai-chips-funding-trends (blocked).
- A team of former Untether AI staff founded Toronto-based Hepzibah AI to keep working on energy-efficient compute — [BetaKit](https://betakit.com/?p=395741)
- Ainekko acquired all of Esperanto's IP and selected assets (Nov 19, 2025) and plans to open-source the many-core RISC-V design as an edge AI platform — [EEJournal](https://www.eejournal.com/industry_news/ainekko-acquires-esperanto-technologies-intellectual-property-to-power-open-source-edge-ai-platform)

### Inferences
- From prior knowledge, not re-verified: Blaize listed on Nasdaq (BZAI) via a SPAC in Jan 2025. EnCharge AI raised a ~$100M Series B in early 2025 and launched EN100 for AI PCs. Hailo shipped the Hailo-10H GenAI accelerator in 2025. Ambiq IPO'd on NYSE (AMBQ) in mid-2025. Sagence AI emerged from stealth in 2024, reportedly formerly called Analog Inference.
- Edge LLM inference is the 2025–2026 product theme across vendors: Hailo-10H, DEEPX DX-M2, Axelera, SiMa Modalix, EnCharge EN100, Kinara Ara-2, Rockchip RK182x, Axera AX8850, Ambarella N1, Skymizer EdgeThought and Neuchips Viper.
- Analog/in-memory compute is the most crowded sub-category: Mythic, EnCharge, Sagence, TetraMem, Blumind, Aspinity, Ambient Scientific, Semron, Synthara, Anaflash, Houmo, WITINMEM, PIMCHIP, Reexen. It also has the highest failure rate: Rain AI, Untether and Gyrfalcon are gone.

### Gaps
- Current status of Deep Vision, AlphaICs, Eta Compute, ArchiTek, LeapMind, Anaflash, PIMCHIP, Reexen and Corerain is unknown; all are marked `unknown`.
- Kneron's reported 2025 SPAC/listing plans could not be checked (search budget exhausted).
- Few genuinely new 2025–2026 edge-silicon startups were found. The Edge AI Foundation and Edge AI and Vision Alliance member lists, plus CB Insights maps, would be the best way to fill this gap once those hosts are allowed.
- Blumind, Ainekko, Hepzibah AI, Skymizer, Neurobus, PIMCHIP, Reexen, Corerain and ArchiTek have `website: null` because I was not confident of the domain.

## Edge AI IP vendors

### Takeaway
NPU IP licensing is led by Arm (Ethos), Ceva (NeuPro), Cadence (Neo/Tensilica) and VeriSilicon (Vivante). Synopsys has exited processor IP. GlobalFoundries now combines ARC with MIPS, while RISC-V AI IP (SiFive, Andes, Semidynamics, Codasip) and independent NPU IP startups (Quadric, Expedera, OpenEdges, Skymizer, Synthara) compete for SoC design wins.

### Cited Findings
- GlobalFoundries completed its acquisition of Synopsys' Processor IP Solutions business. The deal covers ARC-V, ARC-Classic, ARC VPX DSP, ARC NPX NPU, and the ASIP Designer/Programmer tools. Synopsys keeps its interface and foundation IP — [Nasdaq/GF press release](https://www.nasdaq.com/press-release/globalfoundries-completes-acquisition-synopsys-processor-ip-solutions-business); [Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/globalfoundries-acquires-arc-and-risc-v-ip-from-synopsys-company-gains-critical-cpu-ip-as-it-grows-beyond-being-a-mere-chipmaker)
- The ARC business was folded into GF's MIPS unit. The closing was reported as June 2, 2026 — [GF investor PDF](https://investors.gf.com/node/10841/pdf)

### Inferences
- From prior knowledge, not re-verified: GlobalFoundries bought MIPS in 2025. Google released an open-source RISC-V "Coral NPU" IP in 2025 and Synaptics adopted it in its Astra MCUs. Imagination Technologies' owner was reported to be exploring a sale. Codasip was reported to be up for sale in 2025.
- IP vendors in the JSON: Arm, Ceva, Cadence, Synopsys ARC (now GF), MIPS (GF), VeriSilicon, Imagination, SiFive, Andes, Codasip, Semidynamics, Chips&Media, Think Silicon (Applied Materials), OpenEdges, Quadric, Expedera, Skymizer, Synthara, BrainChip (also IP), LeapMind (status unknown).

### Gaps
- I did not check Imagination's or Codasip's 2026 ownership.
- Nuclei, Akeana, StarFive and InCore are RISC-V IP firms with weak AI angles; they were left out.

## Specialist public companies with edge AI SoCs

### Takeaway
Every major MCU/embedded vendor now ships an integrated NPU (NXP, ST, Renesas, Infineon, TI, Microchip, Silicon Labs, Nordic, Nuvoton, ADI, Ambiq). M&A is reshaping the field: NXP bought Kinara and is reportedly pursuing Ambarella, and TI is buying Silicon Labs. Chinese listed players (Horizon, Black Sesame, Rockchip, Allwinner, Amlogic, Intellifusion, Canaan, Bestechnic) dominate domestic camera, auto and IoT edge AI.

### Cited Findings
- NXP closed its Kinara acquisition on Oct 27, 2025 for $307M in cash. The deal was first announced in Feb 2025, and NXP says it expands its portfolio for AI-powered edge systems in industrial/IoT and automotive — [NXP newsroom](https://www.nxp.com/company/about-nxp/newsroom/NW-NXP-COMPLETES-ACQUISITIONS-AVIVA-LINKS-KINARA); [NXP IR](https://investors.nxp.com/news-releases/news-release-details/nxp-completes-acquisitions-aviva-links-and-kinara-advance/)
- On Jul 31, 2026 the FT reported that NXP was in talks to acquire Ambarella (market value about $3.3B). A deal was not certain, and I found no definitive agreement — [SiliconANGLE](https://siliconangle.com/2026/07/31/nxp-reportedly-talks-acquire-vehicle-chip-supplier-ambarella/)
- TI agreed on Feb 4, 2026 to buy Silicon Labs for $231/share in cash (about $7.5B), with closing expected in H1 2027 — [Silicon Labs news release](https://news.silabs.com/2026-02-04-Texas-Instruments-to-acquire-Silicon-Labs)

### Inferences
- From prior knowledge, not re-verified: Horizon Robotics listed on HKEX in Oct 2024 and Black Sesame in Aug 2024. Axera and SemiDrive have pursued Hong Kong listings. Rockchip's RK182x LLM coprocessors launched in 2025. Nordic added an NPU from its 2023 Atlazo acquisition and bought Neuton.AI in 2025. Qualcomm bought Edge Impulse and Arduino in 2025.
- Qualcomm and MediaTek are classed as edge-silicon because edge SoCs are their core business. Apple, Google, Intel, AMD, NVIDIA, Samsung, IBM, HiSilicon and T-Head are placed under `bigtech`.

### Gaps
- I could not confirm a public-listing status for SigmaStar (`type: null`), Axera or SemiDrive.
- These were not included: Novatek, Augentix, OmniVision, onsemi (image sensors with limited AI processing), QuickLogic/SensiML (unclear status), Kalray and Moore Threads.

## Neuromorphic and event-based companies

### Takeaway
Neuromorphic edge silicon is a small, fragile niche. SynSense, Innatera, BrainChip, POLYN, Lynxi and Applied Brain Research are active. GrAI Matter Labs went to Snap, and event-sensor leader Prophesee filed for insolvency in early 2025 but kept operating.

### Cited Findings
- Prophesee filed for insolvency in January 2025. The CEO said operations continued as normal. Its sensors were made with Sony (e.g., the IMX636), and it raised a €50M Series C in 2022 — [Image Sensors World](https://image-sensors-world.blogspot.com/2025/01/prophesee-files-for-insolvency.html); [f4news](https://www.f4news.com/2025/01/29/prophesee-files-for-insolvency/); [Optics.org](https://optics.org/news/prophesees-sensors-proliferate-with-industrial-partners)
- Rain AI, often described as neuromorphic, failed to close a planned $150M Series B. It sought a buyer by May 2025, and OpenAI later acquired some of its patents after full-acquisition talks failed — [StartupWired](https://startupwired.com/2025/05/16/rain-ai-the-rise-and-fall-of-a-chipmaking-challenger/); [Mitrade](https://www.mitrade.com/ae-en/insights/news/live-news/article-3-1973287-20260807)

### Inferences
- From prior knowledge, not re-verified: Snap acquired GrAI Matter Labs in 2023. Innatera launched its Pulsar neuromorphic MCU in 2025. SpiNNcloud (SpiNNaker2) targets on-prem systems rather than devices, so it sits under `onprem-hardware`.
- Other neuromorphic/event entries: SynSense, iniVation, Neurobus, Lynxi, BrainChip, Innatera, POLYN, Applied Brain Research, Intel Loihi (in the Intel entry) and IBM NorthPole (in the IBM entry).

### Gaps
- The outcome of Prophesee's insolvency proceedings (continuation plan versus sale) is unverified. Sources disagree on the date of Rain AI's patent sale (2025 vs 2026).
- General Vision (NeuroMem) and Celepixel (OmniVision) were not added.

## Acquisitions and shutdowns, 2023–2026

### Takeaway
Between 2023 and 2026, at least 15 notable edge-silicon or adjacent companies were acquired, acqui-hired or shut down. The buyers were mostly large incumbents (NXP, AMD, Amazon, Snap, Nordic, ADI, GlobalFoundries, Qualcomm, Infineon, TI).

### Cited Findings
- **Untether AI (Canada):** AMD hired its whole engineering team in June 2025. The IP was not part of the deal, Untether ended support for speedAI and imAIgine, and it later filed for bankruptcy owing $128M — [Tom's Hardware](https://www.tomshardware.com/tech-industry/amd-scoops-entire-untether-ai-chip-team-canada-ai-inference-outfit-will-cease-product-support); [BetaKit](https://betakit.com/american-chip-giant-amd-to-acquire-untether-ai-team/); [BetaKit bankruptcy](https://betakit.com/?p=395741)
- **Esperanto Technologies:** wound down its silicon business in July 2025, and Ainekko bought its IP in Nov 2025 — [EE Times Japan](https://eetimes.itmedia.co.jp/ee/articles/2507/10/news051.html); [EEJournal](https://www.eejournal.com/industry_news/ainekko-acquires-esperanto-technologies-intellectual-property-to-power-open-source-edge-ai-platform)
- **Kinara:** acquired by NXP for $307M (closed Oct 2025) — [NXP](https://www.nxp.com/company/about-nxp/newsroom/NW-NXP-COMPLETES-ACQUISITIONS-AVIVA-LINKS-KINARA)
- **Synopsys ARC/NPX IP:** acquired by GlobalFoundries (closed 2026) — [Nasdaq/GF](https://www.nasdaq.com/press-release/globalfoundries-completes-acquisition-synopsys-processor-ip-solutions-business)
- **Silicon Labs:** TI deal pending, announced Feb 2026 — [Silicon Labs](https://news.silabs.com/2026-02-04-Texas-Instruments-to-acquire-Silicon-Labs)
- **Rain AI:** effectively defunct; patents went to OpenAI — [StartupWired](https://startupwired.com/2025/05/16/rain-ai-the-rise-and-fall-of-a-chipmaking-challenger/)

### Inferences
- From prior knowledge, not re-verified: Perceive went to Amazon (2024), GrAI Matter Labs to Snap (2023), Atlazo to Nordic (2023), Flex Logix to Analog Devices (2024) and MIPS to GlobalFoundries (2025). Edge Impulse (2025) and Arduino (2025) went to Qualcomm, Neuton.AI to Nordic (2025), Imagimob to Infineon (2023) and Graphcore to SoftBank (2024). Gyrfalcon was defunct by about 2022.
- The pattern: discrete-accelerator startups without volume design wins get absorbed by MCU/SoC incumbents, who fold the NPUs into their own chips. Datacenter-adjacent inference startups (Untether, Esperanto, Rain) failed under competition for talent and capital; Esperanto's CEO cited rivals offering 2–4x pay.

### Gaps
- I did not verify claims of an NVIDIA–Groq licensing deal (Dec 2025) or a Ventana–Qualcomm deal. Groq is listed as onprem-hardware without the deal; Ventana was omitted.

### Out-of-segment companies seen (included in JSON with their segment key)
- **onprem-hardware:** Rebellions (raised $400M pre-IPO in Mar 2026 per [Wikipedia](https://en.wikipedia.org/wiki/Rebellions_(company))), FuriosaAI, Tenstorrent, d-Matrix, Graphcore, Cambricon, VSORA, Recogni, SpiNNcloud, Preferred Networks.
- **bigtech:** Apple, Google (Coral), Intel, AMD, NVIDIA, Samsung, IBM, HiSilicon, T-Head.
- **on-device-sdks / efficient-models / industrial-edge:** Edge Impulse, Neuton.AI, Imagimob, Plumerai, Nota AI, Arduino.
- **Seen but not added:** Groq, Cerebras, SambaNova, Etched, Positron, MatX, Fractile, Taalas, NeuReality, Unconventional AI, Lightmatter (all onprem/datacenter); Aizip, Useful Sensors (efficient-models / on-device).
