---
layout: default
title: "Horizon Summary: 2026-11-02 (ZH)"
date: 2026-11-02
lang: zh
---

> 从 37 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [vLLM v0.33.0rc3 发布：升级 PyTorch 2.14 并停发 CUDA 12.9 产物](#item-tech-news-1) ⭐️ 7.0/10
2. [Kingsbury：LLM 让软件成熟度信号更易伪造](#item-tech-news-2) ⭐️ 7.0/10
3. [SemiAnalysis：2027 数据中心已开工，2028 管线受选举与许可牵制](#item-tech-news-3) ⭐️ 7.0/10
4. [LongCat-2.5 发布：1.6 万亿参数原生多模态模型](#item-tech-news-4) ⭐️ 7.0/10
5. [ChatGPT 分享链接漏洞可致会话内代码执行](#item-tech-news-5) ⭐️ 7.0/10
6. [WIRED：400 多个 AI 应用被指暗藏色情深伪](#item-tech-news-6) ⭐️ 7.0/10

**科技博客**
1. [为何 LLM 对齐在原则上不可能](#item-tech-blog-1) ⭐️ 7.0/10

**财经新闻**
1. [Anthropic 前三季度营收 332 亿美元，净亏损 1040 亿美元](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.33.0rc3 发布：升级 PyTorch 2.14 并停发 CUDA 12.9 产物](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 7.0/10

vLLM 发布 v0.33.0rc3 候选版本，包含 927 次提交、389 名贡献者，并新增 Reflection Beam-1.0、Yandex AliceAI-Foundation-80B-A3B 等模型支持。运行环境升级到 PyTorch 2.14.0，配套 torchvision 0.29.0 和 Triton 3.8.0；CUDA wheel 现已与 libtorch ABI 稳定。该版本不再发布 CUDA 12.9 的 wheel 和 -cu129 镜像，默认产物仅为 CUDA 13.0；同时新增带 AWS EFA 库的 vllm/vllm-openai:v0.33.0-efa 镜像，并将每个发布镜像同时以更短的 vllm/vllm 名称发布。破坏性变更包括移除 Medusa 和 MLP speculator、移除旧版 Ray compiled-graph executor，以及 NIXL connector 要求 NIXL 1.5 或更高版本。

github · khluu · 11月2日 10:10

**「背景」** vLLM 是面向大语言模型推理与在线服务的开源引擎，通常以绑定特定 PyTorch 和 CUDA 版本的 Python wheel 与 Docker 镜像分发。其运行时和计算内核依赖构建时所用的 CUDA 版本，因此升级 PyTorch 或切换 CUDA 主版本会直接影响现有部署应使用的镜像标签和驱动环境。

**「影响」** 仍在使用 CUDA 12.9 的部署需要迁移到 CUDA 13.0 或继续停留在旧版本，因为 v0.33.0 起不再提供 -cu129 产物；依赖 Medusa、MLP speculator 或旧 Ray compiled-graph executor 的配置也必须调整，NIXL 用户需至少升级到 1.5。

**标签**: `#vllm`, `#llm-inference`, `#release`, `#pytorch`, `#cuda`

---

<a id="item-tech-news-2"></a>
### [Kingsbury：LLM 让软件成熟度信号更易伪造](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 7.0/10

Simon Willison 摘录了 Kyle Kingsbury 在 Jepsen 对 ParticleDB 1.1.4 分析中的评论：LLM 的使用正在侵蚀人们对文档、软件以及产出这些软件的组织所抱有的信任。Kingsbury 认为，过去被视为成熟系统标志的信号如今更容易被伪造，工程师可能因此对任何新软件项目都更加怀疑。他还追问，在 LLM 时代，维护者应如何确保软件与文档正确，以及如何向用户证明其质量。

rss · Simon Willison · 11月1日 16:49

**「背景」** Jepsen 是 Kyle Kingsbury 维护的故障注入测试工具，其发布的数据库分析以检验事务隔离与一致性保证著称。这段引文出自他对 ParticleDB 1.1.4 的分析报告：该报告称测试覆盖 1.1.4 至 1.1.18.11.rc-22 等版本，在 Debian 13 单节点、容器和 EC2 虚拟机上运行；Hacker News 上的讨论引述报告称，这个宣称兼容 PostgreSQL 的数据库在事务行为上出现了严重异常。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen : ParticleDB 1 . 1 . 4</a></li>
<li><a href="https://news.ycombinator.com/item?id=50316100">Jepsen : ParticleDB 1 . 1 . 4 | Hacker News</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#software trust`, `#documentation`, `#Jepsen`, `#AI risk`

---

<a id="item-tech-news-3"></a>
### [SemiAnalysis：2027 数据中心已开工，2028 管线受选举与许可牵制](https://newsletter.semianalysis.com/p/the-datacenter-backlash-goes-bipartisan) ⭐️ 7.0/10

SemiAnalysis 在 11 月 1 日的分析中判断，2027 年美国前 20 州的 33.8 GW 数据中心容量中约四分之三已进入施工，因此选举不会改变其此前给出的全球 +50 GW 年度预期；真正暴露于政治风险的是 2028 年：其模型预计美国净新增 62.2 GW，其中大部分尚未开工。该分析聚焦 2028 年净新增最大的 13 个州，合计 43.5 GW、占全美预测的 70%，其中 10 个州将在 11 月 3 日选举州长。文章称自 9 月以来风险上升：得州 9 月 21 日冻结 TCEQ 许可，俄勒冈 10 月 9 日将土地冻结扩大到空气和水排放许可（至 2027 年 7 月 1 日），且 20 名州长候选人中 9 人主张暂停新建、11 人主张附加条件。

rss · Semianalysis · 11月1日 18:40

**「背景」** 德州此前已收紧数据中心审批：州长 Abbott 指示 TCEQ 在 ERCOT 完成并网队列审计前停止处理相关许可，把供电接入也纳入冻结范围。SemiAnalysis 9 月曾判断，地方禁令对全美建设进度影响有限；现在的问题变成德州许可冻结会持续多久，因为德州占其 2028 年美国新增容量预测近 30%。

**「对开发商的影响」** 对在得州及上述 13 州推进 2028 年项目的开发商而言，最直接的风险是审批时间表：得州约占 2028 年美国新增 GW 的 30%，而 ERCOT 目标 12 月 10 日提交审计报告并不自动恢复 TCEQ 发证。若许可冻结延续到 2027 年立法会期，相关项目可能比 12 月重启审批多损失 5 至 9 个月。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.breitbart.com/tech/2026/10/16/texas-ag-ken-paxton-sends-compliance-letters-to-156-data-centers-over-water-usage-reporting/">Texas AG Ken Paxton Sends Compliance Letters to 156 Data Centers ...</a></li>
<li><a href="https://www.linkedin.com/pulse/draw-power-data-centres-race-build-them-sunday-27-2026-thompson--5wxse">THE DRAW - Power, data centres and the race to build them - Sunday...</a></li>

</ul>
</details>

**标签**: `#AI datacenters`, `#infrastructure capacity`, `#US policy`, `#power constraints`, `#capacity forecasting`

---

<a id="item-tech-news-4"></a>
### [LongCat-2.5 发布：1.6 万亿参数原生多模态模型](https://longcat.ai/blog/longcat-2.5/) ⭐️ 7.0/10

LongCat 团队发布 LongCat-2.5，一个面向长程 agent 任务的原生多模态模型，总参数 1.6 万亿、每 token 激活约 480 亿，是在 LongCat-2.0 基础上强化视觉理解与 agentic coding（智能体编程）的版本。模型把视觉信号编码为多级离散 token 并与文本统一处理，官方称可完成视觉编程等任务。目前官网已开放试用并提供 API 接入，但 GitHub 与 HuggingFace 上的权重尚未开放。该消息来自单条 Telegram 投稿，未附基准测试数据或第三方评测，上述能力与参数规模均属厂商说法，尚无法独立验证。

telegram · zaihuapd · 11月2日 03:08

**「背景」** LongCat-2.5 的前代是 LongCat-2.0，本次发布将视觉理解与 agentic coding 列为相对前代的重点改进。这里的“原生多模态”指模型把视觉信号编码为多级离散 token，并与文本统一处理，这也是它能完成视觉编程任务的前提。发布信息将 1.6 万亿总参数与约 480 亿的每 token 激活量分开列出，表明模型采用稀疏激活架构，推理时并非全部参数都参与每个 token 的计算。

**「对开发者的直接影响」** 需要长程 agent 或视觉编程能力的开发者现在只能通过官网试用或 API 接入 LongCat-2.5，无法自行部署或微调：GitHub 与 HuggingFace 上的权重尚未开放。因此在评估该模型时，应把调用成本、数据是否需出本地以及后续权重开放时间纳入方案，而不宜按可自托管的前提做架构设计。

**标签**: `#LongCat-2.5`, `#multimodal models`, `#agentic coding`, `#model release`

---

<a id="item-tech-news-5"></a>
### [ChatGPT 分享链接漏洞可致会话内代码执行](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 7.0/10

Parameter 研究团队披露，恶意 ChatGPT 分享链接可在已登录用户的会话中执行代码，读取私密对话并把数据发送到外部服务器，受害者只需打开链接，无需安装任何应用。该漏洞源于预览功能与图表组件之间的消息处理缺陷。OpenAI 已于 10 月 26 日完成修复，将其定为 P1 级问题，并向研究团队支付 5000 美元赏金。

telegram · zaihuapd · 11月2日 10:24

**「背景」** 该漏洞出在 ChatGPT 分享链接的渲染链路上：分享的对话会经过预览功能与图表组件处理，Parameter 指出问题正出在这两者之间的消息处理环节。据 The Hacker News 报道，研究团队于 10 月 18 日通过 OpenAI 的漏洞赏金计划提交报告；OpenAI 随后在服务端完成修复，并在 8 天后处置完毕，将其定级为 P1、支付 5000 美元赏金。

**「实际影响」** 对 ChatGPT 用户而言，风险集中在“打开他人分享的链接”这一动作本身：在修复前，接收方无需授予额外权限，就可能在自己的登录会话中触发代码执行，并泄露私密对话。修复已上线，普通用户无需采取额外操作，但应继续谨慎对待来源不明的分享链接；企业在评估 AI 工具时，也应把分享与预览渲染路径视为需要重点审查的攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/openai-patches-chatgpt-share-link-flaw-that-hijacked-sessions">OpenAI Patches ChatGPT Share - Link Flaw That Hijacked Sessions</a></li>
<li><a href="https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html">A Shared ChatGPT Link Could Run Attacker Code in Your Session ...</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#security vulnerability`, `#account takeover`, `#OpenAI`, `#AI security`

---

<a id="item-tech-news-6"></a>
### [WIRED：400 多个 AI 应用被指暗藏色情深伪](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 7.0/10

WIRED 11 月 2 日发布的调查称，一个由 400 多个关联应用和网站组成的网络以宠物画像、语言学习等普通 AI 工具为掩护，在特定条件下加载色情深伪界面，允许用户上传他人照片生成露骨图像或视频。报道称，9 月仍在 Google Play 上架的 27 款相关应用累计下载超过 35 万次，许多被标为适合所有年龄。苹果在收到 WIRED 提供的线索后下架了 19 款应用，称开发者是在审核通过后替换远端网页内容；谷歌在 WIRED 联系前已移除其中多数应用，Meta 则表示已阻止相关 209 款应用投放广告。报道将这一网络与中文开发者及一家香港注册公司联系起来，但明确这属于媒体和研究人员的调查判断，相关运营方未回应置评请求。

telegram · zaihuapd · 11月2日 12:45

**「背景」** 色情深伪通常指利用生成式模型，把真实人物照片合成到露骨图像或视频中，这类内容也正是各大应用商店审核政策重点限制的对象。正因如此，报道中的网络被指先用宠物画像、语言学习等普通 AI 工具通过审核，再通过远端网页替换或特定条件触发，向用户呈现隐藏的深伪功能。

**「影响」** 对应用商店审核而言，直接后果是上架时通过审核并不等于后续内容安全：苹果称涉事开发者是在审核通过后替换远端网页内容，这表明仅依赖首次审核无法覆盖应用后续加载的界面。

**标签**: `#AI safety`, `#deepfakes`, `#app store moderation`, `#privacy`, `#investigative journalism`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [为何 LLM 对齐在原则上不可能](https://seangoedecke.com/alignment-is-impossible/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月2日 00:00

**「背景」** 强大 AI 的不可预测性让“对齐”成为核心安全问题：传统设想把 AI 视为追求固定目标的盲目优化器，因此对齐就是正确指定目标。作者认为，现代 LLM 并非这种优化器，而更像由模仿人类文本训练出的、会随输入切换的庞大人格混合体，因而没有可被形式化的固定目标。

**「方案」** 既然无法通过指定目标来约束 LLM，就只能退而求其次：充分理解模型，确信它不会做出危险行为。作者主张，这种理解本身在原则上不可得。仅仅追溯权重和计算只能说明“如何发生”，不能给出对齐所需的“动机”层面的解释；而要求完整理解动机，就像要求彻底读懂一个人以确保其永远按你的利益行事一样不现实。作者进一步指出，机制可解释性即便完全成功也无法提供保证：特征必须先诱发出行为才能被标注，而最令人担忧的突发有害行为恰恰未被观察到；标注只是猜测，某个“善良”特征可能实际是“除非到了 2030 年才善良”，类似克里普克“四则运算/四倍运算”的不可区分问题；而且每个 token 背后特征组合的意义过于复杂，人类无法逐项判断“邪恶”特征究竟是在回避、制造还是担忧邪恶。若让另一个模型来检查，又会陷入由第三个模型检查的无限回退。作者也承认，机制可解释性对减少奖励黑客、提升常规表现仍有价值，思维链监控、沙箱和人工介入等缓解措施也有条件地有用，但不足以控制超级智能。

**「启示」** 作者的结论是：LLM 对齐不仅困难，而且概念上不连贯——我们甚至说不清“确信模型已对齐”究竟意味着什么。机制可解释性可以服务普通训练目标，却无法提供防止智能体失控所需的那种动机级理解。

**标签**: `#AI alignment`, `#mechanistic interpretability`, `#AI safety`, `#LLM behavior`, `#philosophy of mind`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Anthropic 前三季度营收 332 亿美元，净亏损 1040 亿美元](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) ⭐️ 7.0/10

Anthropic 在 11 月 2 日周一更新的 IPO 招股书中披露，截至 2026 年 9 月 30 日的前三季度营收为 332.4 亿美元，同比增长约 1200%；同期净亏损为 1040 亿美元，远高于去年同期的 251 亿美元。公司称，上半年亏损主要来自可转换债券及衍生负债的公允价值变动，并不完全代表实际的经营现金消耗；此外，公司累计采购及租赁承诺约 8954 亿美元，几乎全部用于算力和基础设施。

telegram · zaihuapd · 11月2日 15:12

**「背景」** Anthropic 此前披露的招股书显示，2026 年上半年营收为 162.9 亿美元、净亏损为 420 亿美元，其中约 340 亿美元来自可转换为公司股份的融资工具估值等会计处理；公司称这类公允价值变动并不完全等同于实际经营现金消耗。\[tool-1-1\]\[tool-1-2\]

**「影响」** 这些以算力为主的采购与租赁承诺，意味着 Anthropic 未来数年将向芯片和云基础设施供应商支付巨额款项；相关报道还称，博通将提供最高 420 亿美元可转换票据融资，覆盖其 1252 亿美元五年 TPU 租赁承诺的约三分之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fxstreet.com/news/anthropic-ipo-filing-reveals-rapid-growth-as-investors-weigh-an-80-billion-loss-202610270748">Anthropic IPO filing reveals rapid growth as investors weigh an $80...</a></li>
<li><a href="https://www.hokanews.com/2026/09/anthropic-ipo-filing-shows-42-billion.html">Anthropic IPO Filing Shows $42 Billion Net Loss in... - Hokanews</a></li>
<li><a href="https://letsdatascience.com/blog/broadcom-will-lend-anthropic-42-billion-to-lease-broadcoms-own-chips">Broadcom to Lend Anthropic Up to $42 Billion for TPU Chip Leases</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI infrastructure`, `#financial results`, `#net loss`

---