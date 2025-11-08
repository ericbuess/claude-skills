#!/usr/bin/env python3
"""
Adversarial Validator - Clinical Decision Validation

Generates alternative interpretations and challenges initial assessments
to identify weaknesses and improve confidence in clinical recommendations.
"""

import json
import sys
from typing import Dict, List, Any
from pathlib import Path


VALIDATION_FRAMEWORKS = {
    "diagnostic": {
        "name": "Diagnostic Adversarial Validation",
        "agents": [
            {
                "role": "Diagnostic Challenger",
                "task": "Generate alternative diagnoses that fit the clinical picture",
                "focus": [
                    "What other diagnoses could explain these findings?",
                    "What atypical presentations should be considered?",
                    "What key tests would differentiate diagnoses?",
                    "Are there red herrings in the presented data?",
                    "What is the pretest probability of each differential?"
                ]
            },
            {
                "role": "Evidence Skeptic",
                "task": "Challenge the quality and interpretation of diagnostic evidence",
                "focus": [
                    "Are the diagnostic tests adequate and properly interpreted?",
                    "What is the sensitivity/specificity of tests used?",
                    "Are there sampling errors or artifacts to consider?",
                    "What additional testing would increase diagnostic confidence?",
                    "Are there confirmatory tests needed?"
                ]
            },
            {
                "role": "Bias Detector",
                "task": "Identify cognitive biases affecting diagnostic reasoning",
                "focus": [
                    "Is there anchoring bias to the initial presentation?",
                    "Availability bias (recent similar cases influencing judgment)?",
                    "Confirmation bias (only seeking supporting evidence)?",
                    "Premature closure (stopping workup too early)?",
                    "What would change if we started fresh?"
                ]
            }
        ]
    },
    "therapeutic": {
        "name": "Therapeutic Adversarial Validation",
        "agents": [
            {
                "role": "Treatment Challenger",
                "task": "Propose alternative treatment strategies",
                "focus": [
                    "What other evidence-based treatments exist?",
                    "Are there newer therapies with better outcomes?",
                    "Could less intensive treatment achieve similar outcomes?",
                    "What if this treatment fails - what's the backup plan?",
                    "Are there combination strategies being overlooked?"
                ]
            },
            {
                "role": "Risk Analyzer",
                "task": "Quantify and challenge risk-benefit assessments",
                "focus": [
                    "Are treatment risks being underestimated?",
                    "What are the absolute vs relative risk reductions?",
                    "Number needed to treat vs number needed to harm?",
                    "Are patient-specific risk factors accounted for?",
                    "What is the expected quality-adjusted survival?"
                ]
            },
            {
                "role": "Evidence Critic",
                "task": "Evaluate the strength of supporting evidence",
                "focus": [
                    "What is the quality of evidence (Level I vs II vs III)?",
                    "Are guideline recommendations Category 1 or 2B?",
                    "How applicable are trial populations to this patient?",
                    "Are there conflicting studies or guidelines?",
                    "What are the evidence gaps and uncertainties?"
                ]
            },
            {
                "role": "Patient Advocate",
                "task": "Consider patient-centered factors",
                "focus": [
                    "Does this align with patient values and goals?",
                    "Are there quality of life tradeoffs not addressed?",
                    "Practical barriers (cost, transportation, support)?",
                    "Is the treatment burden reasonable for this patient?",
                    "Have alternatives been explained for shared decision-making?"
                ]
            }
        ]
    },
    "prognostic": {
        "name": "Prognostic Adversarial Validation",
        "agents": [
            {
                "role": "Prognostic Challenger",
                "task": "Challenge prognostic estimates",
                "focus": [
                    "Are validated prognostic scores being used correctly?",
                    "What factors could make prognosis better or worse?",
                    "Are molecular markers accurately interpreted?",
                    "What is the confidence interval around estimates?",
                    "Are temporal factors (early vs late relapse) considered?"
                ]
            },
            {
                "role": "Outlier Identifier",
                "task": "Identify factors making this case atypical",
                "focus": [
                    "What unusual features could alter typical outcomes?",
                    "Are there comorbidities affecting prognosis?",
                    "Biology vs chronology (younger/older than typical)?",
                    "Prior treatment exposures affecting future response?",
                    "Genetic or molecular features conferring good/poor risk?"
                ]
            }
        ]
    }
}


