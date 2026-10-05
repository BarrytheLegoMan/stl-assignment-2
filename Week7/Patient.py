from datetime import date


class Patient:
    """
    SmartCare Patient domain object.
    Enforces basic validation.
    """

    #constructor

    def __init__(self, patient_id: str, name: str, dob: date, contact_details: str):
        self.__validate_id(patient_id)
        self.__validate_name(name)
        self.__validate_dob(dob)
        self.__validate_contact(contact_details)

        self.__patient_id = patient_id
        self.__name = name
        self.__dob = dob
        self.__contact_details = contact_details

    # Protected validation

    def __validate_id(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Patient ID must be entered.")

    def __validate_name(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Patient name must be entered.")

    def __validate_dob(self, value: date) -> None:
        if not value or not isinstance(value, date):
            print("Date of birth must be a valid date.")

    def __validate_contact(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Contact details must be entered.")

    # Public operations

    @property
    def patient_id(self) -> str:
        return self.__patient_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def dob(self) -> date:
        return self.__dob

    @property
    def contact_details(self) -> str:
        return self.__contact_details

    def update_details(self, name: str, contact_details: str) -> None:
        """Safely update patient details with validation."""
        self.__validate_name(name)
        self.__validate_contact(contact_details)
        self.__name = name
        self.__contact_details = contact_details

    def view_history(self):
        """
        Placeholder for Stage 4.
        """
        # return self.history.copy() -- Maybe
        print("Appointment history is implemented in later stages.")

# if __name__ == "__main__":
#     main()


#testing calling the class
# warrior = Patient("Warrior", "Doug", date(1986,10,6),"145")
#
# print(f"The Patient ID is {warrior.dob}, warrior {warrior.patient_id},{warrior.name} please call {warrior.contact_details}")
