-- script that displays the top 3 of cities temperature during July and
-- August ordered by temperature (descending)
SELECT city, temperature
FROM weather
WHERE MONTH(date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
