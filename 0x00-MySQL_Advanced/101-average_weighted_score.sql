-- An SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and-- stores the average weighted score for all students

DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT 0;
	DECLARE weighted_average FLOAT;
	DECLARE user_id INT;
	DECLARE cur CURSOR FOR SELECT users.id,
	SUM(score * weight) / SUM(weight) FROM
	users INNER JOIN corrections ON
	corrections.user_id = users.id
	INNER JOIN projects
	ON projects.id = corrections.project_id
	GROUP BY users.id;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET
	done = 1;
	OPEN cur;
	label: LOOP
	FETCH cur INTO user_id, weighted_average;
	UPDATE users
	SET average_score = weighted_average
	WHERE users.id = user_id;
	IF done = 1 THEN 
		LEAVE label;
	END IF;
	END LOOP;
	CLOSE cur;
END $$

DELIMITER ; $$
