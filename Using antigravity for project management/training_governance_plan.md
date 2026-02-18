# Antigravity Training & Governance Plan for the PMO

## 1. Free Training Resources
Most enterprise AI tools come with "Documentation," not "Training." You must curate the free resources into a **Learning Path**.

*   **Official Documentation (The Basics):**
    *   *Source:* The official Antigravity/Gemini Code Assist docs.
    *   *Usage:* Mandatory reading for "Day 1." Covers installation, basic commands, and context selection.
*   **"Prompt Engineering" Guides (The Skill):**
    *   *Source:* Google/Microsoft/Coursera free modules on "Generative AI for Project Managers."
    *   *Usage:* Focus on "Chain of Thought" prompting. Teaches PMs how to break big tasks down so the AI doesn't hallucinate.
*   **The "Internal Library" (The Golden Asset):**
    *   *Source:* You (The Champion).
    *   *Action:* Create a shared Repo/Wiki page called "Approved Prompts."
    *   *Example:* "Here is the exact prompt to use for summarizing a Risk Log." "Here is the prompt for checking compliance."
    *   *Why:* This is better than generic training because it uses *your* templates.

## 2. Standardized Training Modules (To Build Internally)

Since specialized "Antigravity for PMO" courses don't exist yet, you should run these internal workshops:

### Module A: The Mechanic (1 Hour)
*   How to install the extension securely.
*   How to select the right "Context" (e.g., "Only look at the specs folder, ignore the `temp` folder").
*   **Critical Safety Rule:** "Review before Commit." Never trust the output 100%.

### Module B: The Compliance Guardian (1 Hour) - *Mandatory*
*   **Data Classification 101:** What data is "Public" vs "Internal" vs "Restricted."
*   **The "PII" Red Line:** "Never put customer names, credit cards, or passwords into the prompt."
*   **The "Sanitization" Workflow:** How to replace "Client X" with "Client" before running the AI.

## 3. Enforcing Safety & Compliance (Governance)

You cannot rely on "honor systems." You need **Systemic Enforcement**.

*   **Rule 1: Enterprise-Only Logins**
    *   *Enforcement:* IT blocks personal Gmail logins to the extension. Only corporate SSO works. ensuring all logs are auditable.
*   **Rule 2: The "Context Ignore" File (.gitignore for AI)**
    *   *Action:* Deploy a standard `.aignore` (or equivalent) file to every project repo.
    *   *Function:* This file explicitly tells the AI "DO NOT READ these files" (e.g., `passwords.txt`, `customer_data.csv`).
    *   *Benefit:* It creates a "Safety Fence" so PMs can't accidentally leak sensitive data.
*   **Rule 3: Spot Audits**
    *   *Action:* Review a random sample of "AI Generated" docs each month.
    *   *Check:* Are they factually accurate? (Hallucination check). Do they contain PII? (Leak check).

## 4. Summary: The "PMO AI License"
**Recommendation:** Do not give the license to a PM until they have passed your internal "Module B (Compliance)" quiz. Treat it like a driver's license—privilege comes with proven responsibility.
