#!/usr/bin/env python3
"""
Evidence Research - Literature Search and Synthesis

Generates structured prompts for systematic literature review using PubMed tools.

CRITICAL: This script is a FALLBACK framework. The primary method for evidence 
research should be direct use of PubMed MCP server tools:
- PubMed:search_articles
- PubMed:get_article_metadata  
- PubMed:get_full_text_article
- PubMed:find_related_articles

Only use this script if PubMed tools are unavailable or for generating 
comprehensive research plans that require multiple coordinated searches.
"""

import json
import sys
from typing import Dict, List, Any
from pathlib import Path


EVIDENCE_SOURCES = {
    "guidelines": [
        "NCCN (National Comprehensive Cancer Network)",
        "ASCO (American Society of Clinical Oncology)",
        "ASH (American Society of Hematology)",
        "EHA (European Hematology Association)",
        "ESMO (European Society for Medical Oncology)",
        "SITC (Society for Immunotherapy of Cancer)"
    ],
    "literature": [
        "Phase III randomized controlled trials",
        "Meta-analyses and systematic reviews",
        "Large cohort studies",
        "Landmark trials changing practice",
        "Recent conference abstracts (ASCO, ASH, ESMO)"
    ],
    "databases": [
        "PubMed/MEDLINE",
        "Cochrane Library",
        "ClinicalTrials.gov",
        "NCCN Guidelines",
        "UpToDate"
    ]
}


EVIDENCE_LEVELS = {
    "Level I": {
        "description": "Meta-analysis of RCTs or large multicenter RCTs",
        "strength": "Highest",
        "typical_sources": ["Cochrane reviews", "NEJM/Lancet/JAMA phase III trials"]
    },
    "Level II": {
        "description": "Single RCT or high-quality prospective cohort study",
        "strength": "High",
        "typical_sources": ["Journal of Clinical Oncology trials", "Blood journal studies"]
    },
    "Level III": {
        "description": "Case-control studies, retrospective cohort studies",
        "strength": "Moderate",
        "typical_sources": ["Institutional series", "registry analyses"]
    },
    "Level IV": {
        "description": "Case series, expert opinion, consensus statements",
        "strength": "Low",
        "typical_sources": ["Case reports", "review articles", "guidelines with limited evidence"]
    }
}


def generate_literature_search_prompt(case_data: Dict[str, Any],
                                     clinical_question: str) -> str:
    """Generate comprehensive literature search strategy."""
    
    prompt = f"""EVIDENCE-BASED LITERATURE SEARCH

CLINICAL QUESTION:
{clinical_question}

CASE CONTEXT:
{json.dumps(case_data, indent=2)}

SEARCH STRATEGY:

Phase 1: GUIDELINE REVIEW
Search the following guidelines for recommendations:
"""
    
    for guideline in EVIDENCE_SOURCES['guidelines']:
        prompt += f"\n- {guideline}"
    
    prompt += """

For each guideline found:
1. Identify specific recommendation
2. Note category (1, 2A, 2B, 3)
3. Extract supporting evidence cited
4. Flag any contraindications or special populations

Phase 2: PRIMARY LITERATURE SEARCH
Search terms to use:
"""
    
    # Generate search terms from case data
    if 'diagnosis' in case_data:
        prompt += f"\n- {case_data['diagnosis']}"
    if 'treatment_question' in case_data:
        prompt += f"\n- {case_data['treatment_question']}"
    
    prompt += """
- Add: randomized controlled trial, phase III, meta-analysis
- Date filter: Last 5 years (prioritize last 2 years)

Phase 3: TRIAL REGISTRY SEARCH
Check ClinicalTrials.gov for:
1. Completed trials with results posted
2. Ongoing trials potentially relevant
3. Eligibility criteria for trial enrollment

EVIDENCE SYNTHESIS REQUIRED:

1. GUIDELINE SUMMARY:
   - Consensus recommendations across major societies
   - Points of agreement
   - Areas of controversy or variation
   - Most recent updates or changes

2. PRIMARY EVIDENCE:
   - List key trials by evidence level
   - Sample size, design, primary endpoints
   - Results with confidence intervals/p-values
   - Notable limitations or caveats
   
3. EVIDENCE GAPS:
   - What questions remain unanswered?
   - What populations are understudied?
   - Where is there clinical equipoise?

4. PRACTICAL APPLICATION:
   - How does evidence apply to this specific case?
   - Are there extrapolations being made?
   - Patient-specific factors affecting applicability

5. STRENGTH OF RECOMMENDATION:
   Based on evidence quality and consistency:
   - Strong: Multiple Level I studies, guideline consensus
   - Moderate: Level II evidence or single Level I trial
   - Weak: Level III/IV evidence or expert opinion
   - Insufficient: No quality evidence available

OUTPUT COMPREHENSIVE EVIDENCE SUMMARY FOR CLINICAL DECISION-MAKING:
"""
    
    return prompt


