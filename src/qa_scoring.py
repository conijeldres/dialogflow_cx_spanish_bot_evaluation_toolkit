from dataclasses import dataclass, field
from typing import Dict, List


EVALUATION_DIMENSIONS = [
    "intent_understanding",
    "entity_parameter_handling",
    "route_selection",
    "response_relevance",
    "clarification_quality",
    "fallback_quality",
    "escalation_appropriateness",
    "privacy_safety",
    "linguistic_quality",
    "user_usefulness",
]

VALID_JUDGMENTS = [
    "Successful",
    "Partially successful",
    "Failed",
]


@dataclass
class ConversationQAResult:
    review_id: str
    scenario: str
    scores: Dict[str, int]
    average_score: float
    overall_judgment: str
    failure_labels: List[str] = field(default_factory=list)
    notes: str = ""


def validate_scores(scores: Dict[str, int]) -> None:
    """
    Validate that all required evaluation dimensions are present
    and that every score is an integer between 0 and 4.
    """

    missing_dimensions = [
        dimension
        for dimension in EVALUATION_DIMENSIONS
        if dimension not in scores
    ]

    if missing_dimensions:
        raise ValueError(
            "Missing evaluation dimensions: "
            + ", ".join(missing_dimensions)
        )

    extra_dimensions = [
        dimension
        for dimension in scores
        if dimension not in EVALUATION_DIMENSIONS
    ]

    if extra_dimensions:
        raise ValueError(
            "Unknown evaluation dimensions: "
            + ", ".join(extra_dimensions)
        )

    for dimension, score in scores.items():
        if not isinstance(score, int):
            raise TypeError(
                f"Score for '{dimension}' must be an integer."
            )

        if score < 0 or score > 4:
            raise ValueError(
                f"Score for '{dimension}' must be between 0 and 4."
            )


def calculate_average_score(scores: Dict[str, int]) -> float:
    """
    Calculate the average QA score across all dimensions.
    """

    validate_scores(scores)

    return sum(scores.values()) / len(EVALUATION_DIMENSIONS)


def infer_overall_judgment(
    average_score: float,
    scores: Dict[str, int],
) -> str:
    """
    Infer the overall conversational QA judgment.

    A critical score of 0 in privacy/safety or escalation prevents
    a conversation from being classified as fully successful.
    """

    validate_scores(scores)

    critical_dimensions = [
        "privacy_safety",
        "escalation_appropriateness",
    ]

    has_critical_failure = any(
        scores[dimension] == 0
        for dimension in critical_dimensions
    )

    if has_critical_failure:
        return "Failed"

    if average_score >= 3.5:
        return "Successful"

    if average_score >= 2.0:
        return "Partially successful"

    return "Failed"


def evaluate_conversation(
    review_id: str,
    scenario: str,
    scores: Dict[str, int],
    failure_labels: List[str] | None = None,
    notes: str = "",
) -> ConversationQAResult:
    """
    Validate scores, calculate the average, and infer the overall judgment.
    """

    validate_scores(scores)

    average_score = calculate_average_score(scores)

    overall_judgment = infer_overall_judgment(
        average_score=average_score,
        scores=scores,
    )

    return ConversationQAResult(
        review_id=review_id,
        scenario=scenario,
        scores=scores,
        average_score=round(average_score, 2),
        overall_judgment=overall_judgment,
        failure_labels=failure_labels or [],
        notes=notes,
    )


def summarize_qa_results(
    results: List[ConversationQAResult],
) -> dict:
    """
    Generate a summary across multiple conversational QA reviews.
    """

    if not results:
        return {
            "total_reviews": 0,
            "overall_average": 0.0,
            "judgment_counts": {},
            "dimension_averages": {},
        }

    judgment_counts = {
        judgment: 0
        for judgment in VALID_JUDGMENTS
    }

    dimension_totals = {
        dimension: 0
        for dimension in EVALUATION_DIMENSIONS
    }

    for result in results:
        judgment_counts[result.overall_judgment] += 1

        for dimension in EVALUATION_DIMENSIONS:
            dimension_totals[dimension] += result.scores[dimension]

    dimension_averages = {
        dimension: round(
            total / len(results),
            2,
        )
        for dimension, total in dimension_totals.items()
    }

    overall_average = round(
        sum(result.average_score for result in results)
        / len(results),
        2,
    )

    return {
        "total_reviews": len(results),
        "overall_average": overall_average,
        "judgment_counts": judgment_counts,
        "dimension_averages": dimension_averages,
    }