---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 51 条内容中筛选出 22 条重要资讯。

---

**科技新闻**
1. [Google 拟让 AI 代理接入 Workspace MCP，Gmail 服务器不支持发信](#item-tech-news-1) ⭐️ 8.0/10
2. [三部门印发实施方案：2030 年建成新一代通信网，适时开展 6G 建设](#item-tech-news-2) ⭐️ 8.0/10
3. [Neuralink 获 FDA 批准启动渐冻症关键临床试验](#item-tech-news-3) ⭐️ 8.0/10
4. [英伟达叫停对东南亚四国 AI 服务器出货](#item-tech-news-4) ⭐️ 8.0/10
5. [智谱 GLM-5.5 与月之暗面 Kimi K4 或因反蒸馏与算力受限推迟](#item-tech-news-5) ⭐️ 8.0/10
6. [AI 编程代理让自托管重新变得有趣](#item-tech-news-6) ⭐️ 7.0/10
7. [AMD gfx906 专用 llama.cpp 社区分支](#item-tech-news-7) ⭐️ 7.0/10
8. [sqlite3\_rsync：无需整库复制的远程快照](#item-tech-news-8) ⭐️ 7.0/10
9. [华为拟公布新型 HBM 芯片，数据引脚密度号称翻倍](#item-tech-news-9) ⭐️ 7.0/10
10. [Cloudflare Workers 免费计划可向已验证地址发邮件](#item-tech-news-10) ⭐️ 7.0/10
11. [阿斯麦 CEO 反对全面断供中国光刻设备](#item-tech-news-11) ⭐️ 7.0/10
12. [Cloudflare 控制台与 API 故障持续约半小时](#item-tech-news-12) ⭐️ 7.0/10

**全球芯片**
1. [英伟达据报要求代工伙伴停运东南亚四国 AI 芯片](#item-chip-news-1) ⭐️ 7.0/10
2. [华为预告新一代 AI 高带宽内存芯片](#item-chip-news-2) ⭐️ 6.0/10
3. [中特微（成都）集中出货 7 台国产光刻机，带动科创芯片设计指数盘中上涨](#item-chip-news-3) ⭐️ 6.0/10
4. [报道称英伟达暂停对东南亚 AI 芯片出货](#item-chip-news-4) ⭐️ 5.0/10
5. [特朗普将访问台积电凤凰城先进芯片工厂](#item-chip-news-5) ⭐️ 5.0/10
6. [California companies owned by Chinese firms are scooping up Nvidia’s most advanced AI chips: report](#item-chip-news-6) ⭐️ 4.0/10
7. [国产 AI 芯片股大幅回调，海外代工受限下订单承接待解](#item-chip-news-7) ⭐️ 4.0/10

**科技博客**
1. [谁有权判定内容是否由 AI 撰写？](#item-tech-blog-1) ⭐️ 6.0/10

**财经新闻**
1. [中国双 11 智能手机销量同比下降 17%，苹果仍居第一](#item-finance-news-1) ⭐️ 7.0/10
2. [荷兰大臣称不接受美国限制 ASML 对华销售的法案](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Google 拟让 AI 代理接入 Workspace MCP，Gmail 服务器不支持发信](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) ⭐️ 8.0/10

据 TechStackUps 报道，Google 计划让 AI 代理通过 MCP 服务器接入 Workspace，其中 Gmail 服务器被限制为不能发送邮件。报道未给出实现细节，也未说明 Google 的具体理由，该计划目前仍属未经 Google 确认的报道。Hacker News 的讨论集中在两点：MCP 的 elicitation 机制本可让服务器暂停工具调用并要求用户确认，因此把发信功能设为仅限合作伙伴更像是商业决策而非安全考虑；限制也可能促使人们改让代理操作浏览器，反而更杂乱低效。

hackernews · ritzaco · 11月26日 09:44 · [社区讨论](https://news.ycombinator.com/item?id=50653477)

**「背景」** MCP（Model Context Protocol）是一种让 AI 代理以标准化方式连接外部工具和数据的协议。以 Gmail 为例，Google 官方文档称 Gmail MCP 服务器主要提供读取能力：搜索邮件、获取会话线程和列出标签。此前，围绕 Workspace/Gmail MCP 服务器的认证、权限范围以及个人 @gmail.com 账户是否可用，第三方已有相关梳理；这些内容为理解本次“Gmail 服务器不能发信”的争议提供了前提。

**「影响」** 如果 Gmail MCP 服务器确实不提供发信工具，依赖标准 MCP 接口的开发者就无法在代理工作流内完成邮件发送，只能改用浏览器自动化等变通方式，或等待被 Google 认可的合作伙伴渠道。

**「社区讨论」** 有评论者认为，用 MCP 的 elicitation 机制给发信工具加上人工确认即可，因此仅限合作伙伴更像是商业决策而非安全考量；也有人预测用户会转而让代理操作浏览器发信，结果是更杂乱、更浪费。另有评论者从雇主将 API 转向按量计费、封禁违反条款的客户端的经历出发，担心平台会以安全和条款为由收紧第三方访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://felipefontoura.com/articles/google-workspace-mcp/">Google Workspace MCP &amp; Gmail MCP Server : Auth, Scopes, Setup</a></li>
<li><a href="https://fluxmail.ai/blog/best-gmail-mcp-servers">The best Gmail MCP servers for Claude, ChatGPT and... | Fluxmail</a></li>
<li><a href="https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server">Configure the Gmail MCP server | Google for Developers</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI agents`, `#Google Workspace`, `#developer tools`, `#platform policy`

---

<a id="item-tech-news-2"></a>
### [三部门印发实施方案：2030 年建成新一代通信网，适时开展 6G 建设](https://www.news.cn/politics/20261126/9fe827a2d98741acb60f62d36ba89cf7/c.html) ⭐️ 8.0/10

China&\#x27;s industry, cyberspace, and development authorities issued a next-generation communications network implementation plan targeting a complete network by 2030, timely 6G buildout, low-orbit satellite internet, and scaled 5G-A and converged industrial/vehicle networks.

telegram · zaihuapd · 11月26日 06:30

**标签**: `#6G`, `#telecom policy`, `#satellite internet`, `#5G-A`, `#network infrastructure`

---

<a id="item-tech-news-3"></a>
### [Neuralink 获 FDA 批准启动渐冻症关键临床试验](https://www.bloomberg.com/news/articles/2026-11-25/neuralink-gets-clearance-for-brain-implant-trial-in-als-patients?srnd=phx-technology) ⭐️ 8.0/10

Neuralink 宣布，其名为 LINK 的植入式脑机接口已获美国 FDA 批准，将在美国启动面向渐冻症（ALS）患者的关键临床试验，目标是把大脑信号直接转化为计算机控制指令。该试验被描述为美国首个获批的此类关键试验，招募对象为渐冻症患者。Neuralink 表示，试验数据将作为未来申请医疗器械上市许可的核心依据；此前其早期研究已在全球为超过 30 名瘫痪患者植入设备。目前披露信息未包含试验设计、时间表与入组规模，且内容来自 Telegram 对 Bloomberg 报道的转述，尚无独立核实。

telegram · zaihuapd · 11月26日 07:15

**「背景」** Neuralink 由埃隆·马斯克与八名科学家和工程师共同创立，2016 年成立、2017 年 3 月首次公开，长期开发可植入式脑机接口。此次获批前，该公司已在早期研究中为全球超过 30 名瘫痪患者植入设备；据 Engadget 报道，FDA 此次授权以试验性方式作出，是 LINK 植入系统迈向关键试验的一步。

**「对患者与开发者的影响」** 对渐冻症患者而言，Neuralink 总裁 DJ Seo 表示 LINK 试验计划招募 20 名参与者，且招募已经开放。符合条件的重度瘫痪患者可关注入组机会，但该试验属研究性器械，其数据将用于未来上市申请，参与者承担的是研究风险而非已获批治疗。对开发者和研究者来说，这项美国首个植入式脑机接口关键试验的终点设计与数据公开情况，将成为后续同类产品的监管参照。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neuralink">Neuralink - Wikipedia</a></li>
<li><a href="https://www.engadget.com/2329008/neuralink-receives-fda-approval-for-brain-implant-trial-in-als-patients/">Neuralink Receives FDA Approval For &#x27;Pivotal&#x27; Brain Implant Trial In.....</a></li>
<li><a href="https://kz.kursiv.media/en/2026-11-26/engk-nknk-us-greenlights-neuralinks-pivotal-brain-implant-trial/">US greenlights Neuralink ’s pivotal brain implant trial</a></li>
<li><a href="https://casrai.org/news/neuralink-link-pivotal-trial-als-fda-clearance-2026">Neuralink LINK: First US Pivotal BCI Trial in ALS — CASRAI</a></li>
<li><a href="https://www.neurapod.com/blog/neuralink-fda-approval-link-pivotal-trial">Neuralink Gets FDA Approval for LINK, Its First Pivotal Trial</a></li>

</ul>
</details>

**标签**: `#脑机接口`, `#Neuralink`, `#FDA临床试验`, `#渐冻症`, `#神经技术`

---

<a id="item-tech-news-4"></a>
### [英伟达叫停对东南亚四国 AI 服务器出货](https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370) ⭐️ 8.0/10

英伟达已要求主要制造伙伴暂停向马来西亚、新加坡、泰国和印度尼西亚发运 AI 服务器，戴尔、美超微等将英伟达芯片组装成整机的厂商已通知四国买家相关订单无法出厂。三名知情人士称，冻结与美国新一轮出口管制相关，但尚不清楚是否为临时措施。美国商务部上周出台新规，要求区域云服务商在 90 天内取得出口许可，并核实客户不含受限的中国实体。上述消息来自《金融时报》的单一报道，英伟达与相关厂商尚未公开确认。

telegram · zaihuapd · 11月26日 07:38

**「背景」** 此前，美国已禁止英伟达最先进处理器直接出口中国大陆，马来西亚、新加坡、泰国和印度尼西亚因此成为中国 AI 公司获取这类芯片的中转地。据来源报道，美国商务部上周出台新规，要求区域云服务商在 90 天内取得出口许可，并核实客户不含受限的中国实体；此次暂停出货正是在这一新规之后发生。

**「影响」** 对马来西亚、新加坡、泰国和印度尼西亚的 AI 服务器买家而言，戴尔、美超微等组装商已通知相关订单无法出厂，交付因此中断。新规要求区域云服务商在 90 天内取得出口许可并核实客户不含受限的中国实体，这意味着依赖这些中转渠道采购英伟达先进芯片的数据中心项目需要重新规划合规采购路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dw.com/en/how-chinese-companies-circumvent-chips-sanctions-in-southeast-asia/a-80041002">US tries to restrict Chinese offshore computing capacity</a></li>
<li><a href="https://af.net/realtime/us-imposes-export-controls-on-advanced-ai-chips-to-5-nations-and-foreign-data-centers/">US Imposes Export Controls on Advanced AI Chips to 5 Nations and</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI infrastructure`, `#export controls`, `#supply chain`, `#Southeast Asia`

---

<a id="item-tech-news-5"></a>
### [智谱 GLM-5.5 与月之暗面 Kimi K4 或因反蒸馏与算力受限推迟](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/) ⭐️ 8.0/10

路透社报道，智谱原计划本月发布约 3 万亿参数的旗舰模型 GLM-5.5，但至今未推出；知情人士称发布时间可能推迟至 2027 年第一季度或更晚，原因之一是反蒸馏防护措施日趋有效。月之暗面内部预计，若完全失去海外算力，重大版本发布间隔将从 6 个月拉长到一年以上，下一代旗舰 Kimi K4 可能推迟至 2027 年年中，且 Anthropic 与 OpenAI 的反蒸馏措施令其获取训练数据更困难，已转向蒸馏谷歌和 Meta 的模型。报道同时提到，网传朋友圈截图显示智谱否认上述延期说法，相关计划仍存在不确定性。

telegram · zaihuapd · 11月26日 15:14

**「背景」** 路透社的报道提到，月之暗面此前于 2025 年 7 月发布 Kimi K2、2026 年 1 月发布 K2.5、同年 7 月发布 K3，此次被指可能推迟的 Kimi K4 是这一系列的下一个旗舰版本。报道还称，新的美国算力限制与反蒸馏防护共同压缩了中国实验室获取训练资源和算力的空间。

**「影响」** 对依赖这两家模型 API 或开源权重的开发者而言，旗舰版本若推迟到 2027 年，意味着短期内只能继续基于现有模型迭代，升级路线和选型评估需要相应调整；同时反蒸馏防护增强也表明，靠蒸馏前沿模型快速追赶的路径正变得更难走通。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/">EXCLUSIVE: US chip curbs, distillation crackdown threaten ...</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/artificial-intelligence/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-sources-say/articleshow/136182809.cms">distillation technique: US chip curbs, distillation crackdown ...</a></li>

</ul>
</details>

**标签**: `#Chinese AI labs`, `#model releases`, `#compute constraints`, `#anti-distillation`, `#AI industry`

---

<a id="item-tech-news-6"></a>
### [AI 编程代理让自托管重新变得有趣](https://janlukas.blog/posts/ai-self-hosting) ⭐️ 7.0/10

作者 jlelse 在一篇第一人称博客中称，AI 编程代理降低了自托管和小规模基础设施的实现门槛，让这类工作重新变得有趣。文中给出的具体例子包括：以自己的 Debian 为基础构建 bootc 镜像，使更新流程从“改版本号、调整 Docker Compose、推送 Git、SSH 登录服务器拉取并部署”缩短为一次 Git push；以及围绕 Git 驱动部署和基础设施自动化的实践。文章同时承认，这类提速主要来自作者的个人经验，并非经过独立测量的性能结果。

hackernews · jlelse · 11月26日 21:47 · [社区讨论](https://news.ycombinator.com/item?id=50660180)

**「背景」** 自托管长期面临的主要摩擦不在想法本身，而在实现与运维的琐碎工作：手动维护 Compose 文件、登录服务器拉代码、逐步部署。bootc 这类把系统本身作为容器镜像来管理的方案，与 Ansible 等自动化工具，原本就是为了减少这类重复操作；作者的观察是，AI 代理进一步压缩了从想法到可运行服务之间的实现成本。

**「实际影响」** 对自托管者而言，部署变快之后，责任重心会从“能否实现”转向“是否值得实现”和“能否持续打补丁”。评论者 jjcm 指出，代理可以端到端地拉起 VPS 并完成部署，但随之而来的是更紧的安全维护节奏：过去每几个月跑一次系统更新、配好 fail2ban 即可，如今被期待在严重 CVE 出现后 24 小时内完成修补。

**「社区讨论」** 评论者对这些变化看法不一。cliche 半开玩笑地表示自己缺乏克制力，已经把能想到的东西都“vibe”了一遍，甚至在 k3s 之上搭了个小平台，让代理通过 Tailscale 部署到家用服务器；也有评论强调，实现变容易后更应时常自问一个想法是否真的值得做。mrheosuper 则提出另一个实际疑问：人们到底在自托管什么，并以 Jellyfin 加 Arr 栈为例说明下载等待和持续照看仍然不便。

**标签**: `#self-hosting`, `#AI coding agents`, `#infrastructure automation`, `#DevOps`, `#security patching`

---

<a id="item-tech-news-7"></a>
### [AMD gfx906 专用 llama.cpp 社区分支](https://devnull.land/amd-specific-llama-cpp) ⭐️ 7.0/10

社区在 llama.cpp 基础上维护了一个专为 AMD gfx906 数据中心 GPU 优化的分支，目标是让无张量核心、无原生 bf16 支持的老卡也能高效运行本地推理。讨论者 rao-v 指出，这类 2018 年前后的 gfx906 卡拥有约 32GB 显存和最高约 1 TB/s 的 HBM2 带宽，二手价格约 200 美元，而当前接近这一带宽的新卡价格超过 3000 美元，因此形成了一个围绕 llama.cpp 优化的小型生态。该分支属于社区项目，报道未给出具体版本号、性能基准或正式发布状态。

hackernews · julianlam · 11月26日 17:11 · [社区讨论](https://news.ycombinator.com/item?id=50657265)

**「背景」** llama.cpp 是一个通用的本地大模型推理项目，通常以 CPU 和多厂商 GPU 后端运行量化模型。AMD 在 2018 年前后的 gfx906 数据中心卡（如 MI50/MI60 一代）缺少张量核心和原生 bf16 支持，但配备带宽很高的 HBM2 显存，因此社区出现了针对这一硬件特性修改推理内核的尝试。

**「实际影响」** 对使用 gfx906 等老 AMD 卡做本地推理的开发者来说，这类分支提供的量化与内核适配可能让低价高带宽显存变得可用，但用户需要自行验证数值正确性；评论中 fiddlerwoaroof 表示其针对 MI100 的改动通过与原内核对比做了数值校验，说明移植 Nvidia 内核到 ROCm 时校验是必要步骤。

**「社区讨论」** 有评论者认为 gfx906 的高带宽低价显存催生了专门的优化生态，并分享了自己的个人仓库；fiddlerwoaroof 称借助 Claude 激进优化 AMD 代码并把部分 Nvidia 内核移植到 ROCm 后，Qwen3.8 的性能提升到原来的两到三倍，且运行较为稳定。另有评论提到 R9700 上使用 radiance 引擎单卡预填充达 2400 tok/s、解码 150 tok/s，但这些属于个人报告而非独立基准。

**标签**: `#llama.cpp`, `#AMD GPU`, `#local inference`, `#gfx906`, `#quantization`

---

<a id="item-tech-news-8"></a>
### [sqlite3\_rsync：无需整库复制的远程快照](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 7.0/10

Simon Willison 介绍了 SQLite 自带工具 sqlite3\_rsync 的一项实用特性：它可以通过 SSH 连接把数据库快照复制到另一台机器，而无需先在本地创建整库副本。相比之下，使用 backup API 或 VACUUM INTO 生成快照时，都必须在本地创建一份完整副本，因此磁盘占用已超过一半的小型实例可能无法完成。该工具于 2024 年 10 月随 SQLite 3.47.0 以实验性状态加入，并在 2025 年 5 月的 SQLite 3.50.0 中得到增强；它也可用于同步已有的数据库副本，避免每次重传整个数据库，其协议由副本端发送页面或页面组的加密哈希，源端返回有差异的页面内容。

rss · Simon Willison · 11月26日 06:08

**「背景」** SQLite 从 3.47.0（2024 年 10 月）开始以“实验性”形式提供 sqlite3\_rsync 工具，并在 3.50.0（2025 年 5 月）对其做了增强。在此之前，常规快照方式只有备份 API 和 VACUUM INTO，两者都需要在本地完整复制一份数据库，因而受磁盘空间限制。

**「影响」** 对磁盘空间紧张的部署而言，sqlite3\_rsync 把制作快照备份的条件从“需要整库大小的本地空余空间”变为只需网络和 SSH 访问对端机器；在已有远程副本的场景中，哈希比对还能减少重复传输。需要注意的是，该工具在文中所述版本中仍标注为实验性，生产使用前应验证两端 SQLite 版本与协议兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sqlite.org/rsync.html">Database Remote-Copy Tool For SQLite</a></li>
<li><a href="https://til.simonwillison.net/sqlite/compile-sqlite3-rsync">Compiling and running sqlite 3 - rsync | Simon Willison’s TILs</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#databases`, `#rsync`, `#snapshotting`, `#backup`

---

<a id="item-tech-news-9"></a>
### [华为拟公布新型 HBM 芯片，数据引脚密度号称翻倍](https://www.bloomberg.com/news/articles/2026-11-26/huawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix) ⭐️ 7.0/10

华为计划公布一款新型高带宽内存（HBM）芯片的细节，其研究论文标题显示，该芯片的数据引脚密度是三星电子和 SK 海力士量产产品的两倍，理论上可显著提升内存带宽。论文定于明年 2 月在旧金山的一场会议上发表。目前这些信息来自论文标题层面的初步披露，尚未经独立验证，也不代表已实现量产。华为同时正推动 HBM 在中国本土投产，而该部件目前受美国制裁限制。

telegram · zaihuapd · 11月26日 05:30

**「背景」** HBM 通过堆叠 DRAM 裸片并提供超宽数据接口来提升带宽，因此数据引脚密度是决定单颗芯片带宽的关键指标之一。华为即将在旧金山会议（报道指为 ISSCC）上展示的论文标题声称其数据引脚密度达到三星与 SK 海力士量产产品的两倍，但该数值目前仅见于论文标题，尚无论文正文或实测数据支撑。

**「对国内 AI 芯片供应链的影响」** 若该论文所述的数据引脚密度翻倍能在实际产品中兑现，受影响最大的是依赖 HBM 的中国 AI 加速器设计商：在三星、SK 海力士供应受美国制裁限制的情况下，本地 HBM 产能成为其继续扩产的前提。现有进展显示，长鑫存储已于 2026 年 10 月开始向华为等国内厂商送样 HBM3，并计划在 2026 年第四季度末量产 HBM3E，但报道指出其良率不佳，且与 SK 海力士、三星、美光的差距仍以年计。因此，华为的论文属于尚未验证的设计声明，不能替代已送样的国产 HBM 供应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/huawei-poised-to-grow-chinas-ai-chip-market-next-generation-hbm-design-double-data-pin-density/">Huawei Poised To Grow China’s AI Chip Market With...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-26/huawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix">Huawei Teases Next-Gen AI Memory Chip to Take On... - Bloomberg</a></li>
<li><a href="https://www.notebookcheck.net/CXMT-to-mass-produce-HBM3E-memory-chips-in-late-Q4-2026-despite-abysmal-yields.1437211.0.html">CXMT to mass produce HBM 3E memory chips in late Q4 2026 despite...</a></li>
<li><a href="https://www.tomshardware.com/pc-components/dram/chinese-semiconductor-industry-gears-up-for-domestic-hbm3-production-by-the-end-of-2026-cxmt-to-produce-chips-while-naura-maxwell-and-u-preseason-design-tools-for-assembly">China moves to produce domestic HBM 3 | Tom&#x27;s Hardware</a></li>
<li><a href="https://neuroai.site/a/na-chips-domestic-hbm">China &#x27;s first homegrown HBM reaches customers · NeuroAI</a></li>

</ul>
</details>

**标签**: `#HBM`, `#Huawei`, `#semiconductor manufacturing`, `#AI hardware`, `#US sanctions`

---

<a id="item-tech-news-10"></a>
### [Cloudflare Workers 免费计划可向已验证地址发邮件](https://developers.cloudflare.com/changelog/post/2026-11-24-email-sending-workers-free/) ⭐️ 7.0/10

Cloudflare 宣布 Email Sending 已在 Workers Free 计划上线，开发者无需付费即可通过 Workers 绑定、REST API 或 SMTP 向账户中已验证的地址发送提醒、报告和通知。发送至已验证地址的邮件在所有计划中均免费，且不计入月度配额和每日发送限制。若要发送给任意收件人，仍需升级到 Workers Paid 计划。

telegram · zaihuapd · 11月26日 07:35

**「背景」** Cloudflare 的 Workers 平台此前将邮件发送能力与付费计划绑定，免费计划用户无法直接调用 Email Sending。此次变更把向账户已验证地址发信的能力下放到 Free 计划，但发往任意收件人仍需 Workers Paid，等于在免费层保留了一条仅限自测和内部通知的通道。

**「影响」** 对在免费计划上开发通知或报表功能的开发者来说，这提供了一条不占配额的测试与自用发送通道；但面向外部用户的邮件投递仍受付费计划限制，且免费计划下只能发往账户验证过的地址，使用前需先完成地址验证。

**标签**: `#Cloudflare Workers`, `#email sending`, `#serverless`, `#free tier`, `#developer platform`

---

<a id="item-tech-news-11"></a>
### [阿斯麦 CEO 反对全面断供中国光刻设备](https://www.semafor.com/article/11/25/2026/asml-makes-the-case-for-selling-chips-to-china) ⭐️ 7.0/10

阿斯麦 CEO 富凯（Christophe Fouquet）在 Semafor 的《Future Proof》节目采访中表示，出口管制应保护最先进的技术，但不应把中国完全排除在外，否则会促使中国在自研上“加倍甚至三倍投入”。他称阿斯麦卖给中国的设备落后最先进制程十多年，维持这一代差反而让中国继续依赖西方设备。他还表示，近 30 年来阿斯麦在中国光刻机市场的份额接近 100%。美国正推动 MATCH 法案，拟把管制范围从 EUV 扩大到浸没式 DUV 和维护服务，荷兰政府和阿斯麦均表示反对。

telegram · zaihuapd · 11月26日 12:19

**「背景」** 荷兰与美国此前已限制中国获取阿斯麦最先进的 EUV 系统及部分高端 DUV 设备，但阿斯麦仍可向中国销售较旧的 DUV 设备，并为已交付的机器提供维护。据 2026 年 8 月的报道，美国国会正在审议《硬件技术控制多边对齐法案》（MATCH Act），该法案拟要求盟友对齐美国的出口管制，把限制范围从 EUV 扩大到旧款 DUV 的销售，并涵盖中国境内已安装设备的安装、维护、备件、远程软件更新和技术支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thedefensenews.com/US-Pushes-Bill-to-Compel-Netherlands-to-Halt-Remaining-ASML-Machine-Sales-and-Service-to-China/">US Pushes Bill to Compel Netherlands to Halt Remaining ASML ...</a></li>
<li><a href="https://nltimes.nl/2026/08/20/us-preparing-force-netherlands-ban-asml-selling-china">U.S. preparing to force Netherlands to ban ASML from selling ...</a></li>
<li><a href="https://www.trendforce.com/news/2026/08/25/news-u-s-may-push-near-total-asml-china-ban-on-duv-sales-and-servicing-amid-chinas-domestic-lithography-push/">[News] U.S. May Push Near-Total ASML China Ban on DUV Sales ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#export controls`, `#ASML`, `#lithography`, `#US-China tech policy`

---

<a id="item-tech-news-12"></a>
### [Cloudflare 控制台与 API 故障持续约半小时](https://www.cloudflarestatus.com/incidents/xiqj67vl5pqm) ⭐️ 7.0/10

Cloudflare 于 11 月 26 日在状态页发布事故通告，称正在调查 Cloudflare Dashboard 及相关 API 的问题。通告表示，使用控制台和 API 的客户会受到影响，请求可能失败或页面显示错误提示。该故障在通告发布时已持续约半小时，现有信息未说明根本原因或预计恢复时间。

telegram · zaihuapd · 11月26日 16:33

**「背景」** Cloudflare 通过公开状态页按事故条目通报故障，客户可订阅或查看该页面获知进展，这是其披露服务中断的常规渠道。本次通告只说明正在调查 Dashboard 与相关 API 的问题，尚未给出根因、受影响范围或恢复时间。

**「影响」** 依赖控制台或 API 进行配置变更、查询状态和自动化运维的团队，在此期间可能遇到操作失败或页面报错，相关变更和自动化流程需要重试或延后处理。

**标签**: `#cloudflare`, `#outage`, `#api`, `#infrastructure`, `#service-status`

---

## 全球芯片

<a id="item-chip-news-1"></a>
### [英伟达据报要求代工伙伴停运东南亚四国 AI 芯片](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f47ff472cbf875865e3cf1439&amp;url=https%3a%2f%2fgizmodo.com%2fnvidia-reportedly-freezes-ai-chip-shipments-to-southeast-asian-countries-2000845928&amp;c=13759470686377298211&amp;mkt=en-us) ⭐️ 7.0/10

据 Gizmodo 报道，英伟达已告知其制造合作伙伴停止向印度尼西亚、马来西亚、新加坡和泰国运送其 AI 芯片。该报道未披露消息来源的具体身份，也未说明涉及的产品型号、出货数量或生效日期，英伟达方面尚无官方确认。若属实，这将是针对东南亚四国的供应链限制；但在获得确认前，只能视为未经证实的媒体报道，而非已生效的出口管制规则或官方禁运。

rss · Bing News - NVIDIA and China · 11月26日 07:24

**「背景」** 据《金融时报》率先报道，英伟达已通知戴尔、超微（Supermicro）等制造合作伙伴停止向马来西亚、新加坡、泰国和印度尼西亚发运搭载其芯片的服务器，福布斯与《卫报》等媒体在 11 月 26 日跟进报道。福布斯称，这一举动发生在美国出台新一轮出口限制约一周之后，暗示此次暂停与对华管制收紧相关，但相关报道均未披露涉及的具体产品型号、出货数量或生效期限。英伟达及上述四国政府尚未公开确认该指令，因此停运目前仍属媒体报道层面、未经证实的消息。

**「实际影响」** 若暂停供货属实，直接受冲击的是东南亚四国的数据中心与算力租赁业务：这些国家的数据中心运营商此前为无法直接采购或把先进英伟达芯片带入中国的中国企业提供远程算力接入，并因此吸引了大笔投资（据《纽约时报》报道，2026 年 11 月 17 日）。据 CNBC 同日报道，英伟达芯片买家被要求排除中国承租方，新规覆盖从芯片销售方到出租算力的 neocloud 的整条供应链。由于原始报道未点名消息来源，也未给出涉及的产品型号、出货规模与生效日期，目前尚无官方确认，暂停是否长期执行及适用范围仍待澄清。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/siladityaray/2026/11/26/nvidia-reportedly-halts-ai-chip-shipments-to-southeast-asia-as-us-tightens-china-curbs/">Nvidia Halts Server Shipments To 4 Southeast Asian Countries Amid...</a></li>
<li><a href="https://www.theguardian.com/business/live/2026/nov/26/nvidia-chip-shipments-south-east-asia-stock-dentists-live-updates">Nvidia reportedly halts chip shipments to south-east... | The Guardian</a></li>
<li><a href="https://nypost.com/2026/11/26/business/nvidia-halts-server-shipments-to-4-southeast-asian-countries-report/">Nvidia halts server shipments to 4 Southeast Asian countries: report</a></li>
<li><a href="https://www.nytimes.com/2026/11/17/business/southeast-asia-china-ai-chips.html">Trump’s New A . I . Chip Rules Rattle Southeast Asia - The New York...</a></li>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>
<li><a href="https://www.cnbc.com/2026/11/26/neoclouds-nvidia-china-ai.html">Nvidia chip buyers told to rule out Chinese renters to purchase GPUs</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#供应链`

---

<a id="item-chip-news-2"></a>
### [华为预告新一代 AI 高带宽内存芯片](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f8ef34052a1b7b305f9e93101&amp;url=https%3a%2f%2fwww.thestar.com.my%2ftech%2ftech-news%2f2026%2f11%2f27%2fhuawei-teases-next-gen-ai-memory-chip-to-take-on-samsung-hynix&amp;c=10675602340255321941&amp;mkt=en-us) ⭐️ 6.0/10

据媒体报道，华为正准备公布一款新的高带宽内存（HBM）芯片细节，并将其定位为对标三星电子和 SK 海力士的现有产品。该报道仅称该芯片&quot;有可能超越&quot;现有产品，未披露 HBM 代际、带宽或容量数值、制程节点、量产时间表，也未提供经第三方验证的性能数据，因此目前只能视为华为内存路线图的预告，而非已发布或已量产的里程碑。报道未说明该产品是否已进入客户送样，也未交代其与对华出口管制限制之间的关系。

rss · Bing News - China chip policy · 11月26日 12:00

**「背景」** HBM 是一种面向 AI 加速器的高带宽三维堆叠 DRAM 内存接口，最初由三星、AMD 与 SK 海力士联合开发。目前行业正从 HBM3 向扩展版本 HBM3e 过渡，三星与 SK 海力士在这一代际上展开竞争。华为此次仅预告将公布新款高带宽内存芯片，尚未给出所属代际、带宽、容量或量产时间，因此其与现有 HBM3e 产品的可比性暂时无法确认。

**「影响」** 若该预告后续落实为具体规格与量产安排，将意味着中国在 AI 加速器所需的关键内存环节上尝试以国产供应替代三星和 SK 海力士；但在代际、带宽、良率与交付时间均未披露前，尚无证据表明它能改变当前 HBM 供应链格局或缓解中国 AI 算力的内存瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.edn.com/a-sneak-peek-at-the-hbm-cold-war-between-samsung-and-sk-hynix/">A sneak peek at HBM cold war between Samsung and SK hynix - EDN</a></li>

</ul>
</details>

**标签**: `#国产芯片`, `#AI 算力`, `#华为`, `#高带宽内存`, `#对华出口管制`

---

<a id="item-chip-news-3"></a>
### [中特微（成都）集中出货 7 台国产光刻机，带动科创芯片设计指数盘中上涨](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb3005d941b1893fd8de40077a98&amp;url=https%3a%2f%2ffinance.eastmoney.com%2fa%2f202611273941506868.html&amp;c=16915117598286584113&amp;mkt=en-us) ⭐️ 6.0/10

据东方财富网 11 月 27 日报道，在成都双流区空港聚光光电产业园，中特微（成都）电子科技有限公司集中出货 7 台国产光刻机。消息带动下，截至当日 09:33，国联安\(588780\)科创芯片设计 ETF 所跟踪的上证科创板芯片设计主题指数\(950162\)上涨 1.37%，ETF 盘中换手率 0.33%、成交 236.28 万元；成分股杰华特上涨 8.66%，盛科通信上涨 5.49%，新相微上涨 4.47%，思瑞浦、裕太微等跟涨。报道未披露这 7 台光刻机的型号、可支撑制程节点、产能、客户及性能参数，也未说明其与此前交付记录或下游晶圆厂采购的关系。

rss · Bing News - China domestic chips · 11月26日 12:11

**「背景」** 光刻机是芯片制造中决定制程节点的核心设备，也是国内半导体设备国产化中起步较晚、难度较高的环节之一。此次集中出货发生在空港聚光光电产业园，涉及企业中特微（成都）电子科技有限公司；由于报道未介绍该公司的产品谱系与技术路线，无法确认这 7 台设备是否属于同一系列，或是否为此前已有交付的延续订单。

**「影响」** 若这 7 台确为可投入产线使用的整机而非样机或验证机，则意味着国产光刻装备在国内客户处完成了一次多台份集中交付，关系到国产设备在批量采购场景下的供应与交付能力；但由于缺少型号与制程信息，尚无法判断其适用的芯片类别与产线，对国产替代节奏的实际推动仍需后续披露佐证。报道中市场的直接反应集中在芯片设计类成分股与 ETF，而非设备类标的，指数上涨与此次设备出货之间的因果关系亦未经证实。

**标签**: `#国产芯片`, `#光刻机`, `#半导体设备`, `#科创芯片设计ETF`, `#国产替代`

---

<a id="item-chip-news-4"></a>
### [报道称英伟达暂停对东南亚 AI 芯片出货](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f47ff472cbf875865e3cf1439&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fnvidia-reportedly-halts-ai-chip-ship.%2520HelloWORLDts-to-southeast-asia-as-us-tightens-china-curbs%2far-AA2ih9aN&amp;c=7560169844318157466&amp;mkt=en-us) ⭐️ 5.0/10

据单一来源的报道称，英伟达（NVIDIA）已暂停向东南亚地区发运 AI 芯片，报道将此举与美方收紧对华出口管制联系在一起。该报道未提供涉事芯片型号、目的地国家、出货规模、生效时间或具体政策条款，因此暂停的范围与执行方式均无法核实。所附内容还称，黄仁勋在所谓婚外情及疑似中国间谍的丑闻后重新出任英伟达首席执行官，这一说法同样未获证实，且与芯片供应无关，不应视为已确认事实。

rss · Bing News - NVIDIA and China · 11月26日 03:17

**「背景」** 美方此前已多轮收紧对华 AI 芯片出口限制，使东南亚等地一度成为转口与算力部署的敏感环节，但本次报道没有说明它对应哪一项具体规则或此前哪一次执法行动。由于缺乏可核对的型号、时间与政策依据，目前无法判断此次报道的出货暂停是新政策所致，还是企业出于合规审查的自主调整。

**「影响」** 若报道属实，直接影响将是东南亚客户获取英伟达 AI 芯片的交付周期被延长，并可能波及经由该地区进行的算力部署与转口路径；但在芯片型号、受限国家和生效时间明确之前，无法量化对英伟达营收或区域 AI 算力供给的具体影响。

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#东南亚出货`

---

<a id="item-chip-news-5"></a>
### [特朗普将访问台积电凤凰城先进芯片工厂](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f8ef34052a1b7b305f9e93101&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2ftrump-to-visit-maker-of-semiconductor-chips-including-nvidias%2far-AA2ijwJN&amp;c=5887081375257091898&amp;mkt=en-us) ⭐️ 5.0/10

据必应新闻聚合的“中国芯片政策”相关内容报道，美国总统特朗普计划访问台积电位于亚利桑那州凤凰城的工厂。报道称该厂是先进制程芯片的主要制造基地之一，代工产品包括英伟达的芯片。报道未给出访问的具体日期、随行人员，也未说明此行是否会伴随新的出口管制措施、投资承诺或产能安排，因此目前可确认的只是一项访问计划，而非已宣布的政策变化或新增产能。

rss · Bing News - China chip policy · 11月26日 17:21

**「背景」** 台积电在亚利桑那州凤凰城的园区此前已投产先进制程，并为包括英伟达在内的客户代工芯片。KJZZ 援引白宫官员的话报道，特朗普预计将出席该园区一座新厂房的动工仪式；《Independent》进一步称，动工仪式定于 12 月 4 日，白宫和台积电均已确认该安排。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kjzz.org/politics/2026-11-25/trump-is-expected-to-visit-tsmcs-phoenix-campus-where-they-make-nvidia-chips">Trump is expected to visit TSMC&#x27;s Phoenix campus, where they ...</a></li>
<li><a href="https://www.independent.co.uk/news/world/americas/us-politics/trump-tsmc-arizona-chip-foundry-b3092143.html">Donald Trump to celebrate new Arizona chip foundry right ...</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#晶圆产能`, `#先进制程`, `#中美芯片合作`

---

<a id="item-chip-news-6"></a>
### [California companies owned by Chinese firms are scooping up Nvidia’s most advanced AI chips: report](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb2f47ff472cbf875865e3cf1439&amp;url=https%3a%2f%2fnypost.com%2f2026%2f11%2f26%2fus-news%2fchinese-owned-california-companies-buying-up-advanced-nvidia-ai-chips-report%2f&amp;c=10062808716971268677&amp;mkt=en-us) ⭐️ 4.0/10

A short report claims Chinese-owned California companies are acquiring Nvidia&\#x27;s most advanced AI chips, but offers only anonymous, unspecified details and no verifiable figures.

rss · Bing News - NVIDIA and China · 11月26日 12:41

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-7"></a>
### [国产 AI 芯片股大幅回调，海外代工受限下订单承接待解](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b08eb3005d941b1893fd8de40077a98&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261127A069NA00&amp;c=9450142772382014334&amp;mkt=en-us) ⭐️ 4.0/10

11 月 19 日，燧原科技（688801.SH）股价大跌 20%，沐曦股份（688802.SH）下跌 14.72%，摩尔线程（688795.SH）下跌 8.34%；11 月 25 日，港股壁仞科技（06082.HK）下跌 24.71%，天数智芯（09903.HK）下跌 18.51%。燧原科技、天数智芯等公司先后回应称生产经营正常，但相关个股跌势并未止住。报道提出在海外晶圆代工受限背景下由谁承接国产芯片转回订单的问题，但可见内容未给出代工限制的具体条款、订单转移规模或承接产能等细节。

rss · Bing News - China domestic chips · 11月26日 12:10

**「背景」** 就在本轮股价大跌期间，壁仞科技于 11 月 25 日回应称，其新一代旗舰产品 BR20X 已向头部客户送测，实测性能达到 H200 水平（tool-1-1），但这属于厂商自述的送测结果，并非第三方实测。供给端方面，中芯国际与华虹宏力在 2026 年二季度业绩齐增，国产晶圆代工正随行业景气加速扩产（tool-2-1）；中芯国际在 2026 年一季度业绩说明会上称，当季出货量环比下降 0.2%，晶圆平均销售单价环比提升 2.5%（tool-2-3），显示成熟产能趋紧、价格上行。

**「影响」** 股价下跌与公司“经营正常”的回应同时出现，表明市场对国产 AI 算力芯片供给路径的担忧尚未因公司表态而消除；但该报道未披露海外代工受限的具体范围与生效时间，也未说明订单转回后的承接方与产能安排，因此对实际出货和国内替代节奏的影响暂无法从这一来源确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.mydrivers.com/1/1168/1168651.htm">一天 跌 去近四分之一！ 壁 仞 科 技 称新旗舰实测已达H200水平</a></li>
<li><a href="https://wap.eastmoney.com/a/202608133840755654.html">wap.eastmoney.com/a/202608133840755654.html</a></li>
<li><a href="https://news.10jqka.com.cn/20260521/c676848970.shtml">AI 虹 吸成熟 产 能 国 产 晶圆 代 工 开启提价扩 产 周期 | 同花顺财经</a></li>

</ul>
</details>

**标签**: `#国产芯片`, `#AI 算力`, `#对华出口管制`, `#晶圆代工`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [谁有权判定内容是否由 AI 撰写？](https://seangoedecke.com/who-gets-to-decide-if-something-is-written-by-ai/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月27日 00:00

**「背景」** 关于某篇作品是否由 AI 生成的争论几乎每天出现：写作奖获奖故事被指 AI 生成、作者因手稿被 Pangram 检测出高 AI 概率而失去合同、推文作者身份引发争议。作者 Sean Goedecke 指出，围绕 Pangram 等 AI 检测工具的可靠性或伦理的讨论，其实都位于一个更根本的冲突之下：谁有权力裁定“这是 AI 写的”，以及由此衍生出的把关文学奖、判定学生及格与否、排除他人于公共话语之外的权力。

**「方案」** 作者认为，反 AI 人士对检测工具的敌意是理性的，因为这场争议本质上是权力问题：Pangram 在文化与政治上隶属于他们所不信任的同一科技行业，让另一家科技公司充当看门人并不能带来多少安心。他进一步指出，过去几十年社会从社区式、可通融的人类流程转向可计算的工具化流程，许多反 AI 者正是将这一转变视为灾难，因此用又一款 AI 工具来治理 AI 显得荒谬。但作者仍支持 Pangram 类工具，因为在他看来，替代方案只有社区自我 policing：由奖项委员会调查或社区共识来裁定作品是否由 AI 所写。他认为这很糟糕——不用 AI 的人并不擅长识别 AI 文本，在 Twitter 上，带有明显 AI 痕迹的文字常被未读过足够多 AI 内容的人误判，而冗长礼貌的人类推文又常被当成 AI。他主张，若真想阻止 AI 进入艺术与文化领域，就应使用最强工具，包括 AI 检测器；若担心科技公司互相监督，则应推动开源方案或由政府自建检测平台。否则，把“是否 AI 所写”交给社区，只会让更多 AI 生成的故事、文章和诗歌进入公共空间。

**「启示」** 作者的核心论点是：AI 作者身份之争实质上是制度权力之争，而相比不可靠的社区自我 policing，AI 检测工具——尤其是开源或公共机构运营的版本——是更可取的裁决机制。

**标签**: `#AI detection`, `#AI authorship`, `#power and institutions`, `#community moderation`, `#technology criticism`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国双 11 智能手机销量同比下降 17%，苹果仍居第一](https://counterpointresearch.com/en/insights/china-double-11-smartphone-sales-drop-17-percent-on-weak-demand) ⭐️ 7.0/10

Counterpoint Research 数据显示，2026 年双 11 促销期（10 月 12 日至 11 月 13 日）中国智能手机销量同比下降 17%。苹果销量下降 8%但仍居第一，华为是唯一实现增长的主要厂商，销量同比增长 29%。

telegram · zaihuapd · 11月26日 09:38

**「背景」** 品牌折扣、优惠券和以旧换新补贴未能抵消组件成本上涨导致的涨价影响；81%计划半年内购机的中国消费者注意到涨价，更倾向推迟换机而非接受更高价格。

**「影响」** 涨价抑制了促销期的换机需求，计划近期购机的消费者可能继续推迟购买，从而延后手机厂商的销售回暖。

**标签**: `#China smartphone market`, `#Double 11 sales`, `#Apple`, `#Huawei`, `#consumer demand`

---

<a id="item-finance-news-2"></a>
### [荷兰大臣称不接受美国限制 ASML 对华销售的法案](https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml) ⭐️ 7.0/10

荷兰外贸与发展合作大臣 Sjoerd Sjoerdsma 于 11 月 26 日在议会表示，荷兰不会接受美国进一步限制 ASML 对华销售，并反对 MATCH Act 的域外管辖效力。荷兰正与欧盟委员会协调，联合德国、法国游说，争取把该法案从美国年度国防政策法案中剔除，外界预计国会 12 月中旬表决。

telegram · zaihuapd · 11月26日 14:56

**「背景」** MATCH Act 于 2026 年 4 月由美国两党议员提出，要求荷兰、日本等盟友对华实施更严格的半导体设备出口管制，否则美方将单方面限制其设备出口；此前美荷两国已禁止 ASML 向中国出售最先进的 EUV 光刻机。

**「影响」** 若美方按现行法案文本推进，ASML 对华设备销售将直接受限；中国目前约占其销售额的 20%，而这一占比已从 2024 年的约 41%降至 2025 年的约 33%，显示出口管制已在压缩其中国业务（据外部资料，非本文来源）。荷兰联合德国、法国和欧盟委员会游说，表明受影响的不仅是 ASML，还包括依赖对华设备出口的欧洲半导体设备供应链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fool.com/investing/2026/04/24/the-match-act-could-blow-a-hole-in-asmls-revenue-h/">The MATCH Act Could Blow a Hole in ASML &#x27;s Revenue. Here&#x27;s What...</a></li>
<li><a href="https://keepingupwith.ai/articles/netherlands-opposes-match-act-at-risk-to-asmls-china-business/">Netherlands Opposes MATCH Act at Risk to ASML &#x27;s China Business</a></li>
<li><a href="https://www.faf.ae/home/2026/7/6/the-silicon-chokepoint-asml-china-and-the-geopolitics-of-the-worlds-most-important-machine">The Silicon Chokepoint: ASML , China , and the Geopolitics of the...</a></li>
<li><a href="https://www.techi.com/asml-china-euv-export-scrutiny-stock/">Washington Thinks China Has ASML &#x27;s Best Machine. ASML Says...</a></li>

</ul>
</details>

**标签**: `#semiconductor export controls`, `#ASML`, `#Netherlands`, `#US legislation`, `#MATCH Act`

---