### FLOW and DORA Metrics

**FLOW and DORA together \- *Are we delivering value fast and safely?***

* **FLOW \- how work moves**  
* **DORA \- how safely the teams deploy \- DORA measures delivery \+ reliability**

#### Issue with Traditional Metrics 

**They measured outputs, not outcomes**

| Traditional Metric | Why It Failed |
| ----- | ----- |
| Velocity | Measures effort, not value |
| Utilisation | Encourages busyness |
| % On-time / On-budget | Encourages gaming |
| Lines of code | Actively harmful |
| Sprint burndown | Too local, too tactical |
| Individual performance metrics | Destroys collaboration |

**Traditional Leadership Blindspot** 

| Traditional metrics couldn’t answer: Why does work take so long? Where are we waiting? Are releases safe? Can we scale without burning people out? | So leaders: Added more governance Added more approval Added more process Result: slower delivery |
| :---- | :---- |

| FLOW \- how work moves FLOW tells me where delivery is slowing Work movement	 Highlights bottlenecks	 Portfolio → Team ( how work moves from business demand to delivery teams) Predictability | 5 FLOW Metrics Flow Velocity Flow Time Flow Distribution Flow Efficiency Flow Load (WIP) |
| :---- | :---- |
| **FLOW metrics answer:** How fast does business demand turn into completed work? Where does work wait before teams can deliver? Are we investing in the right mix of work? This is why FLOW is leadership-facing.  | **Use this every time: Problem:** Long flow time / low deployment frequency **Insight:** Metrics showed wait states / risk concentration **Action:** Reduced WIP, automated testing, changed policies **Result:** Faster releases and better stability **Business Outcome:** Earlier value / peak-safe delivery |
| **FLOW METRIC DEFINITION** | **STAR STORIES FOR EACH FLOW METRIC** |
| **1: Flow Velocity** \-  **Amount of work completed in a time period**  throughput of value, not effort  helps with predictability of delivery  Flow Velocity is measured in the count of value items completed per time period. Not effort, story points Not hours, days Not individual productivity **Notes: How is Value measured or indicated?**  The unit depends on what your organisation defines as a value item. **Common units include:** User Stories (that meet Definition of Done) Features Epics Production-ready changes Completed service requests The critical rule: The unit must be consistent, meaningful, and value-bearing.  **Example 1: Simple** Sprint 1: 12 stories completed  Sprint 2: 15 stories completed 👉 Flow Velocity increased. No discussion about how big the stories felt.  **Example 2: More mature You define: Value item \= Production-ready feature** Then: April: 8 features released May: 12 features released 👉 Flow Velocity \= 12 features/month **How FLOW Velocity and Story Points coexist (important)** You can still estimate stories. But: Teams use story points for local planning Leaders use flow velocity for system health | **Flow Velocity Situation**: Sprint velocity was low (\~65 SP) and inconsistent. **Task:** Improve throughput without burning out the team. **Action:** Introduced DoR \- definition of ready BAs to be accountable for story clarity Joint grooming and estimation Tracking (Jira): Completed items per sprint Reduced carryover **Result:** Velocity increased to 110 SP More importantly, delivery became predictable **Value:** Leadership could see stable value delivery, not just effort.  Improving Sprint velocity improved the Flow Velocity as the team started delivering more features per PI |
| **2: Flow Time \-**  Time from work start → production **Flow time \= wait time \+ active time** wait time (queues)  Active time (coding, testing) **Delivery actions:** Reduce approval queues Shift left testing Smaller stories | **FLOW METRIC 2: Flow Time Situation:** Stories took multiple sprints to reach Done. **Task:** Reduce end-to-end delivery time. **Action:** Identified wait states (BA clarifications, testing) Shift-left testing Clear acceptance criteria upfront Reduced WIP by not starting new work until the current work had finished \- reorganising resources to peer program and complete the work  **Tracking**: Jira start → done timestamps **Result**: Flow time reduced significantly Stories completed within a single sprint **Value**: Faster time-to-market for regional features. |
| **3: Flow Efficiency  Flow efficiency \= Active time / Total Time**  **What Delivery Leads fix:** Handoffs Environment waits Release windows	 | **FLOW METRIC 3: Flow Efficiency Situation**: High rework and idle time between dev and test, dependencies unmet **Task**: Increase active vs waiting time. **Action**: Test teams embedded earlier Dev-owned unit testing Test scenarios reviewed upfront Better dependency tracking **Tracking**: Time in In Progress vs Waiting **Result**: Less rework Higher productive time per sprint **Value:** Same team delivered more customer value without adding capacity. |
| **4: Flow Load (WIP)** How much work is in progress High WIP \= slow delivery  **Delivery Lead interventions:** Enforce WIP limits Say no to starting more work Finish \> start | **FLOW METRIC 4: Flow Load (WIP) Situation**: Too many stories open, few finishing. **Task**: Reduce overload. **Action**: Enforced WIP discipline Focused on finishing over starting Tracking: Jira WIP limits Reduced concurrent items **Result**: Faster completion Less context switching **Value**: Improved predictability and morale.  |
| **5:Flow Distribution Where effort is going for each of:  Features, Defects, Risk, Tech debt Example \-** At Shell, make PI planning slides with Distribution of various workstreams to worked upon in a PI \- was exactly Flow Distribution   | **FLOW METRIC 5: Flow Distribution Situation**: Leadership couldn’t see where effort was going. **Task**: Make investment visible. **Action**: PI plans categorised work: Features Risk Tech debt **Tracking**: Confluence PI decks Jira epic tagging **Result**: Clear view of delivery mix **Value**: Leadership confidence that platform health wasn’t being sacrificed. Example \- At Shell, make PI planning slides with Distribution of various workstreams is exactly **Flow Distribution**  |
| **FLOW Fixes Visibility \- FLOW metrics:** Make queues, wait time, and overload visible Shift focus from: How fast is this team? → How fast does value reach customers? | **FLOW metrics expose:** Dependency drag Overloaded teams Portfolio imbalance (too many features, not enough risk reduction) |

