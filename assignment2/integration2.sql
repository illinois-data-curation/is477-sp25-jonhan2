INSERT INTO Integrated_Arrival
SELECT
    'A2' AS Airline, 
    F.FlightNumber AS FlightNumber,
    A.Scheduled AS ScheduledArrivalDate,
    A.Actual AS ActualArrivalDate,
    F.ScheduledArrivalTime AS ScheduledArrivalTime,
    F.ActualArrivalTime AS ActualArrivalTime,
    A.GateTime AS GateTime,
    A.LandingTime AS LandingTime,
    (A.Terminal || A.Gate) AS ArrivalGate
FROM
    Airport3_Arrivals AS A
JOIN
    Airline2_Flight AS F 
ON 
    F.FlightNumber=A.FlightNumber
AND 
    A.Scheduled=F.ScheduledArrivalDate
AND
    'A2'=A.Airline
AND 
    F.ArrivalAirport='EWR';