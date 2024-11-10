
 SET autocommit = 0;
START Transaction;

create table users (id int primary key, name char(10), age int);
insert into users values (1,'Alice',20);
insert into users values (2,'Bob',25);
commit;
