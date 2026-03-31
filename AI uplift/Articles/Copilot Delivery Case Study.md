# Delivering Microsoft Copilot: A Real-World Case Study in AI-Driven Data Separation

Moving from theoretical governance to on-the-ground execution is where AI delivery gets truly interesting. One of the most complex, high-stakes environments for any Delivery Manager is navigating a corporate divestiture. 

While working for a global financial organisation undergoing a massive corporate separation from its former parent company, my team was faced with a daunting challenge. We needed to migrate tens of thousands of SharePoint documents and ITSM Knowledge Articles into a new, independent environment. 

The mandate was strict: **Absolutely no legacy intellectual property (IP) or parent-company branding could be migrated across.** 

Historically, this would require an army of analysts manually reviewing documents for 9 to 12 months—a slow, expensive, and operationally risky endeavour. With Microsoft Copilot recently approved within our tenant, there was a strong appetite to approach this carve-out in a smarter, AI-assisted way.

Here is how we delivered this AI transformation end-to-end, securely, and within six months.

---

### The Regulatory Lens: Navigating the EU AI Act
Before deploying the technology, we had to classify the risk. Because we were handling highly sensitive, potentially regulated financial documents, the initial reaction from some stakeholders was to treat this as a "High Risk" AI deployment. 

However, by mapping the use case against the **EU Artificial Intelligence Act**, we formally classified it as a **Limited Risk** scenario. 

Why? Because we designed the architecture so that Copilot acted strictly as a *recommendation engine*, categorising documents and suggesting redactions. It did **not** autonomously delete files or make final legal decisions. Because humans retained the final approval (a "Human-in-the-Loop" safeguard), we avoided the heaviest regulatory burdens of High-Risk AI, while fulfilling the strict transparency and audit obligations required for Limited Risk systems.

---

### The 5-Stage Delivery Lifecycle

Viewing this not as an "AI reporting task" but as a structured data separation programme, I laid out a pragmatic 6-month delivery plan.

#### 1. Discovery and Alignment (Weeks 1 to 4)
The first step was entirely non-technical; it was about stakeholder alignment. I brought together the Director of Digital Workspace, InfoSec, the Data Protection Officer, Legal, and SharePoint Platform Owners.
We framed the initiative around clear objectives: reduce manual effort, accelerate clean separation, and establish an airtight audit trail. We quantified the estate (roughly 50,000 to 100,000 documents) and secured executive sponsorship, a budget envelope, and an agreement to initiate a Data Protection Impact Assessment (DPIA). In regulated industries, governance dictates the pace of technology.

#### 2. Governance and Architecture (Weeks 3 to 8)
The core question from Legal was: *Is it safe to let Copilot process legacy data?* 
Working with InfoSec, we validated that Copilot operates strictly within our Microsoft 365 tenant boundary. No customer data would be used to train foundational LLMs, and there would be no cross-tenant exposure.
We designed a workflow where Copilot would sort documents into four distinct buckets:
1. **Direct Transfer:** Clean files ready to migrate.
2. **Branding Updates:** Files needing automated find-and-replace for legacy logos and names.
3. **Content Adaptation:** Files requiring manual rewriting.
4. **Manager Review:** Ambiguous files routed to a dedicated review pool.

#### 3. Technology Configuration and PoC (Weeks 8 to 20)
Once the budget for Copilot licenses (for ~50 human reviewers) and partner support was approved, we deliberately started small. 
During the Proof of Concept (PoC) phase, we targeted 5,000 documents across 5 SharePoint sites. Copilot used Natural Language Processing to detect legacy branding, legal entities, and contractual references. We rigorously tested the false-positive rates and tweaked our prompt engineering. 
Human reviewers validated the outputs, and Legal sampled the flagged documents. The success criteria were met: a 40% reduction in manual effort with less than a 5% critical misclassification rate.

#### 4. Incremental Scaling and Launch (Months 4 to 6)
Following pilot approval, we expanded processing into iterative waves of 20,000 to 30,000 documents at a time. 
Every action was captured in an audit dashboard: the user, the timestamp, the *AI's suggestion*, and the *human's final decision*. This traceability was paramount to proving to our former parent company that no IP had leaked. 
During the launch cutover, we achieved 100% migration with zero post-cutover legacy content breaches, vastly exceeding our original AI-accuracy benchmarks.

#### 5. Post-Go-Live and Continuous Governance
The job doesn't end at cutover. During the hypercare period, we conducted AI retrospectives to tune our classification rulesets for future internal migrations. We maintained continuous monitoring to ensure that the document taxonomy remained clean and that users weren't bypassing the newly established AI governance checks.

---

### The Takeaway

Delivering enterprise AI is rarely about turning on a shiny new tool. It is about embedding that tool thoughtfully into a high-stakes business context. 

By applying structured delivery governance, proactive risk classification, and strict human-in-the-loop validation, we turned a massive, compliance-heavy divestiture headache into a scalable, repeatable AI success story. 

When you frame AI delivery through the lens of risk control and measurable business outcomes, you stop managing technology—and start driving true enterprise transformation.
