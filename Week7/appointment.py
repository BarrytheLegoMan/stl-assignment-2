from appointment_status import AppointmentStatus
from appointment_exceptions import AppointmentDomainException


class Appointment:
    """
    Appointment entity based on approved UML.

    Attributes:
        appointment_id
        patient_id
        practitioner_id
        date_time
        status
    """

    def __init__(
        self,
        appointment_id,
        patient_id,
        practitioner_id,
        date_time,
        status=AppointmentStatus.BOOKED,
    ):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.practitioner_id = practitioner_id
        self.date_time = date_time
        self.status = status

    def book(self, valid_patient_ids, valid_practitioner_ids):
        """
        Ensures the appointment references an existing
        patient and practitioner.
        """

        if self.patient_id not in valid_patient_ids:
            raise AppointmentDomainException(
                "Appointment must reference an existing patient."
            )

        if self.practitioner_id not in valid_practitioner_ids:
            raise AppointmentDomainException(
                "Appointment must reference an existing practitioner."
            )

        self.status = AppointmentStatus.BOOKED

    def cancel(self):
        """
        Cancels an appointment.
        Uses the legal status transition rule.
        """
        self.update_status(AppointmentStatus.CANCELLED)

    def update_status(self, new_status):
        """
        Updates appointment status while enforcing
        legal status transitions.
        """

        allowed_transitions = {
            AppointmentStatus.BOOKED: {
                AppointmentStatus.COMPLETED,
                AppointmentStatus.CANCELLED,
            },
            AppointmentStatus.COMPLETED: set(),
            AppointmentStatus.CANCELLED: set(),
        }

        if new_status == self.status:
            return

        if new_status not in allowed_transitions[self.status]:
            raise AppointmentDomainException(
                f"Illegal status transition: "
                f"{self.status.name} -> {new_status.name}"
            )

        self.status = new_status

    def detect_duplicate(self, other_appointment):
        """
        Duplicate rule:
        patient_id + practitioner_id + date_time
        must all match.
        """

        return (
            self.patient_id == other_appointment.patient_id
            and self.practitioner_id == other_appointment.practitioner_id
            and self.date_time == other_appointment.date_time
        )