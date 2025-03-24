INSERT INTO Integrated_Arrival

SELECT a.Airline,
a2.FlightNumber,
a2.ScheduledArrivalDate,
NULL AS ActualArrivalDate,
a2.ScheduledArrivalTime,
a2.ActualArrivalTime,
a.GateTime,
a.LandingTime,
a.Terminal || a.Gate AS ArrivalGate

FROM Airline2_Flight AS a2
JOIN Airport3_Arrivals AS a ON a2.FlightNumber = a.FlightNumber;


