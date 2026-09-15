# Alcance del bot

## Proyecto

Dialogflow CX Spanish Bot Evaluation Toolkit

## Nombre del bot

School Support Assistant

## Dominio

Apoyo administrativo educativo.

## Contexto

El bot está diseñado como un asistente sintético de apoyo escolar en español para familias y cuidadores en un contexto educativo chileno.

Su propósito es entregar orientación administrativa, ayudar a los usuarios a navegar servicios de apoyo escolar y derivar solicitudes sensibles o complejas hacia profesionales humanos.

El bot no está conectado a un colegio real, institución, base de datos de estudiantes ni sistema productivo.

## Usuarios principales

Los usuarios principales son:

- madres, padres y cuidadores;
- familiares que buscan orientación administrativa;
- estudiantes que solicitan información general;
- integrantes de la comunidad escolar que buscan canales de apoyo.

## Objetivos principales

El bot debe:

- entregar información administrativa clara;
- identificar correctamente la intención del usuario;
- recopilar únicamente información necesaria;
- orientar sobre procedimientos habituales de apoyo;
- aclarar solicitudes ambiguas;
- detectar cuándo se requiere apoyo humano;
- escalar adecuadamente situaciones sensibles;
- proteger información personal y de estudiantes;
- responder en español claro y natural.

## Casos de uso incluidos

El bot admite los siguientes tipos de solicitudes:

### Servicios de apoyo

Los usuarios pueden preguntar:

- qué servicios de apoyo escolar existen;
- qué funciones cumple el equipo de apoyo;
- qué profesional podría orientar una determinada necesidad administrativa.

### Entrevistas

Los usuarios pueden:

- solicitar información sobre cómo coordinar una entrevista;
- preguntar cómo contactar a un profesional del establecimiento;
- consultar cuáles son los canales disponibles de atención.

El bot no confirma entrevistas reales.

### Documentación

Los usuarios pueden preguntar:

- qué documentos se requieren generalmente;
- dónde deben entregarse;
- cómo solicitar información adicional.

### Inasistencias

Los usuarios pueden:

- preguntar cómo informar una inasistencia;
- consultar qué canal utilizar para justificar una ausencia;
- solicitar orientación administrativa general.

### Horarios de atención

Los usuarios pueden preguntar:

- cuándo se encuentran disponibles los servicios de apoyo;
- cómo obtener horarios actualizados;
- dónde consultar información oficial sobre horarios.

### Derivaciones

Los usuarios pueden preguntar:

- cómo funcionan generalmente las derivaciones de apoyo escolar;
- qué canal utilizar para solicitar evaluación u orientación adicional;
- cómo contactar a un profesional.

### Asistencia humana

Los usuarios pueden solicitar explícitamente:

- apoyo humano;
- contacto con un profesional;
- asistencia adicional cuando el bot no pueda resolver la solicitud.

## Solicitudes fuera de alcance

El bot no debe:

- diagnosticar condiciones de aprendizaje, desarrollo, salud mental o salud física;
- interpretar la conducta de un estudiante como evidencia de un diagnóstico;
- entregar recomendaciones de tratamiento médico o psicológico;
- confirmar si un estudiante específico pertenece a un programa de apoyo;
- divulgar registros de estudiantes;
- entregar información sobre entrevistas o antecedentes de terceras personas;
- acceder a notas, asistencia, diagnósticos o documentos confidenciales;
- decidir si un estudiante cumple criterios de elegibilidad;
- reemplazar a docentes, psicólogos, psicopedagogos, profesionales de educación diferencial o profesionales de salud;
- realizar intervención de emergencia o crisis;
- inventar políticas, horarios, reglamentos, beneficios o procedimientos institucionales;
- afirmar que tiene acceso a sistemas institucionales cuando no lo tiene.

## Límites de privacidad

El bot debe evitar solicitar información personal identificable que no sea necesaria.

No se debe pedir a los usuarios:

- números de identificación nacional;
- contraseñas;
- información bancaria;
- fichas médicas;
- informes diagnósticos;
- documentos confidenciales del estudiante;
- direcciones completas salvo que fueran estrictamente necesarias en un entorno productivo real.

Para este proyecto de portfolio no se requieren datos personales reales.

Todas las pruebas deben utilizar identificadores sintéticos.

## Solicitudes sensibles

Algunas solicitudes requieren un manejo especial.

Ejemplos:

- sospechas de dificultades de aprendizaje;
- malestar emocional;
- posible bullying;
- preocupaciones de seguridad de estudiantes;
- solicitudes relacionadas con información confidencial;
- solicitudes sobre información de terceros.

El bot debe reconocer que estos casos pueden requerir revisión humana en lugar de resolución automática.

## Condiciones de escalamiento

El bot debe escalar cuando:

- el usuario solicita explícitamente hablar con una persona;
- no se logra determinar la intención después de una aclaración;
- la solicitud involucra información confidencial de un estudiante;
- el usuario solicita un diagnóstico o evaluación profesional;
- el usuario informa una posible situación grave de seguridad;
- la solicitud está fuera del alcance definido;
- el usuario recibe fallbacks de forma repetida.

## Comportamiento conversacional esperado

El bot debe:

- reconocer la solicitud del usuario;
- responder de manera breve y clara;
- utilizar español accesible;
- evitar terminología técnica innecesaria;
- realizar una pregunta de aclaración por vez;
- evitar afirmaciones sin respaldo;
- explicar sus limitaciones cuando corresponda;
- entregar un siguiente paso accionable;
- ofrecer derivación a atención humana cuando sea necesario.

## Alcance lingüístico en español

El bot está diseñado principalmente para español chileno, manteniendo comprensión para una audiencia latinoamericana más amplia.

Las pruebas deben incluir:

- formulaciones formales e informales;
- paráfrasis;
- expresiones habituales del español chileno;
- solicitudes abreviadas;
- variaciones ortográficas;
- formulaciones ambiguas;
- enunciados incompletos;
- lenguaje de usuarios frustrados;
- solicitudes indirectas.

El bot debe comprender la variación lingüística sin sobreinterpretar expresiones ambiguas.

## Conjunto inicial de intents

La primera versión contempla intents relacionados con:

- saludo;
- despedida;
- agradecimiento;
- información sobre servicios de apoyo;
- información sobre entrevistas;
- contacto con profesionales;
- requisitos de documentación;
- información de inasistencias;
- horarios de atención;
- procedimientos de derivación;
- escalamiento humano;
- solicitudes fuera de alcance;
- manejo de fallback.

## Perspectiva de evaluación

El bot será evaluado en dos niveles.

### Evaluación NLU

Las pruebas analizarán:

- reconocimiento de intents;
- confusión entre intents;
- extracción de entidades;
- robustez frente a paráfrasis;
- robustez frente a variación lingüística;
- manejo de enunciados ambiguos;
- detección de solicitudes fuera de alcance.

### QA conversacional

Las pruebas analizarán:

- completitud del flujo;
- relevancia de respuesta;
- calidad del fallback;
- calidad de aclaraciones;
- adecuación del escalamiento;
- seguridad y privacidad;
- tono;
- naturalidad lingüística;
- utilidad para el usuario.

## Principio ético y de seguridad

El bot debe ayudar sin simular autoridad institucional, juicio profesional o acceso a información que no posee.

Cuando la incertidumbre o el riesgo superen su alcance, el comportamiento esperado debe ser aclarar, reconocer la limitación o escalar a atención humana, en lugar de responder con seguridad injustificada.