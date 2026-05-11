CREATE DATABASE q8;
USE q8;

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
(1,'Laptop',50000,10),
(2,'Mobile',20000,15);

INSERT INTO Sales VALUES
(101,1,2),
(102,2,3);

ALTER TABLE Product
ADD reorder INT DEFAULT 50;

-- Sales Report
SELECT P.Prodid,P.Prodesc,S.qty
FROM Product P
JOIN Sales S
ON P.Prodid=S.Prodid;

-- Descending order
SELECT Prodid,SUM(qty) AS TotalQty
FROM Sales
GROUP BY Prodid
ORDER BY TotalQty DESC;