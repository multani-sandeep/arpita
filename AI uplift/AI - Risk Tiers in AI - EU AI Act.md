**Understanding High-Risk AI under the EU AI Act**

## **1\. Why the EU AI Act Uses a Risk-Based Model**

The **European Union Artificial Intelligence Act** is the first major regulatory framework designed to govern artificial intelligence systems across the European Union. Instead of regulating every AI application equally, the regulation uses a **risk-based framework**, meaning that obligations increase as the potential harm of an AI system increases.

The logic behind this approach is straightforward:

* AI systems that can affect **health, safety or fundamental rights** require strict controls.  
* AI systems with **limited societal impact** require transparency.  
* Low-risk AI systems are largely left unregulated.

For delivery leaders this matters because **compliance obligations are triggered by risk classification**, not by whether the system uses machine learning, generative AI or simple automation.

In other words: A delivery team must first answer a critical governance question:

**“What risk tier does this AI system fall into?”**

Getting this classification wrong can lead to major consequences including forced system withdrawal or fines of up to **€35 million or 7 percent of global turnover**.

### **Delivery perspective**

For a Delivery Manager, risk classification becomes an **early project governance checkpoint** similar to:

* security architecture reviews  
* data protection impact assessments  
* regulatory approval processes

It should occur **before development begins**, not at deployment.

### **Example: Copilot rollout**

Imagine a company rolling out **AI assistants such as Microsoft Copilot** internally.

If Copilot is used only for:

* drafting emails  
* summarising meeting notes  
* generating internal documentation

then it likely falls into **minimal risk**

However, if the organisation integrates Copilot into systems that **evaluate employee performance or influence HR decisions**, the classification could move toward **high-risk AI** under the employment category.

The **same technology** can therefore fall into **different regulatory categories depending on how it is used**.

---

# **2\. The Four Risk Tiers in the EU AI Act**

The EU AI Act divides AI systems into **four risk tiers**, forming a regulatory pyramid.

1. Unacceptable risk  
2. High risk  
3. Limited risk  
4. Minimal risk

Each level carries different compliance obligations.

---

# **3\.  A \- Unacceptable Risk: AI That Is Completely Prohibited**

At the top of the regulatory pyramid are AI systems classified as **unacceptable risk**. These are considered incompatible with European values and are **banned outright**.

Examples include:

* social scoring systems used by governments  
* AI that manipulates behaviour without awareness  
* systems exploiting vulnerable populations  
* emotion recognition in workplaces or schools  
* untargeted scraping of facial images for biometric databases

These practices are banned because they threaten **fundamental rights and democratic norms**.

### **Delivery perspective**

For delivery teams the key takeaway is simple: These systems **cannot be deployed in the EU at all**.

Therefore governance processes should include an **early ethical and regulatory screening** step.

### **Example: loyalty platforms**

Consider a **customer loyalty platform** that analyses purchase behaviour to determine customer rewards.

This is generally acceptable.  However, if the platform begins to:

* infer sensitive attributes like religion or ethnicity from behaviour  
* apply manipulative behavioural nudges targeting vulnerable groups

**it could cross into prohibited territory.**

A Delivery Manager must therefore ensure that **data science teams understand regulatory boundaries during design**.

---

# **4\. High-Risk AI: The Core Regulatory Focus**

High-risk AI systems are **not banned**, but they are **heavily regulated**.

These are systems that could significantly affect:

* health  
* safety  
* fundamental rights  
* access to services  
* employment opportunities

Under the AI Act, these systems must undergo **strict compliance requirements before deployment and throughout their lifecycle**.

**High-risk AI falls into two main categories:**

### **Category 1: AI embedded in regulated products**

These include AI systems used within products already covered by EU safety legislation, such as:

* medical devices  
* cars and autonomous vehicles  
* aviation systems  
* industrial machinery  
* safety components in infrastructure

These systems are considered high-risk because **failure could endanger human life or physical safety**.

### **Category 2: AI used in sensitive societal domains**

The Act explicitly lists several areas where AI decisions can significantly affect people’s rights or opportunities:

* employment and HR decisions  
* education admissions or assessment  
* access to financial services such as credit  
* law enforcement  
* migration and border control  
* justice systems  
* critical infrastructure management

These domains are listed because they can **directly shape life outcomes for individuals**.

### **Delivery perspective**

High-risk classification introduces a **compliance lifecycle** including:

* conformity assessments  
* technical documentations  
* human oversight mechanisms  
* traceability logs  
* risk management processes

In practical terms, a high-risk AI project resembles a **regulated product programme**, not a typical IT deployment.

### **Example: Copilot used for HR decision support**

If a company integrates AI tools such as Copilot into a system that:

* ranks job applicants  
* recommends promotions  
* assesses employee performance

then the system falls into the **employment category of high-risk AI**.

This means the organisation must implement:

* bias testing  
* human review procedures  
* audit logging  
* documentation explaining the model’s behaviour

A Delivery Manager would therefore need to coordinate between:

* HR leadership  
* legal teams  
* data science teams  
* governance functions

to ensure the system meets regulatory obligations before release.

---

# **5\. Limited Risk AI: Transparency Requirements**

Limited risk systems are allowed but must meet **transparency obligations**.

Users must be informed when they are interacting with AI systems.

Examples include:

* chatbots  
* AI content generators  
* deepfake media  
* emotion recognition outside prohibited contexts

The purpose of these rules is to **ensure informed consent and maintain public trust**.

### **Delivery perspective**

Compliance usually involves:

* labelling AI interactions  
* informing users they are speaking to AI  
* marking AI-generated content clearly

These requirements are comparatively lightweight but still require **product design changes**.

### **Example: loyalty platform customer chatbot**

A loyalty programme might include an AI chatbot that:

* answers reward questions  
* explains offers  
* recommends products

This would likely fall into **limited risk**.

The platform would need to:

* clearly disclose the chatbot is AI  
* ensure users understand responses are automated

A Delivery Manager would need to ensure this disclosure is included in **UX design and legal approval processes**.

---

# **6\. Minimal Risk AI: Most AI Falls Here**

Most AI applications fall into the **minimal risk category**.

Examples include:

* spam filters  
* recommendation engines  
* inventory forecasting  
* AI-enabled video games

These systems face **no specific regulatory obligations beyond existing laws**.

However, organisations are encouraged to adopt **voluntary codes of conduct and responsible AI practices**.

### **Delivery perspective**

Even though minimal risk systems have no formal obligations, many organisations still implement:

* model monitoring  
* bias checks  
* governance frameworks

because the **risk classification could change if the system’s use evolves**.

### **Example: loyalty platform product recommendations**

An AI model recommending products based on purchase history typically qualifies as minimal risk.

However, if the system begins to:

* determine eligibility for financial credit  
* influence insurance decisions  
* decide access to essential services

it could move into the **high-risk category**.

