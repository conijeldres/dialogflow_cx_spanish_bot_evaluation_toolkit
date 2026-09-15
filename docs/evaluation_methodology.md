# Evaluation Methodology

## Project

Dialogflow CX Spanish Bot Evaluation Toolkit

## Purpose

This methodology defines how the School Support Assistant is evaluated across NLU quality, entity extraction, conversational routing, fallback behavior, escalation, privacy, and user usefulness.

The evaluation combines quantitative and qualitative analysis.

The goal is not only to measure whether the bot selects the expected intent, but also whether the full conversational behavior is appropriate, safe, and useful.

## Evaluation Layers

The project evaluates the bot at three levels:

1. NLU Evaluation
2. Entity and Parameter Evaluation
3. Conversational QA

These layers are assessed independently and can also be analyzed together to understand end-to-end conversational performance.

---

## 1. NLU Evaluation

### Objective

Measure whether the system correctly identifies the expected user intent from Spanish-language utterances.

### Input

The evaluation uses:

- `training_phrases_es.jsonl`
- `test_utterances_es.jsonl`

Training phrases are used to define the intent space.

Test utterances are kept separate and are designed to evaluate generalization.

### Test Set Design

The test set includes:

- unseen paraphrases;
- formal and informal Spanish;
- Chilean lexical variation;
- abbreviated requests;
- minor spelling variation;
- implicit subjects;
- ambiguous utterances;
- overlapping intent boundaries;
- sensitive requests;
- out-of-scope requests;
- explicit human escalation requests.

### Primary Metric

#### Intent Accuracy

Intent accuracy measures the proportion of test utterances for which the predicted intent matches the expected intent.

```text
Intent Accuracy =
correct intent predictions / total test utterances