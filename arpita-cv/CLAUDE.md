# Arpita Narula - CV Generator Project

This repository contains CV generation workflows using specialized AI agents for Arpita Narula's job applications.

---

## Agent Configuration

### Primary Agent: CV Generator

```yaml
agent:
  name: cv-generator-claude
  description: Generate tailored CVs with strict rule compliance
  location: .claude/cv-generator-claude.md
  invoke: "@agent cv-generator-claude"
  model: haiku
  auto_load: true
  
  triggers:
    - pattern: "generate CV"
    - pattern: "create CV"
    - pattern: "@agent cv-generator"
    - command: "/cv-gen"
  
  context:
    reference_guide: CV-Generator.md
    source_cv: ArpitaNarula.md
    templates:
      - ArpitaNarula-SkillsLed.md
      - ArpitaNarula-TwoPage-Mar26.md
    application_log: ApplicationLog.md
    job_specs: Job-*.txt
  
  rules:
    - no_new_information_outside_source
    - max_3_overlapping_terms_in_summary
    - no_em_dashes_or_en_dashes
    - conjunction_format_and_not_comma_and
    - meaning_preserved_in_bullets
    - contract_roles_use_twopage_format
    - source_of_truth_never_modified
    - validation_before_output
  
  workflow_steps:
    1: pre_validation
    2: cv_generation
    3: validation
    4: gap_analysis
    5: deliverables
    6: confirmation
```

### Secondary Agent: Gemini (Keyword Analysis)

```yaml
agent:
  name: cv-generator-gemini
  description: Fast keyword analysis and gap assessment
  location: .claude/cv-generator-gemini.md
  invoke: "@agent cv-generator-gemini"
  model: gemini
  auto_load: false
  
  use_case: "Quick keyword matching without full CV generation"
  
  workflow_steps:
    1: job_spec_analysis
    2: keyword_to_cv_mapping
    3: summary_and_skills_pivots
    4: experience_bullet_reordering
    5: format_validation
```

### Format Validator: GitHub Copilot

```yaml
agent:
  name: github-copilot-cv-validator
  description: Format validation and DOCX/PDF optimization
  location: .github/copilot-instructions.md
  platform: github_copilot
  auto_load: true
  
  use_case: "Final format polish before saving"
  
  workflow_steps:
    1: pre_validation_checklist
    2: strict_rules_compliance
    3: format_and_spacing
    4: markdown_rendering
    5: docx_pdf_compatibility
    6: tone_and_meaning
    7: final_report
```

---

## Custom Agent: CV Generator

### Overview

The **CV Generator Agent** is a formal workflow for generating tailored CVs while maintaining strict compliance with rules defined in `CV-Generator.md`.

**Agent Location:** `.claude/cv-generator-claude.md`

### How to Use

#### Option A: Invoke Agent Directly (Recommended)
```
@agent cv-generator-claude

Generate CV for [Job Title] at [Company]

Job spec: [paste job description or reference Job-*.txt file]
```

#### Option B: Use as Shorthand
```
/cv-gen [job reference]

Example:
/cv-gen dcoded-TechDM
```

#### Option C: Full Workflow Request
```
I need to generate a CV for [Job Title].

Job file: Job-dcoded-TechDM.txt
Company: dcoded
Role: Technical Delivery Manager
Type: Contract (3 months)

Use the CV Generator Agent workflow:
1. Pre-validation (duplicate check)
2. CV generation (TwoPage format)
3. Validation (all 8 strict rules)
4. Gap analysis and rating
5. Application Log entry

Proceed with agent steps.
```

---

## Agent Workflow

The CV Generator Agent follows this sequence:

