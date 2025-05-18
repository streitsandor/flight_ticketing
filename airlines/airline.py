from flights.flight import Flight
from bookings.ticket_booking import TicketBooking

from datetime import datetime


class Airline:
    """Légitársaság osztály."""

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._flights: list[Flight] = []
        self._bookings: list[TicketBooking] = []

    def add_flight(self, flight: Flight) -> None:
        """Járat hozzáadása."""
        self._flights.append(flight)

    def book_ticket(self, flight_id: int, passenger_name: str, date: str) -> None | int:
        """Foglalás leadása."""
        for flight in self._flights:
            if flight.flight_id == flight_id:
                try:
                    date_obj = datetime.strptime(date, "%Y-%m-%d")
                    if date_obj < datetime.now():
                        print("Hibás dátum: A foglalás dátuma nem lehet múltbeli.")
                        return None
                    new_booking = TicketBooking(flight, passenger_name, date_obj)
                    self._bookings.append(new_booking)
                    print("Foglalás sikeres.")
                    return flight.ticket_price
                except ValueError:
                    print("Hibás dátumformátum. Használja az ÉÉÉÉ-HH-NN formátumot.")
                    return None
        print("Nincs ilyen járatszám.")
        return None

    def remove_ticket(self, passenger_name: str, flight_id: int) -> bool:
        """Foglalás törlése."""
        for booked_ticket in self._bookings:
            if booked_ticket.passenger_name == passenger_name and booked_ticket.flight.flight_id == flight_id:
                self._bookings.remove(booked_ticket)
                print("Foglalás sikeresen lemondva.")
                return True
        print("Nincs ilyen foglalás.")
        return False

    def show_booked_tickets(self) -> None:
        """Foglalások kiíratása."""
        if not self._bookings:
            print("Nincsenek foglalások.")
        for f in self._bookings:
            print(f)

    def show_available_flight(self) -> None:
        """Elérhető járatok kiíratása."""
        for flight in self._flights:
            print(f"Járat: {flight.flight_id} -> {flight.destination}, Ár: {flight.ticket_price} Ft")
