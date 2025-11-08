# Bayesian Reasoning for Theological Questions

This reference provides comprehensive guidance on applying Bayesian probability to theological and philosophical claims.

## Table of Contents

1. What is Bayes' Theorem?
2. How to Assign Priors
3. How to Assess Likelihoods
4. Calculating Posteriors
5. Worked Examples for Theology
6. Common Pitfalls
7. Sensitivity Analysis
8. Expert Disagreement Adjustments

---

## 1. What is Bayes' Theorem?

**Bayes' Theorem** is a mathematical formula for updating beliefs based on new evidence.

### Formula

```
P(H|E) = [P(E|H) × P(H)] / P(E)
```

Where:
- **P(H)** = Prior probability (how likely H is before seeing evidence E)
- **P(E|H)** = Likelihood (how likely E is if H is true)
- **P(E|¬H)** = Likelihood (how likely E is if H is false)
- **P(H|E)** = Posterior probability (how likely H is after seeing evidence E)
- **P(E)** = Total probability of evidence (normalizing constant)

### Expanded Form (More Useful)

```
P(H|E) = [P(E|H) × P(H)] / [P(E|H) × P(H) + P(E|¬H) × P(¬H)]
```

This version doesn't require calculating P(E) separately.

### Intuition

Bayes' Theorem formalizes common sense:
- **Prior**: What did we think before the evidence?
- **Likelihood**: How well does the evidence fit our hypothesis vs. alternatives?
- **Posterior**: What should we think after the evidence?

**Example**:
- **Prior**: 30% chance it's raining (cloudy morning)
- **Evidence**: I see wet pavement
- **Likelihood**: If raining, P(wet pavement) = 95%. If not raining, P(wet pavement) = 20% (sprinklers, dew)
- **Posterior**: P(raining | wet pavement) = [0.95 × 0.30] / [0.95 × 0.30 + 0.20 × 0.70] = 0.285 / 0.425 ≈ **67%**

Rain more likely after seeing wet pavement, but not certain (sprinklers possible).

---

## 2. How to Assign Priors

**Challenge**: Priors are subjective. Two people with different background beliefs will assign different priors.

**Strategy**: Be transparent about prior assignment and justify it.

### Method 1: Principle of Indifference

If you have **no reason** to favor one hypothesis over another, assign equal priors.

**Example**: Does consciousness emerge from matter or require immaterial soul?
- If you start agnostic, assign P(Materialism) = 50%, P(Dualism) = 50%

