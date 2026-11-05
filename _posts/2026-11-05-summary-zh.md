---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> 从 43 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [月之暗面开源 Kimi K3.1 Pro 权重：2.8T 参数、约百万上下文](#item-tech-news-1) ⭐️ 8.0/10
2. [腾讯混元 Hy4 发布，首次加入视觉与电脑操作](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic 发布 FlashProve 可验证推理规范与代码](#item-tech-news-3) ⭐️ 8.0/10
4. [Go 团队发布新标准库 JSON API encoding/json/v2](#item-tech-news-4) ⭐️ 8.0/10
5. [AI 漏洞发现正迫使清理四十年安全债](#item-tech-news-5) ⭐️ 7.0/10
6. [循环 Transformer 是否节省 HBM 带宽：B200 上的权重复用实测](#item-tech-news-6) ⭐️ 7.0/10
7. [GLM-5.3-Flash 的 Trainium2 NKI 层巨内核解码优化](#item-tech-news-7) ⭐️ 7.0/10
8. [KV 检索实验：上下文退化更多来自注意力竞争而非长度](#item-tech-news-8) ⭐️ 7.0/10
9. [NIKKE PC 启动器被指供应链投毒 官方替换两文件未回应](#item-tech-news-9) ⭐️ 7.0/10
10. [华为据报要求客户自购升腾 960DT 内存](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [甲骨文据报取消与腾讯约 70 亿美元 AI 芯片租赁协议](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [月之暗面开源 Kimi K3.1 Pro 权重：2.8T 参数、约百万上下文](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 8.0/10

月之暗面在 Hugging Face 发布 Kimi K3.1 Pro 的开放权重，这是 K3.1 系列的首个模型，也是原生多模态的智能体模型，总参数 2.8T、激活参数 104B，上下文约 100 万 token，权重以 MXFP4 量化形式提供。官方同步开放 API，在 platform.kimi.ai 选择 kimi-k3.1-pro 即可调用，并兼容 OpenAI 与 Anthropic 两种接口。此次发布的是可直接下载的权重与已上线的托管接口，而非仅公布计划。

hackernews · abrarthought · 11月4日 15:30 · [社区讨论](https://news.ycombinator.com/item?id=50366999)

**「背景」** Kimi K3.1 Pro 是在 Kimi K3 基础上经大规模联合强化学习后训练而来，官方模型卡称其为 K3.1 系列的首个模型。该系列这一代重点覆盖编码、3D 创作、金融研究、事实准确性和其他智能体能力。

**「影响」** 2.8T 总参数意味着自建部署的门槛极高，评论区有人估算需要约 8 张 B300 规模的节点才能运行，因此多数用户实际会走官方 API 或第三方托管。已有第三方推理服务商开始上架该模型，评论提到 Together 在同一价位上的吞吐约为 Moonshot 官方端点的两倍、Modal 又再翻倍，说明成本与速度差异将主要由推理服务商决定，选型时需要按吞吐和价格对比而非只看模型本身。

**「社区讨论」** 讨论集中在两点：一是基准可信度，有评论认为 K3.1 相对 DeepSeekV4.1-Flash 提升不大、在第三方公布的内部基准上得分不高，因而怀疑其“刷榜”；另一位做过测试的评论者则称在自己的测试中并未观察到这种情况，认为它是略逊于前沿但适用面很广的强开源模型。二是硬件与成本，有评论以自嘲口吻指出这类开放权重主要面向企业而非个人，个人开发者更可能继续使用小得多的量化模型配合消费级显卡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3.1-Pro">moonshotai/Kimi-K3.1-Pro - Hugging Face</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#Kimi K3.1 Pro`, `#LLM release`, `#inference infrastructure`, `#AI hardware`

---

<a id="item-tech-news-2"></a>
### [腾讯混元 Hy4 发布，首次加入视觉与电脑操作](https://hy.tencent.ai/research/hy4) ⭐️ 8.0/10

腾讯混元于 11 月 4 日发布 Hy4，首次引入视觉能力和电脑操作支持，并针对 Blender、CAD 等专业软件进行了专项训练。官方称，在 579 个真实金融任务的众测中，Hy4 以 3.04 分位居开源模型第一，幻觉率从 15.76% 降至 5.45%；模型已在腾讯云和 OpenRouter 上线，API 价格不变，并计划开源权重、近期推出 Hy4 flash。腾讯还开源了用于单细胞表征的 HyCell 和用于物理场建模的 HyPDE 两个科学基础模型；面向游戏开发，Hy4 已适配 Unreal Engine、Unity 和 Godot，并扩展到多人游戏开发。腾讯同时承认，在研究级数学、长时程编程、模型自我改进和高级视觉问答等内部基准上，Hy4 与顶级闭源模型仍有明显差距。

hackernews · Philpax · 11月4日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=50365780)

**「背景」** 腾讯混元此前已发布 Hy4 preview，作为该系列的预览版本；本次 Hy4 是在此基础上的正式发布。开放权重模型允许用户下载权重并自行部署，因此 Hy4 常被拿来与闭源 API 模型比较成本和可控性。

**「对开发者的实际影响」** 开发者现在就能通过腾讯云 API 和 OpenRouter 调用 Hy4；官方称 API 价格不变，因此接入试用不需要新的商业流程。但腾讯只表示“将在未来几天”发布模型权重和系统卡，所以希望本地自托管或做私有化部署的团队目前仍需等待，现阶段只能走云端 API（tool-2-2）。做游戏开发的团队可以直接使用官方针对 Unreal Engine、Unity、Godot 的适配，来生成玩法逻辑、状态追踪和资产管线相关代码；不过在 Plotly 数据 analytics 基准上试用的 chriddyp 报告称，该模型每道题会运行约 26 次查询，个别题目多达 64 次，因此规划成本时要把这种“慢而细”的调用模式计入延迟和用量预算。

**「社区讨论」** 评论者赞赏腾讯开源 HyCell 与 HyPDE，并认为官方坦承与顶级闭源模型仍有差距是加分项；也有人特别关注其针对 Unreal Engine、Unity 和 Godot 的游戏开发适配。另有评论者在 Plotly 数据分析基准中报告，Hy4 的成本/准确率位置介于 GPT-6.1 Sol 与 GPT-6.1 Terra 之间，但每题约执行 26 次查询、个别达 64 次，耗时很长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/">Tencent Launches Hy4, Joining the Ranks of the World&#x27;s ...</a></li>

</ul>
</details>

**标签**: `#open-weight models`, `#Tencent Hy4`, `#AI research`, `#game development AI`, `#foundation models`

---

<a id="item-tech-news-3"></a>
### [Anthropic 发布 FlashProve 可验证推理规范与代码](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

Anthropic 发布并开源了 FlashProve 的技术规范与代码，该系统用加密证明验证一段 AI 输出是否由指定模型生成，面向需要识别模型替换或核实第三方关于模型执行任务说法的用户与审计者。模型发布方需公开可供匹配的指纹，指纹不会披露模型权重，验证可在本地设备完成。Anthropic 表示研究仍在进行，目前没有部署计划。

hackernews · ltononro · 11月4日 17:17 · [社区讨论](https://news.ycombinator.com/item?id=50368626)

**「背景」** 可验证推理要解决的问题是：服务方在不公开模型权重的情况下，向用户证明某段输出确实由指定模型生成。Anthropic 在技术说明中把 FlashProve 与此前的零知识推理证明系统对比：VerInf 曾在同一个 400B 参数 Llama 4 Maverick 上只达到约 0.02 tok/s，DeepProve 在 GPT-2 和 Gemma 3 上单机分别约为 2.9 和 1.4 tok/s，说明证明开销一直是这类方案的主要瓶颈。

**「影响」** 若投入实际使用，模型发布方需要为每个模型提供可公开匹配的指纹，第三方才能在不获取权重的情况下本地核验输出；由于尚无部署计划，相关流程目前仍停留在规范和研究代码层面。

**「社区讨论」** 评论中，neuwirth 声称 FlashProve 大量沿用了其 VerInf 工作而署名不足；vessenes 和 gopalv 则讨论了成本问题，提到相较普通推理约 90–100 倍的计算开销、约 6.5 MB 的承诺以及单次证明核验需 17–21 秒。nemo1618 认为开放权重模型只需确定性重算即可验证，vintagedave 则指出此类证明可用于发现请求被路由到其他模型的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/provable-inference">Progress on provable inference for large language models</a></li>

</ul>
</details>

**标签**: `#provable inference`, `#LLM verification`, `#cryptographic proofs`, `#AI safety`, `#Anthropic research`

---

<a id="item-tech-news-4"></a>
### [Go 团队发布新标准库 JSON API encoding/json/v2](https://go.dev/blog/jsonv2) ⭐️ 8.0/10

Go 团队在官方博客中介绍了面向 Go 开发者的新标准库 JSON API：encoding/json/v2。它被描述为对标准库 JSON 接口的重新设计，社区讨论集中在 API 设计与迁移影响上。现有材料未说明该 API 何时进入正式标准库、与 encoding/json 的兼容策略以及具体迁移步骤，这些细节仍需以官方文档为准。

hackernews · olexsmir · 11月4日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=50369106)

**「背景」** Go 标准库原有的 encoding/json 已使用多年，Go 团队曾以实验方式探索替代设计：2025 年 9 月的博客介绍了 Go 1.25 中实验性的 encoding/json/v2 与 encoding/json/jsontext。按更新后的官方文章，这两个包现已在 Go 1.27 中转为稳定并正式可用，因此这次变化是同一套新 API 从实验阶段走向正式发布。

**「迁移影响」** 对已在用 \`encoding/json\` 的 Go 项目来说，迁移到 v2 需要逐字段核对序列化结果：有对比测试显示，同一结构体在 v1 与 v2 下的 JSON 输出会发生变化，需要靠选项或标签（如 \`omitzero\`）修正。Aqua Security 的 Trivy 已从实验性的 \`go-json-experiment/json\` 迁移到 \`encoding/json/v2\`，表明这条替换路径已在真实项目中落地。

**「社区讨论」** 有评论者认可 encoding/json/v2 的整体方向，但特别指出移除 MarshalIndent 会让迁移和快速输出可读 JSON 变得更麻烦，因为等价写法复杂且不直观。这属于对 API 人体工学与迁移成本的个人意见，并非对兼容性结论的确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://go.dev/blog/jsonv2">A new Go API for JSON - The Go Programming Language</a></li>
<li><a href="https://go.dev/blog/jsonv2-exp">A new experimental Go API for JSON - The Go Programming Language</a></li>
<li><a href="https://importstatic.com/go/go-json-v2-migration">Go JSON v 2 Migration : What Breaks in Go 1.27 | ImportStatic</a></li>
<li><a href="https://gitmemories.com/aquasecurity/trivy/issues/9422">trivy refactor: migrate from go -json-experiment to encoding / json / v 2</a></li>
<li><a href="https://blog.stackademic.com/golangs-new-proposal-for-the-encoding-or-json-or-v2-package-code-thursday-6e1498684739">Go encoding / json / v 2 | Stackademic</a></li>

</ul>
</details>

**标签**: `#Go`, `#JSON`, `#standard library`, `#API design`, `#parsing`

---

<a id="item-tech-news-5"></a>
### [AI 漏洞发现正迫使清理四十年安全债](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) ⭐️ 7.0/10

IEEE Spectrum 的一篇分析文章（在 Hacker News 上引发讨论）认为，AI 驱动的漏洞发现正在暴露并迫使软件行业清理过去约四十年积累的安全技术债。文章把重点放在长期延后的安全修复上，而不是某一项新漏洞、工具或版本发布；由于未提供原文细节，其具体案例、方法和数据无法核实。争论的核心是这究竟算真正“还债”，还是开启一轮以修复为主、不增加功能的持续工作。

hackernews · pseudolus · 11月4日 11:52 · [社区讨论](https://news.ycombinator.com/item?id=50364336)

**「背景」** 这里的“技术债”主要指长期搁置的安全缺陷和脆弱的遗留代码，而不只是代码风格问题。IEEE Spectrum 的相关报道以 PHP 2 Shell 为例：这是研究者给 PHP 中两个内存安全缺陷起的绰号，说明旧代码中的隐患更容易被新的漏洞发现手段暴露出来。

**「影响」** 对维护遗留系统的开发和网络安全团队而言，可预见的直接压力是漏洞发现和修复工作量上升；若问题涉及结构性缺陷，修复还可能拖慢发布并推高维护成本。组织应把安全维护视为持续投入，而非一次性清理。

**「社区讨论」** 有评论者怀疑这未必是“还清”技术债，而可能是进入以修复为中心、不增加功能的无尽跑步机，并指出不少问题需要重构而非窄补丁。也有人把根因归于操作系统依赖环境授权，主张转向默认拒绝的能力型系统；另有评论期待国家级或商业间谍工具中的 0-day 被顺带发现，从而长期改善软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability">PHP 2 Shell Is a Wakeup Call for AI in Cybersecurity - IEEE Spectrum</a></li>
<li><a href="https://www.fdaytalk.com/php2shell-vulnerability/">PHP 2 Shell Vulnerability : Affected Versions and How to Fix</a></li>

</ul>
</details>

**标签**: `#AI in cybersecurity`, `#technical debt`, `#vulnerability discovery`, `#legacy software`, `#security engineering`

---

<a id="item-tech-news-6"></a>
### [循环 Transformer 是否节省 HBM 带宽：B200 上的权重复用实测](https://www.reddit.com/r/MachineLearning/comments/1xnskvt/do_looped_transformers_save_hbm_traffic_profiling/) ⭐️ 7.0/10

一篇技术博客在 B200 上分析并实测了循环 Transformer（looped transformer，以 Huginn 为例）的 HBM 流量：共享权重虽然减少了存储占用，但并不能自动避免每次迭代重新从 HBM 读取权重。作者称，在一条由八个矩阵乘法组成的链中，共享同一个 72 MiB 权重比使用八份相同副本快 24%，且几乎不从 HBM 读数据；当权重增大到 288 MiB、超过 L2 容量后，这一差距消失。在完整的 Huginn Core 教学中（使用随机权重）实现里，八次迭代的耗时和 HBM 读取量都约为单次迭代的八倍。作者公开了博客、代码和原始 Nsight Compute 数据，并指出该结论来自单卡实测和教学实现，适用范围有限。

reddit · r/MachineLearning · /u/2dayyy6 · 11月4日 16:26

**「背景」** 循环 Transformer（例如 Huginn）会在多次迭代中重复使用同一组权重，因此参数存储量可以下降；但 HBM 是 GPU 的片外高带宽显存，如果权重不能留在 L2 等片上缓存中，那么每次迭代仍可能重新从 HBM 读取。判断这类架构是否真正节省 HBM 流量，关键要看共享权重的大小、缓存容量以及每轮迭代之间的数据复用情况。

**「影响」** 对实现循环或权重共享 Transformer 的开发者而言，这说明用权重共享降低显存占用，不等于降低带宽需求；如果想让权重在迭代间留在片上，需要显式采用 cache-resident 布局或 persistent kernel 等方案，并用 Nsight Compute 之类的工具核实实际 HBM 流量，而不能只根据参数量推断。72 MiB 与 288 MiB 两组的对比还提示，权重能否被缓存、是否超过 L2 容量，会直接决定共享权重是否带来速度收益。

**标签**: `#looped transformers`, `#HBM bandwidth`, `#GPU profiling`, `#Huginn`, `#Nsight Compute`

---

<a id="item-tech-news-7"></a>
### [GLM-5.3-Flash 的 Trainium2 NKI 层巨内核解码优化](https://www.reddit.com/r/MachineLearning/comments/1xo0yuq/p_nki_layer_megakernels_for_glm53flash_on_aws/) ⭐️ 7.0/10

作者开源了一套运行在单台 trn2.48xlarge 上的 AWS Trainium2 推理引擎，用于服务 320B MoE、支持 1M 上下文的 GLM-5.3-Flash，并把每个层的一半改写成一个 NKI 内核（稀疏注意力层则整层一个）。按其自述，batch-8 解码步从 10 月 17 日构建的 32.2 ms 降至 11 月 1 日的 24.2 ms；融合稀疏注意力层和同时发布的 KDA、MoE 内核各贡献 3.2 ms。剩余 24.2 ms 中，6.1 ms 是内存下限，10.0 ms 是超出下限的引擎忙碌，4.6 ms 是内核内等待，2.8 ms 是暴露的集合通信，0.7 ms 空闲。这些是 Reddit 自述、尚未独立验证的数字；作者没有官方 InferenceX 结果、GPU 对比或该构建的任务级评测，且稀疏注意力预填充仍保留一个近似。

reddit · r/MachineLearning · /u/WildCard727 · 11月4日 21:47

**「背景」** NKI（Neuron Kernel Interface）是 AWS 为 Trainium 芯片提供的内核编写接口，让开发者绕过 XLA 编译器自动生成的算子调度，直接控制片上 SBUF 与指令编排。对 320B 级 MoE 模型的 decode 而言，单步计算量远小于权重读取量，瓶颈通常在显存/片上带宽与每个 kernel 边界的固定开销、跨芯片 collective 等待，因此“megakernel”思路是把一整层（或半个层）合并为单个内核以减少边界和等待。该帖也指出当前并无现成的 AWS 官方基线可对比：最新版 vLLM Neuron 插件未注册 GLM 模型，NxD Inference 处于维护模式。

**「影响」** 对想在 Trainium2 上部署 GLM-5.3-Flash 的团队来说，公开的现成路径并不存在：作者指出最新 vLLM Neuron 插件未注册 GLM 模型，NxD Inference 处于维护模式，因此要复现这套性能需自行编写并调优 NKI 内核，同时不能用模拟器替代设备校验——他们有三个内核通过 NKI 模拟器却在设备上给出错误结果。

**标签**: `#AWS Trainium2`, `#inference optimization`, `#NKI kernels`, `#mixture-of-experts`, `#model serving`

---

<a id="item-tech-news-8"></a>
### [KV 检索实验：上下文退化更多来自注意力竞争而非长度](https://www.reddit.com/r/MachineLearning/comments/1xnzzgn/length_is_cheap_competition_is_not_attention/) ⭐️ 7.0/10

作者在 Reddit 发布了一份未经同行评审的实验总结：在键值检索任务中，把上下文长度从 512 扩展到 32K tokens，并测试五个开源模型（参数规模 0.5B–3B，分属四个模型家族），共进行 126,473 次试验。中性填充几乎不带来损失：Qwen2.5-1.5B 在 32K 时准确率仍为 0.97–1.00，中位损失为 0.004 nats；但把与证据格式相同的竞争性陈述放在相同位置后，准确率降到 0.11–0.21，32K 时中位损失为 4.76 nats，而单条为被查询键提供另一值的陈述会使损失放大 9–110 倍。作者报告，log\(1/a\*\)（即证据上的注意力质量）可解释损失方差的 35%–58%，对数长度只解释 2%–8%。作者还复现了 Du 等（2025）用掩码填充证明“长度本身有害”的协议：在 MMLU 上，30K 时分数下降 11–18 分；但在检索任务中，32K 时掩码造成 46 个准确率百分点的损失，而相同填充内容保持可见时则没有损失。作者明确列出的局限包括：注意力结果是预测性的而非因果性的（未对 a\* 做干预）、只使用单一合成任务、模型最大为 3B（MMLU 复现中包含一个 7B 模型）。

reddit · r/MachineLearning · /u/neom\_gluon · 11月4日 21:08

**「背景：&quot;长度本身有害&quot;的既有结论」** Du 等人 2025 年发表在 EMNLP Findings 的论文《Context Length Alone Hurts LLM Performance Despite Perfect Retrieval》提出：即使检索完全正确，输入变长本身也会拉低准确率，报道的降幅从 13.9% 到 85%（来源见 ACL Anthology 条目）。该结论依赖将无关填充内容遮蔽（mask）的实验协议，而本次作者正是用可见的中性填充作为对照，重新检验&quot;长度单独致害&quot;这一说法。

**「影响」** 对长上下文评测的直接影响是：仅用掩码填充来论证“长度导致退化”，可能把竞争性干扰误判为长度效应；作者据此建议，任何长度结论都应附带“可见中性填充”对照。作者的代码（GitHub: yliusci/length-is-cheap）和逐次试验数据（Hugging Face 同名数据集）已公开，可供他人复核或在大模型与真实 RAG 流程上重做。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aclanthology.org/2025.findings-emnlp.1264/">Context Length Alone Hurts LLM Performance... - ACL Anthology</a></li>
<li><a href="https://ardenus.com/articles/the-diminishing-returns-of-context">Ardenus | The Diminishing Returns of Context : Precision Over...</a></li>

</ul>
</details>

**标签**: `#long-context`, `#retrieval`, `#attention`, `#LLM evaluation`, `#context rot`

---

<a id="item-tech-news-9"></a>
### [NIKKE PC 启动器被指供应链投毒 官方替换两文件未回应](https://github.com/WormW/nikke_malware_analysis) ⭐️ 7.0/10

独立研究者与玩家分析称，《胜利女神：NIKKE》PC 启动器加载的官方 CDN 文件遭篡改，被植入会下载并运行远控木马的加载器。该分析称木马包含 19 条命令，可执行任意命令、截屏，并窃取开发者与 AI 工具凭据以及 28 个钱包扩展的数据。Level Infinite 已于 11 月 3 日替换两个被改文件，但尚未公开回应，因此上述能力仍属独立分析而非厂商披露。玩家可在 debug.log 中搜索 k2f\_chan 自查，分析者建议在情况明确前不要启动 PC 版。

telegram · zaihuapd · 11月4日 07:00

**「背景：启动器为何成为投毒入口」** 游戏启动器通常会在运行时从厂商 CDN 动态拉取 JavaScript 等资源，并把它当作可信代码执行；因此，只要 CDN 上的文件被改动，启动器就会在无提示的情况下变成恶意代码的分发通道。这正是此次事件被称为“供应链投毒”的原因。关于最早受影响时间，独立分析的说法并不一致：一份分析称，最迟从 10 月 23 日起，只要打开启动器就可能被植入远控代理；另一份则称，早在 9 月下旬就有四个 JavaScript 文件遭篡改。当前来源只提到两个文件被替换，实际受影响范围仍有待官方说明。

**「影响与自查」** 若上述加载器确已运行，已安装钱包扩展或使用开发、AI 工具凭据的 PC 玩家可能面临凭据暴露风险；在官方说明前，应按分析建议暂不启动客户端，并检查 debug.log 是否出现 k2f\_chan。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gist.github.com/MotherSphere/d6c049a09ba8ac3085c51ee9df24a4e5">NIKKE PC launcher compromise (Nov 2026): Level Infinite CDN ...</a></li>
<li><a href="https://aviatrix.ai/threat-research-center/nikke-pc-game-launcher-hacked-to-spread-remote-access-data-stealing-malware/">NIKKE PC Launcher Supply-Chain Attack 2026: K2F RAT ...</a></li>
<li><a href="https://gist.github.com/MotherSphere/d6c049a09ba8ac3085c51ee9df24a4e5/12a7b3a029c21c65afe75d3b0f78492bce7b335a">NIKKE PC launcher compromise (Nov 2026): Level Infinite CDN ...</a></li>

</ul>
</details>

**标签**: `#supply chain attack`, `#malware`, `#credential theft`, `#game security`, `#PC launcher`

---

<a id="item-tech-news-10"></a>
### [华为据报要求客户自购升腾 960DT 内存](https://thenextweb.com/news/huawei-hbm-smuggling-samsung-sk-hynix-ascend-960dt) ⭐️ 7.0/10

据 The Information 报道，华为已告知部分客户，下一代旗舰 AI 芯片升腾 960DT 将主要采用三星和 SK 海力士的 HBM，并要求客户自行解决内存采购，原因是国内厂商 HBM 产能不足。报道还称，相关 HBM 被焊在性能较弱的处理器上，按处理器编码报关运至香港，再经人携带入内地并加热拆下；深圳一名芯片经纪人称，单颗 HBM3E 价格已从一年前数百美元涨至约 4000 美元。上述消息来自二手报道，华为及三星、SK 海力士尚未确认。

telegram · zaihuapd · 11月4日 14:52

**「背景」** HBM（高带宽内存）通过堆叠 DRAM 与宽接口提升带宽，是 AI 加速器常用的配套存储；三星、SK 海力士和美光等厂商参与了相关 JEDEC 标准制定。由于内存通常与加速器紧密配套，本土 HBM 产能不足时，厂商就可能把内存采购从芯片交付中拆出，要求客户自行解决。

**「影响」** 若该安排属实，采购升腾 960DT 的客户需自行建立三星和 SK 海力士 HBM 的采购渠道，并承担供应、兼容性验证和合规风险；系统交付进度将不只取决于华为芯片供货，也取决于客户能否及时获得内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Huawei Ascend`, `#HBM supply`, `#AI chips`, `#semiconductor supply chain`, `#China tech`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [甲骨文据报取消与腾讯约 70 亿美元 AI 芯片租赁协议](https://www.tradingview.com/news/seekingalpha:e51e68f4d094b:0-oracle-cancels-7b-ai-chip-lease-with-tencent-amid-us-concerns-ft/) ⭐️ 7.0/10

据媒体报道，甲骨文已取消与腾讯一项价值约 70 亿美元、为期五年的 AI 芯片租赁协议，此前美国官员对该交易表达担忧。协议原计划让腾讯通过甲骨文在东南亚的数据中心租用约 10 万枚先进 AI 芯片，首付款约占 30%；相关消息尚缺乏甲骨文或腾讯的独立确认。

telegram · zaihuapd · 11月4日 11:01

**「背景」** 腾讯今年与甲骨文签署五年期租赁协议，计划通过后者在东南亚的数据中心租用约 10 万枚先进 AI 芯片，因为这类芯片无法在中国使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xenospectrum.com/en/tencent-oracle-ai-chip-lease-prepayments/">Tencent Reportedly Leases About 100,000 AI Chips From Oracle in...</a></li>
<li><a href="https://www.rkjdev.com/blog/tencent-oracle-7-billion-ai-chip-deal/">Tencent Signs $ 7 B Oracle AI Chip Lease Deal | rkj dev</a></li>

</ul>
</details>

**标签**: `#Oracle`, `#Tencent`, `#AI chips`, `#US-China tech restrictions`, `#data centers`

---