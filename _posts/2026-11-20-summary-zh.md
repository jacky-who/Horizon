---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20
lang: zh
---

> 从 38 条内容中筛选出 21 条重要资讯。

---

**科技新闻**
1. [Levent Alpöge 声称证明广义黎曼猜想并附 Lean 形式化](#item-tech-news-1) ⭐️ 9.0/10
2. [陶哲轩谈无外力纳维-斯托克斯奇点与广义黎曼猜想](#item-tech-news-2) ⭐️ 8.0/10
3. [GitHub 仓库声称 Navier–Stokes 有限时间爆破，尚未验证](#item-tech-news-3) ⭐️ 8.0/10
4. [PHP 混合大小写 HTTPS 被指静默降级为明文](#item-tech-news-4) ⭐️ 8.0/10
5. [Meta AI 助手 Muse 被指跨账户泄露私密信息](#item-tech-news-5) ⭐️ 8.0/10
6. [CVE-2026-99312：KVM 漏洞可让虚拟机读取 AMD 主机内存](#item-tech-news-6) ⭐️ 8.0/10
7. [Alessandro Masullo 匆忙发布声称的广义黎曼猜想证明](#item-tech-news-7) ⭐️ 7.0/10
8. [Inkling 2 Mini：循环架构的开放权重 MoE 模型](#item-tech-news-8) ⭐️ 7.0/10
9. [SEC 据报调查英伟达会计处理](#item-tech-news-9) ⭐️ 7.0/10
10. [语言模型重写自身权重引发争议](#item-tech-news-10) ⭐️ 7.0/10
11. [Aaronson 博客讨论 LLM 疑似证明黎曼猜想](#item-tech-news-11) ⭐️ 7.0/10
12. [Signal 发文强调隐私保护，社区聚焦 AI 应用权限](#item-tech-news-12) ⭐️ 7.0/10
13. [Frostbite：公司称 AI 设计并验证交互网 CPU 架构](#item-tech-news-13) ⭐️ 7.0/10
14. [Levent Alpöge 称与 Claude 发现并形式化黎曼猜想证明](#item-tech-news-14) ⭐️ 7.0/10
15. [Gemini 在 Mac 上线可暂停的电脑操作代理](#item-tech-news-15) ⭐️ 7.0/10
16. [英国法庭裁定苹果胜诉，后门令须公开审理](#item-tech-news-16) ⭐️ 7.0/10
17. [美众议院披露近 88 万颗 AI 芯片对华出口获批](#item-tech-news-17) ⭐️ 7.0/10
18. [美收紧芯片出口，印度扩张 AI 算力](#item-tech-news-18) ⭐️ 7.0/10

**科技博客**
1. [vLLM 首日支持循环模型 Inkling 2 Mini](#item-tech-blog-1) ⭐️ 8.0/10
2. [为什么缓存 LLM 输出收效甚微](#item-tech-blog-2) ⭐️ 6.0/10

**财经新闻**
1. [北京拟规定租房正常损耗不得扣减押金](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Levent Alpöge 声称证明广义黎曼猜想并附 Lean 形式化](https://alpo.ge/remark.pdf) ⭐️ 9.0/10

Levent Alpöge 在 alpo.ge 发布 PDF，声称证明了广义黎曼猜想；帖子本身仍是一项声明，尚非经同行评议的定论。社区评论称随附的 Lean 证明约 1.3GB、约 1500 万行，需分成 14 个压缩分片下载。另有评论引用 MIT 的 Andrew Sutherland 检查页面称已进行多项形式化检查（部分用 Claude Code 运行），但该页面注明截至 2026-11-20 22:05 UTC 结果仍在更新、剩余检查尚未完成。

hackernews · iamronaldo · 11月20日 14:16 · [社区讨论](https://news.ycombinator.com/item?id=50574968)

**「背景」** 广义黎曼猜想是黎曼猜想的推广，Scientific American 将其描述为对黎曼最初猜想的巨大扩展。提出此次证明的 Levent Alpöge 是一位土耳其裔美国数论学家，以数论和算术统计方面的工作闻名，曾任哈佛学会初级研究员，后加入 Anthropic 担任技术职员。

**「影响」** 对依赖广义黎曼猜想结论的数论研究者和形式化验证团队而言，当前最直接的影响是验证成本：一份约 1500 万行的 Lean 证明需要分片分发和独立、多路径检查，检查完成前不宜把相关条件性结论当作已获无条件证明。

**「社区讨论」** 评论者一方面引用 MIT 的检查页面称该证明已获多种形式化验证、因而认为没有疑问，另一方面也批评相关标题只用“Anthropic 员工”称呼作者，强调应把功劳归于这位知名数学家本人；还有人贴出所谓纯人类证明的链接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/">Anthropic mathematician claims to prove Riemann hypothesis , most...</a></li>

</ul>
</details>

**标签**: `#Riemann Hypothesis`, `#formal verification`, `#Lean`, `#mathematics`, `#research breakthrough`

---

<a id="item-tech-news-2"></a>
### [陶哲轩谈无外力纳维-斯托克斯奇点与广义黎曼猜想](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 8.0/10

陶哲轩（Terry Tao）于 2026 年 11 月 20 日发表博客文章，同时讨论无外力（unforced）欧拉方程、无外力纳维-斯托克斯方程的奇点问题，以及广义黎曼猜想（GRH）。一位评论者引用陶在文中的说法称，涉及黎曼猜想的论证“似乎动用了朗兰兹纲领与算术几何现代发展的全部力量”，但这一转述无法从现有材料核实。该页面正文未能获取，因此证明的具体构造、是否构成完整证明、以及形式化覆盖到什么范围，均无法确认。评论中另有人称两个独立的 Lean 内核都接受了该结果。

hackernews · archon1410 · 11月20日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=50578358)

**「背景」** 无外力欧拉方程和纳维–斯托克斯方程的“奇点”问题，核心是判断光滑初值下解是否会在有限时间内失去光滑性；广义黎曼猜想则是黎曼猜想向狄利克雷 L 函数等更一般对象推广后的版本。Tao 的这篇 11 月 20 日博文称，Levent Alpöge、Tristan Buckmaster 和 Matei Coiculescu 在大量 AI 辅助下取得了与这两类问题相关的新结果；现有材料未完整呈现证明细节，具体方法与验证状态仍需查阅原文。

**「影响」** 对关注此类结果的人来说，评论指出的问题很具体：Lean 构建通过只说明某个形式命题被内核接受，并不自动说明该命题就是想要证明的数学陈述；因此需要检查形式化的命题本身，而不能只看构建是否成功。有评论者称两个独立内核均接受了结果，并将其视为降低了内核漏洞被利用的可能，但这仍属于社区判断，而非独立验证结论。

**「社区讨论」** 讨论集中在形式验证与 AI 辅助数学上：有人追问，在依靠既有抽象和机器生成并验证证明之后，新的数学抽象和概念该如何产生；也有人担心，像 Lean 这样的大型代码库“构建通过”并不能保证验证的就是目标命题，可能只是某个平凡陈述通过了检查。另有评论者表达了对自己职业前景既兴奋又不安的复杂情绪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/">Unforced Euler singularity, unforced Navier-Stokes ...</a></li>
<li><a href="https://todayforai.com/en/items/art-87f06889-96c">Tao Reports AI-Assisted Proofs on Euler and Navier-Stokes ...</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#formal verification`, `#Lean`, `#AI-assisted proofs`, `#Navier-Stokes`

---

<a id="item-tech-news-3"></a>
### [GitHub 仓库声称 Navier–Stokes 有限时间爆破，尚未验证](https://github.com/tristanbuckmaster/navier-stokes/) ⭐️ 8.0/10

Hacker News 上出现一个指向 GitHub 仓库 tristanbuckmaster/navier-stokes 的帖子，声称给出 Navier–Stokes 方程的有限时间爆破结果。当前可见材料只有一个仓库链接和论坛讨论，没有证明全文、同行评审或独立验证，因此不能把它视为已确认的数学结论。该帖子发布于 2026 年 11 月 20 日；这一声称是否成立，仍取决于对证明的严格审查。

hackernews · trotro · 11月20日 15:34 · [社区讨论](https://news.ycombinator.com/item?id=50576232)

**「背景：千禧年难题与无粘先例」** 三维不可压缩纳维–斯托克斯方程的解是否对任意光滑初始数据都长期保持光滑，还是可能在有限时间内出现奇点，是尚未解决的千禧年大奖难题之一；一旦有限时间爆破的构造成立，就等于以否定方式回答该问题。与之相关，同一批作者还公布了三维不可压缩欧拉方程（纳维–斯托克斯方程的无粘对应）的有限时间奇点构造，但无粘欧拉方程的爆破结果并不能直接推出有粘性的纳维–斯托克斯情形。

**「影响」** 对研究者和工程实践者而言，最直接的后果是：在该仓库内容通过同行评审之前，不能把它当作已确立的结论来使用，例如据此修改湍流数值模拟的基本假设，或宣称千禧年难题已被解决。Clay 数学研究所的 Navier–Stokes 奖仍以正式发表的证明为判定依据。讨论中区分了“外力驱动”与“无外力”两种情形，这一差别直接决定结论的适用范围，引用前需核对原仓库的具体设定。

**「社区讨论」** 评论中最集中的讨论，是把这项声称的“无外力”版本与 OpenAI 据称用外力构造的反例相比较，认为前者更接近真实流体；但这些说法来自评论者，未在给定材料中得到证明。另有评论以调侃方式谈论同日的其他数学传闻和研究者的工作量，不能作为结果可信度或优先权的证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://officechai.com/ai/tristan-buckmaster-levent-alpoge-claim-proof-of-navier-stokes-millennium-prize-problem-without-forcing/">Tristan Buckmaster, Levent Alpöge Claim Proof Of Navier ...</a></li>
<li><a href="https://cims.nyu.edu/~tristanb/cc.pdf">Finite-Time Singularity Formation for the Three-Dimensional ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://vibemathed.com/problem/navier-stokes-millennium-prize-problem-finite-time-breakdown-with-smooth-forcing">Navier – Stokes Millennium Prize problem: finite - time breakdown with...</a></li>

</ul>
</details>

**标签**: `#Navier-Stokes equations`, `#mathematical proof`, `#fluid dynamics`, `#computational science`, `#Hacker News discussion`

---

<a id="item-tech-news-4"></a>
### [PHP 混合大小写 HTTPS 被指静默降级为明文](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 8.0/10

一份被转述的漏洞报告称，PHP 的 HTTP/FTP 流包装器在识别 scheme 时忽略大小写，却只在第五个字符为小写 s 时启用 TLS，导致 HTTPS://、httpS:// 和 FTPS:// 被当作明文 HTTP/FTP 发出。该问题被列为 CVE-2026-128064（GHSA-f6gg-rchx-xw8j），CVSS 4.0 评分为 8.2；令牌、Basic 认证、Cookie、POST 请求体和 FTP 登录信息可能以明文暴露，第三方重定向到此类地址也会触发。修复已进入 PHP 8.2.36、8.3.37、8.4.28、8.5.13 和 8.6.0；8.1 及更早版本已 EOL，不会获得修复，只能把 URL 的 scheme 统一转为小写作为缓解。

telegram · zaihuapd · 11月20日 03:04

**「背景」** PHP 的 HTTP/FTP 流包装器允许程序直接用 URL 发起网络请求。相关漏洞说明指出，这类包装器在识别 scheme 时不区分大小写，但只有在固定位置出现小写 s 时才启用 TLS，因此大小写混写的 scheme 仍会被当作合法地址接受，却可能未进入加密路径。

**「影响」** 该缺陷的失败模式不会报错：受影响请求会以明文发出，应用侧不一定能察觉；无法升级的 PHP 8.1 及更早部署必须在调用流包装器前把 URL 的 scheme 统一改为小写，不能依赖运行时补丁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://everycve.com/CVE-2026-128064">CVE - 2026 - 128064 : Mixed - case HTTPS and FTPS URLs can expose...</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security vulnerability`, `#TLS`, `#CVE`, `#HTTPS`

---

<a id="item-tech-news-5"></a>
### [Meta AI 助手 Muse 被指跨账户泄露私密信息](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/) ⭐️ 8.0/10

据路透社援引 Meta 内部帖子，Meta 的 AI 助手 Muse 被员工指认会在不同账户之间串对话，并显示不属于当前用户的私密信息，包括未曾发出的育儿请求、职业建议、订单以及他人的银行余额。有人称 Muse 在天气聊天中插入“顺便说一句，Capital One 余额 2722.58 美元，Charles Schwab 余额 5899.57 美元”，另一名员工称它提醒她回复姐姐在 Signal 上的消息，而她并未授权其访问其他应用。上述说法来自内部帖子转述，TechCrunch 进行了报道，目前尚无独立技术验证。

telegram · zaihuapd · 11月20日 05:10

**「背景」** Muse 是 Meta 的 AI agent，此次争议由路透社查阅 Meta 内部帖子后爆出。Ars Technica 报道称，Meta 回应表示 Muse 输出中出现的随机银行和比特币余额并不真实；这些员工说法目前来自内部帖子，尚未看到独立技术验证。

**「用户需复查权限与敏感信息」** 对 Muse 用户而言，直接后果是私人对话和财务信息可能出现在另一个账户的会话中；员工还称 Muse 未经授权读取其他应用的消息，因此用户应检查并撤销 Muse 的关联应用权限，避免把银行余额等敏感信息留在助手对话里。Meta 此前曾因隐私缺陷暂停 Muse 的对话分享功能，表明共享和可发现链接仍是需要优先复核的暴露面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/">Meta ’s AI agent Muse is mixing up conversations and... | TechCrunch</a></li>
<li><a href="https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/">Muse privacy invasions are freaking out Meta staffers, internal chats...</a></li>
<li><a href="https://cybersecuritynews.com/meta-muse-ai-privacy-flaw/">Meta Muse AI Privacy Flaw Exposes Confidential Business Data ...</a></li>
<li><a href="https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/">Meta’s AI agent Muse is mixing up conversations and exposing ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#privacy`, `#data leakage`, `#Meta`, `#security incident`

---

<a id="item-tech-news-6"></a>
### [CVE-2026-99312：KVM 漏洞可让虚拟机读取 AMD 主机内存](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 8.0/10

Linux 内核 KVM 被曝出 CVE-2026-99312 漏洞，仅影响启用了嵌套虚拟化的 AMD 主机。研究人员在 DigitalOcean 环境中从虚拟机内读取到约 127 GB 宿主内存。上游修复已于 11 月 18 日随稳定版内核 7.3.5 等发布；Debian、Ubuntu 等发行版内核尚未修复，在补丁到位前可以关闭嵌套虚拟化作为缓解措施。

telegram · zaihuapd · 11月20日 14:23

**「背景」** 嵌套虚拟化允许虚拟机内部再运行自己的 Hypervisor 并创建下一级客户机，因此 KVM 需要额外维护 AMD 平台上的嵌套状态。DigitalOcean 将 CVE-2026-99312 描述为这段 AMD 嵌套虚拟化支持中的过期指针问题；Terra Security 则指出，其根源与之前一次安全修复有关，并且该缺陷只存在于 AMD 的嵌套虚拟化代码路径中，Intel 主机不受影响。

**「影响」** 运行 AMD 主机且开启嵌套虚拟化的虚拟化平台和多租户环境，需要确认所用内核是否已包含上游修复；在 Debian、Ubuntu 等发行版补丁可用前，关闭嵌套虚拟化可以消除这一攻击面，避免虚拟机读取宿主内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE - 2026 - 99312 Lets Guest VMs Access Host ...</a></li>
<li><a href="https://www.digitalocean.com/blog/cve-2026-99312-kvm-patch">Virtualization , Responsible Disclosure, and CVE - 2026 - 99312</a></li>
<li><a href="https://www.terra.security/blog/kvm-guest-to-host-escape">KVM Guest-to- Host Escape | Terra Security Research</a></li>

</ul>
</details>

**标签**: `#KVM`, `#Linux kernel`, `#virtualization security`, `#CVE-2026-99312`, `#AMD`

---

<a id="item-tech-news-7"></a>
### [Alessandro Masullo 匆忙发布声称的广义黎曼猜想证明](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) ⭐️ 7.0/10

一篇博客文章匆忙公布了 Alessandro Masullo 的稿件，声称证明了广义黎曼猜想（GRH），使数学家面对一份尚待核验的声明。评论者称该草稿长达 940 页，且第 1.1.1 节为空；Masullo 据称已研究该问题 12 年。由于评论者猜测发布时机与一则 Anthropic 公告有关，讨论很快转向优先权归属和验证问题。

hackernews · jasondavies · 11月20日 18:33 · [社区讨论](https://news.ycombinator.com/item?id=50579568)

**「背景」** 广义黎曼猜想（GRH）是黎曼猜想在狄利克雷 L 函数上的推广；数论中大量结论都以它成立为前提。据 explainx 汇总，Masullo 是 Brian Conrad 指导的 2019 年斯坦福博士；他的 940 页预印本《The Music of the Primes》在 Conrad 已审查数月、并称“目前看来有希望”之后，由 AMS 主席 Ravi Vakil 于 11 月 20 日匆忙发帖，请数学界尽快审阅。同一天还有 Levent Alpöge 借助 Claude 的证明发布，两起黎曼猜想声明撞在同一天，这也解释了社区对优先权与验证节奏的关注。

**「审阅负担与引用风险」** 对研究该领域的数学家而言，眼前的实际负担是要在结论尚未验证的情况下审阅一份 940 页的预印本；Vakil 于 11 月 20 日发布公告，称 Conrad 数月审阅“目前看来有希望”，并选择让社区尽快介入，因此在独立核验完成前，不宜把这份手稿当作已证明的 GRH 来引用或在此基础上继续工作。

**「社区讨论」** 评论者就优先权展开争论：有人猜测 Masullo 是在看到 Anthropic 公告后抢先发布，也有人建议数学家应定期公布在研稿件的带可信时间戳哈希，以便日后主张部分贡献。另有评论者把 940 页草稿中第 1.1.1 节留空视为值得警惕的迹象，并质疑把如此规模的结果隐藏一年是否现实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/alessandro-masullo-grh-human-proof-claimed-vs-verified-november-2026">Masullo GRH Draft: What Vakil Announced (Nov 20) | explainx ...</a></li>
<li><a href="https://x.com/i/trending/2123859232806064131">Mathematician Claims Proof of Generalized Riemann Hypothe...</a></li>
<li><a href="https://kingy.ai/blog/two-riemann-proof-claims-timeline/">Two Riemann proof claims in one day. What counts as first ...</a></li>
<li><a href="https://x.com/i/trending/2123859232806064131">Mathematician Claims Proof of Generalized Riemann Hypothe...</a></li>

</ul>
</details>

**标签**: `#Generalized Riemann Hypothesis`, `#mathematics research`, `#AI competition`, `#research verification`, `#Hacker News`

---

<a id="item-tech-news-8"></a>
### [Inkling 2 Mini：循环架构的开放权重 MoE 模型](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

Thinking Machines 发布了 Inkling 2 Mini，这是一个采用循环 Transformer 架构和混合专家（MoE）设计的开放权重模型，面向本地推理场景。社区讨论称其基准表现接近 Qwen3.8-27B，但这些数字目前来自发布信息或社区转述，尚缺独立复现。一个名为 unsloth/Inkling-2-Mini-GGUF 的仓库提供了可在 Ollama/Llama.cpp 运行的 GGUF 版本；有用户计划在 AMD 7900XTX 上将其与 Qwen 3.8 27B 对比。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**「背景」** Thinking Machines 的发布说明称，循环 Transformer 会在每个 token 上重复执行中间层，Inkling 2 Mini 将其中间层执行三次，以便用更少 token 完成依赖推理质量的任务。模型卡和 Artificial Analysis 的资料显示，它是总参数 26B、激活参数 5.4B 的 MoE，采用 Apache 2.0 许可，并支持文本与图像输入。

**「影响」** 希望本地部署的用户需要通过 Unsloth 提供的 GGUF 量化版本，并借助 llama.cpp 或 Ollama 运行该模型；厂商同时称其智能体编程基准（DeepSWE v1.1、SWE-bench Pro v2）领先同级模型，但在其他基准上仍落后于 Qwen 3.8-27B，因此选型时应按任务类型核对实际表现，而不是只看单一榜单。

**「社区讨论」** 评论区的态度是谨慎乐观：有人称若基准在真实场景中成立，循环架构能达到 Qwen3.8-27B 水平非常突出，但明确把判断限定在“如果这些基准站得住”的前提下。其他人补充了 GGUF 在 Ollama/Llama.cpp 上的运行路径，并计划在 AMD 7900XTX 上实测 MoE 是否带来更高解码速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>
<li><a href="https://thinkingmachines.ai/model-card/inkling-2-mini/">Inkling 2 Mini Model Card - Thinking Machines Lab</a></li>
<li><a href="https://artificialanalysis.ai/articles/inkling-2-mini">Thinking Machines has released Inkling 2 Mini, an open ...</a></li>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#looped transformers`, `#Mixture-of-Experts`, `#local inference`, `#AI model releases`

---

<a id="item-tech-news-9"></a>
### [SEC 据报调查英伟达会计处理](https://finance.yahoo.com/markets/article/nvidia-stock-extends-25-trillion-rout-as-sec-probe-reportedly-investigates-its-accounting-194945274.html) ⭐️ 7.0/10

据引述消息人士的报道，美国证券交易委员会（SEC）正在调查英伟达的会计处理，但英伟达和 SEC 均未公开确认这一调查。报道出现之际，英伟达股价正延续大幅下跌，市场关注点集中在会计问题和融资安排上。由于缺少公司披露或监管文件，调查的具体范围、时间表以及是否会导致执法行动仍不清楚。

hackernews · ftchd · 11月20日 20:22 · [社区讨论](https://news.ycombinator.com/item?id=50581438)

**「报道来源与审查性质」** 路透社 2026 年 11 月 20 日援引两名了解情况的人士报道称，美国证券交易委员会（SEC）执法部门正在审查英伟达可能存在的会计问题，这是该消息的最初来源。报道没有说明审查涉及哪些具体会计科目或时间范围，也未表示已提出任何指控；这类由执法部门开展的审查通常发生在正式提起诉讼或达成和解之前。

**「社区讨论」** 评论者把焦点放在英伟达的循环融资和“股票换折扣芯片”交易上，有人认为这可能放大当前的市场回调；也有人质疑，若董事会担心会计问题，为何仍让 CFO 出任临时 CEO。另有评论称，英伟达股价已较六周前的高点下跌近 50%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/us-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say-2026-11-20/">Nvidia&#x27;s accounting is a focus of US SEC investigation ...</a></li>
<li><a href="https://www.unite.ai/sec-enforcement-staff-examine-nvidia-accounting-reuters-reports/">SEC Enforcement Staff Examine NVIDIA Accounting, Reuters Reports</a></li>
<li><a href="https://nypost.com/2026/11/20/business/nvidias-accounting-practices-are-focus-of-probe-by-sec-report/">Nvidia&#x27;s accounting practices are focus of probe by SEC: report</a></li>

</ul>
</details>

**标签**: `#nvidia`, `#sec-investigation`, `#ai-hardware`, `#accounting`, `#tech-industry`

---

<a id="item-tech-news-10"></a>
### [语言模型重写自身权重引发争议](https://arxiv.org/abs/2611.21885) ⭐️ 7.0/10

一篇 arXiv 论文提出，语言模型可以依靠自身推理重写权重：它在练习题上测试编辑并只保留有效修改，声称在八次连续会话中准确率持续上升，且不使用梯度或训练。Hacker News 的讨论对这一“无训练自我改进”的说法提出保留，焦点包括实际增益有限、与既有工作的相似性以及安全风险；由于缺少论文全文，这些判断尚不能独立核实。

hackernews · lwhsiao · 11月20日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50577265)

**「背景」** 大语言模型通常依赖基于梯度的训练来更新参数；所谓“自改写权重”，指的是模型在推理过程中直接编辑自身参数，而不经过常规的梯度更新。Hacker News 评论者将这篇论文与此前的“权重空间编程”文章以及 Google 的“sleep”框架相提并论，认为其思路与已有工作存在相似之处。

**「社区讨论」** 有评论指出，论文中真正带来提升的修改只是缩短推理轨迹以避免 token 上限，并认为这与近期的权重空间编程工作及 Google 的“sleep”框架相似，因此新颖性有限。另有评论担忧，自主运行的模型可能定位并抑制与安全对齐相关的激活，再部署后续模型；这是评论者提出的风险路径，不是论文已展示的结果。

**标签**: `#language models`, `#weight editing`, `#self-improvement`, `#AI safety`, `#research`

---

<a id="item-tech-news-11"></a>
### [Aaronson 博客讨论 LLM 疑似证明黎曼猜想](https://scottaaronson.blog/?p=10344) ⭐️ 7.0/10

Scott Aaronson 的博客文章讨论了一个据称由 AI/LLM 得出的黎曼猜想证明，但文章用“apparently”标明这仍只是表面上的说法，目前没有提供证明正文、形式化陈述或验证结论。相关讨论集中在 Lean 形式化的规模与算力需求上，有人质疑人类能否完整理解如此大的形式化开发。由于缺少可核查的证明细节，目前不能把它视为已获确认的数学突破。

hackernews · stratos123 · 11月20日 20:03 · [社区讨论](https://news.ycombinator.com/item?id=50581084)

**「背景」** “随机鹦鹉”（stochastic parrot）是 2021 年出现的一个标签，用来批评大语言模型只会复述训练语料；Aaronson 的帖子正是围绕社交媒体上“这些‘鹦鹉’刚证明了黎曼猜想”的反讽说法展开。相关检索摘要还提到 Levent Alpöge 关于 Anthropic 模型证明广义黎曼猜想的说法，为这次“AI 证明数学难题”的讨论提供了更具体的前情。

**「社区讨论」** 评论者没有给出一致的验证结论：有人追问如此庞大的 Lean 开发能否被任何人完整理解，也有人设想如果数学家拥有近乎无限的算力，会产生多少类似突破，另有评论表达了对人类逐渐无法理解科学结果的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scottaaronson.blog/?p=10344">Shtetl-Optimized » Blog Archive » The stochastic parrots have ...</a></li>
<li><a href="https://agihunt.info/en/p/1a1faf3ca85035bde600331be64">Scott Aaronson: Alpöge claims Anthropic models… · AGI Hunt</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#Riemann Hypothesis`, `#Lean`, `#formal verification`, `#AI for mathematics`

---

<a id="item-tech-news-12"></a>
### [Signal 发文强调隐私保护，社区聚焦 AI 应用权限](https://signal.org/blog/protecting-your-privacy/) ⭐️ 7.0/10

Signal 于 2026 年 11 月 20 日发布博客《Signal Is Serious About Protecting Your Privacy》，表示正在推进隐私保护工作。提供的材料没有博文全文或具体技术细节，因此无法确认是否有新功能上线、覆盖哪些平台，以及是否涉及版本更新；目前能确认的是 Signal 公开发声，而不是一项已可验证的产品变更。

hackernews · dotcoma · 11月20日 09:42 · [社区讨论](https://news.ycombinator.com/item?id=50572348)

**「背景」** 移动端 AI 助手可能截取屏幕或读取聊天界面内容，因此“禁止截屏”只是保护聊天数据的一道不完整防线。The Verge 报道称，Signal 的 Meredith Whittaker 已承认该截屏阻断措施“并不完整”，因为 AI 代理仍可能通过设备文件系统等其他途径取得应用数据。

**「影响」** 对使用 VPN 的新用户，现有垃圾信息防护可能反复触发验证码，增加添加联系人的摩擦；评论中有人称记者和消息源因此不得不改用其他应用。

**「社区讨论」** 评论者担心设备上的第三方 AI 应用会读取 Signal 聊天，甚至通过联系人一侧间接泄露内容，并有人呼吁公开相关取证调查结果。另一组讨论则批评垃圾信息防护在 VPN 下频繁触发验证码，以及 Windows 端无法截图影响正常使用；这些都是用户意见和个体体验，不等同于 Signal 已确认的变更或漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1038390/signal-blocking-ai-agent-screenshots-mobile-app">Signal is blocking Gemini and Siri AI from reading your... | The Verge</a></li>

</ul>
</details>

**标签**: `#privacy`, `#secure messaging`, `#Signal`, `#AI app permissions`, `#mobile security`

---

<a id="item-tech-news-13"></a>
### [Frostbite：公司称 AI 设计并验证交互网 CPU 架构](https://architectlabs.com/blog/frostbite) ⭐️ 7.0/10

Architect Labs 在博客中声称，名为 Frostbite 的 CPU 架构由 AI 完成发现、设计和验证，其基础是交互网（interaction nets），并非传统指令流。对 CPU 架构研究者和编译器、硬件开发者而言，这目前仍只是公司声明：没有独立验证或可复核的基准结果，不能视为已流片或已量产的处理器。

hackernews · shioyama · 11月20日 10:01 · [社区讨论](https://news.ycombinator.com/item?id=50572503)

**「背景：交互网」** Frostbite 所依托的交互网（interaction nets／interaction calculus）是一种不同于主流冯·诺依曼指令流的计算模型：程序被表示为图，计算通过局部的图重写完成，约简在拓扑上局部发生，而不依赖集中式的取指与调度。相关讨论认为，这种局部性使交互网在物理上更接近可直接映射到硬件的计算形式，但能否据此构建通用 CPU 仍取决于具体实现。

**「影响」** 对架构研究者和工具链开发者而言，眼下无法据此做出采用或移植决策；更有意义的后续信号是可复现的基准，尤其是与现代化乱序 CPU 的对比、足够广的程序覆盖以及公开的实现细节。

**「社区讨论」** 有评论者认为标题夸大了 AI 的作用：核心洞见由人类提出，AI 的强项是把数十年研究文献综合成连贯的工程产品。另一类质疑聚焦性能证据，指出其基线是顺序 CPU、测试程序较少，并提到二十多年前的 WaveScalar 已探索过数据流架构方向。

<details><summary>参考链接</summary>
<ul>
<li>There&#x27;s a model of computation called &#x27;interaction nets ... - Hacker News</li>

</ul>
</details>

**标签**: `#CPU architecture`, `#AI-assisted design`, `#interaction nets`, `#hardware verification`, `#computer architecture`

---

<a id="item-tech-news-14"></a>
### [Levent Alpöge 称与 Claude 发现并形式化黎曼猜想证明](https://simonwillison.net/2026/Nov/20/levent-alpoge/) ⭐️ 7.0/10

Levent Alpöge 在个人页面发文称，他与 Claude 合作发现了一个黎曼猜想的证明，并表示该方法还可用于广义黎曼猜想，预计投入更多时间后也能覆盖扩展黎曼猜想。他还声称，两人已在没有额外假设的情况下形式化了相关论证。上述说法目前仅来自其个人声明，未附证明细节、同行评审或独立验证；Simon Willison 的条目只是转引该声明。

rss · Simon Willison · 11月20日 16:30

**「背景」** 黎曼猜想由波恩哈德·黎曼于 1859 年提出，讨论黎曼 ζ 函数非平凡零点的位置，通常被列为数学界最著名、最久未解的难题之一，至今已有 167 年历史。据维基百科条目记载，Levent Alpöge 是数学家，同时受雇于 Anthropic；他于 2026 年 11 月 20 日宣布了这一可能证明，并称相关论证已在 Lean 4 证明语言中完成形式化。需要注意的是，这些报道转述的都是 Alpöge 本人的声明，形式化本身是否成立、证明是否经过同行评审，均尚未得到独立确认。

**「对使用者的实际影响」** 在任何人独立核验之前，数学研究者和引用该结果的作者都应把它当作未经证实的个人声明：原文没有给出证明细节、没有同行评议，也没有第三方确认，因此不能作为定理使用或写进论文。另一个需要留意的因素是，Levent Alpöge 本人是 Anthropic 的技术人员，这使得该声明出自对 Claude 能力评价有直接利益的一方，更应等待外部检验，而不是依据附带的形式化说法直接采信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/">Anthropic mathematician claims to prove Riemann hypothesis ...</a></li>
<li><a href="https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof">Anthropic mathematician claims AI helped solve a 167 ... - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/anthropic-167-year-old-riemann-hypothesis-claude">Claude helped prove 167-year-old Riemann hypothesis , researcher...</a></li>

</ul>
</details>

**标签**: `#AI-assisted mathematics`, `#Riemann Hypothesis`, `#Claude`, `#formal verification`, `#research claims`

---

<a id="item-tech-news-15"></a>
### [Gemini 在 Mac 上线可暂停的电脑操作代理](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 7.0/10

据 Bloomberg 报道，Google Gemini 已向美国地区使用 Mac 版 Gemini、并订阅 Google AI Plus、Pro 或 Ultra 的用户开放“电脑操作”功能，可代用户点击、输入、浏览菜单和填写表单。该代理在独立后台窗口运行，用户可继续使用主屏幕和光标，还能限制其访问的应用、实时查看操作、随时暂停，并在关键操作前审批。

telegram · zaihuapd · 11月20日 02:51

**「背景」** 这类“电脑操作”功能属于图形界面代理：它不依赖应用接口，而是通过模拟点击、输入和菜单导航来替用户完成任务。关键前提是代理能在后台运行，同时用应用限制、暂停和关键操作审批等边界，把自动化操作置于用户控制之下。

**「影响」** 符合条件的用户可把重复性桌面操作交给后台代理，但应用限制、实时查看和关键步骤审批仍是必要控制；该能力目前仅面向美国区使用 Mac 版 Gemini 的 Google AI Plus、Pro 或 Ultra 订阅用户开放，其他用户不在本次开放范围内。

**标签**: `#Google Gemini`, `#AI agents`, `#macOS`, `#desktop automation`, `#product launch`

---

<a id="item-tech-news-16"></a>
### [英国法庭裁定苹果胜诉，后门令须公开审理](https://appleinsider.com/articles/26/11/19/uk-cant-hide-that-it-tried-ordering-apple-to-allow-access-to-user-data) ⭐️ 7.0/10

英国调查权力法庭裁定苹果胜诉，英国内政部不得继续保密其要求苹果开放 iPhone 加密数据访问的「技术能力通知」，案件大部分内容将公开审理。内政部随后确认曾发出该通知，称目的是将罪犯绳之以法；法庭认定其国家安全理由「不切实际」。报道未披露通知的具体技术要求、发出时间或完整判决文本。

telegram · zaihuapd · 11月20日 04:13

**「背景：技术能力通知与调查权力法庭」** 此案的核心法律工具是英国《2016 年调查权力法》下的「技术能力通知」（TCN），内政大臣可据此要求通信服务商提供特定的技术能力。据调查权力法庭（IPT）公布，苹果针对内政大臣的诉讼起初并未公开，法庭此次披露该案涉及向「相关运营商」发出技术能力通知的权力；据 ICLG 报道，法庭这一裁定为公开听证扫清道路，审理焦点是内政大臣能否以监控权力规制科技公司保护其服务的方式。

**「实际影响」** 对英国 iPhone 用户和加密开发者而言，直接后果是这项命令不再处于保密状态，案件大部分程序将公开；但报道没有说明该通知是否仍有效、苹果是否仍须在技术上配合，产品层面的影响仍不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://iclg.com/news/home-secretary-loses-bid-to-keep-apple-surveillance-notice-secret/">Home Secretary loses bid to keep Apple surveillance notice ...</a></li>
<li><a href="https://investigatorypowerstribunal.org.uk/judgement/1-mr-vincent-kearney-2-british-broadcasting-corporation-v-1-chief-constable-of-the-police-service-of-northern-ireland-2-chief-constable-of-durham-constabulary-3-security-service-4-governme/">Apple Inc and Secretary of State for the Home Department and ...</a></li>

</ul>
</details>

**标签**: `#苹果`, `#英国`, `#加密后门`, `#隐私安全`, `#法律裁定`

---

<a id="item-tech-news-17"></a>
### [美众议院披露近 88 万颗 AI 芯片对华出口获批](https://foreignaffairs.house.gov/news/press-releases/chairman-brian-mast-exercises-legislative-authority-to-publicly-release-ai-chip-license-information-for-china) ⭐️ 7.0/10

美国众议院外交事务委员会公布的文件显示，2025 年 12 月至 2026 年 5 月，美国批准英伟达和 AMD 向中国出口 879,868 颗 AI 芯片，涉及 H200、MI325X 等型号，而企业申请总量为 344.4 万颗。获批对象包括腾讯、字节跳动（各 15 万颗），阿里巴巴、快手、滴滴（各 7.5 万颗），以及米哈游、百度、京东等；其中阿里、腾讯、百度、比亚迪被列入美方所谓“中国军方关联企业名单”，引发国会对出口审查的质疑。文件还显示，截至 5 月 11 日，21 份批准许可均未发货，因此获批数量不等于实际交付。

telegram · zaihuapd · 11月20日 04:25

**「背景」** 美国对华先进 AI 芯片出口实行许可证管理，企业须经美国政府批准后才能出口，国会则负责监督相关审批。此次众议院外交事务委员会公开的正是这类许可信息，因此披露内容把审批数量、企业名单和芯片型号置于国会审查之下。

**「获批不等于交付」** 这批许可对实际可用算力的意义有限：截至 5 月 11 日，披露的 21 份许可均未显示发货，因此近 88 万颗只是获批额度，不能当作已交付芯片。依赖 H200 和 MI325X 扩容的中国企业需要把许可审批与装运、清关进度分开评估，避免按批准量规划产能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/geopolitical/revealed-trump-admin-cleared-879868-nvidia-amd-ai-chips-china-third-pentagon-listed">Revealed: Trump Admin Cleared 879 , 868 Nvidia, AMD AI Chips For...</a></li>
<li><a href="https://www.yahoo.com/news/politics/articles/license-information-ai-chips-sent-201033356.html">US signed off on sales of nearly 900,000 AI chips to China in six...</a></li>
<li><a href="https://foreignaffairs.house.gov/news/press-releases/chairman-brian-mast-exercises-legislative-authority-to-publicly-release-ai-chip-license-information-for-china">Chairman Brian Mast Exercises Legislative Authority to Publicly...</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#export controls`, `#NVIDIA`, `#AMD`, `#US-China tech`

---

<a id="item-tech-news-18"></a>
### [美收紧芯片出口，印度扩张 AI 算力](https://www.bloomberg.com/news/articles/2026-11-20/nvidia-scandal-fallout-india-ai-yotta-ambani-adani-am-intelligence-e2e-networks) ⭐️ 7.0/10

美国收紧对马来西亚、泰国和新加坡的先进芯片出口，印度 AI 业界认为这可能把部分外溢需求引向本国。Yotta 表示未来一年将新增约 10 万块 GPU，相当于印度现有算力再增加约 10%；这一规模目前属于公司计划，而非已交付容量。印度现有 153 个数据中心，居全球第 14，信实承诺投入至多 1100 亿美元、阿达尼承诺 1000 亿美元建设 AI 基础设施，但该国长期受算力基础设施短缺和资本受限拖累。

telegram · zaihuapd · 11月20日 07:31

**「背景」** 这轮限制的背景是美国试图堵住中国通过东南亚获取英伟达等先进 AI 芯片的通道；《纽约时报》11 月 17 日报道，相关提案已令依赖中资数据中心投资的东南亚市场感到不安。随后马来西亚表示，正就许可要求以及向第三方提供数据中心服务等细则寻求美方澄清。台积电和三星据报道已暂停向中国客户发运部分受新规影响的芯片，显示限制正从 AI 处理器外溢到更广的半导体供应链。

**「影响」** 对印度本地 AI 开发者和云服务买家而言，Yotta 声称未来一年新增约 10 万块 GPU；若这一计划兑现，相当于把印度现有算力提高约 10%，可部分缓解境内 GPU 容量紧张。但该数字仍是公司前瞻性计划，且信实、阿达尼的千亿美元级投入承诺还受资本与基础设施条件约束，采购方不宜将其视为已可用的容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/17/business/southeast-asia-china-ai-chips.html">Trump’s New A.I. Chip Rules Rattle Southeast Asia - The New York...</a></li>
<li><a href="https://www.freemalaysiatoday.com/category/nation/2026/11/18/malaysia-seeks-us-clarification-on-new-ai-chip-restrictions">Malaysia seeks US clarification on new AI chip restrictions | FMT</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/20/news-tsmc-samsung-reportedly-pause-china-consumer-chip-shipments-under-new-u-s-rules-16nm-orders-affected/">[News] TSMC, Samsung Reportedly Pause China Consumer Chip ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#export controls`, `#GPU compute`, `#India`, `#data centers`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [vLLM 首日支持循环模型 Inkling 2 Mini](https://vllm.ai/blog/2026-11-20-inkling2-mini) ⭐️ 8.0/10

rss · vLLM Blog · 11月20日 00:00

**「背景」** Thinking Machines 发布的 Inkling 2 Mini 是 26B 总参数、3.5B 激活参数、支持 1M token 上下文的多模态 MoE，但其中间 12 层要以共享权重循环三遍，每遍独立的 KV/卷积状态与遍间消息传递给推理系统带来新问题。

**「方案」** 模型分 prelude、循环核心和 coda：三遍均从 prelude 输出出发，后一遍只通过子层消息读取上一遍；每遍每 token 读取 48 条消息，由 rank-64 控制器合并，24 层最终对应 48 份 KV 与卷积状态缓存。vLLM 把每遍的额外核心层注册为普通缓存层，复用 KV 管理与前缀缓存；它融合四次消息读取、将四个控制器堆叠成 batched GEMM，并用 Triton 融合 RMSNorm 与门控合并，合并保持 FP32 且不做 FMA 收缩。作者称其还复用并泛化了 Inkling 2 Small 的子层融合内核；3 层 DSpark 草稿固定读取 prelude、第二/三遍和最终输出，因此变遍数检查点要保留 DSpark 必须用默认三遍。TML-d24-varloop-research 允许启动时用 loop\_num\_passes 选遍数、用 loop\_share\_cache 共享 KV；在单张 GB200、TP1、4K 仅前向测试中，1/2/3 遍的 batch-1 解码步为 1.51/2.67/3.85 ms，KV 容量从 352K 降至 175K token，共享 KV 仅回到 194K，因卷积状态仍按遍保存。作者称隐藏状态差异约等于参考自身两种注意力路径的差异，MoE 输出在相同输入下逐位一致，并做了 1M token NIAH、MMMU-Pro、HLE 与 GSM8K 测试。

**「启示」** 文章说明循环模型无需专用推理栈即可部署：把每一遍当作普通缓存层并融合消息与控制器的读写，就能在 Day-0 获得可用性能；变遍数检查点则把速度、显存与质量的取舍交给部署者。

**标签**: `#looped models`, `#vLLM`, `#KV cache`, `#MoE inference`, `#kernel fusion`

---

<a id="item-tech-blog-2"></a>
### [为什么缓存 LLM 输出收效甚微](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月21日 00:00

**「背景」** LLM 推理通常依靠 KV 缓存复用输入，避免每轮重新计算全部对话历史；作者据此追问：是否也应缓存或去重模型输出，以省下更昂贵的输出 token。

**「方案」** 作者先承认，代理确实会在回复中反复引用代码、证据文档和样例，造成输出 token 浪费；一种设想是微调或提示模型只给出“src/script.py:12-15”这类引用，再由运行框架展开。但他认为，这只能优化用户可见的重复，模型内部思维链未必需要复述已有信息。按其个人代理记录，输出 token 约 50% 是推理、44% 是工具调用，可见输出只占约 6%；即便乐观地省掉其中三分之二，总输出也只降约 4%，这正体现 Amdahl 定律的约束。要真正节省，应减少那 94% 的不可见输出，而这更多取决于模型智能：更强的模型需要的推理和工具调用更少，可能单价高 5 倍，却因 token 少 6 倍而总成本更低。作者也注明，6% 来自自身经验，他对思维链是否重复只有中等信心，工具调用内部是否重复仍待验证。

**「启示」** 作者的结论是，输出缓存瞄准的只是可见文本这一小部分，杠杆很低；降低 LLM 成本的关键不在去重表面输出，而在用更聪明的模型减少推理与工具调用 token。

**标签**: `#LLM inference economics`, `#output caching`, `#token economics`, `#Amdahl&\#x27;s law`, `#AI agents`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [北京拟规定租房正常损耗不得扣减押金](https://mp.weixin.qq.com/s/PmGxh5knIyxiBRhpRoJnoQ) ⭐️ 7.0/10

北京市住建委与市场监管局起草的《北京市住房租赁合同（示范文本）（修订征求意见稿）》自 11 月 20 日起公开征求意见，拟明确承租人正常使用造成的房屋正常损耗不承担赔偿责任，出租人不得以此为由扣减押金。征求意见稿还要求从事转租经营的租赁企业将租金和押金存入监管账户，并新增保密与个人信息保护条款。

telegram · zaihuapd · 11月20日 13:46

**「背景」** 住房租赁合同示范文本是住建部门发布的推荐性合同模板，供房东与租客签约时参照使用，本身并不强制适用。此次修订稿由北京市住建委与市场监管局起草，自 20 日起公开征求意见，目前仍是草案、尚未定稿。

**「影响」** 若该征求意见稿最终落地，北京租户退租时因“正常损耗”被扣押金将有明确的合同依据；而通过租赁企业（含转租经营）租房的租客，押金和租金须进入监管账户，可降低企业挪用资金或经营失败带来的损失风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.fang.com/open/51098736.html">北 京 新规： 租 房 押 金 和 租 金 监管更靠谱！ - 房 产资讯- 房 天下</a></li>

</ul>
</details>

**标签**: `#住房租赁`, `#押金监管`, `#北京住建委`, `#租户权益`, `#征求意见稿`

---