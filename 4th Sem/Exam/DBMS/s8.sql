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
(1,'Laptop',50000,10);

INSERT INTO Sales VALUES
(101,1,2);

-- a
ALTER TABLE Product
ADD reorder1 INT DEFAULT 50;

-- b
SELECT P.Prodid,
       P.Prodesc,
       S.qty
FROM Product P
JOIN Sales S
ON P.Prodid=S.Prodid;

-- c
SELECT Prodid,
       SUM(qty)
FROM Sales
GROUP BY Prodid
ORDER BY SUM(qty) DESC;

-- d
SELECT *
FROM Product
WHERE Stock>0;