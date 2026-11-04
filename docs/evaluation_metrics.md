# Evaluation Metrics

This document defines the evaluation criteria used by the `dialogflow_cx_spanish_bot_evaluation_toolkit`.

The goal of the toolkit is to evaluate how reliably a Dialogflow CX agent classifies Spanish user utterances and routes them to the expected conversational state.

The evaluation separates:

- intent classification,
- page routing,
- no-match behavior,
- improvement after training changes,
- ambiguous utterances.

---

## 1. Intent Accuracy

Intent Accuracy measures how often the detected intent matches the expected intent.

Formula:

```text
Intent Accuracy =
Correct intent predictions
--------------------------
Total evaluable utterances
```

Example:

```text
Expected intent: Derivaciones
Detected intent: Derivaciones
Result: Correct
```

Ambiguous test cases are excluded from the primary Intent Accuracy calculation.

---

## 2. Page Accuracy

Page Accuracy measures whether the conversation reaches the expected Dialogflow CX page.

Formula:

```text
Page Accuracy =
Correct page predictions
------------------------
Total evaluable utterances
```

Example:

```text
Expected page: Opciones derivaciones
Actual page: Opciones derivaciones
Result: Correct
```

This metric complements Intent Accuracy because an intent can be correctly detected while the conversation still transitions to an unexpected page.

---

## 3. No Match Rate

No Match Rate measures how often Dialogflow CX fails to detect an intent.

A No Match occurs when:

```text
actual_intent = empty
```

Formula:

```text
No Match Rate =
No Match cases
--------------
Total evaluable utterances
```

Example:

```text
Utterance:
¿Quién podría orientarme en el colegio?

Detected intent:
None

Result:
No Match
```

A high No Match Rate may indicate insufficient semantic coverage in the training phrases.

---

## 4. Improvement Rate

Improvement Rate measures how many initially failing test cases become successful after modifying the training dataset.

A case is considered improved when the same `test_id` contains:

```text
Iteration 1 → FAIL
Iteration 2 → PASS
```

Example:

```text
DER-001 iteration 1
FAIL

DER-001 iteration 2
PASS
```

Formula:

```text
Improvement Rate =
Initially failing cases later corrected
---------------------------------------
Initially failing cases with reevaluation
```

This metric helps document whether changes to training phrases actually improve the agent.

---

## 5. Ambiguous Cases

Some user utterances may reasonably correspond to more than one intent.

These cases should not automatically be counted as classification errors.

Two categories are currently used:

### AMBIGUOUS_ACCEPTABLE

The agent chooses one of several semantically reasonable intents.

Example:

```text
Quiero hablar con alguien del colegio por mi hijo
```

Possible interpretations:

```text
Entrevistas
Contacto equipo de apoyo
```

If the agent selects one of these reasonable alternatives, the result can be marked:

```text
AMBIGUOUS_ACCEPTABLE
```

### AMBIGUOUS_NO_MATCH

The utterance is genuinely ambiguous and the agent produces no intent match.

Example:

```text
¿Quién podría orientarme en el colegio?
```

Possible interpretations:

```text
Contacto con una persona
Servicios de apoyo
```

These cases are recorded separately from the primary accuracy calculation.

---

## 6. Status Values

The manual evaluation dataset currently uses the following status values:

### PASS

The detected intent and conversational routing match the expected behavior.

### FAIL

The agent detects the wrong intent or produces a No Match for a case with a clear expected intent.

### AMBIGUOUS_ACCEPTABLE

The utterance has more than one reasonable interpretation and the agent selects an acceptable one.

### AMBIGUOUS_NO_MATCH

The utterance is genuinely ambiguous and the agent produces a No Match.

---

## 7. Iterations

Each test case has a stable `test_id`.

The `iteration` field records repeated evaluations after changes to the agent.

Example:

```text
DER-001, iteration 1 → FAIL
DER-001, iteration 2 → PASS
```

This allows the toolkit to preserve the complete evaluation history instead of overwriting previous results.

---

## 8. Primary Evaluation Dataset

The manual evaluation file is located at:

```text
results/manual_evaluation.csv
```

Its current structure is:

```text
test_id
iteration
utterance
expected_intent
actual_intent
expected_page
actual_page
status
change_applied
notes
```

---

## 9. Future Metrics

Once the automated evaluation pipeline is connected to Dialogflow CX, the toolkit should also calculate:

- Precision per intent
- Recall per intent
- F1-score per intent
- Confusion matrix
- Confidence score statistics
- Intent-level No Match Rate
- Accuracy before and after training changes

These metrics should be calculated only on test cases with a single clearly defined expected intent.

Ambiguous cases should be reported separately.

---

## 10. Evaluation Principle

The toolkit should distinguish between:

```text
MODEL ERROR
```

The utterance has a clear expected intent, but the agent predicts another intent or produces No Match.

```text
DATASET COVERAGE ISSUE
```

The intent is appropriate, but the training phrases do not sufficiently represent the user's formulation.

```text
INTENT OVERLAP
```

Two or more intents contain semantically similar training phrases and compete for the same utterance.

```text
GENUINE AMBIGUITY
```

The user utterance can reasonably correspond to more than one intent.

The purpose of the toolkit is not only to measure accuracy, but also to help identify why an error occurred and whether changes to the training data improve the agent.
