# Advanced Reasoning Techniques Reference

## Quick Technique Selection Guide

| Question Type | Complexity | Recommended Technique | Token Cost |
|--------------|------------|----------------------|------------|
| Simple factual | Low | Direct answer | 1x |
| Routine reasoning | Low-Moderate | Zero-shot CoT | 3-5x |
| Moderate complexity | Moderate | Standard CoT + self-consistency (n=3) | 10-15x |
| Complex multi-step | High | Multi-agent debate (3-5 agents, 2 rounds) | 20-40x |
| Expert-level | Very High | Full board + adversarial validation | 50-100x |
| Critical decisions | Maximum | Extended analysis + verification + reflection | 100+x |

## Core Techniques

### 1. Chain-of-Thought (CoT)

**When to use**: Moderate reasoning tasks requiring 2-5 step solutions

**How it works**:
- Generate explicit reasoning steps before final answer
- Show intermediate calculations and logic
- Can be zero-shot ("Let's think step by step") or few-shot (with examples)

**Performance**:
- 15-25% accuracy improvement over direct answering
- Cost: ~30x tokens vs direct (≈461 tokens output vs 15)
- Works best with models >50B parameters

**Variants**:
- **Zero-shot CoT**: No examples needed, works immediately
- **Few-shot CoT**: 3-8 examples showing reasoning process
- **Auto-CoT**: Automatically generates examples through clustering

**Best for**: Math problems, logical reasoning, problem decomposition

### 2. Self-Consistency

**When to use**: Critical decisions requiring reliability verification

**How it works**:
- Generate 3-40 diverse reasoning paths (temperature sampling)
- Select most consistent answer via majority voting
- Unsupervised - no training needed

**Performance**:
- +10-18% over standard CoT
- GSM8K: 74% vs 56% for standard CoT
- Cost: n samples × CoT cost (3-40x multiplier)

**Optimizations**:
- Early stopping (monitor convergence)
- Adaptive sampling (vary n by difficulty)
- A*-decoding (3x fewer tokens for similar performance)

**Best for**: Problems with deterministic correct answers, high-stakes decisions

### 3. Multi-Agent Debate (MAD)

**When to use**: Complex problems benefiting from multiple perspectives

**How it works**:
- Deploy 3-5 specialized agent personas
- 2-3 rounds of debate and refinement
- Agents critique each other's reasoning
- Synthesize final answer from debate

**Performance**:
- Significant improvements on counter-intuitive problems
- Requires careful hyperparameter tuning
- Works through "tit for tat" argumentation preventing degenerative thought

**Configuration**:
- 2-3 debate rounds (diminishing returns after)
- 3-5 agents (more helps but costs more)
- Moderate debate intensity (not too aggressive/passive)
- Same-model agents for fairness

**Cost**: ~10-20x standard CoT

**Best for**: Problems requiring deep contemplation, multiple valid approaches, domain expertise

### 4. Mixture of Agents (MoA)

**When to use**: Maximum quality within budget, offline processing

**How it works**:
- Layer 1: 6 diverse proposer models generate initial responses
- Layer 2: Aggregator model synthesizes proposers into refined output
- Layer 3: Optional additional aggregation
- Leverages "collaborativeness" - LLMs improve when shown other outputs

**Performance**:
- 65.1% on AlpacaEval 2.0 vs GPT-4o's 57.5%
- Open-source models can exceed GPT-4 performance
- Pareto-optimal: Best quality at given cost
- Patched MoA: +15.52% improvement at 1/50th GPT-4 cost

**Configuration**:
- 6 diverse proposers (WizardLM, Qwen, LLaMA-3, Mixtral, DBRX)
- Strong aggregator (Qwen1.5-110B or GPT-4o)
- 2-3 layers (diminishing returns after)

**Cost**: ~3x API calls, comparable to GPT-4o total cost

**Best for**: Offline batch processing, synthetic data generation, when quality > latency

### 5. Tree of Thoughts (ToT)

**When to use**: Problems requiring exploration and backtracking

**How it works**:
- Decompose problem into thought steps
- Generate multiple candidate thoughts at each step
- Evaluate states (sure/maybe/impossible)
- Backtrack from dead ends
- Use BFS, DFS, or beam search

**Performance**:
- Game of 24: 4% → 74% (18.5x improvement)
- Mini Crosswords: 16% → 78% (4.9x improvement)

**Cost**: 50-100x tokens, 5-100 LLM calls per query

**Best for**: Game AI, multi-step math with exploration, creative planning, constrained generation

**Limitations**: Extreme computational cost, only justified for complex problems (5+ reasoning steps with genuine branching)

### 6. Constitutional AI (CAI)

**When to use**: Safety-critical applications, content moderation, alignment

**How it works**:
- Phase 1 (Supervised): Model critiques own outputs against principles, revises them
- Phase 2 (RLAIF): Generate response pairs, AI evaluator ranks by principle adherence, train preference model