| DORA \- how safely the teams deploy DORA measures delivery \+ reliability | 4 DORA Metrics Deployment Frequency Lead Time for Changes Change Failure Rate Mean Time to Restore (MTTR) |
| :---- | :---- |
| DORA tells me *whether* speeding up is safe. Production outcomes Highlights reliability Team → Service Stability **What Service means** A live, customer-facing or internal production system: e.g., Loyalty platform, Checkout, APIs, Data pipelines **DORA Fixes Fear \- DORA metrics prove:** Speed and stability are not trade-offs High performers deploy: More frequently With lower failure rates And faster recovery **This dismantled a long-held myth:** *We must slow down to be safe*.That insight alone changed how executives think. | **DORA focuses on:** What happens after teams finish work How safely it runs in production What DORA measures in this space **DORA metrics answer:** How often do teams release to production? How long does it take to get a change live? How often does it cause issues? How quickly can we recover? This is operational performance, not delivery throughput. |
| DORA METRIC DEFINITION  | STAR STORIES FOR EACH DORA METRIC  |
| **1: Deployment Frequency** It is a misconception that more deployments means risky execution  More deployments \= smaller safer changes deployed  **Delivery Lead role:** Enable trunk-based dev Reduce release friction **Notes: Trunk-based development** means teams integrate small changes into a shared main branch frequently, instead of working on long-lived feature branches. **Long-lived branches cause:** Late integration failures Big, risky merges Delayed releases Release days instead of normal days **Trunk-based development fixes this by:** Integrating early and often Keeping changes small Making every change releasable **Significance of this metric for stakeholders** \- Now it is of not much significance to say to the stakeholder that we increased our deployments from once a quarter to once a month  Stakeholders care more about  Speed to value,  Risk to customers and  Confidence during peak periods  You frame this as \- Instead of bundling lots of changes into a few risky releases, we now release smaller changes more frequently. This reduces release risk, allows us to respond faster to market needs, and gives us more confidence during peak trading. **How frequent deployments  reduce risks?** Smaller changes Easier rollback Lower customer impact  **Increases commercial agility**  When Marketing requests a regional change, we no longer wait for a big batch release,  it can go out independently. This ties deployment frequency to: Commercial agility Regional responsiveness Competitive advantage **Deployment frequency helps stakeholders decide:** Can we commit to this date? Can we safely release ahead of peak? Can we decouple market releases? Do we need more automation investment? It becomes a confidence metric.  | **DORA METRIC 1: Deployment Frequency Situation**: Releases were infrequent and risky. **Task**: Enable safer, more frequent releases. **Action**: Introduced DevOps Release Manager Reduced branching Config-driven market logic **Tracking**: Release counts per PI **Result**: More frequent deployments **Value**: Faster value delivery to priority markets. |
| **2:Lead Time for Changes Code Commit → Production What slows it down:** Manual approvals Environment contention Long-lived branches **Leadership fix:** Policy \+ process, not work harder | **DORA METRIC 2: Lead Time for Changes** **Situation**: Environment contention delayed releases. **Task**: Reduce commit-to-prod time. **Action**: Highlighted environment bottlenecks Improved integration visibility **Tracking**: Code ready → deployed timestamps **Result**: Reduced end-to-end delays **Value**: Markets no longer blocked by others. |
| **3:Change Failure Rate % of deployments causing incidents High performers deploy more often with lower failure rates Delivery Lead actions:** Canary releases Feature flags Better rollback, not fewer releases | **DORA METRIC 3: Change Failure Rate Situation**: Some deployments caused production issues. **Task**: Improve release quality. **Action**: Better test coverage Performance testing Early integration checks **Tracking**: Incidents linked to releases **Result**: Fewer release-related incidents **Value**: Increased trust in frequent delivery |
| **4: Mean Time to Restore (MTTR) How fast service is restored after failure** Resilience is about recovery speed, not zero incidents. | **DORA METRIC 4: MTTR Situation**: Production issues took time to diagnose. **Task**: Restore service faster. **Action**: Better DevOps monitoring Clear rollback strategies **Tracking**: Incident start → resolution time **Result**: Faster recovery **Value**: Reduced customer and revenue impact. |

