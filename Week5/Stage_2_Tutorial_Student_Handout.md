# Assignment 2 Case Study - Stage 2 Tutorial From Problems to Requirements

## Activity 1: Stakeholder Map

| Stakeholder                    | Need                                                                      | Potential conflict                                                            |
|--------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Management                     | A small, maintainable system                                              | Additional requested features may increase scope and maintenance effort       |
| Staff                          | Fewer duplicate bookings, easier patient searches and consistent statuses | Quick access may conflict with controls needed to protect patient information |
| Patients                       | Accurate patient and appointment records                                  | Privacy requirements may limit staff access; the details need confirmation    |
| Practitioners                  | Accurate practitioner and appointment information                         | Schedule or clinical features may exceed the confirmed scope                  |
| System maintainer or developer | Maintainable and independently testable business logic                    | Technical quality work may compete with requests for more visible features    |

## Activity 2: Functional or Non-Functional?

1. **Functional:** The system shall allow staff to cancel an appointment.
2. **Non-functional:** The system should remain responsive for the course-scale dataset.
3. **Functional:** The system shall retain canceled appointments.
4. **Non-functional:** Core business logic should be independently testable.
5. **Functional:** The system shall search for a patient by ID.

## Activity 3: Repair Ambiguous Requirements

### “The system should be easy to use.”

- **Problem:** “Easy to use” is subjective and cannot be tested without defined users, tasks, conditions and success measures.
- **Clarification question:** Which users and core tasks should be assessed, under what conditions, and what measurable result would demonstrate acceptable usability?

### “Patient search should be fast.”

- **Problem:** “Fast” has no response-time target, dataset size or operating conditions.
- **Clarification question:** What maximum response time is acceptable, and for what dataset size and workload?

### “The system should securely manage data.”

- **Problem:** “Securely” does not identify the protected data, required controls, user roles or testable outcome.
- **Clarification question:** Which data must be protected, which roles may access it, and which authentication, authorisation, logging or other controls are required?

### “Appointments should normally be easy to cancel.”

- **Problem:** “Normally” and “easy” are ambiguous. The authorised role, exceptions and required result are not specified.
- **Clarification question:** Who may cancel an appointment, in which appointment states, and what information must remain after cancellation?

## Activity 4: AI Requirements Audit

| AI suggestion                            | Classification                      | Evidence or reason                                                                                                     |
|------------------------------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Patients receive SMS reminders           | Unsupported                         | The client brief does not mention reminders or SMS                                                                     |
| Facial recognition login                 | Unsupported and likely out of scope | No authentication method is stated, and facial recognition is not supported by the brief                               |
| Receptionists create appointments        | Assumption requiring validation     | Appointment management is relevant, but the brief refers to “staff” and does not identify receptionists or permissions |
| Online payment                           | Unsupported and likely out of scope | Payments are not mentioned in the brief                                                                                |
| Practitioners view schedules             | Assumption requiring validation     | Practitioner and appointment information are in scope, but practitioner schedule access is not stated                  |
| AI recommends treatments                 | Out of scope                        | The brief concerns patient, practitioner and appointment administration; treatment recommendations are not supported   |
| Cancelled appointments remain in history | Assumption requiring validation     | Limited appointment history is a stated problem, but cancelled-record retention is not directly confirmed              |

## Exit Question

“AI suggested it” is not sufficient evidence because AI can produce plausible features that the client never requested. A requirement should be traceable to a verified stakeholder need, client statement, policy, business rule or other authorised source. An unsupported AI suggestion should be rejected or recorded as an assumption or clarification question until it is validated.