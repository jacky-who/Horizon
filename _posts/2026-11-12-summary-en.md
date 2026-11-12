---
layout: default
title: "Horizon Summary: 2026-11-12 (EN)"
date: 2026-11-12
lang: en
---

> From 48 items, 13 important content pieces were selected

---

**Technology News**
1. [Voltage glitching unlocks A100 features in mining card](#item-tech-news-1) ⭐️ 8.0/10
2. [AWS emulator brings local service testing, reportedly built by AI agents](#item-tech-news-2) ⭐️ 7.0/10
3. [WSJ headline claims Nvidia is preparing to oust CEO Jensen Huang](#item-tech-news-3) ⭐️ 7.0/10
4. [False Smoke Alarm Nearly Takes Down Jane Street&\#x27;s Only NYC Datacenter](#item-tech-news-4) ⭐️ 7.0/10
5. [Can a Linear Program Do Weight-Space Programming?](#item-tech-news-5) ⭐️ 7.0/10
6. [Google launches Gemini Decisions API for multimodal decision scoring](#item-tech-news-6) ⭐️ 7.0/10
7. [Tim Peters, author of the Zen of Python, has died](#item-tech-news-7) ⭐️ 7.0/10
8. [Anthropic IPO video details four-chip Claude strategy](#item-tech-news-8) ⭐️ 7.0/10
9. [ByteDance Preps Muse-Like AI Agent, Targets Frontier Gap by 2030](#item-tech-news-9) ⭐️ 7.0/10
10. [Report alleges Alice Huang aided 240,000 Nvidia GPU imports to China](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Goolsbee Calls October Inflation &\#x27;Borderline Disturbing&\#x27; as Fed Weighs December Hike](#item-finance-news-1) ⭐️ 8.0/10
2. [China Ends Offshore Trust Income Tax Transition Period With Over RMB 160 Billion Declared](#item-finance-news-2) ⭐️ 8.0/10
3. [Alibaba to spin off and list chip unit T-Head in Hong Kong](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Voltage glitching unlocks A100 features in mining card](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) ⭐️ 8.0/10

A new technical write-up describes using voltage glitching to unlock A100-class functionality in a mining card. It presents the work as a hardware-hacking experiment for cards with disabled capabilities, not as an official NVIDIA feature or supported modification. The available material does not provide independent measurements of the unlocked card&\#x27;s performance or stability.

hackernews · lae · Nov 11, 10:48 · [Discussion](https://news.ycombinator.com/item?id=50451903)

**「Background」** NVIDIA&\#x27;s CMP 170HX is a mining card built on the same GA100 die as the A100, with memory and compute capabilities disabled through on-die fuses so one silicon design can serve different product tiers. The write-up targets the 8 GB CMP 170HX and uses voltage glitching against the GA100 fuse controller, the mechanism NVIDIA uses to distinguish A100 and CMP parts.

**「Impact」** The technique is relevant to people experimenting with second-hand mining cards, not to normal users: it involves voltage glitching rather than an official firmware or driver unlock, and the available material does not establish reliability.

**「Community Discussion」** One commenter trying to unlock 80 GB on a CMP 170HX through software reports no success after two weeks and calls the fuse-blowing approach riskier; another questions whether NVIDIA fused off defective A100 dies rather than simply segmenting the market. A separate suggestion is to use an external PCIe riser and separate power supply so the host can keep running while only the target card is power-cycled.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/">Using voltage glitching to unleash the A 100 in my mining card</a></li>

</ul>
</details>

**Tags**: `#voltage glitching`, `#GPU hardware hacking`, `#NVIDIA A100`, `#mining cards`, `#hardware security`

---

<a id="item-tech-news-2"></a>
### [AWS emulator brings local service testing, reportedly built by AI agents](https://github.com/aws/aws-emulator) ⭐️ 7.0/10

AWS has published an official emulator at github.com/aws/aws-emulator that lets developers run tests against a local clone of its cloud services without provisioning a paid API key. The project is written in Rust and was reportedly built by a large swarm of agents that produced 29,684 commits in its first three weeks; a guest post by Swami Sivasubramanian on Werner Vogels&\#x27; blog describes how it came about. On macOS and Windows it currently requires Docker, and the supplied material does not establish whether it is a long-term maintained product.

hackernews · super\_linear · Nov 11, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50456631)

**「Background」** An AWS emulator gives developers a local clone of AWS services so tests can run without provisioning a paid API key. AWS&\#x27;s GitHub repository says the emulator can be set up through an “aws-emulator” skill for an AI coding agent and requires AWS CLI 2.35.0 or later.

**「Impact」** Developers can use the emulator for local integration tests instead of a live AWS account, but the emulator&\#x27;s security page, as quoted by a commenter, says not to use it for IAM policies, resource-based policies such as bucket policies, KMS key policies, cross-account or cross-Region access, or any other security control. IAM evaluation for emulator-created users and roles also differs from AWS, so security-sensitive tests still need a real AWS environment.

**「Community Discussion」** Commenters questioned whether the emulator is a maintained AWS product or an exercise; one recommended Floci and Testcontainers as alternatives he has used. An Amazonian commenter said it has value if properly maintained, while another argued AI agents made such a broad emulator feasible and could erode the moat of existing local-cloud tools.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/aws/aws-emulator">GitHub - aws / aws - emulator : AWS Emulator is a local emulator of the...</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#cloud emulator`, `#AI coding agents`, `#developer tooling`, `#open source`

---

<a id="item-tech-news-3"></a>
### [WSJ headline claims Nvidia is preparing to oust CEO Jensen Huang](https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad) ⭐️ 7.0/10

A Wall Street Journal headline states that Nvidia is preparing to remove CEO Jensen Huang, but the supplied material contains no article text, named sourcing, board statement, or company confirmation, so the claim remains unverified. No details were provided on the reported basis for such a move, its timing, or a possible successor. The Hacker News discussion that followed is speculation about the implications rather than corroboration of the report.

hackernews · jbredeche · Nov 11, 22:31 · [Discussion](https://news.ycombinator.com/item?id=50459703)

**「Background」** A separate WSJ article published two days earlier reported that Jensen Huang did not believe in succession planning and that the absence of a clear successor had become a big risk for Nvidia. That piece described how Huang had spent decades cultivating relationships with politicians around the world while building Nvidia into one of the world’s most valuable companies, leaving its strategy closely identified with him.

**「Community Discussion」** Commenters argued that at founder-led tech companies, dual-class share structures give founders disproportionate voting power and would make a board-led ouster of a CEO difficult without exceptional legal intervention. Others framed Nvidia as a strategic national asset, saying a leadership change would carry defense and geopolitical weight, and questioned who could replace Huang given his role in the company&\#x27;s long-term technology strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wsj.com/tech/jensen-huang-doesnt-believe-in-succession-planning-its-become-a-big-risk-for-nvidia-abd9ea9d">Jensen Huang Doesn’t Believe in Succession Planning. It’s ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#AI hardware`, `#tech leadership`

---

<a id="item-tech-news-4"></a>
### [False Smoke Alarm Nearly Takes Down Jane Street&\#x27;s Only NYC Datacenter](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/) ⭐️ 7.0/10

Michael Bacarella published a firsthand account on November 10 of a false smoke alarm at Jane Street&\#x27;s only New York City datacenter that nearly overwhelmed the facility. The post describes the incident and the operational response that followed. The Hacker News thread around it centers on two design questions: whether the hall had a physical Emergency Power Off button inside it, and whether smoke detection should be interlocked to power. Commenters who write datacenter sequences of operations said their own designs deliberately keep CRAC units running on a smoke alarm, citing the International Mechanical Code exception for air handlers over 2,000 cfm that serve a single space.

hackernews · mbac32768 · Nov 11, 16:38 · [Discussion](https://news.ycombinator.com/item?id=50455394)

**「Context」** The account is a firsthand war story from Michael Bacarella, a former Jane Street engineer, describing how a false smoke alarm left the trading firm&\#x27;s only New York datacenter without cooling and sent staff sprinting to pull every power cord before the sprinklers went off \(tool-2-1\). Russian-language coverage of the same post attributes the trigger to construction dust, which set off a chain that nearly flooded the server room \(tool-2-3\). In datacenters, smoke detection is commonly interlocked with air handling and fire suppression, so an alarm alone can cut cooling and put water discharge on the clock even when there is no fire.

**「Impact」** The practical takeaway for data hall operators is to verify what a smoke detector actually triggers: if the sequence of operations drops cooling on alarm, a false positive produces the same heat rise as a real fire and the shutdown has to be reversed manually under time pressure. Commenters noted that the alternative — leaving single-space air handlers running under the IMC 2,000 cfm exception — has to be written into the sequence of operations in advance rather than improvised during an incident.

**「Community Discussion」** rdl questioned why the site lacked at minimum an in-hall EPO button and an EPO interlink to the smoke alarms, while rainbowzootsuit argued from datacenter design experience that not shutting down CRACs on smoke alarm is the intentional choice, since the IMC permits air handlers over 2,000 cfm serving one space to keep running without spreading smoke. Other commenters traded stories about being the on-call person who lives closest to the facility — reticulates recalled Hurricane Sandy crews hauling diesel up 17 flights of stairs, and hackermailman described being summoned to shut down servers in person.

<details><summary>References</summary>
<ul>
<li><a href="https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/">How a false smoke alarm almost drowned Jane Street ’s only NYC ...</a></li>
<li><a href="https://dzen.ru/b/avSsqBnX-RwkJu2p">Ложная пожарная тревога едва не затопила серверы Jane Street ...</a></li>

</ul>
</details>

**Tags**: `#datacenter operations`, `#incident response`, `#reliability engineering`, `#infrastructure`, `#Jane Street`

---

<a id="item-tech-news-5"></a>
### [Can a Linear Program Do Weight-Space Programming?](https://nathan.rs/posts/weight-space-lp/) ⭐️ 7.0/10

A new technical post asks whether linear programming can be used for weight-space programming of language models, framing linear constraints as a way to specify behaviors to remove or preserve. It presents the idea as an exploratory analysis rather than a demonstrated method, and the discussion connects it to regularization and weight-space distillation. The supplied material reports no benchmark results or released tooling.

hackernews · emschwartz · Nov 11, 12:30 · [Discussion](https://news.ycombinator.com/item?id=50452655)

**「Background」** Weight-space programming means having a model edit another model&\#x27;s weights directly rather than optimizing text artifacts such as prompts or the surrounding program; the post situates itself against MIT CSAIL&\#x27;s &quot;Sparks of Weight-Space Programming,&quot; which it describes as published the previous week. A linear program optimizes a linear objective under linear constraints, so the post&\#x27;s question is whether a weight edit can be found by solving one, and its later sections compare the resulting edit with a simple steering vector. The author also notes limitations and next steps, so the piece is an exploration rather than a demonstrated replacement for existing weight-editing methods.

**「Community Discussion」** Commenters saw potential in LP-assisted weight edits: one proposed collecting paired examples to find sparse edits for distillation, while another argued such constraints should be enforced during training through regularization. A broader disagreement was whether mathematical programming can replace reward-based reinforcement-learning loops; these were opinions rather than demonstrated results.

<details><summary>References</summary>
<ul>
<li><a href="https://nathan.rs/posts/weight-space-lp/">Can a Linear Program Do Weight - Space Programming ?</a></li>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>

</ul>
</details>

**Tags**: `#linear programming`, `#weight-space editing`, `#LLMs`, `#model optimization`, `#machine learning`

---

<a id="item-tech-news-6"></a>
### [Google launches Gemini Decisions API for multimodal decision scoring](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/) ⭐️ 7.0/10

Google has launched Gemini Decision 1 through a Gemini Decisions API aimed at closed-ended developer decisions such as tool selection, policy checks, and model routing. It handles text, images, audio, video, and PDFs; can score up to 1,000 questions in one request; and returns probability and confidence values, with reported end-to-end latency of about 150–250 ms. Pricing is listed at $0.10 per million input tokens with output free, and the announcement claims it is nearly five times cheaper than an approach using Gemini 3.5 Flash-Lite; the API is available in Google AI Studio. It supports the same yes/no, choice, and rubric-scoring question types as Jev, but unlike Jev&\#x27;s text/JSON-only inputs and OpenAI&\#x27;s text/image inputs, Gemini&\#x27;s version accepts audio and video.

hackernews · iamdelirium · Nov 11, 18:32 · [Discussion](https://news.ycombinator.com/item?id=50456791)

**「Decision-model APIs」** Decision-model APIs return structured judgments—such as a yes/no probability, a choice among labels, or a rubric score—for multiple questions in one request, rather than generating free-form text. Jev&\#x27;s API documentation defines the &quot;noul&quot; as a calibrated yes/no probability and also supports choice and ordered score questions, the terminology and request pattern Gemini Decision 1 is now adopting.

**「Impact」** Developers can send one media input with up to 1,000 labeled questions and get probability and confidence results in a single call, which suits batch classification or routing without chaining separate prompts. The compatibility concern is calibration: in the source&\#x27;s video test Gemini returned about 0.923 for &\#x27;robot&\#x27; rather than the 1.0/0.0 outputs from Jev and OpenAI, so callers need explicit thresholds. At the listed $0.10 per million input tokens and free output, cost scales with input context; Jev remains cheaper at 4.2 cents per million for text-only work.

**「Community discussion」** Commenters questioned how mature the category is: one noted that grammar-constrained JSON output cannot produce probabilities, while another asked how developers actually use decision models in coding harnesses such as Pi. Cost and multimodality drew the most practical debate—Gemini was called more expensive than same-lane models but potentially worth it for audio and video, and one commenter said respan/span-02, described as based on or fine-tuned from Gemma4 26A4, is the best decision model they have used besides Jev.

<details><summary>References</summary>
<ul>
<li><a href="https://jevmodel.org/api/">Jev API Examples: Choice , Score , and Noul Requests</a></li>

</ul>
</details>

**Tags**: `#Gemini API`, `#decision models`, `#Google AI`, `#developer tools`, `#LLM applications`

---

<a id="item-tech-news-7"></a>
### [Tim Peters, author of the Zen of Python, has died](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028) ⭐️ 7.0/10

Tim Peters, a longtime CPython core developer whose work shaped the Python language and community, has died, according to a community obituary posted on the Python discussion forum. He wrote the Zen of Python, available through \`import this\`, and authored Timsort, the sorting algorithm used in CPython, as well as contributing to the \`datetime\` module and decades of CPython maintenance. The announcement is a community report rather than a technical release; the source provided no cause of death or further official details.

hackernews · ayhanfuat · Nov 11, 07:03 · [Discussion](https://news.ycombinator.com/item?id=50450488)

**「What Tim Peters built」** Tim Peters was a longtime CPython core developer whose name is attached to two artifacts many Python users encounter without realizing it. The Zen of Python — the aphorisms printed by \`import this\` — is his, and Timsort, the hybrid stable sorting algorithm he implemented in 2002, became the mechanism behind Python&\#x27;s sorting.

**「The code still runs on his work」** No compatibility change follows from Peters&\#x27; death, but his implementation choices remain load-bearing for working engineers: \`sorted\(\)\` and \`list.sort\(\)\` in Python still default to Timsort, the hybrid stable sort he wrote for the language in 2002, and the same algorithm was adopted for \`Arrays.sort\` on objects in Java 7 onward and in V8. The Zen of Python likewise still prints verbatim from \`import this\` in the standard interpreter.

**「Community discussion」** Commenters exchanged memories of Peters&\#x27; influence beyond CPython, crediting him with helping turn &quot;A Plan for Spam&quot; into the SpamBayes program alongside Gary Robinson and Robert Woodhead, and citing his contributions to the Python Cookbook. Others described following his python-dev and bugs.python.org discussions and credited him with deepening their engagement with Python and adjacent topics such as voting systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tim_Peters_%28software_engineer%29">Tim Peters (software engineer) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Timsort">Timsort - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Timsort">Timsort - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/timsort/">TimSort - GeeksforGeeks</a></li>
<li><a href="https://www.kipuhub.com/en/article/timsort">Timsort – How Python and Java Really Sort | KipuHub</a></li>

</ul>
</details>

**Tags**: `#Python`, `#open source community`, `#Timsort`, `#CPython`, `#obituary`

---

<a id="item-tech-news-8"></a>
### [Anthropic IPO video details four-chip Claude strategy](https://simonwillison.net/2026/Nov/11/anthropic-ipo-roadshow/) ⭐️ 7.0/10

Anthropic&\#x27;s IPO roadshow video, highlighted by Simon Willison, says the company trains and serves Claude across AWS Trainium, Google TPUs, NVIDIA GPUs, and AMD GPUs—a multi-chip bet co-founder Tom Brown describes as deliberate and years in the making. Brown says Anthropic began working with AMD GPUs this year and that a system it calls Mythos got Claude running on AMD in three days with basically no human intervention, porting or writing almost 100% of the kernels; this is a roadshow claim, not an independent measurement. He also describes &quot;compute multipliers&quot; as stackable gains in effective compute and says Anthropic believes Claude will eventually discover them autonomously as it approaches recursive self-improvement.

rss · Simon Willison · Nov 11, 15:11

**「Background」** Anthropic had previously disclosed its multi-chip footprint only indirectly, in a September postmortem describing bugs that affected just its TPU deployments; the roadshow section expands that into an explicit account of training and serving across four chip families. The &quot;Mythos&quot; reference is to an Anthropic Claude model line—Anthropic has described Mythos-class models as restricted-access counterparts to its general-release Fable models—so the video&\#x27;s claim is that an Anthropic model, not a human team, performed most of the AMD port.

**「Impact」** For infrastructure teams, Anthropic is claiming that multi-vendor portability can shrink from dozens of engineers working for months to a few days, while each chip family still needs its own tailored software and inference stack. Because the three-day AMD figure comes from Anthropic&\#x27;s own roadshow, it should be treated as a vendor claim rather than a replicated benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI infrastructure`, `#IPO`, `#multi-chip`, `#compute strategy`

---

<a id="item-tech-news-9"></a>
### [ByteDance Preps Muse-Like AI Agent, Targets Frontier Gap by 2030](https://www.bloomberg.com/news/articles/2026-11-11/bytedance-prepares-muse-like-agent-in-push-to-close-ai-gap) ⭐️ 7.0/10

ByteDance reportedly plans to release an AI assistant similar to Meta&\#x27;s Muse within the next few weeks, according to a Bloomberg report relayed in a brief social-media summary. Co-founder Zhang Yiming told an internal all-hands meeting that the company aims to close the frontier-AI gap with Anthropic and OpenAI, but said that would take until at least 2029 or 2030. The plan includes investing up to $70 billion in the Seedance video-AI platform and a stated preference not to rely on model distillation. The report describes internal goals and a forthcoming product rather than a shipped capability, and it provides no technical details on the agent itself.

telegram · zaihuapd · Nov 11, 12:31

**「Context: video strength, frontier gap」** ByteDance&\#x27;s AI reputation has rested mainly on video generation, and the reported plan would put up to $70 billion behind the Seedance video AI platform. The assistant being prepared is described as a general-purpose agent comparable to Meta&\#x27;s Muse, a different category from video tooling, which is why company leadership frames catching OpenAI and Anthropic as a multi-year effort running to 2029–2030 rather than an imminent release. The report also says ByteDance does not intend to rely on model distillation to close that gap.

**「Impact」** For developers and teams already building on ByteDance&\#x27;s video models, the reporting points to the Seedance video platform — not the assistant itself — as where the money goes: up to $70 billion, with a roughly 1,000-person research org under Google DeepMind alumnus Wu Yonghui supporting it. The consumer assistant is described as launching within weeks, but no model version, API, pricing, or regional availability has been disclosed, so integration and compatibility planning has to wait for an actual product announcement rather than this internal-plan report. If it ships as a Muse-style consumer agent, it would compete directly with Meta&\#x27;s assistant for the same end users rather than offering a new developer surface.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/bytedance-plans-to-launch-ai-video-assistant-in-coming-weeks-targeting-70-25554039">ByteDance Plans to Launch AI Video Assistant in Coming Weeks ...</a></li>
<li><a href="https://aesopacademy.org/ai-news/articles/2026-05-31-bytedance-70b-ai-capex-2026">ByteDance weighs $70 billion in 2026 AI capex — nearly triple ...</a></li>

</ul>
</details>

**Tags**: `#ByteDance`, `#AI agents`, `#AI video`, `#OpenAI`, `#AI industry`

---

<a id="item-tech-news-10"></a>
### [Report alleges Alice Huang aided 240,000 Nvidia GPU imports to China](https://www.tomshardware.com/tech-industry/policy/alice-huang-reportedly-instrumental-in-securing-over-usd7-5-billion-of-nvidia-ai-gpu-imports-during-three-year-relationship-with-jensen-huang-helped-move-240-000-banned-chips-into-china-mostly-h100-and-h200) ⭐️ 7.0/10

The Information has published an investigation alleging that Alice Huang, drawing on a relationship with Nvidia CEO Jensen Huang, helped move about 240,000 restricted Nvidia AI GPUs into China, mostly H100 and H200 chips, in imports worth roughly $7.5 billion. Tom&\#x27;s Hardware&\#x27;s summary of the report names the Shanghai-based 上海世纪利通 and Singapore-based Megaspeed among the companies involved. The figures and involvement are allegations from a news investigation, not a confirmed legal finding or independently verified shipment record.

telegram · zaihuapd · Nov 11, 14:41

**「Background」** Earlier reporting had already focused on Megaspeed, the Singapore-based data-center company led by Alice Huang. The New York Times reported that a U.S. Commerce Department inquiry into Megaspeed was abruptly transferred to the Justice Department, and that officials now believe Huang is a Chinese spy who had a relationship with Nvidia CEO Jensen Huang. Wccftech noted that the same outlet had earlier reported high-end H200 GPUs turning up in China&\#x27;s &quot;ghost offices.&quot;

**「Impact」** If the allegations are substantiated, intermediaries and cloud providers that handled H100/H200 transfers could face closer export-control scrutiny, with end-use, end-user, and ownership documentation becoming central to compliance reviews.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/nvidia-intervened-federal-investigation-megaspeed-ai-chip-smuggling-probe/">NVIDIA Allegedly Became A Roadblock For Federal Investigation In...</a></li>
<li><a href="https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html">U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#export controls`, `#AI hardware`, `#China`, `#semiconductor industry`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Goolsbee Calls October Inflation &\#x27;Borderline Disturbing&\#x27; as Fed Weighs December Hike](https://www.cnbc.com/2026/11/11/goolsbee-october-inflation-fed-rates-disturbing-distressing.html) ⭐️ 8.0/10

Chicago Fed President Austan Goolsbee called October’s 0.4% rise in consumer prices “borderline disturbing,” as Federal Reserve officials debated whether to raise interest rates by a quarter- or half-percentage point in December.

rss · CNBC Finance · Nov 11, 16:49

**「Background」** The Fed left its benchmark rate at 3.75%-4% in October after a quarter-point increase in September; its next policy meeting is in December.

**「Impact」** Fed funds futures price a December increase, with 15% odds of a half-point move that would raise borrowing costs for consumers and businesses.

**Tags**: `#Federal Reserve`, `#inflation`, `#interest rates`, `#monetary policy`, `#CPI`

---

<a id="item-finance-news-2"></a>
### [China Ends Offshore Trust Income Tax Transition Period With Over RMB 160 Billion Declared](https://www.news.cn/20261111/9bcce99c779b4a6197ff45bbbc3e4c50/c.html) ⭐️ 8.0/10

China&\#x27;s tax authority said on 11 November that the 90-day transition period for taxing offshore trust income had ended, with more than RMB 160 billion in personal income tax declared and over RMB 120 billion of that collected in October alone. The authority said the October inflows drove national personal income tax revenue up nearly 90% year on year.

telegram · zaihuapd · Nov 11, 10:35

**「Background」** The 90-day window stemmed from a July 24, 2026 joint announcement by the Ministry of Finance and the tax administration that allowed taxpayers to report historical offshore trust tax owed without late-payment surcharges through an October 22 deadline.

**「Who is affected」** Individuals who benefited from offshore trusts but failed to declare or under-reported their income now face demands for back payment and late fees, and formal tax inspections if they still do not correct their filings, the tax administration said.

<details><summary>References</summary>
<ul>
<li><a href="https://t.me/zaihuapd/45068">在花 科技圈 – Telegram</a></li>
<li><a href="https://news.creaders.net/china/2026/10/20/3060337.html">截止前三 天 ，北京突然又打了6 个 补丁！ - 中 国 瞭望-万维读者网（电脑版）</a></li>

</ul>
</details>

**Tags**: `#offshore trusts`, `#personal income tax`, `#tax enforcement`, `#China fiscal revenue`, `#wealth taxation`

---

<a id="item-finance-news-3"></a>
### [Alibaba to spin off and list chip unit T-Head in Hong Kong](https://www.cnbc.com/2026/11/11/alibaba-pr.html) ⭐️ 7.0/10

Alibaba said it plans to publicly list its semiconductor subsidiary T-Head in Hong Kong, subject to approval from the Hong Kong Stock Exchange and the China Securities Regulatory Commission, after filing confidentially on Sept. 11; the announcement disclosed neither the offering size nor a listing date.

rss · CNBC Finance · Nov 11, 07:47

**「Background」** T-Head is Alibaba&\#x27;s chip-design subsidiary, formed in 2018 by merging the parent company&\#x27;s chip-development units with Hangzhou C-SKY Microsystems, and it designs processors, AI accelerators and server chips.

**「Who is affected」** If approved, the spin-off would list T-Head&\#x27;s shares separately on Hong Kong&\#x27;s main board, giving the chip unit its own access to public capital and letting investors hold the semiconductor business apart from Alibaba&\#x27;s e-commerce operations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.roboticsintl.com/companies/t-head">T-Head Semiconductor Co., Ltd. (Pingtouge) — Company Profile ...</a></li>
<li><a href="https://www.investing.com/news/stock-market-news/alibaba-advances-hong-kong-ipo-plans-for-chip-subsidiary-thead-5015307">Alibaba advances Hong Kong IPO plans for chip subsidiary T - Head ...</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#T-Head`, `#Hong Kong IPO`, `#semiconductors`, `#China tech regulation`

---