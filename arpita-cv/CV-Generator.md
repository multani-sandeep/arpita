# CV Transformer - Arpita Narula

## Multi-Provider Support

This guide works with:
- **Claude** (Anthropic) — primary, fully supported
- **Gemini** (Google) — supported, see provider-specific notes
- **Copilot** (Microsoft) — supported, see provider-specific notes

### Universal Strict Rules (All Providers)

STRICT: Always use the latest committed version (git) of any source files (templates, base CVs) before generating a new CV. Do not rely on previously read versions from earlier in the session.
STRICT: Do not add any new information to the CV
STRICT: ArpitaNarula.md is the source of truth for all information and never updated by the agent.
STRICT: Use a maximum of 3 terms of overlapping terminology between the CV Summary section and the Job advert, do not remove any overlap originally present within the CV.
STRICT: Do not use em-dash (—) or en-dash (–) in the CV.
STRICT: Do not use ", and" syntax; instead use " and".
STRICT: Maintain consistency across all formatting rules regardless of AI provider used.

## Guidance for new CVs
New CVs are created using format from the Generator

- New CVs are named ArpitaNarula-`format used`.md
- Format bullets and new lines so they appear correctly in PDF and DOCX
- TSA Exit was Worldpay programme to separate Digital Workspace from FIS. It involved service delivery change management, vendor management and service readiness for Worldpay's Digital Workspace separation programme during the carve-out from FIS.
- Estee Lauder role reflects broader Digital Commerce Feature Delivery (reviews and ratings, gift options, payment methods) beyond UX optimisation — applied across all templates and source.
- Update application log following every CV generation


### Guidance for new CVs when updating for job spec
Create a new file with the suffix `<position>-<employer>-<mmmYY>` when creating a CV for a specific job. STRICT: DONOT update any of the existing CVs.
Additional considerations:
- If not provided ask which template to use.  Arpita-SkillsLed.md or ArpitaNarula-TwoPage-Mar26.md as the source of truth for the new CV
- DONOT ignore the 'Argos/Homebase/Jewson/LeasePlan' part in the experience.
- Donot add automatically new skills or technologies on new CV based on your knowledge or requirement of the job spec. 
- Donot add expertise areas, domain language, or sector terminology to the Summary or Skills that are not present in the template — even if they appear in the job spec. For example, do not add "payment gateways", "payment flows", "API-led integrations" unless those exact terms or directly adjacent terms already exist in the template.
- Exception: if a term is adjacent to something already in the template (e.g. "API orchestration" is in the template, so referencing API delivery context is acceptable), you may include it BUT must flag it explicitly to the user in a post-generation note with the format: "** Adjacent term added: [term] — derived from [template term]. Please confirm."
- Always identify must-have requirements in the job spec and ask before adding them to the relevant sections of new CV
- If a job spec requirement closely matches what's in my CV, then update the skill to align more closely to the job spec requirement. Donot try to match wording exactly to job spec and if its a close match then leave from source CV. 
- Update application log following every CV generation
- For SkillsLed format: Skills and Highlights section should not be more than 10% different from ArpitaNarula-SkillsLed.md. If its different by 10% then highlight post generation
- For TwoPage format: Skills section should not be more than 10% different from ArpitaNarula-TwoPage-Mar26.md. If its different by 10% then highlight post generation
- If job role is clearly a contract position then suggest highlighting contract positions.
- If contract, use 2 page format.
- Donot remove the redundancy flag in the Worldpay employment
- DONOT make the bullets or content concise when updating for job spec
- Update Summary section to align with the role using the experience and roles provided in the CV. Donot invent a new role based on job specification, use similar roles to what are present in the experience section of the template 

#### Validation
- Check if a similar job exists by looking at Application Log and Job-* files. If duplicate found then inform user and stop generation & validation process
- Check are there skills or technologies not mentioned in the original, show them in a tabular and concise format
- Check for excessive use of C-level or related terms
- Check for overstating responsibilities from original eg:  Steerco reporting being overstated as Steering committee leadership
- Check generated CV against template whether each bullet implies the same meaning and doesn't change scope of the bullet from template
- Check contract roles, only Shell,Estee, Argos are contract roles

#### Rating
- Use key job requirements from the spec to rate the CV and show the rating in a tabular and concise format
- In the tabular format suggest updates that improve alignment without changing the meaning of the original CV
- Always provide a overall rating
- Summarise notable gaps

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

## Proposed Format: Skills-Led CV

### What Changes
- **Summary** — unchanged
- **Skills** — unchanged
- **Experience section is replaced** by a new **Key Achievements** section that aggregates highlights across all roles into themed bullet points focused on project management and delivery
- **Experience is moved to the bottom** as a compact chronological list — one line per role, title only

### Structure

1. **Header**
   - Same as Original

2. **Summary**
   - Same as Original

3. **Skills**
   - Same as Original

