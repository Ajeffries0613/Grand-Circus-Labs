-- Run the following SQL statements to create and populate the two tables needed
-- for the SQL questions on this assessment.

CREATE TABLE students (
 id SERIAL PRIMARY KEY,
 firstname VARCHAR(20),  lastname VARCHAR(20),  email VARCHAR(30),  phone VARCHAR(30)
);
INSERT INTO students (id, firstname, lastname, email, phone)
VALUES
  (1, 'Jane', 'Doe', 'jane@example.com', '313-555-0001'),
  (2, 'James', 'Smith', 'james@example.com', '313-555-0002'),
  (3, 'Susan', 'Jones', 'susan@example.com', '313-555-0003'),
  (4, 'Javier', 'Rodriguez', 'javier@example.com', '313-555-0004'),
  (5, 'DeAndre', 'Taylor', 'deandre@example.com', '313-555-0005');

CREATE TABLE assignments (
 id SERIAL PRIMARY KEY,
 title VARCHAR(40),  score INT,  student_id INT
);
INSERT INTO assignments (title, score, student_id)
VALUES
  ('Geography Quiz', 85, 1),
  ('US States Worksheet', 10, 1),
  ('Geography Quiz', 92, 4);