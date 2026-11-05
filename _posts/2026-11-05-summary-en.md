---
layout: default
title: "Horizon Summary: 2026-11-05 (EN)"
date: 2026-11-05
lang: en
---

> From 43 items, 11 important content pieces were selected

---

**Technology News**
1. [Moonshot AI releases Kimi K3.1 Pro open weights](#item-tech-news-1) ⭐️ 8.0/10
2. [Tencent releases Hy4 with vision, computer use, and game-engine support](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic publishes FlashProve code for provable LLM inference](#item-tech-news-3) ⭐️ 8.0/10
4. [Go team introduces encoding/json/v2 JSON API](#item-tech-news-4) ⭐️ 8.0/10
5. [IEEE Spectrum: AI Is Exposing Decades of Software Security Debt](#item-tech-news-5) ⭐️ 7.0/10
6. [Looped transformers save weight storage, not necessarily HBM traffic on B200](#item-tech-news-6) ⭐️ 7.0/10
7. [Open-source NKI megakernels speed GLM-5.3-Flash decode on Trainium2](#item-tech-news-7) ⭐️ 7.0/10
8. [Study: Attention, Not Length, Drives Retrieval Loss](#item-tech-news-8) ⭐️ 7.0/10
9. [NIKKE PC launcher alleged to load remote-control trojan](#item-tech-news-9) ⭐️ 7.0/10
10. [Huawei tells Ascend 960DT customers to source Samsung, SK Hynix HBM themselves](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Oracle Reportedly Cancels ~$7 Billion AI Chip Lease With Tencent](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Moonshot AI releases Kimi K3.1 Pro open weights](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 8.0/10

Moonshot AI has published open weights for Kimi K3.1 Pro on Hugging Face, describing it as a native multimodal agent model with 2.8 trillion total parameters, 104 billion active parameters, and a context window of roughly 1 million tokens; it is the first model in the K3.1 series. The weights are released in MXFP4 quantization, and Moonshot is also serving the model through its API at platform.kimi.ai under the kimi-k3.1-pro identifier. That endpoint is compatible with OpenAI and Anthropic interfaces, so existing clients can use either interface style.

hackernews · abrarthought · Nov 4, 15:30 · [Discussion](https://news.ycombinator.com/item?id=50366999)

**「Background」** Kimi K3.1 Pro is the first model in Moonshot AI&\#x27;s K3.1 series, a mixture-of-experts model with 2.8 trillion total parameters, 104 billion active parameters per token, and a 1,048,576-token context window. Moonshot describes it as post-trained from Kimi K3 using large-scale joint reinforcement learning across hundreds of downstream domains.

**「Impact」** For teams, the practical split is between a lower-friction hosted endpoint that speaks OpenAI- and Anthropic-compatible APIs and self-hosting the 2.8-trillion-parameter MXFP4 weights, which commenters expect to require very large multi-GPU nodes.

**「Community discussion」** Commenters disagreed over benchmark quality: one called the model &quot;benchmaxxed,&quot; while another reported that their testing did not show this and described it as very strong but a bit off the frontier. Others focused on serving economics, noting that third-party providers including OpenRouter, Together, and Modal were hosting it, with one commenter reporting throughput differences at the same price.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3.1-Pro">moonshotai/Kimi-K3.1-Pro - Hugging Face</a></li>
<li><a href="https://aiweekly.co/alerts/moonshot-ships-kimi-k31-pro-28t-moe-with-1m-context">Moonshot ships Kimi K3.1 Pro: 2.8T MoE with 1M context</a></li>

</ul>
</details>

**Tags**: `#open-weight models`, `#Kimi K3.1 Pro`, `#LLM release`, `#inference infrastructure`, `#AI hardware`

---

<a id="item-tech-news-2"></a>
### [Tencent releases Hy4 with vision, computer use, and game-engine support](https://hy.tencent.ai/research/hy4) ⭐️ 8.0/10

Tencent released Hy4 on November 4 with its first vision capability and computer-use support, plus targeted training for Blender, CAD, and game development across Unreal Engine, Unity, and Godot. The model is available through Tencent Cloud and OpenRouter at an unchanged API price; Tencent says it plans to open-source the weights and launch a Hy4 Flash variant soon. In a 579-task public financial benchmark, Hy4 scored 3.04 and ranked first among open models, while its hallucination rate fell from 15.76% to 5.45%, according to the release. Tencent also open-sourced HyCell for single-cell representation and HyPDE for physical-field modeling, and acknowledged that Hy4 still trails top proprietary models on research-level math, long-horizon coding, self-improvement, and advanced visual question answering.

hackernews · Philpax · Nov 4, 14:11 · [Discussion](https://news.ycombinator.com/item?id=50365780)

**「Background」** Tencent&\#x27;s Hunyuan \(Hy\) line is the company&\#x27;s own model family, and the release describes Hy4 as the first Hunyuan model to add visual capability. It also follows an earlier Hy4 preview, so the relevant shift is from that preview to a version Tencent is pitching for computer operation and specialized software such as Blender and CAD.

**「Deployment path」** Developers can call Hy4 through Tencent Cloud and OpenRouter at the unchanged API price, but cannot yet self-host it: Tencent says model weights and system cards are planned for release &quot;in the coming days,&quot; so teams with data-residency or cost constraints should wait for the actual weights and license terms rather than assume open-weight availability at launch.

**「Community discussion」** Commenters welcomed Tencent&\#x27;s open-sourcing of HyCell and HyPDE as materially useful for scientific research and credited the release with candidly acknowledging Hy4&\#x27;s gap to leading proprietary models. A Plotly benchmark commenter reported that Hy4 landed between GPT-6.1 Sol and GPT-6.1 Terra on cost and accuracy in data-analytics tasks, but was very slow, running roughly 26 queries per question and sometimes 64.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/">Tencent Launches Hy4, Joining the Ranks of the World&#x27;s ...</a></li>

</ul>
</details>

**Tags**: `#open-weight models`, `#Tencent Hy4`, `#AI research`, `#game development AI`, `#foundation models`

---

<a id="item-tech-news-3"></a>
### [Anthropic publishes FlashProve code for provable LLM inference](https://www.anthropic.com/research/provable-inference) ⭐️ 8.0/10

Anthropic has published a technical specification and code for FlashProve, an open-source system that uses cryptographic proofs to check whether a given AI output came from a specified model. The approach relies on model providers publishing a fingerprint for each released model; the fingerprint does not reveal model weights, and verification can run locally. Anthropic says the work remains research with no deployment plans, and presents it as a way to detect model substitution or verify third-party claims about which model performed a task.

hackernews · ltononro · Nov 4, 17:17 · [Discussion](https://news.ycombinator.com/item?id=50368626)

**「Background」** Provable inference lets a model provider publish a commitment or fingerprint for its weights, then supply a cryptographic proof that a given output was produced by that model without disclosing the weights. Earlier work includes VerInf, a zero-knowledge proof system for LLM inference that has proved a 400B-parameter model; Anthropic&\#x27;s research page identifies Llama 4 Maverick as the same model FlashProve targets.

**「Impact」** The practical check depends on providers publishing a model fingerprint, so users cannot verify a model that does not cooperate. With no deployment plan announced, FlashProve is a research prototype rather than an available audit tool.

**「Community discussion」** One commenter who says FlashProve builds on his earlier VerInf work alleges that the design, including the choice of a 400B Maverick model, was reused with little attribution; this is an attribution claim, not a confirmed finding in the source. Another commenter welcomes the result as an improvement on prior zk work but cites a reported 90–100x compute overhead and argues that independent re-execution is cheaper for open-weight models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/JamesPetrie/VerInf">GitHub - JamesPetrie/VerInf</a></li>
<li><a href="https://www.anthropic.com/research/provable-inference">Progress on provable inference for large language models</a></li>

</ul>
</details>

**Tags**: `#provable inference`, `#LLM verification`, `#cryptographic proofs`, `#AI safety`, `#Anthropic research`

---

<a id="item-tech-news-4"></a>
### [Go team introduces encoding/json/v2 JSON API](https://go.dev/blog/jsonv2) ⭐️ 8.0/10

The Go team has published a blog post introducing \`encoding/json/v2\`, a redesigned API for JSON handling in the standard library, rather than another revision of the existing \`encoding/json\` package. The post is presented as an introduction to the new API; the supplied material does not establish a release date, whether v1 will be maintained alongside it, or what migration tooling exists. Developers should read the announcement as a design proposal from the Go team until availability and backward-compatibility details are confirmed.

hackernews · olexsmir · Nov 4, 17:52 · [Discussion](https://news.ycombinator.com/item?id=50369106)

**「From experiment to stable API」** Go 1.25 introduced encoding/json/v2 and encoding/json/jsontext as experimental packages, with a September 2025 blog post explaining why the standard library needed a new major JSON API. The current post is an updated version of that introduction: it says the packages are now stable and generally available in Go 1.27, moving the same design from experiment to supported standard library.

**「Migration cost」** Developers adopting encoding/json/v2 must audit code that depends on v1&\#x27;s exact output: some values encode differently by default, and preserving prior behavior requires v2 options or struct tags, with omitzero covering nil or zero-value omission. Teams that used the experimental github.com/go-json-experiment/json package also face an import-path migration to encoding/json/v2.

**「Community Discussion」** Commenter CamouflagedKiwi said they generally like \`encoding/json/v2\` but wished \`MarshalIndent\` had been retained, arguing the equivalent replacement code is complicated and non-obvious, which makes both migration and quick readable-JSON output harder. Separately, asim described delegating most Go writing to AI models while still wanting the output to be Go for its performance and safety characteristics, a workflow shift rather than an opinion on the API itself.

<details><summary>References</summary>
<ul>
<li><a href="https://go.dev/blog/jsonv2">A new Go API for JSON - The Go Programming Language</a></li>
<li><a href="https://go.dev/blog/jsonv2-exp">A new experimental Go API for JSON - The Go Programming Language</a></li>
<li><a href="https://importstatic.com/go/go-json-v2-migration">Go JSON v 2 Migration : What Breaks in Go 1.27 | ImportStatic</a></li>
<li><a href="https://gitmemories.com/aquasecurity/trivy/issues/9422">trivy refactor: migrate from go -json-experiment to encoding / json / v 2</a></li>
<li><a href="https://blog.stackademic.com/golangs-new-proposal-for-the-encoding-or-json-or-v2-package-code-thursday-6e1498684739">Go encoding / json / v 2 | Stackademic</a></li>

</ul>
</details>

**Tags**: `#Go`, `#JSON`, `#standard library`, `#API design`, `#parsing`

---

<a id="item-tech-news-5"></a>
### [IEEE Spectrum: AI Is Exposing Decades of Software Security Debt](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability) ⭐️ 7.0/10

An IEEE Spectrum analysis argues that AI-driven vulnerability discovery is exposing decades of accumulated software security debt in legacy software and forcing security teams and maintainers to begin cleaning it up. The piece is an argument about a broad remediation burden, not the announcement of a specific product, vulnerability, or research result. It presents the shift as a long-deferred security cleanup now being pushed forward by AI-assisted finding.

hackernews · pseudolus · Nov 4, 11:52 · [Discussion](https://news.ycombinator.com/item?id=50364336)

**「Background」** The IEEE Spectrum analysis is framed around “PHP 2 Shell,” a nickname researchers gave to two memory-safety flaws in PHP, according to a vulnerability write-up. IEEE Spectrum presents that episode as an example of how AI in cybersecurity is accelerating both attackers and defenders while exposing technical debt in fragile legacy systems.

**「Impact」** For organizations maintaining long-lived systems, the practical consequence is a larger remediation queue: previously hidden flaws must be triaged, patched, or accepted as risk, and some fixes will require restructuring rather than a narrow patch.

**「Community discussion」** Commenters disagree about whether this amounts to paying down debt or starting a compulsory treadmill of feature-neutral fix work; one argues many issues require restructuring, while another traces the root cause to default-permit operating-system design. A further comment invokes Gödel, Escher, Bach to argue that no perfectly secure system is possible.

<details><summary>References</summary>
<ul>
<li><a href="https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability">PHP 2 Shell Is a Wakeup Call for AI in Cybersecurity - IEEE Spectrum</a></li>
<li><a href="https://www.fdaytalk.com/php2shell-vulnerability/">PHP 2 Shell Vulnerability : Affected Versions and How to Fix</a></li>

</ul>
</details>

**Tags**: `#AI in cybersecurity`, `#technical debt`, `#vulnerability discovery`, `#legacy software`, `#security engineering`

---

<a id="item-tech-news-6"></a>
### [Looped transformers save weight storage, not necessarily HBM traffic on B200](https://www.reddit.com/r/MachineLearning/comments/1xnskvt/do_looped_transformers_save_hbm_traffic_profiling/) ⭐️ 7.0/10

An r/MachineLearning-linked blog post profiles Huginn-style looped transformers on an Nvidia B200 to test whether reusing one set of weights also reduces HBM traffic. In a chain of eight matmuls with a shared 72 MiB weight, the shared version ran 24% faster than eight identical copies and read almost nothing from HBM; at 288 MiB, larger than L2, the difference disappeared. In a full Huginn Core teaching implementation with random weights, eight iterations took about eight times as long as one and read roughly eight times as much data from HBM. The author concludes that weight sharing saves storage but does not by itself keep weights on chip, so they can still be reread from HBM at every iteration.

reddit · r/MachineLearning · /u/2dayyy6 · Nov 4, 16:26

**「Background」** Looped transformers reuse the same weights across multiple iterations instead of assigning separate parameters to every layer, which reduces parameter storage. Huginn is one such looped architecture; the profiling question is whether that storage saving also translates into fewer HBM reads when the shared weights are reused.

**「Impact」** For developers working on looped or recurrent transformers, the result means weight sharing should not be treated as an HBM-bandwidth optimization unless cache residency is verified; the Huginn measurement shows iteration time and HBM reads scaling with loop count when the weights do not stay cached.

**Tags**: `#looped transformers`, `#HBM bandwidth`, `#GPU profiling`, `#Huginn`, `#Nsight Compute`

---

<a id="item-tech-news-7"></a>
### [Open-source NKI megakernels speed GLM-5.3-Flash decode on Trainium2](https://www.reddit.com/r/MachineLearning/comments/1xo0yuq/p_nki_layer_megakernels_for_glm53flash_on_aws/) ⭐️ 7.0/10

RunAnywhere open-sourced trnrt, an inference engine that serves the 320B-parameter GLM-5.3-Flash mixture-of-experts model with a 1M-token context on one AWS trn2.48xlarge, and reports that NKI layer megakernels cut a batch-8 decode step from 32.2 ms in its 17 October build to 24.2 ms on 1 November. The author attributes two 3.2 ms savings—one from a fused sparse-attention layer and one from jointly shipped KDA and MoE kernels—and breaks the remaining 24.2 ms into a 6.1 ms memory floor, 10.0 ms of engines busy beyond it, 4.6 ms of in-kernel waits, 2.8 ms of exposed collectives, and 0.7 ms idle. There is no stock-AWS or GPU baseline: the latest vLLM Neuron plugin registers no GLM model, NxD Inference is described as in maintenance mode, and the self-run AgentX result \(up to 28.9 agent requests/min on one box; 35.9 tokens/s median at 16 agents\) is not official InferenceX. Accuracy checks are byte-for-byte where no bits should change and reference-based otherwise, but one sparse-attention prefill approximation remains—shifting next-token log-probabilities by 0.012–0.021 nats on average and changing the top token at 3 of 448 positions in an exact rerun—and no task-level eval has been run.

reddit · r/MachineLearning · /u/WildCard727 · Nov 4, 21:47

**「Why kernel boundaries matter on Trainium」** Decode in a large mixture-of-experts model is bandwidth-bound: every generated token requires streaming the model&\#x27;s weights, which is why the post treats 6.1 ms as the memory floor for a batch-8 step on one trn2.48xlarge. On AWS Trainium, models are normally compiled through XLA from framework-level operations, so each operation boundary writes back to HBM and each collective runs as its own kernel that the next one must wait on. NKI is the lower-level kernel interface for writing Trainium kernels by hand, which is what makes it possible to fuse a whole layer into a single kernel instead of relying on the compiler to overlap the seams.

**「Impact」** Developers can rerun the reported profiles using the commands in docs/RESULTS.md, but the 24.2 ms decode figure is an internal before/after comparison rather than a cross-stack benchmark; teams should validate the remaining sparse-attention approximation against their own tasks before treating the engine as production-ready.

**Tags**: `#AWS Trainium2`, `#inference optimization`, `#NKI kernels`, `#mixture-of-experts`, `#model serving`

---

<a id="item-tech-news-8"></a>
### [Study: Attention, Not Length, Drives Retrieval Loss](https://www.reddit.com/r/MachineLearning/comments/1xnzzgn/length_is_cheap_competition_is_not_attention/) ⭐️ 7.0/10

In a non-peer-reviewed Reddit author summary, an experiment reports that key-value retrieval loss is driven mainly by attention allocated to competing statements rather than by context length. Across 126,473 trials using 512–32K tokens and five open models from 0.5B to 3B parameters across four families, neutral filler was nearly free: Qwen2.5-1.5B reached 0.97–1.00 accuracy up to 32K with a median loss of 0.004 nats, while format-matched competing statements reduced accuracy to 0.11–0.21 with a median loss of 4.76 nats at 32K. The author reports that log\(1/a\*\), where a\* is attention mass on the evidence, explains 35–58% of loss variance, versus 2–8% for log length. The author also reports reproducing an MMLU loss of 11–18 points at 30K under a masked-filler protocol, but in retrieval masking cost 46 accuracy points at 32K while the same filler left visible cost none; the attention result is predictive rather than causal, and the work covers one synthetic task and models mostly up to 3B, plus a 7B MMLU replication.

reddit · r/MachineLearning · /u/neom\_gluon · Nov 4, 21:08

**「The prior length claim being tested」** The post takes aim at Du et al.&\#x27;s &quot;Context Length Alone Hurts LLM Performance Despite Perfect Retrieval&quot; \(Findings of EMNLP 2025\), which reported accuracy degrading as input grows even when all relevant information is present and correctly retrieved, attributing part of the loss to length itself. The author reports reproducing that masked-filler protocol on MMLU \(11 to 18 points lost at 30K tokens\) before rerunning the same setup with visible neutral filler as a control.

**「Impact」** For long-context retrieval evaluations, the reported gap means protocols that use masked filler may attribute degradation to length when visible neutral filler causes none; the author recommends including a visible neutral control in any length claim and measuring attention on competing evidence.

<details><summary>References</summary>
<ul>
<li><a href="https://aclanthology.org/2025.findings-emnlp.1264/">Context Length Alone Hurts LLM Performance... - ACL Anthology</a></li>
<li><a href="https://ardenus.com/articles/the-diminishing-returns-of-context">Ardenus | The Diminishing Returns of Context : Precision Over...</a></li>

</ul>
</details>

**Tags**: `#long-context`, `#retrieval`, `#attention`, `#LLM evaluation`, `#context rot`

---

<a id="item-tech-news-9"></a>
### [NIKKE PC launcher alleged to load remote-control trojan](https://github.com/WormW/nikke_malware_analysis) ⭐️ 7.0/10

An independent analysis alleges that tampered files on the official CDN loaded by the NIKKE PC launcher acted as a loader for a remote-control trojan. The reported trojan has 19 commands, including arbitrary command execution and screenshots, and is said to steal developer and AI-tool credentials plus data from 28 wallet extensions. On Nov. 3, Level Infinite reportedly replaced two modified files but has not publicly commented. Players can search debug.log for k2f\_chan to check, and the researchers advised against launching the PC version for now.

telegram · zaihuapd · Nov 4, 07:00

**「Why the CDN mattered」** The NIKKE PC launcher does not keep all of its startup logic inside the installed client: it fetches JavaScript files from Level Infinite&\#x27;s official CDN when it starts. That design means whoever can alter files on the CDN can run code inside every player&\#x27;s launcher without shipping a game update, which is what makes this a supply-chain incident rather than a normal client patch.

**「Impact」** Players who ran the PC client cannot treat the publisher&\#x27;s silent replacement of two files as confirmed cleanup; they should check the documented k2f\_chan indicator and assess any developer, AI-tool, or wallet credentials accessible from the affected machine as potentially exposed.

<details><summary>References</summary>
<ul>
<li><a href="https://gist.github.com/MotherSphere/d6c049a09ba8ac3085c51ee9df24a4e5">NIKKE PC launcher compromise (Nov 2026): Level Infinite CDN ...</a></li>
<li><a href="https://aviatrix.ai/threat-research-center/nikke-pc-game-launcher-hacked-to-spread-remote-access-data-stealing-malware/">NIKKE PC Launcher Supply-Chain Attack 2026: K2F RAT ...</a></li>

</ul>
</details>

**Tags**: `#supply chain attack`, `#malware`, `#credential theft`, `#game security`, `#PC launcher`

---

<a id="item-tech-news-10"></a>
### [Huawei tells Ascend 960DT customers to source Samsung, SK Hynix HBM themselves](https://thenextweb.com/news/huawei-hbm-smuggling-samsung-sk-hynix-ascend-960dt) ⭐️ 7.0/10

Huawei has told some customers that its next-generation flagship AI chip, the Ascend 960DT, will rely mainly on HBM from Samsung and SK Hynix, and that those customers must arrange their own memory supply because Chinese manufacturers lack sufficient HBM capacity, according to a report by The Information relayed by The Next Web. The report also describes HBM being soldered onto low-performance processors, declared under processor codes for shipment to Hong Kong, carried into the mainland by individuals and then heated off — an account of grey-market sourcing that has not been independently verified. A Shenzhen chip broker quoted in the report said a single HBM3E stack has risen from several hundred dollars a year ago to about $4,000. Huawei, Samsung and SK Hynix have not confirmed the arrangement in the supplied material.

telegram · zaihuapd · Nov 4, 14:52

**「Background」** High Bandwidth Memory \(HBM\) packages stacked DRAM dies to give AI accelerators much higher memory bandwidth than conventional DRAM; Samsung, Micron, and SK Hynix contributed to the JEDEC standard. Huawei&\#x27;s Ascend 960DT is the next flagship part in its Ascend AI-chip line, and the report says it relies on Samsung and SK Hynix HBM because Chinese suppliers&\#x27; HBM capacity is insufficient.

**「Impact」** Customers planning to deploy the Ascend 960DT would have to secure Samsung or SK Hynix HBM through their own procurement channels, shifting supply risk and cost onto buyers rather than the chip vendor. The reported roughly $4,000 price for a single HBM3E stack, if accurate, indicates that obtaining that memory is both expensive and dependent on informal import routes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Huawei Ascend`, `#HBM supply`, `#AI chips`, `#semiconductor supply chain`, `#China tech`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Oracle Reportedly Cancels ~$7 Billion AI Chip Lease With Tencent](https://www.tradingview.com/news/seekingalpha:e51e68f4d094b:0-oracle-cancels-7b-ai-chip-lease-with-tencent-amid-us-concerns-ft/) ⭐️ 7.0/10

Oracle reportedly canceled a five-year AI chip lease with Tencent valued at about $7 billion, after US officials raised concerns about the arrangement, according to a Financial Times report cited by Seeking Alpha. The agreement would have let Tencent rent roughly 100,000 advanced AI chips through Oracle data centers in Southeast Asia.

telegram · zaihuapd · Nov 4, 11:01

**「Background」** The reported five-year lease was a workaround for US export controls that keep advanced AI chips out of China, with Tencent planning to rent compute through Oracle data centers in Southeast Asia; the Financial Times reported that Trump administration officials raised concerns with Oracle before the deal was canceled.

**「Impact」** The cancellation closes a planned route for Tencent to obtain advanced AI chips it cannot access inside China, removing data-center capacity it had lined up for AI work.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/ai/oracle-kills-7bn-tencent-ai-chip-deal-under-trump-pressure">Oracle Kills $ 7 BN Tencent AI Chip Deal Under Trump... | ZeroHedge</a></li>
<li><a href="https://xenospectrum.com/en/tencent-oracle-ai-chip-lease-prepayments/">Tencent Reportedly Leases About 100,000 AI Chips From Oracle in...</a></li>

</ul>
</details>

**Tags**: `#Oracle`, `#Tencent`, `#AI chips`, `#US-China tech restrictions`, `#data centers`

---