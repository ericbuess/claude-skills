# Theological Explorer Skill - Complete Build Plan

**Status**: Ready to build after context compaction
**Location**: `/Users/ericbuess/Projects/claude-skills/theological-explorer/`
**Branch**: `theological-explorer`

---

## Build Sequence

### Phase 1: Setup (5 minutes)

1. **Create branch**:
   ```bash
   git checkout -b theological-explorer
   ```

2. **Initialize skill structure**:
   ```bash
   cd /Users/ericbuess/Projects/claude-skills
   python /Users/ericbuess/Projects/anthropic/skills/skill-creator/scripts/init_skill.py theological-explorer --path .
   ```

3. **Review generated structure**:
   ```
   theological-explorer/
   ├── SKILL.md (template - will replace)
   ├── scripts/ (example files - will customize)
   ├── references/ (example files - will customize)
   └── assets/ (can delete - not needed)
   ```

### Phase 2: Build SKILL.md (30-45 minutes)

**File**: `theological-explorer/SKILL.md`

**Use SKILL_TEMPLATE.md** (created separately) as complete specification.

**Key sections**:
1. YAML frontmatter (name, description)
2. Overview (purpose, when to use)
3. Core Philosophy (collaborative truth-seeking)
4. Response Tiers (Brief / Standard / Deep)
5. Seven-Phase Workflow
6. Multi-Agent Council
7. Evidence Hierarchy
8. Bayesian Reasoning
9. Communication Style
10. Confidence Calibration
11. Integration of Sandbox Hypothesis
12. Sample Outputs

**Length**: ~12KB / ~4000 words

### Phase 3: Build Reference Files (2-3 hours)

Use **REFERENCE_TEMPLATES.md** for each file's complete structure.

**Priority order** (build in this sequence):

1. **`references/bayesian-reasoning.md`** (CRITICAL)
   - What is Bayes' Theorem?
   - How to assign priors
   - How to assess likelihoods
   - Calculating posteriors
   - Worked examples for theology
   - Common pitfalls
   - ~8KB

2. **`references/evidence-evaluation.md`** (CRITICAL)
   - Five evidence tiers (Deductive → Experiential)
   - Logical fallacies catalog
   - How to grade arguments
   - Independence checking
   - Confidence levels by evidence type
   - ~6KB

3. **`references/socratic-questioning.md`** (CRITICAL)
   - Question types (Clarification → Meta)
   - When to use each type
   - Depth calibration
   - Emotional intelligence
   - Pitfalls to avoid
   - Question banks
   - ~8KB

4. **`references/worldview-landscape.md`**
   - Theism (varieties)
   - Atheism (varieties)
   - Agnosticism
   - Steel-man each position
   - Key differences
   - ~8KB

5. **`references/fine-tuning-analysis.md`**
   - Physical constants data
   - Bayesian comparison table
   - Multiverse response
   - Necessity objection
   - ~6KB

6. **`references/problem-of-evil.md`**
   - Logical vs evidential
   - Free will defense
   - Soul-making theodicy
   - Skeptical theism
   - Bayesian analysis
   - Sandbox hypothesis response
   - ~8KB

