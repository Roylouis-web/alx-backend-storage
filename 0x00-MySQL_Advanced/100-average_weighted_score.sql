-- An SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weighted_average FLOAT;

	SELECT (SUM(score * weight) / SUM(weight))
	INTO weighted_average
	FROM corrections INNER JOIN projects
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	UPDATE users
	SET average_score = weighted_average
	WHERE users.id = user_id;

END $$

DELIMITER ; $$
