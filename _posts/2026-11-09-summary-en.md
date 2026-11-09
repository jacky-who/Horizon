---
layout: default
title: "Horizon Summary: 2026-11-09 (EN)"
date: 2026-11-09
lang: en
---

> From 29 items, 4 important content pieces were selected

---

**Technology News**
1. [Llama-modchip claims 284B DeepSeek on 64GB RAM without a GPU](#item-tech-news-1) ⭐️ 7.0/10
2. [Outlook.com Reportedly Rejects Mail From Domains Without DMARC](#item-tech-news-2) ⭐️ 7.0/10
3. [Goldman Sachs reportedly pulls Claude Code from bankers and traders](#item-tech-news-3) ⭐️ 7.0/10
4. [Nvidia board reportedly probes intelligence operation targeting Jensen Huang](#item-tech-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Llama-modchip claims 284B DeepSeek on 64GB RAM without a GPU](https://github.com/synchopate/llama-modchip) ⭐️ 7.0/10

A GitHub project called Llama-modchip claims it can run a 284B-parameter DeepSeek model on 64GB of RAM without a GPU. The repository has drawn Hacker News scrutiny rather than independent confirmation: one commenter testing a different model, Nemotron, on a 16-core Ryzen 7945HX with 96GB DDR5 reported roughly the same CPU throughput as plain llama.cpp except for faster prompt prefill, and said they could not find a DeepSeek option in the project&\#x27;s “modchip setup.” The discussion also questions how much aggressive quantization is needed to fit the model into 64GB and what that does to output quality.

hackernews · joshcsimmons · Nov 8, 10:22 · [Discussion](https://news.ycombinator.com/item?id=50411961)

**「Background」** Large mixture-of-experts \(MoE\) models such as DeepSeek&\#x27;s keep total parameter counts high while routing each token through only a small fraction of them, so inference cost tracks the active parameters rather than the full weight set. The project&\#x27;s own description frames the goal as breaking a &quot;64 GB RAM wall,&quot; running the model purely on CPU at a 256K context window while staying under roughly 59 GiB of memory. Projects like this build on llama.cpp, the CPU-capable inference engine that commenters used as their baseline for comparison.

**「Impact」** Developers should treat the 64GB DeepSeek claim as a benchmark target rather than a turnkey setup: the only reported hands-on comparison found faster prefill but no general CPU speedup over llama.cpp for another model, and the DeepSeek path was not located. Users who need quality-sensitive output should also check the quantization level, since commenters warn that compression below 4 bits can cause significant degradation.

**「Community Discussion」** Commenters mixed enthusiasm for cheaper local inference with skepticism about the repo&\#x27;s novelty and quantization costs. aappleby described the project as AI-generated and said it ran about the same as plain llama.cpp on CPU except for faster prefill, while armcat warned that quantization has non-linear effects and that quality generally falls sharply below 4-bit, with sub-8-bit already a large drop in their speech-model work.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/synchopate/llama-modchip">GitHub - synchopate/llama-modchip: Run 284B DeepSeek-V4 ...</a></li>

</ul>
</details>

**Tags**: `#local-llm-inference`, `#quantization`, `#moe-models`, `#consumer-hardware`, `#llama.cpp`

---

<a id="item-tech-news-2"></a>
### [Outlook.com Reportedly Rejects Mail From Domains Without DMARC](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) ⭐️ 7.0/10

Outlook.com is reportedly rejecting email from domains that do not publish DMARC records, according to a Mailroute blog post. The report is secondhand and provides no official Microsoft confirmation, SMTP error codes, start date, or enforcement timeline, so it describes observed behavior rather than a documented policy change. If accurate, domain owners and self-hosted mail operators sending to Outlook.com would need DMARC configured to avoid rejection.

hackernews · xmddmx · Nov 8, 19:20 · [Discussion](https://news.ycombinator.com/item?id=50416158)

**「Background」** DMARC is a DNS-published policy that ties SPF and DKIM authentication to the From domain and tells receiving mail systems how to handle messages that fail alignment checks. A domain with no DMARC record has published no such handling instruction, so the reported Outlook.com behavior would make the record mandatory in practice rather than merely advisory.

**「Deliverability impact」** Administrators of domains without a DMARC record should publish at least a monitoring policy and check SPF/DKIM alignment, because the reported behavior puts mail to Outlook.com consumer inboxes at risk of rejection; commenters add that rejection can appear as silent filtering rather than a clear bounce. Microsoft’s previously published requirements covered high-volume senders above 5,000 messages per day, so if enforcement now extends to domains without DMARC generally, smaller and self-hosted senders are the group most likely to be caught unprepared.

**「Community Discussion」** Hacker News commenters focused on silent filtering: one self-hosting administrator said Outlook.com has accepted messages at SMTP but failed to deliver them for years, even with SPF, DKIM, and DMARC configured, and another described non-public blocklists that are difficult to appeal. Others welcomed DMARC enforcement as overdue and said senders who have not configured it are responsible for fixing their setup.

<details><summary>References</summary>
<ul>
<li><a href="https://www.factae.eu/en/article/outlook-com-quietly-rejects-emails-from-domains-without-dmarc-182744">Outlook . com quietly rejects emails from domains without DMARC</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730">Strengthening Email Ecosystem: Outlook’s New Requirements for ...</a></li>
<li><a href="https://mailrisk.io/guides/outlook-sender-requirements-2026">Microsoft Outlook Sender Requirements 2026: SPF, DKIM, DMARC ...</a></li>

</ul>
</details>

**Tags**: `#email-deliverability`, `#DMARC`, `#Microsoft-Outlook`, `#email-authentication`, `#sysadmin`

---

<a id="item-tech-news-3"></a>
### [Goldman Sachs reportedly pulls Claude Code from bankers and traders](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) ⭐️ 7.0/10

Goldman Sachs is reportedly removing Claude Code from its bankers and traders, according to The State of AI. The available account does not specify how many staff are affected, over what timeframe access is being withdrawn, or whether the bank is replacing the tool with another vendor. The report has not been independently confirmed, and Goldman Sachs has not been quoted on its reasons.

hackernews · TheWiggles · Nov 8, 18:16 · [Discussion](https://news.ycombinator.com/item?id=50415628)

**「Context」** As recently as July, Goldman Sachs CIO Marco Argenti publicly praised &quot;vibe coding&quot; by non-technical staff, and Claude Code and GitHub Copilot had been available to the bank&\#x27;s bankers and traders for months before the restriction. The reversal followed an internal guidance update in October, with the bank citing productivity and risk management, and access narrowed to roughly 12,000 engineers plus the &quot;strats&quot; group of engineer-quants who retain it.

**「Impact」** For other banks weighing similar rollouts, the reported reversal shifts the deployment question from model capability to data entitlements: an agent running on a workstation that also reaches client, trade, or position data, email, and the open internet creates an audit and compliance surface that must be solved before front-office deployment. Firms in that position face a choice between confining coding agents to isolated environments and keeping them away from bankers and traders.

**「Community discussion」** Commenters offered competing explanations: one argued that semi-unattended coding agents on machines holding client, trade, and email access hit the &quot;lethal trifecta&quot; of agent risk regardless of vendor, while another reported that their organization has been cutting Claude access because of chronic billing overages and said Gemini is winning budget with flat-rate billing and throttling instead of overage charges. A third commenter described a finance team that was dismissed after using AI to compile regulatory communication records inaccurately — an anecdote presented as reported experience, not verified fact.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/goldman-sachs-pulls-claude-code-and-github-copilot-from-traders-and-bankers">Goldman Sachs Pulls Claude Code and GitHub Copilot From ...</a></li>
<li><a href="https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/">Goldman Sachs pulls AI coding tools from traders and bankers</a></li>
<li><a href="https://daily.dev/posts/goldman-sachs-is-pulling-claude-code-from-its-bankers-and-traders-dmltlbhnz">Goldman Sachs Is Pulling Claude Code from Its Bankers...</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#enterprise AI`, `#Anthropic Claude`, `#security/compliance`, `#financial services`

---

<a id="item-tech-news-4"></a>
### [Nvidia board reportedly probes intelligence operation targeting Jensen Huang](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors) ⭐️ 7.0/10

Nvidia&\#x27;s board of directors is reportedly examining an intelligence operation that targeted CEO Jensen Huang, not investigating Huang himself. The submission&\#x27;s headline—&quot;Nvidia Board of Directors Is Investigating Jensen Huang&quot;—misstates the direction of the probe, a point commenters flagged. A Bloomberg report cited in the thread describes the matter as a spying case, but the item includes no board statement text or independent confirmation of the operation&\#x27;s details.

hackernews · vincentchau · Nov 8, 20:26 · [Discussion](https://news.ycombinator.com/item?id=50416801)

**「Background」** According to Bloomberg, Nvidia&\#x27;s board said it was investigating whether a foreign intelligence agency targeted CEO Jensen Huang, and Huang sent his own memo admitting an affair. A Google News aggregation of an FT report said U.S. officials believe Huang had a romantic relationship with a Chinese woman recruited by China&\#x27;s main intelligence agency; the board&\#x27;s focus is therefore the alleged targeting of Huang, not an investigation of Huang himself.

**「Impact」** For Nvidia&\#x27;s customers, partners, and investors, the reports raise governance and CEO-continuity questions at the company described as the central supplier of AI compute; the supplied evidence does not indicate any change to Nvidia&\#x27;s products, supply, or operations.

**「Community discussion」** Commenters focused on correcting the submission title: nrmitchi wrote that the board is investigating something that happened to Huang, not investigating Huang himself. Another commenter linked a Bloomberg report on the case, while others speculated about foreign intelligence interest in a prominent CEO without treating those theories as established.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-08/read-the-memos-from-nvidia-s-board-and-ceo-jensen-huang">Read the Statements From Nvidia ’s Board and CEO Jensen Huang</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pKNTRhc0VoRmVQQ1JRNXYzVF9TZ0FQAQ?hl=en-US&amp;gl=US&amp;ceid=US:en">US officials claim Chinese spy targeted Nvidia CEO Jensen Huang ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#cybersecurity`, `#AI hardware industry`

---