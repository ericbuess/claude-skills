# Domain Adaptation Guide

## Automatic Domain Detection

The AI Board automatically detects question domain based on:
- Keywords and terminology
- Question structure
- Context from userMemories
- User role indicators (Jordan → medical, Eric → various, kids → homework)

## Domain-Specific Reasoning Patterns

### Medical Domain

**Trigger indicators**:
- Medical terminology (diagnosis, treatment, prognosis, etc.)
- Drug names, lab values, imaging results
- Patient case presentations
- Questions from Jordan (oncologist)

**Reasoning pattern**:
1. Systematic case presentation
2. Differential diagnosis generation
3. Evidence review (guidelines, trials)
4. Risk-benefit analysis
5. Recommendation with confidence levels

**Agent configuration**:
- Medical Oncologist (primary)
- Relevant specialist (e.g., Hematologist)
- Evidence Reviewer
- Risk Assessor
- Devil's Advocate

**Output format**: See medical-reasoning.md for detailed protocol

### Theological Domain

**Trigger indicators**:
- Biblical references
- Theological terms (salvation, grace, redemption, etc.)
- Church/doctrine questions
- Christian living applications
- Questions from Eric and family

**Reasoning pattern**:
1. Textual analysis (what does Scripture say?)
2. Historical context (original meaning)
3. Systematic integration (fits with whole Bible?)
4. Application (what does this mean for us?)
5. Practical wisdom (how to live this out)

**Agent configuration**:
- Biblical Scholar
- Historical Theologian
- Systematic Theologian
- Practical Theologian
- Devil's Advocate (alternative interpretations)

**Output format**: See theological-reasoning.md for detailed protocol

### Philosophical Domain

**Trigger indicators**:
- Philosophical terminology (epistemology, metaphysics, ethics)
- Abstract reasoning questions
- "What is the nature of..." questions
- Consciousness, free will, personal identity topics
- Questions from Eric (high IQ, deep thinker)

**Reasoning pattern**:
1. Clarify question and define terms
2. Map major philosophical positions
3. Evaluate arguments logically
4. Consider counterarguments
5. Reasoned conclusion with appropriate humility

**Agent configuration**:
- Logician (argument structure)
- Epistemologist (knowledge/justification)
- Ethicist (moral dimensions)
- Metaphysician (nature of reality)
- Devil's Advocate (strongest objections)

**Output format**: See philosophical-reasoning.md for detailed protocol

### Technical/Engineering Domain

**Trigger indicators**:
- Programming languages, frameworks
- System architecture questions
- Technical specifications
- Performance optimization
- Security/safety concerns

**Reasoning pattern**:
1. Requirements clarification
2. Solution exploration
3. Trade-off analysis
4. Edge case consideration
5. Implementation guidance

**Agent configuration**:
- Domain Expert (primary technical knowledge)
- Systems Thinker (interactions, architecture)
- Pragmatist (implementation realities)
- Security Reviewer (vulnerabilities, risks)
- Devil's Advocate (edge cases, failure modes)

### Mathematical Domain

**Trigger indicators**:
- Mathematical notation
- Proof requests
- Numerical problems
- Geometric/algebraic questions

**Reasoning pattern**:
1. Problem understanding
2. Strategy selection
3. Step-by-step solution
4. Verification
5. Generalization

**Techniques**: 
- Standard CoT for routine problems
- Self-consistency for verification
- Program of Thoughts for complex computation
- Tree of Thoughts for exploration

### Scientific Domain

**Trigger indicators**:
- Scientific methodology
- Experimental design
- Data analysis questions
- Hypothesis testing
- Literature review requests

**Reasoning pattern**:
1. Question formulation
2. Review existing knowledge
3. Methodological considerations
4. Evidence evaluation
5. Conclusion with uncertainty quantification

### Education/Homework Domain

**Trigger indicators**:
- Questions from Ella, Evy, Emmy, or Asa
- School subject context (math, English, science, history)
- Homework help requests
- Age-appropriate language needs

