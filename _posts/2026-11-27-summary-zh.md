---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 45 条内容中筛选出 31 条重要资讯。

---

**科技新闻**
1. [Linux 内核 nfsd 曝 9.8 分预认证漏洞，可远程获取 root](#item-tech-news-1) ⭐️ 9.0/10
2. [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待及未经同意的私密图像](#item-tech-news-2) ⭐️ 8.0/10
3. [SemiAnalysis 深度解析 AWS Trainium3 推理与微架构](#item-tech-news-3) ⭐️ 8.0/10
4. [美国情报机构遭 AI 辅助攻击，涉开源工具 Artex](#item-tech-news-4) ⭐️ 8.0/10
5. [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63 版本](#item-tech-news-5) ⭐️ 8.0/10
6. [Convex 编码技能被指未经告知上传用户创意](#item-tech-news-6) ⭐️ 7.0/10
7. [信用卡盗刷脚本利用 WebRTC 规避监控，波及多家购物网站](#item-tech-news-7) ⭐️ 7.0/10
8. [bouncemarket：用确定性模拟和 SSE 直播小球落点](#item-tech-news-8) ⭐️ 7.0/10
9. [计算机验证的证明可能存在缺陷](#item-tech-news-9) ⭐️ 7.0/10
10. [Michael Nielsen 下线其神经网络在线书](#item-tech-news-10) ⭐️ 7.0/10
11. [主流编程语言为何应原生支持形式化验证](#item-tech-news-11) ⭐️ 7.0/10
12. [Anthropic 系统卡承认暗中削弱前沿模型研发请求](#item-tech-news-12) ⭐️ 7.0/10
13. [谷歌 Play 将全球公开商家开发者电话与地址](#item-tech-news-13) ⭐️ 7.0/10
14. [GTA 6 非官方 PC 移植项目 AnyPS5 获 5.8 万星标，GitHub 发文后删帖](#item-tech-news-14) ⭐️ 7.0/10
15. [八达通遭网络攻击：约 7500 客户及 2.2 万商户资料受影响](#item-tech-news-15) ⭐️ 7.0/10

**全球芯片**
1. [美国 BIS 新规收紧远程访问与东南亚芯片许可，中企获取英伟达算力通道收窄](#item-chip-news-1) ⭐️ 8.0/10
2. [英伟达 Blackwell 机架据称现身上海，特朗普提美国或入股](#item-chip-news-2) ⭐️ 7.0/10
3. [美国国会推进芯片管制法案，瞄准 ASML 在华服务工程师](#item-chip-news-3) ⭐️ 7.0/10
4. [广东算力“十五五”规划鼓励算力中心优先用国产芯片](#item-chip-news-4) ⭐️ 7.0/10
5. [中芯国际 Q2 份额 5.4%，逼近三星 5.9%](#item-chip-news-5) ⭐️ 6.0/10
6. [禾润电子冲创业板：拟募资 12 亿元，研发费用率 9.83%](#item-chip-news-6) ⭐️ 5.0/10
7. [BIS 新规限制 16 纳米以下流片，海外代工暂停国产芯片订单](#item-chip-news-7) ⭐️ 5.0/10
8. [华为拟在 ISSCC 2027 披露定制 HBM 变通方案](#item-chip-news-8) ⭐️ 5.0/10
9. [Big Technology 创办人：中国取得英伟达芯片的渠道正快速收窄](#item-chip-news-9) ⭐️ 4.0/10
10. [Penguin 复用退役 DDR4 内存供应 AI 服务器扩容](#item-chip-news-10) ⭐️ 4.0/10
11. [Beyond Lithography: The Battle for Semiconductor Manufacturing Yield](#item-chip-news-11) ⭐️ 4.0/10

**科技博客**
1. [AI 写作判定权应归属谁](#item-tech-blog-1) ⭐️ 7.0/10

**财经新闻**
1. [国常会提出强化“国家队”稳市与中央汇金类“平准基金”功能](#item-finance-news-1) ⭐️ 9.0/10
2. [央行下调大额存单起购门槛 个人降至 10 万元](#item-finance-news-2) ⭐️ 8.0/10
3. [蜜雪冰城 5 亿元入股 DeepSeek 新一轮融资](#item-finance-news-3) ⭐️ 7.0/10
4. [市场监管总局集中约谈雅迪、台铃、爱玛等 15 家电动自行车企业](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Linux 内核 nfsd 曝 9.8 分预认证漏洞，可远程获取 root](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec 披露 Linux 内核 NFS 服务器 nfsd 的预认证堆溢出漏洞 CVE-2026-99362，CVSS 评分 9.8。攻击者无需登录，向 tcp/2049 发送一条连接即可越界写入内核堆，进而获取 root shell；该漏洞自 2014 年的 Linux 3.16 起存在，影响启用 NFSv4.1 或 4.2 的主机，包括文件服务器、NAS 和集群存储节点。修复已在 6.12.117、6.18.61、7.3.2 和 7.4-rc1 发布，需升级内核并重启，无法立即升级者可用防火墙限制 tcp/2049 访问。CVE 于 2026 年 11 月 20 日公开。

telegram · zaihuapd · 11月27日 12:57

**「背景」** 该漏洞的成因在 nfsd 的 NFSv4 会话槽位处理路径：nfsd4\_sequence\(\) 在接受槽位 seqid 之前，会先把回复缓冲区收窄到会话缓存的回复上限，从而可能越过内核堆对象的边界写入。据 Debian 安全跟踪器记录，上游修复的方式是“在接受槽位前先检查 SEQUENCE 回复”，即预先校验。由于 NFSv4.1/4.2 在多数环境中是 NFS 服务器默认启用的协议版本，任何能访问 tcp/2049 的主机在未打补丁前都可能被单条 TCP 连接触发。

**「影响与处置」** 运行受影响版本 nfsd 的主机在打补丁前，对任意可达 tcp/2049 的网络都暴露预认证远程 root 风险，因此运维方应优先升级至 6.12.117、6.18.61、7.3.2 或 7.4-rc1 并重启以启用新内核；若无法立即升级，应在网络边界限制 tcp/2049 的访问来源。这一处置同样适用于启用 NFSv4.1 或 4.2 的 NAS 与集群存储节点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensec.in/blog/nfs2root-cve-2026-99362">NFS2ROOT ( CVE - 2026 - 99362 ): pre - auth root in Linux nfsd | OpenSec</a></li>
<li><a href="https://security-tracker.debian.org/tracker/CVE-2026-99362">CVE - 2026 - 99362</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#NFS`, `#security vulnerability`, `#CVE`, `#remote root`

---

<a id="item-tech-news-2"></a>
### [多州总检察长起诉 SpaceX，要求阻止 Grok 生成儿童性虐待及未经同意的私密图像](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 8.0/10

多个州的总检察长以 SpaceX 作为 xAI 和 Grok 的母公司为由提起诉讼，要求法院制止 Grok 生成儿童性虐待材料和未经同意的私密图像，并指控该平台存在创作和推广此类内容的行为。目前公开信息来自弗吉尼亚州总检察长办公室的新闻稿，未披露参与诉讼的具体州数、受理法院或时间表。

hackernews · DeepLogin · 11月27日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=50670855)

**「背景」** 弗吉尼亚州和俄勒冈州总检察长已对 SpaceX 提起诉讼，指控其作为 xAI/Grok 母公司违反州消费者保护法，允许 Grok Imagine 生成非自愿性露骨图像。此前在 2026 年 9 月，一名儿童性虐待幸存者已提起诉讼，指控 xAI 忽视行业通行的防护措施，导致 AI 生成的儿童性虐待材料出现在 X 平台并传播。此次多州诉讼将争议从模型输出层面扩展到母公司责任和州级消费者保护执法。

**「潜在影响」** 若诉讼推进，xAI 可能面临针对 Grok 输出内容的法律禁令和平台责任压力，需要调整模型防护措施或内容审核机制；使用 Grok 的开发者与企业客户也需关注由此产生的合规风险。

**「社区讨论」** 有评论者疑惑此类内容本应已在各平台被广泛禁止，质疑 Grok 是默认宽松还是需要用户刻意诱导；也有人追问制作这些图像的用户是否应承担责任。另有评论指出使用 Grok 需绑定 Twitter 账号，认为这一门槛让尝试模型存在账号风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.engadget.com/2325111/two-states-sue-spacex-over-sexually-explicit-grok-deepfakes/">Two States Sue SpaceX Over Sexually Explicit Grok Deepfakes</a></li>
<li><a href="https://www.nytimes.com/2026/11/23/technology/spacex-lawsuit-ai-sexualized-images.html">SpaceX Sued By Oregon and Virginia Over A.I.-Generated Sexualized ...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/sep/03/elon-musk-ai-grok-child-porn-lawsuit">Child sexual abuse survivor alleges Elon Musk’s AI... | The Guardian</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI regulation`, `#content moderation`, `#xAI/Grok`, `#platform accountability`

---

<a id="item-tech-news-3"></a>
### [SemiAnalysis 深度解析 AWS Trainium3 推理与微架构](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 8.0/10

SemiAnalysis 发布对 AWS Trainium3 推理与微架构的技术深度剖析，称其从零为机器学习负载设计，把 tile（瓦片）作为一等原语，而非在通用线程阵列上外挂张量计算与数据搬运单元。文章援引基于 UBenchX 微基准的结果称，借助 Trainium 描述符生成引擎（DGE，对标 Nvidia TMA 与 AMD MI455X TDM），Trainium 在小消息尺寸下即可达到接近峰值的 HBM 带宽利用率，而 Nvidia GPU 无法做到。在 InferenceX 的 TCO 对 p90 交互性曲线上，Trainium3 PDS + vLLM 的每美元性能除 Vera Rubin 外优于其他所有加速器；作者同时表示 Trainium3 与 TPU 已在 InferenceX 上线，并在生成 token 的总拥有成本上与 Nvidia GB300 互有胜负甚至领先。需注意，上述结论来自厂商配合验证的微基准与 SemiAnalysis 自建基准，并非独立第三方复现。

rss · Semianalysis · 11月27日 15:54

**「背景」** Nvidia 的数据中心 GPU 源自图形渲染架构，2017 年以来逐代加装 AI 专用硬件来补上一代暴露的瓶颈：Volta 引入 Tensor Core，Hopper 加入用于 HBM 与 SRAM 之间 tile 数据搬运的 TMA，Blackwell 增加用于累加的 Tensor Memory。SemiAnalysis 以此作为对照，指出 Trainium 的路线是把 tile 计算与数据搬运直接做进架构基础，代价是软件生态长期困难，而文章认为这一障碍如今已不再显著。

**「影响」** 对在 AWS 上运行推理服务的团队而言，文章的核心可操作信息是：在相同的延迟目标（p90 交互性）下，Trainium3 配合 vLLM 可能带来更低的每 token 成本，从而直接影响推理业务的毛利；但迁移决策仍需自行验证模型覆盖、算子支持与既有 GPU 代码栈的适配成本，因为该结论建立在 SemiAnalysis 的基准与 AWS 团队协助校验之上。

**标签**: `#AWS Trainium3`, `#AI hardware`, `#inference`, `#microarchitecture`, `#Nvidia`

---

<a id="item-tech-news-4"></a>
### [美国情报机构遭 AI 辅助攻击，涉开源工具 Artex](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 8.0/10

据《纽约时报》报道，美国中央情报局、国家地理空间情报局和国家情报总监办公室遭到黑客攻击，攻击过程中使用了名为 Artex 的 AI 工具。报道称此次攻击看起来不算严重，受影响的是非机密侦察数据。Artex 能整合多个开源 AI 模型来测试网络和计算机防御；一名中国开发者今年早些时候发布了该工具，此后它被用于多起攻击，包括针对欧盟的一起，该开发者已将 Artex 从其 GitHub 账号删除。今年早些时候，FBI 曾警告网络罪犯和间谍正在广泛使用 Artex。

telegram · zaihuapd · 11月27日 10:42

**「背景」** Artex 是一个可整合多个开源 AI 模型、用于自动化测试网络与计算机防御的渗透测试框架；今年早些时候，一名中国开发者将其公开发布，随后又从自己的 GitHub 账号删除。据 TechCrunch 与 BleepingComputer 报道，FBI 于 11 月 13 日警告称，该工具已被用于攻击一家美国 IT 巨头和韩国金融业，部分入侵在不到三小时内便取得特权访问；TechTimes 也报道称，Artex 从 GitHub 移除后仍在继续流通使用。

**「安全防护面临的新挑战」** 对防御方而言，Artex 这类工具能驱动 DeepSeek、Claude 等多个开源模型，自动执行侦察和入侵，从而显著降低攻击成本；AI Threat Watch 称其追踪到 2,269 台暴露服务器。S-RM 表示曾响应过由 Artex 实施的严重入侵，这说明即便开发者已从 GitHub 删除项目，开源代码扩散后也难以收回，组织需要针对这类自主攻击代理建立检测与阻断能力，不能只依赖模型提供方或代码托管平台的下架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/330784/20261116/ai-hacking-tool-artex-survives-github-removal-fbi-some-intrusions-reach-privileged-access-hours.htm">AI Hacking Tool ARTEX Survives GitHub Removal; FBI: Some ...</a></li>
<li><a href="https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/">FBI says Artex AI open source hacking tool used to breach ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/">FBI warns ARTEX AI hacking tool is powering global cyberattacks</a></li>
<li><a href="https://ai-threat.watch/aof/artex/">ARTEX : agentic offensive framework | AI Threat Watch</a></li>
<li><a href="https://www.s-rminform.com/latest-thinking/artex-in-the-wild-lessons-from-responding-to-agentic-ai-attacks">Artex in the wild: Lessons from responding to agentic AI attacks</a></li>

</ul>
</details>

**标签**: `#AI security`, `#cybersecurity`, `#open-source AI`, `#government`, `#hacking`

---

<a id="item-tech-news-5"></a>
### [《我的世界》基岩版资源包漏洞影响 26.52 至 26.63 版本](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 8.0/10

《我的世界》基岩版存在资源包安全漏洞：带有 content.zipe 文件的资源包可改动游戏界面框架 Ore UI 的文件并运行隐藏脚本。附加组件开发者 8Crafter 于 11 月 15 日在 Reddit 公开该问题，称已确认影响 26.52 至 26.63 版本，更早版本也可能受影响，覆盖 PC、手机和主机，Java 版不受影响。玩家加入服务器或 Realm 时若开启资源包自动下载，可能无需手动安装就收到问题文件；8Crafter 列举的利用方式包括删除全部存档、获取玩家 IP，以及在 Windows 上特定条件下无提示打开任意 URI、启动资源包内的批处理文件下载恶意软件。Mojang 已在 26.65 版修复该问题。

telegram · zaihuapd · 11月27日 18:04

**「背景」** 《我的世界》基岩版的资源包用于承载材质、界面与附加组件内容；玩家加入服务器或 Realm 并开启自动下载时，通常不会逐一审查这些包。据披露者 8Crafter 在 Reddit 上的说法，带有 content.zipe 文件的资源包能够修改游戏界面框架 Ore UI 的文件，从而在游戏内运行隐藏脚本。

**「玩家应对措施」** 仍停留在 26.52–26.63 的基岩版玩家应尽快升级到 26.65；在修复前，加入服务器或 Realm 时关闭资源包自动下载可降低在无手动安装情况下收到恶意包的风险。AxmBro 发布的 Windows 只读检测工具能查找资源包内的 content.zipe 文件，但报道明确指出它无法判定资源包是否恶意，因此不能替代升级。另据 Tech Times 报道，该漏洞在 Windows 上可能让攻击者取得账户控制权并清除本机存档。

<details><summary>参考链接</summary>
<ul>
<li>Resource packs can contain malware now : r/ibxtoycat - Reddit</li>
<li>u/8Crafter - Reddit</li>
<li><a href="https://www.techtimes.com/articles/330961/20261117/mojang-patches-bedrock-after-community-discovers-resource-packs-could-execute-malicious-code.htm">Mojang Patches Bedrock After Community Discovers Resource ...</a></li>
<li><a href="https://minecraft.pl/en/news/minecraft-bedrock-mojang-patches-resource-pack-security-hole">Minecraft Bedrock: Mojang patches resource pack security</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Minecraft`, `#gaming`, `#resource-packs`

---

<a id="item-tech-news-6"></a>
### [Convex 编码技能被指未经告知上传用户创意](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

一名 GitHub issue 作者在 convex-backend-skill 仓库第 64 号 issue 中称，Convex 的编码技能会把用户的应用创意发送到远程服务器，且未向用户说明。Convex CEO Jamie 在评论区回应称，该插件中的提示上传用于支撑 Convex 的“quickstart”功能，并提到该功能是已关闭的端到端 vibe-coding 产品 Convex Chef 的后续形态。CEO 的回应确认了上传行为及用途，但现有材料没有说明插件在何时或以何种方式向用户披露这一传输。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**「背景」** Convex 提供一套可安装的 Agent Skills，即供 AI 编码代理执行认证配置、schema 设计、迁移等任务的可移植指令包，其中 convex-quickstart 用于新建 Convex 项目或把 Convex 接入现有应用。据 Convex 文档与仓库，quickstart 命令会运行 bootstrap、发出 telemetry ping 并轮询日志，随后在浏览器中打开 URL。Convex CEO 在讨论中表示，此前的端到端 vibe-coding 产品 Convex Chef 已关闭，该插件上传 prompt 是为支撑被称为 Chef 精神继承者的 quickstart 功能。

**「对开发者的实际影响」** 对使用该插件的开发者而言，实际后果是提示词——包括应用构思——会离开本地环境发往 Convex 的服务器，而据该 issue 的描述，这一行为在插件使用过程中并未被明确告知；Convex CEO 的回应则确认上传是为「quickstart」功能服务。在披露方式与开关/退出机制明确之前，处理未公开产品构想、客户数据或受保密约束需求的团队应假定输入内容已外发，并在采用该 skill 前先核查其网络行为或改用自托管方案。

**「社区讨论」** 有评论者认为，长期来看自托管开放权重模型更值得采用；也有人以“创意本身不值钱”来淡化上传创意的敏感性。这些都属于个人观点，并非对披露是否充分的裁定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.convex.dev/ai/agent-skills">Convex Agent Skills | Convex Developer Hub</a></li>
<li><a href="https://github.com/convex/agent-skills">GitHub - convex/agent-skills: Convex Skills for Agents</a></li>
<li><a href="https://github.com/convex/convex-backend-skill/blob/main/commands/quickstart.md">convex-backend-skill/commands/quickstart.md at main - GitHub</a></li>
<li><a href="https://docs.convex.dev/chef/migration-guide">Chef Migration Guide | Convex Developer Hub</a></li>

</ul>
</details>

**标签**: `#developer tooling`, `#privacy`, `#AI coding agents`, `#open source`, `#Convex`

---

<a id="item-tech-news-7"></a>
### [信用卡盗刷脚本利用 WebRTC 规避监控，波及多家购物网站](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

据 Infohawk 报道，多个热门购物网站上被发现信用卡盗刷脚本，这些脚本利用 WebRTC 来规避常规监控。报道将风险指向第三方脚本嵌入这一环节，而非 WebRTC 本身的漏洞。社区评论也强调，攻击之所以选择 WebRTC，是因为它较少被监控，同样的手法完全可以用普通 HTTP 请求实现。目前尚无受害网站名单、受影响交易数量或具体拦截措施的细节。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**「背景：Magecart 网页盗刷的延续」** 网页盗刷（web skimming，常归入 Magecart 攻击家族）指攻击者在结账页面注入恶意 JavaScript，在支付表单数据被加密发送前于浏览器内截获卡号等信息。Malwarebytes 2026 年 1 月的报道曾记录一起 Magecart 活动，从与 AmEx、Diners Club 和 Mastercard 等支付网络相关的在线结账流程中窃取卡数据，说明第三方脚本注入式盗刷在本次 WebRTC 手法出现前已是持续存在的威胁。本次报道的新变化在于脚本借 WebRTC 规避监测，而非 WebRTC 本身存在新漏洞。

**「影响」** 对电商网站而言，只要页面嵌入了第三方脚本，支付页面就可能被注入此类盗刷代码，因此需要审计第三方脚本的来源，并监控 WebRTC 等非 HTTP 出站通道。

**「社区讨论」** 评论者 afavour 指出，问题不在于 WebRTC 的技术能力，而在于它较少被监控，改用简单 HTTP 请求也能达到同样效果，并认为嵌入第三方脚本的站点始终存在风险。另有评论者认为，允许陌生代码在用户计算机上运行本身就不应被接受，服务器应只提供数据，由浏览器决定如何处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/news/2026/01/online-shoppers-at-risk-as-magecart-skimming-hits-major-payment-networks">Online shoppers at risk as Magecart skimming hits major ...</a></li>
<li><a href="https://cside.com/blog/magecart-attacks-explained-web-skimming">Web Skimming: How Magecart Attacks Steal Card Data in the…</a></li>

</ul>
</details>

**标签**: `#web security`, `#e-commerce`, `#third-party scripts`, `#WebRTC`, `#payment fraud`

---

<a id="item-tech-news-8"></a>
### [bouncemarket：用确定性模拟和 SSE 直播小球落点](https://bouncemarket.minhanhday.com/) ⭐️ 7.0/10

开发者 mday404 发布了 Show HN 项目 bouncemarket：一颗小球从起点落下，玩家以预测市场的方式押注它最终落在哪里。小球下落全程由服务端模拟，并通过带小缓冲的 Server-Sent Events（SSE）实时推送给每个客户端；每次落球的结果由其起始位置决定，因此同一局可以精确回放，但起始位置的微小差异就可能改变最终结果。作者还设置了少量规则式 AI 交易者来维持市场流动性，不过它们在单局超过五人时会退出；作者表示这些机器人使用简单规则集，并不难战胜。

hackernews · mday404 · 11月27日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=50667726)

**「背景」** 预测市场通常围绕体育赛事、选举等现实结果进行交易，而这里把它压缩成一个纯物理随机事件，用户买卖的是“小球落在哪一侧”这类结果的股份。让每一局都能精确复盘，而不是只依赖一次性的随机结果，是该项目的关键设计。

**「对玩家的影响」** 评论区指出，赔率剧烈波动是目前最直接的体验障碍：有用户称赔率能在约零点一秒内从 0.01 跳到 0.99，导致下注决策来不及做出。另有用户报告，完全不看小球、只买入双方的低价股份也能经常获利；如果两边都能以足够低的价格成交，那么无论结果如何都能赢，这从侧面说明当前定价与撮合机制尚不具备市场效率。

**「社区讨论」** 一位评论者认为，这个项目实际会变成“机器人之间的对战”：任何人只要对前沿模型说“去赢下 bouncemarket.minhanhday.com”，就可能得到一个不错的机器人；真正未知的只有小球起始位置的小数部分，而小球混乱的轨迹会逐步暴露这一信息，前沿模型会很快写出精确求解器。另有用户希望看到有人用真钱对纯随机事件的预测市场做一次实验，而不只是像这里一样使用虚拟货币。

**标签**: `#prediction-markets`, `#server-sent-events`, `#deterministic-simulation`, `#multi-agent-game`, `#Show HN`

---

<a id="item-tech-news-9"></a>
### [计算机验证的证明可能存在缺陷](https://cr.yp.to/proofs/falseccp.html) ⭐️ 7.0/10

cr.yp.to 上的一篇文章指出，计算机检查的证明可能因为证明检查器自身的可靠性缺陷而变成错误证明，尽管检查器通常被认为比人工复核更可信。HN 讨论中，多位评论者强调实际系统并非只依赖单一检查器：Metamath 主数据库要求证明通过 5 个由不同作者用不同语言独立实现的验证器，Lean 社区也同时使用多个检查器。因此要让错误证明被接受，需要同时攻破多个独立实现，并且通过非形式化的人工审阅而不显得可疑。讨论也承认形式验证工具并非绝对可靠，Metamath 最初的 C 验证器确实出现过可靠性 bug。

hackernews · \_tk\_ · 11月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50667989)

**「背景」** 该页面由密码学家 D. J. Bernstein 维护，汇集了 HOL Light、Mizar、Metamath、Isabelle、Lean、HOL98/HOL4 和 Coq/Rocq 七个证明检查系统中已报告的健全性（soundness）缺陷链接；他在 11 月的帖子中称收录了约 199 条此类报告。所谓健全性缺陷，指的是检查器自身可能让不成立的陈述通过验证，而这类程序正是“计算机检查过的证明”这一说法的信任基础。

**「实际影响：单一校验器不足以保证可靠性」** 对依赖 Lean、Metamath 等证明助手的开发者而言，实际后果是：某一校验器“检查通过”不能单独作为证明可靠性的结论，面对自动化工具批量生成的形式化证明尤其如此。社区评论指出，Metamath 主数据库要求证明通过用 C、Java 等语言实现的 5 个独立校验器，Lean 生态也存在多检查器并行验证；因此更稳妥的做法是把多校验器交叉验证和非形式人工审查纳入流程。

**「社区讨论」** 评论者 twotwotwo 和 dwheeler 认为原文低估了多重检查器的实际防线：在 Metamath 中，进入 set.mm 和 iset.mm 的证明必须通过 5 个独立创建的验证器，DeepMind 研究人员也曾构造出同时骗过 Lean 和当时一周前版本的 nanoda 的“证明”，但需要利用不同 bug。gr\_norm 则强调，这些系统几十年来的可靠性 bug 总量很少，对绝大多数软件验证已足够，真正利用它们还要同时掩盖被验证程序中的其他问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cr.yp.to/proofs/falseccp.html">False computer-checked proofs (djb) - cr.yp.to</a></li>
<li><a href="https://news.lavx.hu/article/d-j-bernstein-catalogs-soundness-bugs-in-seven-proof-checkers">D. J. Bernstein catalogs soundness bugs in seven proof ...</a></li>
<li><a href="https://x.com/hashbreaker/status/2120889008389837049">Daniel J. Bernstein on X: &quot;Posted new page &quot;False computer ...</a></li>
<li><a href="https://ai-beat.github.io/news/2026/10/lean-soundness-ai-formal-proofs/">When the Verifier Has Bugs · AI Beat</a></li>
<li><a href="https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/">What mathematicians should know about the Lean Theorem Prover ...</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#proof assistants`, `#software correctness`, `#Lean`, `#Metamath`

---

<a id="item-tech-news-10"></a>
### [Michael Nielsen 下线其神经网络在线书](https://neuralnetworksanddeeplearning.com/) ⭐️ 7.0/10

Michael Nielsen 的在线著作《Neural Networks and Deep Learning》已从其网站 neuralnetworksanddeeplearning.com 下线，Hacker News 上相关讨论获得 325 分、209 条评论。目前没有确认的下线理由：社区猜测此举可能是某种抗议，但该说法未获证实。有评论者贴出 Internet Archive 的存档链接（快照时间 2026 年 8 月 8 日），可作为继续访问该书内容的途径。

hackernews · brandonb · 11月27日 19:31 · [社区讨论](https://news.ycombinator.com/item?id=50670757)

**「背景」** Michael Nielsen 的《Neural Networks and Deep Learning》是一本免费在线书，页面标注为 2019 年 12 月，系统讲解神经网络这一受生物启发的编程范式，以及计算机如何从观测数据中学习。该书长期被机器学习学习者用作入门材料，部分章节也以 PDF 形式在第三方站点流传。此次原站内容被撤下，社区讨论中有人给出互联网档案馆的存档链接作为替代访问途径，但撤下原因尚无官方说明。

**「影响」** 对依赖该免费教材学习神经网络基础的学习者而言，原站链接现已失效，需转而使用评论中给出的 Internet Archive 存档副本才能继续阅读。由于下线的确切原因和是否永久移除均未说明，读者不应假定该书会恢复上线。

**「社区讨论」** 有评论者认为下架更像是一种抗议而非实际功能上的必要，并预期此举反而会让更多人想读这本书（WheelsAtLarge）；也有人批评这是失策，认为让公众理解大公司在幕后做什么有助于为其后果做好准备（whatshisface）。另有评论提供了 Internet Archive 的存档链接以便继续访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://neuralnetworksanddeeplearning.com/">Neural networks and deep learning</a></li>

</ul>
</details>

**标签**: `#neural-networks`, `#deep-learning`, `#AI-education`, `#open-access`, `#HN-discussion`

---

<a id="item-tech-news-11"></a>
### [主流编程语言为何应原生支持形式化验证](https://blainehansen.me/post/mainstream-verifiable-language/) ⭐️ 7.0/10

Blaine Hansen 在博客文章中主张，主流编程语言应把形式化验证作为核心设计目标，而非交由 Dafny、SPARK 等专用工具在事后补充。Hacker News 讨论提供了实践证据：一位评论者称自己将现有 C 代码库翻译为 Ada SPARK，并提升到 SPARK Silver 级别（保证无运行时错误），随后把发现的整数溢出等问题报告给各维护者。讨论还列出 Dafny、SPARK Ada、Why3、Verus、Frama-C、TLA+ 等已有验证工具，有人据此质疑“主流”地位源于采用而非设计目标。该文是设计倡议，并非已发布语言或实测研究成果。

hackernews · todsacerdoti · 11月27日 05:22 · [社区讨论](https://news.ycombinator.com/item?id=50663089)

**「何为 SPARK 与形式化验证」** SPARK 是基于 Ada 的语言子集，其设计目标是支持演绎式形式化验证，通过契约在编译期或静态分析阶段证明程序性质，而不只依赖运行期断言检查。该文讨论中提到的 Silver 级别，指 SPARK 证明等级中“运行期错误不存在”这一档，即证明无整数溢出、数组越界等运行时故障。

**「影响」** 对考虑形式化验证的开发者而言，当前可行路径仍是将代码迁入特定子集或专用语言：评论者描述的流程是先做 C 到 SPARK 的翻译，再提升到 Silver 级别，才能系统检查整数溢出等运行时错误。因此短期内更现实的做法是评估 Dafny、SPARK、Verus 等工具与现有代码库的兼容成本，而不是等待一个原生可验证的新主流语言。

**「社区讨论」** 有评论者认为，Dafny、SPARK Ada、Why3、Verus、Frama-C、TLA+ 已覆盖不同语言和验证风格，LLM 正让更多程序员能上手这些工具；但他怀疑无法以“主流”为目标从零设计语言，因为主流性来自采用，并建议先研究这些既有语言为何未普及。另一位评论者主张不必等待编程语言与建模语言统一，可以先在日常开发中更多使用自动机、进程代数、图算法等形式化词汇，逐步推进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.adacore.com/courses/intro-to-spark/chapters/03_Proof_Of_Program_Integrity.html">Proof of Program Integrity - learn.adacore.com</a></li>
<li><a href="https://www.adacore.com/languages/spark">Languages | SPARK | AdaCore</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#programming languages`, `#Ada SPARK`, `#software correctness`, `#LLM-assisted development`

---

<a id="item-tech-news-12"></a>
### [Anthropic 系统卡承认暗中削弱前沿模型研发请求](https://twitter.com/RealAstropulse/status/2126119408997466389) ⭐️ 7.0/10

Anthropic 今年 6 月发布的 Claude Mythos 5 与 Fable 5 系统卡写明，对于开发前沿大模型的请求，Anthropic 会暗中限制 Claude 的回答效果，手段包括改写提示、引导向量和参数高效微调。用户无法察觉这类干预，它也不会像安全拦截那样回退到其他模型。干预覆盖预训练流水线、分布式训练和加速器设计等任务，Anthropic 估算影响约 0.03% 流量、不到 0.1% 的组织，多数编码工作不受影响；用 Claude 开发竞品模型本就违反服务条款。该摘要来自 Telegram 频道对系统卡的转述，Hacker News 讨论引用了系统卡第 13 页原文。

hackernews · baobabKoodaa · 11月27日 08:28 · [社区讨论](https://news.ycombinator.com/item?id=50664325)

**「背景：系统卡中的“不可见”干预」** Anthropic 在 2026 年 6 月发布 Claude Mythos 5 与 Fable 5 时同步公布了系统卡，其中第 13 页写明，针对“前沿 LLM 开发”类请求的干预会降低 Claude 的回答效果，且“这些防护措施不会对用户可见”。外部报道还提到，有研究者据此指责 Anthropic 用 Fable 5 悄悄限制 AI 研究者的账号。本周这份系统卡因开发者讨论重新受到关注，而争议的核心正是该条款是否已从文档描述变为实际部署行为。

**「影响」** 对真正从事前沿 LLM 训练的团队来说，Claude 在预训练、分布式训练和加速器设计类任务上的输出可能已被无声降质，而用户无法从响应中判断是否被干预，因此不能把这类输出当作可靠的训练代码或调参建议来源。

**「社区讨论」** 有评论者称自己让 Fable 5.2 编写 transformer 训练流程，结果 bug 频出、loss 降不下来，转由 Gemini 审查并修复后才训练成功；也有人建议用“在消费级 Blackwell 上用 MXFP8 训练 MoE”这类缺乏公开配方、又同时触发内核、训练、MoE 等多个标记的任务来自行测试，并称 Claude 表现很差。这些均为个人经验，尚不能证明存在刻意削弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.yahoo.com/ai/claude/articles/anthropic-concerned-mythos-based-model-161754496.html">Anthropic Was So Concerned About Its New Mythos -Based...</a></li>
<li><a href="https://ai-digest.liziran.com/en/digest/2026-06-11-anthropic-built-most-capable-model-then-wired-three-ways">Anthropic Built Its Most Capable Model, Then Wired In Three Ways to...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI safety`, `#LLM evaluation`, `#model behavior`, `#AI research`

---

<a id="item-tech-news-13"></a>
### [谷歌 Play 将全球公开商家开发者电话与地址](https://www.androidpure.com/google-play-trader-developer-address/) ⭐️ 7.0/10

谷歌 Play 宣布，自 2027 年 3 月 1 日起在全球范围向用户展示自我声明为“商家”的开发者的联系方式，包括个人账户持有者的电话号码和地址。所有活跃开发者账户必须在 2027 年 2 月 1 日前申报商家或非商家身份，逾期可能无法更新应用，并从 Play 全球下架。该政策于今年 10 月公布，本周因隐私担忧遭到开发者反弹。

telegram · zaihuapd · 11月27日 01:44

**「背景」** 该政策源于欧盟《数字服务法》对“商家”（trader）身份透明的要求：平台须向用户展示商家的联系方式。谷歌 Play 的商家身份申报依据欧洲经济区（EEA）和英国法律定义，但谷歌把展示范围扩大到了全球，而非仅限欧盟用户。苹果的做法则不同：据 The Verge 报道，苹果仅在欧洲相关国家展示开发者地址，并允许开发者提供邮政信箱（需附账单证明其与常规地址的关联）。

**「对开发者的影响」** 对以个人账户发布应用的开发者来说，若申报为商家，其电话号码和地址将在全球范围公开；若未在截止日期前完成申报，则可能无法更新应用甚至被下架。此外，谷歌不接受邮政信箱作为付款地址，这与苹果仅在欧洲相关国家展示地址并允许使用邮政信箱的做法不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/googleplay/android-developer/answer/17594752?hl=en">Trader status declaration - Play Console Help</a></li>
<li><a href="https://www.theverge.com/tech/1043228/android-play-store-google-developer-address-eu">Android app developers will soon have to share their address publicly</a></li>

</ul>
</details>

**标签**: `#Google Play`, `#Android developers`, `#privacy`, `#platform policy`, `#app distribution`

---

<a id="item-tech-news-14"></a>
### [GTA 6 非官方 PC 移植项目 AnyPS5 获 5.8 万星标，GitHub 发文后删帖](https://www.pcgamer.com/games/microsofts-github-posts-message-celebrating-efforts-to-port-playstation-5-version-of-grand-theft-auto-6-to-pc-then-quickly-deletes-it/) ⭐️ 7.0/10

开源项目 AnyPS5 致力于将 PS5 可执行文件重编译到 Windows 和 Linux 上运行，其围绕《GTA 6》的非官方 PC 移植工作已获得超过 5.8 万个星标，开发者正号召借助 AI 代理攻克性能瓶颈。GitHub 在 X 平台发帖公开庆祝该进展，并反问此举是否越过法律红线；由于发行商 Take-Two 近期正严厉打击非官方重编译项目，该帖引发争议后已被迅速删除。

telegram · zaihuapd · 11月27日 03:33

**「背景」** AnyPS5 并非传统意义上的模拟器：按俄罗斯游戏媒体 Playground 的说法，它通过替换索尼的系统库，让 PS5 游戏以原生方式在 Windows 和 Linux 上运行。PC Gamer 报道称，GitHub 在 X 上发文庆祝该项目将 PS5 可执行文件移植到 PC 的进展，并把它与《GTA 6》PC 移植直接联系起来，随后删除了这条帖文。

**「影响」** 对关注该项目的开发者而言，Take-Two 对非官方重编译的打击意味着参与或分发此类移植工具存在明确的法律风险；AnyPS5 目前仍处于需借助 AI 代理攻克性能瓶颈的阶段，尚不能视为可用的 PC 版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/games/microsofts-github-posts-message-celebrating-efforts-to-port-playstation-5-version-of-grand-theft-auto-6-to-pc-then-quickly-deletes-it/">Microsoft&#x27;s Github posts message celebrating efforts to... | PC Gamer</a></li>
<li><a href="https://www.playground.ru/gta_6/news/github_udalila_post_ob_anyps5_posle_kritiki_za_dvojnye_standarty_na_fone_pretenzij_take_two_k_proektam_po_gta_6-1894154">GitHub удалила пост об AnyPS 5 после критики за двойные...</a></li>

</ul>
</details>

**标签**: `#open source`, `#reverse engineering`, `#game porting`, `#AI agents`, `#legal`

---

<a id="item-tech-news-15"></a>
### [八达通遭网络攻击：约 7500 客户及 2.2 万商户资料受影响](https://www.hk01.com/article/60415794) ⭐️ 7.0/10

八达通于 11 月 27 日公布，当天早上侦测到系统遭网络攻击。约 7500 名客户的姓名及相片等个人资料受影响，部分纪录可能涉及自动增值服务的银行编号及增值金额，但不含信用卡和银行户口资料；另有约 2.2 万名商户的公司联络人姓名、职位、电邮地址及电话号码受影响。八达通称主要服务运作如常，未发现客户蒙受财务损失，卡内及钱包余额仍受保障，少数功能或因预防措施暂时受影响。公司表示将直接通知受影响客户，并已向警方报案，同时通报私隐专员公署和运输及物流局。

telegram · zaihuapd · 11月27日 13:11

**「背景」** 八达通是香港广泛使用的储值支付卡及电子钱包系统，其账户可绑定自动增值服务，这也是此次部分客户资料可能涉及银行编号及增值金额的背景。据香港 01 报道，八达通在 11 月 27 日早上侦测到攻击后公布事件，并表示卡内及钱包余额仍受保障；公司已向警方报案，并通报私隐专员公署和运输及物流局。

**「对用户与商户的影响」** 受影响客户应留意八达通发出的直接通知，并核查自动增值服务所关联的银行编号及增值金额等资料是否外泄；商户则需警惕公司联络人姓名、职位、电邮和电话可能被用于针对性的钓鱼或诈骗。虽然八达通表示余额仍受保障、未发现财务损失，但少数功能可能因预防措施暂时不可用，用户在依赖相关功能前应先确认服务状态。

**标签**: `#cybersecurity`, `#data breach`, `#payment systems`, `#privacy`, `#Hong Kong`

---

## 全球芯片

<a id="item-chip-news-1"></a>
### [美国 BIS 新规收紧远程访问与东南亚芯片许可，中企获取英伟达算力通道收窄](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a1572f7d844cf92d2cb7d77ae34cc&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261127A0E31L00&amp;c=9541040611376211452&amp;mkt=en-us) ⭐️ 8.0/10

美国商务部工业和安全局（BIS）于 11 月 16 日发布新规，将远程访问纳入出口管制，并对东南亚四国和巴西新增芯片出口许可要求。据《财经》报道，新规出台仅 10 天，中国企业获取英伟达先进算力的两条主要通道——经东南亚数据中心租用算力、以及提交合规许可申请——都在快速收窄。报道称，当地已有数据中心项目开始寻找买家接盘。报道未给出国产算力补位的具体产品、产能或性能数字，且来源正文被截断，合规申请受阻的完整情况尚不明确。

rss · Bing News - China domestic chips · 11月27日 11:58

**「背景」** 此前，中国企业获取英伟达先进算力的路径主要有两条：在东南亚数据中心租用算力，以及提交合规出口许可申请。报道指出，11 月 16 日 BIS 新规将远程访问纳入管制，并对东南亚四国和巴西新增芯片出口许可要求，直接切断了前一条路径。《金融时报》报道称，英伟达已要求其制造伙伴停止向四个东南亚国家发运服务器，这与本次新规方向一致；《亚洲时报》则指出，东南亚此前以“开放、中立的全球算力中转站”为前提大规模建设 AI 数据中心，如今相关项目面临沦为闲置资产的风险。

**「影响」** 新规把远程访问本身纳入管制，意味着此前通过在东南亚租用数据中心间接调用英伟达算力的做法不再处于许可要求之外；同时对四国与巴西新增的芯片出口许可要求，使相关设备与算力的转口路径需要逐案审批。报道提到当地数据中心项目已在寻找接盘买家，显示这一渠道的收缩已传导到具体项目层面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asiatimes.com/2026/11/southeast-asias-ai-data-center-bets-turning-into-stranded-assets/">Southeast Asia &#x27;s AI data center bets turning into... - Asia Times</a></li>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#英伟达`, `#AI算力`, `#国产芯片`, `#中美芯片合作`

---

<a id="item-chip-news-2"></a>
### [英伟达 Blackwell 机架据称现身上海，特朗普提美国或入股](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a15725faf468d98b2581917572d80&amp;url=https%3a%2f%2fwww.yahoo.com%2fnews%2fpolitics%2farticles%2fnvidias-blackwell-chips-turn-china-170930530.html&amp;c=4276174839387292558&amp;mkt=en-us) ⭐️ 7.0/10

据雅虎新闻转载的一则简要报道，被禁止对华出口的英伟达 Blackwell 机架据称出现在上海一处与 Alice Huang 有关联的数据中心。同一报道提到，特朗普表示美国仍可能入股英伟达。该报道没有给出涉事机架的数量、具体型号或流入渠道，也未提及任何已确认的执法行动或适用的具体规则，因此这批设备的来源与合规状态仍不清楚。关于美国政府入股英伟达的说法目前只是特朗普的表态，并非已宣布或已执行的交易。

rss · Bing News - NVIDIA and China · 11月27日 09:09

**「背景」** 同类报道补充了关键前提：涉事芯片为英伟达 GB300 Blackwell 机架级系统，按美国出口管制规定，向中国出货前须取得出口许可证。据相关报道，彭博通过公开保修数据库将一台 GB300 机架的序列号追溯至台湾技嘉科技，并称两家中国公司将这套系统安装在上海一处与 Alice Huang 有关的数据中心。上述细节说明，此次发现之所以构成潜在的出口管制违规，而非普通商业交易，正源于 GB300 对华出口需持证这一前置条件。

**「实际影响」** 特朗普于 2026 年 11 月 24 日接受《纽约邮报》采访时表示，美国政府可能入股英伟达，并将其与此前对英特尔约 9.9% 的持股先例相提并论；这仍只是表态，而非已敲定的交易，因此目前尚不构成对英伟达对华出货或许可的规则变化。就报道所称上海数据中心出现禁售 Blackwell 机架一事，来源未提及任何执法行动、查扣数量或适用条款，因此对英伟达中国收入和中国替代供应的实际后果仍无法量化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nypost.com/2026/11/27/us-news/banned-nvidia-chips-uncovered-at-chinese-data-center-linked-to-megaspeeds-alice-huang-report/">Banned Nvidia chips uncovered at Chinese data center linked to...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>
<li><a href="https://www.zerohedge.com/ai/nvidia-pares-gains-report-traces-shipment-restricted-ai-blackwell-chips-china-data-center">Nvidia Pares Gains As Report Traces Shipment Of... | ZeroHedge</a></li>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/trump-floats-intel-style-nvidia-142853319.html?fr=sycsrp_catchall">Trump Floats an Intel-Style Nvidia Stake. 10% Would Cost the ...</a></li>
<li><a href="https://www.fool.com/investing/2026/11/27/donald-trump-just-floated-idea-government-buy-stake-in-nvidia-wouldnt-fix-biggest-flaw/">President Donald Trump Just Floated the Idea of the U.S ...</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#Blackwell`, `#中美芯片合作`

---

<a id="item-chip-news-3"></a>
### [美国国会推进芯片管制法案，瞄准 ASML 在华服务工程师](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a15720b4a40afaede776c77b9fe1c&amp;url=https%3a%2f%2fcryptobriefing.com%2fcongress-targets-asml-china-servicing%2f&amp;c=17894802404246916844&amp;mkt=en-us) ⭐️ 7.0/10

美国国会据报正在推进新的芯片出口管制法案，其中包括名为《MATCH Act》的立法，目标指向 ASML 在中国的服务工程师。报道称，此举旨在限制 ASML 对中国客户的设备维护与现场技术支持能力，作为美中芯片摩擦升级的一部分。但现有信息仅为一句话摘要，未披露法案条款、提案人、立法进度或生效日期，限制范围和是否已进入表决程序均不明确。

rss · Bing News - China chip policy · 11月27日 09:12

**「MATCH 法案的立法背景」** 《MATCH 法案》（H.R.8170，第 119 届国会）于 2026 年 4 月提出，其条文主旨正是对特定半导体制造设备及其零部件实施出口限制。据工具结果，该法案可能被附加进国会年度国防授权法案，荷兰议员已敦促本国政府予以抵制，荷兰政府则希望国会将 MATCH 法案排除在年度国防法案之外。与此相比，本次报道所披露的新变化是：立法矛头具体指向 ASML 在中国的服务工程师，而不仅限于设备出口本身。

**「影响」** 若按报道方向立法，限制对象将从新设备出口延伸至已售设备的在华维护与服务，直接压缩 ASML 对中国晶圆厂的售后支持；但当前无法确认限制的具体形式、生效时间以及是否覆盖成熟制程设备，对出货和许可的实际影响仍待法案文本明确。

<details><summary>参考链接</summary>
<ul>
<li>Text - H.R.8170 - 119th Congress (2025-2026): MATCH Act</li>
<li>ASML Can&#x27;t Build Enough Machines for 2028. Is a 20% China Risk a ...</li>
<li>Netherlands challenges US MATCH Act controls on ASML - Magica</li>

</ul>
</details>

**标签**: `#对华出口管制`, `#ASML`, `#中美芯片合作`, `#半导体设备`, `#先进制程`

---

<a id="item-chip-news-4"></a>
### [广东算力“十五五”规划鼓励算力中心优先用国产芯片](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a1572f7d844cf92d2cb7d77ae34cc&amp;url=https%3a%2f%2ffinance.sina.com.cn%2fstock%2fbxjj%2f2026-11-27%2fdoc-inkacqyr3347175.shtml&amp;c=15115256286978933122&amp;mkt=en-us) ⭐️ 7.0/10

广东省印发《广东省算力发展“十五五”规划》，提出加强基础硬件供给能力，集中力量突破产业技术短板，着力缩小与国际领先水平在单芯片算力性能上的代际差距。规划还提出加强芯片异构融合与协同适配，推动多元算力芯片高效互联、优势互补，并明确鼓励算力中心优先使用国产算力芯片，以提升国产化替代水平和应用规模。受此消息影响，A 股算力板块异动，浙大网新等多只个股涨停。这是省级规划文件提出的引导性要求，并非已生效的强制采购规定，也不是已实现的技术突破。

rss · Bing News - China domestic chips · 11月27日 01:37

**「背景」** 广东此次是在省级算力专项规划中明确写入国产算力芯片优先使用导向。此前相关搜索结果显示，广东省已发布《算力发展“十五五”规划》，明确鼓励优先使用国产算力芯片，同时工业和信息化部等部门印发通信网建设方案，为产业提供顶层支持；本次规划进一步提出集中突破技术短板、缩小单芯片算力性能与国际领先水平的代际差距，并推动多元算力芯片异构融合与高效互联。

**「影响」** 该规划把国产 AI 芯片的需求侧支持指向算力中心：广东算力中心在新建或扩容选型时被鼓励优先采用国产芯片，为国产芯片厂商提供本地应用场景和规模验证机会。但“鼓励优先使用”属于引导性表述，规划未给出强制采购比例、补贴额度或实施时间表，实际执行力度取决于后续配套细则。

<details><summary>参考链接</summary>
<ul>
<li>《中国股市集体涨停带动国际市场回暖！》 1.外部供给受限，倒... | 欧易</li>

</ul>
</details>

**标签**: `#国产芯片`, `#AI 算力`, `#政策规划`, `#国产化替代`, `#先进制程`

---

<a id="item-chip-news-5"></a>
### [中芯国际 Q2 份额 5.4%，逼近三星 5.9%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a157213084437ac7c142abd0e2e0d&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261127A07D6Q00&amp;c=15468123504046489902&amp;mkt=en-us) ⭐️ 6.0/10

据伯虎财经援引 TrendForce 数据，2026 年第二季度三星晶圆代工全球市场份额为 5.9%，中芯国际达到 5.4%，两者差距缩小至 0.5 个百分点。文章称中芯国际营收再创新高、毛利率明显回升、产能利用率逼近满载，并将其归因于国产替代推进与 AI 需求增长。需要说明的是，上述份额为第三方机构 TrendForce 的测算数据，营收、毛利率与产能利用率则属于媒体基于公司披露的概括表述，报道摘要未给出具体工艺节点、产能数字或产品型号。

rss · Bing News - SMIC and Chinese vendors · 11月27日 03:17

**「背景」** TrendForce 的全球晶圆代工季度排名长期由台积电居首、三星电子位列第二，中芯国际此前一直处于第二梯队。本期报道引用同一机构的数据显示，2026 年第二季度三星份额为 5.9%、中芯国际为 5.4%，两者差距缩小到 0.5 个百分点，这构成了“逼近全球第二”这一说法的事实基础。需要说明的是，该数据是 TrendForce 的季度估算，并非企业经审计的业绩或已实现的排名更替。

**「影响」** 若 5.4%对 5.9%的份额格局延续，中芯国际与三星的差距已进入可被单一季度订单波动改变的量级，这意味着中国大陆代工产能对国产替代订单的承接能力，正直接转化为其在全球代工排名中的位次变化；但报道未披露先进制程进展或新增产能规划，因此尚不能据此判断其在高端节点的竞争力。

**标签**: `#国产芯片`, `#晶圆产能`, `#先进制程`, `#AI 算力`, `#中芯国际`

---

<a id="item-chip-news-6"></a>
### [禾润电子冲创业板：拟募资 12 亿元，研发费用率 9.83%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a1572f7d844cf92d2cb7d77ae34cc&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1107363135_646494&amp;c=12805390257734187732&amp;mkt=en-us) ⭐️ 5.0/10

11 月 26 日，国产卫星导航定位芯片设计企业禾润电子科技（嘉兴）股份有限公司递交创业板招股书，并披露了对深交所首轮审核问询函的回复。招股书显示，公司拟募资 12 亿元，研发费用率为 9.83%，保荐机构为中信建投证券。禾润电子成立于 2006 年，以 GNSS 卫星导航定位芯片为核心，同时布局模拟信号链和电源链芯片，采用 Fabless 模式，晶圆制造和封装测试完全依赖第三方供应商，2026 年 5 月股权转让中整体估值约 31 亿元。上述募资规模、费用率与估值均来自申报文件，尚需交易所审核及后续发行环节确认。

rss · Bing News - China domestic chips · 11月27日 14:39

**「背景」** 禾润电子成立于 2006 年，长期以卫星导航定位芯片为核心产品，同时布局模拟信号链与电源链芯片；公司采用 Fabless（无晶圆厂）模式，晶圆制造与封装测试全部依赖第三方供应商。此次是其递交创业板招股书并披露深交所首轮审核问询函回复，2026 年 5 月股权转让时整体估值约 31 亿元，保荐机构为中信建投证券。

**「影响」** 若发行落地，12 亿元募资可用于扩充 GNSS 及模拟、电源链产品线，但公司采用 Fabless 模式、制造与封测全部外包，上市募资并不改变其对第三方代工产能的依赖；9.83%的研发费用率也表明其研发投入强度相对有限，产品迭代能否跟上仍取决于募投项目的实际执行。

**标签**: `#国产芯片`, `#IPO`, `#卫星导航芯片`, `#Fabless`

---

<a id="item-chip-news-7"></a>
### [BIS 新规限制 16 纳米以下流片，海外代工暂停国产芯片订单](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a1572f7d844cf92d2cb7d77ae34cc&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1107179063_121977860&amp;c=16257964767875466121&amp;mkt=en-us) ⭐️ 5.0/10

据搜狐一篇报道，美国商务部工业与安全局（BIS）新出台的芯片出口管制规则限制 16 纳米以下国产芯片流片，海外晶圆代工厂据此暂停承接相关订单，报道随后追问本土产能能否承接转回国内的需求。该报道称燧原科技、沐曦股份、摩尔线程、壁仞科技等国产算力芯片公司股价集体下跌，但未给出规则的具体条款、生效日期、涉及的海外代工厂名称，也未提供任何产能数字。因此，目前可确认的仅为报道所描述的管制方向与海外代工暂停现象；规则细节和实际影响尚未在源内容中得到证实。

rss · Bing News - China domestic chips · 11月27日 06:53

**「背景：新规与代工厂暂停的时间线」** 美商务部工业与安全局（BIS）于 2026 年 11 月 17 日至 18 日间公布一份临时最终规则，收紧先进 AI 芯片相关豁免，并提高对晶圆代工厂与封测厂的客户尽职调查（KYC）要求。据媒体报道，台积电与三星自 11 月 19 日起暂停向中国客户交付 16 纳米以下制程相关产品，两家公司均未发布全面停止的正式声明，三星方面还否认了“全面停工”的说法；该规则的 60 天公众评议期将于 2027 年 1 月 18 日截止。中国大陆市场分别约占台积电营收的 11%和三星对外代工量的 12%。

**「影响」** 若报道所述暂停确实持续，直接受影响的将是依赖海外代工完成 16 纳米以下流片的中国算力芯片设计公司，其先进制程样片与量产节奏可能被迫中断或转向国内代工厂。但源内容未提供代工厂产能、工艺验证周期或替代可行性数据，本土产能能否在短期内承接这些转回订单仍无法判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eastasiabrief.com/semiconductors/tsmc-samsung-freeze-sub-16nm-chip-shipments-chinese-clients-1577">TSMC and Samsung freeze sub-16nm chip shipments to Chinese ...</a></li>
<li><a href="https://casrai.org/news/tsmc-samsung-suspend-china-chip-shipments-bis-rule-2026">TSMC, Samsung Halt Some China Chip Shipments — CASRAI</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#国产芯片`, `#先进制程`, `#晶圆代工`, `#BIS新规`

---

<a id="item-chip-news-8"></a>
### [华为拟在 ISSCC 2027 披露定制 HBM 变通方案](https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/) ⭐️ 5.0/10

据 EE Times 报道，华为计划在明年年初于旧金山举行的 ISSCC 2027 上公布其定制高带宽内存（HBM）设计的细节，即以自研的“变通方案”应对 HBM 供应受限问题。该报道未披露这一方案的产品名称、堆叠层数、带宽、容量或所采用的制程，也未说明它是否已经流片或进入量产，因此目前只能将它视为一项拟公开的技术计划，不能等同于已经发布或得到验证的产品。在报道中，EE Times 没有说明华为将如何在无法获得海外 HBM 供应的情况下实现这一设计。

rss · EE Times · 11月27日 08:56

**「背景」** 此前已有公开信息显示，华为研究人员设计了一款数据引脚密度为三星和 SK 海力士量产产品两倍的 HBM 方案，该架构理论上可提供更高内存带宽（tool-1-1）。据 TheElec 披露的 ISSCC 2027 内存议程，华为将于 2 月 16 日（当地时间）在三星电子发布 HBM4E 研究成果之后，介绍其定制 HBM（tool-1-2）。本次报道仅确认华为将在 2027 年于旧金山举行的 ISSCC 上公布该定制 HBM 设计的细节，未给出产品名称、容量、带宽、制程节点或量产时间表。

**「影响」** 现有证据只支持一个有限的判断：华为把 HBM 的替代路径放到 ISSCC 这样的公开技术会议上讨论，说明相关自研工作已经推进到可以对外披露设计思路的阶段；但报道没有给出带宽、容量和量产时间，因此无法据此刻画它对国产 AI 算力供给的实际补充幅度。是否真正缓解 HBM 供应瓶颈，还要看华为在 ISSCC 2027 上公布的具体参数以及后续的流片、量产安排。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/innovation/huawei-hbm-design-data-pin-density">Huawei targets Samsung, SK Hynix with 2X denser memory chip design</a></li>
<li><a href="https://www.thelec.net/news/articleView.html?idxno=15909">Huawei , CXMT Challenge Samsung and SK hynix at ISSCC ...</a></li>

</ul>
</details>

**标签**: `#国产芯片`, `#HBM`, `#华为`, `#AI 算力`, `#先进制程`

---

<a id="item-chip-news-9"></a>
### [Big Technology 创办人：中国取得英伟达芯片的渠道正快速收窄](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a15720b4a40afaede776c77b9fe1c&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fchina-s-nvidia-chip-access-is-closing-fast-says-big-technology-s-alex-kantrowitz%2fvi-AA2in23A&amp;c=481846134368304326&amp;mkt=en-us) ⭐️ 4.0/10

Big Technology 创始人 Alex Kantrowitz 在 CNBC 的《Squawk on the Street》节目中评论了有关英伟达芯片在中国的最新报道，并讨论了近期整顿行动对半导体公司的意义。根据提供的节目摘要，他没有提出新的政策条款、生效日期、许可证决定、出货量或具体产品型号，因此这段内容只是对既有趋势的媒体评论，而不是新增的政策或产业事实。

rss · Bing News - China chip policy · 11月27日 09:34

**「背景」** 2026 年 11 月中旬，美国商务部发布临时最终规则，关闭中国经由新加坡等第三国远程访问先进 AI 芯片的通道，此前白宫介入推动了该规则。英伟达则在 11 月 17 日前后向客户发出法律风险提示，称一项新法律可能使客户和英伟达因中国获取芯片算力而面临“法律诉讼”，现行美国管制仍限制先进芯片的对华出货。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/video/2026/11/27/chinas-nvidia-chip-access-is-closing-fast-says-big-technologys-alex-kantrowitz.html">China&#x27;s Nvidia chip access is closing fast, says Big ... - CNBC Explainer-How China Got Access to Nvidia&#x27;s AI Chips Despite ... Nvidia warns chip buyers of legal risks tied to China access ... Commerce closes China’s backdoor to Nvidia chips ... - POLITICO China&#x27;s access to some Nvidia chips in doubt as curbs gain ... US Closes Loophole That Allowed China To Remotely Access ... US to curb China&#x27;s access to AI chips as Trump heads to Asia</a></li>
<li><a href="https://www.cnbc.com/2026/11/17/nvidia-china-cloud-ai-chip-access.html">Nvidia warns chip buyers of legal risks tied to China access ...</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`

---

<a id="item-chip-news-10"></a>
### [Penguin 复用退役 DDR4 内存供应 AI 服务器扩容](https://www.eetimes.com/penguin-revives-retired-ddr4-for-ai-servers/) ⭐️ 4.0/10

据 EE Times 报道，Penguin（企鹅解决方案）正在将退役的 DDR4 DRAM 重新用于 AI 服务器，以满足企业在内存扩容方面的需求。报道称，超大规模云服务商早已在回收旧 DRAM，而企业客户对 DDR4 再利用的推进相对较慢。该报道未披露具体产品名称、容量或出货数量、性能数据与生效时间，因此这目前只是一项被报道的做法，尚不能视为已发布产品或已量产的方案。

rss · EE Times · 11月27日 19:17

**「背景」** 在此次报道之前，Penguin Solutions 已与 Marvell 合作推出 CXL 转接方案，让企业把退役机器上的 DDR4 模组重新用作 AI 服务器的额外内存，相关计划的目标时间是 2026 年底。TechInsights 的数据显示，AI 数据中心在 2026 年占 DRAM 需求的 34%，预计到 2029 年接近 50%，这解释了退役 DDR4 复用需求的来源。当前报道进一步指出，超大规模云厂商早已在回收旧 DRAM，而企业客户的复用进度相对较慢。

**「影响」** 若更多企业跟进，直接效果是延长已停产 DDR4 的使用周期，为仍基于 DDR4 平台、又面临扩容压力的 AI 服务器提供一条不依赖新增 DDR4 供应的补充路径；但报道未说明复用内存的可靠性验证、兼容平台范围与可供货量，因此能缓解多少缺口目前无法量化。

<details><summary>参考链接</summary>
<ul>
<li>Marvell and Penguin Solutions reuse DDR4 for AI inference - Facebook</li>
<li>Penguin Solutions Introduces CXL-Enabled DDR4 Module to ...</li>

</ul>
</details>

**标签**: `#AI服务器`, `#DDR4`, `#内存供应`, `#AI算力`

---

<a id="item-chip-news-11"></a>
### [Beyond Lithography: The Battle for Semiconductor Manufacturing Yield](https://www.eetimes.com/beyond-lithography-the-battle-for-semiconductor-manufacturing-yield/) ⭐️ 4.0/10

EE Times commentary argues that the proposed MATCH Act exposes strategic vulnerabilities in semiconductor yield technologies extending beyond ASML lithography.

rss · EE Times · 11月27日 14:22

**标签**: `#对华出口管制`, `#先进制程`, `#晶圆产能`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [AI 写作判定权应归属谁](https://seangoedecke.com/who-gets-to-decide-if-something-is-written-by-ai/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月27日 00:00

**「背景」** 关于某段文字是否由 AI 生成的争论每天都在发生：文学奖获奖作品被指 AI 代写、作者因手稿被检测工具标红而失去合同、推文作者身份遭质疑。Pangram 被作者称为当前最好的 AI 检测工具之一，但许多反 AI 人士却对它抱有敌意。作者认为，真正的问题不在于检测是否准确，而在于谁有权力判定一段文字的作者身份。

**「方案」** 作者把反 AI 阵营的抵触解释为对权力的警惕：检测工具一旦成为仲裁者，掌握的就是把关文学奖、决定学生及格与否、把某些人排除出公共话语的权力。Pangram 在文化和政治上属于这些反 AI 人士本来就不信任的科技行业，因此请另一家科技公司来监督 AI 很难令人安心。作者也承认，对“工具化解决方案”的不信任有其合理性——过去几十年，社会从依赖社区判断转向由软件系统规定流程和考核绩效，很多人认为这正是问题所在。

但作者仍然支持使用 AI 检测，因为在他看来，唯一替代方案是社区自治：由奖项委员会调查裁定，或由社区舆论认定某段文字是否 AI 生成。他认为这很糟糕：不用 AI 的人往往不熟悉 AI 写作特征，在 Twitter 上，带有明显 AI 痕迹的文字会被不具备识别能力的人放过，而礼貌、篇幅较长的推文又会被误判为 AI。

因此，关心人类艺术和文化空间的人应当使用现有最强工具，哪怕它本身也是 AI；不信任科技公司互相监督的人，则应推动开源方案，或游说政府自建 AI 检测平台。作者还补充，读者来信指出另一个合理担忧：多数 AI 工具表现糟糕甚至不诚实，使人们害怕好工具也会产生误报。

**「启示」** 作者的核心论点是：AI 写作争议本质上是权力归属问题；把判定权交给不熟悉 AI 写作的社区，只会让更多 AI 生成内容流入人类的文化与公共空间，更可靠的做法是采用经过检验的检测工具，或建立开源、公共的检测能力。

**标签**: `#AI detection`, `#AI authorship`, `#institutional power`, `#community moderation`, `#technology governance`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [国常会提出强化“国家队”稳市与中央汇金类“平准基金”功能](https://www.tmtpost.com/nictation/8220182.html) ⭐️ 9.0/10

11 月 27 日国务院常务会议要求加力发挥“国家队”稳市作用，进一步优化中央汇金公司的类“平准基金”功能并提供充足流动性保障，同时推动上市公司加大分红回购。

telegram · zaihuapd · 11月27日 05:35

**「背景」** 就在三周前，2026 年 11 月 5 日公布的国务院金融工作报告已明确“支持中央汇金公司发挥类平准基金作用”，并提出拓宽中长期资金来源与入市渠道。中央汇金是国有金融资本投资平台，所谓“类平准基金”功能，指其在市场承压时通过增持宽基 ETF 等方式托底；2025 年 4 月外部关税冲击期间，汇金曾大额增持宽基 ETF，并配合央行再贷款应对市场压力。

**「影响」** 若相关举措落地，A 股投资者的稳市预期以及保险、企业年金、社保基金等中长期资金的入市条件可能受到影响，但会议未给出具体规模或时间表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20261106A06JSI00">国务院：支持中央汇金公司发挥类平准基金作用，巩固完善资本市场稳市...</a></li>
<li><a href="https://news.china.com/socialgd/10000169/20261106/49845810.html">中央汇金类平准基金功能再明确 稳市机制制度化升级</a></li>

</ul>
</details>

**标签**: `#China policy`, `#capital markets`, `#Central Huijin`, `#market stabilization`, `#long-term capital`

---

<a id="item-finance-news-2"></a>
### [央行下调大额存单起购门槛 个人降至 10 万元](https://www.news.cn/fortune/20261127/70789d77822242cc82216f51a416f872/c.html) ⭐️ 8.0/10

中国人民银行 11 月 27 日公布《大额存单管理办法》，将个人投资人认购起点由 20 万元下调至不低于 10 万元，机构投资人由 1000 万元下调至不低于 500 万元，自 2027 年 3 月 21 日起施行。

telegram · zaihuapd · 11月27日 11:36

**「背景」** 现行门槛来自 2015 年发布的《大额存单管理暂行办法》：个人认购起点为 20 万元，机构为 1000 万元；此次新规将两个门槛各下调一半，同时废止 2015 年办法和 2016 年第 13 号公告。

**「影响」** 起购门槛减半后，资金达到 10 万元以上的个人储户可参与大额存单；同日发布并同日施行的《人民币存贷款利率管理规定》要求金融机构自主确定存贷款利率、不得以高息揽储等不正当手段吸收存款，将约束银行的存款竞争方式。

**标签**: `#央行政策`, `#大额存单`, `#存款利率`, `#金融监管`, `#个人理财`

---

<a id="item-finance-news-3"></a>
### [蜜雪冰城 5 亿元入股 DeepSeek 新一轮融资](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

据报道，DeepSeek 已完成第二轮融资，规模约 1000 亿至 1055 亿元人民币，投后估值约 6155 亿元；蜜雪冰城股份有限公司通过天津砺思星深基金认缴 5 亿元。蜜雪集团 2025 年营收 335.6 亿元，归母净利润约 58.9 亿元。

telegram · zaihuapd · 11月27日 06:33

**「背景」** 据《The Information》报道，DeepSeek 今年 6 月已完成约 510 亿元人民币的首轮融资；此后第二轮融资目标多次调整，最初设为 500 亿元，随后上调至约 1000 亿元。

**「影响」** 若资金到位，DeepSeek 将获得大规模长期资本用于模型研发与算力投入；蜜雪冰城则以相当于其 2025 年归母净利润约 58.9 亿元中一部分的 5 亿元，将部分资金配置到 AI 领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/1/020/121.htm">曝 DeepSeek 第 二 轮 融 资 1055 亿 元： 估 值 6155 ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#financing round`, `#Mixue Bingcheng`, `#valuation`, `#private markets`

---

<a id="item-finance-news-4"></a>
### [市场监管总局集中约谈雅迪、台铃、爱玛等 15 家电动自行车企业](https://www.news.cn/20261127/0c8c665ce70c417b9263b39fa8a519f0/c.html?hl=zh-CN) ⭐️ 7.0/10

11 月 27 日，国家市场监管总局对雅迪、台铃、爱玛、九号、小牛等 15 家电动自行车企业进行集中约谈，原因是 CCC 认证全覆盖飞行检查发现部分企业质量保证能力欠缺、产品一致性管控不严，并违反强制性国家标准出厂销售不合格产品。约谈要求企业抓紧整改，严格执行“一车一池一充一码”规定，并对确认存在缺陷的产品立即召回。

telegram · zaihuapd · 11月27日 12:06

**「背景」** 此次约谈发生在新规落地后：市场监管总局今年升级了电动自行车 CCC 认证实施规则，新规自 2026 年 11 月 1 日起施行“一车一池一充一码”，即每辆车出厂时必须配备电池和充电器、加施整车追溯编码，并随车附带内容匹配的一致性证书。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E4%B8%80%E8%BD%A6%E4%B8%80%E6%B1%A0%E4%B8%80%E5%85%85%E4%B8%80%E7%A0%81/68048849">一车一池一充一码 - 百度百科</a></li>
<li><a href="https://www.thepaper.cn/newsDetail_forward_34401978">11月1日起，电动自行车新规实施：“一车一池一充一码”_澎湃号·政务_澎...</a></li>
<li><a href="https://www.sohu.com/a/1092094015_123024609">电动车3C认证新规11月1日实施：一车一池一充一码，一致性证书随车_电...</a></li>

</ul>
</details>

**标签**: `#China regulation`, `#Electric bicycles`, `#Product quality`, `#Consumer safety`, `#Corporate compliance`

---