from Airport import Airport
import random

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

        print("~~~~~", source.IATA, destination.IATA)
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



    def __del__(self):
        #print("Deleting")
        del self.SEA
        del self.ANC


