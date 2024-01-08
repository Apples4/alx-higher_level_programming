-- script that lists all the cities of California 
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id =
states.id AND states.name = 'California'
ORDERED BY cities.id ASC;