**Now practical example of FLOW / DORA**

**Prompt:** Okay at Shell I had the following scenarios. 

1. We were measuring velocity in the traditional Agile sense, \- the velocity was quite low about 65 SP and that too never completely done within a sprint.  This was resolved by the BA being accountable to own the story, its whys and wherefores, providing clear acceptance criteria, adding the YAML and other details in,  being crystal clear about the story, not vague requirements which nobody would understand and keep scratching their heads together.    
2. Stories were not completed within each sprint, they would drag on across 2-3 sprints, with lots of discussions with the BAs \- this also ate up a lot of BA and Dev time. A DoR was created so the requirements were actually ready for dev to start. Grooming sessions were put in place where the teams would discuss the solution approach for each story and estimate the size together. This clarified the team's understanding.   
3. Another issue was handoff to the test team \- they were asked to join the Sprint kick off and grooming sessions so they understand what is coming up. They had to document their test scenarios and get them reviewed. The Dev teams were asked to complete proper unit testing, and provide sample test data for the test teams to use. Steps 1,2 and 3 improved the Sprint velocity from 65 to 110\.    
4. For every PI, as a Delivery Manager, I prepared a PI plan for my team plotting  decks that would fit the explanation for a Flow distribution although we weren't using the FLOW/DORA in the program.    
5. I brought in a DevOps Release Manager who would manage more frequent releases. The team also started working on fewer branches although it wasn't completely avoidable. They achieved this through code with market and request variables to identify what part of the logic to execute as the platform was supporting multiple markets with each market having their own contextual logic. Devops helped to highlight integration failure early on   
6. There was more automation testing introduced to test on performance requirements.   
7. Earlier there were issues with an environment being blocked for testing release for one market which blocked the code for other markets to be released quicker \- this led to delays in the end to end deployment speed. 8\. Some deployments did end up causing issues in the live environments \- I think this is a case for Change Failure Rate metric in DORA.

 Now using these details:

