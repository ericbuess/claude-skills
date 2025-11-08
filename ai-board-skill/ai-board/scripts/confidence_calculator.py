#!/usr/bin/env python3
"""
Confidence Calculator for AI Board

Computes calibrated confidence scores based on multiple factors:
- Agent agreement
- Evidence quality
- Counterargument strength
- Domain-specific standards
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class EvidenceQuality(Enum):
    """Quality levels for supporting evidence"""
    STRONG = "strong"  # RCTs, meta-analyses, proven theorems
    MODERATE = "moderate"  # Observational studies, strong arguments
    WEAK = "weak"  # Case reports, anecdotal, speculative
    NONE = "none"  # No evidence available

class Domain(Enum):
    """Different domains have different confidence standards"""
    MEDICAL = "medical"
    THEOLOGICAL = "theological"
    PHILOSOPHICAL = "philosophical"
    MATHEMATICAL = "mathematical"
    SCIENTIFIC = "scientific"
    TECHNICAL = "technical"
    GENERAL = "general"

@dataclass
class ConfidenceFactors:
    """Factors contributing to confidence assessment"""
    agent_agreement: float  # 0-1, proportion of agents agreeing
    evidence_quality: EvidenceQuality
    counterarguments_resolved: bool
    external_validation: bool
    consistency_across_methods: float  # 0-1, if using self-consistency
    domain: Domain
    
    # Factors that decrease confidence
    novel_situation: bool = False
    limited_evidence: bool = False
    significant_uncertainty: bool = False

class ConfidenceCalculator:
    """
    Calculate calibrated confidence scores.
    
    Philosophy: Better to be uncertain than confidently wrong.
    Explicit acknowledgment of Eric's key concern.
    """
    
    def __init__(self):
        # Domain-specific confidence standards
        self.domain_thresholds = {
            Domain.MEDICAL: {
                'high': 0.95,  # Guideline-based care
                'moderate': 0.85,  # Well-studied treatments
                'low': 0.70,  # Limited evidence
            },
            Domain.THEOLOGICAL: {
                'high': 0.95,  # Core gospel truths
                'moderate': 0.85,  # Clear biblical teaching
                'low': 0.70,  # Legitimate disagreement
            },
            Domain.PHILOSOPHICAL: {
                'high': 0.70,  # Rare in philosophy
                'moderate': 0.60,  # Reasonable position
                'low': 0.50,  # One of several views
            },
            Domain.MATHEMATICAL: {
                'high': 0.999,  # Proven theorems
                'moderate': 0.90,  # Strong heuristics
                'low': 0.70,  # Conjectures
            },
            Domain.SCIENTIFIC: {
                'high': 0.95,  # Well-established laws
                'moderate': 0.85,  # Strong empirical support
                'low': 0.70,  # Emerging research
            },
            Domain.TECHNICAL: {
                'high': 0.90,  # Tested implementations
                'moderate': 0.80,  # Standard practices
                'low': 0.70,  # Novel approaches
            },
        }
    
    def calculate_confidence(self, factors: ConfidenceFactors) -> Dict:
        """
        Calculate overall confidence with detailed breakdown.
        
        Returns:
            Dict with:
            - overall_confidence: float 0-1
            - confidence_level: str (very_high, high, moderate, low, very_low)
            - factors_increasing: List[str]
            - factors_decreasing: List[str]
            - recommendation: str
        """
        # Start with base confidence from agent agreement
        base_confidence = factors.agent_agreement
        
        # Adjust for evidence quality
        evidence_modifier = self._get_evidence_modifier(factors.evidence_quality)
        base_confidence *= evidence_modifier
        
        # Adjust for counterarguments
        if not factors.counterarguments_resolved:
            base_confidence *= 0.85  # 15% penalty for unresolved critiques
        
        # Adjust for external validation
        if factors.external_validation:
            base_confidence = min(1.0, base_confidence * 1.1)  # 10% boost
        
        # Adjust for self-consistency
        if factors.consistency_across_methods > 0:
            consistency_boost = factors.consistency_across_methods * 0.15
            base_confidence = min(1.0, base_confidence + consistency_boost)
        
        # Apply penalties for uncertainty factors
        if factors.novel_situation:
            base_confidence *= 0.90
        if factors.limited_evidence:
            base_confidence *= 0.85
        if factors.significant_uncertainty:
            base_confidence *= 0.80
        
        # Domain-specific calibration
        calibrated_confidence = self._calibrate_to_domain(
            base_confidence, 
            factors.domain
        )
        
        # Generate detailed breakdown
        increasing_factors = self._identify_increasing_factors(factors)
        decreasing_factors = self._identify_decreasing_factors(factors)
        
        confidence_level = self._categorize_confidence(
            calibrated_confidence,
            factors.domain
        )
        
        recommendation = self._generate_recommendation(
            calibrated_confidence,
            confidence_level,
            factors
        )
        
        return {
            'overall_confidence': round(calibrated_confidence, 3),
            'confidence_level': confidence_level,
            'factors_increasing': increasing_factors,
            'factors_decreasing': decreasing_factors,
            'recommendation': recommendation,
        }
    
    def _get_evidence_modifier(self, quality: EvidenceQuality) -> float:
        """Convert evidence quality to confidence modifier"""
        modifiers = {
            EvidenceQuality.STRONG: 1.0,
            EvidenceQuality.MODERATE: 0.90,
            EvidenceQuality.WEAK: 0.75,
            EvidenceQuality.NONE: 0.60,
        }
        return modifiers[quality]
    
    def _calibrate_to_domain(self, 
                            base_confidence: float, 
                            domain: Domain) -> float:
        """
        Calibrate confidence to domain-specific standards.
        
        Different domains have different standards for what constitutes
        high/moderate/low confidence.
        """
        # Philosophy should rarely exceed 0.70 given perennial disagreement
        if domain == Domain.PHILOSOPHICAL and base_confidence > 0.70:
            return 0.70 + (base_confidence - 0.70) * 0.3
        
        # Medical should be conservative on rare diseases
        # (This would be refined based on disease rarity in actual use)
        
        return base_confidence
    
    def _identify_increasing_factors(self, 
                                    factors: ConfidenceFactors) -> List[str]:
        """Identify factors that increase confidence"""
        increasing = []
        
        if factors.agent_agreement > 0.8:
            increasing.append(
                f"Strong agent agreement ({factors.agent_agreement:.1%})"
            )
        
        if factors.evidence_quality in [EvidenceQuality.STRONG, 
                                       EvidenceQuality.MODERATE]:
            increasing.append(
                f"{factors.evidence_quality.value.title()} evidence quality"
            )
        
        if factors.counterarguments_resolved:
            increasing.append("All major counterarguments addressed")
        
        if factors.external_validation:
            increasing.append("External validation confirms conclusions")
        
        if factors.consistency_across_methods > 0.8:
            increasing.append(
                "High consistency across multiple methods "
                f"({factors.consistency_across_methods:.1%})"
            )
        
        return increasing
    
    def _identify_decreasing_factors(self, 
                                    factors: ConfidenceFactors) -> List[str]:
        """Identify factors that decrease confidence"""
        decreasing = []
        
        if factors.agent_agreement < 0.7:
            decreasing.append(
                f"Limited agent agreement ({factors.agent_agreement:.1%})"
            )
        
        if not factors.counterarguments_resolved:
            decreasing.append("Some counterarguments remain unresolved")
        
        if factors.evidence_quality in [EvidenceQuality.WEAK, 
                                       EvidenceQuality.NONE]:
            decreasing.append(
                f"{factors.evidence_quality.value.title()} evidence quality"
            )
        
        if factors.novel_situation:
            decreasing.append("Novel or unusual situation")
        
        if factors.limited_evidence:
            decreasing.append("Limited relevant evidence available")
        
        if factors.significant_uncertainty:
            decreasing.append("Significant inherent uncertainty")
        
        if not factors.external_validation:
            decreasing.append("No external validation available")
        
        return decreasing
    
    def _categorize_confidence(self, 
                              confidence: float, 
                              domain: Domain) -> str:
        """Categorize confidence level based on domain standards"""
        thresholds = self.domain_thresholds.get(
            domain, 
            self.domain_thresholds[Domain.GENERAL]
        )
        
        if confidence >= thresholds['high']:
            return "very_high"
        elif confidence >= thresholds['moderate']:
            return "high"
        elif confidence >= thresholds['low']:
            return "moderate"
        elif confidence >= 0.50:
            return "low"
        else:
            return "very_low"
    
    def _generate_recommendation(self, 
                                confidence: float,
                                level: str,
                                factors: ConfidenceFactors) -> str:
        """Generate actionable recommendation based on confidence"""
        if level == "very_high":
            return "High confidence in conclusion. Proceed with recommendation."
        
        elif level == "high":
            return "Good confidence. Recommendation appropriate with noted uncertainties."
        
        elif level == "moderate":
            rec = "Moderate confidence. Consider: "
            suggestions = []
            
            if not factors.external_validation:
                suggestions.append("seeking external validation")
            if factors.evidence_quality == EvidenceQuality.WEAK:
                suggestions.append("gathering additional evidence")
            if not factors.counterarguments_resolved:
                suggestions.append("addressing remaining objections")
            
            return rec + ", ".join(suggestions) + "."
        
        elif level == "low":
            return (
                "Low confidence. Significant uncertainty remains. "
                "Consider expert consultation or additional research."
            )
        
        else:  # very_low
            return (
                "Very low confidence. Insufficient basis for strong conclusion. "
                "Recommend expert consultation before proceeding."
            )

def main():
    """Example usage of ConfidenceCalculator"""
    
    calculator = ConfidenceCalculator()
    
    # Example: Medical question with strong evidence
    factors = ConfidenceFactors(
        agent_agreement=0.90,
        evidence_quality=EvidenceQuality.STRONG,
        counterarguments_resolved=True,
        external_validation=True,
        consistency_across_methods=0.85,
        domain=Domain.MEDICAL,
        novel_situation=False,
        limited_evidence=False,
    )
    
    result = calculator.calculate_confidence(factors)
    
    print("Confidence Assessment")
    print("=" * 50)
    print(f"Overall Confidence: {result['overall_confidence']:.1%}")
    print(f"Confidence Level: {result['confidence_level']}")
    print(f"\nFactors Increasing Confidence:")
    for factor in result['factors_increasing']:
        print(f"  + {factor}")
    print(f"\nFactors Decreasing Confidence:")
    for factor in result['factors_decreasing']:
        print(f"  - {factor}")
    print(f"\nRecommendation: {result['recommendation']}")

if __name__ == "__main__":
    main()
