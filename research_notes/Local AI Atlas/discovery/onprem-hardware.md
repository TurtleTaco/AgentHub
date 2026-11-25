# On-prem / Sovereign AI Hardware & Systems (segment: onprem-hardware)

Companion to `onprem-hardware.json` (89 companies: 78 onprem-hardware, 4 bigtech hyperscalers, 7 out-of-segment). Research date: 2026-11-25. About 32 web searches; I fetched no pages, so the findings rest on search-result summaries of the cited articles. Some JSON entries cite only the vendor homepage, for well-known firms I did not re-verify this session (Pure Storage, MinIO, Cloudian, Pliops, IBM Spyre, Fujitsu, Eviden/Bull, Netweb, QCT, Wiwynn, Inspur, Hypertec, Exxact, Puget, BOXX, BIZON, Comino, Boston, XENON, AMAX, Moore Threads, Nutanix, Axelera, Ampere, Oracle, Normal Computing, Esperanto, Lightmatter). Treat their one-liners as background knowledge, not session-verified facts.

## Inference accelerator companies selling on-prem racks/appliances, and current status

### Takeaway
2025–2026 brought consolidation and very large funding rounds. NVIDIA took Groq's technology and leaders through a license. AMD bought Taalas and acqui-hired Untether. Intel's SambaNova acquisition fell through. Cerebras went public. Etched, Positron, MatX and Fractile raised at multi-billion valuations. Most independents now sell air-cooled racks that drop into existing customer data centers.

