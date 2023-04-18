-- script that prepares a MySQL server
-- the AirBNB SQL Project.

-- CREATE A DATABASE.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- CREATE A NEW USER.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- GRANT ALL PRIVILEGES.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- GRANT ALL PRIVILEGES ON PERFORMANCE_SCHEMA
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
