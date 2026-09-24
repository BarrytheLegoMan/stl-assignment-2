from enum import Enum

class AppointmentStatus(Enum):
    BOOKED = "BOOKED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"