# Interview Prep - Project Delivery Manager | giffgaff | June 2026

## Admin

| Field | Detail |
|-------|--------|
| TA call | Monday 9 June 2026 - Mollie Johnson, Talent Acquisition Partner |
| Round 1 date | Friday 12 June 2026, 10:30am - 11:00am |
| Round 1 format | Zoom, 30 minutes - introductory: CV review, skills discussion, role overview |
| Round 1 interviewer | Colin Woods, Director of Technical Partnerships and Delivery (100% remote, Bristol) |
| Round 2 | 1 hour competency - Colin Woods (+TBC) |
| Round 3 | CTO Steve - culture fit |
| CV used | CV-ProjectDeliveryManager-giffgaff-May26.md |

---

## Critical Signal - Read Before Anything Else

- Colin has been rejecting candidates who ask too much about process or structure
- His primary selection criterion is ambiguity tolerance
- He views Round 1 as a two-way conversation and expects the candidate to ask substantive questions

**Do not ask about:** governance, reporting lines, decision-making process, escalation structure, ways of working frameworks

**Do ask about:** the product, the squad, the business challenge, what success looks like

See also: [Interview-giffgaff-ProjectDeliveryManager-Debrief.md](Interview-giffgaff-ProjectDeliveryManager-Debrief.md) for full TA call notes.

---

## Ideal Candidate Persona - Who Colin Is Trying to Hire

_Visualise this person before the interview. The closer Arpita can embody this, the stronger the signal._

**How they operate**

- Sits in backlog refinement alongside the PO, not just delivery ceremonies
- Blocker in standup: same day, exact person named, impacted ticket, next action - dev time never lost
- Retro produces one change the team implements immediately; not a list in Confluence
- Working ahead on ACs for the next sprint while the current one runs; squad never hits an unready ticket
- Vague brief arrives: 1:1 with the PO first, before deciding whether a squad session is even needed
- Gets across the product quickly; within the first week knows more about what is being built than the delivery history
- Ambiguity in standup: "what does a member experience differently after we ship this?"
- Open questions get a date and a named owner; the squad keeps moving on everything else
- Business pivots mid-sprint: protects the current sprint, replans the next - no escalation, no drama
- Technical unknown: proposes a one-sprint spike with a single question and a named owner
- Status update: "we shipped X, Y is blocked on Z, unblocking by [date]" - one paragraph, not a deck
- Same facts, different framing: squad gets technical detail, stakeholder gets risk and date, executive gets one sentence
- Sprint planning question to EM/TL: "what is the one thing most likely to slip and what do we need to know to prevent it?"

---

## About giffgaff

**What it is**

- Mobile phone company that owns no network infrastructure - rents capacity from O2 and sells it under the giffgaff brand; O2 runs the masts, giffgaff handles everything customer-facing (SIM, app, plans, billing, community)
- No physical stores, no call centres - lean cost base is only possible because they carry no infrastructure overhead
- Founded 2009; lean team; startup culture despite 15+ years of operation
- Owned jointly by Liberty Global (Virgin Media - fibre and cable) and Telefonica (O2)
- Member-led model: members (customers) contribute to running the business - answering questions in the community, recommending friends, creating content - in exchange for Payback (cash, airtime credit or charity donation)
- B Corp certified: independently verified to meet standards on social and environmental impact, not just profit; audited and requalified every 3 years - it is a legal and operational commitment, not a marketing badge; business decisions are weighed against impact on people and planet alongside revenue

**What giffgaff is building**

Core products today:
- Acquisition and checkout flows: the commercial engine for bringing in new members; no stores, so the digital journey is everything
- The giffgaff app: SIM activation, plan management, top-ups and account management
- Community platform: members answer each other's questions here instead of a call centre; central to keeping costs lean
- Payback system: tracks each member's contributions and calculates their reward; pays out as cash, airtime credit or charity donation
- Reconditioned phones marketplace: sells refurbished handsets online, not new; fits the B Corp sustainability angle and keeps the cost model lean

In flight:
- giffgaff Broadband: launched 2025/26 using Virgin Media O2's fibre network; first product outside mobile; new technical infrastructure, new member journey, new billing model
- Subscription bundles: the commercial destination - mobile and broadband sold as one package; changes how members are acquired, billed and retained

What this means for squads:
- giffgaff is moving from a single-product business to a multi-product connectivity provider at pace
- Squads are being asked to build across two product lines with different underlying infrastructure
- The subscription model introduces new flows, new integrations and new data requirements across the stack
- Speed matters: competitor telcos already offer bundles; giffgaff needs to move quickly before members switch

**Who the customers are**

**How it works - simple customer journey**

