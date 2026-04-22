-- Create Table
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

-- Insert Data
INSERT INTO Students VALUES (1, 'Suryakant', 20);
INSERT INTO Students VALUES (2, 'Rahul', 21);

-- Select Query
SELECT * FROM Students;

-- Update Query
UPDATE Students SET age = 22 WHERE id = 1;

-- Delete Query
DELETE FROM Students WHERE id = 2;
