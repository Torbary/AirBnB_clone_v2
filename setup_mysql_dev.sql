-- script that prepares a MySQL server
-- the AirBNB SQL Project.

-- CREATE A DATABASE.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- CREATE A NEW USER.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- GRANT ALL PRIVILEGES.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- GRANT ALL PRIVILEGES ON PERFORMANCE_SCHEMA
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
