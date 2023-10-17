import socket 
import datetime
import threading
import os
import json

class Airport:

    
    def __init__(self, location:str, IATA:str, port:int, IS_HUB:bool) -> None:
        self.location = location
        self.IATA = IATA
        self.port = port
        self.IS_HUB = IS_HUB

        self.connected_airports = []
        self.server_socket = None
        
        # Create logs folder 
        if not os.path.exists("logs"):
            os.makedirs("logs")
        
        self.log_file = "logs/" + self.IATA + "_log.txt"

        # Clear log file if it exists
        with open(self.log_file, 'w') as f:
            f.write("")


    def __del__(self):
        # Close server when class is destroyed
        if (self.server_socket):
            self.server_socket.close()

    def to_dict(self):
        return {
        "location" : self.location,
        "IATA" : self.IATA,
        "port" : self.port,
        "IS_HUB" :self.IS_HUB,
        }


    def receive_passengers(self) -> None:
        """
        Starts TCP server on new thread for this airport.
        """

        self.server_socket = socket.socket(socket.AF_INET,  # IPV4
                                socket.SOCK_STREAM)  # Connection-less service (UDP) for datagrams

        server_address = ('localhost', self.port)
        self.server_socket.bind(server_address)
        self.server_socket.listen(len(self.connected_airports))  # Clients = connected airports


        def listen(self):
            # TODO: Figure out how to stop thread and close socket affectively
            while True:
                client_socket, client_address = self.server_socket.accept()
                data = client_socket.recv(1024)
                if data:
                    self.log_passenger(data.decode(), RECEIVED=True)
                    self.process_passenger(data.decode())
                    client_socket.close()
                    

        # Thread is daemon to exit when the program exits
        server_thread = threading.Thread(target=listen, args=[self], daemon=True)
        server_thread.start()



    def process_passenger(self, message:json) -> None:
        '''
        Logs the passenger and determines if this is the passengers final destination of the 
        passenger. If not, sends it to its next destination.
        :message JSON string with the passenger message.
        '''
        message_dict = json.loads(message)

        # Find index of current location
        curr_location_idx = 0
        for i, airport in enumerate(message_dict["flight_path"]):
            if airport["IATA"] == self.IATA:
                curr_location_idx = i
                break

        # Destination
        if curr_location_idx == len (message_dict["flight_path"]) - 1:
            self.log_passenger(message, FINAL_DESTINATION=True)
            return
        
        # Send to next airport
        self.send_passenger(message_dict["flight_path"][i+1]["port"], message)
        


    def send_passenger(self, destination:"Airport.port", message) -> None:
        """
        Acts as a client to send a passenger to their destination (TCP message).
        :param destination
        """
        self.log_passenger(message, SENDING=True)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', destination)
        client_socket.connect(server_address)

        client_socket.sendall(message.encode())



    def log_passenger(self, message:json, RECEIVED:bool = False, SENDING:bool = False, FINAL_DESTINATION = False):
        """
        Logs passenger details.
        :param message  JSON string message for the passenger.
        :param RECEIVED Logs message for when passenger is received by the airport.
        :param SENDING Logs message for when passenger is sent by the airport.
        :param SENDING Logs message for when passenger has arrived at final destination.
        """


        message_dict = json.loads(message)

        # Find index of current location
        curr_idx = 0
        for i, airport in enumerate(message_dict["flight_path"]):
            if airport["IATA"] == self.IATA:
                curr_idx = i
                break
        
        log_str = ""
        if RECEIVED:
            log_str = f"FROM {message_dict['flight_path'][curr_idx]['IATA']} RECEIVED"
        elif SENDING:
            log_str = f"TO {message_dict['flight_path'][curr_idx + 1]['IATA']} SENDING"
        elif FINAL_DESTINATION:
            log_str = f"FINAL DESTINATION OF"

        timestamp =  str(datetime.datetime.now())

        flight_path_str = '->'.join([x["IATA"] for x in message_dict["flight_path"]])
        log_str = f"{timestamp} | {log_str} Passenger: {message_dict['passenger']}, Flight {message_dict['flight']} | {flight_path_str}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_str)
        pass