CREATE DATABASE q16;
USE q16;

CREATE TABLE order_master(
    Orderno INT PRIMARY KEY,
    Vencode VARCHAR(10),
    Ordstatus VARCHAR(20),
    Delv_date DATE
);

CREATE TABLE order_detail(
    Orderno INT,
    Itemcode INT,
    Qty_ord INT,
    Qty_deld INT
);

INSERT INTO order_master VALUES
(1,'V004','Pending','2006-02-10'),
(2,'V002','Delivered','2006-05-20');

INSERT INTO order_detail VALUES
(1,101,10,5),
(2,102,20,20);

-- a
SELECT *
FROM order_master
WHERE Vencode='V004'
ORDER BY Delv_date;

-- b
SELECT *
FROM order_master
WHERE Delv_date
BETWEEN '2006-01-01'
AND '2006-07-01';

-- c
SELECT *
FROM order_master
WHERE Ordstatus='Pending';

-- d
DELIMITER //

CREATE PROCEDURE LeapYear(IN yr INT)
BEGIN
    IF ((yr%4=0 AND yr%100<>0) OR yr%400=0) THEN
        SELECT 'Leap Year';
    ELSE
        SELECT 'Not Leap Year';
    END IF;
END //

DELIMITER ;

CALL LeapYear(2024);