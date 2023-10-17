from Airport import Airport
import random
import json

class AirportsMap:
    """
    May be needed if implement a more complex mapping structure
    """

    def __init__(self) -> None:
        self.SEA = Airport(
            location="Seattle", 
            IATA="SEA", 
            port=8080,
            IS_HUB = True
        )

        self.ANC = Airport(
            location="Anchorage", 
            IATA="ANC", 
            port=8081,
            IS_HUB = True
        )

        self.OTZ = Airport(
            location="Kotzebue", 
            IATA="OTZ", 
            port=8082,
            IS_HUB = False
        )

        self.BRW = Airport(
            location="Utqiagvik", 
            IATA="BRW", 
            port=8083,
            IS_HUB = False
        )

        self.FAI = Airport(
            location="Fairbanks", 
            IATA="FAI", 
            port=8084,
            IS_HUB = False
        )

        self.SEA.connected_airports = [self.FAI, self.ANC,]
        self.ANC.connected_airports = [ self.OTZ, self.BRW, self.FAI, self.SEA]
        self.OTZ.connected_airports = [self.ANC]
        self.BRW.connected_airports = [self.ANC]
        self.FAI.connected_airports = [self.ANC, self.SEA]

        self.airports = [self.SEA, self.ANC, self.OTZ, self.BRW, self.FAI]

        self.flight_number = 0
        

    def generate_flight_path(self, source:Airport = None, destination:Airport = None) -> list[Airport]:
        """
        This is not guaranteed to generate the shortest path between airports, but it will generate
        a correct path.
        :source    (optional) Airport to leave out of. If no airport passed, chooses a random one.
        :destination (optional) Airport to arrive at. If no airport passed, chooses a random one.
        :return    A list of airports that create the flight path from the source to destination.
        """

        if (not source):
            source = self.get_random_airport()
        if (not destination):
            destination = self.get_random_airport(excluded_airport=source)

        
        def traverse_path(curr_airport:Airport, prev_airports:list[Airport]):
            prev_airports = prev_airports + [curr_airport] # Creates a copy of the list
            if curr_airport == destination:
                return prev_airports
            for next_airport in curr_airport.connected_airports:
                if next_airport not in prev_airports:
                    path = traverse_path(next_airport, prev_airports)
                    if path:
                        return path
            return None

        flight_path = traverse_path(source, [])

        return flight_path


    def get_random_airport(self, excluded_airport:Airport = None) -> Airport:
        """
        :excluded_airport   (optional) Airport to exclude from choosing.
        :return    A random airport (can be used as a source or destination.)
        """
        airport_choices = self.airports.copy()
        if (excluded_airport):
            airport_choices.remove(excluded_airport)

        return random.choice(airport_choices)


    def generate_flight(self, number_passengers:int = None) -> (Airport, json):
        """
        Creates a message for each passenger on the flight.
        :number_passengers  (optional) If the number isn't passed, produces a random  number
                                            of either 100, 200, ..., 800
        :return    The source airport and a List of JSON string that represents each passenger.
        """
        passenger_number = 0
        # Generates between 100 and 800 passengers
        if (not number_passengers):
            number_passengers = random.randint(1, 8) * 100
        

        flight_path = self.generate_flight_path()
        serialized_flight_path = [x.to_dict() for x in  flight_path]
        passenger_messages = []

        for _ in range (number_passengers):
            message = {
                "flight": self.flight_number,
                "passenger": passenger_number,
                "flight_path": serialized_flight_path
            }
            passenger_messages.append(json.dumps(message))

            passenger_number += 1


        flight_path_str = '->'.join([x.IATA for x in flight_path])
        print(f"Flight {self.flight_number}: {flight_path_str}")

        self.flight_number += 1
        

        return flight_path[0], passenger_messages


