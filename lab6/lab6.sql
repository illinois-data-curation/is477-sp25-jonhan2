INSERT INTO Lab6_Flights
SELECT 'A1' as Airline, s.FlightNumber, s.DepartureAirport,
    f.DepartureDate, f.DepartureTime
    s.ArrivalAirport, f.ArrivalDate,
    f.ArriveTime
FROM Airline1_Schedule as s 
JOIN Airline1_Flight as f 
    ON s.FlightId = f.FlightId ;

INSERT INTO Lab6_Flights
SELECT 'A2' as Airline, f.FlightNumber,
    f.DepartureAirport, f.ScheduleDepartureDate AS DepartureDate, f.ActualDepartureTime AS DepartureTime,
    f.ArrivalAirport, f.ScheduledArrivalDate AS ArrivalDate, f.ActualArrivalTime AS ActualArrivalTime
FROM Airline2_Flight as f ;
