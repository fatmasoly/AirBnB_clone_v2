-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it does not already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant SELECT privileges on the 'performance_schema' schema to the 'hbnb_test' user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Refresh MySQL privileges to apply the changes
FLUSH PRIVILEGES;

-- Grant all privileges on the 'hbnb_test_db' database to the 'hbnb_test' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Refresh MySQL privileges to apply the changes
FLUSH PRIVILEGES;
