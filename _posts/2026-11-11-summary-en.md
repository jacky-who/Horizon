---
layout: default
title: "Horizon Summary: 2026-11-11 (EN)"
date: 2026-11-11
lang: en
---

> From 47 items, 18 important content pieces were selected

---

**Technology News**
1. [Microsoft publishes .NET 11 runtime release notes](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepMind Introduces AlphaProof Code for Formal Code Verification](#item-tech-news-2) ⭐️ 8.0/10
3. [Blender 5.3 ships Gaussian Splat support and geometry-node upgrades](#item-tech-news-3) ⭐️ 8.0/10
4. [Chips and Cheese Details AMD Zen 6 Core and Memory Changes](#item-tech-news-4) ⭐️ 8.0/10
5. [Google opens Gemini 4 Carbon to public](#item-tech-news-5) ⭐️ 8.0/10
6. [Synaptics patent claims halt DisplayLink open-source driver work](#item-tech-news-6) ⭐️ 7.0/10
7. [Chrome&\#x27;s modern-web-guidance 1.0 steers coding agents to native browser APIs](#item-tech-news-7) ⭐️ 7.0/10
8. [Meta launches Muse Ember, a small efficient model for agent workloads](#item-tech-news-8) ⭐️ 7.0/10
9. [Apiiro finds 2,539 credentials exposed through Claude Code settings](#item-tech-news-9) ⭐️ 7.0/10
10. [Fireworks confirms new cyberattack exposing customer billing data and model artifacts](#item-tech-news-10) ⭐️ 7.0/10
11. [Anthropic whitelists 185 regions, excluding mainland China, Hong Kong, Macau](#item-tech-news-11) ⭐️ 7.0/10
12. [MiniMax open-weights H3 Image for 4K generation and editing](#item-tech-news-12) ⭐️ 7.0/10

**Technology Blog**
1. [Glue Work Is Still Harmful in the Age of AI](#item-tech-blog-1) ⭐️ 5.0/10

**Financial News**
1. [Polymarket reports $1.8 billion annualized revenue amid U.S. growth](#item-finance-news-1) ⭐️ 7.0/10
2. [Fed Governor Waller leans toward December rate hike, floats possible half-point move](#item-finance-news-2) ⭐️ 7.0/10
3. [China new-energy passenger car exports rose 138.8% in first three quarters of 2026](#item-finance-news-3) ⭐️ 7.0/10
4. [Anthropic 撤回拟募资 693 亿美元的 IPO 文件](#item-finance-news-4) ⭐️ 7.0/10
5. [TSMC October revenue NT$586.89bn, up 59.7% year on year](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Microsoft publishes .NET 11 runtime release notes](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime) ⭐️ 8.0/10

Microsoft has published a &quot;What&\#x27;s new in the .NET 11 runtime&quot; page in its .NET documentation, appearing alongside the .NET 11 announcement post. The page is scoped to runtime-level changes for .NET and C\# developers rather than the full SDK or language feature set. The supplied item itself contains little more than a link to the announcement, so the specific features, version numbers, and any stated performance results in the notes cannot be verified from the excerpt.

hackernews · stevefan1999 · Nov 10, 12:20 · [Discussion](https://news.ycombinator.com/item?id=50439284)

**「Background」** Before .NET 11, the C\# compiler translated \`async\` methods into generated state machines that handled suspension and resumption; Microsoft says the .NET 11 runtime libraries no longer contain those compiler-generated state machines and now rely entirely on runtime-provided async, which it presents as both a migration path and broad functional and performance validation of the feature. External coverage describes the same shift as &quot;Runtime Async V2,&quot; in which the runtime itself manages async suspension and resumption instead of leaving that work entirely to compiler-generated state machines.

**「Impact」** Developers upgrading existing applications should read the compatibility notes before moving to .NET 11: one commenter reports that the cast \`\(decimal\)0.1\` evaluates to \`0.1\` under .NET 10 but \`0.1000000000000000055511151231\` under .NET 11, a behavior difference that could affect code depending on decimal conversions.

**「Community discussion」** Commenters welcomed the release, with one saying they were surprised that runtime async support could deliver equivalent performance while removing state machines from the compiled code and improving stack traces. Others argued that C\# and .NET remain underappreciated because of legacy perceptions that the platform is Windows-only or stuck in the .NET Framework era, and one pointed to the new official \`dotnetup\` version manager as a practical addition.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime">What&#x27;s new in .NET 11 runtime | Microsoft Learn</a></li>
<li><a href="https://www.c-sharpcorner.com/article/net-11-runtime-async-performance-what-actually-changes">.NET 11 Runtime Async Performance: What Actually Changes</a></li>

</ul>
</details>

**Tags**: `#.NET`, `#C\#`, `#runtime`, `#async`, `#release notes`

---

<a id="item-tech-news-2"></a>
### [DeepMind Introduces AlphaProof Code for Formal Code Verification](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 8.0/10

DeepMind has introduced AlphaProof Code, an AI agent for formal verification of code. The supplied material points to Lean theorem proving and software correctness as relevant themes, but the underlying blog post was not provided, so the release&\#x27;s precise scope, availability, and measured results remain unconfirmed. A reported zero-bug result is therefore a claim under discussion, not an established outcome.

hackernews · ilreb · Nov 10, 12:11 · [Discussion](https://news.ycombinator.com/item?id=50439193)

**「What formal verification of libsignal entails」** Formal verification means producing machine-checked proofs that an implementation satisfies a stated specification, rather than relying on tests that sample behavior. The target here is libsignal, the reference implementation of the Signal protocol, with proofs carried out at the machine-code level. DeepMind describes AlphaProof Code as a multi-LLM agentic framework that divides the work as a research team would: human experts decide what to prove, and AI agents attempt the proofs.

**「Impact」** For teams using AI-generated proofs, the practical check is the theorem statement: a proof that code matches a specification does not show that the specification captures the intended behavior. Generated specifications and theorem statements need review before a green proof is treated as evidence of correctness.

**「Community discussion」** Commenters disagreed about how much a formal proof establishes: hedora questioned a reported zero-bug result, suggesting the theorems might be wrong or cover only narrow properties, while thibsrn said the agent appears to verify implementation rather than the specification and asked how it differs from a conventional coding agent. r0ze-at-hn said AI-written Lean can “cheat,” and andai described an AI-assisted refactor whose generated tests all passed even though the implementation was backwards.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-alphaproof-code/">Formal Verification of Signal’s Protocol with... — Google DeepMind</a></li>
<li><a href="https://google-deepmind.github.io/code-verification/">AlphaProof Code : Verifying Signal’s Security at the Machine- Code ...</a></li>
<li><a href="https://shiftdelete.net/en/alphaproof-code">AlphaProof Code Verifies Signal Encryption at Machine Level</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#AI coding agents`, `#Lean theorem proving`, `#Google DeepMind`, `#software correctness`

---

<a id="item-tech-news-3"></a>
### [Blender 5.3 ships Gaussian Splat support and geometry-node upgrades](https://www.blender.org/download/releases/5-3/) ⭐️ 8.0/10

Blender 5.3 is released with Gaussian Splat support and geometry-node workflow enhancements, according to the release announcement. The update is aimed at 3D artists and technical users working with splat-based scenes or node-driven pipelines. The item does not provide further detail on supported splat formats, rendering performance, or hardware compatibility.

hackernews · amlib · Nov 10, 16:15 · [Discussion](https://news.ycombinator.com/item?id=50442426)

**「What Gaussian splatting is」** Gaussian splatting is a scene-reconstruction technique that represents a captured scene as a cloud of oriented 3D Gaussians rather than as a triangle mesh; the widely cited reference implementation is INRIA&\#x27;s graphdeco-inria/gaussian-splatting repository. Blender 5.3&\#x27;s release notes describe the new capability as importing splats as point clouds, manipulating and previewing them through Geometry Nodes and Workbench, and rendering them natively in EEVEE or Cycles.

**「Impact」** For users with existing Gaussian-splat captures, Blender 5.3 provides an in-application path to open and work with them. The release item does not specify performance, format compatibility, or hardware requirements, so production suitability still needs testing.

**「Community Discussion」** Commenters welcomed the release, with one reporting that a 4-million-splat scene exported from Spirula Studio ran fast and felt mature on an M4 during the beta, while another said the bigger pipeline gain is geometry-node bundle support combined with lists and closures. A separate commenter raised triangle splatting as an alternative worth considering because GPUs are built to render triangles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.blender.org/download/releases/5-3/">5 . 3 — Blender</a></li>
<li><a href="https://github.com/graphdeco-inria/gaussian-splatting">GitHub - graphdeco-inria/ gaussian -splatting: Original reference...</a></li>

</ul>
</details>

**Tags**: `#Blender`, `#Gaussian Splatting`, `#3D graphics`, `#open source`, `#geometry nodes`

---

<a id="item-tech-news-4"></a>
### [Chips and Cheese Details AMD Zen 6 Core and Memory Changes](https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast) ⭐️ 8.0/10

Chips and Cheese has published a microarchitecture deep-dive on AMD&\#x27;s Zen 6 CPU family, covering core execution resources, memory I/O, and branch prediction. According to details quoted from the analysis, Zen 6 reduces integer multiply units from three to two and drops PDEP/PEXT throughput from three to two instructions per cycle, while supporting four vector loads per cycle at 256 bits or narrower; the density &quot;C&quot; cores are reported at 32 per chiplet with increased L3 cache. The 2-ahead branch predictor is described as carried over from Zen 5 rather than new. This is an architectural analysis, not a product launch, so no SKUs, prices, or ship dates are established here.

hackernews · pixelpoet · Nov 10, 17:02 · [Discussion](https://news.ycombinator.com/item?id=50443090)

**「Background」** Zen 6 follows AMD&\#x27;s Zen 5 and pairs standard Zen 6 cores with a distinct Zen 6c variant intended for density-focused designs. TechPowerUp reports that the Zen 6c CCD is built on TSMC&\#x27;s 2 nm node, carries 32 cores, and has 128 MB of on-die L3 cache, while Wccftech lists an 8-wide dispatch/rename stage, six ALUs, and four loads plus two stores per cycle for the Zen 6 designs.

**「CCD density and the memory controller」** Server buyers evaluating Zen 6 face a density jump: AMD&\#x27;s disclosed EPYC Venice parts claim up to 256 cores across new SP7/SP8 platforms with a stated 27% IPC uplift, while the 12-core CCD with 4 MB of L3 per core described in TechPowerUp&\#x27;s deep-dive keeps per-core cache from thinning as core counts rise. On the desktop side the practical consequence is the reworked I/O die — commenters report that the current AM5 Zen 4/Zen 5 memory controller struggles past roughly 3600 MT/s with both channels populated, so existing memory-kit and BIOS tuning assumptions should be re-validated for Zen 6 builds rather than carried over unchanged.

**「Community Discussion」** Commenter bmenrigh argues the AM5 I/O die is the weakest part of Zen 4 and Zen 5, reporting that it is hard or impossible to exceed 3600 MT/s when both memory channels are populated, and says they have heard Zen 6 moves to a new I/O chiplet on a smaller node — an expectation, not a confirmed spec. Others focus on the core: Aardwolf asks whether the multiply-unit and PDEP/PEXT reductions are one shared circuit change or two independent cuts, Remnant44 speculates the freed area went to VNNI pipes and questions whether gather performance finally improves, and bee\_rider asks how 32 cores in a single CCD should be managed at the lowest NUMA level.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/amd-zen-6-architecture-ipc-cores-memory-performance-epyc-venice/">AMD Zen 6 Architecture Brings A Phenomenal 27% IPC Increase Over...</a></li>
<li><a href="https://www.techpowerup.com/review/amd-zen-6-technical-deep-dive/">AMD Zen 6 Technical Deep Dive | TechPowerUp</a></li>
<li><a href="https://www.techpowerup.com/review/amd-zen-6-technical-deep-dive/">AMD Zen 6 Technical Deep Dive | TechPowerUp</a></li>
<li><a href="https://wccftech.com/amd-zen-6-architecture-ipc-cores-memory-performance-epyc-venice/">AMD Zen 6 Architecture Brings A Phenomenal 27% IPC Increase Over...</a></li>

</ul>
</details>

**Tags**: `#AMD Zen 6`, `#CPU microarchitecture`, `#semiconductor hardware`, `#branch prediction`, `#memory controllers`

---

<a id="item-tech-news-5"></a>
### [Google opens Gemini 4 Carbon to public](https://deepmind.google/models/model-cards/gemini-4-carbon/) ⭐️ 8.0/10

Google has opened public access to Gemini 4 Carbon, its flagship model for cybersecurity and long-horizon agent workflows, after announcing it two weeks earlier for a subset of cyber defenders. It is available through the Gemini API, Google AI Studio, and Gemini for business, with preview access to multi-agent /swarm collaboration in Antigravity. Launch pricing is $2 per million input tokens and $10 per million output tokens, scheduled to double to $4/$20 on December 1. The release claims first-place rankings on benchmarks including CursorBench 4.0 and costs at least 2x less than the next-best external model, but those figures are vendor claims rather than independent measurements.

telegram · zaihuapd · Nov 10, 15:48

**「Background」** Google announced Gemini 4 Carbon roughly two weeks before this public launch, but limited it to &quot;a subset of cyber defenders&quot; rather than making it generally available. The model is now open to everyone else at launch pricing of $2 per million input tokens and $10 per million output tokens, which Google says will double to $4/$20 on December 1.

**「Pricing deadline for adopters」** Developers and businesses adopting Gemini 4 Carbon through the API should update cost models for the scheduled December 1 price increase: the launch rate of $2 per million input tokens and $10 per million output tokens is set to double to $4/$20, according to the release post. The Antigravity /swarm integration is a preview, so teams should test multi-agent workflows there before depending on them in production.

**Tags**: `#Google DeepMind`, `#Gemini 4 Carbon`, `#AI models`, `#agentic workflows`, `#API pricing`

---

<a id="item-tech-news-6"></a>
### [Synaptics patent claims halt DisplayLink open-source driver work](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/) ⭐️ 7.0/10

Synaptics has asserted patent claims that stopped work on DisplayLink drivers, according to an LWN report. The dispute concerns open-source driver development and patent enforcement around DisplayLink hardware support. The available report does not specify which driver project halted, the exact patent claims, or whether deadlines or settlement talks are involved.

hackernews · speckx · Nov 10, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50443824)

**「Background」** DisplayLink is Synaptics display-connectivity technology, and Synaptics publishes the official DisplayLink Manager driver package. Earlier, Synaptics sent a cease-and-desist to a hobbyist building an open-source DisplayLink driver, and Phoronix reported that the project disappeared after the legal threats.

**「Practical effect」** Linux users waiting on the independent DisplayLink driver will not receive its fixes or added hardware support, and developers pursuing similar reverse-engineered drivers now face a concrete cease-and-desist threat over patent claims.

**「Community discussion」** Commenters criticized a quoted Synaptics demand for US$25,000 to cover documentation costs as a scare tactic, with one arguing that reverse engineering concerns patent disclosure rather than patent infringement. Others reported practical DisplayLink problems, including audio issues when docking and disconnecting, and argued that newer USB4 and Thunderbolt docks using DisplayPort Alt Mode reduce the need for DisplayLink.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation">Synaptics sends cease-and-desist order to creator of open - source ...</a></li>
<li><a href="https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver">Synaptics Appears To Use Legal Threats To Block Open - Source ...</a></li>
<li><a href="https://www.synaptics.com/products/displaylink-manager-graphics-connectivity-1102">DisplayLink Manager Graphics Connectivity 1.10.2 | Synaptics</a></li>
<li><a href="https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver">Synaptics Appears To Use Legal Threats To Block... - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation">Synaptics sends cease-and-desist order to creator... | Tom&#x27;s Hardware</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#patents`, `#DisplayLink`, `#Linux drivers`, `#hardware`

---

<a id="item-tech-news-7"></a>
### [Chrome&\#x27;s modern-web-guidance 1.0 steers coding agents to native browser APIs](https://github.com/GoogleChrome/modern-web-guidance) ⭐️ 7.0/10

Google&\#x27;s Chrome team released modern-web-guidance 1.0, an open-source npm package of more than 200 hand-curated web-platform guides \(~1.7 MB\) built with Firefox, MDN, and Edge to push coding agents toward native browser primitives instead of legacy div-and-JavaScript patterns. It ships as an agent skill plus an Agentic RAG CLI, with commands to install, search guides, and run a deterministic legacy-scan trained on 30,000 GitHub repositories; Chrome reports 92% average precision on held-out repos and an eval lift from 55% to 92% across 200 tasks and about 1,700 Playwright/AST assertions. The materials are available now under an open-source license, and the guide set is updated as the web evolves. Commenters flagged cross-browser limits: some recommended features, including CSS @function, calc-size\(\), and corner-shape, are stable in Chrome but not supported in Firefox and Safari.

hackernews · paulirish · Nov 10, 18:01 · [Discussion](https://news.ycombinator.com/item?id=50443812)

**「Why agents default to legacy patterns」** Coding agents generate frontend code from patterns in their training data, which tends to favor long-standing div-and-JavaScript approaches over newer native browser APIs. Modern-web-guidance packages curated platform guidance as an installable agent skill and search CLI so an agent can retrieve the relevant native pattern instead of defaulting to older code.

**「Verify compatibility before shipping agent output」** Teams that install the skill should gate agent-suggested primitives behind a compatibility check \(for example Can I use or a browserslist step\), because the guidance covers at least some features that are Chromium-only today: CSS \`corner-shape\`, one of the areas the guides address, is ignored entirely by Safari and Firefox, which fall back to ordinary rounded corners so the same stylesheet renders different geometry per browser. Where a chosen primitive lacks support in a target browser, the agent&\#x27;s rewrite needs a fallback rather than a straight replacement of the existing div-plus-JS pattern.

**「Community discussion」** Commenters disagreed about the project&\#x27;s effect on standards: one argued Chrome already has too much power and that LLMs following Chrome&\#x27;s guidance could recreate &quot;view in \[dominant browser\]&quot; lock-in, while another suggested publishing a grep-friendly Markdown index so agents can use the guides without installing the npm package.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/mikhailmogilnikov/how-i-brought-css-corner-shape-to-safari-and-firefox-cka">How I Brought CSS corner-shape to Safari and Firefox</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#web development`, `#browser standards`, `#open source`, `#LLM tooling`

---

<a id="item-tech-news-8"></a>
### [Meta launches Muse Ember, a small efficient model for agent workloads](https://simonwillison.net/2026/Nov/10/muse-ember/) ⭐️ 7.0/10

Meta AI has launched Muse Ember 1.0, a small model positioned for repeated agent work such as tool calls, coding subtasks, routing, extraction, and long document parsing. For short prompts it is priced at $0.10 per million input tokens and $0.50 per million output tokens, matching GPT-6 Luna and Claude Haiku 5.5, with cached input at $0.004 per million tokens. Its price threshold is 200k input tokens, after which rates rise to $0.30 per million input and $1.50 per million output; GPT-6 Luna&\#x27;s threshold is 272k and Claude Haiku 5.5&\#x27;s is 100k. Muse Ember offers six reasoning levels—minimal, low, medium, high, xhigh, and max—and Artificial Analysis places its xhigh and max configurations on its cost-per-task efficiency frontier.

rss · Simon Willison · Nov 10, 07:28

**「Context」** Meta AI&\#x27;s Muse Ember is aimed at the same small-model tier as Claude Haiku 5.5 and GPT-6 Luna, all of which start at $0.10 per million input tokens and $0.50 per million output tokens for short prompts. Because models can consume different numbers of reasoning tokens for the same task, comparisons increasingly rely on cost-per-task benchmarks such as Artificial Analysis rather than list prices alone. Meta&\#x27;s pricier Muse Wonder model is the family reference point the source uses: Ember&\#x27;s sample outputs were judged comparable at roughly one-fortieth the price.

**「Impact」** Developers routing high-volume, short-prompt agent subtasks can match the headline input and output prices of GPT-6 Luna and Claude Haiku 5.5 while paying less for cached input, but long-document workloads should account for Muse Ember&\#x27;s higher rates once a prompt exceeds 200k tokens.

**Tags**: `#AI models`, `#Meta AI`, `#model pricing`, `#efficient inference`, `#agents`

---

<a id="item-tech-news-9"></a>
### [Apiiro finds 2,539 credentials exposed through Claude Code settings](https://www.ithome.com/1/024/888.htm) ⭐️ 7.0/10

Apiiro reported finding 2,539 real credentials, including database passwords and API tokens, across 1,994 GitHub repositories. More than 100,000 Claude Code local settings files were uploaded to public repositories, and about 1,100 of them contained secret data. The exposure occurs because Claude Code writes approved shell commands into a local settings file that is committed with a project when it is not Git-ignored. The Claude Code team said it is studying preventive measures and considering built-in secret scanning.

telegram · zaihuapd · Nov 10, 11:20

**「Why the settings file matters」** Claude Code records approved shell commands in a local settings file, \`.claude/settings.local.json\`; when a developer chooses “don’t ask again,” that permission is stored there. Apiiro’s scan examined public copies of that local file, showing how a per-user settings artifact can enter Git history and carry credentials when it is not ignored.

**「Impact」** Developers who use Claude Code should check whether their local settings files were committed to public repositories and rotate any exposed database passwords or API tokens; adding the settings file to Git ignore rules would prevent the same path from recurring.

<details><summary>References</summary>
<ul>
<li><a href="https://dailysecurityreview.com/cyber-security/apiiro-finds-1994-github-repos-leaking-secrets-via-claude-code-files/">Apiiro Finds 1,994 GitHub Repos Leaking Secrets via Claude ...</a></li>
<li><a href="https://dev.to/madnessbrains_i/apiiros-claude-code-scan-found-2539-secrets-in-claudesettingslocaljson-local-desktop-tools-9ho">Apiiro’s Claude Code Scan Found 2,539 Secrets in .claude ...</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#凭据泄露`, `#GitHub 安全`, `#AI 编程工具`, `#密钥扫描`

---

<a id="item-tech-news-10"></a>
### [Fireworks confirms new cyberattack exposing customer billing data and model artifacts](https://finance.sina.com.cn/stock/usstock/c/2026-11-10/doc-iniyfzhx2605532.shtml) ⭐️ 7.0/10

Fireworks confirmed a new cyberattack that exposed some customer billing information, model weights, and datasets, and it is investigating the incident with Palo Alto Networks&\#x27; Unit 42. The report says it remains unclear whether customers beyond Harvey, which said its own customer data was unaffected, or end users were affected. People familiar with the matter said some large customers paying millions of dollars a year are considering migrating; Fireworks&\#x27; annualized revenue reached $1 billion in July, and it had planned to begin a new funding round this week at a valuation of at least $30 billion.

telegram · zaihuapd · Nov 10, 13:00

**「Background」** The reported attack follows Fireworks&\#x27; October 2026 security incident, which initially involved exposed credentials. In a November 9 update, the company said attackers reached development machines through a third-party cloud provider, widening the exposure to customer account details, billing records, datasets, and incomplete model weights.

**「Customer fallout」** The exposure is not limited to Fireworks&\#x27; own systems: customers who uploaded proprietary model weights and datasets to the platform now have to treat that intellectual property as potentially compromised, alongside any billing details on file. The report says some accounts paying millions of dollars a year are already weighing a move to another inference provider, a churn risk that arrives while the company was reportedly seeking new funding at a $30 billion to $40 billion valuation \(Business Insider\).

<details><summary>References</summary>
<ul>
<li><a href="https://fireworks.ai/security/bulletins/october-2026-security-incident-update">Update on October 2026 security incident | Fireworks AI</a></li>
<li><a href="https://cybersecuritynews.com/fireworks-ai-data-breach/">Hackers Breach Fireworks AI Through Third-Party Cloud ...</a></li>
<li><a href="https://www.forbes.com/sites/annatong/2026/11/09/fireworks-cyberattack-exposes-customer-data-and-ai-models-as-fallout-widens/">Fireworks Cyberattack Exposes Customer Data And AI Models As ...</a></li>
<li><a href="https://www.businessinsider.com/fireworks-ai-is-seeking-new-funding-at-around-valuation-2026-10">Fireworks AI Is in Early Talks for a New Funding ... - Business Insider</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#security breach`, `#Fireworks AI`, `#customer data`, `#model weights`

---

<a id="item-tech-news-11"></a>
### [Anthropic whitelists 185 regions, excluding mainland China, Hong Kong, Macau](https://www.anthropic.com/legal/supported-regions) ⭐️ 7.0/10

Anthropic has published a supported-regions policy that switches Claude availability to a whitelist of 185 countries and territories, effective November 12. Claude.ai, Claude Code, Cowork, the API, and Claude models offered through cloud platforms or authorized resellers are available only in listed locations; mainland China, Hong Kong, and Macau are not included. The policy also prohibits use by anyone physically in an unsupported region—including employees of supported-region companies traveling there—and by entities registered or headquartered in unsupported regions, or majority-owned or controlled by such entities, regardless of where their personnel are located.

telegram · zaihuapd · Nov 10, 13:44

**「Background」** A whitelist policy treats every country or region not expressly listed as unsupported by default, the inverse of a blocklist that names only prohibited markets. Anthropic&\#x27;s policy applies that model to its apps, API and developer platform, and to Claude models offered through cloud platforms and authorized resellers.

**「Impact」** Organizations with mainland Chinese, Hong Kong, or Macau ownership or staff—and supported-region companies whose employees travel to unsupported locations—must treat those users as out of policy, and access routed through cloud platforms or resellers does not create an exemption. Compliance teams will need to check entity registration, headquarters, and majority ownership, not just where a user is located.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/legal/supported-regions">Supported Regions Policy - Anthropic</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude`, `#AI access policy`, `#regional restrictions`, `#compliance`

---

<a id="item-tech-news-12"></a>
### [MiniMax open-weights H3 Image for 4K generation and editing](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) ⭐️ 7.0/10

MiniMax released MiniMax H3 Image with open weights, saying the model handles text-to-image, image-reference, and image-editing tasks and can generate 4096×4096 images—about 16 megapixels—in roughly 10 seconds. The model accepts up to 16 reference images, and MiniMax also announced a Highspeed version that it claims is 3–4× faster than mainstream tools, while the standard mode is 1.5–2× faster. The model is available on Hugging Face and through an API and has been integrated into MiniMax Code and Hailuo; MiniMax lists a standard 4K image at about $0.069, with a first-week price of about $0.034. These speed and performance figures are vendor claims and have not been independently validated in the supplied material.

telegram · zaihuapd · Nov 10, 15:39

**「Background」** MiniMax H3 Image is released as an open-weight model: its weights are published on Hugging Face, while the same model is also offered through MiniMax&\#x27;s platform API and products. That dual distribution lets developers download the model rather than relying only on a hosted endpoint.

**「Impact」** Developers can pull the weights from Hugging Face and self-host, or call the hosted API at about $0.069 per standard 4K image \(~$0.034 during the first-week promo\), with the model also wired into MiniMax Code and Hailuo. The release is under a community licence rather than a permissive open-source one, so teams should confirm commercial-use terms before shipping; the 1.5–2× and 3–4× speed multipliers remain vendor claims without independent measurement.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3-image">MiniMax H 3 - Image : Bringing 4 K Image Generation into the...</a></li>
<li><a href="https://news.sulat.com/2026/11/11/minimax-releases-h3-image-open-weights/">MiniMax releases H 3 - Image as open weights - Sulat AI &amp; Tech News</a></li>

</ul>
</details>

**Tags**: `#AI image generation`, `#open-weight models`, `#MiniMax`, `#4K generation`, `#model release`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Glue Work Is Still Harmful in the Age of AI](https://seangoedecke.com/glue-work-is-still-harmful-in-the-age-of-ai/) ⭐️ 5.0/10

rss · Sean Goedecke · Nov 11, 00:00

**「Background」** In an earlier post, Sean Goedecke argued that glue work—the unrewarded coordination, documentation, onboarding, and reporting that keeps software teams running—should not depend on engineers&\#x27; self-sacrifice. He now asks whether LLMs writing most code make that unpaid work more valuable or less.

**「Solution」** Goedecke argues that LLMs reduce rather than revive the need for glue work, offering four reasons from his experience. AI agents magnify individual engineers, so one person can take on projects that once required a team, eliminating much meeting and status-update coordination. He asserts that engineers need less “careful handling” than in the 2010s because many prickly gatekeepers were forced out or coerced into changing after the end of ZIRP. Fewer junior hires also mean less informal onboarding hand-holding. Finally, “write-only” reports can be generated with LLMs, since their purpose was to prove awareness or satisfy a requirement, not to be read. He cautions, however, that interpersonal communication must not be delegated: making colleagues talk to an LLM will damage relationships. His advice is to avoid becoming “the glue work person,” let bad processes fail, do small amounts of tactical glue work when it clearly helps a project, and spend most effort on code and directing AI agents in line with company values.

**「Takeaway」** Goedecke&\#x27;s thesis is that LLMs weaken rather than restore the career case for glue work: the risk of becoming the glue person remains, while many coordination and reporting tasks are shrinking. Engineers should use glue work selectively and keep their main effort on technical work.

**Tags**: `#glue work`, `#software engineering career`, `#LLM impact on engineering`, `#organizational dynamics`, `#engineering management`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Polymarket reports $1.8 billion annualized revenue amid U.S. growth](https://www.cnbc.com/2026/11/10/polymarket-annualized-revenue-us-growth.html) ⭐️ 7.0/10

Polymarket said its annualized revenue has surpassed $1.8 billion, up from the more than $1 billion run rate it disclosed in June, as its U.S. exchange&\#x27;s October notional volume rose to $14.5 billion from $4 billion in June, according to TickerTracker. The company-reported figures come as Polymarket raises a $1 billion funding round at a $21 billion valuation and faces a CFTC investigation into its advertising practices and past access by U.S. residents to its international exchange.

rss · CNBC Finance · Nov 10, 13:00

**「Background」** Prediction markets let users buy and sell contracts that pay out if a specific event happens, with prices acting as implied odds. Polymarket opened its U.S. exchange in May 2026, and by June it said its annual revenue run rate was above $1 billion; the CFTC&\#x27;s investigation into the company was already reported in June 2026.

**「Who is affected」** Polymarket&\#x27;s growth leans heavily on sports-style &quot;combo&quot; contracts, the same contracts three federal appeals courts are split over classifying as swaps or bets, so the outcome of that fight — alongside state-level regulation — will shape what its U.S. exchange can offer and what its users can trade.

<details><summary>References</summary>
<ul>
<li><a href="https://www.politico.com/news/2026/06/26/cftc-investigation-prediction-market-polymarket-00978218">Wall Street regulator investigating prediction market giant ...</a></li>
<li><a href="https://www.cnbc.com/2026/06/26/cftc-is-conducting-an-investigation-into-polymarket-source-says.html">CFTC is conducting an investigation into Polymarket ... - CNBC</a></li>
<li><a href="https://ctmirror.org/2026/08/05/kalshi-polymarket-prediction-markets-ct/">As prediction markets grow, CT comptroller warns of &#x27;dark side&#x27;</a></li>
<li><a href="https://financefeeds.com/prediction-markets-cftc-state-regulation-2026/">Prediction Markets Hit $410B as CFTC and States Clash</a></li>

</ul>
</details>

**Tags**: `#Polymarket`, `#prediction markets`, `#revenue growth`, `#CFTC investigation`, `#startup funding`

---

<a id="item-finance-news-2"></a>
### [Fed Governor Waller leans toward December rate hike, floats possible half-point move](https://www.cnbc.com/2026/11/10/fed-governor-waller-sees-december-hike-likely.html) ⭐️ 7.0/10

Fed Governor Christopher Waller said he is leaning toward a December rate increase and raised the possibility of a half-point move if inflation data come in hotter than forecast. October CPI rose 0.4% headline and 0.3% core, each 0.1 percentage point above the Dow Jones consensus.

rss · CNBC Finance · Nov 10, 17:13

**「Background」** The Fed left rates unchanged at its October meeting after a quarter-point increase in September, and Waller said carrying out signaled hikes matters because otherwise market rate expectations could fall and loosen monetary policy.

**Tags**: `#monetary policy`, `#Federal Reserve`, `#interest rates`, `#inflation`, `#CPI`

---

<a id="item-finance-news-3"></a>
### [China new-energy passenger car exports rose 138.8% in first three quarters of 2026](https://finance.sina.com.cn/tech/roll/2026-10-26/doc-iniwpfnc2438186.shtml) ⭐️ 7.0/10

In the first three quarters of 2026, China&\#x27;s new-energy passenger car exports reached 3.887 million units, up 138.8% from a year earlier, while domestic retail sales of such cars fell 12.8% to 7.758 million, according to Sina Finance. Exports became an important support for automakers&\#x27; sales growth.

telegram · zaihuapd · Nov 10, 02:56

**「Background」** From January 1, 2026, China halved its purchase-tax break for new-energy vehicles: the 10% purchase tax, previously fully waived, is now charged at an effective 5%, and the tax-free cap fell from 30,000 yuan to 15,000 yuan \(tool-1-2, tool-1-3\). The article links the weaker domestic retail figures to those reduced subsidies and purchase-tax benefits, as well as to a high base of comparison from the prior year.

**「Impact」** In September, domestic new-energy passenger car retail sales fell 16.7% year on year and fuel-car retail fell 43%; the article attributes the weaker demand to adjustments in car-purchase subsidies and purchase-tax preferences as well as a high year-earlier base, factors that directly affect domestic buyers and dealers.

<details><summary>References</summary>
<ul>
<li><a href="https://chejiahao.m.autohome.com.cn/info/24720031">车 市开 年 遇冷！ 2026 补 贴 退 坡 ，1月销量断崖式下滑_ 车 家号_汽 车 之家</a></li>
<li><a href="https://m.dzplus.dzng.com/share/general/0/NEWS2979460TOELOPBZCWQEN">m.dzplus.dzng.com/share/general/0/NEWS2979460TOELOPBZCWQEN</a></li>

</ul>
</details>

**Tags**: `#中国新能源车出口`, `#国内汽车零售`, `#乘用车市场`, `#购车补贴与购置税`, `#行业数据`

---

<a id="item-finance-news-4"></a>
### [Anthropic 撤回拟募资 693 亿美元的 IPO 文件](https://www.reuters.com/business/anthropic-aims-raise-up-693-billion-blockbuster-ipo-2026-11-10/) ⭐️ 7.0/10

Anthropic 撤回了一份分发给银行的证券文件，该文件拟以每股 70 至 80 美元发行约 8.67 亿股 A 类股，最高募资 693 亿美元。该公司随后在一封邮件中称定价信息不准确，表示将更新文件并拒绝进一步置评。

telegram · zaihuapd · Nov 10, 06:25

**「Background」** Anthropic is an artificial-intelligence company; an IPO would be its first public sale of shares, and the document was circulated to banks before being retracted late Monday, Reuters reported.

**「影响」** 该文件还将 Google、Nvidia、AMD、Broadcom、Micron、Microsoft 和 TSMC 列为按发行价参与 260 亿美元私募配售的投资者，因此这次撤回使这些投资方原拟认购的条款，以及预计本周二启动的路演，都处于未定状态。

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/anthropic-aims-raise-up-693-billion-blockbuster-ipo-2026-11-10/">EXCLUSIVE: Anthropic’s nearly $70 billion IPO plan briefly ...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI financing`, `#private placement`, `#capital markets`

---

<a id="item-finance-news-5"></a>
### [TSMC October revenue NT$586.89bn, up 59.7% year on year](https://pr.tsmc.com/chinese/news/3349) ⭐️ 7.0/10

TSMC reported October 2026 consolidated revenue of about NT$586.89 billion, up 59.7% from a year earlier and 14.7% from September. Revenue for January through October totaled about NT$4.4856 trillion, up 43.3% year on year.

telegram · zaihuapd · Nov 10, 08:07

**「Background」** TSMC discloses monthly consolidated revenue, giving an early indication of chip demand before its quarterly results.

**Tags**: `#台积电`, `#半导体`, `#月度营收`, `#台湾股市`

---