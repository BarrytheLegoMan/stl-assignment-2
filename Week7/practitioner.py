class Practitioner:
    """
    SmartCare Practitioner domain object.
    Stores practitioner identity
    """

    def __init__(self, practitioner_id: str, name: str, specialty: str, availability: list[str]):
        self.__validate_id(practitioner_id)
        self.__validate_name(name)
        self.__validate_specialty(specialty)
        self.__validate_availability(availability)

        self.__practitioner_id = practitioner_id
        self.__name = name
        self.__specialty = specialty
        self.__availability = availability

# validation

    def __validate_id(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Practitioner ID must be entered.")

    def __validate_name(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Practitioner name must be entered.")

    def __validate_specialty(self, value: str) -> None:
        if not value or not isinstance(value, str):
            print("Specialty must be entered.")

    def __validate_availability(self, value: list[str]) -> None:
        if not isinstance(value, list):
            print("Availability must be a list.")
        if not all(isinstance(slot, str) for slot in value):
            print("Each availability entry must be entered.")

# Public operations

    @property
    def practitioner_id(self) -> str:
        return self.__practitioner_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def specialty(self) -> str:
        return self.__specialty

    @property
    def availability(self) -> list[str]:
        return self.__availability


    def update_details(self, name: str, specialty: str) -> None:
        """Safely update practitioner details."""
        self.__validate_name(name)
        self.__validate_specialty(specialty)

        self.__name = name
        self.__specialty = specialty

    def view_schedule(self) -> list[str]:
        """Return availability schedule."""
        return self.__availability.copy()

if __name__ == "__main__":
    main()

# testing calling the calse
# warrior = Practitioner("Warrior", "Doug", "ears",["Mon","Tues","Wed"])
#
# print(warrior.view_schedule())
#
# print(f"The Patient ID is {warrior.availability}, warrior")