# Interview Prep: Senior Client Delivery Manager — Worldpay Round 2

**CV:** ArpitaNarula-TwoPage-SCDM-Worldpay-Apr26.md
**Round 1 prep:** Interview-Worldpay-SeniorClientDeliveryManager.md
**Interview:** 29 Apr 2026
**Interviewer:** Ajay Singh (Director, POS Centre of Excellence)

---

## What Ajay Is Looking For in Round 2

- **Seniority** - enterprise-scale accountability, not just execution
- **POS domain gap** - credible ramp-up story; past examples of closing gaps fast
- **Retention** - committed to client delivery long-term; not a product stepping stone
- **Escalation handling** - real examples; JD explicit: resolve and prevent recurrence
- **Cross-functional complexity** - merchants, integrators, product, commercial, technical simultaneously
- **Strategic thinking** - influencing upward, OKR ownership, shaping approach
- **CoE contribution** - recruitment, training, OKRs, continuous improvement
- **Client relationship depth** - probed in Round 1; wants evidence of managing diverse client personalities, not just delivering projects
- **Self-awareness** - competency round will include a failure question; looking for ownership and learning, not defensiveness
- **Structural change confidence** - Global Payments acquisition adds uncertainty; needs assurance she is stable through organisational change

| Deep Dive Area | STAR / Scenario |
|---|---|
| Enterprise-scale delivery ownership | STAR 1 - Shell GO+ replatform: 10M users, 4 markets, £100M+ transactions |
| Difficult client / escalation handling | STAR 3 - Shell POS vendor delay; STAR 6 - Argos UAT pushback |
| Multi-party delivery under pressure (POS-specific) | Situational 2 - POS go-live: merchant + integrator + internal product misaligned |
| Commercial pressure vs delivery reality | Situational 1 - client demanding more, commercial saying yes, engineering saying no |
| Influencing without authority | STAR 2 - Estée Lauder 17 brands |
| Strategic influence upward | STAR 8 - Shell NL cutover: site-type wave approach recommended to and adopted by programme and Shell sponsors |
| Trade-off to protect delivery | STAR 5 - Shell Pilot data ingestion |
| Team / CoE contribution within portfolio | STAR 4 - Costa Coffee team CI (3x velocity) |
| Contribution beyond own project | STAR 7 - Costa Coffee intake process redesign |
| Change management / service transition | STAR 9 - Worldpay ServiceNow migration |
| POS domain gap - ramp-up credibility | STAR 3 (POS-adjacent anchor) + Shell trajectory: FMCG data → Loyalty → POS |
| Retention - commitment to client delivery | Not a STAR - framing: delivery not product; dual perspective (provider + client) is the value |

---

## Q&A — Strengthened for Round 2

---

**How did you work with the different brand managers, because you will be working with different types of clients?**

> - 17 brand managers = 17 different clients
> - Different commercial pressures, digital maturity, risk appetite per brand
> - MAC: volume-driven, trend-reactive vs La Mer: ultra-premium, different journey
> - Backlog prioritisation per brand: evidence and business case behind each change
> - Tailored approach: data-literate managers moved on evidence; others needed competitor examples or peer pilot results first
> - Phased rollout: coalition-building, not just risk management
> - 5 pilot brands: managers already bought in
> - Pilots became advocates; wave 2 sold proven results to peers, not a concept
> - Pushback: understood constraint first (deadline, disruption risk), reframed sequence
> - Escalated to CX leads only if reframing failed
> - NA/EMEA split: separate demo cadences per region; cross-region decisions communicated quickly
> - Punchline: relationship management discipline, not process; business case opens door, relationship determines movement

If probed: how was the 3% conversion improvement measured?

> - Google Analytics; estate-wide baseline per brand before rollout
> - 3% estate-wide average; pilot brands showed lift first
> - Primary driver: checkout flow module; shade selector secondary
> - Lift confirmed 6 weeks post-pilot rollout
> - Pilot results used to bring resistant managers on board in wave two

If probed: which brand manager was most resistant?

