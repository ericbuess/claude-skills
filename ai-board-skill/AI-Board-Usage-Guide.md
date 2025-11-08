# AI Board Skill - Usage Guide

## Overview

The AI Board is a sophisticated reasoning system that combines cutting-edge LLM techniques to achieve maximum accuracy on complex questions. It automatically adapts to your question's domain and complexity, deploying the appropriate reasoning strategies.

## Installation

1. Upload the `ai-board.skill` file to Claude.ai
2. Go to Settings → Skills
3. Upload the skill file
4. The skill will be automatically activated for relevant questions

## How to Use

### Triggering the AI Board

The skill automatically activates when:
- You use trigger phrases: "ai board", "expert panel", "deep analysis", "maximum accuracy"
- Your question is detected as complex or high-stakes
- You're asking about critical decisions

### Example Trigger Phrases

```
"ai board: What's the optimal treatment for..."
"I need deep analysis of..."
"Give me maximum accuracy on..."
"Expert panel: How should I think about..."
```

Or just ask your complex question naturally - the skill will activate when needed.

## What the AI Board Does

### 1. Analyzes Your Question
- Identifies domain (medical, theological, philosophical, technical, etc.)
- Assesses complexity (simple → expert-level)
- Determines appropriate reasoning depth

### 2. Deploys Specialized Agents

**For Medical Questions (Jordan)**:
- Medical Oncologist
- Specialist (e.g., Hematologist)
- Evidence Reviewer
- Risk Assessor
- Devil's Advocate

**For Theological Questions (Eric & Family)**:
- Biblical Scholar
- Historical Theologian
- Systematic Theologian
- Practical Theologian
- Devil's Advocate

**For Philosophical Questions (Eric)**:
- Logician
- Epistemologist
- Ethicist
- Metaphysician
- Devil's Advocate

**For Technical Questions**:
- Domain Expert
- Systems Thinker
- Pragmatist
- Security Reviewer
- Devil's Advocate

### 3. Multi-Agent Analysis
- Agents analyze independently
- Devil's advocate challenges assumptions
- Agents debate and refine
- Synthesis of best insights

### 4. Evidence Validation
- External sources checked (when applicable)
- Self-consistency verification
- Constitutional alignment (ethical/biblical principles)

### 5. Structured Output with Confidence

You'll receive:
- **Analysis Summary**: Clear bottom-line answer
- **Key Findings**: Numbered insights with confidence levels
- **Reasoning Process**: How we reached conclusions
- **Areas of Uncertainty**: What remains unclear
- **Confidence Assessment**: Explicit % with rationale
- **Recommendations**: Actionable next steps

## Domain-Specific Protocols

### Medical Questions

The AI Board implements tumor board simulation:

**Level 1** (2-5 min): Rapid clinical assessment for urgent decisions
**Level 2** (10-20 min): Full tumor board with multi-specialty input
**Level 3** (30+ min): Deep evidence analysis for complex cases

Output includes:
- Clinical impression
- Differential diagnosis
- Primary recommendation with rationale
- Evidence quality assessment
- Confidence levels
- Red flags

### Theological Questions

Biblical-theological framework:

1. **Textual Analysis**: What does Scripture say?
2. **Historical Context**: Original meaning
3. **Systematic Integration**: Fits with whole Bible?
4. **Application**: What does this mean today?
5. **Practical Wisdom**: How to live it out

Output includes:
- Biblical answer (clear statement)
- Scriptural foundation (primary texts + supporting passages)
- Theological integration
- Practical application (age-appropriate for kids)
- Areas of legitimate disagreement

### Philosophical Questions

Analytical philosophy framework:

1. **Clarify the question**: Define terms precisely
2. **Map positions**: Survey major views
3. **Evaluate arguments**: Assess logical validity
4. **Consider objections**: Devil's advocate critique
5. **Reasoned conclusion**: Tentative position with humility

Output includes:
- Question clarification
- Major positions with strengths/weaknesses
- Logical analysis
- Thought experiments
- Critical evaluation with confidence levels

## Confidence Levels Explained

The AI Board always provides explicit confidence levels:

