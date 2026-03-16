# Article Outline: Why AI Risk Classification is the First Step in Project Initiation

## 1. Introduction: The Evolution of Project Governance
*   **The Hook:** In traditional software delivery, bolted-on security is a massive risk. In the era of AI, bolted-on governance is a regulatory disaster.
*   **The Core Concept:** Implementing AI is not just a technological challenge; it is a regulatory one. For a Project or Delivery Manager, categorizing AI risk must be one of the very first steps in project initiation.
*   **The Thesis:** Successful AI delivery requires establishing risk tiers at the Discovery Phase, before a single line of code is written or vendor contract is signed.

## 2. Understanding the Risk-Based Framework (The EU AI Act Approach)
*   **Context:** Briefly introduce the European Union Artificial Intelligence Act and its risk-based model. Emphasize that compliance obligations are triggered by the *potential harm* of the system, not the underlying technology.
*   **The Technology Parallax:** Use a practical example to prove that the **use case** dictates the risk, not the software.
    *   *Example:* Microsoft Copilot summarizing meetings (Minimal Risk) vs. Microsoft Copilot evaluating employee performance (High Risk).
*   **The Four Risk Tiers:** Briefly define the four levels along a linear scale:
    1.  Unacceptable Risk
    2.  High Risk
    3.  Limited Risk
    4.  Minimal Risk

## 3. The "Fast Fail": Identifying and Gracefully Aborting Unacceptable Risk
*   **What is Unacceptable Risk?** Define systems that threaten fundamental rights and democratic norms (e.g., social scoring, emotion recognition in workplaces, psychological profiling).
*   **The Delivery Challenge:** As a Delivery Manager, how do you handle stakeholders pitching an "innovative" idea that actually violates regulations?
*   **The Graceful Abort:** 
    *   Strategies for implementing a "hard stop" at the Discovery phase.
    *   How to steer the conversation away from prohibition and toward compliant alternatives without stifling innovation. 
    *   *Real-World Scenario:* Rejecting an employee psychological profiling tool and pivoting the business need to a High-Risk, but compliant, structured performance dashboard.

## 4. The Delivery Manager’s Playbook: Governance at Discovery
*   **The Early Checkpoint:** How to run an AI Risk Classification Workshop during the Discovery or Feasibility phase.
*   **Mapping the Tiers to the Delivery Lifecycle:**
    *   **Minimal/Limited Risk:** Lightweight transparency checks, simple disclosures (e.g., "You are interacting with AI"), and data governance.
    *   **High Risk:** Treating the project like a regulated engineering discipline (e.g., medical devices). Introducing rigorous compliance cycles, human-in-the-loop oversight, bias testing, and extensive traceability logs.
*   **Cross-Functional Orchestration:** Why the Delivery Manager must now coordinate closely with Legal, Compliance, HR, and Enterprise Architecture as part of the standard sprint zero/design phase.

## 5. Conclusion: AI Readiness is Governance Readiness
*   **The Takeaway:** Great AI project managers aren't just technical facilitators; they are risk and governance orchestrators.
*   **Call to Action:** Encourage PMs to integrate an "AI Risk Classification" artifact into their standard project initiation toolkit. Ensure stakeholders understand that early classification accelerates delivery by preventing late-stage regulatory blockers.

---

# Article: Why AI Risk Classification is the First Step in Project Initiation

## The Evolution of Project Governance
In traditional software delivery, bolting on security at the end of a project is a massive risk. In the era of AI, bolting on governance is a regulatory disaster.

Implementing AI is not just a technological challenge. It is a regulatory one. For a Delivery Manager, categorizing AI risk must be one of the very first steps in project initiation. 

Successful AI delivery requires establishing risk tiers at the Discovery Phase before a single line of code is written or vendor contract is signed.

## Understanding the Risk-Based Framework
The European Union Artificial Intelligence Act introduces a risk-based model. It is the first major regulatory framework designed to govern AI systems across the EU. Instead of regulating every AI application equally, compliance obligations increase as the potential harm of the system increases.

A key concept for Delivery Managers is that the use case dictates the risk, not the software. The same technology can fall into different regulatory categories depending on how it is used. For example, using Microsoft Copilot to summarize meeting notes is considered Minimal Risk. However, using Copilot to evaluate employee performance falls into High Risk.

The EU AI Act divides AI systems into four risk tiers along a linear scale.
1. Unacceptable Risk
2. High Risk
3. Limited Risk
4. Minimal Risk

## Calibrating Risk to Organizational Appetite
While external frameworks provide a baseline, one must also account for the organization's unique appetite for Gen AI risk. It is important to develop a rubric to calibrate expectations of what constitutes a high versus a medium risk internally, as organizations can otherwise run into disagreements. It is essential that the executive or product manager in charge of the use case leads this initial assessment. This profile is then validated by a cross-functional governance group, ensuring that the risk classification reflects both the nature of the technology and the company-specific context.

## The Fast Fail: Aborting Unacceptable Risk
At the far end of this risk scale are AI systems classified as Unacceptable Risk. These are considered incompatible with European values and are banned outright. These systems threaten fundamental rights and democratic norms. Examples include social scoring, emotion recognition in workplaces, and psychological profiling.

A Delivery Manager might handle stakeholders pitching an innovative idea that actually violates regulations. One needs to implement a hard stop at the Discovery phase. It is important to steer the conversation away from prohibition and toward compliant alternatives without stifling innovation. 

For example, a stakeholder might propose analyzing video calls to infer emotional states for HR decisions. This is Unacceptable Risk. One can reject the psychological profiling tool and pivot the business need to a High Risk, but compliant, structured performance dashboard.

## The Delivery Manager’s Playbook: Governance at Discovery
One should run an AI Risk Classification Workshop during the Discovery or Feasibility phase. 

Minimal and Limited Risk systems require lightweight transparency checks. One might need simple disclosures to inform users they are interacting with AI. Data governance is also key.

High Risk systems require a different approach. One must treat the project like a regulated engineering discipline. This means introducing rigorous compliance cycles and human-in-the-loop oversight. Bias testing and extensive traceability logs are also required. 

The Delivery Manager must constantly coordinate with Legal, Compliance, HR, and Enterprise Architecture teams. This collaboration should begin during the standard sprint zero or design phase.

## Conclusion: AI Readiness is Governance Readiness
Great project delivery managers are not just technical facilitators. They are risk and governance orchestrators.

An AI Risk Classification artifact should be integrated into the standard project initiation toolkit. Ensuring stakeholders understand that early classification accelerates delivery by preventing late stage regulatory blockers is paramount.
