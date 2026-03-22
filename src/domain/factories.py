from src.domain.exceptions.invalid_ticket_type_error import InvalidTicketTypeError
from src.domain.models.ticket import Ticket, TicketType


class TicketFactory:
    _PRICE_BY_TYPE = {
        TicketType.STANDARD: 1000.0,
        TicketType.VIP: 2500.0,
        TicketType.EARLY_BIRD: 700.0,
    }

    @classmethod
    def create_ticket(cls, ticket_type: str | TicketType) -> Ticket:
        if isinstance(ticket_type, str):
            normalized = ticket_type.strip().lower()
            mapping = {
                "standard": TicketType.STANDARD,
                "vip": TicketType.VIP,
                "earlybird": TicketType.EARLY_BIRD,
                "early_bird": TicketType.EARLY_BIRD,
                "early-bird": TicketType.EARLY_BIRD,
            }
            ticket_enum = mapping.get(normalized)
        else:
            ticket_enum = ticket_type

        if ticket_enum is None or ticket_enum not in cls._PRICE_BY_TYPE:
            raise InvalidTicketTypeError(f"Unknown ticket type: {ticket_type}")

        return Ticket(ticket_type=ticket_enum, price=cls._PRICE_BY_TYPE[ticket_enum])