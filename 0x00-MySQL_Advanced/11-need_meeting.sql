-- An SQL script that creates a view need_meeting
-- that lists all students that have a score under 80
-- and no last_meeting or more than 1 month


CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR (DATE_FORMAT(last_meeting, "%m") - DATE_FORMAT(last_meeting, "%m")) > 1);