This illustrates a key lesson for delivery leaders:

**AI risk classification depends on use case, not technology.**

---

# **7\. The Business Meaning of “High-Risk”**

In legal language, high-risk refers to **potential harm to safety or fundamental rights**.

In business terms, high-risk AI means:

* regulated deployment  
* mandatory governance controls  
* extensive documentation  
* continuous monitoring  
* regulatory accountability

This transforms AI development into something closer to **regulated engineering disciplines** like:

* medical devices  
* aviation systems  
* financial services infrastructure

### **Delivery implications**

For a Delivery Manager, high-risk AI introduces:

1. regulatory checkpoints in the delivery lifecycle  
2. cross-functional collaboration with legal and compliance teams  
3. longer approval cycles before deployment  
4. traceability requirements for AI decisions  
5. incident reporting obligations

This fundamentally changes **how AI programmes are delivered**.

---

# **8\. Why Risk Classification Is the First Governance Step**

The EU AI Act places responsibility for classification primarily on **AI providers and deployers themselves**.

This means organisations must determine:

* whether their system is AI under the Act  
* whether it falls within a listed high-risk category  
* whether exemptions apply

If the classification is wrong, regulators can:

* demand corrective action  
* suspend deployment  
* impose significant financial penalties.

### **Delivery insight**

A practical approach for delivery teams is to treat **AI risk classification as a mandatory early architecture review**.

This typically occurs during:

* product design  
* solution architecture planning  
* regulatory compliance assessments

### **Example: Copilot integration programme**

If a company launches an enterprise Copilot programme, a Delivery Manager should run a classification exercise across all use cases such as:

* document summarisation  
* internal knowledge search  
* coding assistance  
* HR analytics  
* recruitment automation

Some of these will be **minimal risk** and some may fall into **high-risk employment AI**.

Managing this distinction is essential to avoid regulatory breaches.

---

# **Conclusion**

The EU AI Act introduces a **risk-based regulatory framework** that classifies AI systems into four tiers ranging from prohibited to minimal risk.

The most important category for businesses is **high-risk AI**, which includes systems affecting employment, financial services, education, law enforcement and critical infrastructure.

For Delivery Managers, understanding high-risk AI is not just a legal matter but a **programme governance responsibility**. Risk classification determines the level of compliance, documentation and oversight required throughout the AI lifecycle.

Real-world AI deployments such as Copilot integrations or loyalty platforms demonstrate that the same technology can fall into different risk tiers depending on how it is used. This means delivery leaders must work closely with legal, compliance and engineering teams to ensure that AI systems are correctly classified and governed from the earliest stages of a project.

Below are **four detailed Microsoft Copilot use cases** aligned with the **four EU AI Act risk levels**. Each one is written as a realistic organisational scenario so that it can later be used when discussing AI governance or regulatory implications. 

Also **mapped to each Copilot use case to the relevant provisions of the EU AI Act** and explain *why the risk level applies legally*. This is the type of explanation a Delivery Manager can confidently use when discussing AI governance with legal teams, architects and executives.

For reference the regulation itself is the **EU Artificial Intelligence Act**.

---

# **Use Case 1 — Minimal Risk**

## **Copilot for Meeting Productivity and Knowledge Capture**

A global organisation deploys \*\*Microsoft Copilot integrated with \*\*Microsoft Teams to improve meeting productivity and knowledge sharing across distributed teams.

The organisation has thousands of internal meetings every week involving project teams, delivery managers, engineers and stakeholders. Important discussions, decisions and actions are often lost in personal notes or scattered across emails.

To address this, Copilot is introduced to automatically assist with meeting management tasks.

During each meeting Copilot performs several functions:

* records the meeting (where recording is enabled)  
* transcribes the discussion in real time  
* identifies key discussion topics  
* generates a structured meeting summary  
* extracts decisions and action items  
* distributes summaries to participants

After the meeting, Copilot automatically produces a document containing:

* a concise meeting summary  
* key discussion themes  
* a list of action items with assigned owners  
* relevant timestamps linked to the recording  
* suggested follow-up tasks

This summary is then posted into the meeting chat and optionally stored in a team workspace such as SharePoint.

Teams benefit in several ways:

* participants can focus on the discussion instead of taking notes  
* absent stakeholders can review summaries quickly  
* action items are clearly tracked  
* project knowledge becomes searchable across the organisation

The system does not make decisions about employees or customers. It simply summarises information already shared in meetings and improves collaboration efficiency.

# ---

**Now mapping this to the EU AI act \- *Use Case 1 — Meeting Notes and Summaries***

## **Risk Level: Minimal Risk**

### **Scenario**

Using \*\*Microsoft Copilot with \*\*Microsoft Teams to record meetings, generate transcripts, summarise discussions and extract action items.

### **Relevant Legal Section**

Article 6 and Annex III of the **EU Artificial Intelligence Act** define **high-risk AI systems**. Systems that do **not fall into those categories** are generally considered **minimal risk**.

### **Why This Use Case Is Minimal Risk**

The system performs **assistive productivity tasks**:

* summarising conversations  
* transcribing speech  
* extracting action items  
* organising information

It **does not**:

* make decisions about individuals  
* evaluate employees  
* influence access to services  
* determine eligibility for employment or credit  
* operate in critical infrastructure

The AI is simply **processing content created voluntarily by participants**.

Therefore the system sits outside high-risk categories listed in Annex III.

### **Delivery Governance Considerations**

Even though minimal risk systems are largely unregulated, organisations still typically implement:

* internal AI usage policies  
* data retention controls  
* meeting recording consent policies

### **Practical Delivery Insight**

The main risk here is **data governance**, not AI regulation. Teams should ensure recordings comply with existing laws such as \*\*UK GDPR and \*\*General Data Protection Regulation.

---

Below is the **delivery lifecycle governance table for Use Case 1**.

Use Case 1 \- Meeting recording, transcription and summaries using \*\*Microsoft Copilot integrated with **Microsoft Teams**.

Risk Tier \- Minimal Risk under the **EU Artificial Intelligence Act**

Although the regulatory burden is light, a Delivery Manager should still demonstrate **structured governance and traceability**.

---

## **Delivery Lifecycle Governance — Minimal Risk Use Case**

