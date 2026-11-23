---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 48 items, 27 important content pieces were selected

---

**Technology News**
1. [Zhipu&\#x27;s GLM-5.4 adds looped-transformer architecture](#item-tech-news-1) ⭐️ 8.0/10
2. [Apple removed my open-source app from EU App Stores after 9 years](#item-tech-news-2) ⭐️ 8.0/10
3. [Ladybird browser engine reaches first alpha release](#item-tech-news-3) ⭐️ 8.0/10
4. [Google builds simulated internet Mirror Dimension to test Chrome AI agent](#item-tech-news-4) ⭐️ 8.0/10
5. [Codex2api 疑似供应链投毒，3.1.10–3.1.12 疑含后门](#item-tech-news-5) ⭐️ 8.0/10
6. [Meta AI chief warns superintelligence is near as control risk grows](#item-tech-news-6) ⭐️ 8.0/10
7. [NVIDIA Board Reinstates Jensen Huang as President and CEO](#item-tech-news-7) ⭐️ 8.0/10
8. [LeCun accuses Amodei of hyping risk to suppress open models](#item-tech-news-8) ⭐️ 7.0/10
9. [Spelunkr.tv Curates Internet Archive Videos Into Free Linear TV Channels](#item-tech-news-9) ⭐️ 7.0/10
10. [Open-source nospeaker makes MacBook trackpad vibrate out speech](#item-tech-news-10) ⭐️ 7.0/10

**Global Chips**
1. [星思半导体获证监会备案，拟赴港交所IPO](#item-chip-news-1) ⭐️ 7.0/10
2. [US Intelligence Chief Says China Likely Has Nvidia Advanced AI Chips](#item-chip-news-2) ⭐️ 6.0/10
3. [LCY in advanced talks to sell control of China chip chemicals unit to HSG-led group for about $600M](#item-chip-news-3) ⭐️ 6.0/10
4. [New U.S. BIS chip export rule takes effect amid China auto-tech concerns](#item-chip-news-4) ⭐️ 6.0/10
5. [Report alleges Huang associate had China spy agency contact](#item-chip-news-5) ⭐️ 5.0/10
6. [Nvidia Says U.S. Officials Cleared Jensen Huang&\#x27;s Return as No Security Risk](#item-chip-news-6) ⭐️ 5.0/10
7. [Pakistan, China researchers discuss advanced semiconductor collaboration](#item-chip-news-7) ⭐️ 5.0/10
8. [Report claims two Chinese vendors in top five intelligent-driving chip ranks](#item-chip-news-8) ⭐️ 5.0/10
9. [BIS Nov 16 rule tightens overseas tape-out access, report says](#item-chip-news-9) ⭐️ 5.0/10
10. [How Nvidia’s billion-dollar turnaround in China is threatened by Huang’s exit](#item-chip-news-10) ⭐️ 4.0/10
11. [SoftBank&\#x27;s Reported $1 Trillion SK Hynix Buyout Bid Called a Non-Starter](#item-chip-news-11) ⭐️ 4.0/10

**Technology Blog**
1. [Skip the DRAM Tier: Running Agentic KV Cache on NVMe](#item-tech-blog-1) ⭐️ 8.0/10
2. [Flailing as a Strategy Under Uncertainty](#item-tech-blog-2) ⭐️ 6.0/10
3. [What OpenAI&\#x27;s Perplexity Graph Reveals About Training](#item-tech-blog-3) ⭐️ 5.0/10

**Financial News**
1. [上海地铁21年来首次调整票价](#item-finance-news-1) ⭐️ 8.0/10
2. [蚂蚁集团领投中国具身智能公司 1 亿美元，估值 16 亿美元](#item-finance-news-2) ⭐️ 7.0/10
3. [Bloomberg：英伟达董事会据称未经咨询高管层便恢复黄仁勋CEO职务](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Zhipu&\#x27;s GLM-5.4 adds looped-transformer architecture](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

Zhipu has released GLM-5.4, which it describes as its first model built on a &quot;loop transformer&quot; architecture that reuses layer weights across repeated compute iterations instead of computing each layer once. The company presents the design as easing inference memory-bandwidth pressure and improving generalized coding. GLM-5.4 is available to GLM Coding Plan subscribers, adds vision capability, and raises quotas 50% versus GLM-5.3 for weekly-quota plans. The supplied material includes no benchmark results or independent validation of the claimed efficiency gains, and one early user reported the model was not yet reachable via OpenRouter or the standard Z.ai API plan.

hackernews · foohis · Nov 23, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50609685)

**「Background」** Conventionally, an LLM computes each transformer layer once per generated token, streaming that layer&\#x27;s weights from HBM into the chip and back out before moving to the next layer, which makes memory bandwidth a primary inference bottleneck. A looped transformer instead reuses the same layer weights across multiple passes; according to a technical walkthrough, GLM-5.4 reuses the same 28 layers across iterations, paired with gated progressive updates and a hybrid KV cache. Z.ai&\#x27;s developer documentation describes GLM-5.4 as its latest flagship model and the first built on the Loop Transformer architecture, with the Model API still pending a security assessment.

**「Access and quota effects for Coding Plan users」** Users on the GLM Coding Plan now get GLM-5.4 with vision support, and weekly-quota plans carry 50% more quota than they had for GLM-5.3. One reviewer reported that the new model was not reachable through OpenRouter or the regular Z.ai API plan, so access required moving to the Coding Plan, whose keys behave like regular API keys but expose the new model. Because the announcement included no benchmark results, developers weighing a migration should test GLM-5.4 on their own coding tasks rather than assume the claimed coding improvements hold.

**「Community discussion」** Commenters credited Zhipu with unusually detailed technical disclosure; one explained that a loop transformer cuts memory-bandwidth cost by computing each loaded layer several times rather than moving a fresh layer onto the chip for every token, and noted that the original Transformer resembles an unrolled loop pairing separate attention and feed-forward weight sets. A practitioner countered that Chinese models&\#x27; long &quot;thinking&quot; sessions make even conceptually simple tasks slow, suggesting that behavior may be how they close the gap on benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM - 5 . 4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.youtube.com/watch?v=M6vD9r8kI3A">GLM 5 . 4 Makes AI Smarter by Loop Architecture - YouTube</a></li>
<li><a href="https://explainx.ai/blog/glm-5-4-coding-plan-vision-50-percent-quota-boost-november-2026">GLM-5.4 Coding Plan: +50% Quota, Vision (Nov 2026 ...</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/glm-5-4-review">GLM-5.4 Review: What&#x27;s New and What&#x27;s Confirmed</a></li>

</ul>
</details>

**Tags**: `#loop transformers`, `#LLM architecture`, `#inference efficiency`, `#code generation`, `#Zhipu GLM`

---

<a id="item-tech-news-2"></a>
### [Apple removed my open-source app from EU App Stores after 9 years](https://github.com/glushchenko/fsnotes/discussions/2056) ⭐️ 8.0/10

An open-source Mac app developer reports Apple removed their app from EU App Stores after nine years, with commenters identifying lapsed EU DSA trader verification as the likely cause and citing similar cases.

hackernews · fluder · Nov 23, 18:48 · [Discussion](https://news.ycombinator.com/item?id=50616933)

**Tags**: `#EU DSA`, `#Apple App Store`, `#open source`, `#app compliance`, `#developer platforms`

---

<a id="item-tech-news-3"></a>
### [Ladybird browser engine reaches first alpha release](https://ladybird.org/posts/alpha/) ⭐️ 8.0/10

The Ladybird project has released its first alpha, letting macOS and Linux users install the browser without compiling it themselves. Ladybird is built from scratch rather than on Chromium&\#x27;s Blink or WebKit, with its own HTML parser, CSS engine, layout, JavaScript engine, and WebAssembly support; it still relies on HarfBuzz for text shaping, Skia for 2D graphics, ffmpeg for video, and SQLite. The alpha is explicitly early: Andreas Kling&\#x27;s announcement warns that some websites will not work and the browser will sometimes crash, and asks users to report broken sites and crash reports from inside the browser. The source reports Ladybird finishing October with about 2,184,722 passing web-platform-tests subtests, ahead of Safari&\#x27;s roughly 2,172,990 and just below Firefox&\#x27;s 2,189,315, after a 75,650-pass gain that the project attributes largely to AI coding agents filling in missing functionality.

hackernews · janvdberg · Nov 23, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50614249)

**「Background」** Ladybird grew out of SerenityOS, Andreas Kling&\#x27;s from-scratch operating system, and its browser still incorporates code from that predecessor project. According to the source account, Kling wrote in February 2026 that Ladybird had adopted Rust, porting parts of its LibJS JavaScript engine from C++ to roughly 25,000 lines of Rust in two weeks with AI coding tools. The October 2026 engineering push described in the source — moving style and layout to their own thread, a new JavaScript JIT, and a rewritten WebAssembly engine — preceded this first alpha build.

**「Impact」** Hands-on testing in the supplied accounts found WebAssembly-heavy tools working, including an ffmpeg video compressor and a Pyodide Python REPL, but Datasette Lite failed because \`navigator.serviceWorker.startMessages\` is unimplemented — a FIXME in Ladybird&\#x27;s ServiceWorkerContainer IDL — so service-worker-dependent sites remain a practical compatibility gap. One commenter suggests limiting alpha use to browsing that does not involve logins, authentication, payments, or downloads, consistent with the project&\#x27;s own crash warning.

**「Community discussion」** Commenters reported mostly successful rendering across many sites, including YouTube, Google Maps, and a ProxMox NoVNC view that one found snappier than in Firefox; another noticed slightly jerky page scrolling. One commenter credited the switch to production-grade dependencies such as SQLite and Skia for the improvement while expressing nostalgia for the original SerenityOS hacker spirit.

**Tags**: `#browser engines`, `#open source`, `#web rendering`, `#software releases`

---

<a id="item-tech-news-4"></a>
### [Google builds simulated internet Mirror Dimension to test Chrome AI agent](https://www.landian.news/archives/128701.html) ⭐️ 8.0/10

Google has built an isolated simulated internet called Mirror Dimension to test its Chrome AI agent, according to a report from Landian News. The environment reportedly contains thousands of simulated websites, with each engineer testing in a separate isolated instance and more than 1,000 test cases run per day. The tests cover agent actions such as opening sites, searching, logging in, adding items to a cart, and completing tasks, with a focus on defending against prompt-injection attacks from malicious web pages. The report is a secondhand aggregation and provides no primary documentation, so the scale and effectiveness of the setup remain unverified.

telegram · zaihuapd · Nov 23, 01:30

**「Background」** Google has been adding agentic capabilities to Chrome that let an in-browser agent open sites, search, log in, and complete tasks such as adding items to a cart on a user&\#x27;s behalf. Because such agents read page content and act on it, hostile prompt injections embedded in web pages are a central security risk; Mirror Dimension is Google&\#x27;s isolated, synthetic-web environment for repeatedly evaluating those defenses before agents encounter the real web.

**「Impact」** If the described setup is accurate, it points to a testing requirement for browser-integrated agents: prompt injection from ordinary web content is a direct attack surface, so agent features need sandboxed environments and adversarial pages before they handle logins or purchases on real sites. The report does not specify which Chrome agent features or release channels use this testing, so users cannot yet tell which capabilities have been evaluated this way.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/security/mirror-dimension-for-agents/">Mirror Dimension for Agents: Evaluating Browser-Use Agents ...</a></li>
<li><a href="https://www.wired.com/story/google-built-a-giant-mirror-dimension-internet-to-test-its-chrome-ai-agents/">Google Built a Giant ‘Mirror Dimension’ Internet to Test Its ...</a></li>
<li><a href="https://windowsforum.com/news/google-mirror-dimension-a-synthetic-web-for-testing-chrome-ai-agents-against-prompt-injection.453465/">Google Mirror Dimension: A Synthetic Web for Testing Chrome ...</a></li>

</ul>
</details>

**Tags**: `#AI 代理`, `#Chrome`, `#提示词注入`, `#浏览器自动化`, `#AI 安全`

---

<a id="item-tech-news-5"></a>
### [Codex2api 疑似供应链投毒，3.1.10–3.1.12 疑含后门](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

A Telegram post reports that the codex2api author account was compromised and that the attacker bypassed the main branch by pushing tags, causing Release builds to publish backdoored versions. According to the post, v3.1.11 removed authentication, effectively enabling unauthenticated remote command execution, and a workflow exfiltrated 16 GitHub Actions secrets from at least 21 repositories under the same account. Users who installed or updated to versions 3.1.10–3.1.12 are advised to stop using the tool immediately, roll back to 3.1.9, and rotate the GitHub token, SSH keys, database credentials, and other related secrets such as DeepSeek keys. The post explicitly frames the incident as suspected and relays claimed external reports without independent technical verification.

telegram · zaihuapd · Nov 23, 11:21

**「Why tag-triggered releases matter here」** The reported attack depends on a release workflow in which pushing a tag can build and publish an artifact without going through the main branch, so control of the maintainer account is enough to ship a backdoored version. The Telegram post cites an incident retrospective and an original report but provides no primary technical evidence, and Horizon has no earlier summary of codex2api releases or prior compromises to establish a baseline. The post also does not clarify whether the 21 affected repositories and the exposed DeepSeek keys belong to the maintainer or to downstream users.

**「Impact」** Anyone who ran Codex2API v3.1.10–v3.1.12 should stop that instance immediately, preserve its logs for investigation, and redeploy v3.1.9 as the rollback target. Because the compromised workflow exposed 16 GitHub Actions secrets across at least 21 repositories, affected operators also need to rotate GitHub tokens, SSH keys, and all database and DeepSeek-related credentials; the backdoored releases have reportedly been removed from GitHub, but removal does not revoke secrets already leaked.

<details><summary>References</summary>
<ul>
<li><a href="https://ccnavx.com/blog/codex2api-supply-chain-incident">Codex2API Supply Chain Attack: Affected Versions &amp; Fix</a></li>

</ul>
</details>

**Tags**: `#supply-chain security`, `#github actions`, `#backdoor`, `#credential rotation`, `#open source security`

---

<a id="item-tech-news-6"></a>
### [Meta AI chief warns superintelligence is near as control risk grows](https://thenextweb.com/news/metas-ai-chief-says-superintelligence-is-arriving-and-control-is-at-risk) ⭐️ 8.0/10

Meta&\#x27;s chief AI officer and Superintelligence Labs head Alexandr Wang wrote on X that superintelligence is no longer a &quot;someday&quot; issue, citing a Riemann Hypothesis proof produced by mathematician Levent Alpöge with Anthropic&\#x27;s Claude and machine-verified by the Lean and Mathlib communities on Saturday. Wang argued the gap between AI and top human mathematicians now reduces to specific knowledge, engineering integration, and experimentation, and warned that humans will struggle to retain control of systems capable of unlimited self-improvement or systems 1,000 times smarter than themselves. He called for urgent investment in safety, alignment, and protection research. The proof has no human-readable version yet, and the supplied material provides no independent verification of it.

telegram · zaihuapd · Nov 23, 12:49

**「Background」** The Riemann Hypothesis is one of the Clay Mathematics Institute&\#x27;s Millennium Prize Problems, open since 1859. Lean is a proof assistant whose Mathlib library lets mathematicians formalize arguments as machine-checkable code; on Nov. 21, 2026, the Lean and Mathlib communities certified Levent Alpöge&\#x27;s Claude-assisted Lean proof as correct, with verifiers checking 17 million lines of code. Wang cites that certification as evidence that the gap between AI and top human mathematicians has narrowed to specific knowledge, engineering integration, and experimentation, though the proof still has no human-readable version.

**「Impact」** Wang&\#x27;s warning is aimed at the AI-safety and alignment community, but the concrete case he cites carries an unresolved verification gap: a machine-checked Lean proof without a human-readable exposition means researchers outside the small group that ran the check cannot yet assess what was proved or how much of the work Claude performed. Until a human-readable version and independent review appear, the claim should be treated as a vendor-adjacent assertion rather than a confirmed mathematical result.

<details><summary>References</summary>
<ul>
<li><a href="https://effectstory.com/en/articles/lean-communities-certify-claude-assisted-riemann-hypothesis-proof">Alpöge claims a Claude-assisted Riemann hypothesis proof ...</a></li>
<li><a href="https://the-decoder.com/lean-and-mathlib-community-officially-confirms-levent-alpoges-proof-of-the-riemann-hypothesis-is-correct/">Lean and Mathlib community officially confirms Levent Alpöge ...</a></li>
<li><a href="https://www.datastudios.org/post/claude-riemann-hypothesis-proof-lean-community-certifies-levent-alpoge">Claude-assisted Riemann hypothesis proof certified by Lean ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#superintelligence`, `#AI research`, `#alignment`, `#Meta`

---

<a id="item-tech-news-7"></a>
### [NVIDIA Board Reinstates Jensen Huang as President and CEO](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director) ⭐️ 8.0/10

NVIDIA&\#x27;s board voted unanimously to immediately reinstate Jensen Huang as president, CEO, and board director, with chairman Harvey Jones saying the board has &quot;full confidence&quot; in his leadership. Colette Kress, who had served as interim CEO, returns to her role as chief financial officer. The board said that after receiving input from senior levels of the U.S. government, it concluded Huang&\#x27;s reinstatement poses no national security risk; it has formed an independent-director investigation committee into reports that Huang was a target of foreign intelligence activity, and established a national security and export-control committee while beginning a search for a chief compliance officer. The announcement comes from NVIDIA&\#x27;s newsroom as relayed in a Telegram summary, and the source provides no independent verification of the underlying events.

telegram · zaihuapd · Nov 23, 14:02

**「What led to the reinstatement」** NVIDIA&\#x27;s board removed Jensen Huang from his roles in early November 2026 amid an investigation into whether foreign intelligence efforts had targeted him, with CFO Colette Kress serving as interim CEO. The board now says it received input from senior U.S. government officials before concluding that Huang&\#x27;s return poses no national security risk, and it is keeping an independent-director committee on the investigation while adding a national security and export-control committee and recruiting a chief compliance officer.

**「Continued scrutiny and new compliance roles」** The reinstatement does not resolve the governance questions: Senator Tom Cotton, chair of the Senate Intelligence Committee, said Congress had &quot;much to investigate&quot; regarding Nvidia and Chinese chip smuggling, so export-control scrutiny is likely to continue. The board has also established a national-security and export-control committee and opened a search for a chief compliance officer, meaning Nvidia must staff and operationalize new oversight while the independent-director investigation into Huang proceeds.

**「Community Discussion」** Hacker News commenters focused on the board&\#x27;s statement that it received input from senior U.S. government officials, with one calling that the &quot;most operative part&quot; of the announcement. Others questioned the unanimous reversal after Huang was reportedly forced out less than two weeks earlier, and one commenter argued the board handled communications poorly—either it should have explained its evidence more clearly or hedged by announcing an internal investigation first.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/technology/nvidia-reinstates-jensen-huang-ceo-2026-11-23/">Huang returns as Nvidia CEO after Trump intervention in ...</a></li>
<li><a href="https://www.nytimes.com/2026/11/08/technology/nvidia-investigation-jensen-huang.html">What to Know About Nvidia’s Investigation of CEO Jensen Huang ...</a></li>
<li><a href="https://www.cfr.org/articles/nvidia-chinese-espionage-and-the-ai-race-four-foreign-policy-issues-to-watch">Jensen Huang Resigns From Nvidia: Policy Issues Central to ...</a></li>
<li><a href="https://www.nytimes.com/live/2026/11/23/technology/nvidia-jensen-huang-reinstated">Nvidia Live Updates: Jensen Huang’s Reinstatement as CEO Sparks...</a></li>
<li><a href="https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html">Jensen Huang reinstated as Nvidia CEO. Stock skyrockets 31%</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#corporate-governance`, `#AI-hardware`, `#export-controls`, `#semiconductor-industry`

---

<a id="item-tech-news-8"></a>
### [LeCun accuses Amodei of hyping risk to suppress open models](https://twitter.com/ylecun/status/2124550037912920090) ⭐️ 7.0/10

In a post on X, Yann LeCun claimed that Dario Amodei has been hyping AI dangers since GPT-2 so that open models would be made illegal and Amodei would retain control. The Hacker News thread treated the allegation as a claim rather than a verified fact, and the supplied source reports no specific policy proposal, version, or measured effect behind it.

hackernews · MrBuddyCasino · Nov 23, 17:07 · [Discussion](https://news.ycombinator.com/item?id=50615308)

**「Open-vs-Closed AI and Regulatory Capture」** Yann LeCun accused Anthropic CEO Dario Amodei of using safety warnings and capability-focused regulation to shield closed AI labs from open-weight competition, framing the dispute as regulatory capture rather than genuine risk concern. The two have clashed over open-versus-closed model policy before, and this exchange continues that argument. The Hacker News thread picks up LeCun&\#x27;s claim and discusses possible mechanisms for restricting open models, such as hardware limits and private-compute registration.

**「Impact」** The concrete consequence raised for open-weight users is that restrictions could migrate from model weights to the hardware used to run them: community commenters describe floated ideas such as microcode updates limiting consumer GPUs or registration requirements for privately owned compute. Those are proposals discussed by people in the regulatory space, not enacted rules, and the source provides no policy text or confirmation that any such measure is being drafted. External reporting confirms that export controls already attach to GPU capability and destination, with the January 2025 AI Diffusion rule extending restrictions to certain GPU exports and related AI use—the regulatory channel through which hardware-level limits would most plausibly operate.

**「Community discussion」** One commenter who said they work with people in the AI regulatory space reported an emerging consensus that if you can&\#x27;t ban the bullets, you ban the guns, with floated ideas including microcode updates limiting consumer GPUs&\#x27; LLM capabilities and registration for privately owned compute. Other commenters argued open models are necessary for defense, citing the HuggingFace incident, and accused closed-model companies of appropriating open knowledge and then lobbying to prevent others from doing the same.

<details><summary>References</summary>
<ul>
<li><a href="https://officechai.com/ai/dario-amodei-hypes-ai-dangers-so-that-open-models-are-made-illegal-and-he-can-stay-in-control-yann-lecun/">Dario Amodei Hypes AI Dangers So That Open Models Are Made ...</a></li>
<li><a href="https://asksurf.ai/pulse/en/lecun-accuses-amodei-of-regulatory-capture-open-vs-closed-ai">LeCun Accuses Amodei of Regulatory Capture in the Open-vs ...</a></li>
<li><a href="https://www.timesnownews.com/technology-science/ai-godfather-yann-lecun-attacks-anthropic-ceo-dario-amodei-says-he-wants-to-control-ai-article-156555505">AI Godfather Yann LeCun Attacks Anthropic CEO Dario Amodei ...</a></li>
<li><a href="https://introl.com/blog/ai-export-controls-navigating-chip-restrictions-globally-2025">AI Export Controls: Navigating Chip Restrictions Globally</a></li>
<li><a href="https://www.gtlaw.com/en/-/media/files/insights/alerts/2025/12/gt-advisory_navigating-gpu-export-controls-and-ai-use-restrictions-in-data-center-operations.pdf">GT Alert_Navigating GPU Export Controls and AI Use ...</a></li>

</ul>
</details>

**Tags**: `#ai-policy`, `#open-weight-models`, `#regulatory-capture`, `#ai-safety-debate`, `#hardware-regulation`

---

<a id="item-tech-news-9"></a>
### [Spelunkr.tv Curates Internet Archive Videos Into Free Linear TV Channels](https://spelunkr.tv/) ⭐️ 7.0/10

Spelunkr.tv presents a free, linear &quot;TV network&quot; that curates obscure Internet Archive videos into scheduled channels. Commenters on Hacker News say it streams directly from the Internet Archive rather than hosting its own copies. The project drew 921 points and 159 comments, with users describing watching era-specific music programming and commercials. No source content was supplied, so the exact channel lineup, scheduling mechanics, and whether the code is open source could not be verified.

hackernews · SockThief · Nov 23, 01:13 · [Discussion](https://news.ycombinator.com/item?id=50606192)

**「Context」** I can&\#x27;t write a grounded background because the item provides no source content beyond its analysis summary and comments. The tool results describe Spelunkr.tv itself as 24/7 synchronized channels of Internet Archive video, and FieldStation 42 as an open-source scheduled-broadcast simulator for Raspberry Pi and Linux; neither establishes a earlier Horizon-reported development or a documented predecessor that this item changes.

**「Impact」** The project offers a working example of an always-on, scheduled alternative to on-demand streaming built on Internet Archive material; commenter Woodrow503 reports achieving a similar setup with the open-source FieldStation42 on a Raspberry Pi 5, combining archive and personal media with commercials from YouTube and the Internet Archive.

**「Community Discussion」** Commenters praised the nostalgia of scheduled, era-specific programming, with goatherders describing 45 minutes of 1987 Headbangers Ball and gabriel666smith saying linear viewing eases the loneliness of asynchronous on-demand streaming. andsoitis questioned whether the Internet Archive objects to a third-party interface that bypasses its own user experience.

<details><summary>References</summary>
<ul>
<li><a href="https://spelunkr.tv/">SPELUNKR — Cable TV , but weirder</a></li>
<li><a href="https://www.itechguides.com/fieldstation42-the-golden-age-of-90s-cable-brought-to-you-by-a-raspberry-pi/">FieldStation 42 : 90s Cable TV Simulator on Raspberry Pi</a></li>

</ul>
</details>

**Tags**: `#Internet Archive`, `#streaming media`, `#media preservation`, `#retro TV`, `#DIY/open source`

---

<a id="item-tech-news-10"></a>
### [Open-source nospeaker makes MacBook trackpad vibrate out speech](https://m.mydrivers.com/newsview/1167826.html?ref=https%3A//www.google.com/) ⭐️ 7.0/10

Developer Cody Collier has open-sourced nospeaker, a tool that uses the haptic motor under a MacBook Force Touch trackpad to speak text aloud by driving it at up to 4,000 times per second, fast enough that the glass&\#x27;s vibration becomes audible. It feeds text through macOS speech synthesis, samples two formants every 10 ms, and replays them along with loudness and pitch, producing a robotic-sounding voice. The author reports audible output from 100 Hz to 4 kHz, clearest around 1 kHz, and says it has only been validated on one M5 Max MacBook Pro. The tool speaks text only — not music or video — and bypasses Apple&\#x27;s public haptics APIs by calling the private MultitouchSupport framework.

telegram · zaihuapd · Nov 23, 07:16

**「Background」** Apple&\#x27;s Force Touch trackpads use a linear resonant actuator to simulate clicks through vibration rather than a physical button, and Apple exposes haptics to developers through public APIs intended for feedback patterns, not audio playback. nospeaker instead drives the actuator far above its normal feedback range and relies on formant synthesis, the technique of reconstructing speech from resonant frequency peaks, to turn those vibrations into intelligible words.

**「Impact」** Anyone trying the tool needs Force Touch hardware and should expect it to break, since it depends on an undocumented private framework rather than a supported API; the author&\#x27;s single validated machine also means results on other MacBook models are unconfirmed. Its scope is limited to speech, so it is an experiment in repurposing haptic hardware rather than a replacement for speakers.

**Tags**: `#haptics`, `#open-source`, `#macOS`, `#speech-synthesis`, `#hardware-hacking`

---

## Global Chips

<a id="item-chip-news-1"></a>
### [星思半导体获证监会备案，拟赴港交所IPO](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2fwww.eet-china.com%2fmp%2fa541211.html&amp;c=7886811501635680782&amp;mkt=en-us) ⭐️ 7.0/10

星思半导体已获中国证监会国际合作司境外上市备案，计划在香港联合交易所发行不超过3.88亿股境外上市普通股。备案通知书同时显示，公司76名股东拟将所持合计28.23亿股境内未上市股份转为境外上市股份，并在港交所上市流通。这是监管备案环节的进展，尚非完成发行或挂牌。星思半导体主营卫星通信芯片，属国产芯片设计企业。

rss · Bing News - China domestic chips · Nov 23, 04:42

**「背景」** 中国境内企业赴境外上市须先取得证监会国际合作司出具的备案通知书，之后才能推进港交所的发行与上市程序，此次披露的正是星思半导体在这一环节的结果。备案文件同时列明新股发行上限与现有股东境内股份转为境外上市股份的安排，表明公司拟以新发H股叠加存量股份流通的方式登陆港股。

**「影响」** 若后续发行与挂牌完成，星思半导体将获得境外股权融资渠道，其76名股东所持28.23亿股境内股份也可在港交所流通，为这家卫星通信芯片设计公司提供研发资金并给股东增加退出路径。目前仅完成证监会备案，3.88亿股的发行上限、最终定价与时间表仍取决于港交所审核及市场情况。

**Tags**: `#国产芯片`, `#卫星通信芯片`, `#港股IPO`, `#资本市场`

---

<a id="item-chip-news-2"></a>
### [US Intelligence Chief Says China Likely Has Nvidia Advanced AI Chips](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fwww.yahoo.com%2fnews%2fvideos%2fchina-likely-nvidia-advanced-ai-124615337.html&amp;c=892859684981909522&amp;mkt=en-us) ⭐️ 6.0/10

US Director of National Intelligence Jay Clayton told CNN&\#x27;s Dana Bash that he expects China has found ways to obtain Nvidia&\#x27;s advanced AI chips. He did not specify which chip models, quantities, intermediaries or channels were involved, and gave no timeline. The statement is an unconfirmed public assessment rather than a documented shipment, enforcement action or change to export-control rules; it does not identify any licensed, permitted or prohibited transaction, and no Nvidia or Chinese government response was reported. The account therefore leaves open whether the concern covers chips restricted under current US controls or older, still-legal parts.

rss · Bing News - NVIDIA and China · Nov 23, 04:46

**「Context」** The remark came during a CNN interview in which Jay Clayton was also asked about Nvidia and about ongoing investigations of Megaspeed and China, according to published accounts of the Sunday programme. The statement is a general intelligence assessment rather than an enforcement finding: no models, quantities, buyers or diversion channels were disclosed, so it does not establish what Nvidia hardware China holds or how it was obtained.

**「Export-control effect」** The DNI&\#x27;s remark implies that current US export controls have not stopped Nvidia&\#x27;s advanced AI chips from reaching China, but he gave no details on quantities, chip models or distribution channels, so the practical scale of any leakage remains unquantified. The remark coincides with Taiwan&\#x27;s move to criminalize unauthorized exports of advanced AI chips to China, aimed at closing a loophole exposed when Nvidia-powered servers bought on the island reached Chinese buyers via Indonesia, Japan and Hong Kong, according to an Asia Times report cited alongside the DNI statement.

<details><summary>References</summary>
<ul>
<li><a href="https://theconservativetreehouse.com/blog/2026/11/22/sunday-talks-odni-jay-clayton-discusses-cyber-security-with-dana-bash/">Sunday Talks - ODNI Jay Clayton Discusses Cyber Security with...</a></li>
<li><a href="https://asiatimes.com/2026/11/taiwan-to-criminalize-nvidia-ai-chip-smuggling-to-china/">Taiwan to criminalize Nvidia AI chip smuggling to China - Asia Times</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-3"></a>
### [LCY in advanced talks to sell control of China chip chemicals unit to HSG-led group for about $600M](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d80574ffbb852e6d42a9ae36c&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fother%2flcy-s-china-chip-chemicals-business-draws-600m-takeover-interest-from-hsg-led-consortium-report%2far-AA2i2RcN&amp;c=1322568966284489748&amp;mkt=en-us) ⭐️ 6.0/10

Taiwan-based LCY Group is reportedly in advanced talks to sell control of its China semiconductor chemicals business to a consortium led by HSG, in a deal valued at around $600 million, according to a report relayed by Bing News. The item is report-based: the supplied material does not confirm that a definitive agreement has been signed, that terms were disclosed by either party, or that a closing timetable exists. The asset in question is semiconductor chemicals — a materials-supply operation within China&\#x27;s chip supply chain — rather than AI compute, NVIDIA products or advanced-node equipment. The reported change concerns ownership of China-based chip-materials capacity, not any adjustment to what is permitted, restricted or shipped under export-control rules.

rss · Bing News - China chip policy · Nov 23, 03:50

**「Background」** LCY Group is a Taiwan-based chemicals producer whose China unit supplies semiconductor-grade chemicals; the reported transaction would transfer control at roughly 4 billion yuan \($600 million\), a valuation one report pegs at more than 20 times the unit&\#x27;s core earnings, with LCY seeking to remain the largest single shareholder. The talks remain report-based: no agreement, signing or regulatory clearance has been disclosed, so this is a deal under negotiation rather than a completed sale.

**「Impact」** If completed, the transaction would transfer control of an existing China-based semiconductor chemicals operation from a Taiwanese owner to an HSG-led investment consortium, shifting who directs that materials capacity rather than adding new capacity; the report gives no closing date or regulatory approval step, so the timing and completion of any ownership change remain unconfirmed.

<details><summary>References</summary>
<ul>
<li>HSG-led consortium in talks to buy controlling stake in LCY&#x27;s China chip chemicals business</li>
<li>LCY Group Nears $600M Sale of Semiconductor Chemicals Unit Amid - GuruFocus</li>

</ul>
</details>

**Tags**: `#半导体材料`, `#供应链`, `#对华投资`, `#国产芯片`, `#并购`

---

<a id="item-chip-news-4"></a>
### [New U.S. BIS chip export rule takes effect amid China auto-tech concerns](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261124A02O4R00&amp;c=279504482962160428&amp;mkt=en-us) ⭐️ 6.0/10

A new chip export rule issued by the U.S. Bureau of Industry and Security \(BIS\) took effect around the same time as news about NVIDIA CEO Jensen Huang, according to a truncated Chinese-language news item. The report says the rule could significantly affect the automotive industry and China&\#x27;s broader technology sector, and it raises questions about whether Chinese autonomous-driving training and homegrown chip development will be constrained. However, the supplied text is only a teaser: it does not specify the rule&\#x27;s provisions, its exact effective date, which companies or products are covered, or what is permitted or restricted for China. The claim that the rule has material consequences for Chinese auto-tech and domestic chip sectors therefore cannot be verified from the available evidence.

rss · Bing News - China domestic chips · Nov 23, 08:05

**「Preceding export-control rules」** The new BIS rule follows the AI Diffusion Rule issued on January 13, 2025, which introduced a worldwide licence requirement and complex controls on certain advanced computing chips and on model weights for advanced closed-weight AI models, according to Baker McKenzie&\#x27;s sanctions blog \(tool-1-1\). WilmerHale reports that BIS issued an interim final rule on &quot;remote access&quot; to advanced semiconductors — the high-performance processors used to train and run AI models — on November 15, 2026 \(tool-1-3\). Fenwick says the rule came after pressure from Trump administration officials and Congress to address AI-chip diversion and the absence of controls on remote access from Country Group D:5, which includes China \(tool-1-2\). The supplied source itself does not specify what the new rule prohibits or which products it covers.

<details><summary>References</summary>
<ul>
<li><a href="https://sanctionsnews.bakermckenzie.com/bis-restricts-remote-access-to-advanced-ai-chips-and-formally-rescinds-the-ai-diffusion-rule/">BIS Restricts Remote Access to Advanced AI Chips and Formally ...</a></li>
<li><a href="https://www.fenwick.com/insights/publications/bis-announces-new-export-controls-remote-access-ai-chips">BIS Announces New Export Controls on Remote Access, AI Chips</a></li>
<li><a href="https://www.wilmerhale.com/en/insights/client-alerts/20261117-us-government-restricts-remote-access-to-advanced-ai-chips-and-formally-rescinds-the-ai-diffusion-rule">US Government Restricts Remote Access to Advanced AI Chips ...</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#国产芯片`, `#AI 算力`, `#英伟达`

---

<a id="item-chip-news-5"></a>
### [Report alleges Huang associate had China spy agency contact](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fabc7chicago.com%2fstory%2fwoman-center-nvidia-scandal-was-touch-chinas-top-spy-agency-sources%2f20069206%2f&amp;c=17224972434123134999&amp;mkt=en-us) ⭐️ 5.0/10

A report carried by ABC7 Chicago, citing unnamed sources, alleges that the woman described as having had an affair with NVIDIA CEO Jensen Huang was also in contact with an official of China&\#x27;s top intelligence agency, and that the contact took place while she was in a relationship with the former executive. The item does not name the woman or the official, gives no dates, and offers no documentation or on-record confirmation; the allegation is reported as unconfirmed. The account does not identify any change to NVIDIA products, export licensing, or shipments to China.

rss · Bing News - NVIDIA and China · Nov 23, 02:39

**「Earlier resignation and reinstatement」** The scrutiny follows Jensen Huang&\#x27;s earlier departure from the CEO role: a Yahoo News report states he resigned in the wake of the alleged affair, and BBC News reported that Nvidia&\#x27;s board voted unanimously to reinstate him as CEO and president after he stepped down earlier that month. The same Yahoo report says Alice Huang&\#x27;s contact with a Ministry of State Security official ran from spring 2025 into the fall of this year, the period now under scrutiny.

**「Governance scrutiny, no shipment change documented」** The supplied evidence documents no new export-control measure, licence decision or shipment restriction affecting Nvidia&\#x27;s China business; the item is an unconfirmed allegation from unnamed sources. External reports in the same window do indicate continuing U.S. scrutiny of Nvidia&\#x27;s China exposure: California authorities are reportedly investigating whether Nvidia chip exports ended up in China, and the board reinstated Jensen Huang as CEO on November 23 after his November 13 resignation, saying it had input from senior levels of the U.S. government. The practical consequence supported so far is heightened governance and compliance attention on Nvidia&\#x27;s China channels, not a change in what is permitted to ship.

<details><summary>References</summary>
<ul>
<li><a href="https://www.yahoo.com/news/politics/articles/woman-center-nvidia-scandal-touch-061322657.html">Woman at center of Nvidia scandal was in touch with China &#x27;s top spy ...</a></li>
<li><a href="https://www.bbc.com/news/live/crd61y5dwqgpt">Jensen Huang reinstated as Nvidia CEO, board says - BBC News</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/23/jensen-huang-reinstated-as-nvidia-chief-executive">Jensen Huang reinstated as Nvidia CEO | Jensen Huang | The Guardian</a></li>
<li><a href="https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html">Jensen Huang reinstated as Nvidia CEO. Stock skyrockets 31%</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#中美芯片合作`, `#对华出口管制`, `#Jensen Huang`, `#China`

---

<a id="item-chip-news-6"></a>
### [Nvidia Says U.S. Officials Cleared Jensen Huang&\#x27;s Return as No Security Risk](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fgizmodo.com%2fthe-single-most-important-line-from-nvidias-statement-about-jensen-huangs-return-2000844082&amp;c=17956557870182898364&amp;mkt=en-us) ⭐️ 5.0/10

Nvidia said U.S. government officials assured its board that reinstating Jensen Huang posed no national security risk, according to a Gizmodo report carried by Bing News. The statement addresses a governance question rather than any new export-control provision, product launch or China shipment decision. The supplied account does not identify which officials gave the assurance, when it was given, or what role Huang is returning to. No figures on AI compute supply, capacity or China revenue were disclosed.

rss · Bing News - NVIDIA and China · Nov 23, 11:30

**「Background」** The assurance is framed as a board-level clarification, indicating that Huang&\#x27;s return to a leadership position had been treated as a question requiring U.S. government sign-off. The supplied text does not specify the prior arrangement that removed or limited his role, nor the earlier licence or policy decision that prompted the board to seek the assurance.

**「Impact」** The practical effect supported by the evidence is narrow: Nvidia&\#x27;s board now has a stated U.S. government assurance that Huang&\#x27;s reinstatement raises no national security concern, which removes a governance obstacle rather than altering export licensing or China access. Because the source names no officials, date or conditions, it cannot be read as clearance for any specific product shipment to China.

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`

---

<a id="item-chip-news-7"></a>
### [Pakistan, China researchers discuss advanced semiconductor collaboration](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d80574ffbb852e6d42a9ae36c&amp;url=https%3a%2f%2fwww.msn.com%2fen-xl%2fscience%2fgeneral%2fpak-china-researchers-to-cooperate-in-advanced-semiconductor-techpublished-on-november-23-2026-9-04-am%2far-AA2i0Yqi&amp;c=10844837300057430555&amp;mkt=en-us) ⭐️ 5.0/10

Researchers from Pakistan and China explored opportunities for collaboration in advanced semiconductor technologies at an international symposium hosted by Pakistan&\#x27;s National University, according to a November 23 report. The item describes the event as a discussion of possible cooperation; it names no participating institutions beyond the host university, no specific technologies, process nodes, funding or agreements, and no timeline. No joint programme, memorandum or research output was reported as agreed or shipped.

rss · Bing News - China chip policy · Nov 23, 01:34

**「Background」** The symposium is reported as a bilateral academic exchange rather than a government or corporate arrangement, and the supplied source does not identify any prior Pakistan-China semiconductor cooperation agreement that this event follows. Pakistan has no established commercial advanced-node manufacturing base, so the reported talks concern research collaboration rather than fab capacity or production.

**「Impact」** Because the report names no institutions, funding or work plan, the practical effect cannot yet be assessed: no Chinese or Pakistani company gains fab access, licensing or supply capacity from the announced discussions, and any follow-on research cooperation would depend on details not disclosed in the source.

**Tags**: `#中美芯片合作`, `#国产芯片`, `#先进制程`, `#半导体研究`

---

<a id="item-chip-news-8"></a>
### [Report claims two Chinese vendors in top five intelligent-driving chip ranks](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1105159807_121097259&amp;c=4922930732126220630&amp;mkt=en-us) ⭐️ 5.0/10

A Sohu article asserts that domestic Chinese vendors now hold two of the top five positions in intelligent-driving chips, with Huawei reaching fifth, and frames this as evidence of NVIDIA&\#x27;s decline in that segment. The supplied excerpt, however, contains no top-five list, no market-share or shipment figures, no process-node or performance details, and no sourcing for the ranking, so the claimed placements of the two domestic vendors and Huawei&\#x27;s fifth place cannot be verified from the available text. The excerpt only establishes the article&\#x27;s framing: electric-vehicle subsystems divide into a three-electric system \(battery, motor, electronic control\), intelligent-driving systems including chips and algorithms, and smart-cockpit chips and software, with China described as fully self-sufficient in the three-electric category and holding roughly 80% of global battery share, while cockpit and intelligent-driving chips are characterized as a remaining weak point. No company names beyond Huawei, dates, or shipment figures for the claimed ranking shift appear in the supplied content.

rss · Bing News - China domestic chips · Nov 23, 03:54

**「Background」** Horizon&\#x27;s mid-2026 data already showed Nvidia leading China&\#x27;s urban NOA-capable intelligent-driving chip market for own-brand passenger cars with 39.43%, ahead of Horizon Robotics at 22.82%, establishing a two-vendor top tier. The same reporting noted that several automakers, including Li Auto, Xpeng and Xiaomi, were developing in-house intelligent-driving chips, with Li Auto&\#x27;s expected to reach mass production in 2026. The current claim that domestic vendors hold two of the top five spots and that Huawei has reached fifth extends that earlier ranking picture, but the supplied excerpt provides no top-five list, market-share or shipment figures to confirm it.

<details><summary>References</summary>
<ul>
<li><a href="https://bianews.com/news/details?id=197814">市 值逼近Mobileye， 地 平 线 真的迎来曙光</a></li>
<li><a href="https://k.sina.com.cn/article_6347973665_17a5e642102701wg1m.html">英 伟 达 第一，但半年丢了10%！ 地 平 线 坐稳第二，高阶 智 驾 芯 片 双强</a></li>

</ul>
</details>

**Tags**: `#国产芯片`, `#智能驾驶芯片`, `#英伟达`, `#华为`, `#AI 算力`

---

<a id="item-chip-news-9"></a>
### [BIS Nov 16 rule tightens overseas tape-out access, report says](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9e81bd4cfcb0028a3aa417260a&amp;url=https%3a%2f%2f36kr.com%2fnewsflashes%2f4082941578318729&amp;c=13891380597614384693&amp;mkt=en-us) ⭐️ 5.0/10

A Shanghai Securities News report carried by 36Kr said rumours that Samsung had begun penetrating audits of contract manufacturing were inaccurate, citing checks with domestic foundries and chip design companies. The report said the pressure behind the rumours is &quot;abuse of export controls&quot; following a new rule issued by the U.S. Bureau of Industry and Security \(BIS\) on Nov. 16, which industry figures said further tightened access to overseas tape-out. Several industry people said building a domestic AI supply chain is now necessary, and with process technology lagging overseas advanced manufacturers, so-called &quot;super nodes&quot; are expected to offset single-chip compute shortfalls and open a development opportunity window, according to the report.

rss · Bing News - China domestic chips · Nov 23, 09:08

**「Background」** The restriction the report cites is the November 16 rule from the Commerce Department&\#x27;s Bureau of Industry and Security covering advanced hardware for superintelligence and remote access, which CSIS describes as the formal rescission and replacement of the Biden administration&\#x27;s earlier measure. It follows earlier BIS action: a January 15, 2025 package that tightened export controls on advanced computing semiconductors and added entities in China and Singapore to the Entity List. The source cites no specific provisions, product models, process nodes or volumes, so the practical scope of the tightened overseas tape-out channel remains unquantified.

**「Impact」** The reported effect is on where Chinese AI chip designers can tape out: the Nov. 16 BIS rule is described as narrowing overseas foundry channels, which pushes designers toward domestic foundries and toward system-level &quot;super node&quot; designs that pool multiple chips to compensate for weaker per-chip compute. The source does not specify which rule provisions apply, which products are covered, or when any restriction takes effect, so the scope of the tightened access remains unconfirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-enhance-foundry-due-diligence-prevent">www.bis.gov</a></li>
<li><a href="https://www.csis.org/analysis/new-export-controls-remote-access-implications-industry-and-competition-china">New Export Controls on Remote Access: The Implications for ...</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#国产芯片`, `#AI 算力`, `#晶圆代工`, `#供应链`

---

<a id="item-chip-news-10"></a>
### [How Nvidia’s billion-dollar turnaround in China is threatened by Huang’s exit](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b04cf9d947e4b4b82196c997440c34f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fhow-nvidia-s-billion-dollar-turnaround-in-china-is-threatened-by-huang-s-exit%2far-AA2i2R8Z&amp;c=16636505390457349027&amp;mkt=en-us) ⭐️ 4.0/10

A Reuters teaser says Nvidia staged a China comeback with less powerful chips and software after US export bans, but offers no concrete details or figures.

rss · Bing News - NVIDIA and China · Nov 23, 03:38

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-11"></a>
### [SoftBank&\#x27;s Reported $1 Trillion SK Hynix Buyout Bid Called a Non-Starter](https://www.eetimes.com/the-enigma-of-softbanks-1-trillion-sk-hynix-buyout-attempt/) ⭐️ 4.0/10

EE Times published a commentary arguing that SoftBank&\#x27;s reported $1 trillion attempt to buy SK Hynix was a non-starter, without disclosing deal terms, named sources or a transaction date. The piece frames the approach as a reported bid rather than an agreed or completed deal, and uses it to illustrate memory&\#x27;s strategic appeal amid the AI buildup. It offers no verifiable detail on HBM capacity, DRAM output or how such an acquisition would be financed or approved. The $1 trillion figure should therefore be treated as an unverified report, not a transaction that changes supply agreements or capacity plans.

rss · EE Times · Nov 23, 08:30

**「Background」** The story traces to a report by The Information published on Friday, Nov. 20, 2026, which said SoftBank Group CEO Masayoshi Son had recently approached Wall Street institutions about financing a possible trillion-dollar buyout of SK Hynix, the world&\#x27;s second-largest memory chipmaker. Reuters and other outlets relayed that same report on Nov. 21, 2026, describing the move as exploratory financing soundings rather than a filed or agreed transaction. EE Times&\#x27; commentary treats the approach as a non-starter and uses it to argue that memory has become strategically central to the AI buildup.

**「Impact」** Because the item provides no confirmed terms, financing structure or regulatory status, its practical effect on AI compute supply and on SK Hynix&\#x27;s HBM and DRAM shipments is unestablished; readers tracking memory allocation have no evidence here of a change to customer agreements or capacity plans.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eetimes.com/the-enigma-of-softbanks-1-trillion-sk-hynix-buyout-attempt/">The Enigma of SoftBank’s $1 Trillion SK Hynix Buyout Attempt</a></li>
<li><a href="https://www.reuters.com/world/asia-pacific/softbanks-son-explored-1-trillion-buyout-sk-hynix-information-reports-2026-11-21/">SoftBank’s Son explored $1 trillion buyout of SK Hynix, the ...</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/technology/softbanks-son-explored-1-trillion-buyout-of-sk-hynix-the-information/articleshow/136043315.cms">SoftBank&#x27;s Son explored $1 trillion buyout of SK Hynix: The ...</a></li>

</ul>
</details>

**Tags**: `#AI 算力`, `#存储芯片`, `#行业分析`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Skip the DRAM Tier: Running Agentic KV Cache on NVMe](https://vllm.ai/blog/2026-11-23-skip-the-dram-tier) ⭐️ 8.0/10

rss · vLLM Blog · Nov 23, 00:00

**「Background」** Agentic serving resends long prefixes: in AgentX traces the median turn is 142K input tokens, and over 96% of those tokens are prefix the server has already seen. A KV cache hit avoids recomputing that prefix, and the authors measured that raising the hit rate by 1% of prompt tokens was worth about 10% more throughput in their Kimi-K3 runs. Host DRAM is the usual tier behind GPU memory, but Kimi-K3 wrote 2.3–4.6 TB of KV an hour, so a 1.8 TB DRAM pool \(about $76,000\) holds only the last 23–47 minutes of it.

**「Solution」** AMD and Embedded LLM tested whether vLLM&\#x27;s KV pool could run entirely on local NVMe using UMBP, the KV cache pool in AMD&\#x27;s open-source MoRI library, on 16 MI355X GPUs. In back-to-back runs on the same machines, a 1.8 TB NVMe pool stayed within 1% of a 1.8 TB DRAM pool at 48, 70 and 96 concurrent sessions on Kimi-K3, with KV hit rates differing by at most 0.08% of prompt tokens; a repeat on another pair of machines put NVMe ahead by 0.4–0.9%. DRAM only buffered writes \(64 GB, one to two minutes of new KV\) and staged reads \(16 GiB\), under 5% of the pool; at 70 sessions even a 4 MiB write buffer cost nothing, though the authors advise keeping it under heavier load. The explanation is that throughput follows hit rate, and same-size pools that evict the same way keep the same KV: vLLM&\#x27;s asynchronous load finished while requests waited for prefill. On the longer kvlab prompts, capacity rather than medium drove results — a 4.6 TB NVMe pool held 92.7–95.8% hit rate at every load and served 8,813 tok/s per GPU at 70 sessions, against a 52% hit rate for a 1.0 TB DRAM pool. Three levers mattered: 256 MiB rather than the default 4 GiB segment files \(eviction frees space only by deleting whole files\) raised hit rate from 94.45% to 95.65% and throughput 15.6%; reporting GPU prefix hits to the pool added 2.1–3.9% throughput and cut TTFT p99 from 70–77 s to 35–43 s; and checkpointing every 7,168 tokens raised hit rate from 91.4% to 95.6% and throughput 33%. The authors frame cost as DRAM per TB held versus NVMe per TB written: drives rated for Kimi-K3&\#x27;s 83 TB of writes a day hold a day of KV for about $59,000 — the same as a 1.8 TB NVMe pool replaced as it wears out — against $76,000 for the 1.8 TB DRAM pool. The tradeoff is that every computed KV block is written to the drives, and the 1.8 TB test pair would exhaust its rated life in roughly five and a half months at 96 sessions; the cost figures are list-price arithmetic that omit power, rack space and drive servers, and the retention-to-throughput estimate chains two fitted models.

**「Takeaway」** The authors conclude that for agentic KV caches, NVMe can replace the DRAM tier at equal pool size, because capacity and hit rate matter more than the medium, and NVMe&\#x27;s cost scales with writes rather than held bytes, buying far more retention per dollar. The open questions are write endurance and the fitted estimates behind the cost and throughput projections.

**Tags**: `#KV cache`, `#NVMe`, `#vLLM`, `#agentic serving`, `#memory tiering`

---

<a id="item-tech-blog-2"></a>
### [Flailing as a Strategy Under Uncertainty](https://seangoedecke.com/when-in-doubt-flail-about/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 23, 00:00

**「Background」** Engineers often face situations with no clear guidance: a product without market fit, a system too tangled or large to fully understand, or an organizational problem nobody can articulate. Sean Goedecke argues that the cautious instinct to wait and study first is usually wrong, because modern systems and products change too fast for exhaustive upfront analysis.

**「Solution」** Goedecke&\#x27;s alternative is deliberate, feedback-sensitive experimentation — &quot;flailing.&quot; The method has three parts: try many different things to get direct contact with reality, watch feedback from both people and metrics very carefully, and ruthlessly drop anything that isn&\#x27;t getting positive feedback. Trying many plans also prevents over-investment; with ten plans, you only need one to succeed, so abandoning failing ones is easy. He identifies three contexts. In product work, most features will fail, but one lucky experiment can be the seed of something lasting — as with a GitHub Models integration that let AI inference run from a GitHub Actions token, which proved surprisingly sticky and fed into &quot;Continuous AI.&quot; In engineering, rather than carefully reading an entire complex system before recommending changes, he suggests making speculative changes, dropping them immediately if they don&\#x27;t improve things, and digging in only when they do; AI agents make generating several candidate refactors cheap. In organizational work, senior engineers should try many plausible interventions — automating manual work, volunteering for tasks, proposing long-term plans — because most won&\#x27;t help, but showing effort builds trust. This third case demands the most feedback sensitivity: dropping a failing plan quickly builds trust, while pressing on redirects people&\#x27;s frustration onto you. The catch is that flailing feels like failing from the inside, even when it looks proactive from outside, so the author says that discomfort must be recognized as a normal signal rather than a warning.

**「Takeaway」** Goedecke&\#x27;s thesis is that under genuine uncertainty, cheap experiments judged by fast feedback beat careful upfront analysis — and that the uncomfortable feeling of flailing is itself a sign you&\#x27;re doing the right thing, provided you stay responsive and abandon failing plans.

**Tags**: `#engineering management`, `#experimentation`, `#handling uncertainty`, `#product development`, `#organizational dynamics`

---

<a id="item-tech-blog-3"></a>
### [What OpenAI&\#x27;s Perplexity Graph Reveals About Training](https://seangoedecke.com/notes-on-openais-perplexity-reveal/) ⭐️ 5.0/10

rss · Sean Goedecke · Nov 23, 00:00

**「Background」** Sean Goedecke reacts to OpenAI&\#x27;s release of a perplexity-over-time graph for all its released models, which he calls the most visibility anyone has had into a frontier lab&\#x27;s internal training metrics. Perplexity measures how well a model predicts held-out text, making it a pre-training metric rather than a measure of RL or post-training success.

**「Solution」** Goedecke stresses that perplexity is dataset-dependent, so even an Anthropic graph on the same axes would not be directly comparable. He notes that for frontier models, rumor puts pre-training at half or less of total training time and compute, with the rest going to RL that perplexity cannot capture. Even granting that pre-training creates capabilities while RL elicits them, he argues other measures such as chain-of-thought improvement need not correlate with perplexity. The chart&\#x27;s surprise, to him, is how few models share a base: rather than 4o and 4.1 being post-trained into many releases, it looks like only o1 and o3 did, and 4.1 and o3 share a base despite o3 being the stronger model. He reads GPT-4.5 as a point where OpenAI briefly stopped making large pretrained models, though he cannot tell whether that was a choice or an internal scaling wall. A real acceleration in perplexity loss from GPT-5.2 onward, he says, contradicts common wisdom that labs have largely abandoned pre-training for RL. On alignment, he doubts transparency alone helps: only OpenAI could notice a sudden scary drop, and threshold agreements would require releasing the held-out dataset. He also notes mismatch between the curve and felt model strength—a big GPT-3.5-to-GPT-4 jump, stagnation until GPT-5.5, then acceleration—whereas his own big jumps were o3 and GPT-5.3-Codex, possibly due to RL on chain-of-thought and sycophancy.

**「Takeaway」** Goedecke&\#x27;s conclusion is that OpenAI&\#x27;s perplexity release is genuinely informative about pre-training progress and post-training lineage, but it is a narrow metric that says little about RL-driven capability or alignment risk, and its value depends on publishing the underlying dataset and unreleased-model numbers.

**Tags**: `#perplexity`, `#LLM pre-training`, `#RL post-training`, `#AI safety transparency`

---

## Financial News

<a id="item-finance-news-1"></a>
### [上海地铁21年来首次调整票价](https://weibo.com/1699432410/5368461393397183) ⭐️ 8.0/10

上海轨道交通将于12月1日实施21年来首次票价调整，起乘价3元、起乘间距0-4公里；同步推出四档计次票，11月26日开售，同一支付渠道当月累计满90元后享9折。

telegram · zaihuapd · Nov 23, 10:45

**「Background」** Shanghai&\#x27;s metro fares had gone unchanged for 21 years before this adjustment, so the new 3 yuan starting fare covers the first 0–4 km, with 1 yuan added for each subsequent 4, 4, 4, 7, 7, 10 and 10 km, then every 15 km beyond 50 km.

**「Who is affected」** Commuters making longer trips face higher fares, because the 3-yuan starting fare now covers 0–4 km instead of 0–6 km; the bundled multi-ride tickets and the 10% discount after 90 yuan in a month are intended to limit the cost increase for frequent riders.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bjnews.com.cn/detail/1795425220129482.html">上 海 调 整 地 铁 票 价 — 新京报</a></li>

</ul>
</details>

**Tags**: `#公共交通定价`, `#上海地铁`, `#票价调整`, `#通勤成本`, `#计次票优惠`

---

<a id="item-finance-news-2"></a>
### [蚂蚁集团领投中国具身智能公司 1 亿美元，估值 16 亿美元](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 7.0/10

Simplexity Robotics, a Hangzhou-based embodied-AI/humanoid-robot startup founded in July 2025, raised a $100 million pre-A round led by Ant Group at a $1.6 billion post-money valuation, with existing investors Alibaba, Tencent, HongShan, and BlueRun Ventures participating.

telegram · zaihuapd · Nov 23, 02:02

**Tags**: `#venture financing`, `#humanoid robotics`, `#Ant Group`, `#China tech`, `#embodied AI`

---

<a id="item-finance-news-3"></a>
### [Bloomberg：英伟达董事会据称未经咨询高管层便恢复黄仁勋CEO职务](https://www.bloomberg.com/news/articles/2026-11-23/nvidia-s-about-face-on-huang-made-without-consulting-leadership) ⭐️ 7.0/10

据Bloomberg报道，英伟达董事会于11月22日周日下午决定让被免职的首席执行官Jensen Huang（黄仁勋）复职，高管层直到最后一刻才获知，且未参与咨询。报道称此举源于美国总统特朗普向董事会成员施压；相关说法均来自匿名知情人士，英伟达未予确认，也未经独立验证。

telegram · zaihuapd · Nov 23, 17:59

**「Background」** Jensen Huang had been removed as Nvidia&\#x27;s CEO less than two weeks before the board reinstated him on Nov. 22, according to Bloomberg, which reported that the reversal followed several meetings and input from the U.S. government.

<details><summary>References</summary>
<ul>
<li>Nvidia Rehires Huang in Stunning Reversal After Trump Push - Bloomberg.com</li>
<li>With the backing of President Donald Trump, Nvidia has reinstated Jensen Huang as CEO, less than two weeks after he was ousted due to scandals surrounding his alleged extramarital</li>

</ul>
</details>

**Tags**: `#Nvidia`, `#corporate governance`, `#CEO succession`, `#political pressure`, `#semiconductors`

---