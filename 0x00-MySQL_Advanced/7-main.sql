-- Show and compute average score

SELECT * FROM `users`;
SELECT * FROM `corrections`;

CALL ComputeAverageScoreForUser((SELECT `id` FROM `users` WHERE `name` = 'Bob'));

SELECT "--";
SELECT * FROM `users`;
