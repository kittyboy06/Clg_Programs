create database mydb;
use mydb;
create table employee(
    emp_id int(3),
    emp_name varchar(20),
    dept varchar(20),
    age int(3),
    date_of_join date,
    emp_salary int(10)
);
insert into employee values(101,'John','HR',30,'2020-01-15',50000);
insert into employee values(102,'Alice','IT',28,'2019-03-20',60000);
insert into employee values(103,'Bob','Finance',35,'2018-07-10',55000);
select * from employee;