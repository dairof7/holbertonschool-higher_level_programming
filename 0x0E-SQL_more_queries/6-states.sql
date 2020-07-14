-- creates the database hbtn_0d_usa and the table states
-- creates the database hbtn_0d_usa and the table states with id (unique, not null, primary key) and name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