```
1. PRE-VALIDATION
   ├─ Check ApplicationLog.md for duplicates
   ├─ Confirm template (SkillsLed or TwoPage)
   ├─ Analyze job spec (must-haves, keywords, overlaps)
   └─ Recommend format (contract → TwoPage)

2. CV GENERATION
   ├─ Read ArpitaNarula.md (source of truth)
   ├─ Read template (SkillsLed or TwoPage)
   ├─ Update Summary (job-relevant language)
   ├─ Update Skills (reorder/rephrase)
   ├─ Update Experience (reorder bullets)
   └─ Preserve all other sections

3. VALIDATION
   ├─ No new information (cross-check vs source)
   ├─ Overlapping terms ≤3 in Summary
   ├─ No em-dashes or en-dashes
   ├─ " and" not ", and"
   ├─ Meaning preserved in all bullets
   ├─ Skills count correct (4 or 5)
   └─ Contract roles use TwoPage format

4. GAP ANALYSIS
   ├─ Job-spec must-haves NOT in CV
   ├─ Adjacent terms flagged
   ├─ Fit rating (X/10)
   └─ Suggested bridging language

5. DELIVERABLES
   ├─ CV markdown file: ArpitaNarula-[Format]-[Position]-[Company]-[MMMYY].md
   ├─ Validation report (checklist + gaps + rating)
   ├─ Application Log entry (formatted, ready to insert)
   └─ Post-generation notes (rationale for pivots)

6. CONFIRMATION
   └─ User approves before saving files
```

---

## Example Agent Invocations

### Example 1: dcoded Technical Delivery Manager
```
@agent cv-generator-claude

Job: Technical Delivery Manager (dcoded)
Company: dcoded (fintech B Corp)
Type: Contract (3 months, outside IR35)
Location: Remote-first + occasional Manchester travel
Source: Job-dcoded-TechDM.txt

Key Focus:
- Multi-squad delivery across large-scale technical programmes
- Delivery planning, roadmaps, and forecasting
- Governance, risk management, and reporting
- Senior stakeholder influence
- Fintech/regulated environment

Generate CV with full validation report and Application Log entry.
```

### Example 2: Quick Reference
```
/cv-gen dcoded-TechDM

(Agent will:
- Look up Job-dcoded-TechDM.txt
- Detect contract role → use TwoPage format
- Generate CV with validation
- Provide Application Log entry)
```

### Example 3: With Custom Emphasis
```
@agent cv-generator-claude

Generate CV for [Role] at [Company]

Job spec: [pasted]

Custom instructions:
- Emphasize: [specific keywords from job]
- Bridge gaps with: [specific CV experience]
- Adjacent term approval: Yes (I approve adding: [term])

Proceed with workflow.
```

---

## Strict Rules (All Agent Operations)

The agent enforces these rules on every CV generation:

1. **No new information** — Only from ArpitaNarula.md or templates
2. **Overlapping terms** — Max 3 matching job spec terms in Summary
3. **No em/en-dashes** — Only hyphens (-) allowed
4. **Conjunction format** — " and" not ", and"
5. **Meaning preserved** — Bullets maintain original scope
6. **Contract format** — Contract roles always use TwoPage
7. **Source of truth** — ArpitaNarula.md never modified
8. **Validation before output** — All checks run before returning CV

See `CV-Generator.md` for full guidance.

---

## File Structure

```
ArpitaCV/
├── CLAUDE.md                           ← You are here (agent definitions)
├── CV-Generator.md                     ← Master guide (all rules)
├── ArpitaNarula.md                     ← Source of truth CV
├── ArpitaNarula-SkillsLed.md          ← Template (compact)
├── ArpitaNarula-TwoPage-Mar26.md      ← Template (detailed)
├── ApplicationLog.md                   ← Track all applications
├── Job-*.txt / Job-*.md               ← Individual job specs
├── ArpitaNarula-[Format]-[Role]-[Company]-[Date].md  ← Generated CVs
├── CoverLetter-*.md                   ← Cover letters
├── .github/
│   └── copilot-instructions.md        ← GitHub Copilot instructions (format validation)
└── .claude/agents/
    ├── cv-generator-claude.md         ← Claude agent (primary)
    ├── cv-generator-gemini.md         ← Gemini agent (keyword analysis)
    └── README.md                      ← Agent overview
```

