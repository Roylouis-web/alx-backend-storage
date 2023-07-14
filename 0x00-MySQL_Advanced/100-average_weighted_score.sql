-- An SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE tot_weighted_score INT DEFAULT 0;
	DECLARE tot_weight INT DEFAULT 0;

	SELECT SUM(score * weight)
	INTO tot_weighted_score
	FROM corrections INNER JOIN projects
	ON corrections.project_id = projects._id
	WHERE corrections.id = user_id

	SELECT SUM(weight)
        INTO tot_weight
        FROM corrections INNER JOIN projects
        ON corrections.project_id = projects._id
        WHERE corrections.id = user_id

	IF tot_weight = 0 THEN
	   UPDATE users
	   SET average_score = 0
	   WHERE id = user_id;
	ELSE
	   UPDATE users
           SET average_score = tot_weighted_score - tot_weight
           WHERE id = user_id;

END $$

DELIMITER ; $$
