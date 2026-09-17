# Assignment 2 Case Study Lab - Stage 2 Lab Activities SmartCare Requirements Engineering

## Part A: Client Brief

### Problem statement
SmartCare currently uses spreadsheets and paper records. Staff have reported duplicate bookings, difficulty locating patient information, inconsistent appointment statuses and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system.

## Part B: Stakeholders and Scope

### Stakeholders

| Stakeholder                    | Need                                                                                                      | Evidence status                                                               |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Management                     | A small, maintainable patient, practitioner and appointment system                                        | Confirmed in the brief                                                        |
| Staff                          | Fewer duplicate bookings, easier patient searches, consistent statuses and accessible appointment history | Confirmed in the brief                                                        |
| Patients                       | Accurate patient and appointment records                                                                  | Provisional; affected by the system but not directly described                |
| Practitioners                  | Accurate practitioner and appointment information                                                         | Provisional; practitioner records are in scope but their tasks are not stated |
| System maintainer or developer | A maintainable and testable solution                                                                      | Maintainability is confirmed; detailed testability needs validation           |

### In scope

- Create, store and update patient records.
- Create, store and update practitioner records.
- Create and manage appointment records.
- Search for patient information.
- Record consistent appointment statuses.
- Display appointment history.
- Identify or prevent duplicate bookings.
- Keep the solution small and maintainable.

### Out of scope or unsupported

- SMS or email reminders.
- Online payments.
- Facial recognition or biometric login.
- AI treatment recommendations.
- Patient self-service booking.
- Telehealth.
- Medicare, insurer or external system integration.
- A mobile application.

### Provisional matters

- Which staff roles can create, update or cancel appointments.
- Whether practitioners can view schedules.
- The data fields held in each record.
- The permitted appointment statuses.
- Whether cancelled appointments remain in history.
- Authentication and access-control requirements.

## Part C: Functional Requirements

- **FR-01:** The system shall create and store a patient record.
- **FR-02:** The system shall search for and display a patient record using a unique patient identifier.
- **FR-03:** The system shall update an existing patient record.
- **FR-04:** The system shall create and store a practitioner record.
- **FR-05:** The system shall update an existing practitioner record.
- **FR-06:** The system shall create an appointment linked to a patient and practitioner.
- **FR-07:** The system shall identify a potential duplicate booking before an appointment is saved.
- **FR-08:** The system shall display an appointment's current status.
- **FR-09:** The system shall update an appointment's status using agreed status values.
- **FR-10:** The system shall display appointment history for a selected patient.
- **FR-11:** The system shall cancel an appointment. **Provisional.**
- **FR-12:** The system shall retain a cancelled appointment in appointment history. **Provisional.**

## Part D: Non-Functional Requirements

- **NFR-01 Maintainability:** The system shall separate core business logic from the user interface so the business logic can be tested independently. **Provisional technical requirement.**
- **NFR-02 Data integrity:** The system shall not save an appointment unless it references an existing patient and practitioner. **Requires validation.**
- **NFR-03 Reliability:** The system shall preserve previously saved appointment data when an attempted update fails. **Requires an agreed failure scenario.**
- **NFR-04 Usability:** A trained staff member shall be able to complete agreed core appointment tasks. **Requires defined tasks and a measurable success target.**
- **NFR-05 Performance:** Patient search results shall be returned within an agreed response time for the course-scale dataset. **Requires a time target and dataset definition.**
- **NFR-06 Testability:** Each core business rule shall have an automated successful test and an applicable failure test. **Requires technical validation.**

## Part E: User Stories

- **US-01:** As a staff member, I want to find a patient record by identifier so that I can locate the correct patient information.
- **US-02:** As a staff member, I want to create an appointment linked to a patient and practitioner so that the booking is recorded consistently.
- **US-03:** As a staff member, I want the system to warn me about a potential duplicate booking so that duplicate appointments can be avoided.
- **US-04:** As a staff member, I want to update an appointment status so that its current state is clear.
- **US-05:** As a staff member, I want to view a patient's appointment history so that previous appointments can be located.
- **US-06:** As a staff member, I want to cancel an appointment without deleting its history so that the record remains available. **Provisional.**

