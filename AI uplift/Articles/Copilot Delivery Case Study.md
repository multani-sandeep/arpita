# AI-Driven Data Separation using MS Copilot

Moving from theoretical governance to on-the-ground execution is where AI delivery gets truly interesting. A complex, high-stakes environment for me was navigating a corporate divestiture.

While working for a global organisation undergoing a massive corporate separation from its parent company, my team was faced with an interesting challenge. We needed to migrate tens of thousands of SharePoint documents and ITSM Knowledge Articles into a new, independent environment.

The mandate was strict: **Absolutely no legacy intellectual property (IP) or parent-company branding was to be migrated across.** 

Historically, this would require an army of analysts manually reviewing documents for several months—a slow, expensive, and operationally risky endeavour. With Microsoft Copilot and Copilot Studio recently approved within our tenant, there was a strong appetite to approach this carve-out in a smarter, AI-assisted way.

Here is how this AI transformation was delivered end-to-end, securely, and within six months.

---

### The Regulatory Lens: Navigating the EU AI Act
Initially this use-case was thought to be a High Risk classification which then got recalibrated to *Limited Risk*. This happened because the designed architecture ensured that Copilot would act strictly as a recommendation engine, categorising documents and suggesting redactions. It would not autonomously delete files or make final legal decisions. Also humans would retain the final approval (Human-in-the-Loop safeguard). These safeguards avoided the heavy regulatory burdens of High-Risk AI, while fulfilling the strict transparency and audit obligations required for Limited Risk systems.



---

### The Data Separation Stages

#### 1. Discovery and Alignment
The first step was about stakeholder alignment. The initiative was framed around clear objectives: reduce manual effort, accelerate clean separation, and establish an airtight audit trail. The document estate was quantified (roughly 50,000 to 100,000 documents). Executive sponsorship, a budget envelope, and an agreement to initiate a Data Protection Impact Assessment (DPIA) were secured. In regulated industries, governance dictates the pace of technology.

#### 2. Governance and Architecture
The core question from Legal was: *Is it safe to let Copilot process legacy data?* 
Working with InfoSec, it was validated that Custom Copilot Agents operate strictly within the Microsoft 365 tenant boundary. No customer data would be used to train foundational LLMs, and there would be no cross-tenant exposure. The workflow was designed such that a Custom Copilot Agent (built via Copilot Studio and orchestrated via Power Automate) would scan the repository and sort documents into four distinct buckets:
1. **Direct Transfer:** Clean files ready to migrate.
2. **Branding Updates:** Files needing automated find-and-replace for legacy logos and names.
3. **Content Adaptation:** Files requiring manual rewriting.
4. **Manager Review:** Ambiguous files routed to a dedicated review pool.

#### 3. Technology Configuration and PoC
Once the budget for Copilot licenses (for ~50 human reviewers) and partner support was approved, it was possible to deliberately start small. During the Proof of Concept (PoC) phase, about 5,000 documents across 5 SharePoint sites were targeted. The Custom Copilot Agent used Natural Language Processing to detect legacy branding, legal entities, and contractual references. The team documented, tested and tweaked the prompt engineering. Human reviewers validated the outputs, and Legal sampled the flagged documents. The success criteria were met: a 40% reduction in manual effort with less than a 5% critical misclassification rate.

#### 4. Incremental Scaling and Launch
Following pilot approval, the scope was expanded to enable iterative waves, with 20,000 to 30,000 documents getting processed at a time. Every action was captured in an audit dashboard: the user, the timestamp, the AI Agent's suggestion, and the human’s final decision. This traceability was paramount to ensure that no IP had leaked. During the launch cutover, 100% migration was achieved with zero post-cutover legacy content breaches.

#### 5. Post-Go-Live and Continuous Governance
The job didn’t end at cutover. During the hypercare period, AI retrospectives were conducted to tune the classification rulesets for future internal migrations.  Continuous monitoring was maintained to ensure that the document taxonomy remained clean and that users weren’t bypassing the newly established AI governance checks.

By applying structured delivery governance, proactive risk classification, and strict human-in-the-loop validation, a massive, compliance-heavy divestiture headache was turned into a scalable, repeatable AI success story.

---
**Tags/Hashtags:**
#AIDelivery #MicrosoftCopilot #AIGovernance #EUAIAct #EnterpriseAI #DataSeparation #ProjectManagement #ChangeManagement #AIIntegration #ResponsibleAI #RiskManagement


---
**What I really need to know :**
As an AI Delivery Manager, no, you are not expected to know the nitty-gritty configuration, the code, or the exact menu clicks. An architect knows that your job is to deliver the project, not to build the technical solution.

However, an architect—or a technical interviewer—will expect you to understand the "Architecture Blueprint" and the constraints of what you are delivering. You need to know enough to defend the timeline, the budget, and the risk.

If you are asked about the technical implementation, you only need to know these four high-level components:

1. The Right Tool for the Job (The "What")
What you say: "We didn't just type prompts into the standard Copilot chat window. We worked with the engineering team to build a Custom Agent using Copilot Studio."
Why it matters: It shows you understand that enterprise automation requires bespoke builds, not off-the-shelf chat bots.
2. The Orchestration (The "How it Ran")
What you say: "To process 50,000 documents, we orchestrated the agent using Power Automate. It was set up to trigger sequentially across the SharePoint libraries."
Why it matters: It shows you understand how AI is actually triggered in the real world (using automation workflows).
3. The Data Boundary (The "Security")
What you say: "A major requirement for Legal and InfoSec was that our IP wasn't exposed. We verified with the architects that the Custom Agent operated entirely within our Microsoft 365 tenant boundary, and our data was not used to train Microsoft's foundational models."
Why it matters: This is the #1 question Security will ask a Delivery Manager. Knowing this answer proves you can govern AI securely.
4. The Human-in-the-Loop Workflow (The "Governance")
What you say: "The AI did not have write-access to delete or migrate files on its own. It only generated metadata tags (e.g., categorising into the 4 buckets). Those tags populated a dashboard where our 50 human reviewers gave the final 'Approve/Reject'."
Why it matters: It proves you navigated the EU AI Act / Risk controls by ensuring AI didn't make autonomous, destructive decisions.
**Summary**
If an interviewer drills deeper and asks, "Exactly what connectors did you use in Power Automate?" or "What was the exact system prompt you used?"

Your perfect Delivery Manager answer is: "My Lead Engineer and the Solution Architect handled the exact connector configurations and prompt tuning. My primary focus as the Delivery Manager was ensuring that the architectural design met InfoSec's tenant-boundary requirements, securing the budget for the Copilot Studio licenses, and designing the human-in-the-loop review process so Legal would sign off on the rollout."

That answer instantly commands respect. It shows you know your technical boundaries and are 100% focused on delivery, governance, and business outcomes.