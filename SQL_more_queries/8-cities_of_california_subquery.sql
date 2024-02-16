-- retrieve all cities with a foreign key to California using a subquery

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'california')
ORDER BY id ASC;