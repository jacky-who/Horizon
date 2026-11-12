---
layout: default
title: "Horizon Summary: 2026-11-12 (ZH)"
date: 2026-11-12
lang: zh
---

> 从 48 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [用电压毛刺解锁矿卡中的 A100 级功能](#item-tech-news-1) ⭐️ 8.0/10
2. [AWS 发布官方本地模拟器 aws-emulator，由 AI 代理编写](#item-tech-news-2) ⭐️ 7.0/10
3. [WSJ 头条称 Nvidia 准备罢免黄仁勋，细节缺位](#item-tech-news-3) ⭐️ 7.0/10
4. [误报烟雾报警险些拖垮 Jane Street 纽约唯一数据中心](#item-tech-news-4) ⭐️ 7.0/10
5. [线性规划能否用于语言模型权重空间编程？](#item-tech-news-5) ⭐️ 7.0/10
6. [谷歌发布 Gemini Decisions API，支持多模态决策](#item-tech-news-6) ⭐️ 7.0/10
7. [Python 核心开发者 Tim Peters 去世](#item-tech-news-7) ⭐️ 7.0/10
8. [Anthropic 路演视频披露 Claude 多芯片策略](#item-tech-news-8) ⭐️ 7.0/10
9. [字节跳动筹备类 Muse 智能体，拟 2030 年前追平 OpenAI](#item-tech-news-9) ⭐️ 7.0/10
10. [The Information 调查：Alice Huang 涉助 24 万颗英伟达芯片入华](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [古尔斯比称 10 月通胀报告“近乎令人不安”，美联储 12 月加息幅度受关注](#item-finance-news-1) ⭐️ 8.0/10
2. [离岸信托收益征税过渡期结束 累计申报个税超 1600 亿元](#item-finance-news-2) ⭐️ 8.0/10
3. [阿里巴巴拟分拆半导体子公司平头哥赴港上市](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [用电压毛刺解锁矿卡中的 A100 级功能](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) ⭐️ 8.0/10

一篇硬件破解博客称，它通过电压毛刺（voltage glitching）解锁了一块矿卡中被禁用的 A100 级功能；评论者认为目标卡是 8GB 版 CMP 170HX。帖子把关键步骤放在对显卡的物理故障注入和熔丝限制上，而不是常规固件或驱动修改。现有材料只有作者叙述与社区讨论，尚不能证明该方法能稳定复现或投入日常计算。

hackernews · lae · 11月11日 10:48 · [社区讨论](https://news.ycombinator.com/item?id=50451903)

**「背景」** 电压毛刺属于故障注入：在芯片执行关键判断的瞬间短暂扰动供电，使预设的硬件限制失效。文章针对的是 NVIDIA CMP 170HX 8GB 采矿卡，它与 A100 数据中心卡出自同一颗 GA100 芯片；NVIDIA 通过熔丝配置区分产品并屏蔽功能，因此要绕过的关键是 GA100 的熔丝控制器。

**「影响」** 对想复现的 CMP 170HX 持有者，门槛在于对目标卡进行受控上电、复位和电压毛刺，并承担损坏硬件的风险；这更像一次单卡实验，而不是可直接部署的解锁工具。

**「社区讨论」** 评论者一方面惊叹把 80GB HBM 焊到芯片上却只启用一小部分，另一方面有人报告自己用软件方式解锁 CMP 170HX 的 80GB 两周未果，认为熔丝方案风险更高；还有人建议用外置 PCIe 转接和独立电源，只循环目标卡而让主机保持运行。另有评论猜测这些熔丝可能用于屏蔽存在制造缺陷、无法做成完整 A100 的芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/">Using voltage glitching to unleash the A 100 in my mining card</a></li>

</ul>
</details>

**标签**: `#voltage glitching`, `#GPU hardware hacking`, `#NVIDIA A100`, `#mining cards`, `#hardware security`

---

<a id="item-tech-news-2"></a>
### [AWS 发布官方本地模拟器 aws-emulator，由 AI 代理编写](https://github.com/aws/aws-emulator) ⭐️ 7.0/10

AWS 在 GitHub 上发布官方 aws-emulator，让开发者在本地运行其多项服务的克隆进行测试，无需配置付费 API key。项目用 Rust 编写，AWS 博文称其由自主 AI 代理构建，前三周产生了 29,684 次提交；目前 macOS 和 Windows 上仍需 Docker 运行。AWS 安全说明明确警告不要用它测试 IAM 策略、资源策略、KMS 密钥策略、跨账户或跨区域访问以及其他安全控制，因为模拟器不会按 AWS 的方式执行这些检查。

hackernews · super\_linear · 11月11日 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50456631)

**「背景」** 有评论提到，本地测试 AWS 服务此前常借助 LocalStack、Floci 等第三方模拟器，或通过 Testcontainers 把这类工具接入测试流程。该条目称 AWS 终于推出官方本地模拟器，使开发者可以直接针对本地服务副本运行测试，而不必主要依赖社区方案。

**「影响」** 团队若把它接入 CI，应只把通过结果当作服务行为兼容性信号，而不是授权或安全回归信号；安全相关断言仍需在真实 AWS 或独立策略检查中运行。macOS/Windows 的构建环境还必须提供 Docker，单文件二进制方案目前不可用。

**「社区讨论」** 评论者 CharlieDigital 质疑它究竟是实验还是会被长期维护的产品，并称 Floci 与 Testcontainers 已能满足其本地测试需求，且可覆盖 GCP 和 Azure。有评论者认为，正是自主 AI 代理让覆盖大量 AWS 服务的项目变得可行，并称这会削弱 LocalStack 等本地模拟器的优势；也有人批评 Rust 的可读性，但这属于主观评价。

**标签**: `#AWS`, `#cloud emulator`, `#AI coding agents`, `#developer tooling`, `#open source`

---

<a id="item-tech-news-3"></a>
### [WSJ 头条称 Nvidia 准备罢免黄仁勋，细节缺位](https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad) ⭐️ 7.0/10

《华尔街日报》发布了一条标题为“Nvidia 正准备罢免 CEO 黄仁勋”的报道，该链接于 2026 年 11 月 11 日在 Hacker News 上被广泛讨论。目前可获得的材料仅有这一标题及社区评论：没有报道正文、没有 Nvidia 或董事会的公开回应，也没有任何独立信源佐证，因此“准备罢免”的具体依据、时间表与推动者均无法核实。读者应将该说法视为尚未证实的报道，而非已发生或已确认的公司行动。

hackernews · jbredeche · 11月11日 22:31 · [社区讨论](https://news.ycombinator.com/item?id=50459703)

**「背景」** 英伟达是一家由创始人掌舵的公司；据《华尔街日报》两天前的报道，黄仁勋长期不设继任计划，这已被视为公司的一项风险。此次董事会动作紧接媒体披露其第二段婚外情之后；Semafor 援引《华尔街日报》的报道称，董事会最早可能在当天就罢免黄仁勋，消息传出后英伟达股价在盘后交易中下跌逾 8%，触及 52 周低点。

**「社区讨论」** 评论者的关注点集中在两点：一是治理结构，有人指出近年由创始人主导的科技公司普遍采用双层股权，创始人握有过半投票权，董事会实际上很难在其反对下将其罢免，因此 Nvidia 的情况是否不同成为讨论焦点；二是动因，有评论认为 Nvidia 作为美国关键战略资产，其高层变动更值得追问的是“什么催化剂打破了此前的保护”，并称相关传闻早在 2024 年就出现在亚洲媒体上。另有评论以假设的 NVDA 股东或员工视角发问应当支持还是反对换帅，也有人质疑谁能接替黄仁勋长期主导的技术路线。以上均为未经验证的个人观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad">Exclusive | Nvidia Is Preparing to Oust CEO Jensen Huang - WSJ</a></li>
<li><a href="https://www.semafor.com/article/11/11/2026/nvidia-board-preparing-to-oust-ceo-huang-wsj">Nvidia board preparing to oust CEO Huang: WSJ | Semafor</a></li>
<li><a href="https://www.wsj.com/tech/jensen-huang-doesnt-believe-in-succession-planning-its-become-a-big-risk-for-nvidia-abd9ea9d">Jensen Huang Doesn’t Believe in Succession Planning. It’s ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#AI hardware`, `#tech leadership`

---

<a id="item-tech-news-4"></a>
### [误报烟雾报警险些拖垮 Jane Street 纽约唯一数据中心](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/) ⭐️ 7.0/10

一篇第一人称复盘记录了 Jane Street 纽约唯一数据中心因误报烟雾报警而几乎被拖垮的经过，重点是报警触发后的现场应急操作。文章确认这是一次误报，但没有披露报警器型号、联动逻辑、断电范围或业务中断时长，因此故障边界仍不清楚。对运营关键数据中心的基础设施团队，这份材料可用于复盘告警、紧急断电和人工响应流程。

hackernews · mbac32768 · 11月11日 16:38 · [社区讨论](https://news.ycombinator.com/item?id=50455394)

**「背景」** 在数据中心，烟雾探测通常与消防抑制和空调系统联动：报警可能触发喷淋或气体灭火，并关闭空气处理设备，以防烟雾扩散。问题在于，关闭制冷会使高密度机柜迅速升温，而喷淋一旦启动又可能造成水损，因此一次误报也可能同时带来过热和灭火系统启动的风险。

**「社区讨论」** 评论者 rdl 质疑该数据中心为何没有至少一个物理紧急断电（EPO）按钮，也没有把 EPO 与烟雾报警联动；他认为这类配置在数据中心建设中通常属于规范要求。rainbowzootsuit 则补充说，他为数据大厅编写的操作序列会刻意避免在烟雾报警时关闭 CRAC，并援引《国际机械规范》中针对单一空间、2000 cfm 以上空气处理机的豁免规定，说明告警联动并非越自动越好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/">How a false smoke alarm almost drowned Jane Street ’s only NYC ...</a></li>

</ul>
</details>

**标签**: `#datacenter operations`, `#incident response`, `#reliability engineering`, `#infrastructure`, `#Jane Street`

---

<a id="item-tech-news-5"></a>
### [线性规划能否用于语言模型权重空间编程？](https://nathan.rs/posts/weight-space-lp/) ⭐️ 7.0/10

这篇博文探讨能否把线性规划用于语言模型的权重空间编程，即通过线性约束来编辑权重、抑制或保留特定行为。现有材料将其定位为探索性分析，而非已展示的突破或可直接使用的工具。评论者进一步讨论用 LP 求解器做稀疏权重编辑、权重空间蒸馏，以及在训练中通过正则化实现类似约束。

hackernews · emschwartz · 11月11日 12:30 · [社区讨论](https://news.ycombinator.com/item?id=50452655)

**「背景」** 线性规划是在一组线性约束下优化线性目标函数的数学方法。本文的直接前身是 MIT CSAIL 的《Sparks of Weight-Space Programming》：该工作讨论让 LLM 直接改动模型权重，而不只是优化提示词或外部程序。当前文章接着追问，权重编辑能否被表述为线性规划问题，从而用线性约束来挑选编辑方向。

**「对模型行为编辑者的实际影响」** 对做模型行为编辑的开发者来说，这篇分析提供的可操作思路是：把“压制某种行为、保留另一种行为”写成线性约束，再让 LP 求解器寻找稀疏的权重修改。但由于它仍属于探索性分析、尚无公开演示证明效果，更合理的定位是把它作为与微调或 RLHF 并列的待验证方案，而不是可直接替换现有流程的工具。

**「社区讨论」** 评论中，jsw97 认为 LP 求解器可作为受约束权重编辑的辅助工具，mirekrusin 则提议用成对样本发现行为方向、再以线性规划寻找稀疏权重编辑来做权重空间蒸馏。dansitu 认为这种简洁性说明类似机制应在训练时通过正则化实现，whatever1 则主张传统数学规划会取代或覆盖 RL 循环，以处理多目标下的严格约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nathan.rs/posts/weight-space-lp/">Can a Linear Program Do Weight - Space Programming ?</a></li>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>

</ul>
</details>

**标签**: `#linear programming`, `#weight-space editing`, `#LLMs`, `#model optimization`, `#machine learning`

---

<a id="item-tech-news-6"></a>
### [谷歌发布 Gemini Decisions API，支持多模态决策](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) ⭐️ 7.0/10

谷歌发布 Gemini Decisions API，基于新模型 Gemini Decision 1，面向工具选择、策略检查、模型路由等封闭式决策，支持是/否、选项和评分量表三类问题。该 API 可接收文本、图像、音频、视频和 PDF，单次最多提交 1000 个问题并返回概率与置信度；据发布信息，端到端延迟约 150–250 毫秒，现已在 Google AI Studio 提供。定价为每百万输入 token 0.10 美元、输出 token 免费，与 GPT-6 Luna 决策模型相同，但高于 Jev 的每百万 4.2 美分。Simon Willison 的实测显示，Gemini 对视频是否包含机器人等问题返回概率值，而不是 Jev 和 OpenAI 那样的 0 或 1。

hackernews · iamdelirium · 11月11日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50456791)

**「背景：什么是决策模型」** 决策模型 API 与常规聊天接口不同：它不返回自由文本，而是按预设的问题类型给出结构化答案，例如从多个选项中选一项、在有序评分量表上打分，或输出某个命题为真的校准概率。Jev 的 API 文档把这三类分别称为 choice、score 和 noul，并将 noul 定义为“命题为真的校准概率”。谷歌此次的 Gemini Decision 1 沿用了同一套问题类型和 Noul 这一术语，是在 Jev 与 OpenAI 之后进入这一类别。

**「影响」** 对需要音频、视频或 PDF 输入的开发者，Gemini Decisions API 可直接把这些媒体交给模型判断，但每百万输入 token 0.10 美元约为 Jev 4.2 美分的 2.4 倍；若只需文本或 JSON，低成本场景可能仍倾向 Jev。由于返回的是概率而非 0/1，接入方需要自行设定阈值并校准置信度。

**「社区讨论」** 评论者围绕成本与采用展开讨论：有人认为其支持音频和视频，因此在特定场景下虽贵于同类仍很有用；也有人询问决策模型在编码工具中的实际用法。另有评论注意到 Gemini 返回概率而非 0/1，并关心这些概率如何校准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jevmodel.org/api/">Jev API Examples: Choice , Score , and Noul Requests</a></li>
<li><a href="https://www.firecrawl.dev/blog/openai-decisions-api-vs-jev">OpenAI&#x27;s Decisions API vs Jev : Inside the Decision - Model Architecture</a></li>

</ul>
</details>

**标签**: `#Gemini API`, `#decision models`, `#Google AI`, `#developer tools`, `#LLM applications`

---

<a id="item-tech-news-7"></a>
### [Python 核心开发者 Tim Peters 去世](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028) ⭐️ 7.0/10

长期担任 CPython 核心开发者的 Tim Peters 去世，Python 社区论坛发布了讣告帖，帖中标明他的生卒年为 1952–2026。他以《Python 之禅》（可通过 \`import this\` 查看）和 Timsort 排序算法闻名，并参与 datetime 模块等 CPython 工作；这些成果仍被 Python 开发者直接使用。

hackernews · ayhanfuat · 11月11日 07:03 · [社区讨论](https://news.ycombinator.com/item?id=50450488)

**「背景」** 蒂姆·彼得斯（Tim Peters）是 CPython 的长期核心开发者；2002 年，他为 Python 实现了 Timsort，这是一种结合归并排序与插入排序的稳定混合排序算法（tool-2-1、tool-2-2）。在 Python 中执行 \`import this\` 会打印出他撰写的《Python 之禅》，这些格言长期被社区当作编码风格的参照。他的这两项工作都直接融入了日常 Python 使用，因此他的去世在开发者中引起了广泛悼念。

**「日常排序代码的直接依赖」** 对普通开发者而言，最直接的关联是每天调用的排序接口：Peters 于 2002 年为 Python 实现的 Timsort 至今仍是 Python 中 sorted\(\) 与 list.sort\(\) 的默认算法，并自 Java 7 起用于对象数组的 Arrays.sort。也就是说，即便从未读过《Python 之禅》，使用这些标准库排序的代码仍在依赖他的实现。

**「社区讨论」** 有评论者回忆，Tim Peters 与 Gary Robinson 等人把 pg 的《A Plan for Spam》一文变成了可用的 SpamBayes，并讨论 Robert Woodhead 等人也应分享功劳。另有读者提到他在《Python Cookbook》第二版中的讲解，以及他乐于把讨论引向更深入理解的交流风格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tim_Peters_%28software_engineer%29">Tim Peters (software engineer) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Timsort">Timsort - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Timsort">Timsort - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/timsort/">TimSort - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#Python`, `#open source community`, `#Timsort`, `#CPython`, `#obituary`

---

<a id="item-tech-news-8"></a>
### [Anthropic 路演视频披露 Claude 多芯片策略](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) ⭐️ 7.0/10

Anthropic 在 IPO 路演视频中披露了此前未公开的算力细节：Claude 的训练与推理已覆盖 AWS Trainium、Google TPU、NVIDIA GPU 和 AMD GPU 四大芯片家族。联合创始人 Tom Brown 称，公司早年押注多芯片路线，并为不同芯片维护各自的软件栈和推理栈；今年首次接入 AMD GPU 时，Anthropic 让 Mythos 尝试适配，结果三天内让 Claude 在 AMD 上跑起来，且基本没有人工干预，Claude 编写或移植了接近 100% 的 kernel。视频还提出用“物理算力 × 算力乘数”衡量总算力，并称乘数可以叠加，未来 Claude 可能自主发现算力乘数、走向递归自我改进。上述内容来自 Simon Willison 用 MacWhisper 提取的非官方转录，并非 Anthropic 官方文本记录。

rss · Simon Willison · 11月11日 15:11

**「背景」** Anthropic 的 Claude 一直跨多种芯片运行：Simon Willison 指出，公司此前发布的三起故障复盘就提到过只影响其 TPU 部署的 bug，这是多芯片策略的早期线索。视频中承担 AMD 移植工作的“Mythos”属于 Anthropic 的模型系列——据维基百科条目，2026 年 6 月 Anthropic 公开发布带防护措施的 Claude Fable 5 时，同步提供了受限访问的 Claude Mythos 5。

**「影响」** 对关注 AI 基础设施的团队而言，最直接的参照是芯片适配的人力成本：Anthropic 把接入新平台从“数十名工程师、数月工作”描述为“三天、基本无人干预”，若这一说法可复现，将改变团队在自研或采购加速器时的迁移评估。但视频未披露 Mythos 的具体方法、适配后的性能与稳定性数据，也没有第三方验证，外部团队目前只能将其视为供应商说法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI infrastructure`, `#IPO`, `#multi-chip`, `#compute strategy`

---

<a id="item-tech-news-9"></a>
### [字节跳动筹备类 Muse 智能体，拟 2030 年前追平 OpenAI](https://www.bloomberg.com/news/articles/2026-11-11/bytedance-prepares-muse-like-agent-in-push-to-close-ai-gap) ⭐️ 7.0/10

据彭博社报道，字节跳动计划在未来数周发布一款类似 Meta Muse 的 AI 助手，以巩固其在 AI 视频领域的领先地位，并借此缩小与美国顶尖实验室的差距。报道称，联合创始人张一鸣在内部全员会上向 AI 团队提出，至少要到 2029 或 2030 年才能在前沿领域与 Anthropic、OpenAI 比肩。字节跳动还将最多投入 700 亿美元打造 Seedance 视频 AI 平台，并表示不主张依赖模型蒸馏；上述内容均为报道披露的计划，产品尚未发布。

telegram · zaihuapd · 11月11日 12:31

**「背景」** 报道以 Meta 的 Muse 作为参照，但未说明 Muse 的具体能力，也没有交代字节跳动这款助手将具备哪些功能或采用何种技术路线。可确认的背景是，字节跳动已把 Seedance 视频 AI 平台作为重点业务，其追赶 OpenAI、Anthropic 的目标因此建立在先巩固 AI 视频优势的前提上。

**「影响」** 对于依赖 AI 视频工具的开发者与内容团队，字节跳动计划在数周内推出助手，并准备向 Seedance 视频平台投入最多 700 亿美元，这意味着市场上将多出一个需要实际评测的选项。但公司内部把追平 Anthropic、OpenAI 的时间定在 2029 至 2030 年，因此早期版本更适合按视频场景和具体工作流来选型，而不宜假定其已具备同等的通用智能体能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/bytedance-plans-to-launch-ai-video-assistant-in-coming-weeks-targeting-70-25554039">ByteDance Plans to Launch AI Video Assistant in Coming Weeks ...</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#AI agents`, `#AI video`, `#OpenAI`, `#AI industry`

---

<a id="item-tech-news-10"></a>
### [The Information 调查：Alice Huang 涉助 24 万颗英伟达芯片入华](https://www.tomshardware.com/tech-industry/policy/alice-huang-reportedly-instrumental-in-securing-over-usd7-5-billion-of-nvidia-ai-gpu-imports-during-three-year-relationship-with-jensen-huang-helped-move-240-000-banned-chips-into-china-mostly-h100-and-h200) ⭐️ 7.0/10

《The Information》的一项调查称，Alice Huang（黄乐）借助与英伟达 CEO 黄仁勋的关系，协助约 24 万颗受出口限制的英伟达 AI 芯片进入中国，主要为 H100 和 H200，涉及进口金额约 75 亿美元。报道点名上海世纪利通和新加坡 Megaspeed 等公司，称这些芯片在三年关系中通过相关渠道流转。上述内容仍属媒体调查的指控，源摘要未提供原始文件、交易明细，也未包含英伟达或监管机构的回应。

telegram · zaihuapd · 11月11日 14:41

**「此前的 Megaspeed 调查」** 美国对华 AI 芯片出口管制使 H100、H200 等高端 GPU 的输华渠道成为监管重点。此前《纽约时报》2026 年 11 月 9 日报道，美国商务部曾调查 Alice Huang（黄乐）领导的新加坡数据中心公司 Megaspeed，案件后来被移交司法部；Wccftech 也报道该调查涉及 AI 芯片走私，并称英伟达被指成为联邦调查的障碍。

**「潜在影响」** 若调查内容被监管机构采信，上海世纪利通、Megaspeed 等中间渠道及相应进口路径将成为美国出口管制执法的直接核查对象；依赖 H100/H200 的机构也需要更严格地核验供应商资质与最终用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/nvidia-intervened-federal-investigation-megaspeed-ai-chip-smuggling-probe/">NVIDIA Allegedly Became A Roadblock For Federal Investigation In...</a></li>
<li><a href="https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html">U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#export controls`, `#AI hardware`, `#China`, `#semiconductor industry`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [古尔斯比称 10 月通胀报告“近乎令人不安”，美联储 12 月加息幅度受关注](https://www.cnbc.com/2026/11/11/goolsbee-october-inflation-fed-rates-disturbing-distressing.html) ⭐️ 8.0/10

美国 10 月消费者价格指数（CPI）经季节调整后环比上涨 0.4%，高于经济学家预期，且为连续第三个月涨幅偏高；芝加哥联储主席奥斯坦·古尔斯比称这份报告“近乎令人不安”，美联储官员正在讨论 12 月是否加息以及是否一次加半个百分点。

rss · CNBC Finance · 11月11日 16:49

**「背景」** 美联储 9 月已加息 25 个基点，把利率目标区间提高到 3.75%-4%，10 月则维持不变；10 月核心 CPI（剔除食品和能源）约为 0.3%，达到理事克里斯托弗·沃勒此前所说、会让他考虑 12 月一次加息 50 个基点的条件。

**「影响」** 投资者方面，联邦基金利率期货目前一致预计 12 月会加息，但认为一次加息 50 个基点的概率只有 15%。

**标签**: `#Federal Reserve`, `#inflation`, `#interest rates`, `#monetary policy`, `#CPI`

---

<a id="item-finance-news-2"></a>
### [离岸信托收益征税过渡期结束 累计申报个税超 1600 亿元](https://www.news.cn/20261111/9bcce99c779b4a6197ff45bbbc3e4c50/c.html) ⭐️ 8.0/10

中国税务总局 11 月 11 日表示，离岸信托收益征税的 90 天过渡期已结束，累计申报个人所得税超 1600 亿元，其中 10 月当月入库超 1200 亿元，带动 10 月全国个人所得税收入同比增长近 90%。税务总局称，下一步对未主动申报或申报不实的将督促补缴、加收滞纳金，仍不改正的依法立案稽查。

telegram · zaihuapd · 11月11日 10:35

**「背景」** 这一过渡期源自财政部、税务总局 2026 年 7 月 24 日发布的 2026 年第 21 号公告：离岸信托历史欠税须在 90 天内主动申报缴纳，截止 10 月 22 日，期内完成申报缴税不加收滞纳金。

**「影响」** 未主动申报或申报不实的离岸信托收益受益人，将面临补缴税款、加收滞纳金，甚至被依法立案稽查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/zaihuapd/45068">在花 科技圈 – Telegram</a></li>
<li><a href="https://news.creaders.net/china/2026/10/20/3060337.html">截止前三 天 ，北京突然又打了6 个 补丁！ - 中 国 瞭望-万维读者网（电脑版）</a></li>

</ul>
</details>

**标签**: `#offshore trusts`, `#personal income tax`, `#tax enforcement`, `#China fiscal revenue`, `#wealth taxation`

---

<a id="item-finance-news-3"></a>
### [阿里巴巴拟分拆半导体子公司平头哥赴港上市](https://www.cnbc.com/2026/11/11/alibaba-pr.html) ⭐️ 7.0/10

阿里巴巴表示，港交所已同意其分拆半导体子公司平头哥（T-Head），公司计划将平头哥股份在香港公开发行，但还需获得港交所和中国证监会批准；相关文件未披露发行规模与上市日期。

rss · CNBC Finance · 11月11日 07:47

**「背景」** T-Head 是阿里巴巴旗下的芯片设计子公司，2018 年由阿里内部芯片开发团队与杭州中天微合并而成，主要设计处理器、AI 加速器和服务器芯片。

**「影响」** 若分拆上市获批，T-Head 将成为独立的港股芯片公司，投资者可间接或直接持有其股权，该公司也可通过公开市场融资；发行规模和日期尚未披露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.roboticsintl.com/companies/t-head">T-Head Semiconductor Co., Ltd. (Pingtouge) — Company Profile ...</a></li>
<li><a href="https://www.investing.com/news/stock-market-news/alibaba-advances-hong-kong-ipo-plans-for-chip-subsidiary-thead-5015307">Alibaba advances Hong Kong IPO plans for chip subsidiary T - Head ...</a></li>
<li><a href="https://www.scmp.com/business/companies/article/3373974/alibaba-chip-unit-t-head-files-hong-kong-ipo-plan-amid-chinas-ai-self-sufficiency-drive">Alibaba chip unit T - Head files for Hong Kong IPO amid China’s AI push</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#T-Head`, `#Hong Kong IPO`, `#semiconductors`, `#China tech regulation`

---