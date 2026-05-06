CREATE DATABASE fst5_q3;
USE fst5_q3;

CREATE TABLE Booth (
    Boothid INT PRIMARY KEY,
    Location VARCHAR(50),
    BIncharge VARCHAR(50)
);

CREATE TABLE Voter (
    VoterId INT PRIMARY KEY,
    Votername VARCHAR(50),
    Gender VARCHAR(10),
    Boothid INT,
    Checkvote INT,
    FOREIGN KEY (Boothid) REFERENCES Booth(Boothid)
);

INSERT INTO Booth VALUES
(1,'Kumbakonam','Ravi'),
(2,'Thanjavur','Kumar'),
(3,'Chennai','Siva');

INSERT INTO Voter VALUES
(101,'Arun','Male',1,1),
(102,'Priya','Female',1,1),
(103,'Kavin','Male',2,0),
(104,'Divya','Female',2,1),
(105,'Ajay','Male',3,0);

-- a) Count voters booth-wise
SELECT Boothid, COUNT(*) AS Total_Voters
FROM Voter
GROUP BY Boothid;

-- b) Total voted voters
SELECT COUNT(*) AS Voted_Count
FROM Voter
WHERE Checkvote = 1;

-- c) Booth details with voted count
SELECT B.Boothid,
       B.Location,
       COUNT(V.VoterId) AS Voted_Count
FROM Booth B
JOIN Voter V
ON B.Boothid = V.Boothid
WHERE V.Checkvote = 1
GROUP BY B.Boothid, B.Location;

-- d) Function
DELIMITER //

CREATE FUNCTION PollPercent(bid INT)
RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    DECLARE total INT;
    DECLARE voted INT;

    SELECT COUNT(*) INTO total
    FROM Voter
    WHERE Boothid = bid;

    SELECT COUNT(*) INTO voted
    FROM Voter
    WHERE Boothid = bid
    AND Checkvote = 1;

    RETURN (voted * 100.0 / total);
END //

DELIMITER ;

SELECT PollPercent(1);