## Acceptance Criteria

### US-01: Patient search

**Successful case**

- **GIVEN** a patient record exists with the entered identifier
- **WHEN** a staff member searches using that identifier
- **THEN** the system displays the matching patient record

**Failure case**

- **GIVEN** no patient record exists with the entered identifier
- **WHEN** a staff member searches using that identifier
- **THEN** the system reports that no match was found and does not display a different patient's record

### US-02: Appointment creation

**Successful case**

- **GIVEN** the selected patient and practitioner exist and the appointment is not identified as a duplicate
- **WHEN** a staff member supplies the required information and saves the appointment
- **THEN** the system creates the appointment and links it to the selected patient and practitioner

**Failure case**

- **GIVEN** required appointment information is missing
- **WHEN** a staff member attempts to save the appointment
- **THEN** the system does not create it and identifies the missing information

### US-03: Duplicate booking

- **GIVEN** an existing appointment matches the agreed duplicate-booking conditions
- **WHEN** a staff member attempts to save another matching appointment
- **THEN** the system warns the staff member and follows the agreed duplicate-resolution rule

**Open question:** The client must define what constitutes a duplicate and whether an override is allowed.

### US-04: Appointment status

**Successful case**

- **GIVEN** an appointment exists and the requested status is permitted
- **WHEN** a staff member updates the status
- **THEN** the system saves and displays the new status

**Failure case**

- **GIVEN** an appointment exists
- **WHEN** a staff member enters a status outside the agreed values
- **THEN** the system rejects the update and retains the previous status

## Part F: AI Requirements Review

Significant review findings:

1. “Fast”, “easy to use” and “securely manage data” are ambiguous unless measurable conditions are supplied.
2. The duplicate-booking rule is not defined.
3. Required appointment statuses are not listed.
4. User roles and permissions are not confirmed.
5. Appointment-history contents and cancellation retention are unclear.
6. SMS reminders, online payments and AI treatment recommendations are plausible but unsupported features.

## Part G: Verification of AI Review

| AI suggestion                            | Decision                             | Evidence and reason                                                                    |
|------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------|
| Define duplicate-booking conditions      | Accepted as a clarification question | Duplicate bookings are a stated problem, but the matching rule is absent               |
| Search by patient ID                     | Modified                             | The tutorial supports ID search, while the final search fields still need confirmation |
| Retain cancelled appointments in history | Unverified                           | Cancellation retention is not directly confirmed by the client brief                   |
| Add SMS reminders                        | Rejected                             | Not stated in the brief                                                                |
| Add role-based access                    | Unverified                           | Roles and controls need clarification rather than invention                            |
| Make performance measurable              | Accepted as a clarification question | “Responsive” cannot be tested without a target and dataset                             |

## Part H: Assumptions and Open Questions

1. What information must be stored for patients, practitioners and appointments?
2. Which user roles will use the system, and what may each role view or change?
3. What exact conditions define a duplicate booking?
4. Which appointment statuses and transitions are permitted?
5. Must cancelled appointments be retained, and for how long?
6. What must appointment history display?
7. Which patient search fields are required?
8. What response time and dataset size define acceptable performance?
9. What privacy, security, authentication, authorisation and audit requirements apply?
10. What technical constraints define “small” and “maintainable”?

## Reflection: Draft for Personalisation

The AI review helped identify that several draft requirements sounded reasonable but were not yet testable. Terms such as “fast”, “easy to use” and “securely manage data” did not include measurable conditions. The review also highlighted missing clarification questions about duplicate-booking rules, appointment statuses, user roles and the contents of appointment history. I treated these issues as open questions rather than inventing answers.

The AI overreached when it considered plausible features such as SMS reminders, online payments, authentication details and practitioner schedule views. These features could be useful, but the supplied client brief does not confirm them. I therefore rejected them or marked them as unverified.

FR-07 changed most after review. Instead of claiming a specific duplicate-booking rule, it now requires the system to identify a potential duplicate using conditions that the client must define. Requirements need evidence because they guide design, development and testing. Unsupported assumptions can cause the team to build the wrong capability, expand the scope and create acceptance tests that do not represent the client's needs.