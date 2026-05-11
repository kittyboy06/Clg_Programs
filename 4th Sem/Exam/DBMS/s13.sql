CREATE DATABASE q13;
USE q13;

CREATE TABLE Department(
    Dname VARCHAR(50),
    Deptno INT PRIMARY KEY,
    Dloc VARCHAR(50)
);

CREATE TABLE Employee(
    Empno INT PRIMARY KEY,
    Ename VARCHAR(50),
    Job VARCHAR(50),
    MgrId INT,
    DoB DATE,
    DoJ DATE,
    Sal DECIMAL(10,2),
    Comm DECIMAL(10,2),
    Deptno INT,
    FOREIGN KEY(Deptno) REFERENCES Department(Deptno)
);

INSERT INTO Department VALUES
('Marketing',1,'Chennai'),
('Sales',2,'Madurai');

INSERT INTO Employee VALUES
(101,'Arun','Manager',1,'2000-05-10','2020-01-01',50000,5000,1),
(102,'Ajay','Salesman',1,'1999-05-15','2021-02-10',30000,2000,2);

-- a
SELECT Empno,Ename,Sal,
TIMESTAMPDIFF(YEAR,DoJ,CURDATE()) AS Experience
FROM Employee
ORDER BY Sal DESC;

-- b
SELECT Ename
FROM Employee
WHERE Deptno=(
    SELECT Deptno
    FROM Department
    WHERE Dname='Marketing'
);

-- c
SELECT Ename
FROM Employee
WHERE MONTH(DoB)=MONTH(CURDATE());