CREATE DATABASE q12;
USE q12;

CREATE TABLE stu_details(
reg_no INT PRIMARY KEY,
stu_name VARCHAR(50),
DOB DATE,
address VARCHAR(100),
city VARCHAR(50)
);

CREATE TABLE mark_details(
reg_no INT,
mark1 INT,
mark2 INT,
mark3 INT,
total INT
);

INSERT INTO stu_details VALUES
(1,'Arun','2005-01-10','Chennai','Chennai'),
(2,'Rahul','2004-05-20','Madurai','Madurai');

INSERT INTO mark_details VALUES
(1,80,90,85,255),
(2,70,88,92,250);

-- a
ALTER TABLE mark_details
ADD average BIGINT;

-- b
SELECT reg_no,
TIMESTAMPDIFF(MONTH,DOB,CURDATE()) AS Months
FROM stu_details;

-- c
ALTER TABLE stu_details
DROP COLUMN address;

-- d
DELIMITER //

CREATE PROCEDURE StudentAverage()
BEGIN

SELECT reg_no,
(mark1+mark2+mark3) AS Total,
(mark1+mark2+mark3)/3 AS Average
FROM mark_details;

END //

DELIMITER ;

CALL StudentAverage();