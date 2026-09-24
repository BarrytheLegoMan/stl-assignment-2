# SmartCare v0.4 - Domain Implementation Workbook

## 1. UML-to-Code Trace

| UML element | Python element | Implemented? | Notes |
|-------------|----------------|--------------|-------|
| Patient.patient_id | _patient_id (read-only property) | Yes | Immutable identifier protected via no setter |
| Patient.name | _name | Yes | Updated via update_details() with validation |
| Patient.dob | _dob | Yes | Validated as a date object |
| Patient.contact_details | _contact_details | Yes | Validated; updated via update_details() |
| Practitioner.practitioner_id | _practitioner_id (read-only property) | Yes | Immutable identifier |
| Practitioner.specialty | _specialty | Yes | Validated; updated via update_details() |
| Practitioner.availability | _availability | Yes | List[str] validated |
| Appointment.appointment_id | _appointment_id | Yes | Immutable identifier |
| Appointment.status | _status (enum) | Yes | Protected; updated only through update_status() |
| Appointment.cancel() | cancel() | Yes | Enforces legal transitions; no SQL or external services |

---

## 2. Domain Invariants

| Class | Invariant / rule | How protected |
|-------|-------------------|---------------|
| Patient | patient_id must never change | No setter; stored as private attribute |
| Patient | name must be non-empty | Validated in constructor and update_details() |
| Practitioner | practitioner_id immutable | No setter; private attribute |
| Practitioner | specialty must be valid | Validated in constructor and update_details() |
| Appointment | status must follow legal transitions | update_status() enforces allowed transitions; no public mutation |
| Appointment | cancelled appointments remain objects | cancel() sets status but does not delete object |

---

## 3. Composition / Inheritance Decisions

| Relationship | Decision | Rationale |
|--------------|----------|-----------|
| Appointment ↔ Patient | Composition/association | Appointment *has a* patient; not a subtype |
| Appointment ↔ Practitioner | Composition/association | Appointment *has a* practitioner; not a subtype |
| Patient ↔ Practitioner | No relationship | They are independent domain entities |
| Appointment ↔ AppointmentStatus | Composition | Status is an attribute represented by an enum |
| Appointment ↔ ClinicSystem (optional) | Composition | ClinicSystem coordinates objects but does not own them |

---

## 4. AI Pair-Programming Record

| AI contribution | Conforms? | Decision | Reason | Verification |
|-----------------|-----------|----------|--------|-------------|
| Added AppointmentStatus enum | Yes | Accepted | Required for domain safety | Enum used in status property |
| Added SQL inside cancel() | No | Removed | Domain objects must not handle persistence | No SQL remains in final code |
| Added NotificationManager | No | Rejected | Out of scope for v0.2/v0.3 | Final code has no external dependencies |
| Made status public | No | Refactored | Must protect invariants | Status now private with controlled update |
| Added inheritance from PatientRecord | No | Rejected | Violates UML; incorrect relationship | Final class uses composition only |

---

## 5. Updated UML

No changes required.

The implementation matched the approved UML.  
All deviations proposed by AI (extra fields, inheritance, external dependencies) were rejected because they violated:

- SmartCare v0.2 scope  
- Stage 4 domain-layer constraints  
- UML attribute and behaviour definitions  
- Encapsulation and invariants  

Therefore, the UML remains unchanged.