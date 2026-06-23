# Arpita Narula - CV Generator Project

This repository contains CV generation workflows for Arpita Narula's job applications.

**Master guide:** `CV-Generator.md` — all rules, formats and generation logic live there. Read it before doing anything.

---

## How to Generate a CV

Just describe the job to Claude in natural language:

```
Generate CV for [Job Title] at [Company]

Job spec: [paste job description or reference Job-*.txt file]
```

Claude will follow the workflow in CV-Generator.md automatically:
1. Pre-validation (duplicate check against ApplicationLog.md)
2. Fit assessment (rating, challenge areas, recommendation) — waits for your confirmation
3. CV generation (only after you confirm)
4. Post-generation validation
5. Deliverables (CV file, validation report, Application Log entry)
6. Confirmation before saving files

---

## Workflow Summary

```
1. PRE-VALIDATION
   ├─ Check ApplicationLog.md for duplicates (stop if found)
   ├─ Confirm template (TwoPage — SkillsLed retired May 2026)
   └─ Recommend format (contract → TwoPage)

2. FIT ASSESSMENT (before generating anything)
   ├─ Extract must-have requirements from job spec
   ├─ Rate each must-have: Strong / Partial / Gap
   ├─ Score overall fit (X/10) with one-line rationale
   ├─ List challenge areas: bridgeable gaps vs hard gaps
   ├─ Recommendation: proceed / proceed with caveats / do not proceed
   └─ STOP — wait for user confirmation before generating CV

3. CV GENERATION (only after user confirms)
   ├─ Read ArpitaNarula.md (source of truth)
   ├─ Read ArpitaNarula-TwoPage-Mar26.md (template)
   ├─ Update Summary (job-relevant language)
   ├─ Update Skills (reorder/rephrase)
   ├─ Update Experience (reorder bullets)
   └─ Preserve all other sections unchanged

4. POST-GENERATION VALIDATION
   ├─ No new information (cross-check vs source)
   ├─ Overlapping terms ≤3 in Summary
   ├─ No em-dashes or en-dashes
   ├─ " and" not ", and"
   ├─ Meaning preserved in all bullets
   ├─ Skills count correct (5 in TwoPage)
   ├─ Skills not more than 10% different from template
   └─ Contract roles use TwoPage format

5. DELIVERABLES
   ├─ CV markdown file: CV-[position]-[employer]-[mmmYY].md
   ├─ Validation report (checklist + gaps + rating)
   ├─ Application Log entry (formatted, ready to insert)
   └─ Post-generation notes (rationale for pivots, adjacent terms flagged)

6. CONFIRMATION
   └─ User approves before saving files
```

---

## Strict Rules

1. **No new information** — only from ArpitaNarula.md or templates
2. **Overlapping terms** — max 3 matching job spec terms in Summary
3. **No em/en-dashes** — only hyphens (-) allowed
4. **Conjunction format** — " and" not ", and"
5. **Meaning preserved** — bullets maintain original scope
6. **Contract format** — contract roles always use TwoPage
7. **Source of truth** — ArpitaNarula.md never modified
8. **Fit assessment first** — rating and user confirmation before CV is generated

See `CV-Generator.md` for full rules and format guidance.

---

## File Structure

```
arpita-cv/
├── CLAUDE.md                              ← You are here
├── CV-Generator.md                        ← Master guide (all rules)
├── ArpitaNarula.md                        ← Source of truth CV (never modified)
├── ArpitaNarula-TwoPage-Mar26.md         ← Active template
├── ApplicationLog.md                      ← Track all applications
├── Job-*.txt / Job-*.md                  ← Individual job specs
├── CV-[position]-[employer]-[mmmYY].md   ← Generated CVs
├── CoverLetter-*.md                      ← Cover letters
├── PrepsDebriefs/                        ← Interview prep and debriefs
│   ├── Consolidated-InterviewLearnings-Jun26.md
│   ├── JobHuntAnalysis-Jun25-Jun26.md
│   └── Prep-*.md / Interview-*-Debrief.md
└── .github/
    └── copilot-instructions.md           ← GitHub Copilot format validation
```

---

## Tips

1. Always reference Job-*.txt files — keeps jobs organised and searchable
2. Approve adjacent terms explicitly — Claude flags new terminology for confirmation before adding
3. Keep ApplicationLog.md updated — duplicate detection depends on it
4. If fit rating is below 7.5/10, discuss before proceeding — a weak application wastes time
5. Save validation reports — useful for post-application review

---

Last Updated: June 2026
