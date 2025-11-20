```sql 
create table TR (
	tid int auto_increment primary key,
	userid int,
	amount decimal(10,2),
	type char(10)
);

alter table TR add column balance decimal(10,2);

DELIMITER //
create trigger running_balance 
BEFORE INSERT on TR
FOR EACH ROW
BEGIN
DECLARE user_balance decimal(10,2);

select balance into user_balance from TR  where userid=new.userid order by tid desc limit 1;
IF user_balance is null then 
set user_balance=0;
end if;
IF new.type='withdraw' THEN
set user_balance=user_balance -new.amount;
END IF;

IF new.type='deposit' THEN
	set user_balance=user_balance + new.amount;
END IF;

set new.balance=user_balance;


END //
DELIMITER ;

insert into TR (userid, amount, type) values (1,20,'deposit');
insert into TR (userid, amount, type) values (2,30,'deposit');
insert into TR (userid, amount, type) values (2,10,'withdraw');
insert into TR (userid, amount, type) values (2,30,'withdraw');


select * from TR;
```

