from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class IntentDefinition:
    intent_id: str
    intent_name: str
    category: str
    description: str
    example_user_utterance: str
    expected_behavior: str
    entities: List[str]
    risk_level: str
    escalation_required: str
    notes: str


@dataclass
class EntityAnnotation:
    entity_name: str
    value: str


@dataclass
class TrainingPhrase:
    phrase_id: str
    intent_name: str
    text: str
    linguistic_variant: str
    entities: List[EntityAnnotation] = field(default_factory=list)
    notes: str = ""


@dataclass
class TestUtterance:
    test_id: str
    text: str
    expected_intent: str
    difficulty: str
    variant: str
    entities: List[EntityAnnotation] = field(default_factory=list)
    notes: str = ""


@dataclass
class NLUEvaluationResult:
    test_id: str
    text: str
    expected_intent: str
    predicted_intent: str
    intent_correct: bool
    confidence: Optional[float] = None
    difficulty: str = ""
    variant: str = ""
    failure_labels: List[str] = field(default_factory=list)
    notes: str = ""