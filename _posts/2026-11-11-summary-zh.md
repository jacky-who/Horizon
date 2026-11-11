---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11
lang: zh
---

> 从 47 条内容中筛选出 18 条重要资讯。

---

**科技新闻**
1. [微软发布 .NET 11 运行时新特性文档](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepMind 推出 AlphaProof Code 代码形式化验证代理](#item-tech-news-2) ⭐️ 8.0/10
3. [Blender 5.3 发布：原生支持 Gaussian Splat 并增强几何节点](#item-tech-news-3) ⭐️ 8.0/10
4. [Chips and Cheese 深潜 AMD Zen 6 架构](#item-tech-news-4) ⭐️ 8.0/10
5. [谷歌公开开放 Gemini 4 Carbon，12 月 API 价格将翻倍](#item-tech-news-5) ⭐️ 8.0/10
6. [Synaptics 专利主张致 DisplayLink 驱动开发停止](#item-tech-news-6) ⭐️ 7.0/10
7. [Chrome 开源 modern-web-guidance 1.0 引导编码代理](#item-tech-news-7) ⭐️ 7.0/10
8. [Meta 发布 Muse Ember：主打智能体任务的小模型，定价贴近 Haiku 与 Luna](#item-tech-news-8) ⭐️ 7.0/10
9. [Apiiro：Claude Code 设置文件致 2539 个凭据泄露](#item-tech-news-9) ⭐️ 7.0/10
10. [Fireworks 确认新攻击：客户账单、模型权重与数据集外泄](#item-tech-news-10) ⭐️ 7.0/10
11. [Anthropic 改白名单制：中国大陆及港澳不在支持地区名单](#item-tech-news-11) ⭐️ 7.0/10
12. [稀宇科技开源 MiniMax H3 Image，称约 10 秒生成 4K 图像](#item-tech-news-12) ⭐️ 7.0/10

**科技博客**
1. [AI 时代，胶水工作仍然有害](#item-tech-blog-1) ⭐️ 5.0/10

**财经新闻**
1. [Polymarket 称年化收入突破 18 亿美元](#item-finance-news-1) ⭐️ 7.0/10
2. [美联储理事沃勒：倾向 12 月加息，若通胀超预期可考虑 50 个基点](#item-finance-news-2) ⭐️ 7.0/10
3. [前三季度中国新能源乘用车出口同比增长 138.8%](#item-finance-news-3) ⭐️ 7.0/10
4. [Anthropic 撤回最高拟募 693 亿美元的 IPO 文件](#item-finance-news-4) ⭐️ 7.0/10
5. [台积电 10 月营收 5868.9 亿新台币，同比增 59.7%](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [微软发布 .NET 11 运行时新特性文档](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime) ⭐️ 8.0/10

微软在 Microsoft Learn 上发布了 .NET 11 运行时的新特性文档，条目同时链接到 devblogs 上的 .NET 11 公告，面向 .NET/C\# 开发者说明该版本运行时的变化。由于条目本身只提供一个指向公告的链接，具体的功能清单、性能数据和可用范围仍需以微软官方文档为准。从社区讨论看，值得关注的两项变化是运行时层面的 async 支持，以及 decimal 解析与表示行为的兼容性调整。

hackernews · stevefan1999 · 11月10日 12:20 · [社区讨论](https://news.ycombinator.com/item?id=50439284)

**「背景」** 要理解这项变化，需要先知道 .NET 的 async/await 此前依赖编译器生成的状态机来挂起和恢复异步方法。微软的 .NET 11 文档称，运行时库已不再包含这类编译器生成的状态机，而是完全依赖运行时提供的异步支持；相关文章将这一机制称为 Runtime Async 或 Runtime Async V2。

**「影响」** 升级到 .NET 11 前，依赖 decimal 精度或字符串表示行为的代码和测试需要复核：有评论者引用兼容性文档指出，\`\(decimal\)0.1\` 在 .NET 10 下输出 0.1，而在 .NET 11 下变为 0.1000000000000000055511151231。另有评论者提到微软现已提供官方版本管理器 dotnetup，可用于管理多版本 .NET 安装。

**「社区讨论」** 评论者普遍对 C\#/.NET 的日常后端开发体验评价积极，认为它因 Windows-only 等历史印象而被低估；也有人对运行时 async 支持感到意外，原本以为移除状态机后难以保持同等性能。另有评论者提醒注意上述 decimal 兼容性变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime">What&#x27;s new in .NET 11 runtime | Microsoft Learn</a></li>
<li><a href="https://www.c-sharpcorner.com/article/net-11-runtime-async-performance-what-actually-changes">.NET 11 Runtime Async Performance: What Actually Changes</a></li>

</ul>
</details>

**标签**: `#.NET`, `#C\#`, `#runtime`, `#async`, `#release notes`

---

<a id="item-tech-news-2"></a>
### [DeepMind 推出 AlphaProof Code 代码形式化验证代理](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 8.0/10

DeepMind 发布了 AlphaProof Code；从现有信息看，这是一个使用 AI 代理对代码进行形式化验证的工具。由于没有提供博客正文，目前无法确认它支持哪些语言、验证了哪些代码库、证明复盖到什么程度，以及是否已开放使用。讨论中提到的“零缺陷”结果应视为待核实的说法，而不是已独立验证的结论。

hackernews · ilreb · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「背景：形式化验证证的是什么」** 形式化验证并非直接查找 bug，而是用机器可检查的证明来说明实现符合事先写定的规格；证明通过只意味着代码与规格一致，并不保证规格本身正确或完整，这正是在讨论「零缺陷」结论时值得先厘清的前提。DeepMind 的博文将 AlphaProof Code 描述为一个多 LLM 智能体框架：人类专家与 AI 共同确定要证明什么，再由一组智能体分头完成证明，并将其用于在机器码层面验证 Signal 协议参考实现 libsignal 的关键安全属性。

**「影响」** 对尝试用此类代理做形式化验证的团队，验收标准需要从“证明是否通过”扩展到“定理是否覆盖真实需求”；否则，代理可能高效地证明一组无关或过窄的性质，却无法降低实际缺陷风险。

**「社区讨论」** Hacker News 评论者最有力的质疑是，“零缺陷”可能只说明定理太窄或写错了：hedora 提到被验证的是有历史缺陷的真人代码库，因此更应怀疑规范而非直接相信结果。thibsrn 则认为该代理看起来仍是在代码库中迭代并编写 Lean/Rocq，和普通编码代理的区别主要在于目标不是实现而是证明；andai 分享的“测试全绿但实现完全反向”经历也被用来说明通过检查不等于做对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-alphaproof-code/">Formal Verification of Signal’s Protocol with... — Google DeepMind</a></li>
<li><a href="https://google-deepmind.github.io/code-verification/">AlphaProof Code : Verifying Signal’s Security at the Machine- Code ...</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#AI coding agents`, `#Lean theorem proving`, `#Google DeepMind`, `#software correctness`

---

<a id="item-tech-news-3"></a>
### [Blender 5.3 发布：原生支持 Gaussian Splat 并增强几何节点](https://www.blender.org/download/releases/5-3/) ⭐️ 8.0/10

根据发布公告，Blender 5.3 已发布，新增 Gaussian Splat 支持，并增强了几何节点工作流。该版本面向使用 Blender 进行 3D 建模、渲染和视觉内容制作的用户。已提供的材料未列出 Gaussian Splat 支持的具体导入格式、性能数据或平台限制。

hackernews · amlib · 11月10日 16:15 · [社区讨论](https://news.ycombinator.com/item?id=50442426)

**「背景」** 3D Gaussian Splatting 是一种用大量高斯点表示并渲染重建三维场景的方法，graphdeco-inria 的仓库是其原始参考实现。Blender 5.3 的发布说明称，这类 splat 可作为点云导入，借助 Geometry Nodes 处理，并能在 Workbench 中预览、在 EEVEE 或 Cycles 中原生渲染。

**「影响」** 对已用 Gaussian Splat 做场景捕捉或可视化的用户，原生支持意味着可以在 Blender 内处理这类数据；但具体格式与兼容性尚未在材料中说明，迁移现有流程前应先验证导入和渲染结果。

**「社区讨论」** mturk 称几何节点中的 bundle 支持对复杂管线“意义重大”，并已通过 alpha 构建在实际工作流中使用；guidopallemans 报告在 M4 上测试约 400 万 splat 的 beta 场景时，认为集成成熟且速度很快。Retro\_Dev 则借 Gaussian Splatting 讨论 triangle splatting 的替代路线，认为 GPU 原生擅长三角形渲染，值得探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.blender.org/download/releases/5-3/">5 . 3 — Blender</a></li>
<li><a href="https://github.com/graphdeco-inria/gaussian-splatting">GitHub - graphdeco-inria/ gaussian -splatting: Original reference...</a></li>

</ul>
</details>

**标签**: `#Blender`, `#Gaussian Splatting`, `#3D graphics`, `#open source`, `#geometry nodes`

---

<a id="item-tech-news-4"></a>
### [Chips and Cheese 深潜 AMD Zen 6 架构](https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast) ⭐️ 8.0/10

Chips and Cheese 发布了一篇针对 AMD Zen 6 家族的技术深潜，聚焦核心设计、内存 I/O 和性能取舍，面向关注微架构细节的读者。现有材料只有分析摘要与评论、没有原文正文或 AMD 官方规格，因此文中具体改动与是否已上市无法独立核实。

hackernews · pixelpoet · 11月10日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=50443090)

**「背景」** Zen 6 是 AMD 继 Zen 5 之后的下一代 CPU 微架构。Chips and Cheese 此前测得 Zen 5 的方向预测器是其测试过的核心中表现最好的，而 Zen 6 沿用同一方向预测器，主要变化发生在预测器被压垮之后的处理方式上；此外，Zen 6c 采用与 Zen 6 芯粒相同的台积电 2nm（N2）工艺，做成纯 Zen 6c 的 CCD，将单 CCD 核心数提高到 32 个，片上 L3 缓存扩大到 128MB。

**「对调度与位操作代码的影响」** 对开发者和运维者最直接的影响是核心分组方式的变化：据 TechPowerUp 的 Zen 6 技术解析，Zen 6 采用 12 核 CCD、每核 4 MB L3，高于以往 8 核 CCD 的布局，因此按 CCD 边界做线程绑定、缓存分区或 NUMA 感知调度的既有假设需要重新校准。另一方面，社区评论引述文章数据指出，Zen 6 把整数乘法单元从 3 个减到 2 个，PDEP/PEXT 吞吐也从每周期 3 条降至 2 条；依赖这类位操作吞吐的压缩、哈希、位图类代码不能假定会随更宽的执行窗口线性提速，应在实际芯片上重新测量，而不要沿用 Zen 5 的调优结论。

**「社区讨论」** 评论者最关心内存 I/O：有人称 AM5 平台上 Zen 4/5 的 I/O 小芯片和内存控制器是明显短板，双通道很难超过 3600 MT/s，并期待 Zen 6 改用更小制程的新 I/O 小芯片。讨论还集中在取舍上——2-ahead 分支预测被认为很有意思，但有评论援引文章称整数乘法单元从 3 个减到 2 个、PDEP/PEXT 吞吐下降，并追问这是否在为 VNNI 等单元腾面积；32 核 CCD 如何对应最低 NUMA 层级也被提出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast">AMD ’s Zen 6 Family: Feeding the Beast - by George Cozma</a></li>
<li><a href="https://www.techpowerup.com/review/amd-zen-6-technical-deep-dive/">AMD Zen 6 Technical Deep Dive | TechPowerUp</a></li>
<li><a href="https://www.techpowerup.com/review/amd-zen-6-technical-deep-dive/">AMD Zen 6 Technical Deep Dive | TechPowerUp</a></li>

</ul>
</details>

**标签**: `#AMD Zen 6`, `#CPU microarchitecture`, `#semiconductor hardware`, `#branch prediction`, `#memory controllers`

---

<a id="item-tech-news-5"></a>
### [谷歌公开开放 Gemini 4 Carbon，12 月 API 价格将翻倍](https://deepmind.google/models/model-cards/gemini-4-carbon/) ⭐️ 8.0/10

谷歌已将 Gemini 4 Carbon 从面向“部分网络安全防御者”的受限发布扩展为面向公众开放，用户可通过 Gemini API、Google AI Studio 和 Gemini for business 使用。该模型主打网络安全与长时程智能体工作流，并覆盖复杂知识工作、软件工程和科学推理；谷歌还称其在 CursorBench 4.0 等基准上排名第一、成本比次优外部模型低 2 倍以上，但这些均为厂商说法。发布时价格为每百万 token 输入 2 美元、输出 10 美元，与 Argon 相同，并计划于 12 月 1 日翻倍至 4 美元和 20 美元。Antigravity 中同时提供 /swarm 多智能体协作预览。

telegram · zaihuapd · 11月10日 15:48

**「背景」** Gemini 4 Carbon 并非当天首次亮相的新模型：据来源引述的 Google 博客，它两周前先以受限方式提供给“部分网络安全防御人员”，今天才向其他所有用户开放。此次变化是把同一旗舰模型从面向安全防御者的早期开放，扩展到更广泛的公众和商业用户。

**「成本影响」** 开发者若现在接入并扩容长时程智能体工作流，应按 12 月 1 日起输入/输出价格从每百万 token 2/10 美元翻倍至 4/20 美元来核算成本，避免按首发价做长期预算。

**标签**: `#Google DeepMind`, `#Gemini 4 Carbon`, `#AI models`, `#agentic workflows`, `#API pricing`

---

<a id="item-tech-news-6"></a>
### [Synaptics 专利主张致 DisplayLink 驱动开发停止](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/) ⭐️ 7.0/10

据 LWN 报道，Synaptics 的专利主张已使 DisplayLink 驱动的开发工作停止，直接影响在 Linux 上依赖这些开源驱动连接 DisplayLink 扩展坞或适配器的用户和开发者。报道将此事件置于开源驱动开发与专利执法的冲突中，但现有材料没有说明受影响的具体驱动项目、专利范围或停止工作的详细条件。

hackernews · speckx · 11月10日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50443824)

**「背景」** DisplayLink 是一种通过 USB 连接外接显示器的技术，Linux 上的开源支持长期依赖社区逆向工程实现。据 Tom&\#x27;s Hardware 报道，一名开发开源 DisplayLink 驱动的爱好者此前收到 Synaptics 的停止侵权函，该公司声称该项目侵犯其专利并威胁提起诉讼；Phoronix 随后报道，这个仍在开发中的 Rust 内核驱动因法律威胁而从公开渠道消失。此次 LWN 报道的驱动开发停摆，正是在这一专利争议延续下发生的。

**「对开发者的直接影响」** 对 Linux 用户和独立开发者而言，最直接的后果是：这一开源 DisplayLink 驱动（Vino）的开发在收到 Synaptics 的停止侵权函后被迫中断，想要在 Linux 上通过单条 USB 连接驱动多台显示器的用户，只能继续依赖厂商提供的专有驱动和 SDK。对从事逆向工程的开发者来说，这份函件还附带追讨约 25,000 美元“文档整理费用”的威胁，这实际上把法律成本变成了个人开发者难以承受的门槛。

**「社区讨论」** 评论者普遍批评 Synaptics 的执法方式：有人称其索要 2.5 万美元以补偿“记录侵权行为的文档成本”是恐吓手段，并质疑反向工程应涉及商业秘密而非专利侵权。也有用户报告 DisplayLink 扩展坞曾造成音频故障，认为更新的 USB4/Thunderbolt 或 DisplayPort Alt Mode 支持已可替代；另有评论称 DDR 价格上涨正使 DisplayLink 方案失去经济性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation">Synaptics sends cease-and-desist order to creator of open - source ...</a></li>
<li><a href="https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver">Synaptics Appears To Use Legal Threats To Block Open - Source ...</a></li>
<li><a href="https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver">Synaptics Appears To Use Legal Threats To Block... - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation">Synaptics sends cease-and-desist order to creator... | Tom&#x27;s Hardware</a></li>

</ul>
</details>

**标签**: `#open-source`, `#patents`, `#DisplayLink`, `#Linux drivers`, `#hardware`

---

<a id="item-tech-news-7"></a>
### [Chrome 开源 modern-web-guidance 1.0 引导编码代理](https://github.com/GoogleChrome/modern-web-guidance) ⭐️ 7.0/10

Chrome 团队发布了开源项目 modern-web-guidance 1.0，面向使用编码代理的前端开发者，提供 200 多份、约 1.7MB 的手工整理 Web 平台指南，并与 Firefox、MDN 和 Edge 合作。该项目旨在让代理在实现对话框、文本高亮、自适应文本框等任务时优先使用 \`&lt;dialog&gt;\`、\`CSS.highlights\`、\`field-sizing\` 等原生能力，而不是默认采用 \`div\` 加 JavaScript 的旧模式。项目以 agent skill 和本地 CLI 形式分发，提供 \`search\` 与 \`legacy-scan\` 命令；发布帖称 \`legacy-scan\` 在留出仓库上的平均精度为 92%，其内部 200 项任务评测中代理通过率从无指南的 55% 升至有指南的 92%。这些评测数据由项目方公布，未提供独立复现。

hackernews · paulirish · 11月10日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=50443812)

**「背景」** 现代浏览器已原生支持 \`&lt;dialog&gt;\`、\`CSS.highlights\`、\`field-sizing\` 等能力，但编码代理的训练数据中，旧式 \`&lt;div&gt;\` 加 JavaScript 的写法更常见，因此模型即便知道这些 API，也往往不会默认选用。Chrome 团队为此将专家整理的平台最佳实践做成可供代理调用的技能与检索工具，并在 1.0 版本中与 Firefox、MDN 和 Edge 合作发布。

**「兼容性风险与落地建议」** 对于需要同时支持 Firefox 和 Safari 的项目，如果直接采纳指南中部分仅在 Chromium 稳定实现的特性（例如 CSS corner-shape），同一份样式表在不同浏览器中可能呈现不同结果：Safari 和 Firefox 会完全忽略该属性，回退为普通圆角。社区评论还列出了 @function、calc-size\(\) 等一长串“Chrome 稳定、其他浏览器未支持”的条目；因此，在按指南改造代码前，团队应逐个核对目标特性的支持范围，并要求 agent 同时给出回退方案；如果产品只针对 Chrome，则可以直接采用这些现代原语。

**「社区讨论」** HN 评论中，有人列出指南推荐但 Firefox 和 Safari 尚不支持的 \`CSS @function\`、\`text-fit\`、容器滚动状态查询等特性，质疑跨浏览器兼容性；也有人担心让 LLM 普遍遵循 Chrome 团队的指南会加剧浏览器厂商影响力失衡。另有评论建议用 GitHub Pages 发布可直接用 grep 搜索的 Markdown 索引，以降低安装依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/mikhailmogilnikov/how-i-brought-css-corner-shape-to-safari-and-firefox-cka">How I Brought CSS corner-shape to Safari and Firefox</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#web development`, `#browser standards`, `#open source`, `#LLM tooling`

---

<a id="item-tech-news-8"></a>
### [Meta 发布 Muse Ember：主打智能体任务的小模型，定价贴近 Haiku 与 Luna](https://simonwillison.net/2026/Nov/10/muse-ember/) ⭐️ 7.0/10

Meta AI 发布 Muse Ember 1.0，定位为面向智能体重复性工作的最小、最高效模型，用途包括工具调用、编码子任务、路由、信息抽取和长文档解析。价格方面，当提示不超过 20 万 token 时，其输入价格为每百万 token 0.10 美元、输出价格为每百万 token 0.50 美元，与 GPT-6 Luna（阈值 27.2 万 token）和 Claude Haiku 5.5（阈值 10 万 token）在短提示档位完全一致；缓存输入价格为每百万 token 0.004 美元，低于后两者的 0.01 美元。超过阈值后，其价格升至输入每百万 token 0.30 美元、输出每百万 token 1.50 美元，因此在超长提示场景下反而比 Luna 所属的较高档位更贵。模型提供 minimal、low、medium、high、xhigh、max 六档推理级别。

rss · Simon Willison · 11月10日 07:28

**「背景」** Muse Ember 属于 Claude Haiku、GPT-6 Luna 所在的小型高效模型类别，这类模型主要承担智能体反复执行的工具调用、路由、抽取和文档解析等任务，而不是最重的推理负载。由于不同模型的推理 token 消耗差异很大，单纯比较每百万 token 价格难以反映实际成本，Artificial Analysis 的“每任务成本”和 Intelligence Index 因而成为文中判断性价比的参照。

**「对开发者的影响」** 按 Artificial Analysis 的 Intelligence Index vs. Cost per Task 图，Muse Ember 的 xhigh 与 max 两档分别以约 0.12 和 0.14 美元的单任务成本落在帕累托前沿上，智能指数约为 34 与 36；作为对比，Claude Haiku 5.5 的 xhigh 档成本约 0.25 美元，分数约 34.5，明显偏离前沿。Meta 声称该模型位于完整榜单的效率前沿，但这一说法来自厂商。作者实测也提示选择推理档位时不能只看档位名称：“high”档未能返回完整 SVG，各档位的推理强度与最终输出质量并没有清晰对应。

**标签**: `#AI models`, `#Meta AI`, `#model pricing`, `#efficient inference`, `#agents`

---

<a id="item-tech-news-9"></a>
### [Apiiro：Claude Code 设置文件致 2539 个凭据泄露](https://www.ithome.com/1/024/888.htm) ⭐️ 7.0/10

安全公司 Apiiro 发现，1,994 个 GitHub 代码库中存在 2,539 个真实凭据，包括数据库密码和 API Token，这些泄露与 Claude Code 的本地设置文件被提交有关。研究称，超过 10 万份 Claude Code 本地设置文件被上传至公共仓库，其中约 1,100 份含机密数据。问题源于 Claude Code 会把获准执行的 Shell 命令写入本地设置文件；如果该文件没有被 Git 忽略，就会随项目一起提交。Claude Code 团队表示正在研究预防措施，并考虑加入内置密钥扫描功能。

telegram · zaihuapd · 11月10日 11:20

**「背景」** 问题机制与 Claude Code 的本地权限设置有关：当用户选择“不再询问”时，工具会把获准执行的 Shell 命令写入 \`.claude/settings.local.json\`，该文件若未被 Git 忽略，就会随项目提交。Apiiro 在 2026 年 11 月 5 日公布的扫描显示，公共 GitHub 上有 104,185 份该文件、分布在 103,617 个仓库，其中 1,122 份至少包含一个密钥；这为本次发现提供了背景，但两者统计口径不同。

**「开发者应对」** 使用 Claude Code 的开发者应检查本地设置文件是否已被提交到仓库，将其加入 .gitignore，并轮换已经暴露的数据库密码和 API Token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dailysecurityreview.com/cyber-security/apiiro-finds-1994-github-repos-leaking-secrets-via-claude-code-files/">Apiiro Finds 1,994 GitHub Repos Leaking Secrets via Claude ...</a></li>
<li><a href="https://dev.to/madnessbrains_i/apiiros-claude-code-scan-found-2539-secrets-in-claudesettingslocaljson-local-desktop-tools-9ho">Apiiro’s Claude Code Scan Found 2,539 Secrets in .claude ...</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#凭据泄露`, `#GitHub 安全`, `#AI 编程工具`, `#密钥扫描`

---

<a id="item-tech-news-10"></a>
### [Fireworks 确认新攻击：客户账单、模型权重与数据集外泄](https://finance.sina.com.cn/stock/usstock/c/2026-11-10/doc-iniyfzhx2605532.shtml) ⭐️ 7.0/10

Fireworks 确认遭遇新一轮黑客攻击，部分客户的账单信息、模型权重和数据集外泄，并正与 Palo Alto Networks 旗下 Unit 42 联合调查。Harvey 表示其客户数据未受影响，但其他客户及终端用户是否受影响仍不清楚。知情人士称，部分年付数百万美元的大客户正考虑迁移；Fireworks 今年 7 月年化营收已达 10 亿美元，原计划本周启动目标估值至少 300 亿美元的新一轮融资。报道未披露攻击的技术细节，也未说明外泄数据的具体范围。

telegram · zaihuapd · 11月10日 13:00

**「背景：10 月事件与 11 月更新」** 这起事件是 Fireworks 10 月安全事件的延续：当时的披露仅涉及凭据外泄，11 月 9 日的更新则把影响范围扩大到客户账户信息、账单记录、数据集和不完整的模型权重（据 Fireworks 官方安全公告与 Cybersecurity News 报道）。据 Cybersecurity News 报道，攻击者是通过第三方云服务商进入 Fireworks 的开发机器的。

**「影响与应对」** 对在 Fireworks 上托管专有模型或数据集的客户来说，最直接的风险是模型权重和数据集外泄后难以撤回；这些客户应尽快确认自己的资产是否在受影响范围内，并检查账单异常和访问记录。已有多家年付数百万美元的大客户考虑迁移，因此采购方在续约时应把供应商的事件响应能力以及客户资产隔离承诺纳入评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fireworks.ai/security/bulletins/october-2026-security-incident-update">Update on October 2026 security incident | Fireworks AI</a></li>
<li><a href="https://cybersecuritynews.com/fireworks-ai-data-breach/">Hackers Breach Fireworks AI Through Third-Party Cloud ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#security breach`, `#Fireworks AI`, `#customer data`, `#model weights`

---

<a id="item-tech-news-11"></a>
### [Anthropic 改白名单制：中国大陆及港澳不在支持地区名单](https://www.anthropic.com/legal/supported-regions) ⭐️ 7.0/10

Anthropic 发布《支持地区政策》，把 Claude 产品的可用范围从原来的判断方式改为白名单制：Claude.ai、Claude Code、Cowork、API，以及通过云平台和授权经销商提供的 Claude 模型，仅限名单所列的 185 个国家和地区使用，未列入者一律不支持，政策于 11 月 12 日生效。据转述该政策的 Telegram 帖文，中国大陆、香港、澳门均不在名单内，中国台湾在列；乌克兰则排除克里米亚、顿涅茨克、赫尔松、卢甘斯克、扎波罗热五个地区。除名单外，政策还列出三条禁止：人身处不支持地区时使用即属违规，包括支持地区公司员工出差；在不支持地区注册或设总部的实体及其人员使用违规，不论当事人身处何地；被不支持地区主体直接或间接多数持股或控制的公司，其人员同样违规。帖文同时指出，伊拉克、利比亚、索马里、苏丹、巴勒斯坦等在美国制裁框架下受限的地区反而在名单内，说明该名单依据的是 Anthropic 自身的合规标准。以上内容来自二次转述，具体条款以官方政策页面为准。

telegram · zaihuapd · 11月10日 13:44

**「政策背景」** Anthropic 的《支持地区政策》是一份按国别逐一列举可用范围的政策文本，官方措辞是产品与服务（含 Claude.ai、Claude Code、Cowork、API 及开发者平台）「仅在下列列出的国家和地区可用」，也就是说，名单之外的地区默认不在服务范围内，并非先默认开放、再逐一排除。据 ChainCatcher 报道，此次是同一政策的更新版本，新版本自 11 月 12 日起生效。

**「影响」** 对使用 Claude 的开发者与组织而言，限制不只取决于访问时所在的网络位置，还取决于实体注册地、总部所在地和股权控制关系。因此，在不支持地区注册或被其主体多数持股的团队，即使成员常驻支持地区，也需要重新评估账号与订阅的合规性；支持地区企业的员工前往中国大陆及港澳等地出差期间继续使用，按该政策同样构成违规。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/legal/supported-regions">Supported Regions Policy - Anthropic</a></li>
<li><a href="https://www.kucoin.com/news/flash/anthropic-updates-regional-policy-users-in-china-and-china-controlled-entities-banned-from-using-claude">Anthropic Updates Regional Policy: Users in China and China ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI access policy`, `#regional restrictions`, `#compliance`

---

<a id="item-tech-news-12"></a>
### [稀宇科技开源 MiniMax H3 Image，称约 10 秒生成 4K 图像](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) ⭐️ 7.0/10

稀宇科技发布并开放 MiniMax H3 Image 图像模型权重，支持文生图、图像参考和图像编辑，已上线 Hugging Face 及开放平台 API，并接入 MiniMax Code、海螺等产品。官方称该模型可在约 10 秒内生成 4096×4096、约 1600 万像素的 4K 图像，最多接受 16 张参考图，重点提升复杂指令理解、多图参考和画面细节。同步推出的 Highspeed 高速版被官方称为标准模式速度约为主流工具的 1.5 至 2 倍、高速模式为 3 至 4 倍。价格方面，标准版 4K 单张约 0.069 美元，发布首周优惠价约 0.034 美元；上述生成速度和倍率均为厂商说法，尚未见独立验证。

telegram · zaihuapd · 11月10日 15:39

**「背景」** 开放权重意味着模型参数可供下载和自行部署，而不只是通过厂商 API 调用；文生图、图像参考与图像编辑则分别指从文本生成图像、以输入图作为条件生成，以及修改现有图像。4K 在这款模型中具体指 4096×4096 分辨率、约 1600 万像素的输出，十秒级耗时是官方公布的数据，尚待独立验证。

**「接入与许可」** 开发者现在可以从 Hugging Face 获取 MiniMax H3 Image 的权重，并自行部署，也可以通过开放平台 API、MiniMax Code 和海螺调用；但官方发布采用社区许可，而不是宽松的开源许可，商用集成前需先核对条款。成本方面，标准版生成单张 4K 图像约需 0.069 美元，发布首周优惠价约为 0.034 美元，接入方应按调用量评估预算。此外，最多 16 张参考图的输入会直接影响显存占用和推理时延；约 10 秒生成 4K 图像的速度目前仅为官方口径，尚未见到独立测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3-image">MiniMax H 3 - Image : Bringing 4 K Image Generation into the...</a></li>
<li><a href="https://news.sulat.com/2026/11/11/minimax-releases-h3-image-open-weights/">MiniMax releases H 3 - Image as open weights - Sulat AI &amp; Tech News</a></li>

</ul>
</details>

**标签**: `#AI image generation`, `#open-weight models`, `#MiniMax`, `#4K generation`, `#model release`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [AI 时代，胶水工作仍然有害](https://seangoedecke.com/glue-work-is-still-harmful-in-the-age-of-ai/) ⭐️ 5.0/10

rss · Sean Goedecke · 11月11日 00:00

**「背景」** Sean Goedecke 一直认为，靠工程师无偿牺牲维持的流程本就该被淘汰；在 LLM 承担大部分编码之后，他进一步主张，“胶水工作”对企业的重要性不升反降。

**「方案」** 作者给出四点理由：AI 代理放大了单个工程师的能力，许多原本需要小团队的项目现在一个人就能推进，因此订会议、传状态等协调型胶水工作随之减少；2020 年代的工程师更不需要被“小心伺候”，ZIRP 结束后，一些爱否决项目的强势守门人被迫离开行业或改变态度；企业少招初级工程师，也就少了自愿带新人的隐性工作；而“证明自己在干活”的只写不读报告，可以直接交给 LLM 生成，反正原本也没人读。但他强调，这绝不意味着胶水工作可以全部自动化：与同事沟通、确认项目状态、回复消息必须亲自写，让别人面对你的 Claude Opus 实例会迅速毁掉关系。他的建议与 2024 年一致：不要成为“胶水工作的人”，让坏流程失败，只在能实质推动项目时做少量战术性胶水工作，把主要精力放在写代码和驾驭 AI 代理上。

**「启示」** 文章的核心判断是，LLM 削弱而非复兴了胶水工作的价值；真正稀缺的仍是能推动代码与 AI 代理落地的工程师，而不是靠无偿协调维系坏流程的人。

**标签**: `#glue work`, `#software engineering career`, `#LLM impact on engineering`, `#organizational dynamics`, `#engineering management`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Polymarket 称年化收入突破 18 亿美元](https://www.cnbc.com/2026/11/10/polymarket-annualized-revenue-us-growth.html) ⭐️ 7.0/10

预测市场平台 Polymarket 于周二向 CNBC 表示，其年化收入已超过 18 亿美元，高于该公司 6 月披露的逾 10 亿美元年化收入。公司称，增长主要由今年 5 月上线的美国交易所推动；据数据平台 TickerTracker 统计，该交易所 10 月名义交易量超过 145 亿美元，而 6 月为 40 亿美元。

rss · CNBC Finance · 11月10日 13:00

**「背景」** 所谓“年化收入”是把近期收入按全年折算出的运行速率，用来观察增长势头，而非已经完成的全年业绩；Polymarket 在 6 月披露的这一数字已超过 10 亿美元，当时其美国交易所刚于 5 月上线。据 CNBC 报道，美国商品期货交易委员会（CFTC）早在今年 6 月就已对 Polymarket 展开广泛调查，相关监管压力延续至今。

**「受影响方」** 美国州级监管机构与联邦上诉法院正就体育类合约究竟属于“互换”还是“博彩”产生分歧（tool-2-3），而 Polymarket 本轮交易量增长主要来自世界杯、NFL 等体育事件合约，因此这一裁定结果将直接决定其美国交易所能否继续依靠此类产品扩张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.politico.com/news/2026/06/26/cftc-investigation-prediction-market-polymarket-00978218">Wall Street regulator investigating prediction market giant ...</a></li>
<li><a href="https://www.cnbc.com/2026/06/26/cftc-is-conducting-an-investigation-into-polymarket-source-says.html">CFTC is conducting an investigation into Polymarket ... - CNBC</a></li>
<li><a href="https://financefeeds.com/prediction-markets-cftc-state-regulation-2026/">Prediction Markets Hit $410B as CFTC and States Clash</a></li>

</ul>
</details>

**标签**: `#Polymarket`, `#prediction markets`, `#revenue growth`, `#CFTC investigation`, `#startup funding`

---

<a id="item-finance-news-2"></a>
### [美联储理事沃勒：倾向 12 月加息，若通胀超预期可考虑 50 个基点](https://www.cnbc.com/2026/11/10/fed-governor-waller-sees-december-hike-likely.html) ⭐️ 7.0/10

美联储理事沃勒表示，他倾向于在 12 月加息，并称若通胀读数高于预期，应考虑在 12 月会议上加息 50 个基点；同日公布的 10 月 CPI 总体上涨 0.4%、核心 CPI 上涨 0.3%，均比道琼斯共识预期高 0.1 个百分点。

rss · CNBC Finance · 11月10日 17:13

**「背景」** 美联储在 10 月会议上未加息，9 月已加息 25 个基点；10 月 CPI 高于预期，使官员继续权衡是否需要进一步收紧政策。

**「影响」** 交易员在 CPI 数据后已完全计入 12 月加息 25 个基点，但仅赋予 50 个基点约 12.5%的概率，显示市场对更大幅度收紧的预期仍低。

**标签**: `#monetary policy`, `#Federal Reserve`, `#interest rates`, `#inflation`, `#CPI`

---

<a id="item-finance-news-3"></a>
### [前三季度中国新能源乘用车出口同比增长 138.8%](https://finance.sina.com.cn/tech/roll/2026-10-26/doc-iniwpfnc2438186.shtml) ⭐️ 7.0/10

2026 年前三季度，中国新能源乘用车出口 388.7 万辆，同比增长 138.8%；同期国内零售量为 775.8 万辆，同比下降 12.8%。

telegram · zaihuapd · 11月10日 02:56

**「背景」** 2026 年起，新能源车购置税由全额免征改为减半征收，实际税率为 5%，免税上限从 3 万元降至 1.5 万元；叠加购车补贴退坡，这被认为是中国国内新能源车零售走弱的政策背景。

**「影响」** 对依赖国内零售的车企和经销商而言，国内需求走弱意味着销售压力加大，而出口成为部分车企销量增长的重要支撑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chejiahao.m.autohome.com.cn/info/24720031">车 市开 年 遇冷！ 2026 补 贴 退 坡 ，1月销量断崖式下滑_ 车 家号_汽 车 之家</a></li>
<li><a href="https://m.dzplus.dzng.com/share/general/0/NEWS2979460TOELOPBZCWQEN">m.dzplus.dzng.com/share/general/0/NEWS2979460TOELOPBZCWQEN</a></li>

</ul>
</details>

**标签**: `#中国新能源车出口`, `#国内汽车零售`, `#乘用车市场`, `#购车补贴与购置税`, `#行业数据`

---

<a id="item-finance-news-4"></a>
### [Anthropic 撤回最高拟募 693 亿美元的 IPO 文件](https://www.reuters.com/business/anthropic-aims-raise-up-693-billion-blockbuster-ipo-2026-11-10/) ⭐️ 7.0/10

Anthropic 撤回了一份证券文件。该文件显示，公司拟以每股 70 至 80 美元发行约 8.67 亿股 A 类股，最高募资 693 亿美元；公司随后发邮件称定价信息不准确，表示将更新文件并拒绝进一步置评。

telegram · zaihuapd · 11月10日 06:25

**「背景」** 这份文件是 Anthropic 向银行传阅的 IPO 材料，路透社称其在周一晚间被短暂传阅后撤回；Anthropic 表示定价信息不准确，并将更新文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/anthropic-aims-raise-up-693-billion-blockbuster-ipo-2026-11-10/">EXCLUSIVE: Anthropic’s nearly $70 billion IPO plan briefly ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI financing`, `#private placement`, `#capital markets`

---

<a id="item-finance-news-5"></a>
### [台积电 10 月营收 5868.9 亿新台币，同比增 59.7%](https://pr.tsmc.com/chinese/news/3349) ⭐️ 7.0/10

台积电公布 2026 年 10 月合并营收约 5868.9 亿新台币，同比增长 59.7%；1 至 10 月累计营收约 4 兆 4856 亿新台币，同比增长 43.3%。

telegram · zaihuapd · 11月10日 08:07

**「背景」** 台积电每月公布合并营收，这是公司例行经营数据披露。

**标签**: `#台积电`, `#半导体`, `#月度营收`, `#台湾股市`

---