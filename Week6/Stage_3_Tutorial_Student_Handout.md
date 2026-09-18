# Assignment 2 - Case Study - Stage 3 Tutorial activities From Requirements to Domain Models  

## Candidate Concepts

| Candidate    | Class? | Reason                                                                       |
|--------------|--------|------------------------------------------------------------------------------|
| Patient      | Yes    | Core domain entity; required by FR‑01 to FR‑03 and multiple user stories.    |
| Practitioner | Yes    | Core domain entity; required by FR‑04 and FR‑05.                             |
| Appointment  | Yes    | Central entity linking patient and practitioner; required by FR‑06 to FR‑12. |
| Name         | No     | Attribute of Patient or Practitioner, not a standalone domain concept.       |
| Clinic       | Maybe  | Could exist as a coordinating/system class, but not required in v0.2.        |
| Database     | No     | Technical infrastructure, not part of the domain model.                      |
| Cancellation | No     | Represents an appointment status or event, not a standalone class.           |
| Status       | No     | Controlled value/attribute of Appointment, not a domain class.               |

## CRC Cards

### Patient

| Responsibilities            | Collaborators |
|-----------------------------|---------------|
| Maintain patient details    | Appointment   |
| Provide appointment history | Appointment   |

### Practitioner

| Responsibilities                 | Collaborators |
|----------------------------------|---------------|
| Maintain practitioner details    | Appointment   |
| Provide availability information | Appointment   |

### Appointment

| Responsibilities                    | Collaborators         |
|-------------------------------------|-----------------------|
| Link patient and practitioner       | Patient, Practitioner |
| Maintain appointment status         | Patient, Practitioner |
| Detect potential duplicate bookings | Patient, Practitioner |

## Relationship Reasoning

### Patient → Appointment  
**Relationship:** One‑to‑many  
**Reason:**  
A patient can have multiple appointments .  
An appointment must link to exactly one patient.

### Practitioner → Appointment  
**Multiplicity:** One‑to‑many  
**Reason:**  
A practitioner can have many appointments.  
Each appointment must reference exactly one practitioner.

### Should Appointment inherit from Patient?  
**No.**  
Inheritance represents an “is‑a” relationship.  
An appointment is not a type of patient.

### Does Clinic need to own every object?  
**Not in v0.2.**  
A Clinic or ClinicSystem class may coordinate operations, but does not require to own it.

---

## AI Model Critique

### AI Proposal: PatientManager  
**Issue:** Over‑designed.  
**Reason:** v0.2 does not require separate manager classes; CRUD operations can be handled by business.

### AI Proposal: PractitionerManager  
**Issue:** Over-Designed.  
**Reason:** Adds unnecessary complexity for a small clinic system.

### AI Proposal: AppointmentManager  
**Issue:** Partially reasonable but premature.  
**Reason:** Appointment function exists, but the tracking of who making the appointment is complex in a simple system.

### AI Proposal: ClinicController  
**Decision:** Possibly useful later, but not required now.  
**Reason:** Could coordinate operations, but v0.2 emphasises simplicity.

### AI Proposal: NotificationManager  
**Rejected.**  
**Reason:** Notifications (SMS/email) are explicitly out of scope.

### AI Proposal: ScheduleEngine  
**Rejected for v0.2.**  
**Reason:** Over‑engineered; practitioner availability is simple. 