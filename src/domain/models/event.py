from dataclasses import dataclass
from datetime import datetime

from src.domain.exceptions.not_enough_seat_error import NotEnoughSeatError


@dataclass(slots=True)
class Event:
    id: str
    title: str
    event_date: datetime
    location: str
    capacity: int
    free_seats: int

    def __post_init__(self) -> None:
        self.id = self.id.strip()
        self.title = self.title.strip()
        self.location = self.location.strip()

        if not self.id or not self.title or not self.location:
            raise ValueError("Event id, title and location are required.")
        if self.capacity < 0:
            raise ValueError("Event capacity cannot be negative.")
        if self.free_seats < 0:
            raise ValueError("Free seats cannot be negative.")
        if self.free_seats > self.capacity:
            raise ValueError("Free seats cannot exceed capacity.")

    def reserve_seat(self) -> None:
        if self.free_seats <= 0:
            raise NotEnoughSeatError(f"No free seats for event '{self.title}'.")
        self.free_seats -= 1

    def release_seat(self) -> None:
        if self.free_seats < self.capacity:
            self.free_seats += 1