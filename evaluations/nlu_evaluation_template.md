# NLU Evaluation Template

## Test Metadata

- Test ID:
- Date:
- Evaluator:
- System / Agent version:
- Language:
- Environment:

## Utterance

**Text:**

**Expected intent:**

**Predicted intent:**

**Intent correct:** Yes / No

**Confidence score:**  
If available.

## Linguistic Information

- Difficulty:
- Variant:
- Ambiguity present: Yes / No
- Ambiguity type:
- Notes:

## Entity Evaluation

| Expected Entity | Expected Value | Predicted Entity | Predicted Value | Correct |
|---|---|---|---|---|
| | | | | |

## Routing Evaluation

**Expected flow:**

**Predicted flow:**

**Expected page:**

**Predicted page:**

**Route correct:** Yes / No

## Failure Labels

Select all that apply:

```text
wrong_intent
missed_intent
intent_confusion
overtriggered_intent
fallback_instead_of_intent

missed_entity
wrong_entity_type
wrong_entity_value
partial_entity_match
spurious_entity
entity_overinterpretation

wrong_flow
wrong_page
wrong_transition
routing_loop