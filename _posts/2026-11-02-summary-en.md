---
layout: default
title: "Horizon Summary: 2026-11-02 (EN)"
date: 2026-11-02
lang: en
---

> From 45 items, 11 important content pieces were selected

---

**Technology News**
1. [Terry Tao Argues AI Has Changed Mathematics; HN Debates Proof and Credit](#item-tech-news-1) ⭐️ 8.0/10
2. [No Free Lunch in RLVR: Pass@1 Gains Imply a Pass@k Crossover](#item-tech-news-2) ⭐️ 8.0/10
3. [vLLM v0.33.0rc3 adds models, drops CUDA 12.9](#item-tech-news-3) ⭐️ 7.0/10
4. [SemiAnalysis introduces GDPx benchmark for high-value AI domains](#item-tech-news-4) ⭐️ 7.0/10
5. [SemiAnalysis: 2028 Datacenter Buildout Exposed to State Election and Permitting Risk](#item-tech-news-5) ⭐️ 7.0/10
6. [ISTA releases 763B DeepSeek-V4.1-Flash-1017 Coder at ~1 bit/param](#item-tech-news-6) ⭐️ 7.0/10
7. [CLEAR report: tokenizer costs vary up to 17x across languages](#item-tech-news-7) ⭐️ 7.0/10
8. [LongCat-2.5 arrives as 1.6T-parameter native multimodal model](#item-tech-news-8) ⭐️ 7.0/10
9. [OpenAI Fixes P1 ChatGPT Share-Link Account-Takeover Flaw](#item-tech-news-9) ⭐️ 7.0/10
10. [WIRED finds 400+ AI apps hiding pornographic deepfake tools](#item-tech-news-10) ⭐️ 7.0/10

**Technology Blog**
1. [Why Sean Goedecke Calls LLM Alignment Incoherent](#item-tech-blog-1) ⭐️ 6.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Terry Tao Argues AI Has Changed Mathematics; HN Debates Proof and Credit](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/) ⭐️ 8.0/10

Terry Tao has published an essay titled &quot;Mathematics has changed. Let&\#x27;s act like it,&quot; arguing that AI-assisted proof and discovery have altered mathematical practice enough that the field should revisit its norms around proof, credit, and the value of doing the work personally. The post, published November 1, 2026, is commentary and cultural argument rather than a new technical result; the available material names no specific AI system, version, or measured capability. It drew a substantial Hacker News discussion in which commenters disputed whether mathematics is primarily a means of advancing science or a craft whose value lies in the doing.

hackernews · smilelamp · Nov 1, 18:28 · [Discussion](https://news.ycombinator.com/item?id=50328251)

**「Background」** The essay is a guest post by Frank Calegari published on Terence Tao&\#x27;s blog. The Hacker News thread takes up its argument about how mathematical credit should work when AI can produce proofs: the discussion emphasizes understanding, digesting, and extending results rather than only supplying the original proof step.

**「Impact on Credit and Verification」** For mathematicians, reviewers, and hiring or promotion committees, the concrete pressure is on how credit is assigned: one widely echoed reading of Tao&\#x27;s position is that a person who selects a worthwhile problem, obtains a proof entirely with AI, understands it thoroughly, and extends it deserves substantial credit even without contributing a new ingredient to the original proof. That shifts the burden of evidence toward demonstrated understanding and follow-on questions rather than toward producing the key step, a standard that institutions would need to make explicit before relying on it.

**「Community Discussion」** Commenter sintara argued that mathematics is the bedrock of other sciences and that the goal is finding solutions and advancing the field, rather than providing isolated puzzles for intellectual recreation. Loxicon pushed back that &quot;doing it&quot; is the point for practitioners, comparing mathematics to writing and software development as a craft valued for its own sake, while bsaul framed the shift as mathematics moving from an age of craftsmanship to an age of industrial production.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50328251">Mathematics has changed . Let &#x27; s act like it | Hacker News</a></li>
<li><a href="https://t.me/kmp500/756">kmp+ – Telegram</a></li>

</ul>
</details>

**Tags**: `#AI-assisted mathematics`, `#research culture`, `#proof and verification`, `#scientific discovery`, `#Hacker News discussion`

---

<a id="item-tech-news-2"></a>
### [No Free Lunch in RLVR: Pass@1 Gains Imply a Pass@k Crossover](https://www.reddit.com/r/MachineLearning/comments/1xlnu1y/r_there_is_no_free_lunch_in_rlvr_under_strategy/) ⭐️ 8.0/10

A preprint-style Reddit post presents a theory paper arguing that, under strategy specialization, RLVR has a no-free-lunch property: every update that raises pass@1 provably lowers success on some prompt. The model treats RLVR as an exponential tilt of the base policy over solution strategies shared across prompts, with the exact condition expressed as a Stiemke duality statement; a 3x3 counterexample shows that being the best strategy on each prompt is not sufficient. Once losses reach the hardest prompts, the paper claims a pass@k crossover is forced, with at most as many crossings as the sign variation of the per-prompt success shift, a bound reported tight for one to six crossings and exactly one in the order-preserving case; with a per-prompt floor, the constrained update traces an optimal pass@1-versus-pass@k trade-off, and forbidding any per-prompt loss removes both the crossover and the pass@1 gain. No new training runs were done; the author provides code and a script checking the paper&\#x27;s numbers, reports one indicative GRPO Omni-MATH crossing between k=64 and k=256, and the truncated Reddit post&\#x27;s claims are not independently validated here.

reddit · r/MachineLearning · /u/SwimmingAmbition5148 · Nov 2, 04:30

**「Background」** Reinforcement learning with verifiable rewards \(RLVR\) trains language models against automatically checkable outcomes, most commonly final answers in mathematics and programming, and has been reported to improve reasoning performance on such tasks \(\[tool-2-1\]\). The paper starts from an evaluation pattern in which an RLVR-trained model leads at pass@1—the probability that one sampled solution is correct—while the base model catches up or leads as k grows in pass@k, which measures whether any of k samples succeeds.

**「Impact」** For teams evaluating RLVR, the paper&\#x27;s practical diagnostic takes base and RL per-prompt success rates from existing eval logs to estimate crossing count, the crossover bound, and the worst pass@k loss, so a pass@1-only report can miss the trade-off the theory predicts. The author asks for per-prompt logs showing two or more crossings, which would be the signature of RL reordering prompt difficulty.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.13837">[2504.13837] Does Reinforcement Learning Really Incentivize...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#RLVR`, `#pass@k`, `#machine learning theory`, `#evaluation`

---

<a id="item-tech-news-3"></a>
### [vLLM v0.33.0rc3 adds models, drops CUDA 12.9](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 7.0/10

vLLM published v0.33.0rc3, a release candidate whose notes are headed v0.33.0, covering 927 commits from 389 contributors. It adds day-0 support for Reflection Beam-1.0, a 501B MoE with 23B active parameters, plus integrations for Yandex AliceAI-Foundation-80B-A3B, Recursive Flint, Muse Spark Open, Step-5 Preview, and several other models. The platform stack moves to PyTorch 2.14.0 with Triton 3.8.0, and release wheels and images are CUDA 13.0-only: CUDA 12.9 artifacts are no longer published, ROCm 10.0 becomes the default, and ROCm 7.2 remains available under a \`-rocm72\` tag. Breaking changes remove Medusa and the MLP speculator, remove the legacy Ray compiled-graph executor, and make requests during paused generation return HTTP 503.

github · khluu · Nov 2, 10:10

**「Background」** vLLM packages its serving stack with a specific PyTorch and accelerator runtime, so changes such as moving to PyTorch 2.14 and publishing only CUDA 13.0 artifacts directly affect installation and image choices. The \`rc3\` suffix means these notes describe a release candidate, not a final v0.33.0 build.

**「Impact」** Teams deploying vLLM on CUDA 12.9 must move to CUDA 13.0 artifacts or pin an older release, and ROCm 7.2 users must use the separate \`-rocm72\` wheels or images; deployments that rely on Medusa, the MLP speculator, or the legacy Ray compiled-graph executor must migrate because those components are removed.

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#PyTorch`, `#CUDA`

---

<a id="item-tech-news-4"></a>
### [SemiAnalysis introduces GDPx benchmark for high-value AI domains](https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities) ⭐️ 7.0/10

SemiAnalysis introduced GDPx, a benchmark for frontier agentic models that scores them across 11 high-value domains—including chip design, cybersecurity, biology, finance, legal, quant trading, software engineering, and recursive self-improvement—while deliberately excluding government, real estate, and insurance. The publisher argues that benchmarks weighted by GDP share or the SOC/O\*NET occupational taxonomy misdirect attention, because the first trillion dollars of AI revenue will concentrate in sectors that can deploy frontier intelligence at high ROI. In the benchmark&\#x27;s published results, SemiAnalysis says even the best model scores 12%, and that safety classifiers lower the overall scores of models such as Opus 5.5 and GPT-6 Astra in cyber, biology, and alignment; excluding those three domains produces different results.

rss · Semianalysis · Nov 2, 01:51

**「Background」** GDPx is positioned against general-purpose AI benchmarks that weight tasks by economy-wide measures such as share of GDP or the SOC/O\*NET occupational taxonomy. SemiAnalysis argues those weightings dilute frontier-model progress, so GDPx instead concentrates on domains it expects to deliver high returns from frontier intelligence, including chip design, cybersecurity, biology, finance, legal, quant trading, and recursive self-improvement.

**「Impact」** Because safety classifiers can suppress scores in cyber, biology, and alignment, GDPx&\#x27;s combined score may not identify the most capable model for a specific domain: SemiAnalysis says Muse Wonder Full is the best available cyber model by a meaningful margin, while safety filtering affects overall standings. Teams choosing models for those domains should check the domain-level results rather than rely only on the aggregate score.

**Tags**: `#AI benchmarks`, `#frontier models`, `#agentic AI`, `#evaluation`, `#SemiAnalysis`

---

<a id="item-tech-news-5"></a>
### [SemiAnalysis: 2028 Datacenter Buildout Exposed to State Election and Permitting Risk](https://newsletter.semianalysis.com/p/the-datacenter-backlash-goes-bipartisan) ⭐️ 7.0/10

SemiAnalysis estimates that roughly three-quarters of the 33.8 GW it models for 2027 across its top 20 US states is already under construction, so next week&\#x27;s midterms should leave that part of the pipeline largely intact and its forecast of a +50 GW global year stands. The exposure sits in 2028: the model shows 62.2 GW of US net additions, most not yet started, and the 13 states with the largest 2028 additions — excluding Virginia and Mississippi, which hold no state elections this November — account for 43.5 GW, or 70% of the national total, with 10 of the 13 electing governors on Nov. 3. The firm says conditions have worsened since its September analysis that moratoriums were not killing the buildout: Texas froze TCEQ permits on Sept. 21 on top of an interconnection-queue audit begun Aug. 3, Oregon extended its state-land freeze to air and water-discharge permits on Oct. 9 through July 1, 2027, and of the 20 gubernatorial nominees it tracks, nine want a pause on new construction while 11 want conditions, split roughly evenly by party. Because Texas alone accounts for close to 30% of 2028 US GW, SemiAnalysis calls a prolonged TCEQ freeze the biggest risk to its forecast, noting Gov. Greg Abbott could reopen permitting after ERCOT&\#x27;s audit \(report targeted for Dec. 10\) and the Texas Water Development Board&\#x27;s water-use review, while challenger Gina Hinojosa proposes a moratorium until legislation passes.

rss · Semianalysis · Nov 1, 18:40

**「Background」** Large datacenter projects need state and local environmental permits and grid approvals before construction, so a freeze by a single agency can delay a campus even when its power and land are already secured. SemiAnalysis&\#x27;s September analysis had estimated that only about 1.5 GW of the roughly 20 GW inside local restrictions faced delay, because many projects already had protections or did not need the affected approval until after the pause expired.

**「Impact」** For developers with 2028 capacity in Texas, the decisive variable is when TCEQ resumes issuing permits: SemiAnalysis estimates a freeze lasting through the 2027 legislative session \(Jan. 12–May 31\) would run about five to nine months longer than a December restart, and it cautions that a campus racing toward 2027 delivery may not have that much slack in its schedule.

**Tags**: `#datacenter buildout`, `#AI infrastructure`, `#US midterms`, `#energy policy`, `#regulatory risk`

---

<a id="item-tech-news-6"></a>
### [ISTA releases 763B DeepSeek-V4.1-Flash-1017 Coder at ~1 bit/param](https://www.reddit.com/r/LocalLLaMA/comments/1xlys6k/release_ista_deepseekv41flash1017_gsqrco_coder_a/) ⭐️ 7.0/10

ISTA&\#x27;s Deep Algorithms and Systems Lab has released an experimental Coder build of DeepSeek-V4.1-Flash-1017, a 763.2B-parameter sparse mixture-of-experts model, after GSQ/RCO compression removed half its routed experts so that 192 of 384 remain in every layer. The transformer GGUF is 72.1 GB, versus 138.2 GB for the lab&\#x27;s unpruned IQ2\_XXS build; the release counts that as 1.05 bits per original 551.9B transformer parameter \(rounded to 1 bit\), while the 280.1B retained parameters average 2.06 bits and removed experts count as zero. It runs in llama.cpp b11870 or newer and Strata and reuses the unpruned release&\#x27;s 110.6 GB shared Engram file and vision projector, which need to be downloaded only once. The release reports near-base single-problem coding scores but a larger drop on long agentic repository tasks.

reddit · r/LocalLLaMA · /u/Loginhe · Nov 2, 14:33

**「Context: why 1 bit per parameter here is not 1-bit weights」** Sparse mixture-of-experts models store many more parameters than they use per token: DeepSeek-V4.1-Flash-1017 keeps 384 routed experts per layer but activates only 6, so the full model is far larger than the compute any single token requires. That sparsity is what makes expert pruning viable as a compression route, since dropping whole experts removes stored weights without changing the per-token routing width. The &quot;1 bit per parameter&quot; figure in this release is also measured differently from a normal quantization bit-width: it divides the 72.1 GB file by the original 551.9B transformer parameters, while the parameters actually retained average 2.06 bits.

**「Impact」** Teams using the Coder build for repository-level agentic coding should budget for more accumulated errors: the release reports SWE-bench Verified at 77.00 versus 81.20 for the base model \(94.8% retained\), while LiveCodeBench v6 is 88.57 versus 89.71 \(98.7% retained\).

**Tags**: `#quantization`, `#mixture-of-experts`, `#model-compression`, `#local-llm`, `#gguf`

---

<a id="item-tech-news-7"></a>
### [CLEAR report: tokenizer costs vary up to 17x across languages](https://clear-languages.org/blog/the-tokenizer-tax) ⭐️ 7.0/10

A CLEAR research consortium report says major AI models&\#x27; tokenizers are optimized for English and high-resource languages, causing some languages to consume far more tokens for the same content. Across about 200 languages, the report found token consumption differences of up to 17x. It gives the example of one sentence requiring 13 tokens in English, 26 in Malayalam, and 78 in Amharic. The report says the gap raises user costs and can also increase response latency and reduce effective context capacity.

telegram · zaihuapd · Nov 1, 16:06

**「Background」** Tokenizers split text into the units—tokens—that a model processes, so a language whose text fragments into more pieces consumes more billed usage and context capacity. CLEAR’s study tested this by tokenizing FLORES-200, a benchmark of professionally translated sentences in roughly 200 languages, with models from every major lab; among the tokenizers tested, the gap between the most and least efficiently tokenized language ranged from 2.7x to 17x.

**「Impact」** Developers and organizations serving non-English users may face higher per-request inference costs, slower responses, and less usable context for the same content, so token-based pricing and context budgets should be checked against the target language rather than assumed from English token counts.

<details><summary>References</summary>
<ul>
<li><a href="https://clear-languages.org/blog/the-tokenizer-tax">The Tokenizer Tax | CLEAR</a></li>
<li><a href="https://isoclive.substack.com/p/tokenizer-tax">The Tokenizer Tax: Why Using the Same Model Could Cost Up to ...</a></li>

</ul>
</details>

**Tags**: `#tokenizers`, `#multilingual NLP`, `#LLM efficiency`, `#AI costs`, `#language equity`

---

<a id="item-tech-news-8"></a>
### [LongCat-2.5 arrives as 1.6T-parameter native multimodal model](https://longcat.ai/blog/longcat-2.5/) ⭐️ 7.0/10

LongCat released LongCat-2.5, a native multimodal model with 1.6 trillion total parameters and about 48 billion activated per token, aimed at long-horizon agent tasks. The model builds on LongCat-2.0, strengthens visual understanding and agentic coding, and encodes visual signals as multi-level discrete tokens processed alongside text, including for visual programming tasks. It is available for trial on LongCat&\#x27;s website and via API, but GitHub and Hugging Face releases are not yet open; the release note provides no benchmark results or open weights.

telegram · zaihuapd · Nov 2, 03:08

**「Prior LongCat-2.0 baseline」** LongCat-2.5 follows LongCat-2.0, which the team described as a 1.6-trillion-parameter mixture-of-experts model built on AI ASIC superpods with strong coding and agentic-task performance. The new release keeps that 1.6T total scale while shifting to native multimodal handling — encoding visual signals as multi-level discrete tokens processed together with text — and strengthening agentic coding; unlike the API-accessible model, GitHub and HuggingFace versions are not yet open.

**「API-only release, no self-hosting yet」** Developers who self-hosted the earlier LongCat-2.0 — whose weights are published on Hugging Face — cannot do the same with LongCat-2.5 for now: the new model is reachable only through LongCat&\#x27;s site and API, with GitHub and Hugging Face versions not yet released. Teams that need on-premise deployment or weight-level fine-tuning must either build against the hosted API or wait for an open release.

<details><summary>References</summary>
<ul>
<li><a href="https://longcat.chat/blog/longcat-2.0/">Introducing LongCat - 2 .0</a></li>
<li><a href="https://huggingface.co/meituan-longcat/LongCat-2.0">meituan-longcat/ LongCat - 2 .0 · Hugging Face</a></li>
<li><a href="https://theaidude.net/blog/meituan-longcat-20-16t-open-model-tops-coding-benchmarks">Meituan LongCat - 2 .0: 1.6T Open Model Tops Coding | The AI Dude</a></li>

</ul>
</details>

**Tags**: `#multimodal models`, `#large language models`, `#agentic coding`, `#mixture-of-experts`, `#model release`

---

<a id="item-tech-news-9"></a>
### [OpenAI Fixes P1 ChatGPT Share-Link Account-Takeover Flaw](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 7.0/10

OpenAI fixed a P1 ChatGPT share-link vulnerability on October 26 after Parameter&\#x27;s research team reported that opening a crafted link could execute code in a logged-in user&\#x27;s session, read private conversations, and send data to an external server. The disclosure describes the impact as potential account takeover and says the flaw involved message handling between a preview feature and a chart component, with no app installation required. Parameter says OpenAI paid a $5,000 bounty, but the short report provides no technical reproduction or independent verification.

telegram · zaihuapd · Nov 2, 10:24

**「Background」** Shared ChatGPT links are designed to render a conversation, including rich elements such as chart components, for a recipient who opens the link without installing an app. Because that rendering occurs in the recipient&\#x27;s browser while they may be logged in, a message-handling flaw between a preview feature and a chart component can turn passive link viewing into code execution in the authenticated session.

**「Impact」** For logged-in ChatGPT users, the reported attack required only opening a link, so the exposure did not depend on installing an app. OpenAI&\#x27;s P1 fix closes the reported path, but the disclosure does not say whether users were notified, whether any private conversations were actually exfiltrated, or whether previously shared links remain a concern.

**Tags**: `#ChatGPT`, `#安全漏洞`, `#账号接管`, `#OpenAI`, `#Web安全`

---

<a id="item-tech-news-10"></a>
### [WIRED finds 400+ AI apps hiding pornographic deepfake tools](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 7.0/10

A WIRED investigation published Nov. 2 found that more than 400 linked apps and websites disguised pornographic deepfake features behind ordinary AI tools such as pet-portrait generators and language-learning aids, loading an explicit interface under specific conditions and letting users upload other people&\#x27;s photos to create explicit images or videos. As of September, 27 of the apps were still listed on Google Play, with more than 350,000 cumulative downloads, and many were rated suitable for all ages. After WIRED provided evidence, Apple removed 19 apps and said developers had replaced remote webpage content after review; Google had removed most of the apps before being contacted, and Meta said it blocked 209 related apps from advertising. WIRED linked the network to Chinese developers and a Hong Kong-registered company through Chinese-language code, hosting information, and domains; the operators did not respond, and the report describes the attribution as the outlet&\#x27;s and researchers&\#x27; investigative judgment.

telegram · zaihuapd · Nov 2, 12:45

**「Background」** Pornographic deepfake tools generate explicit images or video from photos uploaded by users, and the reported network concealed those functions behind ordinary AI utilities until specific conditions triggered them. The moderation problem is structural: Apple said the developers replaced remotely loaded webpage content after its app review, so an app that initially passed inspection could later present different material.

**「Impact」** The case indicates that app-store approval and an all-ages rating were not reliable signals of an app&\#x27;s eventual behavior: Apple said developers replaced remote webpage content after the apps passed review, and many of the Google Play apps were rated for all ages. According to the investigation, users who uploaded photos to seemingly benign tools could have had those images processed by an explicit deepfake generator.

**Tags**: `#AI deepfakes`, `#app store moderation`, `#AI safety`, `#platform policy`, `#investigative reporting`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Why Sean Goedecke Calls LLM Alignment Incoherent](https://seangoedecke.com/alignment-is-impossible/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 2, 00:00

**「Background」** Sean Goedecke argues that the standard AI-safety model—a superhuman optimizer with a fixed goal that engineers can specify and constrain—does not describe modern LLMs. That mismatch, he contends, makes “solving alignment” for LLMs not just difficult but incoherent.

**「Solution」** Because LLMs are trained to imitate a huge, varied corpus of human writing, Goedecke says they contain many shifting personas rather than one formalizable goal, so there is nothing to constrain by specification. The fallback is to understand a model well enough to guarantee safety, but he argues that demand is impossible in principle: mechanistic traces through weights do not provide human-like motives, and motives bottom out before that level. He then argues mechanistic interpretability cannot certify safety for three reasons: features are identified only from behavior already elicited, so the shocking unobserved failure is precisely what may be missed; labels such as “kindness” may really be “kindness unless…” and are indistinguishable from alternatives, echoing Kripke’s quaddition; and even a complete feature map would require answering billions of per-token interpretive questions. A model overseen by another model only pushes verification back. Goedecke acknowledges chain-of-thought monitoring, sandboxing, and human oversight as mitigations, but says they are insufficient against superintelligence; interpretability can reduce reward hacking and improve ordinary behavior, not rule out a rogue agent.

**「Takeaway」** Goedecke’s conclusion is that without fixed goals or verifiable motives, confidence in LLM alignment lacks a coherent meaning, so interpretability should be valued as a practical tool rather than mistaken for a safety guarantee.

**Tags**: `#LLM alignment`, `#mechanistic interpretability`, `#AI safety`, `#philosophy of AI`, `#model behavior`

---