> - Clinique: large NA brand, high traffic, protective in-house tech team
> - Objection: timing, not the component; peak trading disruption risk
> - Did not escalate; understood the constraint first
> - Offered post-peak onboarding window with fixed commitment date
> - Agreed and joined wave two without further pushback

If probed: how did you choose the 5 pilot brands?

> - Manager already bought in; not in peak trading; tech stack compatible without major rework
> - At least one NA, one EMEA brand in the set
> - Excluded brands mid-initiative or with regulatory deadlines
> - Goal: results credible to the most sceptical wave-two managers

---

**Tell me about the most complex delivery you have led end to end.**

> - Shell GO+ loyalty replatform
> - 10M+ users, £100M+ annual transactions, EMEA
> - 4 markets: Netherlands, Austria, Germany, Hungary
> - Cross-functional: POS, Mobile, MuleSoft, third-party vendors
> - Accountable to Shell Technology Director and Marketing Director
> - Fortnightly Steering Committee from day one
> - Budget tracked per market; staggered rollout per region
> - Scheidt & Bachmann release cycle misaligned in NL; raised formally; decoupled via MuleSoft
> - All 4 markets on time; 10% under forecast (£350K on £3.5M budget)
> - Dependency map updated for remaining markets post-NL
> - Punchline: scale managed through governance discipline; early dependency surfacing made on-time delivery possible

If probed: POS vendor and the misalignment?

> - Scheidt & Bachmann Energy Retail Solutions: Shell's primary POS vendor, German-based
> - NL delivery: firmware release window fell after GO+ go-live date
> - Impacted: POS-side loyalty updates, GO+ points accrual at forecourt terminal
> - Raised directly with S&B; release cycle fixed, could not move
> - Escalated to Steering with options and consequences before any commitment
> - Technical SMEs: identified loyalty logic decoupling from firmware dependency
> - MuleSoft route: loyalty accrual handled API-side; POS terminal passed transaction data; MuleSoft processed points independently of firmware version
> - Additional integration testing added to go-live checklist
> - NL released on time; S&B firmware applied in next scheduled cycle cleanly
> - S&B release windows mapped across all remaining markets before Austria delivery

If probed: the 10% saving?

> - Budget: £3.5M across four markets
> - Saving: £350K (10% under forecast)
> - NL learnings applied to AT, DE, HU: reduced rework, re-testing, contingency
> - S&B dependency mapped upfront for remaining markets: no unplanned delays
> - Change requests formally assessed; scope creep caught early

If probed: Steering Committee?

> - Shell Technology Director and Marketing Director as senior sponsors
> - Programme leadership from delivery partner and key vendors
> - Fortnightly cadence throughout
> - Escalated: cross-market dependencies, budget variance, vendor risk, go/no-go per market, scope above threshold
> - Resolved below: sprint issues, vendor day-to-day, minor timeline adjustments within tolerance
> - S&B misalignment escalated with recommendation; decoupling decision made at Steering level

If probed: why that market order?

> - NL first: most mature, geographically close, lowest localisation risk
> - AT next: similar regulatory environment to NL, smaller user base
> - DE third: largest market by volume; NL and AT learnings applied before highest-stakes go-live
> - HU last: highest localisation complexity, most stakeholder alignment needed
> - Each cutover plan updated from previous market's go-live

---

**Describe a time you had to manage a difficult client situation or escalation.**

Primary: Shell POS vendor delay

> - Shell multi-market rollout, tight timeline
> - Scheidt & Bachmann release cycle misaligned with go-live date
> - Risk: NL market release date blocked
> - Raised formally before it became a crisis
> - Technical SMEs: decoupling path identified; routed via MuleSoft
> - Revised credible timeline given to POS teams
> - NL released on time
> - Dependency map restructured for subsequent markets
> - Punchline: come out with stronger structure than you went in with

If probed: what did the Shell stakeholder conversation look like?

> - Shell Technology Director: primary sponsor; needed confidence to communicate to their own business
> - Raised at Steering with options and consequences, not just the problem
> - Option A: wait for S&B release cycle; market delayed
> - Option B: decouple via MuleSoft; market on time; additional integration testing required
> - Shell approved Option B at Steering; decoupling approach signed off before any commitment to POS teams
> - Gave Shell a credible revised path before the meeting closed; no open uncertainty left with the client

