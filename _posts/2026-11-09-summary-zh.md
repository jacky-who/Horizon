---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 从 29 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [llama-modchip 宣称 64GB 内存无 GPU 跑 284B DeepSeek](#item-tech-news-1) ⭐️ 7.0/10
2. [Outlook.com 据报拒收未配置 DMARC 域名的邮件](#item-tech-news-2) ⭐️ 7.0/10
3. [高盛据报撤下银行家与交易员使用的 Claude Code](#item-tech-news-3) ⭐️ 7.0/10
4. [英伟达董事会调查针对黄仁勋的情报行动](#item-tech-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [llama-modchip 宣称 64GB 内存无 GPU 跑 284B DeepSeek](https://github.com/synchopate/llama-modchip) ⭐️ 7.0/10

GitHub 项目 synchopate/llama-modchip 宣称可在 64GB 内存、无 GPU 的机器上运行 284B 参数的 DeepSeek 模型，但这仍是项目自述，尚无独立复现确认其效果。Hacker News 讨论集中在激进量化的代价，以及它相对原生 llama.cpp 是否带来实际收益。有评论者用 Nemotron 在 Ryzen 7945HX、96GB DDR5 上对比后称，CPU 推理速度与 llama.cpp 大致相同，仅预填充似乎更快，并且未在仓库的“modchip setup”中找到 DeepSeek 选项。

hackernews · joshcsimmons · 11月8日 10:22 · [社区讨论](https://news.ycombinator.com/item?id=50411961)

**「背景」** MoE（混合专家）模型每个 token 只激活部分专家，因此 284B 模型的单 token 计算量远低于同等参数量的稠密模型，但全部权重仍须驻留内存；量化则通过降低权重精度来压缩内存占用。该项目 v2.1 版本此前已声称可在纯 CPU、256K 上下文下运行 30B 稀疏 MoE，速度约 20–60.4 tok/s。当前仓库页面标为 v2.4.0，称 284B DeepSeek-V4-Flash 可在不足 59 GiB RAM 下运行，但这仍属项目自述，尚非独立复测结果。

**「影响」** 对希望在消费级内存上运行大 MoE 模型的开发者，实际决策应基于同一模型和硬件上相对 llama.cpp 的预填充、解码速度与量化质量对比；现有试跑只覆盖 Nemotron，DeepSeek 路径尚未得到验证。

**「社区讨论」** Hacker News 评论者对仓库的实际增量存在分歧：aappleby 称在 Ryzen 7945HX 与 96GB DDR5 上试跑 Nemotron 时，CPU 推理与 llama.cpp 大致相当、仅预填充更快，并指出未找到 DeepSeek 的“modchip setup”入口。armcat 则认为激进量化呈非线性退化、通常 4 bit 附近才是规模与性能的平衡点，boredatoms 也批评仓库没有把量化方案讲清楚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/synchopate/llama-modchip">GitHub - synchopate/llama-modchip: Run 284B DeepSeek-V4 ...</a></li>
<li><a href="https://github.com/synchopate/llama-modchip/tree/main">GitHub - synchopate/llama-modchip: ♟️ llama-modchip v2.1: Run ...</a></li>

</ul>
</details>

**标签**: `#local-llm-inference`, `#quantization`, `#moe-models`, `#consumer-hardware`, `#llama.cpp`

---

<a id="item-tech-news-2"></a>
### [Outlook.com 据报拒收未配置 DMARC 域名的邮件](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) ⭐️ 7.0/10

据 Mailroute 博客报道，Outlook.com 正在拒收来自未配置 DMARC 的域名所发送的邮件，这将影响所有向该平台发信的邮件服务器运营者。该报道属于二手信息，微软尚未公开确认具体规则、生效时间或适用范围。由于原始来源没有提供可验证的退信样本或微软文档，目前无法判断这是全量策略、灰度测试，还是仅涉及部分过滤路径。

hackernews · xmddmx · 11月8日 19:20 · [社区讨论](https://news.ycombinator.com/item?id=50416158)

**「背景」** DMARC 是一种邮件认证策略，建立在 SPF 与 DKIM 检查之上；域名所有者通过在 DNS 中发布记录，告诉接收方对未通过认证的邮件应拒绝、隔离还是放行。没有这条记录时，接收方只能自行决定如何处理认证结果；Outlook.com 被报道的新做法，是把“缺少 DMARC”本身作为拒收条件。

**「影响」** 对运行自有邮件服务器的发送方，实际动作是给发信域配置并对齐 SPF、DKIM 和 DMARC，并持续检查发往 Outlook.com 的退信与投递日志，否则邮件可能被拒收。需要注意，微软公开的强制认证要求针对每日发送超过 5,000 封的批量发信方，并覆盖 Outlook.com、Hotmail 和 Live；因此中小发送方应先确认该拒收是否已扩大到自身规模，而不宜把当前二手报告直接当成已文档化的全量策略。

**「社区讨论」** 有评论者认为，拒收未配置 DMARC 的域名本身可以接受，但问题在于这个过程不透明、也没有明确退信；一些自建邮件服务器的管理员还报告称，即便 SPF、DKIM、DMARC 齐全且没有垃圾邮件记录，邮件仍可能在 Outlook.com 接收后被静默丢弃，或者受非公开 blocklist 影响而难以申诉。也有人认为，这是发件方早该完成的配置，不值得同情。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.factae.eu/en/article/outlook-com-quietly-rejects-emails-from-domains-without-dmarc-182744">Outlook . com quietly rejects emails from domains without DMARC</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730">Strengthening Email Ecosystem: Outlook’s New Requirements for ...</a></li>
<li><a href="https://mailrisk.io/guides/outlook-sender-requirements-2026">Microsoft Outlook Sender Requirements 2026: SPF, DKIM, DMARC ...</a></li>

</ul>
</details>

**标签**: `#email-deliverability`, `#DMARC`, `#Microsoft-Outlook`, `#email-authentication`, `#sysadmin`

---

<a id="item-tech-news-3"></a>
### [高盛据报撤下银行家与交易员使用的 Claude Code](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) ⭐️ 7.0/10

The State of AI 的报道称，高盛正在撤下银行家和交易员使用的 Anthropic Claude Code。现有材料没有给出撤下时间表、涉及人数、官方确认或具体原因，因此安全、成本或合规都不能被当作已证实的原因。报道将此事置于金融机构使用编码代理的争论中，核心问题是代理在主工作站上的权限、数据访问和审计边界。

hackernews · TheWiggles · 11月8日 18:16 · [社区讨论](https://news.ycombinator.com/item?id=50415628)

**「背景：从放开到收紧」** 据彭博报道，高盛在此前数月允许银行家和交易员使用 Claude Code 与 GitHub Copilot 跟踪客户资金流、搭建市场模型，随后于 10 月更新内部指引，把这两款工具的使用权限收缩到约 1.2 万名工程师，以及横跨交易、量化研究与工程的 strats 团队；官方给出的理由是生产力与风险管理。这一转向发生在该行 CIO Marco Argenti 于 7 月公开称赞非技术员工的“氛围编程”之后。

**「社区讨论」** 在 Hacker News 讨论中，评论者提出了几类解释：有人强调，把可半自主运行的编码代理放在能访问客户/交易数据、邮件、内网和互联网的金融工作站上会形成高风险组合；也有人报告所在机构因用量计费超额而收回 Claude 访问，并称 Anthropic 未提供标准化费率，而 Gemini 的固定计费与限流更易管理。另有评论者强调银行对权限、数据许可和可审计审批链的要求，并转述有团队因用 AI 处理监管文档出错而被解雇；这些都是评论者说法，未经报道证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/goldman-sachs-pulls-claude-code-and-github-copilot-from-traders-and-bankers">Goldman Sachs Pulls Claude Code and GitHub Copilot From ...</a></li>
<li><a href="https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/">Goldman Sachs pulls AI coding tools from traders and bankers</a></li>
<li><a href="https://daily.dev/posts/goldman-sachs-is-pulling-claude-code-from-its-bankers-and-traders-dmltlbhnz">Goldman Sachs Is Pulling Claude Code from Its Bankers...</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#enterprise AI`, `#Anthropic Claude`, `#security/compliance`, `#financial services`

---

<a id="item-tech-news-4"></a>
### [英伟达董事会调查针对黄仁勋的情报行动](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors) ⭐️ 7.0/10

英伟达在其新闻室发布董事会声明，称正就一起针对 CEO 黄仁勋的情报行动展开调查。调查对象是这起事件本身，而非黄仁勋本人；因此，提交到 Hacker News 的标题「Nvidia Board of Directors Is Investigating Jensen Huang」被评论者指为误导。评论者提到的彭博报道标题为「Nvidia Board to Probe Spying Case After CEO Admits Infidelity」，但这只是评论区的转述，现有材料没有给出调查的时间线、涉及方或具体指控。除这份声明外，尚无其他可核实的细节说明调查范围、是否涉及执法机构或外国政府，因此应把它视为仍在进行中的调查，而非已确认的结论。

hackernews · vincentchau · 11月8日 20:26 · [社区讨论](https://news.ycombinator.com/item?id=50416801)

**「背景」** Nvidia 董事会声明的实际指向是调查是否有外国情报机构把 CEO 黄仁勋作为目标，而不是对黄仁勋本人展开调查；黄仁勋另发备忘录承认婚外情。彭博查阅的声明称董事会正在调查这起间谍案，另有报道援引美国官员的说法称，美方认为与黄仁勋有恋爱关系的中国女子被中国主要情报机构招募；这些细节目前主要来自媒体对声明和知情人士的转述。

**「社区讨论」** 评论者主要纠正了提交标题的歧义，强调董事会调查的是黄仁勋遭遇的事件，而不是黄仁勋本人；其中一人引用彭博报道标题，把该案与「CEO 承认婚外情」联系起来，但这一关联未获独立证实。另有评论者认为，处于黄仁勋这一位置的人被各国情报机构长期研究是常态，并提醒目前没有任何证据表明黄仁勋或英伟达有不当行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-08/read-the-memos-from-nvidia-s-board-and-ceo-jensen-huang">Read the Statements From Nvidia ’s Board and CEO Jensen Huang</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pKNTRhc0VoRmVQQ1JRNXYzVF9TZ0FQAQ?hl=en-US&amp;gl=US&amp;ceid=US:en">US officials claim Chinese spy targeted Nvidia CEO Jensen Huang ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#cybersecurity`, `#AI hardware industry`

---