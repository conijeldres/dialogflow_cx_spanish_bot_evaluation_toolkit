# Dialogflow CX Design

## Project

Dialogflow CX Spanish Bot Evaluation Toolkit

## Agent Name

School Support Assistant

## Purpose

The agent is designed as a synthetic Spanish-language school support assistant for families and caregivers in a Chilean educational context.

Its purpose is to provide administrative guidance, identify user intents, collect only necessary parameters, guide users through supported procedures, and escalate sensitive or unsupported requests to human assistance.

## Agent Architecture

The agent is organized around one main flow and several specialized flows.

### Main Flow

The Main Flow handles:

- greetings;
- general orientation;
- routing to specialized flows;
- fallback handling;
- human escalation;
- out-of-scope detection;
- conversation closure.

### Support Information Flow

Handles:

- support service information;
- general information about school support areas;
- support team information.

Associated intents:

- `consultar_servicios_apoyo`

### Appointments and Contact Flow

Handles:

- interview requests;
- professional contact requests;
- support schedules.

Associated intents:

- `solicitar_entrevista`
- `contactar_profesional`
- `consultar_horarios`

### Documentation and Attendance Flow

Handles:

- required documentation;
- absence reporting;
- administrative guidance.

Associated intents:

- `consultar_documentacion`
- `informar_inasistencia`

### Referral Flow

Handles:

- referral procedures;
- requests for support evaluation;
- general guidance about support access.

Associated intents:

- `consultar_derivacion`

### Human Escalation Flow

Handles:

- explicit human assistance requests;
- repeated fallback;
- sensitive requests;
- privacy-related requests;
- urgent language;
- out-of-scope professional judgment requests.

Associated intents:

- `solicitar_humano`
- `fuera_de_alcance`

## Main Flow Pages

### Start Page

Purpose:

- greet the user;
- identify the initial intent;
- route to the corresponding flow.

Possible routes:

```text
saludo
→ welcome response

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