4. **Key Achievements** _(replaces detailed Experience)_
   - Aggregated bullet points drawn from all roles, grouped by PM/delivery theme
   - Each bullet: bold skill/theme label, followed by detail and evidence
   - Each bullet: Should reference and project or company name in a way to indicate where the skill was employed.
   - Themes:
     - **Programme & Service Delivery:** TSA exit, separation programmes, cutover planning, operational readiness (from Worldpay, Shell, Costa)
     - **Stakeholder & Vendor Management:** Cross-functional coordination, senior stakeholder influence, SI/vendor alignment (from Worldpay, Shell, Estee Lauder)
     - **Agile & Roadmap Delivery:** Sprint cadences, backlog prioritisation, PI planning, roadmap execution (from Shell, Costa, Estee Lauder)
     - **Digital Transformation & Platform Rollout:** CMS, eCommerce, loyalty apps, POS integration, global platform rollouts (from Shell, Costa, Lodestone/Vodafone/GSK/Ricoh)
     - **Data, Governance & Compliance:** Azure DWH, GDPR migration, data pipelines, telemetry, governance frameworks (from Costa, Worldpay)
     - **UX & Conversion Optimisation:** UX roadmaps, modular design, checkout conversion, multi-brand delivery (from Estee Lauder)
     - **AI & Automation:** Microsoft 365 Copilot, AI/NLP automation, GenAI in delivery workflows (from Worldpay)
   - Each bullet should reference quantifiable outcomes where available from the original CV (e.g., 3% conversion uplift, 10M+ customers, 80% faster redaction)

5. **Experience Timeline** _(compact, bottom of CV)_
   - Section title: **Experience**
   - One line per role, format: **Role Title** | Company | Date Range
     - Delivery Lead | Worldpay | Nov 2024 - Aug 2025
     - Digital Project Manager | Estee Lauder | Nov 2023 - Oct 2024
     - Technical Product Manager / Delivery Manager | Shell | Apr 2022 - Oct 2023
     - Agile Project Manager / Product Owner | Costa Coffee | May 2019 - Mar 2022
     - Digital Transformation PM / BA | Lodestone Consulting | Jul 2012 - May 2019
     - ECommerce Consultant PM / BA | Various Clients | Prior

6. **Education**
   - Same as Original

7. **Certifications**
   - Same as Original

8. **Volunteering**
   - Same as Original

9. **Footer**
   - Same as Original

### Formatting Conventions
- Same as Original, plus:
- Bold used for theme labels in Key Achievements bullets
- Experience Timeline uses a minimal single-line-per-role format
- No per-role bullet points in the Experience Timeline — all detail lives in Key Achievements

---

## Two-Page Format

### What Changes vs Original
- **Skills** — expanded to 5 categories, adding AI Delivery & Governance
- **Experience** — full role detail retained across both pages, drawn from ArpitaNarula.md and enriched with SkillsLed content where richer
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

**Page 2** (insert `<div class="page-break"></div>` in markdown to force the break)
- Shell (full bullets)
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
   - After the Estee Lauder block, insert: `<div class="page-break"></div>`
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
- Job-specific files: `ArpitaNarula-TwoPage-<position>-<employer>-<mmmYY>.md`

### Formatting Conventions
- Same as Original
- No em-dash or en-dash
- Page break inserted with `<div class="page-break"></div>` on its own line in the markdown
- Present command to generate PDF as information : `python3 cv_to_pdf.py ArpitaNarula-TwoPage-<position>-<employer>-<mmmYY>.md.md /tmp/ArpitaNarula.pdf`

---

## Provider-Specific Guidance

### Claude (Anthropic)
**Strengths:** Deep context understanding, strict rule adherence, file handling
**Use for:** Primary generation, complex validation, multi-step reasoning

**Instructions:**
1. Provide the full CV-Generator.md as system context
2. Reference git commit hash of source files for version control
3. Use structured output with validation steps embedded
4. Leverage file tools (Read, Write, Edit) to maintain consistency
5. Request explicit confirmation before file modifications
6. Use TodoWrite for multi-step CV generation workflows

**Validation approach:**
- Built-in reasoning for gap analysis
- Cross-reference with Application Log automatically
- Flag adjacent terms with explicit user confirmation required
- Run rating checks before returning output

**Output expectations:**
- Detailed post-generation notes with rationale for changes
- Tabular format for skill/gap analysis
- Overall rating with improvement suggestions

---

### Gemini (Google)
**Strengths:** Fast iteration, visual analysis, structured outputs
**Use for:** Quick CV adaptations, keyword matching, format validation

**Instructions:**
1. Provide CV-Generator.md without full file context (Gemini has smaller context windows)
2. Break large tasks into smaller prompts:
   - First prompt: CV analysis against job spec
   - Second prompt: Skills/gaps identification
   - Third prompt: CV regeneration with rules applied
3. Use JSON/table format for structured outputs (Gemini excels here)
4. Explicitly remind on each prompt: strict rules from CV-Generator.md
5. Do NOT rely on Gemini to maintain multi-step state — re-state constraints in each prompt