If probed: what was the conversation with Scheidt & Bachmann?

> - Raised directly with S&B account and project contacts
> - Release cycle confirmed fixed; could not be brought forward commercially or contractually
> - Decision: not to escalate commercially; MuleSoft route faster and lower risk than forcing a vendor release change
> - S&B informed of decoupling approach; confirmed firmware would land in next scheduled cycle
> - Maintained the relationship; no adversarial dynamic; S&B delivered cleanly in their next cycle

Secondary if probed: Argos UAT pushback

> - IBM Commerce platform for Argos
> - Client pushed back at UAT; functionality did not match expectations
> - UAT was client's first view of the product
> - Acknowledged without defensiveness; treated as valid signal
> - Structured session: expected vs delivered, feature by feature
> - Separated delivery gaps from scope never agreed at sign-off
> - Root causes: ambiguous requirements at sign-off; no mid-build demos
> - Prioritised recovery list: must-fix vs post-launch
> - Remaining window restructured; fortnightly demos introduced
> - Gaps resolved within window; timeline protected; relationship recovered
> - Practice changed: AC agreed before build; demos embedded throughout
> - Punchline: UAT surprise is a requirements and engagement failure; fix, own, change the process

If probed: how did you handle telling the client something was out of scope?

> - Argos Digital Director: senior stakeholder, high expectations, initial reaction was adversarial
> - Did not get defensive; opened the signed SoW in the session
> - Mapped expected features against what was formally agreed at sign-off, line by line
> - Some features: genuine delivery gaps; owned those immediately
> - Others: discussed during discovery but never formally agreed; showed the evidence
> - Tone: not adversarial; framed as here is what we committed to, here is what we can absorb, here is what needs a separate conversation
> - Argos initially pushed back on the distinction; held the line but kept the door open on a recovery path
> - Offering a prioritised recovery list shifted the conversation from dispute to resolution

If probed: what actually recovered the relationship?

> - Fortnightly demos: gave Argos visibility they had never had before; no further UAT surprises
> - Progress visible in real time; trust rebuilt incrementally through delivery, not assurances
> - Digital Director signed off delivery at close; relationship intact
> - Follow-on phase of feature delivery commissioned post go-live; relationship continued into next programme cycle

---

**Situational: You are leading a high-profile enterprise POS integration. The merchant wants an aggressive go-live across multiple markets. The integrator is behind on certification. Internal product has open gaps. Talk me through how you handle this.**

> - Reframe: not are we on track; what is minimum viable go-live and trade-offs
> - Goal: controlled delivery, no surprises
> - Day one triage in parallel: product, integrator, critical path
> - Product: Day 1 critical vs deferrable
> - Integrator: challenge vague blockers with specifics; what is blocking, what delivers in two weeks
> - Go-live scope in three layers: Day 1 critical / controlled degradation with merchant sign-off / post-go-live backlog with committed timeline
> - Merchant: options with consequences, not problems
> - Option A: keep date, reduce scope; CX impact explicit
> - Option B: partial rollout; specific stores or markets first
> - Option C: delay; commercial risk quantified
> - Integrator: daily checkpoint cadence; commercial escalation if commitments slip
> - Internal product: escalate with business case; push for workaround or feature toggle
> - Anchor: Shell NL; Scheidt & Bachmann misalignment; decoupled via MuleSoft; released on time
> - Punchline: controlled delivery with no surprises; protect CX and long-term merchant trust

---

**How will you close the POS domain knowledge gap and ramp up fast enough for a senior client-facing role?**

> - Not starting from zero
> - Shell GO+: managed Scheidt & Bachmann release dependencies across 4 markets
> - Costa Coffee: POS and kiosk telemetry pipelines into Azure DWH
> - Worldpay TSA: POS-adjacent workstreams; compliance and vendor landscape from inside
> - Trajectory: FMCG loyalty at Shell, then web/mobile, then POS-adjacent in same programme
> - Understand POS from the merchant side: Shell was a high-volume forecourt merchant; POS uptime and loyalty accrual were business-critical
> - Already inside Worldpay: know the product suite, internal teams, delivery standards; not starting cold on the organisation either
> - Track record of publishing on new domains: AI governance, GenAI delivery; same pattern of structured self-education applied to POS payments
> - First 30 days: build vocabulary; shadow client calls; build relationships with Technical Consultants and Implementation Managers
> - Won't overclaim technical depth; right questions, right specialists
> - Punchline: domain knowledge is learnable; delivery credibility is not

