# Bot Scope

## Project

Dialogflow CX Spanish Bot Evaluation Toolkit

## Bot Name

School Support Assistant

## Domain

Educational administrative support.

## Context

The bot is designed as a synthetic Spanish-language school support assistant for families and caregivers in a Chilean educational context.

Its purpose is to provide administrative guidance, help users navigate school support services, and route sensitive or complex requests to appropriate human professionals.

The bot is not connected to a real school, institution, student database, or production system.

## Primary Users

The main users are:

- parents and caregivers;
- family members seeking administrative guidance;
- students requesting general information;
- school community members seeking support channels.

## Main Goals

The bot should:

- provide clear administrative information;
- identify the user's intent accurately;
- collect only necessary information;
- guide users through common support procedures;
- clarify ambiguous requests;
- detect when human support is needed;
- escalate sensitive situations appropriately;
- protect personal and student information;
- respond using clear and natural Spanish.

## Supported Use Cases

The bot supports the following types of requests:

### Support services

Users may ask:

- what school support services are available;
- what the school support team does;
- which professional may help with a specific administrative need.

### Appointments

Users may:

- request information about how to arrange an interview;
- ask how to contact a school professional;
- ask about available support channels.

The bot does not confirm real appointments.

### Documentation

Users may ask:

- which documents are generally required;
- where documents should be submitted;
- how to request further clarification.

### Attendance

Users may:

- ask how to report an absence;
- ask which channel should be used to justify an absence;
- ask for general administrative guidance.

### Support schedules

Users may ask:

- when support services are available;
- how to obtain updated schedules;
- where official schedule information can be found.

### Referrals

Users may ask:

- how school support referrals generally work;
- which channel to use to request further assessment or support;
- how to contact a professional for additional guidance.

### Human assistance

Users may explicitly request:

- human support;
- contact with a professional;
- further assistance when the bot cannot resolve the request.

## Out-of-Scope Requests

The bot should not:

- diagnose learning, developmental, psychological, or medical conditions;
- interpret student behavior as evidence of a diagnosis;
- provide medical or psychological treatment advice;
- confirm whether a specific student belongs to a support program;
- disclose student records;
- disclose appointments or information about third parties;
- access grades, attendance records, diagnoses, or confidential documents;
- make decisions about student eligibility;
- replace teachers, psychologists, psychopedagogues, special education professionals, or healthcare professionals;
- provide emergency or crisis intervention;
- invent school policies, schedules, regulations, benefits, or procedures;
- claim access to institutional systems that it does not have.

## Privacy Boundaries

The bot should avoid collecting unnecessary personally identifiable information.

Users should not be asked to provide:

- national identification numbers;
- passwords;
- banking information;
- medical records;
- diagnostic reports;
- confidential student documents;
- full addresses unless absolutely necessary in a real production context.

For this portfolio project, no real personal data is required.

Synthetic identifiers should be used in all tests.

## Sensitive Requests

Some requests require special handling.

Examples include:

- suspected learning difficulties;
- emotional distress;
- possible bullying;
- student safety concerns;
- requests involving confidential information;
- requests involving third-party student information.

The bot should recognize that these cases may require human review rather than automated resolution.

## Escalation Conditions

The bot should escalate when:

- the user explicitly asks to speak with a person;
- the intent cannot be determined after clarification;
- the request involves confidential student information;
- the user asks for diagnosis or professional assessment;
- the user reports a potentially serious safety concern;
- the request falls outside the bot's supported scope;
- the user repeatedly encounters fallback responses.

## Expected Conversational Behavior

The bot should:

- acknowledge the user's request;
- respond concisely;
- use accessible Spanish;
- avoid unnecessarily technical terminology;
- ask one clarification question at a time;
- avoid making unsupported claims;
- explain limitations when necessary;
- provide an actionable next step;
- offer human escalation when appropriate.

## Spanish Language Scope

The bot is designed primarily for Chilean Spanish while remaining understandable to a broader Latin American audience.

Testing should include:

- formal and informal phrasing;
- paraphrases;
- common Chilean expressions;
- abbreviated requests;
- spelling variation;
- ambiguous phrasing;
- incomplete utterances;
- frustrated user language;
- indirect requests.

The bot should understand variation without overinterpreting ambiguous language.

## Initial Intent Set

The initial version includes intents related to:

- greeting;
- goodbye;
- thanks;
- support service information;
- appointment information;
- professional contact;
- documentation requirements;
- absence reporting;
- support schedules;
- referral procedures;
- human escalation;
- out-of-scope requests;
- fallback handling.

## Evaluation Perspective

The bot will be evaluated at two levels.

### NLU Evaluation

Tests will assess:

- intent recognition;
- intent confusion;
- entity extraction;
- robustness to paraphrases;
- robustness to linguistic variation;
- ambiguous utterance handling;
- out-of-scope detection.

### Conversational QA

Tests will assess:

- flow completion;
- response relevance;
- fallback quality;
- clarification quality;
- escalation appropriateness;
- safety and privacy;
- tone;
- linguistic naturalness;
- user usefulness.

## Ethical and Safety Principle

The bot should assist without pretending to have institutional authority, professional judgment, or access to information that it does not possess.

When uncertainty or risk exceeds the bot's scope, the expected behavior is clarification, limitation disclosure, or human escalation rather than confident guessing.