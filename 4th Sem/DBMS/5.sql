Create database mydb5;
use mydb5;

CREATE TABLE student(
    studid INT PRIMARY KEY,
    studname VARCHAR(50),
    gender VARCHAR(10),
    percentage DECIMAL(5,2)
);

INSERT INTO student VALUES
(1,'Sooriya','Male',95),
(2,'Prag','Female',88),
(3,'Syed','Male',92),
(4,'Alan','Female',97);

Insert Into student VALUES
(5,'Afsal','Male',91),
(6,'Aash','Female',92);

delimiter ///
Create procedure Student()
Begin
SELECT studid,studname,gender,percentage FROM student WHERE percentage>90;
End ///

call Student;