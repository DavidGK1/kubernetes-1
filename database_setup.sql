-- Create the database
CREATE DATABASE my_flask_app;

-- Use the database
USE my_flask_app;

-- Create the 'users' table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(50)
);
