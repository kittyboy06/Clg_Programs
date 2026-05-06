CREATE DATABASE fst5_q2;
USE fst5_q2;

CREATE TABLE Dept (
    Deptno INT PRIMARY KEY,
    Dname VARCHAR(50),
    Loc VARCHAR(50),
    DeptmanagerId INT
);

CREATE TABLE Employee (
    EmpId INT PRIMARY KEY,
    Empname VARCHAR(50),
    Sal DECIMAL(10,2),
    Deptno INT,
    FOREIGN KEY (Deptno) REFERENCES Dept(Deptno)
);

INSERT INTO Dept VALUES
(10,'HR','Chennai',101),
(20,'IT','Bangalore',102),
(30,'Sales','Mumbai',103);

INSERT INTO Employee VALUES
(101,'Ramesh',50000,10),
(102,'Suresh',65000,20),
(103,'Ganesh',55000,30),
(104,'Vijay',40000,20),
(105,'Ajith',35000,10);

-- a) Count and average salary department-wise
SELECT Deptno,
       COUNT(*) AS Employee_Count,
       AVG(Sal) AS Average_Salary
FROM Employee
GROUP BY Deptno;

-- b) Employee name, department name and salary
SELECT E.Empname, D.Dname, E.Sal
FROM Employee E
JOIN Dept D
ON E.Deptno = D.Deptno;

-- c) Employee and manager name
SELECT E.Empname AS Employee,
       M.Empname AS Manager
FROM Employee E
JOIN Dept D
ON E.Deptno = D.Deptno
JOIN Employee M
ON D.DeptmanagerId = M.EmpId;

-- d) Function
DELIMITER //

CREATE FUNCTION GetSalary(Eid INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE salary DECIMAL(10,2);

    SELECT Sal INTO salary
    FROM Employee
    WHERE EmpId = Eid;

    RETURN salary;
END //

DELIMITER ;

SELECT GetSalary(102);