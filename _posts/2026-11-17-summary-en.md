---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 49 items, 17 important content pieces were selected

---

**Technology News**
1. [vLLM v0.34.0 turns on extensible KV cache by default, removes Model Runner V1](#item-tech-news-1) ⭐️ 8.0/10
2. [US Extends AI Chip Export Controls to Remote Access](#item-tech-news-2) ⭐️ 8.0/10
3. [Carnegie Mellon&\#x27;s CS Learn posts full-semester CS lectures free on YouTube](#item-tech-news-3) ⭐️ 7.0/10
4. [Optimizely Reportedly Served Malware on Zoom and GitLab](#item-tech-news-4) ⭐️ 7.0/10
5. [Report: Windows 11 Telemetry Tracks Coding Agents and Developer Tools](#item-tech-news-5) ⭐️ 7.0/10
6. [Jiff 1.0 brings a new datetime library to Rust](#item-tech-news-6) ⭐️ 7.0/10
7. [Microsoft traces major email outage to defect from July fix](#item-tech-news-7) ⭐️ 7.0/10
8. [Linebender Explains Squircles and Smooth Curve Geometry](#item-tech-news-8) ⭐️ 7.0/10
9. [Marimba: frozen-encoder speech model for calibrated audio queries](#item-tech-news-9) ⭐️ 7.0/10
10. [Duetto steers a pretrained music transformer for live jazz](#item-tech-news-10) ⭐️ 7.0/10
11. [Tencent Hunyuan launches Hy4 flash with 1M context and lower API pricing](#item-tech-news-11) ⭐️ 7.0/10
12. [US and nine countries sign San Francisco Declaration on AI supply chains](#item-tech-news-12) ⭐️ 7.0/10
13. [Amazon says AI agents stole API keys to fund more LLM calls](#item-tech-news-13) ⭐️ 7.0/10
14. [Apple Intelligence goes live on China-region iPad and Mac betas](#item-tech-news-14) ⭐️ 7.0/10
15. [Alibaba, Tencent, Moonshot reportedly curb cyber capabilities; Qwen weights restricted](#item-tech-news-15) ⭐️ 7.0/10

**Financial News**
1. [CNBC: Lutnick Faces Questions Over Nvidia Ties as Sons&\#x27; Firm Cut Stake](#item-finance-news-1) ⭐️ 7.0/10
2. [Intel and CEO face shareholder class action over alleged concealed weak demand](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 turns on extensible KV cache by default, removes Model Runner V1](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0, a release of 1,061 commits from 412 contributors, makes the extensible KV cache the default on CUDA and ROCm: the cache is sized from memory actually free after CUDA graph capture and warmup rather than an estimate, and \`gpu\_memory\_utilization\` now defaults to 1.0. The release notes cite larger caches \(MiniMax-M3 on H200: 433k to 672k tokens\) but also warn that per-token decode latency can rise 6–18% on some H200 models at concurrency 128; \`--gpu-memory-utilization 0.9\` or \`--no-enable-extensible-kv-cache\` restores the old sizing. Model Runner V1 is removed, leaving Model Runner V2 as the only GPU runner, and the default \`--block-size\` moves from 16 to 64. Ten models are added, including Mistral Large 4 \(1T total / 52B active, FP8 and NVFP4 on Blackwell/Hopper and MI350\), MiniMax-M3.1-Flash, and Nemotron-3.5-Transcribe. The release reports vendor-measured speedups such as up to 1.95× decode for Step5 NVFP4 MoE on 4×GB200 and 1.6× output throughput for GLM-5.3-Flash.

github · khluu · Nov 16, 23:22

**「Background」** vLLM’s Model Runner is the GPU execution path for model forward passes, and earlier versions allowed selecting the older V1 runner with \`VLLM\_USE\_V2\_MODEL\_RUNNER=0\`. In v0.34.0, V1 is removed and V2 is the only GPU runner, so deployments that pinned V1 must drop that setting and port V1 logits processors to \`vllm.v1.worker.gpu.sample.logits\_processor\`.

**「Upgrade impact」** Existing deployments need flag and dependency changes before upgrading: any setup setting \`VLLM\_USE\_V2\_MODEL\_RUNNER=0\` now fails at startup, V1 logits processors must be ported to \`vllm.v1.worker.gpu.sample.logits\_processor\`, and \`huggingface\_hub &gt;= 2.0.0\`, \`tokenizers &gt;= 0.23.3\` and \`timm &gt;= 1.0.30\` are required. ROCm users must move to the ROCm 10.0 wheels and images because \`-rocm72\` artifacts are no longer published, and \`fp\_quant\` checkpoints no longer load after the QuTLASS removal. Because the new cache sizing trades higher throughput for potentially higher per-token latency, operators with tight TPOT targets should benchmark at their production concurrency before adopting the new defaults.

**Tags**: `#vLLM`, `#LLM inference`, `#open-source releases`, `#GPU performance`, `#KV cache`

---

<a id="item-tech-news-2"></a>
### [US Extends AI Chip Export Controls to Remote Access](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

The US Commerce Department issued an interim final rule on Nov. 16 extending export controls on advanced AI chips and servers to remote access, aiming to stop users from evading restrictions through third-country data centers. The rule requires licenses for reexports of AI chips to Indonesia, Malaysia, Singapore, Thailand and Brazil, according to The Verge. The source said the measure may further tighten China&\#x27;s access to advanced chips but did not specify an effective date or the full scope of covered hardware.

telegram · zaihuapd · Nov 16, 14:44

**「Why remote access became a loophole」** The Commerce Department’s Bureau of Industry and Security administers US export controls, and the new measure is an interim final rule aimed specifically at remote access to advanced AI chips and servers. The gap it targets is that controls tied to physical shipments and reexports did not clearly cover compute hosted in third-country data centers.

**「Impact」** Data-center operators and cloud providers offering remote access to advanced AI chips in third countries face new licensing exposure and should review whether their configurations or reexports to the five named countries require authorization. The rule specifically targets third-country data centers as a circumvention route.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/the-u-s-shuts-chinas-access-to-advanced-chips-via-singapore-brazil-indonesia-malaysia-and-thailand-as-scott-bessent-gives-nvidia-10-days-to-show-it-did-not-goose-its-revenues/">The U.S. Shuts China&#x27;s Access To Advanced Chips Via Singapore ...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#export controls`, `#US policy`, `#data centers`, `#semiconductors`

---

<a id="item-tech-news-3"></a>
### [Carnegie Mellon&\#x27;s CS Learn posts full-semester CS lectures free on YouTube](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

Carnegie Mellon&\#x27;s Griffin School of Computer Science launched CS Learn, which is publishing full semesters of lectures from current CMU computer science courses free on YouTube, releasing one course per day during launch week with more promised for January. Phillip Compeau, who teaches in the school and runs the program, said the distinguishing feature is the production process: a few CMU students built tools that automate much of it, and he acknowledged in comments that MIT&\#x27;s OpenCourseWare got there roughly 25 years earlier. Commenters identified Tianqi Chen&\#x27;s ML Systems among the offerings, and another said 15-259 Probability and Computing &quot;will be available soon.&quot; The release covers video lectures first; supplementary courseware is described as coming next, so exercises and feedback are not yet part of the free package.

hackernews · pcompeau · Nov 16, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50522980)

**「Background」** CS Learn is an open-courseware effort from Carnegie Mellon&\#x27;s Kenneth C. Griffin School of Computer Science, offering free access to selected courses from its top-ranked CS program. The YouTube channel packages each course as a full semester of lectures from a real CMU class, and the initiative is reported to span seven departments, including AI, robotics, and systems.

**「Impact」** Learners get free access to complete, current CMU course lectures rather than short previews, but the absence of projects and feedback mechanisms means self-study users cannot yet practice or be assessed on the material; those who need graded exercises must wait for the announced courseware.

**「Community Discussion」** Commenters welcomed specific courses — one CMU alum called 15-259 a favorite undergraduate class, and another planned to pair ML Systems with the mlc.ai GPU-programming book — while ecshafer cautioned that lectures without projects or a way to get feedback &quot;can fall flat.&quot; Another commenter argued that learning fundamentals properly makes AI a power tool, whereas skipping them means being replaced by it.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://www.pressreleasepoint.com/cmu-opens-access-top-computer-science-classes-through-free-cs-learn-platform">CMU Opens Access to Top Computer Science Classes Through Free ...</a></li>
<li><a href="https://zeli.app/story/50522980">Carnegie Mellon opens its CS classrooms · Hacker News | Zeli</a></li>

</ul>
</details>

**Tags**: `#open courseware`, `#computer science education`, `#YouTube`, `#Carnegie Mellon`, `#ML systems`

---

<a id="item-tech-news-4"></a>
### [Optimizely Reportedly Served Malware on Zoom and GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 7.0/10

Optimizely was reportedly compromised and used to deliver malware through customer-facing scripts on sites including Zoom and GitLab. The incident affected organizations that load Optimizely&\#x27;s third-party JavaScript, exposing a supply-chain risk in script delivery rather than a problem limited to the customers&\#x27; own code. The supplied material did not establish how attackers obtained the access needed to serve the malicious code.

hackernews · kristjansson · Nov 16, 23:00 · [Discussion](https://news.ycombinator.com/item?id=50524767)

**「Why a vendor snippet compromises every site that embeds it」** Optimizely is an experimentation and A/B testing vendor: customers embed a snippet that pulls JavaScript from Optimizely&\#x27;s CDN \(cdn.optimizely.com\) into their own pages to run tests and personalization. Because that code executes in the page&\#x27;s own security context alongside first-party content, anyone who controls what the vendor&\#x27;s CDN serves effectively controls every embedding site. Commenters also point to tag managers such as Google Tag Manager, which were designed to let marketing add such third-party tags without engineering involvement, as the reason pages now carry large amounts of externally supplied script.

**「Audit third-party snippets」** Any site still loading Optimizely&\#x27;s snippet from cdn.optimizely.com should treat that script as untrusted until Optimizely explains how the injected code reached customer projects — the report says the snippets for Optimizely&\#x27;s own domains carried the code too, so exposure is not limited to the named victims. Because Optimizely is embedded across tens of thousands of sites, per technology-usage trackers, the practical task is to inventory which pages load the tag and decide whether to remove or pin it. Blocking the CDN outright stops the reported vector, but it also disables the A/B testing and personalization those pages depend on, a trade-off some users describe making deliberately.

**「Community Discussion」** Commenters focused on third-party script and tag-manager risk: one argued that Google Tag Manager&\#x27;s premise—letting marketing add tags without engineering involvement—helped produce bloated JavaScript on news sites, while another said the incident was avoidable and called for stronger vendor release controls and accountability. Others reported blocking cdn.optimizely.com in a HOSTS file or using NoScript to reduce exposure.

<details><summary>References</summary>
<ul>
<li><a href="https://technologychecker.io/technology/optimizely">Companies Using Optimizely in 2026: Full Customer List ...</a></li>

</ul>
</details>

**Tags**: `#supply chain security`, `#third-party scripts`, `#web security`, `#malware`, `#Optimizely`

---

<a id="item-tech-news-5"></a>
### [Report: Windows 11 Telemetry Tracks Coding Agents and Developer Tools](https://xusheng.dev/posts/windows-coding-agent-telemetry/) ⭐️ 7.0/10

A report alleges that Windows 11 collects telemetry about which coding agents and developer tools users run. The item provides no primary technical documentation or independent measurement, so the exact data fields, scope, and default-on status are not established by the source. A commenter summarizing the post says the developer-tool data can be sent when diagnostic telemetry is enabled—described as the default—and points users to Settings → Privacy &amp; security → Diagnostics &amp; feedback to disable it.

hackernews · cwaffles · Nov 16, 22:58 · [Discussion](https://news.ycombinator.com/item?id=50524736)

**「Background」** Windows diagnostic telemetry is an optional data stream built on Event Tracing for Windows \(ETW\). A reverse-engineering report found that a Windows 11 component, MissionControlAggregator, adds per-tool usage bits for coding agents such as Codex, Claude, Copilot, and Cursor to that diagnostic stream, and that the tested builds did not capture prompts or source code.

**「Impact」** Developers who run coding agents or other developer tools on Windows 11 face a concrete privacy-review task: check the diagnostics setting before assuming local tool usage is not reported. Because the source does not establish whether tool names, paths, or invocation details are included, teams working with sensitive repositories should treat the scope as unverified rather than confirmed.

**「Community discussion」** Commenters split between normalizing the telemetry—one notes that GPU drivers and browsers already collect executable names, paths, or browsing data unless users opt out—and urging a move to Linux, with others saying the adjustment takes about a week and that single-player gaming is largely viable while multiplayer remains uneven. Another commenter argues that Windows needs non-invasive telemetry to prioritize AI-agent sandboxing, saying Microsoft launched MXC in October and that Claude Code does not yet support it.

<details><summary>References</summary>
<ul>
<li><a href="https://xusheng.dev/posts/windows-coding-agent-telemetry/">Windows 11 Is Collecting Data on Which Coding Agents and ...</a></li>
<li><a href="https://windowsforum.com/news/windows-11-optional-telemetry-can-report-coding-agent-usage-research-finds.452631/">Windows 11 Optional Telemetry Can Report Coding Agent Usage ...</a></li>
<li><a href="https://www.startuphub.ai/ai-news/technology/2026/windows-11-logs-which-coding-agent-you-ran">Windows 11 logs which coding agent you ran | StartupHub.ai</a></li>

</ul>
</details>

**Tags**: `#Windows 11 telemetry`, `#developer tools`, `#coding agents`, `#privacy`, `#operating systems`

---

<a id="item-tech-news-6"></a>
### [Jiff 1.0 brings a new datetime library to Rust](https://burntsushi.net/jiff/) ⭐️ 7.0/10

Jiff 1.0 has been released, giving Rust developers a new datetime library from Andrew Gallant, known online as burntsushi. Its documentation, as quoted in the discussion, explicitly addresses when Jiff is not the right choice, and the project targets date and time handling, including time zones. The supplied material does not include benchmarks, compatibility guarantees, or details of changes from pre-1.0 versions.

hackernews · burntsushi · Nov 16, 16:53 · [Discussion](https://news.ycombinator.com/item?id=50519744)

**「Background」** Jiff is a Rust datetime library by Andrew Gallant \(burntsushi\) whose repository describes its focus as providing high-level datetime primitives that are &quot;difficult to misuse&quot; with reasonable performance \(tool-2-1\). The project publishes a comparison document against other prominent open-source datetime libraries for Rust, framing Jiff&\#x27;s design choices relative to existing options \(tool-2-3\).

**「Impact」** For Rust developers, Jiff 1.0 adds a 1.0-version option to evaluate alongside chrono, which commenters describe as the established choice; the discussion offers no evidence that Jiff is a drop-in replacement or that major ecosystem crates have adopted it.

**「Community discussion」** The most substantive thread comes from chrono&\#x27;s former maintainer, who says attempts to improve chrono&\#x27;s API met resistance because users valued its stability, and welcomes Jiff as an alternative. Other commenters praise Jiff&\#x27;s explicit discussion of when not to use it and express hope for wider adoption, while one user asks whether it can handle specialized timescales such as TAI and UT1 for orbital simulations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BurntSushi/jiff">GitHub - BurntSushi/jiff: A datetime library for Rust that ...</a></li>
<li><a href="https://docs.rs/jiff/latest/jiff/_documentation/comparison/index.html">jiff::_documentation::comparison - Rust - Docs.rs</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#datetime`, `#libraries`, `#open-source`, `#time zones`

---

<a id="item-tech-news-7"></a>
### [Microsoft traces major email outage to defect from July fix](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

Microsoft attributed a large-scale outage of its hosted email service to a software defect that was introduced by a fix shipped in July, according to the company&\#x27;s postmortem account. The explanation describes a recovery that struggled to handle normal load, and it acknowledges that load testing had concentrated on weaker hardware with fewer cores even though the contention problem was worse on newer, higher-core machines. The details come from Microsoft&\#x27;s own incident writeup as reported, not from independent measurement, and the report does not quantify how many users or tenants were affected.

hackernews · Bender · Nov 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50517321)

**「Background」** The outage being explained struck on November 12, 2026, when Outlook and Teams went down for users worldwide. Microsoft said at the time that a software bug, rather than a cyberattack, was responsible.

**「Impact」** For administrators running Microsoft-hosted email, the report makes previously applied updates a candidate cause when similar failures recur, and it shows that the vendor&\#x27;s load testing did not cover the higher-core hardware where the contention was worst — so customers cannot assume vendor testing validates their own configuration. Recovery also depended on bringing capacity back gradually rather than accepting full demand at once, which is worth reflecting in internal incident runbooks.

**「Community Discussion」** Commenters compared the recovery to the power industry&\#x27;s &quot;black start&quot; problem, where load must be reconnected in blocks rather than all at once, and one asked why Microsoft could not simply shed load by admitting only a rotating subset of client IP ranges so that clients could still sync periodically. Another questioned the disclosed testing gap, noting that coverage usually favors weaker hardware and asking why contention worsened on better machines, while a third expressed surprise that Windows processes had any role in critical network infrastructure beyond the Exchange servers themselves.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnet.com/news-live/microsoft-outlook-outage-11-12-2026/">Microsoft Blames Outlook Outage on Software Bug in July ... - CNET</a></li>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6039343/outlook-down-widespread-outage-microsoft-email">A negative Outlook : Microsoft scrambles to fix email outage : NPR</a></li>
<li><a href="https://www.businessinsider.com/microsoft-365-outage-email-outlook-teams-memes-jokes-2026-11">What to Do When Microsoft Outlook Is Down? - Business Insider</a></li>

</ul>
</details>

**Tags**: `#incident postmortem`, `#cloud reliability`, `#Microsoft`, `#load testing`, `#outage`

---

<a id="item-tech-news-8"></a>
### [Linebender Explains Squircles and Smooth Curve Geometry](https://linebender.org/wiki/curves/squircle/) ⭐️ 7.0/10

Linebender&\#x27;s wiki has published a technical article on squircles—rounded-square shapes—and the smooth curve geometry used to construct them, aimed at graphics and interface-design readers. The piece is an explainer rather than a product announcement or a report of measured performance. In the Hacker News discussion, practitioners focused on splines, superellipses, and the practical value of curvature-continuous curves.

hackernews · raphlinus · Nov 16, 07:55 · [Discussion](https://news.ycombinator.com/item?id=50515151)

**「Background」** A squircle is a shape intermediate between a square and a circle; there is no single mathematical definition, and at least two definitions are in use, one based on the superellipse and another arising from optics. The Linebender article treats squircles as a parametrized family of curves that can vary between a circle and a square, providing the geometric context for the curvature-continuous shapes discussed in the source.

**「Community Discussion」** Commenters traded practical examples and references: one praised the Zune&\#x27;s second-generation squircle d-pad for its smooth feel, another linked a work-in-progress spline-authoring demo built around superellipses and clothoids, and another pointed to the “sphube” as a three-dimensional relative. A separate argument held that curves avoiding derivative discontinuities become especially important when a design has to interact with physical reality.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Squircle">Squircle - Wikipedia</a></li>
<li><a href="https://linebender.org/wiki/curves/squircle/">Squircles - Linebender</a></li>

</ul>
</details>

**Tags**: `#squircles`, `#computer graphics`, `#UI design`, `#curves and splines`, `#geometry`

---

<a id="item-tech-news-9"></a>
### [Marimba: frozen-encoder speech model for calibrated audio queries](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

A Reddit research post accompanying an arXiv paper introduces Marimba, a speech model that answers typed yes/no, multiple-choice, or scoring queries about an 8-second audio window with a calibrated probability, using one pass through a frozen Qwen3-ASR-0.6B encoder per window. The authors report matching or beating Qwen3-Omni \(30B-A3B\) on 6 of 9 tests on 1,000 public questions, plus 100% language ID on 300 FLEURS clips and speaker-change AUROC of 0.966–0.980 on AMI and VoxConverse; these are self-reported results, not independent verification. They acknowledge that the turn-end readout was trained on Smart Turn data, that it trails Smart Turn v3.2 on Smart Turn&\#x27;s own test set \(AUROC 0.930 vs 0.982\) while tying on ICSI \(0.716 vs 0.712\), and that it is at chance on CochlScene scene classification. Code, Apache-2.0 weights, a demo, and a \`pip install marimba-audio\` package are linked.

reddit · r/MachineLearning · /u/solanotodesch · Nov 16, 15:47

**「Why a frozen-encoder probe model」** Marimba follows the &quot;System One&quot; framing: fast, low-latency perceptual judgments rather than multi-step reasoning, implemented by probing a frozen speech encoder instead of fine-tuning one model per task. Small readouts trained on intermediate layers \(12 and 18\) of Qwen3-ASR-0.6B supply speaker-change, speaker-count, and turn-end answers, while term spotting reuses the ASR decoder&\#x27;s own hypotheses. The baselines it measures against are established tools in each area — Smart Turn v3.2 for turn-end detection, pyannote 3.1 and ECAPA for speaker tasks, and the much larger Qwen3-Omni \(30B-A3B\) omni model. The author notes this post is a follow-up to an earlier Reddit thread, now accompanied by an arXiv paper, Apache-2.0 weights, and a pip-installable package.

**「What developers should check」** Teams evaluating Marimba for meeting or conversational audio should validate turn-end detection on their own data: the authors report AUROC 0.930 versus Smart Turn v3.2&\#x27;s 0.982 on Smart Turn&\#x27;s test set and only a tie on ICSI, despite the Apache-2.0 weights and pip-installable code making the model easy to try.

**Tags**: `#speech recognition`, `#audio foundation models`, `#model calibration`, `#efficient inference`, `#Qwen3-ASR`

---

<a id="item-tech-news-10"></a>
### [Duetto steers a pretrained music transformer for live jazz](https://www.reddit.com/r/MachineLearning/comments/1xxkyh3/steering_a_pretrained_music_transformer_at/) ⭐️ 7.0/10

A developer has published duetto, a real-time MIDI-keyboard jazz partner that plays solo, comping, and walking-bass parts and takes a solo when the player stops; the code is free for noncommercial use. Rather than fine-tuning, it runs the pretrained Anticipatory Music Transformer \(Thickstun et al., 2023\) as-is and controls it at sampling time: a rule layer masks disallowed notes and biases allowed ones, including chord tones, downbeat guide tones, and quoted phrases drawn from the Weimar Jazz Database. The server samples about one second of music ahead and resamples unplayed notes after each player input; the author reports ~12 ms/note for the medium model and 18 ms/note for the large model on a 3080 Ti, and ~90 ms/note for the large model on a Jetson Orin Nano. The author says the system still drifts from the player, responds unpredictably, and is fragile to tune, and reports that about 61% of solo notes in an Autumn Leaves demo come from quoted phrases or the theme; no independent evaluation is provided.

reddit · r/MachineLearning · /u/GGAllin43 · Nov 16, 09:19

**「Background」** The Anticipatory Music Transformer is a 2023 autoregressive model by Thickstun et al. that generates music as interleaved event and control sequences, a design intended for music-control tasks \(tool-1-1, tool-1-2\). Duetto keeps that pretrained model unchanged and instead alters its sampling distribution through logit masking and biasing, making the project an example of steering a fixed generative model rather than adapting it with new training.

**「Limited real-time headroom, licensing caveat」** For developers building interactive symbolic-music systems, duetto is a concrete data point that a pretrained Anticipatory Music Transformer can be driven in real time without fine-tuning: the author reports roughly 12 ms per note for the medium model and 18 ms per note for the large model on a 3080 Ti, with the large model at about 90 ms per note on a Jetson Orin Nano, which he says is still fast enough for live playing. The tradeoff is behavioral rather than computational — the author reports the model can drift from the player, that its responses are hard to predict, and that the logit bias level is fragile, sounding like a phrase book when too strong. Anyone reusing the code should note it is released free for noncommercial use only.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.08620">[2306.08620] Anticipatory Music Transformer</a></li>
<li><a href="https://paperswithcode.co/paper/2306.08620">Anticipatory Music Transformer (arXiv...) | Papers with Code</a></li>

</ul>
</details>

**Tags**: `#music generation`, `#transformer models`, `#sampling-time control`, `#real-time interaction`, `#MIDI`

---

<a id="item-tech-news-11"></a>
### [Tencent Hunyuan launches Hy4 flash with 1M context and lower API pricing](https://mp.weixin.qq.com/s/5yBbf-ctYziM5r0i6Y17lA) ⭐️ 7.0/10

Tencent Hunyuan announced Hy4 flash, a multimodal model with 224B total and 12B active parameters and a 1M-token context window. The API is priced at ¥0.5 per million input tokens and ¥2 per million output tokens, or ¥0.02 per million tokens on cache hits, and Tencent says its WorkIndex cost per task is 1/13 that of Hy4 preview and 1/20 that of Hy4. It is available on Tencent Cloud TokenHub, WorkBuddy, and Yuanbao, with open sourcing planned; WorkBuddy is free for a limited time and API usage is 50% off through Nov. 30. Tencent claims Hy4 flash is slightly better overall than Hy4 preview, but those performance and cost comparisons are vendor-provided.

telegram · zaihuapd · Nov 16, 07:17

**「背景」** 腾讯混元此前的 Hy4 系列已包含 Hy4 preview 和 Hy4 两个版本，新发布的 Hy4 flash 定位为其中成本最低的一档。其 224B 总参数与 12B 激活参数的差距反映的是混合专家（MoE）结构：每个 token 只调用一小部分参数，从而在保留大模型容量的同时压缩推理开销。1M 上下文与多模态支持此前多见于更高价位的型号，这次被下放到低价档位。

**「Impact」** Developers can access the model through Tencent Cloud TokenHub and test long-context multimodal workloads at the promotional API rates through Nov. 30, but should validate the claimed quality and cost advantages on their own tasks before moving production traffic.

**Tags**: `#Tencent Hunyuan`, `#LLM release`, `#multimodal`, `#long context`, `#API pricing`

---

<a id="item-tech-news-12"></a>
### [US and nine countries sign San Francisco Declaration on AI supply chains](https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/) ⭐️ 7.0/10

On Nov. 15, the United States and nine other countries—Australia, India, Israel, Japan, Qatar, South Korea, Singapore, the UAE, and the UK—signed the San Francisco Declaration, which treats economic security as the foundation of national security and pledges cooperation to protect sensitive technologies and critical infrastructure in supply chains supporting superintelligence \(SI\). The declaration lays out five working groups covering an innovation-policy framework, SI applications in critical sectors, full-stack SI supply-chain collaboration, safe harbors and supply-chain security hubs, and SI safety and resilience. The relayed announcement provides no binding commitments, funding, timelines, or technical specifications.

telegram · zaihuapd · Nov 16, 10:40

**「Where the declaration came from」** The declaration was signed in San Francisco on 15 November 2026 at the Pax Silica Summit — also referred to as the Pax Silica Founders Retreat — a gathering convened by US Under Secretary of State for Economic Affairs Jacob Helberg, with Australia, India, Israel, Japan, Korea, Qatar, Singapore, the UAE and the UK joining the United States. It serves as the vehicle through which the ten governments convert shared principles on protecting sensitive technologies and critical infrastructure into a working partnership, with the stated goal of reducing reliance on US adversaries for critical minerals, AI models and semiconductor chips.

**「Impact」** The declaration does not itself create new binding obligations, funding, or technical rules for AI and semiconductor companies, so near-term compliance requirements are unchanged; the five working groups are the mechanism to watch for later specifics on full-stack supply-chain collaboration and safe harbors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/San_Francisco_Declaration_on_the_Secure_Foundations_of_Enduring_Prosperity">San Francisco Declaration on the Secure Foundations of Enduring Prosperity</a></li>
<li><a href="https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/">The San Francisco Declaration on the Secure Foundations of ...</a></li>
<li><a href="https://www.industry.gov.au/publications/san-francisco-declaration-secure-foundations-enduring-prosperity-signed-countries-attending-pax-silica-summit-15-november-2026">The San Francisco Declaration on the Secure Foundations of ...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#AI supply chain`, `#international cooperation`, `#AI governance`, `#semiconductors`

---

<a id="item-tech-news-13"></a>
### [Amazon says AI agents stole API keys to fund more LLM calls](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

Amazon reported that an AI-agent campaign, driven by the open-source Artex penetration-testing framework, stole API keys from internet-exposed AI applications including LiteLLM and Dify, validated them, and pooled them to pay for additional large-model calls. The activity began on October 3 and was blocked on November 5 by Amazon&\#x27;s MadPot decoy network, according to the report. Amazon attributed the operation to a China-linked threat group with medium confidence, said not all listed targets were compromised, and said it had notified potentially affected AWS customers.

telegram · zaihuapd · Nov 16, 13:00

**「Background」** Artex is an open-source agentic AI penetration-testing framework, so an AI agent can execute multi-step offensive tasks instead of merely generating text. Amazon’s MadPot is a globally distributed network of decoy sensors that impersonate exposed services to capture attacker requests and operating memory. LiteLLM and Dify are AI application tools that, when reachable from the public internet, can store upstream model-provider API keys.

**「Impact」** For operators of public-facing LiteLLM and Dify deployments, a leaked API key can be repurposed to fund further model calls, turning key exposure into direct usage cost; Amazon said it notified potentially affected AWS customers.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/">Amazon Threat Intelligence observes threat actors running ...</a></li>
<li><a href="https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html">Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify ...</a></li>

</ul>
</details>

**Tags**: `#AI 安全`, `#自主代理`, `#API 密钥`, `#网络犯罪`, `#云安全`

---

<a id="item-tech-news-14"></a>
### [Apple Intelligence goes live on China-region iPad and Mac betas](https://www.theverge.com/tech/1034581/apple-intelligence-siri-ai-daily-usage-limits-icloud-subscription) ⭐️ 7.0/10

Apple Intelligence is reported to be available to China-region beta testers on iPad and Mac after updating to iPadOS 27.3 beta 2 or macOS 27.3 beta 2. In the same beta round, Apple is testing daily per-device usage caps on some Siri AI and Apple Intelligence features across iOS 27.3, iPadOS 27.3 and macOS 27.3 beta 2, according to the report. Basic Siri commands remain free and unlimited, while cloud-based advanced functions — including multi-step personal-context requests and image generation and editing — are subject to the limits. The report also says a file-sandbox escape vulnerability affecting Apple OS betas has been fixed.

telegram · zaihuapd · Nov 16, 20:12

**「Why China availability is notable」** Apple Intelligence&\#x27;s China rollout has trailed other markets: during this beta cycle, MacRumors reported Apple&\#x27;s statement that Siri AI and other Apple Intelligence features announced at WWDC 2026 would not be available in China on iOS 27.3. The source says the features are now live for China-region iPad and Mac betas specifically, and does not mention iPhone, so the status of the iPhone rollout in China remains unconfirmed here.

**「Impact」** China-region beta users must be on the specified iPadOS or macOS 27.3 beta 2 builds to try Apple Intelligence, and those relying on cloud-backed Siri requests, image generation or editing should expect a per-device daily ceiling that does not apply to basic commands. The sandbox-escape fix gives beta testers on affected builds a concrete reason to update.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2/">MacRumors: Apple News and Rumors - Page 2</a></li>

</ul>
</details>

**Tags**: `#Apple Intelligence`, `#China`, `#Siri`, `#security vulnerability`, `#usage limits`

---

<a id="item-tech-news-15"></a>
### [Alibaba, Tencent, Moonshot reportedly curb cyber capabilities; Qwen weights restricted](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 7.0/10

Bloomberg reported that Alibaba, Tencent and Moonshot weakened offensive cyber capabilities in their newest models while improving defensive performance, affecting developers and organizations that use Chinese AI models. Alibaba’s latest flagship Qwen is not being released with open weights, so users cannot download or customize the full version. The changes are tied to a draft export-control rule published by China’s Ministry of Commerce last month that would ban exports of AI tools capable of attacking critical infrastructure or government networks; Tencent cut cyber functions before releasing Hy4 this month.

telegram · zaihuapd · Nov 17, 02:20

**「Export-control backdrop」** China’s Ministry of Commerce proposed the export restrictions in October 2026, covering 40 technologies including AI and chips; reporting on the package said it would, for the first time, place controls on AI model weights. The current report links Alibaba’s decision not to release full Qwen weights, and the companies’ reduced offensive-cyber capabilities, to that draft.

**「Impact」** Developers cannot download or locally fine-tune the full Qwen flagship model, removing self-hosting and customization options for that release. Security teams should also verify whether the reduced offensive-cyber capabilities still meet their testing requirements before adopting the new models.

<details><summary>References</summary>
<ul>
<li><a href="https://apnews.com/article/china-export-restrictions-ai-chips-solar-us-5ac381c0c6d6628bbea2e0da7d855a5b">China moves to curb tech exports including for AI and solar ...</a></li>
<li><a href="https://www.reuters.com/business/retail-consumer/chinas-new-export-curbs-draw-line-around-its-ai-crown-jewels-2026-10-28/">China&#x27;s new export curbs draw a line around its AI crown ...</a></li>
<li><a href="https://www.techtimes.com/articles/329196/20261019/chinas-new-ai-export-controls-apply-now-if-you-licensed-deployed-covered-chinese-models.htm">China&#x27;s New AI Export Controls Apply Now if You Licensed or ...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#export controls`, `#AI safety`, `#open-weight models`, `#China AI industry`

---

## Financial News

<a id="item-finance-news-1"></a>
### [CNBC: Lutnick Faces Questions Over Nvidia Ties as Sons&\#x27; Firm Cut Stake](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 7.0/10

CNBC reported that Cantor Fitzgerald, the Wall Street firm formerly led by Commerce Secretary Howard Lutnick and now run by his sons Brandon and Kyle, cut its reported Nvidia share count by 49%, from about 3.5 million shares in September 2025 to 1.78 million by the end of March 2026, a period when, per Axios, Lutnick was resisting pressure to crack down on suspected Nvidia chip smuggling to China. CNBC said there is no evidence of wrongdoing, that the filings do not explain the decline, and that Cantor attributed most of the shares to a brokerage subsidiary hedging client transactions.

rss · CNBC Finance · Nov 16, 12:14

**「Background」** Lutnick’s Commerce Department oversees U.S. export controls, and he had been pressed to add Singapore-based Megaspeed — suspected of diverting Nvidia chips to China — to the entity list, which restricts exports to named companies; Axios reported that he resisted.

**「Impact」** The Commerce Department&\#x27;s move to close an export-control loophole for China data-center use, described as the first U.S. policy response to the Nvidia scandal, directly affects AI-chip makers and their customers in that market.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c67429m3vem3o">How a sex scandal at Nvidia is putting pressure on the White House</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/nvidia-commerce-china-lutnick.html">Nvidia fallout: Commerce targets loophole for China &#x27;s data center use</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/nvidia-commerce-china-lutnick.html">Nvidia fallout: Commerce targets loophole for China &#x27;s data center use</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#U.S. export controls`, `#conflict of interest`, `#Commerce Department`, `#semiconductor industry`

---

<a id="item-finance-news-2"></a>
### [Intel and CEO face shareholder class action over alleged concealed weak demand](https://www.investing.com/news/stock-market-news/intel-sued-by-shareholders-following-29-stock-plunge-5028171) ⭐️ 7.0/10

Intel, CEO Lip-Bu Tan and CFO David Zinsner were sued in a shareholder class action alleging they concealed weak PC demand and inventory problems before Intel&\#x27;s October 29, 2026 fourth-quarter revenue and profit forecast disappointed investors; shares fell 28.6% the next day, erasing about $140 billion in market value. A Michigan pension fund is leading the suit, filed in federal court in San Jose, on behalf of investors who bought Intel shares from July 23 to October 29, 2026.

telegram · zaihuapd · Nov 16, 11:10

**「Background」** The suit is a securities class action—a case brought by one group of investors on behalf of a wider class alleging misleading disclosures—and it names CEO Lip-Bu Tan, who has led Intel since 2025.

**「Who is affected」** Investors who bought Intel shares between July 23 and October 29, 2026 fall within the proposed class, and the 28.6% drop also cut more than $10 billion from the value of the US government&\#x27;s 9.9% stake, according to Yahoo Finance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lip-Bu_Tan">Lip - Bu Tan - Wikipedia</a></li>
<li><a href="https://finance.yahoo.com/markets/article/intel-stock-plunges-nearly-29-its-worst-day-since-1974-205955309.html">Intel stock plunges nearly 29%, its worst day since 1974</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#shareholder class action`, `#stock plunge`, `#earnings guidance`, `#semiconductors`

---