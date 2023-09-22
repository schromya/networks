
class Airport:


    def __init__(self, name:str, IATA_port_mapping:dict, connected_airports: list) -> None:
        self.name = name
        self.IATA_port_mapping = IATA_port_mapping
        self.connected_airports = connected_airports

    def start_server(self) -> None:
        """
        Starts TCP server for this airport.
        """
        
        pass

    def start_client(self) -> None:
        """
        Starts TCP client for this airport.
        """
        pass

    def receive_passenger(self) -> None:
        pass

    def send_passenger(self) -> None:
        pass