### Cited Findings
- **Groq:** On Dec 24, 2025 Groq announced a non-exclusive license of its inference technology to NVIDIA. Founder Jonathan Ross, President Sunny Madra and others joined NVIDIA, and Simon Edwards became CEO. Groq said GroqCloud continues and that it remains independent — [Groq](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale). Tom's Hardware reported ~$20B — [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/nvidia-confirms-20-billion-groq-deal-to-bolster-ai-inference-dominance). Groq gave no price. I found no primary statement on GroqRack's status after the deal. Sacra claims NVIDIA showed a Groq-derived "Groq 3 LPX" with Vera Rubin in March 2026; this is unverified — [Sacra](https://sacra.com/chat/h/e43b369e-0859-4265-9207-48b46aaf0a75/).
- **Cerebras:** IPO closed May 15, 2026 on Nasdaq (CBRS), raising ~$6.38B gross with the over-allotment. Its model has three channels: on-prem hardware, its own cloud, and partner clouds — [Cerebras](https://www.cerebras.ai/press-release/cerebras-systems-announces-closing-of-initial-public-offering). 2025 revenue was $510M with $87.9M net income — [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-17/ai-chipmaker-cerebras-systems-files-publicly-again-for-us-ipo).
- **SambaNova:** Intel's ~$1.6B acquisition talks collapsed in January 2026. In February 2026 they were replaced by a multiyear collaboration and Intel's $350M commitment to SambaNova's Series F — [Jon Peddie](https://www.jonpeddie.com/news/ok-no-wedding-but-can-we-still-date/); [Finviz/Bloomberg](https://finviz.com/news/320765/intel-ceo-bets-on-sambanova-partnership-to-challenge-nvidias-ai-dominance).
- **d-Matrix:** Corsair entered full production in June 2026. The Squadron multi-rack clusters (Oct 2026, with Arista, Broadcom and Supermicro) ship to "priority customers for deployment in their own data centers." They are air-cooled, so no liquid-cooling build-out is needed — [HPCwire](https://www.hpcwire.com/off-the-wire/d-matrix-corsair-ai-inference-platform-enters-full-production-to-meet-customer-demand); [StorageNewsletter](https://www.storagenewsletter.com/2026/10/16/ocp-global-summit-2026-d-matrix-announces-squadron-compute-clusters-for-ai-inference-at-data-center-scale/).
- **Positron:** $230M Series B in Feb 2026 at >$1B valuation — [TechCrunch](https://techcrunch.com/2026/02/04/exclusive-positron-raises-230m-series-b-to-take-on-nvidias-ai-chips). Later an $875M Series C at a $5B valuation; its chips use LPDDR5X rather than HBM — [Dealroom](https://dealroom.co/news/150061-positron-raises-875m-series-c-at-5b-valuation-for-inference-chips/).
- **Etched:** Came out of stealth with ~$800M raised and >$1B in signed contracts. It planned summer 2026 rack shipments — [Converge Digest](https://convergedigest.com/etched-emerges-from-stealth-with-800m-raised-for-ai-inference-systems/); [eWeek](https://www.eweek.com/news/etched-ai-chip-contracts). One report says the first rack went to Jane Street — [byteiota](https://byteiota.com/etched-21b-sohu-chip-ships/). Other coverage says it was still in customer validation (conflicting). Valuation figures conflict, from $5B to $10.3B.
- **Tenstorrent:** Galaxy Blackhole became generally available in April/May 2026: 32 Blackhole chips in 6U, ~$110K per system — [The Register](https://theregister.com/2026/04/28/tenstorrent_galaxy_blackhole_ai_servers_ga). Price conflict: Unite.ai cites $160K per system. On-prem partners include Smallest.ai (voice) — [Unite.ai](https://www.unite.ai/on-prem-voice-agents-get-new-hardware-path-as-smallest-ai-joins-tenstorrent/) — and ConfidentialMind, per Tenstorrent's newsroom.
- **FuriosaAI:** RNGD went into mass production in January 2026, with 20,000 cards planned for 2026. The NXT RNGD Server is 4U and 3kW with 8 cards, 4 PFLOPS FP8 and 384GB HBM3 — [CRN Asia](https://www.crnasia.com/news/2026/components-and-peripherals/furiosaai-to-scale-rngd-inference-chip-production-following). The IPO is expected 2027–2028 — [Korea Times](https://www.koreatimes.co.kr/business/tech-science/20260805/korean-npu-makers-seek-track-records-ahead-of-potential-ipos).
- **Rebellions:** Raised a 640B won (~$448M) pre-IPO round in March 2026 at a 3.4T won valuation, with IPO timing under review — [Korea Times](https://www.koreatimes.co.kr/business/tech-science/20260805/korean-npu-makers-seek-track-records-ahead-of-potential-ipos).
- **NeuReality:** Unconventional AI agreed on Oct 26, 2026 to acquire it, with closing expected Q4 2026 — [Magica](https://magica.com/news/unconventional-ai-neureality-acquisition-production-systems).
- **Fractile:** $220M Series B in May 2026 (~$1.1B valuation) — [TNW](https://thenextweb.com/news/fractile-220m-inference-chip). A reported $720M round in Nov 2026 at a $7B valuation has a single source citing Reuters — [SiliconANGLE](https://siliconangle.com/2026/11/11/inference-chip-developer-fractile-raises-720m-in-funding/). No production chip yet.
- **MatX:** $500M Series B on Feb 24, 2026, led by Jane Street and Situational Awareness — [SiliconANGLE](https://siliconangle.com/2026/02/24/chip-startup-matx-raises-500m-speed-large-language-models/). Sacra cites an unverified Reuters report of Anthropic acquisition talks — [Sacra](https://sacra.com/c/matx).
- **Taalas:** The HC1 (Feb 2026) hardwires Llama 3.1 8B and claims ~17k tokens/s per user — [CNX Software](https://www.cnx-software.com/2026/02/22/taalas-hc1-hardwired-llama-3-1-8b-ai-accelerator-delivers-up-to-17000-tokens-s/). AMD announced the acquisition in Aug 2026 — [AMD IR](https://ir.amd.com/news-events/press-releases/detail/1296) — and completed it per [TechPowerUp](https://www.techpowerup.com/354943/amd-completes-acquisition-of-taalas-to-advance-ai-inference).
- **Tensordyne (ex-Recogni):** Napier was announced June 2026: 3nm, logarithmic math, 72-chip air-cooled quarter-rack pods. Shipments are targeted late 2026 and volume mid-2027. Performance claims are self-reported — [RuntimeWire](https://www.runtimewire.com/article/tensordyne-napier-log-math-ai-inference-chip); [IEEE Spectrum](https://spectrum.ieee.org/inference-hardware-revolution).
- **Untether AI:** AMD hired the whole engineering team in June 2025, and speedAI product supply and support ended — [Tom's Hardware](https://www.tomshardware.com/tech-industry/amd-scoops-entire-untether-ai-chip-team-canada-ai-inference-outfit-will-cease-product-support).
- **Graphcore:** Acquired by SoftBank in July 2024 — [TechCrunch](https://techcrunch.com/2024/07/11/softbank-acquires-uk-ai-chipmaker-graphcore).
- **HyperAccel (Korea):** Showed an 8-LPU server at SC26. It claims 3.5x tokens per watt and per dollar versus RTX PRO 6000 servers — [Plataforma Media](https://www.plataformamedia.com/en/2026/11/12/hyperaccel-to-showcase-lpu-based-ai-inference-system-at-sc26-highlighting-power-and-cost-efficiency/). **VSORA (France):** Jotunn8 has 288GB HBM3e, with sampling expected late 2026 — [DataCentreNews](https://datacentrenews.uk/story/vsora-unveils-jotunn8-ai-chip-after-eur-40-million-boost).
- **Qualcomm:** AI200 (2026) and AI250 (2027) rack-scale inference: 768GB LPDDR per card, 160kW liquid-cooled racks. HUMAIN plans 200MW — [Qualcomm](https://www.qualcomm.com/news/releases/2025/10/qualcomm-unveils-ai200-and-ai250-redefining-rack-scale-data-cent); [ServeTheHome](https://www.servethehome.com/qualcomm-announces-new-integrated-ai-racks-with-768gb-cards-and-a-200mw-ai-deal/). I found no confirmation that it shipped in 2026.
- **Huawei:** Atlas 950 SuperPoD (up to 8,192 Ascend NPUs, open-source CANN) was shown abroad at MWC 2026. The air-cooled Atlas 850 targets enterprises — [TechRadar](https://www.techradar.com/pro/huawei-debuts-its-atlas-950-ai-superpod-at-mwc-2026-taking-the-ai-data-center-fight-to-nvidia-and-amd). Forrester says Atlas nodes will compete with Dell, HPE and Lenovo servers — [Forrester](https://www.forrester.com/blogs/huawei-connect-2025-building-ai-infrastructure-in-a-sanctioned-world/).

### Inferences
- The "air-cooled, drops into existing racks" pitch (d-Matrix, FuriosaAI, Tensordyne, Positron) is the main way the independents target enterprise and sovereign on-prem buyers, as opposed to hyperscalers.
- Big vendors are absorbing inference architectures through licensing or acqui-hires (NVIDIA–Groq, AMD–Taalas/Untether, Unconventional–NeuReality, NVIDIA–Enfabrica). Startups that stay independent need very large rounds.

### Gaps
- Lightmatter and Normal Computing: no 2026 news found. Their on-prem relevance is indirect (interconnect and research silicon).
- Esperanto: reports say it folded its chip business (via EE Times, cited secondhand). I found no dated primary source; status "defunct" is low-confidence.
- Not verified: Enfabrica→NVIDIA (2025), Celestial AI→Marvell, Rain AI status, Moore Threads/MetaX/Biren listings, Ampere→SoftBank closing date. Of these, only Moore Threads and Ampere are in the JSON (homepage sources only).
- No independent benchmarks exist for most vendor performance claims (Taalas, Tensordyne, HyperAccel, VSORA, Tenstorrent).

## Server/system OEMs with private-AI offerings

### Takeaway
Dell, HPE, Lenovo, Supermicro and Cisco each sell a packaged "AI factory" or private-AI stack built on NVIDIA. Taiwanese ODM/OEMs (GIGABYTE, ASUS, QCT, Wiwynn, MSI) and regional builders (Inspur, Netweb, Hypertec, Penguin, Eviden/Bull, Fujitsu) fill out the supply side. I found no 2026 customer counts for any of them.

### Cited Findings
- **HPE Private Cloud AI** gained agent registration and governance, a unified model gateway, multi-node inference up to 256 GPUs, and MCP support at HPE Discover 2026 — [TWIML](https://twimlai.com/articles/hpe-discover-2026-ai-production-era-infrastructure-story). An HPE executive said production AI for most enterprises runs on-prem (vendor claim) — [Next Platform](https://www.nextplatform.com/a/5259579).
- **Cisco Secure AI Factory with NVIDIA:** rack-scale validated designs managed via Cisco Cloud Control — [Cisco](https://www.cisco.com/c/en/us/solutions/collateral/artificial-intelligence/secure-ai-factory-nvidia-rackscale-enterprise-so.html).
- **Dell AI Factory / PowerEdge XE97xx:** turnkey servers, racks and storage — [IntuitionLabs](https://intuitionlabs.ai/articles/on-prem-ai-infrastructure-comparison). Dell builds the Google-certified 8-GPU appliance used to deliver Gemini on-prem — [VentureBeat](https://venturebeat.com/technology/googles-gemini-can-now-run-on-a-single-air-gapped-server-and-vanish-when-you-pull-the-plug).
- **Penguin Solutions** became an NVIDIA AI Factory Specialized Partner in June 2026. Its OriginAI blueprints scale to 16,000+ GPUs, and it manages sovereign clusters such as SK Telecom Haein — [Penguin IR](https://ir.penguinsolutions.com/news/news-details/2026/Penguin-Solutions-Becomes-an-NVIDIA-AI-Factory-Specialized-Partner/default.aspx); [Penguin](https://www.penguinsolutions.com/en-us/industries/sovereign-ai).
- **Supermicro** publishes sovereign-AI telecom designs — [Supermicro](https://www.supermicro.com/solutions/Solution_Brief_Sovereign_AI_for_Telecom.pdf) — and is a d-Matrix Squadron partner — [StorageNewsletter](https://www.storagenewsletter.com/2026/10/16/ocp-global-summit-2026-d-matrix-announces-squadron-compute-clusters-for-ai-inference-at-data-center-scale/).

### Inferences
- Non-NVIDIA accelerators reach enterprises mainly through OEM partnerships (e.g., Supermicro with d-Matrix). Watch for Dell/HPE/Lenovo adding AMD, Qualcomm or Intel options.

### Gaps
- Hypertec, Netweb, QCT, Wiwynn, Inspur, Fujitsu and Eviden/Bull were not verified this session. Bull's ownership after the Atos restructuring is unconfirmed, so type is null.

## AI workstations & desktop supercomputers

### Takeaway
NVIDIA's GB10 "DGX Spark" platform has seven OEM partners selling nearly identical boxes. Boutique builders (Puget, BOXX, Exxact, BIZON, Comino) and tiny corp serve power users. Olares One sits at the prosumer end.

### Cited Findings
- **DGX Spark OEMs:** Acer Veriton GN100, ASUS Ascent GX10, Dell Pro Max GB10, GIGABYTE AI TOP Atom, HP ZGX Nano, Lenovo ThinkStation PGX, MSI EdgeXpert — [heise](https://heise.de/-10759895); [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-launches-ai-first-dgx-personal-computing-systems-with-global-computer-makers). All use the same 128GB LPDDR5X and 273 GB/s memory — [Spheron](https://www.spheron.network/blog/dgx-spark-alternatives-dell-asus-hp-lenovo-gb10-compared-2026/).
- **tiny corp:** configurable tinybox builds from $7,000 without GPUs; NVIDIA configurations require KYC — [Notebookcheck](https://notebookcheck.net/tiny-corp-s-four-gpu-ai-workstation-packs-serious-amd-epyc-power-but-buying-one-isn-t-straightforward.1419179.0.html). The "exabox" is on preorder at $10M, with shipments expected 2027 — [Gigazine](https://gigazine.net/news/20260407-exabox-container-ai-computer/). Prices for red/green v2 conflict across sources.
- **Olares One:** RTX 5090 laptop GPU (24GB), Core Ultra 9 and 96GB DDR5 in a 3.5L case running open-source Olares OS, ~$2,899–$2,999 — [SiliconANGLE](https://siliconangle.com/2025/12/09/olares-launches-personal-ai-computer-turns-local-files-smart-assistant/); [TechPowerUp](https://www.techpowerup.com/342779/olares-to-launch-a-personal-ai-device-bringing-cloud-level-performance-home).

### Inferences
- GB10 boxes are commoditized, so OEMs compete on cooling, software bundles and channel rather than silicon.

### Gaps
- DGX Station (GB300) OEM list and pricing were not confirmed. Lambda's current on-prem hardware sales are unclear (it may now be cloud-focused), so it is excluded. Strix Halo mini-PCs (GMKtec EVO-X2, Framework Desktop) and Apple Mac Studio are left to the consumer/on-device researchers.

## Private-AI appliances / "AI in a box"

### Takeaway
A crowded long tail of small-office appliances exists. Lemony (Uptime Industries) is the best-funded US example. Many others are early-stage or hybrid; Luz AIbox, for one, uses cloud LLMs.

### Cited Findings
- **Lemony:** stackable nodes support LLMs up to ~75B parameters and ship with Granite/Llama models. Reported pricing is from $499/month for 5 users. $2M seed (True Ventures, JetBrains). Partners: IBM, JetBrains, Carahsoft — [TechCrunch](https://techcrunch.com/2025/06/11/uptime-industries-wants-to-boost-localized-ai-usage-with-an-ai-in-a-box-called-lemony-ai); [Campus Technology](https://campustechnology.com/articles/2025/10/08/lemony-introduces-on-premise-ai-device-for-enterprises.aspx).
- **Others:** LionBox (1–30 users), PrivateBox AI (NVIDIA-based), VaultLLM (India, SMB), Cuon/TerraSky (Japan, launch Nov 1, 2026), MyRepublic AI Automation Box (Singapore, 20–200 staff) — [LionBox](https://www.lionbox.ai/); [PrivateBox](https://privateboxai.com/); [BigGo/Cuon](https://finance.biggo.com/news/ir_3915.T_20260924_7f90862babdd); [Malay Mail](https://www.malaymail.com/amp/news/money/mediaoutreach/2025/09/03/myrepublic-launches-ai-automation-box-an-industry-first-plug-and-play-ai-server-that-lets-smes-automate-their-business/406541).
- **Seen but excluded:** Luz AIbox (on-device orchestration, cloud LLMs), Axis One (pre-order/MVP), devxt, Sparki Box — [Luz](https://aiagent.luztrend.com/en/product.html); [Axis One](https://runany.dev/blog/axis-one-local-llm-appliance/).

### Inferences
- Appliance specs and prices come almost entirely from vendor marketing, and many of these vendors may not survive. Treat them as low-confidence.

### Gaps
- No funding or traction data for LionBox, PrivateBox AI or VaultLLM. HQ countries are unknown for several.

## Storage/data platforms for on-prem AI inference

### Takeaway
Storage vendors now pitch KV-cache offload and inference data paths. VAST ($30B valuation) leads the startups. NetApp is acquiring PEAK:AIO. WEKA's Augmented Memory Grid targets time-to-first-token directly.

### Cited Findings
- **VAST Data:** $1B Series F at $30B valuation (Apr 2026) — [Built In](https://builtin.com/articles/vast-data-raises-1b-series-f-30b-valuation-20260423). Reported $10B in commitments (Nov 2026) — [HPCwire](https://www.hpcwire.com/bigdatawire/2026/11/10/vast-data-reports-10b-in-commitments-as-ai-storage-spending-surges/).
- **WEKA:** Augmented Memory Grid is GA. It claims 1000x GPU memory extension and up to 20x faster TTFT (vendor claims) — [WEKA](https://www.weka.io/news/weka-breaks-the-ai-memory-barrier-with-augmented-memory-grid). NeuralMesh integrates with NVIDIA STX — [StorageReview](https://www.storagereview.com/news/weka-integrates-neuralmesh-with-nvidia-stx-to-address-ai-inference-memory-bottlenecks). No 2026 funding found.
- **NetApp–PEAK:AIO:** announced Sept 2026 for pNFS/metadata scaling; PEAK:AIO also had a CXL KV-cache platform — [StorageReview](https://www.storagereview.com/news/netapp-to-acquire-peakaio-bringing-its-scale-out-pnfs-metadata-work-to-ontap); [Blocks & Files](https://www.blocksandfiles.com/file/2026/09/25/netapp-buying-peakaio-to-give-ontap-parallel-nfs-injection/5299234). Sources differ on whether the deal has closed.
- **Hammerspace:** $100M at >$500M valuation (Apr 2025) — [TechCrunch](https://techcrunch.com/2025/04/16/hammerspace-an-unstructured-data-wrangler-used-by-nvidia-meta-and-tesla-raises-100m-at-500m-valuation). **DDN:** $300M Blackstone investment, undated in results — [Blocks & Files](https://blocksandfiles.com/tag/ddn).

### Inferences
- KV-cache tiering (WEKA, Pliops, PEAK:AIO) is becoming a distinct inference-infrastructure category relevant to on-prem TCO.

### Gaps
- Pure Storage, MinIO, Cloudian, IBM Storage Scale and Pliops were not verified this session (homepage sources only).

## Sovereign AI factory integrators and hyperscaler on-prem offerings

### Takeaway
All four hyperscalers now sell on-prem or disconnected options: AWS AI Factories (Dec 2025), Google Distributed Cloud air-gapped with Gemini, Azure Local, and Oracle Cloud@Customer/Dedicated Region. Integrators such as WWT, Penguin, Mark III and Cirrascale build customer-owned and sovereign AI factories.

### Cited Findings
- **AWS AI Factories** (re:Invent, Dec 2, 2025): single-tenant NVIDIA GPU and Trainium racks with AWS networking and storage, plus Bedrock/SageMaker, in customer or colo data centers. Priced after a joint assessment — [AWS](https://aws.amazon.com/about-aws/whats-new/2025/12/aws-ai-factories/); [DCD](https://www.datacenterdynamics.com/en/news/aws-launches-ai-factory-offering-that-gives-customers-dedicated-ai-infrastructure-on-premises/). TechRadar framed it as a test or pilot (conflict) — [TechRadar](https://www.techradar.com/pro/amazon-is-testing-out-private-on-premises-ai-factories).
- **Google Distributed Cloud:** Gemini GA on air-gapped GDC since Aug 2025, authorized for US Secret/Top Secret, and Google cannot remotely shut it down — [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/run-gemini-and-ai-on-prem-with-google-distributed-cloud). Cirrascale delivers Gemini on a single Dell 8-GPU appliance — [VentureBeat](https://venturebeat.com/technology/googles-gemini-can-now-run-on-a-single-air-gapped-server-and-vanish-when-you-pull-the-plug).
- **Azure Local:** Microsoft-managed hardware in customer facilities, cited as an AWS competitor — [DCD](https://www.datacenterdynamics.com/en/news/aws-launches-ai-factory-offering-that-gives-customers-dedicated-ai-infrastructure-on-premises/).
- **WWT:** systems integrator for Polarise's sovereign AI data center in Oslo. Also runs InfiniteAI (£200m UK/EU compute) and a multi-OEM AI Proving Ground. Won NVIDIA 2026 NPN AI Excellence and Federal partner awards — [WWT](https://www.wwt.com/press-release/polarise-partners-with-world-wide-technology-to-accelerate-europes-sovereign-ai-buildout-starting-in-oslo); [WWT awards](https://wwt.com/press-release/world-wide-technology-awarded-nvidias-2026-npn-ai-excellence-partner-of-the-year-npn-ai-enterprise-software-partner-of-the-year-and-npn-federal-partner-of-the-year).
- **Mark III Systems:** Houston-based NVIDIA systems integration partner — [CB Insights](https://www.cbinsights.com/company/mark-iii-systems). I found no 2026 sovereign-project details.
- **Palantir + Armada** sovereign AI infrastructure partnership — [HPCwire](https://www.hpcwire.com/bigdatawire/this-just-in/palantir-and-armada-partner-to-accelerate-sovereign-ai-infrastructure/).

### Inferences
- Hyperscaler on-prem offerings blur the line between "cloud API" and "local AI." The hardware is customer-sited but often vendor-managed.

### Gaps
- Oracle's 2026 AI-specific Cloud@Customer details were not verified.
- Large resellers (SHI, CDW, Insight, Presidio, Computacenter, AHEAD, Trace3) were not added because I found no sovereign-AI-specific evidence for them.
- Sovereign operators (G42/Core42, Nscale, Fluidstack, Sakura Internet) are cloud-style and excluded. Only HUMAIN and Polarise are listed, as "international."

## Out-of-segment companies added (best-fit segment)
HUMAIN (international), Polarise (international), Armada (industrial-edge), ConfidentialMind (private-ai-platforms), Nutanix (private-ai-platforms), Smallest.ai (efficient-models), Axelera AI (edge-silicon). Seen but not added: Samsung SDS (NPU-as-a-Service on FuriosaAI RNGD — cloud), Parasail (d-Matrix cloud user), Gcore, Red Hat, Lambda.
