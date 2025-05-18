from flights.flight import Flight

from datetime import datetime


class TicketBooking:
    """Jegyfoglalás osztály."""

    def __init__(self, flight: Flight, passenger_name: str, date: datetime) -> None:
        self._flight = flight
        self._passenger_name = passenger_name
        self._date = date

    @property
    def flight(self) -> Flight:
        return self._flight

    @property
    def passenger_name(self) -> str:
        return self._passenger_name

    @property
    def date(self) -> datetime:
        return self._date

    def __str__(self) -> str:
        """Foglalás adatainak kiíratása."""
        return f"Foglalás: {self.passenger_name}, {self._flight.flight_id} ({self._flight.destination}), {self._date.strftime('%Y-%m-%d')} - {self._flight.ticket_price} Ft"
