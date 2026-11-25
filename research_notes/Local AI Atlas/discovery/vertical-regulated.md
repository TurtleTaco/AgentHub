# Vertical / Regulated Local AI (segment: vertical-regulated)

Companion to `vertical-regulated.json`: 110 companies in total. 84 are tagged `vertical-regulated` and 26 are local-AI companies from other segments that came up along the way.

**How this was done, and its limits.** The research ran on 2026-11-25. About 20 web searches returned results before the shared search budget ran out. WebFetch could not reach fortune.com, startupfortune.com or resiliencemedia.co, which are blocked by this session's network rules. That leaves two kinds of entries:
- **Search-verified entries.** These list a news or vendor URL beyond the homepage in `sources`. Examples: BigBear.ai/Ask Sage, EdgeRunner, Noah Labs, Reflection, Poolside, Ferrum, OneAdvanced, LAW.co, Alexi, SBS, INDEV, Aveni, Tabnine, Coder, GitLab, Sourcegraph/Tabby/Continue, Speechmatics, Deepgram, AssemblyAI, Voxist, OPAQUE, Confident Security, Fortanix, Prem AI, TrueFoundry, ClearML, H2O.ai, Katonic, ibl.ai and Iternal.
- **Prior-knowledge entries.** These cite only the company homepage. They come from the model's training knowledge (cutoff mid-2026) and were **not re-verified in this session**. A "(verify)" note in an angle marks lower confidence. Before profiling, the 2026 status and deployment claims of these entries should be checked.

## Defense / national security: edge and air-gapped AI

### Takeaway
Defense is the densest and best-funded vertical. In 2026 the market split into two groups. Frontier labs were cleared for classified IL6/IL7 networks. Specialist vendors sell on-device or air-gapped appliances: BigBear.ai/Ask Sage, EdgeRunner, Seekr, Defense Unicorns, Legion, Yurts and Primer.

