# Private / On-Prem / Sovereign AI Platforms (segment: private-ai-platforms)

Discovery pass, 2026-11-25. The JSON file next to this one lists 134 companies: 102 tagged `private-ai-platforms` and 32 tagged with other segments. Method: about 20 web searches, with web fetch blocked for most domains (see Gaps). Some entries have no search hit in this pass. For those I relied on well-established vendor knowledge and cited the vendor's homepage. Those entries are flagged "(verify)" in the JSON where the on-prem claim is less certain.

## Which "AI operating system" / data+AI platforms deploy self-hosted on any Kubernetes like Shakudo?

### Takeaway
The closest peers to Shakudo are TrueFoundry, Kamiwaza, Rafay, Spectro Cloud (Palette AI), Mirantis k0rdent AI, Domino, Dataiku, Red Hat OpenShift AI, SUSE AI and Canonical. Palantir now sells an on-prem "AI operating system" with Dell. The infrastructure vendors (HPE Private Cloud AI, Nutanix Enterprise AI, VMware Private AI Foundation) package the same idea as turnkey stacks.

### Cited Findings
- CB Insights lists Dataiku, Domino and Weights & Biases as Shakudo's top competitors, plus Datagran and Ascend.io as comparison targets. It also shows Iguazio and cnvrg.io in the same competitive set. — [CB Insights](https://www.cbinsights.com/company/shakudo/alternatives-competitors); [CB Insights Iguazio vs Shakudo](https://www.cbinsights.com/compare/iguazio-vs-shakudo); [CB Insights cnvrg](https://www.cbinsights.com/company/cnvrgio/alternatives-competitors)
- Shakudo's own pages position it against Glean, Palantir AIP, Harness AI, Cohere North and Snowflake Cortex. — [Shakudo](https://www.shakudo.io/lp/self-hosted-ai)
- Dell and Palantir introduced an on-prem AI operating system that brings Foundry and Ontology onto customer infrastructure. — [Dell blog](https://www.dell.com/en-us/blog/dell-and-palantir-introduce-an-on-premises-ai-operating-system)
- Dell's on-prem agentic AI Factory names five ISV partners for its software layer: DataRobot, ClearML, Aible, Cohere North and Dataloop. — [Dell InfoHub](https://www.dell.com/en-us/infohub/articles/designing-an-enterprise-ai-factory-architecture-for-agentic-applications); [Dell blog](https://www.dell.com/en-us/blog/build-your-digital-workforce-with-an-agentic-ai-platform-designed-for-the-enterprise)
- NVIDIA's Enterprise AI Factory is a validated on-prem design built with Cisco, Dell, HPE and Lenovo. NVIDIA OpenShell, an agent runtime, is supported across the Dell AI Factory. — [NVIDIA Marketplace](https://marketplace.nvidia.com/en-us/enterprise/ai-factory/); [NVIDIA blog](https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/)
- Kamiwaza raised $11M (pre-seed plus seed) for AI orchestration that runs models where data lives: on-prem, cloud and edge. — [Kamiwaza release](https://giraffe-rose-f9lp.squarespace.com/news-and-insights/kamiwaza-announces-11m-in-back-to-back-funding-rounds-to-power-enterprise-ai-orchestration-at-scale); [GeekWire](https://www.geekwire.com/2025/seattle-vcs-invest-in-kamiwaza-a-new-enterprise-software-startup-helping-companies-adopt-ai/)
- TrueFoundry publishes a market map titled "mapping the on-prem AI market from chips to control planes". I could not fetch it because the domain is blocked. — [TrueFoundry](https://www.truefoundry.com/de/blog/mapping-the-on-prem-ai-market-from-chips-to-control-planes)
- Tensor9 raised a $4M seed to let software vendors install their products in a client's cloud, on-prem or bare-metal environment. — [AOL/Benzinga](https://www.aol.com/amazon-meta-veterans-raise-4m-190115462.html)

### Inferences
- "Self-hosted on any Kubernetes" now splits into three groups. The first is Kubernetes-native platform startups: Shakudo, TrueFoundry, Kamiwaza, Rafay, Spectro Cloud. The second is enterprise Linux and Kubernetes vendors adding AI stacks: Red Hat, SUSE, Canonical, Mirantis, Broadcom/VMware. The third is hardware OEMs bundling ISV software: Dell, HPE, Nutanix. Dell's ISV list is a useful seed for finding more on-prem software vendors.

### Gaps
- I did not verify that each MLOps vendor (Dataiku, Domino, W&B) supports fully air-gapped installs. That needs their deployment docs.
- I could not read the TrueFoundry market map (fetch blocked).

## Which vendors sell private ChatGPT / private RAG / knowledge assistants that run on-prem or air-gapped?

### Takeaway
This is the largest cluster. Leading names include Zylon/PrivateGPT, Prem AI, LLMWare, Katonic, Iterate.ai, Allganize, Pryon, Squirro and Unique. Other active players found: Cohere North, Mistral, Aleph Alpha PhariaAI, LightOn Paradigm, VDF AI, Arc53/DocsGPT, Iternal AirgapAI, AlpineAI, Onyx, Mindbreeze, Sinequa, IntraFind, Vectara, Nextcloud Assistant and Mattermost, plus German mid-market vendors (CONET sovira.ai, DialogBits, Comma Soft Alan).

### Cited Findings
- Prem AI (Lugano, founded 2023) lets enterprises such as hedge funds and law firms run models entirely on their own servers. Bloomberg reported it was raising $100M at a valuation of at least $500M (June 2026). Sources disagree on whether the round has closed. — [TheNextWeb](https://thenextweb.com/news/prem-ai-swiss-100m-series-a-private-ai); [SiliconANGLE](https://siliconangle.com/2026/06/18/prem-seeks-100m-series-export-bans-boost-sovereign-ai-demand/)
- Zylon's PrivateGPT is an open-source RAG pipeline that runs fully on-prem, with documented air-gapped model downloads. — [Starlog](https://starlog.is/articles/data-knowledge/zylon-ai-private-gpt)
- VDF AI (Sweden) sells an on-prem agent platform with permission-aware RAG. It claims fully air-gapped installs using open-weight models. — [VDF AI](https://vdf.ai/resources/on-premise-ai-agent-platform/)
- DocsGPT (Arc53) is MIT-licensed. Its on-prem and air-gapped tiers start at $10,000 per deployment. — [DocsGPT](https://www.docsgpt.cloud/)
- Iternal's AirgapAI is a fully local assistant. It claims use in classified workflows (self-reported). — [Iternal](https://iternal.ai/airgapai)
- Allganize offers on-prem and air-gapped LLM platforms for security-sensitive enterprises and public bodies. It is part of the Upstage consortium in Korea's sovereign foundation-model project. — [Asiae](https://www.asiae.co.kr/en/article/2025080608461946255); [Allganize](https://www.allganize.ai/)
- Onyx supports fully air-gapped self-hosting with local LLMs. H2O.ai sells on-prem and air-gapped GenAI to banks, telcos and government. — [Onyx](https://onyx.app/insights/enterprise-rag-platforms-2026)
- AlpineAI (Davos) raised a double-digit-million seed in April 2026. It runs open-source LLMs only in certified Swiss datacenters. — [Startupticker](https://www.startupticker.ch/en/news/alpineai-raises-double-digit-million-seed-round-for-sovereign-ai)
- Cohere models run in private cloud or air-gapped environments. Cohere raised about $500M at a $6.8B valuation in Aug 2025, and an extension brought it to about $7B. North is deployed on SAP's Sovereign Cloud. — [IntuitionLabs](https://intuitionlabs.ai/articles/cohere-enterprise-ai-llm-profile); [BetaKit](https://betakit.com/canadas-ai-champion-cohere-is-standing-up-the-load-bearing-walls-of-our-economy/)
- German vendors with on-prem options: CONET sovira.ai, which runs in customer datacenters, public cloud or the BSI-certified CONET cloud; DialogBits, which is the basis of the Sparkassen S-KIPilot; and Comma Soft's Alan, which runs on-prem with German open-weight models. — [ESUT](https://esut.de/2025/11/meldungen/65186/souveraene-ki-assistenzsysteme-mit-sovira-ai/); [WZ-IT comparison](https://wz-it.com/blog/ki-plattformen-vergleich/)
- Mattermost markets agentic AI for air-gapped environments. GitLab offers Duo Self-Hosted for air-gapped government installs. — [Mattermost](https://mattermost.com/blog/can-agentic-ai-work-in-air-gapped-environments/); [GitLab](https://about.gitlab.com/the-source/ai/transforming-government-it-ai-for-air-gapped-environments/)

### Inferences
- Switzerland stands out as a hub for private AI: Prem, Squirro, Unique and AlpineAI, with KNIME also Swiss. The bank and wealth-management demand there likely explains it.
- Many "private ChatGPT" products are thin layers over open-source runtimes like Ollama and vLLM. What sets them apart is connectors, permissions and air-gap support, not the models.

### Gaps
- Cognizer, which the user named, came up in no search, so its website and HQ are null. Lamatic's on-prem/VPC option is also unverified.
- I could not check whether Aleph Alpha changed ownership in 2025–26, because the search budget ran out. Its status is marked active, but please verify.
- Funding figures for Zylon, Katonic, Iterate.ai, Pryon, Squirro and Unique were not checked in this pass.

## Which data science / ML / MLOps platforms offer on-prem GenAI?

### Takeaway
H2O.ai, Dataiku, Domino, Cloudera, ClearML, Anaconda, DataRobot, Seldon, Valohai, Comet, Outerbounds, Union.ai, SAS Viya, KNIME, Teradata and C3 AI all offer self-managed or on-prem GenAI. Many early independents now belong to larger companies: Iguazio (McKinsey 2023), cnvrg.io (Intel 2020), Weights & Biases (CoreWeave 2025), Run:ai (NVIDIA 2024).

### Cited Findings
- Cloudera for Digital Sovereignty (Nov 2026) integrates Mistral models into its hybrid platform. It supports sovereign clouds, private datacenters and air-gapped environments. — [Channel Insider](https://www.channelinsider.com/ai/cloudera-digital-sovereignty-private-ai/)
- DataRobot's Agent Workforce Platform runs agents on the Dell AI Factory with NVIDIA. ClearML, Aible and Dataloop are also Dell ISV partners. — [Dell InfoHub](https://www.dell.com/en-us/infohub/articles/designing-an-enterprise-ai-factory-architecture-for-agentic-applications)
- Lamini says it runs on-prem (including air-gapped) or in a VPC. It raised a $25M round, date not confirmed. — [Lamini](https://www.lamini.ai/blog/series-a)

### Inferences
- Within MLOps, "on-prem GenAI" now mostly means a Kubernetes-deployable platform plus model serving with vLLM or NVIDIA NIM. Being an NVIDIA or Dell ISV partner is the main route to market.

### Gaps
- No search confirmed the 2026 acquisition statuses of Anaconda, Domino, Seldon or Valohai. All are marked active from prior knowledge.

## Which agent/LLM-app builders are self-hostable with a company behind them?

### Takeaway
The main self-hostable builders with a company behind them are Dify (LangGenius), Onyx, Langflow (now IBM, via DataStax), Flowise (Workday 2025), n8n, Activepieces, AnythingLLM (Mintplex), Open WebUI, LibreChat, LobeHub, deepset/Haystack, LangChain, LlamaIndex and CrewAI. Commercial conversational and agent platforms with on-prem options include Kore.ai, Rasa, Cognigy (NICE 2025), Stack AI, Airia, xpander.ai and Archestra.AI. Tabnine and TabbyML are self-hosted coding assistants.

### Cited Findings
- 2026 funding for enterprise-agent startups: Archestra.AI raised $10M (seed, 20VC), xpander raised $7.5M, and Airrived raised a $6.1M seed. Airia announced $100M in Sept 2025. — [tech.eu](https://tech.eu/2026/06/02/archestraai-raises-10m-to-unlock-next-gen-agentic-use-case/); [HPCwire](https://www.hpcwire.com/aiwire/2026/08/17/xpander-raises-7-5m-to-expand-enterprise-ai-agent-platform/); [SiliconANGLE](https://siliconangle.com/2026/02/03/airrived-says-agentic-ais-breakthrough-moment-arrived-raising-6-1m-seed-funding); [BusinessWire](https://www.businesswire.com/news/home/20250916641185/en/Airia%E2%88%92Secures%E2%88%92100M-in-Funding-to-Accelerate-Safe-and-Secure-Enterprise-Al-Adoption)
- Yellow.ai's YellowG LLM is listed as supporting on-prem deployment (a listicle source, weak). — [IndianAIapps](https://www.indianaiapps.com/blog/made-in-india-ai-tools-2026)

### Inferences
- The open-source builders turn into businesses through enterprise self-hosted licenses, adding SSO, RBAC and audit features. Acquirers so far are application and data companies (Workday, IBM, NICE, possibly ClickHouse), not AI labs.

### Gaps
- No search confirmed the acquisition statuses I hold from prior knowledge: Flowise by Workday (2025), Langflow via DataStax to IBM (2025), Cognigy by NICE (2025). LibreChat's acquisition by ClickHouse (2025) is especially uncertain and is marked "verify".
- The self-hosted options of Airia, xpander.ai and Archestra.AI are not confirmed by the excerpts I saw. They are marked "(verify)".

## Which 2025–2026 startups launched "sovereign AI" or "private AI" platforms?

### Takeaway
Sovereign and private AI launches came quickly in 2026. New platforms include Airrived (Sept 2026), Fobi AI FORTRESS (Aug 2026), hSenid Mobile Sovereign AI, Prem AI's $100M raise, AlpineAI's seed, Deliverance AI (out of stealth with £6m ARR), Xference.ai (Italy), amber (Aachen), Octostar (Ireland), Soket AI (India) and the KT/Rebellions appliance (Korea). Incumbents such as Cloudera also launched sovereign offerings.

### Cited Findings
- Airrived's Sovereign AI Platform (1 Sept 2026) lets customers build and run agentic AI on-prem, on private GPUs or fully air-gapped. — [ITNerd](https://itnerd.blog/2026/09/01/airrived-launches-sovereign-ai-platform-putting-enterprises-back-in-control-of-their-ai/); [IT Brief Asia](https://itbrief.asia/story/airrived-launches-sovereign-ai-platform-for-governments)
- Fobi AI FORTRESS (17 Aug 2026) supports on-prem, in-country and private-cloud deployments. — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/8/17/3346033/0/en/fobi-ai-launches-fortress-a-sovereign-ai-platform-for-secure-enterprise-owned-intelligence.html)
- hSenid Mobile's Sovereign AI targets banks, telcos and government, with on-prem, private-cloud or hybrid deployment. — [hSenid](https://hsenidmobile.com/sovereign-ai-platform-now-live/)
- Deliverance AI exited stealth with £6m ARR, running agentic AI inside companies' own environments. — [TheNextWeb](https://thenextweb.com/news/deliverance-ai-stealth-sovereign-enterprise-ai)
- amber raised €7m to sell AI sovereignty to the German Mittelstand. Velatir raised €5m (not added, because its local angle was unclear). TensorX raised €8m for sovereign inference (excluded as GPU infrastructure). — [TheNextWeb amber](https://thenextweb.com/news/amber-series-a-7m-ventech-nrw-bank-ai-data-layer); [TheNextWeb Velatir](https://thenextweb.com/news/velatir-5m-seed-european-ai-control); [ThinkBusiness](https://www.thinkbusiness.ie/articles/tensorx-raises-8m-sovereign-ai-infrastructure-europe/)
- Soket AI raised about $4M from Bajaj Finance and Pennant for on-prem LLMs for lenders. — [Indian Startup News](https://indianstartupnews.com/funding/indiaai-mission-startup-soket-ai-gets-4-million-from-bajaj-finance-and-pennant-for-on-premise-llms-12823737)
- KT shipped an on-prem enterprise server combining Rebellions chips and its Mi:dm LLM (Aug 2026). — [Korea Times](https://koreatimes.co.kr/business/companies/20260819/kt-puts-korean-ai-chips-language-model-into-one-enterprise-server)
- Upstage and Cohere are building AI for national data control (Nov 2026). — [Korea Times](https://www.koreatimes.co.kr/business/companies/20261117/upstage-cohere-build-ai-tailored-for-national-data-control)
- BigBear.ai bought Ask Sage for about $250M; the deal closed in January. It is replacing the Ask Sage brand with a GenAI platform that runs up to TS/SCI, locally or air-gapped. — [ExecutiveBiz](https://www.executivebiz.com/articles/bigbear-ai-dow-genai-platform-expansion); [HPCwire](https://www.hpcwire.com/aiwire/2026/07/15/bigbear-ai-expands-generative-ai-platform-for-secure-mission-environments/)
- HUMAIN made a strategic investment in Mozn to pair its sovereign infrastructure with Mozn's enterprise AI. — [Wamda](https://www.wamda.com/2026/08/saudi-ai-firm-mozn-secures-strategic-investment-humain)
- Germany's digital ministry is putting €250M into a sovereign federal AI platform, with SVA and StackIT involved. — [ChannelPartner](https://www.channelpartner.de/article/4176536/sva-ist-beim-ki-projekt-des-bundes-dabei.html)
- T-Systems Switzerland launched a sovereign AI platform (Nov 2026). Not added, because it is closer to a sovereign cloud. — [Netzwoche](https://www.netzwoche.ch/news/2026-11-12/t-systems-schweiz-lanciert-plattform-fuer-souveraene-ki)

### Inferences
- In 2026, "sovereign AI" is being used both by real on-prem software vendors and by cloud or telco players for in-country hosting. Only the first group fits this segment. Several 2026 launches (Airrived, Fobi) are rebrands of existing AI or security products.

### Gaps
- Airrived's HQ is unclear (reported as Dubai-linked; entered as UAE). AlpineAI, Octostar, Deliverance AI, Xference.ai, amber and elbic have null websites because I could not verify their domains.
- I found no Tracxn or CB Insights list specifically for "private LLM" or "on-premise generative AI" (those domains were not reachable).

## Sources consulted, market maps, and out-of-segment finds

### Takeaway
Searches covered press and funding news (SiliconANGLE, TheNextWeb, Sifted, tech.eu, EU-Startups, BetaKit, GlobeNewswire, HPCwire), Dell and NVIDIA partner pages, CB Insights competitor pages, and German, Korean, Indian and Middle Eastern trade press. Web fetch failed for most domains (wetheflywheel.com, getmaxim.ai, dev.to, truefoundry.com), and the shared search budget ran out after about 20 queries.

### Cited Findings
- Market maps and lists found but not readable in this pass: TrueFoundry's on-prem AI market map, the WeTheFlywheel guide to self-hosted LLM platforms, Maxim's "7 Best Private AI Platforms", and dev.to's "Air-Gapped AI Solutions: 7 Platforms 2026". — [TrueFoundry](https://www.truefoundry.com/de/blog/mapping-the-on-prem-ai-market-from-chips-to-control-planes); [WeTheFlywheel](https://wetheflywheel.com/en/guides/self-hosted-llm-platforms/); [Maxim](https://www.getmaxim.ai/articles/private-ai-platforms/); [dev.to](https://dev.to/jaipalsingh/air-gapped-ai-solutions-7-platforms-for-disconnected-enterprise-deployment-2026-2d1p)
- Defense and air-gapped finds: EdgeRunner AI (on-device military AI; Carahsoft and Intel partner) and Ask Sage Edge (HPE Edge Line 8000 with one H100). — [Carahsoft](https://www.carahsoft.com/edgerunner); [HSToday](https://www.hstoday.us/subject-matter-areas/cybersecurity/ask-sage-unveils-edge-ai-solution-to-transform-military-operations/)

### Inferences
- Local-AI companies found that belong to other segments (added to the JSON with their segment key): EdgeRunner AI, BigBear.ai, Ask Sage, Yurts, Defense Unicorns, Scale Donovan, Primer and Octostar (vertical-regulated); Clarifai, Lamini, Run:ai and Hugging Face (selfhosted-inference-llmops); AI21, Arcee, Poolside and elbic (efficient-models); Saltlux, KT, Upstage, Sarvam, Soket, CoRover, HUMAIN, Mozn, Fujitsu Takane, 4Paradigm and Zhipu (international); VAST Data (onprem-hardware); IBM watsonx, NVIDIA AI Enterprise and Google Distributed Cloud (bigtech).
- Seen but not added (other segments or excluded): TensorX, Denvr CAIP, Nscale, eStruxture, IONOS and STACKIT (sovereign GPU cloud or hosting); Velatir (governance, local angle unclear); EY.ai enterprise private (services); Atos (services); T-Systems Switzerland (sovereign cloud).

### Gaps
- Candidates not yet checked, worth adding in a follow-up pass: Langdock, nuwacom, Linagora/LUCIE, Faculty Frontier, Posit, Unstructured, Instabase, Hyperscience, Ori, Platform9, Lucidworks, OpenText Aviator, Naver HyperCLOVA X on-prem, NEC cotomi, ELYZA, iFlytek Spark appliances, AI71 (UAE), Core42, Legion Intelligence, Accrete, Rhombus Power, Nexos.ai, LiteLLM and Portkey (gateways), BentoML, Nomic and Jan.
- Nothing from G2 category pages, NVIDIA Inception or the HPE/Nutanix ISV directories was reachable.
