---
layout: default
title: "Horizon Summary: 2026-11-08 (EN)"
date: 2026-11-08
lang: en
---

> From 41 items, 13 important content pieces were selected

---

**Technology News**
1. [Inside Envision’s Planned 800MW Galaxy AI Campus](#item-tech-news-1) ⭐️ 8.0/10
2. [Fan-made Need for Speed Underground 2 port runs online in the browser](#item-tech-news-2) ⭐️ 7.0/10
3. [Asahi Linux 7.3 report claims first same-day Fedora Asahi Remix release](#item-tech-news-3) ⭐️ 7.0/10
4. [Claude Code settings exposed secrets mainly when committed](#item-tech-news-4) ⭐️ 7.0/10
5. [Analysis: macOS daemons build undocumented personal graph](#item-tech-news-5) ⭐️ 7.0/10
6. [Analysis Questions Whether Strong DeepSWE Scores Hold Up](#item-tech-news-6) ⭐️ 7.0/10
7. [Coldframe honeypot mimics Danfoss and Dixell fridge controllers](#item-tech-news-7) ⭐️ 7.0/10
8. [Claude Code reportedly leaks login emails; Anthropic plans context removal](#item-tech-news-8) ⭐️ 7.0/10
9. [Apple preprint describes HALO humanoid control system using two Qwen models](#item-tech-news-9) ⭐️ 7.0/10
10. [GitHub&\#x27;s Rubicon Git storage targets 7,200 pushes per second](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Berkshire Hathaway Doubles Buybacks as Third-Quarter Earnings Fall](#item-finance-news-1) ⭐️ 7.0/10
2. [Anthropic reportedly plans IPO roadshow next week, listing in week of Nov. 16](#item-finance-news-2) ⭐️ 7.0/10
3. [SoftBank and ABB Weigh China Carve-Out to Salvage Robotics Deal](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Inside Envision’s Planned 800MW Galaxy AI Campus](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) ⭐️ 8.0/10

SemiAnalysis visited Galaxy, an Envision-owned AI datacenter campus in Ulanqab, Inner Mongolia, planned for up to 800MW of IT capacity and described as roughly the size of Stargate Abilene’s core campus. The first 120MW phase was delivered within a year at about one-fifth of US costs, while the rest of the campus remained under construction; all four phases are built-to-suit for two unnamed internet giants. Envision’s vertical integration extends beyond the datacenter: it builds dedicated wind farms and a power line, has a blade factory across the road, designed and integrated low-voltage power modules and an 800V system, manufactured battery storage that smooths the load, and co-designed the prefabricated substation. The surrounding Chahar High-tech Zone had nearly 30,000 construction workers across 22 datacenter projects, according to a local report cited by SemiAnalysis.

rss · Semianalysis · Nov 7, 19:01

**「Background」** SemiAnalysis had previously published a primer on China&\#x27;s datacenter market, noting that Chinese builders rarely use fully modular construction even as costs keep falling—context this site visit returns to. Envision separately said on Nov. 2, 2026 that the Galaxy campus&\#x27;s integrated 800V DC power system was powering live workloads, calling it the first commercial deployment of its kind in a large-scale AI datacenter.

**「Impact」** For datacenter developers and AI infrastructure planners, Galaxy provides a concrete schedule and cost benchmark: 120MW delivered in about a year at roughly 20% of US costs, with much of the power and electrical equipment supplied by the campus owner. The report does not establish that this model can be replicated in markets with different grid interconnection, permitting, or supplier conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://datacentremagazine.com/news/envisions-800v-dc-data-centre-world-first-in-ulanqab-china">Envision’s 800V DC Data Centre World-First in Ulanqab, China</a></li>
<li><a href="https://www.unite.ai/envision-deploys-sst-based-800v-dc-power-at-ulanqab-ai-data-center/">Envision Deploys SST-Based 800V DC Power at Ulanqab AI Data ...</a></li>

</ul>
</details>

**Tags**: `#AI datacenters`, `#China AI infrastructure`, `#datacenter economics`, `#vertical integration`, `#compute buildout`

---

<a id="item-tech-news-2"></a>
### [Fan-made Need for Speed Underground 2 port runs online in the browser](https://nfsu2.xyz/) ⭐️ 7.0/10

A fan-run browser version of Need for Speed Underground 2 is playable at nfsu2.xyz, including online multiplayer, according to the project listing that drew strong Hacker News attention. The port is described as a WebGPU-based reverse-engineering effort that puts a full 3D racing game in the browser, with commenters reporting that it runs on phones as well as desktops. The supplied material includes no technical write-up from the project itself, so how the port was built and how closely it matches the original are not independently documented. Its legal status is unsettled: the game is treated as abandonware, and commenters expect a takedown request now that the site is popular.

hackernews · fluxusars · Nov 7, 09:36 · [Discussion](https://news.ycombinator.com/item?id=50403052)

**「Background」** The browser version of Need for Speed: Underground 2 is a fan-run build, and the project describes itself as not affiliated with or endorsed by Electronic Arts. It runs through static WebAssembly recompilation in Chrome and Firefox, which is the technical precondition for playing the game in a tab rather than through a native install.

**「Compatibility and legal risk」** Linux users on Chromium reportedly need to enable unsafe WebGPU features before the game will run, a concrete compatibility hurdle for part of the audience. Because the site is fan-hosted and unlicensed, anyone trying it should treat availability as temporary rather than a durable way to play the game.

**「Community discussion」** Commenters traded nostalgia and reported that the browser version works smoothly on hardware where the retail release is now largely unplayable, with one describing crowded online sessions full of burnouts and honking. The sharpest disagreement was over legitimacy: one commenter called soliciting donations for copyrighted content dubious, while another argued the game is unavailable commercially and hoped the project would be left alone.

<details><summary>References</summary>
<ul>
<li><a href="https://thegametake.com/guides/need-for-speed-browser">Need for Speed Browser Ports: Fan Projects, Legal Notes ...</a></li>
<li><a href="https://pro-gamer.gg/need-for-speed-underground-2-playable-browser-120-fps-webgpu-multiplayer-free-roam/">Need for Speed: Underground 2 in Browser: 120 FPS &amp; WebGPU ...</a></li>

</ul>
</details>

**Tags**: `#browser gaming`, `#WebGPU`, `#reverse engineering`, `#game preservation`, `#abandonware`

---

<a id="item-tech-news-3"></a>
### [Asahi Linux 7.3 report claims first same-day Fedora Asahi Remix release](https://asahilinux.org/2026/11/progress-report-7-3/) ⭐️ 7.0/10

Asahi Linux&\#x27;s 7.3 progress report says Fedora Asahi Remix shipped on the same day as Fedora Linux 45, which was released on 3 November — the first time the project says it has managed a same-day release alongside upstream Fedora. The report, published 7 November 2026, also says the project had been made aware of &quot;multiple attempts to exploit our permissive licensing to hijack our work,&quot; aimed at replacing the project and monetising Linux on Apple Silicon. USB-C display output remains unsupported, a gap commenters describe as their main reason for not installing Asahi on Apple laptops. The report covers continued Linux-on-Apple-Silicon work more broadly, but the supplied item contains no full text, so further specifics could not be verified.

hackernews · ackyshake · Nov 7, 05:20 · [Discussion](https://news.ycombinator.com/item?id=50401867)

**「Background」** Asahi Linux is a community effort to bring Linux to Apple Silicon Macs, and Fedora Asahi Remix is its Fedora-based distribution. Before this cycle, the project had not managed to ship a new Remix on the same day as an upstream Fedora release; the Linux 7.3 report calls the Fedora Linux 45 release the first such same-day shipment.

**「Downstream licensing checks」** Developers and distributions that build on Asahi Linux code should review the project&\#x27;s relicensing terms: the report says Asahi moved to relicense its repositories after multiple attempts to exploit its permissive license to hijack the work and monetize Linux on Apple Silicon. That changes the obligations forks may face when redistributing or modifying Asahi components.

**「Community discussion」** A longtime financial backer welcomed the same-day Fedora release as &quot;a wonderful thing to read,&quot; while another commenter said the lack of USB-C display output is the single blocker preventing them from installing Asahi on a MacBook Air and questioned why support for newer CPUs was prioritised. Others asked whether the licensing warning referred to Omarchy and said they were surprised the work had ever been MIT-licensed rather than GPL, and one commenter promoted a separate project, Gravity Linux, claiming Vulkan 1.4 support and suspend-to-RAM that &quot;no version of Asahi supports.&quot;

<details><summary>References</summary>
<ul>
<li><a href="https://asahilinux.org/2026/11/progress-report-7-3/">Progress Report: Linux 7.3 - Asahi Linux</a></li>
<li><a href="https://braindetox.kr/en/posts/asahi_linux_progress_report_linux_7_3.html">Asahi Linux 7.3 Report: M3 GA, Partial Thunderbolt, GPL Move</a></li>
<li><a href="https://www.linux.org.hk/archive/20261107-9177-asahi-linux-relicenses-all-repositories.html">Hong Kong Linux User Group - 香港Linux用家協會 (HKLUG) &gt; Archi...</a></li>
<li><a href="https://lwn.net/Articles/1105946/">Why the licensing change? - lwn.net</a></li>

</ul>
</details>

**Tags**: `#Asahi Linux`, `#Apple Silicon`, `#Linux`, `#Open Source`, `#Fedora`

---

<a id="item-tech-news-4"></a>
### [Claude Code settings exposed secrets mainly when committed](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 7.0/10

A security report identified secrets in 1,122 public GitHub files associated with Claude Code&\#x27;s local settings, after scanning committed \`.claude/settings.local.json\` files for commands containing keys or passwords. The exposure is not caused by pressing “Don&\#x27;t Ask Again” alone: it requires a user to commit the local settings file with manually approved commands that contain secrets, as commenters and Claude Code team member Boris Cherny noted. Cherny said Claude Code has historically not scrubbed secrets and is looking into prevention, while stressing that \`.claude/settings.local.json\` is meant to stay local and is automatically gitignored when Claude creates it; the reported files were manually created and checked in.

hackernews · shmulc · Nov 7, 20:45 · [Discussion](https://news.ycombinator.com/item?id=50407882)

**「How the settings file stores approvals」** Claude Code records per-project permission decisions in .claude/settings.local.json; choosing &quot;Yes, and don&\#x27;t ask again&quot; writes the full approved command into that file, including any password or API key typed inline, so the agent does not prompt for it again. The file is intended to remain local and is automatically gitignored when Claude creates it, meaning the copies Apiiro scanned were created and committed to repositories by users rather than generated and published by default.

**「Impact」** Developers and teams using Claude Code should avoid committing \`.claude/settings.local.json\`; if such a file was already pushed, they should audit repository history and rotate any credentials embedded in approved commands, since deleting the file does not remove the secret from Git history.

**「Community discussion」** Commenters said the headline overstated the risk, explaining that “Don&\#x27;t Ask Again” alone does not expose passwords: the chain requires committing local Claude settings containing manually approved commands with secrets and then publishing the repository. Others described mitigations including per-task ephemeral VMs, API proxies that restrict access to external services, and password-manager CLI access that requires fingerprint approval.

**Tags**: `#Claude Code`, `#secrets management`, `#GitHub security`, `#AI coding agents`, `#developer tooling`

---

<a id="item-tech-news-5"></a>
### [Analysis: macOS daemons build undocumented personal graph](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) ⭐️ 7.0/10

An analysis published on 8rank.ai argues that macOS ships undocumented daemons that build a personal knowledge graph of users, their contacts, and how those people relate to and communicate with one another. The article, as quoted in the discussion, says every Mac since 2022 ships a pair of these daemons and ties the capability to Apple Intelligence. These are the analysis&\#x27;s claims, not an Apple confirmation or an independent measurement.

hackernews · infwhispers · Nov 7, 09:46 · [Discussion](https://news.ycombinator.com/item?id=50403097)

**「Background」** Coverage of the analysis identifies the two daemons as knowledgeconstructiond and intelligenceplatformd, which it says have shipped since macOS 13 in 2022 and build a queryable on-device store—a &quot;personal knowledge graph&quot;—that large language models retrieve from to power Apple Intelligence personalization. In that framing, the graph is assembled from local content about user identity, relationships, communications, and behavior rather than from a single explicit user profile; these claims come from the researchers&\#x27; analysis, not an Apple disclosure.

**「Impact」** Until Apple documents the daemons, users and security auditors who want to know what relationship data macOS records must rely on reverse engineering rather than platform documentation.

**「Discussion」** Commenters treated the finding as plausible but differed on its social cost: one said such memory would be fascinating if opt-in yet is now exhausting, while another noted that Photos already recognizes loved ones and pets. A third argued that LLM-assisted audits make hidden telemetry easier to find, though changing the behavior remains harder.

<details><summary>References</summary>
<ul>
<li><a href="https://techplanet.today/post/apples-hidden-personal-knowledge-graph-understanding-macoss-undocumented-family-classifier">Apple&#x27;s Hidden Personal Knowledge Graph: Understanding macOS ...</a></li>
<li><a href="https://www.worldcybernews.com/articles/1884">macOS Builds Undocumented Personal Knowledge Graph Since ...</a></li>
<li><a href="https://todayforai.com/en/items/art-e972e632-f9c">Researchers Expose Undocumented Personal Knowledge Graph ...</a></li>

</ul>
</details>

**Tags**: `#Apple Intelligence`, `#macOS internals`, `#privacy`, `#reverse engineering`, `#personal knowledge graph`

---

<a id="item-tech-news-6"></a>
### [Analysis Questions Whether Strong DeepSWE Scores Hold Up](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 7.0/10

MaxxBench published an analysis arguing that strong DeepSWE benchmark scores are not necessarily trustworthy, citing benchmark bugs and apparent overfitting. The critique targets developers and researchers who use DeepSWE results to compare models, particularly smaller &quot;flash&quot;-style variants. The supplied material covers the article&\#x27;s argument and reader reaction, not an independent reproduction or a response from the benchmark&\#x27;s maintainers.

hackernews · antiuniverse · Nov 7, 17:19 · [Discussion](https://news.ycombinator.com/item?id=50406222)

**「Background」** DeepSWE is a long-horizon software-engineering benchmark for coding agents, with tasks written from scratch across 91 repositories and five languages and hand-written verifiers that check software behavior rather than implementation details. The project describes it as contamination-free and more realistic than prior coding benchmarks: prompts are about half the length of SWE-bench Pro&\#x27;s, while solutions require roughly 5.5 times more code and about twice the output tokens. That design is meant to make high DeepSWE scores meaningful, so MaxxBench&\#x27;s analysis asks whether a strong score reflects real capability or artifacts of benchmark bugs and overfitting.

**「Impact」** Teams using DeepSWE rankings should treat top scores as provisional and inspect the evaluation harness: one commenter reads the article as advising against &quot;max mode,&quot; and another flags an evaluation framework that runs inference with an API key inside the sandbox the agent can access.

**「Community Discussion」** Commenters focused on mechanism and setup rather than the headline score. peri-cl argued that smaller models collapse most on the benchmark, rao-v attributed that pattern to overfitting to simpler RL environments rather than labs training directly on the test, and kqr criticized an evaluation framework for running inference with an API key inside the isolated environment the agent harness can access.

<details><summary>References</summary>
<ul>
<li><a href="https://deepswe.datacurve.ai/">DeepSWE measures frontier coding agents on original, long-horizon...</a></li>
<li><a href="https://deepswe.lol/">DeepSWE — Long-Horizon Software Engineering Benchmark</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#benchmark validity`, `#DeepSWE`, `#overfitting`, `#AI research`

---

<a id="item-tech-news-7"></a>
### [Coldframe honeypot mimics Danfoss and Dixell fridge controllers](https://github.com/hedgerow-dev/coldframe) ⭐️ 7.0/10

Coldframe is a single-file Python honeypot, written with only the standard library, that impersonates Danfoss AK-SM 800A and Dixell XWEB supermarket refrigeration controller interfaces. Its author says Shodan identifies both personas as real devices rather than honeypots, because header ordering, page titles, certificate fields and TLS versions were copied from Shodan records of real units; the Dixell persona sends no Server header and pads its page to exactly 8,202 bytes. It recognises CVE-2025-41450, the Danfoss &quot;code of the day&quot; login bypass, records whether a submitted code is correct for that day, and tags attempts against three other Danfoss CVEs and the XWEB vulnerabilities, while default logins lead to a fake store dashboard with defrost buttons. After about a day with two instances live, the author reports only generic scanners and Shodan&\#x27;s crawler, refrigerator.census.shodan.io, so the detection value is self-reported rather than demonstrated. The tool builds on eppser/danfoss-ak-sm-decoy and public research by Synacktiv, Claroty and Ironhackers.

hackernews · hedgerow-dev · Nov 7, 17:27 · [Discussion](https://news.ycombinator.com/item?id=50406292)

**「The vulnerability behind the decoy」** Coldframe&\#x27;s main target is the Danfoss AK-SM 8xxA series, the same controller family the project impersonates. CVE-2025-41450, which the honeypot logs and evaluates, is an improper authentication flaw affecting Danfoss AK-SM 8xxA devices prior to firmware version 4.2, according to the NVD entry. That flaw underlies the &quot;code of the day&quot; login bypass the honeypot is built to detect.

**「Defender takeaway」** For ICS defenders, Coldframe offers a standard-library Python decoy that mimics Danfoss AK-SM 800A and Dixell XWEB fingerprints and logs attempts against CVE-2025-41450 and other known flaws, so it can be deployed as an early-warning sensor without extra dependencies. Its first day of operation produced only generic scanners and Shodan crawler traffic, so it has not yet yielded evidence of targeted exploitation.

**「Community discussion」** Commenter supriyo-biswas questioned relying on Shodan for fidelity, arguing that many exposed devices found there are themselves honeypots or already compromised, and suggested acquiring a real vulnerable unit to probe instead. The author responded that blood banks have also reportedly been targeted, and argued that because supermarkets have no security teams, VPNs, patching and strong passwords need to ship as vendor or installer defaults rather than depend on a store manager.

<details><summary>References</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-41450">NVD - CVE - 2025 - 41450</a></li>
<li><a href="https://www.tenable.com/cve/CVE-2025-41450">CVE - 2025 - 41450 | Tenable</a></li>

</ul>
</details>

**Tags**: `#ICS security`, `#honeypots`, `#refrigeration controllers`, `#CVE-2025-41450`, `#open source`

---

<a id="item-tech-news-8"></a>
### [Claude Code reportedly leaks login emails; Anthropic plans context removal](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 7.0/10

Anthropic plans to remove users&\#x27; login email from Claude Code&\#x27;s model context in the next release after developers reported the tool was placing the address in web requests, according to an Anthropic engineer responding in a GitHub issue. The engineer said the email had been added to context to stop Claude from inventing author names; reports since July say addresses were sent to sites including Wikipedia and the U.S. Securities and Exchange Commission. Version 2.1.317 added a block, but the source says it can be bypassed with a Python script, so removing the address from model context remains a planned fix rather than a shipped one. One developer said the exposure resulted in large amounts of scam email.

telegram · zaihuapd · Nov 7, 08:09

**「Background」** Model context is the information Claude Code feeds the model for a session, so anything placed there can be carried into model-generated actions. The report says Anthropic had added the user&\#x27;s login email to that context to stop Claude from inventing an author name; the leak was first reported in July, with requests reaching Wikipedia and the U.S. Securities and Exchange Commission.

**「Impact」** For developers using Claude Code&\#x27;s web search, version 2.1.317 is not a reliable privacy boundary: the reported Python-script bypass means login email exposure can continue until the next release removes the address from model context, so users should not treat the current guard as a complete remediation.

**Tags**: `#Claude Code`, `#privacy leak`, `#security vulnerability`, `#AI coding tools`, `#Anthropic`

---

<a id="item-tech-news-9"></a>
### [Apple preprint describes HALO humanoid control system using two Qwen models](https://weibo.com/1642634100/RqjjGllvw) ⭐️ 7.0/10

Apple researchers reportedly submitted a preprint to arXiv on November 4 describing HALO, a three-layer autonomous control system for humanoid robots, and said it was validated on a Unitree G1 by transferring motions learned in simulation to an unfamiliar real room. The top layer uses Qwen3.6-35B-A3B to orchestrate tasks, the middle layer uses Qwen3.5-2B to generate motions, and the bottom layer is a reinforcement-learning-trained motion tracker. The team reportedly released code for data generation, model training, and deployment, but the item comes from a social-media aggregator with no direct primary link, so the paper and code release have not been independently confirmed here.

telegram · zaihuapd · Nov 7, 13:35

**「Background」** The Unitree G1 used for the reported validation is a commercially listed humanoid platform with 23–43 joints, and Unitree publishes reinforcement-learning environments for its G1-29dof configuration built on IsaacLab. Those environments provide a simulated training and evaluation setup that precedes deployment on the physical robot, which is the setting for sim-to-real control work.

**「Impact」** For robotics researchers, the reported release of the data-generation, training, and deployment code would make the HALO pipeline inspectable and potentially reproducible; whether that code is actually available and whether the G1 results can be replicated remain unverified because no primary link was provided.

<details><summary>References</summary>
<ul>
<li><a href="https://shop.unitree.com/">UnitreeRobotics-More than Wisdom, Be with You</a></li>
<li><a href="https://github.com/unitreerobotics/unitree_rl_lab">GitHub - unitreerobotics/ unitree _rl_lab: This is a repository for...</a></li>

</ul>
</details>

**Tags**: `#humanoid robotics`, `#Apple`, `#Qwen`, `#sim-to-real`, `#open-source code`

---

<a id="item-tech-news-10"></a>
### [GitHub&\#x27;s Rubicon Git storage targets 7,200 pushes per second](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 7.0/10

GitHub has introduced a new Git storage architecture, code-named Rubicon, that stores Git objects in Azure Blob Storage, manages reference state through Ref-CAS, and uses virtual replicas to handle reads and writes with background nodes compacting packfiles. In internal tests, GitHub says the system supported 5,000 agents collaborating on a single repository at 7,200 pushes per second while keeping read latency low, a scenario aimed at high-concurrency AI-agent workflows. Those figures are vendor-reported internal test results rather than independently measured production numbers, and Rubicon is currently in a limited private preview, with GitHub saying it will expand availability gradually.

telegram · zaihuapd · Nov 7, 14:12

**「Background」** Every Git push adds a pack to object storage, so a workload with thousands of agents writing to one repository concentrates pressure on storage and on the compute that compacts those packs. GitHub&\#x27;s architecture post describes the design response as decoupling storage from compute and moving compaction to background nodes, with Git objects kept in Azure Blob Storage and reference state in a replicated Ref-CAS journal.

**「Availability gap for agent workloads」** Because Rubicon remains in limited private preview, with a broader rollout reported for early next year, the 7,200-push-per-second figures are not yet available to ordinary repositories, and teams planning high-concurrency agent workflows cannot treat that throughput as a current production guarantee. Organizations building always-on agents against a single repository should plan around access to the preview rather than assume the capacity is generally reachable today.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/">Inside GitHub &#x27;s new Git storage architecture - The GitHub Blog</a></li>
<li><a href="https://dzen.ru/a/au6qec3gh2vpaVUH">GitHub описала Rubicon , новое хранилище Git для... | Дзен</a></li>
<li><a href="https://todayforai.com/en/items/art-8197a014-146">GitHub Unveils Rubicon Storage Architecture for 5,000 ...</a></li>

</ul>
</details>

**Tags**: `#GitHub`, `#Git storage`, `#distributed systems`, `#AI agents`, `#cloud architecture`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Berkshire Hathaway Doubles Buybacks as Third-Quarter Earnings Fall](https://www.cnbc.com/2026/11/07/berkshire-hathaway-q3-2026-earnings-buybacks.html) ⭐️ 7.0/10

Berkshire Hathaway repurchased $9.6 billion of its own stock in the third quarter, more than double the $4.5 billion bought in the second quarter, as operating earnings fell 5.8% to $12.705 billion from $13.485 billion a year earlier and overall earnings dropped 28% to $22.112 billion. Insurance underwriting profit fell 43% to $1.352 billion, while the railroad, energy and manufacturing businesses all posted higher earnings.

rss · CNBC Finance · Nov 7, 15:23

**「Background」** Greg Abel became Berkshire Hathaway’s CEO in January 2026, succeeding Warren Buffett, making this an early quarterly report under his leadership.

**「Shareholder impact」** The $9.6 billion buyback is a direct transfer of cash to shareholders who sold, and it came as Berkshire’s insurance underwriting profit weakened.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cbsnews.com/news/greg-abel-berkshire-hathaway-warren-buffett-successor/">Greg Abel takes over as CEO of Berkshire Hathaway. What to ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/07/berkshire-hathaway-q3-2026-earnings-buybacks.html">Berkshire Hathaway (BRK.A) earnings Q 3 2026</a></li>

</ul>
</details>

**Tags**: `#Berkshire Hathaway`, `#share buybacks`, `#earnings`, `#insurance`, `#capital allocation`

---

<a id="item-finance-news-2"></a>
### [Anthropic reportedly plans IPO roadshow next week, listing in week of Nov. 16](https://www.theinformation.com/briefings/anthropic-proceed-ipo-roadshow-next-week) ⭐️ 7.0/10

Anthropic reportedly plans to begin its IPO roadshow next week and list shares in the week of Nov. 16, before the U.S. Thanksgiving holiday, according to people familiar with the matter. Market expectations before the roadshow had put the company at a $1.5 trillion valuation and a raise of more than $80 billion, though recent concerns about AI stocks and spending could push it to seek a lower valuation.

telegram · zaihuapd · Nov 7, 01:27

**「Background」** An IPO roadshow is the pre-listing pitch to prospective investors; Anthropic&\#x27;s follows its public S-1 filing with the U.S. Securities and Exchange Commission on Oct. 26, which gave investors their clearest look yet at its finances.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fxstreet.com/news/anthropic-ipo-filing-reveals-rapid-growth-as-investors-weigh-an-80-billion-loss-202610270748">Anthropic IPO filing reveals rapid growth as investors weigh an $ 80 ...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI financing`, `#valuation`, `#market volatility`

---

<a id="item-finance-news-3"></a>
### [SoftBank and ABB Weigh China Carve-Out to Salvage Robotics Deal](https://www.bloomberg.com/news/articles/2026-11-07/softbank-abb-weigh-china-carve-out-to-salvage-robotics-deal) ⭐️ 7.0/10

SoftBank and ABB are considering carving out the China portion of ABB&\#x27;s robotics business into an independent entity with a different ownership structure, led by SoftBank, to salvage their $5.4 billion acquisition after China&\#x27;s foreign-investment security review office halted the deal on Thursday. People familiar with the matter said the plan could fail and that ABB is weighing other options, including finding another buyer, with the business potentially valued at $2 billion to $3 billion; both companies declined to comment.

telegram · zaihuapd · Nov 7, 11:24

**「Background」** The carve-out idea follows China’s foreign-investment security review office blocking SoftBank’s $5.4 billion purchase of ABB’s robotics unit, with reporting linking the veto to concerns about robot data being sent overseas for AI training.

<details><summary>References</summary>
<ul>
<li><a href="https://www.swissinfo.ch/eng/workplace/china-blocks-softbanks-5-4bn-takeover-of-abbs-robotics-division/92331403">China blocks SoftBank ’s $ 5 . 4 bn takeover of ABB ’s robotics division</a></li>
<li><a href="https://sguys99.github.io/global-ai-news/en/article/1383/">Chinese regulators block SoftBank &#x27;s $ 5 . 4 billion ABB Robotics ...</a></li>
<li><a href="https://www.abb.com/global/en/news/140154/update-on-divestment-of-abb-robotics">Update on divestment of ABB Robotics</a></li>

</ul>
</details>

**Tags**: `#并购交易`, `#监管审查`, `#机器人`, `#软银`, `#ABB`

---