from collections import Counter, defaultdict
from dataclasses import asdict
from typing import Iterable, List, Dict, Any

from src.schemas import NLUEvaluationResult


def evaluate_prediction(
    test_id: str,
    text: str,
    expected_intent: str,
    predicted_intent: str,
    difficulty: str = "",
    variant: str = "",
    confidence: float | None = None,
    notes: str = "",
) -> NLUEvaluationResult:
    """
    Compare one predicted intent against the expected intent.
    """

    intent_correct = expected_intent == predicted_intent

    failure_labels: List[str] = []

    if not intent_correct:
        if predicted_intent == "fallback_general":
            failure_labels.append("fallback_instead_of_intent")
        else:
            failure_labels.append("wrong_intent")
            failure_labels.append("intent_confusion")

    return NLUEvaluationResult(
        test_id=test_id,
        text=text,
        expected_intent=expected_intent,
        predicted_intent=predicted_intent,
        intent_correct=intent_correct,
        confidence=confidence,
        difficulty=difficulty,
        variant=variant,
        failure_labels=failure_labels,
        notes=notes,
    )


def calculate_intent_accuracy(
    results: Iterable[NLUEvaluationResult],
) -> float:
    """
    Calculate overall intent accuracy.
    """

    results = list(results)

    if not results:
        return 0.0

    correct = sum(result.intent_correct for result in results)

    return correct / len(results)


def accuracy_by_expected_intent(
    results: Iterable[NLUEvaluationResult],
) -> Dict[str, Dict[str, Any]]:
    """
    Calculate accuracy grouped by expected intent.
    """

    grouped = defaultdict(lambda: {"total": 0, "correct": 0})

    for result in results:
        grouped[result.expected_intent]["total"] += 1

        if result.intent_correct:
            grouped[result.expected_intent]["correct"] += 1

    summary = {}

    for intent, values in sorted(grouped.items()):
        total = values["total"]
        correct = values["correct"]

        summary[intent] = {
            "total": total,
            "correct": correct,
            "incorrect": total - correct,
            "accuracy": correct / total if total else 0.0,
        }

    return summary


def accuracy_by_difficulty(
    results: Iterable[NLUEvaluationResult],
) -> Dict[str, Dict[str, Any]]:
    """
    Calculate accuracy grouped by test difficulty.
    """

    grouped = defaultdict(lambda: {"total": 0, "correct": 0})

    for result in results:
        difficulty = result.difficulty or "unknown"

        grouped[difficulty]["total"] += 1

        if result.intent_correct:
            grouped[difficulty]["correct"] += 1

    summary = {}

    for difficulty, values in sorted(grouped.items()):
        total = values["total"]
        correct = values["correct"]

        summary[difficulty] = {
            "total": total,
            "correct": correct,
            "incorrect": total - correct,
            "accuracy": correct / total if total else 0.0,
        }

    return summary


def accuracy_by_variant(
    results: Iterable[NLUEvaluationResult],
) -> Dict[str, Dict[str, Any]]:
    """
    Calculate accuracy grouped by linguistic variant.
    """

    grouped = defaultdict(lambda: {"total": 0, "correct": 0})

    for result in results:
        variant = result.variant or "unknown"

        grouped[variant]["total"] += 1

        if result.intent_correct:
            grouped[variant]["correct"] += 1

    summary = {}

    for variant, values in sorted(grouped.items()):
        total = values["total"]
        correct = values["correct"]

        summary[variant] = {
            "total": total,
            "correct": correct,
            "incorrect": total - correct,
            "accuracy": correct / total if total else 0.0,
        }

    return summary


def build_confusion_counts(
    results: Iterable[NLUEvaluationResult],
) -> Dict[str, Dict[str, int]]:
    """
    Build a nested confusion-count dictionary.

    Structure:
    {
        expected_intent: {
            predicted_intent: count
        }
    }
    """

    confusion = defaultdict(Counter)

    for result in results:
        confusion[result.expected_intent][result.predicted_intent] += 1

    return {
        expected: dict(sorted(predicted.items()))
        for expected, predicted in sorted(confusion.items())
    }


def count_failure_labels(
    results: Iterable[NLUEvaluationResult],
) -> Dict[str, int]:
    """
    Count NLU failure labels across all results.
    """

    counter = Counter()

    for result in results:
        counter.update(result.failure_labels)

    return dict(counter.most_common())


def results_to_records(
    results: Iterable[NLUEvaluationResult],
) -> List[Dict[str, Any]]:
    """
    Convert dataclass results into dictionaries for CSV/JSON output.
    """

    return [asdict(result) for result in results]


def build_evaluation_summary(
    results: Iterable[NLUEvaluationResult],
) -> Dict[str, Any]:
    """
    Build a complete summary of NLU evaluation results.
    """

    results = list(results)

    return {
        "total_utterances": len(results),
        "overall_accuracy": calculate_intent_accuracy(results),
        "accuracy_by_intent": accuracy_by_expected_intent(results),
        "accuracy_by_difficulty": accuracy_by_difficulty(results),
        "accuracy_by_variant": accuracy_by_variant(results),
        "confusion_counts": build_confusion_counts(results),
        "failure_labels": count_failure_labels(results),
    }