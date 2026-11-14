---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 40 items, 8 important content pieces were selected

---

**Technology News**
1. [TorchTitan team scales a 1T MoE to 1,300 tokens/s per GH200](#item-tech-news-1) ⭐️ 8.0/10
2. [AI Decodes Gödel&\#x27;s Shorthand Notebooks, Report Claims Hundreds of Theorems](#item-tech-news-2) ⭐️ 7.0/10
3. [Python contributor Tim Peters dies at 74, Guido van Rossum announces](#item-tech-news-3) ⭐️ 7.0/10
4. [Microsoft Outlook, Teams and Copilot outage exceeds 12 hours](#item-tech-news-4) ⭐️ 7.0/10
5. [DeepSeek opens app APIs for search, files, links, and voice](#item-tech-news-5) ⭐️ 7.0/10
6. [OpenAI launches ChatGPT Wallet for US Pro users with tokenized agent payments](#item-tech-news-6) ⭐️ 7.0/10

**Financial News**
1. [Lutnick faces scrutiny over sons&\#x27; firm&\#x27;s Nvidia ties](#item-finance-news-1) ⭐️ 8.0/10
2. [Goolsbee Says Fed Has &\#x27;Work to Do&\#x27; on Inflation as October PPI Hits 6.5%](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [TorchTitan team scales a 1T MoE to 1,300 tokens/s per GH200](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

A team working with TorchTitan and PyTorch maintainers reports training a ~1T-parameter mixture-of-experts model at ~1,300 tokens/s per GPU on 384 GH200 GPUs, a 14× improvement over its starting point. The configuration uses 384-way FSDP plus 4-way expert parallelism kept inside each node, and skips pipeline parallelism to avoid long steps. The write-up attributes gains to full activation checkpointing \(4×\), offloading checkpoint activations to Grace, Muon optimizer states, FlexShard expert sharding, straggler mitigation \(+13% and +7%\), FP8 expert all-gather \(+18%\), and an allocator fix that cut peak reserved memory by 13.5 GiB and raised throughput 21%. These are the authors&\#x27; reported measurements on JUPITER, not an independent benchmark or a new release.

reddit · r/MachineLearning · /u/f14-bertolotti · Nov 13, 16:28

**「Background」** TorchTitan is PyTorch&\#x27;s native framework for training large models with multi-dimensional parallelism, and FlexShard, one of its distributed components, lets optimizer compute run on a parameter layout that differs from the persistent DTensor storage layout, planning packed storage-to-compute redistribution and overlapping communication with optimizer work. The write-up builds directly on that machinery, including FlexShard&\#x27;s existing placement control and FSDP2&\#x27;s collective and stream handling, so its lessons apply to TorchTitan&\#x27;s FSDP2/DTensor stack rather than to training frameworks in general.

**「Impact」** For teams training large MoEs on similar GH200/JUPITER-class systems, the practical constraint is inter-node InfiniBand: the authors kept expert all-to-all node-local and hid FSDP communication behind compute, so configurations that spread experts across nodes are likely to lose much of the reported throughput. The allocator finding is also an upgrade concern: FSDP2 side-stream buffers can strand cached HBM, so operators should check stream placement when debugging apparent out-of-memory errors.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pytorch/torchtitan/blob/main/torchtitan/distributed/flex_shard/README.md">torchtitan/torchtitan/distributed/flex_shard/README.md at ...</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#distributed training`, `#PyTorch`, `#TorchTitan`, `#GPU scaling`

---

<a id="item-tech-news-2"></a>
### [AI Decodes Gödel&\#x27;s Shorthand Notebooks, Report Claims Hundreds of Theorems](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths) ⭐️ 7.0/10

A Guardian report, discussed on Hacker News, describes AI-assisted decoding of Kurt Gödel&\#x27;s shorthand notebooks, with claims that they contain hundreds of proved theorems. The notebooks were written in Gabelsberger shorthand, a system a commenter describes as long superseded in schools by Deutsche Einheitskurzschrift. The headline claims have not been independently verified, and the available material gives no detail on which theorems were identified, how they were checked, or who is publishing the transcriptions.

hackernews · bookofjoe · Nov 13, 17:30 · [Discussion](https://news.ycombinator.com/item?id=50486748)

**「Background」** Gödel recorded much of his private mathematical work in the rare Gabelsberger shorthand, leaving a 1,009-page corpus that was difficult for historians to transcribe and assess. The reported project had Helsinki logician Jan von Plato use Anthropic&\#x27;s Claude to analyze that material, after which the Coq proof assistant checked 663 extracted theorems, with roughly 400 verified as stated and about 200 requiring sharper formulations.

**「Impact」** For historians of logic and the editors of Gödel&\#x27;s literary remains, the practical consequence is a verification burden: machine transcription of idiosyncratic shorthand would still need expert checking before any recovered result could be treated as part of the canon. Commenters noted that the AI work as described did not address the consistency or completeness of the notebooks&\#x27; contents.

**「Community Discussion」** The strongest skeptical argument, from iltennico, is that Gödel was a harsh reviewer of his own work who published only results he considered bulletproof, so it is unlikely his notes hold conclusive new theorems he simply failed to recognize. Other commenters treated the fragmentary claims more enthusiastically, with ducttapecrown asking to hear about the reported 14 themes of logic Gödel pursued, while hobo123 questioned how rare Gabelsberger literacy really is, citing a relative who wrote in it until 2020.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/claude-godel-notebooks-von-plato-663-theorems-coq-what-is-verified-2026">Claude and Gödel&#x27;s Notebooks: 663 Theorems Checked - explainx.ai</a></li>
<li><a href="https://o-server.main.jp/hacker-news/en/articles/2026/11/14/ai-project-decodes-kurt-g-del-s-private-notebooks-using-gabelsber-50486748.html">AI Project Decodes Kurt Gödel&#x27;s Private Notebooks Using ...</a></li>
<li><a href="https://aiweekly.co/alerts/von-plato-uses-claude-to-extract-663-theorems-from-gdel-notes">Von Plato uses Claude to extract 663 theorems from Gödel ...</a></li>

</ul>
</details>

**Tags**: `#Gödel`, `#AI-assisted research`, `#handwriting recognition`, `#mathematical logic`, `#history of science`

---

<a id="item-tech-news-3"></a>
### [Python contributor Tim Peters dies at 74, Guido van Rossum announces](https://x.com/Itsfoss/status/2120957452937998716) ⭐️ 7.0/10

Tim Peters, an early and foundational Python contributor, has died at 74, Python creator Guido van Rossum announced. Peters was Python&\#x27;s second real user, wrote the Timsort sorting algorithm and the Zen of Python \(PEP 20\), and served 13 years on the Python Software Foundation board. The report is based on a brief social-media announcement and provides no cause of death or independent confirmation.

telegram · zaihuapd · Nov 13, 09:55

**「Background」** Peters found Python shortly after its initial release and became an early user and language co-designer; Guido van Rossum’s memorial credits him with shaping the language well before writing PEP 20. That memorial announced Peters died on July 15, 2026, with broader notice arriving on Nov. 11, 2026, when van Rossum posted it to the Python community forum.

<details><summary>References</summary>
<ul>
<li><a href="https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028">In Memoriam: Tim Peters 1952–2026 - Core Development ...</a></li>
<li><a href="https://peopleforever.com/p/tim-peters">Tim Peters (1952–2026): life, family and tributes</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Tim Peters`, `#Timsort`, `#open source community`, `#obituary`

---

<a id="item-tech-news-4"></a>
### [Microsoft Outlook, Teams and Copilot outage exceeds 12 hours](https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/) ⭐️ 7.0/10

Microsoft&\#x27;s Outlook, Teams and Copilot were still down on November 13, with the disruption lasting more than 12 hours and disrupting communications for businesses and governments worldwide. Microsoft attributed the failure to a server problem, said it found no evidence of malicious activity, and reported that it had widened remediation efforts and was seeing signs of stabilization. Government agencies in Australia, Japan and parts of the United States were affected, Euronext had email disrupted, and some Taiwanese financial institutions switched to fax to confirm trades. According to the report, this is the second Microsoft 365 service outage this year.

telegram · zaihuapd · Nov 13, 12:21

**「Why one Microsoft failure hits email, chat and Copilot at once」** Outlook, Teams and Copilot are delivered to Microsoft 365 subscribers as cloud services from Microsoft&\#x27;s own infrastructure, so a server-side fault can knock out mail, messaging and the AI assistant simultaneously for every tenant rather than only some users. The report describes this as the second Microsoft 365 service disruption this year, but gives no detail on the earlier incident.

**「Impact」** For organizations standardized on Microsoft 365, the incident took out email, chat and Copilot access at the same time rather than isolating a single product, forcing at least some affected institutions to confirm time-sensitive transactions through manual channels such as fax.

**Tags**: `#Microsoft 365 outage`, `#cloud reliability`, `#enterprise software`, `#Microsoft Teams`, `#incident response`

---

<a id="item-tech-news-5"></a>
### [DeepSeek opens app APIs for search, files, links, and voice](https://mp.weixin.qq.com/s/78KBHc4-4N5b2vfL9SkutQ) ⭐️ 7.0/10

DeepSeek announced that developers can enable deep-thinking search, file input, link reading, and voice capabilities in existing API calls by setting the corresponding parameters, with the server handling tool invocation and context assembly. The V4.1-Flash model is supported across three interfaces, while Search, Fetch, OCR, ASR, and TTS can also be called separately. DeepSeek additionally open-sourced a chat frontend demo that can import conversation history. The announcement does not provide pricing, quota, endpoint schema, or regional-availability details and has not been independently verified.

telegram · zaihuapd · Nov 13, 14:27

**「Background」** DeepSeek&\#x27;s API already exposed model endpoints that applications call directly; the new suite is an extension in which developers enable parameters in those existing calls to add search, file, link-reading, and voice capabilities. The server then performs tool calls and context assembly, reducing the orchestration developers must handle themselves, while Search, Fetch, OCR, ASR, and TTS can also be called separately.

**「Impact」** Developers can integrate individual capabilities such as OCR or TTS through separate endpoints instead of adopting the full chat stack, and can use the open-source demo as a starting point for locally deploying a web client against the API. Teams evaluating adoption will still need endpoint schemas, pricing, and quota information that the announcement leaves unspecified.

**Tags**: `#DeepSeek`, `#LLM APIs`, `#multimodal`, `#tool calling`, `#open source`

---

<a id="item-tech-news-6"></a>
### [OpenAI launches ChatGPT Wallet for US Pro users with tokenized agent payments](https://openai.com/index/introducing-chatgpt-wallet/) ⭐️ 7.0/10

OpenAI launched ChatGPT Wallet in the US for ChatGPT Pro subscribers aged 18 and older who use a US-issued card, available through dots. The wallet lets agents make purchases using payment tokens issued by the card networks instead of exposing the user&\#x27;s real card number, through partnerships with American Express, Mastercard, and Visa. For each purchase, the user reviews the item and amount and confirms with Face ID or fingerprint.

telegram · zaihuapd · Nov 13, 15:43

**「Background」** ChatGPT Wallet depends on card-network tokenization: the payment network issues a surrogate credential tied to a user’s card, allowing a purchase to be charged without exposing the underlying card number to the agent.

**「Impact」** The immediate compatibility limit is that the feature is restricted to US Pro subscribers with US-issued cards; for those users, every agent-initiated purchase still requires a per-transaction item-and-amount review plus biometric confirmation.

**Tags**: `#OpenAI`, `#ChatGPT`, `#agentic payments`, `#payment tokenization`, `#digital wallets`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Lutnick faces scrutiny over sons&\#x27; firm&\#x27;s Nvidia ties](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 8.0/10

Commerce Secretary Howard Lutnick is facing conflict-of-interest questions over his sons’ firm Cantor Fitzgerald’s Nvidia ties after Nvidia CEO Jensen Huang resigned and Axios reported Lutnick resisted a U.S. crackdown on suspected Nvidia chip smuggling to China. Cantor’s reported Nvidia share count, excluding options, fell 49% between September 2025 and March 2026 to 1.78 million shares worth $310 million, though CNBC found no evidence the change was tied to intelligence warnings.

rss · CNBC Finance · Nov 13, 23:42

**「Background」** Lutnick left Cantor Fitzgerald to become commerce secretary in February 2025; the department he now leads administers U.S. export controls, including the entity list of companies restricted from receiving certain American technology, while his sons Brandon and Kyle run the firm.

**Tags**: `#Nvidia`, `#U.S. export controls`, `#Commerce Department`, `#corporate governance`, `#semiconductor industry`

---

<a id="item-finance-news-2"></a>
### [Goolsbee Says Fed Has &\#x27;Work to Do&\#x27; on Inflation as October PPI Hits 6.5%](https://www.cnbc.com/2026/11/13/chicago-feds-goolsbee-says-central-bank-has-definitely-got-work-to-do-on-inflation.html) ⭐️ 7.0/10

Chicago Fed President Austan Goolsbee said the Federal Reserve &quot;has definitely got work to do&quot; to restore its inflation credibility, after October producer prices rose 0.3% for the month and 6.5% from a year earlier — the highest annual gain since November 2022. Markets were fully pricing a quarter-percentage-point rate increase at the Dec. 8-9 FOMC meeting, according to CME Group&\#x27;s FedWatch.

rss · CNBC Finance · Nov 13, 14:22

**「Background」** The Fed targets 2% annual inflation and sets interest rates at Federal Open Market Committee meetings; Goolsbee is not currently an FOMC voter and will be in 2027, so his remarks reflect the policy debate rather than a vote at the Dec. 8-9 meeting.

**Tags**: `#Federal Reserve`, `#Inflation`, `#Monetary policy`, `#PPI`, `#Interest rates`

---