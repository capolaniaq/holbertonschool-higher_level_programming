--  script that displays the average temperature
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state;
