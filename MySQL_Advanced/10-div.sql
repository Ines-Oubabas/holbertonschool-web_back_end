-- Task 10: Create function SafeDiv(a INT, b INT) -> a / b or 0 when b = 0
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
RETURN IF(b = 0, 0, a / b);
//
DELIMITER ;
