SELECT X.Airline, X.FlightNumber, NULL AS ArrivalAirport, X.Terminal || X.Gate AS ArrivalGate
FROM Airport3_Arrivals AS X;