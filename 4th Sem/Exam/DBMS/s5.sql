CREATE DATABASE fst5_q5;
USE fst5_q5;

CREATE TABLE Customer (
    Custid INT PRIMARY KEY,
    Custname VARCHAR(50),
    Addr VARCHAR(100),
    Phno VARCHAR(15),
    Panno VARCHAR(20)
);

CREATE TABLE Loan (
    Loanid INT PRIMARY KEY,
    Amount DECIMAL(10,2),
    Interest DECIMAL(5,2),
    Custid INT,
    FOREIGN KEY (Custid) REFERENCES Customer(Custid)
);

CREATE TABLE Account (
    Acctno INT PRIMARY KEY,
    Accbal DECIMAL(10,2),
    Custid INT,
    FOREIGN KEY (Custid) REFERENCES Customer(Custid)
);

INSERT INTO Customer VALUES
(1,'ARUN','Chennai','9876543210','ABCDE1234F'),
(2,'RAHUL','Madurai','9876543211','PQRSX5678K'),
(3,'AJAY','Trichy','9876543212','LMNOP9876A');

INSERT INTO Loan VALUES
(101,100000,7.5,1),
(102,50000,8.0,2),
(103,75000,7.0,3);

INSERT INTO Account VALUES
(1001,70000,1),
(1002,10000,2),
(1003,50000,3);

-- a) Account balance of ARUN
SELECT Accbal
FROM Account A
JOIN Customer C
ON A.Custid = C.Custid
WHERE C.Custname = 'ARUN';

-- b) Update interest
UPDATE Loan L
JOIN Account A
ON L.Custid = A.Custid
SET L.Interest = L.Interest + 1
WHERE A.Accbal > 0.5 * L.Amount;

-- c) View
CREATE VIEW Customer_View AS
SELECT A.Accbal, L.Amount
FROM Account A
JOIN Loan L
ON A.Custid = L.Custid;

SELECT * FROM Customer_View;

-- d) Trigger
DELIMITER //

CREATE TRIGGER Account_Update_Trigger
AFTER UPDATE
ON Account
FOR EACH ROW
BEGIN
    INSERT INTO Account_Log
    VALUES (NEW.Custid, NOW());
END //

DELIMITER ;

-- Log Table
CREATE TABLE Account_Log (
    Custid INT,
    Updated_Time DATETIME
);

UPDATE Account
SET Accbal = 80000
WHERE Acctno = 1001;

SELECT * FROM Account_Log;