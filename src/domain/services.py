from uuid import uuid4

from src.domain.exceptions.user_unverified_error import UserUnverifiedError
from src.domain.models.booking import Booking, BookingStatus
from src.domain.models.event import Event
from src.domain.models.ticket import Ticket, TicketStatus
from src.domain.models.user import User


class BookingService:
    def create_booking(self, user: User, event: Event, ticket: Ticket) -> Booking:
        if not user.is_verified:
            raise UserUnverifiedError("Cannot create booking: user is not verified.")
        if ticket.status != TicketStatus.AVAILABLE:
            raise ValueError("Cannot create booking: ticket is not available.")

        event.reserve_seat()
        ticket.status = TicketStatus.BOOKED

        return Booking(
            id=str(uuid4()),
            user=user,
            event=event,
            ticket=ticket,
            status=BookingStatus.CREATED,
        )

    def cancel_booking(self, booking: Booking) -> Booking:
        if booking.status == BookingStatus.CANCELLED:
            return booking

        booking.status = BookingStatus.CANCELLED
        booking.ticket.status = TicketStatus.CANCELLED
        booking.event.release_seat()
        return booking

    def check_availability(self, event: Event) -> bool:
        return event.free_seats > 0
    