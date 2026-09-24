from datetime import date


class Patient:
    """
    SmartCare Patient domain object.
    Enforces basic validation.
    """

    def __init__(self, patient_id: str, name: str, dob: date, contact_details: str):
        self.validate_id(patient_id)
        self.validate_name(name)
        self.validate_dob(dob)
        self.validate_contact(contact_details)

        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.contact_details = contact_details

    # Protected validation

    def validate_id(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Patient ID must be entered.")

    def validate_name(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Patient name must be entered.")

    def validate_dob(self, value: date) -> None:
        if not isinstance(value, date):
            print("Date of birth must be a valid date.")

    def validate_contact(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Contact details must be entered.")

    # Public operations

    def update_details(self, name: str, contact_details: str) -> None:
        """Safely update patient details with validation."""
        self.validate_name(name)
        self.validate_contact(contact_details)
        self.name = name
        self.contact_details = contact_details

    def view_history(self):
        """
        Placeholder for Stage 4.
        Actual history retrieval occurs in Stage 5+.
        """
        # return self.history.copy() -- Maybe
        print("Appointment history is implemented in later stages.")

# warrior = Patient("Warrior", "Doug", date(1986,10,6),"number")
#
# print(f"The Patient ID is {warrior.dob}, warrior")