1. **First** prepare a scenario of what was happening with Agile metrics and the challenges of visibility that the senior leadership were facing.   
2. **Second**,  detail how and why I introduced FLOW / DORA metrics? How I used FLOW / DORA instead of Agile metrics. How did I do this with minimal disruption to the team? Explain ways of working the team had to change, if any?  What changes did I have to make within Jira and Confluence to start getting the metrics in the first place? What changes were needed, if any, in the user story attributes \- did the user story still estimate the effort? Then what changed to identify and measure value delivered? Where was this change done, at the program level?     
3. **Third**, for each of the 5 FLOW and 4 DORA metrics, take the scenarios described from above and extend where needed.  Create a STAR story for each FLOW and DORA metric. Explain the problem area, explain how I tracked this using Jira and Confluence and what I did to resolved this with Jira. Include in each case how this  helped me to showcase what value we were delivering and how fast, and how safely. 

**PART 1, What was happening with traditional Agile metrics and the visibility problem**

**Context \- At Shell Loyalty, delivery was organised using Scrum and SAFe, with senior leadership primarily looking at:**

* Sprint Velocity (Story Points)  
* Sprint commitments vs completion  
* PI objectives

**What the metrics were showing**

* Velocity was \~65 SP, fluctuating  
* Stories regularly spilled across 2–3 sprints  
* Sprints rarely completed as planned

**Why leadership lacked visibility \- From a leadership perspective:**

* Low velocity looked like poor team performance  
* Spillover looked like execution issues  
* Delays were attributed to estimation problems

**But velocity couldn’t explain why:**

* Work was getting stuck  
* Handoffs caused delays  
* Releases were slow and risky  
* Some markets blocked others

**The real problems (which Agile metrics hid)**

| Hidden Issue | Why Velocity Didn’t Show It |
| ----- | ----- |
| Vague requirements | Velocity only measures effort, not readiness |
| BA–Dev rework loops | Rework counted as progress |
| Testing bottlenecks | Testing is invisible in sprint metrics |
| Environment contention | Not captured in sprint data |
| Risky releases | Velocity ignores production impact |

**Net result:** Leadership saw symptoms, not causes. Teams were busy, but value flow was poor and releases were fragile. This is the classic scenario that led me toward FLOW/DORA thinking.

**PART 2, How and why I introduced FLOW / DORA thinking (without disruption)**

*Important: In interviews, frame this as evolution, not process change.*

| Why I moved away from Agile-only metrics \- I realised that: Velocity was team-local Leadership needed end-to-end visibility I needed to answer: How fast does value reach production? Where is work waiting? Are we safe to release more often? This aligns perfectly with: FLOW → visibility of work movement DORA → safety and reliability of releases | How I introduced FLOW/DORA with minimal disruption I did not: Remove story points Change Scrum cadence Introduce new tools Instead, I: Reframed conversations Reused existing Jira data Changed behaviours, not ceremonies This is very senior delivery leadership. |
| :---- | :---- |

**Ways of working that changed (lightweight, practical)**

