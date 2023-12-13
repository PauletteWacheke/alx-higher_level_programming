-- displays the average temperature (Fahrenheit) by city ordered by
-- temperature (descending).
SELECT city.name, ROUND(AVG(city_temp.fahrenheight),2) AS avg_temp
FROM city
join city_temp ON city_id = city_temp.city_id
GROUP BY city.id
ORDER BY avg_temp DESC;
