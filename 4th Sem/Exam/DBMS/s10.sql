CREATE DATABASE q10;
USE q10;

CREATE TABLE Marks(
    Regno INT PRIMARY KEY,
    Name VARCHAR(50),
    Dept VARCHAR(50),
    Subj1 INT,
    Subj2 INT,
    Subj3 INT
);

INSERT INTO Marks VALUES
(1,'Arun','CSE',80,90,85),
(2,'Rahul','IT',70,88,92);

-- a
ALTER TABLE Marks
ADD Total INT;

UPDATE Marks
SET Total=Subj1+Subj2+Subj3;

-- b
SELECT MAX(Total)
FROM Marks
WHERE Total<
(
SELECT MAX(Total)
FROM Marks
);

-- c
SELECT Name
FROM Marks
WHERE Total=
(
SELECT MAX(Total)
FROM Marks
);

-- d
DELIMITER //

CREATE PROCEDURE StudentReport()
BEGIN
    SELECT Regno,
           Name,
           Total
    FROM Marks;
END //

DELIMITER ;

CALL StudentReport();