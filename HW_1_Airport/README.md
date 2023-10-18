# Usage 
For this program, you need a minimum of Python 3.11.2.
To run this program, run `python main.py` in the terminal. Everything (flights, messages, airports, etc) is automatically generated.

This program contains an `Airport` class that contains:
* airport data (i.e port, IATA, location, connected airports,etc.),
* a function to receive passengers (which is running on it's own thread), 
* a function to process passengers (which determines if this is the final destination of the passenger or not based on the message),
* a function to send passengers to the next airport,
* and a function for logging the passenger.

This program also contains an `AirportMap` class that contains:
* 5 initialized airports (ANC, BRW, FAI, OTZ, SEA) that contain their corresponding information,
* a function for selecting a random airport,
* a function for generating a path between 2 airports, through the layover network using depth-first-search.
* and a function for creating a flight between 2 random destination, with a random number of passengers (either 100, 200...900). Each passenger has their own message that contains the flight number, passenger number, and flight path.

### When main is run...
the program first generates 20 random flights (with random layovers) with 100 passengers each that are printed to the command line. These passengers (i.e. messages) are sent to each initial airport. Then each airport sends each passenger (i.e, message) to the next airport. **Each airport has a log file in the `log` folder that logs each passengers arrival and exit, and if the airport is their final destination.**

The log files currently in this repo are from the following run:
```
Generating 20 flights...

Flight 0: OTZ->ANC->BRW | 400 Passengers
Flight 1: OTZ->ANC->FAI | 500 Passengers
Flight 2: SEA->FAI->ANC->OTZ | 200 Passengers
Flight 3: ANC->BRW | 600 Passengers
Flight 4: OTZ->ANC | 200 Passengers
Flight 5: OTZ->ANC | 300 Passengers
Flight 6: BRW->ANC->FAI | 700 Passengers
Flight 7: OTZ->ANC->BRW | 700 Passengers
Flight 8: BRW->ANC->OTZ | 300 Passengers
Flight 9: OTZ->ANC->BRW | 800 Passengers
Flight 10: FAI->ANC->OTZ | 100 Passengers
Flight 11: FAI->ANC->OTZ | 300 Passengers
Flight 12: ANC->OTZ | 600 Passengers
Flight 13: SEA->FAI | 200 Passengers
Flight 14: ANC->BRW | 500 Passengers
Flight 15: ANC->FAI->SEA | 800 Passengers
Flight 16: FAI->ANC->SEA | 200 Passengers
Flight 17: FAI->ANC | 500 Passengers
Flight 18: ANC->FAI->SEA | 300 Passengers
Flight 19: BRW->ANC->FAI->SEA | 600 Passengers
```

# Scalability
This program can be scaled easily by just initializing more airports in `AirportsMap`. All the other logic will work the same. You can also easily create more random flights by adjusting the `NUMBER_FLIGHTS` variable in main and control the number of passengers per flight by passing an integer to `airports.generate_flight()`


# Comparison to Internet Traffic
In this simulation, each airport can be compared to a router, which is sending internet traffic (i.e) passengers to it's final destination. Additionally, airport topology is like internet hub-and-spoke topology where the major/international airports are hubs (i.e. Internet Exchange Points) and the regional airports ara the spokes (i.e. the smaller local networks). Additionally, mapping the airport IATA to the PORT is like mapping an internet IP to a domain name in DNS.

However, at some points my simulation breaks down when compared to the current internet. For example, right now before the program sends a message/passenger, I pre-generate a flight path. While this is how an airline does it, this is not how the internet does it. Instead a message has a final destination and routers determine how best to get it there.

Through this exercise, I have gotten to experience what it's like to build a network and have been able to see some of the challenges that networks face. It was interesting to see that an airport has to be a server and client simultaneously.


# Citations
* I talked to Jaren Ramirez about this homework. He borrowed my multi-threading idea and I liked his idea about representing this physically in tkinter or other GUI. However, I did not end up creating a GUI for this assignment.
* I used ChatGPT to debug my path finding and also to serialize the airport classes (i.e. turn them into a dictionary) so I could pass them as JSON objects.
* I also used the following sources to remember certain python functionality:
    * https://www.digitalocean.com/community/tutorials/python-time-sleep
    * https://www.geeksforgeeks.org/python-random-module/
    * https://www.w3schools.com/python/python_json.asp
    * https://www.geeksforgeeks.org/python-list-comprehension/
    * https://www.pythontutorial.net/python-basics/python-write-text-file/
    * https://www.geeksforgeeks.org/get-current-date-and-time-using-python/
    * https://www.simplilearn.com/tutorials/python-tutoriallist-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.
    * https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json


