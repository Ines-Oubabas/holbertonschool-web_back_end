-- Task 7: Stored procedure ComputeAverageScoreForUser(user_id)
-- Computes AVG(score) for the user and stores it into users.average_score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
  DECLARE v_avg DECIMAL(10,4);

  SELECT AVG(score) INTO v_avg
  FROM corrections
  WHERE user_id = p_user_id;

  UPDATE users
  SET average_score = COALESCE(v_avg, 0)
  WHERE id = p_user_id;
END//
DELIMITER ;
