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
(2,'Ajay','IT',75,88,95),
(3,'Rahul','ECE',60,70,80);

-- a
ALTER TABLE Marks
ADD Total INT;

UPDATE Marks
SET Total=Subj1+Subj2+Subj3;

-- b
SELECT MAX(Total) AS SecondHighest
FROM Marks
WHERE Total<(
    SELECT MAX(Total) FROM Marks
);

-- c
SELECT Name
FROM Marks
WHERE Total=(
    SELECT MAX(Total)
    FROM Marks
);