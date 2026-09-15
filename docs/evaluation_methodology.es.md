# Metodología de evaluación

## Proyecto

Dialogflow CX Spanish Bot Evaluation Toolkit

## Propósito

Esta metodología define cómo se evalúa el School Support Assistant en calidad NLU, extracción de entidades, routing conversacional, fallback, escalamiento, privacidad y utilidad para el usuario.

La evaluación combina análisis cuantitativo y cualitativo.

El objetivo no es únicamente medir si el bot selecciona el intent esperado, sino también observar si el comportamiento conversacional completo es adecuado, seguro y útil.

## Niveles de evaluación

El proyecto evalúa el bot en tres niveles:

1. Evaluación NLU
2. Evaluación de entidades y parámetros
3. QA conversacional

Estos niveles se analizan de forma independiente y también pueden combinarse para comprender el desempeño conversacional de extremo a extremo.

---

## 1. Evaluación NLU

### Objetivo

Medir si el sistema identifica correctamente la intención esperada a partir de utterances en español.

### Datos utilizados

La evaluación utiliza:

- `training_phrases_es.jsonl`
- `test_utterances_es.jsonl`

Las training phrases se utilizan para definir el espacio de intents.

Las utterances de prueba se mantienen separadas y están diseñadas para evaluar generalización.

### Diseño del set de prueba

El set incluye:

- paráfrasis no vistas;
- español formal e informal;
- variación léxica chilena;
- solicitudes abreviadas;
- variaciones ortográficas menores;
- sujetos implícitos;
- utterances ambiguas;
- fronteras entre intents similares;
- solicitudes sensibles;
- solicitudes fuera de alcance;
- solicitudes explícitas de atención humana.

### Métrica principal

#### Intent Accuracy

Mide la proporción de utterances de prueba en las que el intent predicho coincide con el intent esperado.

```text
Intent Accuracy =
predicciones correctas / total de utterances