def generate_comparative_evidence_prompt(case_data: Dict[str, Any],
                                        option_a: str,
                                        option_b: str) -> str:
    """Generate prompt for comparing evidence between treatment options."""
    
    prompt = f"""COMPARATIVE EVIDENCE ANALYSIS

Compare evidence supporting two treatment approaches:

OPTION A: {option_a}
OPTION B: {option_b}

CASE CONTEXT:
{json.dumps(case_data, indent=2)}

COMPARATIVE ANALYSIS REQUIRED:

1. HEAD-TO-HEAD TRIALS:
   - Are there direct comparison trials?
   - What were the primary endpoints and results?
   - Were the studies adequately powered?
   - Are populations comparable to this case?

2. INDIRECT COMPARISONS:
   - If no head-to-head data, what indirect evidence exists?
   - Cross-trial comparisons (with caveats)
   - Network meta-analyses available?
   - Historical controls or registry data?

3. EFFICACY COMPARISON:
   Option A:
   - Overall survival benefit (HR, CI, p-value)
   - Progression-free survival
   - Response rates
   - Durability of response
   
   Option B:
   - Overall survival benefit
   - Progression-free survival
   - Response rates
   - Durability of response

4. TOXICITY COMPARISON:
   Option A:
   - Grade 3-4 adverse events
   - Treatment discontinuation rates
   - Quality of life impacts
   - Long-term toxicities
   
   Option B:
   - Grade 3-4 adverse events
   - Treatment discontinuation rates
   - Quality of life impacts
   - Long-term toxicities

5. PRACTICAL CONSIDERATIONS:
   - Administration route and schedule
   - Duration of treatment
   - Cost and insurance coverage
   - Availability and access
   - Monitoring requirements

6. SUBGROUP ANALYSES:
   - Are there patient subgroups favoring one option?
   - Biomarker-selected populations?
   - Age, performance status, comorbidity effects?

7. GUIDELINE PREFERENCE:
   - Do guidelines favor one option?
   - Category 1 vs 2A/2B recommendations?
   - Regional or institutional practice variations?

8. EVIDENCE QUALITY COMPARISON:
   - Level of evidence for each option
   - Strength of recommendation
   - Certainty in estimates

OUTPUT SIDE-BY-SIDE EVIDENCE COMPARISON WITH RECOMMENDATION:
"""
    
    return prompt


def generate_evidence_gaps_prompt(case_data: Dict[str, Any],
                                 clinical_question: str) -> str:
    """Identify knowledge gaps and research needs."""
    
    prompt = f"""EVIDENCE GAP ANALYSIS

CLINICAL QUESTION:
{clinical_question}

CASE CONTEXT:
{json.dumps(case_data, indent=2)}

IDENTIFY EVIDENCE GAPS:

1. UNANSWERED CLINICAL QUESTIONS:
   - What specific questions lack quality evidence?
   - Why are these questions unanswered (difficult to study, rare, etc.)?
   - What is the clinical impact of this uncertainty?

2. POPULATION GAPS:
   - What patient populations are underrepresented in trials?
   - Age extremes (very young, very old)?
   - Comorbidities or organ dysfunction?
   - Racial/ethnic diversity?
   - Real-world vs trial populations?

3. OUTCOME GAPS:
   - What outcomes have not been adequately studied?
   - Long-term survival data lacking?
   - Quality of life endpoints missing?
   - Cost-effectiveness not evaluated?

4. AREAS OF EQUIPOISE:
   - Where do experts genuinely disagree?
   - What questions would be ethical to randomize?
   - What trials are ongoing to address these?

5. PRACTICAL GUIDANCE IN ABSENCE OF EVIDENCE:
   - How should clinicians proceed given uncertainty?
   - What is reasonable extrapolation?
   - Expert consensus approaches?
   - When to favor clinical trial enrollment?

OUTPUT EVIDENCE GAP ASSESSMENT WITH RECOMMENDATIONS FOR PROCEEDING:
"""
    
    return prompt


