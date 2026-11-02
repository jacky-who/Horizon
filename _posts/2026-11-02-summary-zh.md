---
layout: default
title: "Horizon Summary: 2026-11-02 (ZH)"
date: 2026-11-02
lang: zh
---

> 从 45 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [Astra 据称可直接改写 Qwen 权重以修复循环](#item-tech-news-1) ⭐️ 8.0/10
2. [ChatGPT 分享链接漏洞可致账号接管，OpenAI 已修复](#item-tech-news-2) ⭐️ 8.0/10
3. [vLLM v0.33.0rc3 候选版发布：CUDA 13.0 与 ROCm 10.0 成默认](#item-tech-news-3) ⭐️ 7.0/10
4. [SGLang v0.5.23 发布：多模型集成与低延迟内核](#item-tech-news-4) ⭐️ 7.0/10
5. [Ubuntu LTS 内核近三周未修复 CVE-2026-98432](#item-tech-news-5) ⭐️ 7.0/10
6. [SemiAnalysis 发布 GDPx 前沿智能体基准](#item-tech-news-6) ⭐️ 7.0/10
7. [LightMIS：13.1 万参数医学分割模型，Mali-G52 上快 10.5 倍](#item-tech-news-7) ⭐️ 7.0/10
8. [LongCat-2.5 发布 1.6 万亿参数原生多模态模型](#item-tech-news-8) ⭐️ 7.0/10
9. [WIRED：400 多款 AI 应用被指暗藏色情深伪功能](#item-tech-news-9) ⭐️ 7.0/10
10. [阿布扎比与 OpenAI 签署四项协议](#item-tech-news-10) ⭐️ 7.0/10

**科技博客**
1. [LLM 直接编辑权重并非超人能力](#item-tech-blog-1) ⭐️ 7.0/10
2. [LLM 对齐为何在原则上不可能](#item-tech-blog-2) ⭐️ 7.0/10
3. [受众捕获：参与度指标如何替换你真正想要的读者](#item-tech-blog-3) ⭐️ 6.0/10

**财经新闻**
1. [Anthropic 更新招股书：前三季度营收 332 亿美元，净亏损 1040 亿美元](#item-finance-news-1) ⭐️ 8.0/10
2. [甲骨文拟发行 200 亿美元股票与债券，股价午盘跌 6%](#item-finance-news-2) ⭐️ 7.0/10
3. [盘前异动：雅诗兰黛业绩超预期，Marvell 拟以 1150 亿美元收购 Lumentum](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Astra 据称可直接改写 Qwen 权重以修复循环](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 8.0/10

一篇博客文章和随后的 Hacker News 讨论声称，Astra 能直接读取并编辑 Qwen 的权重，而不只通过提示词或外部工具影响模型。讨论中引述的案例称，Astra 把一个小型推理模型的循环归因于第 15、19 层 MLP 写出的一个方向，并从这两层各 64 个输出列（合计 131,072 个权重）中减去该方向，减少了重复输出；相关编辑还被报告用于改善数学表现。上述说法目前仅来自作者博客和社区转述，尚无独立复现或同行评审验证，应视为待验证的能力声明。

hackernews · dbreunig · 11月2日 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50341174)

**「背景」** 所谓“权重空间编程”，是指让通用大模型直接读取并改写另一个网络的权重，不经过优化器，也不是由编译器把程序编译成权重。过去权重主要来自 Adam、Muon 等优化过程，或由专门网络生成；Astra 的演示把这一思路放到 Qwen 这类具体模型上，因此需要先区分“直接改权重”与常规训练、微调的不同。

**「影响」** 如果该结果可复现，开发者修复小型模型的循环问题可能只需对特定层做定向权重编辑，而不必重新训练；但在独立验证出现前，这些层号和权重数量不能直接迁移到其他 Qwen 版本或任务。

**「社区讨论」** 评论者对 LLM 是否“原生理解”自身权重展开争论：有评论者称 Astra 无需工具即可判断小型网络的训练任务并手改 Qwen 提升数学能力，另一些人则认为生成或预测网络权重的研究早已存在，因此结果虽惊人却并非完全出乎意料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/weight-space-programming-gpt-6-astra-edits-qwen3-5-0-8b-weights-math-7-9-to-48-1-mit-csail-2026">GPT-6 Astra Edits Qwen Weights: MATH-500 7.9% to 48.1% ...</a></li>
<li><a href="https://elsolitario.org/en/2026/11/02/mit-csail-astra-edits-0-016-of-qwen3-weights/">Weight-Space Programming: How Astra Edits Weights</a></li>

</ul>
</details>

**标签**: `#LLM weight editing`, `#mechanistic interpretability`, `#Qwen`, `#model steering`, `#AI research`

---

<a id="item-tech-news-2"></a>
### [ChatGPT 分享链接漏洞可致账号接管，OpenAI 已修复](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

OpenAI 已修复一个 ChatGPT 分享链接漏洞：Parameter 研究团队称，攻击者可在已登录用户的会话中执行代码，读取私密对话并发送至外部服务器。受害者只需打开恶意链接，无需安装应用；问题出在预览功能与图表组件之间的消息处理缺陷。OpenAI 于 10 月 26 日完成修复，将其定级为 P1，并支付 5000 美元赏金。

telegram · zaihuapd · 11月2日 10:24

**「背景」** ChatGPT 的分享链接用于把一段对话以可浏览的页面形式公开给他人，页面会渲染对话中的富内容组件（例如图表预览），而不仅是纯文本。此次漏洞正出在预览功能与图表组件之间的消息处理环节：分享页需要在不被信任的内容与宿主页面之间传递消息，一旦校验不严，恶意链接就能在已登录用户的会话上下文中执行代码。

**「影响」** 对 ChatGPT 用户而言，这类分享链接的风险在于仅打开链接就可能泄露当前会话中的私密内容；即使漏洞已修复，处理外部分享链接和富内容预览时仍需按不可信输入隔离。

**标签**: `#ChatGPT`, `#security vulnerability`, `#account takeover`, `#OpenAI`, `#data exfiltration`

---

<a id="item-tech-news-3"></a>
### [vLLM v0.33.0rc3 候选版发布：CUDA 13.0 与 ROCm 10.0 成默认](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 7.0/10

vLLM 发布 v0.33.0rc3 候选版本，发布说明按 v0.33.0 列出 927 个提交、389 名贡献者，并新增 Reflection Beam-1.0、Yandex AliceAI-Foundation-80B-A3B、Recursive Flint 等模型支持。运行时栈升级到 PyTorch 2.14.0、torchvision 0.29.0 和 Triton 3.8.0；CUDA wheel 与镜像只提供 CUDA 13.0，CUDA 12.9 的 wheel 及 -cu129 镜像不再发布。ROCm 默认镜像和 wheel 迁移到 ROCm 10.0，ROCm 7.2 仍以 -rocm72 标签提供。破坏性变更包括移除 Medusa 和 MLP speculator、移除旧版 Ray 编译图执行器，以及暂停生成期间的新请求返回 HTTP 503。

github · khluu · 11月2日 10:10

**「背景」** vLLM 是面向大模型推理与服务的引擎，用户通常通过预编译 wheel 或容器镜像，按底层加速栈（CUDA、ROCm、XPU）选择对应版本安装。此次 rc3 是 0.33.0 的候选发布，发布说明中的 PyTorch/CUDA 版本调整和破坏性变更会直接影响现有部署的升级路径；正式产物与兼容性仍需以最终发布为准。

**「影响」** 使用 CUDA 12.9 的生产环境需要切换到 CUDA 13.0 工件或继续留在旧版 vLLM；使用 NIXL 连接器的部署需升级到 NIXL 1.5 以上；依赖 Medusa/MLP speculator 的推理配置也需迁移，因为相关实现已被移除。

**标签**: `#vLLM`, `#LLM inference`, `#PyTorch`, `#CUDA`, `#release notes`

---

<a id="item-tech-news-4"></a>
### [SGLang v0.5.23 发布：多模型集成与低延迟内核](https://github.com/sgl-project/sglang/releases/tag/v0.5.23) ⭐️ 7.0/10

SGLang 发布 v0.5.23，包含来自 257 位贡献者的 1007 个 PR，并新增 Muse Spark Open、MiniMax-M3.1-Flash、MiniCPM-V 4.7 以及 FLUX.3 Image Klein 等 LLM、VLM 和扩散模型支持。发布说明称，DeepSeek-V4.1 在 GB300 上处理 32K 至 64K 提示时，负载下预填充吞吐最高提升 1.5 倍，首 token 延迟降低约 28%；可选的 NVIDIA megakernel 与 AMD monokernel 低延迟模式使单用户解码在 GB300 上最高快 44%、在 MI350X 上最高快 75%。新增可选的 Paged Experts，可在单张消费级 GPU 上运行大于显存的 MoE 模型，发布说明称其比 CPU offload 快至多 30 倍；同时通过 SGLang-TorchTPU 插件支持 Google TPU7x，并允许在 FP8 和 NVFP4 量化 MoE 模型上服务 LoRA 适配器。用户可通过 \`uv pip install --prerelease=allow sglang==0.5.23\` 或对应的 NVIDIA、AMD、Intel 及 TPU Docker 镜像升级。

github · Fridge003 · 11月2日 22:14

**「背景」** SGLang 是开源的大模型推理与服务框架，用户可通过 Python 安装包或按硬件平台提供的容器镜像部署。v0.5.23 是在既有功能上的增量版本，升级时需要按所用平台切换到对应的 0.5.23 镜像或安装包。

**「影响」** 对计划升级的部署者来说，主安装命令需要加上 \`--prerelease=allow\`；Docker 镜像按 NVIDIA CUDA 13、AMD MI35x/MI30x、Intel GPU/CPU 分开，TPU7x 则使用 \`lmsysorg/sglang:v0.1.0-tpu\` 标签，而不是 v0.5.23 标签。低延迟内核、Paged Experts 和量化 MoE 上的 LoRA 引擎均为可选功能，需要显式启用，因此默认路径不会自动获得这些加速或能力。

**标签**: `#SGLang`, `#LLM serving`, `#open source`, `#release notes`, `#model support`

---

<a id="item-tech-news-5"></a>
### [Ubuntu LTS 内核近三周未修复 CVE-2026-98432](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) ⭐️ 7.0/10

据该报道，Ubuntu LTS 内核在近三周内仍未发布针对关键 Linux 远程代码执行漏洞 CVE-2026-98432 的补丁，受影响系统仍处于未修复状态。现有材料没有提供漏洞触发条件、受影响内核版本列表或已确认的在野利用证据，也没有 Ubuntu 对延迟原因的官方说明。因此，补丁缺失是报道中的状态，实际风险与适用范围仍需以 Ubuntu 后续公告和独立验证为准。

hackernews · majorchord · 11月2日 18:39 · [社区讨论](https://news.ycombinator.com/item?id=50341462)

**「背景：CVE-2026-98432 的修复时间线」** CVE-2026-98432 是 Linux 内核 IPv4 TCP 握手处理中的远程释放后使用（use-after-free）漏洞，第三方汇总给出的 CVSS 评分为 9.8，上游修复已于 10 月 15 日合入。据同一汇总，Red Hat 已在 11 月 1 日发布修复内核，而 Ubuntu 尚未发布，这正是本次报道所指的差距；由于条目本身没有提供技术细节，上述时间线来自外部汇总，而不是原始公告。内核补丁通常要在更新并重启进入新内核后才会生效，且不同 Ubuntu 发行版与内核分支的修复状态需要分别核对。

**「实际影响与缓解选项」** 在补丁仍未进入 Ubuntu LTS 正式软件源期间，运维者只能自行选择权宜方案：其一是启用 proposed 软件源（即预发布仓库）获取较新内核，其二是套用 Red Hat 针对 CVE-2026-98432 发布的 nftables 规则；但 Red Hat 自己说明该规则只能减少暴露面、无法完全阻止攻击，而且 Ubuntu 尚未给出对应的缓解说明。公开利用代码的可得性仍不明确：有来源称已有公开的 PoC 参考与代码，另一来源则表示漏洞演示由 Anthropic 撰写、利用代码未公开。因此在补丁进入正式源之前，管理员需要自行验证缓解措施是否有效。

**「社区讨论」** 评论区的核心分歧在风险与应对：pelagicAustral 称未见在野利用，自己至少有 20 台服务器未打补丁，但认为风险被夸大且存在多种缓解；majorchord 则指出 Ubuntu 未给出缓解说明，RHEL 的缓解措施也自称不能完全阻止漏洞。sivakon 称最新 LTS 可从 proposed pocket 获取修复，但这是社区提供的线索，并非材料中 Ubuntu 的正式公告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf">Linux &#x27;s October 2026 TCP Use-After-Free: CVE - 2026 - 98432 — Atlas</a></li>
<li><a href="https://nolimitcloud.eu/blogs/security/cve-2026-98432-linux-ipv4-uaf">CVE - 2026 - 98432 : Linux IPv4 TCP Use-After-Free... | NolimitCloud</a></li>
<li><a href="https://www.thehackerwire.com/vulnerability/CVE-2026-98432/">CVE-2026-98432: Use-After-Free - PoC Available | TheHackerWire</a></li>
<li><a href="https://access.redhat.com/security/vulnerabilities/RHSB-2026-016">RHSB-2026-016 Use-after-free - kernel IPv4 (CVE-2026-98432 ...</a></li>
<li><a href="https://www.fosslinux.com/163418/cve-2026-98432-linux-tcp-use-after-free.htm">CVE-2026-98432: The Linux TCP Use-After-Free Flaw Explained</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#Ubuntu`, `#security vulnerability`, `#RCE`, `#patch management`

---

<a id="item-tech-news-6"></a>
### [SemiAnalysis 发布 GDPx 前沿智能体基准](https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities) ⭐️ 7.0/10

SemiAnalysis 发布 GDPx 基准，面向需要比较前沿智能体能力的评测用户，覆盖芯片设计、网络安全、生物、金融、法律、量化交易、递归自我改进、硬件设计、材料科学、对齐和软件工程 11 个高价值领域，并明确不纳入政府、房地产和保险。发布方称即使最佳模型也只有 12% 得分，认为按 GDP 份额或 O\*NET 职业分类构建通用基准不足以追踪前沿进展。文章还称 Opus 5.5 和 GPT-6 Astra 因安全分类器在网络安全、生物和对齐领域拉低总分，剔除这三项后结果会不同；这些均为 SemiAnalysis 自述结果，现有内容尚未展开具体评分方法或完整分数表。

rss · Semianalysis · 11月2日 01:51

**「背景」** 现有衡量通用能力的基准通常按行业对 GDP 的贡献或 SOC/O\*NET 职业分类来选取任务，试图覆盖整个经济。SemiAnalysis 认为这种口径会稀释前沿模型的真实进展，因为其判断是首万亿美元 AI 收入将集中于能高 ROI 部署前沿智能的少数行业。GDPx 因此改为围绕芯片设计、网络安全、生物学、金融、法律、量化交易和递归自我改进等高价值领域构建任务。

**「影响」** 对按领域选型的团队，GDPx 提示通用总分可能低估受安全分类器影响的模型：SemiAnalysis 称 Opus 5.5 与 GPT-6 Astra 在网络安全、生物和对齐上被压低分数，并称 Muse Wonder Full 是当前网络安全最强模型。采用该基准时应查看目标领域分项而非只看总分，同时注意这是发布方自建、方法细节尚未披露的评测。

**标签**: `#AI benchmarks`, `#frontier models`, `#agentic AI`, `#model evaluation`, `#SemiAnalysis`

---

<a id="item-tech-news-7"></a>
### [LightMIS：13.1 万参数医学分割模型，Mali-G52 上快 10.5 倍](https://www.reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image/) ⭐️ 7.0/10

作者在 Reddit 公开了 LightMIS，一个面向边缘设备的 2D 二值医学图像分割模型，仅有 131K 参数，并直接聚合多尺度编码器特征，不使用逐阶段学习的解码器。在与 nnWNet 相同的 nnU-Net v2.3.1 训练和评估协议下，作者报告其观测到的模态宏平均 Dice 和 IoU 与 nnWNet 接近，同时参数减少 98.14%、GFLOPs 减少 94.58%。作者还在搭载 Arm Mali-G52 MC2 GPU 的真实边缘设备上测试，称完整 LightMIS 比 nnWNet 约快 10.5 倍，所有 LightMIS 变体均实现 100% GPU 算子覆盖且无 CPU 回退；实验覆盖 6 个数据集和 5 种成像模态。论文为 arXiv 预印本，代码、检查点和复现细节已公开，但上述结果来自作者自述，尚未经过同行评审。

reddit · r/MachineLearning · /u/OkLion2068 · 11月2日 20:22

**「背景：nnU-Net 作为统一对比基线」** nnU-Net 是一种自配置的医学图像分割框架，会根据新数据集自动确定预处理、网络架构、训练与后处理设置，因此常被研究者当作强基线和方法开发框架使用。LightMIS 作者正是把 LightMIS 与包括 nnWNet 在内的参考模型都放在同一套 nnU-Net v2.3.1 流程下从零训练，覆盖六个数据集、五种成像模态，从而让参数量、GFLOPs 与边缘设备延迟的对比在同一实验协议内完成，而不是跨论文比较。

**「对边缘部署者的实际影响」** 对需要在低端边缘 GPU 上运行分割推理的开发者来说，可直接获取公开的代码与检查点，在自有的 2D 二分类分割任务上复现或试用，并以“是否出现 CPU 回退”作为部署可行性的关键检查项——作者报告全部 LightMIS 变体在 Mali-G52 MC2 上实现 100% GPU 算子覆盖、无 CPU 回退，这正是边缘推理延迟能否稳定的前提。需要注意的是，这些数字来自作者自述、尚未经同行评审，且范围限于 2D 二分类分割与六个数据集、五种成像模态，迁移到其他模态或三维任务前应自行验证精度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41592-020-01008-z">nnU-Net: a self-configuring method for deep learning-based ...</a></li>
<li><a href="https://github.com/MIC-DKFZ/nnUNet">GitHub - MIC-DKFZ/nnUNet</a></li>

</ul>
</details>

**标签**: `#medical image segmentation`, `#lightweight models`, `#edge AI`, `#model efficiency`, `#nnU-Net`

---

<a id="item-tech-news-8"></a>
### [LongCat-2.5 发布 1.6 万亿参数原生多模态模型](https://longcat.ai/blog/longcat-2.5/) ⭐️ 7.0/10

LongCat 团队发布 LongCat-2.5，这是一个总参数 1.6 万亿、每 token 激活约 480 亿的原生多模态模型，面向长程 agent 任务和 agentic coding，并在 LongCat-2.0 基础上强化视觉理解与编程能力。模型将视觉信号编码为多级离散 token，与文本统一处理，发布信息称其可完成视觉编程等任务。目前用户可通过官网试用并接入 API，但 GitHub 与 HuggingFace 版本尚未开放，发布方也未给出基准测试或独立验证结果。

telegram · zaihuapd · 11月2日 03:08

**「背景」** LongCat-2.5 是在 LongCat-2.0 基础上迭代而来，官方称其强化了视觉理解与 agentic coding。此次发布所说的“原生多模态”，具体是把视觉信号编码为多级离散 token，再与文本统一处理。

**「接入与部署影响」** 对需要私有化部署或本地微调的团队，LongCat-2.5 目前只能通过官网和 API 使用，GitHub 与 HuggingFace 版本尚未开放，架构设计需以托管调用为前提。发布材料未提供基准结果，因此在替换现有模型前，开发者应针对视觉编程和长程 agent 任务自行做对比评测。

**标签**: `#multimodal models`, `#large language models`, `#agentic coding`, `#model release`

---

<a id="item-tech-news-9"></a>
### [WIRED：400 多款 AI 应用被指暗藏色情深伪功能](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 7.0/10

WIRED 11 月 2 日报道，一个由 400 多个关联应用和网站组成的网络被指以宠物画像、语言学习等普通 AI 工具为掩护，在特定条件下提供色情深度伪造功能，允许用户上传他人照片生成露骨图像或视频。报道称，截至 9 月仍有 27 款相关应用在 Google Play 上架，累计下载超过 35 万次，不少标注为适合所有年龄；苹果在收到 WIRED 线索后下架 19 款，谷歌在被联系前已移除其中多数，Meta 表示已阻止 209 款相关应用投放广告。报道称相关开发者通过审核后替换远端网页内容来绕过审查，并依据中文代码、托管信息和域名等线索将网络与中文开发者及一家香港注册公司联系起来；报道明确将此视为调查判断，相关运营方未回应置评请求。

telegram · zaihuapd · 11月2日 12:45

**「背景」** 所谓“换脸色情”内容，是指未经当事人同意，用其照片生成露骨图像或视频。这类内容一直是应用商店和社交平台治理的重点。移动应用商店的审核通常发生在应用提交上架时，而应用之后从远端服务器加载的网页内容并不在初审范围内，这正是此类应用能长期隐藏功能的机制基础。

**「影响」** 对用户而言，看似普通的工具可能在特定条件下加载露骨深伪界面，而部分应用被标为适合所有年龄；对平台而言，审核通过后替换远端网页内容说明上架时的一次性审查无法覆盖后续功能变更，需要持续检查审核后的内容。

**标签**: `#deepfakes`, `#AI safety`, `#app store moderation`, `#platform abuse`, `#trust and safety`

---

<a id="item-tech-news-10"></a>
### [阿布扎比与 OpenAI 签署四项协议](https://thenextweb.com/news/openai-abu-dhabi-deals-machine-readable-government-mubadala) ⭐️ 7.0/10

阿布扎比与 OpenAI 签署了四项协议，覆盖“机器可读政府”、投资分析、面向阿联酋的模型部署以及能源行业应用。所谓“机器可读政府”，是把政策法规转为 AI 可读格式，帮助官员核查许可与证书申请，目前已在食品进口场景试点，官员保留最终决定权。穆巴达拉将与 OpenAI 及 G42 旗下 Inception42 合作开展投资分析；Inception42 另签五年协议，向阿联酋政府、企业和学校提供模型；ADNOC 则成为首家使用 OpenAI Frontier 平台的能源公司。报道未披露这些协议涉及的模型版本或全面推广时间表。

telegram · zaihuapd · 11月2日 15:55

**「背景」** OpenAI 于 2026 年 2 月推出企业级智能体平台 Frontier，用于在复杂业务中协调多个 AI 智能体。ADNOC 的相关部署通过 G42 子公司 Inception42 实施，并运行在 G42 位于阿联酋的主权 AI 基础设施上。

**「影响」** 对在食品进口等许可环节与阿布扎比政府打交道的企业而言，AI 输出只是辅助核查，最终审批仍由官员决定；短期内不应把模型结果当作许可或证书已经获批的依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/adnoc-openai-frontier-g42-first-energy-company-adipec-2026">ADNOC OpenAI Frontier Deal: First Energy Rollout Explained ...</a></li>
<li><a href="https://tech-insider.org/adnoc-g42-openai-frontier-first-energy-company-uae-2026/">ADNOC x OpenAI: 1st Energy Firm in Frontier Program [2026]</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Abu Dhabi`, `#AI governance`, `#government technology`, `#AI policy`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [LLM 直接编辑权重并非超人能力](https://seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月3日 00:00

**「背景」** 近期一篇论文称，前沿 LLM 能直接读写神经网络权重：GPT-6 Astra 可仅凭权重判断小型网络在玩什么游戏，还通过原生权重编辑提升了 0.8B Qwen 的数学能力。作者认为，这被解读为通向递归自我改进的“超人能力”，但这些例子其实没有那么超人类。

**「方案」** 作者逐一拆解：游戏识别之所以看似神奇，是因为小网络的输入通道直接对应 8×8 网格且带有“角色”“移动物体”等标签；对第一层 32 个通道的权重取 L2 范数，就能得到 5×10×10 热图，三行 Python 即可完成，热图本身已足以看出玩家和移动物体的位置。Astra 不运行 Python 就算出范数，属于超人的心算，而非超人的 AI 研究。更受关注的 Qwen 案例也不是泛化的“数学差”，而是超过 32k token 后陷入循环；Astra 写了四对循环与不循环文本，测量造成循环的权重，逐步削减并测试，最终找到停止循环的补丁。作者指出，这与 steering 和 Heretic 式 abliteration 的做法一致，称职的人类研究者也会这样做。

**「启示」** 因此作者主张，直接改权重只是令人印象深刻的技巧，类似让 LLM 生成机器码再修补二进制文件；更新模型权重的正途仍是正常训练。LLM 若推动 AI 研究，更可能靠改进训练，而不是神奇地直接调权重。

**标签**: `#LLM weight editing`, `#mechanistic interpretability`, `#model steering`, `#AI capability claims`

---

<a id="item-tech-blog-2"></a>
### [LLM 对齐为何在原则上不可能](https://seangoedecke.com/alignment-is-impossible/) ⭐️ 7.0/10

rss · Sean Goedecke · 11月2日 00:00

**「背景」** 作者从“强大 AI 可能不可预测”这一担忧出发，指出过去把 AI 视为追求固定目标的盲优化器、靠设定正确目标来对齐的思路，已不适用于以模仿人类文本训练的 LLM。

**「方案」** 作者认为，LLM 没有可形式化的固定目标，而是包含大量随输入切换的人格；所谓目标是有机、多元且不断变化的，因此无法靠指定目标来对齐。剩下的路径是充分理解模型，但他论证这种“理解动机”的要求本身不成立：人的心智也不是由清晰可理解的抽象机制运行，动机追溯到底只会变成无助于解释的机械说明。机制可解释性因此无法提供安全保证：特征只能从已观察行为中标注，而真正令人担忧的突发有害行为按定义尚未出现；标签也可能是错的，被称作“善良”的特征也许实际是“除非到了 2030 年才善良”，与 Kripke 的“quus”例子类似且难以区分。即使得到完整的特征图，单个 token 涉及的组合也复杂到人类无法解释；让另一个模型来审查，还会陷入无限回归。作者承认思维链监控、沙箱和人类监督等缓解措施有用，但引述自 2000 年代初的共识认为它们不足以发现或控制超级智能；可解释性仍能帮助减少奖励黑客、提升常规表现，却不能解决智能体失控并造成大规模伤害的问题。

**「启示」** 因此作者的结论并非所有安全措施都无用，而是我们无法说清“确信 LLM 已被对齐”究竟是什么样，因为所需粒度的“动机”并不存在；在这一意义上，LLM 对齐原则上不可解。是否接受该结论，取决于是否认真对待超级智能风险。

**标签**: `#AI alignment`, `#LLM safety`, `#mechanistic interpretability`, `#AI risk`

---

<a id="item-tech-blog-3"></a>
### [受众捕获：参与度指标如何替换你真正想要的读者](https://seangoedecke.com/audience-capture/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月3日 00:00

**「背景」** 肖恩·戈德克（Sean Goedecke）说，写博客最让他害怕的是“受众捕获”：他自认有工程师的灵魂，一看到参与度数字就想把它推高，而网络写作环境恰好让点击量、来源、按投票排序的评论和变现都唾手可得。

**「方案」** 作者认为，浏览量只是他真正在意之物的代理指标：聪明的读者认真思考他的观点、给出有经验的反馈、参与有意义的行业讨论、被他说服，以及建立“谨慎思考者”的声誉。问题在于，点开标题就关掉的人（“点击者”）和真正阅读的人（“读者”）在指标上无法区分。若某类话题（比如嘲讽微服务）带来流量，他就会多写，数字上升，但真正的读者会流失，点击者本就不读，于是他实际上用“点击者和嘲讽者”替换了原本的受众，却还以为自己成功了。他把这套逻辑延伸到工程职业：Jira 工单数和晋升都是代理游戏，而获得自己尊重的人的认可、做出令自己骄傲的技术工作，则是“真实游戏”；区别不在于目标是否客观有价值，而在于你是否真的在乎它。作者说，有限度地“出卖”自己有时是健康的选择，但最糟的是习惯性地出卖，却什么也没换到。他写作是为了那 5% 会思考、讨论、写邮件来的读者，只能靠自己的品味和这些稀薄反馈来判断。

**「启示」** 代理指标本身无错，危险在于不自觉地被它牵着走。作者的核心结论是：先分清自己玩的到底是真实游戏还是代理游戏，再有意识地做取舍，否则赢了数字，却输掉真正想要的受众与工作。

**标签**: `#audience capture`, `#proxy metrics`, `#engineering career`, `#online writing`, `#Goodhart&\#x27;s law`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Anthropic 更新招股书：前三季度营收 332 亿美元，净亏损 1040 亿美元](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) ⭐️ 8.0/10

Anthropic 于 11 月 2 日更新 IPO 招股书，披露截至 2026 年 9 月 30 日的前三季度营收为 332.4 亿美元，同比增长约 1200%；同期净亏损为 1040 亿美元，高于上年同期的 251 亿美元。公司表示，上半年净亏损主要受可转换债券及衍生负债公允价值变动影响，并不完全代表实际经营现金消耗。

telegram · zaihuapd · 11月2日 15:12

**「背景」** Anthropic 正在推进首次公开募股（IPO），这组数据来自其向美国证券交易委员会提交的更新版 S-1 招股书（IPO 注册文件）；公司称上半年净亏损主要受可转换债券及衍生负债公允价值变动影响，并不完全等于经营现金消耗。

**「影响」** IPO 投资者将需权衡 Anthropic 的高速增长与约 8954 亿美元算力及基础设施采购、租赁承诺所带来的未来成本压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html">Anthropic releases amended IPO prospectus with Q3 financials</a></li>
<li><a href="https://www.bloomberg.com/graphics/2026-anthropic-ipo/">Anthropic IPO: AI Giant Must Convince Investors Revenue Will ...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI 行业`, `#财务业绩`, `#算力基础设施`

---

<a id="item-finance-news-2"></a>
### [甲骨文拟发行 200 亿美元股票与债券，股价午盘跌 6%](https://www.cnbc.com/2026/11/02/stocks-making-the-biggest-moves-midday-orcl-spcx-tem-rivn.html) ⭐️ 7.0/10

甲骨文周一提交监管文件，计划发行 100 亿美元普通股和 100 亿美元高级票据，为人工智能建设融资，午盘股价下跌 6%。

rss · CNBC Finance · 11月2日 20:00

**「背景」** 甲骨文是大型数据库和云计算公司，正在为人工智能基础设施建设融资；发行新股会稀释现有股东持股，发债则会增加负债。

**「影响」** 新股发行会稀释甲骨文现有股东的持股，新增高级票据则提高公司的负债水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html">Oracle files to sell $20 billion in new stock, bonds ... - CNBC</a></li>
<li><a href="https://www.unite.ai/oracle-files-concurrent-common-stock-and-senior-notes-offerings/">Oracle Files Concurrent Common Stock and Senior Notes ...</a></li>

</ul>
</details>

**标签**: `#stock movers`, `#earnings`, `#M&amp;A`, `#AI infrastructure financing`, `#semiconductors`

---

<a id="item-finance-news-3"></a>
### [盘前异动：雅诗兰黛业绩超预期，Marvell 拟以 1150 亿美元收购 Lumentum](https://www.cnbc.com/2026/11/02/stocks-making-the-biggest-moves-premarket-crwd-rivn-mu.html) ⭐️ 7.0/10

盘前交易中，雅诗兰黛公布第一财季调整后每股收益 72 美分、营收 37.2 亿美元，均高于 FactSet 分析师预期的 51 美分和 36.5 亿美元，并上调全年盈利展望。Marvell 同意以 1150 亿美元全股票交易收购 Lumentum，交易预计 2028 年上半年完成；CrowdStrike 和 Rivian 因评级上调分别上涨 3.4%和 3.8%。

rss · CNBC Finance · 11月2日 12:49

**「背景」** Marvell 于 11 月 2 日宣布以全股票交易收购 Lumentum，按约 1,132 美元/股计算，对 Lumentum 的隐含企业价值约为 1,150 亿美元，较 10 月 28 日未受交易传闻影响的收盘价溢价约 23.9%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity">Marvell and Lumentum to Combine, Creating a Category Leader ...</a></li>

</ul>
</details>

**标签**: `#premarket movers`, `#analyst upgrades`, `#M&amp;A`, `#earnings`, `#semiconductors`

---