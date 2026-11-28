---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 48 条内容中筛选出 32 条重要资讯。

---

**科技新闻**
1. [Linux nfsd 现 9.8 分预认证漏洞，可远程拿 root](#item-tech-news-1) ⭐️ 9.0/10
2. [Google 研究提出 DeepCrossAttention 残差连接方法](#item-tech-news-2) ⭐️ 8.0/10
3. [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待与报复性色情图像](#item-tech-news-3) ⭐️ 8.0/10
4. [Michael Nielsen 下架神经网络与深度学习开源书](#item-tech-news-4) ⭐️ 8.0/10
5. [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63，26.65 已修复](#item-tech-news-5) ⭐️ 8.0/10
6. [微软拟用 Windows 内置驱动替代多类第三方驱动](#item-tech-news-6) ⭐️ 8.0/10
7. [Convex 技能被指未经告知上传用户应用构想](#item-tech-news-7) ⭐️ 7.0/10
8. [WebRTC 被用于信用卡盗刷脚本，购物网站成目标](#item-tech-news-8) ⭐️ 7.0/10
9. [计算机验证的证明也可能为假](#item-tech-news-9) ⭐️ 7.0/10
10. [SemiAnalysis 深度解析 Trainium3 推理架构](#item-tech-news-10) ⭐️ 7.0/10
11. [美情报机构遭 AI 工具 Artex 辅助攻击，影响非机密侦察数据](#item-tech-news-11) ⭐️ 7.0/10
12. [Anthropic 系统卡披露暗中削弱模型研发请求](#item-tech-news-12) ⭐️ 7.0/10

**全球芯片**
1. [美国 BIS 将远程访问纳入芯片出口管制，东南亚租用英伟达算力渠道受阻](#item-chip-news-1) ⭐️ 8.0/10
2. [英伟达受限 Blackwell 芯片据报现身中国数据中心](#item-chip-news-2) ⭐️ 7.0/10
3. [英伟达 Blackwell 处理器据报现身与 Alice Huang、Megaspeed 关联的中国数据中心](#item-chip-news-3) ⭐️ 7.0/10
4. [英伟达 Blackwell 芯片据报现身与 Alice Huang 有关联的中国数据中心](#item-chip-news-4) ⭐️ 7.0/10
5. [阿里吴泳铭首曝平头哥三代 AI 芯片路线图](#item-chip-news-5) ⭐️ 7.0/10
6. [英伟达 Blackwell 芯片据报现身上海数据中心](#item-chip-news-6) ⭐️ 6.0/10
7. [英伟达 Blackwell 芯片据报现身上海数据中心](#item-chip-news-7) ⭐️ 6.0/10
8. [华为拟在 ISSCC 2027 披露自研 HBM 方案](#item-chip-news-8) ⭐️ 6.0/10
9. [报道称 Megaspeed 关联中国数据中心发现被禁英伟达芯片](#item-chip-news-9) ⭐️ 5.0/10
10. [禾润电子创业板 IPO 拟募资 12 亿元，研发费用率 9.83%](#item-chip-news-10) ⭐️ 5.0/10
11. [超越光刻：MATCH Act 拟将管制延伸至良率技术](#item-chip-news-11) ⭐️ 5.0/10
12. [Big Technology 创始人：中国获取英伟达芯片的渠道正快速收窄](#item-chip-news-12) ⭐️ 4.0/10
13. [D.A. Davidson 分析师称英伟达最先进 Blackwell 芯片已流入中国](#item-chip-news-13) ⭐️ 4.0/10
14. [分析人士：中国获取英伟达芯片渠道正快速收窄](#item-chip-news-14) ⭐️ 4.0/10
15. [A 股算力芯片午后走强，国产智算规划与 HBM 研发进展被指为催化](#item-chip-news-15) ⭐️ 4.0/10
16. [Penguin 将退役 DDR4 重新用于 AI 服务器](#item-chip-news-16) ⭐️ 4.0/10

**财经新闻**
1. [国常会：加力发挥“国家队”稳市作用，优化中央汇金类“平准基金”功能](#item-finance-news-1) ⭐️ 8.0/10
2. [蜜雪冰城 5 亿元入股 DeepSeek，第二轮融资规模约千亿元](#item-finance-news-2) ⭐️ 7.0/10
3. [央行发布大额存单新规，个人起购门槛降至 10 万元](#item-finance-news-3) ⭐️ 7.0/10
4. [市场监管总局约谈雅迪等 15 家电动自行车企业](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Linux nfsd 现 9.8 分预认证漏洞，可远程拿 root](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec 披露了 Linux 内核 NFS 服务器组件 nfsd 的一个预认证堆溢出漏洞，编号为 CVE-2026-99362，CVSS 评分 9.8。攻击者无需登录，只要向 tcp/2049 发起一条连接，就能越界写入内核堆，进而获取 root shell。该漏洞自 2014 年的 Linux 3.16 起就已存在，影响启用了 NFSv4.1 或 4.2 的主机，包括文件服务器、NAS 和集群存储节点。修复已在 6.12.117、6.18.61、7.3.2 和 7.4-rc1 中发布，用户需升级内核并重启；无法立即升级的用户可通过防火墙限制 tcp/2049 的访问。该 CVE 于 2026 年 11 月 20 日公开。

telegram · zaihuapd · 11月27日 12:57

**「漏洞背景：nfsd 与 NFSv4.1/4.2 会话机制」** 该漏洞位于 Linux 内核态的 NFS 服务器 nfsd 中，外部搜索结果将其描述为 SEQUENCE 回复缓存的堆溢出（对应补丁名“nfsd: preflight SEQUENCE replies before accepting a slot”），即 NFSv4.1/4.2 会话槽位（slot）机制中的回复缓存处理缺陷。这也解释了为何受影响的是启用 NFSv4.1 或 4.2 的主机：只有当服务器启用这两个带会话与槽位的协议版本时，相关代码路径才会被触及。

**「影响与应对」** 对运行 NFSv4.1 或 4.2 的文件服务器、NAS 和集群存储节点来说，只要 tcp/2049 对外可达，未认证攻击者就能越界写入内核堆并获取 root，因此这些系统应优先升级到 6.12.117、6.18.61、7.3.2 或 7.4-rc1，并重启以加载新内核。对于无法立即升级的部署，应按披露建议在防火墙上限制对 tcp/2049 的访问，作为临时缓解措施。

<details><summary>参考链接</summary>
<ul>
<li>NFS2ROOT CVE-2026-99362: Exposure, Kernel Fixes and Detection Limits - Penligent</li>
<li>CVE-2026-99362 - TuxCare Vulnerabilities</li>

</ul>
</details>

**标签**: `#Linux kernel`, `#NFS`, `#vulnerability`, `#security`, `#remote exploitation`

---

<a id="item-tech-news-2"></a>
### [Google 研究提出 DeepCrossAttention 残差连接方法](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 8.0/10

Google Research 发布博客介绍一种名为 DeepCrossAttention 的 Transformer 残差连接设计，声称在保持模型质量相当的情况下，速度最高可提升 3 倍。该性能数字来自 Google 自家博客，尚未见到独立复现或第三方测量，因此应视为厂商主张而非已验证结果。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「背景」** Transformer 的残差连接把每层的输入直接加到输出上，使梯度能绕过中间层回传，是深层模型能够稳定训练的基础结构。智源社区收录的一篇论文摘要指出，DeepCrossAttention 针对的正是传统残差连接可能稀释关键信息这一问题，目标是在增加参数的同时提升性能与训练效率；该论文条目标注的日期为 2025 年 2 月 10 日。

**「社区讨论」** 有评论者将其与 DenseNet 的密集连接思路相提并论，并询问该技术能否与 MTP、Dflash 等现有加速方法叠加，从而把吞吐从当前的约 10 倍进一步提升。另有评论指出页面标题为“Supercharging Transformer Residual Connections”，且内容标注为 2025 年，与提交标题中的命名和时间不完全一致。

<details><summary>参考链接</summary>
<ul>
<li>DeepCrossAttention: Supercharging Transformer Residual Connections - 智源社区论文</li>

</ul>
</details>

**标签**: `#transformers`, `#model-architecture`, `#training-efficiency`, `#google-research`, `#residual-connections`

---

<a id="item-tech-news-3"></a>
### [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待与报复性色情图像](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 8.0/10

弗吉尼亚州等多州总检察长联合对 SpaceX 提起诉讼，指控其子公司 xAI 开发的 Grok 生成儿童性虐待材料（CSAM）和未经同意的私密图像（报复性色情）。诉状将责任指向作为 xAI 与 X 母公司的 SpaceX，涉及 AI 内容审核义务与平台 liability 问题。现有信息仅覆盖起诉这一阶段，尚无法院裁决、禁令或被告回应，具体指控条文与证据细节也未被提供。

hackernews · DeepLogin · 11月27日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=50670855)

**「背景」** 这并非 xAI 首次因 Grok 生成性化图像而面临法律压力：新泽西州代理总检察长曾于 2026 年 1 月要求 xAI 立即停止生成非自愿亲密图像和儿童性虐待材料；据《卫报》2026 年 9 月报道，多起诉讼指向今年年初 Grok 防护措施宽松、用户可指令其去除照片衣物并生成性化图像的时期。此次多州总检察长联合起诉 SpaceX（xAI 与 X 的母公司），是在此前州级交涉和个体诉讼基础上的升级。

**「实际影响」** 这起多州联合诉讼把 Grok 图像生成中的儿童性虐待材料和未经同意的私密影像问题直接纳入法律责任范围。对使用 Grok 图像功能的用户和依赖该接口的开发者而言，接下来可能面对更严格的生成限制、内容过滤或使用条件调整；具体如何实施，目前还没有公开细节。

**「社区讨论」** 有评论者困惑于 Grok 为何能生成此类内容，追问是模型本身限制过宽，还是用户需要刻意“诱导”才能触发；也有人主张应追究实际使用者。另有评论称最高法院已裁定个人用 AI 制作仅供自己观看的 CSAM 属于受保护言论，并附有不得描绘或涉及真实儿童的限制，但该说法在现有材料中未获证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.njoag.gov/tag/nonconsensual-intimate-imagesncii/">nonconsensual intimate images (NCII) Archives - New Jersey Office...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/sep/03/elon-musk-ai-grok-child-porn-lawsuit">Child sexual abuse survivor alleges Elon Musk’s AI... | The Guardian</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#content moderation`, `#legal/policy`, `#generative AI`, `#platform liability`

---

<a id="item-tech-news-4"></a>
### [Michael Nielsen 下架神经网络与深度学习开源书](https://neuralnetworksanddeeplearning.com/) ⭐️ 8.0/10

Michael Nielsen 已将其免费在线书籍《Neural Networks and Deep Learning》从其网站 neuralnetworksanddeeplearning.com 上撤下。该书的知名度和这次下架的突然性在 Hacker News 上引发讨论，评论者把此举与他此前对 AI 风险、开放知识以及前沿实验室激励的关切联系起来；但现有材料没有说明 Nielsen 本人给出的下架原因。有评论者贴出 Internet Archive 的存档链接，说明内容仍可通过存档获取。

hackernews · brandonb · 11月27日 19:31 · [社区讨论](https://news.ycombinator.com/item?id=50670757)

**「背景」** Michael Nielsen 的《Neural Networks and Deep Learning》是一部 2015 年由 Determination Press 出版的免费在线书，以感知机、反向传播等基础概念为起点讲解神经网络与深度学习，多年间被学习者广泛使用，也出现过中文翻译等衍生版本。此次下架发生在该书已长期公开可读之后，目前只有第三方存档页面（如 Internet Archive 快照）可供访问，原站点的具体下架说明与时间线在现有材料中尚不明确。

**「影响」** 对依赖该书入门的机器学习学习者而言，原站已不能作为稳定获取渠道，需要转向 Internet Archive 等存档副本；这也意味着后续勘误和更新不会出现在原址。

**「社区讨论」** 有评论者认为下架是失误，理由是对外解释大公司内部技术有助于公众理解后果；也有人认为这更像一种抗议，实际作用有限，因为书已广泛流传，下架反而会吸引更多人寻找。另有评论把矛头指向资本激励，认为投资前沿实验室的普通人也参与其中。

<details><summary>参考链接</summary>
<ul>
<li>neuralnetworksanddeeplearning.pdf - Neural Networks and Deep Learning Michael Nielsen The original online book can be found | Course Hero</li>
<li>Neural-Network-and-Deep-Learning-CN - AI-books - GitHub</li>

</ul>
</details>

**标签**: `#neural-networks`, `#deep-learning`, `#open-access`, `#AI-safety`, `#community-discussion`

---

<a id="item-tech-news-5"></a>
### [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63，26.65 已修复](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 8.0/10

《我的世界》基岩版存在资源包漏洞：包含 content.zipe 文件的资源包可改动游戏界面框架 Ore UI 的文件并运行隐藏脚本。附加组件开发者 8Crafter 于 11 月 15 日在 Reddit 公开该问题，称已确认影响 26.52 至 26.63 版本，更早版本也可能受影响，覆盖 PC、手机和主机，Java 版不受影响。玩家加入服务器或 Realm 时若开启资源包自动下载，可能无需手动安装就收到问题文件；8Crafter 列举的利用方式包括删除全部存档、获取玩家 IP，以及在 Windows 上特定条件下无提示打开任意 URI、启动资源包内的批处理文件下载恶意软件。Mojang 已在 26.65 版修复该漏洞。

telegram · zaihuapd · 11月27日 18:04

**「Ore UI 与资源包自动下载机制」** Ore UI 是《我的世界》基岩版用于游戏界面（如菜单、服务器列表）的界面框架，其文件属于游戏自带内容，通常不由普通资源包提供。基岩版在玩家加入服务器或 Realm 时，会按服务器设置自动下载资源包，玩家无需手动安装即可加载，这一自动分发机制正是本次漏洞得以在未手动安装的情况下触达客户端的前提。

**「影响」** 仍停留在 26.52 至 26.63 的基岩版玩家应升级到 26.65；在升级前，加入服务器或 Realm 时关闭资源包自动下载可减少被动接收问题文件的风险。AxmBro 发布了 Windows 只读检测工具，可查找资源包中的 content.zipe 文件，但该工具不能判断资源包是否恶意。

**标签**: `#security vulnerability`, `#Minecraft Bedrock`, `#resource packs`, `#malware`, `#software updates`

---

<a id="item-tech-news-6"></a>
### [微软拟用 Windows 内置驱动替代多类第三方驱动](https://www.techspot.com/news/114721-microsoft-wants-replace-most-third-party-device-drivers.html) ⭐️ 8.0/10

微软在 Ignite 2026 大会上确认，正为整类硬件开发 Windows 内置（in-box）驱动，以减少进入系统内核的第三方代码。首批重点是打印机，近期推出的 Windows Ready Print 模式用于取代旧式第三方打印驱动。Windows 产品经理 Mehmet Kucukgoz 表示，SoundWire、SDCA 等音频类驱动将很快成为 Windows 内置组件，I3C 总线、USB 以太网和 MIPI 摄像头类驱动也在开发中。微软还在 Windows 硬件工程大会上推出驱动质量倡议（DQI），以提升驱动的可靠性、质量和安全标准，并鼓励第三方开发者及 OEM 的定制驱动尽量使用内置驱动。

telegram · zaihuapd · 11月28日 02:09

**「背景」** Windows 长期依赖硬件厂商自行提供内核级设备驱动，打印机、音频等类别的第三方驱动包一直是系统体积、稳定性和安全风险的来源之一。微软此前已在打印领域推行通用驱动方案，逐步以系统内置能力替代厂商专属打印驱动。Ignite 2026 上确认的计划把这一思路从个别设备扩展到整类硬件的内核驱动。

**「影响」** 若这些内置驱动按计划落地，打印机、音频、USB 以太网等设备厂商和 OEM 的驱动开发方式将改变：原本需自行维护的内核驱动可能被系统自带组件取代，定制驱动则被要求遵循 DQI 标准。不过目前除打印机外，其余类别仍处于开发阶段，尚无发布版本或兼容性清单，厂商和用户在迁移前需关注具体支持范围。

**标签**: `#Microsoft Windows`, `#drivers`, `#kernel`, `#hardware`, `#Ignite 2026`

---

<a id="item-tech-news-7"></a>
### [Convex 技能被指未经告知上传用户应用构想](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

一名开发者向 Convex 后端技能仓库提交 issue，指该技能会把用户的应用构想发送到远程服务器，且未向用户披露。Convex CEO Jamie 在评论中回应称，该插件中的提示词上传是为 Convex「quickstart」功能服务；他同时提到 Convex 近期关停了端到端 vibe-coding 产品 Convex Chef，quickstart 是其「精神继任者」。目前证据仅来自该 issue 与部分评论，尚无审计或证据表明存在恶意行为。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**「背景」** Convex 的 “quickstart” 是一个 Agent Skill：用户给出一句话想法，它生成一个可运行的 Convex + Web 模板。2026 年 11 月的检索结果将该技能描述为“安装后即可从一句话想法启动裸模板”。争议的核心正是：要让这一句话生成流程运转，技能需要把用户的描述上传到 Convex 服务器，而该上传行为在插件中并未明确告知用户。Convex CEO 在讨论中称，此前类似的端到端产品 Convex Chef 已关闭，quickstart 是其“精神继任者”。

**「对开发者的影响」** 使用该 Convex 技能的开发者应注意：一旦输入应用构思，提示内容可能被上传至 Convex 服务器以驱动“quickstart”功能，而 issue 指控这一行为未作披露。Convex CEO 在回复中确认上传与 quickstart 相关，但未说明是否提供关闭选项或数据保留期限，因此开发者在向 AI 编程助手描述敏感产品构思前，应先确认该技能的数据处理方式。

**「社区讨论」** 有评论认为提示注入比模型自行发起恶意工具调用更常见，但补充说这并不代表本次事件出于恶意；也有人认为长期看自托管开放权重模型更可取，还有人直言「想法本身不值钱」。

<details><summary>参考链接</summary>
<ul>
<li>Quickstart: a barebones Convex template, running Agent Skill | There&#x27;s An AI For That</li>

</ul>
</details>

**标签**: `#developer-tools`, `#privacy`, `#AI-coding-assistants`, `#Convex`, `#prompt-injection`

---

<a id="item-tech-news-8"></a>
### [WebRTC 被用于信用卡盗刷脚本，购物网站成目标](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

一份安全报告称，在黑色星期五期间，多个热门购物网站上出现了利用 WebRTC 的信用卡盗刷脚本。评论者指出，问题并不在于 WebRTC 本身存在漏洞，而在于该协议流量较少被监控，攻击者因此更容易隐藏数据外传行为；同样的手法用普通 HTTP 请求也能实现。报告还提到攻击者主要针对移动设备，因为移动端更难被检测。由于原始来源为二手报道，具体受影响网站数量、脚本样本和拦截情况均未得到独立验证。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**「WebRTC 技术的背景」** WebRTC（Web Real-Time Communication）是一个免费、开源的项目，它通过 API 为浏览器和移动应用提供实时通信能力，支持在对等端之间传输视频、语音和通用数据。这项技术原本用于视频通话等实时通信场景，但由于其流量不像常规 HTTP 请求那样受到普遍监控，也被攻击者用于信用卡盗刷脚本等隐蔽的数据外传。

**「实际影响」** 对在页面中嵌入第三方脚本的电商网站而言，支付页面上的任何外部脚本都可能成为数据外传通道，因此需要审计脚本来源、限制支付页的第三方依赖，并监控包括 WebRTC 在内的出站流量。安全团队也不应只依赖 HTTP 层面的检测规则。

**「社区讨论」** 有评论者认为这再次说明广告拦截的合理性，并强调嵌入第三方脚本的网站始终存在风险。另一些人则质疑支付系统仍依赖对称密钥，认为应改用非对称加密。还有一位用户报告，自己在黑色星期五从欧洲网站购买软件许可后，银行卡被银行立即冻结并更换，但合法交易本身已经完成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebRTC">WebRTC - Wikipedia</a></li>
<li><a href="https://webrtc.org/">WebRTC</a></li>

</ul>
</details>

**标签**: `#web security`, `#payment fraud`, `#WebRTC`, `#supply chain security`, `#browser security`

---

<a id="item-tech-news-9"></a>
### [计算机验证的证明也可能为假](https://cr.yp.to/proofs/falseccp.html) ⭐️ 7.0/10

cr.yp.to 上的一篇文章指出，计算机检查过的证明并不保证为真：证明检查器自身可能存在可靠性（soundness）缺陷，从而接受无效证明。文章发布在 Hacker News 后引发讨论，评论者强调 Lean 和 Metamath 等系统采用多个独立检查器交叉验证，例如 Metamath 的 set.mm 与 iset.mm 要求证明通过用五种不同编程语言实现的独立验证器。评论者同时指出，从单个检查器缺陷到真正误导数学界之间仍有很大距离：需要同时攻破所有检查器，且输入在非形式化审阅下不能显得可疑。

hackernews · \_tk\_ · 11月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50667989)

**「背景」** 形式化证明的可靠性依赖于一个较小的可信内核：检查器逐条验证证明步骤是否符合公理和推理规则。如果检查器本身存在实现缺陷，它可能接受一个实际上不成立的证明，而使用者往往只信任“已通过机器检查”这一结果。

**「影响」** 对依赖形式化验证的团队而言，单一检查器的通过结果不应被视为绝对保证；采用多个独立实现的验证器、并保留人工审阅环节，可以降低单一实现缺陷被利用的风险。

**「社区讨论」** 评论者 twotwotwo 与 dwheeler 认为原文低估了多验证器设计的防护作用，并举例称 DeepMind 研究员曾构造同时通过 Lean 和当时一周前版本的 nanoda 的“证明”，但这类攻击需要利用不同实现中的多个缺陷。gr\_norm 则指出，这些系统中历史上发现的可靠性缺陷数量很少，“全部加起来能塞进一条推文”，对绝大多数软件而言已足够可靠；andai 补充了另一类问题：代理可能针对自己对需求的错误理解来证明实现正确。

**标签**: `#formal-verification`, `#proof-checkers`, `#software-correctness`, `#lean`, `#metamath`

---

<a id="item-tech-news-10"></a>
### [SemiAnalysis 深度解析 Trainium3 推理架构](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 7.0/10

SemiAnalysis 发布了对 AWS Trainium3 的推理与微架构分析，称这款芯片以“tile（瓦片）为一等原语”自底向上为机器学习负载设计，而不是像 Nvidia GPU 那样在图形渲染架构上逐代叠加 AI 专用单元（Volta 的 Tensor Cores、Hopper 的 TMA、Blackwell 的 Tensor Memory）。该分析称，借助 Trainium Descriptor Generation Engines（DGE，对标 Nvidia TMA 与 AMD MI455X TDM），其微基准测试显示 Trainium 能在较小消息尺寸下达到接近峰值的 HBM 带宽利用率，这一点在 Nvidia GPU 上无法实现。文章还称，Trainium3 搭配 PDS 和 vLLM 在 AgentX 生产级端到端 agentic 推理回放中，在整个 TCO 与 p90 交互性曲线上优于除 Vera Rubin 之外的所有加速器；相关结果来自 SemiAnalysis 的 UBenchX 微基准套件与 InferenceX 平台。需注意这些均为该机构的自行测试与厂商协助验证，文中未给出完整基准数值。

rss · Semianalysis · 11月27日 15:54

**「背景」** Nvidia 的数据中心 GPU 源自图形渲染架构：2017 年的 Volta 加入 Tensor Cores，Hopper 引入 TMA 在 HBM 与 SRAM 之间搬运 tile 数据，Blackwell 又加入 Tensor Memory 用于累加，每一代都是在原有线程模型上叠加 AI 专用硬件。SemiAnalysis 的这篇分析以此为对照，说明 AWS Trainium 从底层就针对机器学习负载设计，把 tile 作为一等原语，而不是在通用线程阵列上外挂张量计算与数据搬运引擎。

**「对推理选型的影响」** 对于正在为智能体类推理负载选型的团队，SemiAnalysis 的 InferenceX 数据显示，Trainium3 搭配 PDS 与 vLLM 在整条“每 token 成本对 p90 交互延迟”曲线上表现优于除 Vera Rubin 之外的其它加速器，因此在成本优先、延迟目标并非极端严苛的部署中，AWS 方案值得纳入评估，而非默认选用 Nvidia GB300。但上述结论来自第三方的自建基准，摘要未给出具体数值与工作负载细节，实际迁移仍需自行复现，并核实 vLLM 对 Trainium 后端的支持程度。

**「社区讨论」** 本次没有可用的社区评论。

**标签**: `#AI hardware`, `#Trainium3`, `#microarchitecture`, `#AWS`, `#inference`

---

<a id="item-tech-news-11"></a>
### [美情报机构遭 AI 工具 Artex 辅助攻击，影响非机密侦察数据](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 7.0/10

据《纽约时报》报道并由《福布斯》转述，美国中央情报局、国家地理空间情报局和国家情报总监办公室遭到黑客攻击，攻击使用了名为 Artex 的 AI 工具，受影响的是非机密侦察数据，报道称此次攻击看起来不算严重。Artex 可整合多个开源 AI 模型，用于测试网络和计算机防御；一名中国开发者今年早些时候发布了该工具，此后它被用于多起攻击，包括针对欧盟的一起，该开发者已将 Artex 从其 GitHub 账号删除。今年早些时候，FBI 曾警告网络罪犯和间谍正在广泛使用 Artex。目前细节主要来自二手报道，具体攻击手法和规模尚未公开。

telegram · zaihuapd · 11月27日 10:42

**「背景」** Artex 是一个整合多个开源 AI 模型的 AI 辅助渗透测试框架，原本用于网络安全测试，今年早些时候由中国开发者公开发布。据搜索结果，FBI 在 2026 年 11 月发布 FLASH 预警，称恶意行为者已在多个行业利用 Artex 发动攻击，并指其能将入侵时间从数天压缩到数小时。此后该开发者已将 Artex 从其 GitHub 账号删除。

<details><summary>参考链接</summary>
<ul>
<li>FBI warns ARTEX AI hacking tool is powering global cyberattacks | Edwin Betancourth</li>
<li>FBI Warning: ARTEX and the Scaling of AI-Assisted Intrusion Tooling - Security Boulevard</li>
<li>The FBI just warned about an AI HACKING TOOL. It&#x27;s called ARTEX - Instagram</li>

</ul>
</details>

**标签**: `#AI security`, `#cyberattack`, `#offensive AI`, `#US intelligence`, `#open-source AI`

---

<a id="item-tech-news-12"></a>
### [Anthropic 系统卡披露暗中削弱模型研发请求](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic 在 6 月发布的 Claude Mythos 5 与 Fable 5 系统卡中写明，对于开发前沿大模型的请求，公司会暗中降低 Claude 的回答效果，手段包括改写提示、引导向量和参数高效微调，用户无法察觉，也不会像安全类拦截那样回退到其他模型。干预覆盖预训练流水线、分布式训练和加速器设计等任务；Anthropic 估算影响约 0.03% 的流量、不到 0.1% 的组织，并称多数编码工作不受影响。用 Claude 开发竞品模型本就违反服务条款，这份系统卡本周因开发者讨论重新受到关注。上述内容来自对系统卡的二手转述而非系统卡原文，具体细节无法从现有材料独立核实。

telegram · zaihuapd · 11月27日 13:42

**「背景」** 据相关报道，Anthropic 在 2026 年 6 月发布的系统卡中写道，公司对“针对前沿大模型研发”的请求加入了限制 Claude 有效性的干预措施，并举例说明这些请求涉及预训练流水线、分布式训练基础设施和机器学习加速器设计。这类干预与普通的安全拒答不同：系统不会直接拒绝请求或回退到其他模型，而是在用户难以察觉的情况下降低回答效果，因此从 API 调用方的角度看，得到的是“能力较弱”的回答，而不是一条明确的违规提示。用 Claude 开发竞品模型本身就违反 Anthropic 的服务条款，系统卡把暗中削弱与条款限制并列，说明合约层面的限制也可能在技术层面落地。

**「对开发者的影响」** 对使用 Claude 进行模型研发的开发者而言，风险在于输出质量可能在无提示的情况下被削弱，既不会触发安全拦截，也不会回退到其他模型，因此常规的错误处理难以察觉这种降级。由于干预覆盖预训练流水线、分布式训练和加速器设计等任务，从事这些方向的团队应评估自身工作是否落入受影响范围，并在依赖 Claude 输出做关键研发判断时保留交叉验证手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/">Claude by Anthropic | The AI for problem solvers</a></li>
<li><a href="https://ai-digest.liziran.com/en/digest/2026-06-11-anthropic-built-most-capable-model-then-wired-three-ways">Anthropic Built Its Most Capable Model , Then Wired In Three Ways to...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#Anthropic`, `#model development`, `#API behavior`, `#AI safety`

---

## 全球芯片

<a id="item-chip-news-1"></a>
### [美国 BIS 将远程访问纳入芯片出口管制，东南亚租用英伟达算力渠道受阻](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1107299496_115571&amp;c=17203180096775058747&amp;mkt=en-us) ⭐️ 8.0/10

美国商务部工业和安全局（BIS）于 11 月 16 日发布新规，将远程访问纳入芯片出口管制范围，并对东南亚四国和巴西新增芯片出口许可要求。报道指出，这一变化直接影响中国企业此前通过东南亚数据中心租用英伟达算力的路径。据《财经》了解，当地已有数据中心项目开始寻找买家接盘。报道未提供新规全文的技术细节、生效日期或官方文件编号。

rss · Bing News - China domestic chips · 11月27日 10:31

**「背景」** 这一轮收紧针对的是此前中国企业绕道东南亚租用英伟达算力的既有做法。据《金融时报》报道，英伟达已通知包括戴尔在内的制造合作伙伴，停止向四个东南亚国家发运服务器，以配合美国防止中国获得 AI 算力的出口管制；11 月 16 日 BIS 新规则进一步把远程访问纳入管辖，并对东南亚四国与巴西新增芯片出口许可要求。与早前的服务器出货限制相比，新规把监管对象从实体硬件延伸到跨境远程调用，具体生效日期与官方文件编号在现有报道中尚未披露。

**「影响」** 若新规按报道所述执行，中国企业经东南亚数据中心间接获取英伟达算力的既有渠道将面临许可约束，短期内的替代方案需转向国产算力或其他合规路径；不过报道未说明许可审批标准与生效时间，实际执行力度尚待官方文件确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#英伟达`, `#AI 算力`, `#东南亚数据中心`, `#国产芯片`

---

<a id="item-chip-news-2"></a>
### [英伟达受限 Blackwell 芯片据报现身中国数据中心](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2fnvidia-blackwell-chips-found-in-china-as-trump-floats-us-stake%2far-AA2io1hq&amp;c=8332693631996352713&amp;mkt=en-us) ⭐️ 7.0/10

据 Bing News 聚合的一则简短报道，英伟达受出口管制最严格的 Blackwell 系列 AI 芯片据称已出现在中国某数据中心；报道未披露具体型号、数量、数据中心身份、芯片来源或出现时间。同一报道还称，美国总统特朗普正在考虑联邦政府持有英伟达股份，但未说明该设想处于何种阶段、是否已形成提案或时间表。两项说法均来自媒体报道，而非监管机构公告、企业确认或可核实的出货记录，因此目前只能视为未经证实的报道，尚不能确认相关芯片是经由何种渠道进入中国，也不能确认联邦持股是否已进入政策程序。

rss · Bing News - NVIDIA and China · 11月27日 13:25

**「背景」** Blackwell 是英伟达在美国对华出口管制框架下受限程度最高的一代数据中心 AI 芯片，此前多代高端产品均需获得许可才能对华出货。此次报道称受限的 Blackwell 芯片出现在中国某数据中心，但未披露具体型号、数量、所属数据中心及来源渠道；有关特朗普考虑联邦持股的说法同样停留在传闻层面，尚无已颁布的政策或已确认的交易。

**「对英伟达对华出货与合规审查的影响」** 受限的 Blackwell 芯片出现在中国数据中心，直接后果是英伟达对华出货的合规路径将面临更严格审视：由于报道未给出芯片型号、数量、机房归属或流入渠道，目前无法判断其属于获许可的对华降规版本、第三方转口还是走私，而不同情形对应完全不同的许可与执法后果。特朗普考虑联邦持股目前仍只是报道中的说法，尚未成为既定政策，对英伟达出口许可的实际影响有待观察。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/23/business/trump-jensen-huang-nvidia.html">Jensen Huang Returns to Nvidia , Showing What Trump Will Do for AI...</a></li>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/trumps-nvidia-stake-grew-much-121318426.html">Trump &#x27;s Nvidia stake grew to as much as $62 million, Washington...</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`, `#Blackwell`

---

<a id="item-chip-news-3"></a>
### [英伟达 Blackwell 处理器据报现身与 Alice Huang、Megaspeed 关联的中国数据中心](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fnvidia-blackwell-tech-used-at-china-site-tied-to-alice-huang%2far-AA2ineG3&amp;c=11074468413121558600&amp;mkt=en-us) ⭐️ 7.0/10

据媒体报道，英伟达 Blackwell 处理器被发现出现在一处中国数据中心，该数据中心与 Alice Huang 及 Megaspeed 存在关联。报道称，这是首次披露 Blackwell 芯片进入该中国数据中心。目前可确认的信息仅限于关联关系与芯片“现身”这一事实，报道未提供芯片数量、具体机房名称、采购路径或适用的出口管制许可状态。因此尚不能判定这批 Blackwell 是通过合规渠道出货、经第三方转手，还是违反美国对华出口限制流入，相关合规状态也未获英伟达、Megaspeed 或监管机构公开确认。

rss · Bing News - NVIDIA and China · 11月27日 09:44

**「背景」** 此前已有报道称，英伟达芯片被发现出现在一家与中国数据中心相关的场所，该数据中心与 Megaspeed 首席执行官 Alice Huang 存在关联。据雅虎财经转述的报道，Alice Huang 于 2023 年创办了这家被称为“neocloud”的公司，Megaspeed 在成立后四天内就获得了英伟达的认可，并此后成为英伟达在东南亚最大的客户。本次报道的新变化在于，据称出现在该中国数据中心的芯片是 Blackwell 系列处理器，而在此之前，外界尚不清楚具体是哪一代产品。报道同时提到，美国官员怀疑 Alice Huang 为中国从事间谍活动，不过这一指控目前仅为怀疑，尚无公开证据证实。

**「影响」** 若上述关联得到证实，直接后果是美国对华出口管制执行层面将出现新的审查焦点：Blackwell 属于受控的高端 AI 算力产品，其出现在中国境内设施意味着需厘清出货主体、最终用户申报与转售链条。由于报道未说明数量与时间，目前无法评估此事对英伟达中国营收或中国本土算力供给的实际规模影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nypost.com/2026/11/27/us-news/banned-nvidia-chips-uncovered-at-chinese-data-center-linked-to-megaspeeds-alice-huang-report/">Banned Nvidia chips uncovered at Chinese data center linked to...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>
<li><a href="https://asiatimes.com/2026/11/huangs-fall-us-curbs-put-chinas-ai-computing-in-peril/">Huang &#x27;s fall, US curbs put China &#x27;s AI computing in peril - Asia Times</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#Blackwell`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-4"></a>
### [英伟达 Blackwell 芯片据报现身与 Alice Huang 有关联的中国数据中心](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fgizmodo.com%2fnvidias-advanced-ai-chips-being-used-at-chinese-data-center-tied-to-alice-huang-2000846169&amp;c=11134892719203026605&amp;mkt=en-us) ⭐️ 7.0/10

据一则简短报道，一座与前 Megaspeed 高管 Alice Huang 有关联的中国数据中心已安装使用英伟达 Blackwell AI 芯片的硬件。报道未披露芯片数量、数据中心运营方、采购渠道，也未说明这批芯片的出口是否获得许可或是否落入美国对华出口管制范围。报道同样未交代 Blackwell 的具体型号，因此目前只能确认“安装”这一事实，无法判断其合规状态与规模。

rss · Bing News - NVIDIA and China · 11月27日 05:02

**「背景」** 此前报道显示，与英伟达有业务关联的云计算公司 Megaspeed 曾表示，被指为中国间谍的 Alice Huang 已于 2025 年离开该公司；企业记录还显示，黄与 Megaspeed 的创立有直接关系，其关联公司曾收购一家中国视频公司的新加坡分支。此次报道的新进展是，与黄有关联的中国数据中心已安装搭载英伟达 Blackwell AI 芯片的硬件，但报道未披露芯片数量、数据中心运营方或相关出口合规状态。

**「受限 GB300 疑似经台厂渠道流入」** 据 ZeroHedge 报道，英伟达的 GB300 机架在未取得美国出口许可证的情况下被禁止运往中国，而彭博通过公开保修数据库将该机架序列号追溯至台湾技嘉科技。若这批设备确实进入上海数据中心，其实际影响在于出口管制下的转口或分销路径被暴露，后续对 GB300 等受限型号的许可审查与渠道核查可能收紧。但现有来源未说明设备数量、进口许可状态或相关企业回应，因此尚不能确认这批 Blackwell 硬件属于违规出货。

<details><summary>参考链接</summary>
<ul>
<li>Megaspeed says alleged Chinese spy, Alice Huang, left company last year</li>
<li>Spies and silicon chips: Alice Huang&#x27;s tangled corporate web - NZ Herald</li>
<li><a href="https://www.zerohedge.com/ai/nvidia-pares-gains-report-traces-shipment-restricted-ai-blackwell-chips-china-data-center">Nvidia Pares Gains As Report Traces Shipment Of... | ZeroHedge</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#Blackwell`, `#中美芯片合作`

---

<a id="item-chip-news-5"></a>
### [阿里吴泳铭首曝平头哥三代 AI 芯片路线图](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fwww.huxiu.com%2farticle%2f4909136.html&amp;c=15900593603379902450&amp;mkt=en-us) ⭐️ 7.0/10

阿里巴巴首席执行官吴泳铭在 2027 财年第二季度财报电话会上首次公开平头哥三代 AI 芯片路线图：真武 M890 今年全面上线；性能达到 M890 三倍的真武 V900 计划于明年第一季度量产，并同步推出超节点集群；J900 计划 2028 年量产。吴泳铭表示，2027 年和 2028 年阿里新增 AI 芯片供应的绝大多数将来自自研平头哥，旗舰产品优先保障下一代通义千问等大模型训练，推理侧则广泛采购其他国产芯片品牌。上述内容均为公司公布的计划，而非已交付产品或实测结果。

rss · Bing News - China domestic chips · 11月27日 19:53

**「背景」** 平头哥是阿里巴巴旗下的芯片设计业务，此前已有自研 AI 芯片产品线；此次是吴泳铭首次以 CEO 身份在财报电话会上系统披露三代产品的节奏，将此前相对分散的芯片发布整合为覆盖今年至 2028 年的量产时间表。选择在财报电话会公开，也意味着自研芯片的供应占比已被纳入对投资者的正式表述。

**「影响」** 按这一规划，阿里 AI 算力的增量供给将逐步由外购转向自研：训练侧旗舰芯片由平头哥 M890、V900、J900 逐代接续，推理侧继续向其他国产芯片厂商采购。若 V900 能如期在明年第一季度量产，自研芯片在阿里新增 AI 芯片容量中的占比将明显上升，同时为国产加速卡厂商保留推理侧订单空间。

**标签**: `#国产芯片`, `#AI 算力`, `#阿里巴巴`, `#自研芯片`, `#数据中心`

---

<a id="item-chip-news-6"></a>
### [英伟达 Blackwell 芯片据报现身上海数据中心](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.yahoo.com%2fnews%2fpolitics%2farticles%2fnvidias-blackwell-chips-turn-china-170930530.html&amp;c=4276174839387292558&amp;mkt=en-us) ⭐️ 6.0/10

据 Yahoo News 报道，被禁止对华出口的英伟达 Blackwell 机架被发现出现在上海一座与 Alice Huang 有关的数据中心内。报道未说明查获数量、发现时间、涉及的执法机构，也没有给出独立核实信息，因此目前只能视为媒体披露的线索，而非已确认的执法结论。同一报道还提到，特朗普表示美国仍有可能入股英伟达；这属于他提出的可能性，并非已宣布或已生效的政策安排。两件事并列出现，但报道没有说明二者之间是否存在直接关联。

rss · Bing News - NVIDIA and China · 11月27日 09:09

**「背景」** 此前美国对华出口管制已限制英伟达向中国出口 Blackwell 架构产品。本次报道称，上海一处由 Alice Huang 关联的数据中心发现被禁的英伟达机架，但未说明查获数量、执法部门或官方确认情况。

**「实际影响」** 据彭博追踪，涉事设备为英伟达 GB300 机架，其序列号经公开保修数据库指向台湾技嘉科技；该类芯片对华出货须获美国出口许可，因此此次现身上海数据中心意味着许可链条或转口路径存在待查缺口，而非已获批的对华销售。就目前证据看，这更可能收紧美国对第三方向中国转售 Blackwell 机架的审查，并给英伟达在华合规出货与相关渠道收入带来额外不确定性；具体执法行动和许可结论尚未公布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>
<li><a href="https://www.zerohedge.com/ai/nvidia-pares-gains-report-traces-shipment-restricted-ai-blackwell-chips-china-data-center">Nvidia Pares Gains As Report Traces Shipment Of... | ZeroHedge</a></li>
<li><a href="https://nypost.com/2026/11/27/us-news/banned-nvidia-chips-uncovered-at-chinese-data-center-linked-to-megaspeeds-alice-huang-report/">Banned Nvidia chips uncovered at Chinese data center linked to...</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-7"></a>
### [英伟达 Blackwell 芯片据报现身上海数据中心](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c7c55460c9420dbac114b5cc6&amp;url=https%3a%2f%2fwww.analyticsinsight.net%2fnews%2fnvidias-powerful-blackwell-chips-surface-in-china-raising-a-major-us-security-concern&amp;c=4352821743092553224&amp;mkt=en-us) ⭐️ 6.0/10

据 Analytics Insight 报道，英伟达最先进的 AI 处理器据称出现在上海一座与新加坡公司 Megaspeed 相关联的数据中心，再次引发外界对美国对华出口管制执行情况的质疑。报道未披露涉事芯片的具体型号、数量、转运路径或涉及的监管机构，也未说明是否已有立案调查或政策回应。因此目前只能视为对既有执法关切的进一步报道，不能认定为已确认的违规事件或政策变化。

rss · Bing News - China chip policy · 11月27日 17:30

**「背景」** 此事有前情：公开报道称，总部位于新加坡的 Megaspeed 于 2026 年 11 月中旬启动内部法律调查，起因是有指控称其可能向中国公司提供了接触英伟达高端 AI 芯片的“后门”通道（tool-2-1）。同一时期的报道还指出，在现行规则下，英伟达对华出口许可仅覆盖性能较低的 H200 加速器，且附带装运条件（tool-2-3）。此次 Blackwell 处理器出现在与 Megaspeed 关联的上海数据中心，正是在上述调查与许可框架尚未澄清的背景下发生。

**「影响」** 若报道属实，这一情况意味着受美国出口管制的先进 AI 算力可能经第三国中转进入中国境内数据中心，从而令管制清单对最终流向的约束力受到实际检验；但由于缺少芯片型号、数量和转运路径等细节，尚无法判断涉事产品是否属于受限范围，也无法评估其对英伟达对华销售渠道或中国境内算力供给的具体影响。

<details><summary>参考链接</summary>
<ul>
<li>Megaspeed launches internal legal investigation as suspected chip export violations via Singapore data centres put AI supply chains under US scrutiny | Folio</li>
<li>Export-banned Nvidia chips are behind China&#x27;s most powerful AI models—uh | Tech Bytes</li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`, `#Blackwell`

---

<a id="item-chip-news-8"></a>
### [华为拟在 ISSCC 2027 披露自研 HBM 方案](https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/) ⭐️ 6.0/10

据 EE Times 报道，华为计划在明年年初于旧金山举行的 ISSCC 2027 上公布其定制高带宽内存（HBM）设计的细节。报道将这一方案描述为绕开 HBM 供应限制的变通路径（workaround），指向其 AI 芯片所需的关键部件。目前可确认的仅是这一会议披露计划：报道未给出该 HBM 的容量、带宽、制程节点、量产时间或制造方等任何参数，也未说明该设计是否已流片或量产。

rss · EE Times · 11月27日 08:56

**「背景」** 华为此次披露并非突然出现：此前已有报道称，华为计划公布一款数据引脚密度达到三星和 SK 海力士当前量产 HBM 两倍的设计（tool-2-1），另有报道称其采用 4096 位、64 通道、五层晶圆对晶圆混合键合的方案，可使升腾 960 处理器达到 9.6 TB/s 带宽（tool-2-3）。不过，这些均为媒体披露的设计信息，并非量产或实测结果；本次消息只确认华为将在 2027 年初于旧金山举行的 ISSCC 上说明细节，尚未给出规格、产能或量产状态。

**「对国产 AI 芯片供给的潜在影响」** 若该定制 HBM 方案可行，其直接意义在于为受出口管制的中国 AI 加速器提供一条绕开三星、SK 海力士、美光先进 HBM 栈的路径，因为美国贸易限制禁止中国公司从境外供应商采购先进 HBM。但现有证据仅有 ISSCC 2027 的披露计划，没有带宽、容量、良率或量产时间表，因此尚不能据此判断升腾等国产芯片的供给会在何时、以多大规模改善。

<details><summary>参考链接</summary>
<ul>
<li>Huawei plans to unveil HBM design to challenge Samsung and SK hynix - TechNode</li>
<li>Huawei&#x27;s New 4096-bit HBM Design Claims 9.6 TB/s Bandwidth, Beating Nvidia B300 | Tilt</li>
<li><a href="https://wccftech.com/huawei-poised-to-grow-chinas-ai-chip-market-next-generation-hbm-design-double-data-pin-density/">Huawei Poised To Grow China ’s AI Chip Market With...</a></li>

</ul>
</details>

**标签**: `#国产芯片`, `#华为`, `#HBM`, `#AI 算力`, `#对华出口管制`

---

<a id="item-chip-news-9"></a>
### [报道称 Megaspeed 关联中国数据中心发现被禁英伟达芯片](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fnypost.com%2f2026%2f11%2f27%2fus-news%2fbanned-nvidia-chips-uncovered-at-chinese-data-center-linked-to-megaspeeds-alice-huang-report%2f&amp;c=13417010356993380899&amp;mkt=en-us) ⭐️ 5.0/10

《纽约邮报》11 月 27 日援引一份报道称，在一处与 Megaspeed 相关人员黄文华（Alice Huang）有关的中国数据中心内发现了被禁止出口的英伟达芯片。该条目未给出芯片型号、数量、查获方式、所涉执法行动或具体时间，也未说明采购与运输路径，因此目前只能视为第二手媒体报道的指控，而非已确认的执法结论。同一报道还提到，特朗普曾表示这类芯片“在两三年内”将可以在中国购买，但该表述没有附带具体政策条款、许可安排或生效日期。

rss · Bing News - NVIDIA and China · 11月27日 09:18

**「背景」** 此前，Megaspeed 由 Alice Huang 于 2023 年创办，成立仅四天便获得英伟达的认证，随后成为英伟达在东南亚最大的客户。据 tool-1-2 与 tool-1-3 报道，此次涉事芯片为英伟达 GB300 机架，该型号在未取得美国出口许可证的情况下被禁止运往中国；相关报道通过公开保修数据库将该机架序列号追溯至台湾技嘉科技。现行管制的前提是：GB300 属于受出口许可约束的对华禁运产品，因此任何在华出现的整机都需要解释其许可来源。

**「后续影响」** 该报道未披露涉事芯片的具体型号、数量、查获经过或任何执法处置，因此无法据此判断其对英伟达对华出货、相关许可审批或中国数据中心算力供给的实际影响。目前可确认的只是特朗普表示这些芯片“两三年内”可在华购买，属政策表态而非已生效的规则调整；在缺乏具体执法证据前，不宜将此解读为出口管制松动或国产替代加速的依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>
<li><a href="https://www.zerohedge.com/ai/nvidia-pares-gains-report-traces-shipment-restricted-ai-blackwell-chips-china-data-center">Nvidia Pares Gains As Report Traces Shipment Of... | ZeroHedge</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#数据中心`

---

<a id="item-chip-news-10"></a>
### [禾润电子创业板 IPO 拟募资 12 亿元，研发费用率 9.83%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1107363135_646494&amp;c=12805390257734187732&amp;mkt=en-us) ⭐️ 5.0/10

11 月 26 日，禾润电子科技（嘉兴）股份有限公司递交创业板招股说明书，并披露对深交所首轮审核问询函的回复。这家 2006 年成立的无晶圆厂（Fabless）集成电路设计企业以卫星导航定位（GNSS）芯片为核心，同时布局模拟信号链与电源链芯片，此次拟募资约 12 亿元人民币，保荐机构为中信建投证券。招股书显示，公司晶圆制造与封装测试完全依赖第三方供应商，披露的研发费用率为 9.83%。2026 年 5 月的股权转让中，公司整体估值约 31 亿元。上述募资与估值均为申报和披露口径，尚待交易所审核及发行程序完成。

rss · Bing News - China domestic chips · 11月27日 14:39

**「背景」** 禾润电子成立于 2006 年，以卫星导航定位芯片为核心，同时布局模拟信号链与电源链芯片，采用 Fabless（无晶圆厂）模式，晶圆制造和封装测试完全依赖第三方供应商。此次是其递交创业板招股书并回复深交所首轮审核问询；在 2026 年 5 月的股权转让中，公司整体估值约 31 亿元，保荐机构为中信建投证券。

**「影响」** 若发行完成，约 12 亿元募资将为这家 Fabless 设计公司提供股权融资渠道；但其晶圆制造与封测全部外包的模式意味着产能和成本仍受代工及封测供应商安排制约。目前公开信息仅到问询回复阶段，募资到位时间与具体投向节奏尚不确定。

**标签**: `#国产芯片`, `#GNSS芯片`, `#创业板IPO`, `#模拟芯片`, `#无晶圆厂`

---

<a id="item-chip-news-11"></a>
### [超越光刻：MATCH Act 拟将管制延伸至良率技术](https://www.eetimes.com/beyond-lithography-the-battle-for-semiconductor-manufacturing-yield/) ⭐️ 5.0/10

EE Times 于 2026 年 11 月 27 日发表的分析文章指出，拟议中的 MATCH Act 所暴露的战略脆弱性并不限于 ASML 的光刻设备，还延伸至决定晶圆厂生产率和良率的相关制造技术。该文将其定位为一项政策风险，关注点从单一光刻工具转向影响先进制程产出效率的工艺环节。由于文章仅为摘要式导语，未披露 MATCH Act 的具体条款、生效日期、受限设备类别或受影响企业，因此它目前属于立法提案层面的讨论，而非已颁布的规则或已实施的出口管制。

rss · EE Times · 11月27日 14:22

**「背景」** 该条目所依据的分析文章仅以摘要形式指出，拟议的 MATCH Act 暴露出的战略脆弱性并不局限于 ASML 光刻设备，还延伸至决定晶圆厂生产率和良率的相关制造技术。条目未披露该法案的具体条款、生效状态或受影响的企业与设备，因此目前只能确认它是一项尚在提议阶段的立法动向，而非已颁布的规则。在缺少先前立法或管制节点可对照的情况下，本条无法进一步追溯更早的政策前身。

**「实际影响仍待条款明确」** 由于条目未披露 MATCH Act 的具体条款、生效日期与受限设备清单，目前无法确认其对晶圆厂良率相关设备的实际出口许可或出货影响；路透社报道称修订版法案已删除 4 月令设备商警觉的多项宽泛条款，说明限制范围仍在变动。若最终文本将管制延伸至量测、检测等良率关键环节，受影响方将是依赖美国技术对华出货的设备供应商及中国晶圆厂的产能爬坡节奏。

<details><summary>参考链接</summary>
<ul>
<li>US narrows chip equipment curbs but keeps pressure on ASML tools and Chinese fabs</li>

</ul>
</details>

**标签**: `#对华出口管制`, `#先进制程`, `#晶圆产能`, `#半导体设备`

---

<a id="item-chip-news-12"></a>
### [Big Technology 创始人：中国获取英伟达芯片的渠道正快速收窄](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fchinas-nvidia-chip-access-is-closing-fast-says-big-technologys-alex-kantrowitz%2fvi-AA2in23A&amp;c=9999657886079154578&amp;mkt=en-us) ⭐️ 4.0/10

Big Technology 创始人 Alex Kantrowitz 在 CNBC「Squawk on the Street」节目中评论有关英伟达芯片在中国的最新报道，称中国获取英伟达芯片的渠道正在快速收窄，并讨论了最新一轮限制措施对半导体公司意味着什么。所给素材仅为该访谈片段的预告式摘要，未包含具体政策条款、生效日期、产品型号、算力或带宽参数、出货数量等细节，因此这一说法属于媒体评论，而非已颁布的规则或已发生的出货变化。

rss · Bing News - NVIDIA and China · 11月27日 09:34

**「背景」** 该采访片段仅引述了有关中国获取英伟达芯片渠道收窄的“最新报道”，未给出口管制条款、生效日期或产品清单。其讨论的“crackdowns”（收紧举措）所指的具体政策文件与时间点，在本条素材中均未说明，因此无法确认这次是新增限制还是既有规则的延续。

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-13"></a>
### [D.A. Davidson 分析师称英伟达最先进 Blackwell 芯片已流入中国](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fda-davidson-s-gil-luria-there-s-no-doubt-that-nvidia-s-most-advanced-chip-ended-up-in-china%2fvi-AA2indyO&amp;c=11207026517034740657&amp;mkt=en-us) ⭐️ 4.0/10

D.A. Davidson 科技研究主管 Gil Luria 在 CNBC《Squawk on the Street》节目上表示，有报道称英伟达最先进的 Blackwell 芯片已被安装在上海一座与 Alice Huang 有关联的数据中心，他据此称“毫无疑问”该芯片已进入中国。需要说明的是，这是分析师在电视访谈中的判断，节目仅以“据报道”引出该说法，未给出芯片数量、流入渠道、具体接收方或可核实的证据，因此目前属于未经证实的分析师表态，而非已确认的出货、查获或执法事实。

rss · Bing News - NVIDIA and China · 11月27日 07:21

**「背景」** 该采访所称的“英伟达最先进芯片”，指的就是 Blackwell 世代产品。按英伟达自身的定位，其业务已从游戏 GPU 扩展至 AI 与加速计算，因此 Blackwell 属于对华出口管制重点关注的先进 AI 算力产品。不过，本次提供的材料只包含一段电视访谈的节目简介，没有给出涉事芯片的型号细分、出货数量、经手渠道或收货方等可核查信息，因此无法确认这批芯片究竟通过何种途径进入上海的数据中心。

**「影响」** 若该说法后续得到证实，其指向的是美国对华先进 AI 芯片出口管制可能存在执行缺口，即受控的 Blackwell 级产品经由未披露的渠道进入中国数据中心；但在数量、渠道和接收方均未公开前，尚无法判断其对英伟达对华收入或中国国产替代进程的实际影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia">Nvidia - Wikipedia</a></li>
<li><a href="http://www.nvidia.com/page/home.html">Nvidia - Official Site</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#Blackwell`

---

<a id="item-chip-news-14"></a>
### [分析人士：中国获取英伟达芯片渠道正快速收窄](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c7c55460c9420dbac114b5cc6&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fchina-s-nvidia-chip-access-is-closing-fast-says-big-technology-s-alex-kantrowitz%2fvi-AA2in23A&amp;c=481846134368304326&amp;mkt=en-us) ⭐️ 4.0/10

Big Technology 创始人 Alex Kantrowitz 在 CNBC《Squawk on the Street》节目中表示，中国获取英伟达芯片的渠道正在快速收窄，并讨论了有关英伟达在华芯片的最新报道以及最新一轮限制措施对半导体公司意味着什么。节目文字仅为访谈简介，未给出新的政策条款、生效日期、公司数据或产品型号，因此上述判断属于评论人士的观点，而非已核实的新规或已执行的措施。

rss · Bing News - China chip policy · 11月27日 09:34

**「背景」** 该访谈片段未提供可核实的政策条文、生效日期或公司数据，仅笼统提及围绕英伟达芯片在华销售的最新报道与执法行动。由于缺乏具体的前序政策或产品事实可供衔接，本条目不补充背景细节。

**「影响」** 据《金融时报》报道，英伟达已停止向东南亚出口芯片，此举发生在美国加大出口管制力度、以阻止中国获取 AI 算力的背景下（tool-2-1）。BBC 的报道进一步指出，最新管制措施不仅限制高端芯片对华出口，也限制中国公司通过境外租用算力来训练模型这一途径（tool-2-2）。这些报道说明，实际影响已从“芯片能否卖给中国”扩展到“中国公司能否在境外获得同等算力”，涉及英伟达的出货方向和东南亚等中转市场渠道；但上述报道未给出停止出货的具体生效日期、涉及的产品型号或数量，Kantrowitz 的采访内容本身也未提供可核实的新政策条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south-east Asia</a></li>
<li><a href="https://www.bbc.com/news/articles/cqevr4lnd1nxo">Jensen Huang: How the Nvidia scandal exposed the risks of Asia&#x27;s big...</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-15"></a>
### [A 股算力芯片午后走强，国产智算规划与 HBM 研发进展被指为催化](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261127A0AXO200&amp;c=8859260584746268499&amp;mkt=en-us) ⭐️ 4.0/10

11 月 27 日午后，A 股算力芯片、存储及光通信板块走强，该报道将催化因素归结为国产智算建设规划与高带宽存储（HBM）研发进展，但未给出具体政策条款、涉及企业或产品参数。文中提及 11 月 27 日国务院常务会议研究相关事项，但摘要在此处被截断，可核实的内容有限。文章主体为产品推介，介绍科创创业人工智能 ETF 永赢（159141）覆盖科创板及创业板 AI 核心产业链，科创芯片设计 ETF 永赢（589420）聚焦科创板芯片设计环节，并称二者受相关消息提振；但未披露规模、份额或资金流数据。

rss · Bing News - China domestic chips · 11月27日 07:09

**「背景」** 该报道未给出国产智算建设规划的具体条款、生效时间或高带宽存储研发的具体主体与进度，仅笼统提及“规划”和“研发进展”构成催化。来源内容在国务院常务会议处即被截断，会议审议的具体事项无法从现有材料确认，因此本轮行情的政策依据仍不明确。

**「影响」** 该报道未提供可验证的政策文本，未说明获准或受限的具体范围，也未给出任何芯片产品的制程、产能或出货数据，因此无法据此判断对国产算力供给或相关企业营收的实际影响。对两只 ETF 而言，报道仅称其“受相关消息提振”，未给出资金流或份额变动，短期行情与基本面变化之间的因果关系尚不成立。

**标签**: `#国产芯片`, `#AI 算力`, `#高带宽存储`, `#中国政策`, `#ETF`

---

<a id="item-chip-news-16"></a>
### [Penguin 将退役 DDR4 重新用于 AI 服务器](https://www.eetimes.com/penguin-revives-retired-ddr4-for-ai-servers/) ⭐️ 4.0/10

EE Times 报道称，Penguin 正在将已退役的 DDR4 内存重新用于 AI 服务器，以应对内存扩容需求。报道指出，超大规模云厂商已在回收利用较旧的 DRAM，而企业在复用 DDR4 方面进展相对缓慢。该报道未披露容量、成本、部署规模或客户数量等具体数字，也未说明产品型号或时间表，因此目前只能作为一项行业做法的描述，而非有量化证据的商业部署。

rss · EE Times · 11月27日 19:17

**「背景」** 据 EE Times 报道，Penguin（Penguin Solutions）正在把退役的 DDR4 内存重新用于 AI 服务器；报道同时指出，超大规模数据中心运营商已在回收旧 DRAM，而企业在利用 DDR4 满足内存扩容需求方面进展较慢。更早的一项相关进展是，Marvell 与 Penguin Solutions 于 2026 年 11 月宣布合作开发两项互补的内存扩展技术，面向 AI 基础设施需求（据搜索结果）。本条报道没有给出容量、成本、部署或客户方面的具体数字。

<details><summary>参考链接</summary>
<ul>
<li>Marvell and Penguin Solutions Collaborate on AI Memory - TechIntelPro</li>

</ul>
</details>

**标签**: `#AI 算力`, `#DRAM`, `#AI 服务器`, `#供应链`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [国常会：加力发挥“国家队”稳市作用，优化中央汇金类“平准基金”功能](https://www.tmtpost.com/nictation/8220182.html) ⭐️ 8.0/10

China&\#x27;s State Council pledged to reinforce capital-market stabilization through a stronger &\#x27;national team&\#x27; and an optimized Central Huijin quasi-stabilization fund, alongside measures on dividends/buybacks, long-term fund inflows, and stricter market supervision.

telegram · zaihuapd · 11月27日 05:35

**标签**: `#China policy`, `#capital markets`, `#Central Huijin`, `#market stabilization`, `#long-term capital`

---

<a id="item-finance-news-2"></a>
### [蜜雪冰城 5 亿元入股 DeepSeek，第二轮融资规模约千亿元](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

据报道，DeepSeek 已完成第二轮融资，规模在 1000 亿至 1055 亿元之间，投后估值约 6155 亿元；蜜雪冰城股份有限公司通过天津砺思星深基金认缴 5 亿元，腾讯、宁德时代、中国移动和 vivo 也在新增的 31 家出资人之列。

telegram · zaihuapd · 11月27日 06:33

**「背景」** 这是 DeepSeek 的第二轮融资；据《The Information》10 月底的报道，该轮规模约 1055 亿元、投后估值 6155 亿元，腾讯继续参与。蜜雪的 5 亿元并非直接投资，而是通过砺思资本管理的天津砺思星深基金投入。

**「影响」** 蜜雪冰城认缴的 5 亿元，与其 2025 年 335.6 亿元的营收相比并不大，目前看更像一笔财务性投资；如果交易属实，直接受影响的是参与砺思星深基金的投资人以及 DeepSeek 现有股东，他们的持股比例会在约 6155 亿元投后估值下被稀释。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.zhibo8.com/news/web/game/2026-10-31/6ae5662e6dfe9native.htm">估 值 6155 亿 元！ 曝 DeepSeek 第 二 轮 融 资 1055...</a></li>
<li><a href="https://news.mbalib.com/story/258976">早报|苹果AI入华牵手阿里 千 问; DeepSeek 估 值 6155 ...</a></li>
<li><a href="https://www.lanjinger.com/d/1774341739896494779">蜜 雪 冰 城 ： 2025 年 营 收 335 . 6 亿 元， 净 利 增长32.7%_ 资 讯-蓝鲸财经</a></li>
<li><a href="https://www.tmtpost.com/7928831.html">2025 ...</a></li>
<li><a href="https://h5.ifeng.com/c/vivoArticle/v002UtHhgw77dRdxNzTFeRoS4faeb5ZiwCICSIP80nmlkms__?isNews=1&amp;showComments=0">甜香酸涩苦：五大奶茶品牌的 2025 年报</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#private financing`, `#valuation`, `#strategic investors`, `#China tech`

---

<a id="item-finance-news-3"></a>
### [央行发布大额存单新规，个人起购门槛降至 10 万元](https://www.news.cn/fortune/20261127/70789d77822242cc82216f51a416f872/c.html) ⭐️ 7.0/10

中国人民银行 11 月 27 日公布《大额存单管理办法》，将个人投资人认购起点从 20 万元下调至不低于 10 万元、机构投资人从 1000 万元下调至不低于 500 万元，自 2027 年 3 月 21 日起施行。

telegram · zaihuapd · 11月27日 11:36

**「背景」** 现行 20 万元和 1000 万元的门槛出自 2015 年《大额存单管理暂行办法》，新办法施行后将同时废止该暂行办法和 2016 年第 13 号公告；同日公布的《人民币存贷款利率管理规定》同样于 2027 年 3 月 21 日施行，要求金融机构自主确定存贷款利率，不得通过高息揽储等不正当手段吸收存款。

**「影响」** 门槛减半后，更多个人储蓄者可用 10 万元认购大额存单，机构起点降至 500 万元则可能让更多中小机构参与，但两项规定 2027 年 3 月才生效，此前银行执行的仍是现行门槛。

**标签**: `#China central bank`, `#large-denomination CDs`, `#deposit rates`, `#banking regulation`, `#interest-rate policy`

---

<a id="item-finance-news-4"></a>
### [市场监管总局约谈雅迪等 15 家电动自行车企业](https://www.news.cn/20261127/0c8c665ce70c417b9263b39fa8a519f0/c.html?hl=zh-CN) ⭐️ 7.0/10

11 月 27 日，国家市场监管总局集中约谈雅迪、台铃、爱玛、九号、小牛等 15 家电动自行车企业，原因是近期 CCC 认证全覆盖飞行检查发现部分企业质量保证能力欠缺、产品一致性管控不严，并存在违反强制性国家标准出厂销售不合格产品的问题；约谈要求企业抓紧整改、严格执行“一车一池一充一码”规定，对确认有缺陷的产品立即召回。

telegram · zaihuapd · 11月27日 12:06

**「背景」** CCC 认证是中国对电动自行车等产品实施的强制性产品认证，产品须符合强制性国家标准才能出厂销售；此次约谈源于监管部门对该认证开展的全覆盖飞行检查。

**「影响」** 使用这些品牌电动自行车的消费者，可要求企业对已确认存在缺陷的产品实施召回；企业在售后不得推诿责任、误导消费者无牌上路，也不得以“证书很快恢复”为由拒绝退车。

**标签**: `#regulation`, `#electric-bicycles`, `#consumer-safety`, `#manufacturing`, `#China`

---