1. You want cheap mobile data, no contract. You go to giffgaff.com and order a free SIM
2. It arrives in the post; you activate it online in a few minutes
3. You pick a "goodybag" - a rolling monthly plan, e.g. £10 for a set amount of data, calls and texts
4. Your phone works on O2's network. Done.
5. Next month you can change the plan, pause it or leave - no penalty

giffgaff has no call centre. If something goes wrong - SIM won't activate, billing issue, network query - there is no number to call. Instead you post in the community forum and other giffgaff members answer your question, often within minutes. giffgaff saves on support costs; the members who help get rewarded through Payback.

Payback: every time you help someone in the community, refer a friend or create content for giffgaff, you earn Payback points. You can cash them out as money to your bank, free airtime credit or a charity donation. The most active helpers are effectively being paid to do the support work a call centre would normally do - giffgaff keeps costs low and passes some of that saving back to the people who make it work.

**Why the community and Payback matter for delivery:** they are not nice-to-haves - they are load-bearing parts of the cost model. Any squad touching those systems is working on infrastructure that keeps giffgaff cheap enough to exist.

**How distinctive is this?**
- Community forums exist elsewhere (Apple, Microsoft, Sky) but are supplementary - you can still call an agent; at giffgaff the community is the only channel
- Paying members cash is rarer still - most companies offer badges or recognition, not money to your bank
- Every other major UK provider (EE, O2, Vodafone, Three, Tesco Mobile) has a call centre; giffgaff is the outlier

**Does it actually work?**
- For the majority yes - simple use cases are seamless and common problems get answered fast
- Falls down on complex problems (fraud, account locked, billing dispute) - no human escalation path, no agent to call
- SIM swap fraud has been a specific criticism
- Works for digitally confident, low-maintenance users; not designed for people who want to pick up the phone
- Keeping core journeys (activation, billing, account management) frictionless is critical - when those break, there is no safety net

**What do customers do when the community can't help?**
- Submit a contact form - slow, days to respond, no SLA
- Pressure via social media - Twitter/X tends to get faster responses
- Escalate to CISAS - the independent telecoms dispute scheme; formal, binding, last resort
- Many simply leave - no contract means no friction to switching

**Why someone chooses giffgaff**
- Wants SIM-only on a rolling monthly plan - no contract, no phone bundled
- Price-sensitive; giffgaff is consistently one of the cheapest options on O2's network
- Wants flexibility - change or pause monthly, no penalty for leaving
- Happy to self-serve; no call centre or store, everything through the app or community forum
- Often burned by a big telco; hidden charges, locked contracts, poor service from EE, Vodafone or Three
- Trade-off: support comes from the community, not an agent - works for digitally confident users, puts off anyone who wants to pick up the phone
- Customers are called members; they contribute to the business (community answers, referrals, content) in exchange for Payback - they are invested in giffgaff doing well, not just using it
- Community reacts immediately when something ships - feedback is faster and more unfiltered than any normal customer base

**Mobile SIMs and plans**
- 18-35, budget-conscious, digitally native
- No-contract preference; want flexibility and transparent pricing
- Students and early-career; often burned by big telco hidden charges

**Community platform**
- Long-standing, active members; answer questions, create content, advocate for the brand
- Disproportionately influential; keep support costs low
- Shape the experience for thousands of other members

**Payback**
- Any contributing member: community answers, referrals, content
- Most engaged and brand-loyal segment
- Motivated by a mix of reward and genuine affinity with the model

**Acquisition and checkout flows**
- First-time members; no store or agent to guide them
- Digital journey is the entire first impression
- High drop-off risk if the flow is confusing or slow

**giffgaff Broadband**
- Existing mobile members being upsold connectivity
- Renters and homeowners wanting simple, affordable broadband without a long contract
- Same demographic as mobile but slightly older

**Subscription bundles**
- Households wanting one bill, one provider for mobile and broadband
- Competing with Sky, Virgin and BT for this customer
- Motivated by simplicity and cost savings

**Their language - use these phrases naturally**

| Their word | What it means | How to use it |
|-----------|--------------|---------------|
| "Up to good" | Their mission statement - doing mobile and business differently, as a force for good | "What draws me to giffgaff is that it's genuinely up to good - the B Corp commitment isn't marketing, it's how the business is structured" |
| "The gaff" | What they call their Uxbridge office | "I'm comfortable coming into the gaff regularly" - shows you have read their materials |
| "Good folks" | How they refer to the team | Awareness of tone; informal and values-led, not corporate |
| "Mutual good" | Core value - good for members, good for the business, good for the world | Reference when talking about why the member model is distinctive |
| "Force for good" | B Corp framing - business as a vehicle for positive impact | Shows you understand the B Corp commitment is operational, not just a badge |
| "Find your happy place" | Their employer brand for the team experience | Signals informal, human culture - not hierarchy and process |

**Culture**

