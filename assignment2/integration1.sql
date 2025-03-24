INSERT INTO Integrated_Arrival
SELECT a.Airline,
       s.FlightNumber,
       a.Scheduled AS ScheduledArrivalDate,
       f.ArrivalDate AS ActualArrivalDate,
       s.ArrivalTime AS ScheduledArrivalTime,
       f.ArrivalTime AS ActualArrivalTime,
       a.GateTime,
       a.LandingTime,
       f.ArrivalGate
FROM Airline1_Schedule AS s  
JOIN Airline1_Flight AS f ON s.FlightId = f.FlightId
JOIN Airport3_Arrivals AS a ON f.ArrivalGate = CONCAT(a.Terminal, a.Gate);
