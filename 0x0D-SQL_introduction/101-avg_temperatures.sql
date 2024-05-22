-- Import in hbtn_0c_0 database this table dump
-- a script that displays the average temperature
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
