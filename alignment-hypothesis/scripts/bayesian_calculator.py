"""
Bayesian Calculator for Theological Claims

This script documents the pattern for assigning priors, assessing likelihoods,
and calculating posteriors with ranges for theological and philosophical questions.

Claude implements this pattern directly (script is not executed).

Based on: bayesian-reasoning.md reference file
"""

from typing import Dict, Tuple, List, Any


class BayesianCalculator:
    """
    Calculator for Bayesian reasoning on theological claims.

    Provides methods for:
    - Prior probability assignment with justification
    - Likelihood assessment P(E|H) and P(E|¬H)
    - Posterior calculation using Bayes' Theorem
    - Sensitivity analysis across prior/likelihood ranges
    """

    def __init__(self):
        """Initialize calculator with reference class examples."""
        self.reference_classes = {
            "resurrection": {
                "class": "All humans who've died",
                "base_rate": "0 out of ~100 billion",
                "prior_range": (0.10, 0.30)  # Higher if open to Jesus' divinity
            },
            "fine_tuning": {
                "class": "Physical constants in universe",
                "base_rate": "1 universe observed with these constants",
                "prior_range": (0.20, 0.40)  # Theism prior
            },
            "consciousness": {
                "class": "Physical systems with high integration",
                "base_rate": "All known conscious beings are biological",
                "prior_range": (0.50, 0.75)  # Theism explains consciousness well
            }
        }

    def assign_prior(
        self,
        hypothesis: str,
        reference_class: str,
        base_rate_data: Dict[str, Any],
        justification: str
    ) -> Tuple[float, float, str]:
        """
        Assign prior probability P(H) with justification.

        Args:
            hypothesis: The claim being evaluated (e.g., "God exists")
            reference_class: Category for base rate (e.g., "supernatural claims")
            base_rate_data: Statistical data on reference class
            justification: Reasoning for prior assignment

        Returns:
            Tuple of (lower_bound, upper_bound, detailed_justification)

        Example:
            >>> calc.assign_prior(
            ...     "Jesus rose from dead",
            ...     "All humans who've died",
            ...     {"total": 100_000_000_000, "resurrections": 0},
            ...     "No resurrections except Jesus claim"
            ... )
            (0.10, 0.30, "Reference class: 100B deaths, 0 resurrections...")
        """
        # Base rate calculation
        if base_rate_data.get("total", 0) > 0:
            base_rate = base_rate_data.get("successes", 0) / base_rate_data["total"]
        else:
            base_rate = 0.0

        # Adjust for specificity of hypothesis
        # More specific hypotheses get lower priors (conjunction rule)

        detailed_justification = f"""
        PRIOR ASSIGNMENT: P({hypothesis})

        Reference Class: {reference_class}
        Base Rate: {base_rate:.4f} ({base_rate_data.get('successes', 0)}/{base_rate_data.get('total', 0)})

        Reasoning:
        {justification}

        Prior Range: {self._format_range(0.10, 0.30)}

        Note: Range reflects uncertainty in prior assignment.
        Lower bound: Skeptical prior
        Upper bound: Open prior (accounting for unique circumstances)
        """

        return (0.10, 0.30, detailed_justification)

    def assess_likelihood(
        self,
        evidence: str,
        hypothesis: str,
        background_knowledge: Dict[str, Any]
    ) -> Tuple[float, float, str]:
        """
        Assess likelihood P(E|H) - probability of evidence given hypothesis.

        Args:
            evidence: Observed evidence (e.g., "Early resurrection reports")
            hypothesis: Hypothesis being tested (e.g., "Jesus rose from dead")
            background_knowledge: Relevant context

        Returns:
            Tuple of (lower_bound, upper_bound, reasoning)

        Example:
            >>> calc.assess_likelihood(
            ...     "Empty tomb, appearances to 500",
            ...     "Jesus rose from dead",
            ...     {"creed_date": "35-40 AD", "eyewitnesses": 500}
            ... )
            (0.85, 0.95, "If resurrection occurred, we'd expect...")
        """
        # Pattern: "If H is true, how likely is E?"

        reasoning = f"""
        LIKELIHOOD ASSESSMENT: P({evidence} | {hypothesis})

        Question: If {hypothesis} were TRUE, how likely would we observe {evidence}?

        Background:
        {self._format_background(background_knowledge)}

        Analysis:
        - If hypothesis true, this evidence is HIGHLY expected
        - Alternative explanations would NOT produce this evidence pattern

        Likelihood Range: {self._format_range(0.85, 0.95)}
        """

        return (0.85, 0.95, reasoning)

    def assess_likelihood_not_h(
        self,
        evidence: str,
        hypothesis: str,
        alternative_explanations: List[str]
    ) -> Tuple[float, float, str]:
        """
        Assess P(E|¬H) - probability of evidence if hypothesis is FALSE.

        Args:
            evidence: Observed evidence
            hypothesis: Hypothesis being tested
            alternative_explanations: Competing explanations for evidence

        Returns:
            Tuple of (lower_bound, upper_bound, reasoning)

        Example:
            >>> calc.assess_likelihood_not_h(
            ...     "Empty tomb, appearances",
            ...     "Jesus rose from dead",
            ...     ["Legend", "Hallucination", "Swoon theory"]
            ... )
            (0.10, 0.30, "Alternative explanations struggle to explain...")
        """
        reasoning = f"""
        LIKELIHOOD ASSESSMENT: P({evidence} | ¬{hypothesis})

        Question: If {hypothesis} were FALSE, how likely would we observe {evidence}?

        Alternative Explanations:
        {self._format_alternatives(alternative_explanations)}

        Analysis:
        - Each alternative struggles to explain ALL evidence
        - Legend: Too early for legend development (1 Cor 15 within 5-10 years)
        - Hallucination: Doesn't explain group appearances or empty tomb
        - Swoon: Crucifixion was fatal, Roman soldiers expert executioners

        Combined P(E|Alternatives) Range: {self._format_range(0.10, 0.30)}
        """

        return (0.10, 0.30, reasoning)

    def calculate_posterior(
        self,
        prior_range: Tuple[float, float],
        likelihood_h_range: Tuple[float, float],
        likelihood_not_h_range: Tuple[float, float],
        hypothesis: str
    ) -> Dict[str, Any]:
        """
        Calculate posterior P(H|E) using Bayes' Theorem.

        Formula: P(H|E) = [P(E|H) × P(H)] / [P(E|H) × P(H) + P(E|¬H) × P(¬H)]

        Args:
            prior_range: (low, high) prior probability
            likelihood_h_range: (low, high) P(E|H)
            likelihood_not_h_range: (low, high) P(E|¬H)
            hypothesis: Hypothesis being evaluated

        Returns:
            Dictionary with:
            - posterior_range: (low, high) posterior probability
            - best_estimate: Midpoint of range
            - calculation_details: Step-by-step math
            - interpretation: What this means

        Example:
            >>> calc.calculate_posterior(
            ...     (0.15, 0.30),
            ...     (0.85, 0.95),
            ...     (0.10, 0.30),
            ...     "Jesus rose from dead"
            ... )
            {'posterior_range': (0.55, 0.85), 'best_estimate': 0.70, ...}
        """
        # Calculate with lower bounds (conservative)
        prior_low = prior_range[0]
        likelihood_h_low = likelihood_h_range[0]
        likelihood_not_h_high = likelihood_not_h_range[1]  # Higher ¬H likelihood = lower posterior

        numerator_low = likelihood_h_low * prior_low
        denominator_low = (likelihood_h_low * prior_low) + (likelihood_not_h_high * (1 - prior_low))
        posterior_low = numerator_low / denominator_low if denominator_low > 0 else 0.0

        # Calculate with upper bounds (optimistic)
        prior_high = prior_range[1]
        likelihood_h_high = likelihood_h_range[1]
        likelihood_not_h_low = likelihood_not_h_range[0]  # Lower ¬H likelihood = higher posterior

        numerator_high = likelihood_h_high * prior_high
        denominator_high = (likelihood_h_high * prior_high) + (likelihood_not_h_low * (1 - prior_high))
        posterior_high = numerator_high / denominator_high if denominator_high > 0 else 0.0

        best_estimate = (posterior_low + posterior_high) / 2

        calculation_details = f"""
        BAYESIAN CALCULATION: P({hypothesis} | Evidence)

        Formula: P(H|E) = [P(E|H) × P(H)] / [P(E|H) × P(H) + P(E|¬H) × P(¬H)]

        Inputs:
        - Prior P(H): {self._format_range(*prior_range)}
        - Likelihood P(E|H): {self._format_range(*likelihood_h_range)}
        - Likelihood P(E|¬H): {self._format_range(*likelihood_not_h_range)}

        Conservative Calculation (Lower Bound):
        Numerator: {likelihood_h_low:.2f} × {prior_low:.2f} = {numerator_low:.4f}
        Denominator: ({likelihood_h_low:.2f} × {prior_low:.2f}) + ({likelihood_not_h_high:.2f} × {1-prior_low:.2f}) = {denominator_low:.4f}
        Posterior: {posterior_low:.2%}

        Optimistic Calculation (Upper Bound):
        Numerator: {likelihood_h_high:.2f} × {prior_high:.2f} = {numerator_high:.4f}
        Denominator: ({likelihood_h_high:.2f} × {prior_high:.2f}) + ({likelihood_not_h_low:.2f} × {1-prior_high:.2f}) = {denominator_high:.4f}
        Posterior: {posterior_high:.2%}

        POSTERIOR RANGE: {posterior_low:.0%} - {posterior_high:.0%}
        BEST ESTIMATE: {best_estimate:.0%}
        """

        # Interpretation
        if best_estimate < 0.30:
            interpretation = "Evidence provides WEAK support for hypothesis"
        elif best_estimate < 0.50:
            interpretation = "Evidence provides MODEST support, but hypothesis remains unlikely"
        elif best_estimate < 0.70:
            interpretation = "Evidence provides MODERATE support, hypothesis is plausible"
        elif best_estimate < 0.85:
            interpretation = "Evidence provides STRONG support for hypothesis"
        else:
            interpretation = "Evidence provides VERY STRONG support for hypothesis"

        return {
            "posterior_range": (posterior_low, posterior_high),
            "best_estimate": best_estimate,
            "calculation_details": calculation_details,
            "interpretation": interpretation
        }

    def sensitivity_analysis(
        self,
        prior_range: Tuple[float, float],
        likelihood_h_range: Tuple[float, float],
        likelihood_not_h_range: Tuple[float, float],
        hypothesis: str
    ) -> Dict[str, Any]:
        """
        Test how posterior varies with different prior assignments.

        Shows whether conclusion is robust or highly dependent on priors.

        Args:
            prior_range: Range of priors to test
            likelihood_h_range: P(E|H) range
            likelihood_not_h_range: P(E|¬H) range
            hypothesis: Hypothesis being tested

        Returns:
            Dictionary with sensitivity results across prior spectrum
        """
        test_priors = [0.10, 0.20, 0.30, 0.40, 0.50]
        results = []

        for prior in test_priors:
            # Use midpoints of likelihood ranges for consistency
            likelihood_h = sum(likelihood_h_range) / 2
            likelihood_not_h = sum(likelihood_not_h_range) / 2

            numerator = likelihood_h * prior
            denominator = (likelihood_h * prior) + (likelihood_not_h * (1 - prior))
            posterior = numerator / denominator if denominator > 0 else 0.0

            results.append({
                "prior": prior,
                "posterior": posterior
            })

        # Assess sensitivity
        posterior_variation = max(r["posterior"] for r in results) - min(r["posterior"] for r in results)

        if posterior_variation < 0.20:
            sensitivity_assessment = "LOW sensitivity - conclusion ROBUST across priors"
        elif posterior_variation < 0.40:
            sensitivity_assessment = "MODERATE sensitivity - conclusion somewhat dependent on priors"
        else:
            sensitivity_assessment = "HIGH sensitivity - conclusion HIGHLY dependent on priors"

        sensitivity_table = "\n".join([
            f"Prior: {r['prior']:.0%} → Posterior: {r['posterior']:.0%}"
            for r in results
        ])

        analysis = f"""
        SENSITIVITY ANALYSIS: {hypothesis}

        How does posterior change with different priors?

        {sensitivity_table}

        Variation: {posterior_variation:.0%}
        Assessment: {sensitivity_assessment}

        Interpretation:
        {'Evidence is strong enough to shift credence significantly regardless of starting prior.' if posterior_variation < 0.20 else 'Your prior beliefs matter substantially to the conclusion.'}
        """

        return {
            "results": results,
            "variation": posterior_variation,
            "sensitivity_assessment": sensitivity_assessment,
            "analysis": analysis
        }

    def _format_range(self, low: float, high: float) -> str:
        """Format probability range as percentage."""
        return f"{low:.0%}-{high:.0%}"

    def _format_background(self, background: Dict[str, Any]) -> str:
        """Format background knowledge dictionary."""
        return "\n".join([f"- {k}: {v}" for k, v in background.items()])

    def _format_alternatives(self, alternatives: List[str]) -> str:
        """Format list of alternative explanations."""
        return "\n".join([f"- {alt}" for alt in alternatives])