| Delivery Phase | Delivery Manager Actions to Embed Compliance | Risk Analysis Owner | Review and Sign-off Authority | Additional Governance Details |
| ----- | ----- | ----- | ----- | ----- |
| Discovery | Identify the AI component and confirm whether the system qualifies as AI under the EU AI Act. Document the intended Copilot functionality such as transcription, summarisation and action extraction. Run a preliminary AI risk classification workshop. Confirm that the system does not influence employment decisions or access to services. Document data sources such as meeting recordings and transcripts. Ensure employee awareness that meetings may be recorded and summarised. | Enterprise Architect and AI Architect | AI Governance Lead and Programme Sponsor | Stage Gate: AI Use Case Identification. Outcome: Use case classified as Minimal Risk and allowed to proceed to design. |
| Architecture and Design | Work with architects to ensure Copilot operates only as a productivity assistant. Confirm that the system does not generate behavioural analytics or performance insights about employees. Design data governance controls for recordings, transcripts and summaries. Define where summaries will be stored such as SharePoint or Teams channels. Ensure privacy notices and meeting recording notifications are included in system design. | Solution Architect and Data Protection Specialist | Data Protection Officer and Enterprise Architecture Board | Stage Gate: Responsible AI Design Review. Outcome: Architecture confirmed as productivity tool with no automated decision making. |
| Development and Configuration | Ensure Copilot configuration aligns with approved scope such as transcription, summarisation and action extraction only. Prevent configuration changes that enable behavioural monitoring or analytics. Confirm role based access to meeting recordings and transcripts. Validate that logs exist showing when Copilot generated summaries. | Technical Lead and AI Engineer | Platform Owner and Security Lead | Stage Gate: AI Capability Validation. Outcome: Configuration verified to match approved minimal risk use case. |
| Testing | Validate that Copilot outputs are summaries only and do not generate employee behaviour insights or evaluation metrics. Test consent mechanisms for meeting recording notifications. Validate correct storage and access permissions for transcripts and summaries. Ensure system logs exist to support traceability. | QA Lead and AI Testing Specialist | Data Protection Officer and Programme Steering Committee | Stage Gate: Responsible AI Testing Review. Outcome: System approved for deployment with minimal regulatory exposure. |
| Deployment | Launch Copilot meeting assistance capability within defined governance boundaries. Communicate usage guidance to employees including how summaries are generated. Ensure monitoring dashboards exist to track adoption and detect unexpected usage patterns. | Platform Operations Lead | CIO or Digital Workplace Director | Stage Gate: AI Deployment Approval. Outcome: System deployed as approved productivity capability. |
| Monitoring and Continuous Governance | Monitor system usage to ensure Copilot is not being repurposed for employee performance monitoring. Review logs and user feedback periodically. Update AI inventory records maintained by the organisation. If new features are proposed such as behavioural analytics, trigger a new AI risk classification exercise. | AI Governance Team and Platform Operations | Responsible AI Committee | Stage Gate: AI Operational Oversight Review. Outcome: Use case remains classified as Minimal Risk unless functionality changes. |

---

# **Use Case 2 — Limited Risk**

## **Copilot-Assisted Document Classification During Corporate Separation**

A multinational organisation called Company W is separating from its parent organisation Company F following a strategic divestment. As part of the separation programme, Company W must migrate thousands of operational documents stored within a shared \*\*Microsoft SharePoint repository previously managed by Company F.

These documents include:

* operational procedures  
* customer service guides  
* internal policies  
* project documentation  
* vendor contracts  
* training materials

Many documents reference Company F’s internal structures, branding and processes. Before migration, each document must be assessed to determine whether it should be retained, updated or discarded.

To accelerate the process, the organisation deploys **Microsoft Copilot** integrated with SharePoint to perform an initial classification pass across the document repository.

Copilot analyses document content and automatically categorises each file according to four possible outcomes:

1. **Direct Transfer**  
   Documents that remain valid for Company W and require no changes are flagged for direct migration.  
2. **Branding and Naming Updates**  
    Documents that reference Company F branding or terminology are flagged for automated updates. Copilot identifies phrases such as company names, logos, email domains and organisational references that need replacement with Company W equivalents.  
3. **Content Adaptation Required**  
    Some documents reference processes or systems that only exist within Company F. Copilot flags these documents and highlights sections likely requiring manual updates.  
4. **Manager Review Required**  
    Documents that appear outdated, ambiguous or potentially irrelevant are routed into a separate review pool for subject matter experts.

Once classification is complete:

* documents requiring only branding updates are automatically updated and prepared for migration  
* unchanged documents are transferred directly to Company W’s SharePoint environment  
* flagged documents are assigned to managers for deeper review

Copilot therefore **assists decision-making but does not make final decisions** about document validity. Human managers retain authority to approve or reject each document migration.

This significantly reduces the manual effort required in a large separation programme while maintaining appropriate oversight.

# **Now mapping this to the EU AI Act \- *Use Case 2 — Document Classification During Company Separation***

## **Risk Level: Limited Risk**

### **Scenario**

Using **Microsoft Copilot** integrated with \*\*Microsoft SharePoint to classify thousands of documents during a corporate separation between Company F and Company W.

The AI:

* categorises documents  
* identifies branding references  
* suggests content updates  
* routes certain documents for human review

Managers retain final approval authority.

---

### **Relevant Legal Section**

Article 52 of the **EU Artificial Intelligence Act** defines **transparency obligations for certain AI systems**, often referred to as **limited-risk AI**.

These include systems where users should be **aware they are interacting with AI assistance**.

---

### **Why This Use Case Is Limited Risk**

The AI:

* **supports decision making**  
* **does not autonomously determine outcomes**  
* **does not affect individuals’ rights**

All decisions remain subject to **human review**.

The main regulatory requirement is **transparency**:

Users must understand that:

* classification suggestions are generated by AI  
* human managers must validate outcomes

---

### **Delivery Governance Considerations**

Delivery teams should implement:

* AI-generated suggestion labelling  
* audit trail of classification decisions  
* approval workflows for document migration

---

### **Practical Delivery Insight**

This is an example of **AI augmentation rather than AI decision-making**.

From a programme management perspective, Copilot acts as a **productivity accelerator in large transformation programmes**, such as corporate separations or mergers.

Use Case 2  
 Copilot analysing and classifying documents during a corporate separation where Company W is separating from Company F. The AI reviews documents in **Microsoft SharePoint** and suggests whether documents should be migrated, updated or reviewed by managers using **Microsoft Copilot**.

Risk Tier  
 Limited Risk under the **EU Artificial Intelligence Act** because AI assists decisions but **humans retain final authority**. \- becomes more interesting because the governance introduces **human-in-the-loop controls and decision audit trails**, which Delivery Managers are often expected to implement.

# ---

Below is the **delivery lifecycle governance table for Use Case 2 \-** 

# **Delivery Lifecycle Governance — Limited Risk Use Case**

