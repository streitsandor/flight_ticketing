from abc import ABC, abstractmethod


class Flight(ABC):
    """Járat (absztrakt) osztály."""

    def __init__(self, flight_id: int, destination: str, ticket_price: int) -> None:
        self._flight_id = flight_id
        self._destination = destination
        self._ticket_price = ticket_price

    @property
    def flight_id(self) -> int:
        return self._flight_id

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def ticket_price(self) -> int:
        return self._ticket_price

    @abstractmethod
    def flight_info(self) -> None:
        pass
