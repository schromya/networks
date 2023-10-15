import json
import random
from AirportsMap import AirportsMap
from Airport import Airport

class Messages:
    def __init__(self) -> None:
        self.passenger_number = 0
        self.flight_number = 0
        self.airports = AirportsMap()


    def generate_flight(self, passengers_per_flight:int = None) -> (Airport, json):
        """
        Creates a message for each passenger on the flight.
        :passengers_per_flight  (optional) If the number isn't passed, produces a random  number
                                            of either 100, 200, ..., 800
        :return    The source airport and a List of JSON string that represents each passenger.
        """

        # Generates between 100 and 800 passengers
        if (not passengers_per_flight):
            passengers_per_flight = random.randint(1, 8) * 100
        

        flight_path = self.airports.generate_flight_path()
        port_flight_path = [(x.port, x.IATA) for x in  flight_path]
        print(port_flight_path)
        messages = []

        for _ in range (passengers_per_flight):
            message = {
                "flight": self.flight_number,
                "passenger": self.passenger_number,
                "flight_path": port_flight_path
            }
            messages.append(json.dumps(message))

            self.passenger_number += 1

        self.flight_number += 1

        return flight_path[0], messages




