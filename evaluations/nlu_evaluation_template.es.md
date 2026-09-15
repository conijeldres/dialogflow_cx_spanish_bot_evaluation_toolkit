# Plantilla de evaluación NLU

## Metadatos de la prueba

- ID de prueba:
- Fecha:
- Evaluador/a:
- Versión del sistema / agente:
- Idioma:
- Entorno:

## Utterance

**Texto:**

**Intent esperado:**

**Intent predicho:**

**Intent correcto:** Sí / No

**Confidence score:**  
Si está disponible.

## Información lingüística

- Dificultad:
- Variante:
- Presencia de ambigüedad: Sí / No
- Tipo de ambigüedad:
- Notas:

## Evaluación de entidades

| Entidad esperada | Valor esperado | Entidad predicha | Valor predicho | Correcto |
|---|---|---|---|---|
| | | | | |

## Evaluación de routing

**Flow esperado:**

**Flow predicho:**

**Page esperada:**

**Page predicha:**

**Ruta correcta:** Sí / No

## Etiquetas de fallo

Seleccionar todas las que correspondan:

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