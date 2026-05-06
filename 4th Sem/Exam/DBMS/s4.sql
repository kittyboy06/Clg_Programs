CREATE DATABASE fst5_q4;
USE fst5_q4;

CREATE TABLE Book (
    Bookid INT PRIMARY KEY,
    Book_name VARCHAR(50),
    Author VARCHAR(50),
    Publication VARCHAR(50),
    Price DECIMAL(10,2)
);

CREATE TABLE User1 (
    Userid INT PRIMARY KEY,
    Name VARCHAR(50),
    Dept VARCHAR(50),
    Bookid INT,
    Accdate DATE,
    FOREIGN KEY (Bookid) REFERENCES Book(Bookid)
);

INSERT INTO Book VALUES
(1,'DBMS','Navathe','Wiley',550),
(2,'Java','Herbert','McGrawHill',700),
(3,'Python','Mark Lutz','Wiley',900),
(4,'C Programming','Dennis','Pearson',450);

INSERT INTO User1 VALUES
(101,'Arun','CSE',1,'2026-04-01'),
(102,'Kavin','IT',3,'2026-04-05'),
(103,'Ajay','ECE',2,'2026-04-10');

-- a) User who accessed costliest book
SELECT Name
FROM User1
WHERE Bookid = (
    SELECT Bookid
    FROM Book
    WHERE Price = (
        SELECT MAX(Price)
        FROM Book
    )
);

-- b) User and count of books
SELECT Userid, COUNT(Bookid) AS Book_Count
FROM User1
GROUP BY Userid;

-- c) Wiley publications
SELECT *
FROM Book
WHERE Publication = 'Wiley';

-- d) Procedure
DELIMITER //

CREATE PROCEDURE BookDetails(IN bid INT)
BEGIN
    SELECT Book_name, Author
    FROM Book
    WHERE Bookid = bid;
END //

DELIMITER ;

CALL BookDetails(3);