- **>95%**: Very high confidence - strong evidence, clear answer
- **85-95%**: High confidence - solid support, minor uncertainty
- **70-85%**: Moderate confidence - good evidence, some uncertainty
- **50-70%**: Lower confidence - competing evidence, significant uncertainty
- **<50%**: Low confidence - speculative, recommend expert consultation

**Key Principle**: Better to be uncertain about what you don't know than confident about what's wrong. This directly addresses Eric's primary concern about confident wrongness.

## Advanced Features

### Computational Efficiency

The AI Board scales its approach to question complexity:
- Simple questions: Fast, direct answers
- Moderate: Standard reasoning with verification
- Complex: Multi-agent debate
- Critical: Extended analysis with maximum validation

### Self-Consistency

For important decisions, the AI Board can:
- Generate 3-5 independent reasoning paths
- Verify consistency across approaches
- Flag discrepancies for investigation
- Update confidence based on agreement

### External Validation

When applicable, checks:
- Medical guidelines (NCCN, ESMO)
- Biblical cross-references
- Logical consistency tests
- Technical documentation

### Adversarial Validation

Devil's advocate always:
- Challenges assumptions
- Identifies weak points
- Proposes alternatives
- Tests edge cases
- Forces stronger reasoning

## Example Outputs

### Example 1: Medical Question (Complex)

**Question**: "What's the optimal first-line treatment for newly diagnosed FLT3-mutated AML in a 68-year-old with ECOG 1?"

**AI Board Response**:

```
## Analysis Summary

First-line venetoclax + azacitidine + gilteritinib represents the optimal 
approach based on VIALE-A and recent FLT3-inhibitor data, with expected 
CR/CRi rates of 65-75% and median OS of 12-15 months.

## Key Findings

1. **Standard intensive chemotherapy (7+3) + midostaurin** - Confidence: 70%
   - Supporting: RATIFY trial showed OS benefit
   - Limitations: Age 68 with ECOG 1 - borderline for intensive therapy

2. **Venetoclax + azacitidine + gilteritinib (triplet)** - Confidence: 85%
   - Supporting: VIALE-A established ven+aza efficacy; gilteritinib best 
     FLT3 inhibitor based on ADMIRAL trial
   - Limitations: Triplet combination not yet FDA-approved (off-label)

[Full detailed analysis continues...]

## Confidence Assessment

Overall confidence: 85%

Factors increasing confidence:
- Strong trial data for venetoclax + azacitidine in elderly AML
- ADMIRAL trial data for gilteritinib in FLT3+ AML
- Patient characteristics favor less intensive approach

Factors decreasing confidence:
- Triplet combination remains off-label
- Limited direct comparative data
- Individual risk factors need consideration

## Recommendations

Primary: Enroll in clinical trial if available for triplet therapy
Alternative: Venetoclax + azacitidine + gilteritinib off-label
Fallback: Standard venetoclax + azacitidine if gilteritinib unavailable
```

### Example 2: Theological Question (Moderate)

**Question**: "What does the Bible teach about whether Christians can lose their salvation?"

**AI Board Response**:

```
## Biblical Answer

Scripture teaches that genuine believers are kept secure by God's power 
(perseverance of the saints), though Christians disagree on whether apostasy 
is possible for truly regenerate believers.

## Scriptural Foundation

### Primary Texts
1. **John 10:27-29** - "My sheep hear my voice... and no one will snatch them 
   out of my hand"
   - Context: Jesus's discourse on His identity
   - Meaning: Genuine believers are securely held by both Christ and the Father
   - Application: True Christians can have confidence in their eternal security

[Multiple additional Scripture passages analyzed...]

## Theological Integration

### Systematic Considerations
- Fits with doctrine of God's sovereignty: If salvation were losable, it would 
  depend on us not God
- Relates to perseverance of the saints: True believers endure to the end
- Implications for assurance: We can have confidence based on God's promises, 
  not our performance

### Historical Church Understanding
- Reformed tradition: Perseverance of the saints - true believers cannot lose 
  salvation
- Arminian tradition: Conditional security - apostasy is possible
- Both agree: Genuine faith produces fruit; those who fall away may never have 
  been truly saved

[Full analysis continues...]

## Confidence Assessment

Overall confidence: 80%

Very confident in:
- God's power to keep believers (John 10, Romans 8)
- True faith produces perseverance (1 John)

Less certain about:
- Interpretation of warning passages (Hebrews 6, 10)
- Whether apostates were ever truly regenerate

## Panel Discussion Highlights

**Key Points of Agreement**:
- All agreed genuine faith is evidenced by fruit
- All agreed God's power preserves His people
- All agreed warnings in Scripture are serious

**Debated Aspects**:
- Whether warning passages address true believers or merely professing believers
- Whether perseverance is evidence of salvation or condition of salvation

**Devil's Advocate Challenges Addressed**:
- Challenge: "What about Hebrews 6 and 10:26?" 
- Response: Reformed view sees these as hypothetical warnings; Arminian view 
  sees as real possibility for believers
```