---

**You come from a product background. How do we know you will stay once we have trained you?**

> - Product involvement always adjacent to delivery, not a career ambition
> - Shell, Estée Lauder, Worldpay: accountable to business sponsors for delivery outcomes
> - Most valuable work: client relationship, escalation, cross-functional coordination under pressure
> - Product does not offer that intensity or scale
> - Opportunities to move into product; did not take them
> - Worldpay contract ended due to org restructure; chose to come back for this role specifically; that is a deliberate choice, not default
> - Consistent pattern across 15 years: always returned to client-facing delivery; no detours into product ownership
> - Volunteer PM at Eco Centre CBS: commits to roles without financial incentive; not someone who leaves when a shinier option appears
> - SCDM scope: Europe, US, Australia; enterprise merchants; the right level of challenge
> - Punchline: delivery is the work I want; this role is where that challenge exists

---

**Tell me about a time you had to make a trade-off to protect delivery.**

> - Shell; ready to progress to Pilot stage
> - Data ingestion from legacy to new system: tested and working in lower env
> - Failed in live environment; came to a halt
> - Root cause: production data volumes significantly larger than lower-env test data; ingestion timed out under load
> - Two options: delay Pilot to fix full ingestion (weeks) vs proceed with subset data load, resolve in parallel
> - Presented options and recommendation to Shell Technology and Marketing sponsors
> - They needed confidence to communicate to their own business stakeholders
> - Recommended: proceed Pilot with subset; resolve full ingestion in parallel
> - Shell approved; Pilot commenced on schedule
> - Full data load completed within two weeks
> - Punchline: separate the problems; on-time Pilot does not require complete data load; once split, path forward was clear

If probed: what was the risk of going live on partial data?

> - Pilot users had incomplete loyalty history on launch
> - Risk scoped and accepted: Pilot was a controlled cohort, not full customer base
> - Shell communicated to Pilot users that historical data would be available within two weeks
> - Points accrual was live from day one; no transactions affected
> - Full data load completed before Pilot expanded to wider rollout

If probed: who made the final call?

> - Recommendation made to Shell Technology and Marketing sponsors
> - Shell business leadership made the final call; their risk to accept
> - Role: give a clear recommendation with consequences; not make the call for the client
> - Decision made with full information; no pressure to proceed without sign-off

---

**How have you contributed within your own project to the team or function?**

> - Costa Coffee; delivery capability inconsistent across team
> - Committed items not delivered within forecasted timeframes
> - Ran structured team workshop to diagnose root causes
> - Three systemic issues: no clear acceptance criteria; work thrown over fence without shared readiness; uncontrolled scope changes mid-sprint
> - Facilitated team agreement on Definitions of Ready and Done
> - Tighter requirements definition controls; tighter in-sprint change request process
> - Lightweight coaching: Lean/Agile, RAID, stakeholder engagement
> - Standardised delivery artefacts across workstreams
> - Team velocity doubled, then trebled within 3 months
> - Team shifted from reactive to proactive delivery posture
> - Punchline: 3x velocity from fixing handoffs and requirements, not from working harder

If probed: how was 3x velocity measured?

> - Story points completed per sprint tracked from baseline before changes introduced
> - Baseline over first 3 sprints; improvement tracked sprint by sprint after
> - Velocity doubled within 6 weeks of DoR and DoD adoption
> - Trebled within 3 months; sustained improvement, not a one-sprint spike

If probed: how did you get buy-in without a mandate?

> - Did not impose; ran diagnostic workshop first; team identified the issues themselves
> - When the team names the problem, they own the solution
> - Facilitated agreement on DoR and DoD rather than presenting a pre-built framework
> - Changes incremental; not a big-bang process overhaul
> - Benefit framed in terms the team cared about: less rework, fewer late nights, more predictable sprints

