---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02
lang: en
---

> From 37 items, 8 important content pieces were selected

---

**Technology News**
1. [vLLM v0.33.0rc3 drops CUDA 12.9, moves to PyTorch 2.14](#item-tech-news-1) ⭐️ 7.0/10
2. [Kyle Kingsbury: LLMs erode trust in software documentation](#item-tech-news-2) ⭐️ 7.0/10
3. [SemiAnalysis: Bipartisan Datacenter Backlash Puts 2028 Buildout at Risk](#item-tech-news-3) ⭐️ 7.0/10
4. [LongCat-2.5 released: 1.6T-parameter native multimodal model for agent tasks](#item-tech-news-4) ⭐️ 7.0/10
5. [ChatGPT share-link flaw allowed session code execution; OpenAI patched it](#item-tech-news-5) ⭐️ 7.0/10
6. [WIRED: 400+ AI Apps Allegedly Hid Deepfake Porn Features](#item-tech-news-6) ⭐️ 7.0/10

**Technology Blog**
1. [Why LLM Alignment Is Incoherent, Not Just Unsolved](#item-tech-blog-1) ⭐️ 7.0/10

**Financial News**
1. [Anthropic 最新 IPO 文件显示，前九个月营收 332 亿美元，净亏损 1040 亿美元](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.33.0rc3 drops CUDA 12.9, moves to PyTorch 2.14](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 7.0/10

vLLM published notes for v0.33.0rc3, a release candidate that the project says contains 927 commits from 389 contributors, upgrades the stack to PyTorch 2.14.0 with torchvision 0.29.0 and Triton 3.8.0, and makes CUDA 13.0 the only published CUDA artifact line by dropping CUDA 12.9 wheels and the \`-cu129\`/\`-cu129-ubuntu2404\` images. The notes also describe a CUDA wheel that is ABI stable with libtorch, an AWS EFA image bundling EFA libraries and the EFA build of the Mooncake transfer engine for KV transfer and multi-node serving on EFA-enabled EC2 instances, and a shorter \`vllm/vllm\` alias for every image. New model support listed includes Reflection Beam-1.0 \(501B MoE, 23B active\) with its DFlash2 drafter, Yandex AliceAI-Foundation-80B-A3B, Recursive Flint \(40B MoE, 2.5B active\), Muse Spark Open, and Step-5 Preview. The notes use \`v0.33.0\` tags for artifacts rather than \`rc3\`, so the exact image or wheel tag should be checked before deployment.

github · khluu · Nov 2, 10:10

**「Artifact variants」** vLLM publishes separate Python wheels and Docker images per accelerator stack—CUDA, ROCm, XPU, and CPU—so deployments pin both a vLLM release and an explicit wheel or image tag. In the 0.33.0 notes, CUDA 13.0 becomes the sole default CUDA artifact: the CUDA 12.9 wheels and the \`-cu129\` / \`-cu129-ubuntu2404\` images are no longer published, while ROCm 10.0 becomes the default ROCm build and ROCm 7.2 remains available under a \`-rocm72\` tag.

**「Impact」** Teams whose deployment pins CUDA 12.9 must move to the CUDA 13.0 wheels and images or remain on a prior vLLM release. The release also removes Medusa and the MLP speculator, removes the legacy Ray compiled-graph executor, requires NIXL 1.5 or newer for the NIXL connector, and returns HTTP 503 for requests sent while generation is paused.

**Tags**: `#vllm`, `#llm-inference`, `#release`, `#pytorch`, `#cuda`

---

<a id="item-tech-news-2"></a>
### [Kyle Kingsbury: LLMs erode trust in software documentation](https://simonwillison.net/2026/Nov/1/kyle-kingsbury/) ⭐️ 7.0/10

In his Jepsen analysis of ParticleDB 1.1.4, Kyle Kingsbury argues that LLM use &quot;erodes trust in documentation, in software, and in the organizations which produce them.&quot; He writes that signals engineers previously relied on as markers of a mature system &quot;are now easier to counterfeit,&quot; and suggests engineers may begin treating any new software project with suspicion. Kingsbury frames the result as an open question for maintainers: how to ensure correct software and accurate documentation, and then how to demonstrate that quality to users. The passage is an argument advanced within the analysis, not an independently measured finding.

rss · Simon Willison · Nov 1, 16:49

**「Background」** The quotation comes from Jepsen&\#x27;s analysis of ParticleDB 1.1.4, part of a test campaign covering versions 1.1.4 through 1.1.18.11.rc-22 on Debian 13 nodes, containers, and EC2 VMs. Jepsen&\#x27;s review challenged ParticleDB&\#x27;s claim to be PostgreSQL-compatible, reporting frequent transactional anomalies and describing the system as &quot;a library of confusion&quot;; Kingsbury&\#x27;s broader argument about LLM-era trust follows from that evaluation.

**「Impact」** For maintainers, the practical consequence Kingsbury identifies is a verification burden: producing correct software and accurate documentation is no longer sufficient if the signals used to demonstrate that quality can be imitated. Engineers evaluating unfamiliar projects are left without reliable shortcuts and may need to verify claims directly rather than rely on documentation or apparent maturity.

<details><summary>References</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen : ParticleDB 1 . 1 . 4</a></li>
<li><a href="https://news.ycombinator.com/item?id=50316100">Jepsen : ParticleDB 1 . 1 . 4 | Hacker News</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#software trust`, `#documentation`, `#Jepsen`, `#AI risk`

---

<a id="item-tech-news-3"></a>
### [SemiAnalysis: Bipartisan Datacenter Backlash Puts 2028 Buildout at Risk](https://newsletter.semianalysis.com/p/the-datacenter-backlash-goes-bipartisan) ⭐️ 7.0/10

A SemiAnalysis analysis published Nov. 1 argues that the 2027 US datacenter buildout is largely insulated from the Nov. 3 midterms: about three-quarters of the 33.8 GW due across its top 20 states is already under construction, supporting its forecast of a global +50 GW year. The political risk is concentrated in 2028, when its model projects 62.2 GW of US net additions, most not yet under construction; 13 states with the largest 2028 pipelines account for 43.5 GW, or 70% of the national total, and 10 of them elect governors. The analysis says 9 of 20 midterm nominees want a pause on new construction and the other 11 want conditions, with the split roughly even by party. It cites Texas’s Sept. 21 freeze on TCEQ permits and Oregon’s Oct. 9 expansion of its state-land freeze to air and water-discharge permits through July 1, 2027, noting Texas alone is close to 30% of 2028 US GW.

rss · Semianalysis · Nov 1, 18:40

**「Background」** The piece extends SemiAnalysis&\#x27;s Oct. 16 forecast of a +50 GW global datacenter year in 2027 and its September argument that local moratoriums would delay only about 1.5 GW of the roughly 20 GW then under restrictions. Since then, Texas has stopped processing TCEQ data-center permits until ERCOT completes its interconnection audit, a concrete permitting freeze that makes state elections and reopening timelines material to the 2028 pipeline.

**「Impact」** For developers and power planners, the immediate variable is how long Texas’s TCEQ permitting freeze lasts: a restart after ERCOT’s targeted Dec. 10 report would be a relatively short interruption, while holding approvals through the 2027 legislative session or until new rules take effect could extend the freeze to about eight months or close to a year.

<details><summary>References</summary>
<ul>
<li><a href="https://www.breitbart.com/tech/2026/10/16/texas-ag-ken-paxton-sends-compliance-letters-to-156-data-centers-over-water-usage-reporting/">Texas AG Ken Paxton Sends Compliance Letters to 156 Data Centers ...</a></li>

</ul>
</details>

**Tags**: `#AI datacenters`, `#infrastructure capacity`, `#US policy`, `#power constraints`, `#capacity forecasting`

---

<a id="item-tech-news-4"></a>
### [LongCat-2.5 released: 1.6T-parameter native multimodal model for agent tasks](https://longcat.ai/blog/longcat-2.5/) ⭐️ 7.0/10

LongCat released LongCat-2.5, a native multimodal model with 1.6 trillion total parameters and roughly 48 billion activated per token, aimed at long-horizon agent tasks and agentic coding. It builds on LongCat-2.0 with strengthened visual understanding, encoding visual signals as multi-level discrete tokens that are processed uniformly with text, which the team says enables tasks such as visual programming. The model is available now through the LongCat website trial and an API, but no weights have been published on GitHub or HuggingFace. The announcement gives no benchmark results, and the details come from a single vendor post, so the claimed capabilities have not been independently verified.

telegram · zaihuapd · Nov 2, 03:08

**「Background」** Sparse models separate total parameter count from the compute used for each token; LongCat-2.5 reports 1.6 trillion total parameters but activates about 48 billion per token. In a native multimodal design, visual signals are encoded as multilevel discrete tokens and processed together with text, rather than through a separate vision pipeline. LongCat-2.5 builds on LongCat-2.0, with the new release adding stronger visual understanding and agentic coding.

**「Impact」** Developers can evaluate LongCat-2.5 now through the official trial and API, but cannot self-host it: GitHub and HuggingFace releases are not yet available, so on-premises or fine-tuned deployments must wait. The roughly 48B active parameters per token mean inference cost and latency are tied to the sparse activation rather than the full 1.6T parameter count.

**Tags**: `#LongCat-2.5`, `#multimodal models`, `#agentic coding`, `#model release`

---

<a id="item-tech-news-5"></a>
### [ChatGPT share-link flaw allowed session code execution; OpenAI patched it](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 7.0/10

Parameter researchers reported that a malicious ChatGPT share link could execute code inside a logged-in user&\#x27;s session, read private conversations and send the data to an external server; the victim only had to open the link, with no app installation required. The flaw exploited a message-handling defect between the share-link preview feature and a chart component. OpenAI fixed the issue on October 26, classified it as P1, and paid the research team a $5,000 bug bounty, according to the researchers&\#x27; account.

telegram · zaihuapd · Nov 2, 10:24

**「Context」** ChatGPT share links render a conversation in the recipient’s browser, and the preview and chart components that process the shared message data form part of the attack surface. Parameter reported the flaw through OpenAI’s bug bounty program on October 18, and OpenAI applied a server-side fix eight days later, according to The Hacker News.

**「Impact」** Because exploitation required only that a signed-in user open a crafted link, shared ChatGPT links circulated through chat or email were the practical attack surface, and the researchers say the payload would not have been visible from the link alone before the fix. Users who opened unfamiliar share links before October 26 should treat any private conversations accessible in that session as potentially exposed.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/openai-patches-chatgpt-share-link-flaw-that-hijacked-sessions">OpenAI Patches ChatGPT Share - Link Flaw That Hijacked Sessions</a></li>
<li><a href="https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html">A Shared ChatGPT Link Could Run Attacker Code in Your Session ...</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#security vulnerability`, `#account takeover`, `#OpenAI`, `#AI security`

---

<a id="item-tech-news-6"></a>
### [WIRED: 400+ AI Apps Allegedly Hid Deepfake Porn Features](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 7.0/10

WIRED&\#x27;s November 2 investigation alleged that a network of more than 400 linked AI apps and websites, marketed as ordinary tools such as pet-portrait generators and language-learning services, loaded pornographic deepfake interfaces under specific conditions and let users upload other people&\#x27;s photos to produce explicit images or video. By September, 27 of the apps were still on Google Play and had accumulated more than 350,000 downloads, with many rated suitable for all ages, according to the report. After WIRED supplied details, Apple removed 19 apps and said developers had replaced remote web content after review; Google had already removed most of the apps before being contacted, and Meta said it blocked ads from 209 related apps. WIRED linked the network to Chinese developers and a Hong Kong-registered company through Chinese-language code, hosting and domain clues, but said the operators did not respond and that the attribution is an investigative judgment.

telegram · zaihuapd · Nov 2, 12:45

**「Background」** Pornographic deepfakes are AI-generated explicit images or videos made from someone’s uploaded photo, and consumer-facing tools can produce them without the subject’s consent. The case hinges on how app-store review can be bypassed: Apple said the developers passed review and then changed remote web content, allowing a seemingly ordinary app to load different features later.

**「Impact」** Apple&\#x27;s explanation identifies a concrete moderation gap: developers allegedly swapped remote web content after an app passed review, so store approval did not control what users later saw in the alleged cases. That matters for users who downloaded apps rated for all ages and for review teams assessing apps that load remote web content.

**Tags**: `#AI safety`, `#deepfakes`, `#app store moderation`, `#privacy`, `#investigative journalism`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Why LLM Alignment Is Incoherent, Not Just Unsolved](https://seangoedecke.com/alignment-is-impossible/) ⭐️ 7.0/10

rss · Sean Goedecke · Nov 2, 00:00

**「Background」** Sean Goedecke argues that reliably aligning powerful LLMs is not merely hard but conceptually incoherent: we cannot articulate what it would mean to know an LLM is safe. The older picture of AI as a blind optimizer pursuing a fixed, specifiable goal does not fit modern language models.

**「Solution」** Because LLMs are trained to imitate a vast human corpus, the author says they contain shifting mixtures of personas rather than one formal objective, so there is no goal to specify and constrain. The remaining route is to understand them well enough to trust them, but mechanistic interpretability cannot supply the motive-level understanding that would require—just as tracing a person’s neurons would not let us certify a nanny or president. He identifies three limits: features can only be labeled after the behavior is elicited, so unobserved dangerous behaviors remain untracked; labels are guesses vulnerable to Kripke-style “quaddition” variants, where “kindness” might secretly be conditional; and the per-token combination of features is too complex to interpret, with billions of context-dependent questions. A model checking another model only pushes the problem into regress. The author concedes that chain-of-thought monitoring, sandboxing, human oversight, and feature watching are useful mitigations, and that interpretability helps with ordinary training goals, but says none delivers the safety guarantee alignment would require.

**「Takeaway」** The essay’s conclusion is that alignment’s central demand—knowing an LLM’s motives well enough to guarantee it will never go rogue—rests on a kind of understanding that does not exist even for human minds, so interpretability can improve models without ever solving that problem.

**Tags**: `#AI alignment`, `#mechanistic interpretability`, `#AI safety`, `#LLM behavior`, `#philosophy of mind`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Anthropic 最新 IPO 文件显示，前九个月营收 332 亿美元，净亏损 1040 亿美元](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) ⭐️ 7.0/10

Anthropic 在其更新的 IPO 招股文件中报告称，截至 9 月 30 日的九个月内营收为 332.4 亿美元，同比增长约 1,200%，同期净亏损为 1040 亿美元，而去年同期净亏损为 251 亿美元；相关数据由 CNBC 报道。该公司表示，这一净亏损主要源于可转换债券和衍生负债的公允价值变动，而非经营现金消耗；此外，Anthropic 还披露了约 8,954 亿美元的采购和租赁承诺，几乎全部用于算力和基础设施。

telegram · zaihuapd · Nov 2, 15:12

**「Background」** Anthropic is an AI developer seeking a Nasdaq listing under the ticker ANT, and this is an update to an IPO prospectus that had already shown rapid revenue growth alongside multibillion-dollar losses, partly from accounting charges on financing instruments that could convert into company shares.

**「Impact」** The roughly $895.4 billion in mostly compute-related purchase and lease commitments makes chip suppliers and lease financiers direct counterparties to Anthropic’s spending; Broadcom, for example, is providing a convertible note facility of up to $42 billion that covers about a third of a $125.2 billion five-year TPU lease commitment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fxstreet.com/news/anthropic-ipo-filing-reveals-rapid-growth-as-investors-weigh-an-80-billion-loss-202610270748">Anthropic IPO filing reveals rapid growth as investors weigh an $80...</a></li>
<li><a href="https://www.hokanews.com/2026/09/anthropic-ipo-filing-shows-42-billion.html">Anthropic IPO Filing Shows $42 Billion Net Loss in... - Hokanews</a></li>
<li><a href="https://www.youtube.com/watch?v=E8TJMZeVtHs">Anthropic does not own the data centers it runs on - YouTube</a></li>
<li><a href="https://letsdatascience.com/blog/broadcom-will-lend-anthropic-42-billion-to-lease-broadcoms-own-chips">Broadcom to Lend Anthropic Up to $42 Billion for TPU Chip Leases</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI infrastructure`, `#financial results`, `#net loss`

---