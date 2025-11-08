#!/usr/bin/env python3
"""
Tumor Board Simulator - Multi-Specialty Clinical Analysis

Orchestrates multiple specialty perspectives for comprehensive case analysis.
Each specialty independently evaluates the case, then deliberates to consensus.
"""

import json
import sys
from typing import Dict, List, Any
from pathlib import Path


TUMOR_BOARD_SPECIALTIES = {
    "medical_oncologist": {
        "name": "Medical Oncologist",
        "focus": "Systemic therapy selection, treatment sequencing, toxicity management, supportive care",
        "key_questions": [
            "What is the optimal systemic therapy regimen?",
            "Are there targeted therapies or immunotherapies indicated?",
            "What is the expected benefit vs toxicity profile?",
            "Should this be neoadjuvant, adjuvant, or definitive treatment?",
            "Are there clinical trials this patient should be considered for?"
        ]
    },
    "radiation_oncologist": {
        "name": "Radiation Oncologist",
        "focus": "Role of radiation therapy, treatment volume, dose-fractionation, sequencing with systemic therapy",
        "key_questions": [
            "Is radiation therapy indicated?",
            "What is the appropriate radiation dose and fractionation?",
            "Should RT be given concurrently or sequentially with chemo?",
            "What are the expected acute and late toxicities?",
            "Are there critical structures that limit dosing?"
        ]
    },
    "pathologist": {
        "name": "Pathologist",
        "focus": "Diagnostic accuracy, histologic subtyping, immunohistochemistry, molecular features, prognostic markers",
        "key_questions": [
            "Is the diagnosis confirmed with adequate tissue?",
            "What is the precise histologic subtype?",
            "What IHC stains or molecular tests are needed?",
            "Are there prognostic or predictive biomarkers?",
            "Is the grading and staging accurate?"
        ]
    },
    "radiologist": {
        "name": "Radiologist",
        "focus": "Staging accuracy, response assessment, differential diagnosis, detection of complications",
        "key_questions": [
            "Is the staging complete and accurate?",
            "Are there alternative diagnoses to consider?",
            "What imaging should be used for response assessment?",
            "Are there concerning findings requiring urgent intervention?",
            "Is biopsy guidance needed for diagnosis?"
        ]
    },
    "surgical_oncologist": {
        "name": "Surgical Oncologist",
        "focus": "Resectability, surgical approach, timing of surgery, margin adequacy, procedural risk",
        "key_questions": [
            "Is the tumor resectable?",
            "Would neoadjuvant therapy improve resectability or outcomes?",
            "What is the optimal surgical approach?",
            "What are the surgical risks given patient comorbidities?",
            "Can adequate margins be achieved?"
        ]
    },
    "hematologist": {
        "name": "Hematologist",
        "focus": "Bone marrow interpretation, coagulation disorders, transfusion support, stem cell mobilization",
        "key_questions": [
            "Are there hematologic complications to address?",
            "Is anticoagulation indicated or contraindicated?",
            "What transfusion support is needed?",
            "Are there cytopenias requiring intervention?",
            "Is the patient a transplant candidate if indicated?"
        ]
    },
    "pharmacist": {
        "name": "Clinical Pharmacist",
        "focus": "Drug dosing, interactions, renal/hepatic adjustments, supportive medications, adverse effects",
        "key_questions": [
            "Are dose adjustments needed for organ dysfunction?",
            "What drug-drug interactions should be monitored?",
            "What prophylactic medications are indicated?",
            "How should antiemetics and growth factors be prescribed?",
            "Are there cost-effective alternatives to consider?"
        ]
    },
    "palliative_care": {
        "name": "Palliative Care Specialist",
        "focus": "Symptom management, quality of life, goals of care, psychosocial support, advance directives",
        "key_questions": [
            "What symptoms are impacting quality of life?",
            "Have goals of care been clearly established?",
            "Is the treatment plan aligned with patient values?",
            "What psychosocial support does the patient need?",
            "Are there advance care planning conversations needed?"
        ]
    }
}


def format_case_for_specialty(case_data: Dict[str, Any], specialty_info: Dict[str, str]) -> str:
    """Format case data with specialty-specific lens."""
    
    prompt = f"""You are a {specialty_info['name']} participating in a multidisciplinary tumor board.

Your expertise focuses on: {specialty_info['focus']}

CASE PRESENTATION:
{json.dumps(case_data, indent=2)}

SPECIALTY-SPECIFIC ANALYSIS REQUIRED:

As a {specialty_info['name']}, analyze this case with particular attention to:
"""
    
    for i, question in enumerate(specialty_info['key_questions'], 1):
        prompt += f"\n{i}. {question}"
    
    prompt += """

PROVIDE YOUR ANALYSIS:

1. PRIMARY ASSESSMENT: Your specialty-specific evaluation of this case
2. KEY FINDINGS: Critical observations from your domain expertise
3. RECOMMENDATIONS: What your specialty suggests for management
4. CONCERNS: Potential issues or red flags from your perspective
5. QUESTIONS FOR OTHER SPECIALTIES: What you need clarified by colleagues
6. CONFIDENCE LEVEL: High/Moderate/Low with reasoning

Be specific, evidence-based, and focus on your domain expertise. Reference relevant guidelines where applicable.
"""
    
    return prompt