---

**How have you contributed outside your own project to the team or function?**

> - Costa Coffee; intake process informal: requirements added as one-liners directly to backlog
> - Priority driven by date of addition, not strategic value
> - No business case required; no clarity on ROI, sponsorship, or strategic alignment
> - Backlog cluttered; roadmap unclear; high-value and low-value requests treated equally
> - Designed structured intake template: objectives, business case, sponsorship, funding, ROI, impact of not doing
> - Ran sessions per function to help teams build strong submissions
> - Established review forum to assess and prioritise against strategic goals
> - Roadmap prioritised by value, not arrival date
> - Other business units adopted the process; cross-organisation impact beyond original team
> - Punchline: cluttered backlog is a strategy problem, not a capacity problem; fix intake and prioritisation takes care of itself

If probed: how did you get functions to change without a mandate?

> - Framed as helping them: better submissions meant faster approvals
> - First few submissions coached through the template in person; lowered the barrier
> - Early adopters got faster prioritisation decisions; others saw the benefit and followed
> - Adoption was organic; no function refused

If probed: what happened to requests that did not meet the standard?

> - Returned to submitter with specific feedback on what was missing
> - Not rejected outright; treated as coaching, not gatekeeping
> - Backlog cleared of one-liners over time as intake quality improved

---

**Tell me about a time you coordinated a technology migration with significant change management and business continuity requirements.**

> - Worldpay TSA Exit; ITSM tooling under FIS-managed ServiceNow instance
> - Hard deadline to exit FIS and stand up standalone Worldpay instance
> - ServiceNow underpins incident, change and problem management; zero downtime tolerance
> - Multiple business units; varied process maturity; no single change management authority
> - Mapped current-state service catalogue: incident, change, problem, request workflows
> - Identified integration dependencies: monitoring tools, CMDB feeds, vendor connectors
> - Service acceptance criteria and go/no-go checklist defined with IT leads and business stakeholders
> - RFC raised; CAB approval obtained for cutover event
> - Change freeze window agreed to minimise in-flight changes during migration
> - UAT with service desk leads: incident logging, change workflow, request fulfilment tested end to end
> - Operational Readiness Review with IT Operations, Security and business unit leads
> - Phased comms plan: awareness, readiness, go-live communications to all user groups
> - Training delivered to service desk agents and power users before cutover
> - Cutover executed to plan; parallel monitoring of both instances during transition window
> - Two-week hypercare: dedicated triage channel, daily stand-up with service desk leads
> - Zero ITSM downtime; all business units operational on Worldpay instance from day one
> - No P1 or P2 incidents attributed to cutover; SLA reporting reinstated on day one
> - Punchline: business continuity in an ITSM migration comes from the prep, not the cutover

If probed: who were the key stakeholders and at what level?

> - IT Operations lead and Security lead: signed off service acceptance criteria
> - Business unit leads: represented in Operational Readiness Review
> - Legal and HR: involved in cutover planning given sensitivity of data held in ServiceNow
> - CAB: formal approval for the cutover event
> - Steering Board: TSA Exit programme oversight; migration reported as a workstream delivery

---

**Can you give me an example where you influenced a strategic decision upward, rather than just presenting status?**

> - Shell GO+ NL market cutover; multiple site types across the estate
> - Site types varied by: retailer type, product range, applicable promotions
> - Not all test scenarios applicable to every site type
> - Risk of uniform cutover: mixing site types with different scenarios; failures hard to isolate; customer-facing impact uncontrolled
> - Recommended wave approach to programme and Shell sponsors: pilot per site type, not per geography or volume
> - Proposed starting with sites closed for construction or repair works: live environment, zero customer impact risk
> - Programme leadership and Shell sponsors adopted the approach
> - Local Product Analyst assigned to test each applicable scenario per site type on closed sites first
> - After successful validation of a site type: all live sites of that type switched to new platform
> - Repeated per site type until full NL estate migrated
> - Controlled cutover with no customer-facing incidents across the estate
> - Site-type validation model carried forward for subsequent markets
> - Punchline: presenting a cutover plan is not strategy; identifying the site-type risk and designing the wave model around it is; the closed-sites-first insight gave the team and Shell the confidence to proceed

