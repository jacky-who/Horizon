---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 26 items, 14 important content pieces were selected

---

**Technology News**
1. [Lean formalization of the Riemann Hypothesis reportedly verified](#item-tech-news-1) ⭐️ 10.0/10
2. [GPGME pre-2.3.0 double free disclosed as RCE](#item-tech-news-2) ⭐️ 8.0/10
3. [Trump threatens &\#x27;massive taxes&\#x27; on US firms building AI data centers abroad](#item-tech-news-3) ⭐️ 8.0/10
4. [Microsoft previews RDMA over USB4 for multi-PC local AI](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenRouter warns MiniMax prompts may have been read by third parties](#item-tech-news-5) ⭐️ 8.0/10
6. [Zhejiang University reports first on-chip QRAM demonstration](#item-tech-news-6) ⭐️ 8.0/10
7. [🚘 特斯拉开始推送 FSD v15](#item-tech-news-7) ⭐️ 8.0/10
8. [Monitor&\#x27;s USB Ethernet cut download speed 75%](#item-tech-news-8) ⭐️ 7.0/10
9. [Graham Dumpleton launches Muru, an AI-assisted Rust server for Python apps](#item-tech-news-9) ⭐️ 7.0/10
10. [ChatGPT Spaces opens collaboration to Plus users](#item-tech-news-10) ⭐️ 7.0/10

**Global Chips**
1. [US chip rule takes effect; Taiwanese foundry halts 16nm orders for mainland clients](#item-chip-news-1) ⭐️ 8.0/10
2. [Report: Paid influencers promoted Nvidia AI chip exports to China](#item-chip-news-2) ⭐️ 6.0/10

**Technology Blog**
1. [Avoid Blunders to Code Well](#item-tech-blog-1) ⭐️ 6.0/10

**Financial News**
1. [特朗普力挺卢特尼克，并希望黄仁勋道歉后回归](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Lean formalization of the Riemann Hypothesis reportedly verified](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 10.0/10

On November 20, 2026, Levent Alpöge reportedly published a Lean formalization of the Riemann Hypothesis in a codebase of roughly 17 million lines. The next day, Lean FRO and the Mathlib Initiative jointly stated that the formalized proposition matches Mathlib&\#x27;s \`RiemannHypothesis\` and that the codebase compiles without errors, with multiple independent proof checkers confirming the proof&\#x27;s validity. The claim comes from a Telegram repost of the Lean community blog announcement rather than an independent technical report, so the certification rests on the community&\#x27;s stated verification.

telegram · zaihuapd · Nov 21, 16:48

**「Prior claim and Lean context」** Levent Alpöge, an Anthropic researcher, announced on November 20, 2026 that he and Claude had produced a Lean formalization of the Riemann Hypothesis plus a method extending to the Generalized Riemann Hypothesis; early write-ups treated it as a claim rather than a verified proof, and one account described the archive as 175,187 files. Lean is a proof assistant and Mathlib its main mathematics library, where a formal statement of the Riemann Hypothesis already exists, which is why the community check compared Alpöge&\#x27;s statement against Mathlib&\#x27;s \`RiemannHypothesis\`. The development now reported is the joint Lean FRO/Mathlib Initiative certification and independent-checker verification dated November 21.

**「Impact」** If the certification holds, the result would give researchers a machine-checked proof tied to Mathlib&\#x27;s existing statement of the Riemann Hypothesis, shifting scrutiny toward the reliability of Lean&\#x27;s kernel and the independent checkers rather than the proof&\#x27;s mathematics. Commenters pointed to a prior fake Collatz refutation that passed one such checker, so the result&\#x27;s strength depends on how genuinely independent those verification paths are.

**「Community discussion」** Hacker News commenters argued that falsifying the result would now require a bug affecting every kernel, including those with their own consistency proofs, though one noted that a fake Collatz refutation previously slipped past an independent checker. Others credited Alpöge with eliciting the formalization and suggested the work, if valid, also constitutes a substantial contribution to formalized mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unite.ai/levent-alpoges-unverified-riemann-claim-puts-claudes-lean-code-in-focus/">Levent Alpöge’s Unverified Riemann Claim Puts Claude’s Lean ...</a></li>
<li><a href="https://stateofproof.org/paper-watch/paper-2026-11-20-a-claimed-proof-of-the-riemann-hypothesis">A Claimed Proof of the Riemann Hypothesis — Paper Watch ...</a></li>
<li><a href="https://casrai.org/news/anthropic-levent-alpoge-claude-lean-riemann-hypothesis-claim-2026">175,000-File Lean Riemann Hypothesis Proof Claim — CASRAI</a></li>

</ul>
</details>

**Tags**: `#Lean`, `#formal verification`, `#Riemann Hypothesis`, `#Mathlib`, `#mathematics`

---

<a id="item-tech-news-2"></a>
### [GPGME pre-2.3.0 double free disclosed as RCE](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 8.0/10

GPGME versions before 2.3.0 reportedly contain a memory-safety flaw affecting any software that links the library, including mail clients, XMPP clients, Samba, and Flatpak. The disclosure was moved up to 2026-11-20 from a planned 2026-11-25 coordinated date because GitLab needed to ship updates earlier amid the Ruby2Shell bug; GitLab also published an Omnibus patch for the signed-commit path. Commenters dispute the framing: one says the underlying issue is a double free rather than a full RCE chain, while another points to a Red Hat fix from roughly five years ago that upstream apparently missed. No exploit details or confirmed real-world impact are available in the supplied material.

hackernews · gdgghhhhh · Nov 21, 08:32 · [Discussion](https://news.ycombinator.com/item?id=50587208)

**「Background」** GPGME, the library applications use to integrate GnuPG, has a double-free flaw tracked as CVE-2026-129975 that is triggered by a crafted OpenPGP key. The advisory states the issue affects GPGME versions before 2.3.1, and before 1.24.4 on the 1.x branch. Community commenters add that a Red Hat downstream patch reportedly addressed the flaw years ago without an upstream fix.

**「Affected deployments」** All software linked against GPGME before version 2.3.0 is affected, whether GPGME is loaded as a shared library, a Windows DLL, or statically linked, according to the advisory and coverage citing CVE-2026-129975. Maintainers and users of mail clients, XMPP clients, Samba, Flatpak, and Gpg4win should verify which GPGME version their builds actually ship and upgrade to 2.3.0 or later; the disclosure date was moved from 2026-11-25 to 2026-11-20 because GitLab needed to ship its signed-commit patch earlier.

**「Community discussion」** Commenters disagreed on severity and accuracy: mik1998 called it a double free and questioned whether the RCE label was intentionally overstated, while uptrails noted that Red Hat apparently fixed the issue about five years ago in a CentOS Stream packaging patch that upstream missed. miduil added that Johan Carlsson discovered the bug and that GitLab informed the project on 2026-11-12, prompting the earlier disclosure date.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.ostorlab.co/gpgme-double-free-cve-2026-129975.html">GPGME Double Free: Data Theft, Possible RCE (CVE-2026-129975)</a></li>
<li><a href="https://lists.gnu.org/archive/html/info-gnu/2026-11/msg00006.html">GnuPG Security Advisory for GPGME (T8557,CVE-2026-129975)</a></li>
<li><a href="https://thecybersecguru.com/uncategorized/cve-2026-129975-gpgme-double-free/">GPGME Bug Hid for 24 Years: CVE-2026-129975 Explained | The ...</a></li>
<li><a href="https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html">[Announce] GnuPG Security Advisory for GPGME ...</a></li>
<li><a href="https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html">GnuPG Warns Critical GPGME Flaw Could Expose App Data via...</a></li>

</ul>
</details>

**Tags**: `#security`, `#GnuPG`, `#GPGME`, `#vulnerability`, `#open source`

---

<a id="item-tech-news-3"></a>
### [Trump threatens &\#x27;massive taxes&\#x27; on US firms building AI data centers abroad](https://apnews.com/article/trump-artificial-intelligence-data-centers-f1ac03b73d13445400eeed8631d9d879) ⭐️ 8.0/10

Speaking at a White House press conference on November 20, Trump said he plans to impose &quot;massive taxes&quot; on US tech companies that build AI data centers overseas, framing the measure as a way to keep data centers in the United States and preserve AI competitiveness with China. He said he had not yet told officials inside his administration about the plan. He also urged US communities to accept data centers, suggesting they negotiate with developers for payments, as localities around the country oppose new projects over electricity demand and noise concerns. The proposal has no stated implementation details or timeline.

telegram · zaihuapd · Nov 21, 03:26

**「Background」** Trump&\#x27;s remarks came during a White House press conference on November 20, 2026, and were reported as a threat to penalize or restrict American companies that build data centers abroad, with Trump citing a &quot;tremendous tax&quot; penalty as the mechanism. He acknowledged he had not yet disclosed the plan to officials within his own administration, so the proposal has no published legislative text, rate, or enforcement procedure. The statement sits alongside his call for U.S. communities to accept data centers and negotiate payments from developers, as local opposition over electricity demand and noise has stalled projects in many parts of the country.

**「Impact」** For US operators weighing overseas AI capacity, the statement introduces tax risk without published scope, rate, or legislative path, so it cannot yet be modeled into site-selection decisions. The simultaneous push for communities to negotiate developer payments signals that local opposition over power use and noise remains a practical constraint on domestic buildouts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/technology/trump-says-us-penalize-firms-building-data-centers-abroad-2026-11-20/">Trump says US to penalize firms building data centers abroad</a></li>
<li><a href="https://www.nytimes.com/2026/11/20/us/politics/trump-data-centers-ban.html">Trump threatens to bar U.S. tech firms from building data ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html">Trump vows to stop U.S. companies from building data centers ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#tech policy`, `#US-China competition`, `#tax policy`

---

<a id="item-tech-news-4"></a>
### [Microsoft previews RDMA over USB4 for multi-PC local AI](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

Microsoft released a developer preview of RDMA over USB4 for Windows that lets multiple PCs share memory and GPU compute over ordinary USB4 connections, without specialized network cards or switches, to run a single local AI model. In a demonstration, three AMD Ryzen AI Max+ 395 systems ran a 4-bit quantized Qwen3-235B-A22B model at about 18.5 tokens per second. The preview is to be distributed through Windows Insider. These details come from a Telegram summary of a VideoCardz article rather than Microsoft&\#x27;s primary documentation, and the performance figure has not been independently verified in the supplied material.

telegram · zaihuapd · Nov 21, 06:13

**「Background」** RDMA \(remote direct memory access\) has traditionally required specialized network adapters and switches; Microsoft&\#x27;s developer preview applies it over the USB4 links already present on many PCs so connected machines can pool memory capacity and GPU compute for a single model. Microsoft announced the preview on November 19, 2026, and is distributing it through Windows Insider builds.

**「Impact」** For developers and small teams, this points to pooling existing USB4-equipped machines into a local inference cluster without buying dedicated networking hardware. Because the capability is a developer preview delivered via Windows Insider, it should be treated as experimental rather than a supported production path until Microsoft publishes compatibility and setup requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://techcommunity.microsoft.com/blog/microsoftusbblog/introducing-rdma-over-usb4%C2%AE-on-windows-run-larger-local-ai-models-across-pcs/4574602">Introducing RDMA over USB4® on Windows: run larger local AI ...</a></li>
<li><a href="https://xenospectrum.com/en/windows-rdma-usb4-local-ai/">Microsoft Previews RDMA over USB4 for Windows, Splitting ...</a></li>

</ul>
</details>

**Tags**: `#RDMA over USB4`, `#Windows`, `#local AI inference`, `#distributed computing`, `#USB4`

---

<a id="item-tech-news-5"></a>
### [OpenRouter warns MiniMax prompts may have been read by third parties](https://news.ycombinator.com/item?id=50585962) ⭐️ 8.0/10

OpenRouter has reportedly emailed users warning that request content sent to MiniMax models may have been read by third parties. Security researchers sent prompts containing test URLs to MiniMax models between July and October 2026, and third parties accessed those URLs 40–130 hours later, according to the relayed report. OpenRouter attributed the issue to MiniMax and its relays AtlasCloud, Novita, and StreamLake, removed the &quot;zero data retention&quot; labels from affected endpoints, and advised users who sent sensitive credentials to rotate API keys and passwords. OpenRouter has not published a public notice on its website, and the account comes from a Telegram relay of a Hacker News post rather than an official disclosure.

telegram · zaihuapd · Nov 21, 06:53

**「Background」** OpenRouter is a routing layer that forwards prompts to third-party model hosts, and its Zero Data Retention setting restricts traffic to endpoints that pledge not to routinely store prompts or responses after processing. The labels now removed from the affected MiniMax endpoints and the AtlasCloud, Novita, and StreamLake relays were the indicators that such a policy applied to those routes.

**「Impact」** Developers routing LLM traffic through OpenRouter to MiniMax models or the affected AtlasCloud, Novita, and StreamLake relays can no longer rely on those endpoints&\#x27; &quot;zero data retention&quot; designation, so prompts containing secrets, credentials, or sensitive customer data should be treated as potentially exposed. The recommended mitigation is to rotate any API keys and passwords that appeared in such prompts and to reassess which endpoints are acceptable for confidential workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/docs/guides/features/zdr">Zero Data Retention - How OpenRouter gives you control over your...</a></li>
<li><a href="https://aifoss.dev/blog/ollama-vs-openrouter-vs-groq-vs-nvidia-nim-llm-serving-2026/">Ollama vs OpenRouter vs Groq vs NVIDIA NIM in 2026</a></li>

</ul>
</details>

**Tags**: `#LLM security`, `#data privacy`, `#OpenRouter`, `#MiniMax`, `#API providers`

---

<a id="item-tech-news-6"></a>
### [Zhejiang University reports first on-chip QRAM demonstration](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 8.0/10

Zhejiang University researchers report demonstrating quantum random access memory \(QRAM\) on a real superconducting chip, &quot;Tianmu-2,&quot; which they fabricated themselves; the work was published in Nature Physics. The chip ran 4-bit and 8-bit QRAM prototypes that retrieved data with 80.9% and 60.4% accuracy respectively, according to the report. The team says circuit depth was reduced by more than 30% versus an unoptimized scheme and that the architecture showed local noise resilience for the first time. The item is a brief Sina Finance report relaying the claim rather than the primary paper, and the team&\#x27;s next step is scaling QRAM up.

telegram · zaihuapd · Nov 21, 08:31

**「Background」** QRAM is a proposed quantum memory architecture that would let a quantum computer fetch classical data stored at an address held in superposition, a capability needed for algorithms such as quantum search and quantum linear algebra. The source identifies the device as Zhejiang University&\#x27;s independently fabricated superconducting chip &quot;Tianmu-2&quot;; a co-first author is quoted in external coverage describing it as a 100-qubit chip with a neighbor-tunable coupling architecture. Because the supplied source is a brief repost and does not link the underlying Nature Physics paper, the reported figures and the world-first framing remain claims from the university team as relayed by Sina Finance, not independently measured results.

**「Impact for quantum developers」** The reported 4-bit and 8-bit prototypes at 80.9% and 60.4% accuracy fall well short of fault-tolerant operation, so quantum algorithm developers relying on QRAM for data loading should treat this as a feasibility demonstration rather than usable memory. The reported circuit-depth reduction of over 30% and validation of local noise resilience give hardware teams a concrete design target, since long addressing circuits and noise have historically caused the quantum state to collapse before data is read. The team&\#x27;s stated next step is scaling QRAM research, so the capability remains research-stage on the Tianmu-2 chip rather than a general-purpose component.

<details><summary>References</summary>
<ul>
<li><a href="https://min.news/en/tech/4b9aa39797970c13ed2ca775adc98f77.html">Zhejiang University &amp; Tsinghua University &quot; Nature &quot;: Realizing a ne...</a></li>
<li><a href="https://3g.china.com/act/news/10000169/20260414/49412417.html">量 子 机 器 学习找到新的突破口 绕开 QRAM 实 现指数级内 存 优势_中华网</a></li>
<li><a href="https://news.mydrivers.com/1/1167/1167501.htm">news.mydrivers.com/1/1167/1167501.htm</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#hardware`, `#research`

---

<a id="item-tech-news-7"></a>
### [🚘 特斯拉开始推送 FSD v15](https://x.com/Tesla/status/2124222447855743019) ⭐️ 8.0/10

特斯拉在海外开始推送 FSD v15，宣称安全关键场景处理能力提升至 25 倍，并新增 Tesla Reality View 可视化界面与多项驾驶体验优化。

telegram · zaihuapd · Nov 22, 00:03

**Tags**: `#Tesla FSD`, `#autonomous driving`, `#software release`, `#AI safety`, `#visualization`

---

<a id="item-tech-news-8"></a>
### [Monitor&\#x27;s USB Ethernet cut download speed 75%](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

A blog post documents how routing Ethernet through a USB hub in a monitor reduced a laptop&\#x27;s download speed by 75%. The author traced the problem to added latency introduced by the monitor path, which prevented the laptop from acknowledging packets fast enough; a buffer in the USB Ethernet adapter then filled and dropped packets. Switching to a different adapter that required less frequent acknowledgement fixed the issue. The finding is an anecdotal debugging account, not a controlled benchmark.

hackernews · soheilpro · Nov 21, 10:36 · [Discussion](https://news.ycombinator.com/item?id=50587875)

**「Background」** USB Ethernet adapters depend on timely USB transfers between the adapter and the host; when those transfers are delayed, TCP acknowledgements can arrive too slowly and overwhelm adapter buffering. Monitors with built-in USB hubs add another hop between the host and the adapter, which can introduce latency and make opaque USB hub behavior harder to diagnose.

**「Impact」** For users with monitor or dock Ethernet, the reported case suggests testing the adapter directly on the laptop before blaming the network; a different adapter or a direct connection avoided the 75% slowdown in this account.

**「Community Discussion」** Commenters pushed back on the monitor framing, with one arguing the better description is that the USB network switch cut download speed and that the monitor is largely irrelevant. Another commenter summarized the mechanism for readers who misunderstood the post: extra latency through the monitor led to slow acknowledgements, adapter buffer fill, and packet drops, and a different adapter with less frequent acknowledgement fixed it. A separate commenter said they had experienced a similar issue for over a year with a MacBook and Thunderbolt dock, and that enabling flow control finally made it tolerable.

**Tags**: `#networking`, `#USB`, `#debugging`, `#hardware`, `#performance`

---

<a id="item-tech-news-9"></a>
### [Graham Dumpleton launches Muru, an AI-assisted Rust server for Python apps](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, the creator of mod\_wsgi, has started Muru, an AI-assisted Rust server intended to serve ASGI and WSGI Python applications in both development and production. The project is hosted on GitHub, and over the past three weeks Dumpleton published an 18-post development journal documenting its design, including worker internals, HTTPS in development, running WSGI and ASGI together, release-without-restart deploys, canaries without a service mesh, Kubernetes integration, scaling to zero, and a tracing toolbar. The write-ups describe the project&\#x27;s goals and design rather than an independently benchmarked or widely adopted release, and Dumpleton states that AI does much of the surface work while he judges what is good enough.

rss · Simon Willison · Nov 21, 23:56

**「Background」** Muru is a follow-up to mod\_wsgi, the Apache module Dumpleton began 20 years ago for hosting WSGI Python applications. Existing servers such as Gunicorn already run both WSGI and ASGI frameworks, and ASGI separates server implementation from application framework, so Muru enters a crowded space. His development journal documents design choices including the \`muru.wsgi\_to\_asgi\` bridge object placed in the WSGI environ so WSGI requests can be handed off to ASGI applications.

**「Impact」** Developers running WSGI or ASGI apps get early visibility into an alternative server from the author of mod\_wsgi, with features aimed at production deployment such as Kubernetes-aware operation, scheduled overlays, and scaling to zero; however, the material published so far is a design journal, so teams should treat Muru as early-stage rather than as a validated replacement for existing servers.

<details><summary>References</summary>
<ul>
<li><a href="https://grahamdumpleton.me/posts/2026/11/muru-wsgi-and-asgi-together/">Muru : WSGI and ASGI together - Graham Dumpleton</a></li>
<li><a href="https://github.com/Kludex/uvicorn">GitHub - Kludex/uvicorn: An ASGI web server , for Python.· GitHub</a></li>
<li><a href="https://gunicorn.org/">Gunicorn - Python WSGI HTTP Server for UNIX</a></li>

</ul>
</details>

**Tags**: `#python`, `#asgi`, `#wsgi`, `#rust`, `#web-servers`

---

<a id="item-tech-news-10"></a>
### [ChatGPT Spaces opens collaboration to Plus users](https://x.com/ChatGPT/status/2123850912867471807) ⭐️ 7.0/10

ChatGPT&\#x27;s Space feature is now available to Plus subscribers, letting them collaborate with others on interactive pages, slideshows, and websites. Spaces sits in the sidebar and holds pages, slideshows, images, files, and uploads; pages and slideshows can be set to auto-update from connected tools, and others can be invited to co-edit. Mobile editing is supported, and OpenAI claims the overall experience is smoother and more stable. The item relays OpenAI&\#x27;s announcement without independent testing or details on rollout timing or plan limits.

telegram · zaihuapd · Nov 21, 02:30

**「Background」** ChatGPT Space initially launched for Pro, Business, and Enterprise plan subscribers, where it served as a shared home for pages, uploaded files, and other work in ChatGPT. OpenAI is now extending the feature to Plus subscribers paying $20 per month, and OpenAI&\#x27;s help documentation says Space is rolling out to eligible Plus accounts—users who don&\#x27;t see it in the desktop app may need to update to the latest version or wait for availability on their account.

**「Impact」** Plus subscribers can now invite collaborators into a Space, so teams mixing paid Plus accounts with other tiers may need to confirm who can co-edit before relying on a shared Space as a working document.

<details><summary>References</summary>
<ul>
<li><a href="https://www.engadget.com/2323016/openai-brings-its-collaborative-space-hubs-to-plus-users/">OpenAI brings its collaborative Space hubs to Plus users</a></li>
<li><a href="https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt">Getting started with Space in ChatGPT - OpenAI Help Center</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#OpenAI`, `#AI tools`, `#collaboration`, `#product update`

---

## Global Chips

<a id="item-chip-news-1"></a>
### [US chip rule takes effect; Taiwanese foundry halts 16nm orders for mainland clients](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b024f8fc40b4f7fbc8fd6ebf33c7694&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1104594585_122434980&amp;c=5517385477629821742&amp;mkt=en-us) ⭐️ 8.0/10

A US Commerce Department Bureau of Industry and Security rule titled 《应对先进半导体远程访问》 took effect on November 19, and on the same day a Taiwanese foundry notified mainland Chinese customers that orders at 16nm and below are suspended until a US export licence is obtained. The reported fallback is 28nm and 40nm, but only for chips that do not use high-bandwidth memory and do not require advanced packaging. Mainstream AI chips are mostly produced at 7nm and below, so some design companies reportedly found themselves with completed designs and no available foundry slot. The report is an overview and does not name the foundry or the affected design firms, nor does it give order volumes or licensing figures.

rss · Bing News - China domestic chips · Nov 21, 09:54

**「Background」** The November 19 rule, titled &quot;Addressing Remote Access to Advanced Semiconductors,&quot; builds on successive U.S. tightenings of advanced-computing exports to China. A BIS press release describes it as an interim final rule written at the direction of Treasury and the National Security Council to cover remote access to advanced super-intelligence chips and servers, extending existing restrictions on sensitive computing access. Legal and market analyses published in the days before it took effect noted that Chinese firms, barred from directly buying NVIDIA&\#x27;s high-end AI chips, had still obtained advanced compute by leasing it, including through third countries — a channel this rule targets. The source item adds that on the same day, a Taiwanese foundry told mainland customers to stop 16nm-and-below orders unless they obtain U.S. export licences, with 28nm and 40nm work permitted only for chips that use no high-bandwidth memory and no advanced packaging.

**「Impact on China AI chip supply」** For Chinese AI chip designers, the practical effect is a foundry bottleneck at exactly the nodes their mainstream products use: with 16nm-and-below orders halted pending U.S. export licences, and 28/40nm offered only for designs that avoid high-bandwidth memory and advanced packaging, chips designed at 7nm and below have no compliant path at that Taiwanese foundry. The source presents this as an immediate order stop rather than a licensing review with a defined approval track, and names no specific companies, wafer volumes or licence-processing timelines, so the duration of the disruption and any substitution capacity remain unquantified.

<details><summary>References</summary>
<ul>
<li><a href="https://media.bis.gov/press-release/bis-issues-rule-addressing-remote-access-american-super-intelligence-technology">media.bis.gov</a></li>
<li><a href="https://www.junhe.com/legal-updates/3205">美国BIS新规拟限制先进算力芯片远程访问</a></li>
<li><a href="https://finance.sina.com.cn/wm/2026-11-17/doc-iniyznqf5442111.shtml">美国BIS出新规，封堵新马泰等五国远程算力租赁通道</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#国产芯片`, `#AI 算力`, `#先进制程`, `#晶圆代工`

---

<a id="item-chip-news-2"></a>
### [Report: Paid influencers promoted Nvidia AI chip exports to China](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b024f8ffc1f498796350c8e6e9eff09&amp;url=https%3a%2f%2fwww.yahoo.com%2fnews%2fpolitics%2farticles%2finfluencers-were-paid-back-donald-191500789.html&amp;c=2021865863505746190&amp;mkt=en-us) ⭐️ 6.0/10

An investigation alleges that more than 80 influencers were paid to promote exports of Nvidia AI chips to China, using coordinated talking points and collectively reaching about 14 million followers, according to a report relayed by Yahoo News. The item does not name the investigators, the funders, the payment amounts or the timeframe, and it identifies no change in U.S. export-control rules or in Nvidia&\#x27;s licensed China sales. The claim therefore rests on a single investigation as described in the source, not on an enacted policy or a confirmed corporate action.

rss · Bing News - NVIDIA and China · Nov 21, 11:15

**「Background」** The item does not name the investigating organization, the funder or the campaign dates, so the basic provenance of the paid-influencer claim remains unknown. External reports on the same investigation describe a watchdog finding that more than 80 mostly right-wing influencers likely promoted pro-AI-industry posts without clear sponsorship disclosure, praising Nvidia&\#x27;s interests and backing chip sales to China; the ultimate source of funding is described as unclear. No prior Horizon digest entry establishes a direct predecessor to this campaign.

**「Impact」** Because the report does not establish who paid for the campaign or whether it touched any formal lobbying or licensing process, its practical effect on U.S. export licensing or on Nvidia&\#x27;s China shipments is unverified; any consequence for the export-control debate depends on follow-up reporting identifying the funders and the specific policy asks the messaging promoted.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/news/influencer-campaign-nvidia-chip-sales-china/">Paid influencers pushed Nvidia’s China chip sales while ...</a></li>
<li><a href="https://emergent.sh/news/right-wing-influencers-paid-push-nvidia-ai">Right-Wing Influencers Paid to Push Nvidia AI Talking Points</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Avoid Blunders to Code Well](https://seangoedecke.com/to-code-well-avoid-blunders/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 22, 00:00

**「Background」** Sean Goedecke argues that programmers and others overvalue brilliance. In large commercial codebases, clever abstractions and “extra credit” features distract engineers from the real job: avoiding catastrophic mistakes.

**「Solution」** Goedecke&\#x27;s central insight is that programming offers no durable winning advantage. Unlike basketball, where a blunder merely trims a large lead, one bad decision can turn an elegant codebase into a janky one. He lists common blunders: introducing a parallel system that does the same task, creating a second source of truth for key data, converting a safe synchronous operation into a delicate asynchronous one, adding subtle failure points, and complicating a key interface. These share two cardinal sins: inconsistency and unnecessary requirements. Inconsistency breaks trust—engineers can no longer assume code behaves sensibly and must hunt for surprises. Unnecessary requirements are sticky, because someone encountering one must assume it is necessary unless willing to investigate, and they interact combinatorially, making large codebases hard to work in. His prescription is to fit each task as normally as possible into the existing codebase and trim it to the smallest set of requirements, leaving little energy for clever patterns or extra features. He warns that thinking “I could implement this with a clever pattern” signals distraction and risk.

**「Takeaway」** Goedecke concludes that great programming does not require cleverness—it may even be a disadvantage. Attention to detail and a focus on consistency and minimal requirements matter more, though he notes his advice targets large, team-based commercial codebases and that coding agents remain weaker than humans at avoiding unnecessary requirements.

**Tags**: `#software engineering`, `#code quality`, `#technical debt`, `#engineering judgment`, `#maintainability`

---

## Financial News

<a id="item-finance-news-1"></a>
### [特朗普力挺卢特尼克，并希望黄仁勋道歉后回归](https://www.reuters.com/world/us/trump-says-he-still-backs-lutnick-urges-nvidias-huang-apologize-2026-11-20/) ⭐️ 7.0/10

美国总统特朗普 11 月 20 日表示仍支持商务部长卢特尼克，称其“做得很好”，尽管英伟达相关争议令外界质疑卢特尼克对华芯片销售的处理；他还称希望已辞职的英伟达 CEO 黄仁勋“郑重道歉后回归”，并称已与中国国家主席习近平谈及此事。特朗普的说法与财政部长贝森特称通话未涉及黄仁勋相矛盾。

telegram · zaihuapd · Nov 21, 05:03

**「Background」** The scrutiny of Lutnick stems from criticism that his Commerce Department shielded Nvidia from tougher rules on advanced AI chip sales to China, and some critics called for his resignation over reports he stalled a crackdown on chip diversions. Nvidia&\#x27;s board announced Jensen Huang&\#x27;s resignation as CEO earlier in November 2026, naming CFO Colette Kress as interim boss.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/12/us/politics/lutnick-nvidia-commerce-china-chips.html">Howard Lutnick Took Softer Line on Nvidia as Calls for Tougher...</a></li>
<li><a href="https://www.newsmax.com/newsmax-tv/howard-lutnick-gordon-chang-nvidia/2026/11/14/id/1276323/">Gordon Chang to Newsmax: Lutnick Should Resign Over Nvidia ...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/12/nvidia-ceo-jensen-huang-resigns">Jensen Huang resigns as Nvidia CEO after alleged... | The Guardian</a></li>
<li><a href="https://www.bbc.co.uk/news/live/c6zjry11v8w1t">Huang agrees to appear before Congress, US lawmakers say, after...</a></li>

</ul>
</details>

**Tags**: `#US-China chip policy`, `#Nvidia`, `#Commerce Department`, `#executive personnel`, `#technology regulation`

---