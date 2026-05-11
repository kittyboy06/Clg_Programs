CREATE DATABASE q7;
USE q7;

CREATE TABLE Product(
    Prodid INT PRIMARY KEY,
    Prodesc VARCHAR(50),
    Price DECIMAL(10,2),
    Stock INT
);

CREATE TABLE Sales(
    Salesid INT PRIMARY KEY,
    Prodid INT,
    qty INT,
    FOREIGN KEY(Prodid) REFERENCES Product(Prodid)
);

INSERT INTO Product VALUES
(1,'Mouse',500,100),
(2,'Keyboard',1000,50);

INSERT INTO Sales VALUES
(101,1,10),
(102,2,5);

-- a
ALTER TABLE Product
ADD reorder1 INT DEFAULT 50;

-- b
SELECT Prodid,
       SUM(qty) AS TotalQty
FROM Sales
GROUP BY Prodid
ORDER BY TotalQty DESC;

-- c
DELIMITER //

CREATE PROCEDURE Fibonacci(IN n INT)
BEGIN
    DECLARE a INT DEFAULT 0;
    DECLARE b INT DEFAULT 1;
    DECLARE c INT;

    WHILE n>0 DO
        SELECT a;

        SET c=a+b;
        SET a=b;
        SET b=c;

        SET n=n-1;
    END WHILE;
END //

DELIMITER ;

CALL Fibonacci(5);

-- d
CREATE TABLE Login(
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO Login VALUES
('admin','admin123');

SELECT *
FROM Login
WHERE username='admin'
AND password='admin123';