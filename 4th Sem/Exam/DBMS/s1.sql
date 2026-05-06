CREATE DATABASE fst5_q1;
USE fst5_q1;

CREATE TABLE Customer (
    Custid INT PRIMARY KEY,
    Custname VARCHAR(50),
    Age INT,
    Phone VARCHAR(15)
);

CREATE TABLE Loan (
    Loanid INT PRIMARY KEY,
    Amount DECIMAL(10,2),
    Custid INT,
    EMI DECIMAL(10,2),
    FOREIGN KEY (Custid) REFERENCES Customer(Custid)
);

INSERT INTO Customer VALUES
(1,'Arun',22,'9876543210'),
(2,'Rahul',25,'9876543211'),
(3,'Kavin',24,'9876543212'),
(4,'Ajay',21,'9876543213');

INSERT INTO Loan VALUES
(101,60000,1,2500),
(102,45000,2,2000),
(103,90000,1,3500),
(104,30000,3,1500);

-- a) Customers with loan amount > 50000
SELECT Custname
FROM Customer
WHERE Custid IN (
    SELECT Custid
    FROM Loan
    WHERE Amount > 50000
);

-- b) Customers without loan
SELECT Custid, Custname
FROM Customer
WHERE Custid NOT IN (
    SELECT Custid FROM Loan
);

-- c) Total number of loans
SELECT COUNT(*) AS Total_Loans
FROM Loan;

-- d) Procedure
DELIMITER //

CREATE PROCEDURE GetLoanDetails(IN Lid INT)
BEGIN
    SELECT Amount, Custid
    FROM Loan
    WHERE Loanid = Lid;
END //

DELIMITER ;

CALL GetLoanDetails(101);