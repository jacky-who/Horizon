---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 33 items, 18 important content pieces were selected

---

**Technology News**
1. [OpenAI Explains Why Perplexity Still Tracks Model Intelligence](#item-tech-news-1) ⭐️ 8.0/10
2. [Tesla begins overseas FSD v15 rollout with new Reality View](#item-tech-news-2) ⭐️ 8.0/10
3. [FT links Prince Group figure to NVIDIA chip smuggling into China](#item-tech-news-3) ⭐️ 8.0/10
4. [Anthropic 2028 power mix projected as 87% gas](#item-tech-news-4) ⭐️ 7.0/10
5. [Tim O&\#x27;Reilly Argues Silicon Valley Optimizes for Shareholder Value](#item-tech-news-5) ⭐️ 7.0/10
6. [Muru: AI-assisted Rust server for ASGI and WSGI Python apps](#item-tech-news-6) ⭐️ 7.0/10
7. [Phison 太空 SSD 将携 488 TB 入轨](#item-tech-news-7) ⭐️ 7.0/10
8. [Moore Threads Lushan GPU reportedly targets 64 GB VRAM](#item-tech-news-8) ⭐️ 7.0/10

**Global Chips**
1. [US seeks answers on Nvidia&\#x27;s sale of chips to China, Bessent says](#item-chip-news-1) ⭐️ 7.0/10
2. [Report: China spy agency prioritizes acquiring advanced chips](#item-chip-news-2) ⭐️ 7.0/10
3. [Bessent Seeks Answers on NVIDIA&\#x27;s Role in China AI Chip Shipments](#item-chip-news-3) ⭐️ 6.0/10
4. [Report alleges two-year Chinese spy campaign to obtain advanced AI chips](#item-chip-news-4) ⭐️ 6.0/10
5. [US intelligence chief hints China obtained restricted AI chips](#item-chip-news-5) ⭐️ 5.0/10
6. [Senator Kennedy Seeks Sworn Testimony From Lutnick on China&\#x27;s Nvidia Chip Access](#item-chip-news-6) ⭐️ 4.0/10

**Technology Blog**
1. [Deliberate Flailing as a Strategy Under Uncertainty](#item-tech-blog-1) ⭐️ 6.0/10
2. [Good Programming Is Mostly Avoiding Blunders](#item-tech-blog-2) ⭐️ 6.0/10

**Financial News**
1. [US tech selloff prompts emergency market measures in Asia](#item-finance-news-1) ⭐️ 9.0/10
2. [中国要求美国撤销电话号段接入限制](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI Explains Why Perplexity Still Tracks Model Intelligence](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI published an article examining how perplexity, a measure of next-token prediction loss, relates to language-model intelligence. The piece drew substantial technical discussion, including surprise that cross-entropy trends remain a clear signal of capability and reasoning progress even as reinforcement-learning-based training becomes more common. The article&\#x27;s full argument and any specific claims or measured results are not available in the supplied material, and the piece is OpenAI-authored rather than an independent evaluation.

hackernews · acossta · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**「Background」** Perplexity quantifies how surprised a model is when predicting the next token across a sequence: a perfect predictor scores 1, while a random predictor scores the vocabulary size. Cross-entropy loss, the training objective that produces perplexity, has long been used to compare language models, but the community discussion notes that increasingly convoluted benchmarks have proliferated alongside RL-based post-training.

**「Impact」** The discussion suggests a practical evaluation implication: if perplexity continues to track capability as models scale, developers may have a simpler, cheaper benchmark to consult alongside task-specific evaluations. Commenters caution that perplexity may not capture specialized abilities, since a model trained narrowly on math could show high general perplexity while still performing well on its target task.

**「Community Discussion」** Commenters debated why cross-entropy trends remain so predictive. One found it &quot;pretty shocking&quot; that cross-entropy still matters given the rise of RL and welcomed a simple benchmark, while another argued the correspondence is unsurprising because prediction and compression capture the extraction of world models from raw data. A skeptical commenter questioned claims that specific abilities &quot;emerge&quot; at particular perplexity thresholds, noting that narrowly trained smaller models can have high general perplexity.

**Tags**: `#perplexity`, `#language-models`, `#model-evaluation`, `#cross-entropy`, `#benchmarking`

---

<a id="item-tech-news-2"></a>
### [Tesla begins overseas FSD v15 rollout with new Reality View](https://x.com/Tesla/status/2124222447855743019) ⭐️ 8.0/10

Tesla has started rolling out FSD v15 to overseas customers, according to a company post relayed via Telegram. Tesla claims the update improves handling of safety-critical scenarios by 25x, though the post gives no baseline, methodology, or independent verification for that figure. The release adds a &quot;Tesla Reality View&quot; interface that overlays camera footage and the FSD driving plan on the in-car screen, with full-screen, map, and split-screen views plus a quiet mode. Navigation turn cues can be overlaid on the display, turn-signal chimes are softer and fade gradually, and Tesla says it refined driving over potholes and debris and speed control near schools and in bad weather.

telegram · zaihuapd · Nov 22, 00:03

**「Context: FSD&\#x27;s end-to-end stack and the unverified 25x figure」** Tesla&\#x27;s Full Self-Driving software has been delivered in numbered major releases, and v15 is framed by the company as an upgrade to every part of its end-to-end driving network. Coverage of the rollout notes that Tesla published the 25x multiplier for improved critical-intervention rate but not the baseline rate, so the safety claim cannot yet be independently checked. The release also explicitly targets long-standing weaknesses including sign reading, potholes and school-zone speeds.

**「Impact」** Because the 25x safety claim is a vendor statement without published benchmarks, owners and regulators cannot yet treat it as a measured improvement; the rollout&\#x27;s practical effect will depend on which overseas markets and vehicle configurations actually receive v15.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/tesla-fsd-v15-rollout-25x-critical-intervention-claim-what-is-verified-2026">Tesla FSD v15: 25x Claim Explained and Checked | explainx.ai Blog</a></li>
<li><a href="https://electrek.co/2026/11/21/tesla-fsd-v15-rollout-25x-safety-reality-view/">Tesla launches FSD v15, targets its biggest weaknesses, from ...</a></li>
<li><a href="https://www.digitaltrends.com/cars/tesla-fsd-v15-rollout/">FSD v15 is rolling out, and Tesla says it handles risky ...</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#Tesla FSD`, `#AI systems`, `#software release`, `#computer vision`

---

<a id="item-tech-news-3"></a>
### [FT links Prince Group figure to NVIDIA chip smuggling into China](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 8.0/10

The Financial Times, citing people familiar with the matter, reported that Hu Xiaowei — described by the U.S. Treasury Department as the &quot;number two&quot; figure at Cambodia&\#x27;s Prince Group — is suspected of involvement in moving NVIDIA chips into China. The report ties the conglomerate to a network of alleged shell companies and underground financing channels that used private aircraft to smuggle goods. Trade data cited by the FT put the declared value of imports by Megaspeed&\#x27;s Malaysian subsidiary at about $4.6 billion from December 2024 to December 2025, with some chips allegedly reaching China&\#x27;s black market. Prince Group denied that Hu ever worked for it and said the allegations of an illegal network and private-aircraft smuggling lack factual basis.

telegram · zaihuapd · Nov 22, 04:34

**「Background」** U.S. export controls restrict the sale of advanced NVIDIA AI chips to China, making diverted hardware a focus of semiconductor supply-chain enforcement. The FT report centers on Prince Group, a Cambodian conglomerate whose alleged role in the network is tied to Hu Xiaowei, whom the Treasury Department has described as its &quot;number two&quot; — a characterization the group rejects through its denial that Hu worked for it.

**「Impact」** The reported $4.6 billion in declared imports by Megaspeed&\#x27;s Malaysian subsidiary, if accurate, illustrates how Malaysian intermediaries can appear in trade data as legitimate importers while allegedly supplying China&\#x27;s black market — a routing pattern relevant to companies and compliance teams auditing Southeast Asian chip flows under U.S. export controls. The allegations remain unproven, and Prince Group denies them.

**Tags**: `#NVIDIA`, `#chip smuggling`, `#export controls`, `#semiconductor supply chain`, `#AI hardware`

---

<a id="item-tech-news-4"></a>
### [Anthropic 2028 power mix projected as 87% gas](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 7.0/10

A Better Data Center Project analysis, discussed on Hacker News, projects that by 2028 87% of Anthropic&\#x27;s power will come from natural gas and 11% from coal. The figures are presented as a projection tied to the company&\#x27;s data-center sourcing, not as measured emissions or a company commitment. The item&\#x27;s source content was unavailable, so the underlying methodology and the scope of the facilities covered could not be verified.

hackernews · happosai · Nov 22, 08:57 · [Discussion](https://news.ycombinator.com/item?id=50597612)

**「Background」** Colossus 1 is a Memphis-area data center built by xAI that is largely leased to Anthropic; it houses more than 220,000 Nvidia GPUs and provides over 300 megawatts of compute capacity. That lease is the backdrop for the projected 2028 power mix under discussion.

**「Impact」** For communities hosting Anthropic&\#x27;s leased data-center capacity, the projection implies that local air-quality and emissions burdens would continue to rest largely on fossil generation rather than new renewable supply. Commenters specifically point to the Memphis Colossus 1 lease and argue the company has made no US renewable commitments, contrasting it with Alphabet&\#x27;s public renewable procurement.

**「Community Discussion」** Commenters broadly criticized the fossil-heavy mix: one called Anthropic a &quot;legitimately bad actor&quot; over pollution from the Memphis Colossus 1 lease and its lack of US renewable commitments, while another argued regulation is needed because purely financial accounting ignores environmental and social costs passed to distant communities. A separate thread noted that much US natural gas is a byproduct of shale oil production and is sometimes flared, framing gas-fired data-center demand as tied to continued oil extraction.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Colossus_%28data_center%29">Colossus ( data center ) - Wikipedia</a></li>
<li><a href="https://thenextweb.com/news/musk-spacex-colossus-anthropic-180-day-lease">Musk walks back the Anthropic Colossus deal to a six-month lease</a></li>

</ul>
</details>

**Tags**: `#AI energy use`, `#data centers`, `#Anthropic`, `#grid infrastructure`, `#climate policy`

---

<a id="item-tech-news-5"></a>
### [Tim O&\#x27;Reilly Argues Silicon Valley Optimizes for Shareholder Value](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 7.0/10

In a new O&\#x27;Reilly Radar essay, Tim O&\#x27;Reilly argues that Silicon Valley has optimized for shareholder value instead of human flourishing, and proposes mechanism design—which he calls &quot;reverse game theory&quot;—as a way to rethink the rules shaping the tech economy. The essay&\#x27;s central question, quoted by a commenter, is &quot;What game ought we be playing?&quot;, to which O&\#x27;Reilly answers: &quot;The game of human flourishing.&quot; This is an opinionated industry analysis, not a product, policy, or pricing announcement; it reports no shipped capability, version, or independently measured result.

hackernews · greenyouse · Nov 22, 19:20 · [Discussion](https://news.ycombinator.com/item?id=50602947)

**「Background」** Mechanism design is an economics approach that starts from a desired outcome and works backward to the rules—incentives, constraints, and information flows—that would produce it, which is why O&\#x27;Reilly frames it as reverse game theory. The essay applies that lens to the incentives that have shaped Silicon Valley&\#x27;s growth and current priorities.

**「Impact」** For technologists and founders, the essay&\#x27;s framing suggests examining which metrics and incentive structures their own organizations reward rather than treating market outcomes as a natural force; it offers a basis for that debate but no specific policy or implementation proposal.

**「Community Discussion」** Commenters largely agreed with O&\#x27;Reilly&\#x27;s diagnosis but disputed the proximate cause: one attributed the situation to the ZIRP era, which allowed companies to grow to &quot;grotesque proportions&quot; and pushed startups to chase green fields, and argued that with interest rates back up, tech firms are now cannibalizing core competencies on the back of AI. Another dismissed contemporary &quot;VC influencers&quot; as self-serving, while others said the essay&\#x27;s mechanism-design argument, buried near the end, was its most important contribution.

**Tags**: `#tech industry`, `#mechanism design`, `#Silicon Valley`, `#incentives`, `#AI economics`

---

<a id="item-tech-news-6"></a>
### [Muru: AI-assisted Rust server for ASGI and WSGI Python apps](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, who started mod\_wsgi 20 years ago, has released Muru, an AI-assisted Rust server for running ASGI and WSGI Python applications in both development and production. Alongside the GitHub project, he has published a detailed 19-post development series over three weeks \(November 4–22, 2026\) covering worker internals, combined WSGI/ASGI support, HTTPS in development, releases without restarts, canary deployments without a service mesh, Kubernetes integration, scaling from worker reports, scale-to-zero, scheduled overlays, and a toolbar with tracing. Dumpleton writes that AI does much of the surface work but that he decides what is not good enough yet, drawing on two decades of mod\_wsgi experience. The supplied material contains no benchmarks, adoption figures, version numbers, or release/availability specifics.

rss · Simon Willison · Nov 21, 23:56

**「Background」** Graham Dumpleton created mod\_wsgi two decades ago, and the experience of that project shaped his long-running effort to design a better way to serve Python web applications in production. Muru applies that perspective through a Rust-based routing edge, control plane, and Python runtime for both WSGI and ASGI apps. The supplied material presents it as an early, AI-assisted project rather than a completed, benchmarked release.

**「Impact」** Python teams evaluating production servers now have a design to watch that explicitly targets ASGI and WSGI in one process model, with features like import-once-fork-many workers and scale-to-zero; however, the evidence offered so far is the author&\#x27;s design write-ups rather than independent benchmarks or documented production use, so adoption decisions should wait for measurable results.

<details><summary>References</summary>
<ul>
<li>Muru Python Server: WSGI, ASGI, Zero-Downtime (2026) - explainx.ai</li>
<li>muruhq/muru: Routing edge, control plane and Python runtime for WSGI ...</li>

</ul>
</details>

**Tags**: `#Python`, `#ASGI/WSGI`, `#Rust`, `#Web servers`, `#Open source`

---

<a id="item-tech-news-7"></a>
### [Phison 太空 SSD 将携 488 TB 入轨](https://videocardz.com/newz/phison-announces-488tb-of-ssd-storage-for-space-data-centers-pricing-expected-to-be-astronomical) ⭐️ 7.0/10

Phison announced a space-grade SSD series, with 488 TB planned for Lonestar&\#x27;s 2027 StarVault-001 orbital data center and drives offering up to 128 TB and pSLC-enhanced endurance.

telegram · zaihuapd · Nov 22, 10:31

**Tags**: `#storage`, `#hardware`, `#space computing`, `#data centers`, `#SSD`

---

<a id="item-tech-news-8"></a>
### [Moore Threads Lushan GPU reportedly targets 64 GB VRAM](https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80) ⭐️ 7.0/10

A Moore Threads product manager for the MTT S80 has indicated that the next-generation Lushan gaming GPU will carry more VRAM than any consumer card currently on sale, which VideoCardz calculated as 64 GB based on his earlier remark of &quot;4x the S80&\#x27;s 16 GB&quot; — double the RTX 5090&\#x27;s 32 GB. The statement is not an official company release. Moore Threads is sticking to targets disclosed at MDC 2025 for Lushan relative to the S80: 15x AAA gaming performance, 50x ray tracing, and 64x AI compute. The company says CEO Zhang Jianzhong will unveil a new flagship at MDC 2026, scheduled for December 29–30 in Beijing.

telegram · zaihuapd · Nov 22, 15:11

**「Background」** The MTT S80 is Moore Threads&\#x27; current consumer gaming card with 16 GB of VRAM, and Lushan is the anticipated successor whose performance multiples were first presented at MDC 2025. The 64 GB figure derives from multiplying that S80 baseline rather than from a published specification sheet.

**「Impact」** If the 64 GB capacity holds at launch, Lushan would offer twice the VRAM of an RTX 5090, a capacity aimed at large local AI models and high-resolution gaming workloads; buyers should nonetheless treat both the capacity and the 15x/50x/64x multiples as unverified targets until the MDC 2026 announcement and independent benchmarks.

**Tags**: `#GPU`, `#Moore Threads`, `#hardware`, `#VRAM`, `#gaming`

---

## Global Chips

<a id="item-chip-news-1"></a>
### [US seeks answers on Nvidia&\#x27;s sale of chips to China, Bessent says](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b037dde91064e6aa5f1e643ae7a945c&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2fus-seeks-answers-on-nvidia-s-sale-of-chips-to-china-bessent-says%2far-AA2hZ30C&amp;c=4330629169882901183&amp;mkt=en-us) ⭐️ 7.0/10

The US is seeking answers from Nvidia about its chip sales to China, according to Treasury Secretary Bessent.

rss · Bing News - NVIDIA and China · Nov 22, 09:52

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`

---

<a id="item-chip-news-2"></a>
### [Report: China spy agency prioritizes acquiring advanced chips](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b037dded24045c79d46a19c0945a9e1&amp;url=https%3a%2f%2fwww.fortuneindia.com%2fworld%2fchinas-chip-war-goes-covert-spy-agency-steps-up-hunt-for-advanced-chips-targets-global-semiconductor-intelligence%2f171697&amp;c=190024110062511024&amp;mkt=en-us) ⭐️ 7.0/10

China&\#x27;s intelligence agency has reportedly made acquiring advanced semiconductor chips and gathering intelligence on the global chip industry a strategic priority, according to a Fortune India report published November 22, 2026. The report describes a campaign lasting at least two years aimed at obtaining advanced chips and information about the global semiconductor sector. The available excerpt does not name the agency, identify specific targets, describe the methods used, or cite confirmation from any Chinese or foreign government, so the campaign remains a reported, unconfirmed claim rather than an announced policy or documented enforcement action. It does not establish which chips, companies or countries are involved, or whether any acquisition attempts succeeded.

rss · Bing News - China chip policy · Nov 22, 05:31

**「Background」** The reported intelligence campaign follows prior reporting that China&\#x27;s espionage efforts around advanced AI chips predate the current account. A New York Times report published a day before this item described a campaign in which Chinese intelligence helped domestic companies acquire and smuggle advanced chips into China and collected intelligence on the semiconductor sector and its supply chains, according to officials briefed on it. Advanced semiconductors remain the center of the U.S.-China technological rivalry, which is why chip acquisition and supply-chain intelligence have become an intelligence priority rather than only a trade-policy matter.

**「Impact」** If substantiated, the reported campaign would bear directly on export-control enforcement, since the advanced chips at issue are the same category of items restricted under existing controls on China&\#x27;s access to advanced semiconductors. The excerpt provides no evidence on whether any shipments, licences or diversions actually occurred, so no practical effect on supply, licensing or domestic substitution can be confirmed from this account.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China ’s Spies Set Sights on A.I. Chips Years Before Nvidia Scandal</a></li>
<li><a href="https://www.bbc.com/news/articles/cry49plv8v3go">Nvidia dismisses campaign to bring back Jensen Huang as Trump...</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#国产芯片`, `#中美芯片合作`, `#先进制程`, `#半导体情报`

---

<a id="item-chip-news-3"></a>
### [Bessent Seeks Answers on NVIDIA&\#x27;s Role in China AI Chip Shipments](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b037dde91064e6aa5f1e643ae7a945c&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fbessent-we-need-answers-on-nvidia-role-in-sending-china-ai-chips%2far-AA2hYC6F&amp;c=8529885070083262531&amp;mkt=en-us) ⭐️ 6.0/10

U.S. Treasury Secretary Scott Bessent said the government needs answers on NVIDIA&\#x27;s role in sending AI chips to China, asking whether the company had &quot;malicious actors down at the bottom of the company who were responsible for the noncompliance&quot; with chip export controls. The statement, reported on November 22, 2026, frames the matter as an enforcement question about individual employees rather than an announced action against the company. The supplied excerpt gives no specific enforcement measure, rule change, company response, dates or figures, so it remains an official statement of concern, not a confirmed finding or penalty.

rss · Bing News - NVIDIA and China · Nov 22, 10:49

**「Background」** The questioning comes amid a U.S. enforcement review of NVIDIA&\#x27;s China chip sales under existing export controls. Reuters reported that Washington is seeking answers on those sales and on who was in charge of compliance at the company, which it described as formerly led by Jensen Huang, who resigned following an affair. Bessent&\#x27;s remarks, reported by CBS News and Yahoo Finance, frame the issue as whether &quot;malicious actors down at the bottom of the company&quot; were responsible for noncompliance, rather than as a new rule or licensing decision.

**「Impact」** The remark indicates that U.S. enforcement scrutiny of NVIDIA&\#x27;s China-bound AI chip sales is concentrating on internal compliance and individual accountability, leaving licensing and shipment risk for China-bound products unresolved until the government says whether it has found a violation or is weighing action; the excerpt does not indicate any resulting restriction, charge or licence decision.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cbsnews.com/news/bessent-nvidia-china-ai-chips-alice-huang-canard/">Bessent says we &quot;need answers&quot; on role Nvidia played in ...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/scott-bessent-nvidia-must-answer-175445674.html?fr=sycsrp_catchall">Scott Bessent: Nvidia Must Answer Questions on China Chip Sales</a></li>
<li><a href="https://www.reuters.com/world/china/us-seeks-answers-nvidias-sale-chips-china-bessent-says-2026-11-22/">US seeks answers on Nvidia&#x27;s sale of chips to China, Bessent ...</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-4"></a>
### [Report alleges two-year Chinese spy campaign to obtain advanced AI chips](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b037dded24045c79d46a19c0945a9e1&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fchina-ran-2-year-spy-campaign-to-acquire-advanced-ai-chips-evade-us-curbs-report%2far-AA2hXEnG&amp;c=6558449294980266658&amp;mkt=en-us) ⭐️ 6.0/10

A report cited in a Bing News summary alleges that a Chinese intelligence agency ran a two-year campaign to acquire advanced AI chips and to map global supply chains, framing the effort as an attempt to evade US export controls. The item does not name the agency, the report&\#x27;s author or publisher, the specific chip types or quantities sought, or any dates or licensing provisions. It also includes no response from Chinese officials or companies, and the allegation is not independently corroborated in the supplied material.

rss · Bing News - China chip policy · Nov 22, 05:06

**「Background」** The claim follows earlier reporting that tied Chinese chip-acquisition efforts to a multi-year intelligence campaign. The New York Times reported on November 21, 2026 that the Chinese spy agency&\#x27;s campaign to acquire chips had been underway for at least two years, citing current and former officials who spoke anonymously and noting the details had not previously been reported. That account also places the campaign years before the Nvidia-related scrutiny it references, indicating US attention has extended from formal export-licensing rules to intelligence-collection channels.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China ’s Spies Set Sights on A . I . Chips Years Before Nvidia Scandal</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#英伟达`, `#AI 算力`, `#国产芯片`, `#中美芯片合作`

---

<a id="item-chip-news-5"></a>
### [US intelligence chief hints China obtained restricted AI chips](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b037dded24045c79d46a19c0945a9e1&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fworld%2fus-intelligence-chief-seemingly-confirms-china-accessed-restricted-america-made-ai-chips%2far-AA2hYJIR&amp;c=15614776108833554957&amp;mkt=en-us) ⭐️ 5.0/10

US intelligence chief Jay Clayton suggested that China unlawfully obtained restricted American AI chips, according to a report tied to an ongoing investigation into an alleged chip-smuggling network. The source provides no named companies, chip models, quantities, charges or confirmed findings, and its language remains hedged, describing what Clayton &quot;suggested&quot; rather than any announced enforcement action or enacted policy change. The report therefore signals an incremental development in an active smuggling probe rather than a verified restriction, shipment figure or confirmed court finding.

rss · Bing News - China chip policy · Nov 22, 13:50

**「Background」** The remark follows a federal smuggling case: in October 2026 the FBI arrested California tech CEO Greg Lui on charges of allegedly exporting more than $300 million in restricted US-made AI graphics processors to China, according to the New York Post report retrieved for this item. A New York Times report dated 21 November 2026 further described a Chinese intelligence campaign that included helping Chinese companies acquire and smuggle advanced chips into China, and collecting intelligence on semiconductor supply chains. Clayton&\#x27;s remark is a public statement by the Director of National Intelligence rather than a court finding; no chip models, quantities or named buyers have been confirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China ’s Spies Set Sights on A . I . Chips Years Before Nvidia Scandal</a></li>
<li><a href="https://nypost.com/2026/10/01/us-news/california-tech-ceo-arrested-for-allegedly-smuggling-300-million-in-restricted-ai-chips-into-china/">Exclusive | FBI arrests California tech CEO for smuggling $300M in AI ...</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#AI 算力`, `#中美芯片合作`, `#英伟达`

---

<a id="item-chip-news-6"></a>
### [Senator Kennedy Seeks Sworn Testimony From Lutnick on China&\#x27;s Nvidia Chip Access](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b037dde91064e6aa5f1e643ae7a945c&amp;url=https%3a%2f%2fwww.washingtonpost.com%2fpolitics%2f2026%2f11%2f22%2fsen-kennedy-urges-scrutiny-lutnick-over-chinas-access-nvidia-chips%2f&amp;c=7926976116405803250&amp;mkt=en-us) ⭐️ 4.0/10

Sen. John Kennedy \(R-Louisiana\) said he wants Commerce Secretary Howard Lutnick and Treasury Secretary Scott Bessent to testify under oath and &quot;answer some hard questions&quot; about China&\#x27;s access to Nvidia chips, according to a Washington Post report carried in Bing News&\#x27; Nvidia and China feed. The report supplies no new policy provision, licensing decision, product name, shipment figure or effective date — only the senator&\#x27;s call for sworn testimony. It therefore indicates continued congressional scrutiny of the Commerce Department&\#x27;s export-control posture toward Nvidia&\#x27;s China business rather than any change in what is permitted, restricted or shipped. The report does not say whether either secretary has responded, and no hearing date is given.

rss · Bing News - NVIDIA and China · Nov 22, 14:06

**「Background」** The Commerce Department, which Lutnick leads, administers the US export-control system that determines which Nvidia accelerators may be sold to Chinese customers and under what licence conditions, while Treasury&\#x27;s involvement runs through investment and sanctions authorities. Kennedy&\#x27;s demand for testimony under oath sits within that existing arrangement, but the supplied report does not identify the specific earlier rule, licence decision or hearing that prompted it.

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Deliberate Flailing as a Strategy Under Uncertainty](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 23, 00:00

**「Background」** When an engineer faces an unclear situation—no clear guidance and no obvious next step—the intuitive response is to wait until the situation is better understood. Sean Goedecke argues that this caution is usually a mistake, and that the faster path to understanding is deliberate &quot;flailing&quot;: acting speculatively before you know what will work. He acknowledges the obvious danger that badly executed flailing can damage a reputation.

**「Solution」** Goedecke&\#x27;s method has three mutually reinforcing parts: try many different things, pay very close attention to feedback, and ruthlessly drop anything that isn&\#x27;t getting positive feedback. Trying many things matters because most plans will be bad—if one has a low chance of being right, ten gives you a better shot—and because a portfolio of plans prevents over-investment in any single one. Feedback comes both from people with more expertise and from reality itself, such as measured latency or user metrics; ideally, plans that don&\#x27;t get a &quot;wow\!&quot; reaction are dropped immediately. He identifies three settings: product flailing, where the product hasn&\#x27;t found fit and it&\#x27;s better to explore at the margins than commit early—citing GitHub Models features that mostly failed, except AI inference via a GitHub Actions token, which became the seed of &quot;Continuous AI&quot;; engineering flailing, where large, tangled, or already-optimized systems are too complex to study exhaustively, so engineers should make speculative changes and dig in only if something looks better \(AI agents make this cheaper, he notes\); and organizational flailing, where senior engineers face non-technical problems and should try automating manual work, volunteering for tasks, or proposing long-term plans. In the organizational case, he warns that failing to notice when a plan is failing can redirect people&\#x27;s anger at you, whereas dropping it quickly can build trust. He calls the approach &quot;flailing&quot; because it feels like repeated failure from the inside, even if managers see a proactive experimenter; recognizing that feeling, he argues, helps treat it as a positive signal rather than trouble.

**「Takeaway」** The broader point is that uncertainty is best reduced through direct contact with many possible solutions and honest feedback, not through prolonged analysis—provided you are willing to abandon failing plans immediately. Acknowledging the psychological discomfort is part of the method, since it otherwise encourages premature retreat to caution.

**Tags**: `#engineering-practice`, `#decision-making-under-uncertainty`, `#organizational-effectiveness`, `#feedback-loops`, `#senior-engineers`

---

<a id="item-tech-blog-2"></a>
### [Good Programming Is Mostly Avoiding Blunders](https://seangoedecke.com/to-code-well-avoid-blunders/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 22, 00:00

**「Background」** Sean Goedecke argues that engineers misunderstand what makes code good: they picture brilliant insights and elegant new abstractions, when the real goal is simply to avoid catastrophic mistakes. Writing for people working in large commercial codebases with big teams, he compares programming to chess and tennis, where never blundering beats almost anyone who is only occasionally brilliant.

**「Solution」** The reason programming rewards this discipline is that it offers no durable winning advantage: one blunder can turn an elegant codebase into a janky one, unlike a basketball lead that survives a bad play. Goedecke&\#x27;s examples include introducing a parallel system for the same task, adding a second source of truth for key data, turning a safe sync operation into a delicate async one, adding subtle points of failure, and complicating a key interface. These reduce to two cardinal sins, inconsistency and unnecessary requirements. Inconsistency is dangerous because it breaks trust: engineers can no longer assume code works the sensible way and must hunt for surprises. Unnecessary requirements are dangerous because they are sticky, since someone encountering one in the codebase must assume it is necessary unless willing to research it, and because they interact combinatorially, so each new feature must be checked against every existing requirement. His prescription is to find where a task fits most normally into the current codebase and to trim it to the smallest set of requirements. Thinking &quot;I could implement it with this clever pattern&quot; is, to him, a warning sign of distraction and blunder risk; he adds that coding agents are roughly human-level at consistency but much worse at avoiding unnecessary requirements.

**「Takeaway」** Goedecke&\#x27;s thesis is that great programming does not require cleverness and may even be hindered by it; attention to detail and a laser focus on consistency and minimal requirements matter more. The broader point is that avoiding blunders, not discovering beautiful abstractions, is the main thing.

**Tags**: `#software design`, `#codebase maintainability`, `#engineering judgment`, `#consistency`, `#requirements management`

---

## Financial News

<a id="item-finance-news-1"></a>
### [US tech selloff prompts emergency market measures in Asia](https://news.bjd.com.cn/2026/11/22/12039852.shtml) ⭐️ 9.0/10

US AI technology stocks sold off sharply on Friday, with the Nasdaq falling 5.28% in a single day and the Philadelphia Semiconductor Index dropping nearly 11%. In response, mainland China, South Korea and Taiwan announced emergency market-stability measures, including Taiwan&\#x27;s full ban from Nov 23 on short-selling below the previous close.

telegram · zaihuapd · Nov 22, 13:24

**「Background」** The selloff follows a Reuters report that a wave of AI-related selling had already pushed Wall Street sharply lower in the prior session, with the Philadelphia Semiconductor Index — up as much as 106.6% in mid-June — now giving back part of that gain \(tool-1-3\). China&\#x27;s three main stock exchanges cut the minimum margin ratio for margin financing from 100% to 80% effective November 30, after China Securities Regulatory Commission approval, a measure estimated to theoretically unlock nearly RMB 400 billion in incremental capital \(tool-2-2\).

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/legal/transactional/wall-st-futures-slip-anthropic-debut-fails-reassure-ai-investors-2026-11-20/">Wall St ends sharply lower on AI selloff, S&amp;P 500, Dow in ...</a></li>
<li><a href="https://phemex.com/news/article/chinas-three-major-bourses-cut-margin-ratio-to-80-chinext-plans-market-maker-system-104510">China Cuts Margin Ratio to 80%, Unlocks RMB 400B Capital ...</a></li>

</ul>
</details>

**Tags**: `#U.S. tech selloff`, `#semiconductor stocks`, `#market stabilization measures`, `#Asian equities`, `#short-selling rules`

---

<a id="item-finance-news-2"></a>
### [中国要求美国撤销电话号段接入限制](https://www.bloomberg.com/news/articles/2026-11-22/china-objects-to-us-curbs-on-telecoms-access-to-phone-numbers) ⭐️ 7.0/10

中国商务部11月22日敦促美国撤销一项措施，该措施禁止中国移动、中国电信和中国联通直接获取美国电话号码。中国商务部称，美国联邦通信委员会（FCC）11月19日收紧互联网语音服务商接入美国号码安全要求的投票援引国家安全风险，却缺乏事实依据，并违反非歧视与公平竞争原则。

telegram · zaihuapd · Nov 22, 06:44

**「Background」** The FCC voted on Nov. 19 to bar China Mobile, China Telecom and China Unicom, among other IP-enabled service providers, from direct access to US phone numbers, citing national security and robocall concerns; the proposal had been scheduled for a vote since late October. Beijing&\#x27;s Nov. 22 demand follows earlier US restrictions on Chinese carriers&\#x27; US operations.

<details><summary>References</summary>
<ul>
<li>FCC votes to ban Chinese telecoms from direct access to US ... - Reuters</li>
<li><a href="https://www.reuters.com/world/fcc-votes-ban-chinese-telecoms-direct-access-us-phone-numbers-2026-11-19/">FCC votes to ban Chinese telecoms from direct access to US ...</a></li>
<li><a href="https://www.usnews.com/news/top-news/articles/2026-10-29/us-plans-to-ban-chinese-telecom-firms-from-direct-access-to-us-phone-numbers">US Plans to Ban Chinese Telecom Firms From Direct Access to ...</a></li>

</ul>
</details>

**Tags**: `#US-China relations`, `#telecom regulation`, `#FCC`, `#China carriers`, `#tech decoupling`

---