-- Show and add bonus correction

SELECT * FROM `projects`;
SELECT * FROM `corrections`;

SELECT "--";


CALL AddBonus((SELECT `id` FROM `users` WHERE `name` = 'Jeanne'), 'Python is cool', 100);

CALL AddBonus((SELECT `id` FROM `users` WHERE `name` = 'Jeanne'), 'Bonus Project', 100);

CALL AddBonus((SELECT `id` FROM `users` WHERE `name` = 'Bob'), 'Bonus Project', 10);

CALL AddBonus((SELECT `id` FROM `users` WHERE `name` = 'Jeanne'), 'New Bonus', 90);

SELECT "--";

SELECT * FROM `projects`;
SELECT * FROM `corrections`;
