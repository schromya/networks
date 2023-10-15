from AirportsMap import AirportsMap
from Messages import Messages
import time



def main():


    airports = AirportsMap()
    messages = Messages()



    source, messages = messages.generate_flight(1)

    # print(source.IATA)

    # for message in messages:
    #     print(message)

    for airport in airports.airports:
        airport.receive_passengers()
    


    for message in messages:
        source.process_passenger(message)
        #process_pase(airports.ANC, "Hello " + str(i))
        #airports.ANC.send_passenger(airports.SEA, "Hello " + str(i))
        time.sleep(0.5)

    # del airports
    


if __name__ == "__main__":
    main()