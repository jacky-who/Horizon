---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 54 items, 34 important content pieces were selected

---

**Technology News**
1. [Shortened Lean Formalization of GRH Proof Cuts to Tens of Thousands of Lines](#item-tech-news-1) ⭐️ 8.0/10
2. [Scott Aaronson points to claim that matrix multiplication exponent is 9/4](#item-tech-news-2) ⭐️ 8.0/10
3. [Google Research posts papers on factoring and discrete logs](#item-tech-news-3) ⭐️ 8.0/10
4. [Essay: conscientious developers should use AI coding tools](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI says cybersecurity could outgrow coding as a business](#item-tech-news-5) ⭐️ 8.0/10
6. [Tencent open-sources GGUF quantized weights for 224B Hy4 flash model](#item-tech-news-6) ⭐️ 8.0/10
7. [Minecraft Java RCE via crafted fonts remains unpatched](#item-tech-news-7) ⭐️ 8.0/10
8. [Samsung and SK hynix reportedly to adopt YMTC Xtacking NAND stacking](#item-tech-news-8) ⭐️ 8.0/10
9. [1Password Discloses Malicious Backend Code Push](#item-tech-news-9) ⭐️ 7.0/10
10. [Windows loudness limiter reverse-engineered and ported to PipeWire](#item-tech-news-10) ⭐️ 7.0/10
11. [Clojure Core Audited with Lean; Some Bug Reports Contested](#item-tech-news-11) ⭐️ 7.0/10
12. [Browser gallery revives old Nvidia and ATI GPU tech demos](#item-tech-news-12) ⭐️ 7.0/10
13. [SemiAnalysis launches GDPx benchmark for frontier models](#item-tech-news-13) ⭐️ 7.0/10
14. [LeCun Accuses Amodei of Using AI-Risk Rhetoric to Restrict Open Models](#item-tech-news-14) ⭐️ 7.0/10
15. [SpaceX to forgo $738M in BEAD subsidies, offer free Starlink terminals](#item-tech-news-15) ⭐️ 7.0/10

**Global Chips**
1. [Congress push for new China chip curbs gains steam amid Huang&\#x27;s Nvidia return](#item-chip-news-1) ⭐️ 8.0/10
2. [NVIDIA GPU sellers seek new buyers as U.S. tightens remote AI chip access for China](#item-chip-news-2) ⭐️ 7.0/10
3. [U.S.-based firms helping China access Nvidia&\#x27;s most advanced chips](#item-chip-news-3) ⭐️ 7.0/10
4. [Nvidia GPU sellers seek new buyers after U.S. tightens China AI chip remote access](#item-chip-news-4) ⭐️ 7.0/10
5. [华为与行芯发布“韬EDA”工具进展，面向下一代手机与服务器芯片](#item-chip-news-5) ⭐️ 7.0/10
6. [Top Nvidia chips still sold on Shenzhen black market despite U.S. ban](#item-chip-news-6) ⭐️ 6.0/10
7. [Reuters probe examines how NVIDIA AI chips reached China via Megaspeed](#item-chip-news-7) ⭐️ 6.0/10
8. [Reuters: Trump&\#x27;s intervention to keep Jensen Huang at Nvidia intensifies Washington chip fight](#item-chip-news-8) ⭐️ 5.0/10
9. [Trump Backing of NVIDIA&\#x27;s Huang Deals China Hawks a Setback](#item-chip-news-9) ⭐️ 5.0/10
10. [AMD MEXT Moves Cold Memory Pages to Flash to Cut DRAM Costs](#item-chip-news-10) ⭐️ 5.0/10
11. [Explainer on how China accesses Nvidia AI chips despite US export curbs](#item-chip-news-11) ⭐️ 4.0/10
12. [Hindu BusinessLine previews piece on Nvidia chips reaching China](#item-chip-news-12) ⭐️ 4.0/10
13. [Chinese Chip Stocks Diverge as MOFCOM Move Read as Trade Thaw](#item-chip-news-13) ⭐️ 4.0/10
14. [DeepSeek V4.1 Pro被指12月发布：摆脱NVIDIA、拥抱国产AI芯片倒计时](#item-chip-news-14) ⭐️ 4.0/10
15. [AI Startup Harmonic Expands Into Formal Verification](#item-chip-news-15) ⭐️ 4.0/10
16. [Winbond Promotes Certified NOR Flash for Edge AI Memory](#item-chip-news-16) ⭐️ 4.0/10

**Financial News**
1. [U.S. Commerce Department reportedly threatened Intel over 10% stake demand](#item-finance-news-1) ⭐️ 9.0/10
2. [SpaceX 与特斯拉拟商谈 3.5 万亿美元全股票合并](#item-finance-news-2) ⭐️ 8.0/10
3. [美国拟对14个贸易伙伴加征第301条新关税](#item-finance-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Shortened Lean Formalization of GRH Proof Cuts to Tens of Thousands of Lines](https://github.com/lsernau/grh-lean) ⭐️ 8.0/10

A repository by lsernau hosts a much shorter Lean formalization of the GRH proof, which commenters say shrinks the verification from roughly 17 million lines to about 76,000 lines. The shortened version reportedly includes a clear split between &quot;known math&quot; and &quot;new math&quot; along with human-readable documentation throughout, making the proof easier to digest. The repository states the proof relies only on the axioms propext, Classical.choice and Quot.sound, though the item provides no independent confirmation of the line counts or the formalization&\#x27;s completeness. Discussion centers on what the reduction means for proof readability and AI-assisted mathematics rather than on a verified release announcement.

hackernews · nb-t · Nov 25, 21:48 · [Discussion](https://news.ycombinator.com/item?id=50648050)

**「Background」** The Generalized Riemann Hypothesis extends the Riemann Hypothesis from the classical zeta function to a much broader class of Dirichlet L-functions and remains a central open problem in mathematics. A Lean formalization makes such a proof machine-checkable, but the earlier version was reportedly enormous: Luke Sernau at Anthropic is credited with reducing it from roughly 15 million lines to about 300,000 lines in a readable version and 76,000 in a compact version. The new repository is described as a short Lean 4 proof of GRH, with human-readable documentation and a clear split between &quot;known math&quot; and &quot;new math.&quot;

**「Impact」** The shortened Lean formalization reduces the GRH proof to roughly 76k lines, making it practical for mathematicians and tooling to inspect and audit, whereas the multi-million-line version was effectively opaque to manual review. Downstream users still need to confirm compatibility with the Lean and Mathlib setup; commenters note the proof relies on the axioms propext, Classical.choice, and Quot.sound, so the size reduction alone does not settle questions about proof insight.

**「Community Discussion」** Commenters highlighted the readability improvements, with spootydooty noting the 300kloc proof&\#x27;s known-math versus new-math split and documentation, while bananaflag cited a drop from about 17 million to 76,000 lines, a 99.56% reduction. gre asked whether this undercuts Tao&\#x27;s recent argument that huge proofs without insight are a problem, raising the question of whether smarter LLMs can now golf proofs and explain them, and gus\_massa requested a plain-language explanation of the axiom list for mathematicians who do not use Lean.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lsernau/grh-lean">Much shorter version of GRH Lean verification from Anthropic</a></li>
<li><a href="https://x.com/robinhouston/status/2125720821251596760">Robin Houston on X: &quot;Luke Sernau at Anthropic has reduced the ...</a></li>
<li><a href="https://github.com/lsernau/grh-lean/tree/main/grh">grh-lean/grh at main · lsernau/grh-lean · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alp%C3%B6ge&#x27;s_proof_of_the_Riemann_hypothesis">Alpöge&#x27;s proof of the Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.newscientist.com/article/2583307-why-mathematician-terence-tao-thinks-ai-must-spark-a-rapid-revolution/">Why mathematician Terence Tao thinks AI must spark... | New Scientist</a></li>

</ul>
</details>

**Tags**: `#Lean`, `#formal verification`, `#mathematics`, `#AI-assisted proofs`, `#open source`

---

<a id="item-tech-news-2"></a>
### [Scott Aaronson points to claim that matrix multiplication exponent is 9/4](https://scottaaronson.blog/?p=10379) ⭐️ 8.0/10

A Hacker News thread surfaced a pointer from Scott Aaronson&\#x27;s blog to a paper titled “The matrix multiplication exponent is nine fourths.” The linked discussion drew 813 points and 671 comments, far more attention than the sparse supplied source material can substantiate: the item itself contains only the see-also link and no technical claims, proof details, authorship, venue, or verification status. Commenters treated the claim as a significant mathematical development and debated its connection to Lean/MathLib, LLMs, and subsidized compute, but no element of the claimed result has been independently confirmed in the supplied material.

hackernews · Kotlopou · Nov 25, 19:11 · [Discussion](https://news.ycombinator.com/item?id=50646108)

**「Background」** The matrix multiplication exponent, conventionally denoted omega, describes the asymptotic cost of multiplying large matrices; the naive algorithm runs in O\(n^3\), while Strassen&\#x27;s algorithm lowered the exponent below 3 in 1969 and subsequent work pushed it down further. An assertion that omega equals 9/4 would be a new bound on that exponent, but the supplied item does not state who proved it, what method was used, or whether the paper has been checked.

**「Impact」** If the claimed bound holds up, it would change the theoretical target for fast matrix-multiplication algorithms, though the supplied material provides no evidence about whether the result is peer-reviewed, formally verified, or practical for real implementations. Readers should treat the HN title and blog pointer as a claim to inspect rather than an established improvement.

**「Community Discussion」** Commenters disagreed mainly about causation and significance: utopiah asked how much of the development would have happened with Lean, MathLib, and raw compute but no LLMs, while rufuspollock called it “the end of human mathematics” and gorgoiler compared it to physics being reclassified after quantum mechanics. Those are opinions about the broader trajectory, not evidence about the mathematical result itself.

**Tags**: `#mathematics`, `#matrix multiplication`, `#AI for math`, `#formal verification`, `#research`

---

<a id="item-tech-news-3"></a>
### [Google Research posts papers on factoring and discrete logs](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 8.0/10

Google Research has published a collection of &quot;Cogentic&quot; papers in its public GitHub repository covering integer factorization, discrete logarithms, and related topics. The supplied material is essentially a repository link: no abstracts, methods, benchmarks, or peer-review status are included, so the scale of any result cannot be verified. The problems are foundational to public-key cryptography, which explains the attention the posting drew.

hackernews · rgwohlbold · Nov 25, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50642086)

**「Background」** The repository states that the papers were produced by Cogentic, which a September 2026 arXiv paper describes as a multi-agent harness for automated proof discovery on open research problems. The listed titles address the computational problems underlying much of public-key cryptography: integer factorization and discrete logarithms in finite fields.

**「Community discussion」** Commenters pointed to outside rumors that the papers are &quot;the tip of something bigger,&quot; though the item offers no verification of that claim. Others framed the work as part of a broader pattern of machine-learning systems exploring large mathematical search spaces, drawing an analogy to AlphaGo&\#x27;s 2016 match against Lee Sedol, while one commenter noted the contrast between reported breakthroughs and a declining AI market.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-research/google-research/tree/master/cogentic_research_papers">Google Releases Cogentic Papers on Integer Factorization ...</a></li>
<li><a href="https://arxiv.org/abs/2609.40324">[2609.40324] Cogentic: Multi-Agent Orchestration for ...</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#integer factorization`, `#discrete logarithms`, `#AI for mathematics`, `#Google Research`

---

<a id="item-tech-news-4"></a>
### [Essay: conscientious developers should use AI coding tools](https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools) ⭐️ 8.0/10

An engineering essay published November 19, 2026 on iankduncan.com argues that skilled and conscientious developers should adopt LLM-assisted coding rather than treat AI tools as a shortcut for those who care less. The piece recasts &quot;a model wrote it&quot; as an accountability question in code review, but it presents an argument rather than a measured workflow or tool release. Hacker News commenters pushed back on its central analogy, contending that delegating problem modeling to an LLM differs from earlier moves from assembler to C or C to JavaScript.

hackernews · matthewsinclair · Nov 25, 07:46 · [Discussion](https://news.ycombinator.com/item?id=50639698)

**「Context」** The essay&\#x27;s thesis, as indexed excerpts summarize it, is that LLMs mostly amplify whoever is sitting at the keyboard, with deeply curious and caring engineers multiplying the effect. The Hacker News thread debates whether LLM-assisted coding is comparable to earlier moves to higher-level languages such as assembler-to-C or C-to-JavaScript, with commenters arguing the activity itself differs rather than merely its abstraction level.

**「Impact」** For developers and reviewers, the practical consequence is that verification becomes the load-bearing part of AI-assisted work: teams that accept generated code still need a review process that assigns responsibility to a person, not to the model. The comment thread also notes that LLM speed can favor shippers who skip that verification over those who do it, so review norms and attribution matter as much as tooling choice.

**「Community Discussion」** Several commenters disputed the &quot;just another abstraction&quot; framing, with anothaway arguing that using an LLM is not the same activity as moving from assembler to C or C to JavaScript because the developer is still modeling the problem in code in those transitions. xnorswap argued the post misses that LLM assistance can let developers who skip extra verification out-ship conscientious ones, while notpachet and chrisra focused on the discipline needed to keep one&\#x27;s own understanding from atrophying and on whether &quot;the model wrote it&quot; is a valid excuse in review.

<details><summary>References</summary>
<ul>
<li>Smart People Who Give a Shit Use Tools - Ian Duncan</li>
<li>Engineering - Ian K. Duncan</li>

</ul>
</details>

**Tags**: `#LLM`, `#software engineering`, `#AI coding tools`, `#code review`

---

<a id="item-tech-news-5"></a>
### [OpenAI says cybersecurity could outgrow coding as a business](https://www.theinformation.com/newsletters/ai-agenda/openais-roadmap-making-cyber-bigger-coding-remains-blurry) ⭐️ 8.0/10

OpenAI is positioning cybersecurity as a potential growth engine larger than its coding business. Its CFO said external estimates that the cybersecurity market exceeds $300 billion are still far too low, and President Greg Brockman said cybersecurity will become a bigger business segment for OpenAI than coding. The company has introduced GPT-6 Cyber for security research and expanded its Daybreak trusted-access program, which as of September covered thousands of verified defenders and about 2,000 approved organizations and workspaces, supporting vulnerability discovery, codebase analysis, and binary reverse engineering. The report notes that competition with Anthropic and Google and the path to scaled commercialization remain unclear.

telegram · zaihuapd · Nov 25, 04:51

**「Context: cyber as a second AI market」** OpenAI&\#x27;s coding-focused offerings, notably the Codex line of models and agent tools, have been the company&\#x27;s most visible enterprise push, with usage concentrated among developers. Extending trusted-access security programs turns the same model capabilities—codebase analysis and binary reverse engineering—toward defensive vulnerability discovery, a market the company now frames as larger than coding. The report notes competition with Anthropic and Google and unclear commercialization prospects, so the size claims remain executive assertions rather than verified figures.

**Tags**: `#OpenAI`, `#cybersecurity`, `#AI security`, `#GPT-6 Cyber`, `#business strategy`

---

<a id="item-tech-news-6"></a>
### [Tencent open-sources GGUF quantized weights for 224B Hy4 flash model](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 8.0/10

Tencent Hunyuan has released GGUF quantized weights for its 224B-parameter Hy4 flash model through AngelSlim, its model compression and acceleration toolbox. The original weights are about 410.27GiB; the smallest IQ2-AH build is 125.73GiB, roughly 30% of the original, and Tencent says it can run on a 64 GB Mac mini with the Strata offload framework. Tencent reports 89 tokens/sec at 10K context on a 48 GB VRAM device, and 47 tokens/sec at 32K context with the Q3\_K build on a 128 GB M5 Max. On evaluations including DeepSWE v1.1, the Q3\_K version scored within 0.4 points of the original model, according to the same figures.

telegram · zaihuapd · Nov 25, 09:29

**「Background」** Hy4 flash is Tencent Hunyuan&\#x27;s cost-efficient Hy model, with 220B total parameters—including 64B Engram parameters—and only about 12B active parameters per token, according to the project&\#x27;s GitHub repository. The open weights release was covered alongside claims of a 1M-token context and comparisons with DeepSeek and Claude models, which explains why reduced-size GGUF variants matter for local deployment: the full weight set is far larger than consumer hardware can hold.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-flash">GitHub - Tencent - Hunyuan / Hy 4 - flash · GitHub</a></li>
<li><a href="https://neurohive.io/en/news/tencent-hy4-flash-open-weights/">Hy 4 flash by Tencent : Open Weights, Pricing, Benchmarks</a></li>

</ul>
</details>

**Tags**: `#open-source-models`, `#quantization`, `#local-inference`, `#GGUF`, `#model-compression`

---

<a id="item-tech-news-7"></a>
### [Minecraft Java RCE via crafted fonts remains unpatched](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

A publicly disclosed exploit called minecraft2shell, published November 22, shows that a specially crafted TrueType font delivered through a Minecraft Java server resource pack can trigger a native out-of-bounds write in FreeType 2.14.3 and earlier, leading to arbitrary code execution on a Java Edition 26.3 Windows client. Affected versions are 1.20.5 through 1.21.10 and snapshots 26.1 through 26.4; 1.20.4 and earlier plus Bedrock Edition are reported as unaffected. Mojang still ships lwjgl-freetype 3.4.3 and has released no patch. A community fix, m2sfix 1.0.0, was released November 24 and disables hinting via a Java agent or mod.

telegram · zaihuapd · Nov 25, 12:46

**「Background」** Minecraft Java servers can send resource packs containing custom fonts to connecting clients, and clients render those fonts through lwjgl-freetype, the LWJGL binding for the FreeType font library. That dependency path is why a native font-rendering flaw can affect clients before normal gameplay code runs; the minecraft2shell disclosure traces the issue to an out-of-bounds write in FreeType 2.14.3 and earlier reached through that binding.

**「Impact」** Until an official fix exists, server operators and players should avoid adding resource packs and set the multiplayer server resource-pack setting to &quot;Disabled,&quot; or install the community m2sfix mod; the workaround only turns off font hinting rather than repairing the underlying FreeType dependency.

**Tags**: `#security`, `#vulnerability`, `#minecraft`, `#freetype`, `#open-source`

---

<a id="item-tech-news-8"></a>
### [Samsung and SK hynix reportedly to adopt YMTC Xtacking NAND stacking](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 8.0/10

Samsung Electronics and SK hynix have reportedly agreed, through a cross-licensing deal, to adopt parts of YMTC&\#x27;s Xtacking technology in 3D NAND flash. Xtacking builds the memory array and CMOS control logic on separate wafers and then joins them by wafer bonding, so each part can be manufactured and optimized independently. All three companies declined to comment, leaving the scope and terms of the agreement unconfirmed. An Omdia senior analyst quoted in the report said the approach lets a manufacturer produce the memory array itself while having logic wafers made by a foundry using more advanced processes.

telegram · zaihuapd · Nov 25, 14:33

**「Xtacking&\#x27;s wafer-bonding approach」** Xtacking separates the two halves of a 3D NAND die: the memory-cell array is built on one wafer and the CMOS control logic on another, and the two are then bonded together. Because each wafer can be fabricated and optimized independently, the logic portion can be outsourced to a foundry and produced on a more advanced process node than the array requires.

**「Impact」** If confirmed, the cross-license would let Samsung and SK hynix build NAND arrays and CMOS logic on separate wafers, with the Omdia analyst noting they could outsource logic to foundries running more advanced nodes rather than developing that capability in-house. YMTC would gain licensing revenue and industry standing for Xtacking. Because all three companies declined to comment, the deal&\#x27;s scope, royalty terms, and which product generations would use the technology remain undisclosed.

**Tags**: `#3D NAND`, `#semiconductor manufacturing`, `#hybrid bonding`, `#YMTC`, `#memory industry`

---

<a id="item-tech-news-9"></a>
### [1Password Discloses Malicious Backend Code Push](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 7.0/10

1Password published an update on a November 2026 security incident in which a malicious actor pushed code to its backend services. The post says a small number of users were in an affected state and were specifically notified, but it does not state whether branch protection rules were missing or bypassed, nor does it explicitly say whether encrypted vaults were downloaded, according to commenters reading the announcement. Those unresolved scope questions leave the incident&\#x27;s blast radius unclear beyond the notified users.

hackernews · lxhrstn · Nov 25, 17:18 · [Discussion](https://news.ycombinator.com/item?id=50644817)

**「Background」** 1Password&\#x27;s disclosure states that on November 19, 2026, it began investigating signs that an attacker had gained access to an employee&\#x27;s corporate GitHub account, then used that account to reach source code and push malicious code to backend services. The company says it disabled the account and revoked the stolen token, framing the compromise as an incident affecting backend administrative data rather than encrypted vault contents.

**「Impact」** 1Password says customer vault contents and the keys protecting them were not accessed, so users do not need to rotate vault items on that basis. The reported GitHub-to-CI/CD path and the cited gap between the malicious code push and disclosure point to the operational concern: organizations relying on 1Password should verify the vendor&\#x27;s stated scope of affected records and review who can push to production pipelines and what those pipelines can reach.

**「Community Discussion」** Commenters focused on SaaS supply-chain risk: tptacek called compromise of an employee laptop leading to a GitHub push and deployment &quot;the single most important attack vector for SAAS companies,&quot; while noting 1Password&\#x27;s architecture mitigates its worst-case vault exposure. ctidd and fn-mote criticized disclosure gaps, asking whether push-to-main protections existed or were bypassed and whether encrypted vaults were downloaded; fn-mote said even relatively clear breach statements trigger doubt after years of corporate weasel words.

<details><summary>References</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://www.macrumors.com/2026/11/25/1password-security-breach/">1Password Security Breach: What Was Accessed and What Wasn&#x27;t</a></li>
<li><a href="https://applescoop.org/story/1password-security-incident-november-2026-what-was-exposed-what-to-do">1Password security incident: what was taken and what to do</a></li>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://www.1password.community/announcements-52/update-on-a-security-incident-involving-1password-s-backend-systems-customer-vaults-were-not-affected-and-all-vault-contents-remain-secure-26259">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://www.pk-sharma.com/briefing/1password-nov-2026-security-incident-employee-github-backend-code">1Password GitHub-to-backend breach: 6-day gap and 10-char ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain`, `#SaaS`, `#incident-response`, `#code-deployment`

---

<a id="item-tech-news-10"></a>
### [Windows loudness limiter reverse-engineered and ported to PipeWire](https://github.com/xoxorwr/pw-loudness-eq) ⭐️ 7.0/10

A developer has reverse-engineered Windows&\#x27; shared-mode audio loudness and limiter behavior and ported it to PipeWire in a project called pw-loudness-eq. According to commenter dintech, Windows applies slight compression near peaks when audio plays through loopback shared WASAPI, DirectSound, or MME via audiodg.exe \(CAudioLimiter in AudioEng.dll\), but not through WASAPI exclusive or ASIO, altering peaks by roughly -0.1 dB. The project name has drawn criticism because the processing described is loudness normalization plus limiting rather than frequency-dependent equalization. No source content was supplied, so implementation details and availability are not independently confirmed.

hackernews · ThrowNotAway · Nov 25, 11:34 · [Discussion](https://news.ycombinator.com/item?id=50641171)

**「Background」** Windows&\#x27; shared-mode audio path applies a loudness leveling DSP and a slight peak limiter when audio plays through loopback shared WASAPI, DirectSound, or MME; WASAPI exclusive and ASIO bypass it. According to the project&\#x27;s documentation, pw-loudness-eq reverse-engineers that DSP from WMALFXGFXDSP.dll and the output limiter from AudioEng.dll, then sets \`audioconvert.filter-graph.90\` on each application&\#x27;s playback stream so the processing runs per app inside PipeWire.

**「Impact」** PipeWire users who want to reproduce the sound of Windows shared-mode playback now have a port to test, but they should expect peak-limiting behavior rather than the frequency shaping that the name &quot;loudness equalization&quot; might imply. Commenters also warn that the algorithm can raise gain on focused impulses such as pure tones, which is why it requires a final limiting stage.

**「Community discussion」** Commenters debated terminology, with ZoomZoomZoom arguing that &quot;equalization&quot; should be reserved for frequency-dependent gain and that the processing is loudness normalization. gbraad and pocketman questioned why reverse engineering a Windows DLL was necessary when standard limiter algorithms are available, and getfacl objected that flattening quiet and loud passages destroys a composition&\#x27;s intended dynamic range.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoxorwr/pw-loudness-eq">GitHub - xoxorwr/pw-loudness-eq: Windows Loudness ...</a></li>
<li><a href="https://news.lavx.hu/article/pw-loudness-eq-ports-windows-loudness-equalization-to-pipewire">pw-loudness-eq ports Windows Loudness Equalization to PipeWire</a></li>

</ul>
</details>

**Tags**: `#audio processing`, `#reverse engineering`, `#PipeWire`, `#Windows audio`, `#open source`

---

<a id="item-tech-news-11"></a>
### [Clojure Core Audited with Lean; Some Bug Reports Contested](https://s.conao3.com/blog/2026/e4f733) ⭐️ 7.0/10

A blogger published an account of using Lean to audit Clojure&\#x27;s core library and reported finding bugs not previously reported. No source details, versions, specific findings, or reproduction steps are available in the supplied material, so the individual claims cannot be verified here. Commenters disputed at least two listed items: one argued that \(.indexOf \(seq \(byte-array \[1 2 3\]\)\) 2\) fails because the argument 2 is a Long while byte arrays hold bytes, and another said \(get &quot;abc&quot; 1.9\) fails because get coerces the key to an integer for string objects. The results should therefore be treated as a mixed set of contested findings rather than confirmed defects.

hackernews · encyclopedism · Nov 25, 14:56 · [Discussion](https://news.ycombinator.com/item?id=50642939)

**「Background」** Lean is a proof assistant and functional programming language built on the calculus of constructions with inductive types, the type theory it shares with Coq, which was renamed Rocq in 2024. That lineage makes Lean one of the main tools for mechanized formal verification, which is the context for applying it to an existing library such as Clojure&\#x27;s core rather than to a purpose-built specification.

**「False positives must be filtered before acting」** For Clojure users, the disputed entries should not be treated as confirmed core-library defects: a commenter notes that \`\(.indexOf \(seq \(byte-array \[1 2 3\]\)\) 2\)\` fails because the searched value \`2\` is a \`Long\`, and that \`\(get &quot;abc&quot; 1.9\)\` reflects \`get\` coercing the key to an integer for strings, so simple type inspection could have caught the first case. That suggests the audit needs false-positive filtering before users file bug reports or change code around these calls; its practical value lies in a reduced-noise list rather than the raw count of findings.

**「Discussion」** Commenters questioned the signal-to-noise ratio of the audit, with rvprasad saying simple type checking would have caught some reported failures and that such exercises would be more helpful with less noise. networked asked whether Lean is displacing Rocq \(formerly Coq\) for program-correctness work and whether language models are significantly better at writing Lean, while vitorsr noted that Clojure is used heavily at Nubank and expressed surprise that primitive functions would have defects. yababa\_y linked a separate audit of Common Lisp compilers and ACL2 as a comparable effort.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_%28proof_assistant%29">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://clojuredocs.org/clojure.core/byte-array">byte-array - clojure.core | ClojureDocs - Community-Powered ...</a></li>
<li><a href="https://clojuredocs.org/clojure.core/byte">byte - clojure.core | ClojureDocs - Community-Powered Clojure ...</a></li>
<li><a href="https://clojure.cc/clojuredocs.org/clojure.core/byte-array/">clojure.core/byte-array - ClojureStar</a></li>

</ul>
</details>

**Tags**: `#Clojure`, `#Lean`, `#formal verification`, `#program correctness`, `#bug auditing`

---

<a id="item-tech-news-12"></a>
### [Browser gallery revives old Nvidia and ATI GPU tech demos](https://gpu-demo-gallery.pages.dev/) ⭐️ 7.0/10

A new browser-based gallery at gpu-demo-gallery.pages.dev collects historical Nvidia and ATI GPU tech demos and runs them again in the browser. The project, submitted to Hacker News by arkits, is an emulation or porting effort aimed at graphics and hardware history rather than a new driver or vendor release. Commenters report that some demos work with visible defects, including a missing &\#x27;N&\#x27; in the Nvidia logo in the Grass demo and a mouse-drag rotation issue in Crystal Ball. They also note rendering behavior differences: Demoroom, ATB-TV, and Flip rotate the camera rather than the model, which makes drag direction feel reversed compared with Donut and Borg.

hackernews · arkits · Nov 25, 04:31 · [Discussion](https://news.ycombinator.com/item?id=50638503)

**「Why these demos needed porting」** GPU vendors historically shipped short real-time tech demos to show off new hardware and APIs; Nvidia&\#x27;s 2002 &quot;Dawn&quot; demo, for instance, was built to demonstrate the programmability of the GeForce FX under DirectX 9. Because those demos targeted specific old cards and graphics APIs, revisiting them today generally requires either period hardware or a port to a modern rendering stack such as the browser.

**「Impact」** For readers exploring the gallery, the reported quirks mean the demos should be treated as preservation ports rather than exact reproductions; mouse-drag behavior and some logo rendering differ from the originals, and commenters describe some results as having &\#x27;vibe-fidelity.&\#x27; The gallery also lacks the context some readers want: ogurechny asks for baseline and next-generation feature explanations, plus links to GPU Gems or contemporaneous press releases, and specifically calls for the 2002 Dawn demo and a patched version.

**「Community discussion」** Commenters welcomed the project as a nostalgic revisit of cards such as the Diamond Riva TNT and Creative Labs GeForce 2 GTS, while reporting concrete defects and inconsistencies. ogurechny criticized the omission of the 2002 Dawn demo and asked for historical annotation, and omoikane argued that camera-rotation demos feel backwards on mouse drag compared with model-rotation demos; scoopr suggested adding the PSX T-Rex, PS3 duck, and Tritech Pyramid3D demos.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/343823/nvidia-dawn-dusk-demo-rig-unearthed-geforce-fx-5950-ultra-extracted-long-ago">NVIDIA &quot; Dawn &amp; Dusk&quot; Demo Rig Unearthed, GeForce FX 5950 Ultra...</a></li>
<li><a href="https://www.neogaf.com/threads/nvidia-dawn-demo-for-kepler.477174/">Nvidia Dawn Demo for Kepler | NeoGAF</a></li>

</ul>
</details>

**Tags**: `#graphics`, `#GPU hardware`, `#browser rendering`, `#software preservation`, `#retro computing`

---

<a id="item-tech-news-13"></a>
### [SemiAnalysis launches GDPx benchmark for frontier models](https://newsletter.semianalysis.com/p/evaluating-recent-model-releases) ⭐️ 7.0/10

SemiAnalysis released GDPx on November 1, a benchmark that evaluates frontier models on 11 domains it considers most valuable for frontier intelligence—chip design, cybersecurity, biology, finance, legal, quant trading, recursive self-improvement, hardware design, materials science, alignment, and software engineering—rather than selecting domains by GDP share or the O\*NET taxonomy used by GDPVal and Agent&\#x27;s Last Exam. GDPx was built with 14 specialized data partners and contains 206 tasks; SemiAnalysis says Opus 5.5 was the highest-scoring model on release day at just 12%, headroom the firm argues lets the benchmark discriminate between future releases, unlike saturated benchmarks such as Terminal Bench 4.0. Since the launch, Anthropic and OpenAI have released new frontier models, Google returned with the Gemini 4 series, and Alibaba and Moonshot also shipped notable models; SemiAnalysis notes that safety classifiers on models such as Fable 5.2 and GPT-6.2 Astra depressed overall scores and published an alternative leaderboard excluding cyber, biology, and alignment and applying partial grading to legal and finance. The excerpt does not include the leaderboard results or detailed methodology.

rss · Semianalysis · Nov 26, 00:05

**「Background」** GDPx was released on November 1, according to the source, as an alternative to agentic benchmarks such as OpenAI&\#x27;s GDPVal and Agent&\#x27;s Last Exam, which select tasks by GDP share or the O\*NET taxonomy. SemiAnalysis says it built 206 tasks with 14 specialized data partners across 11 domains, including chip design, cybersecurity, biology, finance, legal, quant trading, recursive self-improvement, hardware design, materials science, alignment, and software engineering. The source reports that Opus 5.5, the top-scoring model on launch day, scored 12%, a far lower starting point than benchmarks that often debut above 50%.

**「Impact」** Readers tracking frontier-model progress now have a benchmark explicitly designed to stay unsaturated: with the top release-day score at 12%, GDPx leaves room for future models to show gains that saturated benchmarks like Terminal Bench 4.0 can no longer register. The catch is that safety classifiers can suppress scores in cyber, biology, and alignment, so comparisons should account for SemiAnalysis&\#x27;s alternative scoring that excludes those domains and uses partial grading for legal and finance.

**Tags**: `#AI benchmarks`, `#frontier models`, `#model evaluation`, `#agentic AI`, `#AI industry analysis`

---

<a id="item-tech-news-14"></a>
### [LeCun Accuses Amodei of Using AI-Risk Rhetoric to Restrict Open Models](https://x.com/ylecun/status/2124550037912920090) ⭐️ 7.0/10

Yann LeCun posted on X on November 22 accusing Anthropic CEO Dario Amodei of inflating AI dangers since the GPT-2 era to push for open models to be made illegal and preserve control. LeCun said Amodei left OpenAI because he could not obtain control there, and compared the approach to the Ottoman Empire&\#x27;s ban on Arabic printing, calling it &quot;a new form of medieval obscurantism.&quot; The claims are LeCun&\#x27;s attributed characterizations in a social-media post, not independently verified facts, and the Telegram feed reports them without original technical analysis. LeCun, a Turing Award winner for convolutional neural networks, left Meta in November 2025 after 12 years as chief AI scientist and now chairs AMI Labs.

telegram · zaihuapd · Nov 25, 01:30

**「The open-model dispute behind the post」** The spat reflects a long-running disagreement over whether open-weight AI models should be restricted. Amodei has repeatedly framed advanced AI as risky and argued for tighter controls, while LeCun has contended that open models distribute scrutiny rather than concentrate it. LeCun left Meta in November 2025 after 12 years as chief AI scientist and founded AMI Labs, where he is executive chairman.

**Tags**: `#open source AI`, `#AI regulation`, `#AI risk`, `#Yann LeCun`, `#industry commentary`

---

<a id="item-tech-news-15"></a>
### [SpaceX to forgo $738M in BEAD subsidies, offer free Starlink terminals](https://x.com/SawyerMerritt/status/2125314062997467640) ⭐️ 7.0/10

SpaceX has reportedly agreed to give up $738 million in U.S. federal broadband subsidies under the NTIA&\#x27;s BEAD program and instead provide free Starlink terminals to eligible American households, with federal disbursement set at $0. Under the arrangement, SpaceX must supply free terminals, guarantee minimum speeds of 100 Mbps down and 20 Mbps up, offer a low-cost monthly plan, commit to 10 years of service, and meet the same delivery timelines and performance testing as other BEAD-funded providers. In exchange, the company is reportedly exempted from most financial audit, procurement, and administrative reporting obligations while remaining subject to network performance testing. The report comes from a Telegram channel relaying a post on X by Sawyer Merritt and has not been confirmed against a primary NTIA or SpaceX source.

telegram · zaihuapd · Nov 25, 02:17

**「Background」** The Broadband Equity, Access, and Deployment \(BEAD\) program is the U.S. federal broadband buildout fund administered by NTIA, which awards grants to providers to connect unserved and underserved locations. SpaceX had been awarded roughly 476,000 rural locations worth about $738 million in BEAD subsidies; the reported arrangement falls under a new NTIA model agreement that lets satellite providers decline subsidy money while still committing to speed, pricing, and service-term obligations.

**「Impact」** Eligible households would receive Starlink hardware at no upfront cost while the federal subsidy funds go unspent, a structure that differs from conventional BEAD grants paid to ISPs. Because SpaceX remains subject to performance testing against the 100/20 Mbps floor, its measured speeds in subsidized households become the concrete condition of the deal rather than a reporting requirement.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/spacex-drops-738-million-federal-154227688.html?fr=sycsrp_catchall">SpaceX Drops $738 Million of Federal Subsidies to Give Dishes ...</a></li>
<li><a href="https://qz.com/spacex-738-million-broadband-grants-free-starlink-hardware-112526">SpaceX is forgoing about $738 million to offer free Starlink ...</a></li>

</ul>
</details>

**Tags**: `#Starlink`, `#broadband policy`, `#BEAD`, `#satellite internet`, `#telecom`

---

## Global Chips

<a id="item-chip-news-1"></a>
### [Congress push for new China chip curbs gains steam amid Huang&\#x27;s Nvidia return](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fthehill.com%2fpolicy%2ftechnology%2f6241299-nvidia-huang-reinstatement-china-chips%2f&amp;c=4113027279060263006&amp;mkt=en-us) ⭐️ 8.0/10

A bipartisan congressional push to attach new restrictions on chip sales to China to a year-end defense bill is reportedly gaining momentum, with Jensen Huang&\#x27;s return to Nvidia cited as a factor fueling the effort amid growing concerns. The Hill report, available here only as a truncated feed excerpt, does not specify the legislative provisions, bill language, effective dates or vote schedule involved. No new rule is described as enacted, and no change to licensing or shipments is confirmed. Huang&\#x27;s return to the company is presented as political context rather than a change in Nvidia&\#x27;s China product or sales policy.

rss · Bing News - NVIDIA and China · Nov 25, 03:00

**「Background」** Nvidia&\#x27;s board reinstated Jensen Huang as chief executive less than two weeks after he stepped down over his ties to Alice Huang, the longtime head of Singapore-registered Megaspeed, a firm under US criminal investigation over the suspected diversion of Nvidia chips to China, according to external reporting. Huang has been described as a close adviser to Trump on AI trade and had repeatedly pushed to loosen chip-sales restrictions to China. That reinstatement and his earlier advocacy for looser China rules form the immediate backdrop to the bipartisan congressional push now reported to be seeking new China chip-sale restrictions in a year-end defense bill.

**「Impact」** If the restrictions are attached to the year-end defense bill as described, the practical effect would fall on Nvidia&\#x27;s ability to ship affected chips to China customers and on the licensing process governing those sales. Because no provisions or effective dates are available in the supplied excerpt, the scope of products covered and the timing of any constraint remain unconfirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://asiatimes.com/2026/11/trumps-nvidia-deal-leaves-asian-allies-holding-the-bag/">Trump’s Nvidia deal leaves Asian allies holding the bag - Asia Times</a></li>
<li><a href="https://www.aljazeera.com/news/2026/11/9/why-is-nvidias-jensen-huang-at-the-centre-of-a-us-china-spy-scandal">Why is Nvidia ’s Jensen Huang at the centre of a US- China spy...</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`, `#政策立法`

---

<a id="item-chip-news-2"></a>
### [NVIDIA GPU sellers seek new buyers as U.S. tightens remote AI chip access for China](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fmarkets%2fnvidia-sellers-seek-new-buyers-as-us-curbs-china-ai-chip-access-sources-tell-cnbc%2far-AA2idMlI&amp;c=12559116889948556070&amp;mkt=en-us) ⭐️ 7.0/10

CNBC, citing sources, reports that sellers of NVIDIA GPUs are seeking new buyers after new U.S. rules tightened remote access to advanced AI chips for China-linked customers. The report does not identify the specific rule, its provisions, an effective date, or which sellers are affected, and neither a U.S. agency nor NVIDIA has confirmed the account. It describes a reported shift in where NVIDIA-based AI compute capacity is being offered rather than a product launch or a measured change in shipments.

rss · Bing News - NVIDIA and China · Nov 25, 09:28

**「Background」** The tightened rules follow U.S. scrutiny of remote-access routes that let China-linked customers use advanced AI chips hosted abroad. According to CNBC, in July U.S. officials accused Chinese AI lab Moonshot AI of accessing Nvidia chips through a facility in Thailand. Bloomberg reported on Nov. 16 that the Trump administration moved to limit several countries from providing Chinese companies remote access to advanced AI chips and servers.

**「Impact」** If the reported tightening holds, China-linked customers would face added constraints on reaching advanced NVIDIA AI chips remotely, not only through direct purchase, while the sellers involved would need to redirect that capacity to buyers outside China. The source gives no detail on how the restriction is enforced or when it applies, so the practical scope for existing cloud and remote-access arrangements remains unclear.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/25/nvidia-china-ai-chip-remote-access.html">Nvidia sellers seek buyers after U . S . China AI rule : Sources</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-16/us-moves-to-limit-remote-access-to-advanced-ai-chips">US Moves to Curb China ’ s Remote Access to Nvidia ’ s AI Chips</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#芯片销售`

---

<a id="item-chip-news-3"></a>
### [U.S.-based firms helping China access Nvidia&\#x27;s most advanced chips](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fus-based-firms-helping-china-access-nvidias-most-advanced-chips%2far-AA2iePh8&amp;c=11309323021637840269&amp;mkt=en-us) ⭐️ 7.0/10

A CBS News investigation reportedly found at least two California-based NVIDIA customers with Chinese ownership, raising concern that China could access NVIDIA&\#x27;s most advanced chips.

rss · Bing News - NVIDIA and China · Nov 25, 15:10

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-4"></a>
### [Nvidia GPU sellers seek new buyers after U.S. tightens China AI chip remote access](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e5680ed4ad98732c1420e63e95a&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fmarkets%2fnvidia-sellers-seek-new-buyers-as-us-curbs-china-ai-chip-access-sources-tell-cnbc%2far-AA2idMlI&amp;c=12559116889948556070&amp;mkt=en-us) ⭐️ 7.0/10

Nvidia GPU sellers are reportedly seeking new buyers after new U.S. rules tightened remote access to advanced AI chips for China-linked customers, according to CNBC sourcing cited in the report. The excerpt provides no rule text, effective date, access thresholds or named officials, so the precise scope of what is now restricted — and which China-linked customers lose access — is not established by the available account. The development is described as a market reaction among sellers of Nvidia accelerators rather than a confirmed change to Nvidia&\#x27;s own licensing status or shipment figures.

rss · Bing News - China chip policy · Nov 25, 09:28

**「Background」** The tightened measure follows a U.S. Commerce Department rule issued in mid-November 2026 that was explicitly framed as addressing remote access to advanced AI chips of the type Nvidia makes, according to ABC News. That action built on global chip-sale rules left by the Biden administration, which included restrictions on Chinese firms remotely accessing data centers, the New York Times reported. Neither account specifies the threshold, licence terms or compliance date that would govern which China-linked customers can still reach Nvidia GPUs remotely.

**「Impact」** The tightened rule shifts enforcement from where Nvidia GPUs are shipped to where the compute is actually used, so sellers who previously placed advanced chips with China-linked customers through third-country cloud or data-center arrangements must now re-qualify those buyers and replace the lost demand. The Commerce Department issued an interim final rule on November 16, 2026 aimed at closing the remote-access loophole that let Chinese firms reach advanced AI chips via third countries — the same cloud-rental workaround CNBC reported in August 2026 — so offshore compute is no longer a substitute for licensed in-country hardware. The practical constraint for vendors is that this is an interim final rule, not a pending proposal: compliance applies now, and China-linked demand either moves to permitted, licensed sales or shifts toward domestic Chinese accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/16/us/politics/trump-china-ai-chip-loophole.html">Trump Administration Moves to Close A . I . Chip Loophole Ahead of...</a></li>
<li><a href="https://abcnews.com/Business/nvidia-reinstates-jensen-huang-ceo/story?id=138375516">Jensen Huang reinstated as Nvidia CEO; board confident... - ABC News</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U.S ... - CNBC</a></li>
<li><a href="https://www.forbes.com/sites/zacharyfolk/2026/11/16/us-closes-loophole-that-allowed-china-to-remotely-access-nvidia-chips/">US Closes Loophole That Allowed China To Remotely Access ...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/new-us-rules-aim-to-restrict-remote-access-to-ai-servers-and-infrastructure-seeks-to-combat-cloud-rental-workarounds-to-gpu-export-controls">New US rules aim to close loophole, restrict Chinese firms ...</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#芯片政策`

---

<a id="item-chip-news-5"></a>
### [华为与行芯发布“韬EDA”工具进展，面向下一代手机与服务器芯片](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e5693e242159172fb36393d3aae&amp;url=https%3a%2f%2fnews.china.com%2fsocialgd%2f10000169%2f20261125%2f49907551.html&amp;c=9719683234704371621&amp;mkt=en-us) ⭐️ 7.0/10

2026年11月25日，华为在北京第七届创新与知识产权论坛上宣布，其与杭州行芯科技合作开发的国产EDA设计工具套件“韬EDA”已取得进展，可为自主设计下一代手机芯片和服务器芯片提供支持。行芯科技董事长贺青表示，双方自2019年起建立战略合作，共同开发这一工具套件。该消息属于进展公告，未披露具体工艺节点、算力或性能指标、部署时间表及已采用客户；芯片设计所需的基础软件EDA此前长期由美国新思科技（Synopsys）和楷登电子（Cadence）主导。

rss · Bing News - China domestic chips · Nov 25, 12:14

**「Background」** EDA is the software layer that turns chip designs into manufacturable layouts, and the advanced end of that market has long been dominated by US vendors Synopsys and Cadence, according to the source. Xingxin Technology chairman He Qing said the two companies began their strategic cooperation in 2019 to jointly develop a new EDA tool suite, which was named Tao \(韬\); Huawei&\#x27;s seventh innovation and IP forum on November 25 said that work has now progressed toward supporting in-house design of next-generation mobile and server chips. The source gives no capability figures, process-node support or deployment details for the suite, so the announcement is a progress claim rather than a shipped or benchmarked product.

**「影响」** 若“韬EDA”后续确能覆盖下一代手机与服务器芯片设计流程，其直接作用是降低华为及国内设计企业在先进节点上对外国EDA工具的依赖；但当前公告未给出节点覆盖范围或工具链完整度，因此能否替代现有美国工具、以及何时进入实际量产设计流程仍不确定。

**Tags**: `#国产芯片`, `#EDA`, `#华为`, `#芯片设计工具`

---

<a id="item-chip-news-6"></a>
### [Top Nvidia chips still sold on Shenzhen black market despite U.S. ban](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2ftop-nvidia-chips-are-still-on-offer-in-china-despite-us-ban%2far-AA2ic8AV&amp;c=17797524072387682616&amp;mkt=en-us) ⭐️ 6.0/10

Traders in Shenzhen are reportedly continuing to sell Nvidia&\#x27;s top-end chips on China&\#x27;s black market even though U.S. export controls bar their lawful sale to Chinese buyers. The reporting says black-market prices for those chips have surged amid turmoil surrounding Nvidia CEO Jensen Huang. The available account does not name the specific chip models, quote price levels, give shipment or volume figures, or identify the traders or their sourcing, and it describes an ongoing gray-market channel rather than a new policy, licence decision or product launch. It also does not establish whether U.S. or Chinese authorities have taken any enforcement action against the sellers or buyers.

rss · Bing News - NVIDIA and China · Nov 25, 02:00

**「Background」** The item does not specify which Nvidia parts are reportedly being sold, at what prices or in what volumes, so the scope of the alleged Shenzhen trade cannot be verified from the supplied text. It also gives no details on the enforcement actions or licence decisions that underpin the U.S. ban it references, leaving the regulatory baseline for these sales unstated.

**「Black-market sales feed calls for tighter controls」** The reported persistence of black-market sales gives U.S. enforcers a concrete case for tightening scrutiny of Nvidia&\#x27;s China trade: Senate Minority Leader Chuck Schumer has publicly accused CEO Jensen Huang of shipping &quot;extremely advanced chips to China&quot; in violation of export controls, and U.S. officials cited restricted AI chips reaching Chinese entities as grounds for renewed calls to tighten controls. The practical effect is added risk that Nvidia&\#x27;s permitted China sales face slower licence approvals or narrower approved configurations, though the source gives no chip models, prices or volumes to quantify the leakage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/nov/24/nvidia-jensen-huang-congress">Schumer accuses Huang of violating US export control... | The Guardian</a></li>
<li><a href="https://www.youtube.com/watch?v=kf5ZtS-xVjY">US officials raise alarm over restricted Nvidia AI chips reaching China</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中国市场`

---

<a id="item-chip-news-7"></a>
### [Reuters probe examines how NVIDIA AI chips reached China via Megaspeed](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fwww.reuters.com%2fworld%2fchina%2fhow-china-got-access-nvidias-ai-chips-despite-rules-stop-them-2026-11-25%2f&amp;c=16450964411480342744&amp;mkt=en-us) ⭐️ 6.0/10

Reuters reported on November 25, 2026, that authorities have spent more than two years investigating whether Megaspeed diverted NVIDIA AI chips to China, which would be illegal under export controls. The available excerpt also notes that companies in countries including Singapore were permitted to buy advanced chips. The report as supplied does not disclose confirmed findings, any enforcement action, specific chip models, quantities, or the exact policy provisions involved, so whether diversion actually occurred remains unestablished.

rss · Bing News - NVIDIA and China · Nov 25, 11:37

**「Background」** US authorities have been investigating whether Megaspeed diverted NVIDIA AI chips to China since 2024. Around 23 November 2026, the US added Megaspeed to its trade blacklist, meaning the company now needs approval from the Commerce Department to obtain covered items. Reuters&\#x27; report follows that enforcement step and examines how Megaspeed and other buyers in countries including Singapore had been permitted to purchase advanced chips.

**「Tighter third-country chip rules」** The Reuters investigation lands alongside a US regulatory push aimed at exactly the routing it describes: on Nov. 16, 2026, the Commerce Department issued an interim final rule closing a loophole that let China remotely access advanced AI chips through third countries such as Singapore and Malaysia, and moved to extend export controls to five additional countries. The practical effect for NVIDIA is narrower permissible use of its advanced chips by third-country buyers and overseas data-center operators, with shipments through Singapore-style hubs exposed to closer licensing scrutiny — though the Reuters excerpt confirms no finding against Megaspeed and no penalty.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/nov/23/megaspeed-us-trade-blacklist-nvidia">US adds Megaspeed, AI firm at center of Nvidia scandal, to ...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/singapore-investigating-nvidia-linked-megaspeed-023356234.html?fr=sycsrp_catchall">Singapore investigating Nvidia-linked Megaspeed after US ...</a></li>
<li><a href="https://fortune.com/2026/11/16/new-commerce-rule-nvidia-chip-singapore-malaysia-china/">The Nvidia scandal fuels tougher China chip rules as Commerce ...</a></li>
<li><a href="https://www.forbes.com/sites/zacharyfolk/2026/11/16/us-closes-loophole-that-allowed-china-to-remotely-access-nvidia-chips/">US Closes Loophole That Allowed China To Remotely Access ...</a></li>
<li><a href="https://www.politico.com/news/2026/11/16/commerce-closes-chinas-backdoor-to-nvidia-chips-after-white-house-steps-in-01167199">Commerce closes China’s backdoor to Nvidia chips ... - POLITICO</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#芯片转运`

---

<a id="item-chip-news-8"></a>
### [Reuters: Trump&\#x27;s intervention to keep Jensen Huang at Nvidia intensifies Washington chip fight](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fwww.msn.com%2fen-ca%2fnews%2fother%2fanalysis-jensen-huangs-return-to-nvidia-fuels-washington-fight-over-chinas-chip-access%2far-AA2ie7rH&amp;c=7380109478756392690&amp;mkt=en-us) ⭐️ 5.0/10

A Reuters analysis by Patricia Zengerle and Simon Lewis, published November 25, reports that President Donald Trump intervened to preserve Jensen Huang&\#x27;s position as Nvidia CEO, a move the analysis says may have settled who will run the company while sharpening the Washington policy fight over China&\#x27;s access to advanced chips. The supplied excerpt does not specify the form of Trump&\#x27;s intervention, any policy provision, effective date, licensing decision, or chip product and performance figure, so the concrete terms of both the intervention and the China-access debate remain unconfirmed in the available text. The piece is framed as analysis of an ongoing political-industry contest rather than a report of a newly enacted rule or a shipped product.

rss · Bing News - NVIDIA and China · Nov 25, 10:32

**「Predecessor: Trump&\#x27;s intervention to reinstate Huang」** The current debate follows Trump&\#x27;s intervention that reversed Nvidia&\#x27;s decision to remove Jensen Huang as chief executive. The Guardian reported on Nov. 23, 2026 that the company reinstated Huang after the president &quot;convinced&quot; its board, and that Nvidia&\#x27;s share price surged on the reversal; CNN reported on Nov. 24 that the move was an extraordinary intervention into the internal workings of a major American company. The Reuters analysis now examines how that personnel fight is entangled with the separate Washington dispute over China&\#x27;s access to advanced chips.

**「Policy stakes」** Because the excerpt ties Huang&\#x27;s tenure directly to the Washington dispute over China&\#x27;s chip access, the practical consequence it points to is that Nvidia&\#x27;s leadership question and the terms of its China business are now being negotiated in the same political channel; no shipment, licence or revenue effect is quantified in the supplied text.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/nov/23/jensen-huang-reinstated-as-nvidia-chief-executive">Jensen Huang reinstated as Nvidia CEO after Trump intervenes</a></li>
<li><a href="https://edition.cnn.com/2026/11/24/politics/trump-democrats-jensen-huang">Trump hands Democrats a political gift with Jensen Huang intervention</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-9"></a>
### [Trump Backing of NVIDIA&\#x27;s Huang Deals China Hawks a Setback](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fin-backing-nvidia-s-huang-trump-deals-his-china-hawks-a-setback%2far-AA2ibESF&amp;c=8562234304114290427&amp;mkt=en-us) ⭐️ 5.0/10

The Trump administration&\#x27;s backing of NVIDIA&\#x27;s Jensen Huang is being framed as a setback to China hawks inside and outside the government, at a time when the administration faces growing bipartisan calls to be tougher on U.S. chip exports and China. The item is a political analysis rather than a policy document: it reports the alignment between the administration and Huang and the bipartisan pressure on export controls, but cites no new rule, licence decision, effective date, product or performance figure. It does not specify what, if anything, was agreed on NVIDIA&\#x27;s China sales, nor does it identify which officials or lawmakers made particular demands. Treat the reported shift in internal influence as the concrete development, and the export-control implications as unresolved.

rss · Bing News - NVIDIA and China · Nov 25, 02:00

**「Background」** The item follows a period in which bipartisan lawmakers had pressed to attach tighter AI-chip export controls to year-end defense legislation. Search results dated within a day of publication describe a bipartisan push and forthcoming congressional hearings tied to Jensen Huang&\#x27;s return to Nvidia, while an earlier report dated Nov. 17, 2026 said federal lawmakers were pushing to include several measures tightening controls on advanced chips and related technologies in the final legislative package. The current item adds only that the administration now faces growing bipartisan calls to be tougher on U.S. chip exports to China.

**「Impact」** Because the item reports no enacted provision or licensing change, the practical effect on NVIDIA&\#x27;s China shipments remains undetermined; what can be said is that continued administration backing of Huang reduces the near-term likelihood that bipartisan pressure translates into tighter export restrictions on NVIDIA&\#x27;s China business. Any such push would still have to run through formal rulemaking or licence decisions, which the source does not describe.

<details><summary>References</summary>
<ul>
<li>Jensen Huang&#x27;s Nvidia comeback gives China chip restrictions new ...</li>
<li>Jensen Huang&#x27;s Nvidia return adds momentum to chip export controls</li>
<li>Congress pushes bills to stymie chip sales to China amid Huang scandal</li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-10"></a>
### [AMD MEXT Moves Cold Memory Pages to Flash to Cut DRAM Costs](https://www.eetimes.com/amd-tackles-dram-shortages-with-ai-and-flash-storage/) ⭐️ 5.0/10

AMD is promoting MEXT, an AI-based memory-tiering approach that parks cold memory pages in flash storage instead of keeping them in DRAM, EE Times reported. The stated aims are to lower DRAM costs and ease data-center DRAM shortages. The supplied report does not give architecture specifics, performance or bandwidth figures, the products or platforms MEXT applies to, or whether it is shipping, so the item should be read as a described approach rather than a launched product or measured result.

rss · EE Times · Nov 25, 14:00

**「Background」** AMD MEXT is existing AMD software rather than a new chip: AMD describes it as an AI-powered solution that lets flash function as an extension of DRAM, creating a lower-cost memory tier for memory-intensive workloads and reducing dependence on volatile DRAM. Phoronix reports that on EPYC servers MEXT enables flash-as-DRAM tiering driven by a predictive AI engine, and that although a Linux driver exists, MEXT is notably not open-source, departing from AMD&\#x27;s usual open ecosystem posture.

**「Impact」** If MEXT works as described, the practical effect would be to reduce how much DRAM a data-center deployment must buy by shifting cold pages to flash, which matters for AI compute operators facing memory supply pressure; however, the source provides no compatibility details, performance data or availability date, so the size of any DRAM saving cannot be assessed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/software/mext.html">AMD MEXT Predictive Memory Software</a></li>
<li><a href="https://www.phoronix.com/news/AMD-MEXT">AMD Talks Up Their MEXT Software Amid RAM Crisis... - Phoronix</a></li>

</ul>
</details>

**Tags**: `#AI 算力`, `#内存与存储`, `#AMD`, `#数据中心`, `#供应链`

---

<a id="item-chip-news-11"></a>
### [Explainer on how China accesses Nvidia AI chips despite US export curbs](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e56aba248b29d2e099d33cc4ce0&amp;url=https%3a%2f%2fwww.thehindubusinessline.com%2finfo-tech%2fhow-china-got-access-to-nvidias-ai-chips-despite-us-export-restrictions%2farticle71745018.ece&amp;c=1213983047051496063&amp;mkt=en-us) ⭐️ 4.0/10

The Hindu BusinessLine published an explainer examining how US export controls affect Nvidia&\#x27;s AI chip sales to China, organized around new rules, licensing requirements, chip smuggling and tracking technology. The supplied source contains only a headline and a short teaser, with no specific rule provisions, licence decisions, shipment or revenue figures, effective dates, or named companies beyond Nvidia, so the article&\#x27;s actual findings could not be verified from the material provided. It reports no new product, enacted measure or confirmed shipment; it is a promised overview rather than a documented policy change or measured outcome.

rss · Bing News - NVIDIA and China · Nov 25, 07:33

**「Background」** The supplied item is only a headline and teaser for an explainer on US export controls, licensing requirements, chip smuggling and tracking technology; it names no rule, licence decision, product generation, date or figure. Without that detail, no specific prerequisite development can be established from this source.

**「Impact」** As supplied, the item establishes no concrete consequence for Nvidia&\#x27;s China access or revenue, for licensing procedures, or for China&\#x27;s domestic chip supply chain, because it contains no provisions, licence outcomes or shipment data to act on.

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-12"></a>
### [Hindu BusinessLine previews piece on Nvidia chips reaching China](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e5680ed4ad98732c1420e63e95a&amp;url=https%3a%2f%2fwww.thehindubusinessline.com%2finfo-tech%2fhow-china-got-access-to-nvidias-ai-chips-despite-us-export-restrictions%2farticle71745018.ece&amp;c=1213983047051496063&amp;mkt=en-us) ⭐️ 4.0/10

The item is a Bing News teaser pointing to a Hindu BusinessLine article that asks how Nvidia AI chips reached China despite US export restrictions, and previews discussion of new export-control rules, licensing requirements, chip smuggling and tracking technology. The teaser supplies no concrete policy provisions, shipment figures, named developments or new facts, so it does not establish what specifically happened, when, or which channels were used. Any claim about how chips got through would rest on the underlying article, which the source content does not reproduce.

rss · Bing News - China chip policy · Nov 25, 07:33

**「Background」** The source item is only a headline-level teaser, so it names no specific prior licence decision or rule provision to anchor the account. Available context indicates the diversion channel predates this teaser: SemiAnalysis&\#x27; Accelerator Model tracked more than 1.5 GW of export-restricted Nvidia hardware reaching China in recent years, according to Tom&\#x27;s Hardware. An Asia Times report dated November 2026 describes Southeast Asia as a staging ground for moving Nvidia chips into China, with the demand originating in Beijing. Nvidia has denied reports that its most advanced chips were smuggled into China, per a TechCrunch report dated November 24, 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls">Mass smuggling of up to 1.5 million Nvidia AI ... | Tom&#x27;s Hardware</a></li>
<li><a href="https://asiatimes.com/2026/11/trumps-nvidia-deal-leaves-asian-allies-holding-the-bag/">Trump’s Nvidia deal leaves Asian allies holding the bag - Asia Times</a></li>
<li><a href="https://techcrunch.com/2026/11/24/yales-sonnenfeld-nvidia-is-a-detriment-to-u-s-industrial-might-not-a-champion/">Yale&#x27;s Sonnenfeld: Nvidia is a &#x27;detriment&#x27; to US industrial... | ...</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-13"></a>
### [Chinese Chip Stocks Diverge as MOFCOM Move Read as Trade Thaw](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e5693e242159172fb36393d3aae&amp;url=https%3a%2f%2ffinance.eastmoney.com%2fa%2f202611253939399642.html&amp;c=4893990208407199299&amp;mkt=en-us) ⭐️ 4.0/10

Analysts cited in an Eastmoney report interpreted a Ministry of Commerce \(MOFCOM\) action as a fresh signal of easing US-China trade tensions, saying export-chain leaders referred to as &quot;易中天&quot; — described as deeply tied to North American cloud vendors — stand to benefit. The same commentary said the perceived urgency of domestic chip substitution has weakened at the margin, contributing to a divergence in which domestic chip shares fell while export-chain names rose. The source does not identify the specific MOFCOM measure, its provisions, or any effective date, and gives no company-level shipment or revenue figures; the benefit to export-chain names is an analyst expectation, not a confirmed order or reported result.

rss · Bing News - China domestic chips · Nov 25, 04:03

**「Background」** The commentary follows a sequence of dueling regulatory moves. Chinese commerce authorities suspended a set of export-control measures — including the second clause of the announcement tightening dual-use exports to the US — from November 9, 2025 through November 27, 2026, and a November 9, 2026 joint announcement with the customs administration extended a suspension of a series of 2025 export-control measures from November 11, 2026 to January 10, 2027. On the US side, BIS issued an interim final rule on November 16, 2026 covering remote access to advanced semiconductors, bringing offshore data-center access to US AI compute under export licensing. The source does not specify which commerce ministry action analysts were reading as the easing signal.

**「What the signal does and does not change」** The evidence supports only a shift in expectations, not a verified change in shipments or licensing: the article cites an unspecified Ministry of Commerce action, with no policy provision, licence adjustment, effective date or volume figure attached. What it does report is that analysts expect &quot;易中天&quot; — described as export-chain leaders tightly bound to North American cloud vendors — to benefit, while the perceived urgency of domestic substitution weakens, which the piece says is widening the split between falling domestic chip shares and rising export-chain shares. That is an analyst read on sentiment rather than confirmation of new orders or approvals. Demand-side context in the supplied results — overseas cloud capex reported up 90% in 2026 with memory shortage expected to persist into Q2 2027 \(tool-3-2\), and a LightCounting forecast of roughly $26 billion for the 2026 global Ethernet optical module market with 800G and 1.6T at 64% \(tool-3-1\) — describes the backdrop, not a demonstrated consequence of the Commerce Ministry move.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sohu.com/a/1103451562_122993442">快讯！中国商务部向全球宣布：中方坚决反对美国商务部发布限制远程获...</a></li>
<li><a href="https://www.toutiao.com/article/7571016476070429193/">商务部暂停对美两用物项出口管制部分条款，中美贸易现缓和信号？</a></li>
<li><a href="https://www.ccpitjs.org/art/2026/11/19/art_279_83733.html">中国国际贸易促进委员会江苏省分会 每周预警 预警信息2026年11月第3期</a></li>
<li><a href="https://www.21jingji.com/article/20260825/herald/af6e737870940ebc8ba2c0b76d64b6be.html">“ 易 中 天 ”半年净赚224亿元，境外收入高占比面临考验 - 21经济网</a></li>
<li><a href="https://www.163.com/dy/article/L1ADG4J70519QIKK.html">海外 云 厂 商 资本开支增90%，存储 芯 片 供不应求至27年，存储权重31...</a></li>

</ul>
</details>

**Tags**: `#国产芯片`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-14"></a>
### [DeepSeek V4.1 Pro被指12月发布：摆脱NVIDIA、拥抱国产AI芯片倒计时](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b077e5693e242159172fb36393d3aae&amp;url=https%3a%2f%2fwww.msn.com%2fzh-cn%2f%25E6%258A%2580%25E6%259C%25AF%2f%25E6%258A%2580%25E6%259C%25AF%25E5%2585%25AC%25E5%258F%25B8%2fdeepseek-v4-1-pro%25E8%25A2%25AB%25E6%258C%258712%25E6%259C%2588%25E5%258F%2591%25E5%25B8%2583-%25E6%2591%2586%25E8%2584%25B1nvidia-%25E6%258B%25A5%25E6%258A%25B1%25E5%259B%25BD%25E4%25BA%25A7ai%25E8%258A%25AF%25E7%2589%2587%25E5%2580%2592%25E8%25AE%25A1%25E6%2597%25B6%2far-AA2icP1p&amp;c=7546181323248552254&amp;mkt=en-us) ⭐️ 4.0/10

A report claims DeepSeek&\#x27;s V4.1 Pro model will be released in December and is expected to reduce reliance on NVIDIA in favor of domestic AI chips, but the claim lacks official confirmation or technical detail.

rss · Bing News - China domestic chips · Nov 25, 06:06

**Tags**: `#国产芯片`, `#英伟达`, `#AI 算力`, `#国产大模型`

---

<a id="item-chip-news-15"></a>
### [AI Startup Harmonic Expands Into Formal Verification](https://www.eetimes.com/ai-makes-formal-verification-practical/) ⭐️ 4.0/10

EE Times reports that Harmonic, described as an AI model startup, is expanding into formal verification for both software and hardware. The item supplies no product names, technical specifications, performance or throughput figures, pricing, availability date, or named customers, so it is not established whether a product has shipped or only a plan has been announced. No measured results or adoption details are provided.

rss · EE Times · Nov 25, 17:34

**「Background」** Harmonic&\#x27;s earlier work focused on formal mathematics and code correctness: a December 2025 report said the company claimed its AI had proved the correctness of several algorithm implementations, including an in-place implementation, and scored 96.8% on a code-verification benchmark, while a November 2025 profile credited it with 90% on MiniF2F, a formal-mathematics benchmark. A Harmonic job posting for a formal verification engineer describes verifying production hardware and software with Aristotle, its formal reasoning agent, indicating the hardware-verification push was already being staffed. The current EE Times item adds only that the startup is expanding into formal verification for both software and hardware, without product names, specifications, performance or adoption figures.

<details><summary>References</summary>
<ul>
<li>Robinhood CEO&#x27;s AI startup Harmonic achieves 96.8% on code verification</li>
<li>Harmonic: Funding, Investors &amp; Jobs | startups.gallery</li>
<li>Formal Verification Engineer at Harmonic - Enlistar</li>

</ul>
</details>

**Tags**: `#形式验证`, `#芯片设计`, `#AI 算力`, `#创业公司`

---

<a id="item-chip-news-16"></a>
### [Winbond Promotes Certified NOR Flash for Edge AI Memory](https://www.eetimes.com/winbond-widens-edge-ai-reach-certifies-nor-flash/) ⭐️ 4.0/10

Winbond is marketing certified NOR flash memory for edge AI applications, positioning it as a way to deliver higher bandwidth and density without the cost of custom-designed memory, according to an EE Times brief. The source provides no product names, density or bandwidth figures, certification bodies, dates or shipment volumes, so the certification status and any performance advantage remain unverified vendor positioning rather than a demonstrated result.

rss · EE Times · Nov 25, 08:59

**「Background」** The supplied source does not identify a prior Winbond NOR product generation, the certifying body, or an earlier edge-AI memory announcement that this positioning follows. Available tool results provide only general context — a security-research report cited by Cybersecurity News describes Winbond as the largest NOR flash maker with more than 25% of the market — and no predecessor product or policy step. The specific certification and any density or bandwidth specifications therefore remain unconfirmed in the available evidence.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/hello-attack-bypasses-windows-hello-and-bitlocker/">New Hello Again Attack Bypasses Windows Hello and BitLocker PIN...</a></li>

</ul>
</details>

**Tags**: `#边缘AI`, `#存储芯片`, `#NOR Flash`, `#AI 算力`

---

## Financial News

<a id="item-finance-news-1"></a>
### [U.S. Commerce Department reportedly threatened Intel over 10% stake demand](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 9.0/10

Court documents reportedly show U.S. Commerce Department lawyers told Intel&\#x27;s CFO in August 2025 that refusing a 10% government stake was not a negotiation and would bring unpredictable consequences; Intel&\#x27;s board then ceded the shares, which Trump said the government fully owns and controls without paying, now worth about $11 billion.

telegram · zaihuapd · Nov 25, 13:25

**「Background」** The U.S. government had been seeking an equity stake in the chipmaker, and a 10% holding would make Washington a major shareholder in a company central to domestic semiconductor production.

**「Impact」** If confirmed, the arrangement would give the U.S. government direct ownership in Intel alongside its existing role funding domestic chip manufacturing, affecting other shareholders and setting a precedent for state equity in strategic firms.

**Tags**: `#semiconductors`, `#industrial policy`, `#Intel`, `#US government equity stake`, `#corporate governance`

---

<a id="item-finance-news-2"></a>
### [SpaceX 与特斯拉拟商谈 3.5 万亿美元全股票合并](https://thenextweb.com/news/spacex-tesla-merger-five-directors-special-committees) ⭐️ 8.0/10

据知情人士透露，SpaceX 与特斯拉已分别在各自公司成立由五名董事组成的特别委员会，就规模达 3.5 万亿美元的全股票合并进行谈判，并力争在年底前完成；目前双方尚未接近达成协议。

telegram · zaihuapd · Nov 25, 00:41

**「背景」** 两家公司均由埃隆·马斯克领导；若交易达成，这将是史上规模最大的合并。委员会仍需确定换股比例、争取股东支持，并防范马斯克此前交易引发的投资者诉讼。

**Tags**: `#mergers-and-acquisitions`, `#Tesla`, `#SpaceX`, `#Elon Musk`, `#equity-markets`

---

<a id="item-finance-news-3"></a>
### [美国拟对14个贸易伙伴加征第301条新关税](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html) ⭐️ 8.0/10

美国政府依据1974年《贸易法》第301条,拟对中国、欧盟、日本、印度等14个贸易伙伴加征针对制造业结构性产能过剩的新关税,税率按国别设定而非统一。对华新关税将在2018年已加征的25%之上再加20%,若中国未遵守2025年10月在韩国釜山达成的贸易休战协议,可能升至40%。

telegram · zaihuapd · Nov 25, 13:59

**「Background」** The proposal follows an eight-month investigation launched in March by US Trade Representative Jamieson Greer into foreign factory subsidies and excess output, and aims to replace tariffs struck down by the Supreme Court earlier this year. Section 301 of the 1974 Trade Law lets the US impose duties on trading partners found to engage in unfair trade practices.

**「影响」** 拟议关税将直接影响这14个伙伴中对美出口制造业产品的企业;由于除中国外不与现有关税叠加、且税率不超过对等贸易框架协议公布的水平,实际成本上升幅度取决于最终国别税率和产品范围。

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html">U.S. unveils new Section 301 tariffs targeting China , EU and others</a></li>
<li><a href="https://www.foxbusiness.com/fox-news-global-economy/trump-admin-raise-tariffs-china-eu-other-trading-partners">Trump administration proposes sweeping Section 301 tariffs on China ...</a></li>
<li><a href="https://nypost.com/2026/11/25/business/us-proposes-new-tariffs-on-14-trading-partners-including-china-japan-eu-and-india/">US proposes new tariffs on 14 trading partners — including China ...</a></li>

</ul>
</details>

**Tags**: `#US tariffs`, `#Section 301`, `#US-China trade`, `#EU trade`, `#trade policy`

---