from dataclasses import dataclass
from enum import Enum


class TicketType(str, Enum):
    STANDARD = "Standard"
    VIP = "VIP"
    EARLY_BIRD = "EarlyBird"


class TicketStatus(str, Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    CANCELLED = "cancelled"


@dataclass(slots=True)
class Ticket:
    ticket_type: TicketType
    price: float
    status: TicketStatus = TicketStatus.AVAILABLE

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Ticket price cannot be negative.")