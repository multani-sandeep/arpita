# CV Transformer - Arpita Narula

STRICT: Always use the latest committed version (git) of any source files (templates, base CVs) before generating a new CV. Do not rely on previously read versions from earlier in the session.
STRICT: Donot add any new information to the CV
STRICT: ArpitaNarula.md is the source of truth for all information and never updated by the agent.
STRICT: Use a maximum of 3 terms of overlapping terminology between the CV Summary section and the Job advert, donot remove any overlap originally present within the CV.
STRICT: Donot use em-dash (—) or en-dash (–) in the CV.
STRICT: Donot use ", and" syntax instead use " and".

<!-- Format decision: switched to Two-Page format exclusively on 5 May 2026. Skills-Led format retired. -->

## Guidance for new CVs
New CVs are created using format from the Generator

- New CVs are named `CV-<position>-<employer>-<mmmYY>.md`
- Format bullets and new lines so they appear correctly in PDF and DOCX
- TSA Exit was Worldpay programme to separate Digital Workspace from FIS. It involved service delivery change management, vendor management and service readiness for Worldpay's Digital Workspace separation programme during the carve-out from FIS.
- Estee Lauder role reflects broader Digital Commerce Feature Delivery (reviews and ratings, gift options, payment methods) beyond UX optimisation — applied across all templates and source.
- Update application log following every CV generation


### Guidance for new CVs when updating for job spec
Create a new file with the suffix `<position>-<employer>-<mmmYY>` when creating a CV for a specific job. STRICT: DONOT update any of the existing CVs.
Additional considerations:
- Use ArpitaNarula-TwoPage-Mar26.md as the source of truth for the new CV
- DONOT ignore the 'Argos/Homebase/Jewson/LeasePlan' part in the experience.
- Donot add automatically new skills or technologies on new CV based on your knowledge or requirement of the job spec. 
- Donot add expertise areas, domain language, or sector terminology to the Summary or Skills that are not present in the template — even if they appear in the job spec. For example, do not add "payment gateways", "payment flows", "API-led integrations" unless those exact terms or directly adjacent terms already exist in the template.
- Exception: if a term is adjacent to something already in the template (e.g. "API orchestration" is in the template, so referencing API delivery context is acceptable), you may include it BUT must flag it explicitly to the user in a post-generation note with the format: "** Adjacent term added: [term] — derived from [template term]. Please confirm."
- Always identify must-have requirements in the job spec and ask before adding them to the relevant sections of new CV
- If a job spec requirement closely matches what's in my CV, then update the skill to align more closely to the job spec requirement. Donot try to match wording exactly to job spec and if its a close match then leave from source CV. 
- Update application log following every CV generation
- If job role is clearly a contract position then suggest highlighting contract positions.
- Donot remove the redundancy flag in the Worldpay employment
- DONOT make the bullets or content concise when updating for job spec
- Update Summary section to align with the role using the experience and roles provided in the CV. Donot invent a new role based on job specification, use similar roles to what are present in the experience section of the template 

#### Pre-Generation Fit Assessment (run before creating the CV)

STRICT: Complete this step before any CV generation. Do not start writing the CV until the user has confirmed they want to proceed.

**Step 1 — Duplicate check**
- Check ApplicationLog.md and Job-* files for a similar role at the same company
- If duplicate found: inform user and stop; do not proceed

**Step 2 — Fit rating**
- Extract must-have requirements from the job spec
- Rate each must-have against ArpitaNarula-TwoPage-Mar26.md
- Present as a table: Requirement | Covered in CV | Strength (Strong / Partial / Gap)
- Include an overall fit score (X/10) with one-line rationale

**Step 3 — Challenge areas**
- List must-haves rated as Gap or Partial in a separate table
- For each gap: note whether it is bridgeable (adjacent experience exists) or a hard gap (nothing in CV supports it)
- Flag any terminology in the job spec that is not present in the CV and would require adding new information (not allowed under strict rules)

**Step 4 — Recommendation and confirmation**
- State a recommendation: proceed / proceed with caveats / do not proceed
- Proceed: fit is 7.5/10 or above; gaps are bridgeable
- Proceed with caveats: fit is 6-7.5/10; gaps are notable but not disqualifying; state what will be left uncovered
- Do not proceed: fit is below 6/10 or hard gaps are in must-have requirements; generating a CV would not be a credible application
- STRICT: Ask the user to confirm before generating the CV. Do not proceed without explicit confirmation.

#### Post-Generation Validation (run after CV is created)
- Check are there skills or technologies not mentioned in the original, show them in a tabular and concise format
- Check for excessive use of C-level or related terms
- Check for overstating responsibilities from original eg: Steerco reporting being overstated as Steering committee leadership
- Check generated CV against template whether each bullet implies the same meaning and doesn't change scope of the bullet from template
- Check contract roles, only Shell, Estee, Argos are contract roles
- Skills section should not be more than 10% different from ArpitaNarula-TwoPage-Mar26.md. If different by more than 10% then highlight post generation

## Original Format

### Structure

1. **Header**
   - Full Name (H1)
   - Contact line: Phone | LinkedIn URL | Location | Substack URL

2. **Summary**
   - Bold section title inline with content
   - Role title + brief paragraph (3-4 lines) covering domain expertise, delivery style, and AI fluency

