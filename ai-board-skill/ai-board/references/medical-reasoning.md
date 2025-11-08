# Medical Reasoning Framework

This reference provides clinical decision support protocols optimized for hematology and oncology, Jordan's specialty.

## Clinical Reasoning Structure

### Phase 1: Case Presentation

Structure information systematically:

**Patient presentation**:
- Demographics and relevant history
- Chief complaint and timeline
- Key physical findings
- Laboratory/imaging results
- Current medications and treatments

**Missing information to identify**:
- What additional data would strengthen the analysis?
- What tests should be ordered?
- What historical details are critical?

### Phase 2: Differential Diagnosis

**Generate comprehensive differentials**:
1. Primary working diagnosis (most likely)
2. Alternative diagnoses (cannot rule out)
3. Must-not-miss diagnoses (low probability but critical)

**For oncology cases**:
- Cancer type and stage considerations
- Histopathology and molecular markers
- Treatment response scenarios
- Complications (disease-related vs treatment-related)

**For hematology cases**:
- CBC abnormality patterns
- Coagulation disorders
- Hemolytic vs production disorders
- Bone marrow pathology considerations

### Phase 3: Evidence-Based Analysis

**Evaluate each diagnosis**:

**Supporting evidence**:
- Clinical findings that support
- Laboratory/imaging consistent with
- Risk factors present
- Epidemiological likelihood

**Contradicting evidence**:
- Findings that argue against
- Atypical features
- Temporal inconsistencies

**Evidence quality levels**:
- Level 1: Systematic reviews, meta-analyses, RCTs
- Level 2: Well-designed cohort studies
- Level 3: Case-control studies
- Level 4: Case series
- Level 5: Expert opinion

### Phase 4: Management Options

**For oncology treatment decisions**:

**Treatment modalities**:
1. **Surgery**: Resectability, surgical candidates
2. **Radiation**: Indications, dose, technique
3. **Systemic therapy**:
   - Chemotherapy (regimens, cycles)
   - Targeted therapy (molecular targets)
   - Immunotherapy (checkpoint inhibitors, CAR-T)
   - Hormone therapy (receptor status)

**Treatment sequencing**:
- Neoadjuvant vs adjuvant
- First-line, second-line options
- Maintenance therapy
- Clinical trial eligibility

**For hematologic disorders**:

**Acute management**:
- Transfusion thresholds
- Coagulation support
- Emergency interventions

**Long-term management**:
- Disease-modifying agents
- Supportive care
- Monitoring protocols

### Phase 5: Risk-Benefit Analysis

**For each management option, evaluate**:

**Benefits (efficacy)**:
- Response rates (ORR, CR, PR)
- Survival metrics (OS, PFS, DFS)
- Quality of life improvements
- Symptom control

**Risks (toxicity)**:
- Common side effects (grade 1-2)
- Serious adverse events (grade 3-4)
- Long-term complications
- Treatment-related mortality

**Patient-specific factors**:
- Performance status (ECOG, Karnofsky)
- Comorbidities
- Age and functional status
- Patient preferences and goals

**Practical considerations**:
- Cost and insurance coverage
- Treatment burden (frequency, duration)
- Support systems available
- Distance to treatment center

### Phase 6: Recommendation

**Structure recommendations**:

```
RECOMMENDATION: [Primary management approach]

RATIONALE:
- [Key evidence supporting this approach]
- [Why this is preferred over alternatives]
- [Evidence level: I, II, or III]

ALTERNATIVE OPTIONS:
1. [Second choice] - Consider if [specific circumstances]
2. [Third choice] - Consider if [specific circumstances]

MONITORING:
- [What to monitor and when]
- [Response assessment timing]
- [Toxicity surveillance]

NEXT STEPS:
1. [Immediate actions]
2. [Short-term follow-up]
3. [Long-term plan]

CONFIDENCE LEVEL: [High 90-95% / Moderate 75-89% / Lower <75%]
- Increasing confidence: [factors]
- Decreasing confidence: [uncertainties]
- Additional information needed: [what would help]
```

## Oncology-Specific Protocols

### Checkpoint Inhibitor Therapy

