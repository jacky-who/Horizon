---
layout: default
title: "Horizon Summary: 2026-11-19 (EN)"
date: 2026-11-19
lang: en
---

> From 42 items, 13 important content pieces were selected

---

**Technology News**
1. [Google launches Gemini 4 Neon with 1M context and $3 input pricing](#item-tech-news-1) ⭐️ 9.0/10
2. [Wiz reports unauthenticated RCE in Nginx HTTP/2](#item-tech-news-2) ⭐️ 8.0/10
3. [Xint discloses nginx-to-root chain, fixes in 1.30.7/1.31.9](#item-tech-news-3) ⭐️ 8.0/10
4. [Microsoft announces seven AI models focused on price-performance](#item-tech-news-4) ⭐️ 7.0/10
5. [Quad9&\#x27;s France exit and the case against DNS piracy blocking](#item-tech-news-5) ⭐️ 7.0/10
6. [Google DeepMind makes Genie 4 available to eligible AI Ultra subscribers](#item-tech-news-6) ⭐️ 7.0/10
7. [Interactive Voyager 1 explainer goes down to a single memory chip](#item-tech-news-7) ⭐️ 7.0/10
8. [curl maintainer: AI Rust rewrites lag upstream bugfixes](#item-tech-news-8) ⭐️ 7.0/10
9. [US Weighs Public Disclosure of Chinese AI Model Use](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [Fed Minutes Point to More Rate Hikes and AI Inflation Risk](#item-finance-news-1) ⭐️ 8.0/10
2. [Waller Floats Half-Point Fed Rate Hike in December](#item-finance-news-2) ⭐️ 8.0/10
3. [Tencent Q3 2026 revenue misses as AI capex climbs](#item-finance-news-3) ⭐️ 8.0/10
4. [中韩宣布自贸协定服务投资后续谈判实质性结束](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Google launches Gemini 4 Neon with 1M context and $3 input pricing](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) ⭐️ 9.0/10

Google announced Gemini 4 Neon, a new model aimed at fast end-to-end work in complex software engineering, knowledge work, and research, and said it is available to developers, enterprises, and Google AI Pro/Ultra subscribers. Google lists pricing at $3 per million input tokens, $0.15 per million cached input tokens, and $15 per million output tokens, with a 1 million-token context window. The company claims Neon ranks first on Artificial Analysis&\#x27;s coding-agent index at 58.6, third overall on its intelligence index at the xhigh setting with 61, and scores 65.2% on Terminal-Bench 4.1; Google also says its default high setting cuts per-task cost 32% versus Carbon.

hackernews · yigitdemirag · Nov 18, 21:34 · [Discussion](https://news.ycombinator.com/item?id=50552424)

**「Model family context」** Gemini 4 Neon belongs to Google&\#x27;s Gemini 4 generation, with &quot;Neon&quot; serving as a variant name within that model line rather than a separate product family. The source compares Neon&\#x27;s default high-tier cost with Carbon, indicating that Google is positioning it against an existing Gemini variant used as the pricing baseline.

**「Token spend may offset savings」** Developers can use Gemini 4 Neon through Google AI Pro/Ultra or enterprise access at $3 per million input tokens and $15 per million output tokens, with a 1-million-token context window; Google reports 32% lower per-task cost than Carbon at its default high setting. Artificial Analysis measured 283 million tokens generated for Neon&\#x27;s Intelligence Index run versus a 65.1 million median, so teams should track actual token consumption rather than assume the lower per-token price alone reduces agent costs.

**「Community Discussion」** Hacker News commenters complained about having to map a growing set of model names—including Neon, Carbon, Sol, Astra, Opus, and Haiku—to specific use cases. One commenter said Argon was removed from the Gemini app in favor of Neon, while another argued that Carbon remains positioned as the long-horizon model despite Neon&\#x27;s higher overall score, citing lower Neon results on research-scale evaluations such as CritPt.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">Introducing Gemini 4 Neon</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-4-neon">Gemini 4 Neon Models - Intelligence... | Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#Gemini 4`, `#Google AI`, `#LLM release`, `#AI models`, `#Hacker News`

---

<a id="item-tech-news-2"></a>
### [Wiz reports unauthenticated RCE in Nginx HTTP/2](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) ⭐️ 8.0/10

A Wiz blog post describes unauthenticated remote code execution vulnerabilities in Nginx&\#x27;s HTTP/2 handling, tracked as CVE-2026-123633 and CVE-2026-123007. The material supplied here consists of those two CVE identifiers and the post&\#x27;s title, with no affected version ranges, fixed releases, or exploit prerequisites, so the practical exposure of any specific deployment cannot be judged from this excerpt alone. The CVE records remain the place to confirm affected builds and available fixes. Commenters stressed that HTTP/2 is not enabled by default in Nginx, which would confine the affected population to servers that turned the protocol on.

hackernews · speedping · Nov 18, 15:19 · [Discussion](https://news.ycombinator.com/item?id=50547374)

**「Background」** For CVE-2026-123007, Xint.io lists all official nginx releases from 1.9.5 through 1.31.8 as containing the vulnerable code, and says it was still present in master as of November 10, 2026. The HTTP/2-specific flaws matter only where HTTP/2 is enabled, which is not the default in NGINX.

**「Mitigation gap」** Operators running NGINX with HTTP/2 enabled—especially configurations that forward requests to an upstream server—remain exposed even when their application code is secure. The practical workaround is to set \`http2 off;\` in each affected server block and remove \`http2\` from \`listen\` directives on NGINX 1.25.1 and later; that blocks CVE-2026-123007 and CVE-2026-123633 but not the three other NGINX flaws, and HTTP/3 must also be disabled where used to remove the path for CVE-2026-121810.

**「Community Discussion」** Commenters disputed the severity: one argued that exploitation needs roughly 128 GB of HTTP/2 traffic plus specific CPU instructions and called it &quot;a non issue,&quot; while another noted HTTP/2 is off by default and, citing W3Techs, used by about 12% of servers. Others criticized disclosure timing, saying the fix appeared in the open-source repository about a week before the advisory and that a plain warning was warranted given how simple the workaround of disabling HTTP/2 is.

<details><summary>References</summary>
<ul>
<li><a href="https://xint.io/blog/nginx2root-remote-code-execution">NGINX 2 Root: New Remote Code Execution Vulnerabilities in nginx ...</a></li>
<li><a href="https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities">Unauthenticated Remote Code Execution in NGINX ... | Wiz Blog</a></li>
<li><a href="https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html">10-Year-Old NGINX HTTP / 2 Flaw Lets Unauthenticated Attackers...</a></li>
<li><a href="https://xint.io/blog/nginx2root-remote-code-execution">NGINX 2 Root: New Remote Code Execution Vulnerabilities in nginx ...</a></li>

</ul>
</details>

**Tags**: `#nginx`, `#security`, `#http/2`, `#remote code execution`, `#vulnerability`

---

<a id="item-tech-news-3"></a>
### [Xint discloses nginx-to-root chain, fixes in 1.30.7/1.31.9](https://nginx2root.com/) ⭐️ 8.0/10

Xint has disclosed NGINX2Root, a chain of five nginx vulnerabilities plus a Linux kernel flaw that, according to the disclosure, can let an nginx visitor reach host root. The central issue, identified as CVE-2026-123007, is described as an HTTP/2 flow-control memory-corruption bug that allows unauthenticated command execution in an nginx worker. The fixes are in nginx 1.30.7 and 1.31.9, which address 10 CVEs as of November 18; Rapid7 has published a proof of concept, and the report says there is no known exploitation in the wild. Users who cannot upgrade should disable externally exposed HTTP/2, though the Telegram summary has not been independently verified and the CVE identifier is unusual.

telegram · zaihuapd · Nov 18, 16:21

**「Context: what the flaws are and who is exposed」** HTTP/2 in nginx is enabled per listening socket, so a host is only reachable through the reported flow-control flaw when HTTP/2 is switched on — the source&\#x27;s guidance to disable outward-facing HTTP/2 is therefore a workable stopgap where upgrading is not yet possible. Cycode reports that the five flaws, led by CVE-2026-123007, affect nginx releases from 0.5.33 onward and were fixed in 1.30.7 and 1.31.9, both released on 18 November 2026. They are memory-safety bugs that let an unauthenticated attacker crash worker processes and, where ASLR is disabled or bypassed, run code as the worker.

**「Upgrade or disable external HTTP/2」** Anyone running nginx with HTTP/2 exposed on an internet-facing listener needs to move to 1.30.7 or 1.31.9, the 18 November 2026 releases that carry the fixes for all five flaws, because the entry point is unauthenticated and the chain ends at host root. Where upgrading is not immediately possible, the stated interim mitigation is to turn off HTTP/2 on externally reachable listeners, which removes the worker-level RCE path. Rapid7&\#x27;s published PoC lowers the effort needed to reproduce the chain, although the source reports no in-the-wild exploitation so far.

<details><summary>References</summary>
<ul>
<li><a href="https://cycode.com/blog/nginx2root-cve-2026-123007/">NGINX2Root (CVE-2026-123007): Affected Versions, How to Check ...</a></li>
<li><a href="https://computingforgeeks.com/nginx-cve-2026-123007/">nginx CVE-2026-123007: Check, Disable HTTP/2, Patch ...</a></li>
<li>nginx2root: five nginx use-after-free and HTTP/2 flow-control bugs give ...</li>

</ul>
</details>

**Tags**: `#nginx`, `#security vulnerabilities`, `#HTTP/2`, `#remote code execution`, `#Linux kernel`

---

<a id="item-tech-news-4"></a>
### [Microsoft announces seven AI models focused on price-performance](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 7.0/10

Microsoft announced seven new AI models at Ignite 2026, positioning them around scalable price-performance for developers and businesses. The available material identifies the MAI Code 2 coding model but gives little technical detail, exact pricing, or independent benchmarks, so claims that it is on par with Anthropic&\#x27;s Opus or OpenAI&\#x27;s Sol are unverified. The announcement also does not establish whether any of the models will be open-weight.

hackernews · gmays · Nov 18, 16:08 · [Discussion](https://news.ycombinator.com/item?id=50548021)

**「Context」** Microsoft&\#x27;s MAI line is its first-party family of AI models, and MAI Code 2 is the coding-focused member that commenters in this thread tested. Ignite serves as the venue for presenting that lineup to enterprise developers, while the comparisons to Anthropic&\#x27;s Opus and OpenAI&\#x27;s Sol remain user impressions and vendor positioning rather than independently verified benchmarks.

**「Cheaper coding-model option to benchmark」** For teams paying per task on coding workloads, Microsoft&\#x27;s claimed price-quality ratios — MAI Code 2 at 98% of GPT-6.1 Sol&\#x27;s coding quality for about 40% of the price, and 96% of Opus 5.5&\#x27;s performance for roughly 5% of the price — make it worth running against current providers on internal evaluations. Those figures are Microsoft&\#x27;s own benchmark comparisons rather than independent measurements, so the practical consequence depends on whether the same cost advantage holds on a team&\#x27;s own tasks.

**「Community discussion」** In the Hacker News thread, a commenter who tested MAI Code 2 said it was “quite good” for their usual work and did not strongly dispute the comparison to Opus or Sol, while another argued Microsoft needs open-source or open-weight releases to gain market share. A separate commenter dismissed the Ignite keynote as shallow and low on innovation.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/microsoft-ignite-2026/">Seven new world-class models at scalable price-performance ...</a></li>
<li><a href="https://www.orcarouter.ai/blog/mai-code-2-ignite-seven-models">Seven MAI Models at Ignite 2026: Where MAI Code 2 Fits In</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#AI models`, `#MAI Code 2`, `#model pricing`, `#open weights`

---

<a id="item-tech-news-5"></a>
### [Quad9&\#x27;s France exit and the case against DNS piracy blocking](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

An analysis argues that DNS resolvers are the wrong enforcement point for piracy blocking, using Quad9&\#x27;s withdrawal from France as its case study. The piece frames DNS-level blocking as a shortcut that puts infrastructure providers in the position of policing content rather than addressing piracy directly. It is an opinion/analysis, not a report of a new technical capability or an independently measured enforcement result.

hackernews · ritzaco · Nov 18, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50545958)

**「Background: the French order behind Quad9&\#x27;s exit」** DNS resolvers translate domain names into IP addresses, which is why rights holders and courts have tried to use them as a choke point for blocking piracy sites — an approach critics say is coarse, centralized, and easy to repurpose for other kinds of blocking. The specific trigger here is a French court order requiring Quad9, a free privacy-focused resolver, to block copyright-infringing sites; Quad9 responded by announcing it would stop serving users in France as of November 24, 2026, a withdrawal reported in late October 2026. The article builds its argument on that episode, using Quad9&\#x27;s exit as evidence that resolver-level enforcement pushes legitimate infrastructure providers out rather than reducing infringement.

**「Community Discussion」** trentnix described every anti-piracy effort short of prosecuting pirates as a censorship backdoor, while bemttevi argued that legal access must be easier and said they would pay $2–5 for DRM-free movie downloads. skrebbel asked whether the French outcome reflects judges misapplying a reasonable law or judges correctly applying a bad one.

<details><summary>References</summary>
<ul>
<li>French Court&#x27;s Site-Blocking Orders Drive Quad9 Out Of France</li>
<li>Copyright orders from a French court have led Quad9 to withdraw its ...</li>

</ul>
</details>

**Tags**: `#DNS`, `#internet censorship`, `#internet policy`, `#Quad9`, `#piracy`

---

<a id="item-tech-news-6"></a>
### [Google DeepMind makes Genie 4 available to eligible AI Ultra subscribers](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) ⭐️ 7.0/10

Google DeepMind announced that Genie 4, a generative world model, is now available to eligible Google AI Ultra subscribers. The announcement as provided did not include technical details on the model&\#x27;s capabilities, changes from earlier versions, or specific regional availability. In the discussion, commenters reported that the Ultra subscription page still showed Genie 3 and that a UK-based user could not determine whether they qualified.

hackernews · leumon · Nov 18, 18:49 · [Discussion](https://news.ycombinator.com/item?id=50550415)

**「Background」** Project Genie is Google DeepMind’s browser-based prototype for building and editing interactive worlds; the new rollout brings Genie 4 into that experience for eligible Google AI Ultra subscribers. Coverage of the launch treats Genie 4 as the successor to Genie 3 in Project Genie, with comparisons focused on editable worlds and audio.

**「Impact」** Prospective users face unclear eligibility: a UK-based commenter could not tell whether Genie 4 is available in their region, and a workspace account holder reported being unable to obtain an Ultra subscription. Those affected may need to confirm account type and region before expecting access.

**「Community Discussion」** Commenters split between practical access complaints and broader unease. One long-time reader said the discussion focused too much on pricing and capability and too little on negative consequences, stating &quot;I don&\#x27;t want any of this,&quot; while another praised DeepMind&\#x27;s craft and questioned how the work could become profitable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unite.ai/google-brings-genie-4-to-project-genie-for-eligible-ai-ultra-users/">Google Brings Genie 4 to Project Genie for Eligible AI Ultra ...</a></li>
<li><a href="https://www.online-tech-tips.com/google-genie-4-access-ai-ultra/">Google opens Genie 4 access to eligible AI Ultra subscribers</a></li>

</ul>
</details>

**Tags**: `#generative world models`, `#Google DeepMind`, `#AI product availability`, `#game engines`, `#AI subscriptions`

---

<a id="item-tech-news-7"></a>
### [Interactive Voyager 1 explainer goes down to a single memory chip](https://rshekhar.com/voyager/) ⭐️ 7.0/10

Raj Shekhar&\#x27;s Show HN project is an interactive dissection of Voyager 1 that goes from spacecraft subsystems down to a single bit of the command computer&\#x27;s memory; direct links cover the RTG&\#x27;s 24 plutonium spheres, the data computer&\#x27;s memory chips, and the Golden Record cover. The site also shows both Voyagers&\#x27; current positions, a radio-based repair sequence, and which Earth dish is listening live. The post marks the occasion as Voyager 1 reaching one light-day from Earth; the project itself is an educational visualization, not a new mission result.

hackernews · raj-shekhar · Nov 18, 16:18 · [Discussion](https://news.ycombinator.com/item?id=50548161)

**「Background」** Voyager 1, the most distant human-made object, crossed into interstellar space in 2012 after launching in the 1970s. A light-day is the distance light travels in 24 hours, so at this separation a radio signal takes roughly a day to reach the probe and another day for a reply.

**「Community discussion」** Commenters praised the visualization, with one calling the 1970s engineering &quot;pretty wild&quot; and another linking their own Golden Record tribute and image decoder. A separate commenter said it is &quot;missing some things&quot; and asked how a CMOS memory IC could fail consistently, while another asked whether the site was &quot;vibecoded&quot; and checked against authoritative sources; the supplied comments do not include an author response to those questions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Voyager_1">Voyager 1 - Wikipedia</a></li>
<li><a href="https://onelightday-voyager1.space/">One Light Day · Voyager 1</a></li>
<li><a href="https://www.aljazeera.com/news/2026/11/18/nasas-voyager-1-hits-record-one-light-day-distance-50-years-after-launch">NASA’s Voyager 1 hits record one light - day distance, 50... | Al Jazeera</a></li>

</ul>
</details>

**Tags**: `#Voyager 1`, `#interactive visualization`, `#computer hardware`, `#spacecraft systems`, `#Hacker News`

---

<a id="item-tech-news-8"></a>
### [curl maintainer: AI Rust rewrites lag upstream bugfixes](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

curl maintainer Daniel Stenberg reported that AI coding agents converted 185,000 lines of C into 340,000 lines of Rust while the upstream C project merged more than 300 commits in a little over three weeks during the same period. He said those commits included just over 200 bugfixes and several vulnerability fixes that none of the Rust rewrites contain, and that curl added another 200 fixes in the following month. Stenberg&\#x27;s count is a maintainer&\#x27;s comparison of generated ports with ongoing upstream maintenance, not an independent evaluation of the rewrites&\#x27; quality.

rss · Simon Willison · Nov 18, 15:58

**「Context」** curl is a widely used open-source C library and command-line tool for transferring data across network protocols, and its upstream repository is actively maintained by Daniel Stenberg and contributors. The Rust rewrites Stenberg refers to are separate AI-agent-generated ports rather than the official curl project, so upstream bugfixes and security patches do not automatically carry over to them.

**「Impact」** For teams considering an AI-generated curl port, Stenberg&\#x27;s comparison implies a need for ongoing synchronization with upstream: the 200-plus bugfixes and vulnerability fixes he cites landed in the maintained C project, so a generated Rust clone would lack them unless separately patched.

**Tags**: `#curl`, `#Rust`, `#AI coding agents`, `#open source maintenance`, `#security`

---

<a id="item-tech-news-9"></a>
### [US Weighs Public Disclosure of Chinese AI Model Use](https://www.reuters.com/world/china/trump-administration-weighs-forcing-us-firms-disclose-chinese-ai-use-2026-11-18/) ⭐️ 7.0/10

The Trump administration is reportedly considering requiring US companies to publicly disclose their use of Chinese AI models, with the Treasury Department and the White House Office of Science and Technology Policy having discussed the proposal. The reported aim is to discourage reliance on cheaper Chinese open-weight models through public naming rather than by imposing new restrictions. If implemented, companies such as Airbnb, which uses Alibaba&\#x27;s Qwen for customer service, would have to disclose such use on their websites. It remains unclear whether the proposal has internal government support or will enter a formal legislative process.

telegram · zaihuapd · Nov 19, 02:30

**「Background」** Chinese developers such as Alibaba have released open-weight models like Qwen, which businesses can download and run themselves rather than relying only on proprietary hosted models. The reported proposal would not ban those models; it would use public disclosure—such as posting their use on a company website—to discourage adoption. The article cites Airbnb&\#x27;s use of Qwen for customer service as an example of the practices that could be covered.

**「Disclosure burden falls on adopters」** If adopted, the measure would push disclosure obligations onto enterprises rather than model vendors: firms running Chinese open-weight models such as Alibaba&\#x27;s Qwen would need to identify and publish that use, which in practice requires tracking model provenance across fine-tuned and self-hosted deployments that many organizations do not currently inventory. The stakes are heightened because Chinese models have moved from marginal to a large share of US enterprise token traffic on cost grounds, so companies would be asked to publicly flag choices they made primarily for price. The proposal remains under discussion, with no confirmed internal support or legislative path, so enterprises face uncertainty about whether to begin documenting model provenance now or wait for a formal rule.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html">Chinese AI models gain ground with U.S. companies as ... - CNBC</a></li>
<li><a href="https://startupfortune.com/us-companies-now-run-nearly-half-their-ai-traffic-on-chinese-models/">US Companies Now Run Nearly Half Their AI Traffic on Chinese ...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#Chinese AI`, `#open-weight models`, `#US regulation`, `#tech industry`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Fed Minutes Point to More Rate Hikes and AI Inflation Risk](https://www.cnbc.com/2026/11/18/fed-minutes-october-2026.html) ⭐️ 8.0/10

Federal Reserve officials said in minutes released Wednesday that further interest-rate increases will likely be needed to return inflation to 2%. The central bank voted 10-2 to hold its benchmark rate at 3.75%-4%, with two officials dissenting in favor of a quarter-point hike.

rss · CNBC Finance · Nov 18, 19:41

**「Background」** The Federal Open Market Committee — the Fed panel that sets the benchmark federal funds rate — left that rate in a 3.75%–4% range at its Oct. 27–28 meeting as it seeks to bring inflation back to its 2% goal.

**「Impact」** The minutes flag that AI-related debt has grown rapidly through complex, opaque financing and is concentrated among a few firms, which Fed staff said could amplify losses if returns on AI investment disappoint.

<details><summary>References</summary>
<ul>
<li><a href="https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20261028.pdf">Minutes of the Federal Open Market Committee - October 27-28, 2026</a></li>

</ul>
</details>

**Tags**: `#Federal Reserve`, `#monetary policy`, `#inflation`, `#interest rates`, `#AI financing risk`

---

<a id="item-finance-news-2"></a>
### [Waller Floats Half-Point Fed Rate Hike in December](https://www.cnbc.com/2026/11/18/federal-reserve-governor-christopher-waller.html) ⭐️ 8.0/10

Federal Reserve Governor Christopher Waller said Wednesday the central bank may need a half-percentage-point increase in its benchmark interest rate at the Dec. 8-9 meeting to &quot;shock&quot; inflation down, and that it may need to reverse last year&\#x27;s three quarter-point cuts. It is one policymaker&\#x27;s proposal, not an FOMC decision.

rss · CNBC Finance · Nov 18, 15:13

**「Background」** The Fed cut rates three times in 2025, then approved its first rate hike in more than three years in September and held rates steady in October, while inflation remained above its 2% target and most readings above 3%.

**Tags**: `#Federal Reserve`, `#monetary policy`, `#interest rates`, `#inflation`, `#Christopher Waller`

---

<a id="item-finance-news-3"></a>
### [Tencent Q3 2026 revenue misses as AI capex climbs](https://api3.cls.cn/share/article/2537922?os=android&amp;amp;sv=8.8.5&amp;amp;app=cailianpress&amp;amp;selected=) ⭐️ 8.0/10

Tencent&\#x27;s Q3 2026 revenue rose 8% year on year to RMB207.3bn, below market expectations, while net profit edged up 0.8% to RMB63.6bn. Capital expenditure reached RMB81.433bn against an estimated RMB55.4bn, free cash flow was negative RMB69.1bn, and Tencent said WorkBuddy has the highest daily token usage among domestic large-language-model products at over 100 trillion tokens.

telegram · zaihuapd · Nov 18, 09:20

**「Background」** WorkBuddy, launched in March 2026, is Tencent’s AI assistant; token usage counts the units of text its models process, and Tencent attributed growth to demand for WorkBuddy, model services, and GPU rentals.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/tencent-workbuddy-hits-10m-daily-active-users-100-trillion-daily-token-usage">Tencent WorkBuddy reaches 10 million daily active ... - KuCoin</a></li>
<li><a href="https://lookonchain.com/feeds/82880">Tencent&#x27;s WorkBuddy has over 10 million daily active users ...</a></li>

</ul>
</details>

**Tags**: `#Tencent`, `#earnings`, `#AI capex`, `#free cash flow`, `#AI token usage`

---

<a id="item-finance-news-4"></a>
### [中韩宣布自贸协定服务投资后续谈判实质性结束](https://x.com/Jaemyung_Lee/status/2122988472994791476) ⭐️ 7.0/10

中韩两国于11月18日宣布，中韩自贸协定服务与投资后续谈判已实质性结束，中国承诺在电影、游戏等领域给予韩国最惠国待遇，并扩大旅游、法律、建筑、金融等领域开放。双方还同意将视听节目共同制作范围从电影扩至电视剧、动画、综艺和纪录片；该谈判自2018年3月启动，历时8年8个月，部分技术事项仍待工作层面协商。

telegram · zaihuapd · Nov 18, 10:02

**「Background」** These follow-up talks on services and investment under the China–South Korea free trade agreement began in March 2018, so the announced “substantive conclusion” comes after 8 years and 8 months; some technical points are still to be worked out at the working level, and the deal has not yet been signed or brought into force. The pledged most-favored-nation treatment means South Korean films and games would get the same treatment China gives its best foreign trading partners.

**「Who is affected」** Korean film, TV and game companies are the clearest beneficiaries: joint-production eligibility now extends beyond movies to TV dramas, animation, variety shows and documentaries, and most-favoured-nation treatment in film and gaming would put Korean suppliers on the same footing as other foreign entrants — though the deal is not yet signed or in force.

**Tags**: `#中韩自贸协定`, `#服务贸易`, `#投资开放`, `#影视合作`, `#金融开放`

---