| 1\. Definition of Ready (DoR) Why: Reduce Flow Time and rework Change: Stories could not start unless: Clear acceptance criteria Business context (why) YAML/config details where applicable Impact: Reduced rework loops Higher Flow Efficiency | 2\. Grooming as solution alignment Why: Reduce wait states mid-sprint Change: Joint BA–Dev–Test grooming Shared estimation Early technical discussion Impact: Fewer stories spanning sprints Improved Flow Velocity  |
| :---- | :---- |
| **3\. Shift-left testing Why**: Improve Change Failure Rate and MTTR **Change**: Test team joined sprint kickoff Test scenarios reviewed early Devs owned unit testing and test data **Impact**: Fewer late surprises Faster recovery when issues occurred  | **4\. Release and branching discipline Why**: Improve Deployment Frequency safely **Change**: Introduced DevOps Release Manager Reduced long-lived branches Used config-based logic for markets **Impact**: More frequent releases Fewer integration failures  |
| **5\. Jira & Confluence changes (this is key) Jira**, I didn’t change the estimation, I added visibility. **Key changes:** Enforced DoR via checklist or custom field Consistent use of: Statuses (Ready → In Dev → In Test → Ready for Release → Done) Linked stories → epics → features (value stream) Captured: Start date Done date Reduced In Progress sprawl This enabled: Flow Time Flow Efficiency WIP visibility **Confluence, what changed** PI-level delivery views Flow distribution decks (features vs risk vs defects) Release retrospectives tied to incidents Leadership-friendly narrative, not sprint charts | **Did stories still estimate effort? Yes**, story points remained. **What changed:** Velocity stopped being the primary success measure Leadership focus shifted to: Time to value Release safety Predictability **Where was this done?** Team level: Jira hygiene, DoR, testing practices Program level: PI planning, release governance, flow distribution Leadership level: Reporting moved from SP delivered to value delivered safely |

**FINAL INTERVIEW-READY POSITIONING STATEMENT**

**To summarise the whole journey:**  At Shell, velocity told us teams were busy but not why value was slow or releases were risky. By shifting focus to FLOW and DORA principles, without disrupting Agile ways of working, we gained visibility into bottlenecks, reduced wait states, improved release safety, and increased throughput. The result was faster, safer delivery aligned to business outcomes rather than sprint mechanics.

#### **Trunk-based Dev** 

Trunk-based development means teams integrate small changes into a shared main branch frequently, instead of working on long-lived feature branches.  

**Long-lived branches cause:**

* Late integration failures  
* Big, risky merges  
* Delayed releases  
* “Release days” instead of “normal days”

**Trunk-based development fixes this by:**

* Integrating early and often  
* Keeping changes small  
* Making every change releasable

👉 This directly increases deployment frequency.

**What *enabling* trunk-based development means for a Delivery Lead**

* You do not rewrite code or pipelines.  
* You do remove organisational and process barriers.  
* Think in four enablement levers.

**1\. Make small changes safe (critical)**  
Teams won’t commit frequently if changes are risky. You enable this by:

* Encouraging feature flags / config-driven behaviour  
* Decoupling deployment from release  
* Supporting market-specific logic via configuration (which you did)

🔹 Shell example: Using request variables and config to route market logic instead of branching.

**2\. Reduce the cost of integration**  
Integration must be:

* Fast  
* Automated  
* Visible

**You enable this by:**

* CI pipelines that run automatically on merge  
* Fast feedback on failures  
* Making broken builds a team priority

**🔹 Shell example:  DevOps surfaced integration failures early instead of at release time.**

**3\. Remove organisational blockers**  
Common blockers you tackled:

* Shared environments blocking markets  
* Test teams engaged too late  
* Manual approvals

You enabled trunk-based dev by:

* Highlighting environment contention  
* Reducing handoff delays  
* Aligning teams around shared release readiness

**4\. Change release mindset**  
This is the most senior part. You helped teams move from: We release when everything is ready  
To: We release continuously, but control what’s visible  
That mindset shift is delivery leadership, not engineering

#### My issues with Flow-Time metric 