def generate_deliberation_summary(specialty_analyses: Dict[str, str], case_data: Dict[str, Any]) -> str:
    """Generate synthesis prompt for tumor board consensus."""
    
    prompt = """MULTIDISCIPLINARY TUMOR BOARD DELIBERATION

You are synthesizing multiple specialty perspectives into a consensus recommendation.

SPECIALTY ANALYSES COMPLETED:

"""
    
    for specialty_key, analysis in specialty_analyses.items():
        specialty_name = TUMOR_BOARD_SPECIALTIES[specialty_key]['name']
        prompt += f"\n{'='*60}\n{specialty_name.upper()} PERSPECTIVE:\n{'='*60}\n{analysis}\n"
    
    prompt += """

TASK: Synthesize these perspectives into a comprehensive tumor board consensus.

REQUIRED OUTPUT STRUCTURE:

1. CONSENSUS DIAGNOSIS/STAGING: Agreed-upon diagnosis with complete staging

2. CONSENSUS TREATMENT PLAN: 
   - Primary treatment modality(ies)
   - Treatment sequencing (neoadjuvant → surgery → adjuvant, etc.)
   - Specific regimens with dosing considerations
   - Timeline and milestones

3. MULTIDISCIPLINARY CONSIDERATIONS:
   - Points of agreement across specialties
   - Areas requiring case-by-case judgment
   - Specialty-specific interventions needed

4. ALTERNATIVE APPROACHES:
   - Other reasonable treatment options discussed
   - Rationale for recommended approach over alternatives
   - Circumstances that would change the recommendation

5. MONITORING & FOLLOW-UP:
   - Response assessment plan
   - Surveillance imaging and labs
   - Specialty-specific follow-up requirements

6. PATIENT COMMUNICATION PLAN:
   - Key points for shared decision-making
   - Risks vs benefits to discuss
   - Quality of life considerations

7. CONTINGENCY PLANS:
   - If patient declines recommended treatment
   - If disease progression occurs
   - Management of expected toxicities

8. OVERALL CONFIDENCE:
   - High/Moderate/Low
   - Key uncertainties or knowledge gaps
   - When to reconvene tumor board

SYNTHESIZE ANALYSES INTO COMPREHENSIVE CONSENSUS RECOMMENDATION:
"""
    
    return prompt


def run_tumor_board_analysis(case_file: str) -> Dict[str, Any]:
    """
    Run complete tumor board simulation.
    
    Args:
        case_file: Path to JSON file with case data
        
    Returns:
        Dictionary with specialty analyses and consensus
    """
    
    # Load case data
    with open(case_file, 'r') as f:
        case_data = json.load(f)
    
    print("=" * 80)
    print("MULTIDISCIPLINARY TUMOR BOARD SIMULATION")
    print("=" * 80)
    print(f"\nCase: {case_data.get('patient_id', 'Unknown')}")
    print(f"Brief: {case_data.get('brief_description', 'N/A')}\n")
    
    # Generate analysis prompts for each specialty
    specialty_analyses = {}
    
    print("PHASE 1: Independent Specialty Analyses")
    print("-" * 80)
    
    for specialty_key, specialty_info in TUMOR_BOARD_SPECIALTIES.items():
        print(f"\n📋 Generating {specialty_info['name']} analysis prompt...")
        
        analysis_prompt = format_case_for_specialty(case_data, specialty_info)
        
        # Store prompt for execution by Claude
        specialty_analyses[specialty_key] = {
            "name": specialty_info["name"],
            "prompt": analysis_prompt,
            "response": None  # To be filled by Claude
        }
    
    print(f"\n✅ Generated {len(specialty_analyses)} specialty analysis prompts")
    
    # Generate deliberation prompt
    print("\n" + "=" * 80)
    print("PHASE 2: Multidisciplinary Deliberation")
    print("-" * 80)
    
    # This would normally be populated with actual responses from Claude
    # For now, we structure the framework
    
    deliberation_prompt = """After all specialties have analyzed the case independently,
synthesize their perspectives into a tumor board consensus using the deliberation_summary prompt."""
    
    result = {
        "case_data": case_data,
        "specialty_analyses": specialty_analyses,
        "deliberation_prompt": deliberation_prompt,
        "instructions": """
USAGE INSTRUCTIONS:

1. For each specialty in 'specialty_analyses', invoke Claude with the provided prompt
2. Store each specialty's response in the 'response' field
3. Once all specialties have responded, use the responses to generate the deliberation summary
4. Invoke Claude with the deliberation summary prompt to synthesize consensus

This framework ensures each specialty analyzes independently before group deliberation,
mimicking real tumor board dynamics and reducing groupthink bias.
"""
    }
    
    return result


def main():
    """Main execution function."""
    
    if len(sys.argv) < 2:
        print("Usage: python tumor_board.py <case_file.json>")
        print("\nExpected JSON format:")
        print(json.dumps({
            "patient_id": "MRN-12345",
            "age": 67,
            "sex": "M",
            "brief_description": "Newly diagnosed lung adenocarcinoma",
            "presentation": "Chronic cough, weight loss, found to have RUL mass",
            "imaging": "4.5cm RUL mass, hilar LAD, no distant metastases",
            "pathology": "Adenocarcinoma, PDL1 80%, EGFR/ALK negative",
            "staging": "cT2aN1M0 (Stage IIB)",
            "performance_status": "ECOG 1",
            "comorbidities": ["COPD", "HTN"],
            "labs": {"Cr": 1.1, "AST": 32, "ALT": 28},
            "question": "Optimal management strategy?"
        }, indent=2))
        sys.exit(1)
    
    case_file = sys.argv[1]
    
    if not Path(case_file).exists():
        print(f"Error: Case file not found: {case_file}")
        sys.exit(1)
    
    # Run tumor board analysis
    result = run_tumor_board_analysis(case_file)
    
    # Output results
    output_file = case_file.replace('.json', '_tumor_board_analysis.json')
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n✅ Tumor board analysis framework generated: {output_file}")
    print("\nNext steps:")
    print("1. Invoke Claude with each specialty prompt")
    print("2. Collect responses")
    print("3. Synthesize into consensus recommendation")


if __name__ == "__main__":
    main()
