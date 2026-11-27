---
layout: default
title: "Horizon Summary: 2026-11-27 (EN)"
date: 2026-11-27
lang: en
---

> From 51 items, 22 important content pieces were selected

---

**Technology News**
1. [Google&\#x27;s Workspace MCP Servers Reportedly Exclude Gmail Sending for Agents](#item-tech-news-1) ⭐️ 8.0/10
2. [三部门印发实施方案：2030 年建成新一代通信网，适时开展 6G 建设](#item-tech-news-2) ⭐️ 8.0/10
3. [Neuralink Wins FDA Clearance for Pivotal ALS Brain-Implant Trial](#item-tech-news-3) ⭐️ 8.0/10
4. [NVIDIA halts AI server shipments to four Southeast Asian countries](#item-tech-news-4) ⭐️ 8.0/10
5. [Report: Zhipu GLM-5.5 and Moonshot Kimi K4 may slip to 2027](#item-tech-news-5) ⭐️ 8.0/10
6. [AI coding agents make self-hosting faster but raise security burden](#item-tech-news-6) ⭐️ 7.0/10
7. [AMD gfx906 fork of llama.cpp targets cheap high-bandwidth VRAM](#item-tech-news-7) ⭐️ 7.0/10
8. [SQLite&\#x27;s sqlite3\_rsync copies remote snapshots without full local duplication](#item-tech-news-8) ⭐️ 7.0/10
9. [Huawei to detail HBM chip with doubled data pin density](#item-tech-news-9) ⭐️ 7.0/10
10. [Cloudflare Workers Free plan adds email sending to verified addresses](#item-tech-news-10) ⭐️ 7.0/10
11. [ASML CEO warns full China chip-equipment cutoff would spur self-development](#item-tech-news-11) ⭐️ 7.0/10
12. [Cloudflare Dashboard and API outage continues past half hour](#item-tech-news-12) ⭐️ 7.0/10

**Global Chips**
1. [Nvidia reportedly halts AI chip shipments to four Southeast Asian nations](#item-chip-news-1) ⭐️ 7.0/10
2. [Huawei teases HBM chip aimed at Samsung, SK Hynix](#item-chip-news-2) ⭐️ 6.0/10
3. [Chengdu&\#x27;s Zhongte Micro Ships Seven Domestic Lithography Machines](#item-chip-news-3) ⭐️ 6.0/10
4. [Report: Nvidia halts Southeast Asia AI chip shipments as US curbs tighten](#item-chip-news-4) ⭐️ 5.0/10
5. [Trump to visit TSMC Phoenix advanced-chip plant](#item-chip-news-5) ⭐️ 5.0/10
6. [California companies owned by Chinese firms are scooping up Nvidia’s most advanced AI chips: report](#item-chip-news-6) ⭐️ 4.0/10
7. [Chinese AI chip stocks slide as overseas foundry question stays open](#item-chip-news-7) ⭐️ 4.0/10

**Technology Blog**
1. [Who Decides What Counts as AI-Written?](#item-tech-blog-1) ⭐️ 6.0/10

**Financial News**
1. [China&\#x27;s Double 11 smartphone sales fall 17% year over year as Apple leads](#item-finance-news-1) ⭐️ 7.0/10
2. [Dutch minister says Netherlands won&\#x27;t accept US bill restricting ASML&\#x27;s China sales](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Google&\#x27;s Workspace MCP Servers Reportedly Exclude Gmail Sending for Agents](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) ⭐️ 8.0/10

Google reportedly plans to have AI agents use MCP servers for its Workspace products, but the Gmail server described in the report cannot send email. The reported restriction is tied to Google&\#x27;s concern about human confirmation in the request path; the article title and Hacker News discussion are the supplied evidence, and no implementation details, version numbers, or rollout dates are available. Google&\#x27;s exact reasoning and the scope of the partner-only limitation therefore remain unconfirmed.

hackernews · ritzaco · Nov 26, 09:44 · [Discussion](https://news.ycombinator.com/item?id=50653477)

**「Context」** The Model Context Protocol \(MCP\) is the standardized interface through which AI agents call external tools and data sources. Google already documents a Gmail MCP server that provides agents a standardized way to read data such as searching emails, retrieving threads, and listing labels. The reported plan extends that pattern across Workspace MCP servers, while the Gmail server&\#x27;s inability to send email leaves agents with read-oriented access and keeps write actions restricted.

**「Impact」** If the reported design holds, developers building email-sending agents against Google Workspace would need separate or partner-only paths rather than a standard MCP send tool. Commenters warned that workaround browser automation would be messier and more wasteful, a concern about both reliability and resource use.

**「Community Discussion」** Commenters argued that MCP already provides elicitation, which lets a server pause a tool call and ask the user to confirm before proceeding, so gating a send-message tool behind partner-only access looks more like a business decision than a safety measure. Others predicted agents would simply drive a browser to send email, while one commenter described a pattern of building custom apps usable by both humans and agents.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server">Configure the Gmail MCP server | Google for Developers</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI agents`, `#Google Workspace`, `#developer tools`, `#platform policy`

---

<a id="item-tech-news-2"></a>
### [三部门印发实施方案：2030 年建成新一代通信网，适时开展 6G 建设](https://www.news.cn/politics/20261126/9fe827a2d98741acb60f62d36ba89cf7/c.html) ⭐️ 8.0/10

China&\#x27;s industry, cyberspace, and development authorities issued a next-generation communications network implementation plan targeting a complete network by 2030, timely 6G buildout, low-orbit satellite internet, and scaled 5G-A and converged industrial/vehicle networks.

telegram · zaihuapd · Nov 26, 06:30

**Tags**: `#6G`, `#telecom policy`, `#satellite internet`, `#5G-A`, `#network infrastructure`

---

<a id="item-tech-news-3"></a>
### [Neuralink Wins FDA Clearance for Pivotal ALS Brain-Implant Trial](https://www.bloomberg.com/news/articles/2026-11-25/neuralink-gets-clearance-for-brain-implant-trial-in-als-patients?srnd=phx-technology) ⭐️ 8.0/10

Neuralink said the FDA has cleared it to launch a pivotal clinical trial in the U.S. of its LINK implantable brain-computer interface in patients with ALS \(amyotrophic lateral sclerosis\). The trial, named LINK, aims to translate brain signals directly into computer control commands and is described as the first such pivotal trial approved in the United States. Neuralink says its earlier studies have implanted devices in more than 30 paralyzed patients worldwide; data from the pivotal trial are intended to support a future medical-device marketing application. The report, relayed via Telegram from Bloomberg, does not disclose the trial&\#x27;s design, enrollment size, timeline, or independent verification.

telegram · zaihuapd · Nov 26, 07:15

**「Background」** Neuralink is an American neurotechnology company founded by Elon Musk that has been developing implantable brain–computer interfaces since 2016. The LINK trial follows earlier-stage studies; the company says more than 30 paralyzed patients worldwide have received its implant in that research, which focused on safety rather than the pivotal data needed for a marketing application.

**「Impact」** Because this is a pivotal study, its data will be used to support a future medical-device marketing application, which means enrollment and site access now matter to ALS patients and the clinicians and research offices referring them; Neuralink says enrollment is open. Neuralink&\#x27;s president, DJ Seo, said the study will enroll 20 participants, a small cohort that falls well short of the more than 30 paralysis patients the company says have received implants in earlier research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neuralink">Neuralink - Wikipedia</a></li>
<li><a href="https://neuralink.com/updates/neuralink-receives-fda-approval-to-launch-link-pivotal-study/">Neuralink Receives FDA Approval to Launch LINK Pivotal Study</a></li>
<li><a href="https://casrai.org/news/neuralink-link-pivotal-trial-als-fda-clearance-2026">Neuralink LINK: First US Pivotal BCI Trial in ALS — CASRAI</a></li>
<li><a href="https://www.neurapod.com/blog/neuralink-fda-approval-link-pivotal-trial">Neuralink Gets FDA Approval for LINK, Its First Pivotal Trial</a></li>

</ul>
</details>

**Tags**: `#脑机接口`, `#Neuralink`, `#FDA临床试验`, `#渐冻症`, `#神经技术`

---

<a id="item-tech-news-4"></a>
### [NVIDIA halts AI server shipments to four Southeast Asian countries](https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370) ⭐️ 8.0/10

NVIDIA has reportedly asked major manufacturing partners to pause AI-server shipments to Malaysia, Singapore, Thailand, and Indonesia, and assemblers including Dell and Supermicro have told buyers in those four countries that affected orders cannot leave the factory. Three people familiar with the matter linked the freeze to a new round of U.S. export controls, though it remains unclear whether the pause is temporary. The U.S. Commerce Department issued rules the previous week requiring regional cloud service providers to obtain an export license within 90 days and to verify that their customers do not include restricted Chinese entities. The four countries have served as transit points through which Chinese AI companies obtain NVIDIA&\#x27;s most advanced processors, which cannot be exported directly to mainland China.

telegram · zaihuapd · Nov 26, 07:38

**「Background」** The four Southeast Asian countries have served as transshipment points through which Chinese AI companies obtain NVIDIA&\#x27;s most advanced processors, which cannot be exported directly to mainland China. Last week, the U.S. Commerce Department issued new rules requiring regional cloud service providers to obtain export licenses within 90 days and to verify that customers do not include restricted Chinese entities.

**「Impact on regional buyers」** For buyers in Malaysia, Singapore, Thailand, and Indonesia, orders already assembled by Dell and Supermicro are being held at the factory, so delivery timelines stay uncertain until the licensing question is resolved. The Commerce Department&\#x27;s interim rule also requires regional cloud providers to obtain export licenses within 90 days and verify their customers, adding a compliance burden for operators that relied on these four countries as a transit point for advanced NVIDIA chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/asia-pacific/nvidia-halts-chip-shipments-southeast-asia-ft-reports-2026-11-26/">Nvidia halts server shipments to four Southeast Asian ...</a></li>
<li><a href="https://www.dw.com/en/how-chinese-companies-circumvent-chips-sanctions-in-southeast-asia/a-80041002">US tries to restrict Chinese offshore computing capacity</a></li>
<li><a href="https://af.net/realtime/us-imposes-export-controls-on-advanced-ai-chips-to-5-nations-and-foreign-data-centers/">US Imposes Export Controls on Advanced AI Chips to 5 Nations and</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI infrastructure`, `#export controls`, `#supply chain`, `#Southeast Asia`

---

<a id="item-tech-news-5"></a>
### [Report: Zhipu GLM-5.5 and Moonshot Kimi K4 may slip to 2027](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/) ⭐️ 8.0/10

Reuters reports that Zhipu&\#x27;s planned flagship GLM-5.5, a roughly 3-trillion-parameter model originally expected this month, has not shipped and could be delayed to the first quarter of 2027 or later, according to unnamed people cited by the outlet. The reported causes include increasingly effective anti-distillation defenses and compute restrictions. Moonshot AI internally expects that losing all overseas compute would stretch its major release cadence from about six months to more than a year, potentially pushing its next flagship Kimi K4 to mid-2027; the report adds that Anthropic and OpenAI anti-distillation measures have made training data harder to obtain, prompting a shift toward distilling Google and Meta models. Zhipu reportedly denies the delay claim, according to a screenshot circulating on social media, so the timeline remains unconfirmed by the companies.

telegram · zaihuapd · Nov 26, 15:14

**「Background」** The report frames the delays around two pressures on Chinese labs: tightening US compute restrictions and more effective anti-distillation defenses at Anthropic and OpenAI, which the item says make training-data acquisition harder. Reuters notes that Moonshot&\#x27;s recent cadence was rapid—Kimi K2 shipped in July 2025, K2.5 in January, and K3 in July—so a reported slip to mid-2027 for K4 would be a marked slowdown from that sequence.

**「Impact」** If the reported timelines hold, users and developers building on the GLM and Kimi model families would face longer waits for next-generation capabilities and should not plan integrations around the expected release windows. The account also indicates that anti-distillation defenses are changing how Chinese labs source training data, a constraint that could affect model quality and release cadence beyond these two specific models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/">EXCLUSIVE: US chip curbs, distillation crackdown threaten ...</a></li>
<li><a href="https://aitoolranked.com/news/glm-5-5-kimi-k4-delayed-2027-us-chip-rules-distillation-reuters">GLM-5.5 and Kimi K4 Delayed? What Reuters Reports</a></li>

</ul>
</details>

**Tags**: `#Chinese AI labs`, `#model releases`, `#compute constraints`, `#anti-distillation`, `#AI industry`

---

<a id="item-tech-news-6"></a>
### [AI coding agents make self-hosting faster but raise security burden](https://janlukas.blog/posts/ai-self-hosting) ⭐️ 7.0/10

In a first-person post, Jan Lukas argues that AI coding agents have revived the appeal of self-hosting by removing much of the manual friction in deploying and maintaining small infrastructure. He describes moving his VPS setup to a custom Debian-based bootc image and replacing a workflow of editing a Docker Compose file, pushing to Git, SSHing in, pulling, and deploying with a single Git push, which may not even be necessary. Commenters agree deployment is easier but warn that faster provisioning shifts more responsibility onto the operator, including patching quickly after high-severity CVEs.

hackernews · jlelse · Nov 26, 21:47 · [Discussion](https://news.ycombinator.com/item?id=50660180)

**「Background」** Self-hosting small services has traditionally required maintaining the deployment pipeline yourself: version bumps, Compose changes, Git pushes, and manual server updates. The post describes using bootc, which builds bootable container images so the host operating system itself can be updated through the same image-based workflow.

**「Impact」** For self-hosters, the practical trade-off is that the same automation that shortens deployment to a Git push also makes it easier to stand up more services that then require ongoing security patching. One commenter says their patching expectations have tightened from periodic system updates and fail2ban to applying fixes within 24 hours of a high-severity CVE, a cadence they describe as increasingly demanding.

**「Community discussion」** Commenters are split on the net effect. One endorses automating drudgery and describes letting an agent deploy freely to a k3s homeserver behind Tailscale as a form of natural selection for projects, while another says the harder problem is accountability for security rather than the deployment itself. A separate commenter also questions whether the ease of implementation makes it more important to ask whether an idea is worth building at all.

**Tags**: `#self-hosting`, `#AI coding agents`, `#infrastructure automation`, `#DevOps`, `#security patching`

---

<a id="item-tech-news-7"></a>
### [AMD gfx906 fork of llama.cpp targets cheap high-bandwidth VRAM](https://devnull.land/amd-specific-llama-cpp) ⭐️ 7.0/10

A community fork of llama.cpp is tailored to AMD&\#x27;s circa-2018 gfx906 datacenter GPUs, which lack tensor cores and native bf16 support but pair modest compute with fast HBM2 memory. According to a commenter, early 2025 saw growing interest in these cards because 32GB of VRAM with roughly 1 TB/s bandwidth could be bought for about $200, versus more than $3,000 for the closest current cards. No source page content was supplied, so the fork&\#x27;s specific code changes, supported models, and measured performance cannot be independently described here. The work sits within a broader set of community efforts to optimize llama.cpp for atypical AMD hardware.

hackernews · julianlam · Nov 26, 17:11 · [Discussion](https://news.ycombinator.com/item?id=50657265)

**「Why gfx906 cards attract llama.cpp forks」** AMD&\#x27;s circa-2018 gfx906 datacenter series combines weak compute with fast HBM2 memory, which is why community work has focused on fitting llama.cpp to these cards rather than treating them as general-purpose AI accelerators. As one commenter describes it, early 2025 saw people notice that 32 GB of VRAM with roughly 1 TB/s bandwidth was available for about $200, well below comparable modern cards. The cards lack tensor cores and native bf16 support, so the optimization work centers on adapting kernels and quantization to their specific limits.

**「Impact」** For practitioners running local inference, the fork&\#x27;s premise is that bandwidth, not compute, limits token generation, so older gfx906 cards can remain useful for memory-bound decoding despite missing tensor cores and bf16. Users of these cards should expect to rely on quantization and community-maintained kernels rather than upstream llama.cpp defaults, and should validate any ported AMD kernels numerically before trusting results.

**「Community discussion」** Commenters described separate optimization efforts on AMD and Apple hardware: one reported roughly 2,400 tok/s prefill and 150 tok/s decode on a single R9700 with a 4-bit Qwen3.8-27B model, and another said aggressive AMD-code optimization plus porting Nvidia kernels to ROCm doubled or tripled Qwen3.8 performance on an MI100, with the ported kernels checked against the originals for numerical closeness. These are self-reported results on different hardware and software stacks, not verified benchmarks.

**Tags**: `#llama.cpp`, `#AMD GPU`, `#local inference`, `#gfx906`, `#quantization`

---

<a id="item-tech-news-8"></a>
### [SQLite&\#x27;s sqlite3\_rsync copies remote snapshots without full local duplication](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 7.0/10

Simon Willison highlighted that SQLite&\#x27;s experimental sqlite3\_rsync tool can copy a database snapshot over an SSH connection to another machine without first creating a full local duplicate. The tool was added as experimental in SQLite 3.47.0 in October 2024 and enhanced in SQLite 3.50.0 in May 2025. Unlike the backup API or VACUUM INTO, which require enough disk space to duplicate the database locally, sqlite3\_rsync sends cryptographic page hashes to the origin and transfers only differing page content; if the two sides start vastly different, bandwidth can exceed the database size by a few percent at most. It also can synchronize an existing copy without retransmitting the whole database.

rss · Simon Willison · Nov 26, 06:08

**「Background」** SQLite introduced \`sqlite3\_rsync\` as an experimental utility in version 3.47.0 in October 2024 and enhanced it in version 3.50.0 in May 2025. It is designed to create or update a copy of a SQLite database over SSH, including a database running in WAL mode.

**「Impact」** For users on small instances where the database already consumes more than half of available disk, sqlite3\_rsync provides a remote snapshot path that the backup API and VACUUM INTO cannot offer without extra local storage. Existing replicas can also be updated over the network without resending the entire database, though the tool is still labeled experimental.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sqlite.org/rsync.html">Database Remote-Copy Tool For SQLite</a></li>
<li><a href="https://til.simonwillison.net/sqlite/compile-sqlite3-rsync">Compiling and running sqlite 3 - rsync | Simon Willison’s TILs</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#databases`, `#rsync`, `#snapshotting`, `#backup`

---

<a id="item-tech-news-9"></a>
### [Huawei to detail HBM chip with doubled data pin density](https://www.bloomberg.com/news/articles/2026-11-26/huawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix) ⭐️ 7.0/10

Huawei plans to publish a research paper detailing a new high-bandwidth memory \(HBM\) chip whose title indicates a data-pin density twice that of Samsung and SK Hynix production products, according to Bloomberg. The paper is scheduled for a conference in San Francisco in February. The claim is theoretical and based on a paper title, not a demonstrated or shipping part, and Huawei is separately pushing to have HBM manufactured domestically in China, a component currently subject to US sanctions.

telegram · zaihuapd · Nov 26, 05:30

**「Context」** HBM stacks DRAM dies vertically and connects them through dense arrays of data pins, a design that trades cost and manufacturing complexity for the bandwidth AI accelerators need. Huawei&\#x27;s reported design is described only from a research-paper title listed in the advance program for the International Solid-State Circuits Conference \(ISSCC\), where the company is scheduled to present in February; the paper&\#x27;s full results have not been released.

**「Impact」** For Chinese AI accelerator designers, domestic HBM supply remains the binding constraint: CXMT has only begun shipping HBM3 samples to Huawei and other domestic AI hardware makers, and the gap to SK hynix, Samsung, and Micron is still measured in years. Even if Huawei&\#x27;s claimed pin-density advantage holds only on paper, a domestic HBM line would let local accelerator production continue insulated from US sanctions — though sourcing CXMT parts at elevated prices and reportedly poor yields implies higher memory costs.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/huawei-poised-to-grow-chinas-ai-chip-market-next-generation-hbm-design-double-data-pin-density/">Huawei Poised To Grow China’s AI Chip Market With...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-26/huawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix">Huawei Teases Next-Gen AI Memory Chip to Take On... - Bloomberg</a></li>
<li><a href="https://www.notebookcheck.net/CXMT-to-mass-produce-HBM3E-memory-chips-in-late-Q4-2026-despite-abysmal-yields.1437211.0.html">CXMT to mass produce HBM 3E memory chips in late Q4 2026 despite...</a></li>
<li><a href="https://neuroai.site/a/na-chips-domestic-hbm">China &#x27;s first homegrown HBM reaches customers · NeuroAI</a></li>

</ul>
</details>

**Tags**: `#HBM`, `#Huawei`, `#semiconductor manufacturing`, `#AI hardware`, `#US sanctions`

---

<a id="item-tech-news-10"></a>
### [Cloudflare Workers Free plan adds email sending to verified addresses](https://developers.cloudflare.com/changelog/post/2026-11-24-email-sending-workers-free/) ⭐️ 7.0/10

Cloudflare has enabled Email Sending on the Workers Free plan, limited to verified target addresses in the account. Developers can send alerts, reports, and notifications during development and testing via a Workers binding, REST API, or SMTP without a paid plan. Emails to verified addresses are free on all plans and do not count toward monthly quotas or daily send limits. Sending to arbitrary recipients still requires upgrading to the Workers Paid plan.

telegram · zaihuapd · Nov 26, 07:35

**「Background」** Email Sending is one of Cloudflare Workers&\#x27; binding-based integrations, letting a Worker send mail through a Workers binding, the REST API, or SMTP rather than through a separate email provider. The changelog entry extends that capability to the Free plan, but only for recipients already verified on the account; arbitrary recipients still require Workers Paid.

**「Impact」** Developers building Workers-based notifications can test and run sends to their own verified addresses without consuming quota, but any production path that emails end users requires the Paid plan, so recipient verification is not a substitute for a paid upgrade.

**Tags**: `#Cloudflare Workers`, `#email sending`, `#serverless`, `#free tier`, `#developer platform`

---

<a id="item-tech-news-11"></a>
### [ASML CEO warns full China chip-equipment cutoff would spur self-development](https://www.semafor.com/article/11/25/2026/asml-makes-the-case-for-selling-chips-to-china) ⭐️ 7.0/10

ASML CEO Christophe Fouquet said in an interview on Semafor&\#x27;s Future Proof program that export controls should protect the most advanced chipmaking technology but should not exclude China entirely, arguing that a full cutoff would push China to &quot;double or triple&quot; investment in its own development. Fouquet said the equipment ASML sells to China is more than a decade behind leading-edge processes, and that preserving that gap keeps China dependent on Western tools. He said ASML has held close to a 100% share of China&\#x27;s lithography market over roughly 30 years. The U.S. is pushing the MATCH Act, which would widen restrictions from EUV to immersion DUV and maintenance services; both ASML and the Dutch government oppose it.

telegram · zaihuapd · Nov 26, 12:19

**「Background」** The US has already restricted China&\#x27;s access to ASML&\#x27;s most advanced EUV systems and certain higher-end DUV equipment, while ASML remains allowed to sell older DUV machines to China. In August 2026, a bill known as the MATCH Act was before the US Congress; it would push allies to align their export controls with Washington&\#x27;s and extend restrictions to immersion DUV sales plus installation, maintenance, spare parts, remote software updates, and technical support for covered machines already in China. Both ASML and the Dutch government oppose the measure.

**「Impact」** If the MATCH Act passes as described, Chinese fabs would face restrictions on immersion DUV tools and maintenance services that current EUV-focused controls do not cover, narrowing what ASML and other suppliers could sell there. ASML and the Dutch government have formally opposed the measure, setting up a conflict with the U.S. push.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thedefensenews.com/US-Pushes-Bill-to-Compel-Netherlands-to-Halt-Remaining-ASML-Machine-Sales-and-Service-to-China/">US Pushes Bill to Compel Netherlands to Halt Remaining ASML ...</a></li>
<li><a href="https://nltimes.nl/2026/08/20/us-preparing-force-netherlands-ban-asml-selling-china">U.S. preparing to force Netherlands to ban ASML from selling ...</a></li>
<li><a href="https://www.trendforce.com/news/2026/08/25/news-u-s-may-push-near-total-asml-china-ban-on-duv-sales-and-servicing-amid-chinas-domestic-lithography-push/">[News] U.S. May Push Near-Total ASML China Ban on DUV Sales ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#export controls`, `#ASML`, `#lithography`, `#US-China tech policy`

---

<a id="item-tech-news-12"></a>
### [Cloudflare Dashboard and API outage continues past half hour](https://www.cloudflarestatus.com/incidents/xiqj67vl5pqm) ⭐️ 7.0/10

Cloudflare posted an incident notice on its status page on November 26 saying it was investigating problems with the Cloudflare Dashboard and related APIs. Customers using the console and API may see failed requests or error pages. The notice describes an outage that had already lasted about half an hour at publication time; Cloudflare did not provide a root cause, scope, or estimated recovery time.

telegram · zaihuapd · Nov 26, 16:33

**「Background」** Cloudflare publishes incident notices on its public status page, which is the company&\#x27;s own channel for reporting problems affecting its Dashboard and APIs. The source reports only that Cloudflare was investigating the issue, without root-cause or scope details beyond affected console and API users.

**「Impact」** Teams that manage configurations or automate deployments through the Cloudflare Dashboard and API should expect failed requests and error pages and may need to delay or retry changes until Cloudflare reports recovery. The notice does not indicate whether traffic served through Cloudflare&\#x27;s network is affected.

**Tags**: `#cloudflare`, `#outage`, `#api`, `#infrastructure`, `#service-status`

---

## Global Chips

<a id="item-chip-news-1"></a>
### [Nvidia reportedly halts AI chip shipments to four Southeast Asian nations](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f47ff472cbf875865e3cf1439&amp;url=https%3a%2f%2fgizmodo.com%2fnvidia-reportedly-freezes-ai-chip-shipments-to-southeast-asian-countries-2000845928&amp;c=13759470686377298211&amp;mkt=en-us) ⭐️ 7.0/10

Nvidia has reportedly instructed its manufacturing partners to stop shipping its AI chips to Indonesia, Malaysia, Singapore and Thailand, according to a Gizmodo report. The report does not name the affected chip products, shipment volumes, the manufacturing partners involved or an effective date, and neither Nvidia nor any government has confirmed the instruction in the supplied material. It is therefore an unconfirmed supply-chain directive rather than an enacted export-control rule or a documented licensing decision, and the scope of any restriction remains unknown.

rss · Bing News - NVIDIA and China · Nov 26, 07:24

**「Background」** The reported halt comes about a week after new U.S. export restrictions, according to Forbes, which frames Nvidia&\#x27;s move as part of tightening curbs on China. Reports name Dell and Supermicro as the manufacturing partners told to stop shipping servers containing Nvidia chips to Malaysia, Singapore, Thailand and Indonesia, though the source item itself confirms only the four destination countries and the instruction to partners, without product names, volumes or an effective date.

**「Practical effect on China&\#x27;s offshore compute access」** The reported halt matters because the four named markets have served as an offshore access route: data-center operators in Indonesia, Malaysia, Singapore and Thailand have provided Chinese firms with remote access to advanced Nvidia chips those firms cannot buy directly or bring into China, according to the New York Times. A separate CNBC report dated the same day says Nvidia chip buyers were told to rule out Chinese renters when purchasing GPUs, a condition that runs through the supply chain from chip sellers to the neoclouds that rent out computing power. If the freeze is confirmed and enforced alongside that restriction, the practical constraint on Chinese AI developers is not only the loss of new hardware in those countries but also scrutiny of who ultimately uses rented capacity — while the affected scope remains unconfirmed, with no product names, volumes or effective dates disclosed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/siladityaray/2026/11/26/nvidia-reportedly-halts-ai-chip-shipments-to-southeast-asia-as-us-tightens-china-curbs/">Nvidia Halts Server Shipments To 4 Southeast Asian Countries Amid...</a></li>
<li><a href="https://www.theguardian.com/business/live/2026/nov/26/nvidia-chip-shipments-south-east-asia-stock-dentists-live-updates">Nvidia reportedly halts chip shipments to south-east... | The Guardian</a></li>
<li><a href="https://nypost.com/2026/11/26/business/nvidia-halts-server-shipments-to-4-southeast-asian-countries-report/">Nvidia halts server shipments to 4 Southeast Asian countries: report</a></li>
<li><a href="https://www.nytimes.com/2026/11/17/business/southeast-asia-china-ai-chips.html">Trump’s New A . I . Chip Rules Rattle Southeast Asia - The New York...</a></li>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>
<li><a href="https://www.cnbc.com/2026/11/26/neoclouds-nvidia-china-ai.html">Nvidia chip buyers told to rule out Chinese renters to purchase GPUs</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#供应链`

---

<a id="item-chip-news-2"></a>
### [Huawei teases HBM chip aimed at Samsung, SK Hynix](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f8ef34052a1b7b305f9e93101&amp;url=https%3a%2f%2fwww.thestar.com.my%2ftech%2ftech-news%2f2026%2f11%2f27%2fhuawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix&amp;c=10675602340255321941&amp;mkt=en-us) ⭐️ 6.0/10

Huawei Technologies is preparing to release details of a new high-bandwidth memory \(HBM\) chip that it positions against current offerings from Samsung Electronics and SK Hynix, according to a report carried by The Star. The report frames the part as potentially surpassing the incumbents&\#x27; products, but discloses no HBM generation, bandwidth or capacity figures, process node, production timeline, or verified performance data, and Huawei has not published specifications. The superiority claim is therefore an unconfirmed assertion rather than a measured or shipped result; what has been disclosed so far signals Huawei&\#x27;s memory roadmap only.

rss · Bing News - China chip policy · Nov 26, 12:00

**「Background」** High-bandwidth memory stacks DRAM dies vertically to feed AI accelerators, a format initially developed by Samsung, AMD and SK Hynix. HBM has since advanced from HBM3 to its extended HBM3e generation, the segment where Samsung and SK Hynix compete most directly. Huawei&\#x27;s teaser does not specify an HBM generation, bandwidth, capacity or release date, so the part cannot yet be placed against those shipping generations.

**「Impact」** If Huawei follows through with specifications or samples, the relevant test is whether a domestic HBM option becomes available for its own AI accelerators, reducing reliance on Samsung and SK Hynix parts at a time when advanced memory imports face export controls. Until a generation, capacity and timing are published, buyers cannot assess compatibility with existing accelerator designs or plan procurement around it.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.edn.com/a-sneak-peek-at-the-hbm-cold-war-between-samsung-and-sk-hynix/">A sneak peek at HBM cold war between Samsung and SK hynix - EDN</a></li>

</ul>
</details>

**Tags**: `#国产芯片`, `#AI 算力`, `#华为`, `#高带宽内存`, `#对华出口管制`

---

<a id="item-chip-news-3"></a>
### [Chengdu&\#x27;s Zhongte Micro Ships Seven Domestic Lithography Machines](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb3005d941b1893fd8de40077a98&amp;url=https%3a%2f%2ffinance.eastmoney.com%2fa%2f202611273941506868.html&amp;c=16915117598286584113&amp;mkt=en-us) ⭐️ 6.0/10

Zhongte Micro \(Chengdu\) Electronic Technology Co. held a concentrated shipment of seven domestically produced lithography machines at the Konggang Juguang Photoelectric Industrial Park in Shuangliu District, Chengdu, according to an Eastmoney report dated November 27, 2026. The news coincided with a 1.37% intraday rise in the SSE STAR Chip Design Theme Index \(950162\), which the Guolian An STAR Chip Design ETF \(588780\) tracks, as of 09:33 that day; the ETF had turnover of 0.33% and traded value of 2.3628 million yuan. Constituent stocks rose, led by JoulWatt \(杰华特\) up 8.66%, Centec Networks \(盛科通信\) up 5.49%, and New Vision Microelectronics \(新相微\) up 4.47%, with Siliup \(思瑞浦\) and Yutai Micro \(裕太微\) also gaining. The report did not specify the models, process nodes, capacity, customers or performance of the seven machines, so the shipment&\#x27;s technical significance cannot be assessed from this account.

rss · Bing News - China domestic chips · Nov 26, 12:11

**「Background」** China&\#x27;s lithography equipment has been the most constrained segment of its semiconductor supply chain, with domestic tools concentrated at mature nodes while advanced immersion and EUV systems remain subject to Dutch and other allied export controls. The report gives no earlier shipment, customer or production milestone for Zhongte Micro \(Chengdu\), and no tool results were supplied to establish a direct predecessor event.

**「Impact」** The shipment indicates that at least one additional domestic supplier is delivering lithography tools in volume to Chinese fabs, but because the report omits machine type, node and customers, it does not establish which production steps or capacity the seven tools support. The market reaction was confined to chip-design equities rather than equipment suppliers, so the report offers no evidence on how much of China&\#x27;s lithography demand these machines replace.

**Tags**: `#国产芯片`, `#光刻机`, `#半导体设备`, `#科创芯片设计ETF`, `#国产替代`

---

<a id="item-chip-news-4"></a>
### [Report: Nvidia halts Southeast Asia AI chip shipments as US curbs tighten](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f47ff472cbf875865e3cf1439&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fnvidia-reportedly-halts-ai-chip-ship.%2520HelloWORLDts-to-southeast-asia-as-us-tightens-china-curbs%2far-AA2ih9aN&amp;c=7560169844318157466&amp;mkt=en-us) ⭐️ 5.0/10

A single unverified report claims that Nvidia has halted AI chip shipments to Southeast Asia as US export restrictions on China tighten, but the item supplies no chip model names, shipment volumes, destination countries, effective dates, or specific policy provisions. The only supporting detail in the supplied content is an unconfirmed allegation involving Jensen Huang, which is not established fact and is not relevant to chip supply. The halt therefore remains a reported claim rather than a confirmed change to Nvidia&\#x27;s shipping or licensing posture.

rss · Bing News - NVIDIA and China · Nov 26, 03:17

**「Background」** The report is framed against the existing US-China export-control regime that has previously constrained Nvidia&\#x27;s China-bound AI chip sales, with Southeast Asia cited as a transshipment route under scrutiny. The supplied item does not identify a specific prior rule, licence decision, or product generation that directly precedes this reported halt, so the trigger and scope cannot be verified from the available evidence.

**「Impact」** If confirmed, a halt on Southeast Asia shipments would constrain Nvidia&\#x27;s regional distribution channel and could affect how AI compute reaches customers that route purchases through those markets, but the supplied report gives no timing, volume, or licensing detail to establish the practical effect on shipments or on China&\#x27;s domestic chip substitution.

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#东南亚出货`

---

<a id="item-chip-news-5"></a>
### [Trump to visit TSMC Phoenix advanced-chip plant](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f8ef34052a1b7b305f9e93101&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2ftrump-to-visit-maker-of-semiconductor-chips-including-nvidias%2far-AA2ijwJN&amp;c=5887081375257091898&amp;mkt=en-us) ⭐️ 5.0/10

President Trump is reportedly set to visit TSMC&\#x27;s Phoenix, Arizona, facility, described as one of the largest makers of advanced chips, including chips produced for Nvidia. The source gives no date for the visit and announces no new policy provisions, investment figures, capacity numbers or licensing decisions. It should therefore be read as a scheduled executive visit rather than a change to semiconductor policy or production.

rss · Bing News - China chip policy · Nov 26, 17:21

**「Background」** The visit is tied to a specific expansion step rather than the original Phoenix site: a White House official told KJZZ that Trump is expected to deliver remarks on the groundbreaking of a new facility at TSMC&\#x27;s Phoenix campus, and The Independent reports the speech is set for Dec. 4, 2026. TSMC&\#x27;s Arizona campus already produces advanced chips, including for Nvidia, according to the source account, so the new construction marks a further stage of that build-out.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cbsnews.com/news/trump-visit-tsmc-semiconductor-facility-phoenix-nvidia/">Trump to visit Arizona manufacturer of semiconductor chips</a></li>
<li><a href="https://www.kjzz.org/politics/2026-11-25/trump-is-expected-to-visit-tsmcs-phoenix-campus-where-they-make-nvidia-chips">Trump is expected to visit TSMC&#x27;s Phoenix campus, where they ...</a></li>
<li><a href="https://www.independent.co.uk/news/world/americas/us-politics/trump-tsmc-arizona-chip-foundry-b3092143.html">Donald Trump to celebrate new Arizona chip foundry right ...</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#晶圆产能`, `#先进制程`, `#中美芯片合作`

---

<a id="item-chip-news-6"></a>
### [California companies owned by Chinese firms are scooping up Nvidia’s most advanced AI chips: report](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f47ff472cbf875865e3cf1439&amp;url=https%3a%2f%2fnypost.com%2f2026%2f11%2f26%2fus-news%2fchinese-owned-california-companies-buying-up-advanced-nvidia-ai-chips-report%2f&amp;c=10062808716971268677&amp;mkt=en-us) ⭐️ 4.0/10

A short report claims Chinese-owned California companies are acquiring Nvidia&\#x27;s most advanced AI chips, but offers only anonymous, unspecified details and no verifiable figures.

rss · Bing News - NVIDIA and China · Nov 26, 12:41

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-7"></a>
### [Chinese AI chip stocks slide as overseas foundry question stays open](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb3005d941b1893fd8de40077a98&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261127A069NA00&amp;c=9450142772382014334&amp;mkt=en-us) ⭐️ 4.0/10

Several Chinese AI compute chip companies saw sharp share-price declines in mid-to-late November 2026, even after some said operations were normal. On November 19, Enflame \(688801.SH\) fell 20%, MetaX \(688802.SH\) dropped 14.72% and Moore Threads \(688795.SH\) fell 8.34%, according to the report. Enflame and Iluvatar CoreX \(09903.HK\) said production and operations were normal, but the declines continued: on November 25, Biren Technology \(06082.HK\) fell 24.71% and Iluvatar CoreX dropped 18.51%. The item frames, but does not substantiate, the question of which companies would absorb domestic chip orders if overseas foundry access is restricted; no details on the restriction, order transfers, capacity or policy provisions were visible.

rss · Bing News - China domestic chips · Nov 26, 12:10

**「Background」** The late-November selloff came after a mid-2026 listings and product push among Chinese GPU designers: Horizon&\#x27;s reporting cited Biren&\#x27;s new flagship BR20X being sent to lead customers, and the Shanghai exchange had scheduled a June 2026 review of Suiyuan Technology&\#x27;s IPO. On the manufacturing side, SMIC said its first-quarter 2026 wafer average selling price rose 2.5% sequentially even as shipments slipped 0.2%, and SMIC and Hua Hong both reported stronger second-quarter results — signs that domestic foundry capacity and pricing were already tightening before the stock declines sharpened the question of who absorbs orders that cannot be placed overseas.

<details><summary>References</summary>
<ul>
<li><a href="https://news.mydrivers.com/1/1168/1168651.htm">一天 跌 去近四分之一！ 壁 仞 科 技 称新旗舰实测已达H200水平</a></li>
<li><a href="https://stock.10jqka.com.cn/20260608/c677305094.shtml">利好突袭，美 股 反弹了！ A 股 ， 年 内93家半导体公司减持 | 同花顺财经</a></li>
<li><a href="https://news.10jqka.com.cn/20260521/c676848970.shtml">AI 虹 吸成熟 产 能 国 产 晶圆 代 工 开启提价扩 产 周期 | 同花顺财经</a></li>

</ul>
</details>

**Tags**: `#国产芯片`, `#AI 算力`, `#对华出口管制`, `#晶圆代工`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Who Decides What Counts as AI-Written?](https://seangoedecke.com/who-gets-to-decide-if-something-is-written-by-ai/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 27, 00:00

**「Background」** Every day brings a new dispute about whether something was written by AI: a writing prize winner accused, an author dropped after Pangram flagged her manuscript, a tweet dissected by strangers. Sean Goedecke notes that arguments about detector reliability and the ethics of scanning other people&\#x27;s writing miss the deeper conflict — many anti-AI people simply hate AI detection tooling — and sets out to explain why.

**「Solution」** Goedecke argues the dispute is really about power: who gets to gatekeep prizes, fail students, and exclude people from public discourse. He presents the skeptics&\#x27; case sympathetically — Pangram belongs to the same tech sector they distrust, and the broader shift toward legible, tool-based processes over messy human community judgment has been bad for people, so distrusting a tool-shaped solution is rational. He is pro-Pangram only because the alternative is community self-policing, which he considers worse: people who don&\#x27;t use AI are poor judges of AI text, as he observes on Twitter, where obvious AI tells go unrecognized and long, polite human writing gets accused. A community-run standard, he concludes, would let more AI-written work into art and culture. Instead, skeptics should push for open-source detectors or government-built detection platforms, even though those are also AI tools.

**「Takeaway」** The real question is not whether detectors are accurate but who should hold the authority to adjudicate authorship; Goedecke contends that, given how unreliable community judgment is, even AI skeptics should prefer institutional detection tools — ideally public or open-source ones.

**Tags**: `#AI detection`, `#AI authorship`, `#power and institutions`, `#community moderation`, `#technology criticism`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China&\#x27;s Double 11 smartphone sales fall 17% year over year as Apple leads](https://counterpointresearch.com/en/insights/china-double-11-smartphone-sales-drop-17-percent-on-weak-demand) ⭐️ 7.0/10

Smartphone sales in China fell 17% year over year during the 2026 Double 11 shopping period, which ran from Oct. 12 to Nov. 13, according to Counterpoint Research. Apple remained the top brand with an 8% decline, while Huawei was the only major vendor to grow, up 29%.

telegram · zaihuapd · Nov 26, 09:38

**「Background」** Brand discounts, coupons and trade-in subsidies failed to offset price increases driven by higher component costs, and 81% of Chinese consumers planning to buy a phone within six months said they had noticed the price rises and were more inclined to delay than pay more.

**「Impact」** Apple held six of the top 10 best-selling models and the iPhone 18 Pro Max ranked first, while Huawei&\#x27;s growth was driven by the Enjoy 90 Pro Max, Pura X View and the newly released Enjoy 100 series.

**Tags**: `#China smartphone market`, `#Double 11 sales`, `#Apple`, `#Huawei`, `#consumer demand`

---

<a id="item-finance-news-2"></a>
### [Dutch minister says Netherlands won&\#x27;t accept US bill restricting ASML&\#x27;s China sales](https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml) ⭐️ 7.0/10

Dutch foreign trade minister Sjoerd Sjoerdsma told parliament on November 26 that the Netherlands will not accept further US restrictions on ASML&\#x27;s China sales, opposing the extraterritorial reach of the proposed MATCH Act, which would require allies such as the Netherlands and Japan to tighten export controls on China or face unilateral US limits on their semiconductor equipment. The Netherlands is coordinating with the European Commission and lobbying with Germany and France to strip the bill from the US annual defense policy legislation ahead of an expected mid-December congressional vote.

telegram · zaihuapd · Nov 26, 14:56

**「Background」** The MATCH Act, a bipartisan US bill introduced in April 2026, would require allies such as the Netherlands and Japan to tighten export controls on chipmaking equipment for China or face unilateral US restrictions. The US and Dutch governments already bar ASML from selling its most advanced EUV machines to China, so the proposal would extend curbs beyond existing limits.

**「Impact」** ASML is directly exposed: China accounted for about 20% of its sales this year, and the proposed MATCH Act could tighten curbs on those shipments and also affect other Dutch, Japanese and allied semiconductor-equipment suppliers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fool.com/investing/2026/04/24/the-match-act-could-blow-a-hole-in-asmls-revenue-h/">The MATCH Act Could Blow a Hole in ASML &#x27;s Revenue. Here&#x27;s What...</a></li>
<li><a href="https://keepingupwith.ai/articles/netherlands-opposes-match-act-at-risk-to-asmls-china-business/">Netherlands Opposes MATCH Act at Risk to ASML &#x27;s China Business</a></li>
<li><a href="https://www.techi.com/asml-china-euv-export-scrutiny-stock/">Washington Thinks China Has ASML &#x27;s Best Machine. ASML Says...</a></li>

</ul>
</details>

**Tags**: `#semiconductor export controls`, `#ASML`, `#Netherlands`, `#US legislation`, `#MATCH Act`

---