* *So I have an epic and a number of front-end, back-end, App and data platform stories related to that epic. Now I can track the start date of this epic and end-date. How do I track Flow time? \- at Epic level or user story level? Or do I break down epics in a different way for multi-component landscape, which I think is always the case \- it cannot be very granular as it won't make sense to the stakeholders then \- Like it would make no sense to calculate and present Flow time for adding a banner on App, having some back end and data platform work. Let's say I track Flow time at Feature level, the whole feature may take months to complete all things required, is that relevant? If I am working in 5 features in parallel in 3 months, I will have a metric at the end of 3 months saying , my Avg Flow time is 3 months? \- how is that of much use?*  
* Tracking flow time at the wrong level makes the metric meaningless \- **Flow Time should be measured at the smallest unit of work that delivers stakeholder-meaningful value and can flow independently.**  
* Considering Project \> Epic \> feature \> User Story 

| ❌Epic-level flow time: Spans multiple components Involves dependencies Often lasts months So: It hides bottlenecks It flattens insight It tells you nothing actionable If you measure 3-month epics: You learn nothing about why it took 3 months	 You can’t improve flow | ❌Story-Level Flow Time Is Also Often Wrong: Too much noise Metrics stakeholders can’t interpret Local optimisation So: It makes no sense to discuss flow time for a user story with senior stakeholders.  | ✅The Correct Level: Feature / Slice of Business Value A customer- or business-visible capability that can be released independently This is often called: Feature Minimum Marketable Feature (MMF) Value Slice Not the epic Not individual component stories.				 |
| :---- | :---- | :---- |
| **✅ Feature: Display personalised offer banner in app** That feature: Has backend, app, and data work But flows as one value unit What happens to component stories? They still exist. But: They roll up into the feature Flow time is measured across the feature Stories support flow, not define it	 |  |  |
| **If I need to reduce WIP by reducing the number of Features being worked on in parallel, how do I support multiple initiatives?**  If you start everything together in the same stage, you will overload the system  \- example you started 5 features in parallel and each took 12 weeks to finish ⇒ too much WIP Instead, Start 2 features, Finish them in \~6 weeks, Then start the next 2 \- Your average flow time drops from: 12 weeks → 6–8 weeks Go to stakeholders to say \- We’re currently starting too much work at once, which means features take 3 months to reach customers. By reducing parallel work, we can deliver value every 4–6 weeks instead. Handling multiple initiatives \- Reducing WIP does NOT mean reducing number of parallel initiatives, it only means to **Reduce unmanaged parallelism at the level where work actually blocks Parallelism is good at the portfolio level, dangerous at the team level, and fatal at the story level** |  |  |
| **Design the right Parallelism for Shell \- Multiple markets, 2 squads, \~7 initiatives in flight, Shared platform (App, backend, data)** The mistake is not the number of initiatives — it’s how they are sliced and activated. **1\. At the portfolio / program level: You absolutely can have parallelism:** Market A initiative Market B initiative Performance initiative Compliance initiative Platform health initiative FLOW is not asking you to stop this. This is where Flow Distribution lives. **Leadership decides:** What mix of work is funded Across how many markets **2\. Team-Level Parallelism (This Is Where FLOW Applies)** Each squad must not work on everything at once. Instead, you do capacity allocation, not hard limits. Squad A Capacity Allocation \- 40% Market A, 40% Market B, 20% Platform Squad B Capacity Allocation \- 50% Market C, 30% Performance, 20% Tech Debt So at Team level you are able to deliver on:  Multiple initiatives ✔ Controlled engagement ✔ Predictable flow ✔ **This avoids:** Everyone context-switching across 7 initiatives Features all starting together and finishing together (late) **3\. Feature-Level Parallelism** Each squad actively pulls only as many features as it can finish. So if: Squad A can handle 2 active features Squad B can handle 2 active features **You can still support:** 4 initiatives in parallel Across markets Without flow collapse **4\. Story-Level Parallelism (This Is What You Reduce Hard ❌) Bad pattern:** 15 stories In Progress Across App, backend, data Everyone waiting on everyone |  |  |