### Example 3: Philosophical Question (Complex)

**Question**: "Is consciousness reducible to physical brain states?"

**AI Board Response**:

```
## Question Clarification

**As stated**: Is consciousness reducible to physical brain states?

**Disambiguated**: Can phenomenal consciousness (subjective experience, qualia) 
be fully explained by and identified with physical processes in the brain?

**Key terms**:
- **Consciousness**: Phenomenal experience; "what it's like" to be in a mental state
- **Reducible**: Can be fully explained in terms of lower-level physical properties
- **Physical brain states**: Neural activity, neurotransmitter release, etc.

## Major Positions

### Position 1: Physicalist Reductionism
**Core thesis**: Consciousness is identical to brain states; no separate mental 
properties exist.

**Main argument**:
1. Neural correlates exist for every conscious state
2. The most parsimonious explanation is identity
3. Therefore, consciousness = brain activity

**Strengths**:
- Consistent with scientific worldview
- Explains neural correlates
- No mysterious non-physical substances

**Weaknesses**:
- Explanatory gap (how do neurons produce experience?)
- Hard problem of consciousness
- Knowledge argument (Mary's room)

[Full analysis of multiple positions continues...]

## Confidence Assessment

Overall confidence in reductionism: 45%

**This is appropriately low** given:
- Perennial disagreement among experts
- Unresolved hard problem of consciousness
- Multiple defensible positions

## Philosophical Tensions

**Tension**: Subjective experience vs. objective description
- Physics describes objective properties (mass, charge, frequency)
- Consciousness involves subjective properties (what red looks like)
- Unclear how objective description captures subjective reality

**How to hold both**:
- Acknowledge legitimacy of problem
- Recognize limits of current understanding
- Remain open to multiple possibilities
```

## Tips for Best Results

### Do:
✓ Be specific about your question
✓ Provide relevant context
✓ Indicate if it's a critical decision
✓ Ask for clarification if needed
✓ Request specific confidence levels

### Don't:
✗ Expect 100% certainty on complex issues
✗ Ignore uncertainty acknowledgments
✗ Use for simple questions that don't need deep analysis
✗ Forget that AI Board respects domain expertise

## Technical Details

### Reasoning Techniques Used

The AI Board automatically selects from:
- **Chain-of-Thought**: Step-by-step reasoning
- **Self-Consistency**: Multiple independent paths
- **Multi-Agent Debate**: Specialized perspectives
- **Tree of Thoughts**: Exploration with backtracking
- **Constitutional AI**: Value-aligned reasoning
- **Reflexion**: Learning from critiques
- **Meta-Reasoning**: Dynamic technique selection

### Token Optimization

The skill balances thoroughness with efficiency:
- Simple: 500-1000 tokens
- Moderate: 2000-5000 tokens
- Complex: 5000-15000 tokens
- Maximum: Unlimited for critical decisions

## Integration with Your Preferences

The AI Board automatically adapts based on who's asking:

**Eric**: High-level intellectual engagement, direct answers, explicit confidence levels
**Jordan**: Clinical consultant mode, evidence-based, risk-benefit analysis
**Kids**: Age-appropriate language, teaching mode, patient guidance

## Questions?

The AI Board is designed to be intuitive, but if you're unsure:
- Just ask your question naturally
- Add "ai board" if you want to ensure activation
- Request specific analysis depth if needed
- Ask follow-up questions for clarification

---

**Ready to use?** Simply ask your complex question or prepend it with "ai board:" and the skill will activate automatically.
