CREATE DATABASE q9;
USE q9;

CREATE TABLE Member(
    membercode INT PRIMARY KEY,
    membername VARCHAR(50),
    phoneno VARCHAR(15)
);

CREATE TABLE Book(
    bookcode INT PRIMARY KEY,
    categorycode INT,
    bookname VARCHAR(50),
    cost DECIMAL(10,2)
);

CREATE TABLE IssueBook(
    membercode INT,
    bookcode INT,
    issuedate DATE,
    returndate DATE
);

INSERT INTO Member VALUES
(1,'Arun','9876543210'),
(2,'Ajay','9876543211');

INSERT INTO Book VALUES
(101,1,'DBMS',500),
(102,2,'Java',300);

INSERT INTO IssueBook VALUES
(1,101,'2007-10-08','2007-10-15'),
(2,102,'2007-10-08','2007-10-16');

-- a
SELECT membername
FROM Member
WHERE membercode IN (
    SELECT membercode
    FROM IssueBook
    WHERE issuedate='2007-10-08'
);

-- b
SELECT membercode
FROM IssueBook
WHERE bookcode IN (
    SELECT bookcode
    FROM Book
    WHERE cost>400
);