- Mission: "up to good" - calling out what is bad in the industry and finding a better way
- Core focuses: flexibility, value and mutual good - all three equally weighted
- B Corp certification is a source of genuine pride; a commitment, not an accreditation
- Fast-paced; fail-fast; comfortable pivoting quickly
- Not process-heavy or governance-heavy
- Lean organisation; empowered teams; low bureaucracy
- Remote-first; Uxbridge HQ attendance 4-8 times/month
- Startup energy with the stability of a Virgin Media O2-backed business
- Informal and conversational tone throughout; wordplay and warmth are deliberate
- Diversity, equity and inclusion formally embedded alongside the values

---

## Role Shape - Confirmed

| Signal | Meaning |
|--------|---------|
| DM + PO + Engineering = one coherent unit (trinity model) | Not a governance layer; an embedded delivery partner |
| Previously tried squads across multiple initiatives - did not work | Squad needs a DM who focuses deep, not broad |
| Not process-heavy or governance-heavy | Do not use words like governance, RAID, steering committee in this round |
| Agile coaching but not changing current processes | Enable and improve; do not restructure or impose |
| Another hire from Costa background | Arpita's Costa experience is directly relevant and validated by the hiring pattern |

**Lead stories for Round 1**

- **Worldpay TSA Exit** - primary anchor for ambiguity; new org, no inherited process, no formed team, hard deadline
- **Shell (DoR and DoD approach)** - primary anchor for enabling a team without imposing; team-agreed not mandated
- **Shell GO+** - end-to-end delivery at scale, multi-team, outcome-focused

---

## Opening Questions

### Tell Me About Yourself

_30-minute intro round: keep this tight, 60-90 seconds maximum. Signal product delivery mindset and comfort with ambiguity immediately. Do not recite CV._

- 15 years across digital, data and technology delivery
- Delivered end to end: from requirements and backlog shaping through to go-live and BAU handover
- Embedded alongside product and engineering - not sitting above the team, working as part of it
- Comfortable operating without a perfect brief - strongest environments have been ones where I had to figure out the shape of the work as I went
- More recently using AI tooling to make delivery proactive rather than reactive
- giffgaff's squad model and the pace of what you are building is exactly where I want to take that

**Key numbers to anchor if asked:** 17 brands - 3% checkout conversion increase - 10M+ users - 4 markets - 10% under budget - 3x team velocity

---

### What Is Your Bread and Butter?

_Colin may ask this or a version of it: "what do you enjoy most?", "what does good delivery look like to you?", "where do you add the most value?" Same answer._

- Being inside the problem, not above it - in the room when the business question is still being shaped, not handed a brief after the decisions have been made
- End-to-end accountability: from the first conversation about what the squad is trying to achieve through to go-live and measuring whether it actually worked
- Outcome over output, not milestone tracking: hitting the date means nothing if the squad shipped the wrong thing or the go-live broke something; the job is done when the member experience is measurably better
- Knowing what must not fail - every piece of work has one thing that, if it breaks, nothing else matters; finding that thing early and protecting it is where most of the value is
- Cutover and go-live planning: the moment where all the delivery work either holds together or falls apart; keeping business continuity in mind when everyone else is focused on shipping

---

### What Is Your Delivery Style? / How Do You Work?

_Variations: "how would you describe how you operate?", "what does your day-to-day look like as a DM?", "how do you approach a new squad?"_

- Embedded alongside the PO and EM/TL as one unit - not a layer above the squad, working as part of it
- New piece of work: quick 1:1 with the PO first to understand the priority and what is already known before committing squad time
- While the sprint runs: working ahead on ACs for the next sprint's backlog so devs never pick up a ticket that is not ready
- Blocker in standup: same day, nail down the exact person to resolve it, the impacted ticket and the next action - dev time is never lost waiting for someone to figure out who owns the problem
- Outcome not milestone: delivery is not done when the feature ships; it is done when the outcome is measurably achieved
- Every piece of work has one thing that must not fail; find it early and protect it - everything else is secondary to that
- Retro: one change the team implements immediately, not a list that sits in Confluence
- With the EM/TL on technical risk: "what is the thing most likely to slip the timeline and what do we need to know to prevent that?" - not telling them how to build it

---

### Why giffgaff - Why This Role

_Mollie explicitly flagged: prepare an authentic answer. Generic answers will not land with Colin._

- The squad model - DM, PO and engineering as one unit - keeps decisions inside the room and momentum never lost to a chain of approvals
- The fail-fast culture means moving inside ambiguity rather than waiting for the brief to be complete; that changes how a squad operates day to day
- The broadband and subscription pivot is a genuinely interesting delivery challenge; moving from single-product to multi-product is exactly where delivery confidence matters most
- The member model creates a feedback loop that is immediate and unfiltered - community reaction after a release is faster and more honest than any internal dashboard
- "Up to good" is embedded in how the business is structured, not a communications line; social impact built into the model, not layered on top

