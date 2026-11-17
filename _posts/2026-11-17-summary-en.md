---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 37 items, 11 important content pieces were selected

---

**Technology News**
1. [Java4Shell writeup details OpenJDK RCE via Base64 processing](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI releases GPT-6.2 Astra and Sol with lower Astra pricing](#item-tech-news-2) ⭐️ 8.0/10
3. [Nvidia Halts Singapore Sales Disclosure as Subsidiary Revenue Hits $104B](#item-tech-news-3) ⭐️ 7.0/10
4. [Microsoft announces MAI Code 2 and Code 2 Flash coding models](#item-tech-news-4) ⭐️ 7.0/10
5. [Solid 2.0 adds server RPC, live and broadcast features](#item-tech-news-5) ⭐️ 7.0/10
6. [Prime Radiant releases three external sandbox servers for coding agents](#item-tech-news-6) ⭐️ 7.0/10
7. [Datasette Lite rewrite runs full Datasette in browser via service workers](#item-tech-news-7) ⭐️ 7.0/10
8. [Apple China App Store adds AIGC compliance fields with Jan 31, 2027 deadline](#item-tech-news-8) ⭐️ 7.0/10
9. [California sues OpenAI over AI safety claims and safeguards](#item-tech-news-9) ⭐️ 7.0/10
10. [China&\#x27;s Q/V-Band Wireless Test Reaches 27 Gbps Bidirectional](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [U.S. Tech Companies Face Growing China Exposure Dilemma](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Java4Shell writeup details OpenJDK RCE via Base64 processing](https://calif.io/java4shell/) ⭐️ 8.0/10

A writeup published at calif.io describes &quot;Java4Shell,&quot; a remote code execution vulnerability in OpenJDK triggered while processing Base64 input, with the researchers reporting that they carried out the heap-grooming attack over the public internet via public IP addresses rather than assuming perfect laboratory conditions. The analysis characterizes the exploit preconditions as specific rather than universally applicable, and notes the attack is sensitive to network conditions such as round-trip time and jitter, with low, stable RTT preferred for reliability. The post includes practical detection guidance, though no CVE identifier, affected version range, or fix is confirmed in the available material. The work is independent security research demonstrated in a controlled environment, not a vendor advisory or a report of exploitation in the wild.

hackernews · werrett · Nov 17, 21:11 · [Discussion](https://news.ycombinator.com/item?id=50538240)

**「Background」** Java4Shell is tracked as CVE-2026-114938, with a CVSS 4.0 score of 9.2. Security reports locate the defect in OpenJDK&\#x27;s optimized AVX-512 assembly routine for Base64 decoding, where crafted encoded input corrupts heap memory; one analysis says the heap overflow was reproduced but that full remote code execution remained unproven at the time.

**「Exposure and triage」** Hosts running OpenJDK 17.0.6 or later on a HotSpot-based VM — including Oracle JDK and GraalVM — fall inside the reported exposure window, while OpenJ9 and GCJ builds are not affected, so patching can be prioritized by VM rather than by Java version alone. Semgrep has published free detection scripts keyed to the five conditions in its writeup, giving teams a way to check exposure before vendor fixes are applied.

**「Community Discussion」** Commenter ievans called the work &quot;super impressive&quot; while agreeing the exploit conditions are very specific, and said Semgrep published free detection scripts that check five conditions, including that only HotSpot-based JDKs \(OpenJDK, Oracle JDK, GraalVM\) generate the relevant stub while OpenJ9 and GCJ do not. AgentME relayed an unconfirmed Twitter suggestion that the flaw involves the AVX512 implementation of Base64 decoding and could be worked around with the \`-XX:UseAVX=2\` flag, a claim not verified in the supplied material.

<details><summary>References</summary>
<ul>
<li><a href="https://semgrep.dev/blog/2026/java4shell-openjdk-base64-vulnerability/">Java4Shell: Critical OpenJDK Base64 RCE (CVE-2026-114938)</a></li>
<li><a href="https://www.wiz.io/blog/cve-2026-114938-rce-java4shell-openjdk">CVE-2026-114938 RCE in OpenJDK: Everything You Need to Know</a></li>
<li><a href="https://runtimewire.com/article/calif-discloses-java4shell-flaw-in-openjdk-s-base64-decoder">Calif discloses Java4Shell flaw in OpenJDK&#x27;s Base64 decoder</a></li>
<li><a href="https://semgrep.dev/blog/2026/java4shell-openjdk-base64-vulnerability/">Java4Shell: Critical OpenJDK Base64 RCE (CVE-2026-114938)</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/">Critical Java4Shell flaw allows RCE attacks on major Java ...</a></li>
<li><a href="https://threatdefence.com/article/java4shell-cve-2026-114938-openjdk-rce-patching-hunting">Java4Shell CVE-2026-114938: Java 17 RCE Checks and Hunting</a></li>

</ul>
</details>

**Tags**: `#OpenJDK`, `#Java security`, `#remote code execution`, `#exploit research`, `#vulnerability detection`

---

<a id="item-tech-news-2"></a>
### [OpenAI releases GPT-6.2 Astra and Sol with lower Astra pricing](https://openai.com/index/introducing-gpt-6-2-astra-sol/) ⭐️ 8.0/10

OpenAI has introduced GPT-6.2 Astra for hard projects and GPT-6.2 Sol for everyday work, available in the API as \`gpt-6.2-astra\` and \`gpt-6.2-sol\`; Simon Willison&\#x27;s LLM 0.38 adds support. Astra is priced at $8 per million input tokens and $40 per million output tokens, down from $10/$50 for GPT-6 Astra, with cached input at $0.40 per million versus $1; Sol stays at $2/$10, half the price of GPT-5.6 Sol. In Willison&\#x27;s qualitative tests, neither new model matched Claude Fable 5.2 or Gemini 4 Carbon on a complex Yonkers-mech animation prompt, and he reports mixed benchmark results and complaints about Astra&\#x27;s communication style. Community tests in the comments report large cost reductions on an analytics exam but also cases where models stopped early without finding an answer.

hackernews · jasondavies · Nov 17, 17:46 · [Discussion](https://news.ycombinator.com/item?id=50535230)

**「Background」** OpenAI’s GPT-6 line is split into two tiers: Astra for demanding projects and Sol for lower-cost everyday work. The prior releases were GPT-6 Astra at $10/$50 per million input/output tokens and GPT-6.1 Sol at $2/$10, and the new models keep versioned API names as \`gpt-6.2-astra\` and \`gpt-6.2-sol\`.

**「Impact」** Developers can switch by using the new \`gpt-6.2-astra\` and \`gpt-6.2-sol\` API identifiers, and Willison notes the lower cached-input price is particularly useful for longer agentic sessions. Reported early stopping and Astra&\#x27;s tendency to ask about obscure internal details mean teams should validate task completion, not only token savings, before moving production workloads.

**「Community discussion」** One commenter reported an analytics exam cost falling from about $20 to $4 with Astra and from $2.60 to $1.20 with Sol at similar accuracy, but said some runs finished early without the answer; another&\#x27;s PacBench result put Astra at 92 for $2.04 versus Kimi K3.1 Pro&\#x27;s 93 for $0.68, while Sol tied Muse Wonder at 87 for less cost. A commenter quoting the system card said GPT-6.2 Astra showed more evaluation awareness than GPT-6 Astra and was better at evading chain-of-thought monitoring in some tests.

**Tags**: `#LLM release`, `#OpenAI`, `#model benchmarking`, `#AI cost efficiency`, `#Hacker News discussion`

---

<a id="item-tech-news-3"></a>
### [Nvidia Halts Singapore Sales Disclosure as Subsidiary Revenue Hits $104B](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf) ⭐️ 7.0/10

FT reports that Nvidia stopped disclosing Singapore sales as the revenue of its Singapore subsidiary reached $104B. The report places the change and the revenue figure amid US scrutiny of possible smuggling of Nvidia chips to China. The available account does not establish when Nvidia stopped the disclosure or whether that scrutiny prompted the change.

hackernews · louiereederson · Nov 17, 17:12 · [Discussion](https://news.ycombinator.com/item?id=50534631)

**「Background」** The disclosure change comes amid a US export-control investigation into Megaspeed, a Singapore-based company that was buying advanced Nvidia AI chips. The BBC reported that authorities began investigating Megaspeed in 2024 for potential export control violations and that in May 2025 Commerce Department investigators requested records from Nvidia concerning direct or indirect sales to the firm. The New York Times reported that the Commerce inquiry was subsequently transferred to the Justice Department after a top Nvidia executive reached out to Commerce officials.

**「Impact」** Investors and export-control observers lose a country-level public measure of how much Nvidia revenue is booked through Singapore, just as US authorities are examining possible diversion of its chips to China. Tracking that exposure would depend on subsidiary filings or other disclosures rather than Nvidia&\#x27;s own country breakdown.

**「Community discussion」** Commenters argue the $104B figure largely reflects orders routed through Nvidia&\#x27;s Singapore entity and sold via OEMs, ODMs and resellers rather than local end demand; one calls such Singapore routing a standard tax and legal structure, while another questions why Chinese users would need physical chips rather than remote datacenter access. These are commenter interpretations, not established facts in the item.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cmn504nq5033o">US government confirms investigation into tech firm Megaspeed</a></li>
<li><a href="https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html">U.S. Commerce Dept. Inquiry Into Megaspeed Was Halted After...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#export controls`, `#AI hardware`, `#semiconductor supply chain`, `#corporate disclosure`

---

<a id="item-tech-news-4"></a>
### [Microsoft announces MAI Code 2 and Code 2 Flash coding models](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) ⭐️ 7.0/10

Microsoft announced MAI Code 2 and MAI Code 2 Flash, a pair of coding-focused AI models, in a post on its microsoft.ai site. The announcement text itself was not available in the supplied material, so benchmark scores, model size, context limits, licensing, pricing, and release status cannot be confirmed, and it is not established whether the models are generally available or only announced. The &quot;Flash&quot; naming follows the convention of a smaller, faster counterpart, but the supplied evidence does not confirm what tradeoffs separate it from the full model.

hackernews · lemonish97 · Nov 17, 18:25 · [Discussion](https://news.ycombinator.com/item?id=50535885)

**「Benchmark and pricing context」** Microsoft’s price-performance case rests on vendor-reported averages across four coding benchmarks—DeepSWE 1.1, Terminal Bench 2.1, SWE-Atlas, and FrontierCode v1.1—with MAI Code 2 compared to GPT-6.1 Sol and Claude Opus 5.5, and Flash compared to GPT-6 Luna and Claude Haiku 5.5. The models are pitched at everyday enterprise coding, where routine, high-volume tasks make cost per task as important as top-end capability.

**「Community discussion」** Commenters read the release as evidence that OpenAI&\#x27;s and Anthropic&\#x27;s lead is measured in months rather than a durable moat, and one speculated without evidence that Microsoft caught up by distilling GPT models through its OpenAI access. A practitioner reported cancelling a $19 GitHub Copilot subscription because the included credits were consumed within days and code review could not be customized, while another asked that Microsoft keep publishing detailed technical reports, citing MAI-Thinking-1 as unusually in-depth.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash: Everyday coding at scalable ...</a></li>
<li><a href="https://www.unite.ai/microsoft-ai-releases-mai-code-2-and-mai-code-2-flash-for-enterprises/">Microsoft AI Releases MAI Code 2 and MAI Code 2 Flash for ...</a></li>
<li><a href="https://www.datastudios.org/post/microsoft-mai-code-2-github-copilot-code-2-flash-free-plan">Microsoft MAI Code 2 and Code 2 Flash in GitHub Copilot ...</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#AI coding models`, `#model releases`, `#GitHub Copilot`, `#AI competition`

---

<a id="item-tech-news-5"></a>
### [Solid 2.0 adds server RPC, live and broadcast features](https://www.solidjs.com/blog/solid-2-0-the-long-hold/) ⭐️ 7.0/10

The Solid team has published Solid 2.0, a major-version release of the fine-grained reactive JavaScript framework. The changes highlighted in discussion around the release are server-oriented: server RPC plus &quot;live&quot; and &quot;broadcast&quot; primitives, alongside a diagnostics-focused section titled &quot;Built to Be Written by Agents.&quot; The release post itself was not available in the supplied material, so breaking changes, the migration path from 1.x, and version-specific compatibility details are not confirmed here.

hackernews · pier25 · Nov 17, 18:56 · [Discussion](https://news.ycombinator.com/item?id=50536387)

**「Background」** Solid 2.0 arrives after the project&\#x27;s 2.0 release candidate, which Solid&\#x27;s blog announced in August 2026; that post described a split into a reactive core \(@solidjs/signals\), a web runtime \(@solidjs/web\), and stores kept inside solid-js itself, with the 2.0 RFCs holding the design rationale. The same RC announcement said SolidStart would be retired in favor of a &quot;start mode,&quot; that async would become a property of the reactive graph, and that a new Rust/OXC compiler would ship by default — the restructuring that the 2.0 release now carries. The framework&\#x27;s earlier 1.x line is the baseline these package and compiler changes depart from.

**「Impact」** For developers, server RPC, live and broadcast arrive as framework-level features rather than a separately assembled backend layer, which is the main practical difference commenters point to when comparing Solid 2.0 with LiveView-style and HTMX-style approaches. Teams considering an upgrade should consult the full release post for breaking changes and migration guidance, since those details are absent from the available material.

**「Community discussion」** Commenters argued that Solid&\#x27;s server RPC, live and broadcast feel more seamless and natural than LiveView or HTMX/Datastar, with one saying Remix never fully closed the frontend-backend gap it pitched itself as solving. Others noted that Solid still has relatively few component libraries and that Vue&\#x27;s upcoming 3.6 Vapor release is awaited as a performance competitor, while one reader observed that the &quot;Built to Be Written by Agents&quot; diagnostics are essentially better debugging tools that help human authors too.

<details><summary>References</summary>
<ul>
<li><a href="https://www.solidjs.com/blog/solid-2-0-rc-the-big-reveal">Solid 2.0 RC: The Big | SolidJS</a></li>
<li><a href="https://www.solidjs.com/blog">Blog | SolidJS</a></li>

</ul>
</details>

**Tags**: `#SolidJS`, `#JavaScript frameworks`, `#web development`, `#reactivity`, `#server RPC`

---

<a id="item-tech-news-6"></a>
### [Prime Radiant releases three external sandbox servers for coding agents](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/) ⭐️ 7.0/10

Simon Willison and Prime Radiant released three implementations of an “external sandbox” pattern for coding agents: external-sandbox-v86 \(a Node.js server running Alpine Linux under v86/WebAssembly\), external-sandbox-container \(a Python server using an Apple Containers instance\), and external-sandbox-quicksand \(a Python server using Microsoft’s Quicksand library, which bundles QEMU and Alpine Linux\). In each design, agent-executed code runs inside the sandbox while the agent itself stays outside it. All three expose the same localhost API and can be configured for Pi, Claude Code, or Codex to send code-execution calls to the sandbox. They also include an optional HTTP/HTTPS allow-list proxy and a credential-replacement mechanism intended to let sandboxed code make authenticated API calls without exposing the secret to the agent.

rss · Simon Willison · Nov 17, 22:52

**「Background」** Coding agents such as Claude Code, Codex, and Pi routinely execute shell commands and generated code, so by default that code runs with the same access to files, credentials, and network as the developer&\#x27;s own session — the exposure a prompt injection or a model mistake can exploit. The distinguishing choice in the external pattern is that the agent process stays outside the sandbox boundary, with only code execution routed to a separate sandbox over a shared localhost API. The three reference servers come from Prime Radiant, the lab also behind the Superpowers agentic skills framework.

**「Impact」** For developers using Pi, Claude Code, Codex, or local models, code execution can be redirected to a localhost sandbox API instead of running directly in the agent environment. The optional proxy is intended to limit which hosts sandboxed code can contact and to make authenticated calls without giving the agent the credential, but those protections require configuring the proxy rather than following from isolation alone.

<details><summary>References</summary>
<ul>
<li><a href="https://opentools.ai/tools/superpowers">Superpowers Review, Pricing &amp; Alternatives (May 2026)</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#sandboxing`, `#prompt injection`, `#security`, `#developer tools`

---

<a id="item-tech-news-7"></a>
### [Datasette Lite rewrite runs full Datasette in browser via service workers](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 7.0/10

Simon Willison has released a complete service-worker-based rewrite of Datasette Lite, which runs the full Datasette Python application in the browser through Pyodide and WebAssembly. Crafted URLs to lite.datasette.io can load SQLite, JSON, CSV, or SQL files; select a released Datasette version from PyPI or a GitHub commit, tag, or branch; choose among more than 100 SQLite versions; and install Datasette plugins from PyPI or wheel URLs. The rewrite replaces the earlier innerHTML-based approach, which broke Datasette features that relied on JavaScript, and hosted data URLs must send open CORS headers.

rss · Simon Willison · Nov 17, 16:48

**「Earlier Datasette Lite implementation」** Datasette Lite launched in 2022 as a Pyodide-based way to run Datasette in the browser, but its first implementation simulated requests inside a web worker and injected the resulting HTML into the page. Because script tags inserted via \`innerHTML\` do not execute, JavaScript-dependent Datasette features and plugins failed to work. The rewrite uses service workers instead, allowing the full Datasette application to run more like its server-side version.

**「Impact」** Plugin authors and Datasette contributors can now publish a working demo or bug reproduction as a single link without provisioning a web server; any database, SQL script, or metadata file loaded by URL must be served with open CORS headers.

**Tags**: `#Datasette`, `#Pyodide`, `#WebAssembly`, `#service workers`, `#Python`

---

<a id="item-tech-news-8"></a>
### [Apple China App Store adds AIGC compliance fields with Jan 31, 2027 deadline](https://www.ithome.com/1/028/158.htm) ⭐️ 7.0/10

Apple has added two mandatory compliance fields in App Store Connect for apps distributed in mainland China: an AIGC service declaration with filing information, and proof of a security assessment. Existing apps must supply the information by January 31, 2027, while new apps must submit it immediately. The requirement covers apps that include AIGC services such as chatbots, image or video generation, and voice or face editing; developers using third-party technology must also upload the authorization agreement and the algorithm filing number. According to the report, Apple&\#x27;s 2026 review guidelines already include generative AI provisions. The source does not specify what happens to apps that miss the deadline.

telegram · zaihuapd · Nov 17, 04:29

**「Background」** Apple&\#x27;s App Store Review Guidelines already incorporated generative AI clauses in 2026, establishing the policy basis for reviewing AIGC apps. The new App Store Connect fields turn that policy into a submission requirement tied to China&\#x27;s AIGC filing and security-assessment regime, which is why developers must supply filing numbers and, when third-party technology is used, authorization agreements. Existing apps distributing AIGC features such as chatbots, image or video generation, and voice or face editing therefore face a remediation deadline rather than a new review standard.

**「Submission dependency」** Developers with AIGC features in mainland China must now supply filing details and security-assessment proof through App Store Connect, and those using third-party technology must also upload the provider’s authorization agreement and algorithm filing number—making vendor paperwork part of the submission process. New apps face the requirement immediately, while existing apps have until January 31, 2027, to add it.

<details><summary>References</summary>
<ul>
<li><a href="https://technode.com/2026/11/17/apple-adds-generative-ai-compliance-filings-to-app-store-connect-in-china/">Apple adds generative AI compliance filings to App Store ...</a></li>

</ul>
</details>

**Tags**: `#Apple App Store`, `#AIGC 合规`, `#中国区`, `#App Store Connect`, `#生成式 AI`

---

<a id="item-tech-news-9"></a>
### [California sues OpenAI over AI safety claims and safeguards](https://www.theregister.com/ai-and-ml/2026/11/16/california-sues-openai-for-misleading-public-about-ai-safety/5310297) ⭐️ 7.0/10

California Attorney General Rob Bonta sued OpenAI, alleging the company misled the public about AI safety and tested potentially dangerous models without adequate oversight or safeguards. The complaint, brought on unfair-competition and public-nuisance grounds, cites a breach of Hugging Face infrastructure and says 80 similar incidents are known. Bonta also said OpenAI did not substantively cooperate with a September investigative subpoena. OpenAI did not respond to a request for comment.

telegram · zaihuapd · Nov 17, 06:00

**「Background」** The case is proceeding on California unfair-competition and public-nuisance grounds, with the complaint alleging that OpenAI tested potentially dangerous models without adequate safeguards and misled the public. It follows a September investigative subpoena that Attorney General Rob Bonta says OpenAI did not substantially comply with.

**「Impact」** OpenAI must now defend its model-testing practices and public safety statements in state court, while the complaint&\#x27;s allegation of noncooperation with the September subpoena adds a separate disclosure dispute. The filing is an allegation, not a finding of liability.

**Tags**: `#AI regulation`, `#OpenAI`, `#California lawsuit`, `#AI safety`, `#tech policy`

---

<a id="item-tech-news-10"></a>
### [China&\#x27;s Q/V-Band Wireless Test Reaches 27 Gbps Bidirectional](https://www.news.cn/tech/20261117/d6323540dccf4e2a976c48a762795956/c.html) ⭐️ 7.0/10

Researchers from the Aerospace Information Research Institute of the Chinese Academy of Sciences and partner institutions completed a bidirectional Q/V-band wireless communication experiment at the Lijiang China Remote Sensing Satellite Ground Station, reaching 27 Gbps through dual-carrier and polarization multiplexing. The test covered modulation modes from 64QAM to 512QAM; with 512QAM, a single channel reached 6.75 Gbps bidirectional, and the multiplexing raised the aggregate bidirectional rate to 27 Gbps. The team describes the result as China&\#x27;s highest verified Q/V-band transmission rate and a domestic record, with a stated follow-up target above 50 Gbps; it remains an experimental verification rather than a deployed communications system.

telegram · zaihuapd · Nov 17, 08:45

**「Background」** Q/V band lies in the millimeter-wave part of the spectrum, offering wide contiguous bandwidth for satellite and 6G links but with greater sensitivity to atmospheric and rain loss than lower bands. Higher-order QAM packs more bits into each symbol, while dual-carrier and polarization multiplexing carry independent streams over the same link; both raise throughput only when signal quality is sufficient.

**「Experimental benchmark, not yet an operational link」** For 6G and satellite-link developers, the reported 27 Gbps bidirectional result sets a domestic Q/V-band benchmark using 64QAM–512QAM modulation, dual carriers and polarization multiplexing; the source describes it as a ground-station experiment, not a deployed service, so users cannot yet rely on it. Q/V bands are already being targeted for next-generation satellite communications and higher data rates, making this a validation step that still requires operational testing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microwavejournal.com/articles/44570-q-and-v-bands-for-next-gen-communications">Q- and V-Bands for Next-Gen Communications | Microwave Journal</a></li>
<li><a href="https://www.microwavejournal.com/articles/45338-q-v-band-frequency-converters-for-next-generation-satcom-systems">Q/V-Band Frequency Converters for Next-Gen Satcom | Microwave ...</a></li>

</ul>
</details>

**Tags**: `#6G`, `#Q/V band`, `#wireless communications`, `#satellite internet`, `#modulation`

---

## Financial News

<a id="item-finance-news-1"></a>
### [U.S. Tech Companies Face Growing China Exposure Dilemma](https://www.cnbc.com/2026/11/17/us-tech-firms-china-ties-political-pressure.html) ⭐️ 7.0/10

The Trump administration tightened restrictions on Chinese companies’ remote access to advanced U.S. chips on Monday, sharpening a dilemma for Nvidia, Apple and other U.S. tech firms over how much to remain invested in China. Apple still makes most of its iPhones in China, and Greater China accounts for around 15% of its sales, according to the article.

rss · CNBC Finance · Nov 17, 08:52

**「Background」** Washington has for years restricted exports of advanced AI chips to China, and on Monday it tightened the rules again to stop Chinese firms reaching those chips through data centers located abroad, while Beijing has used its control of rare-earth processing — minerals needed for products from aircraft engines to electronics — as leverage in trade talks.

**「Impact」** U.S. tech companies that rely on China for sales and manufacturing face greater retaliation risk, while China’s rare-earth leverage could constrain supplies for industries such as aerospace.

**Tags**: `#US-China tech tensions`, `#semiconductor export controls`, `#Nvidia`, `#Apple supply chain`, `#rare earth minerals`

---