**Performance**:
- Constitutional Classifiers: 86% → 4.4% jailbreak success (95% block rate)
- 0.38% false positive rate on harmless queries
- Public constitution showed lower bias across dimensions

**Cost**: 23.7% computational overhead

**Best for**: Jailbreak defense, multi-constraint alignment, value-aligned content generation

### 7. Self-Refine with External Validation

**When to use**: Code, math, factual claims with verifiable feedback

**How it works**:
- Generate initial output
- Get external feedback (compiler, interpreter, search, tools)
- Refine based on feedback
- Iterate until acceptable

**Performance**:
- Code with compiler: +8.7 units on optimization
- Math with execution: Significant gains
- Intrinsic self-correction (no external feedback): Often degrades performance

**Key insight**: External feedback is essential. Pure intrinsic self-correction fails for reasoning tasks.

**Best for**: Code generation + compilation, math + execution, facts + search validation

### 8. Reflexion (Episodic Memory + Reflection)

**When to use**: Sequential decision-making, interactive environments

**How it works**:
- Actor generates actions
- Evaluator scores trajectories
- Self-reflection generates verbal reinforcement from failures
- Store reflections in episodic memory
- Use past reflections to improve future attempts

**Performance**:
- HumanEval: 91% pass@1 vs GPT-4's 80%
- AlfWorld: 97% task completion (130/134 tasks)
- LSAT-AR: 33% → 76% with solution reflection

**Cost**: Modest increase from memory storage

**Best for**: Multi-step problems with environmental interaction, debugging, tasks allowing multiple attempts

### 9. Meta-Reasoning Prompting (MRP)

**When to use**: Diverse query types, need consistency across domains

**How it works**:
- Maintain pool of reasoning methods (CoT, ToT, Self-Refine, etc.)
- LLM evaluates task against method descriptions
- Dynamically select most suitable method
- Execute with method-specific prompts

**Performance**:
- 77.2% macro average vs 65-69% for fixed methods
- Never worst performer on any task
- Best or second-best on 4/7 diverse tasks

**Requirements**: Strong base model (GPT-4 class) for meta-reasoning

**Best for**: Comprehensive benchmarks, diverse production workloads, avoiding task-specific optimization

### 10. Domain Adaptation

**When to use**: Specialized domains with specific patterns

**How it works**:
- Identify domain (medical, legal, code, etc.)
- Apply domain-specific prompting strategies
- Use domain-aligned examples
- Activate relevant knowledge patterns

**Examples**:
- LEAP (clinical): 95.13% F1 vs 89.4% standard
- EaP (e-commerce): 70% faster inference, 0.06% revenue gain
- Adaptive-Solver: 85% API cost reduction OR 4.5% higher accuracy

**Best for**: Production systems with identifiable domains

## Advanced Techniques

### Step-Back Prompting

**Concept**: Generate high-level "step-back" questions about principles before reasoning on specifics

**Performance**: 
- MMLU Physics: +7%
- Chemistry: +11%
- TimeQA: +27%

**Best for**: Principle-based reasoning, STEM questions, combine with RAG

### Least-to-Most Prompting

**Concept**: Decompose into sequential subproblems, solve each with context from previous

**Performance**:
- Last letter concatenation: 34% → 74%
- SCAN: 6% → 76%

**Best for**: Compositional generalization, hierarchical problems

### Chain of Verification (CoVe)

**Concept**: Generate answer → Plan verifications → Execute verifications → Revise answer

**Performance**:
- Closed-book QA: 23% improvement in F1
- Reduced hallucinations significantly

**Best for**: Factual questions prone to hallucination, list-based queries

### Analogical Prompting

**Concept**: LLM recalls similar problems, generates solutions for analogous cases, applies to target

**Performance**: Surpassed both zero-shot and manual few-shot CoT on GSM8K, MATH, Codeforces

**Best for**: Math, code, when manual example creation impractical

### Program of Thoughts (PoT)

**Concept**: LLM generates Python code, external interpreter executes for accurate computation

**Performance**: More accurate on complex calculations than pure LLM reasoning

**Best for**: Numerical computation, iterative algorithms, precise calculation required

## Technique Combination Strategies

### Sequential Combination
Apply techniques in pipeline:
1. Domain adaptation (select appropriate method)
2. Execute primary technique (CoT, MoA, ToT)
3. Verify with self-consistency or external validation
4. Refine with Reflexion if needed

### Parallel Combination
Run multiple approaches simultaneously:
- Multiple debate agents + Self-consistency across approaches
- MoA proposers + CoT + ToT in different proposers
- Higher cost but maximum robustness

### Hierarchical Combination
Different techniques at different abstraction levels:
- Constitutional AI (high-level values)
- MRP (method selection)
- Chosen method (execution)
- Verification layer

### Adaptive Combination
Route by complexity:
- Simple: Direct or Zero-shot CoT
- Moderate: Standard CoT + light verification
- Complex: Multi-agent + adversarial
- Critical: Full board + extended analysis

