from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List

from src.schemas import ManualEvaluationResult


AMBIGUOUS_STATUSES = {
    "AMBIGUOUS_ACCEPTABLE",
    "AMBIGUOUS_NO_MATCH",
}


def load_manual_evaluations(
    csv_path: str | Path,
) -> List[ManualEvaluationResult]:
    """
    Load manual Dialogflow CX evaluation results from CSV.
    """

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Manual evaluation file not found: {path}"
        )

    required_columns = {
        "test_id",
        "iteration",
        "utterance",
        "expected_intent",
        "actual_intent",
        "expected_page",
        "actual_page",
        "status",
        "change_applied",
        "notes",
    }

    evaluations: List[ManualEvaluationResult] = []

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        reader = csv.DictReader(file)

        fieldnames = set(reader.fieldnames or [])
        missing_columns = required_columns - fieldnames

        if missing_columns:
            missing = ", ".join(sorted(missing_columns))
            raise ValueError(
                f"Missing required CSV columns: {missing}"
            )

        for row in reader:
            try:
                iteration = int(row["iteration"])
            except ValueError as exc:
                raise ValueError(
                    "Invalid iteration "
                    f"'{row['iteration']}' "
                    f"for test_id '{row['test_id']}'."
                ) from exc

            evaluations.append(
                ManualEvaluationResult(
                    test_id=row["test_id"].strip(),
                    iteration=iteration,
                    utterance=row["utterance"].strip(),
                    expected_intent=row[
                        "expected_intent"
                    ].strip(),
                    actual_intent=row[
                        "actual_intent"
                    ].strip(),
                    expected_page=row[
                        "expected_page"
                    ].strip(),
                    actual_page=row[
                        "actual_page"
                    ].strip(),
                    status=row["status"].strip(),
                    change_applied=row[
                        "change_applied"
                    ].strip(),
                    notes=row["notes"].strip(),
                )
            )

    return evaluations


def is_ambiguous(
    result: ManualEvaluationResult,
) -> bool:
    """
    Return True when the test case is marked as ambiguous.
    """

    return result.status in AMBIGUOUS_STATUSES


def is_no_match(
    result: ManualEvaluationResult,
) -> bool:
    """
    Return True when no intent was detected.
    """

    return result.actual_intent == ""


def intent_is_correct(
    result: ManualEvaluationResult,
) -> bool:
    """
    Check whether actual and expected intents match.
    """

    return (
        bool(result.expected_intent)
        and result.expected_intent
        == result.actual_intent
    )


def page_is_correct(
    result: ManualEvaluationResult,
) -> bool:
    """
    Check whether actual and expected pages match.
    """

    return (
        bool(result.expected_page)
        and result.expected_page
        == result.actual_page
    )


def safe_rate(
    numerator: int,
    denominator: int,
) -> float:
    """
    Calculate a rate without division-by-zero errors.
    """

    if denominator == 0:
        return 0.0

    return numerator / denominator


def get_latest_iterations(
    results: Iterable[ManualEvaluationResult],
) -> List[ManualEvaluationResult]:
    """
    Return only the latest iteration for every test_id.
    """

    latest: Dict[str, ManualEvaluationResult] = {}

    for result in results:
        current = latest.get(result.test_id)

        if (
            current is None
            or result.iteration > current.iteration
        ):
            latest[result.test_id] = result

    return list(latest.values())


