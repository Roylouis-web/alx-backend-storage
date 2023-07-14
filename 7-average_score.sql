-- An SQL script that creates a stored procedure
-- named ComputeAverageScoreForUser that computes
-- the average score for a student


DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;

	SELECT (SUM(`score`) / COUNT(*)) INTO avg_score
	FROM `users` INNER JOIN `corrections`
	ON `corrections`.`user_id` = `id`
	WHERE `id` = user_id
	GROUP BY `id`;

	UPDATE `users`
	SET `average_score` = avg_score
	WHERE `id` = user_id;
END $$

DELIMITER ; $$
