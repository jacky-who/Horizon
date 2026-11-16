---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> 从 30 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [美团开源 1.6 万亿参数 LongCat-2.5，称全程用华为升腾训练](#item-tech-news-1) ⭐️ 8.0/10
2. [MacBook Pro OLED 屏幕的 PWM 频闪争议](#item-tech-news-2) ⭐️ 7.0/10
3. [现代 LLM 位置嵌入的实现解读](#item-tech-news-3) ⭐️ 7.0/10
4. [Meta FAIR/NYU 拆解多模态视觉编码：预训练可选，视觉专属参数必需](#item-tech-news-4) ⭐️ 7.0/10
5. [开源工具称将 B300 上 pageable cudaMemcpy 提速约 5 倍](#item-tech-news-5) ⭐️ 7.0/10

**财经新闻**
1. [CNBC：卢特尼克因家族公司与英伟达的关系面临道德质疑](#item-finance-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [美团开源 1.6 万亿参数 LongCat-2.5，称全程用华为升腾训练](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美团 LongCat 团队在模型正式发布一周后公开了 LongCat-2.5 的权重。该模型总参数约 1.6 万亿，每个 token 激活约 480 亿参数，面向需要自主完成冗长多步骤任务（尤其是编程）的智能体场景，支持文本、图像和视频输入，并以 MIT 许可证发布，允许商用。官方称训练全程使用华为升腾加速卡、未使用英伟达 GPU，并称该模型在 Terminal Bench v2.1 上得分 88.4，略低于 Claude Opus 5 的 89.1。上述训练硬件与基准成绩均为美团方面的说法，来源未提供独立验证或详细技术报告。

telegram · zaihuapd · 11月15日 11:08

**「背景」** LongCat-2.5 采用混合专家（MoE）架构：总参数约 1.6 万亿，但每个 token 仅激活约 480 亿参数；权重以 MIT 许可证发布，并支持 100 万 token 上下文。美团给出的自托管方案基于 194 张华为升腾加速卡的 4 位量化版本，且未提供英伟达 GPU 选项，这与“训练全程未使用英伟达 GPU”的说法相呼应。

**「影响」** 由于权重以 MIT 许可证开放，开发者和企业可以自行部署、微调并用于商业产品，不必依赖闭源 API；但 88.4 的 Terminal Bench 成绩来自厂商自报，团队在选型时应自行复现测试，尤其是长程编程任务上的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/">Meituan releases a 1.6-trillion-parameter agent model that ...</a></li>
<li><a href="https://phemex.com/news/article/meituan-opensources-16tparameter-longcat25-model-trained-entirely-on-domestic-chinese-hardware-103629">Meituan LongCat-2.5: 1.6T MoE AI Model Trained on Huawei Chi ...</a></li>
<li><a href="https://www.gate.com/news/detail/meituan-releases-longcat-25-ai-model-with-16-trillion-parameters-trained-on-25640116">Meituan Releases LongCat-2.5 AI Model With 1.6 Trillion ...</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#large language models`, `#AI agents`, `#Huawei Ascend`, `#AI hardware`

---

<a id="item-tech-news-2"></a>
### [MacBook Pro OLED 屏幕的 PWM 频闪争议](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 7.0/10

一篇技术分析聚焦 MacBook Pro 的 OLED 显示屏，讨论 PWM 调光频闪为何可能让部分用户觉得更难使用，尽管屏幕显示素质更好。文章同时涉及测量方法和实际体感，但现有材料没有给出可核验的完整测试条件，评论区也对 240Hz 等频率结论存在分歧。

hackernews · MacAnorak · 11月15日 13:15 · [社区讨论](https://news.ycombinator.com/item?id=50506719)

**「背景」** PWM（脉宽调制）调光通过快速开关像素来调节屏幕亮度，频率越低、亮度波动越深，越容易被敏感用户感知为闪烁。Notebookcheck 的实验室测试称，新款 14 英寸 MacBook Pro 的 PROLED XDR 屏幕在亮度 99% 及以下时以 240 Hz PWM 调光，波动深度约 56%；AppleInsider 也报道了相同频率和幅度，并指出 PWM 频率与屏幕刷新率不是一回事。已有用户报告头痛、头晕等不适，且目前没有明确修复方法。

**「影响」** 对已经知道自己对频闪敏感的用户，实际影响是购买前应在常用亮度下试用，而不能只依据分辨率、色域等参数判断；评论中的严重不适案例也说明个体差异很大，不能据此推断所有用户都会受影响。

**「社区讨论」** 评论区的核心分歧在测量：有评论者称 240Hz 不是最坏情况，tandem OLED 的两层可能以 480Hz、180 度反相调光，从而在同时工作时形成约 960Hz 的有效频率。另有评论者强调频闪敏感真实存在，家人会因轻微频闪出现恶心和头痛，也有人表示脑震荡后几乎对各类屏幕都更敏感。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.appleheadlines.com/macbook-pro-oled-eye-strain-pwm-flicker/">MacBook Pro OLED Eye Strain &amp; PWM Flicker: 7 Moves - AH</a></li>
<li><a href="https://www.macobserver.com/news/oled-macbook-pro-owners-report-headaches-and-dizziness-from-screen-flickering/">OLED MacBook Pro Owners Report Headaches and Dizziness From ...</a></li>
<li><a href="https://appleinsider.com/articles/26/11/10/if-youre-getting-dizzy-using-proled-macbook-pro-you-are-not-alone">Pulse width modulation on MacBook Pro with PROLED - AppleInsider</a></li>

</ul>
</details>

**标签**: `#OLED PWM`, `#display flicker`, `#MacBook Pro`, `#hardware usability`, `#tandem OLED`

---

<a id="item-tech-news-3"></a>
### [现代 LLM 位置嵌入的实现解读](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 7.0/10

一篇面向机器学习读者的技术解释文章《Understanding Positional Embeddings in Modern LLMs》上线，梳理现代大语言模型中位置嵌入的实现方式。从现有摘要看，它属于教育性深入解读，而非新的研究结果、模型发布或基准测试。现有材料未提供正文，因此文中涉及的具体模型、版本和实验结论无法核实。

hackernews · vismit2000 · 11月15日 12:14 · [社区讨论](https://news.ycombinator.com/item?id=50506376)

**「背景」** Transformer 的自注意力机制本身不包含词序信息，因此模型需要位置嵌入来区分不同位置的 token。早期 GPT-2 使用可学习的绝对位置嵌入；Su 等人在 2021 年的 RoFormer 论文中提出 RoPE，通过对 query 和 key 向量施加旋转来编码相对位置，这一方法目前已被前沿模型广泛采用。

**「影响」** 对正在实现或选型位置编码的开发者，这篇文章可作为实现层面的入门梳理；但若需要推导或改造位置编码，评论者提醒还需补充群表示等理论基础。

**「社区讨论」** 评论者 programjames 认为文章只覆盖实现，真正理解位置编码需要群表示理论，并称旋转位置编码是平移群的表示。这是评论者的理论视角，不等同于文章结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://magazine.sebastianraschka.com/p/understanding-positional-embeddings">Understanding Positional Embeddings in Modern LLMs</a></li>
<li><a href="https://www.institutepm.com/knowledge-hub/rope-alibi-yarn-explained">RoPE , ALiBi , and YaRN Explained: How Modern LLMs Handle Long...</a></li>

</ul>
</details>

**标签**: `#positional embeddings`, `#LLMs`, `#transformer architecture`, `#machine learning education`

---

<a id="item-tech-news-4"></a>
### [Meta FAIR/NYU 拆解多模态视觉编码：预训练可选，视觉专属参数必需](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 7.0/10

Meta FAIR 与 NYU 的一篇预印本报告称，他们在相同数据和总算力预算下从头训练 200 多个多模态大模型，以分别检验视觉编码器的三项作用：独立预训练、仅视觉 token 使用的参数，以及把编码器放在 LLM 之前的位置。实验主要采用 Qwen3-1.7B 和 4B 配置、0.4B 视觉容量，覆盖 0.6B 到 6.4B 主干，并在 Cambrian 的 16 个 448px VQA 基准和 12 个语言基准上评测。结果显示，独立视觉预训练是可选的：四种预训练目标至多与随 LLM 从头训练的编码器打平，即使预训练不占算力也无优势；但视觉专属参数仍是必需的，无编码器模型在各规模上均落后，追上约需 3 倍算力。把编码器放在 LLM 之前同样可选，“in-fusion”在前 8 层加入零初始化的视觉专属权重，在 1.7B 到 6.4B 上与编码器相当，并报告首 token 时间低约 13%；这些是作者自述的受控实验结果，尚非同行评审的独立复现。

reddit · r/MachineLearning · /u/trungh98 · 11月15日 17:38

**「背景」** 在多模态大模型中，标准视觉编码器通常把三项设计选择捆绑在一起：独立的视觉预训练、仅由视觉 token 使用的参数，以及把编码器置于 LLM 之前。不同实验室已发布的模型在数据、算力和这些选择上并不一致，因此仅比较成品模型很难判断哪一项是必要的。

**「影响」** 对多模态架构选型而言，这意味着可以把编码器预训练的算力转投入多模态训练，但不能省掉视觉专属参数；试图完全去掉视觉分支的团队需准备约 3 倍算力，或采用 in-fusion 这类在前层加入视觉专属权重的折中。

**标签**: `#multimodal LLMs`, `#vision encoders`, `#pretraining`, `#model architecture`, `#controlled experiments`

---

<a id="item-tech-news-5"></a>
### [开源工具称将 B300 上 pageable cudaMemcpy 提速约 5 倍](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

开发者 /u/makneeee 在 Reddit 发布开源工具 cudamemcpy-tuner，声称可显著加快 pageable 内存的 cudaMemcpy 传输，并在 NVIDIA B300 上给出示例。按照帖子中的 1 GB uint8 张量基准，直接运行 PyTorch 的 CPU→GPU 拷贝得到 10.2 GB/s，执行 \`cmt tune -- python bench.py\` 后报告为 51.5 GB/s，约 5 倍。该结果来自作者自行提供的基准，帖子未给出独立复现，工具代码和博客已公开在 GitHub 与作者网站。

reddit · r/MachineLearning · /u/makneeee · 11月15日 18:20

**「背景：可页内存与页锁定内存」** 在 CUDA 中，当源数据位于普通可页内存（pageable memory）时，cudaMemcpy 无法直接进行 DMA 传输，驱动需要先把数据复制到内部的页锁定（pinned）暂存缓冲区，再传往设备，这一隐藏步骤会明显拉低有效带宽。NVIDIA 的优化文档与多篇实测都指出，改用 cudaMallocHost 分配的页锁定内存可以提升主机到设备的传输速率，代价是占用不可换出的物理内存。这个工具针对的正是默认的可页传输路径，尝试在不改用户代码的前提下缩小这部分开销。

**「影响」** 对需要在未使用 pinned memory 的情况下把主机数据搬到 GPU 的开发者，这类调优工具提供了一条可能减少传输瓶颈的路径；但当前 5 倍提升仅为作者自报结果，采用前应在目标 GPU、数据规模和 CUDA 版本上自行复测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/">How to Optimize Data Transfers in CUDA C/C++ | NVIDIA ...</a></li>
<li><a href="https://stackoverflow.com/questions/50184146/cuda-pinned-memory-vs-pageable-memory-tradeoffs">optimization - CUDA - Pinned Memory vs. Pageable Memory ... Code sample</a></li>
<li><a href="https://jinseok-moon.github.io/p/pinned-memory/">CUDA Pinned vs Pageable Memory: Faster Host-to-Device Transfers</a></li>

</ul>
</details>

**标签**: `#CUDA`, `#GPU memory transfer`, `#performance optimization`, `#open source tools`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [CNBC：卢特尼克因家族公司与英伟达的关系面临道德质疑](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 8.0/10

CNBC 11 月 13 日报道，美国商务部长霍华德·卢特尼克在其负责对华芯片出口执法期间，因两个儿子领导的坎托·菲茨杰拉德公司与英伟达的持股及业务往来而面临道德质疑。证交文件显示，该行报告的英伟达持股从 2025 年 9 月的逾 350 万股降至 2026 年 3 月底的 178 万股，降幅 49%；报道称没有证据表明卢特尼克泄露非公开信息，坎托表示相关持仓是客户掉期交易中的非重大自营头寸。

rss · CNBC Finance · 11月15日 19:58

**「背景」** 此前，英伟达首席执行官黄仁勋因被曝与一名疑似中国间谍有婚外情而辞职。美国商务部负责出口管制，而卢特尼克主政期间，该部门因迟迟未将涉嫌向中国转运英伟达 AI 芯片的 Megaspeed 列入限制贸易的实体清单而受到批评。

**「影响」** 只要商务部继续推迟把 Megaspeed 列入实体清单，美国芯片及设备供应商向这家新加坡公司出口 AI 芯片时就仍不需要申请出口许可（据《金融时报》报道）；而财政部长贝森特表示，包括财政部在内的四个部门数月来一直支持将其列入，这表明相关管制措施目前只停留在部分机构的立场上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nypost.com/2026/11/12/business/commerce-depts-lutnick-kessler-under-fire-over-inaction-on-nvidias-megaspeed-spy-fiasco/">Commerce Dept&#x27;s Lutnick, Kessler under fire over inaction on ...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/12/nvidia-ceo-jensen-huang-resigns">Jensen Huang resigns as Nvidia CEO after alleged... | The Guardian</a></li>
<li><a href="https://www.reuters.com/business/retail-consumer/bessent-says-treasury-favored-limits-megaspeed-2026-11-13/">Bessent blames Commerce Dept over lack of export controls for ...</a></li>
<li><a href="https://www.ft.com/content/afb6c960-a910-4d67-9588-73ba3bea5b06?syn-25a6b1a6=1">US commerce department delays Megaspeed’s inclusion on trade ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Howard Lutnick`, `#Cantor Fitzgerald`, `#export controls`, `#conflict of interest`

---