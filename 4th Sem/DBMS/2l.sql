create database sub;
use sub;
create table t1(
    id int(3),
    Name varchar(20),
    Dept varchar(20)
);
create table t2(
    id int(3),
    Name varchar(20),
    Dept varchar(20)
);
create table t3(
    id int(3),
    Age int(20),
    City varchar(20)
);

insert into t1 values(1,'AAA','MATHS');
insert into t1 values(2,'BBB','SCIENCE');
insert into t1 values(3,'CCC','SCIENCE');
insert into t1 values(4,'DDD','ENGLISH');

insert into t2 values(1,'FFF','MATHS');
insert into t2 values(2,'GGG','SCIENCE');
insert into t2 values(3,'HHH','SCIENCE');
insert into t2 values(4,'III','ENGLISH');
insert into t2 values(5,'JJJ','ENGLISH');
insert into t2 values(6,'QQQ','MATHS');

insert into t3 values(1,20,'CHENNAI');
insert into t3 values(2,21,'CHENNAI');
insert into t3 values(3,22,'CHENNAI');
insert into t3 values(4,23,'CHENNAI');
insert into t3 values(5,24,'CHENNAI');
insert into t3 values(6,25,'CHENNAI');
insert into t3 values(7,26,'CHENNAI');

SELECT *
FROM t1
WHERE Dept IN
(
SELECT Dept
FROM t2
WHERE Dept='SCIENCE'
);

SELECT *
FROM t1
FULL JOIN t3;

select * FROM t1;
select * FROM t3;