def summarize_results(
    results: Iterable[ManualEvaluationResult],
) -> Dict[str, Any]:
    """
    Calculate core metrics for manual evaluation results.

    Ambiguous cases are excluded from the primary
    intent accuracy, page accuracy and No Match Rate.
    """

    results = list(results)

    evaluable = [
        result
        for result in results
        if not is_ambiguous(result)
    ]

    ambiguous = [
        result
        for result in results
        if is_ambiguous(result)
    ]

    correct_intents = sum(
        intent_is_correct(result)
        for result in evaluable
    )

    correct_pages = sum(
        page_is_correct(result)
        for result in evaluable
    )

    no_matches = sum(
        is_no_match(result)
        for result in evaluable
    )

    status_counts = Counter(
        result.status
        for result in results
    )

    return {
        "total_rows": len(results),
        "evaluable_rows": len(evaluable),
        "ambiguous_rows": len(ambiguous),
        "correct_intents": correct_intents,
        "intent_accuracy": safe_rate(
            correct_intents,
            len(evaluable),
        ),
        "correct_pages": correct_pages,
        "page_accuracy": safe_rate(
            correct_pages,
            len(evaluable),
        ),
        "no_match_count": no_matches,
        "no_match_rate": safe_rate(
            no_matches,
            len(evaluable),
        ),
        "ambiguous_rate": safe_rate(
            len(ambiguous),
            len(results),
        ),
        "status_counts": dict(
            sorted(status_counts.items())
        ),
    }


def calculate_improvement(
    results: Iterable[ManualEvaluationResult],
) -> Dict[str, Any]:
    """
    Calculate improvement across repeated test iterations.

    A case is considered improved when its first
    iteration is FAIL and a later iteration is PASS.
    """

    grouped: Dict[
        str,
        List[ManualEvaluationResult],
    ] = defaultdict(list)

    for result in results:
        grouped[result.test_id].append(result)

    initially_failed_reevaluated = 0
    improved_cases = 0
    improved_test_ids: List[str] = []

    for test_id, test_results in grouped.items():
        ordered = sorted(
            test_results,
            key=lambda result: result.iteration,
        )

        if len(ordered) < 2:
            continue

        if ordered[0].status != "FAIL":
            continue

        initially_failed_reevaluated += 1

        later_pass = any(
            result.status == "PASS"
            for result in ordered[1:]
        )

        if later_pass:
            improved_cases += 1
            improved_test_ids.append(test_id)

    return {
        "initially_failed_reevaluated":
            initially_failed_reevaluated,
        "improved_cases": improved_cases,
        "improvement_rate": safe_rate(
            improved_cases,
            initially_failed_reevaluated,
        ),
        "improved_test_ids": sorted(
            improved_test_ids
        ),
    }


def build_manual_evaluation_summary(
    results: Iterable[ManualEvaluationResult],
) -> Dict[str, Any]:
    """
    Build the complete manual evaluation summary.
    """

    results = list(results)

    latest_results = get_latest_iterations(
        results
    )

    return {
        "all_iterations": summarize_results(
            results
        ),
        "latest_iteration": summarize_results(
            latest_results
        ),
        "improvement": calculate_improvement(
            results
        ),
    }


def results_to_records(
    results: Iterable[ManualEvaluationResult],
) -> List[Dict[str, Any]]:
    """
    Convert evaluation dataclasses into dictionaries.
    """

    return [
        asdict(result)
        for result in results
    ]


def main() -> None:
    """
    Command-line entry point.
    """

    parser = argparse.ArgumentParser(
        description=(
            "Calculate metrics from manual "
            "Dialogflow CX evaluation results."
        )
    )

    parser.add_argument(
        "csv_path",
        nargs="?",
        default="results/manual_evaluation.csv",
        help=(
            "Path to the manual evaluation CSV "
            "(default: results/manual_evaluation.csv)"
        ),
    )

    args = parser.parse_args()

    results = load_manual_evaluations(
        args.csv_path
    )

    summary = build_manual_evaluation_summary(
        results
    )

  output_path = Path(
    "results/manual_evaluation_summary.json"
)

output_path.parent.mkdir(
    parents=True,
    exist_ok=True,
)

with output_path.open(
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        summary,
        file,
        ensure_ascii=False,
        indent=2,
    )

"w",
    encoding="utf-8",
) as file:
    json.dump(
        summary,
        file,
        ensure_ascii=False,
        indent=2,
    )

print(
    json.dumps(
        summary,
        ensure_ascii=False,
        indent=2,
    )
)

print(
    f"\nSummary saved to: {output_path}"
)

if __name__ == "__main__":
    main()
