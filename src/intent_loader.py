import csv
import json
from pathlib import Path
from typing import List

from src.schemas import (
    EntityAnnotation,
    IntentDefinition,
    TestUtterance,
    TrainingPhrase,
)


def load_intent_catalog(
    path: str | Path = "data/intents/intents_catalog.csv",
) -> List[IntentDefinition]:
    path = Path(path)
    intents = []

    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            entity_list = [
                item.strip()
                for item in row["entities"].split(";")
                if item.strip()
            ]

            intents.append(
                IntentDefinition(
                    intent_id=row["intent_id"],
                    intent_name=row["intent_name"],
                    category=row["category"],
                    description=row["description"],
                    example_user_utterance=row["example_user_utterance"],
                    expected_behavior=row["expected_behavior"],
                    entities=entity_list,
                    risk_level=row["risk_level"],
                    escalation_required=row["escalation_required"],
                    notes=row["notes"],
                )
            )

    return intents


def _parse_entities(raw_entities: list[dict]) -> List[EntityAnnotation]:
    return [
        EntityAnnotation(
            entity_name=item["entity_name"],
            value=item["value"],
        )
        for item in raw_entities
    ]


def load_training_phrases(
    path: str | Path = "data/intents/training_phrases_es.jsonl",
) -> List[TrainingPhrase]:
    path = Path(path)
    phrases = []

    with path.open(encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            data = json.loads(line)

            phrases.append(
                TrainingPhrase(
                    phrase_id=data["phrase_id"],
                    intent_name=data["intent_name"],
                    text=data["text"],
                    linguistic_variant=data["linguistic_variant"],
                    entities=_parse_entities(data.get("entities", [])),
                    notes=data.get("notes", ""),
                )
            )

    return phrases


def load_test_utterances(
    path: str | Path = "data/intents/test_utterances_es.jsonl",
) -> List[TestUtterance]:
    path = Path(path)
    utterances = []

    with path.open(encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            data = json.loads(line)

            utterances.append(
                TestUtterance(
                    test_id=data["test_id"],
                    text=data["text"],
                    expected_intent=data["expected_intent"],
                    difficulty=data["difficulty"],
                    variant=data["variant"],
                    entities=_parse_entities(data.get("entities", [])),
                    notes=data.get("notes", ""),
                )
            )

    return utterances


def summarize_dataset() -> None:
    intents = load_intent_catalog()
    training_phrases = load_training_phrases()
    test_utterances = load_test_utterances()

    print("Dataset summary")
    print("----------------")
    print(f"Intents: {len(intents)}")
    print(f"Training phrases: {len(training_phrases)}")
    print(f"Test utterances: {len(test_utterances)}")


if __name__ == "__main__":
    summarize_dataset()