---

### What Do You Expect This Role to Be - What It Is and What It Isn't

_Use if asked. Reflects understanding of the giffgaff model without sounding like you read a job description._

**What it is:**
- Embedded delivery partner alongside PO and engineering - one unit, shared accountability
- Facilitating momentum: unblocking, surfacing dependencies, keeping the squad focused on the outcome
- Coaching the team's delivery capability - enabling improvement, not imposing a framework
- Navigating ambiguity; bringing clarity when the brief is loose, not waiting for it to arrive

**What it isn't:**
- A governance layer sitting above the team
- A process enforcer
- A project administrator tracking tasks
- Someone who needs a clear brief before they can start adding value

---

## STAR Answers

_Position every story as a collaboration with the PO and engineering team. Name the PO and EM/TL as active participants in every story - not people managed or reported to._

---

### Ambiguity

**The 5 types of ambiguity in delivery - and how to handle each**

---

**1. Unclear problem definition - the "what" is not agreed**

What it looks like:
- Squad asked to build something but the problem is still being shaped
- Requirements are vague; the PO is still discovering; the brief changes week to week

Techniques:
- Start with the outcome, not the feature: "what does a member experience that is better after this ships?"
- Run a lightweight discovery: 3-5 targeted questions to PO and stakeholders before any sprint commitment
- Use a simple known/unknown list: write down what is certain versus what is still open; makes the unknowns visible so the team cannot pretend they are not there
- Timebox the discovery: 2 days clarifying the core question before committing to a sprint is not adding process - it is protecting the sprint from rework
- Propose a spike if the unknown is technical: one sprint item, one question to answer, output is a decision - not more questions
- Unclear requirements at the start are expected - make them visible quickly so the squad learns from the first iteration, not the third

---

**2. Shifting priorities - the "what next" changes mid-flight**

What it looks like:
- Roadmap changes; a business decision pivots the squad's focus
- What was sprint 3 is now sprint 1; something else is shelved

Techniques:
- Accept the pivot as a feature, not a failure; changing direction is evidence the business is learning
- Protect current sprint commitments: a pivot affects the next sprint, not the one already in motion; finishing in-progress work is usually faster than abandoning it
- Keep a lightweight "what we are not doing" list: prevents the new priority pulling in scope from the old priority under a different name
- Communicate the pivot quickly and with context: the squad needs to know why, not just what; "the business learned X, so we are now doing Y" prevents confusion and resentment
- Document the rationale when direction changes: if it is not written down, it gets relitigated in three weeks
- Treat the pivot as expected, not exceptional - the question is not whether to change direction but how to do it without losing momentum

---

**3. Unclear ownership - no-one knows who decides**

What it looks like:
- A decision needs to be made and it is not clear who has authority
- Multiple stakeholders think they have a view; the squad waits because no-one wants to be wrong

Techniques:
- Name the decision-maker for each significant choice early: "who needs to say yes to this?" prevents weeks of drift
- Default ownership clearly: product decisions to the PO, technical decisions to the EM/TL, delivery decisions to the DM; when it falls outside all three, surface it immediately
- Make the gap visible rather than assuming someone else has it: the worst outcome is two people each assuming the other is accountable
- Resolve ownership in a stand-up, not a separate meeting: the heavier the resolution process, the longer the team waits
- If there is no answer, escalate with a recommended default: "I am going to proceed on the basis that X unless I hear otherwise by end of day" - forces a response without stopping the work
- In small lean teams ownership overlaps are common - act on a reasonable default rather than waiting for the org structure to clarify

---

**4. Technical unknowns - the "how" has not been figured out**

What it looks like:
- The squad knows what needs to be built but not how
- Multiple technical approaches exist; there is a risk the chosen approach will not work

Techniques:
- Propose a spike: a timebox (one sprint or less) with a single question - "is approach A technically viable?"; output is a decision, not a document
- Frame technical unknowns as delivery risks with a named path: "we do not know yet how this will be built; here is the plan to find out by X date"
- Rely on the EM/TL to answer the technical question; DM's job is to create the time and space to answer it, not to answer it
- Build the spike into the sprint plan as a first-class item: it is the work, not overhead
- Set a clear exit condition: "we know enough to proceed" or "we know enough to change approach" - not "we need more time"

---

**5. Unstable success criteria - no-one agrees what done looks like**

What it looks like:
- Squad is building but stakeholders have different pictures of what success means
- Definition of done shifts; at launch, the business is disappointed even though the squad delivered what was asked

