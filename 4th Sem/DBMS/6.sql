USE mydb2;
CREATE TABLE fool(
    a INT,
    b INT,
    ts TIMESTAMP
);
CREATE TABLE barl(
    a INT,
    b INT
);
INSERT INTO fool (a,b) VALUES
(1,2),
(3,4),
(5,6);
SELECT * FROM fool;
delimiter ///
CREATE TRIGGER sum AFTER insert on fool
FOR EACH ROW
BEGIN
INSERT INTO barl (a,b) VALUES (NEW.a,NEW.b);
END;
delimiter;
DESC Fool;
UPDATE fool set a = 20 WHERE b = 1;
SELECT * FROM barl;