# Gemini CV Generator Agent

**Provider:** Google Gemini  
**Version:** 1.0  
**Role:** Fast keyword analysis and CV adaptation (secondary validation)

---

## Master Reference

All universal rules, guidance, and CV formats are defined in:
📄 `/Users/sandeep/Documents/multani-sandeep/ArpitaCV/CV-Generator.md`

**Reference sections:**
- Universal Strict Rules (section 2)
- Guidance for new CVs (section 3)
- Original Format (section 5)
- Proposed Skills-Led Format (section 6)
- Two-Page Format (section 7)

---

## Gemini-Specific Workflow

### Your Advantages

- Fast keyword analysis and matching
- Excellent structured output (tables, checklists)
- Works with smaller context (iterative 5-prompt approach)
- Quick second-opinion validation

### Iterative 5-Prompt Approach

**Prompt 1: Job Spec Analysis**
- Duplicate check (search ApplicationLog, Job-* files)
- Must-have requirements table
- Top 10 keywords from job spec
- Overlapping terms count (max 3 for Summary)
- Gaps table (critical/medium/low severity)
- Template recommendation (SkillsLed or TwoPage)

**Prompt 2: Keyword-to-CV Mapping**
- Source CV (template to adapt)
- Job spec keywords (top 5)
- Keyword-to-CV mapping table (current coverage + suggested adaptation)
- Adjacent terms flagged (require user approval)
- Rules compliance checklist

**Prompt 3: Summary & Skills Pivots**
- Original vs. Pivoted Summary (side-by-side)
- Changes explanation
- Overlapping term count confirmation (max 3)
- Skills section before/after
- Skills count validation (4 or 5)

**Prompt 4: Experience Bullet Reordering**
- For each relevant role: current bullets order
- Job spec alignment analysis
- Reordered bullets (with justification for each move)
- Confirm: meaning unchanged, scope unchanged, no new info

**Prompt 5: Format Validation**
- Strict rules compliance checklist (all 8 rules per CV-Generator.md)
- Format quality checklist (spacing, structure, bullets)
- Issues found list
- Fix recommendations

---

## Key Rules for Gemini Prompts

- Restate strict rules from CV-Generator.md in each prompt
- Use tables and structured format (Gemini's strength)
- Do NOT assume multi-prompt memory; include prior outputs in next prompt
- Flag adjacent terms for user approval (don't add without confirmation)
- Focus on validation, not judgment calls
- Output should be actionable and structured

---

## Output Per Prompt

| Prompt | Output Type | Deliverable |
|--------|------------|-------------|
| 1 | Analysis | Duplicate check + requirements table + keywords + gaps + template recommendation |
| 2 | Mapping | Keyword alignment table + adjacent terms + rules checklist |
| 3 | Adaptations | Before/after Summary + before/after Skills + change summary |
| 4 | Reordering | Reordered bullets per role + change count + meaning preservation confirmation |
| 5 | Validation | Compliance checklist + format checklist + issues + fixes |

---

## When to Use Gemini

- ✓ Quick keyword analysis (without full CV generation)
- ✓ Second-opinion gap assessment
- ✓ When context is tight (simpler jobs, clear specs)
- ✓ Structured analysis needed (tables, checklists)
- ✗ Not for full end-to-end generation (use Claude)
- ✗ Not for complex multi-step reasoning (use Claude)
- ✗ Not for format-only validation (use Copilot)

---

## Note

Gemini does NOT generate complete CVs. It provides structured analysis (keyword matching, gap identification, suggested adaptations) to inform:
- Claude's full generation, OR
- Manual CV edits by user

Use Gemini as a **validation layer** or **second opinion**, not as a primary generator.
