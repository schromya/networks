from Airport import Airport


class AirportsMap:
    """
    May be needed if implement a more complex mapping structure
    """

    def __init__(self) -> None:
        self.SEA = Airport(
            name="Seattle", 
            IATA="SEA", 
            port=8080,
            IS_HUB = True
        )

        self.ANC = Airport(
            name="Anchorage", 
            IATA="ANC", 
            port=8081,
            IS_HUB = True
        )

        self.SEA.connected_airports = [self.ANC]
        self.ANC.connected_airports = [self.SEA]


    def __del__(self):
        print("Deleting")
        del self.SEA
        del self.ANC

    pass
