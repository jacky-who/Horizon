---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16
lang: en
---

> From 30 items, 6 important content pieces were selected

---

**Technology News**
1. [Meituan open-sources LongCat-2.5, claiming Ascend-only training](#item-tech-news-1) ⭐️ 8.0/10
2. [MacBook Pro OLED PWM flicker: measurement dispute and sensitivity](#item-tech-news-2) ⭐️ 7.0/10
3. [Explainer Walks Through Positional Embeddings in Modern LLMs](#item-tech-news-3) ⭐️ 7.0/10
4. [Meta FAIR/NYU: vision needs its own parameters, not encoder pretraining](#item-tech-news-4) ⭐️ 7.0/10
5. [Open-source tool tunes pageable cudaMemcpy, reports 5x speedup on B300](#item-tech-news-5) ⭐️ 7.0/10

**Financial News**
1. [Lutnick Faces Ethics Questions Over His Sons&\#x27; Firm&\#x27;s Nvidia Ties](#item-finance-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Meituan open-sources LongCat-2.5, claiming Ascend-only training](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

Meituan&\#x27;s LongCat team has released the weights for LongCat-2.5, a 1.6-trillion-parameter agent model, one week after the model&\#x27;s launch. The model activates about 48 billion parameters per token, accepts text, image, and video inputs, and is published under the MIT license for commercial use. Meituan says it was trained entirely on Huawei Ascend accelerators without Nvidia GPUs and scored 88.4 on Terminal Bench v2.1, just below Claude Opus 5&\#x27;s 89.1. Those training and benchmark figures are company claims and have not been independently verified in the supplied material.

telegram · zaihuapd · Nov 15, 11:08

**「Background」** LongCat-2.5 is a mixture-of-experts model with 1.6 trillion total parameters, of which about 48 billion are activated per token. Meituan&\#x27;s LongCat team published the weights a week after the model&\#x27;s initial launch, so the open-weight release follows that earlier announcement.

**「Impact」** Organizations can use, modify, and commercialize LongCat-2.5 under the MIT license, but the model&\#x27;s 1.6-trillion-parameter size makes self-hosting a substantial infrastructure commitment, and its 88.4 Terminal Bench v2.1 result is close to—not equal to—Claude Opus 5&\#x27;s 89.1. Teams evaluating it for coding agents should test it on their own tasks; the Ascend-only training claim remains a vendor assertion until independently confirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://phemex.com/news/article/meituan-opensources-16tparameter-longcat25-model-trained-entirely-on-domestic-chinese-hardware-103629">Meituan LongCat-2.5: 1.6T MoE AI Model Trained on Huawei Chi ...</a></li>

</ul>
</details>

**Tags**: `#open-source AI`, `#large language models`, `#AI agents`, `#Huawei Ascend`, `#AI hardware`

---

<a id="item-tech-news-2"></a>
### [MacBook Pro OLED PWM flicker: measurement dispute and sensitivity](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 7.0/10

An analysis examines PWM flicker on MacBook Pro OLED displays and argues that the dimming method can make an otherwise better screen harder to use for flicker-sensitive people. The article&\#x27;s 240 Hz PWM figure is contested in the comments: one reader says the evidence points to 480 Hz, or an effective 960 Hz when the two tandem OLED layers run 180 degrees out of phase. Other commenters report that flicker unnoticed by many people can cause nausea and headaches for them. The supplied discussion does not settle the measurement dispute or establish how many users are affected.

hackernews · MacAnorak · Nov 15, 13:15 · [Discussion](https://news.ycombinator.com/item?id=50506719)

**「Background」** PWM is a dimming technique that rapidly switches OLED pixels on and off; it is separate from the display refresh rate. Earlier lab testing of the new 14-inch MacBook Pro with PROLED XDR reported 240 Hz PWM at brightness settings of 99% or lower with about 56% flicker amplitude, and subsequent owner reports described headaches and dizziness among PWM-sensitive users.

**「Impact」** Flicker-sensitive buyers may need to try the MacBook Pro OLED in person or wait for independent PWM testing before committing, because commenters describe symptoms ranging from mild annoyance to nausea and headaches.

**「Community Discussion」** Commenters focus on two issues: one disputes the 240 Hz PWM figure by arguing the tandem OLED layers run at 480 Hz out of phase for an effective 960 Hz, while others describe severe sensitivity to flicker that less-sensitive users do not perceive.

<details><summary>References</summary>
<ul>
<li><a href="https://www.appleheadlines.com/macbook-pro-oled-eye-strain-pwm-flicker/">MacBook Pro OLED Eye Strain &amp; PWM Flicker: 7 Moves - AH</a></li>
<li><a href="https://www.macobserver.com/news/oled-macbook-pro-owners-report-headaches-and-dizziness-from-screen-flickering/">OLED MacBook Pro Owners Report Headaches and Dizziness From ...</a></li>
<li><a href="https://appleinsider.com/articles/26/11/10/if-youre-getting-dizzy-using-proled-macbook-pro-you-are-not-alone">Pulse width modulation on MacBook Pro with PROLED - AppleInsider</a></li>

</ul>
</details>

**Tags**: `#OLED PWM`, `#display flicker`, `#MacBook Pro`, `#hardware usability`, `#tandem OLED`

---

<a id="item-tech-news-3"></a>
### [Explainer Walks Through Positional Embeddings in Modern LLMs](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 7.0/10

A technical explainer examines how positional embeddings are implemented in modern large language models, the component that lets transformer attention account for token order. The piece is educational rather than a report of new research or a shipped system, and it stays at the implementation level. In the Hacker News thread, commenter programjames argued that implementation alone does not give a full understanding: they frame positional embeddings as group representations, a view they say shows how such embeddings are found and parameterized to be differentiable and learnable, citing rotary positional embeddings as representations of the translation group. The supplied comment excerpt is truncated mid-explanation of the n-dimensional translation group ℝⁿ, so the rest of that argument is not available here.

hackernews · vismit2000 · Nov 15, 12:14 · [Discussion](https://news.ycombinator.com/item?id=50506376)

**「Background」** Positional information in transformers has evolved from learned absolute position embeddings, as used in GPT-2, toward relative schemes. RoPE, introduced in the 2021 RoFormer paper, rotates query and key vectors before the attention dot product and is now the dominant positional method in frontier models.

**「Community Discussion」** Commenter programjames contended that the article explains only the implementation of positional embeddings, while real understanding requires the underlying theory, presenting positional embeddings as group representations and rotary embeddings as representations of the translation group. This is one commenter&\#x27;s theoretical framing rather than a finding established by the article, and the excerpt cuts off before the argument is complete.

<details><summary>References</summary>
<ul>
<li><a href="https://magazine.sebastianraschka.com/p/understanding-positional-embeddings">Understanding Positional Embeddings in Modern LLMs</a></li>
<li><a href="https://www.institutepm.com/knowledge-hub/rope-alibi-yarn-explained">RoPE , ALiBi , and YaRN Explained: How Modern LLMs Handle Long...</a></li>

</ul>
</details>

**Tags**: `#positional embeddings`, `#LLMs`, `#transformer architecture`, `#machine learning education`

---

<a id="item-tech-news-4"></a>
### [Meta FAIR/NYU: vision needs its own parameters, not encoder pretraining](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 7.0/10

A Meta FAIR and NYU preprint reports controlled experiments across 200+ multimodal LLMs, all trained from scratch \(LLM included\) on the same data, to separate three choices normally bundled into a vision encoder: separate pretraining, parameters used only by vision tokens, and placement before the LLM. The authors find separate encoder pretraining is optional — encoders pretrained with four objectives \(contrastive, self-supervised, and two captioning\) at best tie a from-scratch encoder at matched lifetime compute, and even &quot;free&quot; pretraining did not help; pretraining MetaCLIP 6.5x longer raised ImageNet linear-probe accuracy from 80.4% to 84.4% without improving VQA. Vision-only parameters, by contrast, were required: encoder-free models trailed at every backbone size from 0.6B to 6.4B and needed roughly 3x the compute to catch up, while giving the LLM the encoder&\#x27;s parameters improved text but not VQA. Placement was also optional — an &quot;in-fusion&quot; design adding zero-initialized vision-only weights to the LLM&\#x27;s first 8 layers matched the encoder from 1.7B to 6.4B with about 13% lower time to first token, and at 1.7B reached 45.0 VQA versus 44.4 for the encoder, 42.3 when text shared those weights, and 35.1 when the branches sat in the last 8 layers. Main comparisons use Qwen3-1.7B and 4B configurations with 0.4B vision parameters, evaluated on 16 Cambrian VQA benchmarks at 448 px and 12 language benchmarks; the work is a preprint summary posted by a co-author, not a peer-reviewed publication.

reddit · r/MachineLearning · /u/trungh98 · Nov 15, 17:38

**「Background」** Multimodal LLMs commonly pair a language model with a vision encoder, often one pretrained separately, but that standard design bundles three distinct choices: separate vision pretraining, parameters used only by vision tokens, and placement of the encoder before the LLM. Comparisons between published models cannot isolate those choices because the models differ in training data and compute and rarely account for encoder pretraining; the preprint separates them to test each one directly.

**「Impact」** For teams training multimodal models under a fixed compute budget, the result implies encoder pretraining is a place to save rather than spend: the same budget is better allocated to dedicated vision-only parameters inside the LLM, and encoder-free architectures should be planned with roughly 3x the training compute if they are to match. The reported ~13% lower time to first token for the in-fusion placement is also a concrete serving consideration, though it comes from a single preprint and has not been independently reproduced.

**Tags**: `#multimodal LLMs`, `#vision encoders`, `#pretraining`, `#model architecture`, `#controlled experiments`

---

<a id="item-tech-news-5"></a>
### [Open-source tool tunes pageable cudaMemcpy, reports 5x speedup on B300](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

An open-source tool called cudamemcpy-tuner, invoked as \`cmt tune -- python bench.py\`, is claimed to make pageable \`cudaMemcpy\` transfers about 5x faster on an NVIDIA B300 GPU. In the author&\#x27;s example, CPU-to-GPU throughput for a 1 GB uint8 tensor rose from 10.2 GB/s to 51.5 GB/s after tuning. The post links to a blog and GitHub code, but the result is self-reported and not independently verified, and the Reddit post does not provide broader compatibility or methodology details.

reddit · r/MachineLearning · /u/makneeee · Nov 15, 18:20

**「Why pageable copies were slow」** A cudaMemcpy out of ordinary pageable host memory is slower than a copy from pinned memory because the driver must first stage the data through an internal page-locked buffer, so NVIDIA&\#x27;s long-standing optimization guidance is to allocate with cudaMallocHost and copy from pinned memory instead. A 1 GB benchmark write-up from June 2025 illustrates the same gap, noting that the hidden staging step in pageable copies can roughly halve effective host-to-device bandwidth. The posted tool targets that pageable path directly, aiming to raise transfer rates for code that keeps using ordinary pageable allocations.

**「Impact」** For developers who move data with pageable CUDA copies, the tool provides a concrete command to test on their own workloads rather than relying on the B300 figure. Because the 5x claim comes from one author-run benchmark, adoption should follow reproduction on the target GPU and application.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/">How to Optimize Data Transfers in CUDA C/C++ | NVIDIA ...</a></li>
<li><a href="https://jinseok-moon.github.io/p/pinned-memory/">CUDA Pinned vs Pageable Memory: Faster Host-to-Device Transfers</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#GPU memory transfer`, `#performance optimization`, `#open source tools`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Lutnick Faces Ethics Questions Over His Sons&\#x27; Firm&\#x27;s Nvidia Ties](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 8.0/10

CNBC reported that Commerce Secretary Howard Lutnick faces ethics questions because Cantor Fitzgerald, the Wall Street firm he formerly ran and now led by his sons, reported a 49% drop in its Nvidia share count between September 2025 and March 2026 while he oversaw enforcement of chip export controls on China. The report cites an ethics expert saying there is no proof Lutnick shared nonpublic information, and CNBC said it found no evidence the holdings changes were tied to intelligence warnings or that the firm&\#x27;s business interests influenced his decisions.

rss · CNBC Finance · Nov 15, 19:58

**「Background」** Howard Lutnick ran the Wall Street firm Cantor Fitzgerald before becoming Commerce Secretary in February 2025, putting him in charge of the department that enforces chip export controls, including the entity list of restricted companies. Scrutiny of his Nvidia ties intensified after CEO Jensen Huang resigned in November following reports of an affair with an alleged Chinese spy.

**「Impact」** Because Megaspeed has not been added to Commerce’s entity list, U.S. technology suppliers do not face the entity-list licensing requirement for exports to it, leaving a gap in the controls aimed at blocking Nvidia chip flows to China unless another restriction applies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/nov/12/nvidia-ceo-jensen-huang-resigns">Jensen Huang resigns as Nvidia CEO after alleged... | The Guardian</a></li>
<li><a href="https://www.reuters.com/business/retail-consumer/bessent-says-treasury-favored-limits-megaspeed-2026-11-13/">Bessent blames Commerce Dept over lack of export controls for ...</a></li>
<li><a href="https://www.ft.com/content/afb6c960-a910-4d67-9588-73ba3bea5b06?syn-25a6b1a6=1">US commerce department delays Megaspeed’s inclusion on trade ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Howard Lutnick`, `#Cantor Fitzgerald`, `#export controls`, `#conflict of interest`

---