#### **Flow Time measurement \- Tracking Start time?** 

Flow Time starts when Feature moves into In Progress / Committed / Building  
Everything before that is Discovery / Intake — tracked separately if you want, but not FLOW Time.

* **So, Not when:**  
  * PO drafts a feature  
  * BA refines it over weeks  
  * Grooming discussions happen intermittently  
* ✅ **It starts when:**  
  * The Feature is pulled into delivery  
  * The Feature is:  
  * Prioritised  
  * Meets Definition of Ready (at Feature level)  
  * Actively consuming team capacity  
* Flow time \= Wait time \+ Active time \- **how to capture Blocked time**?   
  * Your Feature workflow should include:  
    * Ready  
    * In Progress  
    * Blocked / Waiting  
    * Done  
  * Required:  
    * Start date auto-set on In Progress  
    * End date auto-set on Done  
  * **Add one required field when Blocked:**  
    * Blocker Type (dropdown):  
      * Another component  
      * Environment  
      * External dependency  
      * Test readiness  
      * Market constraint  
  * Blocked is not a failure — it’s data.  
  * **You can now say:**  
    * 40% of Feature Flow Time is waiting on Data dependencies  
    * Market-specific environments add 12 days on average  
    * Config-driven releases reduced blocked time by 30%  
    * That is delivery leadership, not reporting.

#### Pre-Prod vs Canary Releases vs Blue-Green deployments 

What issue are we trying to address- we are trying to improve the Change Failure Rate i.e., reduce the percentage of change deployments causing incidents. Now suggested approach is to use Canary releases but what’s the issue with Pre-Prod deployments instead? And what are Blue-Green deployments? 

| Deploying on Pre-Prod | Canary Releases  | Blue-Green Deployments  |
| :---- | :---- | :---- |
| **Isn’t Pre-Prod \+ automated testing basically doing the same as canary releases? Pre-Prod \+ Automation Is Good For Pre-Prod environments help you catch:** Functional defects Integration failures Contract mismatches Performance regressions (to a degree) Basic security issues **Automated tests in Pre-Prod typically include:** Unit tests Integration tests API contract tests Smoke tests Performance baselines This prevents bad code from ever reaching Prod. **This lowers Change Failure Rate indirectly Even the best Pre-Prod environment:** Does not have real user behaviour Does not have real traffic spikes Does not reflect real data complexity Does not include every dependency exactly as Prod **So failures still happen:** Edge cases Real customer flows Third-party latency Market-specific behaviour **That’s why:** It worked in Pre-Prod is not a DORA success story | A canary release is a deployment strategy where: A new change is released to a small, controlled subset of users, services, or environments first,  before rolling it out to everyone.  *(The name comes from coal mines: Miners used canaries as early warning systems. If the canary showed distress → danger detected early)* A canary can be: 1–5% of live users One region / one market One pod / one service instance One tenant or customer segment Internal users only The key is: **Real production traffic Real behaviour Limited blast radius** Without canaries: You deploy to 100% of users Any defect immediately affects everyone Failures are: More visible More costly Harder to diagnose This **inflates Change Failure Rate**.  | Blue–Green deployments are another core DevOps release pattern, fits perfectly within a mature, risk-aware environment A Blue–Green deployment means: You run two identical production environments side by side: Blue \= current live version Green \= new version (idle or receiving no traffic) You deploy the new code to Green, test it, and only then switch traffic from Blue to Green. No gradual rollout,  it’s a controlled switch. **How it works:** Blue is live, serving users Green is deployed with new version Smoke tests / sanity checks run on Green **When confident:** Traffic is switched (via load balancer, DNS, routing rules) Green becomes live Blue is kept around temporarily for rollback **If something goes wrong:** Switch traffic back to Blue No redeploy needed |
|  | **Mechanism 1:** R**educed Blast Radius**  Instead of: 1 bad deployment → affects millions. You get: 1 bad deployment → affects 1–5% (or one market) Even if it fails: It may not count as a major incident. Often no customer-facing outage | **How Blue–Green Impacts DORA Metrics Deployment Frequency** Enables more frequent releases Low fear of rollback **Lead Time for Changes** Faster promotion to Prod No long outage windows **Change Failure Rate** Failures are less disruptive Rollback doesn’t escalate into incidents **MTTR** Extremely low Often seconds |
|  | **Mechanism 2: Early Signal Detection** Canary deployments are paired with: Monitoring Alerts SLIs/SLOs **You watch:** Error rates Latency Conversion drop API failures Resource usage **If metrics degrade:** You halt rollout Or auto-roll back | **Blue–Green deployments allow** teams to deploy new versions into a parallel production environment and switch traffic only once confidence is high. This gives us instant rollback capability, which significantly reduces MTTR and limits the operational impact of failed changes. At Shell, this approach worked well alongside market-based feature configuration.  |
|  | **Mechanism 3: Faster, Safer Rollbacks Because:** Canary touches fewer components Code paths are isolated Rollback scope is small **Rollback becomes:** Automated Low risk Non-disruptive  **Failures don’t escalate into incidents** |  |
|  | **When Canary Is NOT Feasible (Also Important)** Some systems: Legacy monoliths Batch jobs Regulatory constraints **In those cases:** Strong Pre-Prod Blue-green deployments Feature flags Strict rollback procedures DORA does not mandate canary, it measures outcomes. |  |
| Pre-Prod environments are essential, but they validate correctness, not operational risk. Canary releases complement Pre-Prod by validating behaviour under real production conditions while limiting customer impact.  |  |  |

