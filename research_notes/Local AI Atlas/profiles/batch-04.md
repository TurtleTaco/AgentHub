# Batch 04 profiling notes

40 candidates: **33 in, 5 borderline, 2 out**. Basis: 4 searched, 9 mixed, 25 knowledge (plus 2 out rows).

**Method limit:** the shared web-search budget (200 searches per turn, across all agents) ran out after about 25 searches in this batch. WebFetch was blocked by the network allowlist for every domain tried (eejournal.com, siliconcatalyst.com, analog.com, weka.io, alphaics.ai). Searches went to recent funding and M&A first. Profiles marked `knowledge` carry low confidence on funding, headcount and (often) founding year. They should be re-checked when search capacity is available. Priority re-checks: ArchiTek, Anaflash, Corerain, AlphaICs, Blumind, BOS Semiconductors, D-Robotics, Cix, Chipintelli, Codasip.

## Verdict changes vs discovery
- **Wiwynn: out.** It is a cloud ODM. Its AI racks go to public-cloud hyperscalers, and Wiwynn does not name customers. I found no enterprise or sovereign line, so the hardware is not under the end customer's control.
- **Deep Vision: out (duplicate).** Deep Vision rebranded as **Kinara** in 2022, and Kinara is profiled in batch-05. NXP's agreement to buy Kinara (announced Feb 2025, ~$307M) comes from knowledge; I could not confirm by search that the deal closed.
- **Borderline:** World Wide Technology and XENON Systems are integrators reselling generic NVIDIA hardware or services. Bestechnic and Bouffalo Lab make general SoCs where the NPU is a feature. Codasip sells general RISC-V IP, with AI only through custom instructions.
- **Edge-silicon judgement calls:** Allwinner, Amlogic, Chips&Media, Canaan and Analog Devices are rated **in** because each markets a dedicated AI product line: V-series AI vision SoCs, C3/A311D, WAVE-N NPU IP, Kendryte, and MAX78000 respectively.

## Corrections to discovery data
- **Alif Semiconductor is acquired, not active.** Analog Devices announced the deal on Sep 9, 2026 and completed it on Nov 3, 2026, paying $1.35B in cash plus up to $200M contingent (ADI press release, 8-K). Alif is headquartered in Pleasanton, CA. One aggregator (Multiples) gives $1.4B and Sep 2026; the ADI figures above take precedence.
- **Analog Devices:** the claim that ADI acquired Flex Logix is **confirmed**. ADI took over Flex Logix's technology assets and team in Nov 2024 (terms undisclosed). ADI now also owns Alif.
- **Ainekko:** the Esperanto IP acquisition is **confirmed**. Esperanto shut down in Jul 2025, and Ainekko announced the IP deal in Oct/Nov 2025. Discovery missed two things: the **merger with Veevx** (Mesa, AZ; MRAM IP) in Jan 2026 (CB Insights/EE Times, thinly sourced), and CORE-ET becoming an OpenHW Foundation project in Jun 2026. The website is unknown (null in discovery too). Funding of about $16.8M comes only from ZoomInfo (low confidence).
- **Ambarella:** NXP acquisition talks were reported by the FT on Jul 31, 2026. **No agreement had been announced** as of the search, so I recorded the company as active.
- **Ambiq:** listed on NYSE (AMBQ) on Jul 30, 2025, with an IPO raising $110.4M gross. Recorded as public.
- **VSORA:** an Ardian Semiconductor-led Series B extension followed in Jul 2026, with Otium, XAnge and Omnes. One outlet reports about €32M (~$32M per Dealroom), but terms were not officially disclosed. The total of ~$78M is an estimate (low-medium confidence). The company says a larger round is planned for 2027.
- **Axelera AI:** raised more than $250M (EUR211M) in Feb 2026, led by Innovation Industries with BlackRock and SiteGround Capital. Total funding exceeds $450M, but that figure includes grants and venture debt.
- **WEKA:** no new round in 2025 or 2026. The last is the Series E (May 2024, $140M, $1.6B post-money). Totals conflict across aggregators ($412M+ vs $515.9M); I used $412M at low confidence.
- **AlphaICs:** the latest funding found is a Series B ($8M, Jan 2021; ~$10.5M total). I found no news since about 2022, so activity is unverified.

## Unconfirmed claims
- **Atlazo:** acquired by Nordic Semiconductor (2023). This is plausible from knowledge but **unconfirmed by search**, and is recorded that way in status_detail. Nordic is profiled in batch-06.
- **Axera:** the Hong Kong IPO in Feb 2026 comes from discovery sources (Qiming VC, eWeek) and was not re-verified. The ticker is unknown.
- **Codasip:** reported in 2025 to be exploring a sale. The outcome is unconfirmed.
- **ArchiTek** (Osaka; AiOnIc chip, aIPE virtual-engine architecture): the profile is from model knowledge only. Its website and existence were not verified.
- **Anaflash, Corerain:** current activity is unverified.
- **Ambient Scientific:** funding sources conflict (TechInsights says a ~$17M Series A; Startup-Seeker says ~$10M total).
- **Canaan:** HQ recorded as Beijing. Its principal executive office may have moved to Singapore; not verified.

## Duplicates and related entities in other batches
- Deep Vision is the same company as **Kinara** (batch-05).
- These are related entities, not duplicates:
  - Flex Logix and Esperanto Technologies (batch-05): their assets are now with ADI and Ainekko respectively.
  - Nordic Semiconductor (batch-06): the acquirer of Atlazo's assets.
  - Horizon Robotics (batch-05): D-Robotics was spun out of it.
  - NXP (batch-02): the acquirer of Kinara and the reported suitor for Ambarella.
