from AirportsMap import AirportsMap
import time



def main():
    airports = AirportsMap()

    # Get Airports ready to receive passengers (receive passengers)
    for airport in airports.airports:
        airport.receive_passengers()

    # Generate 20 flights with 100 passengers each
    NUMBER_FLIGHTS = 20
    NUMBER_PASSENGERS = 100

    print(f"Generating {NUMBER_FLIGHTS} flights...\n")
    for _ in range(NUMBER_FLIGHTS):
        time.sleep(0.5)
        source, passenger_messages = airports.generate_flight() 

        # Send each passenger from the source airport
        for message in passenger_messages:
            source.process_passenger(message)
        


if __name__ == "__main__":
    main()