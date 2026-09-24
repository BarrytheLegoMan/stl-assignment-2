class Practitioner:
    """
    SmartCare Practitioner domain object.
    Stores practitioner identity
    """

    def __init__(self, practitioner_id: str, name: str, specialty: str, availability: list[str]):
        self.validate_id(practitioner_id)
        self.validate_name(name)
        self.validate_specialty(specialty)
        self.validate_availability(availability)

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty
        self.availability = availability

# validation

    def validate_id(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Practitioner ID must be entered.")

    def validate_name(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Practitioner name must be entered.")

    def validate_specialty(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Specialty must be entered.")

    def validate_availability(self, value: list[str]) -> None:
        if not isinstance(value, list):
            print("Availability must be a list.")
        if not all(isinstance(slot, str) for slot in value):
            print("Each availability entry must be entered.")

# Public operations

    def update_details(self, name: str, specialty: str) -> None:
        """Safely update practitioner details."""
        self.validate_name(name)
        self.validate_specialty(specialty)

        self.name = name
        self.specialty = specialty

    def view_schedule(self) -> list[str]:
        """Return availability schedule."""
        return self.availability.copy()

# warrior = Practitioner("Warrior", "Doug", "ears",["Mon","Tues","Wed"])
#
# print(warrior.view_schedule())
#
# print(f"The Patient ID is {warrior.availability}, warrior")