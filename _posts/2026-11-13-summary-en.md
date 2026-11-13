---
layout: default
title: "Horizon Summary: 2026-11-13 (EN)"
date: 2026-11-13
lang: en
---

> From 41 items, 14 important content pieces were selected

---

**Technology News**
1. [Rust 1.100 stabilizes never type, custom allocators, and Cargo safeguards](#item-tech-news-1) ⭐️ 9.0/10
2. [Google Announces Gemini 4 Hydrogen and Orchestrator](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic IPO link draws Hacker News debate on valuation and compute](#item-tech-news-3) ⭐️ 8.0/10
4. [UMAP 0.6 adds faster initialization and opt-in optimizers](#item-tech-news-4) ⭐️ 8.0/10
5. [Gemma 3 encodes a spatial map its answers ignore, study finds](#item-tech-news-5) ⭐️ 7.5/10
6. [Hacker News post claims Jensen Huang has resigned; unverified](#item-tech-news-6) ⭐️ 7.0/10
7. [A 2016 Essay on Why Math Alone Won&\#x27;t Make Software Correct](#item-tech-news-7) ⭐️ 7.0/10
8. [smolmaxxing Runs 16B LLMs on Low-Memory Older Devices](#item-tech-news-8) ⭐️ 7.0/10
9. [Chips and Cheese interviews AMD&\#x27;s Mike Clark on Zen 6](#item-tech-news-9) ⭐️ 7.0/10
10. [Microsoft 365 degradation disrupts email as Microsoft applies recovery fix](#item-tech-news-10) ⭐️ 7.0/10
11. [Open-source app replaces subscription lock on a $300 embroidery machine](#item-tech-news-11) ⭐️ 7.0/10
12. [TRIBE v2 audit finds no retinotopy or tonotopy, but MT+ motion signal](#item-tech-news-12) ⭐️ 7.0/10
13. [US Commerce finalizing rule to block Chinese AI firms&\#x27; remote chip access](#item-tech-news-13) ⭐️ 7.0/10

**Financial News**
1. [China approves Eli Lilly’s oral GLP-1 weight-loss drug, a first](#item-finance-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Rust 1.100 stabilizes never type, custom allocators, and Cargo safeguards](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/) ⭐️ 9.0/10

Rust 1.100 has been released, stabilizing the never type and custom allocators. Cargo also gains dependency cooldowns: a minimum publish age setting makes the resolver ignore crate versions published more recently than the configured age unless they are already in Cargo.lock, implementing RFC 3923. Cargo now reports unused dependencies by default at the \`warn\` level, and \`cargo install\` uses the lockfile already present in the \`.crate\` tarball by default, making \`--locked\` a no-op.

hackernews · mbStavola · Nov 12, 18:39 · [Discussion](https://news.ycombinator.com/item?id=50472038)

**「Background」** Rust 1.100&\#x27;s dependency cooldowns are based on Cargo RFC 3923. The RFC defines a resolver cutoff, exposed through the --exclude-newer option, that accepts an RFC 3339 timestamp or a duration and excludes releases published after that point.

**「Impact」** Projects that enable a minimum publish age will intentionally hold back newly published crate versions until they pass the threshold, unless those versions are already pinned in \`Cargo.lock\`. Users of \`cargo install --locked\` will see no behavioral change from that flag because \`cargo-install\` now defaults to the lockfile in the \`.crate\` tarball.

**「Community discussion」** Commenters welcomed the release and pointed to additional stabilized APIs omitted from the blog post, including \`bool::toggle\(\)\`, \`Box::map\(\)\`, \`str::trim\_prefix\(\)\`/\`trim\_suffix\(\)\`, and \`Path::trim\_prefix\(\)\`. One commenter also asked whether compiler speed had improved and complained about repeatedly clearing roughly 90 GB of temporary files with \`cargo clean\`.

<details><summary>References</summary>
<ul>
<li><a href="https://rust-lang.github.io/rfcs/3923-cargo-min-publish-age.html">3923 -cargo-min-publish-age - The Rust RFC Book</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Cargo`, `#programming languages`, `#never type`, `#custom allocators`

---

<a id="item-tech-news-2"></a>
### [Google Announces Gemini 4 Hydrogen and Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/) ⭐️ 8.0/10

Google announced Gemini 4 Hydrogen and an Orchestrator on its Antigravity blog, but the supplied item provides no benchmarks, model specifications, or formal rollout terms. One Hacker News commenter said the change appeared immediately in Gemini, with 3.8 Flash replaced by &quot;4 Hydrogen&quot;; others described the Orchestrator as handling model and effort selection that users previously made manually. The source does not explain how that routing works or what access conditions apply.

hackernews · jonbaer · Nov 12, 18:52 · [Discussion](https://news.ycombinator.com/item?id=50472260)

**「What Orchestrator sits on top of」** Orchestrator is a routing option inside Google Antigravity rather than a single model: Google describes it as pairing Hydrogen with &quot;our strongest models for long-horizon tasks, including Gemini 4 Carbon,&quot; so Hydrogen enters an existing Gemini 4 roster as the lighter, faster tier instead of replacing the heavier models. Commenters on the thread describe the rollout as a swap in the product&\#x27;s model picker, with the 3.8 Flash option they had been using replaced by &quot;4 Hydrogen.&quot;

**「Impact」** For developers who assign specific models to coding subagents, the Orchestrator creates a choice between keeping manual routing and delegating model selection to the system. One commenter welcomed not having to switch models and effort levels manually, while another said they were wary of delegating that authority because models can be optimistic about their own capabilities.

**「Community Discussion」** The most substantive discussion concerned routing trust and latency: one commenter said Argon and Carbon were so slow they had switched to 3.8 Flash, and another was hesitant to let a model choose subagent models. Others focused on naming, arguing that &quot;Hydrogen&quot; continued a confusing scheme after Carbon.

<details><summary>References</summary>
<ul>
<li><a href="https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity">Gemini 4 Hydrogen and Orchestrator | Google Antigravity Blog</a></li>

</ul>
</details>

**Tags**: `#Gemini 4`, `#Google`, `#LLM releases`, `#model orchestration`, `#AI industry`

---

<a id="item-tech-news-3"></a>
### [Anthropic IPO link draws Hacker News debate on valuation and compute](https://ipo.anthropic.com/us/) ⭐️ 8.0/10

A Hacker News post linking to ipo.anthropic.com/us/ drew heavy discussion, but the supplied material contains no page content, so the IPO terms are not independently confirmed here. Commenters citing the linked documents reported a $70–$78 price range, an implied market capitalization near $968 billion, Q3 2026 revenue of $17.0 billion, and $900.9 billion in compute commitments through 2045. Those figures should be treated as community-reported claims rather than verified facts.

hackernews · josephljohnston · Nov 12, 11:46 · [Discussion](https://news.ycombinator.com/item?id=50465829)

**「IPO filing」** Anthropic publicly filed its S-1 on October 26, 2026, to list Class A shares on Nasdaq under the ticker ANT, opening the formal IPO process. An updated filing cited a $70–$78 per-share range and expected proceeds of $57.75 billion to $64.35 billion, with pricing expected in mid-November.

**「Community discussion」** Commenters split between seeing LLM demand as durable and arguing that model access is easy to switch, with cheaper or local models sufficient for many tasks; one thread questioned why Anthropic would accept IPO dilution if recursive self-improvement were near. Others focused on the reported deal structure, including whether earlier Series H investors could be underwater at the low end of the range.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dividenddata.com/stocks/ant">ANT Stock: Anthropic IPO , S-1 Financials &amp; Price Range ( Anthropic ...)</a></li>
<li><a href="https://vectorweekly.com/section/models/how-anthropics-1-404-trillion-valuation-shifts-ai/">How Anthropic ’s $1.404 Trillion Valuation Shifts AI... | Vector Weekly</a></li>
<li><a href="https://www.marketbeat.com/articles/anthropics-ipo-filing-reveals-a-massive-opportunity-for-ai-infrastructure-giants/">Anthropic IPO Filing Signals Billions in Spending for AMZN, GOOGL...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#LLM business models`, `#Hacker News`

---

<a id="item-tech-news-4"></a>
### [UMAP 0.6 adds faster initialization and opt-in optimizers](https://www.reddit.com/r/MachineLearning/comments/1xudaah/umap_06_new_initialization_new_optimizers_and/) ⭐️ 8.0/10

UMAP 0.6 is released for Python users via \`pip install -U umap-learn\` and conda-forge, adding a recursive UMAP-based initialization, new optimizers, and faster nearest-neighbor search. The author reports about 4x faster neighbor search and says a 3-million-paper arXiv dataset completes in under five minutes, compared with 52 minutes for a single-threaded seeded UMAP 0.5 run; these performance and quality claims are not independently verified in the supplied material. The release also claims better fine cluster structure and neighborhood accuracy at million scale and reproducible multithreaded runs with a fixed seed. The new initialization and optimizers are opt-in because they change output: set \`compatibility\_layout=False\` to use them, with defaults planned for future versions.

reddit · r/MachineLearning · /u/lmcinnes · Nov 12, 13:51

**「What UMAP does and what changed underneath」** UMAP is a dimensionality-reduction library that builds a weighted nearest-neighbor graph over high-dimensional data and optimizes a low-dimensional layout to match that graph. In 0.5 and earlier, the layout started from a spectral or PCA embedding and the optimizer relied on negative sampling over a deliberately narrow portion of the attraction–repulsion spectrum, which the announcement describes as a ceiling on quality and on usable repulsion strengths. Version 0.6 replaces both stages: it initializes by running UMAP recursively on a coarse version of the graph, and adds an efficient hard-negative-mining optimizer, both currently opt-in via compatibility\_layout=False.

**「Impact」** Existing pipelines that depend on UMAP 0.5 layouts should stay on the default compatibility path until they validate the changed embeddings; testing the new path requires \`compatibility\_layout=False\`. The multithreaded reproducibility benefit applies only when a fixed seed is set, as described in the announcement.

**Tags**: `#UMAP`, `#dimensionality reduction`, `#machine learning`, `#open source`, `#performance optimization`

---

<a id="item-tech-news-5"></a>
### [Gemma 3 encodes a spatial map its answers ignore, study finds](https://www.reddit.com/r/MachineLearning/comments/1xuqs9d/gemma_3_builds_a_linearly_decodable_spatial_map/) ⭐️ 7.5/10

An independent, preregistered mechanistic-interpretability study reports that Gemma 3 12B and 27B build a linearly decodable spatial map when reading text-only layout descriptions such as &quot;A is 3 north of B, C is 2 east of A.&quot; Probes recovered every object&\#x27;s position, including positions that require combining two sentences, at R² 0.74, but erasing that map cost no more than erasing random directions, indicating the answers never read it. The models instead rely on a two-dimensional per-sentence code identified with DAS at 72% \(12B\) and 83% \(27B\) against 0% for random controls; that code behaves like a switch rather than a coordinate. Reading answers off the unused map beat the model on chain questions, 80% versus 73%. The results cover two model sizes in a single unreplicated report, with paper, code, and demo released by the author.

reddit · r/MachineLearning · /u/Cristhian-AI-Math · Nov 12, 22:29

**「What DAS measures that a probe does not」** The study&\#x27;s causal claim rests on distributed alignment search \(DAS\), a causal-abstraction method that learns a rotation of a model&\#x27;s internal representation so that a chosen subspace lines up with a supplied causal variable, then tests the alignment with interchange interventions rather than mere correlation. That distinction matters here: a linear probe shows only that a position is decodable from activations, while DAS is what lets the authors argue the model actually routes its answers through a particular two-dimensional per-sentence code instead of the spatial map.

**「Impact」** The study&\#x27;s combination of probing and ablation shows that a concept being decodable from a model&\#x27;s activations is not evidence that the model uses it, so interpretability claims about latent structure need a causal check like the one applied here. The 80% versus 73% gap also indicates that externally decoding a latent map the model ignores can outperform its own chain reasoning, a possible route to extracting structure without retraining, though the margin is small and demonstrated only on these two Gemma 3 sizes.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2303.02536">[2303.02536] Finding Alignments Between Interpretable Causal ... Finding Alignments Between Interpretable Causal Variables and ... Interchange interventions / DAS — Paper 2 method Interpretability at Scale: Identifying Causal Mechanisms in ... A Partial Replication of Distributed Alignment Search Interpretability at scale | Proceedings of the 37th ... (PDF) Finding Alignments Between Interpretable Causal ...</a></li>
<li><a href="https://arxiv.org/html/2303.02536v4">Finding Alignments Between Interpretable Causal Variables and ...</a></li>
<li><a href="https://akmaier.github.io/UnderstandingVCS/m_das.html">Interchange interventions / DAS — Paper 2 method</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#Gemma 3`, `#spatial reasoning`, `#probing`, `#LLM representations`

---

<a id="item-tech-news-6"></a>
### [Hacker News post claims Jensen Huang has resigned; unverified](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f) ⭐️ 7.0/10

A Hacker News submission posted on 12 November 2026 asserts that Nvidia CEO Jensen Huang has resigned, linking to a claimed Nvidia newsroom page at the path &quot;nvidia-announces-ceo-transition,&quot; Reuters articles and a Reuters live page whose URL refers to the board meeting over &quot;affair reports,&quot; and a New York Times live page titled &quot;nvidia-jensen-huang-resigns.&quot; The supplied item contains only those headline-style links and no article text from Nvidia, Reuters, the Times, or the AP News URL the submission points to, so the resignation itself is not confirmed by the material available here. The story was published at 13:52 UTC on 12 November 2026 and drew heavy comment traffic, but the thread consists largely of speculation about the cause and consequences rather than first-hand information. Treat the claim as an unverified report until a primary Nvidia announcement or full article text is available.

hackernews · lldb · Nov 12, 13:52 · [Discussion](https://news.ycombinator.com/item?id=50467087)

**「What preceded the resignation」** Jensen Huang founded Nvidia and led it as CEO through the period in which its GPUs became the central hardware of the AI buildout, making his personal standing a market-moving subject in its own right. Reuters and New York Times accounts describe the resignation, dated November 12, 2026, as following revelations of two extramarital affairs, one involving a woman identified by U.S. intelligence as a Chinese spy, which pushed the board into crisis deliberations.

**「Community discussion」** Commenters disagreed sharply about why Huang would be leaving: one argued that a CEO&\#x27;s perceived stability matters enormously for a company at the center of the AI economy, while another contended the alleged affairs are not the real issue and that Nvidia may have been skirting export controls — a claim other commenters \(keeda among them\) disputed as unproven and legally permitted. Others focused on consequences rather than cause, with one saying the risk is Nvidia becoming &quot;just another company&quot; and another hoping a transition would not change the company&\#x27;s stance on blocking inference for unsigned open models in GPU firmware. These are opinions and unverified assertions from the thread, not established facts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investing.com/news/stock-market-news/nvidia-ceo-jensen-huang-to-step-down-in-big-blow-to-ai-boom-5021980">Nvidia CEO Jensen Huang resigns , in blow to AI boom he helped...</a></li>
<li><a href="https://www.nytimes.com/live/2026/11/12/business/nvidia-jensen-huang-resigns">Jensen Huang Resigns as Nvidia CEO After Affairs: Live Updates</a></li>
<li><a href="https://www.aljazeera.com/news/liveblog/2026/11/12/live-jensen-huang-resigns-as-nvidia-ceo-as-affairs-raise-security-concerns">Updates: Jensen Huang resigns as Nvidia CEO amid... | Al Jazeera</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#CEO resignation`, `#AI industry`, `#unverified report`, `#Hacker News`

---

<a id="item-tech-news-7"></a>
### [A 2016 Essay on Why Math Alone Won&\#x27;t Make Software Correct](https://pron.github.io/posts/correctness-and-complexity) ⭐️ 7.0/10

No new capability or release is announced: the item resurfaces a 2016 essay arguing that writing correct software is hard and that mathematical formal methods alone cannot fully solve the problem. The argument is conceptual, and the item&\#x27;s tags point to software correctness, formal verification, formal methods, software complexity, and Rice&\#x27;s theorem. For software engineers, it is an older long-form argument to evaluate, not a new tool or independently measured result.

hackernews · AriFordsham · Nov 12, 10:28 · [Discussion](https://news.ycombinator.com/item?id=50465352)

**「Context」** The essay is a July 2016 piece by Ron Pressler that reviews results from computability and complexity theory to argue that programs and complete understanding—the prerequisite for correctness—are fundamentally at odds. That theoretical framing, including computability results such as Rice&\#x27;s theorem referenced in the discussion, is what makes the question of whether formal methods can fully establish real-world software correctness contentious.

**「Impact」** For teams considering formal methods, the discussion implies an upfront requirement: define the specification and the acceptable input, output, and intermediate states before proof can mean much, especially for software handling messy real-world inputs and human workflows.

**「Community Discussion」** Commenters split over the scope of formal correctness: one argued that abstract mathematical correctness must be distinguished from functioning in the real world, with formal methods valuable only when worth the cost for complex human workflows, while another compared software to contract law, where acceptable inputs, outputs, and intermediate states cannot all be fixed at once \[turbobutton; hinkley\]. Another commenter disputed the essay&\#x27;s invocation of Rice&\#x27;s theorem, arguing it rules out a general decision method for all programs rather than one-off proofs about a particular program, and a further commenter asked how the specification itself is known to be correct \[johnbender; mpweiher\].

<details><summary>References</summary>
<ul>
<li><a href="https://pron.github.io/posts/correctness-and-complexity">Why Writing Correct Software Is Hard - Ron Pressler</a></li>

</ul>
</details>

**Tags**: `#software correctness`, `#formal verification`, `#formal methods`, `#software complexity`, `#Rice&\#x27;s theorem`

---

<a id="item-tech-news-8"></a>
### [smolmaxxing Runs 16B LLMs on Low-Memory Older Devices](https://github.com/hyperionaidev/smolmaxxing/) ⭐️ 7.0/10

The author of the open-source smolmaxxing project is sharing custom kernels and modified models intended to run LLMs on small, old, low-memory hardware, claiming support for models up to 16B parameters on a first-generation iPad Air and a Xiaomi TV box with less than 1GB of usable memory. The kernels, results, and modified Hugging Face models are published for others to reproduce and extend. These are the author&\#x27;s claims; the supplied material provides no independent benchmarks or detailed per-device speed figures.

hackernews · mrashad74 · Nov 12, 15:23 · [Discussion](https://news.ycombinator.com/item?id=50468888)

**「Background」** LLM inference generally requires holding model weights in memory and running many matrix-multiply operations, so older hardware with under 1 GB of usable memory is constrained by both capacity and kernel efficiency. The smolmaxxing project addresses that gap by pairing modified models with custom kernels intended to make inference practical on such devices.

**「Reproducibility and throughput limits」** Developers can check the claims on their own hardware: the repository ships a benchmark harness plus a live token-stream page for llama-server showing confidence colours, top-3 alternatives, speed and box stats, so the numbers are meant to be re-run rather than taken on faith. The reported 5.1 tokens/sec for a 16.3B model on a Xiaomi TV box implies single-digit throughput, so a 500-token answer takes roughly a minute and a half — workable for offline or batch jobs, but not for snappy interactive chat.

**「Community discussion」** Commenters generally welcomed the small-model optimization trend: one described moving from a fine-tuned Qwen 2.5 0.5B conversational model to a locally trained 6.5M-parameter model that can handle reasoning and math, while another asked what practical tasks such small models are actually good for. A separate comment argued that modern coding agents can already build an inference engine from a one-shot prompt, so sourcing old hardware and granting SSH access is now the harder part.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/hyperionaidev/smolmaxxing/">GitHub - hyperionaidev / smolmaxxing : maxxing the ability to run...</a></li>
<li><a href="https://dzen.ru/b/avYB4oD4cDo6u0G6">16 млрд параметров на ТВ-приставке: 5,1 токена в секунду Xiaomi ...</a></li>

</ul>
</details>

**Tags**: `#local LLM inference`, `#edge computing`, `#model optimization`, `#open source`, `#small models`

---

<a id="item-tech-news-9"></a>
### [Chips and Cheese interviews AMD&\#x27;s Mike Clark on Zen 6](https://chipsandcheese.com/p/talking-zen-6-with-mike-clark-at) ⭐️ 7.0/10

Chips and Cheese has published an in-depth interview with AMD&\#x27;s Mike Clark discussing the Zen 6 CPU architecture. The piece is a designer-level technical conversation rather than a product announcement, and the supplied material contains no performance figures, specifications, or availability details, so any specific claims about Zen 6 capabilities would have to come from the interview itself.

hackernews · dverlaeckt80 · Nov 12, 14:12 · [Discussion](https://news.ycombinator.com/item?id=50467460)

**「Background」** Zen is AMD&\#x27;s CPU core family built as a single scalable microarchitecture rather than separate high-power and low-power designs, a point Mike Clark made when the first Zen generation was introduced. Clark is AMD&\#x27;s chief Zen architect, and AMD has announced EPYC Embedded 9006 CPUs built on Zen 6, scaling to 256 cores with PCIe Gen 6 and CXL 3.1 connectivity.

**「Tuning implication」** The interview is architectural discussion rather than a shipping announcement, so it does not by itself establish Zen 6 availability or performance. For teams preparing workloads, independent testing of Zen 6 EPYC parts — Phoronix&\#x27;s runs on the 256-core EPYC 9996 and 96-core EPYC 9686F — found SMT still worthwhile for both performance and power, so disabling SMT on the assumption that it no longer pays off would carry a cost.

**「Community Discussion」** Commenter koutakun described the article as interesting and said it is very rare to see CPU designers go into this level of depth publicly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/news/amd-zen-cpu-microarchitecture,32540.html">Everything Zen : AMD Presents New... | Tom&#x27;s Hardware</a></li>
<li><a href="https://www.techpowerup.com/news-tags/AMD">News Posts matching &#x27; AMD &#x27; | TechPowerUp</a></li>
<li><a href="https://mezha.net/eng/news/mezha-385a51640a816c08fe1be1d3_amd_executives_say/">AMD executives say Zen 6 was not designed specifically for... | Межа</a></li>
<li><a href="https://www.phoronix.com/review/amd-epyc-zen6-smt">AMD Zen 6 SMT Proves Very Advantageous Even For 256... - Phoronix</a></li>

</ul>
</details>

**Tags**: `#AMD Zen 6`, `#CPU architecture`, `#hardware`, `#semiconductors`, `#technical interview`

---

<a id="item-tech-news-10"></a>
### [Microsoft 365 degradation disrupts email as Microsoft applies recovery fix](https://status.cloud.microsoft/) ⭐️ 7.0/10

A Microsoft 365 service degradation disrupted email for users, while at least one organization reported that Teams chat and meetings and its Azure infrastructure remained available. An update from Microsoft quoted in the discussion said that at 9:02 PM UTC it had validated an alternative health-check method on a subset of affected infrastructure, returned those servers to service, and was applying the change more broadly while preparing automated recovery to detect and restart unresponsive servers. The incident also affected Microsoft&\#x27;s status page, which a commenter said was not working well, prompting updates to be relayed via its RSS feed.

hackernews · dkpk · Nov 12, 18:20 · [Discussion](https://news.ycombinator.com/item?id=50471731)

**「Background」** Microsoft 365 bundles Outlook, Teams, Word, Excel, and other cloud services, so customers rely on Microsoft&\#x27;s status page to distinguish a broad platform failure from an isolated product problem. During the November 12, 2026 disruption, independent monitoring by ThousandEyes recorded global Microsoft 365 availability issues, and Downdetector showed a spike of nearly 130,000 user reports.

**「Impact」** Affected administrators could not rely on Teams availability as an all-clear: one organization reported chat and meetings working while email had been down for 5.5 hours, and the status page itself was unreliable enough that RSS carried the updates.

**「Community discussion」** Commenters described the email outage as unusually severe—one said it was their organization&\#x27;s worst Microsoft 365 outage since 2019—while another reported that Outlook desktop could not reach a self-hosted mail account because Microsoft acts as the relay.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thousandeyes.com/blog/microsoft-365-outage-analysis-november-12-2026">Microsoft 365 Outage Analysis: November 12, 2026</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/13/microsoft-outage-outlook-teams-word-excel-reports">Global Microsoft outage affects Outlook and Teams users, with ...</a></li>

</ul>
</details>

**Tags**: `#Microsoft 365`, `#cloud outage`, `#service reliability`, `#incident response`

---

<a id="item-tech-news-11"></a>
### [Open-source app replaces subscription lock on a $300 embroidery machine](https://github.com/simpsoka/zigzag) ⭐️ 7.0/10

Developer simpsoka published zigzag, an open-source application on GitHub, as a replacement for the subscription-gated software workflow that came with their $300 embroidery machine. The project was posted to Hacker News as a Show HN entry on 12 November 2026, framed explicitly as a way to avoid paying the vendor subscription rather than as a commercial product. The submission supplies no implementation details, supported machine models, file formats, license terms, or evidence that the app reproduces every function of the paid workflow, so the scope of what it actually replaces remains unverified. It is a working personal project shared publicly, not a vendor-endorsed tool or an audited compatibility layer.

hackernews · simpsoka · Nov 12, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50470488)

**「Background」** Open-source embroidery software is not new: commenters point to InkStitch, an Inkscape plugin that exports SVGs into machine-readable embroidery formats. Zigzag is described as a visual Mac editor that converts SVGs into PES/DST files and uploads them to a Brother Skitch machine over Bluetooth; older low-cost machines often depend on proprietary cartridges or vendor software.

**「Impact」** For owners of similarly locked-down hobby machines, the practical takeaway is that the software side of the workflow is separable from the hardware, so the viable path is an open-source toolchain rather than continued subscription payments. The immediate compatibility caveat is that the post gives no list of supported machines or stitch file formats, so other owners cannot assume zigzag works with their model without checking the repository themselves.

**「Community Discussion」** Commenters treated the project as part of a broader pattern: gregsadetsky described a friend, Owen Trueblood, reverse engineering the Brother PE-150 and building a replacement motherboard to control it over USB, noting working units sell for around $100 on eBay but get abandoned because of proprietary data cartridges. rocmcd recommended InkStitch, an Inkscape plugin that exports SVGs to embroidery machine formats, while warning that stitch placement, size, type, and layering each require real care. spdustin assumed an LLM did much of the coding and praised that as empowerment for users to build their own fixes, an opinion rather than a confirmed fact about how zigzag was written.

<details><summary>References</summary>
<ul>
<li><a href="https://trendshift.io/repositories/326658">simpsoka / zigzag — GitHub trending stats &amp; insights | Trendshift</a></li>

</ul>
</details>

**Tags**: `#right-to-repair`, `#open-source hardware`, `#reverse engineering`, `#subscription circumvention`, `#embroidery`

---

<a id="item-tech-news-12"></a>
### [TRIBE v2 audit finds no retinotopy or tonotopy, but MT+ motion signal](https://www.reddit.com/r/MachineLearning/comments/1xuillf/does_metas_brainresponse_model_tribe_v2_actually/) ⭐️ 7.0/10

An independent, self-funded audit posted on Reddit reports that Meta&\#x27;s TRIBE v2 brain-response model does not recover classic retinotopic or tonotopic maps. After validating the pipeline against synthetic ground truth, the author found no retinotopic map \(d=0.05, n.s.\) and no tonotopic map \(ρ=-0.07, n.s., even with loudness controlled\), but strong motion selectivity in MT+ \(d=4.31, 52× enrichment over chance\). Eccentricity appeared null by default and became significant under three stimulus-geometry controls, which the author interprets as an image-statistics confound rather than a positional code; the analysis is a single non-peer-reviewed post with linked code and paper.

reddit · r/MachineLearning · /u/Own\_Tank1283 · Nov 12, 17:16

**「Background」** TRIBE v2 is Meta FAIR&\#x27;s second-generation trimodal brain encoder: it takes video, audio, or text as input and outputs a predicted whole-brain fMRI response pattern, and it was released with open weights and reportedly trained on more than 1,000 hours of fMRI from 720 subjects \(tool-2-1, tool-2-2, tool-2-3\). Retinotopy, tonotopy and motion selectivity are standard topographic maps that researchers recover by fitting encoding models to real fMRI data recorded during checkerboard wedges, tone sweeps or moving dots, which gives the audit a well-established benchmark to compare the model&\#x27;s predictions against.

**「Impact」** For researchers using TRIBE v2 as a brain-encoding model, the audit suggests restricting claims about retinotopic or tonotopic position and treating apparent eccentricity effects as requiring stimulus-geometry controls; motion selectivity in MT+ is the topographic-like result that survives. These are single-lab, non-peer-reviewed findings pending replication.

<details><summary>References</summary>
<ul>
<li><a href="https://www.therundown.ai/tools/tribe-v2">TRIBE v 2 : Model , License, Setup &amp; Alternatives</a></li>
<li><a href="https://www.linkedin.com/posts/herambvpatil_meta-tribev2-neuroscience-activity-7446912120987844608-IMJ6">Meta &#x27;s TRIBE v 2 Predicts Brain Response to Video Audio Text</a></li>
<li><a href="https://theomar.me/blogs/adneural">Adneural: TRIBE v 2 + MiroFish for Pre-Launch Ad Testing</a></li>

</ul>
</details>

**Tags**: `#brain-encoding models`, `#fMRI`, `#reproducibility`, `#multimodal models`, `#neuroscience AI`

---

<a id="item-tech-news-13"></a>
### [US Commerce finalizing rule to block Chinese AI firms&\#x27; remote chip access](https://www.theinformation.com/articles/commerce-department-finalizing-long-awaited-ai-remote-access-rule) ⭐️ 7.0/10

The US Commerce Department is finalizing a rule that would stop Chinese AI companies from remotely using advanced AI chips hosted in overseas data centers, with publication possible as soon as this month, according to The Information. The measure would extend existing semiconductor export restrictions to seven countries, including Malaysia, Singapore and Thailand, aiming to close remote-access and chip-smuggling routes. Commerce is still consulting other government agencies before finalizing the text, so the specific requirements and any thresholds remain unknown. The report follows a White House request that Congress legislate to have Commerce write such a rule, and says Nvidia lobbied against closing the remote-access gap, arguing US AI infrastructure needs to win globally.

telegram · zaihuapd · Nov 12, 03:42

**「背景」** 美国现有的半导体出口管制由商务部工业与安全局（Bureau of Industry and Security）执行，主要针对先进芯片的实体运输。据报道，新规则将在此基础上把新加坡、马来西亚、泰国、印度尼西亚、巴西、挪威和南非这七个国家列入许可证清单，并要求提交最终用户报告，目的是堵住通过在海外数据中心租用先进算力来规避管制的路径。

**「Remote compute route at risk」** If finalized, the rule would close the remote-access path that Chinese AI developers have used to rent advanced Nvidia compute through Southeast Asian data centers, which reporting in 2026 described as a major gap in U.S. chip restrictions. China-linked data center operators in the region were already reporting disruption from tightened enforcement in June 2026, and Chinese commentators quoted at the time expected affected firms to seek alternative ways to reach restricted processors rather than halt work.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theinformation.com/articles/commerce-department-finalizing-long-awaited-ai-remote-access-rule">Commerce Department Finalizing Long-Awaited AI Remote Access Rule</a></li>
<li><a href="https://biz.chosun.com/en/en-international/2026/11/12/M2ICNVHJPVCFLJDLAGG5IP4VDE/">US to widen AI chip export controls to seven nations, curb ...</a></li>
<li><a href="https://en.sedaily.com/world/2026/11/12/us-set-to-tighten-ai-chip-export-curbs-on-singapore">U.S. Moves to Close Southeast Asian Detour for AI Chips</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U.S ... - CNBC</a></li>
<li><a href="https://www.nbcnews.com/tech/tech-news/nvidia-chips-loophole-export-ruleschinese-companies-access-megaspeed-rcna608601">How Chinese companies access Nvidia chips through a loophole ...</a></li>
<li><a href="https://asiatimes.com/2026/06/nvidia-gpu-crackdown-hits-china-linked-southeast-asia-data-centers/">Nvidia GPU crackdown hits China-linked Southeast Asia data ...</a></li>

</ul>
</details>

**Tags**: `#AI芯片出口管制`, `#美国商务部`, `#远程算力`, `#东南亚数据中心`, `#半导体政策`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China approves Eli Lilly’s oral GLP-1 weight-loss drug, a first](https://www.reuters.com/business/healthcare-pharmaceuticals/china-approves-eli-lillys-weight-loss-pill-orforglipron-2026-11-12/) ⭐️ 8.0/10

China’s National Medical Products Administration approved Eli Lilly’s once-daily oral GLP-1 weight-loss drug orforglipron on Nov. 12 as a Class 1 new drug—a Chinese regulatory category for innovative medicines—for adults with obesity or overweight plus at least one weight-related condition, making it the country’s first approved oral GLP-1 obesity treatment. The pill is taken without food or water restrictions; price and launch timing were not announced, and a type 2 diabetes indication is still under review.

telegram · zaihuapd · Nov 12, 10:09

**「Background」** Orforglipron is a non-peptide small-molecule GLP-1 drug taken as a pill rather than by injection, and Lilly had already filed for marketing authorization for it in China ahead of this approval.

**「Impact」** The approval adds an oral option for the approved patient group and puts Lilly in competition with Novo Nordisk, Pfizer and Innovent’s weekly injectable weight-loss treatments, the report said.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/jack-shuang-hou-75314a2b3_commits-china-scale-activity-7437517930319491072-GyIO?rcm=ACoAAEtOR68Bp30UtTNTOKmHTZ08WurIS789aGg">Eli Lilly Invests $3B in China for Obesity Drug Production | LinkedIn</a></li>
<li><a href="https://eureka.patsnap.com/blog/life-science/esc-2026-glp-1-receptor-agonists-competitive-landscape-analysis/">GLP - 1 Receptor Agonists Competitive Landscape Analysis 2026</a></li>

</ul>
</details>

**Tags**: `#GLP-1`, `#Eli Lilly`, `#China drug approval`, `#obesity treatment`, `#pharmaceutical competition`

---