| Delivery Phase | Delivery Manager Actions to Embed Compliance | Risk Analysis Owner | Review and Sign-off Authority | Additional Governance Details |
| ----- | ----- | ----- | ----- | ----- |
| Discovery | Identify the AI capability being introduced into the document separation programme. Document the business objective which is accelerating document classification during the separation of Company W from Company F. Confirm that Copilot is only recommending document classifications and not making final legal or operational decisions. Identify the document sources in SharePoint and confirm that the AI will analyse text for company names, branding references and system dependencies. Confirm that human reviewers will validate all documents flagged as requiring review. Document the AI use case in the organisational AI inventory. | Enterprise Architect and Information Governance Architect | Programme Sponsor and AI Governance Lead | Stage Gate: AI Use Case Qualification. Outcome: Use case classified as Limited Risk because AI provides recommendations while humans retain final decision authority. |
| Architecture and Design | Design the document classification workflow. Define classification categories such as Direct Transfer, Branding Update Required, Content Review Required and Manager Review Required. Ensure Copilot outputs are clearly labelled as AI generated recommendations. Design a human review stage where subject matter experts validate flagged documents before migration. Define audit logs capturing classification suggestions and final human decisions. Confirm storage and access controls within SharePoint for migrated documents. | Solution Architect and Data Governance Lead | Enterprise Architecture Board and Legal Counsel | Stage Gate: Responsible AI Architecture Review. Outcome: Architecture approved with human-in-the-loop review and transparency controls. |
| Development and Configuration | Configure Copilot prompts and workflows to analyse document content for references to Company F and Company W. Configure automation rules that update branding only when rules are clearly defined such as company names or logos. Ensure documents requiring contextual interpretation are routed to managers instead of automatically modified. Build logging capabilities capturing which documents were analysed, which classification Copilot suggested and which final decision was taken by the reviewer. | AI Engineer and SharePoint Technical Lead | Platform Owner and Information Security Lead | Stage Gate: AI Workflow Validation. Outcome: System confirmed to operate as a recommendation engine rather than an autonomous decision maker. |
| Testing | Test classification accuracy using representative document sets. Validate that Copilot correctly identifies branding references and organisational terminology. Confirm that AI generated updates do not alter substantive legal or operational content. Test the manager review pool to ensure flagged documents are correctly routed for human review. Validate audit logging of both AI recommendations and human decisions. Confirm that users are aware that classification suggestions are generated by AI. | QA Lead and Information Governance Testing Specialist | Legal Counsel and Data Protection Officer | Stage Gate: Responsible AI Testing Approval. Outcome: System confirmed to meet transparency requirements and maintain human oversight. |
| Deployment | Deploy Copilot enabled document classification capability within the separation programme. Provide guidance to managers explaining that Copilot classifications are recommendations requiring validation. Monitor the migration process to ensure documents are only transferred after the defined review process. Ensure the separation programme maintains a record of classification decisions in case of audit or regulatory review. | Programme Operations Lead and SharePoint Platform Owner | Programme Steering Committee and CIO | Stage Gate: AI Deployment Approval. Outcome: System deployed as part of corporate separation document migration process. |
| Monitoring and Continuous Governance | Monitor classification accuracy and user feedback during the separation programme. Review logs to confirm human validation remains active and that no automated changes are made beyond approved branding updates. Maintain records of document migrations and classification decisions. If the AI system begins making autonomous document approval decisions without review, trigger a new risk classification assessment under the EU AI Act. | AI Governance Team and Information Governance Team | Responsible AI Committee and Programme Sponsor | Stage Gate: AI Operational Governance Review. Outcome: Use case remains Limited Risk as long as human oversight remains active. |

---

# **Use Case 3 — High Risk**

## **Copilot-Driven Communication Pattern Analysis for Workforce Performance Insights**

A large enterprise deploys **Microsoft Copilot** integrated with **Microsoft Teams**, email and calendar data to analyse collaboration patterns across the organisation.

The stated goal of the initiative is to improve organisational productivity and identify teams that may be struggling with workload, communication inefficiencies or employee burnout.

Using meeting transcripts, chat histories and collaboration metadata, Copilot analyses communication patterns such as:

* frequency of meetings attended by employees  
* speaking time during meetings  
* response time to messages  
* sentiment within conversations  
* collaboration patterns between teams

From this data, Copilot generates insights for managers including:

* employees who dominate discussions  
* individuals who rarely contribute during meetings  
* teams where conversations frequently show signs of conflict or negative sentiment  
* employees who appear overloaded due to meeting volume  
* individuals who may be disengaged or silent during team discussions

The system then produces dashboards ranking employees or teams across various behavioural indicators such as:

* participation levels  
* communication responsiveness  
* collaboration engagement  
* perceived sentiment trends

Managers are encouraged to use these insights to:

* identify potential leadership candidates  
* flag employees who may require coaching  
* detect possible team conflicts early  
* support workforce performance reviews

Although the intention is to improve organisational health and collaboration effectiveness, the system effectively **analyses employee behaviour and influences management decisions about performance, engagement and leadership potential**.

Because these insights could directly affect employment outcomes such as performance reviews, promotions or disciplinary action, the system enters a regulatory domain where AI decisions may significantly impact individuals.

Now mapping this to the EU AI Act \- ***Use Case 3 — Employee Behaviour Analysis***

## **Risk Level: High Risk**

### **Scenario**

Using **Microsoft Copilot** to analyse internal collaboration behaviour using data from:

* \*\*Microsoft Teams meetings  
* chat transcripts  
* email patterns  
* calendar data

The system generates behavioural insights including:

* meeting participation levels  
* communication responsiveness  
* collaboration sentiment  
* employee engagement indicators

Managers use these insights during:

* performance reviews  
* leadership identification  
* workforce management.

---

### **Relevant Legal Section**

Annex III of the **EU Artificial Intelligence Act** identifies **AI systems used in employment, worker management and access to self-employment** as **high-risk systems**.

Examples listed include systems used to:

* evaluate employee performance  
* monitor worker behaviour  
* influence promotion decisions  
* allocate tasks

---

### **Why This Use Case Is High Risk**

The system is analysing behavioural data and producing insights that may affect:

* performance evaluations  
* promotion decisions  
* disciplinary action  
* workload allocation

Even if the AI **only produces recommendations**, the fact that the system **influences employment decisions** triggers the high-risk classification.

---

### **Legal Obligations Triggered**

High-risk systems must meet strict requirements under the **EU Artificial Intelligence Act**, including:

* risk management framework  
* high-quality training data  
* technical documentation  
* human oversight mechanisms  
* accuracy and robustness testing  
* detailed event logging

---

### **Delivery Governance Considerations**

For delivery teams this introduces new programme responsibilities:

* AI compliance documentation  
* bias testing  
* fairness validation  
* monitoring and incident reporting  
* regulatory audit readiness

This effectively turns the project into a **regulated system deployment**.

---

Below is the **delivery lifecycle governance table for Use Case 3 \-** 

Use Case 3  
 Using **Microsoft Copilot** to analyse communication behaviour from **Microsoft Teams** meetings, chats and collaboration data to generate insights about employee participation, engagement and communication patterns that managers may use during workforce management or performance discussions.

Risk Tier  
 High Risk under the **EU Artificial Intelligence Act** because the system analyses worker behaviour and may influence employment decisions such as performance evaluation, promotions or workload allocation.

