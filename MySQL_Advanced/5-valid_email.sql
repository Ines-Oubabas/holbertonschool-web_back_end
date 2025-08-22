-- Task 5: Create trigger that resets valid_email to 0 ONLY when the email is changed
-- Uses BEFORE UPDATE so we can modify NEW.valid_email
DROP TRIGGER IF EXISTS reset_valid_email;
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END//
DELIMITER ;