### Cited Findings
- On May 1, 2026 the Department of War (DoW) signed agreements letting eight firms run models on classified IL6/IL7 networks: SpaceX, OpenAI, Google, NVIDIA, Microsoft, AWS, Oracle and Reflection. Reflection is the one startup, and it is NVIDIA-backed. — [WinBuzzer](https://winbuzzer.com/2026/05/03/pentagon-classified-ai-agreements-nvidia-microsoft-aws-google-openai-spacex-oracle-reflection-xcxwbn/); [Federal News Network](https://federalnewsnetwork.com/defense-news/2026/05/dod-strikes-deals-with-major-tech-firms-to-deploy-ai-on-classified-networks/)
- BigBear.ai expanded its generative AI platform in July 2026. It added a local device for air-gapped deployments up to TS/SCI that uses locally hosted models when disconnected. It is also retiring the Ask Sage brand for DoW customers. — [HPCwire](https://www.hpcwire.com/aiwire/2026/07/15/bigbear-ai-expands-generative-ai-platform-for-secure-mission-environments/); [ExecutiveBiz](https://www.executivebiz.com/articles/bigbear-ai-dow-genai-platform-expansion)
- EdgeRunner AI (Seattle) builds air-gapped, on-device agents tuned for military roles. It raised a $5.5M seed in 2024 led by Four Rivers, then a $12M Series A in 2025 led by Madrona, with HP Tech Ventures and Alumni Ventures joining. Total raised: $17.5M. — [GeekWire](https://www.geekwire.com/2025/seattle-startup-edgerunner-ai-raises-12m-to-help-military-use-ai-without-the-internet/); [BusinessWire](https://www.businesswire.com/news/home/20250501050946/en/EdgeRunner-Raises-$17.5M-to-Develop-Air-Gapped-On-Device-AI-for-the-Warfighter)
- Coverage of the classified-AI "secure backbone" names these vendors:
  - Poolside: on-prem and air-gapped models.
  - ClearML: classified and air-gapped networks.
  - Seekr: an all-in-one system for air-gapped and contested environments.
  - Noah Labs.
  - CoreWeave with Leidos: SCIF-accredited data centres.

  An Ask Sage founder quote puts the market at about $2B. That figure has a single source. — [StartupFortune](https://startupfortune.com/startups-building-ais-secure-backbone-for-us-intelligence/); [Poolside](https://poolside.ai/government); [ClearML](https://clear.ml/industry/defense); [TheNextWeb](https://thenextweb.com/news/coreweave-leidos-classified-ai-cloud-intelligence-defence)
- Noah Labs is a Stanford spin-out. Its Sentinel AI IDE handles legacy C/C++, Ada, Fortran and COBOL code. It is fully air-gapped, with no telemetry and no cloud calls. — [IT Brief](https://itbrief.com.au/story/noah-labs-ai-touts-governed-software-agents-for-defence)
- Fortune (Apr 2026) covered infrastructure startups that wrap LLMs for classified use and quoted Unstructured's CEO. The article itself was unreachable, so this comes from the search summary only. — [Fortune](https://fortune.com/2026/04/11/ai-startups-defense-department-pentagon-secrets-intelligence/)

### Inferences
- The main 2025–2026 change is **consolidation**: BigBear.ai absorbed Ask Sage. Frontier labs also moved directly onto classified networks. This puts pressure on small "secure wrapper" startups unless they own edge or on-device deployment, as EdgeRunner, Noah Labs and Rune do.
- These are listed from prior knowledge and were not re-verified: Shield AI (Hivemind on-board), Anduril (Lattice edge), Helsing, Palantir AIP, Scale Donovan/Defense Llama, Yurts, Legion, Primer, Defense Unicorns, Striveworks, Rune, Adarga, Safran.AI (Preligens), Auterion, Lilt, AppTek and Systran.

### Gaps
- Not verified this session: Legion's and Yurts' funding, Defense Unicorns' latest round, Seekr's appliance name, Rebellion Defense's 2026 status (marked unknown) and Vannevar's deployment model.
- Arondite's and Noah Labs' websites are unconfirmed (set to null).
- Other defense edge startups were not researched, for example Scout AI, ARX Robotics, Alta Ares, Harmattan AI and Comand AI. Comand AI was dropped for lack of a local-deployment source.

## Healthcare: on-prem and on-device clinical AI

### Takeaway
Healthcare local AI is mostly **on-prem orchestration and federated or confidential computing**. Examples: Ferrum, deepc, CARPL, Owkin, Rhino and BeeKeeperAI. Vendors that host private LLMs inside the hospital are few. John Snow Labs is the clearest. Ambient-scribe leaders such as Abridge, Nabla and Suki are cloud SaaS and were excluded.

### Cited Findings
- Ferrum Health sells an on-prem and single-tenant private-cloud AI platform with a catalog of validated clinical AI. Its claims:
  - PHI never leaves the customer environment.
  - It has more than 250 sites, including Sutter Health and Carle.
  - It raised a $16M Series A (2024).
  - It formed a Google Cloud partnership (2025).

  The search found no Ferrum-hosted LLM. — [Healthcare IT Today](https://www.healthcareittoday.com/2024/11/01/ferrum-health-raises-16m-in-series-a-funding-to-unlock-ai-adoption-in-healthcare/); [MedTech Dive](https://www.medtechdive.com/press-release/20241127-ferrum-health-expands-ai-orchestrator-platform-with-managed-private-cloud-d/)
- OneAdvanced (UK) launched a private LLM for healthcare businesses in Apr 2025. It is vendor-hosted, so it is borderline for this study's scope. — [Digital Health](https://digitalhealth.net/2025/04/oneadvanced-launches-private-llm-for-healthcare-businesses)
- Hospitals are also building their own on-prem gen AI: URMC's Hyperion AI, and a 2026 JMIR AI study of an on-prem open-source platform at a university hospital. These are not companies, so they are not in the JSON. — [URMC](https://www.urmc.rochester.edu/cancer-institute/research/informatics/projects/hyperion-ai); [JMIR AI](https://ai.jmir.org/2026/1/e84362)

### Inferences
- Health systems are increasingly choosing **in-house open-weight stacks** over buying from a vendor. That weakens the startup category for private medical LLMs.

### Gaps
- Not verified: on-prem options at Corti, Aidoc, Lunit and Augnito; whether Rhino Health renamed itself "Rhino Federated Computing"; and the scope of Qure.ai's offline deployments.

## Legal / finance / insurance

### Takeaway
Finance has real **sovereign-AI platforms** from SBS with NVIDIA, Aveni FinLLM, INDEV, Squirro and Unique. Legal is thin. Market leaders Harvey and Legora are cloud SaaS. Local options come mainly from small vendors (LAW.co, Alexi) and from on-prem eDiscovery tools (Nuix).

### Cited Findings
- SBS launched a "banking's first sovereign AI platform" with NVIDIA, deployable on private cloud, managed cloud or fully on-prem. — [The Paypers](https://thepaypers.com/fintech/news/sbs-launches-sovereign-ai-platform-for-banks-with-nvidia)
- INDEV operates domain-specific LLMs inside European banks' regulatory perimeter. — [INDEV](https://indevsoftware.io/solutions/sovereignai/)
- Two UK banks co-released a custom sovereign LLM. Based on prior knowledge this is Aveni FinLLM with Lloyds and Nationwide; confirm the naming. — [The Stack](https://www.thestack.technology/two-uk-banks-team-up-to-release-custom-sovereign-llm/)
- LAW.co offers on-prem "LLM-in-a-Box" appliances or private and hybrid cloud for law firms. — [LAW.co](https://law.co/private-llms-for-law-firms)
- Alexi markets private-cloud deployments with complete model and data isolation. — [Alexi](https://www.alexi.com/private-cloud)
- Prem AI (Switzerland) was reported to be seeking a $100M Series A at a valuation of $500M or more, expected to close in Q3 2026; the close was unconfirmed. It launched TEE-based Confidential APIs in May 2026. — [RuntimeWire](https://www.runtimewire.com/article/swiss-ai-startup-prem-ai-100m-series-a)

### Gaps
- Not verified: on-prem options at Luminance, DeepJudge and Relativity; whether Noxtua is on-prem (excluded as likely sovereign SaaS); and whether Unique and Instabase support true on-prem.
- Insurance-specific local AI vendors were not found.

## Self-hosted / air-gapped coding assistants

### Takeaway
Tabnine is still the reference air-gapped product. Coder Agents became generally available in Sept 2026 and brought fully self-hosted agents. Other self-hostable options:
- GitLab Duo Self-Hosted, Sourcegraph (strict air-gap needs configuration), Qodo, JetBrains/Mellum, Poolside and Noah Labs.
- Open-source tools: Tabby, Continue and Refact.

GitHub Copilot and Amazon Q are cloud-only.

### Cited Findings
- Tabnine is the most explicitly documented air-gapped option, and it has been enterprise-only since early 2026. — [Tech Insider](https://tech-insider.org/au/tabnine-vs-copilot-vs-windsurf-2026/); [Context7](https://context7.com/guides/air-gapped-ai-coding)
- Coder Agents launched in beta in May 2026 and went GA on Sept 9, 2026. Both the agent and its execution run on customer infrastructure, including air-gapped. — [Coder](https://coder.com/blog/coder-agents-ga); [SD Times](https://sdtimes.com/ai-coding-agents/coder-agents-bring-self-hosted-ai-coding/)
- Sourcegraph Cody Enterprise can meet a strict air-gap only if Cody Gateway is disabled. Tabby runs fully offline after the model download. Continue and CodeGeeX can be self-hosted. — [Context7](https://context7.com/guides/self-hosted-ai-coding-assistant)
- GitLab markets AI for air-gapped government environments. — [GitLab](https://about.gitlab.com/the-source/ai/transforming-government-it-ai-for-air-gapped-environments/)

### Gaps
- Windsurf's current self-hosted support after its 2025 acquisition by Cognition was not verified.
- HQs for TabbyML and Refact.ai are unknown (null).

## On-prem / on-device speech and voice

### Takeaway
Speech has broad on-prem support:
- Self-hosted APIs: Speechmatics, Deepgram, AssemblyAI and Voxist.
- On-device: Picovoice, Sensory, Cerence, SoundHound and Vivoka.
- Security-focused on-prem: Phonexia, AppTek and Cobalt.

### Cited Findings
- Deepgram and Fortanix announced fully on-prem voice AI for regulated industries on June 1, 2026. Prem AI self-hosts Deepgram Nova-3. — [Deepgram](https://deepgram.com/learn/deepgram-fortanix-press-release); [Deepgram case study](https://deepgram.com/customers/prem-ai)
- AssemblyAI offers deployment on customer infrastructure, cloud or on-prem. — [AssemblyAI](https://www.assemblyai.com/features/self-hosted-voice-ai)
- Speechmatics publishes on-prem deployment guidance and an essay titled "return of on-prem". — [Speechmatics](https://www.speechmatics.com/company/articles-and-news/how-to-deploy-on-premises-speech-recognition-for-secure-enterprise-environments)
- Voxist Enterprise installs its ASR, MT and TTS models inside the customer environment. — [G2](https://www.g2.com/products/voxist-enterprise/reviews)
- NVIDIA Nemotron Speech is self-hosted on a single L40, A100 or H100. That belongs to the big-tech segment, so it is not in the JSON. — [NVIDIA](https://perspectives.nvidia.com/nemotron-speech/task/faq/enterprises-on-premise-speech-recognition-data-residency-regulated-industries/)

### Gaps
- Not checked: the deployment details of Phonexia, Cobalt, Voicegain, Spitch, Intelligent Voice and Veritone (prior knowledge only); and whether Rev, Gladia and Smallest.ai offer on-prem.

## Confidential / privacy-preserving AI

### Takeaway
Confidential AI is a funded niche. OPAQUE raised $24M at a $300M valuation, and Confident Security launched in 2025. Several deliver private inference as attested cloud enclaves rather than on customer hardware: Tinfoil, Confident Security and Privatemode. Fortanix, Anjuna and Edgeless Systems' Continuum and Contrast also run on-prem.

### Cited Findings
- OPAQUE raised a $24M Series B in Feb 2026, led by Walden Catalyst with Intel Capital, at a $300M valuation. Total raised: $55.5M. The funds are aimed at confidential training, post-quantum security and sovereign cloud. — [SiliconANGLE](https://siliconangle.com/2026/02/12/opaque-raises-24m-300m-valuation-confidential-ai-platform/)
- Confident Security came out of stealth in July 2025 with $4.2M from Decibel, South Park Commons and others. Its CONFSEC product implements Apple's Private Cloud Compute architecture for enterprises. — [TechCrunch](https://techcrunch.com/2025/07/17/confident-security-the-signal-for-ai-comes-out-of-stealth-with-4-2m)
- Arcium's Blackthorn MPC inference stack is in private alpha. It is crypto-native and not local, so it is excluded. — [Crypto Briefing](https://cryptobriefing.com/arcium-blackthorn-ai-inference-private-alpha/)

### Gaps
- Mithril Security's 2026 status is unknown.
- TripleBlind and Cape Privacy have uncertain status and were omitted.

## On-prem document / intelligent automation AI

### Takeaway
ABBYY, Hyperscience, Tungsten Automation (formerly Kofax) and Instabase keep on-prem deployment options for government and banking customers. These are listed from prior knowledge and not verified this session.

### Gaps
- Not checked: whether these vendors run gen AI or LLM features on-prem. Some may route gen AI features to cloud LLMs.

## Out-of-segment companies seen (included in the JSON with their own segment)
- **private-ai-platforms:** Reflection AI, Prem AI, Cohere, AI21, Zylon, H2O.ai, Katonic, Clarifai, ibl.ai, Kamiwaza, Mindbreeze.
- **selfhosted-inference-llmops:** TrueFoundry, ClearML.
- **international:** Mistral, Aleph Alpha (status unknown), LightOn, ChapsVision, Sinequa, Sarvam AI, Upstage, aiXcoder.
- **industrial-edge:** Utilidata, Avathon, Skydio.
- **on-device-sdks:** Vivoka.
- **consumer-local-apps:** Pieces.

These were noted but excluded:
- **Cloud-only or vendor-hosted privacy products:** Proton Lumo, Venice, Harvey, Legora, Abridge, Nabla, Suki and Hebbia.
- **Big-tech offerings belonging to another researcher:** Google Distributed Cloud air-gapped (IL6), IBM Sovereign Core, NVIDIA Nemotron Speech, and CoreWeave with Leidos classified cloud.
- **Services firms:** InTechHouse, Sphere and SCAND.
