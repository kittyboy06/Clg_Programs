create database mydb2;
use mydb2;
CREATE TABLE Department (
Dept_ID INT PRIMARY KEY,
Dept_Name VARCHAR(20)
);

CREATE TABLE Employee (
Emp_ID INT PRIMARY KEY,
Emp_Name VARCHAR(20),
Salary INT,
Dept_ID INT
);
INSERT INTO Department VALUES (1, 'HR');
INSERT INTO Department VALUES (2, 'IT');
INSERT INTO Employee VALUES (101, 'John', 50000, 1);
INSERT INTO Employee VALUES (102, 'Alice', 60000, 2);
Select * from Department;
Select * from Employee;

SELECT Emp_Name
FROM Employee
WHERE Dept_ID =
(
SELECT Dept_ID
FROM Department
WHERE Dept_Name = 'IT'
);

SELECT *
FROM Employee
Inner JOIN Department
ON Employee.Dept_ID = Department.Dept_ID;

SELECT *
FROM Employee
left JOIN Department
ON Employee.Dept_ID = Department.Dept_ID;

SELECT *
FROM Employee
right JOIN Department
ON Employee.Dept_ID = Department.Dept_ID;

SELECT *
FROM Employee
FULL JOIN Department;

SHOW COLUMNS FROM Employee;