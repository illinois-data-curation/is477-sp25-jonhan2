SELECT X.FlightNumber, X.ArrivalAirport, Y.ArrivalGate
FROM Airline1_Schedule as X
JOIN Airline1_Flight AS Y ON X.FlightId = Y.FlightId;