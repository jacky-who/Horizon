---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 37 items, 17 important content pieces were selected

---

**Technology News**
1. [OpenAI Links Language-Model Perplexity to Intelligence](#item-tech-news-1) ⭐️ 8.0/10
2. [FT 称与太子集团有关联的人士参与英伟达芯片走私](#item-tech-news-2) ⭐️ 8.0/10
3. [Google builds simulated internet to test Chrome AI agent](#item-tech-news-3) ⭐️ 8.0/10
4. [Phison&\#x27;s space-rated Pascari SSDs to carry 488 TB into orbit](#item-tech-news-4) ⭐️ 7.0/10
5. [Moore Threads PM hints Lushan gaming GPU at 64 GB VRAM](#item-tech-news-5) ⭐️ 7.0/10

**Global Chips**
1. [US Treasury Seeks Answers From Nvidia on China Chip Sales, Bessent Says](#item-chip-news-1) ⭐️ 7.0/10
2. [Bessent Seeks Answers on Nvidia&\#x27;s Role in China AI Chip Export Noncompliance](#item-chip-news-2) ⭐️ 7.0/10
3. [US intelligence chief hints China obtained restricted AI chips](#item-chip-news-3) ⭐️ 7.0/10
4. [Senator Kennedy Seeks Sworn Testimony on China&\#x27;s Nvidia Chip Access](#item-chip-news-4) ⭐️ 6.0/10
5. [China’s chip war goes covert: Spy agency steps up hunt for advanced chips, targets global semiconductor intelligence](#item-chip-news-5) ⭐️ 6.0/10
6. [Report: China&\#x27;s top spy agency added AI chip goals to priorities](#item-chip-news-6) ⭐️ 5.0/10
7. [Report: H200 sales halted as overseas AI compute route narrows](#item-chip-news-7) ⭐️ 5.0/10
8. [Report Links China Spy Priorities to AI Chip Barriers](#item-chip-news-8) ⭐️ 4.0/10
9. [Report alleges China ran two-year campaign to obtain advanced AI chips](#item-chip-news-9) ⭐️ 4.0/10

**Technology Blog**
1. [When in Doubt, Flail About](#item-tech-blog-1) ⭐️ 6.0/10

**Financial News**
1. [美股科技股大跌引发亚洲市场稳定措施](#item-finance-news-1) ⭐️ 9.0/10
2. [蚂蚁集团领投 Simplexity Robotics 1亿美元 pre-A 轮，投后估值16亿美元](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI Links Language-Model Perplexity to Intelligence](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI published an analysis arguing that language-model perplexity — the degree of surprise a model shows when predicting each next token — tracks with model intelligence. In the accompanying discussion, commenters noted that perplexity is 1 for a perfect predictor and equals the vocabulary size at worst. The article is a conceptual piece, not a new model or benchmark release; the supplied metadata contains no measured results beyond what the community thread describes.

hackernews · acossta · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**「Background」** Perplexity is derived from cross-entropy loss: it measures how uncertain a model is about the next token across a sequence, so lower values mean better prediction. Because it requires only held-out text rather than task-specific labeling, it is far simpler to compute than the bespoke benchmarks now common in model evaluation.

**「Impact」** Commenters said the article&\#x27;s apparent trend is striking because cross-entropy loss was assumed to matter less as reinforcement-learning-based training spread, and they welcomed a simple benchmark in place of increasingly convoluted evaluations. One commenter also claimed Microsoft has begun reporting base-model log-perplexity on OpenAI&\#x27;s held-out set — a claim from the discussion thread, not something the supplied source material confirms.

**「Community Discussion」** Commenters supplied the definition the article reportedly omits, explaining that perplexity ranges from 1 for a perfect next-token predictor to the vocabulary size for a random one. One commenter argued the perplexity-intelligence correspondence follows necessarily from intelligence as extracting world models from raw data, citing a 2008 paper; another questioned what happened with GPT-4.5 and dated true reasoning models to o1.

**Tags**: `#AI`, `#language-models`, `#perplexity`, `#machine-learning`, `#model-evaluation`

---

<a id="item-tech-news-2"></a>
### [FT 称与太子集团有关联的人士参与英伟达芯片走私](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 8.0/10

据《金融时报》援引知情人士报道，被美国财政部指认为柬埔寨太子集团“二号人物”的胡小伟，涉嫌参与将英伟达芯片走私进入中国。该报道称，相关网络利用空壳公司、地下融资渠道和私人飞机运送货物；报道援引的贸易数据显示，在 2024 年 12 月至 2025 年 12 月期间，Megaspeed 的马来西亚子公司进口货物的申报价值约为 46 亿美元，其中部分芯片据称流入了中国黑市。太子集团否认胡小伟曾为其工作，并表示关于非法网络和私人飞机走私的指控缺乏事实依据。这些指控来自未具名消息源，且仍存在争议。

telegram · zaihuapd · Nov 22, 04:34

**「Background」** The United States restricts exports of advanced Nvidia AI chips to China, and reporting has documented efforts to move restricted hardware into the country anyway. The New York Times reported in November 2026 that a group was assigned to China&\#x27;s &quot;counter-blockade&quot; work, helping Chinese companies acquire and smuggle advanced chips, while CNN reported the same month that restricted Nvidia chips appeared on procurement records from a Chinese university blacklisted by the U.S. government. The FT report describes one alleged channel: shell companies, underground financing and private aircraft, with a Malaysian subsidiary declaring about $4.6 billion in imports over the cited period.

**「Southeast Asia Intermediaries Face Added Scrutiny」** For firms handling Nvidia hardware in Southeast Asia, the report directs scrutiny at the intermediary layer—Malaysian subsidiaries, shell companies, and underground financing—rather than at Nvidia itself. Malaysia&\#x27;s police opened a probe in April 2025 under the Strategic Trade Act 2010 into US allegations that the country served as a transit point for diverted advanced chips, and Singapore has pursued its largest semiconductor export-control case as fraud and money-laundering charges rather than as export violations. That pattern means regional distributors and logistics operators face traceability expectations beyond checking end-user paperwork.

**「社区讨论」** 未提供社区评论，因此没有可总结的讨论。

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China ’s Spies Set Sights on A.I. Chips Years Before Nvidia Scandal</a></li>
<li><a href="https://edition.cnn.com/2026/11/21/world/video/meanwhile-in-asia-nvidia-chip-china-hnk-digvid-mia-vod-hrzn-vrtc">How do restricted Nvidia chips make it into China ? | CNN</a></li>
<li><a href="https://modeldiplomat.com/story/singapores-390m-nvidia-chip-case-explained">Singapore&#x27;s $390M Nvidia Chip Case Explained</a></li>
<li><a href="https://www.malaymail.com/news/malaysia/2026/11/14/a-secret-transit-hub-for-nvidia-ai-chips-minister-says-malaysian-police-on-the-case-since-april/243254">A secret transit hub for Nvidia AI chips? Minister says ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#chip smuggling`, `#export controls`, `#AI hardware`, `#tech industry`

---

<a id="item-tech-news-3"></a>
### [Google builds simulated internet to test Chrome AI agent](https://www.landian.news/archives/128701.html) ⭐️ 8.0/10

Google reportedly built an isolated simulated internet, called Mirror Dimension, to test Chrome&\#x27;s AI agent as it opens sites, searches, logs in, adds items to carts, and completes tasks. According to Landian, the environment contains thousands of mock websites, gives each engineer an individually isolated test setup, and runs more than 1,000 test cases per day, with emphasis on defending against malicious prompt injection from web pages. The report is a brief secondary account attributed to Landian, and Google has not been independently confirmed to have publicly detailed the system.

telegram · zaihuapd · Nov 23, 01:30

**「Background」** Google&\#x27;s Mirror Dimension is a synthetic web made of thousands of simulated sites, built so Chrome engineers can evaluate the browser&\#x27;s &quot;auto browse&quot; agent in realistic online journeys without exposing the live web to an experimental agent. The isolation matters because agentic browsing widens the attack surface: any page the agent reads can carry prompt-injection instructions, so testing in a sealed environment lets Google observe failures and defenses without putting real accounts, purchases, or data at risk.

**「Impact」** If the reported setup reflects Chrome&\#x27;s development process, testing browser agents would need to move beyond single-page checks to large-scale runs across many simulated sites, including adversarial pages designed to hijack agent instructions. The reported per-engineer isolation also points to a practical constraint: agent tests that log in and complete purchases must be kept separate to avoid cross-contaminating accounts and state.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/security/mirror-dimension-for-agents/">Mirror Dimension for Agents: Evaluating Browser-Use Agents ...</a></li>
<li><a href="https://www.wired.com/story/google-built-a-giant-mirror-dimension-internet-to-test-its-chrome-ai-agents/">Google Built a Giant ‘Mirror Dimension’ Internet to Test Its ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#browser automation`, `#prompt injection`, `#security testing`, `#Chrome`

---

<a id="item-tech-news-4"></a>
### [Phison&\#x27;s space-rated Pascari SSDs to carry 488 TB into orbit](https://videocardz.com/newz/phison-announces-488tb-of-ssd-storage-for-space-data-centers-pricing-expected-to-be-astronomical) ⭐️ 7.0/10

Phison has announced the Pascari Space SSD line for spacecraft, satellites, and orbital data centers, and confirmed that Lonestar Data Holdings&\#x27; StarVault-001 orbital data center will use 488 TB of them. StarVault-001 is planned to launch in the first half of 2027, and about 370 TB will be usable after low-Earth-orbit redundancy; that figure covers the whole machine. The line is split into Flight Critical, Main Storage, and Orbital Data Center tiers, tops out at 128 TB, and is already on sale. Phison says pSLC mode on some models can raise write endurance by up to 60 times, but pricing has not been disclosed.

telegram · zaihuapd · Nov 22, 10:31

**「Background」** Phison&\#x27;s space-rated Pascari line is aimed at spacecraft, satellites, and orbital data centers, a category distinct from terrestrial data-center SSDs because of launch, power, and reliability constraints. The series spans Flight Critical, Main Storage, and Orbital Data Center tiers, reaches 128 TB per drive, and Phison says pSLC can raise write endurance by up to 60 times on some models. Phison says the products are already on sale, while Lonestar Data Holdings&\#x27; StarVault-001 orbital data center is planned to launch in the first half of 2027 with 488 TB of Phison SSDs, about 370 TB usable in low Earth orbit after redundancy.

**「Impact」** The confirmed deployment gives StarVault-001 a named storage supplier and capacity figure ahead of its planned 2027 launch. Phison&\#x27;s tiering and pSLC endurance option point to capacity versus write endurance as a concrete tradeoff for orbital operators, while the roughly 118 TB difference between raw and usable capacity shows redundancy consumes a substantial share of the installed drives.

**Tags**: `#storage`, `#space computing`, `#hardware`, `#data centers`, `#SSD`

---

<a id="item-tech-news-5"></a>
### [Moore Threads PM hints Lushan gaming GPU at 64 GB VRAM](https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80) ⭐️ 7.0/10

A Moore Threads product manager for the MTT S80 said the next-generation Lushan gaming GPU will have more VRAM than any consumer graphics card currently on sale, VideoCardz reported; extrapolating from his earlier statement of &quot;4x the S80&\#x27;s 16 GB&quot; gives 64 GB, twice the RTX 5090&\#x27;s 32 GB. The remark is not an official company release, so the 64 GB figure is a media extrapolation rather than a confirmed specification. Moore Threads has carried over targets disclosed at MDC 2025 for Lushan: 15x the S80&\#x27;s AAA gaming performance, 50x ray tracing, and 64x AI compute. The company says CEO Zhang Jianzhong will unveil a new flagship at MDC 2026, scheduled for December 29-30 in Beijing.

telegram · zaihuapd · Nov 22, 15:11

**「Where the 64 GB figure comes from」** Moore Threads&\#x27; current gaming GPU, the MTT S80, carries 16 GB of VRAM. The company had previously promised the Lushan generation would offer four times the memory capacity of its predecessor, so the product manager&\#x27;s statement that Lushan will exceed any currently selling consumer card points to a 64 GB estimate rather than an official specification. The 15x gaming, 50x ray-tracing, and 64x AI targets also date from MDC 2025, ahead of the CEO&\#x27;s planned flagship launch at MDC 2026 in Beijing on December 29-30.

**「Impact」** Because the 64 GB figure comes from an informal remark and the 15x/50x multiples have no independent validation, readers planning around Lushan should treat these as unconfirmed targets until the December 29-30 MDC 2026 unveiling, when Moore Threads is expected to publish actual specifications and performance data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80">Moore Threads &#x27; next &#x27; Lushan &#x27; gaming GPU could pack a record 64 GB ....</a></li>
<li><a href="https://www.techpowerup.com/355084/moore-threads-claims-its-next-gpu-will-break-the-consumer-vram-record">Moore Threads Claims Its Next GPU Will Break the Consumer VRAM ...</a></li>
<li><a href="https://wccftech.com/moore-threads-teases-lushan-desktop-gpu-largest-vram-capacity-consumer-history/">China’s Moore Threads Has Teased An Upcoming Graphics Card...</a></li>

</ul>
</details>

**Tags**: `#GPUs`, `#Moore Threads`, `#hardware`, `#gaming graphics`, `#VRAM`

---

## Global Chips

<a id="item-chip-news-1"></a>
### [US Treasury Seeks Answers From Nvidia on China Chip Sales, Bessent Says](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fus-seeks-answers-on-nvidias-sale-of-chips-to-china-bessent-says%2far-AA2hZ30C&amp;c=3104520399582928168&amp;mkt=en-us) ⭐️ 7.0/10

US Treasury Secretary Scott Bessent said the US government is seeking answers from Nvidia about its chip sales to China and will establish who was in charge of compliance at the company, Reuters reported on November 22. The report, citing Bessent, presents this as a government inquiry rather than an announced enforcement action, and the published excerpt does not identify which products, transactions or period are under scrutiny. Nvidia has not been accused of violating export controls in the supplied material, and no licence decision, penalty or rule change was disclosed.

rss · Bing News - NVIDIA and China · Nov 22, 09:52

**「Earlier compliance demands」** The request follows Bessent&\#x27;s November 15 public call for Nvidia&\#x27;s board to look outside the company for its next chief executive and for other executives to face scrutiny over the chipmaker&\#x27;s compliance with U.S. export controls; he said the priority was whether Nvidia knowingly allowed its most advanced AI chips to reach China. In the same remarks, he argued the administration already has the tools it needs to limit sales to China and should focus on enforcement rather than new chip-sale legislation.

**「Impact」** As far as the supplied report shows, the practical effect is added scrutiny of Nvidia&\#x27;s China business and of the compliance function that oversaw it, since Bessent&\#x27;s stated aim of finding out who ran compliance suggests the inquiry could reach beyond individual shipments to how the company policed export rules. No shipment halt, licence condition or revenue figure was disclosed, so any effect on Nvidia&\#x27;s China sales remains unquantified.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/15/bessent-nvidia-ceo-lutnick-megaspeed.html">Bessent calls for ‘dramatic shakeup’ at Nvidia , urges outside CEO</a></li>
<li><a href="https://www.newsmax.com/newsfront/nvidia-bessent-results/2026/11/15/id/1276371/">US Treasury Chief Wants Answers Soon from Nvidia | Newsmax.com</a></li>
<li><a href="https://www.politico.com/news/2026/11/15/bessent-pushes-back-chip-sale-legislation-01166709">Bessent pushes back on need for tighter chip sale ... - POLITICO</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#合规审查`

---

<a id="item-chip-news-2"></a>
### [Bessent Seeks Answers on Nvidia&\#x27;s Role in China AI Chip Export Noncompliance](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fbessent-we-need-answers-on-nvidia-role-in-sending-china-ai-chips%2far-AA2hYC6F&amp;c=8529885070083262531&amp;mkt=en-us) ⭐️ 7.0/10

U.S. Treasury Secretary Scott Bessent said the government wants to know whether Nvidia had &quot;malicious actors down at the bottom of the company who were responsible for the noncompliance&quot; with chip export controls tied to China AI chips. The statement, reported on November 22, 2026, frames the issue as an inquiry into individual responsibility rather than a confirmed finding, charge or enforcement action against the company. The supplied excerpt discloses no specific violations, named individuals, penalties or timelines.

rss · Bing News - NVIDIA and China · Nov 22, 10:49

**「Background」** The remarks follow a leadership change at Nvidia: Reuters reports that Jensen Huang resigned as chief executive following an affair, and that Washington is now seeking answers from the company on its China chip sales and on who was in charge of compliance. Bessent&\#x27;s statement, as reported by Newsmax, widens that scrutiny beyond individual transactions to whether compliance failures were confined to lower-level employees or extended through the company.

**「Impact」** The practical effect on Nvidia&\#x27;s China business is still contingent: Bessent&\#x27;s remarks indicate U.S. authorities are examining whether export-control lapses originated inside the company, but the excerpt contains no licensing change, shipment restriction or penalty that would alter Nvidia&\#x27;s China access or revenue. Any concrete consequence would depend on the outcome of that inquiry, which the supplied content does not describe.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/china/us-seeks-answers-nvidias-sale-chips-china-bessent-says-2026-11-22/">US seeks answers on Nvidia&#x27;s sale of chips to China, Bessent ...</a></li>
<li><a href="https://www.newsmax.com/newsfront/scott-bessent-trump-administration-nvidia/2026/11/22/id/1277169/">Scott Bessent: Nvidia Must Answer Questions on China Chip ...</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-3"></a>
### [US intelligence chief hints China obtained restricted AI chips](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fworld%2fus-intelligence-chief-seemingly-confirms-china-accessed-restricted-america-made-ai-chips%2far-AA2hYJIR&amp;c=15614776108833554957&amp;mkt=en-us) ⭐️ 7.0/10

US intelligence chief Jay Clayton suggested that China unlawfully acquired restricted American AI chips, as authorities investigate an alleged chip-smuggling network, according to a brief report. The item names no investigating agency beyond Clayton, no specific chip models, quantities, routes, or new rule or licence decision. His statement is characterized as a suggestion rather than a confirmed enforcement finding or an enacted policy change.

rss · Bing News - China chip policy · Nov 22, 13:50

**「Background」** The United States has restricted exports of advanced AI chips to China since 2022, and enforcement attention has increasingly focused on alleged diversion networks. In a separate case, US authorities charged a Super Micro Computer co-founder with illegally diverting Nvidia-powered servers to China, described in reporting as the highest-profile prosecution over alleged smuggling of restricted AI technology to the country. Taiwan prosecutors have also conducted searches in a related investigation into the alleged illegal export of high-end Supermicro AI servers containing Nvidia chips, a case in which reporting says the US provided assistance. The source item does not identify specific chip models, quantities or routes tied to Clayton&\#x27;s remarks.

**「Impact」** If the alleged smuggling network is substantiated, the practical effect would fall on export-control enforcement rather than on licensing terms: the report discloses no enacted rule change, no named chip vendor, and no confirmed shipment or seizure, so it does not by itself alter the conditions under which restricted US AI accelerators can reach Chinese buyers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/super-micro-co-founder-charged-sending-ai-tech-china">Super Micro co-founder charged with sending AI tech to China</a></li>
<li><a href="https://www.ntd.com/taiwan-says-us-helped-solve-advanced-chip-smuggling-case_1162832.html">Taiwan Says US Helped Solve Advanced Chip Smuggling Case | NTD</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#AI 算力`, `#中美芯片合作`, `#英伟达`

---

<a id="item-chip-news-4"></a>
### [Senator Kennedy Seeks Sworn Testimony on China&\#x27;s Nvidia Chip Access](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.washingtonpost.com%2fpolitics%2f2026%2f11%2f22%2fsen-kennedy-urges-scrutiny-lutnick-over-chinas-access-nvidia-chips%2f&amp;c=7926976116405803250&amp;mkt=en-us) ⭐️ 6.0/10

Senator John Kennedy \(R-Louisiana\) said he wants Commerce Secretary Howard Lutnick and Treasury Secretary Scott Bessent to testify under oath and &quot;answer some hard questions&quot; about China&\#x27;s access to Nvidia chips, according to a Washington Post report. The call is a demand for congressional scrutiny rather than an enacted rule or a documented licensing decision, and the available account does not specify which Nvidia chips, volumes or policy provisions are at issue. No hearing date, subpoena or formal committee action was reported.

rss · Bing News - NVIDIA and China · Nov 22, 14:06

**「Background」** The Commerce Department, through its Bureau of Industry and Security, administers U.S. export controls on advanced AI chips, including Nvidia products, and grants or denies the licences that govern sales to Chinese customers; the Treasury Department handles related investment and sanctions matters. Kennedy&\#x27;s request follows that existing division of authority, but the supplied source does not identify a specific prior licence decision or rule change that prompted it.

**「Impact」** If Kennedy&\#x27;s push leads to sworn testimony, Lutnick and Bessent would have to publicly account for how the Commerce and Treasury departments have handled Nvidia chip flows to China, which could constrain how much licensing discretion the agencies exercise without congressional explanation. Any practical effect on shipments or licence approvals depends on whether a hearing is actually scheduled, and none has been reported.

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#美国国会`, `#AI 算力`

---

<a id="item-chip-news-5"></a>
### [China’s chip war goes covert: Spy agency steps up hunt for advanced chips, targets global semiconductor intelligence](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.fortuneindia.com%2fworld%2fchinas-chip-war-goes-covert-spy-agency-steps-up-hunt-for-advanced-chips-targets-global-semiconductor-intelligence%2f171697&amp;c=190024110062511024&amp;mkt=en-us) ⭐️ 6.0/10

China&\#x27;s intelligence agency reportedly elevated advanced-chip acquisition and global semiconductor intelligence gathering to a strategic priority over at least two years.

rss · Bing News - China chip policy · Nov 22, 05:31

**Tags**: `#对华出口管制`, `#国产芯片`, `#AI 算力`, `#半导体情报`

---

<a id="item-chip-news-6"></a>
### [Report: China&\#x27;s top spy agency added AI chip goals to priorities](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.seattletimes.com%2fbusiness%2fchinas-spies-set-sights-on-ai-chips-years-before-nvidia-scandal%2f&amp;c=17514016541139213266&amp;mkt=en-us) ⭐️ 5.0/10

A news report says China&\#x27;s top espionage agency added, in a priorities update this year, the goal of overcoming Western barriers to technologies that Xi Jinping considers crucial to China&\#x27;s rise, including AI chips. The report links the change to an Nvidia-related scandal. The supplied excerpt does not name the agency, specify the policy provisions or dates, or detail the alleged incident, so the concrete scope and timing remain unconfirmed.

rss · Bing News - China chip policy · Nov 22, 09:55

**「Prior context」** The item provides only a one-sentence excerpt: China&\#x27;s top espionage agency added &quot;overcoming Western barriers&quot; to technologies Xi Jinping considers crucial as a priority in its updated mandate this year. The supplied material does not name the agency, specify the policy provisions or effective date, or detail the Nvidia-linked scandal itself, so the concrete predecessor event remains unverified in this source.

**「Impact」** If the reported priority shift is accurate, it signals that Beijing&\#x27;s effort to work around U.S.-led export controls on advanced AI chips extends beyond domestic R&amp;D and procurement into intelligence collection, a channel that falls outside licensing rules and cannot be addressed through export-control waivers alone — though the excerpt provides no evidence of specific shipments, thefts or targets.

**Tags**: `#对华出口管制`, `#英伟达`, `#国产芯片`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-7"></a>
### [Report: H200 sales halted as overseas AI compute route narrows](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f4d6c448f87957f4b27695a83&amp;url=https%3a%2f%2fee.ofweek.com%2f2026-11%2fART-8420-2801-30712829.html&amp;c=5441554697017970739&amp;mkt=en-us) ⭐️ 5.0/10

An OFweek article claims that H200 sales have been suspended and that restrictions on AI compute leasing are intended to block Chinese AI companies from obtaining overseas compute through leasing. The article says firms had previously built data centers abroad and accessed NVIDIA advanced AI chips remotely because those chips could not enter China, and that this route is now closed. The item names no policy provision, effective date, official source, or shipment figure, so the H200 sales halt is an assertion rather than a confirmed rule or vendor action.

rss · Bing News - China domestic chips · Nov 22, 18:42

**「Background」** The item supplies no details on the export-control or licensing step that preceded the alleged H200 sales halt, and no earlier Horizon summary or verified external record was available to establish a direct predecessor. The only stated precursor is the article&\#x27;s own account that advanced NVIDIA AI chips could not be sold into China, which led some Chinese AI firms to build compute centers abroad and call them remotely — the route the article says is now blocked.

**「Impact」** Nvidia&\#x27;s H200 China business remains effectively stalled even where sales are licensed: Reuters reported on 18 November 2026 that Nvidia had stopped shipping US-approved AI chips to China, and a July 2026 account noted the company held US licences to sell H200 chips to China but almost none had shipped, with a 25% tariff applying. For Chinese AI firms, the practical effect of curbs on overseas compute leasing is to narrow the remote-access route the article describes — building data centres abroad and calling capacity remotely — pushing them toward domestically designed accelerators led by Huawei, which Beijing has been encouraging as the substitute.

<details><summary>References</summary>
<ul>
<li><a href="https://techjournal.org/us-imposes-25-tariff-on-nvidia-h200-ai-chips-bound-for-china">US-China AI Chip War 2026: Nvidia, Tariffs &amp; the H200</a></li>
<li><a href="https://www.reuters.com/world/china/nvidia-stops-shipping-us-approved-ai-chips-china-2026-11-18/">Nvidia stops shipping US-approved AI chips to China | Reuters</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#英伟达`, `#AI 算力`, `#国产芯片`, `#H200`

---

<a id="item-chip-news-8"></a>
### [Report Links China Spy Priorities to AI Chip Barriers](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80ff0454abc82b3fd345520c7f9&amp;url=https%3a%2f%2fwww.seattletimes.com%2fbusiness%2fchinas-spies-set-sights-on-ai-chips-years-before-nvidia-scandal%2f&amp;c=17514016541139213266&amp;mkt=en-us) ⭐️ 4.0/10

According to a Seattle Times teaser tied to an Nvidia-related scandal, China&\#x27;s top espionage agency added overcoming Western barriers to AI-relevant technologies as a priority when it updated its goals this year. The supplied source does not name the agency, identify the specific technologies or the date of the update, or describe the Nvidia scandal, and it does not confirm any actual espionage operation. The item therefore conveys a reported priority statement rather than an enacted policy, a licensing decision or a chip shipment.

rss · Bing News - NVIDIA and China · Nov 22, 09:55

**「Background」** The teaser refers to an update of the Ministry of State Security&\#x27;s stated priorities, and external reporting dated November 21, 2026 describes a previously unreported MSS campaign of at least two years to acquire advanced AI semiconductors and gather supply-chain intelligence, attributed to serving and former foreign security officials. The supplied source does not identify which earlier priority list was revised, when the update took effect, or what the Nvidia-related scandal involves, so those details remain unverified here.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/21/world/asia/china-nvidia-spy-chips-state-security.html">China Spies Set Sights on Chips Years Before NVIDIA Scandal ...</a></li>
<li><a href="https://explainx.ai/blog/china-mss-ai-chip-espionage-campaign-two-years-nyt-claimed-vs-verified-november-2026">China MSS AI Chips: 2-Year Campaign Explained | explainx.ai Blog</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#AI 算力`, `#英伟达`, `#国产芯片`, `#间谍活动`

---

<a id="item-chip-news-9"></a>
### [Report alleges China ran two-year campaign to obtain advanced AI chips](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b03a80f06c44918935acab0a1752a9d&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fchina-ran-2-year-spy-campaign-to-acquire-advanced-ai-chips-evade-us-curbs-report%2far-AA2hXEnG&amp;c=6558449294980266658&amp;mkt=en-us) ⭐️ 4.0/10

A report alleges that a Chinese intelligence agency ran a two-year campaign to acquire advanced AI chips and to map global supply chains, with the stated aim of evading US export curbs. The supplied excerpt does not name the agency, the companies involved, chip models, quantities, dates or specific policy provisions, and it attributes the claim to a report rather than to documented evidence. No element of the alleged campaign is confirmed by an official US or Chinese source in the material provided. The item therefore describes an allegation, not an enacted rule, a licensing decision or a shipped transaction.

rss · Bing News - China chip policy · Nov 22, 05:06

**「Background」** The supplied excerpt does not identify the intelligence agency, the report&\#x27;s publisher, a time frame or any specific chip model or shipment involved, so no concrete predecessor action can be established from the source. The alleged campaign is framed against Washington&\#x27;s tightening export controls on advanced AI chips to China, but the item provides no rule, licence decision or prior enforcement case to anchor the claim in a verifiable sequence of events.

**「Impact」** Because the excerpt names no entities, quantities or enforcement action, the practical effect on licensing, shipments or China&\#x27;s domestic substitution cannot be established from this material; any consequence for AI compute supply or for vendor access to the China market remains unverified.

**Tags**: `#对华出口管制`, `#AI 算力`, `#国产芯片`, `#中美芯片合作`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [When in Doubt, Flail About](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 23, 00:00

**「Background」** Sean Goedecke addresses the situation engineers often face when guidance is unclear and they don&\#x27;t yet know what will help. The instinct is to be cautious and wait for better understanding, but he argues that this usually delays progress and that deliberate experimentation is the faster route.

**「Solution」** Goedecke&\#x27;s central insight is that &\#x27;flailing&\#x27;—trying many speculative approaches while reading feedback closely and ruthlessly dropping plans that aren&\#x27;t working—is often the quickest way to become useful in an unclear situation. He explains that trying lots of things gives direct contact with reality, increases the odds that one idea is good since most plans will fail, and prevents over-investment in any single plan. He distinguishes three contexts: product flailing, where teams search for product-market fit around the margins \(at GitHub Models, an AI-inference feature run from a GitHub Actions token proved surprisingly sticky and seeded &\#x27;Continuous AI&\#x27;\); engineering flailing, where speculative changes beat attempting to understand large, fast-changing systems first \(AI agents help generate candidates\); and organizational flailing, for non-technical problems such as teams not communicating, where trying several things demonstrates effort. He warns that organizational flailing demands the most feedback sensitivity, since pressing on with failing plans can turn others&\#x27; anger toward you. The approach is dangerous if done badly—engineers with only bad ideas can damage their reputation—and the author notes that it feels like failing from the inside even when managers see a proactive engineer.

**「Takeaway」** Goedecke&\#x27;s broader point is that the uncomfortable feeling of flailing is a psychological barrier to push through rather than a sign of trouble: as long as you stay sensitive to feedback and drop failing plans immediately, deliberate flailing can be an effective approach to difficult engineering and organizational problems.

**Tags**: `#engineering-practice`, `#uncertainty`, `#experimentation`, `#organizational-dynamics`, `#feedback-loops`

---

## Financial News

<a id="item-finance-news-1"></a>
### [美股科技股大跌引发亚洲市场稳定措施](https://news.bjd.com.cn/2026/11/22/12039852.shtml) ⭐️ 9.0/10

美国AI科技股周五遭遇大规模抛售，纳斯达克指数单日下跌5.28%，费城半导体指数重挫近11%。随后中国内地、韩国和中国台湾地区相继推出市场稳定措施，包括下调融资保证金比例、限制卖空和放宽回购限制。

telegram · zaihuapd · Nov 22, 13:24

**「Background」** The drop extends an earlier AI-driven retreat in US tech shares: the Nasdaq Composite had already lost 5.2% in October, as investors sold semiconductor stocks ahead of earnings, midterm elections and a key jobs report.

**「影响」** 这些措施直接改变投资者交易科技股的成本与卖空规则：中国台湾地区自11月23日起全面禁止平盘以下卖空，并将融券保证金比例从130%提高至150%；韩国则从11月24日起实施为期3个月的放宽回购限制。

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/live/stock-market-today-monday-november-2-dow-sp-500-nasdaq-091835095.html">Stock market today: S&amp;P 500 and Nasdaq extend tech sell - off , Dow...</a></li>

</ul>
</details>

**Tags**: `#US tech selloff`, `#semiconductor stocks`, `#market stabilization policy`, `#short-selling rules`, `#Asian markets`

---

<a id="item-finance-news-2"></a>
### [蚂蚁集团领投 Simplexity Robotics 1亿美元 pre-A 轮，投后估值16亿美元](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 7.0/10

蚂蚁集团领投中国具身智能公司 Simplexity Robotics 的 1 亿美元 pre-A 轮融资，投后估值 16 亿美元。公司董事长兼联合创始人 Wang Kai 向彭博确认此消息，阿里巴巴、腾讯、HongShan 和蓝驰创投跟投。

telegram · zaihuapd · Nov 23, 02:02

**「背景」** Simplexity Robotics 2025 年 7 月成立于杭州，核心团队来自理想汽车；今年 3 月它曾披露成立半年内完成五轮融资、累计 20 亿元人民币，当时投后估值已超 10 亿美元。

**「影响」** 这笔资金将用于与宇树、优必选等更成熟的厂商争夺中国人形机器人市场。

**Tags**: `#embodied AI`, `#humanoid robotics`, `#private funding`, `#Ant Group`, `#China tech`

---