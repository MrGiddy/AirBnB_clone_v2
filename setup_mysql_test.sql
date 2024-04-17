-- Prepares MYSQL Server db for testing
-- Database: hbnb_test_db
-- User: hbnb_test
-- User Password: hbnb_test_pwd
-- Host: localhost
-- Grants all privileges for this user on the Database
-- Also grants SELECT to the user on performance_schema db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT on performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
