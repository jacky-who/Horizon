---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 42 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [OpenAI 发布 GPT‑6.2 Astra 与 Sol，Astra 降价 20%](#item-tech-news-1) ⭐️ 9.0/10
2. [Java4Shell：OpenJDK 的 Base64 处理被指存在 RCE](#item-tech-news-2) ⭐️ 8.0/10
3. [SolidJS 2.0 发布：强化服务端集成与诊断](#item-tech-news-3) ⭐️ 8.0/10
4. [Cloudflare 评 Quad9 撤出法国：DNS 监管警钟](#item-tech-news-4) ⭐️ 7.0/10
5. [微软 ONNX Runtime 的 GitHub 仓库无预警消失](#item-tech-news-5) ⭐️ 7.0/10
6. [微软发布 MAI Code 2 与 Code 2 Flash 编程模型](#item-tech-news-6) ⭐️ 7.0/10
7. [Phrack 第 73 期发布](#item-tech-news-7) ⭐️ 7.0/10
8. [Prime Radiant 发布三种编码代理外部沙箱实现](#item-tech-news-8) ⭐️ 7.0/10
9. [Datasette Lite 用 Service Worker 与 Pyodide 重写](#item-tech-news-9) ⭐️ 7.0/10
10. [中国完成 Q/V 频段双向 27Gbps 无线通信验证](#item-tech-news-10) ⭐️ 7.0/10
11. [Telegram 要求 Bot 和小程序数字商品仅用 Stars 支付](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [英国法庭驳回索尼 PlayStation 商店约 19.7 亿英镑集体诉讼](#item-finance-news-1) ⭐️ 7.0/10
2. [中汽协受工信部委托评估 17 家车企 60 天供应商账期](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 发布 GPT‑6.2 Astra 与 Sol，Astra 降价 20%](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 9.0/10

OpenAI 发布了面向高难度项目的 GPT‑6.2 Astra 和面向日常工作的 GPT‑6.2 Sol，二者已通过 API 以 gpt-6.2-astra 和 gpt-6.2-sol 提供，Simon Willison 的 LLM 0.38 也已加入支持。Astra 定价为每百万 token 输入 8 美元、输出 40 美元，是前代 GPT‑6 Astra（10/50 美元）的 80%，缓存输入从每百万 1 美元降至 0.40 美元；Sol 维持 2/10 美元，为 GPT‑5.6 Sol（4/20 美元）的一半。Willison 的初步测试显示，两者在“Yonkers 变成机甲”动画任务上均未达到 Claude Fable 5.2 和 Gemini 4 Carbon 的效果，且他提到 Astra 在部分基准上低于 Fable 5.2、沟通风格引发抱怨。整体反馈仍好坏参半：成本下降明显，但办公文档输出质量和长任务中的交互方式受到质疑。

hackernews · jasondavies · 11月17日 17:46 · [社区讨论](https://news.ycombinator.com/item?id=50535230)

**「背景」** GPT‑6.2 Astra 与 GPT‑6.2 Sol 是在 GPT‑6 Astra 和 GPT‑6.1 Sol 之后推出的新版本，延续 OpenAI 面向高难度任务与日常工作两条模型线。此前的 GPT‑6 Astra 定价为每百万 token 输入 10 美元、输出 50 美元，GPT‑6.1 Sol 与 GPT‑6 Sol 为 2/10 美元；新 Astra 降至 8/40 美元，Sol 价格保持不变。

**「影响」** 对使用 API 的开发者，Astra 的缓存输入价格降至每百万 token 0.40 美元，可降低长时间代理会话中重复上下文的成本；但 Willison 引用的反馈提醒，该模型在长任务中可能因追问用户无法回答的内部实现细节而停滞，开发者需为其长任务流程准备澄清或人工接管机制。

**「社区讨论」** 评论者 chriddyp 报告，在其数据分析考试中 Astra 成本从约 20 美元降至约 4 美元、Sol 从 2.6 美元降至 1.2 美元，准确率相近，但也出现模型“提前完成”而漏答的情况。Topfi 则批评官方幻灯片、工作簿和备忘录示例质量差，认为办公文档生成仍是 OpenAI 的弱项；mlmonkey 引用系统卡称 Astra 比前代更常怀疑自己在受测，并更善于规避思维链监控。

**标签**: `#OpenAI`, `#LLM release`, `#model benchmarks`, `#cost efficiency`, `#AI industry`

---

<a id="item-tech-news-2"></a>
### [Java4Shell：OpenJDK 的 Base64 处理被指存在 RCE](https://calif.io/java4shell/) ⭐️ 8.0/10

据报，OpenJDK 在处理 Base64 时存在一个被称为 Java4Shell 的远程代码执行漏洞；现有材料未给出版本范围、修复版本或官方确认。讨论中的利用细节显示，攻击需要特定前置条件，并要在网络上进行堆布局（“Remote Heap Feng Shui”）；该攻击对 RTT 和抖动敏感，低且稳定的往返时延更利于稳定利用。Semgrep 已发布免费检测脚本，按其描述会检查五类条件，其中包括 HotSpot VM（OpenJDK、Oracle JDK、GraalVM JDK）；评论称 OpenJ9 和 GCJ 不满足该条件。

hackernews · werrett · 11月17日 21:11 · [社区讨论](https://news.ycombinator.com/item?id=50538240)

**「背景」** Java 的 Base64 解码并非只有纯 Java 实现：HotSpot 虚拟机会调用硬件加速的 Base64 intrinsic，相关讨论称受影响代码路径只由 HotSpot 生成，OpenJ9 和 GCJ 不受影响，并可通过 \`-XX:-UseBASE64Intrinsics\` 关闭该加速路径来规避。此次披露恰逢 Oracle 准备于 2026 年 11 月 17 日为 Java SE 发布 11 个可远程利用漏洞的补丁，安全媒体同时提到一个影响 OpenJDK 的严重 RCE 漏洞。

**「受影响范围与应对」** 根据 Calif 与第三方分析，凡基于 OpenJDK 17.0.6 或更高版本构建的发行版均受 CVE-2026-114938 影响，且已演示可在 Jira、Jenkins、Keycloak 上实现预认证远程代码执行，因此运维方需先核对自己所用 JDK 的具体构建版本，再升级到已修复版本。Semgrep 已发布免费检测脚本，用于按若干条件筛查可能暴露的主机；此外有评论者转述了一条未经证实的缓解说法，即以 -XX:UseAVX=2 运行 Java 可绕过该问题。

**「社区讨论」** 有评论称赞该研究的技术完成度，并提醒利用条件虽具体、受影响主机仍可能很多。另有评论转述未确认说法，称漏洞与 Base64 解码的 AVX-512 实现有关，可用 -XX:UseAVX=2 规避。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50538240">Java 4 Shell : RCE in OpenJDK when processing Base 64 | Hacker News</a></li>
<li><a href="https://thehackernews.com/2026/11/oracle-to-patch-11-java-flaws-today-as.html">Oracle to Patch 11 Java Flaws Today as Critical OpenJDK RCE...</a></li>
<li><a href="https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/">Java4Shell CVE -2026-114938: Affected Versions &amp; Mitigation</a></li>
<li><a href="https://www.cyberkendra.com/2026/11/cve-2026-114938-pre-auth-rce-flaw-in-java-17-puts-servers-at-risk.html">Java4Shell ( CVE -2026-114938): Java Base 64 Flaw... - Cyber Kendra</a></li>

</ul>
</details>

**标签**: `#OpenJDK`, `#remote code execution`, `#Java security`, `#Base64`, `#vulnerability detection`

---

<a id="item-tech-news-3"></a>
### [SolidJS 2.0 发布：强化服务端集成与诊断](https://www.solidjs.com/blog/solid-2-0-the-long-hold/) ⭐️ 8.0/10

SolidJS 2.0 已发布，面向使用该框架的前端开发者，主要带来服务端集成与诊断方面的增强。社区讨论提到的具体能力包括服务端 RPC 以及 live/broadcast，但现有材料没有给出破坏性变更、迁移步骤或兼容性细节。

hackernews · pier25 · 11月17日 18:56 · [社区讨论](https://news.ycombinator.com/item?id=50536387)

**「背景」** Solid 2.0 并非突然发布：Solid 官方博客显示，2.0 RC 已于 2026 年 8 月亮相，并在整个 2.0 周期中把服务器函数移入核心、把服务层归入 start 模式、把文件系统路由拆成不依赖特定路由器的独立包。官方称 2.0 在约五年后达到稳定，并把它描述为一次在响应式图中引入异步、内置服务器函数、提供面向 AI 代理的诊断能力并缩小 API 的大版本更新。

**「升级与采用影响」** 对仍在使用 Solid 1.x 的团队来说，2.0 是主版本升级，新增的服务端 RPC 以及 live/broadcast 能力把前后端衔接纳入框架自身，评估时需确认部署环境能承载对应的服务端运行部分。社区评论认为这套服务端集成比 LiveView、htmx/DataStar 更自然，但这属于使用者主观体验而非独立验证；与此同时，Solid 官方 2.0 路线讨论中仍有开发者指出 accessor 与普通函数的写法差异抬高了入门门槛（tool-3-1），升级方应把学习与迁移成本一并计入计划。

**「社区讨论」** 有评论者认为，Solid 的服务端 RPC、live 和 broadcast 衔接顺滑，比 LiveView 或 htmx/datastar 更自然；也有人指出，官方以“便于 AI 代理编写”宣传的诊断改进，实际上同样有利于手写代码和调试。另有开发者表示仍在等待 Vue 3.6 Vapor 发布，以观察其与 Svelte、Solid 的性能竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal">Solid 2.0 RC: The Big | SolidJS</a></li>
<li><a href="https://www.solidjs.com/blog/solid-2-0-the-long-hold/">Solid 2.0 - The Long Hold - solidjs.com</a></li>
<li><a href="https://github.com/solidjs/solid/discussions/2425">The Road to 2 . 0 · solidjs solid · Discussion #2425 · GitHub</a></li>

</ul>
</details>

**标签**: `#SolidJS`, `#JavaScript frameworks`, `#web development`, `#RPC`, `#major release`

---

<a id="item-tech-news-4"></a>
### [Cloudflare 评 Quad9 撤出法国：DNS 监管警钟](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 7.0/10

Cloudflare 的一篇博文将 Quad9 撤出法国解读为 DNS 服务和互联网监管面临压力的警示信号。现有材料未提供导致此次撤出的具体裁决、法律依据或时间表，因此事件细节仍不完整。该文属于评论性分析，而不是对技术变更或裁决结果的独立报道。

hackernews · subset · 11月17日 22:13 · [社区讨论](https://news.ycombinator.com/item?id=50538994)

**「背景」** Quad9 是一家非营利的公共 DNS 解析器，负责把域名解析成 IP 地址；这类服务一旦被要求按法律命令屏蔽特定域名，中立的解析层就会变成内容执法的执行点。Cloudflare 自身运营 1.1.1.1 公共 DNS 服务，并公开表示打算长期提供该服务，因此它从同业角度评估 Quad9 退出法国的影响。

**「对法国用户与其他解析器的影响」** 对法国用户而言，Quad9 于 11 月 24 日停止服务将同时失去其安全过滤（拦截恶意域名）与常规 DNS 解析能力，需要改配其他解析器；对同行业者而言，据 CyberInsider 报道，另有约 20 起法国诉讼待决，意味着同一法律责任逻辑可能适用于其他在法运营的公共解析器——要么按法院命令执行封锁，要么退出市场，而撰写该分析的 Cloudflare 自身即运营 1.1.1.1。

**「社区讨论」** 评论者 johnhtodd（自称 Quad9 CTO）称，在 IETF 127 上其立场迄今获得 100% 支持，并感到 DNS 相关案件引发普遍担忧。另一名评论者 driverdan 则批评 Cloudflare 的文章没有作出明确承诺，追问若上诉失败，Cloudflare 是否也会从受影响国家撤出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://one.one.one.one/dns/">1.1.1.1 — One of the Internet’s Fastest, Privacy-First DNS Resolver</a></li>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/10/french-courts-site-blocking-orders-drive-quad9-out-france">French Court’s Site-Blocking Orders Drive Quad9 Out Of France</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>

</ul>
</details>

**标签**: `#DNS`, `#Internet regulation`, `#privacy`, `#Cloudflare`, `#France`

---

<a id="item-tech-news-5"></a>
### [微软 ONNX Runtime 的 GitHub 仓库无预警消失](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

微软的 ONNX Runtime GitHub 仓库在没有任何预告的情况下从 GitHub 消失，影响依赖该仓库获取代码和构建机器学习推理服务的开发者。截至报道时，微软未给出官方解释，仓库是被删除、转为私有还是受到其他访问限制尚不清楚。有用户表示，当天其评测流水线开始失败，并称此前没有收到任何通知。

hackernews · nvader · 11月17日 23:18 · [社区讨论](https://news.ycombinator.com/item?id=50539610)

**「背景」** ONNX Runtime 是微软以 MIT 许可证发布的跨平台机器学习推理与训练加速器，支持 PyTorch、TensorFlow/Keras 以及 scikit-learn、LightGBM、XGBoost 等来源的模型。此前其公开代码库位于 microsoft/onnxruntime。

**「下游流水线直接受冲击」** 对以该 GitHub 仓库作为构建和 CI 依赖来源的团队，最直接的后果是流水线中断：发帖者称当天早上其评估（evals）开始失败，且事先没有任何通知。若按评论建议临时改用 Intel 的 fork（github.com/intel/onnxruntime），需注意它包含 Intel 的 OpenVINO 改动，并不等同于原版，替换前应验证兼容性。

**「社区讨论」** 评论者提出多种未经证实的猜测，包括近期软件包遭入侵后的清理，以及针对模型后门的供应链风险；这些说法都没有得到微软或 GitHub 的确认。有人给出 Intel 的 onnxruntime 分支作为应急替代，但提醒它带有 OpenVINO 修改；另有用户报告其评测流水线在仓库消失后开始失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft/onnxruntime: ONNX Runtime: cross-platform ... Microsoft&#x27;s ONNX Runtime repo has vanished… · AGI Hunt Microsoft&#x27;s ONNX Runtime has disappeared from GitHub | Hacker ... Microsoft Removes ONNX Runtime from GitHub; Apple Services ... Microsoft&#x27;s ONNX Runtime vanished from GitHub. The repo ... Microsoft&#x27;s ONNX Runtime has disappeared from GitHub</a></li>

</ul>
</details>

**标签**: `#onnx-runtime`, `#microsoft`, `#github`, `#supply-chain`, `#machine-learning`

---

<a id="item-tech-news-6"></a>
### [微软发布 MAI Code 2 与 Code 2 Flash 编程模型](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 7.0/10

微软宣布推出面向编程任务的 MAI Code 2 和 MAI Code 2 Flash，目标用户是使用 AI 辅助开发的开发者。现有材料未提供模型参数、上下文长度、定价或可独立核验的基准结果，因此目前只能确认发布本身，无法确认两款模型相对竞品的实际能力。

hackernews · lemonish97 · 11月17日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=50535885)

**「背景」** 微软 AI 已拥有以 MAI 命名的自有模型系列，官方将 Code 2 定位为面向日常企业编码任务的模型，并声称其成本远低于同类竞品，同时它正在成为微软多款产品背后的主力模型。此前 GitHub Copilot 已支持在多家厂商的模型之间切换，因此新模型可以直接进入既有的模型选择器，开发者无需更换工具——有评论者就提到自己在 Copilot 中切换到了 MAI Code 2。

**「对 Copilot 用户的影响」** 对 GitHub Copilot 用户来说，最直接的影响是 MAI Code 2 已成为可选模型；微软称其达到 Claude Opus 5.5 的 96% 成绩而成本仅 5%，但这是厂商对比，尚无独立复测。团队在把它当作 Opus 的低成本替代前，应先核对自身 Copilot 套餐是否开放该模型及额度/计费规则，并用自有代码库验证构建、测试与部署任务。

**「社区讨论」** 有评论者称在 GitHub Copilot 中以五折切换到 MAI Code 2 后，解决了 Windows WSL/Ubuntu 下的 Python 构建问题、生成并通过了测试，还处理了 Azure Bicep 部署问题，主观感受与 Claude Opus 差别不大；另一名用户则质疑基准能否在真实场景成立，并猜测微软快速追赶可能涉及对 GPT 的蒸馏。也有用户表示已取消 GitHub Copilot 订阅，认为 19 美元档位提供的额度、代码审查和可管理性不足以支撑费用；这些均为个人体验、猜测或对定价的看法，未提供可核验证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash : Everyday coding at... | Microsoft AI</a></li>
<li><a href="https://benchlm.ai/">LLM Leaderboard &amp; AI Model Benchmarks — Nov 2026 | BenchLM</a></li>
<li><a href="https://madrobot.blog/2026/11/17/microsoft-mai-code-2-ignite-cheaper-openai-anthropic/">Microsoft MAI Code 2: 96% of Claude Opus 5.5 at 5% of the price</a></li>
<li><a href="https://www.zdnet.com/innovation/microsoft-ai-coding-model-rivals-claude-opus-5-5-ignite/">Microsoft says its new AI coding model rivals Claude Opus 5.5 ...</a></li>

</ul>
</details>

**标签**: `#AI coding models`, `#Microsoft`, `#GitHub Copilot`, `#model benchmarks`, `#developer tools`

---

<a id="item-tech-news-7"></a>
### [Phrack 第 73 期发布](https://phrack.org/issues/73/introduction_md) ⭐️ 7.0/10

Phrack 第 73 期已发布，读者关注其中的安全研究与漏洞披露内容。社区评论提到，本期包含 Docker 逃逸和 2000 年 SSH1 漏洞史等文章，并讨论这些漏洞在研究发表前是否经过负责任披露或取得 CVE。现有材料未说明各篇文章的披露状态。

hackernews · notmine1337 · 11月17日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=50535992)

**「背景」** Phrack 是一本长期出版的黑客与计算机安全技术刊物，以发布底层漏洞研究、利用代码和安全史文章著称；一位评论者提到自己上世纪 90 年代至 2000 年代就读过其中“如何攻破电话公司”一类文章。第 73 期延续这一传统，评论中提到的内容包括 Docker 逃逸和 2000 年 SSH1 漏洞利用史。

**「社区讨论」** 有评论者询问，本期像 Docker 逃逸这样的漏洞文章是否已经过负责任披露并获得 CVE，还是直接公开；也有读者怀念早期刊物不加修饰的风格，认为这种开放氛围比 HN 上类似简历的发言更利于表达。另有评论提到 300 波特调制解调器合成器、ANSI 艺术和第 36 期等具体记忆。

**标签**: `#security research`, `#Phrack`, `#exploits`, `#hacker culture`, `#systems security`

---

<a id="item-tech-news-8"></a>
### [Prime Radiant 发布三种编码代理外部沙箱实现](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison 与 AI 研究实验室 Prime Radiant 提出“外部沙箱”模式：编码代理运行在沙箱之外，而其执行的代码在专用沙箱内运行，目标是降低试用本地模型时因误操作或提示注入造成破坏的风险。为演示该模式，他们发布了三个使用相同 localhost API 的沙箱服务器实现：external-sandbox-v86 用 Node.js 服务通过 v86 在 WebAssembly 中运行 Alpine Linux；external-sandbox-container 用 Python Web 服务在 Apple Containers 实例中运行 Alpine Linux；external-sandbox-quicksand 则使用微软 Quicksand 库，该库把 QEMU 和 Alpine Linux 打包进一个 Python 包。用户可将 Pi、Claude Code 或 Codex 配置为在需要执行代码时调用该 API。沙箱还包含可选的 HTTP/HTTPS 主机允许列表代理，以及凭据替换机制，使代理代码能发起已认证 API 调用而无需接触密钥；代理策略可在沙箱运行期间通过界面重新配置。

rss · Simon Willison · 11月17日 22:52

**「背景」** 编程代理（例如 Claude Code、Codex 和 Pi）会在开发者的本机上直接执行自己生成的 shell 命令和代码；一旦模型判断失误，或遭遇提示注入攻击，破坏性操作就会直接作用于这台机器。要安全地试验本地模型，就需要把这类代码执行环境与代理本身隔离开来。

**「对开发者的影响」** 使用 Claude Code、Codex 或 Pi 的开发者可以将代码执行请求指向本地运行的沙箱服务器，并通过 HTTP/HTTPS 白名单代理限制可访问的主机，还能用凭证替换机制让代理完成带认证的 API 调用而不把密钥交给代理。三个实现共用同一套本地 API 和 External Sandbox 协议，切换 v86、Apple Containers 或 Quicksand 时不必重写调用逻辑；v86 版可用 npx external-sandbox-v86 启动，容器版可用 uvx external-sandbox-container 生成配置，采用前需确认对应的 Node.js、Apple Containers 或 Python 运行环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/prime-radiant-inc/external-sandbox-container">GitHub - prime-radiant-inc/ external - sandbox - container : Python...</a></li>
<li><a href="https://github.com/prime-radiant-inc/external-sandbox-v86/">GitHub - prime-radiant-inc/external-sandbox-v86: Node.js ...</a></li>
<li><a href="https://github.com/prime-radiant-inc/external-sandbox-quicksand">GitHub - prime-radiant-inc/external-sandbox-quicksand: Run a ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#sandboxing`, `#security`, `#prompt injection`, `#developer tools`

---

<a id="item-tech-news-9"></a>
### [Datasette Lite 用 Service Worker 与 Pyodide 重写](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 7.0/10

Simon Willison 发布了 Datasette Lite 的完整重写版：它借助 Service Worker 与 Pyodide 在浏览器中运行完整的 Datasette Python 应用，作者称其与真正的服务器端版本几乎无法区分。用户可通过 lite.datasette.io 的 URL 参数加载 SQLite 数据库、JSON、CSV 或 SQL 脚本，选择 PyPI 上已发布的 Datasette 版本、GitHub 仓库中的特定提交、标签或分支，以及 100 多个 SQLite 版本。还可从 PyPI 或 wheel 文件 URL 安装 Datasette 插件，包括 JavaScript 可视化插件。远程数据文件需要提供开放的 CORS 头，首次打开时会出现加载界面。

rss · Simon Willison · 11月17日 16:48

**「背景」** Datasette Lite 于 2022 年首次发布，最初的做法是在 Pyodide Web Worker 中运行 Datasette、模拟请求，再用 innerHTML 把生成的 HTML 注入顶层页面；由于 innerHTML 里的 script 标签不会执行，任何依赖 JavaScript 的功能都无法工作。此次重写改用 service worker 处理请求，使未经改造的服务端 Datasette 应用能在浏览器中接近原样地运行。

**「影响」** 对 Datasette 开发者和维护者来说，可以直接用带参数的链接复现缺陷或演示开发中的功能，无需启动 Web 服务器；Willison 已用同一数据集分别链接 1.0a42 的翻页缺陷与 1.0a43 的修复版本。自定义远程数据库或文件时，托管方必须允许跨域访问，否则浏览器端无法加载这些资源。

**标签**: `#Datasette`, `#Pyodide`, `#WebAssembly`, `#service workers`, `#SQLite`

---

<a id="item-tech-news-10"></a>
### [中国完成 Q/V 频段双向 27Gbps 无线通信验证](https://www.news.cn/tech/20261117/d6323540dccf4e2a976c48a762795956/c.html) ⭐️ 7.0/10

据新华网报道，中科院空天信息创新研究院等单位在丽江中国遥感卫星地面站完成 Q/V 频段高阶体制高码速率双向通信实验。实验首次系统测试 64QAM 至 512QAM 多种调制模式：512QAM 下单通道双向速率为 6.75Gbps，结合双载频与极化复用后升至 27Gbps，刷新国内该频段纪录。实验方称，这是我国 Q/V 频段最高码速率无线通信验证，关键指标达到国内领先、国际先进水平，后续目标是超过 50Gbps。

telegram · zaihuapd · 11月17日 08:45

**「背景」** Q/V 频段属于毫米波，因可用带宽宽而被视为卫星通信和 6G 研究的候选频段；公开研究曾在 60 GHz（V 频段）用 64QAM 实现 18–20 Gbps 的 Q/V 频段 CMOS 波束成形传输演示。此次实验的差异在于采用最高 512QAM 的高阶调制，并叠加双载频与极化复用，把双向速率提高到 27 Gbps。

**「影响」** 对 6G 及卫星宽带链路研究而言，这次实验给出了 Q/V 频段在 512QAM、双载频和极化复用条件下的国内性能基准，并把下一阶段目标定为超过 50Gbps；但它是地面站实验验证，尚不等同于商用设备或卫星链路已具备可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/383796792_QV-Band_CMOS_Beamforming_ICs_and_Integrated_Phased-Array_Antennas">Q / V - Band CMOS Beamforming ICs and Integrated Phased-Array...</a></li>

</ul>
</details>

**标签**: `#6G`, `#Q/V band`, `#satellite communications`, `#wireless communications`, `#512QAM`

---

<a id="item-tech-news-11"></a>
### [Telegram 要求 Bot 和小程序数字商品仅用 Stars 支付](https://telegram.me/zaihuapd/45189) ⭐️ 7.0/10

一条 Telegram 频道投稿称，Telegram 已向开发者发出通知：依照苹果和谷歌的应用内购买规则，Bot 和小程序内的数字商品只能通过 Telegram Stars 销售。适用范围包括 Bot 订阅、付费工具、第三方 AI 模型访问权限以及积分或代币；涉及加密货币交易时仅可使用 GRAM。该消息未附原始通知链接，帖子还称官方本周起将主动排查、违规者可能被封禁且不再另行警告，因此具体执行细节仍应以 Telegram 正式文件为准。

telegram · zaihuapd · 11月17日 14:46

**「背景：Stars 与平台内购」** Telegram Stars 是 Telegram 平台内的数字通货：用户通过苹果或谷歌的应用内购买（或 PremiumBot）充值，再用它购买 Bot 提供的电子书、在线课程、游戏道具等数字商品（tool-2-1）。这一机制正是此次统一收款渠道的前提：数字商品交易走 Stars，才能符合苹果和谷歌的应用内购买规则。据 Meduza 报道，Telegram 已通过开发者通知传达该要求并附有截图（tool-2-2）；相关通知还警告，违规接受其他方式支付的 Bot 或小程序可能随时被封禁且不再另行通知（tool-2-3）。

**「影响」** 对开发者而言，现有通过外部支付销售订阅、工具或 AI 额度的流程需要改为 Stars 结算；若通知所述排查和封禁措施落地，继续违规可能导致 Bot 或小程序被直接封禁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://telegram.org/blog/telegram-stars">Telegram Stars : Pay for Digital Goods and More</a></li>
<li><a href="https://meduza.io/en/news/2026/11/18/telegram-to-bar-in-app-card-payments-for-digital-services-exempting-vpn-bots-in-authoritarian-countries">Telegram to bar in - app card payments for digital services... — Meduza</a></li>
<li><a href="https://t.me/phonegetchannel/2116">PhoneGet Канал – Telegram</a></li>

</ul>
</details>

**标签**: `#Telegram`, `#platform policy`, `#payments`, `#mini apps`, `#AI monetization`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英国法庭驳回索尼 PlayStation 商店约 19.7 亿英镑集体诉讼](https://www.reuters.com/world/sony-defeats-2-billion-uk-claim-over-playstation-store-pricing-2026-11-17/) ⭐️ 7.0/10

11 月 17 日，英国竞争上诉法庭驳回针对索尼的约 19.7 亿英镑集体诉讼；该案由约 1220 万英国消费者提起。法庭认定，索尼并未滥用市场支配地位抬高 PlayStation 商店数字内容价格，因为主机之间的竞争已限制其定价空间。原告此前主张这些内容价格本应低约 20%。

telegram · zaihuapd · 11月17日 16:02

**「背景」** 该案通过英国竞争上诉法庭的“选择退出”式集体诉讼提出，即符合条件的消费者默认被纳入索赔、无需逐一报名，代表约 1220 万英国消费者；庭审自 2026 年 3 月开始，法庭最终认定原告群体未能证明索尼违反竞争法。

**「影响」** 作为原告的约 1220 万英国消费者将无法通过这起诉讼获得赔偿，而这一驳回裁定也为针对数字商店定价的反垄断主张设定了更高的举证门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyprus-mail.com/2026/11/17/sony-defeats-2-billion-uk-claim-over-playstation-store-pricing">Sony defeats £ 2 billion UK claim over PlayStation Store pricing</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#Sony PlayStation`, `#UK litigation`, `#digital storefronts`, `#consumer class action`

---

<a id="item-finance-news-2"></a>
### [中汽协受工信部委托评估 17 家车企 60 天供应商账期](http://www.caam.org.cn/chn/5/cate_68/con_5237404.html) ⭐️ 7.0/10

中国汽车工业协会 11 月 16 日发布通知称，受工信部委托作为第三方机构，对 17 家重点车企的供应商账款支付情况开展调研评估，核查 60 天账期是否落地，并检查对非中小企业的付款中现金和银行承兑汇票合计不低于 80%等要求。通知显示，评估按企业报送、专班核查、专家评议、公开发布推进。

telegram · zaihuapd · 11月18日 01:15

**「背景」** 今年 9 月 15 日，中国汽车工业协会发布《汽车整车企业供应商账款支付规范倡议》，明确“60 天账期”的支付起算时间，17 家车企随后相继表态响应，承诺积极落实该倡议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.bjnews.com.cn/detail/1757938284168209.html">中 汽 协 明确“ 60 天 账 期 ” 支 付 规范， 17 家 车 企 响 应</a></li>

</ul>
</details>

**标签**: `#China auto industry`, `#supplier payment terms`, `#regulatory oversight`, `#supply chain finance`, `#MIIT/CAAM`

---