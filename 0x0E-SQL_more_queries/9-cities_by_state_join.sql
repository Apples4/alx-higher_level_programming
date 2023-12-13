-- script that lists all cities contained in the database 
SELECT 
	cities.name,
	cities.id,
	states.names
FROM 
	cities
INNER JOIN 
	states 
ON 
	cities.states = states.id
ORDER BY cities.id ASC;
