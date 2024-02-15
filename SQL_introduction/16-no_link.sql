-- display all records that have names in order of descending scores
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;