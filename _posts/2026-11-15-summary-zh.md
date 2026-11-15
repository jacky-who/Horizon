---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 38 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [Lovable 应用因 RLS 配置不当泄露护照信息与逾 20 万条私信](#item-tech-news-1) ⭐️ 8.0/10
2. [星舰第 15 次试飞：飞船首次由发射塔捕获](#item-tech-news-2) ⭐️ 7.0/10
3. [Project Zero 将漏洞披露期逐步缩短至 30 天](#item-tech-news-3) ⭐️ 7.0/10
4. [EFF：科技公司再次试图重新定义隐私](#item-tech-news-4) ⭐️ 7.0/10
5. [Cloudflare 以 Apache 2.0 开源 AI 代理浏览器 Kitesurf](#item-tech-news-5) ⭐️ 7.0/10
6. [意大利因违规读取相册对 Meta 罚款 8.05 亿欧元](#item-tech-news-6) ⭐️ 7.0/10
7. [特斯拉 Cybercab 条款：月费 299 美元，不订阅无法行驶](#item-tech-news-7) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Lovable 应用因 RLS 配置不当泄露护照信息与逾 20 万条私信](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

一份安全研究报告称，部分由 Lovable 构建的应用因行级安全（RLS）配置不足，泄露了护照信息和超过 20 万条私人消息；评论者指出，这类暴露可通过检查浏览器网络请求发现，无需复杂攻击手段。Lovable 安全负责人回应称，根因正是其扫描机制要捕捉的 RLS 不足，平台会在发布前自动扫描每个应用，并提供更深入的 SAST 扫描、修复建议、自动修复以及发布拦截能力。报告作者表示，文章此前在 Hacker News 未获关注，此次重新提交后引发讨论；相关结论来自研究者披露和厂商回应，尚非独立复现的测量结果。

hackernews · armcat · 11月14日 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**「背景」** 行级安全（RLS）是 Supabase 所依托的 PostgreSQL 的按行访问控制机制：查询能否返回或修改某条记录，取决于为该表配置的策略；策略过宽或缺失时，公开 API 就可能暴露数据。社区讨论还指向 Supabase 的默认权限设置：有评论称该平台多年前为降低上手门槛采用了较宽松默认值，并称 10 月 30 日的修复对已有项目未必自动生效。

**「对已发布应用的影响」** 对于使用 Lovable 生成并连接 Supabase 的已发布应用，团队应把匿名 API 密钥的可达性和每张表的 RLS 策略作为上线前审计项。Supabase 自 10 月 30 日起不再自动向 anon、authenticated 角色授予 public schema 新表的 API 权限，开发者必须显式授权并配置 RLS；否则可能遇到 42501 权限错误，而对仍沿用旧默认的表则可能继续暴露数据。Lovable 表示发布前会自动扫描并提供 SAST 与自动修复，但这不能替代对既有应用的实际权限检查。

**「社区讨论」** 评论者把部分责任指向 Supabase 的默认配置：有人提到一项据称于 10 月 30 日修复的问题，但现有项目可能仍沿用旧默认值；也有人主张数据库应默认拒绝访问、API 应最小权限，并加入自动化鉴权测试。另有观点认为，AI 生成应用只是让原本存在的泄露问题更易被大规模复制和发现，不能把责任完全归于单一平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/syed_shaameerali_52c39bf/supabase-permission-denied-for-table-42501-after-the-oct-30-change-the-fix-3dco">Supabase “permission denied for table” (42501) after the Oct ...</a></li>

</ul>
</details>

**标签**: `#security`, `#AI app builders`, `#Supabase`, `#row-level security`, `#data exposure`

---

<a id="item-tech-news-2"></a>
### [星舰第 15 次试飞：飞船首次由发射塔捕获](https://www.spacex.com/launches/starship-flight-15) ⭐️ 7.0/10

SpaceX 宣布，星舰第 15 次试飞中的飞船在飞行约 22.5 小时、绕地球约 14 圈后返回得州 Starbase，并首次由发射塔机械臂捕获。任务还部署了 26 颗星链 V3 卫星，其中 3 颗携带摄像头用于检查隔热瓦。但超重型助推器未按计划返回发射塔，而在墨西哥湾受控溅落，具体原因未公布，因此两级同时回收尚未实现。

hackernews · ls612 · 11月14日 21:22 · [社区讨论](https://news.ycombinator.com/item?id=50500963)

**「背景」** 星舰是 SpaceX 的两级可重复使用运载系统，第 15 次试飞于 11 月 13 日从得州 Starbase 发射，飞船在轨飞行约 22 小时，并在约 42 分钟内陆续部署 26 颗星链 V3 卫星。所谓“塔捕”，是指用发射塔机械臂夹住返回的箭体；此前这一回收方式只用于超重型助推器，飞船本身从未在轨道返回后被捕获，因此这次是首次对飞船实施塔捕。相比之下，SpaceX 对火箭一级的回收复用已有多年积累，这也是本次尝试的技术基础。

**「影响」** 这次捕获把验证重点移到回收后的检查与复飞：SpaceX 需要确认隔热瓦和结构状态，并让同一艘飞船再次执行任务，才能证明可重复使用；助推器返塔未完成，也使两级同时回收的验证被推迟。

**「社区讨论」** 评论者把星舰与航天飞机对比，认为其优势在于助推器不带固体助推器、飞船置于顶部且可流水线生产；也有人强调，只有隔热瓦经受住再入、实现两级同时捕获并复飞同一艘飞船，入轨成本才会显著下降。另有评论推测助推器若多带少量推进剂可能也能返塔，但最终入轨质量分数仍不清楚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnn.com/2026/11/13/science/live-news/spacex-starship-flight-15-ship-catch">Live updates: SpaceX Starship nails historic ship catch in... | CNN</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-flight-15-chopsticks-double-catch-super-heavy-ship">SpaceX launches Starship on ambitious 22-hour Flight 15 ... | Space</a></li>

</ul>
</details>

**标签**: `#spaceflight`, `#reusable rockets`, `#hardware`, `#engineering`, `#SpaceX`

---

<a id="item-tech-news-3"></a>
### [Project Zero 将漏洞披露期逐步缩短至 30 天](https://projectzero.google/2026/11/disclosure-policy.html) ⭐️ 7.0/10

Google Project Zero 公布了分阶段的漏洞披露时间表：即日起采用“Full 90”，在向厂商报告漏洞 90 天后公开；2027 年 2 月 2 日起改为 60 天，2028 年 1 月 3 日起进一步缩短至 30 天。该安排适用于 Project Zero 报告给厂商的漏洞，后两个期限目前是已宣布但尚未生效的计划。

hackernews · hacb · 11月14日 11:13 · [社区讨论](https://news.ycombinator.com/item?id=50496051)

**「背景」** 漏洞披露期限是指安全研究团队私下通知厂商后，等待多久再把漏洞细节公开；期限越短，厂商的修补窗口越小。Project Zero 是 Google 的漏洞研究团队，这次公告把当前规则定为报告后 90 天，并排定 2027 年 2 月 2 日改为 60 天、2028 年 1 月 3 日改为 30 天。

**「影响」** 按已公布的计划，软件厂商和安全团队可用的修复窗口会从 90 天逐步压缩到 30 天；企业应把 2027 年和 2028 年的两个节点纳入补丁管理，因为公开披露时点提前后，验证和部署修复的时间也会同步减少。

**「社区讨论」** 有评论者质疑 Ubuntu 等发行版无法在 30 天内完成修复；另一人则主张应尽快披露，认为不公开就不足以迫使厂商修复。

**标签**: `#vulnerability disclosure`, `#Project Zero`, `#security policy`, `#zero-day vulnerabilities`, `#cybersecurity`

---

<a id="item-tech-news-4"></a>
### [EFF：科技公司再次试图重新定义隐私](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 7.0/10

电子前哨基金会（EFF）发表评论文章，认为科技公司正在再次试图重新定义“隐私”这一概念。该文属于倡导性分析，而非技术发布或独立测量结果，目前可见材料也没有给出具体公司、产品或政策提案。文章在 Hacker News 引发讨论，焦点包括 AI 会议记录、监控常态与无障碍转录需求之间的冲突。

hackernews · gslin · 11月14日 12:45 · [社区讨论](https://news.ycombinator.com/item?id=50496602)

**「背景」** EFF 的 Thorin Klosowski 在文中把当前的隐私争议描述为一次概念转移：科技公司将隐私从对侵扰的保护，重新包装成佩戴者或用户个人的选择，而被拍摄、被转录的旁观者则被置于视野之外。文章以 Meta 和 Google 的智能眼镜、Apple Watch 的 Audio Intelligence 转录功能以及 Amazon Bee 等可记录设备为例，说明这种再次重定义为何与 AI 记录日常化同时出现。

**「社区讨论」** 评论者 toddmorey 称，如今几乎所有职业会议——包括经理与同事的一对一谈话——都会被看得见或看不见的 AI 访客录制并上传，员工很难在不影响就业的情况下退出。另一位评论者 abecedarius 则强调，做得好的实时转录对失聪和重听者可能是变革性工具，若采用本地模型且不保存或导出数据，就不应被简单禁止；讨论由此集中在隐私规范与无障碍需求如何取舍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.my/items/46520/tech-companies-are-trying-to-shift-the-concept-of-privacy-again">Tech Companies Are Trying to Shift the Concept of Privacy (Again)</a></li>

</ul>
</details>

**标签**: `#privacy`, `#AI surveillance`, `#tech policy`, `#human rights`, `#EFF`

---

<a id="item-tech-news-5"></a>
### [Cloudflare 以 Apache 2.0 开源 AI 代理浏览器 Kitesurf](https://www.phoronix.com/news/Cloudflare-Kitesurf-Open-Source) ⭐️ 7.0/10

Cloudflare 以 Apache 2.0 协议开源了面向 AI 代理的无状态浏览器 Kitesurf，相关代码已发布在 GitHub。该浏览器基于 Cloudflare Workers 构建，无需浏览器容器即可解析 HTML、处理 CSS 并执行 JavaScript。Cloudflare 表示，其目标是提供比 Chromium 占用更少 CPU 和内存的轻量方案，并能在全球 Workers 网络上按需扩展；这些性能和扩展性说法目前来自厂商，报道未提供基准测试或兼容性细节。

telegram · zaihuapd · 11月14日 09:33

**「背景」** Cloudflare Workers 是 Cloudflare 的边缘无服务器运行环境，Kitesurf 将网页解析与脚本执行放在这一环境中，而不是启动完整的 Chromium 浏览器容器。对需要访问网页的 AI 代理而言，这种设计的关键前提是把页面处理能力做成可按需调用的无状态服务，从而避免常驻浏览器实例带来的资源开销。

**「影响」** 对在 Cloudflare Workers 上构建 AI 代理的开发者而言，Kitesurf 提供了不依赖 Chromium 容器即可处理网页内容的选项，可能简化部署和资源管理；但其实际兼容范围和资源占用是否达到 Cloudflare 宣称的水平，仍需独立测试验证。

**标签**: `#Cloudflare`, `#AI agents`, `#open source`, `#browser`, `#Cloudflare Workers`

---

<a id="item-tech-news-6"></a>
### [意大利因违规读取相册对 Meta 罚款 8.05 亿欧元](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10321080) ⭐️ 7.0/10

意大利隐私监管机构 Garante Privacy 对 Meta 处以 8.05 亿欧元罚款，指其 Facebook Android 应用在未取得具体同意的情况下，通过 2023 年上线的相册推荐功能读取约 2000 万意大利用户的照片、视频及元数据。该功能默认开启，授权提示被指过于笼统。监管机构要求 Meta 在 60 天内改为默认关闭并单独征得用户同意，否则不得向未有效授权的用户启用该功能。

telegram · zaihuapd · 11月14日 14:37

**「背景」** 在欧盟《通用数据保护条例》（GDPR）框架下，处理个人数据必须有合法依据；若依赖用户同意，该同意应是具体、知情且可撤回的。Android 系统授予的相册访问权限并不自动等同于这种具体同意，意大利隐私监管机构 Garante Privacy 因而可审查应用将相册数据用于推荐等目的时是否取得有效授权。

**「对 Meta 意大利用户与授权流程的影响」** 根据监管要求，Meta 须在 60 天内将该相册推荐功能改为默认关闭，并单独征得用户同意，否则不得对未有效授权的用户启用；这涉及约 2000 万意大利用户。这意味着 Meta 需要重新设计意大利 Android 端的授权引导和功能入口，该功能在当地的默认覆盖面将随之缩小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cwn83gxemk35o">Italy fines Meta € 805 m over accessing users&#x27; photos</a></li>

</ul>
</details>

**标签**: `#privacy-regulation`, `#meta`, `#mobile-permissions`, `#data-protection`, `#italy`

---

<a id="item-tech-news-7"></a>
### [特斯拉 Cybercab 条款：月费 299 美元，不订阅无法行驶](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 7.0/10

特斯拉在配置器条款中列出的 Cybercab 条件显示，车辆售价 29,990 美元，车主须每月支付 299 美元自主驾驶订阅费，否则车辆无法运行，且特斯拉可提前一个月通知调价。条款还规定，欠费或违规使用可导致订阅暂停或取消，累计三次警告将停用自动驾驶一周；车辆仅在指定区域运行，未经授权不得接入网约车、配送或租赁平台。Electrek 指出，Cybercab 与用于 Robotaxi 的 Model Y 采用同款 AI4 硬件、运行相同的自动驾驶软件，但面向普通车主的 FSD 仍需人类监督。目前公开的只是条款文本，实际执行方式尚无独立验证。

telegram · zaihuapd · 11月15日 01:10

**「背景」** Cybercab 的个人销售并非面向所有消费者：The Verge 报道称特斯拉只邀请部分客户购买，且初期限定在奥斯汀；Daily Sabah 也称其无人驾驶能力只能在特斯拉支持自动驾驶服务的区域使用。正因个人版仍依赖特斯拉的自动驾驶服务网络，购车、订阅、服务区域和商业运营限制才会被写进同一套条款，而不是作为可选功能单独出售。

**「影响」** 对车主而言，车辆能否使用取决于订阅是否持续有效：一旦欠费或违规，自动驾驶乃至车辆运行都会被停用；同时使用场景被限定在指定区域，若要转入网约车、配送或租赁车队，必须先获得授权。长期持有和二手转让的价值也因此与这套订阅规则绑定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/transportation/1033844/tesla-personal-cybercab-orders-299-subscription-fine-print">Tesla is inviting some people to buy a Cybercab ‘for personal use ...</a></li>
<li><a href="https://www.dailysabah.com/business/tech/tesla-opens-cybercab-sales-to-select-customers-for-29990">Tesla opens Cybercab sales to &#x27;select customers&#x27; for $ 29 , 990</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#Cybercab`, `#autonomous driving`, `#subscription model`, `#software-defined vehicles`

---