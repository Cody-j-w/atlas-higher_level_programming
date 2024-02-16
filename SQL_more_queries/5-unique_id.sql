-- create table with enforced unique id
CREATE TABLE  IF NOT EXISTS unique_id(id INT, name VARCHAR(256), UNIQUE(id));