**Problem**: Often we DO have reasons to favor simpler hypotheses (Occam's Razor).

### Method 2: Occam's Razor (Simplicity)

**Simpler** hypotheses (fewer entities, fewer assumptions) get **higher priors**.

**Example**: God exists vs. God doesn't exist
- Naturalism: Only one type of stuff (matter/energy). Simpler ontology.
- Theism: Two types of stuff (matter + immaterial God). More complex.

**Bayesian Treatment**:
- P(Naturalism) = 60%, P(Theism) = 40% (rough starting point)
- Theism's complexity penalizes it initially, BUT evidence can overcome this penalty

**Important**: This doesn't mean naturalism is true, just that it starts with a slight advantage due to simplicity. Evidence can shift credences dramatically.

### Method 3: Reference Class

Use **base rates** from similar cases.

**Example**: Did Jesus rise from the dead?
- **Reference class**: All humans who've ever died
- **Base rate**: Resurrection rate ≈ 0 out of ~100 billion humans (excluding Jesus)
- **Prior**: P(Resurrection) << 1% (extremely low)

**BUT**: This assumes Jesus is just another human. If you assign non-negligible prior to "Jesus is God incarnate," reference class changes.

**Lesson**: Prior depends on background beliefs. Be explicit.

### Method 4: Survey Expert Opinion

If experts deeply disagree, your prior should be **modest** (not extreme).

**Example**: Theism vs. Atheism
- PhilPapers Survey (2020): ~17% theism, ~72% atheism among philosophers
- Among philosophers of religion: ~70% theism

**Bayesian Approach**: Given deep disagreement, avoid extreme priors. Starting at 20-40% for theism is reasonable, even if you lean atheist. Epistemic humility.

### Practical Guidance

**For theological claims**:
1. **Start with modest priors** (20-60%, not 0% or 100%)
2. **Justify based on**:
   - Simplicity (Occam's Razor)
   - Scope (does it explain a lot?)
   - Prior arguments (cosmological, moral arguments already shift prior?)
3. **Acknowledge subjectivity**: "My prior is X based on Y, but yours may differ"
4. **Use ranges**: "My prior for theism is 25-45%, best estimate 35%"

---

## 3. How to Assess Likelihoods

**Likelihoods** answer: "If this hypothesis were true, how likely is this evidence?"

### Key Insight: Compare Likelihoods

Bayes' Theorem is about **ratios**. What matters is how much more likely the evidence is under one hypothesis vs. another.

**Likelihood Ratio** = P(E|H) / P(E|¬H)

- **Ratio > 1**: Evidence favors H
- **Ratio < 1**: Evidence favors ¬H
- **Ratio ≈ 1**: Evidence is neutral

### Example: Fine-Tuning

**Evidence (E)**: Physical constants (gravitational constant, cosmological constant, etc.) fall within extremely narrow ranges (~1 in 10^60) necessary for life.

**Hypothesis 1 (H1)**: Theism (God designed universe for life)
- **P(Fine-Tuning | Theism)**: High (~80-95%)
  - Reasoning: If God wants to create life, He'd set constants appropriately
  - Not 100% because maybe God prefers different universes

**Hypothesis 2 (H2)**: Bare Naturalism (no God, no multiverse)
- **P(Fine-Tuning | Bare Naturalism)**: Extremely low (~10^-60)
  - Reasoning: If constants set randomly, odds of life-permitting values are astronomically low

**Likelihood Ratio** = P(E|H1) / P(E|H2) = 0.90 / 10^-60 ≈ **10^60 in favor of theism**

**Conclusion**: Fine-tuning is POWERFUL evidence for theism over bare naturalism.

**BUT**: What about multiverse?

**Hypothesis 3 (H3)**: Multiverse (many universes with different constants)
- **P(Fine-Tuning | Multiverse)**: High (~60-90%)
  - Reasoning: With infinite universes, at least one will have life-permitting constants. We observe fine-tuning because we can only exist in a life-permitting universe (selection bias).

**Likelihood Ratio** = P(E|Theism) / P(E|Multiverse) = 0.90 / 0.75 ≈ **1.2 (modest favor for theism)**

**Lesson**: Likelihoods depend on what hypotheses you're comparing. Fine-tuning strongly favors theism vs. bare naturalism, but only modestly favors theism vs. multiverse.

### Guidelines for Assessing Likelihoods

1. **Ask**: "If this hypothesis were true, would I expect to see this evidence?"
2. **Consider alternative explanations**: What else could produce this evidence?
3. **Be honest about uncertainty**: Use ranges (60-80%, not "exactly 73%")
4. **Avoid double-counting**: If E1 and E2 share a common source, don't treat them as independent

### Common Theological Likelihood Assessments

| Evidence | P(E\|Theism) | P(E\|Naturalism) | Notes |
|---|---|---|---|
| Fine-tuning | 80-95% | 10^-60 (bare) / 60-90% (multiverse) | Powerful for theism vs. bare naturalism |
| Consciousness | 70-90% | 30-60% | Depends on whether materialism can explain qualia |
| Moral realism | 75-90% | 20-40% | If objective moral values exist, theism explains better |
| Suffering | 30-50% | 60-80% | Theodicy challenges theism |
| Divine hiddenness | 20-40% | 70-90% | Why isn't God more obvious? |

**Combining Evidence**: Multiply likelihood ratios (if evidence is independent).

---

## 4. Calculating Posteriors

Once you have **P(H)**, **P(E|H)**, and **P(E|¬H)**, calculate **P(H|E)**.

### Method 1: Direct Formula

```
P(H|E) = [P(E|H) × P(H)] / [P(E|H) × P(H) + P(E|¬H) × P(¬H)]
```

**Example**: Fine-Tuning + Theism vs. Bare Naturalism

- **Prior**: P(Theism) = 30%, P(Naturalism) = 70%
- **Likelihoods**: P(Fine-Tuning | Theism) = 90%, P(Fine-Tuning | Naturalism) = 10^-60

**Posterior**:
```
P(Theism | Fine-Tuning) = [0.90 × 0.30] / [0.90 × 0.30 + 10^-60 × 0.70]
                        = 0.27 / (0.27 + ~0)
                        ≈ 99.999...%
```

**Conclusion**: Fine-tuning raises credence for theism to near-certainty IF comparing to bare naturalism.

**BUT**: If comparing theism vs. multiverse (prior 30% each, naturalism 40% split):
- P(Fine-Tuning | Multiverse) = 75%

```
P(Theism | FT) = [0.90 × 0.30] / [0.90 × 0.30 + 0.75 × 0.30 + 10^-60 × 0.40]
               = 0.27 / (0.27 + 0.225 + ~0)
               ≈ 54%
```

**Lesson**: Posterior depends heavily on what alternatives you consider.

### Method 2: Bayes Factor (Likelihood Ratio)

**Bayes Factor** = P(E|H1) / P(E|H2)

**Odds Form**:
```
Posterior Odds = Prior Odds × Bayes Factor
```

Where:
- **Odds(H)** = P(H) / P(¬H)

**Example**: Prior odds for theism = 0.30 / 0.70 ≈ 0.43
- Bayes Factor (fine-tuning) = 0.90 / 10^-60 ≈ 10^60
- Posterior Odds = 0.43 × 10^60 ≈ 4.3 × 10^59
- Posterior Probability ≈ 99.999...%

**Advantage of Odds Form**: Makes it clear how much evidence shifts beliefs.

### Method 3: Use Ranges (Recommended for Uncertainty)

Instead of point estimates, provide **ranges**.

**Example**: Resurrection

- **Prior**: P(Jesus is God incarnate) = 15-35% (my uncertainty)
- **Likelihood**: P(Resurrection reports | Jesus is God) = 60-80%
- **Likelihood**: P(Resurrection reports | Jesus is not God) = 5-15% (legendary development, hallucinations)

**Posterior (Low End)**:
- Prior 15%, P(E|H) 60%, P(E|¬H) 15%
- P(H|E) = (0.60 × 0.15) / (0.60 × 0.15 + 0.15 × 0.85) = 0.09 / 0.2175 ≈ **41%**

**Posterior (High End)**:
- Prior 35%, P(E|H) 80%, P(E|¬H) 5%
- P(H|E) = (0.80 × 0.35) / (0.80 × 0.35 + 0.05 × 0.65) = 0.28 / 0.3125 ≈ **90%**

**Final Assessment**: "Resurrection reports shift my credence for Jesus' divinity to 40-90%, depending on priors and likelihoods. My best estimate: 60-75%."

**Benefit**: Communicates uncertainty honestly, avoids false precision.

---

## 5. Worked Examples for Theology

### Example 1: Does God Exist? (Fine-Tuning Argument)

**Evidence**: Physical constants fine-tuned for life

**Step 1: Assign Priors**
- P(Theism) = 25% (penalized for complexity, but not negligible)
- P(Multiverse) = 35% (natural extension of inflationary cosmology)
- P(Bare Naturalism) = 40% (simplest ontology)

**Step 2: Assess Likelihoods**
- P(Fine-Tuning | Theism) = 85% (designer would set constants)
- P(Fine-Tuning | Multiverse) = 75% (anthropic selection)
- P(Fine-Tuning | Bare Naturalism) = 10^-60 (extremely improbable)

**Step 3: Calculate Posteriors**
```
P(Theism | FT) = (0.85 × 0.25) / (0.85 × 0.25 + 0.75 × 0.35 + 10^-60 × 0.40)
               = 0.2125 / (0.2125 + 0.2625 + ~0)
               ≈ 0.2125 / 0.475
               ≈ 45%
```

Similarly:
- P(Multiverse | FT) ≈ 55%
- P(Bare Naturalism | FT) ≈ 0%

**Interpretation**: Fine-tuning eliminates bare naturalism, but leaves theism and multiverse both plausible. Posterior credence shifts **toward** theism (+20 points), but multiverse remains viable.

---

### Example 2: Problem of Evil

**Evidence**: Extensive suffering (child cancer, tsunamis, Holocaust)

**Step 1: Assign Priors**
- P(Theism) = 45% (after fine-tuning update from Example 1)
- P(Naturalism) = 55%

**Step 2: Assess Likelihoods**
- P(Suffering | Theism) = 30% (low—why would loving God allow this?)
  - Theodicies (free will, soul-making) explain some, but not all suffering
- P(Suffering | Naturalism) = 70% (high—if no God, suffering just happens due to physics/biology)

**Step 3: Calculate Posterior**
```
P(Theism | Suffering) = (0.30 × 0.45) / (0.30 × 0.45 + 0.70 × 0.55)
                      = 0.135 / (0.135 + 0.385)
                      = 0.135 / 0.52
                      ≈ 26%
```

**Interpretation**: Suffering lowers credence for theism from 45% → 26%. This is significant evidence against theism.

**BUT**: What if Alignment Hypothesis is true?
- P(Suffering | Alignment Hypothesis) = 60% (pedagogical necessity for moral training)

Then:
```
P(Alignment Hypothesis | Suffering) = (0.60 × 0.45) / (0.60 × 0.45 + 0.70 × 0.55)
                                     = 0.27 / 0.655
                                     ≈ 41%
```

**Lesson**: Theodicy matters. Different versions of theism predict suffering differently.

---

### Example 3: Resurrection (Historical Jesus)

**Evidence**:
- E1: Empty tomb reports (all four Gospels)
- E2: Resurrection appearances (Paul's letters, Gospels)
- E3: Early church willingness to die for belief

**Hypotheses**:
- H1: Jesus rose bodily (theism)
- H2: Legend developed over decades (naturalism)
- H3: Disciples hallucinated (naturalism)

**Step 1: Priors**
- P(H1) = 20% (low due to no other resurrections in history)
- P(H2) = 40%
- P(H3) = 40%

**Step 2: Likelihoods**

| Evidence | P(E\|H1) | P(E\|H2) | P(E\|H3) |
|---|---|---|---|
| Empty tomb | 90% | 30% | 50% |
| Appearances | 95% | 20% | 70% |
| Martyrdom | 90% | 30% | 60% |

**Step 3: Combined Likelihood** (assuming independence—debatable)
- P(All E | H1) = 0.90 × 0.95 × 0.90 ≈ 77%
- P(All E | H2) = 0.30 × 0.20 × 0.30 ≈ 2%
- P(All E | H3) = 0.50 × 0.70 × 0.60 ≈ 21%

**Step 4: Posterior**
```
P(H1 | All E) = (0.77 × 0.20) / (0.77 × 0.20 + 0.02 × 0.40 + 0.21 × 0.40)
              = 0.154 / (0.154 + 0.008 + 0.084)
              = 0.154 / 0.246
              ≈ 63%
```

**Interpretation**: Evidence shifts credence for resurrection from 20% → 63%. Not certainty, but substantial.

**Critiques**:
- Independence assumption weak (if legend, all three pieces of evidence could share common source)
- Priors debatable (reference class: all humans vs. claimed Son of God?)

---

## 6. Common Pitfalls

### Pitfall 1: Base Rate Neglect

Ignoring **prior probability** and focusing only on likelihoods.

**Example**: Medical test for rare disease
- Disease affects 0.1% of population (prior)
- Test 95% accurate (likelihood)
- You test positive

**Naive**: "95% accurate, so I have 95% chance of disease"
**Correct Bayesian**: P(Disease | Positive Test) ≈ 2% (false positives dominate when disease is rare)

**Theological Application**: Don't ignore **low prior** for resurrection just because evidence (appearances) seems strong. Bayes factors matter, but so do priors.

### Pitfall 2: Ignoring Alternative Explanations

Failing to consider **P(E|¬H)** carefully.

**Example**: "Disciples died for their belief, so Jesus must have risen"
- P(Martyrdom | Resurrection) = high
- BUT: P(Martyrdom | Sincere False Belief) = also high (9/11 hijackers died for false beliefs)

**Lesson**: Evidence only supports H if P(E|H) **much greater than** P(E|¬H).

### Pitfall 3: Double-Counting Evidence

Treating **dependent** pieces of evidence as **independent**.

**Example**: Four Gospels report resurrection
- Naive: Four independent witnesses, so probability = 1 - (1-0.7)^4 ≈ 99%
- Reality: Matthew and Luke copied from Mark (synoptic problem), so NOT independent

**Lesson**: Check independence before multiplying probabilities.

### Pitfall 4: Extreme Priors (0% or 100%)

Assigning **P(H) = 0%** or **100%** makes you **unable to update**.

**Cromwell's Rule**: Never assign 0% or 100% to empirical claims.

**Example**: "I'm 100% certain God doesn't exist"
- No amount of evidence (miracles, resurrection, fine-tuning) can shift you
- This is dogmatism, not rationality

**Better**: "I'm 95% confident God doesn't exist, but I could be wrong"

### Pitfall 5: Overconfidence (False Precision)

Claiming **exact probabilities** when you're uncertain.

**Bad**: "My credence for theism is 62.37%"
**Good**: "My credence for theism is 55-70%, best estimate 62%"

**Lesson**: Use **ranges** to communicate uncertainty.

---

## 7. Sensitivity Analysis

**Sensitivity analysis** tests how much your conclusion depends on your inputs.

### Why It Matters

If your posterior is highly sensitive to small changes in priors, your conclusion is **fragile**.

**Example**: Does fine-tuning prove theism?

**Scenario A**: Prior for theism = 30%
- Posterior (after fine-tuning) ≈ 60%

**Scenario B**: Prior for theism = 10%
- Posterior (after fine-tuning) ≈ 35%

**Sensitivity**: Changing prior from 30% → 10% shifts posterior from 60% → 35%. This is **moderate sensitivity**.

**Interpretation**: Fine-tuning provides **meaningful evidence** for theism (increases credence by ~20-25 percentage points), but doesn't approach certainty. Conclusion is robust to reasonable prior variation.

### How to Perform Sensitivity Analysis

1. **Identify uncertain inputs**: Priors, likelihoods
2. **Vary them across reasonable ranges**:
   - Low estimate, middle estimate, high estimate
3. **Recalculate posterior for each scenario**
4. **Report range**: "Depending on priors (10-40%) and likelihoods (70-95% vs. 5-15%), posterior ranges from 35-85%"

**Example Output**:
> "My credence for resurrection ranges from **45-80%** depending on:
> - Prior for Jesus' divinity (15-35%)
> - Likelihood of legendary development (5-20%)
> Best estimate: **62%** (moderate confidence)"

---

## 8. Expert Disagreement Adjustments

When qualified experts deeply disagree, **reduce your confidence**.

### Why

If smart, informed people disagree after studying the evidence, that's evidence you might be missing something.

**Epistemic humility**: Acknowledge your fallibility.

### Adjustment Scale

- **Modest disagreement** (60/40 split among experts): Reduce confidence by **10%**
- **Significant disagreement** (70/30 split): Reduce by **20%**
- **Deep disagreement** (80/20 or worse split): Reduce by **30%**

**Example**: Fine-Tuning

You calculate:
- P(Theism | Fine-Tuning) = 70%

BUT:
- Cosmologists deeply disagree on multiverse (50/50 split)
- This uncertainty propagates to your posterior

**Adjusted confidence**: 70% - 20% = **50%**

**Reasoning**: If experts can't agree on multiverse viability, my 70% confidence is overconfident.

### When NOT to Adjust

Don't defer to experts who:
- Are biased (religious apologists, New Atheists with agendas)
- Are outside their domain (Stephen Hawking on philosophy, Dawkins on theology)
- Have obvious motivated reasoning

**Lesson**: Weigh expert opinion by **domain expertise + objectivity**.

---

## Summary: Bayesian Reasoning Checklist

For **every** substantive theological claim:

- [ ] **Assign Prior**: Justify based on simplicity, scope, expert opinion (use range, not point estimate)
- [ ] **Assess P(E|H)**: If hypothesis true, how likely is evidence? (use range)
- [ ] **Assess P(E|¬H)**: If hypothesis false, how likely is evidence? (use range)
- [ ] **Calculate Posterior**: Use Bayes' Theorem (provide range based on input ranges)
- [ ] **Sensitivity Analysis**: How much does posterior change if priors/likelihoods vary?
- [ ] **Expert Disagreement**: Do qualified experts disagree? Adjust confidence accordingly.
- [ ] **Communicate Uncertainty**: "My credence is 55-70%, best estimate 62%"
- [ ] **Cromwell's Rule**: Never 0% or 100%

**Goal**: Transparent, honest, rigorous reasoning that acknowledges uncertainty and invites critique.

---

**"A wise man proportions his belief to the evidence."** —David Hume

**"The goal is not certainty, but calibrated confidence."** —Bayesian Epistemology
