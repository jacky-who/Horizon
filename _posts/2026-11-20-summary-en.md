---
layout: default
title: "Horizon Summary: 2026-11-20 (EN)"
date: 2026-11-20
lang: en
---

> From 38 items, 21 important content pieces were selected

---

**Technology News**
1. [Levent Alpöge Posts Claimed Generalized Riemann Hypothesis Proof](#item-tech-news-1) ⭐️ 9.0/10
2. [Terry Tao Discusses Unforced Fluid Singularities and GRH](#item-tech-news-2) ⭐️ 8.0/10
3. [Unverified Navier–Stokes blow-up claim posted on GitHub](#item-tech-news-3) ⭐️ 8.0/10
4. [PHP mixed-case https:// schemes silently skip TLS, patched in 8.2.36+](#item-tech-news-4) ⭐️ 8.0/10
5. [Meta&\#x27;s AI Agent Muse Reportedly Mixes Accounts, Exposing Private Data](#item-tech-news-5) ⭐️ 8.0/10
6. [KVM CVE-2026-99312 lets AMD guests read host memory](#item-tech-news-6) ⭐️ 8.0/10
7. [Alessandro Masullo Announces Claimed GRH Proof in Haste](#item-tech-news-7) ⭐️ 7.0/10
8. [Inkling 2 Mini: open-weight looped MoE model for local inference](#item-tech-news-8) ⭐️ 7.0/10
9. [Report: SEC probing Nvidia accounting as shares extend rout](#item-tech-news-9) ⭐️ 7.0/10
10. [Paper Claims a Language Model Can Rewrite Its Own Weights; HN Questions Novelty](#item-tech-news-10) ⭐️ 7.0/10
11. [Scott Aaronson on an apparent LLM proof of the Riemann Hypothesis](#item-tech-news-11) ⭐️ 7.0/10
12. [Signal describes privacy work as users debate AI app access and VPN CAPTCHAs](#item-tech-news-12) ⭐️ 7.0/10
13. [AI-designed Frostbite CPU claim prompts debate on novelty and verification](#item-tech-news-13) ⭐️ 7.0/10
14. [Levent Alpöge claims Claude-assisted Riemann Hypothesis proof](#item-tech-news-14) ⭐️ 7.0/10
15. [Gemini can now control Mac apps on users&\#x27; behalf in the US](#item-tech-news-15) ⭐️ 7.0/10
16. [UK tribunal rules for Apple, opens encryption backdoor case to public](#item-tech-news-16) ⭐️ 7.0/10
17. [U.S. House panel discloses nearly 880,000 AI chip export approvals to China](#item-tech-news-17) ⭐️ 7.0/10
18. [US tightens chip exports as India seeks AI compute growth](#item-tech-news-18) ⭐️ 7.0/10

**Technology Blog**
1. [Day-0 vLLM Support for the Looped Inkling 2 Mini](#item-tech-blog-1) ⭐️ 8.0/10
2. [Why Output Caching Is Low-Leverage for LLM Costs](#item-tech-blog-2) ⭐️ 6.0/10

**Financial News**
1. [Beijing draft lease contract would bar deposit deductions for normal wear and tear](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Levent Alpöge Posts Claimed Generalized Riemann Hypothesis Proof](https://alpo.ge/remark.pdf) ⭐️ 9.0/10

Levent Alpöge has posted a claimed proof of the Generalized Riemann Hypothesis at alpo.ge/remark.pdf, reportedly supported by a large Lean formalization rather than a conventional short paper. Commenters describe the Lean artifact as about 1.3 GB and roughly 15 million lines, split into 14 downloadable parts, and point to an MIT page associated with Andrew Sutherland that lists verification checks and says more were still finishing as of 2026-11-20 22:05 UTC. The result has not been independently confirmed in the supplied material, so it remains a claim; a separate “completely human proof” is also linked in the discussion.

hackernews · iamronaldo · Nov 20, 14:16 · [Discussion](https://news.ycombinator.com/item?id=50574968)

**「What the conjecture says and who is claiming it」** The Riemann Hypothesis is the 167-year-old conjecture about the distribution of the primes; the Generalized Riemann Hypothesis, which Alpöge says his proof confirms, extends that guess far beyond Riemann&\#x27;s original formulation into a much broader class of zeta and L-functions. The author of the claimed proof, Levent Alpöge, is a Turkish-American number theorist known for work in number theory and arithmetic statistics who was a junior fellow in the Harvard Society of Fellows before joining Anthropic as a member of its technical staff.

**「Impact」** For mathematicians and formal-methods researchers, assessing the claim means auditing a very large Lean development—commenters cite 1.3 GB and about 15 million lines delivered in 14 parts—so independent checking is a substantial engineering and compute task, not just a reading exercise; the MIT checks page indicates verification was still in progress at the reported timestamp.

**「Community discussion」** Commenters report that the Lean checks provide strong evidence and also link a separate “completely human proof,” while one objects to framing that could shift credit from Alpöge as a mathematician to a company. One commenter also cites a recent Terence Tao remark that current AI alone could not have solved the Riemann hypothesis, making the role of AI in this claim a point of debate.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/">Anthropic mathematician claims to prove Riemann hypothesis , most...</a></li>
<li><a href="https://www.clarin.com/us-news/who-is-levent-alpoge-the-anthropic-mathematician-who-claims-solved-the-riemann-hypothesis-with-claude_0_2WdGvYKBVM.html">Who is Levent Alpöge ? The Anthropic mathematician who claims he...</a></li>

</ul>
</details>

**Tags**: `#Riemann Hypothesis`, `#formal verification`, `#Lean`, `#mathematics`, `#research breakthrough`

---

<a id="item-tech-news-2"></a>
### [Terry Tao Discusses Unforced Fluid Singularities and GRH](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 8.0/10

A post by Terry Tao addresses unforced Euler and Navier-Stokes singularities and the Generalized Riemann Hypothesis, according to the item&\#x27;s title and metadata. The supplied material contains no post text, theorem statement, or proof artifact, so it cannot be determined from this item alone whether the post announces a new result, surveys prior work, or reports a formalization. The accompanying Hacker News discussion focuses on Lean kernel verification and AI-assisted mathematics rather than on the technical claims.

hackernews · archon1410 · Nov 20, 17:21 · [Discussion](https://news.ycombinator.com/item?id=50578358)

**「Background」** The unforced Euler and Navier–Stokes singularity questions ask whether the incompressible equations can blow up in finite time from smooth data without external forcing; the Generalized Riemann Hypothesis extends the Riemann hypothesis from the Riemann zeta function to Dirichlet L-functions. Tao&\#x27;s November 20, 2026 post is tagged as covering the incompressible Euler equations and naming Levent Alpöge, Tristan Buckmaster, and Matei Coiculescu, and a secondary summary describes their work as heavily AI-assisted while noting that the available text is truncated and that methods and verification remain to be confirmed.

**「Community Discussion」** Commenters debated trust in Lean formalization: one reported that two independent kernels accepted the result, while another asked how a large Lean build can be checked to prove the intended theorem rather than a trivial statement. A separate thread questioned whether AI-driven proof search can create new mathematical abstractions, not only verify consequences of existing ones.

<details><summary>References</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/">Unforced Euler singularity, unforced Navier-Stokes ...</a></li>
<li><a href="https://todayforai.com/en/items/art-87f06889-96c">Tao Reports AI-Assisted Proofs on Euler and Navier-Stokes ...</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#formal verification`, `#Lean`, `#AI-assisted proofs`, `#Navier-Stokes`

---

<a id="item-tech-news-3"></a>
### [Unverified Navier–Stokes blow-up claim posted on GitHub](https://github.com/tristanbuckmaster/navier-stokes/) ⭐️ 8.0/10

A Hacker News post links to a GitHub repository whose title asserts a finite-time blow-up result for the Navier–Stokes equations, a claim that would matter to mathematicians and fluid-dynamics researchers if established. The supplied item contains no proof text, paper, or peer review, so the result is unverified and should be treated as an announced claim rather than a confirmed theorem. Commenters describe it as the &\#x27;unforced&\#x27; version of the problem and contrast it with a separate result attributed in the thread to OpenAI, which they say uses a carefully designed external force; those details come only from discussion.

hackernews · trotro · Nov 20, 15:34 · [Discussion](https://news.ycombinator.com/item?id=50576232)

**「Background」** The Navier–Stokes existence and smoothness question is a Millennium Prize problem: whether the three-dimensional equations governing viscous fluid flow can develop a singularity in finite time from smooth initial data with no external force. A finite-time singularity has already been constructed for the inviscid three-dimensional Euler equations by Alpöge, Buckmaster and Coiculescu, using smooth periodic initial data. Coverage of the current claim describes it as the unforced Navier–Stokes case, distinguishing it from an earlier example that relied on a carefully designed external force.

**「Prize stakes and verification burden」** A verified finite-time blow-up for the unforced three-dimensional Navier–Stokes equations would settle the Clay Mathematics Institute&\#x27;s existence-and-smoothness Millennium Prize problem in the negative, which is what makes the repository&\#x27;s claim consequential rather than routine. As posted, it is an unrefereed GitHub document rather than a published proof, so researchers and journals should treat the result as unverified until independent experts can check the argument.

**「Community discussion」** Commenters focus on the distinction between this claimed &\#x27;unforced&\#x27; blow-up and a separate OpenAI result they say relies on a designed external force, with one calling the unforced case more &\#x27;realistic.&\#x27; That framing is community opinion, and the thread offers no independent check of the proof.

<details><summary>References</summary>
<ul>
<li><a href="https://officechai.com/ai/tristan-buckmaster-levent-alpoge-claim-proof-of-navier-stokes-millennium-prize-problem-without-forcing/">Tristan Buckmaster, Levent Alpöge Claim Proof Of Navier ...</a></li>
<li><a href="https://cims.nyu.edu/~tristanb/cc.pdf">Finite-Time Singularity Formation for the Three-Dimensional ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Navier-Stokes equations`, `#mathematical proof`, `#fluid dynamics`, `#computational science`, `#Hacker News discussion`

---

<a id="item-tech-news-4"></a>
### [PHP mixed-case https:// schemes silently skip TLS, patched in 8.2.36+](https://x.com/ljachowicz/status/2123477025268924514) ⭐️ 8.0/10

A reported flaw in PHP&\#x27;s HTTP and FTP stream wrappers causes URLs whose scheme is written with non-lowercase letters — HTTPS://, httpS:// or FTPS:// — to be sent as plaintext HTTP or FTP instead of over TLS. The wrapper matches the scheme case-insensitively but reportedly enables TLS only when the fifth character is a lowercase &quot;s&quot;, so tokens, Basic authentication credentials, cookies, POST bodies and FTP logins would travel in cleartext; requests reached through a third-party redirect to such a URL are said to be affected the same way. The issue is tracked as CVE-2026-128064 \(GHSA-f6gg-rchx-xw8j\) with a CVSS 4.0 score of 8.2 and is fixed in PHP 8.2.36, 8.3.37, 8.4.28, 8.5.13 and 8.6.0. PHP 8.1 and earlier are end-of-life and will not receive a fix, leaving lowercasing the scheme before use as the workaround. The claim originates from a single social-media report and has not been independently confirmed here.

telegram · zaihuapd · Nov 20, 03:04

**「Background」** PHP&\#x27;s HTTP and FTP stream wrappers parse a URL&\#x27;s scheme before opening a remote connection. The wrappers recognize schemes case-insensitively, but enable TLS only when the scheme contains a lowercase &quot;s&quot; at a fixed position, so capitalization can change the transport without changing the parsed protocol. That mismatch is the precondition for the reported cleartext exposure.

**「Impact」** Anyone running PHP 8.1 or older has no patched release available and must normalize URL schemes to lowercase in application code before handing them to stream wrappers, and should audit code paths that follow redirects with attacker-influenced targets — a redirect to a mixed-case scheme URL is described as sufficient to trigger cleartext transmission.

<details><summary>References</summary>
<ul>
<li><a href="https://everycve.com/CVE-2026-128064">CVE - 2026 - 128064 : Mixed - case HTTPS and FTPS URLs can expose...</a></li>

</ul>
</details>

**Tags**: `#PHP`, `#security vulnerability`, `#TLS`, `#CVE`, `#HTTPS`

---

<a id="item-tech-news-5"></a>
### [Meta&\#x27;s AI Agent Muse Reportedly Mixes Accounts, Exposing Private Data](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/) ⭐️ 8.0/10

Meta employees reported that the company&\#x27;s AI assistant Muse mixed conversations across accounts and displayed other users&\#x27; private information, according to internal posts cited by Reuters and reported by TechCrunch. The reported exposures included parenting requests and career advice the recipients never sent, orders they never placed, and bank balances belonging to someone else; one employee said Muse inserted Capital One and Charles Schwab balances into a weather chat. Another employee said Muse prompted her on her personal phone to reply to her sister&\#x27;s Signal message despite her not authorizing access to other apps. The account relies on secondary reporting of internal posts rather than independent technical verification.

telegram · zaihuapd · Nov 20, 05:10

**「Background」** Muse is Meta’s AI agent, and the incident account is based on internal company posts reviewed by Reuters rather than an independent technical audit. Meta disputed the most alarming outputs, telling Ars Technica that the erratic messages showing random bank and bitcoin balances were not real.

**「Account isolation at risk」** For users, the reported behavior means account boundaries cannot be assumed: Muse surfaced another person&\#x27;s Capital One and Charles Schwab balances in a weather chat and referenced a Signal message without authorization, so users should review their Muse history for unfamiliar financial or message content and revoke app access they did not intend to grant. Meta&\#x27;s earlier pause of Muse&\#x27;s conversation-sharing feature after a separate flaw involving discoverable chat links is not evidence that this reported cross-account mixing has been fixed; the scope remains unresolved until Meta confirms it.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/">Meta ’s AI agent Muse is mixing up conversations and... | TechCrunch</a></li>
<li><a href="https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/">Muse privacy invasions are freaking out Meta staffers, internal chats...</a></li>
<li><a href="https://cybersecuritynews.com/meta-muse-ai-privacy-flaw/">Meta Muse AI Privacy Flaw Exposes Confidential Business Data ...</a></li>
<li><a href="https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/">Meta’s AI agent Muse is mixing up conversations and exposing ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#privacy`, `#data leakage`, `#Meta`, `#security incident`

---

<a id="item-tech-news-6"></a>
### [KVM CVE-2026-99312 lets AMD guests read host memory](https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html) ⭐️ 8.0/10

A Linux KVM vulnerability, CVE-2026-99312, allows guests to read host memory on AMD systems when nested virtualization is enabled. Researchers demonstrated the flaw on DigitalOcean by reading about 127 GB of host memory from inside a guest. The upstream fix shipped on November 18 in stable kernel 7.3.5 and related stable releases, but Debian, Ubuntu, and other distribution kernels remain unpatched. Until those updates arrive, the reported mitigation is to disable nested virtualization.

telegram · zaihuapd · Nov 20, 14:23

**「Background」** KVM is the Linux kernel&\#x27;s built-in hypervisor, and nested virtualization lets a guest VM run its own virtual machines. DigitalOcean&\#x27;s advisory describes CVE-2026-99312 as a stale-pointer bug in KVM&\#x27;s nested-virtualization support on AMD, which is why Intel-based hosts are not affected. Terra Security&\#x27;s analysis traces the flaw&\#x27;s roots to a previous security fix in that same area.

**「Impact」** For operators of affected AMD hosts, guest workloads may expose host memory contents until the hypervisor kernel is fixed; the immediate action is to turn off nested virtualization on Debian and Ubuntu hosts that have not received the patch.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/new-linux-kvm-flaw-cve-2026-99312-lets.html">Linux KVM Flaw CVE - 2026 - 99312 Lets Guest VMs Access Host ...</a></li>
<li><a href="https://www.digitalocean.com/blog/cve-2026-99312-kvm-patch">Virtualization , Responsible Disclosure, and CVE - 2026 - 99312</a></li>
<li><a href="https://www.terra.security/blog/kvm-guest-to-host-escape">KVM Guest-to- Host Escape | Terra Security Research</a></li>

</ul>
</details>

**Tags**: `#KVM`, `#Linux kernel`, `#virtualization security`, `#CVE-2026-99312`, `#AMD`

---

<a id="item-tech-news-7"></a>
### [Alessandro Masullo Announces Claimed GRH Proof in Haste](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) ⭐️ 7.0/10

A blog post announced that Alessandro Masullo has published a claimed proof of the Generalized Riemann Hypothesis, with the release described as hurried. The item supplies no manuscript text or independent verification, so the proof remains an unconfirmed claim rather than a validated result. Hacker News commenters treated it as a developing priority dispute, citing a 940-page draft and an empty early section as reasons for caution.

hackernews · jasondavies · Nov 20, 18:33 · [Discussion](https://news.ycombinator.com/item?id=50579568)

**「Background」** The Generalized Riemann Hypothesis extends the Riemann Hypothesis from the Riemann zeta function to a broader class of L-functions and constrains the distribution of primes in arithmetic progressions. Coverage of the announcement describes Masullo&\#x27;s 940-page preprint, &quot;The Music of the Primes,&quot; as following months of review by Brian Conrad, Masullo&\#x27;s former Stanford advisor, and says AMS president Ravi Vakil announced it on November 20, 2026, to invite rapid community scrutiny. A separate Claude-assisted Lean proof claim by Levent Alpöge appeared the same day.

**「Verification Burden」** Vakil&\#x27;s post explicitly asks mathematicians to review Masullo&\#x27;s 940-page preprint, so the practical burden falls on analytic number-theory experts willing to check a draft that commenters note has an empty section 1.1.1. Until that scrutiny produces a verdict, the proof remains an unverified claim rather than an established result.

**「Community Discussion」** Commenters debated priority and verification: one said a 12-year effort made a hurried release understandable given the Anthropic announcement, while another called the 940-page draft with an empty section 1.1.1 a red flag. Another proposed that mathematicians post verifiable, timestamped hashes of in-progress work to secure partial credit if an AI system solves the problem first, and one speculated without evidence that an AI cross-check could have exposed the work.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/alessandro-masullo-grh-human-proof-claimed-vs-verified-november-2026">Masullo GRH Draft: What Vakil Announced (Nov 20) | explainx ...</a></li>
<li><a href="https://x.com/i/trending/2123859232806064131">Mathematician Claims Proof of Generalized Riemann Hypothe...</a></li>
<li><a href="https://kingy.ai/blog/two-riemann-proof-claims-timeline/">Two Riemann proof claims in one day. What counts as first ...</a></li>
<li><a href="https://x.com/i/trending/2123859232806064131">Mathematician Claims Proof of Generalized Riemann Hypothe...</a></li>
<li><a href="https://explainx.ai/blog/alessandro-masullo-grh-human-proof-claimed-vs-verified-november-2026">Masullo GRH Draft: What Vakil Announced (Nov 20) | explainx ...</a></li>

</ul>
</details>

**Tags**: `#Generalized Riemann Hypothesis`, `#mathematics research`, `#AI competition`, `#research verification`, `#Hacker News`

---

<a id="item-tech-news-8"></a>
### [Inkling 2 Mini: open-weight looped MoE model for local inference](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 7.0/10

Inkling 2 Mini is described as an open-weight, locally runnable AI model built on a looped transformer and mixture-of-experts design. A GGUF version is reported for Ollama and Llama.cpp, making it usable in common local inference stacks. Commenters compare its benchmarks to Qwen3.8-27B and describe the results as strong, but those comparisons are community claims and were not independently validated in the supplied material. A Reddit note quoted in the comments also says the model was trained end-to-end in nvfp4.

hackernews · jasondavies · Nov 20, 20:12 · [Discussion](https://news.ycombinator.com/item?id=50581260)

**「Background」** A looped transformer reuses the same middle layers multiple times per token instead of stacking more unique layers; Inkling 2 Mini runs its middle layers three times for each token, adding repeated computation without increasing parameter count. It is also a mixture-of-experts model with 26 billion total parameters but only 5.4 billion active per token, which lowers the compute required for each token during inference.

**「Local deployment and evaluation caveat」** Because quantized GGUF builds are published through Unsloth and llama.cpp, local-inference users can run Inkling 2 Mini on their own hardware instead of only through a hosted API. Thinking Machines claims it leads comparable models on agentic coding benchmarks such as DeepSWE v1.1 and SWE-bench Pro v2 but trails Qwen 3.8-27B on others, so teams considering a swap for coding-agent work should validate it against their own tasks rather than assume a uniform improvement.

**「Community discussion」** Commenters are enthusiastic but conditional: one calls the benchmark results “bonkers good” only if they hold up in real-world use, and another plans to test the GGUF build on an AMD 7900XTX against Qwen 3.8 27B while expecting the MoE design to provide higher decode speed.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>
<li><a href="https://artificialanalysis.ai/articles/inkling-2-mini">Thinking Machines has released Inkling 2 Mini, an open ...</a></li>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>

</ul>
</details>

**Tags**: `#open-weight models`, `#looped transformers`, `#Mixture-of-Experts`, `#local inference`, `#AI model releases`

---

<a id="item-tech-news-9"></a>
### [Report: SEC probing Nvidia accounting as shares extend rout](https://finance.yahoo.com/markets/article/nvidia-stock-extends-25-trillion-rout-as-sec-probe-reportedly-investigates-its-accounting-194945274.html) ⭐️ 7.0/10

Reporting attributed to unnamed sources says the SEC is investigating Nvidia&\#x27;s accounting, according to a Yahoo Finance article that also said the chipmaker&\#x27;s shares extended a steep selloff. The supplied material does not say whether the inquiry is formal or informal, which periods or figures it covers, or whether Nvidia or the SEC have commented, so the probe remains an unconfirmed report rather than a disclosed enforcement action. No filing, company statement or regulator confirmation accompanies the claim.

hackernews · ftchd · Nov 20, 20:22 · [Discussion](https://news.ycombinator.com/item?id=50581438)

**「Scope of the reported SEC review」** The report describes SEC enforcement staff examining potential accounting issues at Nvidia, based on two people briefed on the matter, rather than a filed case or a finding of wrongdoing. Reuters reported the examination on Nov. 20, 2026, but the supplied reports did not specify which accounting practices are at issue.

**「Impact」** Nvidia&\#x27;s quarterly reports are the main public gauge of AI data-center demand, so an accounting inquiry whose scope is undisclosed leaves investors and hardware buyers unable to tell whether specific revenue figures — for example from multi-year chip and capacity deals — are in question.

**「Community discussion」** Commenters attributed the trouble to what one called years of &quot;circular financing&quot; and predicted that renegotiating usage deals with neocloud customers would backfire, while another questioned why the board would name the CFO interim CEO if it suspected accounting problems. One commenter noted the stock is down nearly 50% from its high six weeks earlier; these are reader claims and opinions, not established facts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/us-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say-2026-11-20/">Nvidia&#x27;s accounting is a focus of US SEC investigation ...</a></li>
<li><a href="https://www.unite.ai/sec-enforcement-staff-examine-nvidia-accounting-reuters-reports/">SEC Enforcement Staff Examine NVIDIA Accounting, Reuters Reports</a></li>

</ul>
</details>

**Tags**: `#nvidia`, `#sec-investigation`, `#ai-hardware`, `#accounting`, `#tech-industry`

---

<a id="item-tech-news-10"></a>
### [Paper Claims a Language Model Can Rewrite Its Own Weights; HN Questions Novelty](https://arxiv.org/abs/2611.21885) ⭐️ 7.0/10

An arXiv preprint titled &quot;Language Models Can Rewrite Their Own Weights&quot; \(arXiv:2611.21885\) argues that a language model can improve itself by editing its own weights through its own reasoning, with no gradients and no training, according to the abstract text quoted in the Hacker News thread. No source content or full paper was available, so the methodology, model, and benchmark details behind that claim could not be verified here. Commenters pushed back on the result: the one self-modification described was shortening the model&\#x27;s reasoning traces to avoid hitting a token limit, which they said echoes earlier weight-space programming and &quot;sleep&quot;-style work rather than demonstrating general self-improvement. The thread also disputed the framing that skipping gradients means the process is not training, since the model reportedly tests edits on practice problems and keeps only those that work.

hackernews · lwhsiao · Nov 20, 16:29 · [Discussion](https://news.ycombinator.com/item?id=50577265)

**「Background」** The paper sits between two existing lines of work: weight editing, which changes a model&\#x27;s behavior by modifying its parameters instead of only its prompt, and self-improvement, in which a model generates its own practice material or revision targets. Commenters in the HN thread compared it with earlier weight-space programming and Google&\#x27;s &quot;sleep&quot; framework, which they described as also updating weights from self-generated experience, and questioned how much the new result adds beyond those approaches.

**「Impact」** For developers evaluating self-editing models, commenters&\#x27; concrete advice is to benchmark any reported gain against prior weight-space programming and Google&\#x27;s &quot;sleep&quot; framework, which they say produced comparable effects. One commenter raises a safety concern specific to this capability: a model that can autonomously rewrite its own weights could, if directed, locate and suppress activations associated with safety and alignment behavior; this is presented as a plausible risk, not a demonstrated result in the paper.

**「Community Discussion」** The most substantive disagreement is over novelty: one commenter says the only self-edit reported was trimming reasoning-trace length to avoid a token limit, matching what the weight-space programming write-up found even for a strong model, while another points to Google&\#x27;s &quot;sleep&quot; framework, which already updates numerical weights offline from self-generated examples. A separate commenter argues the &quot;no training&quot; framing is misleading because the model tests candidate edits on practice problems and submits only the ones that work, and another raises the concern that autonomous self-weight editing is a particularly risky direction for AI safety research.

**Tags**: `#language models`, `#weight editing`, `#self-improvement`, `#AI safety`, `#research`

---

<a id="item-tech-news-11"></a>
### [Scott Aaronson on an apparent LLM proof of the Riemann Hypothesis](https://scottaaronson.blog/?p=10344) ⭐️ 7.0/10

Scott Aaronson&\#x27;s blog post takes up an apparent proof of the Riemann Hypothesis produced with a large language model, framed in its title as &quot;the stochastic parrots&quot; having &quot;apparently proved&quot; it. The supplied material contains no statement of the argument, no indication of independent checking by mathematicians, and no outcome beyond the post&\#x27;s own framing, so the claim stays unconfirmed. Discussion around the post centered on the size of the accompanying Lean formalization and on the compute such an effort would require.

hackernews · stratos123 · Nov 20, 20:03 · [Discussion](https://news.ycombinator.com/item?id=50581084)

**「What preceded the claim」** The phrase &quot;stochastic parrots&quot; comes from a 2021 critique of large language models that treated them as remixing training text without understanding it, and Aaronson&\#x27;s post notes social-media users turning the term back on him now that &quot;these so-called &\#x27;stochastic parrots&\#x27; just proved the Riemann Hypothesis.&quot; The immediate backdrop, as summarized by AGI Hunt, is Levent Alpöge&\#x27;s claim that Anthropic models proved the Generalized Riemann Hypothesis, which Aaronson had commented on.

**「Impact」** For readers trying to judge the claim, the decisive artifact is a Lean development that actually compiles against the proof checker&\#x27;s kernel rather than prose describing a proof; commenters&\#x27; reaction suggests the formalization, if present, is large enough that few will audit it line by line. Until that artifact and an independent check are available, the result should be treated as unverified.

**「Community discussion」** Commenters focused on comprehensibility rather than correctness: one asked whether anyone can understand the Lean formalization &quot;in it&\#x27;s entirety,&quot; another wondered how many mathematicians could reach similar breakthroughs given near-infinite compute, and a third worried that researchers are becoming unable to follow machine-produced science at all. A separate thread derailed into a complaint about blogs, including this author&\#x27;s, returning nginx 403 pages.

<details><summary>References</summary>
<ul>
<li><a href="https://scottaaronson.blog/?p=10344">Shtetl-Optimized » Blog Archive » The stochastic parrots have ...</a></li>
<li><a href="https://agihunt.info/en/p/1a1faf3ca85035bde600331be64">Scott Aaronson: Alpöge claims Anthropic models… · AGI Hunt</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#Riemann Hypothesis`, `#Lean`, `#formal verification`, `#AI for mathematics`

---

<a id="item-tech-news-12"></a>
### [Signal describes privacy work as users debate AI app access and VPN CAPTCHAs](https://signal.org/blog/protecting-your-privacy/) ⭐️ 7.0/10

Signal published a blog post describing privacy-protection work for its users. The supplied excerpt does not name a release version, describe a specific technical mechanism, or provide independent measurements, so the post is best treated as a vendor description rather than a verified new capability. The accompanying discussion focuses on AI apps that may reach Signal chats and on spam defenses that affect VPN users.

hackernews · dotcoma · Nov 20, 09:42 · [Discussion](https://news.ycombinator.com/item?id=50572348)

**「Background」** Mobile AI assistants can read on-screen content or reach app data outside an app&\#x27;s own sandbox, so screenshot blocking is only one layer of defense for a messenger. The Verge reported that Signal is blocking Gemini and Siri from reading messages, while acknowledging that this remedy is incomplete because AI agents may still retrieve app data through the device file system \(tool-1-1\).

**「Impact」** Because the supplied post includes no implementation details or rollout version, users and third-party developers cannot yet verify what effect the privacy protections have on third-party app access to Signal chats.

**「Community Discussion」** Commenters pressed on two practical tensions: one cited Meredith Whittaker&\#x27;s interview warning that AI apps can access Signal chats indirectly through contacts, while another reported that Signal&\#x27;s spam defenses produce repeated CAPTCHAs for VPN users adding contacts, pushing some privacy-sensitive users to other apps. Others asked Signal to publish its forensics findings and complained that blocking screenshots on Windows removes a basic feature.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1038390/signal-blocking-ai-agent-screenshots-mobile-app">Signal is blocking Gemini and Siri AI from reading your... | The Verge</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#secure messaging`, `#Signal`, `#AI app permissions`, `#mobile security`

---

<a id="item-tech-news-13"></a>
### [AI-designed Frostbite CPU claim prompts debate on novelty and verification](https://architectlabs.com/blog/frostbite) ⭐️ 7.0/10

Architect Labs has published a blog post claiming that an AI system discovered, designed, and verified a CPU architecture called Frostbite, which is built around interaction nets. The post frames Frostbite as an AI-originated design, but the available account provides no independent verification of its performance or implementation status. For chip architects and hardware-verification researchers, the significance depends on whether the design can be reproduced and compared against modern processors, not just described as AI-generated.

hackernews · shioyama · Nov 20, 10:01 · [Discussion](https://news.ycombinator.com/item?id=50572503)

**「Background: interaction nets and prior dataflow work」** Interaction nets \(also called the interaction calculus\) are a graph-rewriting model of computation in which reduction happens through local rewrites on a network of nodes rather than a program counter stepping through memory; a Hacker News commenter characterized these reductions as &quot;more physically-meaningful, local, topologically-smooth.&quot; Frostbite is presented as a CPU architecture built around that paradigm instead of a conventional von Neumann-style design. Commenters also pointed to earlier dataflow architecture research, such as WaveScalar from more than 20 years ago, as prior art for the general approach.

**「Impact」** Chip architects and verification teams should treat Frostbite as a claim to reproduce rather than an established result: commenters note that the comparison uses an in-order CPU baseline and a small program set, so the reported performance does not yet support conclusions against modern out-of-order designs.

**「Community Discussion」** Commenters disputed the headline&\#x27;s framing: jkhdigital argued that humans supplied the insights while AI synthesized decades of research into a coherent engineered product, and pizza234 questioned the novelty, citing WaveScalar&\#x27;s dataflow work and criticizing the in-order baseline and limited benchmark set. shioyama, who posted the item, urged readers to focus on interaction nets as a fundamentally different paradigm rather than dismiss the work outright.

<details><summary>References</summary>
<ul>
<li>There&#x27;s a model of computation called &#x27;interaction nets ... - Hacker News</li>

</ul>
</details>

**Tags**: `#CPU architecture`, `#AI-assisted design`, `#interaction nets`, `#hardware verification`, `#computer architecture`

---

<a id="item-tech-news-14"></a>
### [Levent Alpöge claims Claude-assisted Riemann Hypothesis proof](https://simonwillison.net/2026/Nov/20/levent-alpoge/) ⭐️ 7.0/10

Levent Alpöge has publicly claimed that, working with Anthropic&\#x27;s Claude, he discovered a proof of the Riemann Hypothesis and formalized the arguments without assumptions. In a short PDF statement at alpo.ge/remark.pdf, he says the method &quot;easily extends&quot; to the Generalized Riemann Hypothesis and that he expects the Extended Riemann Hypothesis to follow with more time. The quotation, relayed by Simon Willison, contains no proof details, no statement of which formal system or proof assistant was used, and no evidence of peer review or independent verification, so the claim remains an unverified personal assertion rather than a demonstrated result.

rss · Simon Willison · Nov 20, 16:30

**「Background」** The Riemann Hypothesis is the 167-year-old conjecture about the nontrivial zeros of the Riemann zeta function, and proving it would settle central questions about how the prime numbers are distributed. Levent Alpöge is a mathematician employed at Anthropic, and the argument he describes was formalized in the Lean 4 proof assistant. Such a formalization checks that each step follows from the stated assumptions, but it does not by itself establish that the formal statement matches the conjecture as it is normally posed.

**「Verification burden falls on the formalization」** The decisive test is not the announcement but the accompanying Lean archive, since the claim asserts the arguments were formalized &quot;without assumptions&quot; and that a large Lean code archive accompanies it; mathematicians and formal-verification practitioners would need to check that archive independently before treating the result as established. Because the source provides no proof details or peer review, and the claimant is an Anthropic technical staff member as well as a number theorist, the claim should be read as an unverified personal assertion until such checking occurs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/">Anthropic mathematician claims to prove Riemann hypothesis ...</a></li>
<li><a href="https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof">Anthropic mathematician claims AI helped solve a 167 ... - IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Levent_Alp%C3%B6ge">Levent Alpöge - Wikipedia</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/anthropic-167-year-old-riemann-hypothesis-claude">Claude helped prove 167-year-old Riemann hypothesis , researcher...</a></li>

</ul>
</details>

**Tags**: `#AI-assisted mathematics`, `#Riemann Hypothesis`, `#Claude`, `#formal verification`, `#research claims`

---

<a id="item-tech-news-15"></a>
### [Gemini can now control Mac apps on users&\#x27; behalf in the US](https://www.bloomberg.com/news/articles/2026-11-19/google-s-gemini-can-now-control-mac-devices-on-users-behalf) ⭐️ 7.0/10

Google Gemini has added a &quot;computer use&quot; feature that lets it click, type, navigate menus, and fill out forms on a Mac to complete tasks for the user. The feature is available to US users of the Gemini Mac app who subscribe to Google AI Plus, Pro, or Ultra. Gemini runs in a separate background window while the user continues using the main screen and cursor. Users can restrict which apps it can access, watch its actions in real time, pause it at any time, and approve key actions before they proceed.

telegram · zaihuapd · Nov 20, 02:51

**「Why desktop agents need controls」** Desktop-control agents differ from ordinary chat assistants because they operate through the same graphical interface a person uses: clicking controls, typing into fields, and moving through menus rather than calling an application programming interface. That makes app-level restrictions, live observation, and approval before sensitive steps the relevant safeguards when an agent is allowed to run in the background.

**「Impact」** Eligible subscribers can delegate repetitive desktop tasks while retaining oversight, but they need to set app restrictions and review approval prompts before letting the agent act in sensitive apps or complete consequential actions.

**Tags**: `#Google Gemini`, `#AI agents`, `#macOS`, `#desktop automation`, `#product launch`

---

<a id="item-tech-news-16"></a>
### [UK tribunal rules for Apple, opens encryption backdoor case to public](https://appleinsider.com/articles/26/11/19/uk-cant-hide-that-it-tried-ordering-apple-to-allow-access-to-user-data) ⭐️ 7.0/10

Britain&\#x27;s Investigatory Powers Tribunal ruled in Apple&\#x27;s favor and barred the Home Office from keeping secret its order demanding access to encrypted iPhone data, according to AppleInsider. The tribunal ordered that most of the case be heard in public and found the government&\#x27;s national-security rationale &quot;impractical.&quot; The Home Office confirmed it had issued a technical capability notice \(TCN\) and said the measure was meant to bring criminals to justice.

telegram · zaihuapd · Nov 20, 04:13

**「Background」** The case concerns a Technical Capability Notice \(TCN\), the mechanism the Home Office confirmed it used to demand that Apple provide access to encrypted iPhone data. Apple challenged the notice at the Investigatory Powers Tribunal, an independent judicial body, which has now rejected the Home Office&\#x27;s bid to keep the matter secret and cleared the way for a public hearing.

**「Impact」** The immediate consequence is that the Home Office&\#x27;s technical capability notice will be examined in largely public proceedings, giving researchers and privacy advocates a documented record of the government&\#x27;s demand for encrypted iPhone access. The supplied report does not specify whether the tribunal quashed the underlying notice or only rejected the secrecy order, leaving the order&\#x27;s operational status unclear.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ft.com/content/46a5cf3c-a827-477f-b72f-e7415565e729?syn-25a6b1a6=1">UK loses bid to keep Apple ‘backdoor’ order secret</a></li>
<li><a href="https://iclg.com/news/home-secretary-loses-bid-to-keep-apple-surveillance-notice-secret/">Home Secretary loses bid to keep Apple surveillance notice ...</a></li>

</ul>
</details>

**Tags**: `#苹果`, `#英国`, `#加密后门`, `#隐私安全`, `#法律裁定`

---

<a id="item-tech-news-17"></a>
### [U.S. House panel discloses nearly 880,000 AI chip export approvals to China](https://foreignaffairs.house.gov/news/press-releases/chairman-brian-mast-exercises-legislative-authority-to-publicly-release-ai-chip-license-information-for-china) ⭐️ 7.0/10

A public release of licensing data by the U.S. House Foreign Affairs Committee shows that from December 2025 through May 2026 the United States approved 879,868 AI chips for export to China, including Nvidia H200 and AMD MI325X accelerators, out of 3.444 million chips requested. Approved recipients include Tencent and ByteDance at 150,000 chips each; Alibaba, Kuaishou and Didi at 75,000 each; and miHoYo, Baidu and JD, according to the documents. The release notes that Alibaba, Tencent, Baidu and BYD appear on a U.S. list of companies tied to China&\#x27;s military, raising congressional scrutiny, and that 21 approved licenses showed no shipments as of May 11, so approvals do not equal deliveries.

telegram · zaihuapd · Nov 20, 04:25

**「Background」** Under U.S. export controls, chipmakers must obtain licenses before exporting advanced AI accelerators such as NVIDIA&\#x27;s H200 or AMD&\#x27;s MI325X to China. A license approval authorizes a potential shipment but does not establish that the chips were actually delivered.

**「Approvals are not delivered capacity」** For the Chinese cloud and AI companies named in the disclosure, the nearly 880,000 approved chips do not represent usable compute: the report says 21 approved licenses had not shipped as of May 11, so capacity planning and model-training schedules should depend on confirmed deliveries rather than approval totals.

<details><summary>References</summary>
<ul>
<li><a href="https://www.yahoo.com/news/politics/articles/license-information-ai-chips-sent-201033356.html">US signed off on sales of nearly 900,000 AI chips to China in six...</a></li>
<li><a href="https://foreignaffairs.house.gov/news/press-releases/chairman-brian-mast-exercises-legislative-authority-to-publicly-release-ai-chip-license-information-for-china">Chairman Brian Mast Exercises Legislative Authority to Publicly...</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#export controls`, `#NVIDIA`, `#AMD`, `#US-China tech`

---

<a id="item-tech-news-18"></a>
### [US tightens chip exports as India seeks AI compute growth](https://www.bloomberg.com/news/articles/2026-11-20/nvidia-scandal-fallout-india-ai-yotta-ambani-adani-am-intelligence-e2e-networks) ⭐️ 7.0/10

The post reports that U.S. restrictions on advanced chip exports to Malaysia, Thailand and Singapore are leading India&\#x27;s AI industry to position the country as a destination for redirected demand. Yotta says it will add about 100,000 GPUs over the next year, equivalent to roughly a 10% increase in India&\#x27;s existing compute, while Reliance has committed up to $110 billion and Adani $100 billion to AI infrastructure. India currently has 153 data centers, ranking 14th globally, but the report says expansion remains constrained by shortages of compute infrastructure and limited capital. The GPU target and investment figures are announced plans, not confirmed installed capacity.

telegram · zaihuapd · Nov 20, 07:31

**「Background」** The tighter export environment described here follows a mid-November U.S. proposal aimed at preventing China from obtaining advanced AI chips through Southeast Asian data centers, a route that had helped fuel the region’s data-center investment boom. Malaysia said it was seeking clarification on the new licensing requirements and on providing data-center services to third parties, leaving key implementation details unsettled.

**「Impact」** Indian AI developers and cloud buyers would gain additional domestic GPU capacity if Yotta&\#x27;s planned ~100,000 GPUs come online, but the post&\#x27;s own figure puts that at only about a 10% increase over India&\#x27;s existing compute. Yotta had already announced 20,736 liquid-cooled NVIDIA Blackwell Ultra GPUs in February 2026 as part of a $2 billion AI hub, so the new plan extends an existing buildout; actual capacity still depends on U.S. export licensing and on converting Reliance&\#x27;s and Adani&\#x27;s large infrastructure commitments into operating data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/11/17/business/southeast-asia-china-ai-chips.html">Trump’s New A.I. Chip Rules Rattle Southeast Asia - The New York...</a></li>
<li><a href="https://www.freemalaysiatoday.com/category/nation/2026/11/18/malaysia-seeks-us-clarification-on-new-ai-chip-restrictions">Malaysia seeks US clarification on new AI chip restrictions | FMT</a></li>
<li><a href="https://www.cnbc.com/2026/02/27/india-yotta-nvidia-ai-gpu-demand-data-centers-investment.html">India’s Yotta to build $2 billion AI hub with Nvidia GPUs ...</a></li>
<li><a href="https://yotta.com/press-releases/yotta-to-deploy-20000-nvidia-blackwell-ultra-gpus/">Yotta Deploys 20,000+ NVIDIA Blackwell GPUs in India</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#export controls`, `#GPU compute`, `#India`, `#data centers`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Day-0 vLLM Support for the Looped Inkling 2 Mini](https://vllm.ai/blog/2026-11-20-inkling2-mini) ⭐️ 8.0/10

rss · vLLM Blog · Nov 20, 00:00

**「Background」** Inkling 2 Mini is a 26B-total, 3.5B-active multimodal MoE whose middle 12 layers run three times per token with shared weights, yet each pass keeps its own KV and conv-state caches and passes gated messages forward. Serving it on day 0 therefore required vLLM to treat the repeated computation as a first-class caching and kernel problem rather than unrolling a custom path.

**「Solution」** The authors&\#x27; key move is to register every extra pass of a core layer as an ordinary attention layer with its own KV and conv-state cache, so the existing KV-cache manager and prefix caching work unchanged; the 24-layer model appears as 48 KV caches and 48 conv-state caches. To avoid many small launches, vLLM reads a layer&\#x27;s four messages in one attention-residual kernel, stacks the four rank-64 controllers&\#x27; weights into batched GEMMs, and fuses controller RMSNorm and the gated FP32 merge with the receiving sublayer&\#x27;s RMSNorm. It generalizes Inkling 2 Small&\#x27;s fused all-reduce, convolution, residual and RMSNorm kernels from hidden size 4,608 to 2,304 and reuses them at every tensor-parallel size, including TP1. The released TML-d24-varloop-research checkpoint exposes pass count and shared-versus-per-pass KV cache at startup, but not on fixed-loop checkpoints. On one GB200 at 4K context, forward-only decode at batch 32 rose from 3.81 ms with one pass to 5.92 ms with two and 8.11 ms with three; KV capacity fell from 352K to 233K to 175K tokens, and sharing the KV cache at three passes raised capacity only to 194K because conv states remain per pass. The authors report numerics matching the reference within its own attention-path variation, with MoE outputs bitwise identical given the same inputs.

**「Takeaway」** The broader point is that a looped MoE can be served with ordinary cache abstractions and targeted fusion, while the variable-loop checkpoint makes the latency-quality tradeoff explicit—though the evidence here is one GB200 configuration and largely qualitative accuracy reporting.

**Tags**: `#looped models`, `#vLLM`, `#KV cache`, `#MoE inference`, `#kernel fusion`

---

<a id="item-tech-blog-2"></a>
### [Why Output Caching Is Low-Leverage for LLM Costs](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 21, 00:00

**「Background」** Input caching is central to LLM inference economics because it prevents the entire conversation history from being recomputed on every message. Sean Goedecke asks whether output-side repetition should be cached in a similar way, since coding agents often repeat code snippets, evidence documents, and sample outputs in their responses.

**「Solution」** The proposed mechanism is to make models reference earlier content—for example, emitting “src/script.py:12-15” instead of reproducing the lines—and let the harness expand those references, whether through prompting or fine-tuning. The author argues that this is low leverage because it only targets visible output: based on his own agent histories, he estimates that visible output is roughly 6% of output tokens, with 50% reasoning tokens and 44% tool calls. That estimate is anecdotal, and he is only moderately confident that frontier models avoid repetition in their chain of thought. Applying Amdahl’s law, even saving two-thirds of visible tokens would reduce total output tokens by only about 4%. The remaining 94% is largely tied to model intelligence: stronger models need fewer reasoning and tool-call tokens, which can make a more expensive model cheaper overall—5x the per-token price but 6x fewer tokens.

**「Takeaway」** The author concludes that output caching optimizes a minor share of LLM output costs, while the higher-leverage path is reducing invisible reasoning and tool-call tokens through smarter models.

**Tags**: `#LLM inference economics`, `#output caching`, `#token economics`, `#Amdahl&\#x27;s law`, `#AI agents`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Beijing draft lease contract would bar deposit deductions for normal wear and tear](https://mp.weixin.qq.com/s/PmGxh5knIyxiBRhpRoJnoQ) ⭐️ 7.0/10

Beijing&\#x27;s housing authority and market regulator opened public comment on Nov 20 on a draft model residential lease contract that would bar landlords from deducting from a tenant&\#x27;s deposit for normal wear and tear caused by ordinary use. The draft, which is not yet finalized, would also require rental companies that sublet apartments to pay tenants&\#x27; deposits and rent into supervised accounts.

telegram · zaihuapd · Nov 20, 13:46

**「Background」** A &quot;model contract&quot; is a template drafted by Beijing&\#x27;s housing and market regulators that landlords and tenants can adopt when signing a lease; this revised version is still a draft open for public comment, so it is not yet in force.

**「Who is affected」** If finalized, the draft would mainly affect Beijing renters, who could cite the model contract&\#x27;s terms when disputing deductions for ordinary wear and tear, and subletting rental companies, which would have to route tenant deposits and rent through supervised accounts rather than holding the money themselves.

<details><summary>References</summary>
<ul>
<li><a href="https://news.fang.com/open/51098736.html">北 京 新规： 租 房 押 金 和 租 金 监管更靠谱！ - 房 产资讯- 房 天下</a></li>

</ul>
</details>

**Tags**: `#住房租赁`, `#押金监管`, `#北京住建委`, `#租户权益`, `#征求意见稿`

---