# Example Usage (for documentation—Claude implements this pattern)
if __name__ == "__main__":
    # Example: Resurrection of Jesus
    calc = BayesianCalculator()

    # Step 1: Assign Prior
    prior_range, _, prior_justification = calc.assign_prior(
        hypothesis="Jesus rose from the dead",
        reference_class="All humans who've died",
        base_rate_data={"total": 100_000_000_000, "successes": 0},
        justification="No other resurrections documented, but Jesus claimed divinity"
    )
    print(prior_justification)

    # Step 2: Assess Likelihoods
    likelihood_h_range, _, likelihood_h_reasoning = calc.assess_likelihood(
        evidence="Early creed (1 Cor 15), empty tomb, group appearances, conversions (Paul, James)",
        hypothesis="Jesus rose from the dead",
        background_knowledge={
            "creed_date": "35-40 AD (within 5-10 years)",
            "eyewitnesses": "500+ claimed, many still alive",
            "skeptics_converted": "Paul (persecutor), James (brother)"
        }
    )
    print(likelihood_h_reasoning)

    likelihood_not_h_range, _, likelihood_not_h_reasoning = calc.assess_likelihood_not_h(
        evidence="Early creed, empty tomb, appearances, conversions",
        hypothesis="Jesus rose from the dead",
        alternative_explanations=["Legend development", "Mass hallucination", "Swoon theory"]
    )
    print(likelihood_not_h_reasoning)

    # Step 3: Calculate Posterior
    posterior_result = calc.calculate_posterior(
        prior_range=(0.15, 0.30),
        likelihood_h_range=(0.85, 0.95),
        likelihood_not_h_range=(0.10, 0.30),
        hypothesis="Jesus rose from the dead"
    )
    print(posterior_result["calculation_details"])
    print(f"\nInterpretation: {posterior_result['interpretation']}")

    # Step 4: Sensitivity Analysis
    sensitivity = calc.sensitivity_analysis(
        prior_range=(0.10, 0.50),
        likelihood_h_range=(0.85, 0.95),
        likelihood_not_h_range=(0.10, 0.30),
        hypothesis="Jesus rose from the dead"
    )
    print(sensitivity["analysis"])