High-risk systems must comply with **strict governance obligations** including risk management systems, data governance, human oversight, logging and regulatory documentation. \- becomes **much more complex** because once the system is classified as **High Risk**, the **EU AI Act introduces mandatory compliance controls such as risk management systems, training data governance, technical documentation, human oversight design and post-market monitoring**.

---

# **Delivery Lifecycle Governance — High Risk Use Case**

| Delivery Phase | Delivery Manager Actions to Embed Compliance | Risk Analysis Owner | Review and Sign-off Authority | Additional Governance Details |
| ----- | ----- | ----- | ----- | ----- |
| Discovery | Conduct a formal AI risk classification workshop because the system analyses employee behaviour and may influence workforce management decisions. Document the intended use of Copilot analytics such as participation levels, communication responsiveness and collaboration sentiment. Identify the potential impact on employees including fairness, bias and workplace monitoring concerns. Initiate an AI risk management file describing potential harms, mitigations and governance controls. Record the system in the organisation’s AI registry required for high-risk systems. Engage HR, legal and worker representation bodies early to validate whether the system is acceptable from an employment governance perspective. | Enterprise Architect and Responsible AI Specialist | Chief Risk Officer and Responsible AI Committee | Stage Gate: High-Risk AI Identification. Outcome: Use case formally classified as High Risk and allowed to proceed only with full compliance programme. |
| Architecture and Design | Design the AI system with mandatory human oversight controls. Define clear limitations stating that Copilot insights are advisory and cannot independently determine employment outcomes. Architect safeguards preventing automated ranking or scoring of employees without review. Define fairness and bias evaluation criteria for behavioural analytics models. Create technical documentation describing system purpose, architecture, algorithms and data sources as required by the EU AI Act. Define logging architecture capturing AI outputs, data inputs and manager interactions. Design transparency mechanisms explaining to employees how AI insights may be generated. | Solution Architect and Responsible AI Architect | Enterprise Architecture Board and Legal Counsel | Stage Gate: High-Risk AI Architecture Compliance Review. Outcome: Architecture approved with documented human oversight and transparency mechanisms. |
| Development and Configuration | Implement the Copilot analytics capability according to approved governance boundaries. Ensure models analysing communication patterns are trained on representative datasets to minimise bias. Build system controls preventing automatic decisions such as promotion recommendations or disciplinary triggers. Implement detailed event logging capturing AI outputs, input datasets and human actions. Create documentation describing the system’s technical behaviour and model assumptions to satisfy regulatory traceability requirements. | AI Engineering Lead and Data Science Lead | Platform Owner and Chief Information Security Officer | Stage Gate: High-Risk AI Implementation Review. Outcome: System verified to align with approved architecture and regulatory requirements. |
| Testing | Conduct extensive model validation and bias testing across demographic groups to identify potential discriminatory patterns. Test whether behavioural insights could unfairly disadvantage certain employees such as those working remotely or those with different communication styles. Validate that the system does not automatically generate performance scores or rankings unless explicitly approved by governance bodies. Test the effectiveness of human oversight processes ensuring managers must interpret AI insights rather than rely on automated outputs. Validate logging and traceability mechanisms required for regulatory audits. | QA Lead and Responsible AI Testing Specialist | Data Protection Officer and Responsible AI Committee | Stage Gate: High-Risk AI Compliance Testing Review. Outcome: System approved only if fairness testing, oversight controls and logging meet regulatory standards. |
| Deployment | Deploy the system under strict governance controls. Provide training to managers explaining how Copilot insights should be interpreted responsibly and that AI outputs must not be used as sole decision making evidence in employment actions. Publish transparency notices explaining to employees that collaboration analytics may be generated. Ensure regulatory documentation and technical files are stored for audit readiness. | Platform Operations Lead and HR Technology Lead | Chief Human Resources Officer and CIO | Stage Gate: High-Risk AI Deployment Approval. Outcome: System deployed with mandatory governance controls and employee transparency measures. |
| Monitoring and Continuous Governance | Monitor system behaviour continuously for fairness, bias or unintended consequences affecting employees. Review logs to detect misuse such as automated ranking of employees based solely on AI outputs. Establish a process for employees to challenge or question AI generated insights affecting them. Maintain ongoing post-deployment monitoring reports required for high-risk AI systems. If the system expands into automated decision making, trigger regulatory reassessment and potentially new conformity obligations. | Responsible AI Monitoring Team and HR Governance Team | Responsible AI Committee and Chief Risk Officer | Stage Gate: Post-Market Monitoring Review. Outcome: System remains compliant while human oversight and fairness monitoring continue. |

---

# **Use Case 4 — Psychological Profiling of Employees**

## **Risk Level: Unacceptable Risk**

### **Scenario**

An organisation proposes using **Microsoft Copilot** to analyse meeting recordings, voice tone and facial expressions during video calls in order to infer:

* emotional states  
* psychological traits  
* honesty or trustworthiness  
* leadership potential

These inferred traits would be used to guide internal HR decisions.

---

### **Relevant Legal Section**

Article 5 of the **EU Artificial Intelligence Act** lists **prohibited AI practices**.

One prohibited category includes **AI systems that infer emotions or sensitive attributes in workplace environments**, especially when used for decision-making about individuals.

---

### **Why This Use Case Is Unacceptable**

The system attempts to infer **psychological and emotional characteristics** from behavioural signals such as:

* voice tone  
* facial expressions  
* speech patterns

This creates several unacceptable risks:

* intrusive workplace surveillance  
* pseudoscientific psychological inference  
* discriminatory outcomes  
* manipulation of employees

Because these systems directly threaten **fundamental rights and dignity**, they are **prohibited under the Act**.

---

### **Regulatory Consequences**

If an organisation attempted to deploy such a system within the EU:

* regulators could order the system withdrawn  
* fines could reach **7 percent of global turnover**

---

### **Delivery Governance Insight**

For delivery leaders this type of proposal should trigger an **immediate regulatory stop**.

The correct response is not mitigation but **project termination or redesign**.

---

# **Now mapping this to the EU AI act \- *Use Case 4 — Unacceptable Risk***

## **Copilot-Based Psychological Profiling of Employees from Meeting Conversations**

An organisation explores an advanced Copilot capability designed to analyse recorded meetings and internal communications in order to generate psychological profiles of employees.

The proposed system would analyse:

* meeting recordings  
* voice tone  
* facial expressions during video calls  
* language patterns in conversations  
* emotional cues in speech

Using this information, Copilot would attempt to infer psychological characteristics of employees such as:

* emotional stability  
* stress levels  
* personality traits  
* honesty and trustworthiness  
* likelihood of leadership capability  
* risk of employee misconduct

The organisation’s stated goal is to support HR and leadership teams in:

