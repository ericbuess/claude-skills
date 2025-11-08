#!/usr/bin/env python3
"""
Risk Analyzer - Quantitative Risk-Benefit Analysis

Calculates and visualizes risk-benefit tradeoffs for treatment decisions
with patient-specific risk factor adjustments.
"""

import json
import sys
from typing import Dict, List, Any, Optional
from pathlib import Path


def generate_risk_benefit_prompt(case_data: Dict[str, Any],
                                 treatment_option: str,
                                 comparison_option: Optional[str] = None) -> str:
    """Generate quantitative risk-benefit analysis prompt."""
    
    prompt = f"""QUANTITATIVE RISK-BENEFIT ANALYSIS

TREATMENT UNDER EVALUATION: {treatment_option}
"""
    
    if comparison_option:
        prompt += f"COMPARISON TO: {comparison_option}\n"
    
    prompt += f"""
PATIENT CONTEXT:
{json.dumps(case_data, indent=2)}

REQUIRED ANALYSIS:

1. BASELINE RISK ASSESSMENT (Without Treatment)
   Based on patient characteristics:
   - Disease stage and biology
   - Age and performance status
   - Comorbidities
   - Prognostic scores/indices
   
   Estimate:
   - Probability of disease progression (%)
   - Expected survival (median and range)
   - Quality of life trajectory
   - Risk of complications

2. TREATMENT BENEFIT QUANTIFICATION
   From clinical trial data and real-world evidence:
   
   A. Survival Benefits:
      - Absolute overall survival benefit (months added)
      - Hazard ratio with 95% CI
      - Median OS: treated vs untreated
      - 1-year, 2-year, 5-year survival rates
      - Number needed to treat (NNT) for survival benefit
   
   B. Progression-Free Survival:
      - PFS benefit (months)
      - Hazard ratio with 95% CI
      - Time to progression differences
      - Response rates (CR, PR, OR)
   
   C. Quality of Life:
      - QoL improvement vs decline
      - Time to symptom improvement
      - Duration of benefit
      - Functional status preservation

3. TREATMENT RISK QUANTIFICATION
   From clinical trial safety data:
   
   A. Common Toxicities (>10%):
      - Grade 1-2 adverse events
      - Expected impact on daily life
      - Duration of side effects
      - Manageability with supportive care
   
   B. Serious Toxicities (Grade 3-4):
      - Frequency of severe adverse events
      - Hospitalization rates
      - Treatment modifications needed
      - Permanent organ damage risk
      - Number needed to harm (NNH)
   
   C. Life-Threatening Risks:
      - Treatment-related mortality rate
      - ICU admission rates
      - Fatal complications
   
   D. Long-Term Risks:
      - Secondary malignancies
      - Chronic organ dysfunction
      - Late effects (cardiac, pulmonary, etc.)

4. PATIENT-SPECIFIC RISK MODIFICATION
   Adjust baseline estimates for:
   - Age (<65, 65-75, >75)
   - Performance status (ECOG 0-4)
   - Organ dysfunction (renal, hepatic, cardiac)
   - Prior treatments and resistance
   - Comorbidities (diabetes, CAD, etc.)
   - Genetic/molecular factors
   
   Calculate modified:
   - Expected benefit (may be reduced)
   - Expected toxicity (may be increased)
   - Risk-adjusted recommendations

5. ABSOLUTE vs RELATIVE BENEFIT
   Present both:
   - Relative risk reduction (RRR): "30% reduction in death"
   - Absolute risk reduction (ARR): "5% more patients alive at 5 years"
   - Number needed to treat (NNT): "20 patients treated to save 1 life"
   
   Frame in patient-friendly terms:
   - "If 100 similar patients received this treatment..."
   - "Your personal chance of benefit is..."

6. RISK-BENEFIT RATIO CALCULATION
   Quantify tradeoff:
   - Life-years gained vs quality-years lost to toxicity
   - Quality-adjusted survival (QALY)
   - Therapeutic ratio (benefit/toxicity)
   
   Categorize decision:
   - Clear net benefit: NNT << NNH, substantial survival gain
   - Marginal benefit: NNT ~ NNH, modest survival gain
   - Unfavorable: NNT >> NNH, minimal survival gain
   - No benefit: No survival advantage, only toxicity

7. DECISION SCENARIOS
   Consider different patient priorities:
   
   Scenario A: Maximize survival (accept more toxicity)
   → Recommendation and expected outcomes
   
   Scenario B: Optimize quality of life (accept less aggressive)
   → Recommendation and expected outcomes
   
   Scenario C: Balance survival and quality
   → Recommendation and expected outcomes

8. COMPARISON ANALYSIS"""
    
    if comparison_option:
        prompt += f"""
   Direct comparison of {treatment_option} vs {comparison_option}:
   
   Efficacy Comparison:
   - Survival: Option A vs B (months, HR, CI)
   - Response: Option A vs B (%, OR, CI)
   - NNT for survival benefit: Option A vs B
   
   Toxicity Comparison:
   - Grade 3-4 AEs: Option A vs B (%)
   - Treatment discontinuation: Option A vs B (%)
   - NNH for serious toxicity: Option A vs B
   
   Net Benefit:
   - Which option has better risk-benefit ratio?
   - For which patient types?
   - What factors favor one over the other?
"""
    
    prompt += """
9. UNCERTAINTY QUANTIFICATION
   - Confidence intervals around estimates
   - Quality of supporting evidence
   - Extrapolation assumptions made
   - Individual variation expected

10. SHARED DECISION-MAKING FRAMEWORK
    Create decision aid with:
    - Visual representation (if possible)
    - Simple comparison tables
    - "What would happen to 100 patients like me" framing
    - Questions to consider
    - Resources for more information

OUTPUT COMPREHENSIVE QUANTITATIVE RISK-BENEFIT ANALYSIS:
- Include specific numbers with confidence intervals
- Frame in absolute terms (not just relative)
- Calculate NNT and NNH
- Provide patient-specific estimates
- Clear recommendation with reasoning
"""
    
    return prompt