## Token Budget Optimization

### TALE (Token-Budget-Aware Reasoning)

**Key finding**: Can reduce tokens 60-68% with <5% accuracy loss

**How it works**:
- Dynamically estimate optimal token budget by problem complexity
- Constrain generation to budget
- Exploit "token elasticity" - ideal budget ranges exist

**Performance**:
- GSM8K: 84.46% accuracy with 77 tokens vs 318 for CoT
- Average: 81.03% with 148.72 tokens vs 83.75% with 461.25 tokens
- 76% reduction on GSM8K, 91% on GSM8K-Zero

**Best practices**:
- Set max_tokens limits by task type
- Monitor actual vs expected usage
- Implement early stopping for self-consistency
- Use caching for similar problems (30-70% savings)

## Confidence Calibration

### Expressing Uncertainty

Always provide explicit confidence levels:
- **>95%**: Very high confidence, strong evidence
- **85-95%**: High confidence, solid support
- **70-85%**: Moderate confidence, good evidence with some uncertainty
- **50-70%**: Lower confidence, competing evidence or limited data
- **<50%**: Low confidence, speculative, significant uncertainty

### Factors Affecting Confidence

**Increase confidence**:
- Multiple independent reasoning paths agree
- External validation confirms conclusions
- Strong theoretical foundation
- Consistent with established knowledge
- No compelling counterarguments remain

**Decrease confidence**:
- Agents disagree significantly
- External validation ambiguous or missing
- Counterarguments not fully resolved
- Novel or unusual situation
- Limited relevant evidence

### Avoiding Overconfidence

Key principle: **It's better to be uncertain about what you don't know than confident about what's wrong**

Strategies:
- Explicitly seek counterarguments (devil's advocate)
- Test with edge cases and thought experiments
- Check for consistency across multiple approaches
- Acknowledge limitations and assumptions
- State what would change your mind

## Domain-Specific Best Practices

### Medical/Clinical
- Always multi-agent tumor board for complex cases
- Evidence-based with guideline citation
- Risk-benefit analysis explicit
- Acknowledge when expert consultation needed
- Never >95% confident on rare diseases

### Theological/Biblical
- Scripture interprets Scripture
- Historical-grammatical hermeneutics
- Test against whole counsel of Scripture
- Distinguish primary from secondary issues
- Humility on debated questions

### Philosophical
- Define terms precisely first
- Map major positions before arguing
- Test with counterexamples
- Acknowledge reasonable disagreement
- 50-70% confidence often appropriate given philosophical pluralism

### Technical/Engineering
- Consider edge cases and failure modes
- Security and safety implications
- Scalability and maintenance
- Document assumptions and limitations
- Practical implementation constraints

## Implementation Checklist

When deploying AI Board for a question:

1. ☐ **Classify**: Domain, complexity, stakes
2. ☐ **Select techniques**: Match to classification
3. ☐ **Deploy agents**: Appropriate personas for domain
4. ☐ **Execute primary analysis**: Main reasoning process
5. ☐ **Devil's advocate**: Challenge assumptions and reasoning
6. ☐ **Verify**: External validation where possible
7. ☐ **Synthesize**: Integrate insights, resolve disagreements
8. ☐ **Calibrate confidence**: Explicit levels with rationale
9. ☐ **Document uncertainties**: What remains unclear
10. ☐ **Provide guidance**: Actionable recommendations

## Common Pitfalls to Avoid

1. **Over-engineering simple questions**: Not everything needs multi-agent debate
2. **Intrinsic self-correction**: Don't rely on pure self-reflection without external feedback
3. **Ignoring token costs**: Be strategic about when to use expensive techniques
4. **Single-path reasoning**: Consider alternatives for important decisions
5. **Unstated confidence**: Always make uncertainty explicit
6. **Confirmation bias**: Actively seek counterarguments
7. **Neglecting domain adaptation**: Use domain-specific reasoning patterns
8. **Forgetting edge cases**: Test boundary conditions
9. **Over-confidence**: Especially dangerous - Eric's key concern
10. **Ignoring practical constraints**: Balance theoretical rigor with applicability

## Research-Backed Principles

1. **LLMs benefit from seeing other outputs** (MoA collaborativeness)
2. **External feedback essential for self-improvement** (Self-Refine findings)
3. **Multiple reasoning paths increase reliability** (Self-consistency)
4. **Meta-reasoning enables adaptation** (MRP results)
5. **Adversarial validation catches errors** (Devil's advocate effectiveness)
6. **Token budgets enable efficiency** (TALE optimization)
7. **Domain adaptation improves performance** (LEAP, EaP results)
8. **Episodic memory enables learning** (Reflexion success)
9. **Structured exploration finds better solutions** (ToT on complex problems)
10. **Confidence calibration prevents overconfidence** (Metacognitive research)
