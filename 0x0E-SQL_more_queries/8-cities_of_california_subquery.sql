-- lists all the cities of California that can be found in th database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities where state_id = 1 ORDER BY cities.id;