Techniques:
- Agree what good looks like before any build begins: one sentence maximum - "this is successful if a member can do X and the squad can measure Y"
- Use minimum viable success as a forcing question: "what is the one thing that must be true for this to be worth shipping?" cuts through preference and gets to the outcome
- If stakeholders cannot agree, surface the disagreement early: it will not resolve itself at launch
- Accept that criteria will evolve: document the current agreed version and update it explicitly when it changes; everyone must be working to the same version at all times
- Connect delivery outcomes to member impact: "what does a member experience differently after this ships?" cuts through internal disagreement
- Success criteria are owned by the PO - DM's job is to make sure they are written down, agreed and visible before the sprint starts, not to define them

---

**The overarching principle - deliver this if asked directly**

- Ambiguity is not a problem I wait for someone else to resolve before I start
- Approach: anchor on the outcome that must not fail, make the unknowns explicit and visible early, timebox the resolution of each one and keep the squad moving
- Do not need a perfect brief to be useful - need to understand what we are trying to achieve and who needs to say yes to the decisions along the way

---

**STAR anchor: Worldpay TSA Exit** - see La Fosse prep guide for full story (covers ambiguity types 1, 3 and 5)

---

### Coaching Without Imposing

_Variations: "how would you bring structure without changing what exists?", "tell me about improving a team's delivery", "how do you enable a team without imposing a framework?"_

- Diagnose before prescribing: run a session where the team names the problems themselves before introducing any change
- The team owns the solution when they named the problem; change imposed from outside does not stick
- Introduce changes incrementally and only what the team has agreed to; not everything at once
- Measure the outcome not the activity: velocity, consistency and quality are the proof, not the framework adopted
- Enable the PO and EM/TL to lead their domains; coaching is removing the friction in the spaces between them, not restructuring how they work

**STAR anchor: Shell (same DoR/DoD approach)** - use Shell context; see Costa DoR and DoD STAR in Global prep guide for structure and detail to adapt

---

### End-to-End Delivery at Scale

_Variations: "tell me about a complex end-to-end delivery", "what does end-to-end mean to you?", "how do you manage delivery across multiple teams or vendors?"_

- Accountable from requirements and backlog shaping through to go-live and post-launch hypercare - not just the build phase
- Owns every dependency, not just the workstream directly managed: vendor release cycles, third-party integrations, shared services
- Surfaces cross-team dependencies early and builds them into the delivery plan before they become blockers
- When a dependency slips, does not wait - builds a technical case with the EM/TL and proposes an alternative path
- End-to-end means the outcome works on day one, not that the features were shipped on time

**STAR anchor: Shell GO+** - see Global prep guide line 283 for full story (4 markets, 10M+ users, 10% under forecast, Netherlands vendor decoupled)

---

## JD Must-Have Questions

_These are JD must-haves Colin may probe in Round 1 or save for Round 2. Anchors prepared here so nothing catches cold._

---

### Coaching Away from Project Thinking

_Variations: "how do you coach a team away from project thinking?", "what is the difference between a project team and a product team?", "how do you help a squad think about outcomes?"_

- Every ticket needs a member outcome before it enters the sprint - "build X" is not ready; "so that a member can do Y without needing to call support" is
- Sprint goal must be written as a member benefit - if it cannot be, the squad is building the wrong thing
- ACs written as member outcomes not system behaviours: "a member can do X" not "the system displays Y"
- Scope change mid-sprint is framed as learning: "the business found out X so we are now doing Y" - not a failure, evidence of a product mindset
- Retro includes outcome data: "we shipped it - did it work? What did the member do differently?" - squad accountable for impact, not just delivery
- When something ships and the community reacts, use it as a coaching moment - the feedback is immediate and unambiguous
- PO owns product decisions; if the PO is acting as a requirements conduit rather than a decision-maker, that is the coaching conversation to have first

**STAR anchor: Shell (same DoR/DoD approach)** - use Shell context; see Costa DoR and DoD STAR in Global prep guide for structure and detail to adapt

---

### Influence Without Authority

_Variations: "how do you get things done when you have no direct authority?", "tell me about a time you had to align people who didn't report to you", "how do you manage upwards or across?"_

- Credibility comes from making people's jobs easier - engineers and POs follow a DM who unblocks, not one who chases and sends requests
- Make the consequence visible, not the demand: "if this dependency is not resolved this sprint, here is what it costs the squad" - a fact, not pressure
- A stakeholder blocking is not being awkward; they have a risk that needs mitigating - find it, address it, and the block clears
- Use the sprint commitment as the anchor: if a dependency owner is not holding up their end, the team's shared commitment surfaces it - not the DM's authority
- Propose and get consent: "here is what I am thinking, does that work for you?" - consent creates durable agreements; telling creates compliance that evaporates

**STAR anchor: Estée Lauder - 17 brand managers** - see Global prep guide line 329 (also La Fosse prep guide line 663) for full story (influencing without authority across competing stakeholder priorities)

