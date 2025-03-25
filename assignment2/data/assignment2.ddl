CREATE TABLE Airline1_Schedule (
    FlightId NUMBER,
    FlightNumber NUMBER,
    StartDate TEXT,
    EndDate TEXT,
    DepartureTime TEXT,
    Departure Airport TEXT,
    ArrivalTime TEXT,
    ArrivalAirport TEXT,
    PRIMARY KEY (FlightId)
);
CREATE TABLE Airline1_Flight (
    FlightId NUMBER,
    DepartureDate TEXT,
    DepartureTime TEXT,
    DepartureGate TEXT,
    ArrivalDate TEXT,
    ArrivalTime TEXT,
    ArrivalGate TEXT,
    PlaneId NUMBER,
    PRIMARY KEY (FlightId, DepartureDate)
    FOREIGN KEY (FlightId) REFERENCES Airline1_Schedule(FlightId)
);
CREATE TABLE Airline2_Flight (
    FlightNumber NUMBER,
    DepartureAirport TEXT,
    ScheduledDepartureDate TEXT,
    ScheduledDepartureTime TEXT, 
    ActualDepartureTime TEXT,
    ArrivalAirport TEXT,
    ScheduledArrivalDate TEXT,
    ScheduledArrivalTime TEXT,
    ActualArrivalTime TEXT,
    PRIMARY KEY (ScheduledDepartureDate, FlightNumber, DepartureAirport)
);
CREATE TABLE Airport3_Arrivals (
    Airline TEXT,
    FlightNumber NUMBER,
    Scheduled TEXT,
    Actual TEXT,
    GateTime TEXT,
    LandingTime TEXT,
    Terminal TEXT,
    Gate TEXT,
    Runway TEXT,
    PRIMARY KEY (Scheduled, Airline, FlightNumber)
);
CREATE TABLE Airport3_Departures (
    Airline TEXT,
    FlightNumber NUMBER,
    Scheduled TEXT,
    Actual TEXT,
    GateTime TEXT,
    TakeoffTime TEXT,
    Terminal TEXT,
    Gate NUMBER,
    Runway TEXT,
    PRIMARY KEY (Airline, FlightNumber, Scheduled)
);