**Indications** (tumor-specific):
- Melanoma: PD-1/PD-L1 inhibitors (pembrolizumab, nivolumab)
- NSCLC: PD-1/PD-L1 ± chemotherapy
- RCC: PD-1 + CTLA-4 or PD-1 + TKI
- Head/neck: Pembrolizumab
- Bladder: PD-1/PD-L1 inhibitors
- MSI-H/dMMR tumors: Pembrolizumab (tissue-agnostic)

**Biomarkers**:
- PD-L1 expression (TPS, CPS)
- TMB (tumor mutational burden)
- MSI/dMMR status
- Other emerging markers

**Management considerations**:
- Immune-related adverse events (irAEs)
- Corticosteroid management protocols
- When to hold vs rechallenge
- Duration of therapy

### Hematologic Malignancies

**Acute leukemias**:
- Induction chemotherapy protocols
- Consolidation strategies
- Transplant candidacy
- Targeted therapies (FLT3, IDH)

**Lymphomas**:
- R-CHOP and variants
- Salvage regimens
- CAR-T cell therapy eligibility
- Maintenance rituximab

**Multiple myeloma**:
- Triplet/quadruplet induction
- Transplant-eligible vs ineligible
- Novel agents (PI, IMiD, anti-CD38)
- Maintenance strategies

## Clinical Guidelines Integration

**Always reference current guidelines**:
- NCCN (National Comprehensive Cancer Network)
- ASCO (American Society of Clinical Oncology)
- ASH (American Society of Hematology)
- ESMO (European Society for Medical Oncology)

**Note guideline version and date**: Guidelines are regularly updated; specify which version you're referencing

**Flag off-guideline recommendations**: If recommending outside standard guidelines, explicitly state rationale and evidence

## Multi-Agent Configuration for Medical Cases

**Optimal 5-agent setup**:

1. **Primary Oncologist/Hematologist**:
   - Generates main clinical assessment
   - Proposes primary management plan
   - Integrates all perspectives

2. **Subspecialist** (if applicable):
   - Disease-specific expertise
   - Specialized treatment knowledge
   - Novel therapy awareness

3. **Evidence Reviewer**:
   - Literature review
   - Guideline interpretation
   - Trial data analysis

4. **Devil's Advocate**:
   - Challenges differential diagnosis
   - Questions treatment assumptions
   - Identifies potential complications
   - Tests edge cases

5. **Risk/Ethics Assessor**:
   - Patient-centered considerations
   - Quality of life focus
   - Ethical implications
   - Goals of care alignment

## Confidence Calibration in Medicine

**High confidence (90-95%)**:
- Well-established diagnoses with classic presentation
- Standard-of-care treatments with robust Level 1 evidence
- Clear guideline recommendations

**Moderate confidence (75-89%)**:
- Atypical presentations of common conditions
- Treatment approaches with Level 2-3 evidence
- Guidelines with conditional recommendations

**Lower confidence (<75%)**:
- Rare presentations or diagnoses
- Novel therapies with limited data
- Off-label uses without strong evidence
- Complex cases with complicating factors

**Acknowledge uncertainty explicitly**:
- "This presentation is most consistent with X, though Y cannot be ruled out"
- "Current evidence suggests [treatment], though data is limited for this specific scenario"
- "Additional testing with [specific test] would significantly improve diagnostic certainty"

## Red Flags Requiring Explicit Acknowledgment

**Always acknowledge**:
- Recommendations diverging from standard guidelines
- Novel therapies without long-term safety data
- Off-label uses
- Patient-specific factors that complicate standard approach
- Significant treatment risks or potential complications

**Never suggest**:
- Specific dosing without disclaimer (complex calculations require verification)
- Medication changes without consulting prescribing physician
- Delaying emergency care for non-urgent workup

## Quality Assurance

**Every medical recommendation should include**:
✅ Evidence basis (cite guidelines, trials, or mark as expert opinion)
✅ Confidence level with rationale
✅ Alternative options considered
✅ Patient-specific considerations
✅ Monitoring plan
✅ What would change the recommendation
✅ When to seek additional consultation

**Clinical reasoning checklist**:
✅ Did I consider the full differential?
✅ Did I identify must-not-miss diagnoses?
✅ Is my recommendation evidence-based?
✅ Did I assess risk vs benefit?
✅ Did I account for patient-specific factors?
✅ Did I acknowledge uncertainties?
✅ Is my confidence calibrated appropriately?
