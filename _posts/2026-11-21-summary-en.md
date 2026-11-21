---
layout: default
title: "Horizon Summary: 2026-11-21 (EN)"
date: 2026-11-21
lang: en
---

> From 29 items, 13 important content pieces were selected

---

**Technology News**
1. [Lean formalization of the Riemann Hypothesis certified](#item-tech-news-1) ⭐️ 9.0/10
2. [Zhejiang University demonstrates QRAM on superconducting chip](#item-tech-news-2) ⭐️ 9.0/10
3. [Trump threatens large tax on US firms building AI data centers abroad](#item-tech-news-3) ⭐️ 8.0/10
4. [Microsoft brings RDMA over USB4 to Windows for multi-PC AI inference](#item-tech-news-4) ⭐️ 8.0/10
5. [GPGME/GnuPG flaw hits pre-2.3.0 versions, RCE claim disputed](#item-tech-news-5) ⭐️ 7.0/10
6. [USB hub in a monitor throttled Ethernet download speed](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenAI cuts reasoning-chain extraction rate to 0.2% with anti-distillation defenses](#item-tech-news-7) ⭐️ 7.0/10
8. [TSMC halts 16nm-and-below orders for Chinese firms](#item-tech-news-8) ⭐️ 7.0/10
9. [OpenRouter warns MiniMax prompts may have been read by third parties](#item-tech-news-9) ⭐️ 7.0/10
10. [Daraxonrasib First-Line Data: Tumor Disappearance in About 1 in 12 of 61 Patients](#item-tech-news-10) ⭐️ 7.0/10

**Technology Blog**
1. [Why output caching can&\#x27;t meaningfully cut LLM costs](#item-tech-blog-1) ⭐️ 7.0/10
2. [Avoiding Blunders Beats Clever Code](#item-tech-blog-2) ⭐️ 6.0/10

**Financial News**
1. [Trump backs Lutnick on China chip sales and urges Nvidia CEO Huang to apologize and return](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Lean formalization of the Riemann Hypothesis certified](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

On November 20, 2026, Levent Alpöge published a Lean formalization of the Riemann Hypothesis spanning roughly 17 million lines of code, according to the source report. The next day, Lean FRO and the Mathlib Initiative jointly certified that both the statement and its proof are correct: the statement matches Mathlib&\#x27;s RiemannHypothesis definition, the repository compiles without errors, and multiple independent proof checkers validated the proof. The report describes this as a Lean verification of the Riemann Hypothesis, though the source summary is discussion-based and does not detail the proof&\#x27;s mathematical argument or the checkers used.

hackernews · g-b-r · Nov 21, 14:36 · [Discussion](https://news.ycombinator.com/item?id=50589618)

**「Background」** Lean is an interactive theorem prover whose proofs are checked by a small kernel, and Mathlib is its community library of formalized mathematics; a formal proof is only meaningful if the encoded statement faithfully matches the intended theorem. Mathlib already contained a RiemannHypothesis definition, which is why the certifiers&\#x27; confirmation that Alpöge&\#x27;s statement agrees with it is a decisive part of the announcement.

**「Impact」** For mathematicians and formalization users, the certification rests on statement-to-Mathlib agreement and a clean compile, so anyone relying on the result should check which Mathlib version was pinned and whether the independent checkers were run against the same statement. If the reported scale is accurate, the work also represents a large body of formalized mathematics beyond the theorem itself, which the community discussion flags as a separate contribution.

**「Community discussion」** Commenters argued that the risk of a proof exploiting a kernel bug is now very small, since several checker implementations exist in different languages with varying consistency proofs, though one noted that a fake Collatz refutation previously passed an independent checker and questioned how independent the checkers really are. Others credited Levent Alpöge for the result and highlighted that, per their understanding, the proof required formalizing a huge chunk of modern mathematics, making the formalization scope itself a major outcome.

**Tags**: `#formal-verification`, `#lean`, `#riemann-hypothesis`, `#ai-theorem-proving`, `#mathematics`

---

<a id="item-tech-news-2"></a>
### [Zhejiang University demonstrates QRAM on superconducting chip](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 9.0/10

Zhejiang University researchers report the first real-machine implementation of a quantum random access memory \(QRAM\) on their own superconducting quantum chip, &quot;Tianmu-2,&quot; with results published in Nature Physics. On-chip prototypes retrieved 4-bit and 8-bit data with accuracies of 80.9% and 60.4%, respectively, while using circuit depths more than 30% lower than an unoptimized scheme. The team also reports the first verification that the architecture has local noise resilience. Next steps are scaling up QRAM research.

telegram · zaihuapd · Nov 21, 08:31

**「Background」** QRAM is the quantum-computing analogue of random-access memory: a circuit that can fetch a data entry indexed by a quantum superposition of addresses, so that a quantum algorithm can read many table entries in parallel. A practical QRAM has been a long-standing hardware goal because the addressing circuitry must stay coherent and fault-tolerant while fanning out to many stored qubits.

**「Impact」** The 8-bit retrieval accuracy of 60.4% — well below the 80.9% seen at 4 bits — shows that scaling QRAM to practical address widths remains the central obstacle, so the near-term value is as a testbed for hardware-level QRAM designs rather than a usable memory for quantum algorithms.

**Tags**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#research breakthrough`, `#Nature Physics`

---

<a id="item-tech-news-3"></a>
### [Trump threatens large tax on US firms building AI data centers abroad](https://apnews.com/article/trump-artificial-intelligence-data-centers-f1ac03b73d13445400eeed8631d9d879) ⭐️ 8.0/10

At a White House press conference on November 20, Trump said he plans to impose a &quot;large tax&quot; on US tech companies that build AI data centers overseas, aiming to keep data centers in the United States and preserve AI competitiveness against China. He said he had not yet disclosed the plan to officials within his administration. Trump also urged US communities to accept data center projects, suggesting they negotiate with developers for payments, amid local opposition over electricity demand and noise. No tax rate, legal basis, or implementation timeline was provided, so this remains a stated intention rather than a specified policy.

telegram · zaihuapd · Nov 21, 03:26

**「Context: local pushback and midterms」** Trump&\#x27;s remarks come after opposition to data centers became a central issue in the US midterm elections, in which Republicans lost their majorities in both the House and Senate, according to ABC News reporting. Local objections have centered on electricity demand and noise, which is the backdrop for Trump&\#x27;s urging that communities negotiate payments from developers.

**「Impact」** If pursued, the plan would add a tax consideration to overseas site selection for US tech companies&\#x27; AI compute buildouts, while offering no defined rate or timing for firms to plan around. The call for communities to negotiate developer payments signals that local opposition over power use and noise remains a practical hurdle for domestic siting.

<details><summary>References</summary>
<ul>
<li><a href="https://www.abc.net.au/news/2026-11-21/trump-vows-tax-companies-building-data-centres-overseas/107412162">Donald Trump vows to tax US companies building data centres ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#technology policy`, `#US-China competition`, `#tax policy`

---

<a id="item-tech-news-4"></a>
### [Microsoft brings RDMA over USB4 to Windows for multi-PC AI inference](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

Microsoft released a Windows developer preview of RDMA over USB4 that lets multiple PCs share memory and GPU compute to run a single local AI model without dedicated network cards or switches. In a demo, three AMD Ryzen AI Max+ 395 machines running a 4-bit quantized Qwen3-235B-A22B model produced about 18.5 tokens per second. The capability is described as rolling out through Windows Insider, though the source does not specify timing or hardware requirements.

telegram · zaihuapd · Nov 21, 06:13

**「Background」** RDMA \(remote direct memory access\) lets one machine read and write another&\#x27;s memory with low overhead, and is typically used over specialized fabrics such as InfiniBand or RoCE in data centers. USB4 offers high-bandwidth peer-to-peer links between consumer PCs, so this preview applies RDMA-style shared memory to ordinary USB4 connections rather than data-center networking hardware.

**「Impact」** Developers with multiple USB4-equipped PCs, such as Ryzen AI Max+ 395 systems, could pool memory and GPU resources to run models larger than one machine can hold locally. Because this is a developer preview delivered via Windows Insider, it should be treated as experimental, and the source does not confirm which Windows builds or USB4 implementations are supported.

**Tags**: `#RDMA over USB4`, `#Windows`, `#local AI inference`, `#distributed computing`, `#hardware`

---

<a id="item-tech-news-5"></a>
### [GPGME/GnuPG flaw hits pre-2.3.0 versions, RCE claim disputed](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 7.0/10

A disclosed flaw in GPGME/GnuPG affects versions before 2.3.0, according to the supplied item. One commenter says all software using GPGME prior to 2.3.0 is affected, whether as a shared library, DLL or statically linked build, citing Gpg4win, GnuPG Desktop, most mail clients, many XMPP clients, Samba and Flatpak as examples. The headline&\#x27;s code-execution framing is contested: another commenter says the issue is a double-free bug rather than an RCE chain. The item&\#x27;s analysis notes that the supplied technical evidence is incomplete, so the precise exploitation path is not established here.

hackernews · gdgghhhhh · Nov 21, 08:32 · [Discussion](https://news.ycombinator.com/item?id=50587208)

**「Background」** The flaw is tracked as CVE-2026-129975 and affects all software using GPGME before version 2.3.0, whether the library is loaded as a shared library, Windows DLL, or statically linked into the program. Per the advisory, Johan Carlsson discovered the bug and GitLab notified the GnuPG project on 2026-11-12; the initially planned 2026-11-25 coordinated disclosure date was moved earlier to 2026-11-20.

**「Who Is Affected and What to Patch」** Any software that links GPGME before 2.3.0 — as a shared library, DLL, or static build — inherits the flaw, including most mail clients, many XMPP clients, Samba, Flatpak, and Gpg4win, GnuPG Desktop, and GnuPG VS-Desktop. The advisory says remote code execution cannot be ruled out, and GitLab patched its Omnibus package because signed-commit paths run through GPGME; as of disclosure the project reported no known exploitation.

**「Community discussion」** One commenter disputed the RCE framing, calling the flaw a double-free bug and asking whether vulnerability reports are being intentionally overstated. A commenter identifying as involved said the vulnerability was discovered by Johan Carlsson and that GitLab informed them on 2026-11-12; they had set 2026-11-25 for coordinated disclosure but moved the GPGME disclosure to 2026-11-20 because GitLab needed to update earlier due to a new Ruby2Shell bug. Another commenter said Red Hat had reportedly fixed the issue five years ago according to conventional tools, but upstream missed it, linking a CentOS Stream gpgme packaging commit.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html">GnuPG Warns Critical GPGME Flaw Could Expose App Data via...</a></li>
<li><a href="https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html">[Announce] GnuPG Security Advisory for GPGME ...</a></li>
<li><a href="https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html">[Announce] GnuPG Security Advisory for GPGME ...</a></li>
<li><a href="https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html">GnuPG Warns Critical GPGME Flaw Could Expose App Data via...</a></li>
<li><a href="https://www.phoronix.com/news/GnuPG-GPGME-Critical">GnuPG&#x27;s GPGME Affected By Critical Security Bug In Turn... - Phoronix</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability-disclosure`, `#gnupg`, `#gpgme`, `#open-source`

---

<a id="item-tech-news-6"></a>
### [USB hub in a monitor throttled Ethernet download speed](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

A blog post-mortem explains how routing a USB network adapter through a monitor&\#x27;s built-in hub cut download throughput by roughly 75 percent. The added latency from the hub prevented the laptop from acknowledging packets quickly enough, causing the Ethernet adapter&\#x27;s buffer to fill and drop packets rather than sustain full speed. Switching to a different adapter that required less frequent acknowledgement restored throughput. The write-up attributes the failure to opaque USB hub and adapter buffering behavior rather than the monitor or the network link itself.

hackernews · soheilpro · Nov 21, 10:36 · [Discussion](https://news.ycombinator.com/item?id=50587875)

**「Background」** USB-attached Ethernet adapters can add latency compared with a native Ethernet port, and that latency becomes dependent on the USB hub or dock in between the adapter and the host. USB hubs add their own transaction scheduling and buffering, so an adapter connected through a hub—integrated into a monitor or dock—may see delayed transfers and less frequent acknowledgements than one plugged in directly. Commenters note the same class of issue appears with Thunderbolt docks and MacBooks, which is why the monitor in this post-mortem is incidental to the hub path.

**「Practical Takeaway」** For users diagnosing slow Ethernet through a USB dock or hub, the post-mortem suggests swapping the adapter or changing its port before blaming the internet connection itself; the author&\#x27;s different adapter, which required less frequent acknowledgement, restored throughput. It also makes USB hub topology and latency variables worth checking before replacing a monitor, dock, or ISP service.

**「Community Discussion」** Commenters clarified that the monitor is largely incidental and the real bottleneck is the USB networking path, with one noting that additional latency through the hub caused acknowledgement delays and adapter-side packet drops. Another reader reported a similar throughput problem with a MacBook and Thunderbolt dock that persisted for over a year, and described flow control plus a newer setup as finally making it usable. A separate commenter compared it to a debugging case where Ghostty&\#x27;s io\_uring usage registered as I/O pressure and caused Baldur&\#x27;s Gate 3 to throttle its Vulkan shader compilation.

<details><summary>References</summary>
<ul>
<li><a href="https://superuser.com/questions/1592635/does-a-usb-c-ethernet-adapter-have-a-higher-latency-than-a-regular-ethernet-port">networking - Does a USB -C ethernet adapter have a higher latency ...</a></li>

</ul>
</details>

**Tags**: `#USB`, `#networking`, `#hardware-troubleshooting`, `#systems-debugging`, `#ethernet`

---

<a id="item-tech-news-7"></a>
### [OpenAI cuts reasoning-chain extraction rate to 0.2% with anti-distillation defenses](https://openai.com/index/combatting-adversarial-distillation/) ⭐️ 7.0/10

OpenAI published a post on November 20 describing strengthened defenses against &quot;adversarial distillation,&quot; saying its GPT-6.2 Astra and Sol models now better protect reasoning chains. In red-team testing, the success rate of extracting reasoning from historical requests fell from 54.0% to 0.2%, the company reported. OpenAI also said it takes enforcement action against thousands to tens of thousands of distillation accounts each week, and that it had previously briefed Congress on suspected distillation activity by DeepSeek. These are vendor-reported figures; the Telegram summary does not describe the red-team methodology or provide independent verification.

telegram · zaihuapd · Nov 21, 01:30

**「Background」** OpenAI&\#x27;s post presents the change as tying a model&\#x27;s protected reasoning to the conversation history that produced it in GPT-6.2 Astra and GPT-6.2 Sol. The context is adversarial distillation: extracting a model&\#x27;s reasoning outputs to train or improve another model, which OpenAI frames as a safety risk rather than only a terms-of-service issue.

**「Impact」** Developers and API users who rely on models&\#x27; reasoning traces should expect extraction of historical chain-of-thought to be far less reliable, and accounts involved in distillation-style scraping face ongoing enforcement at a scale of thousands to tens of thousands per week, according to OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/combatting-adversarial-distillation/">Combatting adversarial distillation | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#OpenAI`, `#red teaming`, `#LLM reasoning`

---

<a id="item-tech-news-8"></a>
### [TSMC halts 16nm-and-below orders for Chinese firms](https://appleinsider.com/articles/26/11/20/apple-supplier-tsmc-cuts-off-china-chip-orders-amid-tighter-export-controls) ⭐️ 7.0/10

TSMC has reportedly notified customers that it is suspending 16nm-and-below advanced-node orders from Chinese companies under tightened US semiconductor export rules, with shipments barred unless a US export license or exemption is obtained in advance. Chinese firms are pushed back to older 28nm and 40nm processes and lose access to the high-bandwidth memory needed for AI data centers. Previously TSMC could itself assess whether a customer&\#x27;s design qualified for an exemption; under the new approach, customers must apply in advance. Apple, AMD, and Nvidia appear on the US approved list while no Chinese company does, and TSMC said it will comply with the new rules.

telegram · zaihuapd · Nov 21, 02:01

**「Background」** The reported suspension follows earlier US restrictions that led TSMC and Samsung to halt some advanced-chip shipments to Chinese customers, with Samsung&\#x27;s clients reportedly including Baidu&\#x27;s AI data-center unit Kunlun and ByteDance. Under the earlier arrangement, TSMC could itself assess whether a customer&\#x27;s chip design qualified for an exemption; the tightened rules now require customers to obtain US export approval before orders can proceed.

**「Impact」** Chinese chip designers relying on TSMC&\#x27;s advanced nodes now face a licensing step before any order can be filled, and those unable to secure a US license or exemption must redesign or re-source products onto 28nm/40nm processes. The loss of HBM access directly constrains plans for AI data-center accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sinodefenceforum.com/t/chinese-semiconductor-thread-ii.9109/page-1589">Chinese semiconductor thread II | Page 1589 | Sino Defence Forum...</a></li>
<li><a href="https://theoutpost.ai/news-story/tsmc-cuts-chinese-chip-designers-off-from-the-tech-their-ai-chips-need-33882/">TSMC tightens chip curbs on Chinese designers</a></li>

</ul>
</details>

**Tags**: `#semiconductor export controls`, `#TSMC`, `#AI chips`, `#supply chain`, `#US-China tech`

---

<a id="item-tech-news-9"></a>
### [OpenRouter warns MiniMax prompts may have been read by third parties](https://news.ycombinator.com/item?id=50585962) ⭐️ 7.0/10

OpenRouter emailed users warning that request content sent to MiniMax models may have been read by third parties, according to a Telegram relay of a Hacker News item. Security researchers sent prompts containing test URLs to MiniMax models between July and October 2026, and third parties accessed those URLs after 40 to 130 hours. OpenRouter attributed the problem to MiniMax and its forwarding providers AtlasCloud, Novita, and StreamLake, removed &quot;zero data retention&quot; labels from the affected endpoints, and advised users who may have exposed sensitive credentials to rotate API keys and passwords. As of the report, OpenRouter had not published an official advisory on its website, so the warning is not independently confirmed there.

telegram · zaihuapd · Nov 21, 06:53

**「Why prompt retention matters」** OpenRouter routes requests to many upstream model providers, so users typically rely on its endpoint labels — such as &quot;zero data retention&quot; — to judge whether prompts and completions are stored. A third party later fetching test URLs embedded in prompts indicates the prompt text itself left the intended handling path.

**「Users of affected MiniMax endpoints should rotate credentials」** Teams that sent sensitive data — API keys, passwords, internal URLs — through MiniMax endpoints routed by AtlasCloud, Novita, or StreamLake should treat those credentials as potentially exposed and rotate them, as OpenRouter advised. The removal of &quot;zero data retention&quot; labels also means those routes can no longer be relied on for confidential or regulated workloads until MiniMax or OpenRouter restores and independently verifies that guarantee.

**Tags**: `#LLM security`, `#data privacy`, `#MiniMax`, `#OpenRouter`, `#API providers`

---

<a id="item-tech-news-10"></a>
### [Daraxonrasib First-Line Data: Tumor Disappearance in About 1 in 12 of 61 Patients](https://event.eortc.org/ena2026/2026/11/20/metastatic-pancreatic-cancer-responds-well-to-initial-treatment/) ⭐️ 7.0/10

At ENA 2026 in Barcelona on November 20, late-breaking oral data showed daraxonrasib 200 mg once daily plus gemcitabine/nab-paclitaxel in 61 previously untreated metastatic pancreatic ductal adenocarcinoma patients produced a confirmed objective response rate of 60.7%, a complete response rate of 8.2% \(about 1 in 12\), and a disease control rate of 90.2%. Median progression-free survival was 12.8 months, the 12-month overall survival rate was 76.6%, and median follow-up was 18.3 months. The study is a single-arm Phase I/II trial without a chemotherapy control, and the principal investigator said efficacy comparisons require the ongoing Phase III trial; the historical chemotherapy reference range for 1-year survival is 22%–48% \(MPACT 35%, mFOLFIRINOX 48%\). Daraxonrasib is an oral RAS\(ON\) multi-selective inhibitor covering multiple KRAS/NRAS mutations, and it received FDA approval on August 26 as RASONQUE for previously treated patients based on Phase III RMC-302, which reported median overall survival of 13.2 vs 6.7 months.

telegram · zaihuapd · Nov 21, 11:24

**「Background」** Daraxonrasib is an oral RAS\(ON\) multi-selective inhibitor that targets active-state RAS across multiple KRAS/NRAS mutations rather than a single G12C variant. The FDA approved it on August 26 under the brand name RASONQUE for adults with metastatic pancreatic adenocarcinoma who have received at least one prior systemic therapy or who are not candidates for multiagent systemic therapy, based on the Phase III RMC-302 trial that reported median overall survival of 13.2 versus 6.7 months. The new ENA 2026 report tests the drug in the first-line setting, combined with gemcitabine/nab-paclitaxel.

**「Impact」** For previously treated metastatic pancreatic ductal adenocarcinoma, daraxonrasib&\#x27;s approval rests on the randomized Phase III RASolute 302 trial against second-line chemotherapy, which reported median overall survival of 13.2 versus 6.7 months. The first-line use presented at ENA 2026 remains unproven against a chemotherapy control until the ongoing Phase III trial reports, so the single-arm 60.7% response rate should be read as hypothesis-generating; eligibility in the completed Phase III trial covered KRAS G12, G13, or Q61 mutations as well as wild-type disease.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-daraxonrasib-metastatic-pancreatic-adenocarcinoma">FDA approves daraxonrasib for metastatic pancreatic ... | FDA</a></li>
<li><a href="https://today.ucsd.edu/area-story/top-5-highlights-from-asco-2026-moores-cancer-center-at-the-forefront">Top 5 Highlights from ASCO 2026: Moores Cancer Center at the...</a></li>
<li><a href="https://ascopost.com/videos/asco-2026/brian-m-wolpin-and-eileen-m-oreilly-on-daraxonrasib-in-previously-treated-metastatic-pancreatic-cancer/">Brian M Wolpin and Eileen M OReilly on Daraxonrasib in Previously...</a></li>
<li><a href="https://alipanc.org/en/daraxonrasib-or-chemotherapy-in-previously-treated-metastatic-pancreatic-cancer/">Daraxonrasib or Chemotherapy in Previously Treated Metastatic ...</a></li>

</ul>
</details>

**Tags**: `#pancreatic cancer`, `#daraxonrasib`, `#RAS inhibition`, `#clinical trial`, `#FDA approval`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Why output caching can&\#x27;t meaningfully cut LLM costs](https://seangoedecke.com/why-output-caching-doesnt-work/) ⭐️ 7.0/10

rss · Sean Goedecke · Nov 21, 00:00

**「Background」** LLM inference economics already rely on caching model inputs, typically in the KV cache, so the full conversation history is not recomputed on every turn. Sean Goedecke asks whether caching model outputs—or otherwise eliminating self-repetition in replies—should get the same treatment.

**「Solution」** The apparent case for output caching is that agents repeat content a lot: they paste code snippets into pull-request explanations, quote evidence documents when answering the user, and reprint sample outputs for review. Because output tokens are generated one at a time and cost much more than input tokens, Goedecke argues this waste is worse than the input-caching problem. One could fine-tune or prompt a coding model to emit references like “src/script.py:12-15” instead of regurgitating the lines, or teach a model to cite segments of its own conversation history that the harness then expands transparently. His objection is that such a scheme optimizes only visible output. In his own agent histories—an informal sample with no stated methodology—roughly 6% of output tokens were visible, 50% were reasoning, and 44% were tool calls. Under Amdahl’s law, even saving an optimistic two-thirds of visible tokens would cut only about 4% of total output tokens. He is only moderately confident that frontier models rarely loop in their chains of thought, and he flags that tool calls may also contain repetition, inviting readers with more evidence to weigh in. The real lever, he concludes, is reducing the invisible 94%: smarter models need fewer reasoning tokens and tool calls to reach the right answer, which can make a model that is 5x pricier per token cheaper overall if it uses 6x fewer tokens.

**「Takeaway」** Goedecke’s thesis is that output caching attacks the wrong bottleneck: because visible repetition is a small slice of output tokens, Amdahl’s law caps its benefit, and the larger gains come from model intelligence that shortens reasoning and tool-call traces—more an intelligence and harness problem than a caching one.

**Tags**: `#LLM inference economics`, `#output token costs`, `#Amdahl&\#x27;s law`, `#agent harnesses`, `#caching`

---

<a id="item-tech-blog-2"></a>
### [Avoiding Blunders Beats Clever Code](https://seangoedecke.com/to-code-well-avoid-blunders/) ⭐️ 6.0/10

rss · Sean Goedecke · Nov 22, 00:00

**「Background」** Engineers often treat good programming as a search for brilliant abstractions or clever patterns, but the author argues this gets the emphasis backwards. Drawing on analogies to chess and tennis, the piece contends that the real goal is to avoid catastrophic mistakes — a skill that matters especially in large commercial codebases built by big teams, where one bad change can undo an elegant design.

**「Solution」** Programming rewards error-avoidance because it offers no durable winning advantage: unlike basketball, where a blunder barely dents a large lead, one poor decision can turn a clean codebase into a janky one. The author&\#x27;s examples include introducing a parallel system to do an existing task, creating a second source of truth for key data, converting a safe synchronous operation into a fragile asynchronous one, adding subtle new points of failure, and complicating a key interface. The two cardinal sins behind these are inconsistency and unnecessary requirements. Inconsistency is dangerous because it breaks trust: engineers can no longer assume code behaves sensibly and must instead hunt for surprises. Unnecessary requirements are dangerous first because they are sticky — an engineer implementing a requirement has the context to judge whether it is needed, but someone reading it later must assume it is necessary unless they invest time in research, so requirements outlive their justification. Second, they interrelate combinatorially: if the codebase supports feature X, every new feature must be considered against X, which is what makes large codebases so hard to work in. The practical discipline is to find where a task fits most normally into the existing codebase and trim it to the smallest set of requirements possible, reserving so much attention for this that little energy remains for clever tricks or extra-credit features. Thinking &quot;I could implement this with a clever pattern&quot; should be treated as a warning sign of distraction. The author notes the advice applies to hand-written code and AI agents alike, and while coding agents are roughly as good as humans at consistency, they are much worse at avoiding unnecessary requirements.

**「Takeaway」** The author&\#x27;s conclusion is that great programming does not require cleverness and can even be hindered by it; what matters is attention to detail and a laser focus on avoiding blunders through consistency and the ruthless removal of unnecessary requirements.

**Tags**: `#software engineering`, `#codebase maintainability`, `#engineering judgment`, `#technical debt`, `#code consistency`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Trump backs Lutnick on China chip sales and urges Nvidia CEO Huang to apologize and return](https://www.reuters.com/world/us/trump-says-he-still-backs-lutnick-urges-nvidias-huang-apologize-2026-11-20/) ⭐️ 7.0/10

President Donald Trump said on November 20 that he still supports Commerce Secretary Howard Lutnick, saying he is &quot;doing a great job&quot; despite scrutiny of his handling of chip sales to China amid the Nvidia affair. Trump also said he wants Nvidia CEO Jensen Huang, whom he described as having resigned, to &quot;return after a sincere apology,&quot; and said he had discussed the matter with Chinese President Xi Jinping — an account Treasury Secretary Scott Bessent partly contradicted by saying the call did not involve Huang.

telegram · zaihuapd · Nov 21, 05:03

**「Background」** Nvidia CEO Jensen Huang resigned in November 2026 after admitting to an affair with a woman alleged to be a Chinese spy, and the Commerce Department&\#x27;s May clearance of advanced Nvidia chip sales to China-affiliated entities has drawn scrutiny of Secretary Howard Lutnick&\#x27;s oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://www.axios.com/2026/11/10/lutnick-nvidia-jensen-huang-china-memo">The agency cleared advanced AI chip sales in May.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Jensen_Huang_scandal">Jensen Huang scandal - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/11/12/podcasts/hardfork-jensen-huang-resigns.html">Jensen Huang Is Out at Nvidia - The New York Times</a></li>

</ul>
</details>

**Tags**: `#US-China tech policy`, `#semiconductor export controls`, `#Nvidia`, `#Trump administration`, `#Commerce Department`

---