def generate_validation_prompt(case_data: Dict[str, Any], 
                              initial_assessment: str,
                              validation_type: str,
                              agent: Dict[str, Any]) -> str:
    """Generate adversarial validation prompt for specific agent."""
    
    prompt = f"""You are the {agent['role']} in an adversarial validation process.

TASK: {agent['task']}

INITIAL CLINICAL ASSESSMENT TO CHALLENGE:
{initial_assessment}

CASE DATA:
{json.dumps(case_data, indent=2)}

YOUR ROLE: {agent['role']}

Focus your adversarial analysis on:
"""
    
    for i, question in enumerate(agent['focus'], 1):
        prompt += f"\n{i}. {question}"
    
    prompt += """

PROVIDE ADVERSARIAL ANALYSIS:

1. PRIMARY CHALLENGES: What weaknesses do you identify in the initial assessment?

2. ALTERNATIVE INTERPRETATIONS: What other conclusions are plausible?

3. MISSING INFORMATION: What data would change your challenge?

4. SUPPORTING EVIDENCE: What evidence supports your alternative view?

5. CONFIDENCE IN CHALLENGE: How strong is your counter-argument?
   - High: Initial assessment has significant flaws
   - Moderate: Some concerns but not fatal to initial assessment
   - Low: Minor quibbles, initial assessment likely sound

6. RECOMMENDED ACTIONS: What should be done to resolve uncertainty?

Be critical and rigorous. Your job is to find flaws, not to agree.
"""
    
    return prompt


def generate_synthesis_prompt(case_data: Dict[str, Any],
                             initial_assessment: str,
                             challenges: List[Dict[str, Any]]) -> str:
    """Generate prompt for synthesizing validation results."""
    
    prompt = f"""ADVERSARIAL VALIDATION SYNTHESIS

INITIAL ASSESSMENT:
{initial_assessment}

ADVERSARIAL CHALLENGES RECEIVED:

"""
    
    for i, challenge in enumerate(challenges, 1):
        prompt += f"\n{'='*60}\nCHALLENGE #{i} from {challenge['role']}:\n{'='*60}\n"
        prompt += f"{challenge['response']}\n"
    
    prompt += """

SYNTHESIS TASK:

Integrate the adversarial challenges to produce:

1. VALIDATED ASSESSMENT:
   - What from the initial assessment survives scrutiny?
   - What needs to be modified or abandoned?
   - How confident can we be now?

2. IDENTIFIED WEAKNESSES:
   - What flaws were found in initial reasoning?
   - Which challenges were most compelling?
   - What assumptions were questioned successfully?

3. ALTERNATIVE SCENARIOS:
   - What plausible alternatives emerged?
   - Under what conditions would each apply?
   - How likely is each scenario?

4. UNRESOLVED UNCERTAINTIES:
   - What questions remain unanswered?
   - What data would resolve key uncertainties?
   - Where is there true clinical equipoise?

5. STRENGTHENED RECOMMENDATION:
   - Given all challenges, what is the best course of action?
   - What hedges or contingencies are needed?
   - How should monitoring differ given uncertainties?

6. CONFIDENCE CALIBRATION:
   - High (>90%): Assessment withstood rigorous challenge
   - Moderate (70-90%): Some modifications but core intact
   - Low (<70%): Significant concerns raised, multiple viable alternatives

7. AREAS NEEDING FURTHER INVESTIGATION:
   - Additional testing needed
   - Specialist consultation warranted
   - Literature review required

OUTPUT CALIBRATED, VALIDATED CLINICAL RECOMMENDATION:
"""
    
    return prompt