* identifying employees suited for leadership roles  
* detecting individuals experiencing high stress  
* predicting potential workplace conflicts  
* assessing cultural fit during internal promotions

Managers would receive automated reports ranking employees across various inferred psychological attributes based purely on their behaviour during workplace communications.

Although the system is framed as a way to support workforce wellbeing and leadership development, it effectively attempts to **infer emotional states and personality traits from behavioural signals captured during workplace interactions**.

Employees would be unaware of how these inferences are generated and could be evaluated or categorised based on opaque algorithmic analysis of their conversations.

Because such a system attempts to derive sensitive psychological insights about individuals using behavioural data collected in the workplace, it would create profound concerns around surveillance, manipulation and employee rights.

Now we will **map each Copilot use case to the relevant provisions of the EU AI Act** and explain *why the risk level applies legally*. This is the type of explanation a Delivery Manager can confidently use when discussing AI governance with legal teams, architects and executives.

For reference the regulation itself is the **EU Artificial Intelligence Act**.

# ---

Below is the **delivery lifecycle governance table for Use Case 4 \-** Use Case 4  Using **Microsoft Copilot** to analyse meeting recordings from **Microsoft Teams**, including facial expressions, voice tone and conversational patterns, to infer employee emotional state, psychological traits or honesty levels in order to support HR decisions such as promotions, leadership potential or trustworthiness assessments.

Risk Tier  
 Unacceptable Risk under the **EU Artificial Intelligence Act** because the system attempts to infer emotions and psychological attributes of individuals in a workplace environment. Such practices are **prohibited AI uses** under Article 5 of the regulation.

Because the use case is prohibited, the delivery lifecycle effectively stops at the **early governance stages**.- is actually **very interesting from a Delivery Manager perspective** because the lifecycle stops early and the governance outcome becomes **“project terminated or redesigned”**, which is an important scenario to show when discussing AI governance maturity.

| Delivery Phase | Delivery Manager Actions to Embed Compliance | Risk Analysis Owner | Review and Sign-off Authority | Additional Governance Details |
| ----- | ----- | ----- | ----- | ----- |
| Discovery | Document the proposed AI capability which attempts to infer employee emotional states or psychological traits using meeting recordings. Initiate an AI risk classification workshop to evaluate whether the proposed system falls within prohibited AI categories. Review the EU AI Act provisions on emotion recognition and behavioural inference in workplace environments. Engage HR, legal and responsible AI governance teams to evaluate the ethical and legal implications. Identify potential violations of employee rights and privacy laws. | Responsible AI Architect and Enterprise Architect | Responsible AI Committee and Chief Risk Officer | Stage Gate: Prohibited AI Screening. Outcome: Initial assessment indicates the proposed capability may fall into a prohibited AI category. |
| Architecture and Design | Conduct a detailed legal and ethical review of the proposed system architecture including analysis of facial expression recognition, voice tone analysis and behavioural inference models. Confirm that the system attempts to infer emotional or psychological characteristics from behavioural signals captured during workplace interactions. Document the legal conclusion that such inference mechanisms fall under prohibited practices. Prepare recommendation to halt the design stage due to regulatory prohibition. | Responsible AI Architect and Legal Counsel | Chief Legal Officer and Responsible AI Governance Board | Stage Gate: Prohibited AI Determination. Outcome: Architecture rejected because the proposed capability constitutes prohibited AI under the EU AI Act. |
| Development and Configuration | No development activities permitted once the prohibited classification is confirmed. Delivery Manager ensures project resources are redirected and that no experimental development continues within the organisation. If the business objective remains valid such as improving employee wellbeing or collaboration health, initiate redesign workshops to identify compliant alternative solutions that do not rely on emotional or psychological inference. | Responsible AI Governance Team | Chief Technology Officer and Responsible AI Committee | Stage Gate: AI Development Halt. Outcome: Development phase cancelled due to regulatory prohibition. |
| Testing | Testing phase does not occur because the system cannot legally progress beyond design review. Any prototype created during early exploration must be decommissioned or archived for internal research purposes only with strict access controls. | Responsible AI Governance Team | Chief Risk Officer | Stage Gate: Compliance Termination Confirmation. Outcome: No testing permitted for prohibited AI use cases. |
| Deployment | Deployment phase cannot occur. Delivery Manager documents the decision that the system cannot be deployed within the EU or within organisational environments governed by EU AI Act requirements. Communicate the outcome to executive stakeholders and ensure that procurement teams do not acquire similar capabilities from vendors. | Responsible AI Governance Team | Executive Risk Committee and CIO | Stage Gate: AI Deployment Prohibition. Outcome: Use case formally rejected and recorded as prohibited. |
| Monitoring and Continuous Governance | Record the rejected use case in the organisation’s AI governance register as an example of prohibited AI. Use the case in internal training programmes to educate teams about prohibited AI practices. Monitor future project proposals to ensure similar capabilities are not reintroduced under different project names. | Responsible AI Governance Office | Responsible AI Committee | Stage Gate: Governance Knowledge Capture. Outcome: Case recorded as prohibited and used as governance precedent. |

In interviews this approach lets you say:

“I built a portfolio analysing real enterprise AI deployments and mapped them to EU AI Act compliance controls and delivery lifecycle governance.”

That signals **practical leadership**, not just awareness.

# 

---

# **Key Lesson for Delivery Managers**

Across these four examples the **same AI platform — Microsoft Copilot — produces completely different regulatory outcomes depending on the use case**.

| Use Case | Risk Level | Why |
| ----- | ----- | ----- |
| Meeting summaries | Minimal risk | Productivity assistance |
| Document classification | Limited risk | AI suggestions with human oversight |
| Employee behaviour analytics | High risk | Impacts employment decisions |
| Psychological profiling | Unacceptable | Violates fundamental rights |

This illustrates one of the most important principles of the **EU Artificial Intelligence Act**:

**AI regulation is driven by use case and impact, not by the technology itself.**

---

Below are **three practical tools Delivery Managers can use when discussing AI systems under the EU Artificial Intelligence Act**. These tools help translate legal language into quick operational judgement during project discussions, architecture reviews or executive meetings.

---

# **1\. The 10-Question AI Risk Classification Checklist**

A Delivery Manager can run through these questions during early design or governance workshops. If the answer to any of the early questions is **yes**, the system may already be in a higher risk category.

### **Step 1 — Check for Prohibited AI First**

Ask these questions first because they immediately stop the project.

1. Does the AI attempt to **manipulate people’s behaviour without their awareness**?  
2. Does it attempt to **infer emotions or psychological traits in the workplace or education environments**?  
3. Does it involve **social scoring of individuals based on behaviour or characteristics**?  
4. Does it attempt **biometric identification using scraped images or surveillance databases**?

If the answer to any of these is yes, the project may fall into **unacceptable risk** and must be redesigned.