---

## Questions to Ask Colin

_Critical: Colin expects substantive questions. Minimum 3-4. Not about process or structure. Mix of substantive and personal - shows genuine curiosity about the role and about him._

**About the squad and the work**

1. What product area or initiative is this squad currently working on, and where are they in the delivery lifecycle?
2. giffgaff has just launched broadband and is pivoting towards a subscription model - how is that shaping what squads are being asked to build in the next 6 to 12 months?
3. Where is the squad right now in terms of what they're building - are you still figuring out the problem or are you already in delivery?
4. What would the squad be doing differently if this DM is getting it right?
5. What do you enjoy most about working here - and has anything surprised you since you joined?

---

## Likely Challenges

### Employment gap

- Role at Worldpay ended when the programme reached its key milestones and the team was reorganised as the carve-out completed
- Been applying deliberately rather than rushing; keeping delivery skills sharp by volunteering with an organisation in the same capacity

### Risk of sounding process-heavy

- The strongest risk in this interview
- Every time instinct says governance, RAID, steering committee or reporting cadence - stop
- Reframe as: making dependencies visible, surfacing blockers, keeping the team focused on the outcome

---

## Domain Knowledge - giffgaff and Telco Context

| Topic | Key Points |
|-------|-----------|
| **MVNO model** | Uses O2's mobile network; no physical infrastructure ownership; lean cost model; margins depend on efficient customer acquisition and low churn |
| **Member model** | Members contribute to running the business (community support, referrals, content) in exchange for Payback; unusually low CAC vs traditional telco |
| **Connectivity pivot** | Single-product (mobile) to multi-product (mobile + broadband); subscription bundles are the commercial destination; squads building across two product lines with different infrastructure at pace |
| **Squad delivery context** | Product-led; empowered teams make their own decisions; DM role is facilitating not directing; squad owns the outcome not just the delivery |
| **B Corp** | Certified B Corp: balances profit against people and planet; decisions have a social impact lens; community and environmental commitments are built into the business model |
| **Parent company** | Liberty Global (Virgin Media) + Telefonica (O2) joint venture as Virgin Media O2; giffgaff sits within the O2 part of that structure |

---

## CV Walk

_Colin will move through the CV chronologically. One or two sentences per role maximum. These are the keywords to anchor on - not a full answer._

**Eco Centre (Oct 2025 - Present) - Volunteer**
- Structured delivery in an unstructured environment; keeping skills sharp between roles
- Community-led initiative; no budget, no authority - just delivery

**Worldpay (Nov 2024 - Aug 2025) - Delivery Lead**
- TSA exit; Worldpay carving out from FIS; no inherited process, no formed team, hard deadline
- Business continuity was the one thing that could not fail - everything anchored on that
- ServiceNow, endpoint migration, Copilot rollout across three workstreams simultaneously
- AI tooling to accelerate delivery - 80% faster on content redaction and service documentation

**Estée Lauder (Nov 2023 - Oct 2024) - Contract**
- 17 prestige global brands; digital commerce feature delivery across NA and EMEA
- Checkout conversion up 3%; modular design so each brand did not need custom build
- Influence without authority - 17 brand managers, none reporting to me

**Shell (Apr 2022 - Oct 2023) - Contract**
- Loyalty API platform; 10M+ customers; £100M+ annual transactions
- Multi-region EMEA rollouts; staggered delivery to manage cross-market dependencies
- TPM and DM hybrid; embedded across UX, POS, MuleSoft and App teams
- GDPR-compliant data migration across regulated markets

**Costa Coffee (May 2019 - Mar 2022)**
- Azure Data Warehouse; 12+ data sources; reporting lag reduced from months to days
- PO and PM hybrid - owned the backlog and ran the delivery
- Loyalty app features alongside the data platform; concurrent streams, no cross-team delays

**Lodestone Consulting (Jul 2012 - May 2019)**
- 7 years consulting across global brands - Vodafone, GSK, Ricoh
- Vodafone: Adobe Analytics and Quad Play into eCommerce platform
- GSK: global CMS rollout, faster content publishing
- Ricoh: data platform migration, 90% adoption in three months via train-the-trainer
- Foundation in digital transformation before moving into dedicated delivery roles

---

## Pacing Note

- 30 minutes is short; Colin will move through the CV quickly
- Deliver Tell Me About Yourself in 90 seconds maximum
- Pause after each punchline; let silence work
- Content is strong; delivery speed is the risk
- From La Fosse debrief: explicit feedback was to slow down and pause so the interviewer can note responses
- Every story ends with what the team did, not what the DM controlled

---

## Round 2 - Questions to Prepare

