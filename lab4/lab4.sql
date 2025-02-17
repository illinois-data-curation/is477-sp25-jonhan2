SELECT airlines.name AS carrier_name,
    AVG(flights.dep_delay) AS avg_departure_delay
FROM flights
JOIN airlines ON flights.carrier = airlines.carrier
GROUP BY airlines.name
ORDER BY avg_departure_delay ASC;