# CV Generator Agents

Multi-provider agents for generating tailored CVs for Arpita Narula.

**Master Reference:** All universal rules, guidance, and CV formats are defined in:
📄 `/Users/sandeep/Documents/multani-sandeep/ArpitaCV/CV-Generator.md`

Each agent references CV-Generator.md instead of duplicating content. Agents only contain provider-specific instructions and workflows.

---

## Agents

### 1. **Claude Agent** (`cv-generator-claude.md`)

**Provider:** Anthropic Claude  
**Role:** Primary CV generation with comprehensive validation  
**Use for:** Full end-to-end CV generation, complex multi-step reasoning

**Strengths:**
- Deep context understanding
- Strict rule adherence
- Built-in validation and gap analysis
- File handling and git version control
- Can maintain complex multi-step state

**Typical workflow:**
1. Copy `cv-generator-claude.md` as system prompt
2. Provide job spec + source CV + ApplicationLog
3. Claude generates complete CV + validation report
4. Claude provides Application Log entry ready to insert

**Output:**
- Complete CV markdown file
- Detailed validation report with gap analysis and rating
- Application Log entry (formatted and ready)
- Post-generation notes with rationale

---

### 2. **Gemini Agent** (`cv-generator-gemini.md`)

**Provider:** Google Gemini  
**Role:** Fast keyword analysis and CV adaptation (secondary validation)  
**Use for:** Quick keyword matching, second-opinion gap analysis

**Strengths:**
- Fast iteration with structured outputs
- Excellent at keyword matching and tables
- Works well with smaller context windows (iterative prompts)

**Typical workflow:**
1. **Prompt 1:** Job spec analysis (duplicate check, keywords, gaps)
2. **Prompt 2:** Keyword-to-CV mapping (which CV content aligns with job spec)
3. **Prompt 3:** Summary & Skills adaptations (before/after comparison)
4. **Prompt 4:** Experience bullet reordering (with justification)
5. **Prompt 5:** Format validation (checklist-based compliance)

**Output:**
- Keyword analysis tables
- Gap identification (critical/medium/low severity)
- Content adaptation suggestions (structured)
- Format validation checklist

**Note:** Gemini doesn't generate full CVs; it provides structured analysis to inform Claude or manual CV generation.

---

### 3. **GitHub Copilot Instructions** (`.github/copilot-instructions.md`)

**Provider:** Microsoft GitHub Copilot  
**Location:** In repository (for GitHub Copilot to access)  
**Role:** Format validation and DOCX/PDF optimization (final polish)  
**Use for:** Format compliance check, visual rendering validation, export preparation

**File location:**
📄 `/Users/sandeep/Documents/multani-sandeep/ArpitaCV/.github/copilot-instructions.md`

**Strengths:**
- Conversational, iterative process
- Format and spacing validation
- DOCX/PDF export preparation
- Visual rendering simulation
- Tone and meaning preservation check

**Typical workflow:**
1. Pre-format validation checklist
2. Strict rules compliance check (8 rules, all pass/fail)
3. Format & spacing validation (structure, bullets, indentation)
4. Markdown rendering preview (how it looks in Word)
5. DOCX/PDF compatibility check
6. Tone & meaning verification
7. Final compliance report

**Output:**
- Format validation checklist (strict rules)
- Format quality report (spacing, structure)
- DOCX/PDF compatibility assessment
- Tone preservation verification
- Export recommendations

**Note:** GitHub Copilot accesses this file via `.github/copilot-instructions.md` in the repository. It's separate from Claude Code agents.

---

## Usage Patterns

### Pattern 1: Full Claude (Recommended for most jobs)
```
User: Generate CV for [Job]
Claude: Full generation + validation + Application Log entry
```

### Pattern 2: Claude + Gemini (Keyword second-opinion)
```
User: Generate CV for [Job]
Claude: Full generation + validation
Gemini: Keyword analysis + gap check (optional second pass)
```

### Pattern 3: Claude + Copilot (Format polish)
```
User: Generate CV for [Job]
Claude: Full generation + validation
Copilot: Format validation + DOCX/PDF prep
```

### Pattern 4: Gemini only (Quick analysis)
```
User: Is my CV a good fit for [Job]?
Gemini: Keyword analysis + gap assessment (no new CV generated)
```

### Pattern 5: Copilot only (Format review)
```
User: Check this CV for formatting issues
Copilot: Format validation + export recommendations
```

---

## Strict Rules (All Agents Enforce)

1. **No new information** — Content must be from ArpitaNarula.md or templates
2. **Overlapping terms** — Max 3 matching job spec terms in Summary
3. **No em/en-dashes** — Only hyphens (-) allowed
4. **Conjunction format** — " and" not ", and"
5. **Meaning preserved** — Bullets maintain original scope
6. **Contract format** — Contract roles use TwoPage format only
7. **Source of truth** — ArpitaNarula.md never modified
8. **Validation before output** — All checks run before returning CV

---

## File Locations

**Claude Code Agents** (`.claude/`):
- `cv-generator-claude.md` — Primary generation
- `cv-generator-gemini.md` — Keyword analysis

**GitHub Copilot Instructions** (in repository):
- `.github/copilot-instructions.md` — Format validation

**Master Reference** (in repository):
- `CV-Generator.md` — All universal rules and guidance
- `ArpitaNarula.md` — Source of truth CV
- `ArpitaNarula-SkillsLed.md` — Template (compact)
- `ArpitaNarula-TwoPage-Mar26.md` — Template (detailed)
- `ApplicationLog.md` — Track applications
- `Job-*.md` — Job specifications

---

## Quick Decision Tree

| Scenario | Use Agent |
|---|---|
| Need full CV generated | **Claude** |
| Want keyword check only | **Gemini** |
| Want format polished | **Copilot** |
| Want full pipeline | **Claude → Gemini → Copilot** |
| Unsure about job fit | **Gemini** (analysis only) |
| CV ready, just format check | **Copilot** |
| Complex role, many gaps | **Claude** (detailed reasoning) |
| Simple role, clear spec | **Gemini** (faster) |

---

## How to Invoke Each Agent

### Claude (in Claude Code)
Use as system prompt or provide the file as context.

### Gemini (via Google)
Copy each prompt template from `cv-generator-gemini.md` and run iteratively.

### Copilot (in Microsoft Teams or web)
Paste the content or copy sections from `cv-generator-copilot.md` and work conversationally.

---

## Versioning

- **Agent version:** 1.0 (all agents)
- **CV-Generator.md:** Source of truth for all rules and guidance
- **Last updated:** 2026-04-17

All agents reference the same strict rules and comply with the same standards.