**Validation approach:**
- Focus on keyword matching against job spec (Gemini's strength)
- Ask for rules compliance explicitly in each prompt
- Request formatted table outputs for gap analysis
- Ask for duplicate job detection by searching Application Log

**Output expectations:**
- Structured JSON or markdown tables
- Keyword analysis with match percentages
- Clear compliance checklist for each strict rule

---

### Copilot (Microsoft)
**Strengths:** Rapid prototyping, integration with Office/enterprise tools, format handling
**Use for:** Format-specific generation (DOCX, PDF optimization), real-time feedback

**Instructions:**
1. Provide CV-Generator.md in markdown blocks (Copilot handles markdown well)
2. Frame as a collaborative process (Copilot is conversational)
3. Ask for iterative feedback on:
   - Rule compliance (em-dash, comma usage, overlapping terminology)
   - Format validation (spacing, page breaks, bullet alignment)
   - Content tone (avoid overstating, maintain original meaning)
4. Use Copilot to generate PDF/DOCX-compatible markdown (handles formatting nuances)
5. Leverage Copilot's Office integration for final formatting polish

**Validation approach:**
- Detailed rule-by-rule compliance check requested explicitly
- Ask for visual format inspection (Copilot can simulate DOCX/PDF rendering)
- Request a "before/after" comparison with source template
- Use checklists for validation steps

**Output expectations:**
- Markdown optimized for DOCX/PDF conversion
- Format compliance report (spacing, indentation, page breaks)
- Rule adherence checklist with line-by-line cross-reference
- Tone/meaning preservation verification

---

## Cross-Provider Workflow

### When to use each provider:

| Task | Claude | Gemini | Copilot |
|------|--------|--------|---------|
| Full CV generation | ✓ Primary | ✓ Quick pass | ✓ Format pass |
| Gap analysis vs job spec | ✓ Deep | ✓ Keyword focus | ✓ Coverage check |
| Validation/compliance check | ✓ Comprehensive | ✓ Structured | ✓ Format/rules |
| Application Log search | ✓ Native | ⚠ Ask to search | ⚠ Manual input |
| Rating & recommendations | ✓ Full | ✓ Focused | ✓ Practical |
| PDF/DOCX optimization | ⚠ Basic | ⚠ Limited | ✓ Strong |

### Multi-Provider Sequence (Optional):

1. **Claude (Primary)** → Full CV generation with all validations
2. **Gemini (QA)** → Keyword matching against job spec (second opinion)
3. **Copilot (Format)** → Final format polish for PDF/DOCX export

---

## Prompt Templates by Provider

### Claude Prompt Template
```
You are a CV generator for Arpita Narula. Use CV-Generator.md as your system guide.

Task: Generate a CV for [Job Title] at [Company]

Job Spec: [paste job posting]
Source CV: [paste template: SkillsLed OR TwoPage]
Application Log: [paste relevant entries to check for duplicates]

Strict Rules (non-negotiable):
- Do not add new information not in source CV
- Maximum 3 overlapping terms with job spec in Summary
- No em-dashes or en-dashes
- Use " and" not ", and"
- Maintain original meaning in all bullets
- Contract roles use TwoPage format only

Steps:
1. Check for duplicate jobs in Application Log
2. Validate template choice (SkillsLed vs TwoPage)
3. Generate CV applying role-specific pivots
4. Validate against all strict rules
5. Provide gap analysis and rating
6. List any adjacent terms added (with justification)
7. Provide post-generation notes

Output: Generated CV + validation report + Application Log entry ready to insert
```

### Gemini Prompt Template
```
CV Generation Task for Arpita Narula

Job: [Job Title] at [Company]
Job Spec: [paste - focus on must-haves]

Source CV (latest): [paste template]

Strict rules to enforce:
- NO new info outside source CV
- Max 3 matching terms with job spec
- No em-dash or en-dash (use hyphens)
- Format: " and" not ", and"

Analysis needed:
1. Is there a duplicate job? [provide list of Job-* files to check]
2. Keyword match: Which 3 job-spec terms map to CV? [table format]
3. Gaps: What job-spec must-haves are missing? [table format]
4. Template: Should this be SkillsLed or TwoPage? [decision]
5. New content: Any terms to add beyond source? [list with source]

Output: keyword match table + gap analysis + template recommendation
```

### Copilot Prompt Template
```
I need to review a CV for formatting and rule compliance.

CV Generated: [paste generated CV]
Source Template: [paste template]

Compliance Checklist:
☐ No em-dashes or en-dashes (only hyphens)
☐ Uses " and" not ", and"
☐ Bullets match template meaning (no overstating)
☐ Page breaks correct (TwoPage format)
☐ Indentation and spacing consistent
☐ Contact line readable
☐ Skills section 5 categories (TwoPage) or 4 (SkillsLed)

Please:
1. Mark each checkbox as ✓ or ✗
2. Flag any format issues (spacing, alignment, bullets)
3. Verify tone: is anything overstated vs source template?
4. Suggest any DOCX/PDF compatibility improvements

Output: Compliance report + format recommendations + corrected markdown if needed
```

---

## Choosing Your Provider

| Need | Provider |
|------|----------|
| Full reasoning + validation | **Claude** |
| Quick keyword check | **Gemini** |
| Format excellence | **Copilot** |
| Complex multi-step | **Claude** |
| Simple single-pass | **Gemini** |
| Enterprise DOCX/PDF | **Copilot** |
