---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 38 items, 7 important content pieces were selected

---

**Technology News**
1. [Lovable apps leak passport details and 200K private messages via weak RLS](#item-tech-news-1) ⭐️ 8.0/10
2. [SpaceX catches Starship upper stage after orbital Flight 15](#item-tech-news-2) ⭐️ 7.0/10
3. [Project Zero to shorten vulnerability disclosure windows to 60 and then 30 days](#item-tech-news-3) ⭐️ 7.0/10
4. [EFF argues tech firms are redefining privacy again](#item-tech-news-4) ⭐️ 7.0/10
5. [Cloudflare open-sources Kitesurf, a stateless browser for AI agents](#item-tech-news-5) ⭐️ 7.0/10
6. [Italy&\#x27;s Garante Fines Meta €805M for Android Album Access](#item-tech-news-6) ⭐️ 7.0/10
7. [Tesla ties Cybercab operation to $299 monthly subscription](#item-tech-news-7) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Lovable apps leak passport details and 200K private messages via weak RLS](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

A security research report by Crissy Field found that apps built with Lovable exposed passport details and more than 200,000 private messages through misconfigured Row-Level Security. Lovable&\#x27;s head of security, posting as igorandri, said insufficient RLS was the root cause and that the platform automatically scans every app before publishing and offers a free deeper SAST scan, with &quot;Fix&quot; and auto-fix options for findings. The report&\#x27;s findings and the vendor&\#x27;s account are not independently verified in the supplied material.

hackernews · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**「Background」** Row-Level Security \(RLS\) is the database access-control layer that decides which rows a given user or client can read or write. It matters for AI app builders such as Lovable because generated apps can query a Supabase backend directly from the browser, so missing or overly broad RLS policies can expose other users&\#x27; records.

**「Required release check」** Users of the affected Lovable-built apps had passport details and more than 200,000 private messages exposed through misconfigured Row-Level Security, so developers cannot treat a published frontend as proof that the backend is access-controlled. Supabase&\#x27;s post-Oct. 30 permission change also means new public tables are no longer automatically reachable by the anon/authenticated API roles, making explicit RLS policies and table grants a required release check.

**「Community discussion」** One commenter argued that Supabase shares responsibility, saying a defaults change was reported fixed on October 30 but may still not apply to existing projects. Others argued that platforms need deny-by-default databases, least-privilege APIs, and automated authentication tests, and that AI-generated apps are numerous and easy for non-experts to target.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/syed_shaameerali_52c39bf/supabase-permission-denied-for-table-42501-after-the-oct-30-change-the-fix-3dco">Supabase “permission denied for table” (42501) after the Oct ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI app builders`, `#Supabase`, `#row-level security`, `#data exposure`

---

<a id="item-tech-news-2"></a>
### [SpaceX catches Starship upper stage after orbital Flight 15](https://www.spacex.com/launches/starship-flight-15) ⭐️ 7.0/10

SpaceX&\#x27;s Flight 15 ended with the Starship upper stage caught by the launch tower after roughly 22.5 hours in orbit and about 14 revolutions of Earth—a first for a ship returning from orbit, according to reports citing the company. The flight deployed all 26 Starlink V3 satellites, three of which carried cameras to inspect heat-shield tiles. The Super Heavy booster did not return to the tower as planned and instead splashed down in the Gulf of Mexico, so SpaceX did not complete a two-stage catch. The cause of the booster&\#x27;s failure to return was not disclosed.

hackernews · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**「Background」** Starship is SpaceX’s two-stage, fully reusable launch system, made up of the Super Heavy booster and the Starship upper stage; Flight 15 was the 15th integrated test of the vehicle. The ship returns from orbital velocity, while Super Heavy reaches only about 6,000 km/h before heading back, so the ship’s heat shield and precise terminal descent are central to the tower-catch approach.

**「Impact」** The immediate consequence for SpaceX is a recovered orbital-class ship available for post-flight inspection; the mission did not demonstrate reflight or a simultaneous booster-and-ship catch.

**「Community Discussion」** Commenters framed the catch as a reusability milestone but focused on what remains unproven: whether the heat shield holds up, whether both stages can be caught, and whether the same ships can be re-flown. One commenter compared Starship to a corrected Space Shuttle design, while another questioned the eventual mass fraction to orbit.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnn.com/2026/11/13/science/live-news/spacex-starship-flight-15-ship-catch">Live updates: SpaceX Starship nails historic ship catch in... | CNN</a></li>

</ul>
</details>

**Tags**: `#spaceflight`, `#reusable rockets`, `#hardware`, `#engineering`, `#SpaceX`

---

<a id="item-tech-news-3"></a>
### [Project Zero to shorten vulnerability disclosure windows to 60 and then 30 days](https://projectzero.google/2026/11/disclosure-policy.html) ⭐️ 7.0/10

Google Project Zero announced a staged tightening of its vulnerability-disclosure policy: reported vulnerabilities will be disclosed 90 days after vendor notification for now, 60 days starting February 2, 2027, and 30 days starting January 3, 2028. The change affects vendors that receive Project Zero reports and the security teams responsible for patching them, compressing the prior 90-day norm in two steps. The supplied item does not detail exceptions, extension rules, or how the deadlines will be enforced.

hackernews · hacb · Nov 14, 11:13 · [Discussion](https://news.ycombinator.com/item?id=50496051)

**「Background」** Project Zero is Google&\#x27;s vulnerability research team, and its disclosure deadlines have long served as an industry reference point for coordinated disclosure — the window a vendor gets to ship a fix before technical details become public. The staged rollout is labeled &quot;Full 90&quot;, &quot;Full 60&quot; and &quot;Full 30&quot;, wording that implies the current arrangement still leaves some room past the headline deadline, which is why the reaction treats the change as a tightening rather than a loosening.

**「Shorter patching window」** Vendors and maintainers will have less time to develop, test, and ship fixes, with the sharpest adjustment arriving when the window falls to 30 days in 2028. Security teams should plan for shorter triage and release cycles rather than assuming the 90-day window remains the norm.

**「Community discussion」** Commenters questioned whether a 30-day window is realistic for large projects, with one saying Ubuntu would need much more time, while another argued for immediate disclosure because only pressure compels vendors to fix flaws. A separate comment raised concern that companies discovering bugs could use access to their products as leverage to push adoption of their own LLMs.

**Tags**: `#vulnerability disclosure`, `#Project Zero`, `#security policy`, `#zero-day vulnerabilities`, `#cybersecurity`

---

<a id="item-tech-news-4"></a>
### [EFF argues tech firms are redefining privacy again](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 7.0/10

An EFF opinion analysis argues that technology companies are again trying to shift the meaning of privacy, with the debate centered on AI meeting transcription, workplace surveillance norms, and accessibility. The piece is advocacy and analysis rather than a report of a new product or an independently measured technical result. The supplied material does not identify specific companies, proposals, or policy changes behind the claim.

hackernews · gslin · Nov 14, 12:45 · [Discussion](https://news.ycombinator.com/item?id=50496602)

**「Ambient-recording backdrop」** EFF’s Thorin Klosowski frames the debate as a shift from privacy as an individual choice to a bystander problem, citing Meta and Google smart glasses that can record and describe what the wearer sees, Apple’s Audio Intelligence feature turning the Apple Watch into a transcription device, and Amazon’s Bee devices that record and transcribe continuously. Those examples set up the consent question the analysis addresses: whether people around a device can avoid being captured.

**「Impact」** The discussion points to a practical design fork: local, non-retaining transcription can serve deaf and hard-of-hearing users, while default recording and retention in workplace meetings creates an opt-out problem for participants.

**「Community discussion」** Commenters debated whether workers can refuse AI notetakers without hurting their employment, with one asking how to establish a norm of turning transcription off for sensitive meetings. Another argued that live transcription can be transformative for deaf and nearly deaf users, especially if it runs locally without saving or exporting data, while acknowledging that retention is only one design choice away.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.my/items/46520/tech-companies-are-trying-to-shift-the-concept-of-privacy-again">Tech Companies Are Trying to Shift the Concept of Privacy (Again)</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#AI surveillance`, `#tech policy`, `#human rights`, `#EFF`

---

<a id="item-tech-news-5"></a>
### [Cloudflare open-sources Kitesurf, a stateless browser for AI agents](https://www.phoronix.com/news/Cloudflare-Kitesurf-Open-Source) ⭐️ 7.0/10

Cloudflare has open-sourced Kitesurf under the Apache 2.0 license; it is a stateless browser aimed at AI agents. Built on Cloudflare Workers, it parses HTML, processes CSS, and executes JavaScript without requiring a browser container, and the code is available on GitHub. Cloudflare says the design uses less CPU and memory than Chromium and can scale on its Workers network, but the source provides no benchmark figures or compatibility details.

telegram · zaihuapd · Nov 14, 09:33

**「Why a browser without a browser engine」** AI agents that read or interact with web pages have conventionally been paired with full browser engines such as headless Chromium, driven through automation frameworks — an approach that is heavy on CPU and memory and awkward to scale across many concurrent tasks. Kitesurf&\#x27;s premise is to move that work onto Cloudflare Workers, a serverless runtime, so that HTML parsing, CSS handling and JavaScript execution happen without a browser container. Cloudflare has published the code on GitHub under Apache 2.0.

**「Impact」** Teams building AI agents can evaluate Kitesurf as a Workers-native alternative to provisioning a separate browser container for parsing HTML, applying CSS, and running JavaScript. Cloudflare&\#x27;s claim that it uses less CPU and memory than Chromium remains unverified because the source publishes no benchmarks.

**Tags**: `#Cloudflare`, `#AI agents`, `#open source`, `#browser`, `#Cloudflare Workers`

---

<a id="item-tech-news-6"></a>
### [Italy&\#x27;s Garante Fines Meta €805M for Android Album Access](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10321080) ⭐️ 7.0/10

Italy&\#x27;s privacy regulator, Garante Privacy, fined Meta €805 million, saying the Facebook Android app&\#x27;s album recommendation feature accessed the photos, videos, and metadata of about 20 million Italian users without specific consent. The feature, launched in 2023, was on by default and used a generic permission prompt, according to the regulator. Meta has 60 days to make the feature default-off and obtain separate user consent, or it cannot be enabled for users who have not validly authorized it.

telegram · zaihuapd · Nov 14, 14:37

**「Consent rules behind the case」** Under the EU&\#x27;s General Data Protection Regulation, consent must be specific, informed and unambiguous, which is why a pre-enabled setting paired with a broad permission prompt is legally exposed. The album-recommendation feature at issue in this case went live in 2023 and stayed on by default, and that is the arrangement Italy&\#x27;s Garante assessed.

**「Compliance deadline」** Meta has 60 days to make the Facebook Android album-recommendation feature off by default and obtain separate consent. If it misses that deadline, the feature cannot be enabled for Italian users who have not given valid authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cwn83gxemk35o">Italy fines Meta € 805 m over accessing users&#x27; photos</a></li>

</ul>
</details>

**Tags**: `#privacy-regulation`, `#meta`, `#mobile-permissions`, `#data-protection`, `#italy`

---

<a id="item-tech-news-7"></a>
### [Tesla ties Cybercab operation to $299 monthly subscription](https://www.tesla.com/configurator/api/v4/terms?category=autonomy_subs&amp;amp;locale=en_US&amp;amp;model=cc&amp;amp;saleType=Sale) ⭐️ 7.0/10

Tesla&\#x27;s Cybercab subscription terms require a $299 monthly autonomous-driving payment for the vehicle to operate, with the car listed at $29,990. The document says Tesla can change the subscription price with one month&\#x27;s notice, and that nonpayment or misuse can trigger suspension or cancellation; three cumulative warnings disable autonomous driving for one week. It also limits operation to designated areas and bars unauthorized use on ride-hailing, delivery, or rental platforms. The terms were reported via a Telegram aggregator and have not been independently verified here.

telegram · zaihuapd · Nov 15, 01:10

**「Background」** Tesla&\#x27;s Full Self-Driving feature for ordinary owners still requires human supervision, according to the source, while the Cybercab is intended for driverless operation. The reported terms make an autonomous-driving subscription mandatory for the car to run at all; Verge coverage says the $29,990 Cybercab is initially offered to select customers with an Austin-only geofence, and Daily Sabah reports availability is limited to areas where Tesla supports its autonomous service.

**「Impact」** For buyers, the sticker price understates the commitment: the car&\#x27;s use depends on an ongoing $299 monthly payment, and Tesla&\#x27;s one-month price-change right means that recurring cost can rise. Commercial operators also cannot treat the Cybercab as an unrestricted ride-hailing, delivery, or rental vehicle without authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/transportation/1033844/tesla-personal-cybercab-orders-299-subscription-fine-print">Tesla is inviting some people to buy a Cybercab ‘for personal use ...</a></li>
<li><a href="https://www.dailysabah.com/business/tech/tesla-opens-cybercab-sales-to-select-customers-for-29990">Tesla opens Cybercab sales to &#x27;select customers&#x27; for $ 29 , 990</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#Cybercab`, `#autonomous driving`, `#subscription model`, `#software-defined vehicles`

---