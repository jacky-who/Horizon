---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> 从 44 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [Qwen4-Max 上线：2.4T 稀疏 MoE 与百万上下文](#item-tech-news-1) ⭐️ 8.0/10
2. [美商务部将先进 AI 芯片出口管制扩至远程访问](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0 发布：Rust 日期时间库](#item-tech-news-3) ⭐️ 7.0/10
4. [微软将大规模邮件中断归因于 7 月修复引入的缺陷](#item-tech-news-4) ⭐️ 7.0/10
5. [CMU 在 YouTube 免费上线 CS Learn 完整学期课程](#item-tech-news-5) ⭐️ 7.0/10
6. [Duetto：不微调，采样时引导预训练音乐 Transformer 实时爵士伴奏](#item-tech-news-6) ⭐️ 7.0/10
7. [腾讯混元发布 Hy4 flash：224B 总参数、1M 上下文与低价 API](#item-tech-news-7) ⭐️ 7.0/10
8. [亚马逊称 AI 代理借 Artex 框架窃取并共享 API 密钥](#item-tech-news-8) ⭐️ 7.0/10
9. [山大团队称给出哥德巴赫猜想条件性证明](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [中国 10 月经济放缓加剧：消费、工业产出与投资均低于预期](#item-finance-news-1) ⭐️ 8.0/10
2. [卢特尼克因英伟达相关关系受审查，其子所在公司持股下降近 50%](#item-finance-news-2) ⭐️ 8.0/10
3. [中美俄领导人计划在深圳 APEC 场边举行首次三方会晤](#item-finance-news-3) ⭐️ 7.0/10
4. [全国猪肉价格跌至近十年低位](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen4-Max 上线：2.4T 稀疏 MoE 与百万上下文](https://mp.weixin.qq.com/s/pJUt0xwD6H-WMyzd8TjZaQ) ⭐️ 8.0/10

据该聚合帖，阿里通义千问正式上线旗舰模型 Qwen4-Max，采用稀疏 MoE 架构，总参数 2.4 万亿，原生支持视觉理解和 100 万 Token 上下文。帖子称它在编程、办公和长程任务上表现突出，前端编程在 Code Arena 盲测中位居全球前列，但这些性能说法尚无独立验证。成本方面，单个任务平均费用由 26.58 元降至 11.16 元，降幅近 58%，Token 消耗减少近 50%，API 定价同步下调。团队还表示，后续将推出更小的 Qwen4 系列模型并公开权重，具体时间、规模和许可证尚未披露。

telegram · zaihuapd · 11月16日 02:52

**「背景」** Qwen4-Max 是通义千问新一代旗舰模型，素材称其采用稀疏 MoE，总参数为 2.4 万亿，并原生支持视觉理解和百万 Token 上下文。稀疏 MoE 的关键在于总参数规模很大，但每个 token 只激活部分专家，因此“2.4T 总参数”不能直接理解为每次推理都会用满全部参数。素材还以“上代”为基准给出单任务费用从 26.58 元降至 11.16 元，但未点名上代的具体版本。

**「迁移与容量规划注意」** 接入 Qwen4-Max 的开发者需要把延迟和输出冗长度纳入容量与成本预算：Artificial Analysis 的评测将该模型列为“每任务明显偏慢、输出相当冗长”，因此即便官方称 token 消耗较上代减少近一半，实际单任务开销仍会随任务类型波动；OpenRouter 还显示该模型默认开启推理，接入时需显式管理推理 token 与超时设置。该模型支持文本、图像和视频输入、上下文约 98.4 万至 100 万 token，现有纯文本调用链需要相应改造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen4-max">Qwen 4 Max - Intelligence, Performance &amp; Price ... | Artificial Analysis</a></li>
<li><a href="https://openrouter.ai/qwen/qwen4-max">Qwen 4 Max - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**标签**: `#Qwen4-Max`, `#sparse MoE`, `#LLM release`, `#long context`, `#open-weight models`

---

<a id="item-tech-news-2"></a>
### [美商务部将先进 AI 芯片出口管制扩至远程访问](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

美国商务部于 11 月 16 日发布临时最终规则，将先进 AI 芯片和服务器的出口管制延伸至远程访问，目标是防止通过第三国数据中心绕过限制。规则还要求向印度尼西亚、马来西亚、新加坡、泰国和巴西再出口 AI 芯片时申请许可。源报道未说明规则的生效日期、许可审批标准或完整适用国家名单，这些细节仍待官方文本确认。

telegram · zaihuapd · 11月16日 14:44

**「背景」** 美国对先进 AI 芯片的出口管制原本围绕芯片和服务器的跨境出口与再出口展开；当境外数据中心可被远程调用时，这一覆盖范围留下了规避空间。新规因此把远程访问纳入管制，以堵住借第三国数据中心绕开限制的通道。

**「影响」** 对通过第三国数据中心远程调用受控芯片的云服务商和企业而言，规则把原先针对实物出口的许可要求扩展到远程使用场景；向上述五国再出口 AI 芯片也需先申请许可，相关跨境算力安排和供应链需按新规调整。由于报道未提供许可条件，实际合规负担取决于后续官方文本。

**标签**: `#AI chips`, `#export controls`, `#US policy`, `#semiconductors`, `#data centers`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0 发布：Rust 日期时间库](https://burntsushi.net/jiff/) ⭐️ 7.0/10

Andrew Gallant（burntsushi）开发的 Rust 日期时间库 Jiff 已发布 1.0 版本，面向需要处理日期和时间等任务的 Rust 开发者。当前材料只确认了 1.0 这一版本节点，未提供具体 API、性能或兼容性变更细节。社区讨论主要围绕它与 chrono 的取舍、API 稳定性以及时间尺度处理展开，而非已公布的功能清单。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** Rust 生态中的日期时间处理长期以 chrono 为主要选择；一位曾维护 chrono 约五年的开发者在前述讨论中表示，其 API 稳定性既是用户采用的原因，也使大幅改进变得困难。Andrew Gallant（burntsushi）开发的 Jiff 以替代方案出现，此次发布 1.0 版本。

**「影响」** Rust 项目在日期时间库选型时多了一个已发布 1.0 的候选；若考虑从 chrono 迁移，仍需自行核验 API、依赖与行为兼容性，现有评论只表达采用意愿，未给出迁移结果。

**「社区讨论」** 曾维护 chrono 约五年的 quodlibetor 表示，自己当年接手是因为不满其 API，但改进常遇阻力，最终因倦怠停止维护，并对 burntsushi 开发 Jiff 表示感谢；其他评论者则赞赏项目明确说明“并非总是合适”，并希望生态更多采用 Jiff。上述均为社区观点，不能视为对 Jiff 兼容性或采用程度的独立验证。

**标签**: `#Rust`, `#datetime`, `#libraries`, `#open source`, `#time handling`

---

<a id="item-tech-news-4"></a>
### [微软将大规模邮件中断归因于 7 月修复引入的缺陷](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

据 The Register 11 月 16 日报道，微软将一次大规模电子邮件服务中断归因于一项早在 7 月的修复中引入的软件缺陷。现有信息没有给出受影响用户数量、具体产品版本、缺陷的完整技术细节或独立验证结果，因此这仍是微软方面的归因。相关分析集中在测试环境与生产环境的差异，以及并发问题为何没有在测试阶段暴露。

hackernews · Bender · 11月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50517321)

**「背景」** 这起邮件中断的根源被追溯到 7 月发布的一次修复：该修复在后续运行中引入了软件缺陷，直到 11 月故障爆发才显现。社区讨论中还提到，微软的低配置测试环境通过了 7 月代码，却未能复现高配置生产环境中的并发问题；这一说法来自评论者，并非已独立验证的结论。

**「影响」** 对依赖微软邮件服务的组织而言，直接后果是服务中断期间的邮件收发受阻；报道未说明完全恢复时间、SLA 影响或补偿安排，这些仍需以微软后续披露为准。

**「社区讨论」** 评论中，ncr100 质疑用低端测试环境验证 7 月代码、而生产环境是高端机器，可能让并发缺陷逃过测试；k0morebi 则追问超大规模服务为何不在达到阈值时丢弃部分流量，而非继续把请求压向下游。另有评论者对关键网络基础设施中运行 Windows 进程表示意外，这些都属于社区观点而非调查结论。

**标签**: `#Microsoft`, `#outage`, `#software reliability`, `#concurrency bug`, `#testing environments`

---

<a id="item-tech-news-5"></a>
### [CMU 在 YouTube 免费上线 CS Learn 完整学期课程](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学格里芬计算机科学学院推出 CS Learn，开始在 YouTube 免费发布当前 CMU 计算机科学课程的完整学期讲座，面向希望系统学习计算机科学的公众。项目负责人 Phillip Compeau 在讨论中表示，本周每天首播一门课程，明年 1 月还会上线更多课程，因此上线首日目录尚不完整。Compeau 也提到 MIT 约 25 年前就已开始开放课件；CS Learn 的不同点在于发布现行课程和整学期讲座，并由学生开发的工具承担大量制作工作。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** 开放课件已有很长历史：CS Learn 负责人 Phillip Compeau 在讨论中坦言，MIT 大约 25 年前就已推出 OpenCourseWare，因此免费公开大学课程视频本身并不新鲜。CMU 此次的不同之处在于，放出的是当前正在开设的课程之完整学期讲座，而非少量精选讲座或过期材料。

**「影响」** 自学者和课堂辅助使用者可以直接按学期顺序观看 CMU 的现行课程，而不必只依赖零散短视频或单门公开课。实际使用时需注意课程按日、按月分批释出，想按某一主题完整选学的人要先确认相关课程是否已经上线。

**「社区讨论」** 有评论者认为，在 AI 时代更应先把基础学扎实，这样才能把 AI 当作增效工具，否则可能被取代；另一位长期关注开放课件的用户则强调，光有视频还不够，学习计划、提醒和笔记等问责机制才是让人坚持完成课程的关键。

**标签**: `#open courseware`, `#computer science education`, `#CMU`, `#online learning`, `#YouTube`

---

<a id="item-tech-news-6"></a>
### [Duetto：不微调，采样时引导预训练音乐 Transformer 实时爵士伴奏](https://www.reddit.com/r/MachineLearning/comments/1xxkyh3/steering_a_pretrained_music_transformer_at/) ⭐️ 7.0/10

开发者公开了 Duetto 项目及代码：这是一个面向 MIDI 键盘的实时爵士伴奏系统，它原样使用预训练的 Anticipatory Music Transformer（Thickstun 等，2023），通过采样时的规则化 logit 掩码与偏置来控制独奏、伴奏和走动贝斯，而不做微调。玩家的音符与模型输出被放在同一事件序列中逐音符续写；规则层会屏蔽不允许的音符（如必须等待的手、超出音域的音、非拍点贝斯音），并提高当前和弦音、强拍引导音或待引用乐句下一音的权重。作者称在《Autumn Leaves》、160 bpm 的演示中，约 61% 的独奏音符来自引用乐句或主题，其余由模型生成；服务器预采样约 1 秒音乐，并在玩家弹奏时重采样未播放部分，以兼顾低延迟和模型的“规划”。作者报告 3080 Ti 上每音符约 12 ms（medium）/18 ms（large），大型模型在 Jetson Orin Nano 上约 90 ms/音符，同时承认它会偏离演奏者、响应难预测，规则偏置过强会像“乐句手册”、过弱又不像爵士；代码免费供非商业使用，该项目展示尚非同行评审结果。

reddit · r/MachineLearning · /u/GGAllin43 · 11月16日 09:19

**「背景」** Duetto 依赖的 Anticipatory Music Transformer 由 Thickstun 等人于 2023 年提出，其核心是交错生成“事件”与“控制”序列，从而在生成过程中施加音乐控制（tool-2-1、tool-2-2）。Duetto 将该预训练模型原样用于实时伴奏，因此所有控制都放在采样阶段完成：每次采样前修改 logits，而不通过微调改变模型权重。

**「影响」** 对想在本地或边缘设备上做交互式音乐生成的开发者，Duetto 表明可以把控制逻辑放在采样阶段、直接复用预训练符号音乐模型，省去先收集配对数据做微调的前置工作。实际采用时的主要工作量会落在规则层：作者报告的漂移、不可预测响应和偏置强度敏感，意味着需要按曲目与演奏者反复调整掩码和偏置，而不能把低推理延迟当作稳定合奏的保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.08620">[2306.08620] Anticipatory Music Transformer</a></li>
<li><a href="https://paperswithcode.co/paper/2306.08620">Anticipatory Music Transformer (arXiv...) | Papers with Code</a></li>

</ul>
</details>

**标签**: `#music-generation`, `#transformer`, `#sampling-time-control`, `#real-time-systems`, `#jazz`

---

<a id="item-tech-news-7"></a>
### [腾讯混元发布 Hy4 flash：224B 总参数、1M 上下文与低价 API](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

腾讯混元发布 Hy4 flash，这是一款总参数 224B、激活参数 12B 的多模态模型，支持 1M 上下文，并已在腾讯云 TokenHub、WorkBuddy 和元宝上线。其 API 定价为每百万 Token 输入 0.5 元、输出 2 元，命中缓存时仅需 0.02 元，较 Hy4 大幅下降；11 月 30 日前 WorkBuddy 限免，API 五折。腾讯混元称，Hy4 flash 的综合效果略优于 Hy4 preview；按 WorkIndex 计算，其单任务成本分别为 Hy4 preview 的 1/13 和 Hy4 的 1/20，但上述效果与成本对比均为厂商说法。腾讯混元还表示计划开源该模型，目前尚未公布具体许可证或权重发布时间。

telegram · zaihuapd · 11月16日 07:17

**「背景：稀疏 MoE 与 Hy4 系列」** Hy4 flash 采用稀疏混合专家（MoE）架构：总参数 224B，但每个 token 只激活其中 12B，推理时仅需计算这部分参数，这是其能把官方所称的单任务成本压到前代零头的结构性原因。它属于腾讯混元 Hy4 系列的轻量版本，官方称综合效果略优于此前的 Hy4 preview。1M 上下文则面向需要一次性读入长文档或大量历史材料的日常任务场景。

**「影响」** 开发者现在可以在腾讯云 TokenHub 以每百万 Token 输入 0.5 元、输出 2 元调用该模型，并把更长、多模态的请求放入 1M 上下文；若要从 Hy4 preview 迁移，需自行验证官方所称的“略优”效果，因为目前缺少独立评测。

**标签**: `#Tencent Hunyuan`, `#LLM release`, `#Mixture-of-Experts`, `#API pricing`, `#open source`

---

<a id="item-tech-news-8"></a>
### [亚马逊称 AI 代理借 Artex 框架窃取并共享 API 密钥](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

亚马逊称，攻击者利用开源渗透测试框架 Artex 驱动 AI 代理，从 LiteLLM、Dify 等公网暴露的 AI 应用中窃取 API 密钥，在验证有效性后汇入共享密钥池，用于支付后续更多大模型调用。亚马逊表示该活动始于 10 月 3 日，于 11 月 5 日被其 MadPot 诱饵网络截获并阻断；公司以“中等信心”将行动归因于与中国相关的威胁组织，并称并非所有被列出的目标都已失陷，已通知可能受影响的 AWS 客户。上述说法目前均为亚马逊单方面披露，尚无独立验证。

telegram · zaihuapd · 11月16日 13:00

**「背景」** LiteLLM、Dify 等 AI 应用通常通过 API 密钥调用付费大模型服务；一旦这些应用在公网暴露且配置不当，密钥就可能被滥用，并直接转化为模型调用额度。亚马逊称，其 MadPot 诱饵网络用于观测并阻断此类恶意活动。

**「影响与应对」** 对在公网暴露 LiteLLM、Dify 等 AI 应用实例的组织而言，直接风险是 API 密钥被取走并用于支付攻击者的大模型调用费用；亚马逊表示已通知可能受影响的 AWS 客户，并称并非所有被点名目标都已失陷。可行的处置是排查此类实例的公网暴露面、轮换并收紧密钥权限、监视异常的模型调用量与账单增长；需注意亚马逊对中国相关组织的归属判断仅为中等信心。

**标签**: `#AI security`, `#API keys`, `#autonomous agents`, `#cybercrime`, `#cloud security`

---

<a id="item-tech-news-9"></a>
### [山大团队称给出哥德巴赫猜想条件性证明](https://mrc.sdu.edu.cn/info/1018/2193.htm) ⭐️ 7.0/10

山东大学李嘉民、刘建亚在论文中称，在狄利克雷 L 函数广义黎曼猜想成立、并满足两种附加谱假设之一的条件下，可证明所有充分大的偶数都是两个素数之和。论文还称，这两个素数位于该偶数的三分之一至三分之二之间，并称这是首个覆盖所有充分大偶数的二元哥德巴赫猜想条件性证明。该结果并非无条件证明，单靠广义黎曼猜想也不足以推出结论，所用方法不同于经典筛法和圆法。

telegram · zaihuapd · 11月16日 16:01

**「背景」** 哥德巴赫猜想断言每个充分大的偶数都可写成两个素数之和；广义黎曼猜想则是数论中一个尚未证明的假设，涉及狄利克雷 L 函数。山东大学团队的结论以该猜想和两种附加谱假设之一为前提，因此是条件性证明，并未无条件解决哥德巴赫猜想。

**「对研究者的影响」** 研究者在引用该结论时，必须将其限定在广义黎曼猜想成立且满足两种谱假设之一的前提下，不能当作无条件定理使用。该结果不改变哥德巴赫猜想仍未获得无条件证明的现状。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.tencent.cn/developer/article/2206748">cloud.tencent.cn/developer/article/2206748</a></li>
<li><a href="https://www.chinanews.com.cn/m/gn/2022/11-22/9899441.shtml">轰动数学界的张益唐究竟证明了啥？ -中国新闻网</a></li>

</ul>
</details>

**标签**: `#Goldbach conjecture`, `#number theory`, `#conditional proof`, `#mathematics research`, `#Shandong University`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国 10 月经济放缓加剧：消费、工业产出与投资均低于预期](https://www.cnbc.com/2026/11/16/china-retail-sales-october-industrial-output-investment.html) ⭐️ 8.0/10

中国 10 月社会消费品零售总额同比增长 0.4%，低于分析师预期的 0.8%；规模以上工业增加值同比增长 4.8%，也低于 5.3%的预期。今年前 10 个月固定资产投资同比下降 8.1%，而分析师原本预期下降 7%。

rss · CNBC Finance · 11月16日 03:53

**「背景」** 中国房地产市场低迷已进入第五年，房产贬值持续侵蚀家庭财富，是消费疲软、投资收缩的主要背景；官方数据显示，三季度经济同比增长 4.5%，已从三年低点回升。

**「影响」** 由于国内消费和投资走弱，增长更加依赖外需；花旗研究警告，欧盟可能出台更多针对中国的贸易措施，这会使中国出口企业面临额外的政策风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/16/china-retail-sales-october-industrial-output-investment.html">China ’s slowdown deepens in October as key economic data disappoint</a></li>

</ul>
</details>

**标签**: `#China economy`, `#macroeconomic data`, `#consumer spending`, `#fixed investment`, `#trade surplus`

---

<a id="item-finance-news-2"></a>
### [卢特尼克因英伟达相关关系受审查，其子所在公司持股下降近 50%](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 8.0/10

美国商务部长霍华德·卢特尼克因两个儿子领导的坎托·菲茨杰拉德公司与英伟达的关系受到审查；据 CNBC 分析证券申报文件，该公司报告的英伟达持股数在 2025 年 9 月至 2026 年 3 月间下降近 50%。据 Axios 11 月 11 日报道，这一变化正值卢特尼克多次抵制对涉嫌向中国走私英伟达芯片的公司采取行动；报道同时指出，没有证据表明存在不当行为，坎托称相关持仓属日常业务且“不重大”。

rss · CNBC Finance · 11月16日 12:14

**「背景」** 美国商务部负责执行出口管制，包括把外国企业列入「实体清单」（受限制企业名单）。卢特尼克于 2025 年 2 月离开投行坎托·菲茨杰拉德（Cantor Fitzgerald）出任商务部长，该公司现由他的两个儿子经营；英伟达首席执行官黄仁勋本周辞职，此前有报道称他与一名被美方怀疑为中国情报机构工作的女性有私情，黄仁勋和卢特尼克均已被传唤于下月到参议院一个委员会作证。

**「影响」** 审查直接落在美国商务部对 Nvidia 芯片出口许可和实体清单的执行上，使 Nvidia 及其依赖先进 AI 芯片的云服务客户面临更严格的合规与政策审视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://edition.cnn.com/2026/11/16/tech/nvidia-sex-spies-serious-problems">Lies, spies and sex are just one part of the Nvidia story.</a></li>
<li><a href="https://www.nytimes.com/live/2026/11/12/business/nvidia-jensen-huang-resigns">Nvidia Updates: Huang ’s Resignation Reverberates Through...</a></li>
<li><a href="https://www.nytimes.com/2026/11/15/us/politics/trump-lutnick-ai-chips-cantor-fitzgerald.html">Lutnick Pushed to Weaken Chip Rules That Overlap With His Family...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Howard Lutnick`, `#export controls`, `#conflict of interest`, `#China chip smuggling`

---

<a id="item-finance-news-3"></a>
### [中美俄领导人计划在深圳 APEC 场边举行首次三方会晤](https://apnews.com/article/trump-xi-putin-summit-china-5fe92253ef38100bae913834a9b74d72) ⭐️ 7.0/10

中国外交部发言人宣布，中美俄三国领导人计划于 11 月 19 日在深圳 APEC 峰会期间举行三方会晤；媒体称这将是三国领导人首次专门举行三方会晤，会晤在 APEC 场边举行，不属于 APEC 正式议程。

telegram · zaihuapd · 11月16日 01:38

**「背景」** 亚太经合组织（APEC）是促进亚太地区贸易的 21 个成员经济体政府间论坛；2026 年深圳峰会是继 2001 年上海、2014 年北京之后，中国第三次主办该峰会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asia-Pacific_Economic_Cooperation">Asia-Pacific Economic Cooperation - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/2026%E5%B9%B4%E4%B8%AD%E5%9B%BDAPEC%E5%B3%B0%E4%BC%9A">2026年中国 APEC 峰会 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#APEC`, `#US-China-Russia`, `#trade policy`, `#diplomacy`

---

<a id="item-finance-news-4"></a>
### [全国猪肉价格跌至近十年低位](https://finance.sina.com.cn/jjxw/2026-11-15/doc-iniyupuh6583194.shtml) ⭐️ 7.0/10

11 月以来全国猪肉价格跌至近 10 年低位，11 月 9 日生猪均价降至每公斤 8.63 元；福州生猪收购价为每 50 公斤 480 至 550 元，同比下跌 20%至 26%。业内人士将下跌归因于需求减弱和生猪供应增加，分析人士预计未来 6 至 8 个月猪价反弹仍可能乏力。

telegram · zaihuapd · 11月16日 03:45

**「背景」** 猪价由生猪供需关系决定；业内人士将本轮下跌归因于消费需求减弱、生猪供应增加，以及养殖管理改善使每头母猪每年提供的出栏生猪数量提高。

**「影响」** 此轮猪价下跌直接压低生猪养殖户的销售收入，而零售端猪肉价格低于部分蔬菜则减轻家庭食品开支。

**标签**: `#猪肉价格`, `#生猪养殖`, `#食品通胀`, `#中国CPI`, `#农产品市场`

---