-- create a database
-- create a table with the primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	PRIMARY KEY(id),

	FOREING KEY (state_id)
	   REFERENCES states(id)

);