def generate_prognostic_calculator_prompt(case_data: Dict[str, Any],
                                         score_system: str) -> str:
    """Generate prompt for applying prognostic scoring system."""
    
    prompt = f"""PROGNOSTIC SCORE CALCULATION

SCORING SYSTEM: {score_system}

PATIENT DATA:
{json.dumps(case_data, indent=2)}

CALCULATION STEPS:

1. IDENTIFY REQUIRED VARIABLES
   List all factors needed for {score_system} calculation

2. EXTRACT FROM CASE DATA
   Map patient data to scoring variables:
   - Age
   - Laboratory values
   - Disease characteristics
   - Molecular/cytogenetic features
   - Performance status
   - Comorbidities

3. CALCULATE SCORE
   Apply {score_system} algorithm:
   - Individual variable points
   - Total score
   - Risk category (low, intermediate, high)

4. INTERPRET RESULTS
   Based on score:
   - Expected overall survival (median with range)
   - Progression-free survival
   - Treatment response likelihood
   - Relapse risk
   
   Provide:
   - 1-year, 2-year, 5-year survival probabilities
   - Comparison to population averages

5. VALIDATE SCORE APPLICATION
   Check:
   - Is this score validated for this population?
   - Are all required variables available?
   - Any caveats to interpretation?
   - When was score last updated?

6. TREATMENT IMPLICATIONS
   How does score impact recommendations:
   - Risk-adapted therapy selection
   - Transplant candidacy
   - Clinical trial eligibility
   - Surveillance intensity

7. CONFIDENCE IN ESTIMATE
   - High: All variables available, well-validated
   - Moderate: Some extrapolation needed
   - Low: Missing key variables or unvalidated population

OUTPUT CALCULATED PROGNOSTIC SCORE WITH INTERPRETATION:
"""
    
    return prompt


def generate_decision_tree_prompt(case_data: Dict[str, Any],
                                 decision_points: List[str]) -> str:
    """Generate decision tree analysis for sequential choices."""
    
    prompt = f"""DECISION TREE ANALYSIS

PATIENT CONTEXT:
{json.dumps(case_data, indent=2)}

DECISION POINTS:
"""
    
    for i, point in enumerate(decision_points, 1):
        prompt += f"{i}. {point}\n"
    
    prompt += """

CREATE DECISION TREE:

For each decision point:

1. IDENTIFY OPTIONS
   List all reasonable choices at this node

2. ESTIMATE OUTCOMES
   For each option:
   - Success probability
   - Failure probability
   - Expected survival
   - Quality of life
   - Costs (financial, time, suffering)

3. SEQUENTIAL DEPENDENCIES
   How does choice at this node affect:
   - Future options available
   - Future success probabilities
   - Overall expected outcome

4. CALCULATE EXPECTED VALUE
   For each path through tree:
   - Multiply probabilities along path
   - Sum outcomes weighted by probability
   - Identify optimal path

5. SENSITIVITY ANALYSIS
   What if assumptions change:
   - Patient priorities (QoL vs survival)
   - Probability estimates (optimistic vs pessimistic)
   - Available options (new therapy, trial access)

6. RECOMMENDATION
   - Optimal initial decision
   - Contingency plans for each outcome
   - Key decision points for reassessment

OUTPUT DECISION TREE WITH EXPECTED VALUES AND RECOMMENDATION:
"""
    
    return prompt


