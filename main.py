from dataclasses import asdict
from datetime import datetime, timedelta

from src.domian.builders import UserBuilder
from src.domian.factories import TicketFactory
from src.domian.models.booking import Booking
from src.domian.models.event import Event
from src.domian.services import BookingService
from src.infrastructure.repositories.json_repository import JSONRepository


def booking_to_dict(booking: Booking) -> dict:
    result = asdict(booking)
    result["created_at"] = booking.created_at.isoformat()
    result["event"]["event_date"] = booking.event.event_date.isoformat()
    return result


def run_demo() -> None:
    user = (
        UserBuilder()
        .set_name("Ivan", "Petrov")
        .set_passport("4510 123456")
        .set_address("Moscow")
        .build()
    )
    event = Event(
        id="event-001",
        title="Python Conference",
        event_date=datetime.now() + timedelta(days=7),
        location="Moscow Expo",
        capacity=100,
        free_seats=100,
    )
    ticket = TicketFactory.create_ticket("VIP")

    service = BookingService()
    booking = service.create_booking(user=user, event=event, ticket=ticket)

    repo = JSONRepository("data/bookings.json")
    repo.save(booking.id, booking_to_dict(booking))

    print("=== Demo: Ticket Booking ===")
    print(f"User: {booking.user.first_name} {booking.user.last_name}")
    print(f"Event: {booking.event.title} ({booking.event.location})")
    print(f"Ticket: {booking.ticket.ticket_type.value} | price={booking.ticket.price}")
    print(f"Booking id: {booking.id}")
    print(f"Free seats left: {booking.event.free_seats}")
    print(f"Saved bookings in repository: {len(repo.load_all())}")


if __name__ == "__main__":
    run_demo()