If probed: what were the site types?

> - Shell Express (unmanned/automated): fuel only, card payment, basic GO+ points accrual; simplest scenario set; lowest risk for first wave
> - Manned forecourt with Shell Select shop: fuel plus convenience retail; combined basket promotions, product-level points multipliers; mid-complexity
> - Motorway service stations (snelweg): highest volume, extended trading hours, partner food outlets; most complex promotion and accrual combinations; final wave

If probed: what did the Product Analyst testing look like?

> - Local NL Product Analyst ran each applicable test scenario on the closed site
> - Scenarios covered: loyalty accrual, promotion application, transaction types relevant to that site type
> - Pass rate required before any live site of that type was switched
> - Failures resolved before moving to live sites; no known defect carried into live cutover
> - Sign-off per site type before the wave proceeded

If probed: what was the alternative and why was it rejected?

> - Alternative: uniform cutover across all sites on a single date or by geography
> - Risk: different site types have different applicable scenarios; a failure on a motorway service station mid-cutover would be high-volume, high-visibility
> - Wave approach isolated that risk; motorway stations were the final wave, by which point the model was proven on simpler site types

---

**Situational: You are leading a strategic client. They are unhappy due to delays and defects. Commercial is pushing to keep them happy at all costs. Engineering says it is out of scope. The client is asking for more features and faster delivery.**

> - First move: reframe the objective; not keep client happy at all costs; restore trust while protecting delivery integrity and commercial boundaries
> - Separate emotional escalation from structural problem; not the same conversation
> - Stabilise before accepting anything new: fix defects first; demonstrate improving quality with evidence
> - Adding scope on top of instability compounds the problem
> - Three clean tracks:
> - Track 1: defects and service recovery; our responsibility to fix
> - Track 2: contracted scope; committed, in progress, on track
> - Track 3: new feature requests; separate conversation, separate commercial process
> - Internal alignment before any client conversation
> - Push product and engineering with commercial context: strategic client, renewal at risk; where can we flex without breaking other commitments
> - Reset commercial: can support this client, not at the cost of delivery failure or uncontrolled precedent
> - Goodwill only where clearly at fault; not entitlement
> - Client conversation: options with consequences
> - Option A: current scope; timeline unchanged
> - Option B: add features; revised timeline or cost
> - Option C: prioritise new features; de-scope existing items
> - Time, scope and cost are linked; cannot flex all three simultaneously
> - Anchor: Shell go-live; POS vendor delayed; business directed Loyalty and Middleware to absorb out-of-scope POS work
> - Controlled the process: options explicit before decision; scope change formally documented; team protected from it becoming the new normal
> - Punchline: sometimes business overrides the recommendation; what matters is they do it with clear eyes

---

## Out of the Box - Be Ready For

**How do you feel about joining during a period of structural change with the Global Payments acquisition?**

> - Joined Worldpay during FIS carve-out; more disruptive than this; delivered through it from the inside
> - Structural change is where senior CDMs add most value
> - Not deterred by ambiguity; know the organisation, the standards, the people

**Tell me about a time you failed.**

> - Costa Coffee Azure DWH; schema change delivered to a core data pipeline
> - Upstream sources mapped and engaged; delivery completed
> - Finance team had a scheduled SQL extract pulling directly from the DWH for monthly cost and sales reconciliation
> - Owned outside the delivery team's scope; not identified or engaged at kick-off
> - Schema change broke the extract silently; Finance flagged it only when their month-end reconciliation failed
> - High-impact: financial reporting affected; urgent fix required
> - Owned it completely; no ambiguity about where the gap was
> - Finance team had to rework their extract on a compressed timeline; unplanned effort on their side
> - Failure: downstream consumers outside the immediate delivery scope not treated with same rigour as upstream sources
> - Learning: full landscape mapping at kick-off; upstream and downstream; who ingests, who consumes, who runs extracts against the schema
> - Downstream impact assessment added to RAID as standard on every subsequent delivery
> - Did not happen again on the programme