3. **Skills**
   - 4 categories, each as a bold bullet with colon-separated skill tags:
     - Delivery Management
     - Methodologies & Governance
     - Business & Technology Delivery
     - Data & Analytics

4. **Experience** (5 roles, reverse chronological)
   - Each role block:
     - **Role Title | Company | Project/Domain | Date Range** (bold, on one line)
     - _Contract/redundancy note in italics if applicable_
     - Bullet points (5-8 per role) describing delivery contributions
     - Final bullet: **Impact:** summary statement (optional — only include where it adds meaning not already in the bullets)
   - Roles listed:
     1. Delivery Lead | Worldpay (Nov 2024 - Aug 2025)
     2. Digital Project Manager | Estee Lauder - Contract (Nov 2023 - Oct 2024)
     3. Technical Product Manager / Delivery Manager | Shell - Contract (Apr 2022 - Oct 2023)
     4. Agile Project Manager / Product Owner | Costa Coffee (May 2019 - Mar 2022)
     5. Digital Transformation PM / BA | Lodestone Consulting (Jul 2012 - May 2019)
        - Sub-bullets for individual clients: Vodafone, GSK, Ricoh

5. **Past Experience**
   - Two bullets:
     - Argos/Homebase: ecommerce programmes — checkout payment methods, private label credit card journeys, user-generated content, loyalty integrations
     - Jewson (trade community portal) and LeasePlan (B2B/B2C fleet leasing journeys) — B2B digital programmes

6. **Education**
   - Separate bullets with dates:
     - MBA, Warwick Business School | 2012 - 2014
     - Bachelor of Engineering | 1999 - 2003

7. **Certifications**
   - Separate bullets, dated ones first, undated at bottom:
     - PRINCE2 | 2014
     - Certified Scrum Master (CSM) | 2016
     - Microsoft Copilot for Productivity | 2025
     - Generative AI for Project Managers | 2025
     - Prompt Engineering for Generative AI
     - AI Governance

8. **Thought Leadership**
   - Single line referencing Substack AI Delivery & GenAI Governance series at arpitanarula.substack.com

9. **Community & Volunteering**
   - Single line: Eco Centre CBS - Project Manager | STEM Ambassador | Club Safeguarding Officer

### Formatting Conventions
- Bold used for section titles, role titles, and impact labels
- Bullets (●) for skill categories and experience points
- Pipes (|) to separate contact details, education items, and certifications
- Italics for employment context notes (e.g., contract, redundancy)
- 2-page layout with footer on each page

---

## Two-Page Format

### What Changes vs Original
- **Skills** — expanded to 5 categories, adding AI Delivery & Governance
- **Experience** — full role detail retained across both pages, drawn from ArpitaNarula.md
- **Page 1** contains the high-value content a recruiter/hiring manager needs first
- **Page 2** contains older experience and credentials
- **Impact:** labels optional — only retain where the impact statement adds meaning not already in the bullets; remove where it restates the bullets

### Source of Truth
- ArpitaNarula.md

### Page Structure

**Page 1**
- Header + Summary + Skills
- Worldpay (full bullets)
- Estee Lauder (full bullets)
- Shell (full bullets)

**Page 2** (insert `<div class="page-break"></div>` in markdown to force the break)
- Costa Coffee (full bullets)
- Lodestone Consulting (client sub-bullets: Vodafone, GSK, Ricoh)
- Eco Centre CBS (volunteer, brief paragraph)
- Past Experience (two bullets: Argos/Homebase retail; Jewson/LeasePlan B2B)
- Education + Certifications + Thought Leadership + Community & Volunteering

### Structure

1. **Header** — same as Original

2. **Summary** — same as Original

3. **Skills** — 5 categories (bold bullet, colon-separated tags):
   - Delivery Management
   - Methodologies & Governance
   - Business & Technology Delivery
   - Data & Analytics
   - AI Delivery & Governance

4. **Experience** (reverse chronological, condensed)
   - Each role block uses the same structure as Original (Role Title | Company | Project/Domain | Date Range [- italics note])
   - Bullet count: 5-7 per role (fewer than Original)
   - After the Shell block, insert: `<div class="page-break"></div>`
   - Lodestone Consulting entry uses an intro bullet summarising the consulting engagement, followed by bold client name sub-bullets (Vodafone, GSK, Ricoh) with one line each
   - Volunteering role added as a full role block after Lodestone:
     - **Project Manager (Volunteer) | Eco Centre CBS | Oct 2025 - Present**
     - 2 bullets: structured project plans / stakeholder coordination; Eco-Save app development coordination and community testing

5. **Past Experience** — same as Original (two bullets: Argos/Homebase retail, Jewson/LeasePlan B2B)

6. **Education** — same as Original (separate bullets with dates)

7. **Certifications** — same as Original (separate bullets, dated first, undated at bottom)

8. **Thought Leadership** — same as Original (single line, Substack reference)

9. **Community & Volunteering** — same as Original

### Naming Convention
- Job-specific files: `CV-<position>-<employer>-<mmmYY>.md`

### Formatting Conventions
- Same as Original
- No em-dash or en-dash
- Page break inserted with `<div class="page-break"></div>` on its own line in the markdown
- Present command to generate PDF as information : `python3 cv_to_pdf.py CV-<position>-<employer>-<mmmYY>.md /tmp/ArpitaNarula.pdf`
