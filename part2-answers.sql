-- Paste your answers for each question in the appropriate spot below. (Keep the number headings)

-- #1 Select all students that have both firstname starting with "J" and id greater than 3. (In this case, only Javier would match.)

SELECT *
FROM students
WHERE firstname LIKE 'J%' AND id > 3;

-- #2 In one SQL statement, get the first and last names of all students that scored above 90 on the Geography Quiz. (Include only the firstname and lastname columns in the result.)

SELECT s.firstname, s.lastname
FROM students AS s
JOIN assignments AS a ON s.id = a.student_id
WHERE a.title = 'Geography Quiz' AND a.score > 90;