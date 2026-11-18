---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 40 items, 13 important content pieces were selected

---

**Technology News**
1. [Google announces Gemini 4 Neon](#item-tech-news-1) ⭐️ 9.0/10
2. [Nginx patches 10 CVEs tied to unauthenticated NGINX2Root chain](#item-tech-news-2) ⭐️ 8.0/10
3. [Quad9&\#x27;s France exit and the case against DNS piracy blocking](#item-tech-news-3) ⭐️ 7.0/10
4. [Google DeepMind makes Genie 4 available to AI Ultra subscribers](#item-tech-news-4) ⭐️ 7.0/10
5. [Microsoft announces seven AI models at Ignite 2026](#item-tech-news-5) ⭐️ 7.0/10
6. [Stenberg: AI Rust rewrites of curl lag real project&\#x27;s bugfixes](#item-tech-news-6) ⭐️ 7.0/10
7. [Reported Java4Shell RCE Affects Java 17/21/25/27](#item-tech-news-7) ⭐️ 7.0/10

**Technology Blog**
1. [FlyDSL MonoKernels Cut Interactive LLM Decode Latency in vLLM](#item-tech-blog-1) ⭐️ 8.0/10

**Financial News**
1. [Fed minutes signal further rate hikes and flag AI inflation risk](#item-finance-news-1) ⭐️ 9.0/10
2. [Fed’s Waller floats half-point December rate hike](#item-finance-news-2) ⭐️ 7.0/10
3. [Banks Pause $480 Million ByteDance GPU Loan After New US Chip Rules](#item-finance-news-3) ⭐️ 7.0/10
4. [UK Immigration and Asylum Bill passes House of Commons](#item-finance-news-4) ⭐️ 7.0/10
5. [Tencent Q3 2026: AI capex jumps, free cash flow negative](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Google announces Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) ⭐️ 9.0/10

Google has announced Gemini 4 Neon, a new model in its Gemini lineup. The supplied item does not include the announcement body, so Neon&\#x27;s pricing, context window, benchmark results, and availability cannot be verified. Hacker News discussion focused on how the model is positioned relative to Gemini Carbon and Anthropic&\#x27;s Opus 5.5.

hackernews · yigitdemirag · Nov 18, 21:34 · [Discussion](https://news.ycombinator.com/item?id=50552424)

**「Earlier Gemini 4 releases」** Google announced Gemini 4 Carbon on November 10, 2026, describing it as its strongest model for cybersecurity work and long-horizon agentic workflows. A Reddit discussion surfaced in search results placed the then-upcoming Gemini 4 Neon between Carbon and Hydrogen in capability, framing Neon as part of a multi-tier Gemini 4 lineup rather than a replacement for Carbon.

**「Impact」** Developers comparing Gemini variants will need task-specific evaluations rather than name-based assumptions: commenter declanjackson reports that Neon scores higher overall on the AA Index while Carbon remains positioned for long-horizon work and scores higher on CritPt research-reasoning evals.

**「Community discussion」** The most substantive disagreement was about whether benchmark leadership translates into practical quality: impulser\_ said Gemini models still feel less capable than Anthropic&\#x27;s Opus 5.5 in general use despite comparable benchmark scores, while stillpointlab described fatigue with the pace of new model names and said the industry has not settled on a stable naming scheme. Commenters also struggled to map names such as Neon, Carbon, Sol, Astra, and Opus to specific use cases.

<details><summary>References</summary>
<ul>
<li>Gemini 4 Carbon is now available - Google Blog</li>
<li>Gemini 4 Neon coming today, it sits right between Carbon and ... - Reddit</li>

</ul>
</details>

**Tags**: `#Gemini 4`, `#large language models`, `#Google`, `#AI model releases`, `#model naming`

---

<a id="item-tech-news-2"></a>
### [Nginx patches 10 CVEs tied to unauthenticated NGINX2Root chain](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) ⭐️ 8.0/10

Xint disclosed NGINX2Root, a chain of five Nginx vulnerabilities plus a Linux kernel flaw that it says can take an unauthenticated Nginx visitor to host root; the cited HTTP/2 bug, CVE-2026-123007, is described as flow-control memory corruption that allows command execution inside an Nginx worker without authentication. Nginx 1.30.7 and 1.31.9 fix 10 CVEs as of November 18, and the item also references CVE-2026-123633. Rapid7 has published a proof-of-concept exploit, while the report says there is no known in-the-wild exploitation; administrators who cannot upgrade are advised to disable externally exposed HTTP/2.

hackernews · speedping · Nov 18, 15:19 · [Discussion](https://news.ycombinator.com/item?id=50547374)

**「Background」** HTTP/2 uses flow-control windows to limit how much data each stream may send; CVE-2026-123007 is an integer underflow \(CWE-191\) in NGINX&\#x27;s accounting for that mechanism, which permits an invalid memory copy and memory corruption in the worker process. Rapid7 rates the flaw 9.2 \(critical\), and Ubuntu&\#x27;s advisory notes the exposure is in NGINX&\#x27;s data plane rather than its control plane.

**「Upgrade or disable HTTP/2」** Any server running an affected NGINX release with HTTP/2 enabled is exposed to unauthenticated code execution in the worker process, and the vulnerable code dates back to 1.9.5 through 1.31.8. Operators should upgrade to 1.30.7 or 1.31.9; where that is not immediately possible, disabling HTTP/2 removes the exposed path at the cost of HTTP/2 throughput and compatibility.

**「Community discussion」** Commenters focused on disclosure timing and exposure: black3r said the fix appeared in the open-source repository a week earlier and argued a public warning was warranted because disabling HTTP/2 is a simple workaround. fduran noted that HTTP/2 is not enabled by default in Nginx and cited W3Techs&\#x27; 12% server share, while aftbit flagged the Linux SCTP local-privilege-escalation bug used in the chain as an additional, apparently still-unassigned concern.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed/">Rapid7 discloses a critical vulnerability affecting NGINX HTTP / 2 that...</a></li>
<li><a href="https://ubuntu.com/security/CVE-2026-123007">CVE - 2026 - 123007 | Ubuntu</a></li>
<li><a href="https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html">10-Year-Old NGINX HTTP / 2 Flaw Lets Unauthenticated Attackers...</a></li>
<li><a href="https://www.ox.security/blog/nginx2root-five-critical-nginx-flaws-expose-web-servers-to-remote-code-execution/">NGINX 2 Root: 5 Critical NGINX RCE Vulnerabilities ... | OX Security</a></li>
<li><a href="https://www.getastra.com/blog/security-advisory/nginx2root/">nginx 2 root: Five nginx RCE Flaws and a Kernel Bug...</a></li>

</ul>
</details>

**Tags**: `#nginx`, `#security`, `#remote-code-execution`, `#http2`, `#vulnerability`

---

<a id="item-tech-news-3"></a>
### [Quad9&\#x27;s France exit and the case against DNS piracy blocking](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

Quad9 has withdrawn from France, and the article uses that exit to argue that DNS resolvers are the wrong place to enforce piracy blocking. The argument is aimed at policymakers and resolver operators: DNS-level orders make public resolution infrastructure a censorship chokepoint without directly addressing infringement. It is a policy analysis of the French action, not a report of a new blocking technology or measurement.

hackernews · ritzaco · Nov 18, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50545958)

**「Background」** DNS resolvers map domain names to IP addresses, so a legal order to block a domain makes the resolver itself the enforcement point. Before this article, copyright orders from a French court led Quad9 to withdraw its privacy-protective DNS service from France; Quad9 said it would stop serving French users on November 24, 2026, citing the ruling, about 20 other pending cases, and a matter of principle.

**「Impact」** For French users who relied on Quad9, the immediate consequence is losing a public resolver option and having to choose another DNS provider; for resolver operators, the case is a warning that national blocking orders can force a choice between compliance and withdrawal.

**「Community discussion」** Commenters largely doubted DNS blocking as an anti-piracy tool: one called non-prosecution enforcement a backdoor to suppressing speech, and another argued legal access remains more cumbersome than piracy. A separate comment asked whether responsibility lies with the French court&\#x27;s interpretation or with the lawmakers who wrote the law.

<details><summary>References</summary>
<ul>
<li>Copyright orders from a French court have led Quad9 to withdraw its ...</li>
<li>Quad9 Leaves France: Public DNS Resolvers vs Piracy Blocking Orders</li>

</ul>
</details>

**Tags**: `#DNS`, `#internet policy`, `#censorship`, `#Quad9`, `#piracy`

---

<a id="item-tech-news-4"></a>
### [Google DeepMind makes Genie 4 available to AI Ultra subscribers](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) ⭐️ 7.0/10

Google DeepMind announced that Genie 4, the latest version of its generative world model, is now available to eligible Google AI Ultra subscribers. The supplied announcement provides few technical details about the model&\#x27;s capabilities or how it differs from earlier versions. It also leaves unclear which countries and account types qualify for access.

hackernews · leumon · Nov 18, 18:49 · [Discussion](https://news.ycombinator.com/item?id=50550415)

**「Earlier limited rollout」** Google DeepMind announced Genie 4 on Oct. 27, 2026, saying it had begun a limited rollout to trusted testers and planned access through Project Genie, the Gemini API, and AI Studio. Project Genie is the subscriber-facing experience for using the Genie 4 world model; the latest update opens it to eligible Google AI Ultra subscribers, with AI Pro users placed on a waitlist.

**「Access and readiness constraints」** Access runs through Project Genie in the browser and is limited to eligible Google AI Ultra subscribers, so prospective users should confirm regional and account eligibility before paying for a tier — one commenter reported that their UK workspace account could not obtain Ultra and that their personal account&\#x27;s Ultra offer still listed Genie 3. Google also describes Genie 3 and Genie 4 as frontier research world models and lists unresolved camera latency, physical-interaction, audio-precision and scene-permanence problems, so teams should not yet plan production game-engine pipelines around it.

**「Community discussion」** Commenters focused heavily on access and pricing: one said their Workspace account could not obtain an Ultra subscription and that their personal account still advertised Genie 3, leaving them unsure whether UK availability was the issue. Others debated whether generative world models could eventually serve as game engines, with one wondering whether Google would allow recreations of games such as GTA, while another argued the discussion paid too little attention to potential negative consequences.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/">Project Genie update featuring Genie 4 - The Keyword</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/">We’re announcing Genie 4, our new world model for real-time ...</a></li>
<li><a href="https://thenextweb.com/news/google-genie-4-project-genie-ai-ultra-world-model">Google opens its Genie 4 world model to AI Ultra subscribers</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/">Project Genie update featuring Genie 4</a></li>
<li><a href="https://www.youtube.com/watch?v=EDp4IoAUsXY">Introducing the new Project Genie, powered by Genie 4 - YouTube</a></li>

</ul>
</details>

**Tags**: `#Google DeepMind`, `#generative world models`, `#AI research`, `#game engines`, `#product availability`

---

<a id="item-tech-news-5"></a>
### [Microsoft announces seven AI models at Ignite 2026](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 7.0/10

Microsoft announced seven new AI models at Ignite 2026, positioning them around scalable price-performance. The available material does not include benchmark details, per-model pricing, or independent validation, so the performance and cost claims remain vendor positioning rather than measured results.

hackernews · gmays · Nov 18, 16:08 · [Discussion](https://news.ycombinator.com/item?id=50548021)

**「Background」** Microsoft Ignite is the company&\#x27;s annual enterprise IT and developer conference, the venue for this seven-model announcement. The thread&\#x27;s main hands-on reference point is MAI Code 2, which one commenter says they have been testing for their usual work and found roughly on par with Opus- and Sol-class models.

**「What buyers should verify」** Teams selecting models for coding and vulnerability-discovery work now have a Microsoft option pitched at a fraction of incumbent per-task cost: Microsoft claims MAI Cyber 2 Flash matches GPT-6 Astra&\#x27;s quality at under 2% of the cost per task on its CyberGymE 2 benchmark, and ForkLog reports the lineup targets performance comparable to Claude and GPT at significantly lower cost. Because that comparison is Microsoft&\#x27;s own benchmark figure rather than an independent measurement, buyers should re-run it on their own repositories and security workloads before shifting spend.

**「Community discussion」** One commenter who tested MAI Code 2 called it “quite good” for their usual work and broadly comparable to Opus or Sol, while another argued Microsoft should release some models as open source or open weight to secure market share, warning of a Windows Phone outcome. A third dismissed the keynote as shallow and lacking innovation.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/microsoft-ignite-2026/">Seven new world class models at scalable... | Microsoft AI</a></li>
<li><a href="https://forklog.com/en/microsoft-unveils-ai-models-for-coding-and-cybersecurity/">Microsoft unveils AI models for coding and cybersecurity | ForkLog</a></li>

</ul>
</details>

**Tags**: `#Microsoft AI`, `#model releases`, `#price-performance`, `#AI coding tools`, `#Hacker News discussion`

---

<a id="item-tech-news-6"></a>
### [Stenberg: AI Rust rewrites of curl lag real project&\#x27;s bugfixes](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

curl lead maintainer Daniel Stenberg reported that while AI agents converted 185,000 lines of curl&\#x27;s C code into 340,000 lines of Rust over a little more than three weeks, the actual curl project merged over 300 commits in the same period, including a little over 200 bugfixes and a few vulnerability fixes. He noted that none of the Rust rewrites contain those 200 bugfixes, and asked whether the AI-generated clones can keep up as the real project lands roughly another 200 fixes per month. The figures are Stenberg&\#x27;s own counts, and the excerpt does not identify which agents or which specific Rust rewrite projects he is referring to.

rss · Simon Willison · Nov 18, 15:58

**「Context」** The quoted passage comes from Daniel Stenberg&\#x27;s November 17, 2026 post, “Actual curl rewrites in Rust,” published a day before this excerpt. In that post Stenberg, the curl maintainer, documented the agent-driven conversion of curl&\#x27;s C code into Rust as a separate rewrite effort, which is the comparison point for his question about whether such ports can track the canonical project&\#x27;s fixes.

**「Impact」** Anyone evaluating or shipping an AI-generated curl port should treat it as a fork that starts out missing upstream&\#x27;s recent bug and security fixes, and should plan to track and re-apply curl&\#x27;s ongoing commits rather than assume the generated code stays current.

<details><summary>References</summary>
<ul>
<li><a href="https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/">Actual curl rewrites in rust | daniel .haxx.se</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#open source maintenance`, `#curl`, `#Rust`, `#security`

---

<a id="item-tech-news-7"></a>
### [Reported Java4Shell RCE Affects Java 17/21/25/27](https://censys.com/advisory/cve-2026-114938/) ⭐️ 7.0/10

A Telegram post reports CVE-2026-114938, a CVSS 4.0 9.2 unauthenticated remote code execution flaw in Java that it says went unnoticed for nearly four years. The post lists Java 17.0.6 and later within the 17 line, plus Java 21, 25, and 27; standard Java 8/11 is usually unaffected, except Oracle Java 8 Performance Pack. It limits exposure to x86-64 processors with AVX-512 VBMI—roughly 2021-and-later Intel Ice Lake/newer Xeon and 2022-and-later AMD Zen 4/newer EPYC/Ryzen—and says ARM64 is unaffected. The post provides no exploit mechanism, patch status, or mitigation details, and the claim has not been independently confirmed in the supplied material.

telegram · zaihuapd · Nov 18, 03:55

**「Background」** OpenJDK published a vulnerability advisory dated 2026/11/17 listing source-code vulnerabilities fixed in that release, and Censys&\#x27;s initial write-up identified CVE-2026-114938 as a remotely exploitable memory-corruption flaw in OpenJDK nicknamed “Java4Shell” \(\[tool-1-1\], \[tool-1-3\]\). Censys later said it had updated its advisory with a detailed list of affected components, so the Telegram post reflects an evolving advisory response rather than a fully independent exploit analysis \(\[tool-1-2\]\).

**「Impact」** Organizations running the listed JDK lines on AVX-512 VBMI x86-64 hosts should inventory those instances and seek vendor guidance or patches, since the post itself supplies neither; standard Java 8/11 deployments are largely out of scope except Oracle Java 8 Performance Pack.

<details><summary>References</summary>
<ul>
<li>Nov 17 Advisory: OpenJDK Remote Code Execution (Java4Shell) [CVE ...</li>
<li>Censys on X: &quot; Rapid Response Update</li>
<li>2026/11/17 - OpenJDK Vulnerability Advisory</li>

</ul>
</details>

**Tags**: `#Java`, `#security vulnerability`, `#remote code execution`, `#CVE`, `#AVX-512`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [FlyDSL MonoKernels Cut Interactive LLM Decode Latency in vLLM](https://vllm.ai/blog/2026-11-18-flydsl-monokernels) ⭐️ 8.0/10

rss · vLLM Blog · Nov 18, 00:00

**「Background」** Interactive agents need each decode step to finish before the next tool call, so at low concurrency per-user latency matters more than aggregate throughput. A decode step still runs a chain of small dependent GPU kernels whose launch, startup, drain, and serialization costs can dominate at small batch sizes; HIP graphs remove CPU launch overhead but not these GPU-side costs.

**「Solution」** The authors describe FlyDSL MonoKernels: persistent launches that keep a fixed grid of thread blocks alive across several dependent stages. Blocks take ready work from the next stage, prefetch later weights during earlier computation, and pass intermediate tiles through tagged mailboxes so consumers start when their inputs are ready; tensor-parallel all-reduces can also run inside the kernel. Boundaries are deliberately model-specific—DeepSeek-V4.1-Flash uses K1/K2 across the decoder layer, while MiniMax-M3 initially fuses only the FFN—because over-fusing can outrun dependencies or GPU resources. vLLM treats the result as an opt-in specialized decode behind --monokernel: model-owned code, stock fallback per layer and step, unchanged HIP graphs and speculative decoding. Reported gains include DeepSeek-V4.1-Flash rising from 318.1 to 429.1 tok/s/user at concurrency 1 on TP2 MI355X, and a standard decoder layer on the MI300X/MI325X port falling from 32 kernels in 320 µs to 2 kernels in 115 µs; GLM-5.2 drops from about 2,459 to 210 kernels and from 13.70 to 5.92 ms per token at batch 1. Accuracy differences were reported within noise for tested configurations, though the DeepSeek-V4-Pro baseline includes historical stack changes. Limits include smaller gains at higher concurrency, capped step widths, and duplicate weights on MI300X/MI325X.

**「Takeaway」** The authors argue that the payoff comes from model-specific persistent scheduling, not a universal one-kernel template: MonoKernels materially improve low-concurrency interactivity while remaining an opt-in specialized path rather than a throughput cure.

**Tags**: `#LLM inference`, `#decode latency`, `#MonoKernels`, `#FlyDSL`, `#ROCm`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Fed minutes signal further rate hikes and flag AI inflation risk](https://www.cnbc.com/2026/11/18/fed-minutes-october-2026.html) ⭐️ 9.0/10

Federal Reserve meeting minutes released Wednesday showed almost all officials judged further rate increases would likely be appropriate to bring inflation back to 2%, while the rate-setting Federal Open Market Committee voted 10-2 to hold its benchmark rate at 3.75%-4%, with both dissents favoring a quarter-point hike. The minutes also said artificial-intelligence-related demand was a material inflation risk and that rapid AI-related debt growth through complex, opaque financing could amplify losses if AI investment returns disappoint.

rss · CNBC Finance · Nov 18, 19:41

**「Background」** The Fed&\#x27;s stated goal is 2% inflation, and at its October 27-28 meeting officials weighed whether price pressures tied to the Iran war and President Donald Trump&\#x27;s tariffs are temporary shocks or are becoming entrenched in the economy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20261028.pdf">Minutes of the Federal Open Market Committee October 27-28, 2026</a></li>

</ul>
</details>

**Tags**: `#Federal Reserve`, `#monetary policy`, `#inflation`, `#interest rates`, `#AI risk`

---

<a id="item-finance-news-2"></a>
### [Fed’s Waller floats half-point December rate hike](https://www.cnbc.com/2026/11/18/federal-reserve-governor-christopher-waller.html) ⭐️ 7.0/10

Federal Reserve Governor Christopher Waller said the central bank may need a half-point rate increase at the Dec. 8-9 FOMC meeting to “shock people” and fight inflation that is running above his expectations.

rss · CNBC Finance · Nov 18, 15:13

**「Background」** The FOMC raised rates in September for the first time in more than three years and held steady in October, while most inflation readings remained above 3% versus the Fed’s 2% target after energy prices spiked.

**「Impact」** A half-point increase would raise borrowing costs for households and businesses more sharply than the quarter-point December move that futures markets are fully pricing.

**Tags**: `#monetary policy`, `#Federal Reserve`, `#interest rates`, `#inflation`, `#FOMC`

---

<a id="item-finance-news-3"></a>
### [Banks Pause $480 Million ByteDance GPU Loan After New US Chip Rules](https://www.bloomberg.com/news/articles/2026-11-17/banks-pause-480-million-chip-loan-tied-to-china-s-bytedance) ⭐️ 7.0/10

Five banks paused a $480 million loan intended to fund ByteDance&\#x27;s purchase of Nvidia GPUs for a Malaysia data center after new US AI chip rules raised compliance concerns; the borrower is Singapore cloud provider Aolani Cloud, with DBS Group as lead arranger.

telegram · zaihuapd · Nov 18, 05:11

**「Background」** The $480 million facility was a syndicated loan—money pooled from several banks—with Singapore cloud provider Aolani Cloud as borrower and DBS as lead arranger, intended to buy Nvidia chips for a ByteDance data center in Malaysia; the new US AI-chip export rules were announced on Monday.

**「Impact」** The pause leaves ByteDance&\#x27;s planned GPU purchase for the Malaysia data center without the intended loan funding while the banks assess whether the deal complies with the new rules.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/NVDA/bytedance-480m-loan-stalled-after-us-tightens-ai-chip-export-rules-25700410">ByteDance $480M Loan Stalled After US Tightens AI Chip Export ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-17/banks-pause-480-million-chip-loan-tied-to-china-s-bytedance">Banks Pause $480 Million Chip Loan Tied to China’s ByteDance</a></li>

</ul>
</details>

**Tags**: `#US chip export controls`, `#ByteDance`, `#GPU financing`, `#bank lending`, `#AI chips`

---

<a id="item-finance-news-4"></a>
### [UK Immigration and Asylum Bill passes House of Commons](https://www.bloomberg.com/news/articles/2026-11-17/uk-s-house-of-commons-passes-controversial-immigration-bill) ⭐️ 7.0/10

The UK House of Commons passed the Immigration and Asylum Bill by 290 votes to 94, sending it to the House of Lords for further scrutiny. The bill would speed removals of people denied asylum, extend the standard residency requirement for settlement from five to 10 years, and tighten care-visa routes, while some health and social care visa holders earning at least £25,000 a year could still apply after five years.

telegram · zaihuapd · Nov 18, 05:51

**「Background」** The bill had already passed its Commons second reading in July 2026, and this latest Commons approval sends it to the House of Lords for further scrutiny before it can become law.

**「Impact」** Overseas health and social care staff are directly affected: only those on qualifying visas earning at least £25,000 keep the five-year route to settlement, while most other migrants now face a 10-year wait, a difference that matters to care employers who recruit abroad.

<details><summary>References</summary>
<ul>
<li><a href="https://www.valerievazmp.co.uk/immigration-and-asylum-bill-second-reading/">Immigration and Asylum Bill (Second Reading) - Valerie Vaz MP</a></li>
<li><a href="https://hansard.parliament.uk/commons/2026-11-17/debates/710E2102-AD6B-4646-8BAE-087AC69569D3/ImmigrationAndAsylumBill">Immigration and Asylum Bill - Hansard - UK Parliament</a></li>

</ul>
</details>

**Tags**: `#UK immigration policy`, `#asylum reform`, `#health and social care visas`, `#labour market`, `#House of Commons`

---

<a id="item-finance-news-5"></a>
### [Tencent Q3 2026: AI capex jumps, free cash flow negative](https://api3.cls.cn/share/article/2537922?os=android&amp;amp;sv=8.8.5&amp;amp;app=cailianpress&amp;amp;selected=) ⭐️ 7.0/10

Tencent&\#x27;s Q3 2026 revenue rose 8% year on year to RMB 207.3 billion, below market expectations, while capital spending jumped to RMB 81.4 billion against an estimated RMB 55.4 billion and free cash flow was negative RMB 69.1 billion. Tencent said WorkBuddy had the highest daily token usage among domestic large-language-model products, exceeding 100 trillion tokens a day, and reported net profit attributable to shareholders up 0.8% to RMB 63.6 billion.

telegram · zaihuapd · Nov 18, 09:20

**「Background」** WorkBuddy, the product behind the token-usage claim, was launched in March 2026 and had surpassed 10 million daily active users by early November, according to earnings coverage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/tencent-workbuddy-hits-10m-daily-active-users-100-trillion-daily-token-usage">Tencent WorkBuddy reaches 10 million daily active ... - KuCoin</a></li>
<li><a href="https://todayforai.com/en/items/art-829728b4-a1a">Tencent WorkBuddy Tops 10M Daily Users With 100 Trillion ...</a></li>
<li><a href="https://finance.sina.com.cn/tech/digi/2026-11-18/doc-inizeacc1577026.shtml">腾讯 WorkBuddy 日活跃用户数超 1000 万，成为中国大语言模型日均 Tok...</a></li>

</ul>
</details>

**Tags**: `#Tencent earnings`, `#AI capex`, `#free cash flow`, `#China tech`, `#token usage`

---