---

## Secondary Agents

### Gemini Agent (Keyword Analysis)
Use for quick keyword matching and gap assessment without full CV generation.

Location: `.claude/cv-generator-gemini.md`

**Invocation:**
```
Analyze job spec keywords and provide gap assessment.

Job spec: [pasted]
Source CV template: ArpitaNarula-TwoPage-Mar26.md

Use Gemini agent workflow:
1. Job spec analysis (keywords, must-haves, overlaps)
2. Keyword-to-CV mapping
3. Summary & Skills pivots
4. Experience bullet reordering
5. Format validation
```

### GitHub Copilot (Format Validation)
Use for final format polish before saving.

Location: `.github/copilot-instructions.md`

**Note:** GitHub Copilot reads this file automatically from the repository.

---

## Quick Start

### Generate CV for a Job

1. **Have job spec ready** (Job-*.txt file or pasted text)
2. **Invoke agent:**
   ```
   @agent cv-generator-claude
   
   Generate CV for [Job Title] at [Company]
   Job spec: [reference or paste]
   ```
3. **Agent delivers:**
   - CV markdown file
   - Validation report
   - Application Log entry (ready to copy)
4. **Approve:** Confirm format looks good
5. **Save:** Agent saves files when you approve

### Check Job Fit Without Generating CV

```
@agent cv-generator-gemini

Analyze fit for [Job Title]
Job spec: [pasted]
Use Gemini workflow for keyword analysis.
```

### Polish CV Format

```
@agent github-copilot (or use .github/copilot-instructions.md)

Validate CV format and prepare for export.
CV: [filename]
```

---

## Configuration

### Agent Permissions in settings.json

The following permissions are configured in `settings.json`:

```json
{
  "permissions": {
    "additionalDirectories": [
      ".claude"
    ]
  },
  "model": "haiku"
}
```

This allows agent files to be accessed and loaded.

### Register Agents in settings.json (Optional)

For more formal agent registration, add to `settings.json`:

```json
{
  "agents": {
    "cv-generator": {
      "file": ".claude/cv-generator-claude.md",
      "description": "Generate tailored CVs with strict rule compliance",
      "model": "haiku",
      "auto_load": true,
      "context": {
        "reference_guide": "CV-Generator.md",
        "source_cv": "ArpitaNarula.md",
        "application_log": "ApplicationLog.md"
      }
    },
    "cv-validator": {
      "file": ".claude/cv-generator-gemini.md",
      "description": "Keyword analysis and gap assessment",
      "model": "gemini",
      "auto_load": false
    }
  },
  "hooks": {
    "on_command": {
      "/cv-gen": {
        "agent": "cv-generator",
        "description": "Shorthand for CV generation"
      }
    }
  },
  "permissions": {
    "additionalDirectories": [
      ".claude"
    ]
  },
  "model": "haiku"
}
```

### How to Add This Configuration

**Step 1:** Use the `update-config` skill
```
/update-config

Add agents section to settings.json with cv-generator and cv-validator agents
```

**Step 2:** Or edit settings.json manually
```bash
# Open settings file
open /Users/sandeep/.claude/settings.json

# Add the "agents" and "hooks" sections from above
```

### Model Selection

- **Default:** Haiku (fast, cost-effective, suitable for CV work)
- **For complex analysis:** Sonnet (`model: sonnet`)
- **For deep reasoning:** Opus (`model: opus`)
- **For keyword analysis:** Gemini (`model: gemini`)

Override per invocation:
```
@agent cv-generator-claude (model: sonnet)
```

---

### Environment Variables

(Optional) Set CV generator defaults:

