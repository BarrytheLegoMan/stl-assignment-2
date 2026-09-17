# SmartCare v0.2 Requirements Specification

## 1. Problem and Scope

SmartCare currently uses spreadsheets and paper records. Staff have reported duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system.

### In scope

- Patient records.
- Practitioner records.
- Appointment records.
- Patient search.
- Appointment creation and management.
- Duplicate-booking detection or prevention.
- Consistent appointment statuses.
- Appointment history.
- A small and maintainable solution.

### Out of scope unless confirmed

- SMS or email reminders.
- Online payments.
- Facial recognition.
- AI treatment recommendations.
- Patient self-service booking.
- Telehealth.
- External-system integrations.
- Mobile applications.

## 2. Stakeholders

| Stakeholder                    | Need                                                                                                        | Evidence                                                            |
|--------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Management                     | A small, maintainable patient, practitioner and appointment system                                          | Confirmed by client brief                                           |
| Staff                          | Reduce duplicate bookings, find patient information, use consistent statuses and access appointment history | Confirmed by client brief                                           |
| Patients                       | Accurate patient and appointment records                                                                    | Provisional; not directly stated                                    |
| Practitioners                  | Accurate practitioner and appointment information                                                           | Provisional; detailed tasks not stated                              |
| System maintainer or developer | Maintainable and testable business logic                                                                    | Maintainability confirmed; detailed testability requires validation |

## 3. Functional Requirements

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

## 4. Non-Functional Requirements

- **NFR-01 Maintainability:** The system shall separate core business logic from the user interface so the business logic can be tested independently. **Provisional.**
- **NFR-02 Data integrity:** The system shall not save an appointment unless it references an existing patient and practitioner. **Requires validation.**
- **NFR-03 Reliability:** The system shall preserve previously saved appointment data when an attempted update fails. **Requires an agreed failure scenario.**
- **NFR-04 Usability:** A trained staff member shall complete the agreed core appointment tasks against an agreed success measure. **Target not yet defined.**
- **NFR-05 Performance:** Patient search results shall be returned within an agreed response time for the course-scale dataset. **Target and dataset not yet defined.**
- **NFR-06 Testability:** Each core business rule shall have an automated successful test and an applicable failure test. **Requires validation.**

## 5. User Stories

- **US-01:** As a staff member, I want to find a patient record by identifier so that I can locate the correct patient information.
- **US-02:** As a staff member, I want to create an appointment linked to a patient and practitioner so that the booking is recorded consistently.
- **US-03:** As a staff member, I want the system to warn me about a potential duplicate booking so that duplicate appointments can be avoided.
- **US-04:** As a staff member, I want to update an appointment status so that its current state is clear.
- **US-05:** As a staff member, I want to view a patient's appointment history so that previous appointments can be located.
- **US-06:** As a staff member, I want to cancel an appointment without deleting its history so that the record remains available. **Provisional.**

## 6. Acceptance Criteria

### US-01: Find a patient

**Scenario 1: Matching patient exists**

- **GIVEN** a patient record exists with the entered identifier
- **WHEN** a staff member searches using that identifier
- **THEN** the system displays the matching patient record

**Scenario 2: No matching patient exists**

- **GIVEN** no patient record exists with the entered identifier
- **WHEN** a staff member searches using that identifier
- **THEN** the system reports that no match was found and does not display a different patient's record

### US-02: Create an appointment

**Scenario 1: Valid appointment**

- **GIVEN** the selected patient and practitioner exist and the appointment is not identified as a duplicate
- **WHEN** a staff member enters the required information and saves it
- **THEN** the system creates the appointment and links it to the selected patient and practitioner

**Scenario 2: Required information is missing**

- **GIVEN** required appointment information is missing
- **WHEN** a staff member attempts to save the appointment
- **THEN** the system does not create it and identifies the missing information

### US-03: Potential duplicate booking

- **GIVEN** an existing appointment matches the agreed duplicate-booking conditions
- **WHEN** a staff member attempts to save another matching appointment
- **THEN** the system warns the staff member and follows the agreed duplicate-resolution rule

### US-04: Update appointment status

**Scenario 1: Permitted status**

- **GIVEN** an appointment exists and the requested status is permitted
- **WHEN** a staff member updates its status
- **THEN** the system saves and displays the new status

**Scenario 2: Invalid status**

- **GIVEN** an appointment exists
- **WHEN** a staff member enters a status outside the agreed values
- **THEN** the system rejects the update and retains the previous status

### US-05: View appointment history

- **GIVEN** a patient has recorded appointments
- **WHEN** a staff member opens that patient's appointment history
- **THEN** the system displays the recorded appointments and their statuses

### US-06: Cancel and retain appointment

- **GIVEN** an appointment exists and cancellation is permitted
- **WHEN** a staff member cancels it
- **THEN** the system applies the agreed cancelled status and retains the appointment in history

**Status:** Provisional until cancellation and retention rules are confirmed.

## 7. Assumptions and Open Questions

### Assumptions requiring validation

- Staff are authorised to maintain patient and appointment information.
- Patient and practitioner records use unique identifiers.
- Appointment statuses use a controlled list.
- Duplicate detection occurs when appointments are created or changed.
- Appointment history may include cancelled appointments or status changes.

### Open questions

1. What fields must be stored for patients, practitioners and appointments?
2. Which user roles may view or change each type of information?
3. What exact conditions define a duplicate booking?
4. Which appointment statuses and transitions are allowed?
5. Must cancelled appointments be retained, and for how long?
6. What information must appointment history contain?
7. Which patient search fields are required?
8. What response time and dataset size define acceptable performance?
9. What privacy, security, authentication, authorisation and audit controls apply?
10. What technical constraints define a small and maintainable solution?

## 8. AI Requirements Review Record

| AI suggestion                            | Evidence?                                         | Decision                             | Reason                                                        | Verification                                                    |
|------------------------------------------|---------------------------------------------------|--------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------|
| Define duplicate-booking conditions      | The problem is confirmed, but the rule is missing | Accepted as a clarification question | A rule cannot be invented                                     | Ask the client to define matching fields and override behaviour |
| Add patient search by ID                 | Tutorial example and client problem               | Modified                             | Search is supported but final search fields need confirmation | Confirm identifiers and search fields                           |
| Retain cancelled appointments in history | Indirect and tutorial evidence only               | Unverified                           | Client brief does not expressly confirm retention             | Ask about cancellation and retention                            |
| Add SMS reminders                        | No                                                | Rejected                             | Not stated in client brief                                    | No action unless requested                                      |
| Add role-based access                    | General concern only                              | Unverified                           | Roles and controls need clarification                         | Ask which roles and controls are required                       |
| Make performance measurable              | Requirements-quality evidence                     | Accepted as a clarification question | “Responsive” is not testable without a target                 | Obtain response-time and dataset targets                        |
