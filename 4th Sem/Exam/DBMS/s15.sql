CREATE DATABASE q15;
USE q15;

CREATE TABLE Department(
    Depno INT PRIMARY KEY,
    Depname VARCHAR(50),
    Deplocation VARCHAR(50)
);

CREATE TABLE Employee(
    Empno INT PRIMARY KEY,
    Empname VARCHAR(50),
    DOJ DATE,
    Salary DECIMAL(10,2),
    Depno INT,
    FOREIGN KEY(Depno) REFERENCES Department(Depno)
);

INSERT INTO Department VALUES
(1,'CSE','Chennai'),
(2,'IT','Madurai');

INSERT INTO Employee VALUES
(101,'Arun','2020-01-01',50000,1),
(102,'Ajay','2021-02-10',30000,2);

-- a
SELECT Depno,COUNT(*) AS TotalEmployees
FROM Employee
GROUP BY Depno
ORDER BY Depno DESC;

-- b
SELECT DISTINCT D.Depname
FROM Department D
JOIN Employee E
ON D.Depno=E.Depno;

-- c
SELECT Empname,
       DOJ,
       TIMESTAMPDIFF(YEAR,DOJ,CURDATE()) AS YearsCompleted
FROM Employee;