from flights.flight import Flight


class ForeignFlight(Flight):
    """Külföldi járat osztály."""

    def __init__(self, flight_id: int, destination: str) -> None:
        super().__init__(flight_id, destination, ticket_price=30000)

    def flight_info(self) -> None:
        """Járat adatainak kiíratása."""
        print(f"Nemzetközi Járat - {self.flight_id} -> {self.destination}, Ár: {self.ticket_price} Ft")