Example: A proposal to analyse facial expressions in \*\*Microsoft Teams meetings to assess employee honesty would fail at this stage.

---

### **Step 2 — Check if the AI Falls into High-Risk Domains**

If the system passes the first stage, move to the next questions.

5. Will the AI **influence hiring, promotions, performance reviews or employee evaluation**?  
6. Will it **determine access to education, credit, insurance or public services**?  
7. Will it operate in **critical infrastructure such as energy, transport or healthcare systems**?  
8. Will the AI be used by **law enforcement or government authorities**?

If the answer to any of these is yes, the system may be classified as **high-risk AI** under Annex III.

Example: A system using \*\*Microsoft Copilot to analyse employee communication behaviour during performance reviews would trigger this stage.

---

### **Step 3 — Check for Transparency Requirements**

If the system is not high risk, check the following.

9. Will users **interact directly with an AI system such as a chatbot or AI assistant**?  
10. Will the system **generate synthetic content such as text, images or audio**?

If yes, the system may fall into **limited risk** and require transparency disclosures.

Example: A Copilot chatbot assisting customers with loyalty programme questions.

---

### **Outcome**

After answering the checklist, the likely classification becomes clear:

| Outcome | Risk Tier |
| ----- | ----- |
| Prohibited behaviour detected | Unacceptable risk |
| AI influences employment or rights | High risk |
| AI interacts with users or generates content | Limited risk |
| AI assists internal productivity | Minimal risk |

---

# **2\. How Copilot Projects Accidentally Become High-Risk**

Many organisations begin with safe productivity use cases but gradually expand functionality. This process is known as **use case drift**. Below are three common examples.

---

### **Scenario 1 — Meeting Insights Become Performance Monitoring**

Initial use case- Copilot summarises meetings and generates notes.

Expansion- Managers request analytics showing:

* who speaks the most  
* who interrupts others  
* who contributes the least

Final stage- The data begins influencing **performance reviews or promotion decisions**.

Result- The system moves from minimal risk to **high-risk employment AI**.

---

### **Scenario 2 — Document Classification Becomes Compliance Scoring**

Initial use case- Copilot classifies documents during a migration.

Expansion- The system begins flagging employees responsible for outdated documents.

Final stage- Managers use AI outputs to **evaluate employee performance or compliance behaviour**.

Result- The system enters **worker monitoring territory**, again triggering high-risk classification.

---

### **Scenario 3 — Collaboration Insights Become Behaviour Profiling**

Initial use case-  Copilot analyses organisational collaboration trends.

Expansion- Dashboards show **individual productivity scores**.

Final stage- Managers begin ranking employees based on AI-generated collaboration metrics.

Result-  The system becomes a **worker management AI system**, classified as high risk.

---

# **3\. How to Explain AI Risk Levels to Executives**

Executives often do not need detailed legal explanations. The key is translating the framework into **business language**. A simple explanation might look like this.

---

### **Minimal Risk**

AI helps employees work faster.

Example- Copilot summarising meetings or drafting documents.

Business impact- Productivity improvement with minimal regulatory concern.

---

### **Limited Risk**

AI interacts with people or produces content.

Example- AI chatbots or automated document classification.

Business impact- Transparency obligations and clear disclosure that AI is being used.

---

### **High Risk**

AI influences important decisions affecting people’s rights or opportunities.

Example \- AI evaluating employee performance or recommending promotions.

Business impact

* strict compliance requirements  
* documentation and monitoring  
* regulatory oversight

---

### **Unacceptable Risk**

AI that violates fundamental rights or creates intrusive surveillance.

Example- AI attempting to infer psychological traits or emotions of employees.

Business impact- The system **cannot legally be deployed in the EU**.

---

# **Final Delivery Insight**

For a Delivery Manager, the key governance question is always:

**“Does this AI system influence decisions about people?”**

If the answer is yes, the project likely enters **high-risk territory under the EU Artificial Intelligence Act**.

If the system only **assists humans with productivity tasks**, it typically remains minimal or limited risk.

---

# **Suggested Client Workshop Slide Framework**

Below is a **10-slide structure** you could reuse repeatedly for different AI use cases. The beauty of this structure is that you can analyse **any AI system in the market**.

---

# **Slide 1 — Workshop Title**

**Title**

AI Governance in Practice \- Applying the EU AI Act to Real AI Deployments

Subtitle example \- Using real enterprise AI use cases to assess risk classification and delivery governance

Possible opening statement \- AI adoption is accelerating faster than governance capability. This workshop explores how organisations can deploy AI safely while complying with the EU AI Act.

---

# **Slide 2 — Why AI Governance Matters**

Explain the strategic context.

Key points

AI systems increasingly influence:

• hiring decisions  
 • financial services access  
 • customer behaviour  
 • operational decision making

The EU AI Act introduces **legal accountability for AI deployment**.

Organisations must now demonstrate:

• responsible AI governance  
 • risk classification  
 • lifecycle monitoring.

---

# **Slide 3 — EU AI Act Risk Framework**

Introduce the **four risk tiers** of the **EU Artificial Intelligence Act**.

Structure the slide visually as a pyramid.

Top  
 Unacceptable Risk  
 Prohibited AI

High Risk  
 AI affecting rights safety or employment

Limited Risk  
 Transparency obligations

Minimal Risk  
 General productivity AI

Key message

**Risk is determined by use case, not technology.**

---

# **Slide 4 — Delivery Lifecycle Governance Model**

Show the lifecycle framework you created earlier.

Lifecycle phases

Discovery  
 Architecture and Design  
 Development  
 Testing  
 Deployment  
 Monitoring

Explain that **AI governance must be embedded across the lifecycle**, not just checked at deployment.

---

# **Slide 5 — AI Risk Classification Checklist**

Introduce the **10-question checklist**.

Highlight three critical triggers:

Does the system influence decisions about people?  
 Does it operate in employment or financial services?  
 Does it infer emotions or behaviour?

If yes, the risk level escalates.

This becomes your **practical decision tool**.

---

# **Slide 6 — Example Use Case Analysis**

Introduce a real AI system.

Example \- **Microsoft Copilot**

Explain the use case briefly such as meeting summaries.

Then show the classification:

Risk tier- Minimal Risk

Reason- Productivity assistance only.

---

# **Slide 7 — Governance Implementation**

Show the **delivery lifecycle governance table** condensed.

Explain:

What the Delivery Manager does  
 Who analyses risk  
 Who signs off  
 What the stage gate is.

This slide demonstrates **execution capability**.

---

# **Slide 8 — Risk Escalation Scenario**

Show how the same AI system becomes high risk.

Example

Copilot analysing employee behaviour in \*\*Microsoft Teams meetings.

Explain how the use case crosses into **employment monitoring**, triggering high-risk obligations.

Key insight

Small design changes can drastically change regulatory classification.

---

# **Slide 9 — Governance Decision Outcomes**

