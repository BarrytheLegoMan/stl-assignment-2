# SmartCare v0.3 – Domain Model Workbook  

## Requirement-to-Concept Trace

| Requirement                             | Concept      | State / Behaviour                                      | Decision                                             |
|-----------------------------------------|--------------|--------------------------------------------------------|------------------------------------------------------|
| FR‑01: Create patient record            | Patient      | patient_id, name, dob, contact_details                 | Confirmed class                                      |
| FR‑02: Search patient by ID             | Patient      | get_by_id()                                            | Behaviour belongs in service layer, not domain class |
| FR‑03: Update patient record            | Patient      | update_details()                                       | Confirmed behaviour                                  |
| FR‑04: Create practitioner record       | Practitioner | practitioner_id, name, specialty                       | Confirmed class                                      |
| FR‑05: Update practitioner record       | Practitioner | update_details()                                       | Confirmed behaviour                                  |
| FR‑06: Create appointment               | Appointment  | appointment_id, patient_id, practitioner_id, date_time | Confirmed class                                      |
| FR‑07: Detect duplicate booking         | Appointment  | detect_duplicate()                                     | Behaviour confirmed; rule needs clarification        |
| FR‑08: Display appointment status       | Appointment  | status                                                 | Confirmed attribute                                  |
| FR‑09: Update appointment status        | Appointment  | update_status()                                        | Confirmed behaviour                                  |
| FR‑10: Display appointment history      | Patient      | view_history()                                         | Confirmed behaviour                                  |
| FR‑11: Cancel appointment (provisional) | Appointment  | cancel()                                               | Included but provisional                             |
| FR‑12: Retain cancelled appointment     | Appointment  | status="cancelled"                                     | Confirmed but provisional                            |

---

## CRC Cards

### Patient

| Responsibilities            | Collaborators |
|-----------------------------|---------------|
| Maintain patient details    | Appointment   |
| Provide appointment history | Appointment   |

---

### Practitioner

| Responsibilities                 | Collaborators |
|----------------------------------|---------------|
| Maintain practitioner details    | Appointment   |
| Provide availability information | Appointment   |

---

### Appointment

| Responsibilities                    | Collaborators         |
|-------------------------------------|-----------------------|
| Link patient and practitioner       | Patient, Practitioner |
| Maintain appointment status         | Patient, Practitioner |
| Detect potential duplicate bookings | Patient, Practitioner |

---

### Optional Class (ClinicSystem)

| Responsibilities                                           | Collaborators                      |
|------------------------------------------------------------|------------------------------------|
| Coordinate creation and updating of domain objects         | Patient, Practitioner, Appointment |
| Enforce business rules (duplicate detection, status rules) | Appointment                        |

---

## UML Class Diagram

### classDiagram
    class Patient {
        +patient_id
        +name
        +dob
        +contact_details
        +update_details()
        +view_history()
    }

    class Practitioner {
        +practitioner_id
        +name
        +specialty
        +availability
        +update_details()
        +view_schedule()
    }

    class Appointment {
        +appointment_id
        +patient_id
        +practitioner_id
        +date_time
        +status
        +book()
        +cancel()
        +update_status()
        +detect_duplicate()
    }

    Patient "1" --> "0..*" Appointment
    Practitioner "1" --> "0..*" Appointment

## Design Rationale

Based on confirmed SmartCare v0.2 requirements.

### Class Selection
Patient, Practitioner and Appointment were selected because they appear directly in functional requirements FR‑01 to FR‑12. These are core domain entities and represent the minimum viable model for SmartCare v0.3.  

### Responsibility Allocation
Patient and Practitioner store identity and descriptive information only.  
Appointment contains behavioural logic such as status updates and duplicate detection because these behaviours are explicitly required in FR‑07 to FR‑12.  
Appointment history is accessed through Patient because FR‑10 specifies that history is viewed “for a selected patient.”

### Key Relationships
Patient to Appointment is one‑to‑many because a patient can have multiple appointments.  
Practitioner to Appointment is one‑to‑many because a practitioner can have multiple appointments.  
Appointment does not inherit from Patient or Practitioner because it is not a subtype; it is an association between them.

---

## AI Design Review Record

| AI Suggestion       | Evidence                   | Decision | Reason                             | Model Change                |
|---------------------|----------------------------|----------|------------------------------------|-----------------------------|
| PatientManager      | Not in requirements        | Rejected | Adds unnecessary complexity        | None                        |
| PractitionerManager | Not in requirements        | Rejected | Over‑designed for v0.2             | None                        |
| AppointmentManager  | FR‑06 to FR‑12             | Modified | Behaviour stays inside Appointment | No manager class added      |
| ClinicController    | Possible coordination role | Accepted | Helps enforce business rules       | Added optional ClinicSystem |
| NotificationManager | Out of scope               | Rejected | SMS/email not confirmed            | None                        |
| ScheduleEngine      | Over‑designed              | Rejected | Availability is simple attribute   | None                        |


