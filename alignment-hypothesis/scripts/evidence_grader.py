"""
Evidence Grader for Theological Arguments

This script documents the pattern for assigning evidence to the 5-tier hierarchy,
checking for logical fallacies, and assessing independence of evidence sources.

Claude implements this pattern directly (script is not executed).

Based on: evidence-evaluation.md reference file
"""

from typing import Dict, List, Tuple, Any


class EvidenceGrader:
    """
    Grades evidence quality using 5-tier hierarchy.

    Tiers:
    1. Deductive (95-99% if sound)
    2. Strong Inductive (75-90%)
    3. Abductive (60-80%)
    4. Testimonial (40-80%, highly variable)
    5. Experiential (30-90% for self, 20-50% for others)
    """

    # Evidence Tier Definitions
    TIERS = {
        1: {
            "name": "Deductive",
            "confidence_range": (0.95, 0.99),
            "description": "Logically valid argument with true premises",
            "examples": [
                "Mathematical proofs",
                "Logical syllogisms (if premises true)"
            ],
            "weakness": "Requires certainty about premises"
        },
        2: {
            "name": "Strong Inductive",
            "confidence_range": (0.75, 0.90),
            "description": "Large sample, well-controlled, repeatable",
            "examples": [
                "Scientific experiments (RCTs)",
                "Meta-analyses",
                "Physical constants data"
            ],
            "weakness": "Assumes past patterns continue"
        },
        3: {
            "name": "Abductive",
            "confidence_range": (0.40, 0.70),
            "description": "Inference to best explanation",
            "examples": [
                "Fine-tuning argument",
                "Inference to design",
                "Historical reconstructions"
            ],
            "weakness": "Depends on completeness of hypothesis space"
        },
        4: {
            "name": "Testimonial",
            "confidence_range": (0.40, 0.80),
            "description": "Reports from witnesses (highly variable)",
            "examples": [
                "Resurrection reports (1 Cor 15)",
                "Near-death experiences",
                "Answered prayer testimonies"
            ],
            "weakness": "Memory errors, bias, fabrication possible"
        },
        5: {
            "name": "Experiential",
            "confidence_range": (0.50, 0.80),
            "description": "Personal subjective experience (first-person)",
            "examples": [
                "Mystical experiences",
                "Sense of God's presence",
                "Qualia (subjective consciousness)"
            ],
            "weakness": "Not independently verifiable, interpretation-laden. Note: Range for first-person; reduce to (0.20, 0.50) for second-hand reports."
        }
    }

    # Logical Fallacies Catalog
    FALLACIES = {
        "ad_hominem": {
            "name": "Ad Hominem",
            "pattern": "Attacking person instead of argument",
            "example": "Dawkins is arrogant, so atheism is false",
            "detection": "Check if argument targets character vs. claim"
        },
        "straw_man": {
            "name": "Straw Man",
            "pattern": "Misrepresenting opponent's position",
            "example": "Theists believe in sky wizard granting wishes",
            "detection": "Would opponent recognize this as their view?"
        },
        "false_dilemma": {
            "name": "False Dilemma",
            "pattern": "Only two options when more exist",
            "example": "Either Bible is inerrant or it's worthless",
            "detection": "Are there middle positions being ignored?"
        },
        "appeal_to_authority": {
            "name": "Appeal to Authority",
            "pattern": "X says it, therefore it's true",
            "example": "Einstein believed in God, so theism is true",
            "detection": "Is authority qualified in this domain?"
        },
        "appeal_to_ignorance": {
            "name": "Appeal to Ignorance",
            "pattern": "Not proven false, therefore true",
            "example": "Can't disprove God, so God exists",
            "detection": "Burden of proof shifted improperly?"
        },
        "circular_reasoning": {
            "name": "Circular Reasoning",
            "pattern": "Conclusion assumed in premise",
            "example": "Bible is true because it says it's God's Word",
            "detection": "Does argument presuppose its conclusion?"
        },
        "post_hoc": {
            "name": "Post Hoc Ergo Propter Hoc",
            "pattern": "After this, therefore because of this",
            "example": "I prayed, then recovered, so prayer caused healing",
            "detection": "Is correlation confused with causation?"
        },
        "hasty_generalization": {
            "name": "Hasty Generalization",
            "pattern": "Small sample to broad conclusion",
            "example": "I met a mean atheist, so atheists are mean",
            "detection": "Is sample size adequate for conclusion?"
        },
        "special_pleading": {
            "name": "Special Pleading",
            "pattern": "Exempting own view from standard applied to others",
            "example": "Everything needs cause except God",
            "detection": "Are standards applied consistently?"
        },
        "texas_sharpshooter": {
            "name": "Texas Sharpshooter",
            "pattern": "Cherry-picking data to fit conclusion",
            "example": "Bible predicted [selective hits], ignore [misses]",
            "detection": "Are negative cases being ignored?"
        }
    }

    def assign_tier(
        self,
        evidence_description: str,
        argument_type: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Assign evidence to one of 5 tiers.

        Args:
            evidence_description: Description of the evidence
            argument_type: Type of argument being made
            context: Additional context (sample size, controls, etc.)

        Returns:
            Dictionary with tier assignment, confidence range, reasoning

        Example:
            >>> grader.assign_tier(
            ...     "1 Cor 15:3-7 resurrection creed",
            ...     "Historical testimony",
            ...     {"date": "35-40 AD", "eyewitnesses": 500}
            ... )
            {'tier': 4, 'name': 'Testimonial', 'confidence': (0.65, 0.80), ...}
        """
        # Decision tree for tier assignment

        # Tier 1: Deductive
        if argument_type in ["mathematical_proof", "logical_syllogism", "deductive"]:
            tier = 1
            confidence = (0.95, 0.99)
            reasoning = f"""
            TIER 1: DEDUCTIVE (95-99%)

            Evidence: {evidence_description}
            Type: {argument_type}

            Characteristics:
            - Logically valid structure
            - If premises true, conclusion MUST be true
            - Certainty limited only by premise certainty

            Confidence: {self._format_range(*confidence)}

            Note: Deductive arguments are only as strong as their premises.
            """

        # Tier 2: Strong Inductive
        elif argument_type in ["scientific_experiment", "rct", "meta_analysis", "physical_constants"]:
            tier = 2
            confidence = (0.75, 0.90)
            reasoning = f"""
            TIER 2: STRONG INDUCTIVE (75-90%)

            Evidence: {evidence_description}
            Type: {argument_type}

            Characteristics:
            - Large sample size: {context.get('sample_size', 'N/A')}
            - Well-controlled: {context.get('controls', 'Yes')}
            - Repeatable: {context.get('repeatable', 'Yes')}

            Confidence: {self._format_range(*confidence)}

            Limitation: Assumes future resembles past (problem of induction)
            """

        # Tier 3: Abductive
        elif argument_type in ["inference_to_best_explanation", "abductive", "fine_tuning", "design_inference"]:
            tier = 3
            confidence = (0.40, 0.70)
            reasoning = f"""
            TIER 3: ABDUCTIVE (40-70%)

            Evidence: {evidence_description}
            Type: {argument_type}

            Characteristics:
            - Inference to best explanation
            - Compares explanatory power of competing hypotheses
            - Criteria: Scope, precision, coherence, simplicity, fecundity

            Competing Hypotheses: {context.get('alternatives', 'N/A')}

            Confidence: {self._format_range(*confidence)}

            Limitation: Only as strong as hypothesis space is complete
            """

        # Tier 4: Testimonial
        elif argument_type in ["testimony", "witness_report", "historical_document", "answered_prayer"]:
            # Variable quality based on factors
            early = context.get("early", False)
            eyewitness = context.get("eyewitness", False)
            multiple_sources = context.get("multiple_sources", False)
            embarrassment = context.get("embarrassment", False)

            # Adjust confidence based on quality factors
            base_confidence = 0.50
            if early:
                base_confidence += 0.10
            if eyewitness:
                base_confidence += 0.10
            if multiple_sources:
                base_confidence += 0.10
            if embarrassment:
                base_confidence += 0.10

            tier = 4
            confidence = (max(0.40, base_confidence - 0.10), min(0.80, base_confidence + 0.10))

            reasoning = f"""
            TIER 4: TESTIMONIAL ({self._format_range(*confidence)})

            Evidence: {evidence_description}
            Type: {argument_type}

            Quality Factors:
            - Early (within years of event): {early}
            - Eyewitness (not hearsay): {eyewitness}
            - Multiple independent sources: {multiple_sources}
            - Embarrassment criterion: {embarrassment}

            Base Confidence: {base_confidence:.0%}
            Adjusted Range: {self._format_range(*confidence)}

            Limitation: Memory errors, bias, fabrication possible
            """

        # Tier 5: Experiential
        elif argument_type in ["personal_experience", "mystical_experience", "qualia", "religious_experience"]:
            first_person = context.get("first_person", False)
            tier = 5

            if first_person:
                confidence = (0.50, 0.80)  # High for self, but interpretation-laden
            else:
                confidence = (0.20, 0.50)  # Low for others' experiences

            reasoning = f"""
            TIER 5: EXPERIENTIAL ({self._format_range(*confidence)})

            Evidence: {evidence_description}
            Type: {argument_type}

            First-Person: {first_person}

            Characteristics:
            - Subjective, not independently verifiable
            - Interpretation-laden (shaped by prior beliefs)
            - High confidence for self, low transferability to others

            Confidence: {self._format_range(*confidence)}

            Limitation: "The person who has an experience knows it's real. The person who hasn't cannot be convinced."
            """

        else:
            # Default: Abductive (middle tier)
            tier = 3
            confidence = (0.50, 0.70)
            reasoning = f"""
            TIER 3: ABDUCTIVE (DEFAULT) ({self._format_range(*confidence)})

            Evidence: {evidence_description}
            Type: {argument_type} (not clearly categorized)

            Defaulting to middle tier. Manual review recommended.
            """

        return {
            "tier": tier,
            "tier_name": self.TIERS[tier]["name"],
            "confidence_range": confidence,
            "reasoning": reasoning,
            "quality_factors": context
        }

    def check_fallacies(self, argument: str, context: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Detect logical fallacies in argument.

        Args:
            argument: The argument to check
            context: Additional context (opposing view, etc.)

        Returns:
            List of detected fallacies with explanations

        Example:
            >>> grader.check_fallacies(
            ...     "Dawkins is arrogant, so atheism is wrong",
            ...     {}
            ... )
            [{'fallacy': 'Ad Hominem', 'explanation': '...'}]
        """
        detected_fallacies = []

        # Pattern matching for fallacies (simplified - Claude uses deeper reasoning)

        # Ad Hominem
        if any(word in argument.lower() for word in ["arrogant", "stupid", "biased", "evil"]):
            detected_fallacies.append({
                "fallacy": "Ad Hominem (possible)",
                "explanation": "Argument may attack person instead of position. Check: Does argument address claim or character?",
                "severity": "medium"
            })

        # Straw Man
        opponent_view = context.get("opponent_view", "")
        if opponent_view and "believe" in argument.lower():
            detected_fallacies.append({
                "fallacy": "Straw Man (possible)",
                "explanation": "Check if opponent's view is being misrepresented. Would they recognize this as their position?",
                "severity": "medium"
            })

        # False Dilemma
        if "either" in argument.lower() and "or" in argument.lower():
            detected_fallacies.append({
                "fallacy": "False Dilemma (possible)",
                "explanation": "Argument presents binary choice. Check: Are there middle positions being ignored?",
                "severity": "medium"
            })

        # Circular Reasoning
        if context.get("conclusion") and context.get("conclusion").lower() in argument.lower():
            detected_fallacies.append({
                "fallacy": "Circular Reasoning (possible)",
                "explanation": "Conclusion may be assumed in premise. Check: Is argument presupposing what it's trying to prove?",
                "severity": "high"
            })

        return detected_fallacies

    def check_independence(self, evidence_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Check if pieces of evidence are truly independent.

        Non-independent evidence should NOT be multiplied in Bayesian calculations.

        Args:
            evidence_list: List of evidence pieces with metadata

        Returns:
            Dictionary with independence assessment

        Example:
            >>> grader.check_independence([
            ...     {"source": "Gospel of Matthew", "content": "Empty tomb"},
            ...     {"source": "Gospel of Mark", "content": "Empty tomb"},
            ...     {"source": "Gospel of Luke", "content": "Empty tomb"}
            ... ])
            {'independent': False, 'reason': 'Synoptic problem - Matthew and Luke use Mark', ...}
        """
        # Check for shared sources
        sources = [e.get("source", "") for e in evidence_list]

        # Synoptic Gospels dependency
        if "Gospel of Matthew" in sources and "Gospel of Mark" in sources and "Gospel of Luke" in sources:
            return {
                "independent": False,
                "reason": "Synoptic problem: Matthew and Luke likely used Mark as source",
                "true_independent_count": 2,  # Mark + John (if present)
                "correction": "Treat Matthew, Mark, Luke as ~1.5-2 independent sources, not 3",
                "severity": "high"
            }

        # Same author multiple works
        authors = [e.get("author", "") for e in evidence_list]
        if len(authors) != len(set(authors)):
            return {
                "independent": False,
                "reason": "Multiple pieces from same author (not independent)",
                "true_independent_count": len(set(authors)),
                "correction": "Count by unique authors, not total pieces",
                "severity": "medium"
            }

        # Shared underlying source
        underlying_sources = [e.get("underlying_source", "") for e in evidence_list]
        if any(underlying_sources.count(s) > 1 for s in underlying_sources if s):
            return {
                "independent": False,
                "reason": "Evidence shares underlying source (not independent)",
                "true_independent_count": len(set(s for s in underlying_sources if s)),
                "correction": "Discount for shared source material",
                "severity": "high"
            }

        # If no issues detected
        return {
            "independent": True,
            "reason": "No obvious dependencies detected",
            "true_independent_count": len(evidence_list),
            "correction": "None needed",
            "severity": "none"
        }

    def grade_argument(
        self,
        premises: List[str],
        conclusion: str,
        evidence_list: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Comprehensive grading of full argument.

        Args:
            premises: List of premises
            conclusion: Conclusion being argued for
            evidence_list: Supporting evidence with metadata

        Returns:
            Complete grading report with tier assignments, fallacies, independence check

        Example:
            >>> grader.grade_argument(
            ...     ["Fine-tuning constants extremely precise", "Multiverse unverified"],
            ...     "Theism best explains fine-tuning",
            ...     [{"description": "Cosmological constant", "type": "physical_constant"}]
            ... )
            {'overall_tier': 3, 'confidence': (0.60, 0.75), 'fallacies': [], ...}
        """
        # Grade each piece of evidence
        graded_evidence = []
        for evidence in evidence_list:
            tier_result = self.assign_tier(
                evidence.get("description", ""),
                evidence.get("type", ""),
                evidence.get("context", {})
            )
            graded_evidence.append(tier_result)

        # Check for fallacies
        full_argument = " ".join(premises) + " Therefore, " + conclusion
        fallacies = self.check_fallacies(full_argument, {"conclusion": conclusion})

        # Check independence
        independence = self.check_independence(evidence_list)

        # Overall tier = weakest link (conservative)
        overall_tier = max(e["tier"] for e in graded_evidence) if graded_evidence else 5

        # Overall confidence = intersection of ranges (conservative)
        if graded_evidence:
            min_confidence = min(e["confidence_range"][0] for e in graded_evidence)
            max_confidence = max(e["confidence_range"][1] for e in graded_evidence)
            overall_confidence = (min_confidence, max_confidence)
        else:
            overall_confidence = (0.30, 0.50)

        # Generate report
        report = f"""
        ARGUMENT GRADING REPORT

        CONCLUSION: {conclusion}

        PREMISES:
        {self._format_list(premises)}

        EVIDENCE GRADING:
        {self._format_evidence_grades(graded_evidence)}

        FALLACY CHECK:
        {self._format_fallacies(fallacies)}

        INDEPENDENCE CHECK:
        {independence['reason']}
        True Independent Count: {independence['true_independent_count']}

        OVERALL ASSESSMENT:
        Tier: {overall_tier} ({self.TIERS[overall_tier]['name']})
        Confidence Range: {self._format_range(*overall_confidence)}

        RECOMMENDATION:
        {self._generate_recommendation(overall_tier, fallacies, independence)}
        """

        return {
            "overall_tier": overall_tier,
            "overall_tier_name": self.TIERS[overall_tier]["name"],
            "confidence_range": overall_confidence,
            "graded_evidence": graded_evidence,
            "fallacies": fallacies,
            "independence": independence,
            "report": report
        }

    def _format_range(self, low: float, high: float) -> str:
        """Format confidence range as percentage."""
        return f"{low:.0%}-{high:.0%}"

    def _format_list(self, items: List[str]) -> str:
        """Format list with bullets."""
        return "\n".join([f"- {item}" for item in items])

    def _format_evidence_grades(self, graded: List[Dict[str, Any]]) -> str:
        """Format graded evidence list."""
        return "\n".join([
            f"- Tier {g['tier']} ({g['tier_name']}): {self._format_range(*g['confidence_range'])}"
            for g in graded
        ])

    def _format_fallacies(self, fallacies: List[Dict[str, str]]) -> str:
        """Format detected fallacies."""
        if not fallacies:
            return "✅ No obvious fallacies detected"
        return "\n".join([f"⚠️  {f['fallacy']}: {f['explanation']}" for f in fallacies])

    def _generate_recommendation(
        self,
        tier: int,
        fallacies: List[Dict[str, str]],
        independence: Dict[str, Any]
    ) -> str:
        """Generate recommendation based on grading."""
        recommendations = []

        if tier >= 4:
            recommendations.append("Evidence is primarily testimonial or experiential - lower confidence appropriate")

        if fallacies:
            recommendations.append("Address detected fallacies to strengthen argument")

        if not independence["independent"]:
            recommendations.append(f"Adjust for non-independence: {independence['correction']}")

        if not recommendations:
            recommendations.append("Argument appears reasonably strong - maintain appropriate confidence calibration")

        return "\n".join([f"- {r}" for r in recommendations])


# Example Usage (for documentation—Claude implements this pattern)
if __name__ == "__main__":
    # Example: Fine-Tuning Argument
    grader = EvidenceGrader()

    evidence_list = [
        {
            "description": "Cosmological constant fine-tuned to 1 in 10^120",
            "type": "physical_constants",
            "context": {"sample_size": "Observable universe", "repeatable": "No", "controls": "No (only 1 universe)"}
        },
        {
            "description": "Strong nuclear force precisely calibrated",
            "type": "physical_constants",
            "context": {"sample_size": "Observable universe", "repeatable": "No"}
        }
    ]

    result = grader.grade_argument(
        premises=[
            "Physical constants are fine-tuned to extreme precision",
            "Life requires this precise calibration",
            "Multiverse hypothesis is unverified speculation"
        ],
        conclusion="Theism best explains fine-tuning",
        evidence_list=evidence_list
    )

    print(result["report"])
