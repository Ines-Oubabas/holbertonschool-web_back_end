-- Task 0: Create table `users` with unique email
-- Requirements: id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255)
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  PRIMARY KEY (id),
  UNIQUE KEY email (email)
);
