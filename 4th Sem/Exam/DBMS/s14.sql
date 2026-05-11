CREATE DATABASE q14;
USE q14;

CREATE TABLE Course(
    Ccode INT PRIMARY KEY,
    Course_name VARCHAR(50)
);

CREATE TABLE Student(
    Rollno INT PRIMARY KEY,
    Name VARCHAR(50),
    Coursecode INT,
    Mark1 INT,
    Mark2 INT,

    FOREIGN KEY(Coursecode)
    REFERENCES Course(Ccode)
);

ALTER TABLE Student
ADD total INT;

INSERT INTO Course VALUES
(1,'CSE'),
(2,'IT');

-- b
INSERT INTO Student
(Rollno,Name,Coursecode,Mark1,Mark2)
VALUES
(101,'Arun',1,80,90),
(102,'Rahul',2,70,85);

UPDATE Student
SET total=Mark1+Mark2;

-- c
SELECT S.Name,
       C.Course_name
FROM Student S
JOIN Course C
ON S.Coursecode=C.Ccode;

-- d
DELIMITER //

CREATE PROCEDURE OddEven(IN num INT)
BEGIN

IF MOD(num,2)=0 THEN
    SELECT 'Even Number';

ELSE
    SELECT 'Odd Number';

END IF;

END //

DELIMITER ;

CALL OddEven(5);