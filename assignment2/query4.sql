SELECT X.Airline, X.FlightNumber
FROM Airport3_Arrivals AS X 
WHERE X.Scheduled != x.Actual;
