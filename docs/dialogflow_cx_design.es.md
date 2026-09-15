# Diseño de Dialogflow CX

## Proyecto

Dialogflow CX Spanish Bot Evaluation Toolkit

## Nombre del agente

School Support Assistant

## Propósito

El agente está diseñado como un asistente sintético de apoyo escolar en español para familias y cuidadores en un contexto educativo chileno.

Su propósito es entregar orientación administrativa, identificar intents, recopilar únicamente los parámetros necesarios, guiar a los usuarios por procedimientos incluidos dentro del alcance y escalar solicitudes sensibles o no soportadas hacia atención humana.

## Arquitectura del agente

El agente se organiza en un flujo principal y varios flujos especializados.

### Main Flow

El Main Flow administra:

- saludos;
- orientación general;
- routing hacia flujos especializados;
- manejo de fallback;
- escalamiento humano;
- detección de solicitudes fuera de alcance;
- cierre de conversación.

### Support Information Flow

Administra:

- información sobre servicios de apoyo;
- información general sobre áreas de apoyo escolar;
- información sobre el equipo de apoyo.

Intent asociado:

- `consultar_servicios_apoyo`

### Appointments and Contact Flow

Administra:

- solicitudes de entrevista;
- solicitudes de contacto con profesionales;
- consultas de horarios.

Intents asociados:

- `solicitar_entrevista`
- `contactar_profesional`
- `consultar_horarios`

### Documentation and Attendance Flow

Administra:

- documentación requerida;
- información sobre inasistencias;
- orientación administrativa.

Intents asociados:

- `consultar_documentacion`
- `informar_inasistencia`

### Referral Flow

Administra:

- procedimientos de derivación;
- solicitudes de evaluación o apoyo;
- orientación general sobre acceso a servicios.

Intent asociado:

- `consultar_derivacion`

### Human Escalation Flow

Administra:

- solicitudes explícitas de atención humana;
- fallbacks repetidos;
- solicitudes sensibles;
- solicitudes relacionadas con privacidad;
- lenguaje de urgencia;
- solicitudes de juicio profesional fuera del alcance.

Intents asociados:

- `solicitar_humano`
- `fuera_de_alcance`

## Pages del Main Flow

### Start Page

Propósito:

- recibir al usuario;
- identificar su intent inicial;
- enrutarlo hacia el flujo correspondiente.

Rutas posibles:

```text
saludo
→ respuesta de bienvenida

consultar_servicios_apoyo
→ Support Information Flow

solicitar_entrevista
→ Appointments and Contact Flow

contactar_profesional
→ Appointments and Contact Flow

consultar_horarios
→ Appointments and Contact Flow

consultar_documentacion
→ Documentation and Attendance Flow

informar_inasistencia
→ Documentation and Attendance Flow

consultar_derivacion
→ Referral Flow

solicitar_humano
→ Human Escalation Flow

fuera_de_alcance
→ Human Escalation Flow