Explain the three possible outcomes after risk assessment.

Proceed-  Use case approved with governance controls

Proceed with strict controls-  High risk compliance required

Stop \- Prohibited AI use case

This reinforces **executive accountability**.

---

# **Slide 10 — Key Takeaways**

Summarise the core lessons. 

AI governance must start at the design stage.

The same AI platform can fall into different risk categories depending on use.

Delivery teams must collaborate with:  
• legal  
 • architecture  
 • data governance  
 • responsible AI teams.

---

# **Your Portfolio Strategy (Excellent Idea)**

Your next step should be creating **case study analyses** using this framework.

Each case study should contain:

1 AI system description  
 2 use case explanation  
 3 EU AI Act risk classification  
 4 governance implications  
 5 delivery lifecycle controls.

---

# **Example Portfolio Topics**

You could analyse systems like:

* **ChatGPT** in customer service  
* **Microsoft Copilot** in productivity tools  
* **Salesforce Einstein** in CRM analytics  
* **Amazon Rekognition** in surveillance systems  
* **Google Gemini** in enterprise knowledge search

Each one could be a **4–6 page analysis**.

After analysing **8–10 real AI systems**, you will have a **serious AI governance portfolio**.

---

# **Why This Will Help You Get Roles**

Most organisations currently struggle with:

• AI governance implementation  
 • interpreting the EU AI Act  
 • embedding compliance into delivery programmes.

Your portfolio would show you can:

• interpret regulation  
 • assess AI risk  
 • design governance frameworks  
 • run compliance programmes.

That combination is exactly what **AI Delivery Leads, Responsible AI Managers and AI Programme Directors** need.

Here's a **ready‑to‑use list of about 20 real AI use cases from major organisations** that are ideal candidates for EU AI Act analysis. These span across risk tiers from **minimal to high‑risk and borderline cases**, which will make your portfolio **rich, nuanced and compelling** for hiring managers and clients.

For each use case below, you can apply your *risk classification framework \+ delivery governance analysis* from the slides we built.

---

# **📌 20 Real‑World AI Use Cases to Analyse Under the EU AI Act**

## **A. Minimal or Limited Risk — Productivity & Wizard‑Style Assistance**

These systems help users be more efficient but do **not make impactful decisions about people or access to services**.

1. **Microsoft Copilot** summarising Teams meetings and auto‑generating action items

2. **ChatGPT** drafting and revising internal policy documents

3. \*\*Google Gemini‑powered search assistance to support enterprise knowledge retrieval

4. **Grammarly** providing writing quality suggestions in business communication

5. **Notion AI** assisting brainstorming or content structuring in internal wikis

6. **Jasper** generating marketing copy for customer newsletters

7. **AI‑based routing in CRM platforms** such as **Salesforce Einstein** offering product recommendations

**Focus for portfolio:**  
 Minimal risk classification \+ transparency (if user interacts with AI)

---

## **B. Limited Risk — Customer Interface & Transparency‑Sensitive AI**

These interact with external users and need **clear notice and consent**, but typically won’t hit high‑risk unless decisions affect rights.

8. Chatbots handling customer service FAQ (banking or telecom)

9. AI recommendation panels on e‑commerce product pages

10. Real‑time transcription and summarisation for multilingual support lines

**Focus for portfolio:**  
 What transparency controls should be in place

---

## **C. Borderline / High Risk — Decisions That *May* Affect People**

These systems **begin to influence people outcomes**, even if not directly making decisions.

11. **AI resume screening systems** used by recruiters

12. **AI scheduling assistants** that rank employee shifts

13. **AI tools analysing meeting behaviours** to propose workload balancing

14. **AI sentiment analysis** in employee engagement platforms

15. **AI forecasting for credit recommendations** in banks (non‑binding)

**Portfolio insights:**  
 Good place to expand on *human oversight controls* and *bias testing*

---

## **D. Clearly High Risk — Impacting Rights, Access or Opportunities**

These are strong examples of systems that **affect people’s rights, opportunities or access to services** and require full high‑risk compliance.

16. **IBM Watson for Oncology** (clinical decision support in cancer treatment)

17. **AI‑based loan risk scoring models** in retail banking

18. **Automated candidate ranking systems** used by major enterprises

19. **AI in law enforcement predictive analytics**

20. **AI‑based credit scoring in micro‑finance** affecting financial inclusion

**Portfolio impact:**  
 These force you to explore **conformity assessments, data governance, human oversight, logs and corrective actions**

---

# **🧠 How to Turn These into Portfolio Case Studies**

For each use case you analyse, follow a consistent structure:

---

## **📄 Case Study Template (5 Sections)**

### **1\. Business Context**

Describe the company, the AI system and its functional purpose (what it *does*).

Example  
 Copilot summarises meetings so distributed teams don’t lose key decisions.

---

### **2\. EU AI Act Risk Tier Classification**

Use your risk checklist to classify:

* Minimal risk  
* Limited risk  
* High risk  
* Unacceptable risk

Include *why* — reference risk triggers such as:

* employee evaluations  
* access to services  
* impact on rights

---

### **3\. Delivery Governance Implications**

Use your lifecycle framework:

**Discovery** → risk analysis  
 **Architecture & Design** → human oversight controls  
 **Development** → bias mitigation  
 **Testing** → fairness and performance validation  
 **Deployment** → transparency and consent  
 **Monitoring** → logs, corrective actions

Fill this in with your own interpretation for the use case.

---

### **4\. Regulatory Controls Required**

List what the EU AI Act would require here:

* transparency notices  
* human‑in‑the‑loop controls  
* documented data governance  
* risk management file  
* post‑deployment logging

---

### **5\. Practical Recommendations**

Based on your analysis:

• What should the organisation do next?  
 • Is the use case compliant as‑is?  
 • What governance changes are required?  
 • Would you advise redesign or stop?

---

# **🗂 Optional Bonus Add‑Ons for Your Portfolio**

To make your work **stand out further**, consider adding:

🔥 A **decision flowchart** for determining AI risk level  
 📊 A **heatmap** showing which AI systems are high vs limited risk  
 🎤 **Narrative summaries** for non‑technical leaders  
 📁 **Regulatory mapping table** linking each use case to specific articles in the EU AI Act

---

# **🎯 Value Proposition for Hiring Managers**

When presenting this portfolio in interviews or proposals, you can say:

“I can take any AI deployment — internal or external — and rapidly assess it with a decision framework, classify it under the EU AI Act, map it to delivery governance controls and recommend compliance actions.”

Very few applicants can speak to **both regulatory interpretation AND delivery execution**, which is why this portfolio would position you as a *practical AI governance practitioner*, not just a theorist.

Source: 

* ChatGPT and   
* EU AI Act \- [https://artificialintelligenceact.eu/chapter/1/](https://artificialintelligenceact.eu/chapter/1/) 