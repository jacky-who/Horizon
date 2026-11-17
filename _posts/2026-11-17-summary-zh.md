---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 49 条内容中筛选出 17 条重要资讯。

---

**科技新闻**
1. [vLLM v0.34.0 发布：默认扩展 KV 缓存，移除 V1 运行器](#item-tech-news-1) ⭐️ 8.0/10
2. [美国将 AI 芯片出口管制延伸至远程访问](#item-tech-news-2) ⭐️ 8.0/10
3. [卡内基梅隆大学 CS Learn 免费上线整学期课程讲座](#item-tech-news-3) ⭐️ 7.0/10
4. [Optimizely 被曝遭入侵并向 Zoom、GitLab 等站点投放恶意脚本](#item-tech-news-4) ⭐️ 7.0/10
5. [报告称 Windows 11 遥测收集开发者所用编码代理与工具](#item-tech-news-5) ⭐️ 7.0/10
6. [Rust 日期时间库 Jiff 发布 1.0 版本](#item-tech-news-6) ⭐️ 7.0/10
7. [微软称大规模邮件中断源于 7 月修复引入的缺陷](#item-tech-news-7) ⭐️ 7.0/10
8. [Linebender 的圆角方形与曲线几何文章](#item-tech-news-8) ⭐️ 7.0/10
9. [Marimba：冻结语音编码器支持多类型查询](#item-tech-news-9) ⭐️ 7.0/10
10. [duetto：不微调，仅在采样时引导预训练音乐 Transformer 实时伴奏爵士](#item-tech-news-10) ⭐️ 7.0/10
11. [腾讯混元发布 Hy4 flash：224B 总参数、1M 上下文，API 大幅降价](#item-tech-news-11) ⭐️ 7.0/10
12. [美国与九国签署《旧金山宣言》共保 AI 供应链](#item-tech-news-12) ⭐️ 7.0/10
13. [亚马逊称 AI 代理窃取 API 密钥以维持模型调用](#item-tech-news-13) ⭐️ 7.0/10
14. [Apple 智能登陆国行 iPad 与 Mac 测试版，云端功能设每日上限](#item-tech-news-14) ⭐️ 7.0/10
15. [阿里、腾讯、月之暗面据报限制新模型攻击性网络能力](#item-tech-news-15) ⭐️ 7.0/10

**财经新闻**
1. [卢特尼克因英伟达间谍风波受质询，其子掌管的 Cantor 减持英伟达](#item-finance-news-1) ⭐️ 7.0/10
2. [英特尔及 CEO 陈立武遭股东集体诉讼](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 发布：默认扩展 KV 缓存，移除 V1 运行器](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM 发布 v0.34.0，包含 1,061 次提交和 10 个新模型集成，并将可扩展 KV 缓存设为默认：在 CUDA 和 ROCm 上按预热后的实际空闲显存确定缓存大小，官方示例称 MiniMax-M3 在 H200 上由 433k 增至 672k tokens。该版本移除了 Model Runner V1，GPU 端只剩 Model Runner V2；Blackwell 和 MI355X 上报告了最高 1.95 倍解码、1.6 倍吞吐等提升。升级需注意默认块大小从 16 改为 64、ROCm 7.2 构件不再发布，并要求 huggingface\_hub &gt;= 2.0.0。

github · khluu · 11月16日 23:22

**「背景」** vLLM 是广泛使用的开源大模型推理与服务引擎，升级版本会直接影响现有部署的启动参数、镜像与依赖兼容性。其 KV 缓存用于保存注意力计算的键值状态，缓存可占用的显存决定了能同时承载多少上下文和请求，因此缓存容量计算方式的变化会直接改变吞吐与延迟表现。

**「升级影响」** 对现有部署而言，升级前应移除 VLLM\_USE\_V2\_MODEL\_RUNNER=0，否则启动会失败；若要保留旧的 KV 缓存估算和块大小行为，需显式传入 --gpu-memory-utilization 0.9（或 --no-enable-extensible-kv-cache）和 --block-size 16。依赖还须满足 huggingface\_hub &gt;= 2.0.0、tokenizers &gt;= 0.23.3 和 timm &gt;= 1.0.30。

**标签**: `#vLLM`, `#LLM inference`, `#open-source releases`, `#GPU performance`, `#KV cache`

---

<a id="item-tech-news-2"></a>
### [美国将 AI 芯片出口管制延伸至远程访问](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

美国商务部于 11 月 16 日发布临时最终规则，将先进 AI 芯片与服务器的出口管制扩展至远程访问，目标是堵住通过第三国数据中心规避限制的通道。据报道，新规还要求向印度尼西亚、马来西亚、新加坡、泰国和巴西再出口 AI 芯片时申请许可。该规则由财政部和国家安全委员会主导起草；现有摘要未说明许可门槛、生效日期或具体执行细节。

telegram · zaihuapd · 11月16日 14:44

**「背景」** 美国此前的先进芯片出口管制在执行中难以阻止经第三国中转的转运；相关报道指出，这类转运仍是规避限制的渠道。新规把管制范围从硬件跨境流动扩展到远程访问，正是针对这一缺口。

**「影响」** 对通过海外数据中心远程调用受控芯片的云服务商和 AI 开发者而言，跨境算力安排将需要纳入出口许可审查，原本借助第三国节点提供算力的路径可能不再可行。相关企业应核查远程访问和再出口是否触发许可要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reason.com/2026/11/16/trumps-new-chip-export-rule-targets-china-but-exempts-tiktoks-parent-company/">Trump’s new chip export rule exempts TikTok’s parent company</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#export controls`, `#US policy`, `#data centers`, `#semiconductors`

---

<a id="item-tech-news-3"></a>
### [卡内基梅隆大学 CS Learn 免费上线整学期课程讲座](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学推出 CS Learn，在 YouTube 免费发布该校当前计算机科学课程的整学期讲座视频；首批课程本周每天上线一门，更多课程计划于明年 1 月推出。项目负责人 Phillip Compeau 表示，部分学生开发了用于自动化部分制作流程的工具。发布内容以讲座视频为主，课程项目和反馈机制等课程材料尚未随首批视频一同提供。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** CS Learn 是卡内基梅隆大学 Kenneth C. Griffin 计算机科学学院推出的免费在线学习平台，其 YouTube 频道把一门门真实课程按完整学期组织成播放列表，向任何人开放。除了当前已上线的讲座视频，校方还计划由学生与 ScottyLabs 合作加入可自定进度、带即时反馈、徽章和 AI 辅导的课程材料，覆盖人工智能、机器人、系统等多个方向。

**「影响」** 对自学者和开发者而言，可按上线节奏免费学习 CMU 当前课程的完整学期讲授内容，包括讨论中提到的 ML Systems 等主题；但缺少项目和反馈时，单看讲座难以形成有评价的学习闭环，课程材料是否以及何时补齐会直接影响使用价值。

**「社区讨论」** 有 CMU 校友对 Tianqi Chen 的 ML Systems 和 15-259 概率与计算表示期待，并请求增加分布式系统、操作系统等课程；也有人提醒，只有讲座视频而缺少项目和反馈时，学习效果会打折扣。另有评论认为，在 AI 时代更应打好基础，把 AI 当作工具而非替代基本功。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://www.pressreleasepoint.com/cmu-opens-access-top-computer-science-classes-through-free-cs-learn-platform">CMU Opens Access to Top Computer Science Classes Through Free ...</a></li>
<li><a href="https://zeli.app/story/50522980">Carnegie Mellon opens its CS classrooms · Hacker News | Zeli</a></li>

</ul>
</details>

**标签**: `#open courseware`, `#computer science education`, `#YouTube`, `#Carnegie Mellon`, `#ML systems`

---

<a id="item-tech-news-4"></a>
### [Optimizely 被曝遭入侵并向 Zoom、GitLab 等站点投放恶意脚本](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 7.0/10

据报告，Optimizely 遭到入侵，并通过其面向客户的脚本在 Zoom、GitLab 等网站投放恶意代码；攻击者如何获得跨客户写入权限仍不清楚。评论中引述的说明称，这不是 CDN 缓存投毒：Optimizely 的 CDN 分发了被植入的代码，连 www.optimizely.com 和 login.optimizely.com 的脚本片段也受到影响。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**「背景：第三方脚本与标签管理的暴露面」** Optimizely 属于一类通过 cdn.optimizely.com 向客户页面注入实验与标签脚本的第三方服务，这些脚本在访问者浏览器中以站点自身的权限执行，因此一旦该域名下发的内容被篡改，影响会同时落到所有接入的站点上。社区评论把这一模式追溯到 Google Tag Manager 的设计初衷——让市场团队无需工程介入即可往页面加“标签”，评论者称其代价是每篇新闻文章都要加载约 10MB 的 JavaScript。换言之，本次事件的核心并非 CDN 缓存污染，而是评论者所指的那条“第三方脚本可被任意改写”的信任链。

**「影响」** 直接后果是，嵌入 Optimizely 脚本的站点会把被篡改的第三方脚本加载给访问者；报道点名 Zoom 和 GitLab，评论还提到 Optimizely 自家域名也受影响。在 Optimizely 查清攻击者如何获得写入权限并完成清理前，这些站点的运营者应审计、暂停或移除该脚本，而不能只把它当作 CDN 缓存问题处理。

**「社区讨论」** 有评论者批评 Google Tag Manager 这类让市场团队绕过工程团队添加脚本的机制，认为它使页面加载大量第三方 JavaScript 并扩大攻击面；也有人主张大型站点应自托管关键脚本或对供应商脚本实施更严格的发布审查，另有用户表示已在 hosts 文件中屏蔽 cdn.optimizely.com。

**标签**: `#supply chain security`, `#third-party scripts`, `#web security`, `#malware`, `#Optimizely`

---

<a id="item-tech-news-5"></a>
### [报告称 Windows 11 遥测收集开发者所用编码代理与工具](https://xusheng.dev/posts/windows-coding-agent-telemetry/) ⭐️ 7.0/10

一篇开发者博客文章称，Windows 11 会收集用户运行了哪些编码代理和开发者工具的信息，该文在 Hacker News 上引发讨论。由于原文正文未能获取，目前可依据的只有文章标题和社区转述：评论者 not\_a\_bot\_4sho 称，开发工具的使用情况会随“可选诊断数据”一并上传（其说法是默认开启），并可通过“设置 → 隐私和安全性 → 诊断和反馈”关闭。这些说法来自文章作者与评论者，现有材料中没有微软的确认或回应，具体收集哪些字段、上传频率和保留期限均不清楚。

hackernews · cwaffles · 11月16日 22:58 · [社区讨论](https://news.ycombinator.com/item?id=50524736)

**「技术背景」** 这次争议的技术背景是 Windows 11 的 ETW 诊断报告：一篇逆向分析称，系统组件 MissionControlAggregator 会把 Codex、Claude、Copilot、Cursor 等编码代理和开发工具的使用情况编码成位图，放入可选诊断数据并排队等待上传。该分析称未发现提示词或源代码被收集，因此争论焦点集中在“运行了哪些工具”这类元数据是否应纳入遥测。

**「对开发者的影响」** 对在 Windows 11 上运行编码代理的开发者而言，可立即采取的动作是检查“设置 → 隐私和安全性 → 诊断和反馈”中的可选诊断数据开关，按评论者的说法，关闭后这类开发工具遥测就不再上传。由于缺少微软公开的字段清单，企业也难以判断哪些工具名称或路径会进入遥测数据，从而评估合规与保密风险。

**「社区讨论」** 评论者对该做法的定性存在分歧：dannyw 指出 Intel、AMD、NVIDIA 驱动以及 Chrome 等早已收集可执行文件名和路径，认为 Windows 并非特例；herf 则认为非侵入式遥测有助于微软确定功能优先级，理由是 Windows 的 AI 代理沙箱 MXC 直到 10 月 7 日才推出、Claude Code 尚未支持，不少代理仍在无沙箱环境或 WSL 中运行。另有数位评论者建议转向 Linux，s\_dev 称单机游戏在 Linux 上基本可正常游玩、多人游戏仍有问题，dead\_hn\_theory 则认为适应期大约一周。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/windows-coding-agent-telemetry/">Windows 11 Is Collecting Data on Which Coding Agents and ...</a></li>
<li><a href="https://windowsforum.com/news/windows-11-optional-telemetry-can-report-coding-agent-usage-research-finds.452631/">Windows 11 Optional Telemetry Can Report Coding Agent Usage ...</a></li>
<li><a href="https://www.startuphub.ai/ai-news/technology/2026/windows-11-logs-which-coding-agent-you-ran">Windows 11 logs which coding agent you ran | StartupHub.ai</a></li>

</ul>
</details>

**标签**: `#Windows 11 telemetry`, `#developer tools`, `#coding agents`, `#privacy`, `#operating systems`

---

<a id="item-tech-news-6"></a>
### [Rust 日期时间库 Jiff 发布 1.0 版本](https://burntsushi.net/jiff/) ⭐️ 7.0/10

Rust 日期时间库 Jiff 发布 1.0 版本，作者为 burntsushi，面向需要在 Rust 中处理日期和时间的开发者。当前材料未给出具体 API 变更、性能数据或兼容性承诺，因此这次发布应理解为库进入 1.0 阶段，而不是已公布可量化改进。Hacker News 讨论显示社区关注其技术质量和 API 设计，并把它视为 chrono 之外的一个可选方案。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** Jiff 是 BurntSushi 开发的 Rust 日期时间库，项目文档将其定位为提供难以误用的高层日期时间原语，同时保持合理性能。其文档还专门设有与 Rust 其他主流开源日期时间库的对比页面，便于开发者评估不同库之间的取舍。

**「影响」** 对正在选型的 Rust 项目来说，Jiff 1.0 值得纳入评估；但材料没有提供与 chrono 的迁移路径或兼容性说明，采用前需自行验证现有日期时间代码的替换成本。

**「社区讨论」** chrono 前维护者 quodlibetor 表示，他当年接手是因为 API 不理想，但用户更看重稳定性，改进常遇阻力，最终因倦怠停止维护，并对 burntsushi 编写 Jiff 表示感谢。另有评论者赞赏 Jiff 明确说明并非适用于所有场景，也有人询问 TAI、UT1 等时间尺度支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/jiff: A datetime library for Rust that ...</a></li>
<li><a href="https://docs.rs/jiff/latest/jiff/_documentation/comparison/index.html">jiff::_documentation::comparison - Rust - Docs.rs</a></li>

</ul>
</details>

**标签**: `#Rust`, `#datetime`, `#libraries`, `#open-source`, `#time zones`

---

<a id="item-tech-news-7"></a>
### [微软称大规模邮件中断源于 7 月修复引入的缺陷](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

微软将一次大规模邮件服务中断归因于 7 月一次修复中引入的软件缺陷，相关说明以事后复盘形式给出。根据社区评论引用的复盘内容，其负载测试主要覆盖核心较少、性能较弱的硬件，而争用问题在核心更多、更新的机器上反而更严重。给定材料只呈现微软的归因及围绕恢复和负载测试的解释，未提供独立验证或完整故障时间线。

hackernews · Bender · 11月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50517321)

**「背景」** 2026 年 11 月 12 日，Outlook 与 Teams 等 Microsoft 365 服务发生全球性中断；CNET 与 NPR 当时的报道称，Microsoft 表示故障并非网络攻击所致并在抢修，但未给出根本原因（tool-2-1、tool-2-2）。本次报道是事后给出的解释：问题源自 7 月一次修复中引入的软件缺陷，且在受影响服务恢复后，Microsoft 才逐步公布这一归因。

**「影响」** 这次复盘暴露了负载测试的硬件覆盖差距：若争用确实在核心更多、更新的机器上更严重，只按低核数设备验证容量的团队会低估生产环境风险，应把高核数配置纳入容量测试和恢复演练。

**「社区讨论」** 评论区把焦点放在恢复策略上：有用户用电网‘黑启动’类比说明不能直接满载恢复，另有人主张按 IP 段限流或轮换连接以逐步恢复服务。还有评论质疑为何负载测试覆盖了较弱硬件却漏掉问题更严重的高核数新硬件，并对关键网络设施使用 Windows 表示意外。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/news-live/microsoft-outlook-outage-11-12-2026/">Microsoft Blames Outlook Outage on Software Bug in July ... - CNET</a></li>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6039343/outlook-down-widespread-outage-microsoft-email">A negative Outlook : Microsoft scrambles to fix email outage : NPR</a></li>

</ul>
</details>

**标签**: `#incident postmortem`, `#cloud reliability`, `#Microsoft`, `#load testing`, `#outage`

---

<a id="item-tech-news-8"></a>
### [Linebender 的圆角方形与曲线几何文章](https://linebender.org/wiki/curves/squircle/) ⭐️ 7.0/10

Linebender 的 wiki 上有一篇由 raphlinus 撰写的技术文章，主题是圆角方形（squircle）和平滑曲线几何。文章面向图形渲染、UI 设计以及曲率连续曲线相关读者。可用材料没有提供文章正文，因此无法核实其具体方法、示例或结论。

hackernews · raphlinus · 11月16日 07:55 · [社区讨论](https://news.ycombinator.com/item?id=50515151)

**「背景」** squircle 是介于正方形与圆形之间的形状，没有单一的数学定义；常见的实现之一是超椭圆，此外还有源自光学领域的另一类定义。Linebender 的文章将 squircle 视为一族可参数化、能在圆形与方形之间连续变化的曲线。超椭圆因用于 iOS 应用图标而广为人知，CSS 中也有 \`corner-shape\` 或 \`figma-squircle\` 等复现方案。

**「社区讨论」** 评论中，darthcircuit 以 Zune 第二代播放器的方向键为例，称 squircle 在实体交互中手感顺滑；mosura 则强调曲线若在导数上保持连续，对需要与物理现实交互的设计很重要。另有 thot\_experiment 分享用于样条与超椭圆/回旋曲线的实验工具，scarecrw 提到四维“sphube”并链接论文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Squircle">Squircle - Wikipedia</a></li>
<li><a href="https://linebender.org/wiki/curves/squircle/">Squircles - Linebender</a></li>
<li><a href="https://elsolitario.org/en/2026/11/16/squircle-css-ios-icon-superellipse/">Squircle in CSS: What It Is and How to Build One</a></li>

</ul>
</details>

**标签**: `#squircles`, `#computer graphics`, `#UI design`, `#curves and splines`, `#geometry`

---

<a id="item-tech-news-9"></a>
### [Marimba：冻结语音编码器支持多类型查询](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Reddit 研究帖介绍了 Marimba：它针对每 8 秒音频窗口只运行一次冻结的 Qwen3-ASR-0.6B 编码器，并用校准后的概率回答用户输入的词项、语言、话轮结束、说话人变化和说话人数等查询。作者报告，在 1,000 道公共问题上，Marimba 在 9 项测试中的 6 项追平或超过 Qwen3-Omni（30B-A3B），但在 Speech Commands 上仍落后；语言识别在 300 条 FLEURS 片段上达到 100%，说话人变化 AUROC 为 0.966–0.980。作者也承认，话轮结束检测在 Smart Turn 自身测试集上的 AUROC 为 0.930，低于 Smart Turn v3.2 的 0.982；在 ICSI 会议上，Marimba 为 0.716，Smart Turn v3.2 为 0.712，基本持平；并且所有任务头在 CochlScene 场景分类上只达到随机水平。代码、Apache-2.0 权重和 pip 包 marimba-audio 已发布，但上述结果来自作者自述的论文摘要，尚待独立验证。

reddit · r/MachineLearning · /u/solanotodesch · 11月16日 15:47

**「背景」** Marimba 建立在已有的 Qwen3-ASR-0.6B 语音识别模型之上：它不重新训练编码器，而是把冻结编码器的输出当作共享特征，再为不同查询接上轻量读出层或校准步骤。作者表示，这是对上周帖子的后续，此次补充了论文、Apache-2.0 权重、代码和在线演示，因此当前材料已从初步预告扩展为可供检查的技术说明。

**「影响」** 对语音机器学习开发者而言，Marimba 的主要价值是同一个冻结编码器可复用于多种查询，并输出校准后的概率；但它的层读出方案在未见任务上失效，因此不能直接当作通用音频分类器部署。已发布的 Apache-2.0 权重和 pip 包可用于复现和基线比较。

**标签**: `#speech recognition`, `#audio foundation models`, `#model calibration`, `#efficient inference`, `#Qwen3-ASR`

---

<a id="item-tech-news-10"></a>
### [duetto：不微调，仅在采样时引导预训练音乐 Transformer 实时伴奏爵士](https://www.reddit.com/r/MachineLearning/comments/1xxkyh3/steering_a_pretrained_music_transformer_at/) ⭐️ 7.0/10

Reddit 用户 /u/GGAllin43 发布了 duetto：一个面向 MIDI 键盘的实时爵士伴奏程序，把演奏者与模型的音符合并为同一事件序列，逐音符预测，并直接使用预训练的 Anticipatory Music Transformer（Thickstun 等，2023）而不做微调，所有控制都放在采样阶段——用规则层遮蔽不允许的 logits（该等待的手、超出音域的音、不在拍点上的低音），并对当前和弦音、强拍引导音、待引用乐句的下一个音加权。乐句取自 Weimar Jazz Database 的转谱独奏，按独奏者换气处切分、移调到曲目和弦上并在一个 chorus 内发展；作者称演示中约 61% 的独奏音符来自引用乐句或主题，其余由模型生成。服务端始终提前采样约 1 秒音乐，并在演奏者弹奏时重采样尚未播放的部分，以降低延迟；速度约为 3080 Ti 上每音符 12 ms（medium）和 18 ms（large），large 模型在 Jetson Orin Nano 上约 90 ms/音符，仍可现场演奏。作者也列出局限：可能偏离演奏者、响应难以预测、模型想法与规则之间的平衡很脆弱（偏置过强像乐句手册，过弱则不像爵士），且未给出量化评测；代码在 GitHub 上免费供非商业使用，演示曲为 160 bpm 的《Autumn Leaves》。

reddit · r/MachineLearning · /u/GGAllin43 · 11月16日 09:19

**「背景：预期式音乐 Transformer」** Anticipatory Music Transformer 是 Thickstun 等人于 2023 年提出的自回归符号音乐模型（arXiv:2306.08620），它把事件序列与控制序列交错排列作为建模对象，使模型在生成一路内容时能“预期”另一路输入，从而支持音乐控制任务。正因为预训练模型本身就建立在交错序列之上，duetto 才能把演奏者的音符与模型的输出拼成同一条事件序列，并把控制放在采样阶段而不是微调阶段完成。

**「对实时 MIDI 伴���开发者的影响」** 对想做实时 MIDI 合奏系统的开发者来说，这个项目说明可以不改动预训练模型权重，把乐理约束全部放到采样阶段——用一个规则层在每次采样前屏蔽非法音符（该等待的手、超出音域的音、不在拍上的低音）并加权当前和弦音与导音——而代价是这套掩码与偏置规则需要按声部、音域和节拍逐条编写和调参，作者也承认偏置过多会像背乐句库、过少则不像爵士，且模型会偏离演奏者。延迟数据（3080 Ti 上每音符约 12 ms/18 ms，Jetson Orin Nano 上大型模型约 90 ms/音符）表明嵌入式现场演出在算力上可行，但代码仅限非商业用途，商用需要另行获得授权；此外作者未提供任何量化评测，效果仍属演示级别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.08620">[2306.08620] Anticipatory Music Transformer</a></li>
<li><a href="https://paperswithcode.co/paper/2306.08620">Anticipatory Music Transformer (arXiv...) | Papers with Code</a></li>

</ul>
</details>

**标签**: `#music generation`, `#transformer models`, `#sampling-time control`, `#real-time interaction`, `#MIDI`

---

<a id="item-tech-news-11"></a>
### [腾讯混元发布 Hy4 flash：224B 总参数、1M 上下文，API 大幅降价](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

腾讯混元发布 Hy4 flash，这是一个总参数 224B、激活 12B 的多模态模型，支持 1M 上下文，并已上线腾讯云 TokenHub、WorkBuddy 和元宝。定价为每百万 Token 输入 0.5 元、输出 2 元，命中缓存时输入为 0.02 元，明显低于 Hy4。官方称其综合效果略优于 Hy4 preview，WorkIndex 单任务成本为 Hy4 preview 的 1/13、Hy4 的 1/20；上述效果与成本数字均为厂商自述，尚无独立验证。11 月 30 日前 WorkBuddy 限免、API 五折，开源仅为计划，尚未落地。

telegram · zaihuapd · 11月16日 07:17

**「背景」** 腾讯混元此前已提供 Hy4 preview 与 Hy4，二者是此次 Hy4 flash 在效果和成本上的参照。Hy4 flash 以 224B 总参数、12B 激活参数和 1M 上下文面向日常任务，官方把 API 定价下调作为主要区分点。

**「影响」** 对开发者而言，直接变化是长上下文多模态推理的单价被压低到每百万输入 Token 0.5 元、缓存命中 0.02 元，使批量文档处理类任务可以先按官方公布的 WorkIndex 成本口径试算再接入；但自托管方案暂时不可行，因为开源只是计划，且实际效果仍需以自有任务集验证厂商宣称的“略优于 Hy4 preview”。

**标签**: `#Tencent Hunyuan`, `#LLM release`, `#multimodal`, `#long context`, `#API pricing`

---

<a id="item-tech-news-12"></a>
### [美国与九国签署《旧金山宣言》共保 AI 供应链](https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/) ⭐️ 7.0/10

11 月 15 日，美国与澳大利亚、印度、以色列、日本、韩国、卡塔尔、新加坡、阿联酋和英国签署《旧金山宣言》，称将共同保护支撑超级智能（SI）的敏感技术和关键基础设施。宣言设立五个工作组，分别负责创新政策框架、SI 在关键领域的应用、SI 全栈供应链协作、安全港与供应链安全枢纽，以及 SI 安全与韧性。目前公布的内容未包含约束性承诺、资金安排、时间表或具体技术标准，因此其直接效果限于启动政府间协调机制，而非已生效的监管或采购规则。

telegram · zaihuapd · 11月16日 10:40

**「背景」** 《旧金山宣言》是在美国负责经济事务的副国务卿雅各布·赫尔伯格（Jacob Helberg）召集的 Pax Silica 创始人闭门会议（Pax Silica Founders Retreat）上签署的，该活动于 2026 年 11 月 15 日在旧金山举行，签署方被称为“Pax Silica 参与方”。据维基百科条目记述，宣言要求参与方设立工作组，最终目标是减少各国在关键矿产、AI 模型和半导体芯片上对美国对手的依赖；美国国务院的声明则称，参与方要先把“必须保护什么”确定下来，再承诺共同保护。

**「影响」** 对半导体和 AI 供应链企业而言，现阶段没有新增的约束性合规义务或截止期限；需要关注的是“安全港与供应链安全枢纽”和“全栈供应链协作”两个工作组后续是否形成出口管制、采购或认证要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/San_Francisco_Declaration_on_the_Secure_Foundations_of_Enduring_Prosperity">San Francisco Declaration on the Secure Foundations of Enduring Prosperity</a></li>
<li><a href="https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/">The San Francisco Declaration on the Secure Foundations of ...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#AI supply chain`, `#international cooperation`, `#AI governance`, `#semiconductors`

---

<a id="item-tech-news-13"></a>
### [亚马逊称 AI 代理窃取 API 密钥以维持模型调用](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

亚马逊报告称，一个 AI 代理活动利用开源渗透测试框架 Artex 驱动，窃取公网暴露的 LiteLLM、Dify 等 AI 应用的 API 密钥，验证后将有效密钥汇入共享池，用于支付更多大模型调用。该活动据称自 10 月 3 日开始，11 月 5 日被亚马逊的诱饵网络 MadPot 截获并阻断。亚马逊以中等信心将该行动归因于中国相关威胁组织，并称并非所有被列出的目标都已失陷，已通知可能受影响的 AWS 客户。上述内容均为亚马逊的单方面说法，来自二手聚合渠道的转述，尚无独立验证。

telegram · zaihuapd · 11月16日 13:00

**「背景」** Artex 是一个开源的代理式 AI 渗透测试框架，攻击者可让 AI 代理自动扫描公网暴露的 AI 应用；LiteLLM、One API、Dify 这类应用通常保存着模型提供商的 API 密钥，一旦暴露，这些密钥就可能被读取和滥用。亚马逊的 MadPot 是一个分布式诱饵传感器网络，此次通过把传感器伪装成可被利用的服务，捕获了代理发出的请求。

**「影响与关注点」** 对运行公网暴露的 LiteLLM、Dify 等 AI 网关或代理服务的团队而言，直接风险是密钥泄露后可被用于支付攻击者自身的模型调用费用，而非仅造成一次性数据泄露；这也意味着密钥轮换与出站调用额度监控需要按已被滥用的前提来核查。已被亚马逊通知的 AWS 客户应优先确认自身密钥是否出现在暴露实例中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/">Amazon Threat Intelligence observes threat actors running ...</a></li>
<li><a href="https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/">AI credential theft campaign used stolen API keys to scale</a></li>
<li><a href="https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html">Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify ...</a></li>

</ul>
</details>

**标签**: `#AI 安全`, `#自主代理`, `#API 密钥`, `#网络犯罪`, `#云安全`

---

<a id="item-tech-news-14"></a>
### [Apple 智能登陆国行 iPad 与 Mac 测试版，云端功能设每日上限](https://www.theverge.com/tech/1034581/apple-intelligence-siri-ai-daily-usage-limits-icloud-subscription) ⭐️ 7.0/10

据 The Verge 报道，Apple 智能（Apple Intelligence）已在中国区（国行）iPad 和 Mac 的测试版上线，用户需升级到 iPadOS 27.3 beta 2 或 macOS 27.3 beta 2 才能体验。同一批测试版中，苹果开始测试部分 Siri AI 与 Apple 智能功能的每日设备使用上限：基础 Siri 命令仍免费且不限量，受限于云端进阶功能，包括多步骤个人情境请求以及图片生成与编辑。报道还称，影响所有 Apple 操作系统的一个 worse\_query 文件沙箱逃逸漏洞已被修复。上述内容来自简短的聚合测试版报道，未披露具体限额数值或漏洞技术细节。

telegram · zaihuapd · 11月16日 20:12

**「背景」** MacRumors 汇总称，苹果表示 WWDC 2026 发布的 Siri AI 及其他 Apple Intelligence 功能不会在国行 iOS 27.3 上提供。此次国行 iPad 和 Mac 的 27.3 beta 2 可体验这些能力，说明中国区上线至少先落在 iPad 和 Mac 测试版，iOS 侧是否同步尚不明确。

**「影响」** 对国行 iPad 与 Mac 测试用户而言，升级后虽然能用上 Apple 智能，但多步骤个人情境请求和图片生成、编辑等云端功能在达到每日上限后当天将不可用，只有基础 Siri 命令不受限制；依赖这些功能做日常工作的用户需要预留替代方案。此外，报道称沙箱逃逸漏洞已在各系统测试版中修复，正式版用户何时获得修复尚未说明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2/">MacRumors: Apple News and Rumors - Page 2</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#China`, `#Siri`, `#security vulnerability`, `#usage limits`

---

<a id="item-tech-news-15"></a>
### [阿里、腾讯、月之暗面据报限制新模型攻击性网络能力](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 7.0/10

据 Bloomberg 报道，阿里巴巴、腾讯和月之暗面等中国头部 AI 公司在新一代模型中削弱了进攻性网络能力，同时提升防御表现。阿里最新旗舰 Qwen 未开放权重，用户无法下载并自定义完整版本；腾讯在 11 月发布 Hy4 前已削减网络功能。报道将这些调整与中国商务部上月公布的出口管制草案联系起来，该草案拟禁止可攻击关键基础设施或政府网络的 AI 工具出口。上述报道为简要汇总，未说明各模型具体削减了哪些能力，也未提供独立验证。

telegram · zaihuapd · 11月17日 02:20

**「背景」** 此次收紧发生在 10 月中国商务部公布出口管制措施之后：据 AP 和 Tech Times 报道，该措施涉及 40 项技术，并首次将 AI 模型权重纳入出口限制范围，路透则将其概括为围绕中国 AI 核心资产划出界线。对于以开放权重为主要发布方式的中国厂商，模型权重和能力能否对外提供，由此成为发布前需要评估的合规问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apnews.com/article/china-export-restrictions-ai-chips-solar-us-5ac381c0c6d6628bbea2e0da7d855a5b">China moves to curb tech exports including for AI and solar ...</a></li>
<li><a href="https://www.reuters.com/business/retail-consumer/chinas-new-export-curbs-draw-line-around-its-ai-crown-jewels-2026-10-28/">China&#x27;s new export curbs draw a line around its AI crown ...</a></li>
<li><a href="https://www.techtimes.com/articles/329196/20261019/chinas-new-ai-export-controls-apply-now-if-you-licensed-deployed-covered-chinese-models.htm">China&#x27;s New AI Export Controls Apply Now if You Licensed or ...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#export controls`, `#AI safety`, `#open-weight models`, `#China AI industry`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [卢特尼克因英伟达间谍风波受质询，其子掌管的 Cantor 减持英伟达](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 7.0/10

据 CNBC 报道，美国商务部长霍华德·卢特尼克因其前公司 Cantor Fitzgerald 与英伟达的关系面临质询；CNBC 对证券文件的分析显示，该公司报告的英伟达持股数量在 2025 年 9 月至 2026 年 3 月间下降 49%，至 178 万股，但目前没有证据表明存在不当行为。

rss · CNBC Finance · 11月16日 12:14

**「背景」** 美国商务部主管出口管制；卢特尼克曾任坎托·菲茨杰拉德负责人，该公司现由其子经营。据 Axios 报道，他曾抵制对涉嫌将英伟达先进芯片转运至中国的 Megaspeed 采取行动。

**「影响」** 美国商务部已针对中国数据中心使用方面的漏洞采取行动，这是 Nvidia 丑闻后的首个政策回应；相关限制若落地，可能进一步收紧 Nvidia 芯片对华销售，并直接影响依赖这些芯片的中国数据中心运营商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c67429m3vem3o">How a sex scandal at Nvidia is putting pressure on the White House</a></li>
<li><a href="https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html">Howard Lutnick&#x27;s sons&#x27; Nvidia ties amid Jensen Huang China ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/nvidia-commerce-china-lutnick.html">Nvidia fallout: Commerce targets loophole for China &#x27;s data center use</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#U.S. export controls`, `#conflict of interest`, `#Commerce Department`, `#semiconductor industry`

---

<a id="item-finance-news-2"></a>
### [英特尔及 CEO 陈立武遭股东集体诉讼](https://www.investing.com/news/stock-market-news/intel-sued-by-shareholders-following-29-stock-plunge-5028171) ⭐️ 7.0/10

英特尔及 CEO 陈立武、CFO 津斯纳遭股东集体诉讼，股东指控他们在公司 10 月 29 日发布不及预期的第四季度营收和利润预测之前，隐瞒了 PC 需求疲软和库存积压的影响；预测发布后的次日，公司股价暴跌 28.6%，市值蒸发约 1400 亿美元。该诉讼由一家密歇根州养老基金牵头，上周五在美国圣何塞联邦法院提起，代表 2026 年 7 月 23 日至 10 月 29 日期间买入股票的投资者。

telegram · zaihuapd · 11月16日 11:10

**「背景」** 陈立武自 2025 年起出任英特尔 CEO；这起集体诉讼拟代表 2026 年 7 月 23 日至 10 月 29 日买入股票的投资者，并已在圣何塞联邦法院提起，指控称公司在 10 月 29 日发布不及预期的第四季度营收和利润预测前，隐瞒了 PC 需求疲软和库存积压。

**「影响」** 美国政府持有的英特尔 9.9%股份因这轮股价暴跌账面缩水逾 100 亿美元，尽管仍约为其买入价的三倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lip-Bu_Tan">Lip - Bu Tan - Wikipedia</a></li>
<li><a href="https://finance.yahoo.com/markets/article/intel-stock-plunges-nearly-29-its-worst-day-since-1974-205955309.html">Intel stock plunges nearly 29%, its worst day since 1974</a></li>

</ul>
</details>

**标签**: `#Intel`, `#shareholder class action`, `#stock plunge`, `#earnings guidance`, `#semiconductors`

---