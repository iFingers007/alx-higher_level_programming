-- A script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
-- Import the table dump
SOURCE ./table_dump.sql;

-- Select the database
USE hbtn_0c_0;

-- Query to display the top 3 cities by average temperature during July and August
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
