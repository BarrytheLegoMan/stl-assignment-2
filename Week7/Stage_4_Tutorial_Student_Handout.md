# Assignment 2 - Case Study Stage 4 Tutorial Activities Object-Oriented Design Decisions

## Activity 1 – Encapsulation Review

| Class        | Protected state / invariant                                                                                 | Public operations                                     |
|--------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Patient      | patient_id must be unique; name and DOB must be valid                                                       | update_details(), view_history()                      |
| Practitioner | practitioner_id unique; specialty; availability timeslot                                                    | update_details(), view_schedule()                     |
| Appointment  | status must follow transitions rules; must reference valid patient + practitioner; must use valid date_time | book(), cancel(), update_status(), detect_duplicate() |

## Activity 2 – Composition or Inheritance?

### Appointment and Patient  
**Composition/association**  
**Reason:** An appointment *uses* a patient but is not a type of patient.

### Appointment and Practitioner  
**Composition/association**  
**Reason:** An appointment links to a practitioner but does not inherit practitioner behaviour.

### Doctor and Practitioner (hypothetical)  
**Inheritance**  
**Reason:** A doctor *is a* specialised type of practitioner. 

### Clinic and Appointment  
**Composition/association**  
**Reason:** A clinic *contains* appointments but does not inherit from them. The clinic is an organisational container.

---

## Activity 3 – Responsibility Allocation

### Who decides whether SCHEDULED can become CANCELLED?  
The **Appointment** (or enforcing business rules).  
Status transitions are domain rules, not UI rules.

### Who validates a patient name?  
The **Patient** class or a **validation module**.  
Validation belongs in it own module, not the UI.

### Should Appointment execute SQL? Why?  
**No.**  
SQL belongs in the data access layer.  
Domain objects should not know how data is stored — this breaks separation of concerns.

### Should the UI decide whether a status transition is legal?  
**No.**  
The UI should request the change; the domain model decides legality.  
Otherwise business rules become duplicated and inconsistent.

---

## Activity 4 – AI Code Critique

AI generated an Appointment class with:
- public status mutation  
- SQL inside cancel()  
- NotificationManager dependency  
- inheritance from PatientRecord  

### Five design problems and corrections

1. **Public status mutation breaks invariants**  
   - *Problem:* Anyone can set status directly.  
   - *Correction:* Make status private; expose update_status() with validation.

2. **SQL inside cancel() violates separation of concerns**  
   - *Problem:* THe SQL allocates for more than functions ability.  
   - *Correction:* Move SQL to a repository/data access class.

3. **NotificationManager dependency inside Appointment**  
   - *Problem:* Appointment becomes tightly coupled to external services.  
   - *Correction:* Use a higher-level service (e.g., AppointmentService) to trigger notifications.

4. **Inheritance from PatientRecord is incorrect**  
   - *Problem:* Appointment is not a type of patient record.  
   - *Correction:* Remove inheritance; use associations only.

5. **Status transitions not validated**  
   - *Problem:* Illegal transitions (e.g., CANCELLED → SCHEDULED) allowed.  
   - *Correction:* Add a controlled list and enforce transitions inside update_status().

---

## Exit Question

### Why can code be object-oriented syntactically but still have poor object-oriented design?

Because **syntax is not design**.  
A program can use classes, methods, and objects but still violate core Object Oriented principles such as:

- Encapsulation  
- Cohesion  
- Separation of concerns  
- Correct responsibility allocation  
- Avoiding unnecessary coupling  
- Using inheritance only when appropriate  

Object-Oriented design is about **behaviour, responsibility, and relationships**, not just using the `class` keyword.