**What do you know about Worldpay's enterprise POS merchant base?**

> - Large retail: major high street and grocery chains, UK and Europe
> - Fuel: Shell is a Worldpay merchant; understand forecourt POS complexity from delivery side
> - Hospitality and QSR: high volume, uptime-critical POS
> - Omnichannel: in-store, self-checkout, mobile POS converging
> - Scheme mandates and PCI compliance driving upgrade cycles across the estate

---

## Questions to Ask in Round 2

<!-- - What does success look like in the first 6 months for this role?
- What is the biggest delivery challenge the CoE is navigating right now?
- How does the SCDM work day-to-day with the Technical Consultants and Implementation Managers? -->
- How is performance measured for the SCDM beyond delivery milestones — OKRs, client satisfaction, commercial outcomes?
- What is the biggest capability gap in the team right now?
- How do Technical Consultants feed merchant requirements or product gaps back into the product roadmap?
- How does the CoE handle situations where merchant expectations push beyond what the product can currently deliver?
- How are portfolios structured across SCDMs and CDMs — by merchant, sector, or geography?
<!-- - Europe, US, Australia timezone coverage: as Australian market matures, managed on the ground or centrally from UK long-term?
- POS CoE in combined Global Payments and Worldpay structure: expanding function or deepening service quality with existing merchants? -->

---

## Appendix — Worldpay POS Commercial Model

### The Layered Stack

- **Hardware** — POS terminal (Ingenico, Verifone, PAX); sourced by merchant or ISV; certified by Worldpay
- **ISV / merchant POS software** — EPOS or retail management system; owned by ISV; handles merchant business logic (inventory, orders, promotions); Worldpay does not touch this layer
- **Worldpay payment application** — sits on terminal or integrates via Worldpay SDK/API; handles payment flow; connects to Worldpay processing
- **Worldpay gateway and acquiring** — the core product; authorisation, capture, settlement, scheme connectivity; what Worldpay sells
- ISV integrates their software into Worldpay's payment layer using Worldpay APIs and SDK

### What Drives Product Enhancements

- **Scheme mandates** — Visa/Mastercard deadlines (contactless, SCA, tokenisation, network tokens); non-negotiable; both Worldpay and merchants/ISVs must update their respective layers
- **PCI-DSS** — evolving security standards; platform and integration changes required
- **Merchant requests** — enterprise merchants request specific features: loyalty integrations, BNPL, digital wallets, bespoke reporting; strategic merchants carry more roadmap weight
- **Competitive / market driven** — product team tracks Adyen, Stripe; builds to remain competitive (tap-to-phone, unified commerce, click-to-pay)
- **Sales team driven** — sales flags gaps blocking deals; feeds into product prioritisation

### Who Manages Enhancements

- Worldpay Product Management owns the roadmap
- Priority order: scheme mandates first (non-negotiable), then commercial impact, competitive positioning, strategic direction
- SCDM is the key conduit between merchant requirements and the product team
- JD explicit: collaborate with product on requested changes based on evolving customer needs
- SCDM role: capture merchant pain points; distinguish bespoke (one merchant) from systemic (multiple merchants); escalate systemic gaps to product with a business case; manage merchant expectations on timeline

### Who Pays

- **Standard roadmap enhancements** — funded by Worldpay product investment; no direct charge to merchants; recovered through transaction fees over time
- **Scheme mandate changes** — Worldpay bears platform cost; merchants/ISVs bear their own integration update cost
- **Bespoke merchant-specific features** — commercially negotiated: one-time development fee, or Worldpay-funded in exchange for longer contract or volume commitment, or folded into the transaction fee rate
- **Transaction fees** — different per client; enterprise merchants negotiate based on volume; bespoke development costs can be structured into the commercial deal

### Why This Matters for the Interview

- When Ajay asks how she handles merchant feature requests or product gaps: distinguish bespoke from systemic; escalate systemic with a business case; manage expectations on timeline; flag when a request has a commercial conversation attached
- That framing shows senior CDM thinking, not just delivery management
- Her question — how does the CoE handle situations where merchant expectations push beyond what the product can deliver — directly signals this understanding
