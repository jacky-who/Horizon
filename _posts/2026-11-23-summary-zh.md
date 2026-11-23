---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 37 条内容中筛选出 17 条重要资讯。

---

**科技新闻**
1. [OpenAI 撰文探讨困惑度与智能的关系](#item-tech-news-1) ⭐️ 8.0/10
2. [英媒指控英伟达芯片经太子集团关联人走私入华](#item-tech-news-2) ⭐️ 8.0/10
3. [谷歌搭建模拟互联网测试 Chrome AI 代理](#item-tech-news-3) ⭐️ 8.0/10
4. [Phison 推出太空级 Pascari SSD，488 TB 将随 StarVault-001 入轨](#item-tech-news-4) ⭐️ 7.0/10
5. [摩尔线程庐山 GPU 传闻达 64GB 显存](#item-tech-news-5) ⭐️ 7.0/10

**全球芯片**
1. [美财政部就英伟达对华芯片销售与合规问责寻求答复](#item-chip-news-1) ⭐️ 7.0/10
2. [美财长贝森特：需查明英伟达在对华 AI 芯片出口中的角色](#item-chip-news-2) ⭐️ 7.0/10
3. [美国情报高官暗示中国获取受限美制 AI 芯片](#item-chip-news-3) ⭐️ 7.0/10
4. [美参议员肯尼迪要求鲁特尼克就中国获取英伟达芯片宣誓作证](#item-chip-news-4) ⭐️ 6.0/10
5. [China’s chip war goes covert: Spy agency steps up hunt for advanced chips, targets global semiconductor intelligence](#item-chip-news-5) ⭐️ 6.0/10
6. [报道称中国情报机构将突破 AI 芯片等西方技术壁垒列为优先事项](#item-chip-news-6) ⭐️ 5.0/10
7. [H200 停售传闻与海外算力租赁受限，国产 AI 芯片或迎需求](#item-chip-news-7) ⭐️ 5.0/10
8. [中国情报机构优先突破 AI 芯片技术壁垒，报道关联英伟达事件](#item-chip-news-8) ⭐️ 4.0/10
9. [报道称中国开展两年情报行动获取先进 AI 芯片以规避美国管制](#item-chip-news-9) ⭐️ 4.0/10

**科技博客**
1. [不确定时，不妨四处试探](#item-tech-blog-1) ⭐️ 6.0/10

**财经新闻**
1. [美股科技股遭抛售，亚洲多地推出稳市措施](#item-finance-news-1) ⭐️ 9.0/10
2. [蚂蚁集团领投 Simplexity Robotics 1 亿美元融资，投后估值 16 亿美元](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 撰文探讨困惑度与智能的关系](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI 发表文章《Perplexity and Intelligence》，讨论语言模型困惑度（perplexity）与智能之间的关系，并附带一项跨模型比较。困惑度衡量模型预测下一个 token 时的“意外程度”：最差情况等于词表大小，最好情况为 1。社区评论指出文章本身未给出困惑度的定义。该文发布后在 Hacker News 获得 495 分、346 条评论，讨论集中在交叉熵指标是否仍具意义，以及微软据称将 MAI 模型加入同一评估图表的表态。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「背景」** 困惑度源自信息论，等于模型在序列上平均每 token 交叉熵的指数，长期被用作语言建模的基准指标。随着 RL 训练和推理模型兴起，业界一度认为单纯的交叉熵损失不再重要，因此该文展示的困惑度与模型能力之间的清晰趋势引发了讨论。

**「影响」** 对模型评估实践而言，这篇文章提供了一个比日益复杂的基准更简单的比较维度；社区评论提到，微软的 Mustafa Suleyman 表示将以 OpenAI 的评估集报告 MAI-2 Base 的 log-perplexity 为 0.819，若属实，意味着厂商可能开始在统一的 held-out 集合上公开预训练进展。

**「社区讨论」** 评论者 hazrmard 补上了文章缺失的定义，解释困惑度的取值范围；jrflo 对交叉熵在 RL 时代仍有如此清晰的趋势感到意外，并认为简单基准优于层出不穷的复杂评测。d\_burfoot 认为预测即压缩，这一对应关系“回头看只能如此”，并援引自己 2008 年的论文。

**标签**: `#AI`, `#language-models`, `#perplexity`, `#machine-learning`, `#model-evaluation`

---

<a id="item-tech-news-2"></a>
### [英媒指控英伟达芯片经太子集团关联人走私入华](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 8.0/10

英国《金融时报》援引知情人士称，被美国财政部指为柬埔寨太子集团“二号人物”的胡小伟涉嫌参与将英伟达芯片运入中国，相关网络被指利用空壳公司、地下融资渠道和私人飞机完成走私。报道援引贸易数据称，2024 年 12 月至 2025 年 12 月，Megaspeed 马来西亚子公司进口货物申报价值约 46 亿美元，部分芯片据称流入中国黑市。太子集团否认胡小伟曾为其工作，并表示有关非法网络和私人飞机走私的指控缺乏事实依据。上述内容均为报道中的指控与否认，尚待独立核实。

telegram · zaihuapd · 11月22日 04:34

**「背景」** 美国对先进 AI 芯片实施对华出口管制并多轮收紧，英伟达面向中国市场的受限型号须获许可才能出货。这一框架催生了经第三国转运、空壳公司等规避渠道；近期多家媒体的调查均聚焦中国如何通过东南亚获取受限的美国芯片。

**「影响」** 对依赖马来西亚中转的英伟达芯片买家与转售链条而言，相关风险已进入实际执法层面：马来西亚皇家警察已于 2025 年 4 月依据《2010 年战略贸易法》立案，并由贸工部牵头多个监管机构调查美国关于马来西亚被用作受控先进芯片非法转运点的指控。这意味着经马来西亚子公司的申报与转运路径可能面临更严格的合规审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China ’s Spies Set Sights on A.I. Chips Years Before Nvidia Scandal</a></li>
<li><a href="https://edition.cnn.com/2026/11/21/world/video/meanwhile-in-asia-nvidia-chip-china-hnk-digvid-mia-vod-hrzn-vrtc">How do restricted Nvidia chips make it into China ? | CNN</a></li>
<li><a href="https://www.malaymail.com/news/malaysia/2026/11/14/a-secret-transit-hub-for-nvidia-ai-chips-minister-says-malaysian-police-on-the-case-since-april/243254">A secret transit hub for Nvidia AI chips? Minister says ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#chip smuggling`, `#export controls`, `#AI hardware`, `#tech industry`

---

<a id="item-tech-news-3"></a>
### [谷歌搭建模拟互联网测试 Chrome AI 代理](https://www.landian.news/archives/128701.html) ⭐️ 8.0/10

据蓝点网报道，谷歌为 Chrome 的 AI 代理搭建了一个名为 Mirror Dimension 的隔离模拟互联网，用于测试其打开网站、搜索浏览、登录、加购和完成任务等操作。该环境包含数千个模拟网站，每名工程师在单独隔离的环境中测试，每天运行超过 1000 个测试案例。报道称测试重点之一是防御恶意网页的提示词注入攻击。上述细节来自单一二手报道，尚未见谷歌官方确认。

telegram · zaihuapd · 11月23日 01:30

**「背景」** Chrome 的 AI 代理需要能够自动打开网页、登录、加购和完成任务，这类“自动浏览”（auto browse）能力若直接在真实网络上训练或测试，一旦代理被恶意网页误导，就可能造成真实的账号或交易风险。谷歌因此构建了 Mirror Dimension：一个由数千个模拟网站组成的合成网络，工程师在其中隔离评估代理，据谷歌安全博客说明，这些模拟站点取材于日常用户路径，可在不引入真实世界安全风险的前提下复现逼真的线上环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/security/mirror-dimension-for-agents/">Mirror Dimension for Agents: Evaluating Browser-Use Agents ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser automation`, `#prompt injection`, `#security testing`, `#Chrome`

---

<a id="item-tech-news-4"></a>
### [Phison 推出太空级 Pascari SSD，488 TB 将随 StarVault-001 入轨](https://videocardz.com/newz/phison-announces-488tb-of-ssd-storage-for-space-data-centers-pricing-expected-to-be-astronomical) ⭐️ 7.0/10

Phison 发布面向航天器、卫星与在轨数据中心的 Pascari Space SSD 系列，产品已上市，分为 Flight Critical、Main Storage 与 Orbital Data Center 三类，单款最高 128 TB。公司确认该系列将用于 Lonestar Data Holdings 的轨道数据中心 StarVault-001：后者计划 2027 年上半年发射，整机合计搭载 488 TB Phison SSD，进入低地球轨道后可用容量约 370 TB。Phison 还称部分型号采用 pSLC 可将写入寿命提高至多 60 倍。价格尚未披露。

telegram · zaihuapd · 11月22日 10:31

**「背景」** 低地球轨道数据中心是指把存储与计算设备部署在卫星上、在轨处理数据，以减少回传地面站的数据量。Lonestar Data Holdings 此前已推进这类在轨设施，StarVault-001 是其计划于 2027 年上半年发射的整机项目。存储厂商为航天环境提供经过筛选和加固的 SSD，是这类项目能否落地的硬件前提。

**「影响」** 对在轨数据中心的运营方来说，488 TB 物理容量在低地球轨道冗余后降至约 370 TB，可用容量与写入耐久是选型时必须核算的约束；pSLC 模式虽可将写入寿命提高至多 60 倍，但会降低容量密度，需要在两者之间权衡。

**标签**: `#storage`, `#space computing`, `#hardware`, `#data centers`, `#SSD`

---

<a id="item-tech-news-5"></a>
### [摩尔线程庐山 GPU 传闻达 64GB 显存](https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80) ⭐️ 7.0/10

据 VideoCardz 转述，摩尔线程 MTT S80 产品经理称下一代庐山游戏 GPU 的显存将超过目前任何在售消费级显卡；按其此前“4 倍于 S80 的 16 GB”的说法推算为 64 GB，是 RTX 5090 的 32 GB 的两倍，但该表态并非公司官方发布。庐山沿用 MDC 2025 披露的目标：相对 S80 的 AAA 游戏性能 15 倍、光追 50 倍、AI 算力 64 倍。公司称将在 12 月 29—30 日于北京举行的 MDC 2026 上由 CEO 张建中发布新旗舰产品。上述显存数字与性能倍数均尚无独立验证。

telegram · zaihuapd · 11月22日 15:11

**「背景」** 摩尔线程面向消费市场的 MTT S80 游戏显卡配备 16 GB 显存，庐山是该系列的下一代产品。公司此前曾提出庐山显存容量将达到 S80 的四倍，按此推算即 64 GB，这也解释了外界为何会把产品经理“超过任何在售消费级显卡”的说法换算成具体数字。

**「对用户的影响」** 如果 64 GB 显存最终落地，庐山将面向需要大显存承载本地 AI 模型或高分辨率素材的桌面用户，而非仅对标游戏卡；不过在 MDC 2026 正式发布前，容量、价格和软件兼容性都还不确定，关注者应等待官方规格而非按推算值做采购规划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80">Moore Threads &#x27; next &#x27; Lushan &#x27; gaming GPU could pack a record 64 GB ....</a></li>
<li><a href="https://www.techpowerup.com/355084/moore-threads-claims-its-next-gpu-will-break-the-consumer-vram-record">Moore Threads Claims Its Next GPU Will Break the Consumer VRAM ...</a></li>

</ul>
</details>

**标签**: `#GPUs`, `#Moore Threads`, `#hardware`, `#gaming graphics`, `#VRAM`

---

## 全球芯片

<a id="item-chip-news-1"></a>
### [美财政部就英伟达对华芯片销售与合规问责寻求答复](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fus-seeks-answers-on-nvidias-sale-of-chips-to-china-bessent-says%2far-AA2hZ30C&amp;c=3104520399582928168&amp;mkt=en-us) ⭐️ 7.0/10

美国财政部长贝森特表示，美国政府正就英伟达向中国销售芯片一事寻求答复，并将查明这家此前由他人执掌的公司在合规事务上由谁负责。据路透社 11 月 22 日发自华盛顿的报道（记者凯瑟琳·杰克逊），该表态确认了美方的问询意向，但报道未披露涉及的具体芯片型号、销售规模、审查时间表或可能采取的处置措施。因此目前可确认的是美方提出了问询要求，而非已作出裁决、达成协议或实施新的出口限制。英伟达方面的回应以及问询所依据的具体法规条款，在现有信息中均未出现。

rss · Bing News - NVIDIA and China · 11月22日 09:52

**「背景」** 此前，美国财政部长贝森特已在 11 月中旬公开要求英伟达说明其最先进 AI 芯片是否被知情地流入中国，并称这一问题比前 CEO 黄仁勋的个人丑闻更重要（据 Newsmax 2026 年 11 月 15 日报道）。同一时期他还主张英伟达董事会应从公司外部寻找下一任首席执行官，并让其他高管就公司遵守美国出口管制的情况接受审查（据 CNBC 2026 年 11 月 15 日报道）。此次表态是上述问责要求的延续：美方现在表示将追查这家由前任领导的公司究竟由谁负责合规工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/15/bessent-nvidia-ceo-lutnick-megaspeed.html">Bessent calls for ‘dramatic shakeup’ at Nvidia , urges outside CEO</a></li>
<li><a href="https://www.newsmax.com/newsfront/nvidia-bessent-results/2026/11/15/id/1276371/">US Treasury Chief Wants Answers Soon from Nvidia | Newsmax.com</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#合规审查`

---

<a id="item-chip-news-2"></a>
### [美财长贝森特：需查明英伟达在对华 AI 芯片出口中的角色](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fbessent-we-need-answers-on-nvidia-role-in-sending-china-ai-chips%2far-AA2hYC6F&amp;c=8529885070083262531&amp;mkt=en-us) ⭐️ 7.0/10

美国财政部长斯科特·贝森特表示，美国政府想要查明英伟达内部是否存在“公司底层的恶意行为者”，这些人应对对华 AI 芯片出口管制的不合规行为负责。贝森特以“需要答案”概括这一问询立场，但现有报道仅为简短摘录，未提供具体调查发现、被指控对象、时间表或已宣布的处理结论。这是一项官方表态，而非已生效的新规或已确认的执法行动。

rss · Bing News - NVIDIA and China · 11月22日 10:49

**「背景」** 这一表态延续了美方围绕英伟达对华 AI 芯片出口合规的追问。路透社报道称，美方将查明这家由已辞职的黄仁勋此前领导的公司中由谁负责合规事务；报道提到黄仁勋因一起婚外情事件辞职。财长斯科特·贝森特 11 月 22 日表示，特朗普政府正就可能的违规对华 AI 芯片销售向英伟达索取答案，并要确认合规失察是否波及公司整体。

需要说明的是，上述辞职与人事细节来自媒体报道，并非本次短讯原文所载；贝森特目前只是提出问询，尚未公布调查结论、指控对象或具体处置措施。

**「影响」** 该表态将关注点放在英伟达自身的合规责任上，而非规则本身的变化；若美方后续认定存在内部违规，可能影响英伟达对华 AI 芯片的出口许可和相关收入，但目前尚无证据显示已启动正式处罚或许可收紧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/us-seeks-answers-nvidias-sale-chips-china-bessent-says-2026-11-22/">US seeks answers on Nvidia&#x27;s sale of chips to China, Bessent ...</a></li>
<li><a href="https://www.newsmax.com/newsfront/scott-bessent-trump-administration-nvidia/2026/11/22/id/1277169/">Scott Bessent: Nvidia Must Answer Questions on China Chip ...</a></li>

</ul>
</details>

**标签**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-3"></a>
### [美国情报高官暗示中国获取受限美制 AI 芯片](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fworld%2fus-intelligence-chief-seemingly-confirms-china-accessed-restricted-america-made-ai-chips%2far-AA2hYJIR&amp;c=15614776108833554957&amp;mkt=en-us) ⭐️ 7.0/10

美国情报高官杰伊·克莱顿（Jay Clayton）暗示，中国以不当方式获得了受限的美制人工智能芯片，同时当局正在调查一个被指存在的芯片走私网络。报道以“暗示”“似乎证实”等措辞描述其表态，但未给出具体芯片型号、数量、运输路线或涉案机构，也未说明是否出台新的管制规则或作出正式执法决定。因此，目前可确认的只是一位官员的公开表态和一项正在进行的调查，而非已确认的执法行动或政策变动。

rss · Bing News - China chip policy · 11月22日 13:50

**「背景」** 美国自 2022 年起对先进 AI 芯片实施对华出口限制。此前已有多起相关执法案件：美国检方指控三人参与约 25 亿美元的 AI 芯片走私网络，FBI 官员称涉案方伪造文件、布置设备以通过审计，并借中转公司隐匿客户；Super Micro 一名联合创始人被控将搭载英伟达芯片的服务器非法转运至中国；台湾检方也就搭载英伟达芯片的高端 Supermicro AI 服务器非法出口进行了多轮搜查。此次情报总监的表态正出现在这类调查背景下，但来源未披露具体芯片型号、数量或涉案主体。

**「影响」** 若调查最终指向具体走私渠道，实际效果将落在受限 AI 加速器对华出货的合规审查与许可执行环节；但由于涉案主体、芯片型号和运输路线均未披露，目前无法判断其对英伟达等厂商对华出货或收入的具体影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://head-post.com/three-charged-in-us-over-alleged-2-5bn-ai-chip-smuggling-to-china/">Three charged in US over alleged $2.5bn AI chip smuggling to China</a></li>
<li><a href="https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/super-micro-co-founder-charged-sending-ai-tech-china">Super Micro co-founder charged with sending AI tech to China</a></li>
<li><a href="https://www.ntd.com/taiwan-says-us-helped-solve-advanced-chip-smuggling-case_1162832.html">Taiwan Says US Helped Solve Advanced Chip Smuggling Case | NTD</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#AI 算力`, `#中美芯片合作`, `#英伟达`

---

<a id="item-chip-news-4"></a>
### [美参议员肯尼迪要求鲁特尼克就中国获取英伟达芯片宣誓作证](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.washingtonpost.com%2fpolitics%2f2026%2f11%2f22%2fsen-kennedy-urges-scrutiny-lutnick-over-chinas-access-nvidia-chips%2f&amp;c=7926976116405803250&amp;mkt=en-us) ⭐️ 6.0/10

美国路易斯安那州共和党参议员约翰·肯尼迪公开要求商务部长霍华德·鲁特尼克和财政部长斯科特·贝森特宣誓作证，就中国获取英伟达芯片的问题“回答一些尖锐问题”。这是国会参议员提出的作证呼吁，并非已颁布的规则、已作出的许可决定，也没有披露芯片流向的新事实。《华盛顿邮报》的报道未说明涉及哪些具体芯片型号、出货数量或政策条款。

rss · Bing News - NVIDIA and China · 11月22日 14:06

**「背景」** 鲁特尼克领导的商务部负责执行美国对华芯片出口管制，包括审批英伟达 AI 加速器对华出口许可；贝森特所在的财政部则参与相关制裁与投资审查。肯尼迪的作证要求出现在这一管制框架持续受到国会审视的背景下，但现有材料未指明此次质询针对哪一项具体许可或规则变动。

**「影响」** 若作证要求推进，鲁特尼克需在国会公开说明商务部审批英伟达芯片对华出口许可的依据，这可能加大该部门在具体许可决定上的政治压力；但目前没有证据显示此举已改变任何许可、出货或管制条款。

**标签**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#美国国会`, `#AI 算力`

---

<a id="item-chip-news-5"></a>
### [China’s chip war goes covert: Spy agency steps up hunt for advanced chips, targets global semiconductor intelligence](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.fortuneindia.com%2fworld%2fchinas-chip-war-goes-covert-spy-agency-steps-up-hunt-for-advanced-chips-targets-global-semiconductor-intelligence%2f171697&amp;c=190024110062511024&amp;mkt=en-us) ⭐️ 6.0/10

China&\#x27;s intelligence agency reportedly elevated advanced-chip acquisition and global semiconductor intelligence gathering to a strategic priority over at least two years.

rss · Bing News - China chip policy · 11月22日 05:31

**标签**: `#对华出口管制`, `#国产芯片`, `#AI 算力`, `#半导体情报`

---

<a id="item-chip-news-6"></a>
### [报道称中国情报机构将突破 AI 芯片等西方技术壁垒列为优先事项](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.seattletimes.com%2fbusiness%2fchinas-spies-set-sights-on-ai-chips-years-before-nvidia-scandal%2f&amp;c=17514016541139213266&amp;mkt=en-us) ⭐️ 5.0/10

据《西雅图时报》报道，中国最高情报机构今年更新工作优先事项时，新增了一项目标：突破西方对中国国家主席习近平视为崛起关键技术的封锁，其中涉及 AI 芯片。报道将这一调整与一起英伟达相关丑闻联系起来，但提供的摘要未点名具体机构、未给出政策条款、生效日期或可核实的事件细节，也未说明涉及哪些产品或涉案人员。因此目前只能确认这是一项被报道的优先事项调整，而非已公布的具体行动方案或已执行的管制措施。

rss · Bing News - China chip policy · 11月22日 09:55

**「背景」** 《纽约时报》的这篇报道指出，中国最高情报机构今年更新工作优先事项时，新增了一项目标：突破西方对习近平视为中国崛起关键技术的封锁，其中涉及先进 AI 芯片。该报把这一优先事项调整与英伟达间谍案报道联系在一起，但现有来源未点名具体情报机构、政策条款、生效日期或所涉产品型号，相关细节尚待披露。

**「影响」** 由于报道未提供具体机构名称、涉案环节和已确认的执法行动，目前无法据此判断对英伟达在华销售、出口许可审批或中国国产芯片替代进程的实际影响；相关说法仍属媒体披露层面，需等待更具体的官方信息或后续调查结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China ’s Spies Set Sights on A . I . Chips Years Before Nvidia Scandal</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#英伟达`, `#国产芯片`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-7"></a>
### [H200 停售传闻与海外算力租赁受限，国产 AI 芯片或迎需求](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f4d6c448f87957f4b27695a83&amp;url=https%3a%2f%2fee.ofweek.com%2f2026-11%2fART-8420-2801-30712829.html&amp;c=5441554697017970739&amp;mkt=en-us) ⭐️ 5.0/10

OFweek 的一篇文章称，英伟达 H200 芯片的销售已经暂停，同时 AI 算力租赁正受到限制。文章认为，这类限制的实际目的是堵住中国 AI 企业此前常用的绕行路径：由于先进英伟达芯片无法直接进入中国，部分企业便把算力中心建在海外、通过远程调用获取算力。该文据此推断，海外算力通道被卡死后，国产 AI 芯片可能获得更多需求。需要说明的是，上述说法属于媒体评论性报道，原文未给出具体政策条款名称、生效日期或官方信源，也未提供 H200 停售的细节及任何算力、出货数字，因此“H200 停售”与相关租赁限制目前只能视为缺乏细节支撑的报道，而非已确认的监管规则。

rss · Bing News - China domestic chips · 11月22日 18:42

**「背景」** 此前英伟达先进 AI 芯片无法进入中国市场，部分中国 AI 企业转而将算力中心建在海外，通过远程调用或算力租赁方式获取算力。此次报道称，针对 AI 算力租赁的限制正是为堵住这一海外绕道路径；但原文未给出具体政策条款、生效日期或官方信息来源，H200 停售的说法也缺少可核实的细节。

**「影响」** 若 H200 停售与算力租赁限制同时落地，中国 AI 企业通过海外算力中心远程调用先进芯片的通道将被直接压缩，短期算力缺口只能更多转向国产 AI 芯片。路透 2026 年 11 月 18 日报道称，英伟达已停止向中国发货美方批准的 AI 芯片，使此前许可安排下的实际出货进一步收窄；美联社报道则指出，在美方一度同意 H200 对华销售后，北京已转向鼓励采用以华为为首的国产芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apnews.com/article/ai-chips-nvidia-huawei-china-1ae6228c4928ddbb43f984e9b38f49dd">Nvidia’s AI chip sales in China stall, as local chipmakers ...</a></li>
<li><a href="https://www.reuters.com/world/china/nvidia-stops-shipping-us-approved-ai-chips-china-2026-11-18/">Nvidia stops shipping US-approved AI chips to China | Reuters</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#英伟达`, `#AI 算力`, `#国产芯片`, `#H200`

---

<a id="item-chip-news-8"></a>
### [中国情报机构优先突破 AI 芯片技术壁垒，报道关联英伟达事件](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.seattletimes.com%2fbusiness%2fchinas-spies-set-sights-on-ai-chips-years-before-nvidia-scandal%2f&amp;c=17514016541139213266&amp;mkt=en-us) ⭐️ 4.0/10

《西雅图时报》一篇报道的导语称，中国最高情报机构今年更新工作重点时，新增了一项意图明确的目标：突破西方对习近平视为中国崛起关键技术的封锁，其中包括与人工智能相关的芯片技术。该报道将这一情报优先事项与一起涉及英伟达的事件相联系。所给材料仅为标题和一句导语，未提供具体政策条文、官员姓名、生效日期、产品或架构名称、性能数字，也未说明任何已发生的可核实行动，因此上述内容应视为报道框架而非已证实的事实。

rss · Bing News - NVIDIA and China · 11月22日 09:55

**「背景」** 《纽约时报》2026 年 11 月 21 日的报道称，中国国家安全部至少两年来一直在运行一项此前未被公开的行动，帮助本国企业获取先进 AI 芯片并搜集全球供应链情报，还设有专门工作组协助芯片入境；这些说法来自数名现任和前任外国安全官员，属于官员转述，而非可独立核实的公开文件。相较之下，本条素材只提到中国最高情报机构今年更新工作重点时，把“突破西方对相关技术的壁垒”列入目标，并未给出具体条款、时间或涉案细节。

**「影响」** 由于材料未给出可核实的具体措施或时间表，目前无法确认这一情报优先事项对英伟达在华出货、出口许可审批或中国国产芯片替代进程产生了何种实际影响；报道所提及的“英伟达事件”细节及两者关联方式在现有材料中均未展开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China Spies Set Sights on Chips Years Before NVIDIA Scandal ...</a></li>
<li><a href="https://explainx.ai/blog/china-mss-ai-chip-espionage-campaign-two-years-nyt-claimed-vs-verified-november-2026">China MSS AI Chips: 2-Year Campaign Explained | explainx.ai Blog</a></li>
<li><a href="https://economictimes.indiatimes.com/news/international/world-news/chinas-spies-set-sights-on-ai-chips-years-before-nvidia-scandal-report/articleshow/136071430.cms">China’s spies set sights on AI chips years before Nvidia ...</a></li>

</ul>
</details>

**标签**: `#对华出口管制`, `#AI 算力`, `#英伟达`, `#国产芯片`, `#间谍活动`

---

<a id="item-chip-news-9"></a>
### [报道称中国开展两年情报行动获取先进 AI 芯片以规避美国管制](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fchina-ran-2-year-spy-campaign-to-acquire-advanced-ai-chips-evade-us-curbs-report%2far-AA2hXEnG&amp;c=6558449294980266658&amp;mkt=en-us) ⭐️ 4.0/10

据媒体报道，中国情报机构被指开展了一项为期两年的行动，目的是获取先进 AI 芯片并摸清全球供应链布局，以规避美国出口管制。该报道将这一行动与北京在管制收紧背景下推进技术自主的努力联系起来。由于所提供的原文仅为简短摘要，未给出具体机构名称、时间节点、涉及企业、芯片型号、数量或政策条款，相关指控目前无法独立核实，应视为媒体转述的指称而非已证实的事实。

rss · Bing News - China chip policy · 11月22日 05:06

**「背景」** 该报道所称的两年情报活动，指向的是美国对华先进 AI 芯片出口管制持续收紧这一既有背景：相关管制自 2022 年起分阶段扩大，限制范围涵盖高端 GPU 及用于 AI 训练与推理的加速卡，并使中国企业获取此类产品的渠道受到许可审查约束。目前来源仅给出“据报道”的概括性说法，未点名具体机构、芯片型号、数量或时间节点，因此该活动是否真实存在、规模如何，均无法从现有材料核实。

**「潜在影响」** 若该指称成立，其直接影响在于美国对华先进 AI 芯片出口管制的执行与合规审查，可能促使美方加强对第三方转口和供应链信息流通的监控；但在缺乏具体涉案主体与芯片型号的情况下，尚无法判断对具体企业出货或许可审批的实际后果。

**标签**: `#对华出口管制`, `#AI 算力`, `#国产芯片`, `#中美芯片合作`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [不确定时，不妨四处试探](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 6.0/10

rss · Sean Goedecke · 11月23日 00:00

**「背景」** 面对指引不明、不知什么做法有效的工程或组织问题，Sean Goedecke 认为最有效的做法往往不是谨慎等待，而是主动“乱撞”。他也承认这很危险：方式不当会损害个人声誉，让同事觉得你只会不断抛出糟糕点子。

**「方案」** 他把好的“乱撞”拆成三条相互关联的原则：大量尝试不同做法；密切关注来自同事、专家以及现实指标（延迟、用户数据等）的反馈；无情放弃得不到积极反馈的方案。多试之所以关键，一是为了尽可能直接接触现实，二是承认自己缺乏判断力、多数方案注定不佳，十次尝试中可能只有一次可行，三是避免过度投入单一计划。作者把这种策略分为三类：产品“乱撞”是在尚未找到产品市场契合的新功能边缘反复试探，例如他在 GitHub Models 中做过多项未成功的功能，但允许用 GitHub Actions token 跑 AI 推理意外地有黏性，后来成为“Continuous AI”的起点；工程“乱撞”是面对过于复杂、庞大或已高度优化的系统时先做若干推测性改动，看效果再决定是否深挖，而不是先通读整个系统；组织“乱撞”则针对团队互不沟通或某团队不满等非技术问题，尝试自动化手工工作、主动接手任务、提出长期方案。他强调组织场景最需要敏感于反馈：及时放弃失败举措能建立信任，忽略反馈继续推进则会让不满转向自己。作者说，称之为“乱撞”是因为从内部感受像不断失败、信息不足还出丑，但这种不适感应被忽略。

**「启示」** Goedecke 的核心论点是：在无法预先判断正确做法的高不确定性中，广泛试探、紧盯反馈并迅速止损，比等待完整理解更快获得理解并变得有用；其代价是过程会让人自觉在“乱撞”，需要把它当作积极信号而非麻烦征兆。

**标签**: `#engineering-practice`, `#uncertainty`, `#experimentation`, `#organizational-dynamics`, `#feedback-loops`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美股科技股遭抛售，亚洲多地推出稳市措施](https://news.bjd.com.cn/2026/11/22/12039852.shtml) ⭐️ 9.0/10

美国 AI 科技股周五遭遇大规模抛售，纳斯达克指数单日下跌 5.28%，费城半导体指数重挫近 11%；随后中国内地、韩国和中国台湾地区相继推出下调融资保证金最低比例至 80%、限制卖空等市场稳定措施。

telegram · zaihuapd · 11月22日 13:24

**「背景」** 此次抛售发生在市场对 AI 相关股票估值本就敏感的时期：据雅虎财经报道，纳斯达克综合指数 10 月已因 AI 热潮降温累计下跌 5.2%。

**「影响」** 这些措施直接改变投资者卖空与融资交易的成本和可行性：中国台湾地区自 11 月 23 日起全面禁止平盘以下卖空，并将融券保证金比例由 130%提高至 150%；韩国自 11 月 24 日起放宽上市公司每日回购订单数量限制，为期 3 个月，同时加强对非法卖空和强制平仓的监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/live/stock-market-today-monday-november-2-dow-sp-500-nasdaq-091835095.html">Stock market today: S&amp;P 500 and Nasdaq extend tech sell - off , Dow...</a></li>

</ul>
</details>

**标签**: `#US tech selloff`, `#semiconductor stocks`, `#market stabilization policy`, `#short-selling rules`, `#Asian markets`

---

<a id="item-finance-news-2"></a>
### [蚂蚁集团领投 Simplexity Robotics 1 亿美元融资，投后估值 16 亿美元](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 7.0/10

蚂蚁集团领投中国具身智能公司 Simplexity Robotics 的 1 亿美元 pre-A 轮融资，投后估值 16 亿美元；老股东阿里巴巴、腾讯、红杉中国和蓝驰创投跟投，董事长兼联合创始人 Wang Kai 向彭博确认了这一消息。

telegram · zaihuapd · 11月23日 02:02

**「背景」** 该公司 2025 年 7 月在杭州成立，核心团队来自理想汽车；今年 3 月它曾披露，成立半年内完成五轮融资、累计 20 亿元人民币，当时投后估值已超过 10 亿美元。

**「影响」** 彭博报道称，这笔资金将用于与宇树、优必选等更成熟的厂商争夺市场，反映中国具身智能赛道的竞争可能进一步升温。

**标签**: `#embodied AI`, `#humanoid robotics`, `#private funding`, `#Ant Group`, `#China tech`

---