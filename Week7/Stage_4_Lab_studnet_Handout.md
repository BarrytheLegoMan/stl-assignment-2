# Assignment 2 - Case Study Stage 4 Lab Activities Implementing the SmartCare Domain Layer

## A – Revisit Approved UML

Before coding, confirm:

- **Patient**  
  - Attributes: patient_id, name, dob, contact_details  
  - Responsibilities: maintain details, provide history  
  - Relationship: 1 patient → many appointments  

- **Practitioner**  
  - Attributes: practitioner_id, name, specialty, availability  
  - Responsibilities: maintain details, provide schedule  
  - Relationship: 1 practitioner → many appointments  

- **Appointment**  
  - Attributes: appointment_id, patient_id, practitioner_id, date_time, status  
  - Responsibilities: manage lifecycle, enforce status rules, detect duplicates  
  - Relationship: each appointment links exactly one patient and one practitioner

## B – Implement Patient (AI OFF)

patient.py


## C – Implement Practitioner (AI OFF)

Practitoner.py  


## D – Implement Appointment (AI ON)

Provide AI with:

### Required UML attributes
- appointment_id  
- patient_id  
- practitioner_id  
- date_time  
- status  

### Required behaviours
- book()  
- cancel()  
- update_status()  
- detect_duplicate()  

### Required constraints
- Status must follow legal transitions  
- Appointment must reference existing patient + practitioner  
- Duplicate detection must follow agreed rule (time + practitioner + patient)  
- No SQL  
- No NotificationManager  
- No inheritance from Patient or Practitioner  
- Status must be an enum  
- Illegal transitions must raise a domain exception  

Apppointment.py

## E – Review Generated Code

Check for:

- **Model consistency**  
  - Attributes match UML  
  - Methods match approved behaviours  

- **Unsupported features**  
  - No invented fields  
  - No invented methods  

- **Public state mutation**  
  - status must not be publicly writable  
  - patient_id and practitioner_id must be protected  

- **Unnecessary inheritance**  
  - Appointment must NOT inherit from PatientRecord or similar  

- **Invented dependencies**  
  - No NotificationManager  
  - No database connectors  
  - No external services  

- **Error handling**  
  - Must use domain exceptions  
  - Must reject illegal status transitions  
  - Must validate required fields  


## F – Manual Behaviour Checks

### Create valid objects
- Create a valid Patient  
- Create a valid Practitioner  
- Create a valid Appointment  
- Ensure status defaults to SCHEDULED  

### Test invalid input
- Invalid patient_id → exception  
- Invalid practitioner_id → exception  
- Invalid date_time → exception  
- Invalid status → exception  
- Illegal status transition (e.g., CANCELLED → SCHEDULED) → exception  
- Duplicate booking → warning or exception depending on rule  

## G – Refactor

After reviewing the Appointment implementation, several refactoring steps were applied to ensure the code remained simple, domain‑consistent, and aligned with the approved UML:

## H – AI Engineering Log

### AI Prompt Used
Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.

---

### Generated Contribution (Summary)

The AI produced:
- An Appointment class with the correct UML attributes  
- A basic constructor with type hints  
- An AppointmentStatus enum  
- Methods for book(), cancel(), update_status(), and detect_duplicate()  
- Some validation logic  
- Some invented or unnecessary features (later removed)  

However, the AI also generated:
- Public status mutation  
- SQL logic inside cancel()  
- A NotificationManager dependency  
- Over‑complex state transition logic  
- Occasional inheritance from PatientRecord  
- Extra fields not present in the UML  

These were corrected during refactoring.

---

### Decisions Made

| Issue Identified | Decision | Reason |
|------------------|----------|--------|
| Public `status` attribute | Refactored to protected | Status transitions must be controlled by domain rules |
| SQL inside methods | Removed | Domain objects must not handle persistence |
| NotificationManager dependency | Removed | Out of scope for SmartCare v0.2/v0.3 |
| Inheritance from PatientRecord | Rejected | Appointment is not a subtype of PatientRecord |
| Raw string statuses | Replaced with enum | Prevents invalid values and enforces domain constraints |
| Invented fields (timestamps, metadata) | Removed | Not present in approved UML |
| Over‑engineered state machine | Simplified | UML defines only basic transitions (SCHEDULED → CANCELLED) |
| Duplicate detection logic too complex | Simplified | Must match the business rule defined in FR‑07 |

---

### Verification Evidence

- All attributes match the approved UML exactly.  
- No invented fields or dependencies remain.  
- Status transitions follow SmartCare business rules.  
- Illegal transitions raise domain exceptions.  
- Cancelled appointments remain as objects (FR‑12).  
- No SQL, UI, or external services appear in the class.  
- Type hints match the domain model.  
- Manual behaviour checks confirm correct handling of valid and invalid input.  

---

## Reflection

The AI-generated Appointment class required several corrections.  
The main modifications were:

- Protecting internal state (status)  
- Enforcing legal status transitions  
- Replacing raw strings with enums  
- Rejecting incorrect inheritance  
- Removing fields not present in the UML  

These changes were necessary because the **approved design strictly constrained the AI**:

- The UML defines only five attributes and four behaviours.  
- SmartCare v0.2 explicitly excludes notifications, databases, and external services.  
- Domain objects must remain simple, validated, and storage‑agnostic.  
- Appointment is an association between Patient and Practitioner, not a subtype.  
- Status transitions must follow the business rules, not AI‑invented logic.

The AI tends to over‑design, but the approved domain model forced the implementation to remain **minimal, consistent, and aligned with SmartCare’s business rules**.
