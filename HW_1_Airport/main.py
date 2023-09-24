from AirportsMap import AirportsMap
from time import sleep



def main():
    airports =AirportsMap()
    airports.SEA.receive_passengers()
    airports.ANC.receive_passengers()

    for i in range(3):
        airports.SEA.send_passenger(airports.ANC, "Hello " + str(i))
        airports.ANC.send_passenger(airports.SEA, "Hello " + str(i))
        sleep(0.5)

    del airports
    


if __name__ == "__main__":
    main()