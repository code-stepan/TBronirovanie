from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

from src.domain.models.event import Event
from src.domain.models.ticket import Ticket
from src.domain.models.user import User


class BookingStatus(str, Enum):
    CREATED = "created"
    CANCELLED = "cancelled"


@dataclass(slots=True)
class Booking:
    id: str
    user: User
    event: Event
    ticket: Ticket
    status: BookingStatus = BookingStatus.CREATED
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("Booking id is required.")