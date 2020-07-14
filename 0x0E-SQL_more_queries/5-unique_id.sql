-- creates the table unique_id on your MySQL server
-- creates the table unique_id on your MySQL server with unique default to 0 and unique
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
