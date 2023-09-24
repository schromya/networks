import socket 
from enum import Enum
import threading

class Airport:

    
    def __init__(self, name:str, IATA:str, port:int, IS_HUB:bool) -> None:
        self.name = name
        self.IATA = IATA
        self.port = port
        self.IS_HUB = IS_HUB

        self.connected_airports = []
 


    def __del__(self):
        # Close server when class is destroyed

        # TODO: get this working
        print("here")
        if (self.server_socket):
            print("Closing", self.name, "server")
            self.server_socket.close()


    def receive_passengers(self) -> None:
        """
        Starts TCP server on new thread for this airport.
        """

        self.server_socket = socket.socket(socket.AF_INET,  # IPV4
                                socket.SOCK_STREAM)  # Connection-less service (UDP) for datagrams

        server_address = ('localhost', self.port)
        self.server_socket.bind(server_address)
        self.server_socket.listen(len(self.connected_airports))  # Clients = connected airports
        print("Server is listening on {}:{}".format(*server_address))

        def listen(self):
            # TODO: Figure out how to stop thread and close socket affectively
            while True:
                client_socket, client_address = self.server_socket.accept()
                data = client_socket.recv(1024)
                if data:
                    print(self.name, "received data:", data.decode())
                    self.process_passenger(data.decode())
                    client_socket.close()

        # Thread is daemon to exit when the program exits
        server_thread = threading.Thread(target=listen, args=[self], daemon=True)
        server_thread.start()



    def process_passenger(self, message:str) -> None:
        pass

    def send_passenger(self, destination:"Airport", message) -> None:
        """
        Acts as a client to send a passenger to their destination (TCP message).
        :param destination
        """

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', destination.port)
        client_socket.connect(server_address)

        print(self.name, "sending data to:{}".format(server_address))
        client_socket.sendall(message.encode())

        # data = client_socket.recv(1024)
        # print("Received from server: {}".format(data.decode()))


    def log_passenger(message):
        pass