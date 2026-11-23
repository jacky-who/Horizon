---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 48 条内容中筛选出 27 条重要资讯。

---

**科技新闻**
1. [GLM-5.4 发布：首个循环 Transformer 架构瞄准通用编程](#item-tech-news-1) ⭐️ 8.0/10
2. [Apple removed my open-source app from EU App Stores after 9 years](#item-tech-news-2) ⭐️ 8.0/10
3. [独立浏览器引擎 Ladybird 发布首个 Alpha 版](#item-tech-news-3) ⭐️ 8.0/10
4. [谷歌为 Chrome AI 代理搭建模拟互联网测试环境](#item-tech-news-4) ⭐️ 8.0/10
5. [Codex2api 疑似遭供应链投毒，3.1.10–3.1.12 含后门](#item-tech-news-5) ⭐️ 8.0/10
6. [Meta AI 负责人警告超级智能临近与失控风险](#item-tech-news-6) ⭐️ 8.0/10
7. [英伟达董事会全票恢复黄仁勋总裁兼 CEO 职务](#item-tech-news-7) ⭐️ 8.0/10
8. [LeCun 指 Dario 夸大 AI 风险以封杀开放权重模型](#item-tech-news-8) ⭐️ 7.0/10
9. [互联网档案馆老片变身免费线性电视频道](#item-tech-news-9) ⭐️ 7.0/10
10. [开源 nospeaker 用 MacBook 触控板振动发声](#item-tech-news-10) ⭐️ 7.0/10

**全球芯片**
1. [星思半导体获证监会境外上市备案，拟赴港发行不超 3.88 亿股](#item-chip-news-1) ⭐️ 7.0/10
2. [美国国家情报总监称中国或已获得英伟达先进 AI 芯片](#item-chip-news-2) ⭐️ 6.0/10
3. [LCY 拟以约 6 亿美元向 HSG 牵头财团出售中国半导体化学品业务控股权](#item-chip-news-3) ⭐️ 6.0/10
4. [BIS 新规生效：中国智驾训练与自研芯片会否受限？](#item-chip-news-4) ⭐️ 6.0/10
5. [报道称与黄仁勋有关的女子曾接触中国情报官员](#item-chip-news-5) ⭐️ 5.0/10
6. [英伟达称美政府向董事会保证黄仁勋复职无国安风险](#item-chip-news-6) ⭐️ 5.0/10
7. [巴基斯坦与中国研究人员探讨先进半导体技术合作](#item-chip-news-7) ⭐️ 5.0/10
8. [文章称国产智驾芯片商占前五两席、华为第五，原文未给出排名数据](#item-chip-news-8) ⭐️ 5.0/10
9. [BIS 新规收紧海外流片，国产超节点迎机遇窗口](#item-chip-news-9) ⭐️ 5.0/10
10. [How Nvidia’s billion-dollar turnaround in China is threatened by Huang’s exit](#item-chip-news-10) ⭐️ 4.0/10
11. [软银 1 万亿美元收购 SK 海力士传闻：EE Times 称其为不可行的设想](#item-chip-news-11) ⭐️ 4.0/10

**科技博客**
1. [NVMe 取代 DRAM 层运行 vLLM Agentic KV 缓存](#item-tech-blog-1) ⭐️ 8.0/10
2. [不确定时，先四处试探](#item-tech-blog-2) ⭐️ 6.0/10
3. [OpenAI 困惑度曲线图的几点解读](#item-tech-blog-3) ⭐️ 5.0/10

**财经新闻**
1. [上海地铁票价 21 年来首次调整，起乘价定为 3 元](#item-finance-news-1) ⭐️ 8.0/10
2. [蚂蚁集团领投中国具身智能公司 1 亿美元，估值 16 亿美元](#item-finance-news-2) ⭐️ 7.0/10
3. [英伟达董事会据称未咨询高管层，决定让 Jensen Huang 复任 CEO](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GLM-5.4 发布：首个循环 Transformer 架构瞄准通用编程](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

智谱（Zhipu）发布 GLM-5.4，这是其首个采用「循环 Transformer」（loop transformer）架构的模型，目标指向通用编程能力。据官方博客，该架构在推理时让同一组层权重被多次迭代复用，以缓解 HBM 内存带宽这一推理瓶颈。GLM-5.4 已向所有 GLM Coding Plan 用户开放，新增视觉能力，编程表现较 GLM-5.3 增强；按周计配额的套餐配额提高 50%。目前公开信息仅为厂商公告与社区评论，尚无基准测试结果或第三方验证其宣称的收益。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「循环 Transformer 的背景」** 循环 Transformer 的基本思路是：标准 Transformer 的每一层权重在一次推理中只参与一次计算，而生成每个 token 都需要把整层权重从 HBM 搬到计算单元再搬回，因此内存带宽长期是推理的主要瓶颈。GLM-5.4 并非孤立出现：Z.ai 的开发者文档将其定位为首个基于 Loop Transformer 架构的旗舰模型，第三方报道也提到该架构让同一组 28 层在多次迭代中反复使用以细化理解。至于它与 GLM-5.3 的关系，本次公告只给出按周计配额提高 50% 这一运营层面的变化，并未提供架构层面的前后对比。

**「对 Coding Plan 用户的直接影响」** 对已有 GLM Coding Plan 用户而言，GLM-5.4 是逐步切换而非立即替换：按周计配额的套餐配额提升 50%，并新增视觉输入能力，但据开发者反馈，该模型当时尚未出现在 OpenRouter 或常规 Z.ai API 套餐中，需要通过 Coding Plan 签发的 API key 才能调用。第三方评测同时指出官方未发布基准图表和定价表，并提醒代理类工作流升级需自行衡量回归风险，因此现有 GLM-5.3 用户应先小范围验证再全量迁移。

**「社区讨论」** 有评论者赞赏智谱公开技术细节，并解释循环 Transformer 的原理：传统推理中每层权重只计算一次，需要反复在 HBM 与芯片间搬运整层权重，内存带宽因此成为头号瓶颈，而循环结构可让权重驻留并多次复用。另有开发者抱怨部分中国模型的「马拉松式思考」——即便面对概念上很简单的问题也反复自我怀疑，导致完成时间远高于前沿模型，并猜测这是它们在基准测试上逼近对手的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM - 5 . 4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.youtube.com/watch?v=M6vD9r8kI3A">GLM 5 . 4 Makes AI Smarter by Loop Architecture - YouTube</a></li>
<li><a href="https://explainx.ai/blog/glm-5-4-coding-plan-vision-50-percent-quota-boost-november-2026">GLM-5.4 Coding Plan: +50% Quota, Vision (Nov 2026 ...</a></li>
<li><a href="https://dev.to/buluo/glm-54-vs-glm-53-for-coding-agents-a-migration-decision-you-can-measure-1a05">GLM-5.4 vs GLM-5.3 for Coding Agents: A Migration Decision ...</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/glm-5-4-review">GLM-5.4 Review: What&#x27;s New and What&#x27;s Confirmed</a></li>

</ul>
</details>

**标签**: `#loop transformers`, `#LLM architecture`, `#inference efficiency`, `#code generation`, `#Zhipu GLM`

---

<a id="item-tech-news-2"></a>
### [Apple removed my open-source app from EU App Stores after 9 years](https://github.com/glushchenko/fsnotes/discussions/2056) ⭐️ 8.0/10

An open-source Mac app developer reports Apple removed their app from EU App Stores after nine years, with commenters identifying lapsed EU DSA trader verification as the likely cause and citing similar cases.

hackernews · fluder · 11月23日 18:48 · [社区讨论](https://news.ycombinator.com/item?id=50616933)

**标签**: `#EU DSA`, `#Apple App Store`, `#open source`, `#app compliance`, `#developer platforms`

---

<a id="item-tech-news-3"></a>
### [独立浏览器引擎 Ladybird 发布首个 Alpha 版](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

Ladybird 项目于 2026 年 11 月 23 日发布首个 Alpha 版，用户现在可以在 macOS 和 Linux 上直接下载安装，无需自行编译。该浏览器自行实现了 HTML 解析、CSS 引擎、布局、JavaScript 和 WebAssembly 等大部分核心组件，仅依赖 HarfBuzz 做文本整形、Skia 做 2D 图形、ffmpeg 处理视频和 SQLite 存储。项目方说明这是 Alpha 版本，部分网站无法正常工作且会偶发崩溃，但用户可在浏览器内报告问题站点，并在崩溃后自行决定是否发送崩溃报告。

hackernews · janvdberg · 11月23日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50614249)

**「背景」** Ladybird 源自 Andreas Kling 的 SerenityOS 项目：那是一个从零构建的操作系统，浏览器最初是其配套组件，后来独立成项目，并将部分自研组件替换为 HarfBuzz、Skia、ffmpeg、SQLite 等成熟外部库。此前用户需自行编译源码，这次 alpha 首次提供 macOS 和 Linux 的现成安装包。据项目 2026 年 10 月通讯，其 WebAssembly 引擎改用新代码后在 JetStream 3 的 WASM 基准上提升约 7 倍，并在约 225 万项的 web-platform-tests 子测试中新增 75,650 项通过。

**「实际影响」** 对关注浏览器引擎多样性的用户和开发者而言，这是目前少有的不基于 Chromium/Blink 的可安装浏览器引擎。项目方明确建议把它当作尚不稳定的软件：遇到站点故障应通过内置渠道上报，涉及登录、支付等敏感操作时需自行评估风险；实测中 service worker 相关 API 仍有缺失（如 navigator.serviceWorker.startMessages 报错），依赖这类能力的 Web 应用可能无法运行。

**「社区反馈」** 多位评论者报告了实际试用结果：有人称包括 ProxMox 的 NoVNC 远程桌面在内的站点渲染正常，甚至比 Firefox 更流畅；也有人表示测试的网站全部正确渲染，只有页面滚动略显卡顿，并提到 YouTube 和 Google Maps 可用但有些迟滞。另有评论者对 Ladybird 改用 SQLite、Skia 等成熟第三方库表示理解，同时怀念早期 SerenityOS 阶段的自研黑客精神，还有人询问在 Alpha 阶段应避免登录、支付和下载等敏感操作。

**标签**: `#browser engines`, `#open source`, `#web rendering`, `#software releases`

---

<a id="item-tech-news-4"></a>
### [谷歌为 Chrome AI 代理搭建模拟互联网测试环境](https://www.landian.news/archives/128701.html) ⭐️ 8.0/10

谷歌为 Chrome 的 AI 代理搭建了一个名为 Mirror Dimension 的隔离模拟互联网，用于测试代理打开网站、搜索浏览、登录、加购及完成任务等操作。据蓝点网报道，该环境包含数千个模拟网站，每名工程师单独隔离测试，每天运行超过 1000 个测试案例，重点防御恶意网页的提示词注入等攻击。上述细节来自二手科技资讯聚合，尚无谷歌官方文档或可验证材料确认。

telegram · zaihuapd · 11月23日 01:30

**「背景」** Chrome 内置的浏览器 AI 代理需要像真实上网一样打开网页、搜索、登录和完成任务，因此其安全测试必须在接近真实的网络环境中进行，同时又要避免引入真实风险。据谷歌 Chrome AI 安全工程师 Aaron Selya 与 Charles Qian 撰写的博客介绍，Mirror Dimension 正是为此构建的合成版互联网，用于评估并加固 Chrome 对恶意提示词注入的防御，并通过提高沙盒真实度来减少代理察觉自己处于测试环境的情况。

**「影响」** 若该测试方式属实，它表明在浏览器内代理真正向用户开放前，厂商需要在隔离环境中反复验证代理对恶意网页内容的反应；对开发者而言，代理在登录、加购等涉及账户和交易的操作上能否抵抗提示词注入，将成为评估其可用性的关键条件。但现有报道未披露具体防护效果或测试结论，相关能力仍属未证实状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/security/mirror-dimension-for-agents/">Mirror Dimension for Agents: Evaluating Browser-Use Agents ...</a></li>
<li><a href="https://windowsforum.com/news/google-mirror-dimension-a-synthetic-web-for-testing-chrome-ai-agents-against-prompt-injection.453465/">Google Mirror Dimension: A Synthetic Web for Testing Chrome ...</a></li>

</ul>
</details>

**标签**: `#AI 代理`, `#Chrome`, `#提示词注入`, `#浏览器自动化`, `#AI 安全`

---

<a id="item-tech-news-5"></a>
### [Codex2api 疑似遭供应链投毒，3.1.10–3.1.12 含后门](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

据 Telegram 频道 zaihuapd 转述，codex2api 作者账号被黑后，攻击者绕开 main 分支直接推送 tag，使 Release 构建出带后门的版本。v3.1.11 移除了鉴权，等同于无密码远程执行命令；另有 workflow 将仓库的 16 个 GitHub Actions secrets 外传，波及同一账号下至少 21 个仓库。该帖明确将事件称为「疑似」，内容转述所谓外部报告与事件复盘，未提供独立的原始技术证据。帖文建议已安装或更新 3.1.10–3.1.12 的用户立即停用、回退到 3.1.9，并轮换 GitHub token、SSH key、数据库及 DeepSeek 等相关密钥。

telegram · zaihuapd · 11月23日 11:21

**「背景」** Codex2api 通过 GitHub Release 分发构建产物，发布流程依赖作者账号权限和 Actions 工作流；一旦账号被控制，攻击者便可绕过主分支审查直接推 tag 触发构建。来源称已有外部事件复盘和原始报告，但本条 Telegram 消息只是转述，未提供独立技术核验。

**「影响与应对」** 对于已部署或升级到 3.1.10–3.1.12 的用户，最直接的后果是受影响实例已无鉴权暴露，并可能已发生 GitHub Actions secrets 泄露；应隔离旧实例并保留日志，回退到 3.1.9，同时轮换 GitHub token、SSH key、数据库及 DeepSeek 等相关密钥。外部报道称这三个带后门的 Release 已从 GitHub 移除，但该说法来自单一二手来源，尚未获得项目方或 GitHub 的独立确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ccnavx.com/blog/codex2api-supply-chain-incident">Codex2API Supply Chain Attack: Affected Versions &amp; Fix</a></li>

</ul>
</details>

**标签**: `#supply-chain security`, `#github actions`, `#backdoor`, `#credential rotation`, `#open source security`

---

<a id="item-tech-news-6"></a>
### [Meta AI 负责人警告超级智能临近与失控风险](https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk) ⭐️ 8.0/10

Meta 首席 AI 官、超级智能实验室负责人 Alexandr Wang 在 X 发长文表示，超级智能已不再是“未来某天”的议题。他以数学家 Levent Alpöge 借助 Anthropic 的 Claude 完成、并经 Lean 与 Mathlib 社区机器校验的黎曼猜想证明为例，认为 AI 与顶尖人类的差距只剩具体知识、工程整合与实验三块。他警告人类难以继续掌控可无限自我改进、或比自己聪明 1000 倍的系统，呼吁紧急投入安全、对齐与防护研究。该证明目前尚无人类可读版本，来源内容也未提供独立验证。

telegram · zaihuapd · 11月23日 12:49

**「机器验证的黎曼猜想证明」** 黎曼猜想是数学界最著名的未解问题之一，此前普遍预期其解决尚需数十年——数学家 Terence Tao 曾预测要到 2050 年左右，且不认为 AI 能独立完成。据外部报道，2026 年 11 月 21 日 Lean 与 Mathlib 社区发表联合声明，认证 Levent Alpöge 借助 Claude 完成的黎曼猜想 Lean 证明正确，数十名独立验证者检查了约 1700 万行代码。不过，该证明目前仍无人类可读版本，且克莱数学研究所的百万美元奖金另有发表与两年等待期等条件，因此获奖资格与证明正确性是两回事。

**「影响」** 对 AI 安全与对齐研究者而言，这一表态把“超级智能控制”从长期议题推为需要立即投入的工程问题；但其依据的黎曼猜想证明尚无人类可读版本，也未获独立验证，因此相关论证目前只能视为个人判断，而非已确认的技术结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://effectstory.com/en/articles/lean-communities-certify-claude-assisted-riemann-hypothesis-proof">Alpöge claims a Claude-assisted Riemann hypothesis proof ...</a></li>
<li><a href="https://the-decoder.com/lean-and-mathlib-community-officially-confirms-levent-alpoges-proof-of-the-riemann-hypothesis-is-correct/">Lean and Mathlib community officially confirms Levent Alpöge ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#superintelligence`, `#AI research`, `#alignment`, `#Meta`

---

<a id="item-tech-news-7"></a>
### [英伟达董事会全票恢复黄仁勋总裁兼 CEO 职务](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director) ⭐️ 8.0/10

英伟达董事会全票通过，黄仁勋即刻恢复总裁兼首席执行官职务，并重新担任董事会成员；此前担任临时 CEO 的 Colette Kress 继续出任首席财务官。董事会称，在听取美国政府高层意见后，认为黄仁勋复任不构成国家安全风险；针对此前有关黄仁勋曾成为外国情报活动目标的报道，董事会成立了由独立董事组成的调查委员会，并新设国家安全与出口管制委员会，同时启动首席合规官招聘。董事长 Harvey Jones 表示，董事会对黄仁勋领导公司“有充分信心”。上述内容来自英伟达新闻稿及 Telegram 转发摘要，尚无独立第三方核实。

telegram · zaihuapd · 11月23日 14:02

**「背景」** 黄仁勋此前于 2026 年 11 月从英伟达离职，董事会随后任命首席财务官 Colette Kress 担任临时 CEO。此次全票复职发生在不到两周内；董事会同时成立由独立董事组成的调查委员会，调查黄仁勋是否曾成为外国情报活动的目标，并新设国家安全与出口管制委员会、启动首席合规官招聘。

**「后续影响」** 董事会同时设立国家安全与出口管制委员会，并启动首席合规官招聘，这意味着英伟达的出口管制合规将进入常设监督架构。参议院情报委员会主席 Tom Cotton 表示，国会围绕英伟达与中国芯片走私问题“有大量事项需要调查”，公司仍将面对立法层面的审视。

**「社区讨论」** 有评论者认为，声明中最关键的是董事会“听取美国政府高层意见”后认定复任不构成国家安全风险，这实际上把政府态度置于治理判断的核心。也有人质疑董事会此前迅速让黄仁勋离职、不到两周又全票逆转的做法，认为若掌握实质证据应更清晰说明，若证据不足则应先宣布内部调查而非直接换人；另有评论者指出，目前公开信息并未显示存在被掩盖的犯罪证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/08/technology/nvidia-investigation-jensen-huang.html">What to Know About Nvidia’s Investigation of CEO Jensen Huang ...</a></li>
<li><a href="https://www.cfr.org/articles/nvidia-chinese-espionage-and-the-ai-race-four-foreign-policy-issues-to-watch">Jensen Huang Resigns From Nvidia: Policy Issues Central to ...</a></li>
<li><a href="https://www.nytimes.com/live/2026/11/23/technology/nvidia-jensen-huang-reinstated">Nvidia Live Updates: Jensen Huang’s Reinstatement as CEO Sparks...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#corporate-governance`, `#AI-hardware`, `#export-controls`, `#semiconductor-industry`

---

<a id="item-tech-news-8"></a>
### [LeCun 指 Dario 夸大 AI 风险以封杀开放权重模型](https://twitter.com/ylecun/status/2124550037912920090) ⭐️ 7.0/10

Yann LeCun 在 X 上发帖称，Anthropic 首席执行官 Dario Amodei 自 GPT-2 时期起就夸大 AI 风险，目的是推动开放权重模型被立法禁止，从而让自己保持对 AI 的控制权。LeCun 还称 Amodei 离开 OpenAI 是因为在那里无法获得控制权。该帖是个人指控，未提供可核实的证据，Hacker News 上的讨论也以观点和推测为主。

hackernews · MrBuddyCasino · 11月23日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=50615308)

**「背景」** LeCun 与 Amodei 围绕开放权重与闭源模型的争论并非首次：LeCun 此前已多次公开批评 Amodei 的安全叙事，认为其以 AI 风险警告推动有利于闭源实验室的监管。本次 HN 讨论中，LeCun 进一步指控 Amodei 夸大 AI 危险，目的是让开放权重模型被非法化，从而使自己保持对 AI 的控制。社区评论随后将议题延伸到监管俘获、硬件级限制（如要求 Nvidia/AMD 推送微码更新限制消费级 GPU 运行 LLM）以及私有算力登记等具体政策设想。

**「实际影响」** 开源权重模型的使用者和开发者真正面临的风险不是一则推文，而是可能落地的硬件与算力管控路径：社区讨论中提到的方案包括要求 AMD、Nvidia 通过微码更新限制消费级 GPU 运行大模型，以及对私人算力进行登记备案。公开资料显示，美国自 2025 年 1 月的 AI Diffusion 规则起已对 GPU（ECCN 3A090/4A090）及相关服务设限，因此若硬件级限制被纳入政策，直接受影响的将是依赖消费级显卡本地部署模型的个人和中小团队，而不仅是前沿实验室。

**「社区讨论」** 一位自称与 AI 监管领域人士有往来的评论者称，业界讨论的思路是“禁不了子弹就禁枪”，包括要求 AMD、Nvidia 通过微码更新限制消费级 GPU 运行大模型的能力，以及对私有算力进行登记。另一名评论者则以 HuggingFace 事件为例，认为没有开放模型就无法防御前沿闭源模型的攻击；也有人认为闭源厂商正通过补贴培养用户依赖，若存在开放模型替代品其商业模式将难以为继。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://officechai.com/ai/dario-amodei-hypes-ai-dangers-so-that-open-models-are-made-illegal-and-he-can-stay-in-control-yann-lecun/">Dario Amodei Hypes AI Dangers So That Open Models Are Made ...</a></li>
<li><a href="https://asksurf.ai/pulse/en/lecun-accuses-amodei-of-regulatory-capture-open-vs-closed-ai">LeCun Accuses Amodei of Regulatory Capture in the Open-vs ...</a></li>
<li><a href="https://www.gtlaw.com/en/-/media/files/insights/alerts/2025/12/gt-advisory_navigating-gpu-export-controls-and-ai-use-restrictions-in-data-center-operations.pdf">GT Alert_Navigating GPU Export Controls and AI Use ...</a></li>
<li><a href="https://idsa.in/publisher/issuebrief/computational-resource-control-the-2025-us-ai-framework">Computational Resource Control: The 2025 US AI Framework</a></li>

</ul>
</details>

**标签**: `#ai-policy`, `#open-weight-models`, `#regulatory-capture`, `#ai-safety-debate`, `#hardware-regulation`

---

<a id="item-tech-news-9"></a>
### [互联网档案馆老片变身免费线性电视频道](https://spelunkr.tv/) ⭐️ 7.0/10

Spelunkr.tv 是一个免费的流媒体“电视网”，它把互联网档案馆（Internet Archive）中鲜为人知的视频整理成按节目表播出的线性频道。该项目由用户 SockThief 发布在 Hacker News，获得 921 分和 159 条评论。目前没有来源内容说明频道数量、节目表生成方式、是否开源或播放可用性等具体细节。它更像是一个怀旧向的 DIY 媒体实验，而不是底层技术范式的改变。

hackernews · SockThief · 11月23日 01:13 · [社区讨论](https://news.ycombinator.com/item?id=50606192)

**「背景」** Spelunkr 将 Internet Archive 中大量冷门视频编排成频道，提供 24 小时同步播出的线性“有线电视”体验；观众在同一时间看到同一节目，而不是按需点播。社区中已有类似的自建项目：FieldStation 42 是一个开源广播/有线电视模拟器，可在 Linux、树莓派或 Windows WSL 上使用自己的视频文件排成频道表，并插入广告时段。Spelunkr 的不同之处在于，它直接把 Internet Archive 的公开馆藏作为片源和节目表。

**「影响」** 对想重温“按点播出”观看体验的用户来说，这个项目提供了一条直接路径：不用自己搭建媒体服务器或整理片源，就能看到由互联网档案馆素材编排的频道。评论中有人提到，它绕过互联网档案馆自身的界面直接播放视频，这可能会引发关于第三方界面使用档案馆内容的讨论。

**「社区讨论」** 评论者 gabriel666smith 指出，点播观看有时会带来“背景性的孤独感”，因为没有人同时在看同一内容，而线性频道恢复了这种同步感；goatherders 表示自己连续看了 45 分钟 1987 年的 Headbangers Ball，并称赞了其中的怀旧广告。Woodrow503 则分享了自己用 FieldStation42 在树莓派 5 上搭建类似系统的经验，说明这类 DIY 项目已有实践基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spelunkr.tv/">SPELUNKR — Cable TV , but weirder</a></li>
<li><a href="https://www.itechguides.com/fieldstation42-the-golden-age-of-90s-cable-brought-to-you-by-a-raspberry-pi/">FieldStation 42 : 90s Cable TV Simulator on Raspberry Pi</a></li>
<li><a href="https://www.xda-developers.com/raspberry-pi-project-recreates-favorite-90s-tv-channels/">This Raspberry Pi project recreates your favorite 90s TV channels...</a></li>

</ul>
</details>

**标签**: `#Internet Archive`, `#streaming media`, `#media preservation`, `#retro TV`, `#DIY/open source`

---

<a id="item-tech-news-10"></a>
### [开源 nospeaker 用 MacBook 触控板振动发声](https://m.mydrivers.com/newsview/1167826.html?ref=https%3A//www.google.com/) ⭐️ 7.0/10

开发者 Cody Collier 开源了工具 nospeaker，把 MacBook 触控板下方的触觉马达驱动频率提高到每秒 4000 次，让玻璃振动快到人耳可闻，从而「念出」文字。它用 macOS 语音合成读入文字，每 10 毫秒提取两个共振峰，连同响度和音高一起重放，听感偏机器人；实测在 100 Hz 至 4 kHz 范围内可发声，1 kHz 附近最清晰。该工具只能朗读文字，无法播放音乐和视频，且绕开苹果公开的触觉接口、调用私有框架 MultitouchSupport。它需要 Force Touch 触控板，作者称只在 M5 Max 的 MacBook Pro 上验证跑通。

telegram · zaihuapd · 11月23日 07:16

**「背景」** MacBook 的 Force Touch 触控板依靠线性谐振马达提供按压反馈，原本只用于模拟点击和触觉提示。nospeaker 的思路是把同一个马达当作扬声器振膜来驱动，用高频振动直接产生可听声，而不是走常规音频输出通道。

**「影响」** 对想在 Mac 上做硬件实验的开发者来说，nospeaker 提供了一条不依赖额外扬声器的验证路径，但代价是依赖私有框架和特定 Force Touch 机型，适用面和可移植性都很有限；想要复现的人需先确认自己的设备是否已被验证。

**标签**: `#haptics`, `#open-source`, `#macOS`, `#speech-synthesis`, `#hardware-hacking`

---

## 全球芯片

<a id="item-chip-news-1"></a>
### [星思半导体获证监会境外上市备案，拟赴港发行不超 3.88 亿股](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2fwww.eet-china.com%2fmp%2fa541211.html&amp;c=7886811501635680782&amp;mkt=en-us) ⭐️ 7.0/10

据中国证监会国际合作司披露的备案通知书，国产卫星通信芯片厂商星思半导体拟发行不超过 3.88 亿股境外上市普通股，并在香港联合交易所上市。同时，公司 76 名股东拟将所持合计 28.23 亿股境内未上市股份转为境外上市股份，在港交所上市流通。这是备案阶段的信息披露，尚不等同于已完成发行或挂牌；发行上限与股份转换数量均为备案文件所列数字。

rss · Bing News - China domestic chips · 11月23日 04:42

**「背景」** 境内企业赴港上市须先完成中国证监会境外发行上市备案，取得备案通知书后才能推进港交所发行程序。此次备案通知书由证监会国际合作司披露，是星思半导体赴港上市流程中的前置环节。

**「影响」** 若发行与股份转换按备案推进，星思半导体将获得境外资本市场融资通道，其 76 名境内股东所持 28.23 亿股也将转为可在港交所流通的境外上市股份，改变该公司股东结构的流动性安排。但备案不等于通过港交所上市聆讯或完成发行，实际募资规模与时间表仍取决于后续审核和市场情况。

**标签**: `#国产芯片`, `#卫星通信芯片`, `#港股IPO`, `#资本市场`

---

<a id="item-chip-news-2"></a>
### [美国国家情报总监称中国或已获得英伟达先进 AI 芯片](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fwww.yahoo.com%2fnews%2fvideos%2fchina-likely-nvidia-advanced-ai-124615337.html&amp;c=892859684981909522&amp;mkt=en-us) ⭐️ 6.0/10

美国国家情报总监杰伊·克莱顿在接受 CNN 主持人达娜·巴什采访时表示，他预计中国已经找到获得英伟达先进 AI 芯片的途径。克莱顿没有说明涉及哪些芯片型号、经由何种渠道获取，也未给出数量或证据。这一表态属于情报主管的公开判断，而非已确认的调查结论或已公布的执法行动。

rss · Bing News - NVIDIA and China · 11月23日 04:46

**「事件背景」** 此次表态发生在 CNN 主持人达娜·巴什对美国国家情报总监杰伊·克莱顿的采访中，克莱顿称他预计中国已找到获取英伟达先进 AI 芯片的途径，但没有说明渠道、数量或具体型号。相关报道提到，克莱顿在同一场采访中还谈及网络安全议题，以及围绕 Megaspeed 和中国正在进行的调查；2026 年 10 月曾有报道称特朗普任命克莱顿兼任白宫 AI 事务负责人，但现有材料未说明该任命与本次芯片表态存在直接关联。

**「管制重心或转向转运稽查」** 若这一判断成立，实际影响更多落在对华出口管制的执行缺口而非规则本身：台湾正推动将未经许可向中国出口先进 AI 芯片入刑，其背景是英伟达服务器经印尼、日本和香港转运后流入中国买家。这意味着后续管制重点可能从许可审批转向第三地转运路径与中介的稽查。有研究非法贸易的学者估算，现行管制已催生规模达数十亿美元的灰色市场，但该数字为外部估算而非官方统计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thegatewaypundit.com/2026/11/video-director-national-intelligence-jay-clayton-shuts-down/">(VIDEO) Director of National Intelligence Jay Clayton Shuts Down...</a></li>
<li><a href="https://theconservativetreehouse.com/blog/2026/11/22/sunday-talks-odni-jay-clayton-discusses-cyber-security-with-dana-bash/">Sunday Talks - ODNI Jay Clayton Discusses Cyber Security with...</a></li>
<li><a href="https://www.npr.org/2026/10/04/nx-s1-5990781/jay-clayton-ai-czar-trump">Trump names national intelligence chief Jay Clayton as new AI czar</a></li>
<li><a href="https://www.breitbart.com/tech/2026/11/23/nvidia-nightmare-investigations-reveal-jensen-huangs-girlfriend-has-ties-to-chip-smugglers-chinese-intelligence/">Nvidia Nightmare: Investigations Reveal Jensen Huang&#x27;s Girlfriend...</a></li>
<li><a href="https://asiatimes.com/2026/11/taiwan-to-criminalize-nvidia-ai-chip-smuggling-to-china/">Taiwan to criminalize Nvidia AI chip smuggling to China - Asia Times</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-3"></a>
### [LCY 拟以约 6 亿美元向 HSG 牵头财团出售中国半导体化学品业务控股权](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d80574ffbb852e6d42a9ae36c&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fother%2flcy-s-china-chip-chemicals-business-draws-600m-takeover-interest-from-hsg-led-consortium-report%2far-AA2i2RcN&amp;c=1322568966284489748&amp;mkt=en-us) ⭐️ 6.0/10

台湾 LCY 集团据报正就出售其中国半导体化学品业务控股权，与 HSG 牵头的投资财团进行深入谈判，交易估值约 6 亿美元。该消息属媒体报道，双方尚未公布签约、监管审批或交割时间，也未披露具体产品线、产能规模及买方持股比例。

rss · Bing News - China chip policy · 11月23日 03:50

**「背景」** LCY（李长荣集团）在中国大陆运营半导体化学品业务。据本次报道，该业务估值约为 40 亿元人民币（约 6 亿美元），超过其核心盈利的 20 倍；交易完成后，LCY 计划仍为该业务的单一最大股东。上述估值倍数与股权安排均来自报道中的消息人士说法，交易条款尚未正式披露。

**「影响」** 若交易按报道推进，中国半导体化学品业务的所有权将由台资集团部分转向 HSG 牵头的资本财团；半导体化学品是晶圆制造与封装环节的投入品，股权变更可能影响该业务与客户的关系及扩产决策。但报道未说明客户构成、产能规模，也未说明是否涉及先进制程材料，因此在交割与审批明朗前，无法判断对中国国内芯片材料供给的实际影响。

<details><summary>参考链接</summary>
<ul>
<li>HSG-led consortium in talks to buy controlling stake in LCY&#x27;s China chip chemicals business</li>
<li>LCY Group Nears $600M Sale of Semiconductor Chemicals Unit Amid - GuruFocus</li>

</ul>
</details>

**标签**: `#半导体材料`, `#供应链`, `#对华投资`, `#国产芯片`, `#并购`

---

<a id="item-chip-news-4"></a>
### [BIS 新规生效：中国智驾训练与自研芯片会否受限？](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261124A02O4R00&amp;c=279504482962160428&amp;mkt=en-us) ⭐️ 6.0/10

腾讯新闻 2026 年 11 月 24 日的一篇报道提到，美国商务部工业与安全局（BIS）的一项芯片出口新规在同期生效，并称其影响将波及汽车行业和整个中国科技行业。该报道把此事与同期英伟达 CEO 黄仁勋的相关新闻并列，同时认为后者对多数人并无实质影响。所给原文仅为节选，新规的具体条款、生效日期、涉及企业与产品型号，以及对中国智能驾驶训练和国产自研芯片究竟限制或允许了什么，均未在材料中说明，无法核实。报道以设问方式提出中国智驾训练和自研芯片“会不会被卡住”，这是待回答的问题，而非已确认的结论。

rss · Bing News - China domestic chips · 11月23日 08:05

**「背景」** 据 WilmerHale 与 Baker McKenzie 的客户提示，美国商务部工业与安全局（BIS）于 2026 年 11 月 15 日发布一项临时最终规则（IFR），首次把“远程访问”先进半导体（用于训练和运行 AI 模型的高性能处理器）纳入管制，并同时正式撤销此前拜登政府于 2025 年 1 月 13 日出台的“AI 扩散规则”。该旧规则曾对部分先进计算集成电路及特定闭源先进 AI 模型的模型权重设定全球许可要求与复杂出口管制；Fenwick 的解读指出，新规是在特朗普政府官员与国会就 AI 芯片出口、转运规避以及中国等 D:5 国家组远程访问缺乏管控持续施压后推出的。来源文本仅提及该新规生效，未给出具体条款，因此其对中国智驾训练与国产芯片的实际约束范围尚待规则文本确认。

**「影响」** 所给原文仅为截断的导语，没有披露新规的具体条款、生效日期、许可要求或涉及的企业名单，因此无法据此判断该规则对中国智驾训练算力采购或国产自研芯片供货的实际影响——究竟哪类芯片、以何种门槛被限制，目前均无证据支持。检索结果中仅有一条提及美国汽车智驾调研与自研芯片布局的页面标题，以及一条关于英伟达芯片经东南亚流向中国企业的出口管制漏洞说法，均属无法核实的二手或无关信息（tool-2-1、tool-2-2、tool-2-3），不足以支撑任何具体的后果判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sanctionsnews.bakermckenzie.com/bis-restricts-remote-access-to-advanced-ai-chips-and-formally-rescinds-the-ai-diffusion-rule/">BIS Restricts Remote Access to Advanced AI Chips and Formally ...</a></li>
<li><a href="https://www.fenwick.com/insights/publications/bis-announces-new-export-controls-remote-access-ai-chips">BIS Announces New Export Controls on Remote Access, AI Chips</a></li>
<li><a href="https://www.wilmerhale.com/en/insights/client-alerts/20261117-us-government-restricts-remote-access-to-advanced-ai-chips-and-formally-rescinds-the-ai-diffusion-rule">US Government Restricts Remote Access to Advanced AI Chips ...</a></li>
<li>openclaw-impact-report/index.html at main - GitHub</li>
<li>AI Coding Agents Compared: Claude Code, Devin, AutoGPT (July Update) | AIFOD</li>
<li>rkkk.net at WI. Rkkk Platform Slot Resmi Indonesia | Daftar Login Aman - Website Informer</li>

</ul>
</details>

**标签**: `#对华出口管制`, `#国产芯片`, `#AI 算力`, `#英伟达`

---

<a id="item-chip-news-5"></a>
### [报道称与黄仁勋有关的女子曾接触中国情报官员](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fabc7chicago.com%2fstory%2fwoman-center-nvidia-scandal-was-touch-chinas-top-spy-agency-sources%2f20069206%2f&amp;c=17224972434123134999&amp;mkt=en-us) ⭐️ 5.0/10

据 ABC7 Chicago 转载的报道，未具名消息人士称，一名据称与英伟达首席执行官黄仁勋存在婚外情的女子，曾与中国最高情报机构的一名官员保持联系，接触发生在她与黄仁勋交往期间。该报道未披露接触的具体时间、内容，也未说明涉及任何英伟达产品、出口许可或供应链安排。报道同样未提及是否已启动调查、是否提出指控，或英伟达与黄仁勋方面作何回应。上述内容均属匿名消息源的说法，未经独立证实。

rss · Bing News - NVIDIA and China · 11月23日 02:39

**「事件背景」** 该报道涉及的背景是：据称与英伟达（NVIDIA）首席执行官黄仁勋（Jensen Huang）有婚外情的女性，被指在 2025 年春季至 2026 年秋季期间，与中国国家安全部（Ministry of State Security）的一名官员保持联系。据多个报道，黄仁勋在相关丑闻曝光后辞去英伟达首席执行官职务；英伟达董事会随后投票决定恢复其首席执行官兼总裁职位。这些内容均来自未经独立证实的报道和匿名消息源，目前尚无公开证据说明该事件对英伟达产品、出口管制或供应链产生实质影响。

**「实际影响」** 目前可核实的影响集中在公司治理与合规审查层面，而非芯片供应或出口许可的直接变化：加州正就英伟达芯片出口是否流入中国展开调查，董事会则称在让黄仁勋复职前征求了美国联邦政府高层意见。就现有报道而言，尚未出现许可证被撤销、出货被叫停或对华销售规则调整的具体条款，因此对该事件的供应链后果应保持谨慎，不能据此推断英伟达对华业务已被限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yahoo.com/news/politics/articles/woman-center-nvidia-scandal-touch-061322657.html">Woman at center of Nvidia scandal was in touch with China &#x27;s top spy ...</a></li>
<li><a href="https://www.foxbusiness.com/politics/trump-doubles-down-call-nvidia-rehire-jensen-huang-amid-alleged-chinese-spy-scandal">Trump urges Nvidia to rehire Jensen Huang after affair with alleged ...</a></li>
<li><a href="https://www.bbc.com/news/live/crd61y5dwqgpt">Jensen Huang reinstated as Nvidia CEO, board says - BBC News</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/23/jensen-huang-reinstated-as-nvidia-chief-executive">Jensen Huang reinstated as Nvidia CEO | Jensen Huang | The Guardian</a></li>
<li><a href="https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html">Jensen Huang reinstated as Nvidia CEO. Stock skyrockets 31%</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#中美芯片合作`, `#对华出口管制`, `#Jensen Huang`, `#China`

---

<a id="item-chip-news-6"></a>
### [英伟达称美政府向董事会保证黄仁勋复职无国安风险](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fgizmodo.com%2fthe-single-most-important-line-from-nvidias-statement-about-jensen-huangs-return-2000844082&amp;c=17956557870182898364&amp;mkt=en-us) ⭐️ 5.0/10

英伟达表示，美国政府官员已向其董事会保证，让黄仁勋重新出任相关职务不构成国家安全风险。这一说法出自公司就黄仁勋复职发布的声明。现有材料只涵盖这一公司—政府层面的表态，未说明复职的具体职位与时间安排，也未提及对华出口管制、产品或出货数据的任何变化。

rss · Bing News - NVIDIA and China · 11月23日 11:30

**「背景」** 该声明回应的是围绕黄仁勋在英伟达职务状态的治理问题。由于英伟达对华业务长期处于美国出口管制审查之下，公司选择以“政府官员已作安全评估”的方式公开澄清，但现有材料未提供此前的具体规则、许可决定或职务变动细节。

**「影响」** 按现有证据，这一保证的作用限于治理层面：它降低了黄仁勋复职在国家安全审查上的不确定性；但材料未显示英伟达对华出货、许可申请或产品供应因此出现任何具体变化，因而无法据此判断其中国业务准入条件已调整。

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`

---

<a id="item-chip-news-7"></a>
### [巴基斯坦与中国研究人员探讨先进半导体技术合作](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d80574ffbb852e6d42a9ae36c&amp;url=https%3a%2f%2fwww.msn.com%2fen-xl%2fscience%2fgeneral%2fpak-china-researchers-to-cooperate-in-advanced-semiconductor-techpublished-on-november-23-2026-9-04-am%2far-AA2i0Yqi&amp;c=10844837300057430555&amp;mkt=en-us) ⭐️ 5.0/10

巴基斯坦国立大学主办的一场国际研讨会上，巴基斯坦与中国研究人员就先进半导体技术领域的合作机会进行了探讨。公开报道仅确认这是学术研讨层面的交流，未披露参与机构名单、具体合作项目、投资规模、涉及的技术节点或任何政策与许可安排。报道也没有说明合作形式是联合研究、人才培养还是产业对接，亦无后续时间表。因此目前可确认的事实仅限于双方学者在研讨会场合表达了合作意向这一层面。

rss · Bing News - China chip policy · 11月23日 01:34

**「背景」** 该研讨会由巴基斯坦高校主办，属于中巴两国在半导体领域学术往来的一部分。现有报道未提及此前的具体合作项目、协议或上一阶段进展，因此无法确认此次研讨与既往中巴半导体合作之间存在直接承继关系。

**「影响」** 由于报道未披露合作的具体内容、参与方与资金安排，目前无法评估其对中巴芯片供应链、产能或技术获取的实际影响；若后续形成联合研究或人才培养机制，可能影响巴基斯坦的半导体人才储备，但现有证据不足以支持这一判断。

**标签**: `#中美芯片合作`, `#国产芯片`, `#先进制程`, `#半导体研究`

---

<a id="item-chip-news-8"></a>
### [文章称国产智驾芯片商占前五两席、华为第五，原文未给出排名数据](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1105159807_121097259&amp;c=4922930732126220630&amp;mkt=en-us) ⭐️ 5.0/10

搜狐一篇评论文章称，国产智能驾驶芯片厂商已在智驾芯片市场前五名中占两席，华为进入第五。但可获取的原文片段只讨论新能源汽车三电系统、智能系统与智能座舱的分工，并笼统提到座舱芯片和智驾芯片此前存在“隐患”，没有列出前五名名单，也没有提供市场份额、出货量、制程或数据来源，因此这一排名变化无法核实。文章标题中“英伟达没落”的判断同样缺少数据支撑，应视为作者评述，而非已公布的第三方统计或厂商出货数据。

rss · Bing News - China domestic chips · 11月23日 03:54

**「背景」** 从高阶智驾芯片市场格局看，英伟达此前仍居首位。高工智能汽车研究院发布的 2026 年上半年数据显示，在自主品牌乘用车支持城区 NOA 的芯片市场中，英伟达份额为 39.43%，地平线为 22.82%，两者形成“双强”格局。与此同时，国产厂商正加快自研与量产布局：理想代号“舒马赫”的自研智驾芯片预计 2026 年量产，小鹏汽车、小米汽车也在自研智驾芯片；地平线于 2026 年 4 月发布中国首款舱驾融合整车智能体芯片“星空”6 系列。在此背景下，该文所称国产厂商占据前五中两席、华为升至第五，尚缺乏具体排名与份额数据支撑。

**「影响」** 由于原文未给出前五名的具体份额、出货量或客户名单，这则“两席进前五”说法目前只能视为一种市场趋势描述，无法据此确认英伟达在中国智驾芯片市场的实际份额变化，也不足以说明国产替代已经推进到哪一个量产节点。从可获得的信息看，本土厂商之间仍在争夺同一梯队的位置：地平线被拿来与 Mobileye 和英伟达对标，蔚来的自研芯片神玑 NX9031 于今年 7 月宣布流片成功，理想代号“舒马赫”的自研智驾芯片预计年内完成流片、2026 年量产；这些进展尚未转化为可核验的装车规模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bianews.com/news/details?id=197814">市 值逼近Mobileye， 地 平 线 真的迎来曙光</a></li>
<li><a href="https://k.sina.com.cn/article_6347973665_17a5e642102701wg1m.html">英 伟 达 第一，但半年丢了10%！ 地 平 线 坐稳第二，高阶 智 驾 芯 片 双强</a></li>
<li><a href="https://nev.ofweek.com/2026-07/ART-77013-8420-30694449.html">高通、 英 伟 达 、 地 平 线 ，都在做同一件事 - OFweek新 能 源汽车网</a></li>
<li><a href="https://bianews.com/news/details?id=197814">市 值逼近Mobileye，地平线真的迎来曙光</a></li>

</ul>
</details>

**标签**: `#国产芯片`, `#智能驾驶芯片`, `#英伟达`, `#华为`, `#AI 算力`

---

<a id="item-chip-news-9"></a>
### [BIS 新规收紧海外流片，国产超节点迎机遇窗口](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2f36kr.com%2fnewsflashes%2f4082941578318729&amp;c=13891380597614384693&amp;mkt=en-us) ⭐️ 5.0/10

上证报报道称，近日流传的三星对代工订单展开穿透式严查的传闻并不准确，记者已向国内晶圆代工厂、芯片设计公司等多方求证。报道指出，传闻背后是美国商务部工业和安全局（BIS）于 11 月 16 日出台新规，被指存在滥用出口管制问题，使海外流片通道进一步收紧。多位业内人士表示，在此态势下国产 AI 供应链建设势在必行；在制程技术落后于海外先进厂商的情况下，超节点有望弥补单芯片算力短板，并将迎来发展机遇窗口。报道未披露新规的具体条款、受限产品型号、制程节点或量产数据，相关判断属业内预期而非已确认的规则细节或出货结果。

rss · Bing News - China domestic chips · 11月23日 09:08

**「背景」** 上证报的报道把传闻澄清与规则背景分开：三星“穿透严查代工”的说法经向国内晶圆代工厂、芯片设计公司等多方求证后被认为不准确，但报道同时指出，传闻背后是美国商务部工业和安全局（BIS）11 月 16 日新规带来的出口管制收紧。CSIS 的分析显示，这项 11 月 16 日规则针对支撑“超级智能”的先进硬件，并正式撤销、替换拜登时期的相应规定；BIS 今年 1 月也曾发布过一轮先进计算芯片出口管制与实体清单更新。在这一背景下，报道引述业内人士称海外流片通道进一步收紧，国产 AI 供应链建设与超节点方案因此被寄予弥补单芯片算力短板的期待。

**「影响」** 若海外流片通道如业内所述持续收紧，国内 AI 芯片设计公司获取境外先进制程代工服务的路径将受到更多限制，其流片安排需更多转向本土代工产能与现有工艺条件。报道据此提出，以超节点在系统层面聚合多颗芯片、用集群规模弥补单芯片算力差距，是制程落后条件下的一条可行替代方向；但新规适用范围与执行细节未在报道中说明，实际影响仍待观察。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-enhance-foundry-due-diligence-prevent">www.bis.gov</a></li>
<li><a href="https://www.csis.org/analysis/new-export-controls-remote-access-implications-industry-and-competition-china">New Export Controls on Remote Access: The Implications for ...</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#国产芯片`, `#AI 算力`, `#晶圆代工`, `#供应链`

---

<a id="item-chip-news-10"></a>
### [How Nvidia’s billion-dollar turnaround in China is threatened by Huang’s exit](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fhow-nvidia-s-billion-dollar-turnaround-in-china-is-threatened-by-huang-s-exit%2far-AA2i2R8Z&amp;c=16636505390457349027&amp;mkt=en-us) ⭐️ 4.0/10

A Reuters teaser says Nvidia staged a China comeback with less powerful chips and software after US export bans, but offers no concrete details or figures.

rss · Bing News - NVIDIA and China · 11月23日 03:38

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-11"></a>
### [软银 1 万亿美元收购 SK 海力士传闻：EE Times 称其为不可行的设想](https://www.eetimes.com/the-enigma-of-softbanks-1-trillion-sk-hynix-buyout-attempt/) ⭐️ 4.0/10

EE Times 于 11 月 23 日刊发评论文章，讨论外界所传软银以 1 万亿美元收购 SK 海力士的尝试。文章称该收购从一开始就不可行，并认为这一传闻反映出存储芯片在 AI 算力扩张中的战略吸引力。所提供的源内容仅有导语和页面链接，未披露交易条款、谈判参与方、时间表或消息来源，因此无法确认收购是否真实存在、由谁提出以及目前进展如何。

rss · EE Times · 11月23日 08:30

**「背景」** 这一讨论源于 The Information 于 11 月 20 日（周五）的报道：软银集团 CEO 孙正义近期接触华尔街机构，商讨为一笔规模约 1 万亿美元的 SK 海力士收购交易融资；路透社 11 月 21 日转述了这一消息。SK 海力士是全球第二大存储芯片厂商，EE Times 的这篇评论即围绕该报道展开，探讨这笔交易为何难以推进。

**「影响与不确定性」** 由于缺少可核实的交易细节，目前无法判断该传闻会对 SK 海力士的股权结构、HBM 等 AI 存储芯片供应或软银的投资布局产生何种实际影响。文章本身也只将其作为对存储战略价值的评论，而非已经启动的收购程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eetimes.com/the-enigma-of-softbanks-1-trillion-sk-hynix-buyout-attempt/">The Enigma of SoftBank’s $1 Trillion SK Hynix Buyout Attempt</a></li>
<li><a href="https://www.reuters.com/world/asia-pacific/softbanks-son-explored-1-trillion-buyout-sk-hynix-information-reports-2026-11-21/">SoftBank’s Son explored $1 trillion buyout of SK Hynix, the ...</a></li>

</ul>
</details>

**标签**: `#AI 算力`, `#存储芯片`, `#行业分析`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [NVMe 取代 DRAM 层运行 vLLM Agentic KV 缓存](https://vllm.ai/blog/2026-11-23-skip-the-dram-tier) ⭐️ 8.0/10

rss · vLLM Blog · 11月23日 00:00

**「背景」** Agentic 服务中，多轮会话反复重发长前缀：AgentX 回放里中位单轮输入为 142K token，其中 96% 以上是服务器已经见过的前缀。KV 命中率每提高 1 个百分点（例如 95%→96%），作者在 42 组 Kimi-K3 运行中测得约多出 10% 吞吐，但 GPU 显存很快装不下，主机 DRAM 也会填满——Kimi-K3 每小时写入 2.3–4.6 TB KV，1.8 TB DRAM 池只能保留最近 23–47 分钟。

**「方案」** 作者因此跳过 DRAM 层，把 vLLM 的 KV 池直接放在 NVMe 上，采用 AMD 开源 MoRI 库中的 UMBP 池，并以 vLLM 连接器接入。同容量的 1.8 TB NVMe 池与 DRAM 池在 48/70/96 会话下吞吐相差不超过 1%（另一对机器上 NVMe 领先 0.4%–0.9%），命中率差最多 0.08 个百分点，p50 TTFT 差在 0.3–0.8 秒内；机制是 vLLM 异步加载 KV，慢速读盘被 prefill 等待掩盖，且同容量同淘汰策略保留同样的 KV。DRAM 只留 64 GB 写缓冲加 16 GiB 读暂存（不足池的 5%），70 会话下去掉写缓冲也无损失，更高负载则建议保留。作者总结出三条可迁移经验：一是 NVMe 上 UMBP 只能追加写、按文件回收，把默认 4 GiB 段文件改为 256 MiB，使 70 会话命中率从 94.45% 升到 95.65%、吞吐提高 15.6%，让 NVMe 从落后 DRAM 12.8% 变为领先 0.8%；二是让 vLLM 连接器把 GPU 前缀命中回报给池，避免池把仍被使用的 KV 当作冷数据淘汰，两个测试中吞吐提高 2.1% 和 3.9%，TTFT p99 从 70–77 秒降到 35–43 秒；三是为混合模型更频繁地做 checkpoint，把间隔设为 7,168 token 后命中率从 91.4% 升到 95.6%、吞吐提高 33%，但 checkpoint 本身占 Kimi-K3 NVMe 写入的一半以上。成本逻辑也随之改变：DRAM 按持有容量计价（约每 TB 4.2 万美元），NVMe 按写入量消耗寿命（每天全盘写一次的盘五年折合约每 TB 0.36 美元）；按 96 会话每天 83 TB 写入计算，能存一天的 83 TB NVMe 池与反复更换的 1.8 TB 池五年成本都约 5.9 万美元，而 1.8 TB DRAM 池约 7.6 万美元，存一天的 DRAM 池则约 350 万美元；保留时间低于约 24 分钟时 DRAM 反而更便宜。作者也明确局限：每个计算出的 KV 块都写入硬盘、加速磨损（测试盘按 96 会话写入约五个半月耗尽额定寿命），需用分布式池把写入摊到更多 SSD；成本是标价算术，未计电力、机架与盘服务器，保留时间与吞吐的估算由两个拟合模型串联，只在有限区间校验过。

**「启示」** 作者的核心论点是：当 KV 池的瓶颈从“能存多少”转向“能留住多久”时，NVMe 可以跳过 DRAM 层，以同容量近似的吞吐换来数量级更长的保留时间。真正的设计杠杆不在介质本身，而在段文件粒度、GPU 前缀回报和 checkpoint 策略这些决定命中率的实现细节，以及按写入量而非容量计算 NVMe 的寿命成本。

**标签**: `#KV cache`, `#NVMe`, `#vLLM`, `#agentic serving`, `#memory tiering`

---

<a id="item-tech-blog-2"></a>
### [不确定时，先四处试探](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** 面对缺乏明确指引、不知道什么做法有效的模糊处境，Sean Goedecke 认为，谨慎等待理解清晰往往不如主动“四处试探”（flailing）。他承认这种建议有风险：方法不当会像那些不断推销糟糕方案的工程师一样损害声誉，但正确地试探能最快获得理解并变得有用。

**「方案」** 作者把好的试探拆成三条相互支撑的做法：尝试大量不同的事情，以尽可能多地接触现实；极其仔细地观察反馈；并果断放弃没有获得积极反馈的计划。之所以要试很多，是因为在信息不足时大多数计划都会失败，你也没有能力预先判断哪个可行，试十个才可能有一个是好的；同时拥有多个计划还能避免过度投入，使放弃失败方案变得容易。

他给出三类适用场景。产品试探发生在尚未找到产品市场契合的新功能上：他在 GitHub Models（现已停用）时期构建过许多最终无效的功能或集成，但“允许用 GitHub Actions token 运行 AI 推理”出乎意料地有粘性，成为“Continuous AI”的种子；若不做试探，很可能把大量精力押在注定失败的想法上，找到有牵引力的方向后再全力投入。工程试探针对过于纠缠、已高度优化或庞大未知的系统：与其先通读整个系统，他认为更实际的是做一批探索性修改，看效果或性能是否改善，无效则立即放弃，有效再深究原因，并提到 AI agent 可以帮助快速生成多个重构方案供筛选。组织试探则最常见于资深和 staff 工程师面对的跨团队不沟通、团队不满等非技术问题：自动执行部分手工工作、主动接手任务、提出可能改善局面的长期计划，多数不会有用，但至少显示你在尝试；这里尤其要对反馈敏感，否则人们的不满会转向你。作者解释之所以叫“flailing”，是因为从内部感受像反复失败、信息不足、出丑，而管理者可能只看到一位主动实验的工程师，这种不适感是需要克服的心理障碍。

**「启示」** 作者的核心论点是：在不确定且没有清晰路径时，有反馈意识地快速尝试许多廉价实验、立即放弃无效方案，比先追求完整理解更能有效地解决工程与组织问题；关键不是避免“像在乱扑”，而是把这种感受视为正常信号，同时保持对反馈的高度敏感。

**标签**: `#engineering management`, `#experimentation`, `#handling uncertainty`, `#product development`, `#organizational dynamics`

---

<a id="item-tech-blog-3"></a>
### [OpenAI 困惑度曲线图的几点解读](https://seangoedecke.com/notes-on-openais-perplexity-reveal/) ⭐️ 5.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** OpenAI 罕见公开了其所有已发布模型随时间的困惑度（perplexity）曲线，这是外界迄今对一个前沿实验室内部训练指标最直接的一瞥。作者 Sean Goedecke 以零散笔记的形式回应这张图，试图区分哪些结论能从指标本身读出来，哪些只是基于传闻的推测。

**「方案」** 他首先强调指标的可比性边界：困惑度必须相对于特定数据集测量，因此其他实验室即便公布同类数据，也不能直接横向比较，除非双方披露具体的留出文本。在他看来，困惑度只反映预训练对文本的拟合程度，而传闻称预训练在前沿模型的总训练时间与算力中占比不超过一半，其余是 RL，因此这张图无法说明后训练的成功。若相信“预训练创造能力、RL 只是把能力引出来”，困惑度仍可作为能力的粗略代理，但链式思维带来的提升等能力维度未必与它相关。

图中真正让作者意外的是基座复用：几乎没有模型共享完全相同的困惑度，此前关于 OpenAI 把 4o 和 4.1 后训练成许多模型的传闻，实际只对应 o1 与 o3；而表现亮眼的 o3 与令人失望的 4.1 共享同一基座，也颇为耐人寻味。曲线还显示 GPT-4.5 附近出现过一次对大型预训练模型的短暂放弃，其困惑度与 GPT-5.3-Codex 相近却远不如后者有用，至于这是主动选择还是撞上内部扩展瓶颈，作者无法判断。从 GPT-5.2 起困惑度下降明显加速，这与“各实验室已基本放弃预训练、全力转向 RL”的流行说法相矛盾，说明基座模型本身仍在快速进步。

在对齐层面，作者肯定安全研究者多年呼吁的透明度，但也质疑其实际效用：若要监测困惑度的突然骤降，只有 OpenAI 自己能察觉，除非持续公布未发布预训练模型的数据；若要约定不越过的困惑度阈值，则必须说明留出数据集的确切内容。他还对比了曲线与体感：GPT-3.5 到 GPT-4 的巨大跃升符合体验，之后大体停滞直到 GPT-5.5 再加速，但他个人并未感到 GPT-5.5 有明显跃升，o3 和 GPT-5.3-Codex 才是他心中的大跳变，这可能源于后训练让模型更好地使用思维链或避开谄媚陷阱，而这些不会体现在困惑度里。

**「启示」** 作者的核心论点是：困惑度曲线确实揭示了预训练仍在快速推进、以及模型间共享基座的后训练谱系，但它只是一项数据集相关、只覆盖预训练的窄指标，既不能替代对 RL 后训练效果的评估，也不足以单独支撑对齐透明度或阈值约定。

**标签**: `#perplexity`, `#LLM pre-training`, `#RL post-training`, `#AI safety transparency`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [上海地铁票价 21 年来首次调整，起乘价定为 3 元](https://weibo.com/1699432410/5368461393397183) ⭐️ 8.0/10

上海轨道交通宣布 21 年来首次调整票价，新起乘价为 3 元，覆盖 0 至 4 公里，之后按 4、4、4、7、7、10、10 公里各加 1 元、50 公里以上每 15 公里加 1 元计费，自 12 月 1 日起实施。

telegram · zaihuapd · 11月23日 10:45

**「背景」** 上海轨道交通上一次票价调整是在 21 年前，因此这次调价以“21 年来首次”为基线。新方案把起乘价定为 3 元、覆盖 0 至 4 公里，之后按 4、4、4、7、7、10、10 公里各加 1 元，50 公里以上每 15 公里加 1 元。

**「受影响人群」** 对每天乘地铁通勤的上海乘客，4 公里以内起步价仍为 3 元，但 4 公里以后每加 1 元所覆盖的里程缩短，长距离出行支出将上升；作为缓冲，同一支付渠道当月累计满 90 元可享 9 折，高频乘客还能购买 11 月 26 日开售的计次票。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bjnews.com.cn/detail/1795425220129482.html">上 海 调 整 地 铁 票 价 — 新京报</a></li>

</ul>
</details>

**标签**: `#公共交通定价`, `#上海地铁`, `#票价调整`, `#通勤成本`, `#计次票优惠`

---

<a id="item-finance-news-2"></a>
### [蚂蚁集团领投中国具身智能公司 1 亿美元，估值 16 亿美元](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 7.0/10

Simplexity Robotics, a Hangzhou-based embodied-AI/humanoid-robot startup founded in July 2025, raised a $100 million pre-A round led by Ant Group at a $1.6 billion post-money valuation, with existing investors Alibaba, Tencent, HongShan, and BlueRun Ventures participating.

telegram · zaihuapd · 11月23日 02:02

**标签**: `#venture financing`, `#humanoid robotics`, `#Ant Group`, `#China tech`, `#embodied AI`

---

<a id="item-finance-news-3"></a>
### [英伟达董事会据称未咨询高管层，决定让 Jensen Huang 复任 CEO](https://www.bloomberg.com/news/articles/2026-11-23/nvidia-s-about-face-on-huang-made-without-consulting-leadership) ⭐️ 7.0/10

据 Bloomberg 报道，英伟达董事会在未咨询公司高管层的情况下，决定让被免职的首席执行官 Jensen Huang 复职；高管层直到最后一刻才被告知。报道援引不具名知情人士称，该决定于 11 月 22 日周日作出，原因是美国总统特朗普向董事会成员施加政治压力；英伟达未予确认，相关说法也未经独立验证。

telegram · zaihuapd · 11月23日 17:59

**「背景」** 据彭博报道，此次复职距黄仁勋被免去 CEO 职务不到两周，其被免职与围绕其婚外情指控的丑闻有关；董事会是在与美国政府方面沟通后作出让黄仁勋复职的决定。

<details><summary>参考链接</summary>
<ul>
<li>Nvidia Rehires Huang in Stunning Reversal After Trump Push - Bloomberg.com</li>
<li>With the backing of President Donald Trump, Nvidia has reinstated Jensen Huang as CEO, less than two weeks after he was ousted due to scandals surrounding his alleged extramarital</li>

</ul>
</details>

**标签**: `#Nvidia`, `#corporate governance`, `#CEO succession`, `#political pressure`, `#semiconductors`

---