.mode csv
.headers on
.output results/sql-fac-types.csv

SELECT "Facility Type" AS Facility_Type, COUNT(*) AS Count
FROM Inspections
GROUP BY "Facility Type"
ORDER BY "Facility Type" ASC;
