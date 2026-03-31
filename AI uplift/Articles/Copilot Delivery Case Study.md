# AI-Driven Data Separation using MS Copilot

Moving from theoretical governance to on-the-ground execution is where AI delivery gets truly interesting. A complex, high-stakes environment for me was navigating a corporate divestiture.

While working for a global organisation undergoing a massive corporate separation from its parent company, my team was faced with an interesting challenge. We needed to migrate tens of thousands of SharePoint documents and ITSM Knowledge Articles into a new, independent environment.

The mandate was strict: **Absolutely no legacy intellectual property (IP) or parent-company branding was to be migrated across.** 

Historically, this would require an army of analysts manually reviewing documents for several months—a slow, expensive, and operationally risky endeavour. With Microsoft Copilot recently approved within our tenant, there was a strong appetite to approach this carve-out in a smarter, AI-assisted way.

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
Working with InfoSec, it was validated that Copilot operates strictly within the Microsoft 365 tenant boundary. No customer data would be used to train foundational LLMs, and there would be no cross-tenant exposure. The workflow was designed such that Copilot would sort documents into four distinct buckets:
1. **Direct Transfer:** Clean files ready to migrate.
2. **Branding Updates:** Files needing automated find-and-replace for legacy logos and names.
3. **Content Adaptation:** Files requiring manual rewriting.
4. **Manager Review:** Ambiguous files routed to a dedicated review pool.

#### 3. Technology Configuration and PoC
Once the budget for Copilot licenses (for ~50 human reviewers) and partner support was approved, it was possible to deliberately start small. During the Proof of Concept (PoC) phase, about 5,000 documents across 5 SharePoint sites were targeted. Copilot used Natural Language Processing to detect legacy branding, legal entities, and contractual references. The team documented and tested the false-positive rates and tweaked the prompt engineering. Human reviewers validated the outputs, and Legal sampled the flagged documents. The success criteria were met: a 40% reduction in manual effort with less than a 5% critical misclassification rate.

#### 4. Incremental Scaling and Launch
Following pilot approval, the scope was expanded to enable iterative waves, with 20,000 to 30,000 documents getting processed at a time. Every action was captured in an audit dashboard: the user, the timestamp, the AI’s suggestion, and the human’s final decision. This traceability was paramount to ensure that no IP had leaked. During the launch cutover, 100% migration was achieved with zero post-cutover legacy content breaches.

#### 5. Post-Go-Live and Continuous Governance
The job didn’t end at cutover. During the hypercare period, AI retrospectives were conducted to tune the classification rulesets for future internal migrations.  Continuous monitoring was maintained to ensure that the document taxonomy remained clean and that users weren’t bypassing the newly established AI governance checks.

By applying structured delivery governance, proactive risk classification, and strict human-in-the-loop validation, a massive, compliance-heavy divestiture headache was turned into a scalable, repeatable AI success story.

---
**Tags/Hashtags:**
#AIDelivery #MicrosoftCopilot #AIGovernance #EUAIAct #EnterpriseAI #DataSeparation #ProjectManagement #ChangeManagement #AIIntegration #ResponsibleAI #RiskManagement