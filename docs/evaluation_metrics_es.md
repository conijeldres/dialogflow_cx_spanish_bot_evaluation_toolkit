# Métricas de evaluación

Este documento define los criterios de evaluación utilizados por `dialogflow_cx_spanish_bot_evaluation_toolkit`.

El objetivo del toolkit es evaluar con qué nivel de fiabilidad un agente de Dialogflow CX clasifica expresiones de usuarios en español y las dirige al estado conversacional esperado.

La evaluación distingue entre:

- clasificación de intents,
- enrutamiento a páginas,
- comportamiento No Match,
- mejora después de cambios en el entrenamiento,
- expresiones ambiguas.

---

## 1. Exactitud de intent

La Exactitud de Intent mide con qué frecuencia la intent detectada coincide con la intent esperada.

Fórmula:

```text
Exactitud de Intent =
Predicciones de intent correctas
---------------------------------
Total de expresiones evaluables
```

Ejemplo:

```text
Intent esperada: Derivaciones
Intent detectada: Derivaciones
Resultado: Correcto
```

Los casos ambiguos se excluyen del cálculo principal de Exactitud de Intent.

---

## 2. Exactitud de página

La Exactitud de Página mide si la conversación llega a la página esperada de Dialogflow CX.

Fórmula:

```text
Exactitud de Página =
Predicciones de página correctas
---------------------------------
Total de expresiones evaluables
```

Ejemplo:

```text
Página esperada: Opciones derivaciones
Página actual: Opciones derivaciones
Resultado: Correcto
```

Esta métrica complementa la Exactitud de Intent, ya que una intent puede ser detectada correctamente mientras la conversación transiciona a una página inesperada.

---

## 3. Tasa de No Match

La Tasa de No Match mide con qué frecuencia Dialogflow CX no logra detectar una intent.

Se considera No Match cuando:

```text
actual_intent = vacío
```

Fórmula:

```text
Tasa de No Match =
Casos No Match
--------------
Total de expresiones evaluables
```

Ejemplo:

```text
Expresión:
¿Quién podría orientarme en el colegio?

Intent detectada:
Ninguna

Resultado:
No Match
```

Una Tasa de No Match alta puede indicar una cobertura semántica insuficiente en las training phrases.

---

## 4. Tasa de mejora

La Tasa de Mejora mide cuántos casos de prueba que inicialmente fallaban pasan a funcionar correctamente después de modificar el dataset de entrenamiento.

Un caso se considera mejorado cuando el mismo `test_id` contiene:

```text
Iteración 1 → FAIL
Iteración 2 → PASS
```

Ejemplo:

```text
DER-001 iteración 1
FAIL

DER-001 iteración 2
PASS
```

Fórmula:

```text
Tasa de Mejora =
Casos inicialmente fallidos que luego fueron corregidos
--------------------------------------------------------
Casos inicialmente fallidos con reevaluación
```

Esta métrica permite documentar si los cambios realizados en las training phrases mejoran efectivamente el comportamiento del agente.

---

## 5. Casos ambiguos

Algunas expresiones de usuario pueden corresponder razonablemente a más de una intent.

Estos casos no deben contabilizarse automáticamente como errores de clasificación.

Actualmente se utilizan dos categorías:

### AMBIGUOUS_ACCEPTABLE

El agente selecciona una de varias intents semánticamente razonables.

Ejemplo:

```text
Quiero hablar con alguien del colegio por mi hijo
```

Interpretaciones posibles:

```text
Entrevistas
Contacto equipo de apoyo
```

Si el agente selecciona una de estas alternativas razonables, el resultado puede marcarse como:

```text
AMBIGUOUS_ACCEPTABLE
```

### AMBIGUOUS_NO_MATCH

La expresión es realmente ambigua y el agente no detecta ninguna intent.

Ejemplo:

```text
¿Quién podría orientarme en el colegio?
```

Interpretaciones posibles:

```text
Contacto con una persona
Servicios de apoyo
```

Estos casos se registran de forma separada respecto del cálculo principal de exactitud.

---

## 6. Valores de estado

El dataset de evaluación manual utiliza actualmente los siguientes valores de estado:

### PASS

La intent detectada y el enrutamiento conversacional coinciden con el comportamiento esperado.

### FAIL

El agente detecta una intent incorrecta o produce un No Match en un caso con una intent esperada claramente definida.

### AMBIGUOUS_ACCEPTABLE

La expresión admite más de una interpretación razonable y el agente selecciona una opción aceptable.

### AMBIGUOUS_NO_MATCH

La expresión es genuinamente ambigua y el agente produce un No Match.

---

## 7. Iteraciones

Cada caso de prueba posee un `test_id` estable.

El campo `iteration` registra evaluaciones repetidas después de realizar cambios en el agente.

Ejemplo:

```text
DER-001, iteración 1 → FAIL
DER-001, iteración 2 → PASS
```

Esto permite que el toolkit conserve el historial completo de evaluación en lugar de sobrescribir resultados anteriores.

---

## 8. Dataset principal de evaluación

El archivo de evaluación manual se encuentra en:

```text
results/manual_evaluation.csv
```

Su estructura actual es:

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

## 9. Métricas futuras

Cuando el pipeline de evaluación automática esté conectado a Dialogflow CX, el toolkit también debería calcular:

- Precisión por intent
- Recall por intent
- F1-score por intent
- Matriz de confusión
- Estadísticas de confidence score
- Tasa de No Match por intent
- Exactitud antes y después de cambios en el entrenamiento

Estas métricas deben calcularse únicamente sobre casos de prueba con una sola intent esperada claramente definida.

Los casos ambiguos deben informarse por separado.

---

## 10. Principio de evaluación

El toolkit debe distinguir entre:

```text
MODEL ERROR
```

La expresión tiene una intent esperada claramente definida, pero el agente predice otra intent o produce No Match.

```text
DATASET COVERAGE ISSUE
```

La intent es apropiada, pero las training phrases no representan suficientemente la forma en que el usuario formula su solicitud.

```text
INTENT OVERLAP
```

Dos