```bash
# In .env or shell
export CV_GENERATOR_TEMPLATE="TwoPage"        # Default format
export CV_GENERATOR_MODEL="haiku"             # Default model
export CV_APPLICATION_LOG="ApplicationLog.md" # Tracking file
export CV_SOURCE="ArpitaNarula.md"            # Source CV
```

---

## Tips & Best Practices

1. **Always reference Job-*.txt files** — Keeps jobs organized and searchable
2. **Use agent checklist** — Ensure all deliverables before saving
3. **Approve adjacent terms** — Agent flags new terminology for confirmation
4. **Keep ApplicationLog.md updated** — Duplicate detection depends on it
5. **Reference CV-Generator.md** — When you need to understand the rules
6. **Save validation reports** — Keep for post-application review

---

## Support

- **Rules & Guidance:** See `CV-Generator.md`
- **Agent Workflow:** See `.claude/cv-generator-claude.md`
- **Job Specifications:** See `Job-*.txt` or `Job-*.md` files
- **Application History:** See `ApplicationLog.md`

---

---

## Setup Checklist

### Required Files (Already Created ✓)

- [x] `/Users/sandeep/Documents/multani-sandeep/ArpitaCV/CLAUDE.md` — Agent definitions (this file)
- [x] `.claude/cv-generator-claude.md` — Primary agent
- [x] `.claude/cv-generator-gemini.md` — Secondary agent
- [x] `.claude/agents-README.md` — Agent overview
- [x] `/Users/sandeep/Documents/multani-sandeep/ArpitaCV/CV-Generator.md` — Master guide
- [x] `/Users/sandeep/Documents/multani-sandeep/ArpitaCV/.github/copilot-instructions.md` — GitHub Copilot config

### Optional: Formal Agent Registration

**Option A: Use `update-config` Skill** (Recommended)
```
/update-config

Task: Register CV generator agents in settings.json

Add to settings.json:
- agents section with cv-generator and cv-validator
- hooks section with /cv-gen command
- Reference CLAUDE.md for exact config
```

**Option B: Manual Edit**
```
1. Open /Users/sandeep/.claude/settings.json
2. Add "agents" section (see Configuration section above)
3. Add "hooks" section (see Configuration section above)
4. Save and reload
```

**Option C: Just Use It (Minimal Setup)**
```
@agent cv-generator-claude

Generate CV for [Job Title] at [Company]
Job spec: [pasted or referenced]
```

This works immediately without additional configuration.

---

## Quick Start: First CV Generation

### 1. Load Agent
```
@agent cv-generator-claude
```

### 2. Provide Job Details
```
Generate CV for Technical Delivery Manager at dcoded.

Job spec: Job-dcoded-TechDM.txt
Key focus: Multi-squad delivery, governance, technical leadership
```

### 3. Agent Executes
- Checks for duplicates
- Selects TwoPage format (contract)
- Generates CV
- Validates all rules
- Provides Application Log entry

### 4. Review & Approve
```
User: Looks good, save it
Agent: Files saved + AppLog entry ready to copy
```

### 5. Copy to ApplicationLog.md
Paste the provided entry into `ApplicationLog.md` to track the application.

---

## Troubleshooting

### "Agent file not found"
```
Solution: Verify path in CLAUDE.md matches actual file location:
.claude/cv-generator-claude.md
```

### "Agent doesn't load automatically"
```
Solution: Either:
1. Use @agent cv-generator-claude (explicit invocation)
2. Register in settings.json with auto_load: true (see Configuration)
```

### "CV-Generator.md rules not being enforced"
```
Solution: Agent reads CV-Generator.md on startup.
Verify:
- CV-Generator.md exists in repository root
- Agent has read access to CV-Generator.md
- Use @agent cv-generator-claude to reload
```

### "Model doesn't exist (e.g., 'gemini')"
```
Solution: Gemini agent uses text-based structured output instead.
Change model in cv-generator-gemini.md:
model: haiku (works for Gemini workflow)
```

---

Last Updated: 2026-04-17
**Agent Configuration Version:** 1.0