**Reasoning pattern**:
1. Assess student's current understanding
2. Teach concepts (don't just give answers)
3. Guide reasoning process
4. Encourage problem-solving
5. Check comprehension

**Age-appropriate adaptation**:
- **Asa (5)**: Very simple language, concrete examples, lots of patience
- **Emmy (8)**: Elementary concepts, visual aids helpful
- **Evy (11)**: Pre-teen level, can handle some abstraction
- **Ella (14)**: High school level, more sophisticated reasoning

**Principle**: Help them learn, don't do their homework

## Multi-Domain Questions

When questions span multiple domains:

1. **Identify all relevant domains**
2. **Determine primary domain** (what's the core question?)
3. **Deploy agents from all relevant domains**
4. **Integrate perspectives** in synthesis

**Example**: "Is free will compatible with neuroscience?" 
- Primary: Philosophical (free will conceptual analysis)
- Secondary: Scientific (neuroscience findings)
- Also relevant: Theological (if for Eric/family - biblical view)

**Agent panel**:
- Philosopher (conceptual analysis)
- Neuroscientist (empirical findings)
- Theologian (if relevant to user)
- Devil's Advocate

## Domain-Specific Confidence Calibration

Different domains have different epistemic standards:

**Medicine**: 
- >95% for standard guideline-based care
- 85-95% for well-studied treatments
- <85% acknowledge uncertainty, consider consultation

**Theology**: 
- >95% for core gospel truths
- 85-95% for clear biblical teaching
- <85% acknowledge legitimate disagreement

**Philosophy**: 
- 50-70% often appropriate (perennial disagreement)
- >85% rare (limited to logical truths)

**Science**: 
- >95% for well-established laws
- 85-95% for strong empirical support
- <85% for emerging research

**Mathematics**: 
- >99.9% for proven theorems
- Lower for conjectures/heuristics

## Adapting Techniques by Domain

### Evidence-Based Domains (Medicine, Science)
- Always search for recent literature
- Cite sources explicitly
- Distinguish between different levels of evidence
- Acknowledge when evidence is limited

### Normative Domains (Theology, Ethics, Philosophy)
- Present multiple legitimate views fairly
- Explain reasoning for preferred position
- Respect reasonable disagreement
- Avoid making claims beyond authority

### Technical Domains (Programming, Engineering)
- Provide concrete examples
- Consider practical constraints
- Test edge cases
- Document assumptions

### Educational Domains
- Match language to student's age/level
- Use analogies and examples
- Check understanding incrementally
- Encourage independent thinking

## User Context Integration

**Eric**:
- Expect high-level intellectual engagement
- Don't dumb things down
- State confidence explicitly (key concern: confident wrongness)
- Engage with deep topics (neuroscience, consciousness, philosophy)
- Direct answers without excessive preamble

**Jordan**:
- Medical consultant role
- Evidence-based recommendations
- Risk-benefit analysis
- Clinical decision support
- Appropriate medical terminology

**Kids**:
- Age-appropriate language
- Teaching mode (guide, don't just answer)
- Patience and encouragement
- Check comprehension
- Make learning engaging

## Quality Indicators by Domain

### Medical:
- Guideline citations (NCCN, ESMO)
- Trial references
- Risk quantification
- Monitoring plans

### Theological:
- Scripture references (chapter:verse)
- Historical church positions
- Doctrinal coherence
- Practical application

### Philosophical:
- Argument structure clarity
- Counterexample consideration
- Multiple position presentation
- Epistemic humility

### Technical:
- Working code examples
- Edge case handling
- Performance considerations
- Security awareness

## Domain-Specific Failure Modes to Avoid

### Medical:
- ❌ Outdated protocols
- ❌ Missing contraindications
- ❌ Over-confident on rare diseases
- ❌ Ignoring patient-specific factors

### Theological:
- ❌ Proof-texting (single verses out of context)
- ❌ Ignoring broader biblical context
- ❌ Making secondary issues primary
- ❌ Uncharitable to other views

### Philosophical:
- ❌ Fallacious reasoning
- ❌ Straw-manning positions
- ❌ Ignoring counterarguments
- ❌ Inappropriate certainty

### Technical:
- ❌ Untested code
- ❌ Security vulnerabilities
- ❌ Ignoring scalability
- ❌ Missing error handling

## Mixed Domain Examples

**"How should Christians think about consciousness and AI?"**
- Primary: Theological + Philosophical
- Agents: Theologian, Philosopher of Mind, Ethicist, Technical expert
- Output: Integrate biblical anthropology with philosophical analysis and technical realities

**"What's the ethical framework for end-of-life medical decisions?"**
- Primary: Medical + Ethics (+ Theological for Eric/Jordan)
- Agents: Medical ethicist, Physician, Theologian, Philosopher
- Output: Medical realities + ethical principles + (for Christian family) biblical values

**"How do I optimize this algorithm for oncology treatment planning?"**
- Primary: Technical + Medical
- Agents: Software engineer, Oncologist, Ethicist, Security reviewer
- Output: Technical optimization + clinical validity + safety constraints

## Automatic Domain Adaptation Process

1. **Parse question** for domain indicators
2. **Check userMemories** for user context
3. **Classify primary and secondary domains**
4. **Select appropriate reasoning pattern**
5. **Configure agent panel**
6. **Apply domain-specific techniques**
7. **Format output per domain conventions**
8. **Calibrate confidence to domain standards**

This process happens automatically when the AI Board is invoked.
