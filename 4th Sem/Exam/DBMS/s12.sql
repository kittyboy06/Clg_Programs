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

ALTER TABLE mark_details
ADD average BIGINT;

-- b
SELECT reg_no,
TIMESTAMPDIFF(MONTH,DOB,CURDATE()) AS Months
FROM stu_details;

-- c
ALTER TABLE stu_details
DROP COLUMN address;