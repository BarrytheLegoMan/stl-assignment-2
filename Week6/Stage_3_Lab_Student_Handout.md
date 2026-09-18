# Assignment 2 – Case Study  - Stage 3 Lab activites SmartCare Domain Modelling

## A. Requirements Review

### Nouns (from SmartCare v0.2)
- Patient, Practitioner, Appointment  
- Patient record, Practitioner record  
- Appointment record, Appointment status, Appointment history  
- Duplicate booking  
- Staff member, Management  
- System, Business logic, User interface  
- Identifier, Status values  
- Cancellation, Search

### Verbs (from SmartCare v0.2)
- Create, Store, Search, Display  
- Update, Identify, Warn, Save  
- Reject, Cancel  
- Retain, Preserve, Validate  
- Confirm, Link, Maintain  
- Test, View  

### Business Rules (derived from FRs, NFRs, User Stories, Acceptance Criteria)
- BR‑01: Patient records must use unique identifiers.  
- BR‑02: Practitioner records must use unique identifiers.  
- BR‑03: Appointments must reference an existing patient and practitioner.  
- BR‑04: Duplicate bookings must be detected before saving.  
- BR‑05: Appointment statuses must use a controlled list.  
- BR‑06: Invalid status updates must be rejected and previous status retained.  
- BR‑07: Cancelled appointments must be retained in history (provisional).  
- BR‑08: Appointment history must display all recorded appointments.  
- BR‑09: Previously saved appointment data must be preserved if an update fails.  
- BR‑10: Business logic must be separated from UI for maintainability.  
- BR‑11: Patient search must return correct results and never display the wrong patient.  
- BR‑12: Required appointment fields must be validated before saving.  
- BR‑13: Duplicate detection rules must be confirmed.  
- BR‑14: Cancellation rules must be confirmed.  

## B. Candidate Classes

### Patient

State:
- patient_id  
- name  
- dob  
- contact_details  

Behaviour:
- update_details()  
- view_history()  

### Practitioner

State:
- practitioner_id  
- name  
- specialty  
- availability  

Behaviour:
- update_availability()  
- view_schedule()  

### Appointment

State:
- appointment_id  
- patient_id  
- practitioner_id  
- date_time  
- status  

Behaviour:
- book()  
- cancel()  
- update_status()  
- detect_duplicate()  

## C. CRC Cards

### Patient
Responsibilities:
- Maintain personal details  
- Provide appointment history  

Collaborators:
- Appointment  

### Practitioner
Responsibilities:
- Maintain availability  
- Provide schedule  

Collaborators:
- Appointment  

### Appointment
Responsibilities:
- Manage booking lifecycle  
- Maintain status  
- Detect duplicates  

Collaborators:
- Patient  
- Practitioner  

## D. UML Class Model
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
        +update_availability()
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

## E. AI Design Review

| AI Suggestion                      | Requirement Evidence  | Decision | Reason                                                 |
|------------------------------------|-----------------------|----------|--------------------------------------------------------|
| Add ClinicSystem controller        | FR‑01–FR‑12           | Accepted | Needed to coordinate core logic                        |
| Add AvailabilitySlot               | FR‑06, Open Questions | Modified | Too detailed for v0.2; simplified to availability list |
| Link Appointment → ReportGenerator | Out of scope          | Rejected | Reporting not confirmed in v0.2                        |

---

## F. Compare and Decide

### Accepted
- ClinicSystem (central controller)

### Modified
- AvailabilitySlot → simplified availability list inside Practitioner

### Rejected
- ReportGenerator linked directly to Appointment

---

## G. Python Skeletons

### python
    class Patient:
        def __init__(self, patient_id, name, dob, contact_details):
            self.patient_id = patient_id
            self.name = name
            self.dob = dob
            self.contact_details = contact_details
    
    
    class Practitioner:
        def __init__(self, practitioner_id, name, specialty, availability):
            self.practitioner_id = practitioner_id
            self.name = name
            self.specialty = specialty
            self.availability = availability
    
    
    class Appointment:
        def __init__(self, appointment_id, patient_id, practitioner_id, date_time, status):
            self.appointment_id = appointment_id
            self.patient_id = patient_id
            self.practitioner_id = practitioner_id
            self.date_time = date_time
           self.status = status

## H. Consistency Check

- UML attributes match Python attributes.
- Primary Keys are represented using IDs inside the Appointment class.
- No out‑of‑scope features (SMS, payments, telehealth, integrations) were included.

---

## Reflection

The most challenging modelling decision was determining which features belong in SmartCare v0.2 and which should be deferred to later iterations. Duplicate‑booking detection and cancellation rules were particularly difficult because the requirements mention them but do not fully define the conditions or workflow.

AI suggestions tended to over‑design the system by proposing detailed availability structures and reporting subsystems. These were not confirmed in the requirements and would have made the initial version more complex than intended.