| Typical DevOps Flow (High-Performing Teams)  | How DevOps impacts DORA metrics |
| :---- | :---- |
| Commit CI (unit \+ integration tests) Deploy to Pre-Prod Automated regression \+ perf tests Deploy to Prod (Canary) Monitor Gradual rollout OR rollback  | Deployment Frequency Automation \+ pipelines make deployments cheap No manual gates → more frequent releases Lead Time for Changes Fewer manual approvals Faster promotion between environments  Change Failure Rate Pre-Prod catches defects Canary limits blast radius Combined → significantly lower CFR MTTR Canary failures are easier to isolate Rollbacks are faster Recovery is measured in minutes |

#### Why % projects On Time / On Budget \- not a useful metric? 

In traditional delivery models, the **“% on-time / on-budget”** metric often ***encourages gaming*** because it rewards the appearance of success rather than the actual delivery of value or learning. Teams quickly learn that missing a date or budget is punished, while the reasons *why* it happened are rarely examined.   
**As a result, behaviour shifts toward protecting the metric**: 

* estimates are padded, scope is quietly reduced, dates are renegotiated late in the cycle, risks are hidden until the last moment, and progress is reported optimistically rather than accurately.   
* This creates a false sense of control for senior leadership, because the metric says nothing about customer outcomes, delivery flow, quality, or operational risk. Instead of surfacing system constraints early, teams delay bad news to “stay green,” which ultimately increases delivery risk and reduces trust.   
* Hiding risks until the last minute helps teams “fix” the **% on-time / on-budget** metric because the metric is usually treated as a **binary outcome measured at a fixed point in time**, not as a continuous indicator of delivery health. As long as a project is reported as “on track” during status reviews, i**t remains green**, **attracts less scrutiny, and avoids escalation.** Teams therefore delay surfacing risks in the **hope that they can be resolved quietly before the reporting deadline**. Even when the risk is real, acknowledging it early would immediately turn the metric red, triggering governance friction, loss of confidence, or pressure to re-baseline — outcomes that are often perceived as worse than the risk itself.

FLOW and DORA metrics were introduced to counter this by measuring how work actually flows through the system and how safely it reaches production, making problems visible early rather than incentivising teams to conceal them.  
