-- Prepares a MYSQL Server for the project
-- Database: hbnb_dev_db
-- User: hbnb_dev
-- User Password: hbnb_dev_pwd
-- Host: localhost
-- Grants all privileges for this user on the Database
-- Also grants SELECT to the user on performance_schema db

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
