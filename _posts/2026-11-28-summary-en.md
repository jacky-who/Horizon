---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 48 items, 32 important content pieces were selected

---

**Technology News**
1. [OpenSec Discloses 9.8-Rated Pre-Auth NFS Root Flaw in Linux](#item-tech-news-1) ⭐️ 9.0/10
2. [Google Research: DeepCrossAttention speeds Transformer training up to 3x](#item-tech-news-2) ⭐️ 8.0/10
3. [States sue SpaceX over Grok&\#x27;s child abuse and revenge porn images](#item-tech-news-3) ⭐️ 8.0/10
4. [Michael Nielsen removes his free neural-networks book](#item-tech-news-4) ⭐️ 8.0/10
5. [Minecraft Bedrock Resource Pack Flaw Affected 26.52–26.63, Fixed in 26.65](#item-tech-news-5) ⭐️ 8.0/10
6. [Microsoft moves to replace some third-party Windows drivers with in-box drivers](#item-tech-news-6) ⭐️ 8.0/10
7. [Convex skill uploads app ideas to power quickstart feature](#item-tech-news-7) ⭐️ 7.0/10
8. [WebRTC-based card skimming scripts found on shopping sites](#item-tech-news-8) ⭐️ 7.0/10
9. [The limits of computer-checked proofs](#item-tech-news-9) ⭐️ 7.0/10
10. [SemiAnalysis benchmarks Trainium3 inference per dollar](#item-tech-news-10) ⭐️ 7.0/10
11. [黑客借 AI 工具 Artex 攻击 CIA 等美国情报机构](#item-tech-news-11) ⭐️ 7.0/10
12. [Anthropic says it covertly degrades Claude for frontier-model work](#item-tech-news-12) ⭐️ 7.0/10

**Global Chips**
1. [BIS Adds Remote Access to Chip Export Controls, Tightens Southeast Asia Licensing](#item-chip-news-1) ⭐️ 8.0/10
2. [Report: Restricted Nvidia Blackwell Chips Found in Chinese Data Center](#item-chip-news-2) ⭐️ 7.0/10
3. [Nvidia Blackwell Chips Reportedly Found at China Data Center Tied to Alice Huang](#item-chip-news-3) ⭐️ 7.0/10
4. [Nvidia Blackwell chips installed at Chinese data center tied to ex-Megaspeed executive](#item-chip-news-4) ⭐️ 7.0/10
5. [Alibaba&\#x27;s T-Head AI chip roadmap: M890 ramp, V900 in Q1, J900 in 2028](#item-chip-news-5) ⭐️ 7.0/10
6. [Banned Nvidia Blackwell Racks Reported in Shanghai Data Center](#item-chip-news-6) ⭐️ 6.0/10
7. [NVIDIA Blackwell chips reported at Shanghai data center tied to Megaspeed](#item-chip-news-7) ⭐️ 6.0/10
8. [Huawei to Detail Custom HBM Workaround at ISSCC 2027](#item-chip-news-8) ⭐️ 6.0/10
9. [Report alleges banned Nvidia chips found at China data center tied to Megaspeed](#item-chip-news-9) ⭐️ 5.0/10
10. [禾润电子递交创业板招股书，拟募资12亿元，研发费用率9.83%](#item-chip-news-10) ⭐️ 5.0/10
11. [MATCH Act Said to Extend Tool Curbs Beyond Lithography to Yield Technologies](#item-chip-news-11) ⭐️ 5.0/10
12. [Big Technology&\#x27;s Kantrowitz: China&\#x27;s Nvidia chip access narrowing](#item-chip-news-12) ⭐️ 4.0/10
13. [Analyst claims NVIDIA Blackwell chip reached China data center](#item-chip-news-13) ⭐️ 4.0/10
14. [Kantrowitz: Nvidia&\#x27;s China chip access narrowing, no new policy detail](#item-chip-news-14) ⭐️ 4.0/10
15. [A-share AI compute chip shares rise on vague policy, HBM catalysts](#item-chip-news-15) ⭐️ 4.0/10
16. [Penguin Revives Retired DDR4 for AI Server Memory Expansion](#item-chip-news-16) ⭐️ 4.0/10

**Financial News**
1. [国常会：加力发挥“国家队”稳市作用，优化中央汇金类“平准基金”功能](#item-finance-news-1) ⭐️ 8.0/10
2. [蜜雪冰城5亿元入股DeepSeek新一轮融资，规模约千亿元](#item-finance-news-2) ⭐️ 7.0/10
3. [央行下调大额存单起购门槛，个人降至10万元](#item-finance-news-3) ⭐️ 7.0/10
4. [China regulator summons 15 e-bike makers over certification failures](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenSec Discloses 9.8-Rated Pre-Auth NFS Root Flaw in Linux](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec has disclosed CVE-2026-99362, a pre-authentication heap overflow in Linux&\#x27;s NFS server \(nfsd\) rated CVSS 9.8. A single connection to tcp/2049 can trigger an out-of-bounds kernel heap write and yield a root shell without logging in. The flaw has existed since Linux 3.16 \(2014\) and affects hosts running NFSv4.1 or 4.2, including file servers, NAS devices, and cluster storage nodes. Fixes ship in kernels 6.12.117, 6.18.61, 7.3.2, and 7.4-rc1 and require upgrading and rebooting; operators who cannot patch immediately should restrict tcp/2049 access at the firewall. The CVE was published on November 20, 2026.

telegram · zaihuapd · Nov 27, 12:57

**「Background」** The flaw lies in the in-kernel NFS server&\#x27;s handling of NFSv4.1/4.2 session SEQUENCE replies, where a reply-cache slot can be reached before the request is validated; the upstream fix is titled &quot;nfsd: preflight SEQUENCE replies before accepting a slot.&quot; Because that code path dates to Linux 3.16 \(2014\), kernels from that release onward with NFSv4.1 or 4.2 enabled are exposed over tcp/2049 until patched.

**「Operational impact」** Operators running NFSv4.1 or 4.2 servers, including NAS appliances and cluster storage nodes, need to upgrade to kernel 6.12.117, 6.18.61, 7.3.2, or 7.4-rc1 and then reboot, since the fix is not live until the new kernel is running. If immediate upgrade is not possible, the disclosed mitigation is to restrict tcp/2049 at the firewall, which cuts off legitimate NFS traffic to that port as well.

<details><summary>References</summary>
<ul>
<li>NFS2ROOT CVE-2026-99362: Exposure, Kernel Fixes and Detection Limits - Penligent</li>
<li>CVE-2026-99362 - TuxCare Vulnerabilities</li>
<li>NFS2ROOT: Pre-auth Remote Root in Linux nfsd - Detections AI</li>

</ul>
</details>

**Tags**: `#Linux kernel`, `#NFS`, `#vulnerability`, `#security`, `#remote exploitation`

---

<a id="item-tech-news-2"></a>
### [Google Research: DeepCrossAttention speeds Transformer training up to 3x](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 8.0/10

Google Research published a blog post describing DeepCrossAttention, a Transformer residual-connection design that it claims preserves model quality while running up to 3x faster. The claim covers training and/or latency speedups, but comes from a vendor research blog and has not been independently verified. Community commenters note the work appears to date from 2025, and one commenter says the post&\#x27;s actual on-page title is &quot;Supercharging Transformer Residual Connections,&quot; not &quot;DeepCrossAttention.&quot;

hackernews · ComputedCamp995 · Nov 27, 23:06 · [Discussion](https://news.ycombinator.com/item?id=50672565)

**「Context: residual connections and DeepCrossAttention」** Transformer layers conventionally add each sublayer&\#x27;s output to its input through a residual connection, a design long credited with helping gradients flow through deep networks. The DeepCrossAttention paper appearing in search results is dated February 2025 and describes the approach as replacing or supplementing conventional residual connections to avoid diluting key information while aiming to improve performance and training efficiency; the submitted blog post is dated November 2026, and commenters note the underlying work is from 2025.

**「Impact」** Practitioners evaluating residual-connection alternatives for Transformer training should treat the up-to-3x figure as a vendor claim pending independent benchmarks; the discussion also connects the technique to prior efficiency work such as MTP and Dflash derivatives, raising the question of whether gains compound with those methods.

**「Community Discussion」** Commenters compared the idea to DenseNet&\#x27;s dense connections and asked whether the speedup could stack with existing speculative-decoding-style techniques that already delivered roughly 10x tokens/sec over two years. Others flagged that the post is dated 2025 and that the linked page&\#x27;s title is &quot;Supercharging Transformer Residual Connections,&quot; suggesting the submission&\#x27;s naming was added rather than taken from the source.

<details><summary>References</summary>
<ul>
<li>DeepCrossAttention: Supercharging Transformer Residual Connections - 智源社区论文</li>

</ul>
</details>

**Tags**: `#transformers`, `#model-architecture`, `#training-efficiency`, `#google-research`, `#residual-connections`

---

<a id="item-tech-news-3"></a>
### [States sue SpaceX over Grok&\#x27;s child abuse and revenge porn images](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 8.0/10

A coalition of state attorneys general, including Virginia&\#x27;s Jay Jones and another identified as Rayfield, sued SpaceX as the parent company of X, xAI, and Grok, alleging the platform created and promoted child sexual abuse material and non-consensual intimate images. The suit targets Grok&\#x27;s image-generation behavior and frames the issue as a content-moderation and platform-liability matter. The supplied material does not specify the filing venue, the exact models or versions involved, or the remedy sought. The action is an allegation filed in court, not an adjudicated finding.

hackernews · DeepLogin · Nov 27, 19:42 · [Discussion](https://news.ycombinator.com/item?id=50670855)

**「Background」** The lawsuit follows earlier regulatory and legal pressure over Grok&\#x27;s image-generation safeguards. In January 2026, New Jersey&\#x27;s acting attorney general demanded that xAI immediately stop producing non-consensual intimate images and child sexual abuse material, and by September 2026 The Guardian reported that many lawsuits against xAI stemmed from a period at the start of that year when loose safeguards let users direct Grok to remove clothing from photos and generate sexualized images. This multistate action escalates that pressure from state demands and individual suits into a coordinated coalition lawsuit against SpaceX as xAI&\#x27;s parent company.

**「Potential Liability Exposure」** The suit seeks to hold SpaceX accountable for Grok&\#x27;s outputs, which could force xAI to change how the model handles image prompts involving minors or real people and to add safeguards for such requests. Because the available source is only the attorneys general announcement, the requested relief, any compliance deadlines, and the case schedule remain unconfirmed.

**「Community discussion」** Commenters questioned whether Grok required deliberate prompting to produce such images or was unusually permissive by default, and some argued the suit should also target the users who request the material. One commenter asserted that Supreme Court precedent protects AI-generated child sexual abuse material made for personal consumption when no real children are depicted, though that claim is not verified in the supplied evidence.

<details><summary>References</summary>
<ul>
<li><a href="https://www.njoag.gov/tag/nonconsensual-intimate-imagesncii/">nonconsensual intimate images (NCII) Archives - New Jersey Office...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/sep/03/elon-musk-ai-grok-child-porn-lawsuit">Child sexual abuse survivor alleges Elon Musk’s AI... | The Guardian</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#content moderation`, `#legal/policy`, `#generative AI`, `#platform liability`

---

<a id="item-tech-news-4"></a>
### [Michael Nielsen removes his free neural-networks book](https://neuralnetworksanddeeplearning.com/) ⭐️ 8.0/10

Michael Nielsen has taken down neuralnetworksanddeeplearning.com, the site hosting his free online book Neural Networks and Deep Learning. The item provides no statement from Nielsen, so the reason for the removal is not established; the Hacker News submission and comments frame it as a possible protest connected to AI risk. A commenter linked a Wayback Machine snapshot from 2026-08-08 as an archival copy, so the text remains reachable outside Nielsen&\#x27;s site.

hackernews · brandonb · Nov 27, 19:31 · [Discussion](https://news.ycombinator.com/item?id=50670757)

**「Background」** Michael Nielsen&\#x27;s Neural Networks and Deep Learning was a free online book published in 2015 through Determination Press, covering perceptrons, backpropagation, and techniques for improving neural-network training. Its freely accessible format made it a widely circulated introductory text, and copies and translations have circulated independently of the original site.

**「Community discussion」** Commenters disagreed about the removal&\#x27;s effect: one called it a misstep, arguing that helping people understand what large companies build better prepares them for the consequences, while another said it now functions more as a protest than a practical restriction and may simply drive more readers to seek the book out. Other comments connected frontier-lab work to capital incentives and made broader claims about advanced AI capability that the item does not substantiate.

<details><summary>References</summary>
<ul>
<li>neuralnetworksanddeeplearning.pdf - Neural Networks and Deep Learning Michael Nielsen The original online book can be found | Course Hero</li>
<li>Neural-Network-and-Deep-Learning-CN - AI-books - GitHub</li>

</ul>
</details>

**Tags**: `#neural-networks`, `#deep-learning`, `#open-access`, `#AI-safety`, `#community-discussion`

---

<a id="item-tech-news-5"></a>
### [Minecraft Bedrock Resource Pack Flaw Affected 26.52–26.63, Fixed in 26.65](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 8.0/10

A resource-pack vulnerability in Minecraft Bedrock allowed packs containing a content.zipe file to modify Ore UI framework files and run hidden scripts. Developer 8Crafter disclosed the issue on Reddit on November 15, reporting confirmed impact on versions 26.52 through 26.63, with earlier versions possibly affected as well; PC, mobile, and console were covered, while Java Edition was not. Players could receive crafted packs without manually installing them when automatic resource-pack downloads were enabled upon joining a server or Realm. Listed exploits included deleting all saves and obtaining player IP addresses, and on Windows under specific conditions silently opening arbitrary URIs and launching batch files from the pack to download malware. Mojang fixed the flaw in version 26.65; AxmBro released a Windows read-only detection tool that finds content.zipe files but cannot determine whether a pack is malicious.

telegram · zaihuapd · Nov 27, 18:04

**「Background」** Minecraft Bedrock uses resource packs to customize textures, sounds, and interface elements, and servers or Realms can require clients to download them automatically. Ore UI is the newer interface framework Bedrock uses to render menus and other on-screen elements, which is the layer the crafted content.zipe file was able to modify.

**「Impact」** Players who joined servers or Realms with automatic resource-pack downloads enabled could be exposed without installing anything themselves, so updating Bedrock to 26.65 is the direct mitigation. Server and Realm operators should also review resource packs they distribute, since the detection tool can locate content.zipe files but cannot judge whether a pack is malicious.

**Tags**: `#security vulnerability`, `#Minecraft Bedrock`, `#resource packs`, `#malware`, `#software updates`

---

<a id="item-tech-news-6"></a>
### [Microsoft moves to replace some third-party Windows drivers with in-box drivers](https://www.techspot.com/news/114721-microsoft-wants-replace-most-third-party-device-drivers.html) ⭐️ 8.0/10

Microsoft confirmed at Ignite 2026 that it is developing first-party Windows in-box drivers for entire hardware classes, aiming to limit third-party code entering the kernel. Printers are the first focus, with the recently introduced Windows Ready Print mode replacing legacy third-party print drivers. Windows product manager Mehmet Kucukgoz said SoundWire and SDCA audio drivers will soon become Windows in-box components, while I3C bus, USB Ethernet, and MIPI camera drivers are also in development. Microsoft also introduced a Driver Quality Initiative \(DQI\) at a recent Windows hardware engineering conference to raise driver reliability, quality, and security standards and to encourage third-party developers and OEMs to use in-box drivers where possible.

telegram · zaihuapd · Nov 28, 02:09

**「Background」** Windows has traditionally depended on hardware vendors to supply kernel-mode drivers for many device classes, which brings third-party code and varying quality levels into the operating system. Microsoft&\#x27;s Windows Ready Print mode previously targeted printer drivers by shifting printing toward an in-box path; the effort confirmed at Ignite 2026 extends that in-box approach to audio, I3C, USB Ethernet and MIPI camera driver classes.

**「Impact」** Hardware vendors and OEMs that currently ship custom kernel drivers for printers, audio, I3C, USB Ethernet, or MIPI cameras may eventually see those drivers superseded by Microsoft&\#x27;s in-box versions, so their development and certification work would shift toward validating compatibility with Microsoft&\#x27;s drivers rather than maintaining their own. Because the source describes the additional driver classes as in development rather than shipped, the timing and exact scope of any replacement remain unconfirmed.

**Tags**: `#Microsoft Windows`, `#drivers`, `#kernel`, `#hardware`, `#Ignite 2026`

---

<a id="item-tech-news-7"></a>
### [Convex skill uploads app ideas to power quickstart feature](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

A GitHub issue against the Convex backend skill alleges that the tool sends a user&\#x27;s app idea to a remote server without disclosing the upload. Convex CEO Jamie responded in the thread that the prompt upload powers Convex&\#x27;s &quot;quickstart&quot; feature, the successor to the company&\#x27;s now-shut-down Convex Chef end-to-end &quot;vibe-coding&quot; product. The available evidence is the issue report plus a partial in-thread explanation; no audit or confirmed malicious behavior is documented.

hackernews · MickyTheMouse · Nov 27, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50669765)

**「Background」** Convex offers a &quot;Quickstart&quot; Agent Skill that, per a listing dated Nov 16, 2026, generates a barebones Convex + web template from a one-sentence idea. In the thread, Convex CEO Jamie describes the reported prompt upload as powering this quickstart feature, which he calls the successor to the shut-down Convex Chef end-to-end coding product. Separate reports have also flagged that the convex-agent skill&\#x27;s AI Gateway guidance drifted from current setup documentation by October 2026.

**「Community Discussion」** Commenters debated the implications rather than the specifics: one argued that self-hosted open-weight models are the long-term answer, and another noted that prompt injection is far more common than models making malicious tool calls on their own, while explicitly not calling this case malicious. A further reply dismissed the concern on the grounds that &quot;ideas are cheap.&quot;

<details><summary>References</summary>
<ul>
<li>Quickstart: a barebones Convex template, running Agent Skill | There&#x27;s An AI For That</li>
<li>`convex-agent` gateway guidance is out of date · Issue #35 - GitHub</li>

</ul>
</details>

**Tags**: `#developer-tools`, `#privacy`, `#AI-coding-assistants`, `#Convex`, `#prompt-injection`

---

<a id="item-tech-news-8"></a>
### [WebRTC-based card skimming scripts found on shopping sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

A security report published on Black Friday describes credit card skimming scripts that use WebRTC to exfiltrate payment data from popular shopping sites, according to discussion of the report. Commenters stress that the technique does not exploit a WebRTC vulnerability; rather, WebRTC traffic is monitored less often than ordinary HTTP requests, and the scripts reportedly target mobile devices where detection is harder. The source is secondary and no technical details of the affected sites or script families are available here.

hackernews · scanr · Nov 27, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50668145)

**「Background」** WebRTC is a free, open-source project that gives browsers and mobile apps real-time communication APIs, including peer-to-peer data channels. The skimming scripts reportedly abuse that data-transfer capability to exfiltrate stolen card data; commenters stress this is not a WebRTC vulnerability but a monitoring gap, since WebRTC traffic is less commonly inspected for malicious behavior.

**「Impact」** The practical exposure for site operators is third-party script inclusion: as one commenter argues, embedding third-party scripts leaves a site vulnerable regardless of whether exfiltration uses WebRTC or plain HTTP requests. Security teams monitoring outbound traffic should therefore treat WebRTC channels as a possible skimming path rather than assuming only standard HTTP egress matters.

**「Community discussion」** Commenters pushed back on framing the finding as a WebRTC flaw, with afavour noting the approach could equally use simple HTTP requests and that embedded third-party scripts are the underlying weakness. jszymborski cited the report as a reason to keep blocking ads, while NordStreamYacht described a Black Friday purchase from a European software site that was followed by an immediate card block and replacement, with the legitimate transaction still completing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebRTC">WebRTC - Wikipedia</a></li>
<li><a href="https://webrtc.org/">WebRTC</a></li>

</ul>
</details>

**Tags**: `#web security`, `#payment fraud`, `#WebRTC`, `#supply chain security`, `#browser security`

---

<a id="item-tech-news-9"></a>
### [The limits of computer-checked proofs](https://cr.yp.to/proofs/falseccp.html) ⭐️ 7.0/10

A post on cr.yp.to argues that computer-checked proofs can be false when the proof checker itself has a soundness bug. The piece targets formal verification systems that rely on a single checker, such as Lean and Metamath, and says a checker bug can let an invalid proof be accepted. Commenters push back on the practical severity, noting that Metamath&\#x27;s main databases require proofs to pass five independently created verifiers in five programming languages, and that the Lean community actively works on checker soundness. No specific new bug or version is disclosed in the item.

hackernews · \_tk\_ · Nov 27, 15:26 · [Discussion](https://news.ycombinator.com/item?id=50667989)

**「Background」** Proof assistants such as Lean and Metamath validate a proof by having a relatively small trusted kernel check each step against the system&\#x27;s axioms and inference rules. The security of the whole arrangement therefore rests on that kernel being correct, which is why soundness bugs in checkers are treated as a serious class of flaw rather than ordinary software bugs.

**「Impact」** Readers who rely on a single proof checker for high-assurance work should treat checker soundness as part of their trust base; the Metamath example shows a workable mitigation is requiring acceptance by multiple independently implemented verifiers. Commenters also note that a checker bug still has to be exploited in a way that hides a further problem in the program being verified, so the risk is real but narrow.

**「Community discussion」** Commenters agreed soundness bugs exist but disputed how alarming the page makes them: twotwotwo said one incorrect verification is far from misleading mathematicians, since you would need bugs in all independent checkers without the input looking implausible, and cited a DeepMind researcher&\#x27;s &\#x27;proof&\#x27; that passed Lean and a then-week-old nanoda by exploiting different bugs. dwheeler noted Metamath&\#x27;s set.mm and iset.mm require proofs to pass five independently created verifiers in five languages, while gr\_norm argued all known soundness bugs in these systems fit in a tweet and are good enough for most software.

**Tags**: `#formal-verification`, `#proof-checkers`, `#software-correctness`, `#lean`, `#metamath`

---

<a id="item-tech-news-10"></a>
### [SemiAnalysis benchmarks Trainium3 inference per dollar](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 7.0/10

SemiAnalysis has added AWS Trainium3 and Google TPUs to its InferenceX benchmark suite and reports that Trainium3 with vLLM achieves better performance per total cost of ownership than every accelerator except Nvidia&\#x27;s Vera Rubin across the entire TCO-versus-p90-interactivity frontier. SemiAnalysis attributes part of the result to Trainium3&\#x27;s tile-first microarchitecture, in which tiles are a first-class primitive rather than an addition to a thread-based GPU design, and says its Trainium Descriptor Generation Engines \(DGE\), comparable to Nvidia&\#x27;s TMA, reach peak HBM bandwidth utilization at small message sizes, which it says is not possible on Nvidia GPUs. The analysis also states that Trainium3 and TPUs trade blows with, or beat, Nvidia GB300 on token-generation cost at TCO in some InferenceX workloads. These are SemiAnalysis&\#x27;s own UBenchX microbenchmarks and modeled results, produced with assistance from AWS&\#x27;s Trainium architecture team, not independently verified production measurements.

rss · Semianalysis · Nov 27, 15:54

**「Background」** Nvidia&\#x27;s datacenter GPUs were originally designed for graphics, and each generation since 2017 has added AI-specific hardware to address the previous bottleneck: Volta added Tensor Cores, Hopper added TMA for tile data movement between HBM and SRAM, and Blackwell added Tensor Memory for accumulation. SemiAnalysis argues Trainium3 instead treats tiles as a first-class primitive from the ground up, and that the software difficulty this once created for AWS has now been addressed.

**「Impact」** For teams comparing accelerator TCO for inference, SemiAnalysis reports that Trainium3 with PDS and vLLM beats every accelerator except Vera Rubin across its entire TCO-versus-p90-interactivity curve, and that Trainium3&\#x27;s descriptor engines reach peak HBM bandwidth utilization at small message sizes where Nvidia GPUs cannot, based on its UBenchX microbenchmarks. These are third-party results that SemiAnalysis says AWS engineers helped validate, not independently replicated measurements, so anyone planning a deployment should verify the perf-per-dollar ordering against their own latency targets and software stack before treating it as established.

**Tags**: `#AI hardware`, `#Trainium3`, `#microarchitecture`, `#AWS`, `#inference`

---

<a id="item-tech-news-11"></a>
### [黑客借 AI 工具 Artex 攻击 CIA 等美国情报机构](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 7.0/10

《纽约时报》报道并经《福布斯》转述，美国中央情报局、国家地理空间情报局和国家情报总监办公室遭到黑客攻击，攻击中使用了名为 Artex 的 AI 工具。Artex 可整合多个开源 AI 模型，用于测试网络和计算机防御。此次攻击看起来不算严重，影响的是非机密侦察数据。报道还称，一名中国开发者今年早些时候发布了 Artex，该工具后来被用于多起攻击，包括针对欧盟的一起；该开发者已将其从 GitHub 账号删除，而 FBI 今年早些时候曾警告网络罪犯和间谍正在广泛使用 Artex。

telegram · zaihuapd · Nov 27, 10:42

**「Background」** Artex is an AI-assisted penetration-testing framework that chains multiple open-source AI models to test networks and computer defenses. According to search results, the FBI issued an advisory in mid-November 2026 warning that state-backed and criminal actors had used ARTEX in campaigns across multiple sectors, compressing breach timelines. The source adds that a Chinese developer released Artex earlier in 2026 and later removed it from GitHub after it was used in attacks, including one against the EU.

**「影响」** 对使用开源 AI 模型搭建安全测试或监测流程的机构而言，报道显示同一类工具可被改用于探测防御，且开发者已删除 GitHub 上的 Artex，依赖该仓库获取或复现工具的组织需要另找来源并重新评估暴露面。

<details><summary>References</summary>
<ul>
<li>FBI warns ARTEX AI hacking tool is powering global cyberattacks | Edwin Betancourth</li>
<li>FBI Warning: ARTEX and the Scaling of AI-Assisted Intrusion Tooling - Security Boulevard</li>

</ul>
</details>

**Tags**: `#AI security`, `#cyberattack`, `#offensive AI`, `#US intelligence`, `#open-source AI`

---

<a id="item-tech-news-12"></a>
### [Anthropic says it covertly degrades Claude for frontier-model work](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic&\#x27;s June system card for Claude Mythos 5 and Fable 5 stated that requests aimed at developing frontier models receive covertly degraded responses, rather than being visibly blocked or routed to another model. The interventions use prompt rewriting, steering vectors, and parameter-efficient fine-tuning, and cover tasks such as pretraining pipelines, distributed training, and accelerator design. Anthropic estimated the effect at roughly 0.03% of traffic and under 0.1% of organizations, saying most coding work is unaffected. Using Claude to build competing models already violated the service terms; the disclosure drew renewed developer attention this week.

telegram · zaihuapd · Nov 27, 13:42

**「Background」** Anthropic&\#x27;s system card for Claude Mythos 5 and Fable 5, released in June 2026, stated that the company added interventions limiting Claude&\#x27;s effectiveness on requests aiming at frontier LLM development, citing pretraining pipelines, distributed training infrastructure, and ML accelerator design as examples. The disclosure resurfaced this week amid developer discussion of how these interventions are applied without user-visible refusal.

**「Impact」** Developers using Claude for frontier-model work — pretraining pipelines, distributed training, or accelerator design — may receive quietly degraded responses rather than an explicit refusal, so they cannot tell from the output that an intervention occurred and get no fallback routing to another model. Anthropic estimates the affected scope at roughly 0.03% of traffic and under 0.1% of organizations, and notes that such use already violates its terms of service, meaning teams should treat this as a policy-enforcement mechanism rather than a service defect.

<details><summary>References</summary>
<ul>
<li><a href="https://ai-digest.liziran.com/en/digest/2026-06-11-anthropic-built-most-capable-model-then-wired-three-ways">Anthropic Built Its Most Capable Model , Then Wired In Three Ways to...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#Anthropic`, `#model development`, `#API behavior`, `#AI safety`

---

## Global Chips

<a id="item-chip-news-1"></a>
### [BIS Adds Remote Access to Chip Export Controls, Tightens Southeast Asia Licensing](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1107299496_115571&amp;c=17203180096775058747&amp;mkt=en-us) ⭐️ 8.0/10

The U.S. Commerce Department&\#x27;s Bureau of Industry and Security \(BIS\) issued a new rule on November 16 that brings remote access under export controls and adds new chip export licensing requirements for four Southeast Asian countries and Brazil, according to a Sohu report. The change directly closes a route Chinese companies had used to rent NVIDIA compute capacity through Southeast Asian data centers. The report, citing Caijing, says local data center projects have begun looking for buyers to take over. The source does not provide the rule&\#x27;s official document number, technical details, or an effective date.

rss · Bing News - China domestic chips · Nov 27, 10:31

**「Background」** The 16 November BIS rule follows an earlier enforcement step in the same region: the Financial Times reported that Nvidia had told manufacturing partners, including Dell, to stop shipping servers to four south-east Asian countries as Washington tightened export controls aimed at preventing Chinese access to AI computing power \(tool-1-2\). The new rule extends that pressure by covering remote access and adding chip export licence requirements for those countries and Brazil, reaching the data-centre rental route that server-shipment restrictions alone did not close.

**「Impact」** For Chinese AI compute users, the practical effect is that renting NVIDIA capacity via Southeast Asian data centers is no longer an uncontrolled workaround: such remote access now falls under BIS licensing, and new license requirements apply to chip exports to the four Southeast Asian countries and Brazil. The report&\#x27;s claim that local data center projects are seeking buyers suggests some operators expect rental demand from Chinese clients to disappear, though this is attributed to Caijing and not independently confirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#英伟达`, `#AI 算力`, `#东南亚数据中心`, `#国产芯片`

---

<a id="item-chip-news-2"></a>
### [Report: Restricted Nvidia Blackwell Chips Found in Chinese Data Center](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fmoney%2fgeneral%2fnvidia-blackwell-chips-found-in-china-as-trump-floats-us-stake%2far-AA2io1hq&amp;c=8332693631996352713&amp;mkt=en-us) ⭐️ 7.0/10

A brief Bing News report says Nvidia&\#x27;s most restricted Blackwell AI chips have surfaced in a Chinese data center, a claim that, if confirmed, would indicate restricted AI compute reaching China despite export controls. The same report says President Donald Trump is considering federal ownership of Nvidia, described only as a possibility rather than an announced or enacted policy. The source does not identify the chip model or quantity, the data center operator, how the chips were sourced, or when they appeared, and it does not say whether U.S. authorities or Nvidia have verified the sighting. No license, enforcement action, shipment figure, or ownership decision is reported.

rss · Bing News - NVIDIA and China · Nov 27, 13:25

**「Background」** The report does not specify which Blackwell model surfaced, when, where, or how it was sourced, so the specific antecedent cannot be confirmed from the supplied material. What the item does establish is that the chip in question falls under existing U.S. export restrictions on Nvidia&\#x27;s advanced AI accelerators for China, which is the framework against which any appearance of restricted silicon in a Chinese data center would be assessed; the current snippet provides no verified licensing or enforcement detail beyond that.

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`, `#Blackwell`

---

<a id="item-chip-news-3"></a>
### [Nvidia Blackwell Chips Reportedly Found at China Data Center Tied to Alice Huang](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-in%2fnews%2fother%2fnvidia-blackwell-tech-used-at-china-site-tied-to-alice-huang%2far-AA2ineG3&amp;c=11074468413121558600&amp;mkt=en-us) ⭐️ 7.0/10

A report states that Nvidia Blackwell processors have been found in a Chinese data center connected to Alice Huang and Megaspeed, describing this as the first disclosure of such use. The supplied account provides no quantity, delivery date, facility name beyond the Huang-Megaspeed link, procurement route, or regulatory status for the chips. It is therefore not established which Blackwell variant is involved or whether the deployment complies with U.S. export controls. Nvidia is not cited commenting on the report.

rss · Bing News - NVIDIA and China · Nov 27, 09:44

**「Prior context」** Alice Huang founded Megaspeed, a so-called neocloud, in 2023, and it reportedly obtained Nvidia&\#x27;s approval as a customer within four days of its creation and went on to become the chipmaker&\#x27;s largest Southeast Asian customer, according to the Yahoo Finance account cited in coverage of the report. Under current U.S. controls, exporters need licences to bring Nvidia Blackwell-class or more advanced chips into China, the regulatory baseline against which this first disclosure of Blackwell hardware at a China site tied to Huang and Megaspeed is being assessed.

**「Impact」** The report, if confirmed, would put U.S. export-control enforcement around advanced Nvidia accelerators back in focus for China-linked operators, since Blackwell-class parts are restricted for sale to Chinese customers without a licence. The practical questions — who supplied the chips, under what authorisation, and whether any licence covered them — remain unanswered in the available account, so no shipment or revenue effect for Nvidia can be quantified from this evidence.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>
<li><a href="https://asiatimes.com/2026/11/huangs-fall-us-curbs-put-chinas-ai-computing-in-peril/">Huang &#x27;s fall, US curbs put China &#x27;s AI computing in peril - Asia Times</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#Blackwell`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-4"></a>
### [Nvidia Blackwell chips installed at Chinese data center tied to ex-Megaspeed executive](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fgizmodo.com%2fnvidias-advanced-ai-chips-being-used-at-chinese-data-center-tied-to-alice-huang-2000846169&amp;c=11134892719203026605&amp;mkt=en-us) ⭐️ 7.0/10

A Chinese data center linked to Alice Huang, a former executive at Megaspeed, has installed hardware using Nvidia&\#x27;s Blackwell AI chips, according to a brief report. The account provides no details on the number of chips, the facility&\#x27;s operator, the specific Blackwell variant, or when the hardware was installed. It also does not state whether the deployment complies with U.S. export controls or whether any license was granted, and Nvidia is not quoted in the supplied material.

rss · Bing News - NVIDIA and China · Nov 27, 05:02

**「Prior context: Megaspeed and Alice Huang」** The data center&\#x27;s reported link to Alice Huang follows earlier reporting that Megaspeed, a cloud computing company with ties to Nvidia, said Huang left the company in 2025; that report described her as an alleged Chinese spy. Corporate-records reporting from mid-November 2026 also traced Huang&\#x27;s direct involvement in Megaspeed&\#x27;s founding, including a company linked to her acquiring the Singapore arm of a Chinese video firm. The current item adds only that a Chinese data center tied to Huang has installed hardware using Nvidia&\#x27;s Blackwell AI chips, without identifying the operator, quantities, or any export-licence status.

**「Licensing exposure via third-party channel」** Because GB300 rack stacks are barred from shipment to China without a U.S. export license, the reported Shanghai deployment points to a channel question rather than a permitted direct sale: Bloomberg traced the rack&\#x27;s serial number through a public warranty database to Taiwan&\#x27;s Gigabyte Technology, according to ZeroHedge, indicating the hardware reached the site through a third-party system builder rather than an Nvidia-to-China shipment. That distinction matters for Nvidia&\#x27;s China access, since it moves scrutiny onto warranty and channel records instead of the vendor&\#x27;s own bookings. The source does not state whether a license was obtained or whether regulators have opened a case, so the practical licensing consequence for these operators is unresolved.

<details><summary>References</summary>
<ul>
<li>Megaspeed says alleged Chinese spy, Alice Huang, left company last year</li>
<li>Spies and silicon chips: Alice Huang&#x27;s tangled corporate web - NZ Herald</li>
<li><a href="https://www.zerohedge.com/ai/nvidia-pares-gains-report-traces-shipment-restricted-ai-blackwell-chips-china-data-center">Nvidia Pares Gains As Report Traces Shipment Of... | ZeroHedge</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#Blackwell`, `#中美芯片合作`

---

<a id="item-chip-news-5"></a>
### [Alibaba&\#x27;s T-Head AI chip roadmap: M890 ramp, V900 in Q1, J900 in 2028](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fwww.huxiu.com%2farticle%2f4909136.html&amp;c=15900593603379902450&amp;mkt=en-us) ⭐️ 7.0/10

Alibaba CEO Wu Yongming used the company&\#x27;s fiscal 2027 second-quarter earnings call to disclose T-Head&\#x27;s three-generation AI chip roadmap for the first time: Zhenwu M890 is being fully brought online this year, the next-generation Zhenwu V900 — claimed at three times M890 performance — is slated for mass production in the first quarter of next year alongside super-node clusters, and J900 mass production is targeted for 2028. Wu said the majority of Alibaba&\#x27;s incremental AI-chip supply in 2027 and 2028 will come from its in-house T-Head chips, with flagship parts prioritized for training next-generation Qwen-class large models, while inference capacity will be sourced broadly from other domestic Chinese chip brands. These are announced plans and vendor performance claims, not shipped products or independently measured results.

rss · Bing News - China domestic chips · Nov 27, 19:53

**「Background」** Alibaba designs its own silicon through T-Head, the chip unit behind its Yitian server CPUs and Hanguang interconnect technology, and the Zhenwu line extends that in-house effort into AI accelerators. The disclosure marks the first public three-generation roadmap for that AI chip family, shifting the company from a general statement of self-design ambition to dated production targets and a stated sourcing split between in-house and third-party domestic chips.

**「Impact」** The commitment matters most for Alibaba&\#x27;s own procurement: if the plan holds, most of the cloud provider&\#x27;s incremental AI compute in 2027 and 2028 would be filled by T-Head rather than imported accelerators, with the V900&\#x27;s Q1 mass-production window and super-node cluster rollout the nearest test of that schedule. The stated policy of buying other domestic brands for inference also gives Chinese accelerator vendors a named, large-volume outlet, though the roadmap remains a plan until V900 shipments and measured performance are confirmed.

**Tags**: `#国产芯片`, `#AI 算力`, `#阿里巴巴`, `#自研芯片`, `#数据中心`

---

<a id="item-chip-news-6"></a>
### [Banned Nvidia Blackwell Racks Reported in Shanghai Data Center](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.yahoo.com%2fnews%2fpolitics%2farticles%2fnvidias-blackwell-chips-turn-china-170930530.html&amp;c=4276174839387292558&amp;mkt=en-us) ⭐️ 6.0/10

Banned Nvidia Blackwell racks were reportedly found at a Shanghai data center tied to Alice Huang, according to the source item, which does not name the discovering authority, the quantity of hardware involved, or any independent verification of the finding. Separately, President Trump said the U.S. could still take a stake in Nvidia — a floated possibility rather than an enacted policy, with no mechanism, size, or timing specified. The report does not establish how the Blackwell hardware reached the data center, nor whether any enforcement action, licence decision, or shipment restriction has followed. Both developments remain reported or suggested rather than confirmed outcomes.

rss · Bing News - NVIDIA and China · Nov 27, 09:09

**「Background」** The report sits on top of U.S. export-control restrictions that already bar advanced Nvidia accelerators from China, though the source gives no prior licensing decision specific to Blackwell racks. The Shanghai finding is described only as banned racks at a data center tied to Alice Huang, with no enforcement authority, quantity, seizure date or independent confirmation supplied. Trump&\#x27;s remark that the U.S. could still take a stake in Nvidia is a floated possibility, not an enacted policy or completed transaction.

**「Licensing exposure for GB300 racks」** The report places Nvidia GB300 Blackwell racks inside a Shanghai data center run by two Chinese firms, even though GB300 shipments to China require a US export license, so the practical question is how the hardware arrived and whether Nvidia, Gigabyte Technology or the Chinese operators face scrutiny. Bloomberg traced a rack&\#x27;s serial number through a public warranty database to Taiwan&\#x27;s Gigabyte Technology, alongside regulatory filings, giving investigators a concrete paper trail rather than an inference; no enforcement authority is named as opening a case, so any licensing consequence remains potential rather than imposed. For China&\#x27;s AI compute supply, the episode shows restricted top-end racks can surface domestically despite controls, but the source gives no quantities, so it does not establish a sustained GB300 channel.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>
<li><a href="https://www.zerohedge.com/ai/nvidia-pares-gains-report-traces-shipment-restricted-ai-blackwell-chips-china-data-center">Nvidia Pares Gains As Report Traces Shipment Of... | ZeroHedge</a></li>
<li><a href="https://nypost.com/2026/11/27/us-news/banned-nvidia-chips-uncovered-at-chinese-data-center-linked-to-megaspeeds-alice-huang-report/">Banned Nvidia chips uncovered at Chinese data center linked to...</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-7"></a>
### [NVIDIA Blackwell chips reported at Shanghai data center tied to Megaspeed](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c7c55460c9420dbac114b5cc6&amp;url=https%3a%2f%2fwww.analyticsinsight.net%2fnews%2fnvidias-powerful-blackwell-chips-surface-in-china-raising-a-major-us-security-concern&amp;c=4352821743092553224&amp;mkt=en-us) ⭐️ 6.0/10

NVIDIA Blackwell AI processors have reportedly appeared at a data center in Shanghai connected to Singapore-based Megaspeed, according to Analytics Insight, an account that raises new US security and export-control questions. The report does not identify which Blackwell models were involved, how many units were present, how they reached Shanghai, or which US or Chinese authorities are examining the matter. It therefore describes an enforcement concern rather than a confirmed violation or an enacted policy change, and the supplied material includes no NVIDIA, Megaspeed, US or Chinese government statement confirming the details.

rss · Bing News - China chip policy · Nov 27, 17:30

**「Background」** The reported sighting follows an earlier stage of the same case: Horizon&\#x27;s November 16 digest reported that Singapore-based Megaspeed had launched an internal legal investigation after allegations that it may have provided Chinese companies with backdoor access to Nvidia&\#x27;s high-end AI chips. A November 13 report noted that under current US rules Nvidia holds export permissions only for less capable H200 accelerators, and only under specified shipment conditions, which is why Blackwell processors appearing in Shanghai raise enforcement questions. Chip model, quantity and transit route remain unconfirmed in the supplied source.

**「Impact」** If the report holds, the practical consequence is a fresh test of how US export controls on advanced NVIDIA accelerators are enforced through third-country intermediaries, with Singapore-linked entities operating Blackwell-class hardware in mainland China drawing scrutiny over licensing and re-export routes. Because no chip model, quantity, transit path or investigating authority is named in the supplied material, the specific effect on NVIDIA&\#x27;s China-related revenue or on licensing outcomes cannot be established.

<details><summary>References</summary>
<ul>
<li>Megaspeed launches internal legal investigation as suspected chip export violations via Singapore data centres put AI supply chains under US scrutiny | Folio</li>
<li>Export-banned Nvidia chips are behind China&#x27;s most powerful AI models—uh | Tech Bytes</li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`, `#Blackwell`

---

<a id="item-chip-news-8"></a>
### [Huawei to Detail Custom HBM Workaround at ISSCC 2027](https://www.eetimes.com/huawei-next-big-ai-move-hbm-workaround/) ⭐️ 6.0/10

Huawei plans to provide details of a custom high-bandwidth memory \(HBM\) design at ISSCC 2027 in San Francisco early next year, according to EE Times. The report describes the disclosure as a workaround for HBM, a critical component for its AI chips that is subject to export restrictions. No specifications, bandwidth or capacity figures, manufacturing partners, or production status were disclosed, so the design remains an announced conference presentation rather than a shipped product.

rss · EE Times · Nov 27, 08:56

**「Background」** Huawei&\#x27;s AI accelerators have depended on high-bandwidth memory that export controls make difficult to obtain, and the company has been working on a custom HBM approach as an alternative. Reports describing the ISSCC 2027 disclosure say the design uses 64 channels and five-layer wafer-to-wafer hybrid bonding to give the Ascend 960 processor 9.6 TB/s of bandwidth — claims that have not been independently confirmed. This follows Huawei&\#x27;s prior Ascend accelerator generations, which relied on external HBM supply for their memory bandwidth.

**「Impact」** Since U.S. trade restrictions bar Chinese firms from purchasing advanced HBM stacks from foreign suppliers, a workable Huawei design would most directly affect the supply of memory for its own AI accelerators rather than the broader merchant HBM market. Reported descriptions of the design point to roughly double the data-pin density of HBM that Samsung and SK Hynix mass-produce, which would imply higher theoretical bandwidth — but Huawei has disclosed no capacity, yield or production timing, so the constraint on shipments remains until the design is shown to be manufacturable.

<details><summary>References</summary>
<ul>
<li>Huawei plans to unveil HBM design to challenge Samsung and SK hynix - TechNode</li>
<li>Huawei&#x27;s New 4096-bit HBM Design Claims 9.6 TB/s Bandwidth, Beating Nvidia B300 | Tilt</li>
<li><a href="https://wccftech.com/huawei-poised-to-grow-chinas-ai-chip-market-next-generation-hbm-design-double-data-pin-density/">Huawei Poised To Grow China ’s AI Chip Market With...</a></li>
<li><a href="https://interestingengineering.com/innovation/huawei-hbm-design-data-pin-density">Huawei targets Samsung, SK Hynix with 2X denser memory chip design</a></li>

</ul>
</details>

**Tags**: `#国产芯片`, `#华为`, `#HBM`, `#AI 算力`, `#对华出口管制`

---

<a id="item-chip-news-9"></a>
### [Report alleges banned Nvidia chips found at China data center tied to Megaspeed](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fnypost.com%2f2026%2f11%2f27%2fus-news%2fbanned-nvidia-chips-uncovered-at-chinese-data-center-linked-to-megaspeeds-alice-huang-report%2f&amp;c=13417010356993380899&amp;mkt=en-us) ⭐️ 5.0/10

A New York Post report alleges that banned Nvidia chips were uncovered at a Chinese data center linked to Alice Huang of Megaspeed, according to the item supplied. The source gives no chip models, quantities, enforcement action, named suppliers or dates, so the claim is unverified secondhand reporting rather than a confirmed enforcement finding or a stated change in export-control rules. The same item notes that President Trump had said the chips would be available for purchase in China &quot;in two or three years,&quot; which is a remark about future availability, not a licensing decision or a shipped product.

rss · Bing News - NVIDIA and China · Nov 27, 09:18

**「Background」** The report follows Megaspeed&\#x27;s rise as a Southeast Asian Nvidia customer: the company was founded in 2023 by Alice Huang and, per the cited coverage, obtained Nvidia approval within four days and became the chipmaker&\#x27;s largest Southeast Asian customer. It also follows the US export-licence requirement that bars Nvidia&\#x27;s GB300 rack systems from shipment to China without a licence; the same coverage traces the reported rack&\#x27;s serial number through a public warranty database to Taiwan&\#x27;s Gigabyte Technology.

**「Limited verifiable effect」** The supplied account does not identify the chip models, quantities, sourcing channel or any enforcement action, so no concrete consequence for Nvidia&\#x27;s China shipments, licensing or China&\#x27;s domestic substitution effort can be established from this item. The only policy signal in the source is President Trump&\#x27;s remark that the chips would be available for purchase in China &quot;in two or three years,&quot; which points to future availability rather than a change to current export rules.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/technology/articles/nvidia-blackwell-chips-turn-china-114546617.html">Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang</a></li>
<li><a href="https://www.zerohedge.com/ai/nvidia-pares-gains-report-traces-shipment-restricted-ai-blackwell-chips-china-data-center">Nvidia Pares Gains As Report Traces Shipment Of... | ZeroHedge</a></li>

</ul>
</details>

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#数据中心`

---

<a id="item-chip-news-10"></a>
### [禾润电子递交创业板招股书，拟募资12亿元，研发费用率9.83%](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fwww.sohu.com%2fa%2f1107363135_646494&amp;c=12805390257734187732&amp;mkt=en-us) ⭐️ 5.0/10

2026年11月26日，禾润电子科技（嘉兴）股份有限公司递交创业板招股说明书，并披露对深交所首轮审核问询函的回复。这家2006年成立的集成电路设计企业以卫星导航定位（GNSS）芯片为核心，同时布局模拟信号链和电源链芯片，拟募资约12亿元，保荐机构为中信建投证券。招股书显示公司采用Fabless（无晶圆厂）模式，晶圆制造与封装测试全部依赖第三方供应商，披露的研发费用率为9.83%。2026年5月的股权转让中，公司整体估值约31亿元。上述信息来自公司申报文件及问询回复，目前处于交易所审核阶段，并非已完成的发行或定价。

rss · Bing News - China domestic chips · Nov 27, 14:39

**「Previous context」** 禾润电子成立于2006年，是一家无晶圆厂集成电路设计公司，在卫星导航定位芯片之外还布局了模拟信号链和电源链芯片。此次申报文件中约31亿元人民币的估值来自2026年5月的股权转让，公司选择的保荐机构是中信建投证券。

**「影响」** 若发行获批，约12亿元募集资金将为这家国产GNSS及模拟芯片设计公司提供研发与扩张资金；但其Fabless结构意味着产能最终取决于第三方晶圆代工与封测供应商的排期和产能分配，而非自有产线。

**Tags**: `#国产芯片`, `#GNSS芯片`, `#创业板IPO`, `#模拟芯片`, `#无晶圆厂`

---

<a id="item-chip-news-11"></a>
### [MATCH Act Said to Extend Tool Curbs Beyond Lithography to Yield Technologies](https://www.eetimes.com/beyond-lithography-the-battle-for-semiconductor-manufacturing-yield/) ⭐️ 5.0/10

An EE Times analysis by Ron Honig, published November 27, 2026, argues that the proposed MATCH Act exposes a strategic vulnerability in semiconductor manufacturing that extends beyond ASML&\#x27;s lithography systems to the process technologies that determine fab productivity and yield. The article frames the measure as a policy risk rather than an enacted rule, and the supplied excerpt does not specify its provisions, effective dates, covered equipment or affected companies. What would be restricted, and for whom, therefore remains undefined in the available text.

rss · EE Times · Nov 27, 14:22

**「Background」** The MATCH Act referenced in the article is a proposed bill, not an enacted rule, and the supplied item does not specify its provisions, effective dates, or which companies and equipment it would cover. The piece frames it as a policy risk that extends past ASML&\#x27;s lithography tools to the manufacturing technologies that set fab productivity and yield.

**「Scope of curbs still unsettled」** The practical effect hinges on provisions the source does not detail: the article argues the proposed MATCH Act would reach beyond ASML&\#x27;s lithography tools to the process-control and manufacturing technologies that determine fab productivity and yield, which would widen the number of points where Chinese fabs face restricted equipment access rather than concentrating the constraint on scanners alone. However, a Reuters-reported revision to the bill removed several broad provisions that had alarmed equipment makers earlier in April, so the yield-relevant scope remains a moving proposal rather than an enacted rule, and no effective date or named covered equipment is established here.

<details><summary>References</summary>
<ul>
<li>US narrows chip equipment curbs but keeps pressure on ASML tools and Chinese fabs</li>

</ul>
</details>

**Tags**: `#对华出口管制`, `#先进制程`, `#晶圆产能`, `#半导体设备`

---

<a id="item-chip-news-12"></a>
### [Big Technology&\#x27;s Kantrowitz: China&\#x27;s Nvidia chip access narrowing](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fchinas-nvidia-chip-access-is-closing-fast-says-big-technologys-alex-kantrowitz%2fvi-AA2in23A&amp;c=9999657886079154578&amp;mkt=en-us) ⭐️ 4.0/10

In a CNBC &quot;Squawk on the Street&quot; appearance, Big Technology founder Alex Kantrowitz discussed reports that China&\#x27;s access to Nvidia chips is narrowing and what the latest crackdowns mean for semiconductor companies. The supplied clip preview contains no specific policy provisions, effective dates, product names, shipment or performance figures, so the segment is commentary on existing reports rather than an announced rule, a vendor statement or a measured result. The material does not identify which crackdowns are being referenced or cite any new facts, leaving the scope and timing of the reported tightening unconfirmed.

rss · Bing News - NVIDIA and China · Nov 27, 09:34

**「Background」** The supplied clip does not identify which Nvidia product lines, export-control provisions or licensing decisions are at issue, so no concrete predecessor can be established from the item itself. Without that detail, the segment cannot be tied to a specific earlier rule change or product generation.

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#中美芯片合作`

---

<a id="item-chip-news-13"></a>
### [Analyst claims NVIDIA Blackwell chip reached China data center](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c32c24eb680f1db65da34213f&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fda-davidson-s-gil-luria-there-s-no-doubt-that-nvidia-s-most-advanced-chip-ended-up-in-china%2fvi-AA2indyO&amp;c=11207026517034740657&amp;mkt=en-us) ⭐️ 4.0/10

Gil Luria, head of technology research at D.A. Davidson, said on CNBC&\#x27;s &quot;Squawk on the Street&quot; that NVIDIA&\#x27;s most advanced Blackwell chip ended up in China. He was speaking to a report that Blackwell chips were installed at a Shanghai data center linked to Alice Huang. The item gives no confirmed quantities, shipment channels, named recipient companies beyond the Huang link, or supporting documentation, and Luria&\#x27;s statement is an analyst assertion rather than a verified shipment record or an enforcement finding; neither NVIDIA nor U.S. export-control authorities are cited as confirming the installation.

rss · Bing News - NVIDIA and China · Nov 27, 07:21

**「Background」** Blackwell is NVIDIA&\#x27;s GPU architecture that follows Hopper and is subject to U.S. export controls on advanced AI chips shipped to China. The source clip gives no details on how a Blackwell part would have reached a Shanghai data center, and it includes no confirmation from NVIDIA or U.S. authorities.

**「Impact」** If substantiated, the reported installation would mean U.S. export controls — which restrict shipments of advanced AI accelerators such as Blackwell to China without a licence — are being circumvented for NVIDIA&\#x27;s top-end parts, a question that bears directly on how licensing and end-use checks for China-bound AI compute are enforced. The item supplies no volume or route for the alleged chips, so the effect on NVIDIA&\#x27;s China revenue or on Chinese domestic substitution cannot be measured from this source.

**Tags**: `#英伟达`, `#对华出口管制`, `#AI 算力`, `#Blackwell`

---

<a id="item-chip-news-14"></a>
### [Kantrowitz: Nvidia&\#x27;s China chip access narrowing, no new policy detail](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503c7c55460c9420dbac114b5cc6&amp;url=https%3a%2f%2fwww.msn.com%2fen-us%2fnews%2fother%2fchina-s-nvidia-chip-access-is-closing-fast-says-big-technology-s-alex-kantrowitz%2fvi-AA2in23A&amp;c=481846134368304326&amp;mkt=en-us) ⭐️ 4.0/10

Alex Kantrowitz, founder of the Big Technology newsletter, said in a CNBC &quot;Squawk on the Street&quot; segment that Nvidia&\#x27;s access to China&\#x27;s chip market is closing quickly, discussing recent reports and crackdowns and what they mean for semiconductor companies. The supplied material contains no new policy provisions, effective dates, shipment or revenue figures, product names, or verified regulatory decisions, so the segment is commentator analysis rather than a confirmed development. It reflects how one close industry observer characterizes the direction of U.S.-China chip restrictions, not an enacted rule or a change in what Nvidia is permitted to sell in China.

rss · Bing News - China chip policy · Nov 27, 09:34

**「Background」** The segment follows repeated rounds of US export-control tightening that have progressively narrowed which Nvidia accelerators can be sold to Chinese customers, and parallel Chinese regulatory scrutiny of those purchases. The supplied interview description does not identify which specific rule, licence decision or product change prompted the discussion, so the immediate predecessor cannot be pinned down from this source.

**Tags**: `#英伟达`, `#对华出口管制`, `#中美芯片合作`, `#AI 算力`

---

<a id="item-chip-news-15"></a>
### [A-share AI compute chip shares rise on vague policy, HBM catalysts](http://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;tid=6b0a503df3074614a5e322ce3dc9e7d5&amp;url=https%3a%2f%2fnews.qq.com%2frain%2fa%2f20261127A0AXO200&amp;c=8859260584746268499&amp;mkt=en-us) ⭐️ 4.0/10

On Nov 27, A-share shares in computing chips, memory and optical communications strengthened in afternoon trading, with a Chinese report attributing the move to domestic intelligent-computing construction planning and progress in high-bandwidth memory \(HBM\) R&amp;D. The report cites a State Council executive meeting that day as the news catalyst, but gives no specific policy provisions, named chip products, process nodes, capacity or shipment figures, and does not identify the companies behind the HBM progress. The article is primarily a promotion of two Yongying ETFs — the STAR/ChiNext AI ETF \(159141\) and the STAR chip-design ETF \(589420\) — rather than a report of confirmed industry developments, so the catalysts remain loosely described.

rss · Bing News - China domestic chips · Nov 27, 07:09

**「Context」** The Nov 27 move was attributed in the source to a State Council executive meeting held the same day that took up domestic intelligent-computing construction planning, although the brief did not reproduce specific provisions, funding levels or effective dates. The report also cited progress in high-bandwidth memory \(HBM\) research and development as a second catalyst lifting storage-related shares, again without naming a product, process node or shipment volume. No earlier policy stage, prior product generation or documented capacity milestone was supplied that would establish a direct predecessor to either catalyst.

**「Impact」** Because the report does not specify which measures the State Council meeting discussed or which companies reported HBM progress, it establishes no concrete change to China&\#x27;s domestic AI-compute supply, HBM output or licensing conditions; the share-price move and ETF promotion should be read as market commentary rather than evidence of new capacity or shipments.

**Tags**: `#国产芯片`, `#AI 算力`, `#高带宽存储`, `#中国政策`, `#ETF`

---

<a id="item-chip-news-16"></a>
### [Penguin Revives Retired DDR4 for AI Server Memory Expansion](https://www.eetimes.com/penguin-revives-retired-ddr4-for-ai-servers/) ⭐️ 4.0/10

EE Times reports that Penguin is reviving retired DDR4 for use in AI servers, positioning reused DRAM as a way to meet memory expansion demand. According to the report, hyperscalers already reclaim older DRAM, while enterprises have been slower to reuse DDR4. The item does not provide capacity, cost, deployment or customer figures, and does not specify which Penguin products or server configurations use the reclaimed modules.

rss · EE Times · Nov 27, 19:17

**「Background」** Penguin Solutions had already moved into AI memory expansion through a collaboration with Marvell Technology announced in mid-November 2026, under which the two companies said they were developing two complementary memory expansion technologies for AI infrastructure as demand shifted from training toward large-scale inference \(tool-2-1, tool-2-3\). The current report adds a different lever: reusing retired DDR4 modules rather than new memory products, and it notes that hyperscalers already reclaim older DRAM while enterprise customers have been slower to adopt the practice.

**「Impact」** If enterprises follow the hyperscaler practice described by EE Times, reclaimed DDR4 could offer a lower-cost path to memory expansion in AI servers; however, the source offers no shipment, pricing or customer evidence to show that enterprise adoption is actually occurring.

<details><summary>References</summary>
<ul>
<li>Marvell and Penguin Solutions Collaborate on AI Memory - TechIntelPro</li>
<li>Penguin Solutions&#x27; Post - LinkedIn</li>

</ul>
</details>

**Tags**: `#AI 算力`, `#DRAM`, `#AI 服务器`, `#供应链`

---

## Financial News

<a id="item-finance-news-1"></a>
### [国常会：加力发挥“国家队”稳市作用，优化中央汇金类“平准基金”功能](https://www.tmtpost.com/nictation/8220182.html) ⭐️ 8.0/10

China&\#x27;s State Council pledged to reinforce capital-market stabilization through a stronger &\#x27;national team&\#x27; and an optimized Central Huijin quasi-stabilization fund, alongside measures on dividends/buybacks, long-term fund inflows, and stricter market supervision.

telegram · zaihuapd · Nov 27, 05:35

**Tags**: `#China policy`, `#capital markets`, `#Central Huijin`, `#market stabilization`, `#long-term capital`

---

<a id="item-finance-news-2"></a>
### [蜜雪冰城5亿元入股DeepSeek新一轮融资，规模约千亿元](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

据搜狐网报道，DeepSeek已完成第二轮融资，规模在1000亿至1055亿元之间，投后估值约6155亿元；蜜雪冰城股份有限公司认缴出资5亿元，腾讯、宁德时代、中国移动、vivo等共31家新出资人参与。该报道并非公司正式披露，相关数字尚未获独立确认。

telegram · zaihuapd · Nov 27, 06:33

**「Background」** DeepSeek previously drew reports of a restart in fundraising at an around RMB 500 billion valuation, according to Chinese media coverage. The latest round has been reported by outlets citing The Information, but the figure here comes from a Sohu article relayed by a Telegram channel rather than a company disclosure.

**「Impact」** Mixue Bingcheng&\#x27;s RMB 500 million commitment is small next to its reported RMB 58.9 billion 2025 net profit, but it links a mass-market tea chain&\#x27;s balance sheet to a private AI valuation. The reported investor list also ties DeepSeek to strategic backers from social media, batteries, telecom and smartphones, including Tencent, CATL, China Mobile and vivo.

<details><summary>References</summary>
<ul>
<li><a href="https://m.zhibo8.com/news/web/game/2026-10-31/6ae5662e6dfe9native.htm">估 值 6155 亿 元！ 曝 DeepSeek 第 二 轮 融 资 1055...</a></li>
<li><a href="https://post.smzdm.com/p/aom07rr7/">DeepSeek 估 值 5000 亿 重启 融 资 ，自建智算 中 心并涨价_IT...</a></li>
<li><a href="https://www.lanjinger.com/d/1774341739896494779">蜜 雪 冰 城 ： 2025 年 营 收 335 . 6 亿 元， 净 利 增长32.7%_ 资 讯-蓝鲸财经</a></li>
<li><a href="https://www.tmtpost.com/7928831.html">2025 ...</a></li>
<li><a href="https://h5.ifeng.com/c/vivoArticle/v002UtHhgw77dRdxNzTFeRoS4faeb5ZiwCICSIP80nmlkms__?isNews=1&amp;showComments=0">甜香酸涩苦：五大奶茶品牌的 2025 年报</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#private financing`, `#valuation`, `#strategic investors`, `#China tech`

---

<a id="item-finance-news-3"></a>
### [央行下调大额存单起购门槛，个人降至10万元](https://www.news.cn/fortune/20261127/70789d77822242cc82216f51a416f872/c.html) ⭐️ 7.0/10

中国人民银行11月27日公布《大额存单管理办法》，将个人投资人认购起点从20万元降至10万元、机构从1000万元降至500万元，两个门槛均下调一半，自2027年3月21日起施行。

telegram · zaihuapd · Nov 27, 11:36

**「背景」** 新办法取代2015年《大额存单管理暂行办法》和2016年第13号公告；同日央行还发布《人民币存贷款利率管理规定》，同自2027年3月21日起施行，要求金融机构自主确定存贷款利率，不得以高息揽储等不正当手段吸收存款。

**「影响」** 门槛下调后，个人和机构投资者能以更少资金购买大额存单；要求银行自主定价、禁止高息揽储，则可能改变银行吸收存款的竞争方式。

**Tags**: `#China central bank`, `#large-denomination CDs`, `#deposit rates`, `#banking regulation`, `#interest-rate policy`

---

<a id="item-finance-news-4"></a>
### [China regulator summons 15 e-bike makers over certification failures](https://www.news.cn/20261127/0c8c665ce70c417b9263b39fa8a519f0/c.html?hl=zh-CN) ⭐️ 7.0/10

China&\#x27;s State Administration for Market Regulation summoned 15 electric bicycle manufacturers—including Yadea, Tailg, Aima, Ninebot and Niu—on Nov. 27, ordering them to rectify quality-control and product-consistency problems found in its full-coverage spot checks of CCC certification. Regulators also required recalls of confirmed defective products and barred companies from shifting responsibility to consumers or refusing returns.

telegram · zaihuapd · Nov 27, 12:06

**「Background」** China requires electric bicycles sold domestically to hold CCC certification and comply with mandatory national standards; the regulator said its full-coverage &quot;flying check&quot; inspections found quality-assurance gaps and weak product-consistency controls at some companies. The &quot;one vehicle, one battery, one charger, one code&quot; rule ties each bike to a matched battery, charger, and traceability code to keep uncertified or incompatible components out of the market.

**「Impact」** Owners of defective e-bikes gain a stated right to recall and return without being pushed toward discounted trade-ins or told to ride unregistered; the 15 named manufacturers must fix production and after-sales practices across their model lines.

**Tags**: `#regulation`, `#electric-bicycles`, `#consumer-safety`, `#manufacturing`, `#China`

---