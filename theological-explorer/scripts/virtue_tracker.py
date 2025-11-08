"""
Virtue Tracker for Intellectual Character Development

This script documents the pattern for detecting and celebrating intellectual virtues
displayed during theological inquiry.

Claude implements this pattern directly (script is not executed).

Based on: Virtue epistemology tradition (Zagzebski, Roberts & Wood)
"""

from typing import List, Dict, Any, Optional


class VirtueTracker:
    """
    Tracks and celebrates intellectual virtues displayed during inquiry.

    Core Principle: Process over conclusion. Virtue is about HOW you seek truth,
    not WHAT conclusion you reach.

    Virtues tracked:
    1. Intellectual Humility
    2. Intellectual Courage
    3. Intellectual Honesty
    4. Open-Mindedness
    5. Intellectual Rigor
    6. Fair-Mindedness
    7. Intellectual Perseverance
    """

    VIRTUES = {
        "humility": {
            "name": "Intellectual Humility",
            "definition": "Owning limitations in knowledge and being willing to revise beliefs",
            "indicators": [
                "Acknowledging uncertainty",
                "Saying 'I don't know'",
                "Asking clarifying questions",
                "Revising previous position",
                "Recognizing complexity",
                "Admitting bias susceptibility"
            ],
            "quotes": [
                "I'm not certain about this",
                "I could be wrong",
                "I don't fully understand",
                "That's a good point I hadn't considered",
                "I'm realizing my view was too simplistic"
            ],
            "celebration": "✅ Intellectual Humility: You acknowledged uncertainty and limitations. This is the foundation of wisdom."
        },
        "courage": {
            "name": "Intellectual Courage",
            "definition": "Pursuing truth even when emotionally costly or socially unpopular",
            "indicators": [
                "Questioning deeply held beliefs",
                "Following evidence despite discomfort",
                "Considering opposing views seriously",
                "Admitting previous belief was wrong",
                "Exploring ideas that community rejects",
                "Facing difficult questions"
            ],
            "quotes": [
                "I'm questioning what I've always believed",
                "This evidence challenges my view",
                "I need to face this difficulty honestly",
                "Even though it's uncomfortable, I want to know the truth",
                "I'm willing to be wrong"
            ],
            "celebration": "✅ Intellectual Courage: You pursued truth despite emotional discomfort. This takes real bravery."
        },
        "honesty": {
            "name": "Intellectual Honesty",
            "definition": "Accurately representing evidence and opposing views without distortion",
            "indicators": [
                "Steel-manning opponent's position",
                "Acknowledging weaknesses in own view",
                "Not cherry-picking evidence",
                "Reporting evidence that contradicts own view",
                "Avoiding straw man characterizations",
                "Transparent about motivations and biases"
            ],
            "quotes": [
                "To be fair to the opposing view...",
                "The strongest objection to my position is...",
                "I want to believe this, which makes me suspicious of my reasoning",
                "Here's evidence that doesn't support my view",
                "Let me represent their actual position, not a caricature"
            ],
            "celebration": "✅ Intellectual Honesty: You represented evidence and opposing views accurately. This integrity is rare and valuable."
        },
        "open_mindedness": {
            "name": "Open-Mindedness",
            "definition": "Willingness to consider new ideas and revise beliefs in light of evidence",
            "indicators": [
                "Seriously engaging opposing arguments",
                "Asking 'What would change my mind?'",
                "Exploring views outside comfort zone",
                "Not dismissing ideas prematurely",
                "Seeking out challenging perspectives",
                "Changing mind when evidence warrants"
            ],
            "quotes": [
                "I hadn't considered that perspective",
                "What would it take to convince me otherwise?",
                "I'm genuinely curious about the opposing view",
                "I want to understand why smart people disagree",
                "I'm willing to change my mind if evidence supports it"
            ],
            "celebration": "✅ Open-Mindedness: You seriously considered perspectives that challenge your own. This openness is essential for truth-seeking."
        },
        "rigor": {
            "name": "Intellectual Rigor",
            "definition": "Careful, thorough reasoning with attention to logical coherence and evidence quality",
            "indicators": [
                "Checking for fallacies",
                "Assessing evidence quality",
                "Distinguishing correlation from causation",
                "Considering alternative explanations",
                "Using Bayesian reasoning",
                "Precision in definitions"
            ],
            "quotes": [
                "Let me check if this reasoning is valid",
                "What's the quality of this evidence?",
                "Are there alternative explanations?",
                "I need to be more precise about what I mean by...",
                "Is this correlation or causation?",
                "What's my prior probability for this claim?"
            ],
            "celebration": "✅ Intellectual Rigor: You engaged in careful, thorough reasoning. This discipline strengthens your conclusions."
        },
        "fair_mindedness": {
            "name": "Fair-Mindedness",
            "definition": "Treating all views by the same standards, avoiding double standards",
            "indicators": [
                "Applying same evidential standards to all views",
                "Acknowledging strengths in opposing views",
                "Not privileging own position",
                "Avoiding motivated reasoning",
                "Checking for bias in evaluation",
                "Proportioning confidence to evidence"
            ],
            "quotes": [
                "Would I accept this evidence if it supported the opposing view?",
                "Am I holding my view to the same standard as theirs?",
                "The opposing view has strengths too",
                "I need to check if I'm being biased here",
                "Let me apply the same scrutiny to my own position"
            ],
            "celebration": "✅ Fair-Mindedness: You applied consistent standards across all positions. This impartiality is intellectually virtuous."
        },
        "perseverance": {
            "name": "Intellectual Perseverance",
            "definition": "Sustained effort in inquiry despite difficulty, confusion, or lack of immediate answers",
            "indicators": [
                "Continuing inquiry despite complexity",
                "Not giving up when confused",
                "Tolerating ambiguity",
                "Seeking deeper understanding",
                "Engaging difficult questions repeatedly",
                "Not settling for easy answers"
            ],
            "quotes": [
                "This is confusing, but I want to understand",
                "Let me think about this more deeply",
                "I'm not satisfied with surface-level answers",
                "Even though this is hard, I want to keep exploring",
                "I've been thinking about this for [long time]"
            ],
            "celebration": "✅ Intellectual Perseverance: You sustained inquiry despite difficulty. This persistence leads to deeper understanding."
        }
    }

    def __init__(self):
        """Initialize tracker with session history."""
        self.session_history: List[Dict[str, Any]] = []

    def detect_virtue(
        self,
        user_message: str,
        context: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Detect intellectual virtues displayed in user's message.

        Args:
            user_message: What user said/asked
            context: Conversation context (previous messages, topic)

        Returns:
            List of virtues detected with evidence and celebration messages

        Example:
            >>> tracker.detect_virtue(
            ...     "I'm not certain about this. I could be wrong, but...",
            ...     {"topic": "resurrection"}
            ... )
            [{'virtue': 'humility', 'evidence': 'Acknowledged uncertainty', 'celebration': '...'}]
        """
        detected = []
        message_lower = user_message.lower()

        # Humility detection
        humility_indicators = [
            "i don't know",
            "i'm not certain",
            "i could be wrong",
            "i'm uncertain",
            "i'm not sure",
            "help me understand",
            "i don't fully understand",
            "that's a good point",
            "i hadn't considered"
        ]
        if any(indicator in message_lower for indicator in humility_indicators):
            detected.append({
                "virtue": "humility",
                "virtue_name": self.VIRTUES["humility"]["name"],
                "evidence": "Acknowledged uncertainty and limitations",
                "celebration": self.VIRTUES["humility"]["celebration"],
                "quote": self._extract_quote(user_message, humility_indicators)
            })

        # Courage detection
        courage_indicators = [
            "questioning what i've believed",
            "challenges my view",
            "uncomfortable",
            "difficult to accept",
            "questioning my faith",
            "doubting",
            "scared to think about",
            "even though it's hard"
        ]
        if any(indicator in message_lower for indicator in courage_indicators):
            detected.append({
                "virtue": "courage",
                "virtue_name": self.VIRTUES["courage"]["name"],
                "evidence": "Pursued truth despite emotional discomfort",
                "celebration": self.VIRTUES["courage"]["celebration"],
                "quote": self._extract_quote(user_message, courage_indicators)
            })

        # Honesty detection
        honesty_indicators = [
            "to be fair",
            "strongest objection to my view",
            "weakness in my position",
            "i want to believe this",
            "i'm biased toward",
            "not a straw man",
            "steel-man",
            "their actual position"
        ]
        if any(indicator in message_lower for indicator in honesty_indicators):
            detected.append({
                "virtue": "honesty",
                "virtue_name": self.VIRTUES["honesty"]["name"],
                "evidence": "Accurately represented opposing views and own weaknesses",
                "celebration": self.VIRTUES["honesty"]["celebration"],
                "quote": self._extract_quote(user_message, honesty_indicators)
            })

        # Open-Mindedness detection
        open_indicators = [
            "hadn't considered",
            "what would change my mind",
            "willing to change",
            "want to understand why",
            "genuinely curious",
            "open to",
            "help me see",
            "what am i missing"
        ]
        if any(indicator in message_lower for indicator in open_indicators):
            detected.append({
                "virtue": "open_mindedness",
                "virtue_name": self.VIRTUES["open_mindedness"]["name"],
                "evidence": "Willingness to consider new perspectives and revise beliefs",
                "celebration": self.VIRTUES["open_mindedness"]["celebration"],
                "quote": self._extract_quote(user_message, open_indicators)
            })

        # Rigor detection
        rigor_indicators = [
            "what's the evidence",
            "is this valid",
            "fallacy",
            "bayesian",
            "prior probability",
            "what tier of evidence",
            "correlation or causation",
            "alternative explanation",
            "let me be more precise"
        ]
        if any(indicator in message_lower for indicator in rigor_indicators):
            detected.append({
                "virtue": "rigor",
                "virtue_name": self.VIRTUES["rigor"]["name"],
                "evidence": "Careful attention to logical coherence and evidence quality",
                "celebration": self.VIRTUES["rigor"]["celebration"],
                "quote": self._extract_quote(user_message, rigor_indicators)
            })

        # Fair-Mindedness detection
        fair_indicators = [
            "same standard",
            "would i accept this if",
            "double standard",
            "being consistent",
            "opposing view has strengths",
            "not privileging my view",
            "check for bias"
        ]
        if any(indicator in message_lower for indicator in fair_indicators):
            detected.append({
                "virtue": "fair_mindedness",
                "virtue_name": self.VIRTUES["fair_mindedness"]["name"],
                "evidence": "Applied consistent standards across all positions",
                "celebration": self.VIRTUES["fair_mindedness"]["celebration"],
                "quote": self._extract_quote(user_message, fair_indicators)
            })

        # Perseverance detection
        perseverance_indicators = [
            "keep thinking about",
            "still trying to understand",
            "been wrestling with",
            "not giving up",
            "deeper understanding",
            "for years",
            "for months",
            "decade",
            "keep exploring"
        ]
        if any(indicator in message_lower for indicator in perseverance_indicators):
            detected.append({
                "virtue": "perseverance",
                "virtue_name": self.VIRTUES["perseverance"]["name"],
                "evidence": "Sustained inquiry despite difficulty and complexity",
                "celebration": self.VIRTUES["perseverance"]["celebration"],
                "quote": self._extract_quote(user_message, perseverance_indicators)
            })

        return detected

    def celebrate(self, virtues_detected: List[Dict[str, Any]]) -> str:
        """
        Generate celebration message for detected virtues.

        Args:
            virtues_detected: List from detect_virtue()

        Returns:
            Formatted celebration message

        Example:
            >>> tracker.celebrate([
            ...     {'virtue': 'humility', 'celebration': '...'},
            ...     {'virtue': 'courage', 'celebration': '...'}
            ... ])
            "✅ Intellectual Humility: You acknowledged...\n✅ Intellectual Courage: You pursued..."
        """
        if not virtues_detected:
            return ""

        celebrations = [v["celebration"] for v in virtues_detected]
        return "\n\n" + "\n\n".join(celebrations)

    def track_growth(self, virtue_key: str) -> None:
        """
        Track virtue over time in session.

        Args:
            virtue_key: Key of virtue displayed (e.g., 'humility')
        """
        self.session_history.append({
            "virtue": virtue_key,
            "timestamp": "current"  # In real implementation, would use actual timestamp
        })

    def generate_session_summary(self) -> str:
        """
        Summarize intellectual virtues displayed during session.

        Returns:
            Summary report of virtues and growth

        Example:
            >>> tracker.generate_session_summary()
            "SESSION VIRTUE SUMMARY\n\nIntellectual Humility: 5 times\nIntellectual Courage: 3 times\n..."
        """
        if not self.session_history:
            return "No virtues tracked this session."

        # Count occurrences
        virtue_counts = {}
        for entry in self.session_history:
            virtue = entry["virtue"]
            virtue_counts[virtue] = virtue_counts.get(virtue, 0) + 1

        # Generate summary
        summary = "SESSION VIRTUE SUMMARY\n\n"
        summary += "Virtues Displayed:\n"

        for virtue_key, count in sorted(virtue_counts.items(), key=lambda x: x[1], reverse=True):
            virtue_name = self.VIRTUES[virtue_key]["name"]
            summary += f"- {virtue_name}: {count} {'time' if count == 1 else 'times'}\n"

        summary += f"\nTotal Virtue Instances: {len(self.session_history)}\n"

        # Add encouragement
        summary += "\n🎯 GROWTH REFLECTION\n"
        if len(virtue_counts) >= 4:
            summary += "You displayed a wide range of intellectual virtues. This holistic approach to truth-seeking is exemplary.\n"
        elif len(self.session_history) >= 5:
            summary += "You consistently demonstrated intellectual virtue throughout our conversation. This sustained practice builds character.\n"
        else:
            summary += "You demonstrated intellectual virtue in your inquiry. Keep cultivating these habits of mind.\n"

        # Most frequent virtue
        if virtue_counts:
            top_virtue = max(virtue_counts.items(), key=lambda x: x[1])
            top_virtue_name = self.VIRTUES[top_virtue[0]]["name"]
            summary += f"\nYour strongest virtue this session: {top_virtue_name}\n"

        return summary

    def _extract_quote(self, message: str, indicators: List[str]) -> str:
        """
        Extract relevant quote from message that triggered virtue detection.

        Args:
            message: User's message
            indicators: List of indicator phrases

        Returns:
            Extracted quote or empty string
        """
        message_lower = message.lower()
        for indicator in indicators:
            if indicator in message_lower:
                # Find sentence containing indicator (simplified)
                sentences = message.split('. ')
                for sentence in sentences:
                    if indicator in sentence.lower():
                        return sentence[:100] + ("..." if len(sentence) > 100 else "")
        return ""

    def suggest_virtue_development(self, virtues_not_displayed: List[str]) -> str:
        """
        Suggest virtues to develop based on what wasn't displayed.

        Args:
            virtues_not_displayed: List of virtue keys not yet shown

        Returns:
            Gentle suggestions for growth

        Example:
            >>> tracker.suggest_virtue_development(['fair_mindedness', 'honesty'])
            "VIRTUE DEVELOPMENT OPPORTUNITIES\n\n..."
        """
        if not virtues_not_displayed:
            return ""

        suggestions = "VIRTUE DEVELOPMENT OPPORTUNITIES\n\n"
        suggestions += "Consider cultivating:\n\n"

        for virtue_key in virtues_not_displayed[:3]:  # Suggest max 3
            virtue = self.VIRTUES[virtue_key]
            suggestions += f"**{virtue['name']}**: {virtue['definition']}\n"
            suggestions += f"Try: {virtue['indicators'][0]}\n\n"

        suggestions += "Remember: Intellectual virtue is a journey, not a destination. Every conversation is an opportunity to practice.\n"

        return suggestions


# Example Usage (for documentation—Claude implements this pattern)
if __name__ == "__main__":
    # Example: Tracking virtues during theological inquiry
    tracker = VirtueTracker()

    # Simulate user messages
    user_messages = [
        "I'm questioning what I've always believed about the resurrection. It's uncomfortable, but I want to know the truth.",
        "I don't fully understand the fine-tuning argument. Can you help me see what I'm missing?",
        "To be fair to the atheist position, the problem of evil is a strong objection. What's the best response?",
        "I've been thinking about this for years. I'm not giving up, but I need deeper understanding."
    ]

    # Detect virtues in each message
    for i, message in enumerate(user_messages, 1):
        print(f"\n=== Message {i} ===")
        print(f"User: {message}\n")

        virtues = tracker.detect_virtue(message)

        if virtues:
            print("Virtues Detected:")
            for v in virtues:
                print(f"- {v['virtue_name']}")
                tracker.track_growth(v['virtue'])

            print(tracker.celebrate(virtues))

    # Session summary
    print("\n" + "="*60)
    print(tracker.generate_session_summary())