def run_adversarial_validation(case_file: str, 
                               assessment_file: str,
                               validation_type: str = "diagnostic") -> Dict[str, Any]:
    """
    Run adversarial validation on clinical assessment.
    
    Args:
        case_file: Path to case data JSON
        assessment_file: Path to initial assessment text
        validation_type: Type of validation (diagnostic, therapeutic, prognostic)
        
    Returns:
        Dictionary with challenges and synthesis prompts
    """
    
    # Validate inputs
    if validation_type not in VALIDATION_FRAMEWORKS:
        raise ValueError(f"Unknown validation type: {validation_type}. "
                        f"Must be one of {list(VALIDATION_FRAMEWORKS.keys())}")
    
    # Load case data and initial assessment
    with open(case_file, 'r') as f:
        case_data = json.load(f)
    
    with open(assessment_file, 'r') as f:
        initial_assessment = f.read()
    
    framework = VALIDATION_FRAMEWORKS[validation_type]
    
    print("=" * 80)
    print(f"{framework['name'].upper()}")
    print("=" * 80)
    print(f"\nCase: {case_data.get('patient_id', 'Unknown')}")
    print(f"Validation Type: {validation_type}\n")
    
    # Generate challenge prompts for each agent
    challenges = []
    
    print("PHASE 1: Generating Adversarial Challenges")
    print("-" * 80)
    
    for agent in framework['agents']:
        print(f"\n🔍 {agent['role']}...")
        
        challenge_prompt = generate_validation_prompt(
            case_data, 
            initial_assessment,
            validation_type,
            agent
        )
        
        challenges.append({
            "role": agent['role'],
            "task": agent['task'],
            "prompt": challenge_prompt,
            "response": None  # To be filled by Claude
        })
    
    print(f"\n✅ Generated {len(challenges)} adversarial challenge prompts")
    
    # Generate synthesis prompt
    print("\n" + "=" * 80)
    print("PHASE 2: Synthesis & Validation")
    print("-" * 80)
    
    synthesis_prompt = """After all adversarial agents have challenged the assessment,
synthesize their challenges into a validated, calibrated recommendation."""
    
    result = {
        "case_data": case_data,
        "initial_assessment": initial_assessment,
        "validation_type": validation_type,
        "challenges": challenges,
        "synthesis_prompt": synthesis_prompt,
        "instructions": """
USAGE INSTRUCTIONS:

1. For each challenge in 'challenges', invoke Claude with the provided prompt
2. Store each response in the 'response' field
3. Once all challenges collected, generate synthesis prompt with responses
4. Invoke Claude with synthesis prompt to produce validated recommendation

This adversarial process:
- Identifies flaws in reasoning
- Generates alternative interpretations
- Quantifies uncertainty
- Produces higher-confidence recommendations

Confidence calibration:
- More challenges sustained = lower confidence in initial assessment
- Challenges refuted = higher confidence in initial assessment
- New evidence needed = honest acknowledgment of uncertainty
"""
    }
    
    return result


def main():
    """Main execution function."""
    
    if len(sys.argv) < 3:
        print("Usage: python adversarial_validator.py <case_file.json> <assessment_file.txt> [validation_type]")
        print("\nValidation types: diagnostic, therapeutic, prognostic (default: diagnostic)")
        print("\nExample case file:")
        print(json.dumps({
            "patient_id": "MRN-12345",
            "age": 54,
            "presentation": "Anemia, fatigue",
            "labs": {"Hgb": 8.2, "MCV": 78, "Fe": 25},
            "initial_diagnosis": "Iron deficiency anemia"
        }, indent=2))
        sys.exit(1)
    
    case_file = sys.argv[1]
    assessment_file = sys.argv[2]
    validation_type = sys.argv[3] if len(sys.argv) > 3 else "diagnostic"
    
    # Validate files exist
    for filepath in [case_file, assessment_file]:
        if not Path(filepath).exists():
            print(f"Error: File not found: {filepath}")
            sys.exit(1)
    
    # Run adversarial validation
    result = run_adversarial_validation(case_file, assessment_file, validation_type)
    
    # Output results
    output_file = assessment_file.replace('.txt', f'_adversarial_{validation_type}.json')
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n✅ Adversarial validation framework generated: {output_file}")
    print("\nNext steps:")
    print("1. Invoke Claude with each challenge prompt")
    print("2. Collect challenge responses")
    print("3. Synthesize into validated recommendation")


if __name__ == "__main__":
    main()
