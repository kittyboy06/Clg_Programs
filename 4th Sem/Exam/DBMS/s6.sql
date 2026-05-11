CREATE DATABASE q6;
USE q6;

CREATE TABLE Customer(
    Custid INT PRIMARY KEY,
    Custname VARCHAR(50),
    phno VARCHAR(15),
    pan VARCHAR(20),
    DOB DATE
);

CREATE TABLE HomeLoan(
    HLoanid INT PRIMARY KEY,
    Amount DECIMAL(10,2),
    Custid INT,
    FOREIGN KEY(Custid) REFERENCES Customer(Custid)
);

CREATE TABLE VehicleLoan(
    VLoanid INT PRIMARY KEY,
    Amount DECIMAL(10,2),
    Custid INT,
    FOREIGN KEY(Custid) REFERENCES Customer(Custid)
);

INSERT INTO Customer VALUES
(1,'Arun','9876543210','ABCDE1234F','2000-01-01'),
(2,'Rahul','9876543211','PQRS1234K','2001-02-02');

INSERT INTO HomeLoan VALUES
(101,500000,1);

INSERT INTO VehicleLoan VALUES
(201,200000,1);

-- a
SELECT Custid
FROM HomeLoan
WHERE Custid IN
(SELECT Custid FROM VehicleLoan);

-- b
SELECT Custid
FROM Customer
WHERE Custid NOT IN
(
SELECT Custid FROM HomeLoan
UNION
SELECT Custid FROM VehicleLoan
);

-- c
CREATE VIEW LoanView AS
SELECT C.Custid,
       C.Custname,
       IFNULL(H.Amount,0)+IFNULL(V.Amount,0) AS TotalLoan
FROM Customer C
LEFT JOIN HomeLoan H
ON C.Custid=H.Custid
LEFT JOIN VehicleLoan V
ON C.Custid=V.Custid;

SELECT * FROM LoanView;

-- d
DELIMITER //

CREATE TRIGGER HomeLoanTrigger
AFTER INSERT
ON HomeLoan
FOR EACH ROW
BEGIN
    SELECT * FROM HomeLoan
    WHERE HLoanid=NEW.HLoanid;
END //

DELIMITER ;