---
layout: default
title: "Horizon Summary: 2026-11-14 (ZH)"
date: 2026-11-14
lang: zh
---

> 从 40 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [TorchTitan 在 384 块 GH200 上把 1T MoE 推到每 GPU 1300 token/s](#item-tech-news-1) ⭐️ 8.0/10
2. [AI 辅助破译哥德尔笔记，数百条定理说法待验证](#item-tech-news-2) ⭐️ 7.0/10
3. [Python 早期贡献者 Tim Peters 去世，享年 74 岁](#item-tech-news-3) ⭐️ 7.0/10
4. [微软 Outlook、Teams 与 Copilot 全球宕机逾 12 小时](#item-tech-news-4) ⭐️ 7.0/10
5. [DeepSeek 开放应用 API 套件：搜索、文件与语音可由参数开启](#item-tech-news-5) ⭐️ 7.0/10
6. [OpenAI 推出 ChatGPT Wallet，智能体凭支付令牌付款](#item-tech-news-6) ⭐️ 7.0/10

**财经新闻**
1. [卢特尼克因英伟达相关关系面临质询，其子执掌的 Cantor 持股减半](#item-finance-news-1) ⭐️ 8.0/10
2. [芝加哥联储行长古尔斯比：通胀回落停滞，美联储“还有工作要做”](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [TorchTitan 在 384 块 GH200 上把 1T MoE 推到每 GPU 1300 token/s](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

一篇 Reddit 工程实践帖称，团队与 TorchTitan/PyTorch 维护者合作，在 JUPITER 超算的 384 块 GH200 上把约 1T 参数 MoE 的训练吞吐推到每 GPU 约 1,300 tokens/s，较起点提升 14 倍。其方案采用 384 路 FSDP 加节点内 4 路专家并行、不做流水线并行，并结合全量激活重计算、将检查点卸载到 Grace、Muon 优化器与按完整专家切分的 FlexShard。帖子还报告了将 Newton-Schulz 放到 GPU 后优化器步从 42 秒降至约 2 秒、吞吐提升 35%，以及修复分配器侧流占用后峰值保留显存减少 13.5 GiB、吞吐提升 21%；但分组受限路由虽带来 7% 提升，早期结果提示可能损害训练，作者称尚无定论。该文是工程经验分享，不是正式论文或版本发布。

reddit · r/MachineLearning · /u/f14-bertolotti · 11月13日 16:28

**「背景」** 1T 参数 MoE 无法放进单卡，需要组合并行策略：FSDP 把每层参数切片分散到各 rank、用时再 all-gather，专家并行（EP）则让每个 GPU 只持有部分专家、token 经 all-to-all 送往对应专家；这两类通信的代价与拓扑直接决定可扩展性——在 JUPITER 上，节点间 InfiniBand 远慢于节点内 NVLink 和 Grace-Hopper 的 C2C 链路。TorchTitan 此前已加入 FlexShard，它提供 PyTorch 原生构建块，使优化器计算可以采用与持久化 DTensor 参数存储不同的布局，并规划从存储到计算的重分布、让通信与优化器工作重叠（tool-2-1）。文中所依赖的 FSDP2 unshard\_async\_op 当时仍是私有开关。

**「实际影响」** 对在 Hopper 集群上训练大 MoE 的团队，这些结果给出了可操作的兼容性提示：按专家切分的 FlexShard 已在 TorchTitan 中，而用于避免分配器把约 21 GiB 临时缓冲留在侧流上的 unshard\_async\_op 仍是 FSDP2 私有标志，正在转为公开 API，采用前需确认所用版本是否包含相应改动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pytorch/torchtitan/blob/main/torchtitan/distributed/flex_shard/README.md">torchtitan/torchtitan/distributed/flex_shard/README.md at ...</a></li>

</ul>
</details>

**标签**: `#MoE`, `#distributed training`, `#PyTorch`, `#TorchTitan`, `#GPU scaling`

---

<a id="item-tech-news-2"></a>
### [AI 辅助破译哥德尔笔记，数百条定理说法待验证](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths) ⭐️ 7.0/10

《卫报》报道，一项 AI 辅助解码工作正在处理库尔特·哥德尔用加贝尔斯贝格速记写下的笔记，并称其中包含数百条已证明定理。对数学逻辑和科学史研究者而言，这意味着此前难以阅读的手稿可能变得可检索，但当前说法仍属媒体报道，尚无公开的逐条转录或独立核验。

hackernews · bookofjoe · 11月13日 17:30 · [社区讨论](https://news.ycombinator.com/item?id=50486748)

**「背景」** 哥德尔这些笔记是他用加贝尔斯贝格速记（Gabelsberger）写下的私人工作簿，共 1009 页，长期因辨读困难而未被系统整理。据 explainx.ai 的梳理，赫尔辛基逻辑学家扬·冯·普拉托把转录文本交给 Claude，随后用 Coq 证明助手核验：663 条定理中约 400 条按原陈述通过，约 200 条需要更精确的表述。

**「影响」** 若解码准确，研究者可据笔记追踪哥德尔未发表的工作线索；在此之前，学术引用仍需依赖逐页转写和同行核验，不能把报道中的“数百条定理”直接当作新成果。

**「社区讨论」** 有评论者质疑加贝尔斯贝格速记“世界上只有少数人能读”的说法，并以家人长期使用该体系的经历作反例；也有人认为哥德尔是极端严苛的自我审稿者，不太可能留下自己未意识到的结论性新定理，因此对“数百条定理”应保持怀疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/claude-godel-notebooks-von-plato-663-theorems-coq-what-is-verified-2026">Claude and Gödel&#x27;s Notebooks: 663 Theorems Checked - explainx.ai</a></li>
<li><a href="https://aiweekly.co/alerts/von-plato-uses-claude-to-extract-663-theorems-from-gdel-notes">Von Plato uses Claude to extract 663 theorems from Gödel ...</a></li>

</ul>
</details>

**标签**: `#Gödel`, `#AI-assisted research`, `#handwriting recognition`, `#mathematical logic`, `#history of science`

---

<a id="item-tech-news-3"></a>
### [Python 早期贡献者 Tim Peters 去世，享年 74 岁](https://x.com/Itsfoss/status/2120957452937998716) ⭐️ 7.0/10

Python 创造者 Guido van Rossum 宣布，Python 早期贡献者 Tim Peters 去世，享年 74 岁。据该宣布，Peters 是 Python 的第二位真实用户，撰写了《Python 之禅》（PEP 20），以 Timsort 排序算法的作者身份为人所知，并曾在 Python 软件基金会董事会任职 13 年。当前公开信息来自 Guido van Rossum 的宣布，现有来源未提供死因等进一步细节。

telegram · zaihuapd · 11月13日 09:55

**「消息为何此时出现」** 这条消息滞后于事件本身：据 Python 社区论坛的 In Memoriam 帖，Tim Peters 于 2026 年 7 月 15 日去世，享年 74 岁，更广泛的编程社区直到 11 月 11 日 Guido van Rossum 发帖后才得知（tool-2-1、tool-2-3）。Guido 在帖中表示，Peters 在 Python 首次发布后不久就加入了这门语言，而且早在写下《Python 之禅》之前，就已经是他的导师和语言共同设计者（tool-2-1、tool-2-2）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028">In Memoriam: Tim Peters 1952–2026 - Core Development ...</a></li>
<li><a href="https://lwn.net/Articles/1106901/">In Memoriam: Tim Peters 1952–2026 - lwn.net</a></li>
<li><a href="https://peopleforever.com/p/tim-peters">Tim Peters (1952–2026): life, family and tributes</a></li>

</ul>
</details>

**标签**: `#Python`, `#Tim Peters`, `#Timsort`, `#open source community`, `#obituary`

---

<a id="item-tech-news-4"></a>
### [微软 Outlook、Teams 与 Copilot 全球宕机逾 12 小时](https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/) ⭐️ 7.0/10

据路透社报道，微软 Outlook、Teams 和 Copilot 在 11 月 13 日仍处于全球性宕机状态，故障已持续超过 12 小时，扰乱企业和政府通信。微软将原因归为服务器问题，称未发现恶意活动，并表示已扩大修复范围、出现回稳迹象。澳大利亚、日本和美国部分政府机构受到影响，Euronext 的邮件受阻，台湾有金融机构改用传真确认交易；这是微软 365 服务今年第二次中断。

telegram · zaihuapd · 11月13日 12:21

**「背景」** Microsoft 365 是微软面向企业提供的云端办公订阅服务，Outlook 承担邮件与日历，Teams 承担聊天、会议与协作，Copilot 则是嵌入这些应用的 AI 助手。源报道称，本次故障是 Microsoft 365 服务今年第二次中断，但没有交代上一次中断的具体时间、影响范围和原因。

**「实际影响」** 对依赖 Microsoft 365 实时协作的机构而言，直接后果是邮件和会议通信可能同时不可用，需要切换备用通知与交易确认渠道；台湾金融机构改用传真正是这种应急替代的实例。

**标签**: `#Microsoft 365 outage`, `#cloud reliability`, `#enterprise software`, `#Microsoft Teams`, `#incident response`

---

<a id="item-tech-news-5"></a>
### [DeepSeek 开放应用 API 套件：搜索、文件与语音可由参数开启](https://mp.weixin.qq.com/s/78KBHc4-4N5b2vfL9SkutQ) ⭐️ 7.0/10

DeepSeek 宣布开放“全家桶”应用 API：开发者在原有 API 中开启对应参数，即可获得深度思考搜索、文件输入、阅读链接和语音等对话能力，工具调用与上下文拼接由服务端自动完成。官方称 V4.1-Flash 模型已在三个接口中支持，Search、Fetch、OCR、ASR、TTS 也可脱离对话单独调用。配套开源的 chat-demo 前端支持导入历史对话，可基于 API 把 DeepSeek 网页端本地部署使用。该内容为官方公告，未披露具体参数名、计费方式、限流额度与各端点差异，也没有独立验证或实测数据。

telegram · zaihuapd · 11月13日 14:27

**「背景」** 在对话式 API 中，服务端工具调用指模型按需触发搜索、抓取或 OCR 等外部工具，再把结果回填到上下文，开发者无需在客户端逐次编排。DeepSeek 此次把 Search、Fetch、OCR、ASR、TTS 做成可单独调用的端点，同时保留在原有对话 API 中开启参数、由服务端自动完成工具调用与上下文拼接的方式。

**「影响」** 对已接入 DeepSeek API 的开发者，这意味着不必自建搜索抓取或语音链路，打开参数即可在现有对话中启用这些能力；若只需单项功能，则可分别调用 Search、Fetch、OCR、ASR、TTS 端点。由于官方公告未给出各端点的计费与调用限制，接入前需要自行确认配额与成本。

**标签**: `#DeepSeek`, `#LLM APIs`, `#multimodal`, `#tool calling`, `#open source`

---

<a id="item-tech-news-6"></a>
### [OpenAI 推出 ChatGPT Wallet，智能体凭支付令牌付款](https://openai.com/index/introducing-chatgpt-wallet/) ⭐️ 7.0/10

OpenAI 发布 ChatGPT Wallet，并与美国运通、万事达和 Visa 合作，让智能体在付款时不直接接触用户的真实卡号。该功能今日起在美国向 18 岁以上的 ChatGPT Pro 订阅用户开放，并要求使用美国发行的银行卡。每笔交易中，用户需核对商品和金额，再通过 Face ID 或指纹确认；支付网络会下发替代真实卡号的支付令牌。

telegram · zaihuapd · 11月13日 15:43

**「背景：支付令牌与智能体代付」** 支付令牌是卡组织为单张卡签发的替代凭证，用它替换真实卡号可让交易环节不暴露原始卡信息；此次 ChatGPT Wallet 正是由支付网络下发这种令牌。智能体代付还需要把授权绑定到具体交易上，因此该流程要求用户逐笔核对商品与金额，并用 Face ID 或指纹确认后才完成付款。

**「影响」** 对符合条件的用户来说，智能体代买仍需逐笔人工核对并进行生物识别确认，因此不能当作后台自动扣款或无人值守下单来使用；非美国发卡用户和未订阅 Pro 的用户暂时无法使用该功能。

**标签**: `#OpenAI`, `#ChatGPT`, `#agentic payments`, `#payment tokenization`, `#digital wallets`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [卢特尼克因英伟达相关关系面临质询，其子执掌的 Cantor 持股减半](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 8.0/10

据 CNBC 11 月 13 日报道，美国商务部长霍华德·卢特尼克因其两个儿子执掌的 Cantor Fitzgerald 与英伟达关系密切而面临质询；CNBC 对证券申报文件的分析显示，该券商报告的英伟达持股数量在 2025 年 9 月至 2026 年 3 月间下降约 49%，从约 350 万股降至 178 万股，对应市值由 6.52 亿美元降至 3.1 亿美元。报道指出，没有证据表明卢特尼克的儿子事先知情、持股变动与相关警告有关，或该公司的商业利益影响了其父的决定；利益冲突质疑目前仍属外界指控。

rss · CNBC Finance · 11月13日 23:42

**「背景」** 英伟达 CEO 黄仁勋因与一名疑似中国间谍的女性存在婚外情，于 11 月辞去 CEO 职务（据 People 报道）；新加坡公司 Megaspeed 曾是英伟达 AI 芯片的大客户，被怀疑非法将最先进的芯片转运至中国（据 CBS 新闻）。卢特尼克原为坎托·菲茨杰拉德掌门人，2025 年 2 月出任美国商务部长，而商务部正是负责制定出口管制“实体清单”的部门。

**「影响」** 财政部、国防部、国务院和美国贸易代表办公室都主张将涉嫌走私英伟达芯片的新加坡公司 Megaspeed 列入实体清单，而这一限制清单由商务部掌管；这些机构之间的分歧可能影响依靠英伟达 AI 芯片出口许可的海外客户的合规与供货前景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://people.com/jensen-huang-resigns-nvidia-after-affair-bombshells-12245984">Nvidia’s Jensen Huang Resigns After Sex Scandal with ...</a></li>
<li><a href="https://www.cbsnews.com/news/lutnick-nvidia-ai-chips-china/">Lutnick should have prevented the diversion of sensitive ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#U.S. export controls`, `#Commerce Department`, `#corporate governance`, `#semiconductor industry`

---

<a id="item-finance-news-2"></a>
### [芝加哥联储行长古尔斯比：通胀回落停滞，美联储“还有工作要做”](https://www.cnbc.com/2026/11/13/chicago-feds-goolsbee-says-central-bank-has-definitely-got-work-to-do-on-inflation.html) ⭐️ 7.0/10

芝加哥联储行长古尔斯比 11 月 13 日表示，美联储在恢复通胀可信度方面“肯定还有工作要做”；此前公布的美国 10 月生产者价格指数（PPI）环比上涨 0.3%、同比上涨 6.5%，为 2022 年 11 月以来最高同比涨幅。市场随后完全计入 12 月 8 日至 9 日议息会议加息 25 个基点的预期。

rss · CNBC Finance · 11月13日 14:22

**「背景」** 这一担忧延续自本周早些时候：Goolsbee 曾把高于预期的 10 月消费者价格指数（CPI）称为“近乎令人不安”，而美联储的通胀目标是 2%，负责利率决策的联邦公开市场委员会（FOMC）将在 12 月 8 日至 9 日开会，他目前不是投票委员、要到 2027 年才轮值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scotsmanguide.com/news/feds-goolsbee-flags-october-inflation-data-as-borderline-disturbing/">Fed&#x27;s Goolsbee flags October inflation data as &#x27;borderline ...</a></li>

</ul>
</details>

**标签**: `#Federal Reserve`, `#Inflation`, `#Monetary policy`, `#PPI`, `#Interest rates`

---