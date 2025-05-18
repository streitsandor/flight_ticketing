from flights.domestic_flight import DomesticFlight
from flights.foreign_flight import ForeignFlight
from airlines.airline import Airline

from typing import Callable
import os
import sys
import re

regex_dict = {"date": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"}


def clear_console() -> None:
    """Console tisztítása."""
    os.system("cls" if os.name == "nt" else "clear")


def menu() -> str:
    """Fő menü kirajzolása."""
    print("\n--- Jegyfoglaló Rendszer ---")
    print("1. Jegy foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    return input("Válassz egy lehetőséget: ").strip()


def book_ticket() -> None:
    """Foglalás menü kirajzolása, adatok bekérése."""
    show_flights()

    flight_id = int(input("Járatszám: "))
    passenger_name = input("Utas neve: ")
    date = input("Dátum (ÉÉÉÉ-HH-NN): ")

    if re.search(regex_dict["date"], date):
        default_airline.book_ticket(flight_id, passenger_name, date)
    else:
        raise ValueError("Nem megfelelő dátum forma.")


def remove_ticket() -> None:
    """Törlés menü kirajzolása, adatok bekérése."""
    show_bookings()  # TESZT! csak kényelemből hozzáadva

    passenger_name = input("Utas neve: ")
    flight_id = int(input("Járatszám: "))
    default_airline.remove_ticket(passenger_name, flight_id)


def show_flights() -> None:
    """Elérhető járatok kiíratása."""
    clear_console()
    default_airline.show_available_flight()


def show_bookings() -> None:
    """Foglalások kiíratása."""
    clear_console()
    default_airline.show_booked_tickets()


def quit_program() -> None:
    """Programból kilépés."""
    print("Kilépés...")
    sys.exit(0)


if __name__ == "__main__":
    """Program belépési pontja."""

    clear_console()

    # Teszt adatok hozzáadása
    default_airline = Airline("HighFly légitársaság")
    default_airline.add_flight(DomesticFlight(101, "Debrecen"))
    default_airline.add_flight(DomesticFlight(102, "Pécs"))
    default_airline.add_flight(ForeignFlight(201, "London"))

    default_airline.book_ticket(101, "Kovács Anna", "2025-08-01")
    default_airline.book_ticket(102, "Szabó Béla", "2025-08-02")
    default_airline.book_ticket(201, "Tóth Gábor", "2025-09-01")
    default_airline.book_ticket(101, "Farkas Júlia", "2025-08-05")
    default_airline.book_ticket(102, "Kiss István", "2025-08-06")
    default_airline.book_ticket(201, "Nagy Mária", "2025-09-10")
    # Tesz adatok VÉGE

    operations: dict[str, Callable[[], None]] = {
        "1": lambda: book_ticket(),
        "2": lambda: remove_ticket(),
        "3": lambda: show_bookings(),
        "4": lambda: quit_program(),
    }

    while True:
        try:
            choice = menu()
            action = operations.get(choice)
            if action:
                action()
            else:
                print("Érvénytelen választás.")
        except ValueError:
            print("Hiba! Nem megfelelő adatbevitel!")
        except Exception as e:
            print("Hiba: %s" % e, file=sys.stderr)