_Competency-based, 1 hour with James. Colin flagged James will go deeper. Questions drawn from JD must-haves, Round 1 intel and the cross-functional delivery gap Colin identified._

---

### Product Thinking and Coaching Away from Project Mindset

_Colin recommended Transformed by Marty Cagan; this is the primary probe area for Round 2._

**1. What is the difference between an empowered product team and a feature team?**
- Empowered teams are given problems to solve, not features to build; they own the outcome
- Discovery and delivery happen together; the team is continuously learning and adjusting
- Feature teams are handed a roadmap; they measure completion, not impact
- PO in an empowered team makes decisions; PO in a feature team relays requirements from above
- Reference: Transformed by Marty Cagan — this is exactly the model giffgaff operates

**2. Tell me about a time you coached a team away from project thinking towards product thinking**
- Diagnose the symptom first — what behaviours show project thinking?
- Change how work is defined — outcomes not tasks, ACs as member benefits
- Introduce outcome-based sprint goals — team agrees them, not imposed
- Retros ask "did it work?" not just "did we ship?"
- Measure the shift — what changed in how the team operated

**3. How do you ensure a squad is focused on outcomes rather than outputs?**
- Sprint goals written as member benefits, not feature lists
- ACs written as "a member can do X" not "the system displays Y"
- Retro includes outcome data — "did the member experience change after we shipped?"
- Success criteria agreed before build starts; one sentence maximum
- Done is when the outcome is measurably achieved, not when the feature ships

**4. How would you work with a PO who is acting as a requirements conduit rather than a decision-maker?**
- Diagnose first — is it a confidence issue, an authority issue or an org design issue?
- Have a 1:1 conversation before any team intervention
- Create space for them to make decisions in standup — "what do you think we should do?"
- Protect their decisions upwards — don't let stakeholders bypass them
- Gradual shift; don't restructure their role overnight

**5. How do you define done in a product delivery context?**
- Not when the feature ships; when the outcome is measurably achieved
- Success criteria agreed before build starts — what does a member experience differently after this ships?
- Includes post-launch monitoring and hypercare — go-live is not the finish line
- The squad should be able to answer "did it work?" before closing the initiative

---

### Cross-Functional and External Delivery

_Colin explicitly said giffgaff squads are strong internally but struggle working with VMO2, finance, legal and marketing — this is the delivery gap this role is hired to address._

**6. Tell me about a time you delivered something that required alignment across teams outside your squad**
- Map all external dependencies early — named owner for each
- External timelines built into the delivery plan as first-class items, not assumptions
- Regular touchpoints with external teams, not just escalation when things slip
- What happened when an external team slipped and how it was resolved

**7. How do you manage dependencies on external partners or third-party vendors?**
- Named contact, agreed cadence, clear deliverables with dates — confirmed in writing
- Never assume; never accept "it should be fine" without a date
- Build contingency for vendor slippage — what is the fallback path?
- Escalate early when signals appear, not when the deadline is missed
- Treat the vendor's timeline as a delivery risk from day one

**8. Tell me about a time finance, legal or marketing became a blocker — how did you resolve it?**
- Found the real concern first — blockers usually have a risk behind them
- Did not chase or escalate immediately; understood what they needed
- Brought a proposed solution, not just the problem
- Used the shared delivery commitment to create urgency without pressure
- If unresolved: stated a default and proceeded — "proceeding on basis of X unless I hear otherwise by [date]"

**9. How do you keep internal squads moving when external dependencies slip?**
- Identified immediately what can proceed without the dependency
- Protected the current sprint; reprioritised the next sprint
- Made the dependency visible and named — not the squad's fault, but their concern to track
- Built a contingency path in parallel where possible
- Did not let the external slip become permission for the squad to slow down

---

### Influence Without Authority

**10. Tell me about a time you had to align people who did not report to you**
- Establish credibility first — make their job easier before asking for anything
- Find the shared goal both parties care about
- Make the consequence of misalignment visible as a fact, not pressure
- Gain consent, not compliance — propose and get agreement
- End with the outcome — what changed as a result

**11. How do you build credibility with engineering teams quickly?**
- Listen before suggesting — understand how they work before proposing changes
- Remove a blocker fast in the first few days — action builds more credibility than any introduction meeting
- Ask good questions: "what is the one thing most likely to slip and what do we need to prevent it?"
- Be honest about the boundary of your technical knowledge; don't pretend
- Protect their time from unnecessary meetings and status requests

**12. Tell me about a time a stakeholder was resistant — what did you do?**
- Find the resistance behind the resistance — what are they actually worried about?
- Address the concern directly rather than pushing harder or going around them
- Use data or a shared goal to reframe
- If unresolvable: surface it with a recommendation, not a standoff

---

### Ambiguity and Delivery Under Uncertainty

