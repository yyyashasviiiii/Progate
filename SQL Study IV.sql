
--      INSERT Statement in SQL 

-- add data to the students table

INSERT INTO students(   name,course)
VALUES(   "Kate","Java");
-- do not delete the following query
select * from students;


--    UPDATE  Statement  in  SQL

-- within the students table, update the name to Jordan and the course to HTML for the record that has an id of 6
UPDATE students
SET name = "Jordan", course = "HTML"
WHERE id = 6;
-- do not delete the following query
SELECT * FROM students WHERE id = 6;


--      DELETE  Statement in  SQL

-- delete the record with the id of 7 within the students table
DELETE FROM students
WHERE id = 7;
-- do not delete the following query
SELECT * FROM students;

