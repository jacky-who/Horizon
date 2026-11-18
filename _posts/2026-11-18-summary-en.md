---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 42 items, 13 important content pieces were selected

---

**Technology News**
1. [OpenAI releases GPT-6.2 Astra and Sol with cheaper Astra pricing](#item-tech-news-1) ⭐️ 9.0/10
2. [Reported Java4Shell RCE affects OpenJDK Base64 processing](#item-tech-news-2) ⭐️ 8.0/10
3. [SolidJS 2.0 adds server RPC, live/broadcast, diagnostics](#item-tech-news-3) ⭐️ 8.0/10
4. [Cloudflare flags DNS regulation risk after Quad9&\#x27;s France exit](#item-tech-news-4) ⭐️ 7.0/10
5. [Microsoft&\#x27;s ONNX Runtime GitHub Repository Vanishes Without Notice](#item-tech-news-5) ⭐️ 7.0/10
6. [Microsoft announces MAI Code 2 and Code 2 Flash coding models](#item-tech-news-6) ⭐️ 7.0/10
7. [Phrack Issue 73 Released](#item-tech-news-7) ⭐️ 7.0/10
8. [Prime Radiant releases external sandbox servers for coding agents](#item-tech-news-8) ⭐️ 7.0/10
9. [Datasette Lite rewritten with service workers and Pyodide](#item-tech-news-9) ⭐️ 7.0/10
10. [China demonstrates 27 Gbps bidirectional Q/V-band wireless link](#item-tech-news-10) ⭐️ 7.0/10
11. [Telegram Reportedly Limits Bot and Mini-App Payments to Stars](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [UK tribunal rejects £2bn Sony PlayStation Store class action](#item-finance-news-1) ⭐️ 7.0/10
2. [China Auto Association Reviews 17 Automakers&\#x27; 60-Day Supplier Payment Terms](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI releases GPT-6.2 Astra and Sol with cheaper Astra pricing](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 9.0/10

OpenAI introduced GPT-6.2 Astra, its new frontier model, and GPT-6.2 Sol, an efficient model for everyday work; both are available in the API as gpt-6.2-astra and gpt-6.2-sol, and Simon Willison shipped LLM 0.38 with support. Astra costs $8 per million input tokens and $40 per million output tokens, 80% of GPT-6 Astra&\#x27;s $10/$50, with cached input at $0.40 per million versus $1 for the older model. Sol remains at $2/$10, the same price as GPT-6.1 Sol and GPT-6 Sol.

hackernews · jasondavies · Nov 17, 17:46 · [Discussion](https://news.ycombinator.com/item?id=50535230)

**「Pricing context」** OpenAI&\#x27;s prior frontier model, GPT-6 Astra, was priced at $10 per million input tokens and $50 per million output tokens, and the Sol line had held at $2/$10 through GPT-6.1 Sol and GPT-6 Sol after GPT-5.6 Sol&\#x27;s $4/$20. GPT-6 Astra shared that $10/$50 tier with Claude Fable 5, while the Sol models were half the price of GPT-5.6 Sol.

**「Impact」** Developers using Astra in long-running agentic sessions pay $0.40 per million cached input tokens instead of $1, a 60% reduction that directly lowers the cost of repeatedly passing context.

**「Community Discussion」** One commenter reported that a data-analytics exam fell from about $20 to $4 with Astra and from $2.60 to $1.20 with Sol at similar accuracy, though the models sometimes finished early without finding the expected answer. Another commenter criticized the release&\#x27;s slideshow, workbook, and memo examples as poor compared with earlier models, while others cited PacBench scores and system-card notes that Astra showed more evaluation awareness and better chain-of-thought evasion than GPT-6 Astra.

**Tags**: `#OpenAI`, `#LLM release`, `#model benchmarks`, `#cost efficiency`, `#AI industry`

---

<a id="item-tech-news-2"></a>
### [Reported Java4Shell RCE affects OpenJDK Base64 processing](https://calif.io/java4shell/) ⭐️ 8.0/10

A reported remote-code-execution vulnerability nicknamed Java4Shell affects OpenJDK when it processes Base64 data, according to a Calif writeup discussed on Hacker News. The reported attack path is described as requiring specific heap-grooming and network conditions, so it is not presented as a universal one-request exploit against every Java service. A fixed version and confirmed in-the-wild exploitation are not established in the supplied material.

hackernews · werrett · Nov 17, 21:11 · [Discussion](https://news.ycombinator.com/item?id=50538240)

**「Background」** Base64 is a text encoding used to carry binary data, and OpenJDK’s HotSpot VM can replace its Base64 encoder and decoder with hardware-accelerated “intrinsics”; the reported flaw is tied to that optimized decoding path. Detection guidance circulated after disclosure scopes affected systems to HotSpot-based JDKs—OpenJDK, Oracle JDK, and GraalVM—and cites starting Java with \`-XX:-UseBASE64Intrinsics\` to disable the accelerated codec as a mitigation. A separate report labels the issue CVE-2026-114938, but the supplied item gives no advisory text or confirmation.

**「Who needs to act」** Because the flaw is reported to affect every OpenJDK-based distribution built from 17.0.6 or later, remediation has to start with an inventory of JDK builds in use, not just application code — Oracle JDK, GraalVM, and other HotSpot-based runtimes are in scope, while OpenJ9, GCJ, and Azul Prime \(Zing\) fall outside the described attack path. Hosts running the vulnerable decoder on AVX-512 hardware are the exposed population, where a 65-character Base64 string is reported to corrupt the Java heap. Teams running Java services such as Jira, Jenkins, or Keycloak should treat pre-auth RCE as a live patching priority and check whether they meet all of the exploit&\#x27;s preconditions before deprioritizing.

**「Community discussion」** Commenters highlighted that exploitation depends on remote heap grooming and low, stable round-trip times and jitter, while ievans of Semgrep linked free detection scripts aimed at five conditions, including HotSpot-based JDKs. AgentME noted an unconfirmed suggestion that the flaw involves AVX-512 Base64 decoding and could be worked around with the -XX:UseAVX=2 flag.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50538240">Java 4 Shell : RCE in OpenJDK when processing Base 64 | Hacker News</a></li>
<li><a href="https://dzen.ru/b/avzWWOwLzhLQmwdZ">Ошибка Base 64 в OpenJDK открыла путь к удалённому... | Дзен</a></li>
<li><a href="https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/">Java4Shell CVE -2026-114938: Affected Versions &amp; Mitigation</a></li>
<li><a href="https://calif.io/java4shell/">Java4Shell: Write once, RCE everywhere</a></li>
<li><a href="https://www.cyberkendra.com/2026/11/cve-2026-114938-pre-auth-rce-flaw-in-java-17-puts-servers-at-risk.html">Java4Shell ( CVE -2026-114938): Java Base 64 Flaw... - Cyber Kendra</a></li>

</ul>
</details>

**Tags**: `#OpenJDK`, `#remote code execution`, `#Java security`, `#Base64`, `#vulnerability detection`

---

<a id="item-tech-news-3"></a>
### [SolidJS 2.0 adds server RPC, live/broadcast, diagnostics](https://www.solidjs.com/blog/solid-2-0-the-long-hold/) ⭐️ 8.0/10

SolidJS 2.0 is a major release for developers using the JavaScript framework, adding server-integration features and new diagnostic capabilities. Commenters point to server RPC plus “live” and “broadcast” capabilities, and one commenter says the “Built to Be Written by Agents” section is really about better debugging diagnostics rather than agent-specific tooling. The supplied material does not include the release notes, so exact version numbers, compatibility requirements, and migration details are not available here.

hackernews · pier25 · Nov 17, 18:56 · [Discussion](https://news.ycombinator.com/item?id=50536387)

**「Prior development」** Solid 2.0 follows a long 1.x line, and an August 2026 release candidate previewed how the 2.0 cycle would reorganize the stack: server functions moving into core, the serving layer folded into a &quot;start mode,&quot; and file-system routing split out into a router-neutral package, with the framework&\#x27;s reactive graph made async-aware. The stable release now ships that restructuring rather than introducing it at launch.

**「Impact」** Teams building full-stack apps can use Solid 2.0&\#x27;s server RPC and live/broadcast primitives instead of assembling a separate real-time data layer, which is the main practical change for early adopters. Newcomers still face Solid&\#x27;s accessor-versus-function API; a GitHub discussion on the 2.0 roadmap flags that distinction as a learning-curve hurdle.

**「Community discussion」** pwmglenn praised Solid’s server RPC and “live”/“broadcast” integration as seamless and more natural than LiveView or htmx/datastar, saying it fills the frontend-backend gap that Remix did not. wk\_end suggested the “Built to Be Written by Agents” framing may be marketing, since the improvements are better debug diagnostics that also help hand-written code.

<details><summary>References</summary>
<ul>
<li><a href="https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal">Solid 2.0 RC: The Big | SolidJS</a></li>
<li><a href="https://github.com/solidjs/solid/discussions/2425">The Road to 2 . 0 · solidjs solid · Discussion #2425 · GitHub</a></li>

</ul>
</details>

**Tags**: `#SolidJS`, `#JavaScript frameworks`, `#web development`, `#RPC`, `#major release`

---

<a id="item-tech-news-4"></a>
### [Cloudflare flags DNS regulation risk after Quad9&\#x27;s France exit](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 7.0/10

Quad9 has withdrawn its public DNS resolution service from France under legal pressure, and Cloudflare&\#x27;s blog post treats the departure as a warning about how DNS resolvers are being drawn into internet regulation. The post is analysis and advocacy rather than a new Cloudflare product or policy change; it does not announce a Cloudflare withdrawal or a new commitment to leave any jurisdiction. The immediate effect falls on Quad9 users in France, who lose that resolver option, while the broader dispute concerns intermediary liability and privacy rules for DNS providers.

hackernews · subset · Nov 17, 22:13 · [Discussion](https://news.ycombinator.com/item?id=50538994)

**「Background」** Public recursive DNS resolvers such as Quad9 answer domain-name queries for users across many networks, so blocking orders aimed at them can affect access well beyond a single ISP. Cloudflare&\#x27;s analysis frames Quad9&\#x27;s withdrawal from France under legal pressure as a precedent for applying intermediary-liability and site-blocking rules to DNS providers.

**「Impact」** French users of Quad9 must reconfigure to another resolver before service stops on November 24, 2026, and because the withdrawal covers both its security-filtering and general resolution services, networks and devices pointed at 9.9.9.9 lose malware blocking as well as name resolution through Quad9. Quad9 says roughly 20 other French lawsuits are pending, so the same blocking-order exposure applies to whichever alternative resolver French users switch to — including Cloudflare&\#x27;s 1.1.1.1, the operator publishing the analysis.

**「Community discussion」** John Todd, Quad9&\#x27;s CTO, reported at IETF 127 that he had found 100% support so far for Quad9&\#x27;s position and a general sense of dread about DNS legal pressure, while noting that the support was informal. Other commenters criticized European internet overregulation and the loss of 2000s-era freedoms, and one pressed Cloudflare to commit to withdrawing from affected countries rather than only opposing the outcome.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/10/french-courts-site-blocking-orders-drive-quad9-out-france">French Court’s Site-Blocking Orders Drive Quad9 Out Of France</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#Internet regulation`, `#privacy`, `#Cloudflare`, `#France`

---

<a id="item-tech-news-5"></a>
### [Microsoft&\#x27;s ONNX Runtime GitHub Repository Vanishes Without Notice](https://github.com/microsoft/onnxruntime) ⭐️ 7.0/10

Microsoft&\#x27;s ONNX Runtime GitHub repository \(github.com/microsoft/onnxruntime\) went dark without advance notice, and one user reported that evaluation pipelines began failing the morning the disappearance was noticed. The repository had roughly 22,000 stars, but the item contains no official explanation from Microsoft or GitHub; community members speculated about a compromised package or a security review. A user pointed to Intel&\#x27;s onnxruntime fork with OpenVINO modifications as the closest available alternative.

hackernews · nvader · Nov 17, 23:18 · [Discussion](https://news.ycombinator.com/item?id=50539610)

**「Background」** ONNX Runtime is Microsoft&\#x27;s cross-platform machine-learning inference and training accelerator, distributed under the MIT license and used to run models from frameworks such as PyTorch and TensorFlow/Keras. In the outage, an issue filed in the separate onnx/onnx project reported that both the main microsoft/onnxruntime repository and the companion onnxruntime-swift-package-manager repository had disappeared and were breaking CI/CD systems.

**「Broken pipelines and a non-equivalent fallback」** Teams that depend on ONNX Runtime as a cross-platform inference accelerator \(tool-3-1\) reported the failure concretely: commenter nvader said evals began failing in their pipelines the morning the repository went dark, with no advance warning. The only mirror surfaced in the thread is Intel&\#x27;s fork at github.com/intel/onnxruntime, which Heliodex noted carries Intel&\#x27;s OpenVINO modifications, so it is not a drop-in substitute for the upstream project without review.

**「Community Discussion」** Commenters traded speculative causes, including a recently compromised package and a Phrack article on backdoored models, while another user claimed ONNX collects application telemetry unless built from source with telemetry disabled. These are community claims and hypotheses, not confirmed reasons for the repository&\#x27;s disappearance.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/onnx/onnx/issues/8842">Onnxruntime has disappeared? · Issue #8842 · onnx/onnx · GitHub</a></li>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft/onnxruntime: ONNX Runtime: cross-platform ... Microsoft&#x27;s ONNX Runtime repo has vanished… · AGI Hunt Microsoft&#x27;s ONNX Runtime has disappeared from GitHub | Hacker ... Microsoft Removes ONNX Runtime from GitHub; Apple Services ... Microsoft&#x27;s ONNX Runtime vanished from GitHub. The repo ... Microsoft&#x27;s ONNX Runtime has disappeared from GitHub</a></li>
<li><a href="https://onnxruntime.ai/docs/">ONNX Runtime is a cross-platform machine-learning model accelerator</a></li>

</ul>
</details>

**Tags**: `#onnx-runtime`, `#microsoft`, `#github`, `#supply-chain`, `#machine-learning`

---

<a id="item-tech-news-6"></a>
### [Microsoft announces MAI Code 2 and Code 2 Flash coding models](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 7.0/10

Microsoft announced MAI Code 2 and MAI Code 2 Flash, two coding-focused AI models, with the announcement drawing attention for GitHub Copilot integration and competitive implications for developers. The supplied material does not include model sizes, context windows, benchmark results, pricing, or availability dates, so the models&\#x27; capabilities and shipping status cannot be verified from it. As a result, the announcement should be read as a vendor claim rather than an independently measured result, and real-world performance remains unconfirmed.

hackernews · lemonish97 · Nov 17, 18:25 · [Discussion](https://news.ycombinator.com/item?id=50535885)

**「Background」** Microsoft AI already publishes models under its own MAI prefix — third-party API marketplaces list image-generation entries such as MAI-Image-2.7 Flash — and MAI Code 2 and Code 2 Flash apply that branding to coding models positioned for everyday enterprise coding tasks at lower cost than competing models. A third-party model leaderboard lists both coding models as released on Nov. 17, 2026.

**「Practical impact」** Developers using GitHub Copilot can now select MAI Code 2, giving them a lower-cost coding-model option inside the same tool; Microsoft claims it reaches 96% of Claude Opus 5.5’s benchmark result at 5% of the cost. Those performance and price figures are vendor claims, so teams should test the model on their own codebases before treating it as a like-for-like replacement.

**「Community discussion」** One commenter reported switching GitHub Copilot to MAI Code 2 and using it to resolve tricky Python build issues in Windows WSL/Ubuntu and Azure Bicep deployment problems, saying it felt comparable to Claude Opus. Other commenters questioned whether the benchmark gains would hold up in real use and whether fast-following rivals can sustain a durable lead.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash : Everyday coding at... | Microsoft AI</a></li>
<li><a href="https://benchlm.ai/">LLM Leaderboard &amp; AI Model Benchmarks — Nov 2026 | BenchLM</a></li>
<li><a href="https://openrouter.ai/microsoft/mai-image-2.7-flash">MAI -Image- 2 .7 Flash - Image Generation API Pricing | OpenRouter</a></li>
<li><a href="https://madrobot.blog/2026/11/17/microsoft-mai-code-2-ignite-cheaper-openai-anthropic/">Microsoft MAI Code 2: 96% of Claude Opus 5.5 at 5% of the price</a></li>
<li><a href="https://www.zdnet.com/innovation/microsoft-ai-coding-model-rivals-claude-opus-5-5-ignite/">Microsoft says its new AI coding model rivals Claude Opus 5.5 ...</a></li>

</ul>
</details>

**Tags**: `#AI coding models`, `#Microsoft`, `#GitHub Copilot`, `#model benchmarks`, `#developer tools`

---

<a id="item-tech-news-7"></a>
### [Phrack Issue 73 Released](https://phrack.org/issues/73/introduction_md) ⭐️ 7.0/10

Phrack issue 73 has been released at phrack.org, the latest edition of the long-running security and hacker publication. The supplied item does not include the issue text, but the release is described as containing security research, and commenters point to a Docker escape write-up and a history of the 2000 SSH1 exploit among its contents. It is aimed at security researchers and systems-security readers rather than a general audience.

hackernews · notmine1337 · Nov 17, 18:31 · [Discussion](https://news.ycombinator.com/item?id=50535992)

**「What Phrack is」** Phrack is a long-running, community-produced hacking and computer-security publication that publishes technical articles and exploit write-ups rather than vendor announcements, so a new issue is generally read as primary research rather than a product release. Issue 73 follows that format: participants in the discussion point to a write-up on a Docker escape in the issue and to an article revisiting the history of the 2000 SSH1 exploit.

**「Impact」** Container operators have a concrete review task: check the Docker escape article for affected versions, disclosure status, and mitigations, because the supplied material does not confirm a CVE or patch.

**「Community Discussion」** Commenters debated whether Phrack&\#x27;s exploit write-ups, such as the Docker escape referenced in this issue, go through responsible disclosure and CVE assignment or are published without warning. Others shared nostalgia for Phrack&\#x27;s unpolished zine style and earlier issues, contrasting it with more polished, career-oriented comments on HN.

**Tags**: `#security research`, `#Phrack`, `#exploits`, `#hacker culture`, `#systems security`

---

<a id="item-tech-news-8"></a>
### [Prime Radiant releases external sandbox servers for coding agents](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison and Prime Radiant have released three sandbox server implementations demonstrating an “external sandbox” pattern: the coding agent runs outside the sandbox, while any code it executes runs inside a dedicated sandbox. The implementations use v86 with Alpine Linux in WebAssembly, Alpine Linux in an Apple Containers instance, or Microsoft’s Quicksand library, which bundles QEMU and Alpine Linux in a Python package. All expose the same localhost API and can be configured for Pi, Claude Code, or Codex, with an optional HTTP/HTTPS allow-list proxy and credential replacement so agent code can make authenticated requests without receiving the secret. The stated goal is safer experimentation with local models against mistakes or prompt-injection attacks.

rss · Simon Willison · Nov 17, 22:52

**「Why agents need an outer sandbox」** Coding agents such as Claude Code, Codex, and Pi run shell commands on the machine where they are installed, so a mistaken command or a prompt injection hidden in fetched content can act directly on that host. The external sandbox pattern reverses the usual arrangement: rather than confining the whole agent, it leaves the agent outside and routes only its code execution to a separate sandbox reached through a localhost API, with the released implementations backing that sandbox by WebAssembly-emulated Alpine Linux, an Apple Containers instance, or Microsoft&\#x27;s Quicksand library bundling QEMU and Alpine Linux.

**「What it changes for agent users」** Because all three servers expose the same localhost API, developers can point Pi, Claude Code, or Codex at a sandbox once and switch backends — v86 in WebAssembly, Alpine under Apple Containers, or Quicksand&\#x27;s bundled QEMU VM — without changing the agent configuration, though the container variant requires Apple Container on the host. The allow-list proxy and credential-replacement mechanism let agent-generated code reach only approved hosts and make authenticated calls without the agent holding the secret itself; these are the projects&\#x27; own design claims, not an independent security audit. Setup is a single command per server, such as \`uvx external-sandbox-container --write-setup\` or \`npx external-sandbox-v86\`.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/prime-radiant-inc/external-sandbox-container">GitHub - prime-radiant-inc/ external - sandbox - container : Python...</a></li>
<li><a href="https://github.com/prime-radiant-inc/external-sandbox-v86/">GitHub - prime-radiant-inc/external-sandbox-v86: Node.js ...</a></li>
<li><a href="https://github.com/prime-radiant-inc/external-sandbox-quicksand">GitHub - prime-radiant-inc/external-sandbox-quicksand: Run a ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#sandboxing`, `#security`, `#prompt injection`, `#developer tools`

---

<a id="item-tech-news-9"></a>
### [Datasette Lite rewritten with service workers and Pyodide](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 7.0/10

Simon Willison released a complete rewrite of Datasette Lite that runs the full Datasette Python application in the browser using Pyodide and service workers, and he says it is now almost indistinguishable from the server-side app. A crafted lite.datasette.io URL can load SQLite, JSON, CSV, or SQL files; select a released Datasette version from PyPI or a commit, tag, or branch from GitHub; choose from more than 100 SQLite versions; and install Datasette plugins from PyPI or wheel URLs, including JavaScript visualization tools. The rewrite replaces an earlier innerHTML-based approach that prevented JavaScript-dependent features from working; loaded data URLs must send open CORS headers.

rss · Simon Willison · Nov 17, 16:48

**「Background」** Pyodide runs Python code in the browser via WebAssembly, and Datasette Lite is Simon Willison&\#x27;s port of the Datasette server application onto that runtime. The original 2022 version simulated requests in a Pyodide web worker and injected the returned HTML with \`innerHTML\`; because script tags inserted that way do not execute, JavaScript-dependent Datasette features did not work. Service workers change that by letting the browser intercept requests and route them through the in-browser Datasette app.

**「What it enables」** Developers can share demos and bug reproductions as a single URL that pins the Datasette release and plugins without running a web server, as Willison demonstrates with Datasette 1.0a42 versus 1.0a43 pagination-bug links. The practical constraint is that any database, metadata, or other file loaded by URL must be hosted with open CORS headers, such as a GitHub Gist.

**Tags**: `#Datasette`, `#Pyodide`, `#WebAssembly`, `#service workers`, `#SQLite`

---

<a id="item-tech-news-10"></a>
### [China demonstrates 27 Gbps bidirectional Q/V-band wireless link](https://www.news.cn/tech/20261117/d6323540dccf4e2a976c48a762795956/c.html) ⭐️ 7.0/10

Researchers from the Aerospace Information Research Institute of the Chinese Academy of Sciences and other institutions demonstrated a bidirectional Q/V-band wireless link at 27 Gbps at the Lijiang China Remote Sensing Satellite Ground Station. The experiment tested modulation from 64QAM to 512QAM; 512QAM reached 6.75 Gbps bidirectionally on a single channel, and dual carriers plus polarization multiplexing raised the total to 27 Gbps, described as a domestic record. The team calls the key metrics domestically leading and internationally advanced and aims to exceed 50 Gbps in follow-up work. This was an experimental validation, not a deployed commercial service.

telegram · zaihuapd · Nov 17, 08:45

**「Background」** Q/V-band links are a millimeter-wave route to wider channels, but they demand high signal quality and linearity, which is why moving from 64QAM to 512QAM is a meaningful step in spectral efficiency. The Lijiang experiment tested that modulation range and then added dual-carrier and polarization multiplexing to build the 27 Gbps bidirectional link.

**「Impact」** The demonstration gives 6G and satellite-communications researchers a concrete domestic benchmark for Q/V-band links that combine high-order modulation with dual-carrier and polarization reuse. Because it was conducted at a ground station, it does not yet show how the link performs in operational satellite conditions or with commercial terminals.

**Tags**: `#6G`, `#Q/V band`, `#satellite communications`, `#wireless communications`, `#512QAM`

---

<a id="item-tech-news-11"></a>
### [Telegram Reportedly Limits Bot and Mini-App Payments to Stars](https://telegram.me/zaihuapd/45189) ⭐️ 7.0/10

A Telegram post from the channel zaihuapd reports that Telegram has told developers that digital goods sold in bots and mini-apps must be sold only through Telegram Stars, citing Apple and Google in-app purchase rules. The reported scope covers bot subscriptions, paid tools, access to third-party AI models, and credits or tokens, while cryptocurrency transactions would be limited to GRAM. The post says Telegram will begin proactive checks this week and that violating bots or mini-apps can be banned without a separate warning; the item provides no primary link, and the claim had previously lacked corroboration.

telegram · zaihuapd · Nov 17, 14:46

**「Why Stars sits behind the rule」** Telegram introduced Stars as its in-app currency for digital goods: users buy Stars through Apple&\#x27;s or Google&\#x27;s in-app purchase systems \(or via PremiumBot\) and then spend them on products sold by bots, such as e-books, online courses, and in-game items. That design is what connects bot and mini-app sales to the two app stores&\#x27; in-app purchase rules, the justification cited in the notice.

**「Impact」** For developers, the reported policy would require replacing or removing external payment flows for bot subscriptions, paid tools, and AI credits; the post&\#x27;s warning of immediate bans makes compliance timing the main operational risk.

<details><summary>References</summary>
<ul>
<li><a href="https://telegram.org/blog/telegram-stars">Telegram Stars : Pay for Digital Goods and More</a></li>

</ul>
</details>

**Tags**: `#Telegram`, `#platform policy`, `#payments`, `#mini apps`, `#AI monetization`

---

## Financial News

<a id="item-finance-news-1"></a>
### [UK tribunal rejects £2bn Sony PlayStation Store class action](https://www.reuters.com/world/sony-defeats-2-billion-uk-claim-over-playstation-store-pricing-2026-11-17/) ⭐️ 7.0/10

A UK tribunal on 17 November rejected a roughly £1.97bn collective action alleging Sony abused its dominance to overprice PlayStation Store content, ruling that competition between consoles limits its pricing power. The claim had sought to represent about 12.2 million UK consumers, who alleged prices should have been around 20% lower.

telegram · zaihuapd · Nov 17, 16:02

**「Background」** The case was a UK collective action—a lawsuit brought on behalf of many consumers—and after a trial that began in March, the Competition Appeal Tribunal dismissed it in full, ruling that the claimant class had not shown Sony infringed competition law.

<details><summary>References</summary>
<ul>
<li><a href="https://cyprus-mail.com/2026/11/17/sony-defeats-2-billion-uk-claim-over-playstation-store-pricing">Sony defeats £ 2 billion UK claim over PlayStation Store pricing</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#Sony PlayStation`, `#UK litigation`, `#digital storefronts`, `#consumer class action`

---

<a id="item-finance-news-2"></a>
### [China Auto Association Reviews 17 Automakers&\#x27; 60-Day Supplier Payment Terms](http://www.caam.org.cn/chn/5/cate_68/con_5237404.html) ⭐️ 7.0/10

The China Association of Automobile Manufacturers said in a Nov. 16 notice that, at the request of the Ministry of Industry and Information Technology, it is assessing 17 major automakers on whether they pay small and medium-sized enterprises \(SMEs\) within 60 days. The review also checks whether cash and bank acceptance bills make up at least 80% of payments to non-SME suppliers, with company submissions, a special-team review, expert evaluation and public release.

telegram · zaihuapd · Nov 18, 01:15

**「Background」** The 17 automakers had already publicly committed to paying suppliers within 60 days, and in September the same association issued a payment standard clarifying when that 60-day clock starts; the new evaluation checks whether those commitments are actually being followed.

<details><summary>References</summary>
<ul>
<li><a href="https://m.bjnews.com.cn/detail/1757938284168209.html">中 汽 协 明确“ 60 天 账 期 ” 支 付 规范， 17 家 车 企 响 应</a></li>

</ul>
</details>

**Tags**: `#China auto industry`, `#supplier payment terms`, `#regulatory oversight`, `#supply chain finance`, `#MIIT/CAAM`

---