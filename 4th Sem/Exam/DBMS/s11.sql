CREATE DATABASE q11;
USE q11;

CREATE TABLE Department(
    DeptID INT PRIMARY KEY,
    Dept_Name VARCHAR(50),
    HoD VARCHAR(50)
);

CREATE TABLE Student(
    Regno INT PRIMARY KEY,
    name VARCHAR(50),
    gender VARCHAR(10),
    DeptID INT,
    FOREIGN KEY(DeptID) REFERENCES Department(DeptID)
);

INSERT INTO Department VALUES
(1,'CSE','Ravi'),
(2,'IT','Kumar');

INSERT INTO Student VALUES
(101,'Arun','Male',1),
(102,'Ajay','Male',2),
(103,'Divya','Female',1);

-- a
CREATE VIEW CSE_Students AS
SELECT *
FROM Student
WHERE DeptID=1;

-- b
SELECT D.Dept_Name,
       COUNT(S.Regno) AS TotalStudents
FROM Department D
JOIN Student S
ON D.DeptID=S.DeptID
GROUP BY D.Dept_Name
ORDER BY TotalStudents DESC;

-- c
SELECT S.name,
       D.Dept_Name,
       D.HoD
FROM Student S
JOIN Department D
ON S.DeptID=D.DeptID;