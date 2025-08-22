-- Task 1: Create table `users` with country ENUM('US','CO','TN') defaulting to 'US'
-- Requirements: id INT NOT NULL AUTO_INCREMENT PK, email UNIQUE NOT NULL, name VARCHAR(255), country ENUM NOT NULL DEFAULT 'US'
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  country ENUM('US','CO','TN') NOT NULL DEFAULT 'US',
  PRIMARY KEY (id),
  UNIQUE KEY email (email)
);
