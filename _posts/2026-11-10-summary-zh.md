---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10
lang: zh
---

> 从 46 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [Claude Fable 5.2 与 Mythos 5.2 引发 HN 讨论](#item-tech-news-1) ⭐️ 7.0/10
2. [Meta Research 推出小型高效模型 Muse Ember](#item-tech-news-2) ⭐️ 7.0/10
3. [watched.earth：回溯一周内飞越某地的卫星影像](#item-tech-news-3) ⭐️ 7.0/10
4. [e-means 声称以十分之一轮次超越 k-means](#item-tech-news-4) ⭐️ 7.0/10
5. [LingBot-Touch：潜空间预测在触觉预训练中胜过重建](#item-tech-news-5) ⭐️ 7.0/10
6. [SwarmEvolve 用潜空间智能体集群加速数学优化](#item-tech-news-6) ⭐️ 7.0/10
7. [谷歌发布 TPU 8tx 与 TPU 8i Max，扩展对英伟达的挑战](#item-tech-news-7) ⭐️ 7.0/10
8. [泄露草案：欧盟拟以《数字公平法案》限制成瘾性设计与游戏虚拟货币](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [中国继续暂停对美 24%加征关税两个月，保留 10%税率](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude Fable 5.2 与 Mythos 5.2 引发 HN 讨论](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 7.0/10

Hacker News 的讨论围绕 Anthropic 的 Claude Fable 5.2 与 Mythos 5.2 展开，但所给材料没有公告正文，因此版本可用性、兼容性和官方基准都无法核实。一段被引用的公告段落称，1,000 个 Fable 5.2 智能体在 30 小时内完成费马大定理的形式化，几乎无需人工干预；同一说法称，此前未发布的研究版耗时 11 天，并依赖专用工具链和人类研究者指导。评论者质疑基准比较的公平性，包括为何用 Fable xHigh 对比 Carbon Med、为何主要定位为网络安全模型的 Carbon 未出现在唯一的网络安全基准对比中，以及为何 robodojo 改用 Argon 对比。另有评论者怀疑 5.5 是为准备新版本而被人为削弱。

hackernews · meetpateltech · 11月9日 18:56 · [社区讨论](https://news.ycombinator.com/item?id=50429906)

**「背景」** Anthropic 此次沿用同一底层模型的两种配置发布方式：按其系统卡说明，Fable 5.2 面向一般使用，并在生物学、网络安全等高风险两用领域附加防护措施，Mythos 5.2 为另一种配置。迁移指南给出的模型 ID 为 claude-fable-5-2（Amazon Bedrock 上为 anthropic.claude-fable-5-2），并指出自 Fable 5.1 起，每个 thinking 块仅对生成它时所用的系统提示、工具和对话历史有效，这一破坏性变更延续至 5.2。

**「对迁移与能力评估的影响」** 打算迁移的团队需要用自己的工作负载来验证，而不能直接照搬发布方的对比：有已上手的用户在讨论中表示，Fable 5.2 与 Opus 5.5 在日常任务上的差别很难分辨，只有把提示写得更激进时才看得出分工，另有人质疑对比中双方「努力等级」设置不对等、且被定位为网络安全模型的版本恰恰缺席唯一的网络安全基准。此外，所谓「形式化费马大定理」指的是用 Lean 完成并机器校验一个已知证明，而不是提出新的数学证明，评估这类自动化说法时应把范围限定在形式化与验证环节。

**「社区讨论」** 有评论者称，实际使用 Fable 5.2 时，普通任务与 Opus 5.5 差别不大，必须刻意把提示词的目标定得更高，才能看出明显差距。另一位在约 12.5 万行项目上使用 Opus 5.5 xhigh 的开发者则质疑，普通工作流是否真的需要 Fable/Mythos，而不是 Opus 5.5 就够用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf">Claude Fable 5.2 &amp; Claude Mythos 5.2 System Card</a></li>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-2/migration-guide">Claude Fable 5.2 and Claude Mythos 5.2 migration guide</a></li>
<li><a href="https://www.datastudios.org/post/claude-formalizes-fermat-s-last-theorem-11-days-of-autonomous-work-lean-verification-and-ai-for-a">Claude Formalizes Fermat ’ s Last Theorem : 11 Days of Autonomous...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI models`, `#model release`, `#automated theorem proving`

---

<a id="item-tech-news-2"></a>
### [Meta Research 推出小型高效模型 Muse Ember](https://research.meta.ai/blog/muse-ember) ⭐️ 7.0/10

Meta Research 宣布推出小型高效模型 Muse Ember，并将其定位为目前最小、最高效的模型。该模型提供 minimal、low、medium、high、xhigh、max 六档推理强度，但 Hacker News 评论者未找到公开权重，讨论中将其视为一次非开放权重发布。讨论还质疑基准测试的选择：有人指出，最亮眼的成绩出现在 mini-swe-agent 上，而不是 Meta 自有的 agent harness 上。

hackernews · dvaplima · 11月9日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=50429024)

**「背景」** Meta 将 Muse Ember 定位为其最小、最高效的模型，目标场景是工具调用、编码子任务、路由、抽取和长文档解析等高频智能体工作，并已在 Meta Model API 和 Muse Code 中提供。Artificial Analysis 将其归为 Meta 最新的高效档模型系列，输入与输出 token 定价与 Claude Haiku 5.5、GPT-6 Luna 相同，并在 max 与 xhigh 推理档位进入智能指数对单任务成本的前沿曲线。

**「影响」** 评论中引用的定价为每百万输入 token 0.10 美元、缓存输入 0.004 美元、输出 0.50 美元；若该定价准确，缓存输入仅为输入价的 4%，低于评论所称 Luna/Haiku 的 10%，对反复使用长上下文的调用方更有利。对希望本地部署或微调的团队来说，未开放权重是直接限制，只能等待权重发布或使用托管接口。

**「社区讨论」** 评论者用六档推理强度生成 SVG 的测试发现，更多推理 token 不一定带来更好结果；还有人指出最佳基准成绩来自 mini-swe-agent 而非 Meta 自有 harness，并对没有开放权重表示失望。另有评论引用每百万 token 0.10/0.50 美元的输入/输出定价，认为缓存输入仅为输入价 4% 这一点值得注意。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/meta/muse-ember">Muse Ember - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/articles/meta-s-muse-ember-is-the-cheapest-model-scoring-36-on-the-intelligence-index">Meta &#x27;s Muse Ember is the cheapest model scoring... | Artificial Analysis</a></li>
<li><a href="https://www.linkedin.com/showcase/meta-for-developers/">Meta for Developers | LinkedIn</a></li>

</ul>
</details>

**标签**: `#Meta AI`, `#small language models`, `#model efficiency`, `#reasoning models`, `#benchmarking`

---

<a id="item-tech-news-3"></a>
### [watched.earth：回溯一周内飞越某地的卫星影像](https://www.watched.earth/) ⭐️ 7.0/10

开发者 a585gupt 在 Hacker News 发布了开源浏览器工具 watched.earth：用户输入地点后，该工具基于 CelesTrak 目录、使用 SGP4 计算过去 7 天内飞越该地的卫星，并调取对应的 Sentinel-2、Landsat 和 NASA 影像。作者称轨道搜索在浏览器本地约半秒完成，并用暴力搜索在极点、反子午线和狭窄扫幅等边界条件下核对，结果为 0 漏检。作者还称已处理 Sentinel-2 时间戳与实际过境常相差 5-10 分钟的问题；工具只在存在真实影像时标注“watched”，且不存储用户位置。源代码已在 GitHub 发布。

hackernews · a585gupt · 11月9日 17:51 · [社区讨论](https://news.ycombinator.com/item?id=50428907)

**「背景」** SGP4 是常用的轨道传播模型，可根据 CelesTrak 提供的两行根数（TLE）推算卫星在特定时刻的位置。Sentinel-2、Landsat 和 NASA 的对地观测任务会公开部分影像，因此把轨道经过计算与影像目录检索结合，才能判断某地是否真的被拍到。

**「影响」** 对于想核实自家街区或某片区域被哪颗卫星拍到的人，这个工具能按地点和时间范围列出相应影像；但结果取决于这些卫星是否实际拍摄并发布了影像，未覆盖或未发布时就不会有可用结果。开源代码也便于开发者复用轨道搜索或补充新的影像数据源。

**「社区讨论」** 评论区对实际效果评价不一：一位自称从事地理空间工作的用户认为，能查看卫星实际拍摄的影像很有用，另有评论称赞想法和执行；同时有人批评页面文案像是用 LLM 生成，并报告地点输入框存在光标与字符间距异常、难以输入的问题。

**标签**: `#satellite-tracking`, `#orbital-mechanics`, `#GPU-rendering`, `#geospatial-imagery`, `#open-source`

---

<a id="item-tech-news-4"></a>
### [e-means 声称以十分之一轮次超越 k-means](https://e-means.github.io/) ⭐️ 7.0/10

一个名为 e-means 的聚类项目声称，只需 k-means 约十分之一的迭代轮次就能取得更好的聚类结果，并将其定位为 k-means 的替代方案。Hacker News 上的讨论既有人把该方法适配到 GPU 上的 IVF 索引并报告 146 倍加速，也有人在实际替换 Lloyd 算法时发现并不适用。现有材料主要来自项目自述和社区讨论，尚缺少同行评审或完整独立基准来确认这些加速结论的普遍性。

hackernews · porridgeraisin · 11月9日 18:45 · [社区讨论](https://news.ycombinator.com/item?id=50429734)

**「背景」** k-means（Lloyd 算法）交替执行“把每个点分配给最近的质心”和“按簇重算均值”两步，需要对数据做多轮遍历，实践中常通过并行化来加速。e-means 项目自称是 Meta FAIR 开发并开源的 k-means 变体，主张用约十分之一的迭代轮数（epochs）取得可比结果。

**「影响」** 若“减少轮次或数据遍历”的优势在目标负载上成立，最直接的受益者是需要对海量数据反复扫描的聚类任务；但 jlhawn 的实测表明，在球面等面积网格松弛这类迭代成本结构不同的场景中，e-means 并不更好，采用前应针对具体数据和硬件复现基准。

**「社区讨论」** 讨论中的核心分歧是适用场景：real\_faxenoff 称将其适配到自己的 IVF 索引后，在 GPU 上获得 146 倍加速，而 jlhawn 在球面网格松弛中实测效果不如 Lloyd 算法。shiandow 则尝试从期望最大化或模拟退火的角度理解该更新规则，并指出质心保持在凸包内这一性质很重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://e-means.github.io/">Modern optimization and scaling laws for k - means clustering</a></li>
<li><a href="https://pastel.hal.science/tel-00744768v1/file/texfiles@DistributedKMeans@ParallelKMeansPhD.tex">Introduction to clustering and distributed Batch K - Means</a></li>

</ul>
</details>

**标签**: `#k-means`, `#clustering`, `#algorithms`, `#machine-learning`, `#performance`

---

<a id="item-tech-news-5"></a>
### [LingBot-Touch：潜空间预测在触觉预训练中胜过重建](https://www.reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for/) ⭐️ 7.0/10

一篇 Reddit 帖子介绍的 Robbyant 论文称，其 JEPA 式自监督触觉编码器 LingBot-Touch 用潜空间预测替代原始信号重建，并已公开推理代码和检查点。与同尺寸的 MAE、VAE 重建模型相比，在 1K 小时数据上，触觉到视频的 top-5 召回率分别为 32.1%、5.6% 和 4.4%；到 4K 小时，JEPA 升至 49.3%，MAE 仍低于 9%，VAE 反降至 3.1%。作者将重建方法的弱势归因于触觉片段大量近零背景，使重建损失可以在不学习实际接触的情况下下降。训练把掩码比例在 300 步内从 40% 升到 80%，并将磁、压阻和视触觉三类传感器经规范指尖坐标与 5D RoPE（时间、手指、3D 位置）送入共享 Transformer。在 26 个真实机器人任务、4 种策略的 104 个组合中，冻结编码器特征在 89 个组合中得分最高；在预训练未见的磁触觉手上，LingBot-VLA 从 57.21 提升到 75.04。

reddit · r/MachineLearning · /u/Zealousideal-War7154 · 11月9日 18:52

**「背景」** LingBot-Touch 是 Robbyant（蚂蚁集团）开源的 JEPA 式触觉基础模型，采用共享 Haptic Transformer，从时空触觉上下文中预测潜在表示而非重建原始信号，并已以 Apache 2.0 许可公开推理代码与冻结目标编码器。JEPA 与 MAE、VAE 的关键区别在训练目标：后两者直接重建被掩码的输入，前者则在隐空间预测目标表示，因此把二者放在同一触觉数据上比较正是这篇论文要回答的问题。

**「影响」** 对触觉表征研究和机器人团队而言，直接的行动项是使用公开的推理代码与检查点复现该编码器，并在自有多传感器数据上优先测试冻结特征；报告显示冻结特征在 89/104 个策略-任务组合中最佳。评估时还应保留同尺寸的 MAE/VAE 重建基线，因为近零背景可能让重建损失下降却不代表学到接触表征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Robbyant/lingbot-touch">GitHub - Robbyant/lingbot-touch: Learning Heterogeneous ...</a></li>
<li><a href="https://technology.robbyant.com/lingbot-touch">LingBot-Touch Tactile Foundation Model - Robbyant</a></li>
<li><a href="https://agihunt.info/en/p/1a1c20d6d7c43e4b3f2845b66f2">Ant Group&#x27;s Robbyant open-sources LingBot Touch… · AGI Hunt</a></li>

</ul>
</details>

**标签**: `#self-supervised learning`, `#tactile sensing`, `#robot manipulation`, `#JEPA`, `#representation learning`

---

<a id="item-tech-news-6"></a>
### [SwarmEvolve 用潜空间智能体集群加速数学优化](https://www.reddit.com/r/MachineLearning/comments/1xrunu7/using_latentagent_swarms_for_math_discovery_and/) ⭐️ 7.0/10

Reddit 用户 /u/QileHQ 发布了 SwarmEvolve，一个面向数学发现与优化的潜空间智能体集群框架。发帖者称，在 Qwen3 8B、14B 和 32B 上运行数百个不写出显式推理过程的智能体，并通过相互传递 KV 缓存来混合思路，约 5 分钟即可达到 OpenEvolve、ShinkaEvolve 和 CodeEvolve 需要 1 小时以上才达到的分数；仅用 8B 模型还追平了已知最佳圆堆积结果。该框架据称已扩展到 Qwen3.5 和 Muse 模型，但相关论文和代码尚未经过同行评审或独立复现，代码链接仍标注为“available soon”。

reddit · r/MachineLearning · /u/QileHQ · 11月9日 15:30

**「背景」** 这类“进化式”程序搜索由 Google DeepMind 的 AlphaEvolve 推广开来：让 LLM 生成候选程序、由评测器打分、再迭代改写，其成果之一是找到了比 1969 年以来保持的纪录更快的 4×4 复数矩阵乘法算法。但 AlphaEvolve 依赖 Gemini 模型，OpenEvolve、ShinkaEvolve、CodeEvolve 等开源实现普遍更慢、更贵。SwarmEvolve 所借鉴的 LatentMAS 思路是让智能体不把推理过程写成文本，而是在潜空间中推理并把 KV cache 直接传给其他智能体，以削减每轮生成开销；据 alphaXiv 页面，该工作来自 Brown University，主打用一块 GPU 上的小模型集群替代前沿模型。

**「复现与部署的前提条件」** 对想直接使用该框架的开发者来说，最现实的约束是代码尚未放出：帖子只给出 GitHub 链接并注明 &quot;available soon&quot;，因此 5 分钟对 1 小时以上的加速比、以及 8B 模型追平已知最优圆堆积结果等说法目前无法独立验证，只能等仓库公开后复现。另一个部署层面的限制来自方法本身：LatentMAS 式的代理间通信以 Transformer KV 缓存状态作为消息载体，这意味着参与交换的代理需要共享同一套模型权重与推理栈，实际使用更可能落在自托管的同构集群上，而不是混用不同厂商的 API 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/">Explore | alphaXiv</a></li>
<li><a href="https://arxiv.org/html/2604.13349v1">When Less Latent Leads to Better Relay: Information-Preserving...</a></li>
<li><a href="https://www.emergentmind.com/papers/2511.20639">Latent Collaboration in Multi- Agent Systems</a></li>

</ul>
</details>

**标签**: `#LLM evolutionary optimization`, `#latent reasoning`, `#multi-agent systems`, `#math discovery`, `#open-source models`

---

<a id="item-tech-news-7"></a>
### [谷歌发布 TPU 8tx 与 TPU 8i Max，扩展对英伟达的挑战](https://www.bloomberg.com/news/articles/2026-11-09/google-escalates-nvidia-rivalry-with-new-versions-of-its-tpu-systems) ⭐️ 7.0/10

谷歌宣布推出两款新的张量处理单元：TPU 8tx 和 TPU 8i Max，分别面向安全敏感场景和超长上下文 AI 应用。TPU 8tx 主要服务政府机构及受严格监管行业，用于处理机密数据，并将与 AMD 芯片协同工作；TPU 8i Max 则把两颗 TPU 集成在同一封装内，以提供更强算力和更大内存容量。谷歌正打破过去每两年推出一款新处理器的节奏，转而针对不同场景扩充 TPU 产品线，并借助苹果、Meta、甲骨文和 Anthropic 等客户，把 TPU 打造为英伟达 GPU 之外的选择；目前公布的信息未包含性能基准或上市时间。

telegram · zaihuapd · 11月9日 13:36

**「背景」** 谷歌的 TPU 已发展到第八代；这一代此前先推出了面向大规模基础模型训练的 TPU 8t，以及与 TPU 8t 一起构成这一代产品基础的 TPU 8i。此次新增的 TPU 8tx 和 TPU 8i Max 把第八代产品线扩展到四个型号，分别面向安全推理和超大上下文场景。

**「影响」** 对需要超长上下文推理的团队而言，谷歌宣布的 TPU 8i Max 把两颗 TPU 集成在同一封装内以提供更大算力和内存，是一个可纳入评估的扩容选项；但谷歌未公开定价，且目前只有架构说明、缺少独立基准，生产迁移前应先确认可用区域和软件支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/">Introducing TPU 8 tx and TPU 8 i Max</a></li>
<li><a href="https://bingx.com/en/flash-news/post/google-adds-tpu-tx-and-tpu-i-max-expanding-eighth-gen-lineup-to-four">Google Adds TPU 8 tx and TPU 8 i Max , Expanding Eighth-Gen Lineup...</a></li>
<li><a href="https://www.techpowerup.com/354620/google-extends-tensor-processor-unit-series-with-tpu-8tx-and-8i-max">Google Extends Tensor Processor Unit Series with TPU 8 tx and 8 i Max</a></li>
<li><a href="https://jimmyresearch.com/entities/google-tpu/">Google TPU — jimmy·research</a></li>

</ul>
</details>

**标签**: `#TPU`, `#Google`, `#AI hardware`, `#Nvidia competition`, `#AI infrastructure`

---

<a id="item-tech-news-8"></a>
### [泄露草案：欧盟拟以《数字公平法案》限制成瘾性设计与游戏虚拟货币](https://www.mlex.com/mlex/articles/2546584/digital-businesses-face-addictive-design-controls-under-draft-eu-consumer-law) ⭐️ 7.0/10

一份泄露的草案显示，欧盟《数字公平法案》拟要求数字企业允许用户关闭自动播放、连续使用奖励等诱导强迫或过度使用的功能，并针对在线订阅规定取消按钮、续费提醒和人工客服，且在免费试用转为付费订阅前须取得用户明确同意。草案还拟禁止面向未成年人的游戏付费抽奖、“付费获胜”和画像广告，并要求游戏虚拟货币标明真实币值。违规企业最高可被处以全球营业额的 6% 罚款。欧盟委员会计划于 11 月 11 日提交该法案并同步改革消费者保护合作框架，但两项提案均需欧洲议会与欧盟各国政府同意才能生效；目前内容来自泄露草案，并非已生效法律，最终条款与时间仍存不确定性。

telegram · zaihuapd · 11月9日 16:42

**「背景」** 所谓“暗黑模式”是指通过界面和流程设计诱导用户做出非本意选择，例如虚假通知、免费试用悄然转为付费订阅，以及难以取消的订阅。Euronews 根据泄露草案报道，欧盟委员会拟在《数字公平法案》中点名并禁止十类此类操纵性设计；TechTimes 则指出，该提案已列入欧委会 11 月 11 日会议议程，可能把针对暗黑模式、成瘾性设计和订阅陷阱的限制写入欧盟消费者法。

**「合规改造压力」** 对面向欧盟市场的游戏和订阅服务，最直接的后果是商城标价与用户流程需要重做：游戏内货币要能换算并显示真实币值，面向未成年人的付费抽奖、付费获胜和画像广告要移除，订阅则需提供取消按钮、续费提醒并在试用转付费前取得明确同意。由于草案尚未生效且仍需欧洲议会与成员国批准，企业应把它当作可能落地的合规基线来评估改造范围，而不是已确定的执法期限；若按草案通过，最高可达全球营业额 6%的罚款会放大这一优先级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/330286/20261109/eu-dark-patterns-law-listed-wednesday-digital-fairness-act-targets-firms-platform-rules-miss.htm">EU Dark Patterns Law Listed for Wednesday: Digital Fairness ...</a></li>
<li><a href="https://www.euronews.com/2026/11/09/eu-to-blacklist-ten-manipulative-online-design-traps-leaked-draft-shows">EU to blacklist ten online design &#x27;traps&#x27;, leaked draft shows</a></li>

</ul>
</details>

**标签**: `#EU regulation`, `#dark patterns`, `#game monetization`, `#consumer protection`, `#subscription traps`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国继续暂停对美 24%加征关税两个月，保留 10%税率](https://mp.weixin.qq.com/s/nNxJB3y0YA_2zJvOK6onUQ) ⭐️ 7.0/10

中国国务院关税税则委员会公告，经国务院批准，自 2026 年 11 月 10 日 13 时 01 分起，在两个月内继续暂停实施 24%的对美加征关税税率，保留 10%的加征关税税率。公告称，此举是为落实中美两国元首华盛顿会晤达成的成果共识，依据关税法、海关法、对外贸易法等法律法规作出。

telegram · zaihuapd · 11月9日 04:03

**「背景」** 这 24%并非新增税负：中国此前已将对美加征关税从 34%下调至 10%，剩余 24%以限期暂停的方式搁置，并先后按 90 天、一年等不同期限延长。此次公告由国务院关税税则委员会发布，该委员会是负责拟定关税税则与税率的国务院机构。

**「对进口商的影响」** 对从美国进口原材料和商品的中国企业来说，未来两个月内 24%的加征关税继续不征收、只保留 10%，进口税负维持现状；但此前同类暂停多为 90 天，此次为期两个月，期满后是否延续尚无公告，相关企业的采购与定价安排可能需随政策节点重新调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://stmtest.migage.com/news/yeeyi/details/2857470">国 务 院 关 税 税 则 委 员 会 ：在一 年 内 继 续 暂 停 实施 24 ...</a></li>
<li><a href="https://www.douyin.com/zhuanti/7562027068574173194">中 美 继 续 暂 停 实施相互 24 % 关 税 - 抖音</a></li>
<li><a href="https://www.gladcc.com/article/1924365739924140034">中 美 日内瓦联合声明 对 经济和市场的 影 响 _文章_GladCC</a></li>
<li><a href="https://www.douyin.com/zhuanti/7562027068574173194">中 美 继续 暂 停 实施相互 24 % 关 税 - 抖音</a></li>

</ul>
</details>

**标签**: `#China-US trade`, `#tariffs`, `#trade policy`, `#customs`, `#macroeconomic policy`

---