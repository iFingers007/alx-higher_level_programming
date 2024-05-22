-- a script that displays the max temperature
-- of each state (ordered by State name).
SOURCE ./table_dump.sql;

-- Select the database
USE hbtn_0c_0;

-- Query to display the max temperature of each state, ordered by state name
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
