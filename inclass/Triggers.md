```sql

create database Triggers2;

use Triggers2;

create table Emp(
ssn char(10),
name varchar(50) not null,
salary decimal(8,2) ,
dept_id int not null, 
constraint minsalary check (salary >=10000),
Primary key  (ssn)
);

create table Dept(
id int,
name char(20) not null,
manager_ssn char(10),
budget decimal(10,2) default 0,
no_of_employee int default 0,

primary key (id)
);

Alter table  Dept add foreign key (manager_ssn) references Emp(ssn);
Alter table Emp add Foreign key (dept_id) references dept(id);

DELIMITER // 
create trigger Emp_insert 
after Insert on Emp 
For Each Row
BEGIN
update Dept set budget= budget + new.salary where id=new.dept_id;
update Dept set no_of_employee= no_of_employee + 1 where id=new.dept_id;
END
//


create trigger del_emp 
after Delete on Emp 
For Each Row
BEGIN
update Dept set budget= budget - old.salary where id=old.dept_id;
update Dept set no_of_employee= no_of_employee - 1 where id=old.dept_id;
END //

create trigger update_emp 
after Update on Emp 
For Each Row
BEGIN
update Dept set budget= budget - old.salary where id=old.dept_id;
update Dept set budget= budget + new.salary where id=new.dept_id;
update Dept set no_of_employee= no_of_employee - 1 where id=old.dept_id;
update Dept set no_of_employee= no_of_employee + 1 where id=new.dept_id;
END
//

create trigger delete_dept 
before Delete on Dept
For Each Row
BEGIN
   IF old.no_of_employee >0  then
      SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Could not delete that department'; 
    END IF;
END
//

```