def run_risk_analysis(case_file: str,
                     analysis_type: str = "risk_benefit",
                     **kwargs) -> Dict[str, Any]:
    """
    Run risk analysis.
    
    Args:
        case_file: Path to case data JSON
        analysis_type: Type of analysis (risk_benefit, prognosis, decision_tree)
        **kwargs: Additional arguments specific to analysis type
        
    Returns:
        Dictionary with analysis prompts
    """
    
    # Load case data
    with open(case_file, 'r') as f:
        case_data = json.load(f)
    
    print("=" * 80)
    print("QUANTITATIVE RISK ANALYSIS")
    print("=" * 80)
    print(f"\nCase: {case_data.get('patient_id', 'Unknown')}")
    print(f"Analysis Type: {analysis_type}\n")
    
    result = {
        "case_data": case_data,
        "analysis_type": analysis_type
    }
    
    if analysis_type == "risk_benefit":
        treatment = kwargs.get('treatment', case_data.get('treatment', 'Proposed treatment'))
        comparison = kwargs.get('comparison', None)
        print(f"Analyzing: {treatment}")
        if comparison:
            print(f"vs: {comparison}")
        result["analysis_prompt"] = generate_risk_benefit_prompt(
            case_data, treatment, comparison
        )
        
    elif analysis_type == "prognosis":
        score_system = kwargs.get('score_system', 'IPI')
        print(f"Calculating: {score_system} score")
        result["prognosis_prompt"] = generate_prognostic_calculator_prompt(
            case_data, score_system
        )
        
    elif analysis_type == "decision_tree":
        decision_points = kwargs.get('decision_points', 
                                    ['Initial treatment', 'Response assessment', 'Next steps'])
        print(f"Decisions: {', '.join(decision_points)}")
        result["decision_tree_prompt"] = generate_decision_tree_prompt(
            case_data, decision_points
        )
    
    result["instructions"] = """
USAGE INSTRUCTIONS:

1. Invoke Claude with generated analysis prompt
2. Provide any additional clinical trial data or guidelines
3. Claude will calculate quantitative risk-benefit metrics
4. Output includes:
   - NNT (number needed to treat)
   - NNH (number needed to harm)
   - Absolute risk reduction
   - Patient-specific estimates
   - Visual decision aids

TIPS:
- Always present absolute numbers, not just relative
- Include confidence intervals
- Account for patient-specific risk factors
- Frame in patient-friendly terms
"""
    
    return result


def main():
    """Main execution function."""
    
    if len(sys.argv) < 2:
        print("Usage: python risk_analyzer.py <case_file.json> [analysis_type] [options]")
        print("\nAnalysis types:")
        print("- risk_benefit: Quantitative risk-benefit analysis (default)")
        print("- prognosis: Calculate prognostic scores")
        print("- decision_tree: Sequential decision analysis")
        print("\nExample case file:")
        print(json.dumps({
            "patient_id": "MRN-12345",
            "age": 68,
            "diagnosis": "Diffuse large B-cell lymphoma",
            "stage": "III",
            "IPI_score": 3,
            "ECOG": 1,
            "comorbidities": ["diabetes", "CAD"],
            "treatment": "R-CHOP",
            "alternative": "Dose-adjusted R-EPOCH"
        }, indent=2))
        sys.exit(1)
    
    case_file = sys.argv[1]
    analysis_type = sys.argv[2] if len(sys.argv) > 2 else "risk_benefit"
    
    if not Path(case_file).exists():
        print(f"Error: Case file not found: {case_file}")
        sys.exit(1)
    
    # Run risk analysis
    result = run_risk_analysis(case_file, analysis_type)
    
    # Output results
    output_file = case_file.replace('.json', f'_risk_{analysis_type}.json')
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n✅ Risk analysis framework generated: {output_file}")
    print("\nNext steps:")
    print("1. Invoke Claude with analysis prompt")
    print("2. Claude will calculate quantitative metrics")
    print("3. Review risk-benefit tradeoffs")


if __name__ == "__main__":
    main()