def run_evidence_research(case_file: str,
                         research_type: str = "comprehensive") -> Dict[str, Any]:
    """
    Run evidence research process.
    
    Args:
        case_file: Path to case data JSON
        research_type: Type of research (comprehensive, comparative, gaps)
        
    Returns:
        Dictionary with research prompts and structure
    """
    
    # Load case data
    with open(case_file, 'r') as f:
        case_data = json.load(f)
    
    clinical_question = case_data.get('clinical_question', 
                                     'Optimal management approach for this case?')
    
    print("=" * 80)
    print("EVIDENCE-BASED RESEARCH")
    print("=" * 80)
    print(f"\nCase: {case_data.get('patient_id', 'Unknown')}")
    print(f"Research Type: {research_type}")
    print(f"Clinical Question: {clinical_question}\n")
    
    result = {
        "case_data": case_data,
        "clinical_question": clinical_question,
        "research_type": research_type,
        "evidence_sources": EVIDENCE_SOURCES,
        "evidence_levels": EVIDENCE_LEVELS
    }
    
    if research_type == "comprehensive":
        print("Generating comprehensive literature search strategy...")
        result["search_prompt"] = generate_literature_search_prompt(
            case_data, clinical_question
        )
        
    elif research_type == "comparative":
        option_a = case_data.get('option_a', 'Standard therapy')
        option_b = case_data.get('option_b', 'Alternative therapy')
        print(f"Generating comparative analysis: {option_a} vs {option_b}...")
        result["comparison_prompt"] = generate_comparative_evidence_prompt(
            case_data, option_a, option_b
        )
        
    elif research_type == "gaps":
        print("Generating evidence gap analysis...")
        result["gaps_prompt"] = generate_evidence_gaps_prompt(
            case_data, clinical_question
        )
    
    result["instructions"] = """
USAGE INSTRUCTIONS:

1. Use web search tools to find:
   - Recent NCCN, ASCO, ASH guidelines
   - Key clinical trials (search PubMed)
   - Meta-analyses and systematic reviews

2. Invoke Claude with generated prompt and search results

3. Claude will synthesize evidence into clinical recommendation

4. Output should include:
   - Evidence summary with levels
   - Strength of recommendation
   - Gaps and uncertainties
   - Application to specific case

TIP: For recent evidence, search:
- "condition treatment phase III" in PubMed
- "[condition]" in NCCN guidelines
- ClinicalTrials.gov for ongoing/completed trials
"""
    
    return result


def main():
    """Main execution function."""
    
    if len(sys.argv) < 2:
        print("Usage: python evidence_research.py <case_file.json> [research_type]")
        print("\nResearch types:")
        print("- comprehensive: Full literature search and synthesis (default)")
        print("- comparative: Compare evidence for two treatment options")
        print("- gaps: Identify evidence gaps and uncertainties")
        print("\nExample case file:")
        print(json.dumps({
            "patient_id": "MRN-12345",
            "diagnosis": "Newly diagnosed multiple myeloma",
            "clinical_question": "Optimal induction regimen?",
            "transplant_eligible": True,
            "option_a": "VRd (Velcade/Revlimid/dex)",
            "option_b": "Dara-VRd (Daratumumab/Velcade/Revlimid/dex)"
        }, indent=2))
        sys.exit(1)
    
    case_file = sys.argv[1]
    research_type = sys.argv[2] if len(sys.argv) > 2 else "comprehensive"
    
    if not Path(case_file).exists():
        print(f"Error: Case file not found: {case_file}")
        sys.exit(1)
    
    # Run evidence research
    result = run_evidence_research(case_file, research_type)
    
    # Output results
    output_file = case_file.replace('.json', f'_evidence_{research_type}.json')
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n✅ Evidence research framework generated: {output_file}")
    print("\nNext steps:")
    print("1. Perform web searches for guidelines and literature")
    print("2. Invoke Claude with research prompt and search results")
    print("3. Synthesize evidence into clinical recommendation")


if __name__ == "__main__":
    main()
