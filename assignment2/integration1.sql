INSERT INTO Integrated_Arrival
SELECT
    'A1' AS Airline, 
    S.FlightNumber AS FlightNumber,
    F.ArrivalDate AS ScheduledArrivalDate,
    F.ArrivalDate AS ActualArrivalDate,
    S.ArrivalDate AS ScheduledArrivalTime,
    F.ArrivalTime AS ActualArrivalTime,
    A.GateTime AS GateTime,
    A.LandingTime AS LandingTime,
    F.ArrivalGate AS ArrivalGate
FROM 
    Airline1_Schedule AS S,
    Airport3_Arrivals AS A,
    Airline1_Flight as F 
WHERE 
    S.FlightId=F.FlightId
AND 
    S.FlightNumber=A.FlightNumber
AND 
    'A1'=A.Airline
AND
    S.ArrivalAirports='EWR';