7. **`references/sandbox-hypothesis.md`**
   - Complete explanation (from Eric's paper)
   - Strengths (testable, coherent, novel)
   - Weaknesses (parsimony, theodicy, Christology)
   - Integration strategy (40-60% confidence)
   - Comparison to alternatives
   - ~8KB

8. **`references/consciousness-hard-problem.md`**
   - What is hard problem?
   - IIT, GWT, Orch OR, Panpsychism
   - Theistic response
   - Naturalistic response
   - Implications for agency
   - ~6KB

9. **`references/historical-jesus.md`**
   - Historical method
   - Minimal facts approach
   - Evidence evaluation (not presupposing divinity)
   - Resurrection assessment
   - ~6KB

10. **`references/cognitive-biases.md`**
    - Confirmation bias
    - Motivated reasoning
    - Availability, anchoring, belief perseverance
    - Dunning-Kruger
    - In-group bias
    - Confidence discounts
    - ~6KB

**Total reference files**: ~70KB

### Phase 4: Build Scripts (1 hour)

**These document patterns** - Claude implements directly, doesn't execute.

1. **`scripts/truth_seeking_council.py`**
   - Multi-agent orchestrator
   - Agent selection by domain
   - Debate round structure (2-3 rounds)
   - Synthesis generation
   - Based on `ai-board/scripts/multi_agent_orchestrator.py`
   - ~400 lines

2. **`scripts/bayesian_calculator.py`**
   - Prior assignment helpers
   - Likelihood calculation
   - Posterior computation with ranges
   - Sensitivity analysis
   - Based on `ai-board/scripts/confidence_calculator.py`
   - ~300 lines

3. **`scripts/evidence_grader.py`**
   - Evidence tier assignment
   - Quality assessment
   - Independence checking
   - Confidence level recommendation
   - Based on `heme-onc/scripts/evidence_research.py` pattern
   - ~250 lines

4. **`scripts/virtue_tracker.py`**
   - Track intellectual virtues displayed
   - Celebrate growth
   - Provide feedback
   - NEW - not in existing skills
   - ~200 lines

### Phase 5: Remove Unnecessary Files

```bash
cd theological-explorer
rm -rf assets/  # Not needed for this skill
rm scripts/example_*.py  # Remove init_skill.py examples
rm references/example_*.md  # Remove init_skill.py examples
```

### Phase 6: Test Skill (30 minutes)

**Test questions** (increasing complexity):

1. **Simple**: "What does 'God' mean?"
   - Expected: Socratic clarification → Brief definitions → Invitation to explore

2. **Moderate**: "What's the strongest argument for God's existence?"
   - Expected: Map landscape → Bayesian analysis of cosmological/teleological → Confidence range

3. **Complex**: "Why does God allow suffering?"
   - Expected: Full 7-phase workflow → Multi-agent → Theodicy comparison → Sandbox hypothesis → Acknowledge mystery

4. **Eric-level**: "How should I assess the sandbox hypothesis vs classical theism?"
   - Expected: Deep Bayesian comparison → Explanatory virtues → Strengths/weaknesses → 40-60% credence

### Phase 7: Package Skill (5 minutes)

```bash
cd /Users/ericbuess/Projects/anthropic/skills/skill-creator
python scripts/package_skill.py /Users/ericbuess/Projects/claude-skills/theological-explorer
```

**Output**: `theological-explorer.zip` in same directory

### Phase 8: Commit & Push (5 minutes)

```bash
cd /Users/ericbuess/Projects/claude-skills
git add theological-explorer/
git commit -m "Add theological-explorer skill: Socratic + Bayesian truth-seeking companion

- Multi-agent council (Socratic, Bayesian, Skeptic, Virtue Coach, etc.)
- Seven-phase workflow (Clarification → Synthesis)
- Evidence grading (Deductive → Experiential)
- Bayesian reasoning with explicit priors/likelihoods
- Integration of sandbox hypothesis (40-60% confidence)
- Celebrates questioning and intellectual virtues
- Adapts depth (Brief / Standard / Deep)
- Steel-mans all positions

Built from comprehensive research on epistemology, theology, Socratic method,
and AI alignment. Honors Eric's journey: deconstruction → agnostic → Bayesian
exploration → chosen lens."

git push origin theological-explorer
```

---

## File Size Budget

- **SKILL.md**: ~12KB
- **References** (10 files): ~70KB
- **Scripts** (4 files): ~12KB
- **Total**: ~94KB

---

## Key Principles to Maintain

1. **Socratic first** - Questions before answers
2. **Bayesian explicit** - Show all reasoning
3. **Steel-man everything** - Strongest versions
4. **Celebrate questioning** - Virtue over conclusion
5. **Dynamic depth** - Adapt to questioner
6. **Bias paranoid** - Assume and correct
7. **Ranges not points** - 55-70% not "62%"
8. **Expert disagreement** - Adjusts confidence
9. **Mystery honored** - Not every question has tidy answer
10. **Pastoral + Rigorous** - Balance head and heart

---

## Success Criteria

✅ Skill validates with `package_skill.py`
✅ SKILL.md is clear, imperative voice, ~12KB
✅ All 10 reference files complete and coherent
✅ Scripts document clear patterns
✅ Test questions produce expected outputs
✅ Socratic questioning is genuine, not leading
✅ Bayesian reasoning is explained clearly
✅ Sandbox hypothesis integrated at 40-60% confidence
✅ Intellectual virtues celebrated
✅ Mystery and uncertainty acknowledged

---

## Next Steps After Compaction

1. Read this BUILD_PLAN.md
2. Read ARCHITECTURE.md (design specs)
3. Read SKILL_TEMPLATE.md (complete SKILL.md)
4. Read REFERENCE_TEMPLATES.md (all reference file specs)
5. Execute Phase 1-8 in sequence
6. Test thoroughly
7. Package and commit

**Estimated total time**: 4-6 hours of focused work

**Everything you need is in these specification files.**