**13. Tell me about the most ambiguous delivery you have managed — what did you anchor on?**
- Anchor on the one thing that must not fail — business continuity, member outcome, hard deadline
- Make unknowns explicit and visible early — known/unknown list
- Timebox each unknown: named owner, date
- Keep the squad moving on what is clear; do not stop for an incomplete brief
- [Worldpay TSA exit is the primary anchor — use it here]

**14. How do you keep a squad moving when requirements are still being defined?**
- Start with what is known; build what is certain without waiting for the full picture
- Timebox the discovery of what is unknown — give it a date, not an open end
- Use spikes to answer specific technical or product questions in parallel with delivery
- Stop the squad for an unclear outcome; do not stop for an incomplete brief

**15. Tell me about a time the roadmap changed mid-sprint — how did you respond?**
- Protected the current sprint — the pivot affected the next sprint, not the one in motion
- Communicated the why to the squad quickly: "the business learned X, so we are now doing Y"
- Documented the rationale so it did not get relitigated in three weeks
- Treated the pivot as expected, not exceptional — direction changes are evidence of learning

**16. How do you handle a situation where no-one knows who owns a decision?**
- Named the decision-maker explicitly: "who needs to say yes to this?"
- Defaulted to the closest owner and proceeded with a stated assumption
- Made the gap visible rather than assuming someone else had it
- Resolved in standup, not a separate meeting; the heavier the process, the longer the wait

---

### Taking Over Mid-Flight

_Relevant if this role picks up Laura's Broadband initiative._

**17. Tell me about a time you joined a programme or initiative that was already in flight**
- Read the existing state before forming any view
- 1:1s with the PO and EM/TL before any team session
- Establish what must not fail first
- Do not change anything in week 1 — observe, understand, then act
- Protect what is working; change what is not — be clear why

**18. How do you get up to speed on a product you have not worked on before?**
- PO first — they know the why behind what is being built
- Within the first week: know more about what is being built than the delivery history
- Member/community feedback is a fast signal — what are users actually saying?
- Ask the EM/TL for the top technical risks; understand the risks, not the full architecture

**19. What is the first thing you do when taking over delivery from someone else?**
- Find the open risks and blockers — what is most likely to blow up?
- Understand what commitments have already been made and to whom
- Do not change the team's rhythm immediately — earn the right to suggest changes
- Identify the relationships that matter most and make contact within the first few days

---

### Engineering and Technical Engagement

**20. How do you engage with Engineering Managers and Tech Leads on technical risks and dependencies?**
- Opening question in sprint planning: "what is the one thing most likely to slip and what do we need to know to prevent it?"
- Frame technical unknowns as delivery risks with a named resolution path and a date
- Build technical risks into the delivery plan as first-class items, not footnotes
- The EM/TL answers the technical question; the DM creates the time and space to answer it
- Do not pretend to understand technical decisions outside your knowledge — ask the right questions instead

**21. How do you surface a technical risk you do not fully understand yourself?**
- Ask the EM/TL to translate it into delivery impact: "what does this mean for the timeline and the release?"
- Do not hide the uncertainty — "help me understand the delivery risk so I can surface it correctly"
- Escalate the risk, not the technical debate
- Propose a spike: one question, one sprint, one named owner, one decision as output

**22. Tell me about a time a technical dependency nearly derailed a delivery — what did you do?**
- Spotted early — dependency mapping or sprint planning conversation with EM/TL
- Built a contingency path in parallel
- Escalated with a recommendation, not just a problem
- Worked with EM/TL to decouple or work around the dependency
- End with the delivery outcome

---

### Communication and Stakeholder Management

**23. How do you tailor your communication for different audiences — squad, stakeholder, executive?**
- Squad: current sprint, specific blockers, named next actions and owners
- Stakeholder: risk and date — what is the issue, what is the impact, when will it be resolved
- Executive: one sentence — on track / at risk because X, resolving by Y
- Same facts, different framing; never send a deck to someone who needs a paragraph
- Format follows the audience's need, not a default weekly cadence

**24. Tell me about a time you had to deliver difficult news to a senior stakeholder**
- Lead with the fact — "we are going to miss the date because X"
- Come with a plan, not just a problem
- Be honest about recovery — do not oversell
- Give space to react before proposing next steps
- Follow up in writing

**25. How do you report on delivery health without creating unnecessary overhead?**
- One paragraph: shipped X, Y is blocked on Z, unblocking by [date]
- Outcome-focused: is the member experience on track to improve?
- Reporting cadence matched to the stakeholder's need, not a default weekly deck
- Make risks visible early — do not hide problems until they become crises
- The report should prompt a decision or action, not just acknowledge progress

---

## Notes from Round 1

_Add notes here during or after the call._

---

_Round 2 prep will be built after Round 1 outcome and any feedback from Mollie._
