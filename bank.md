
### Assignment: Implement Overdraft Fees in a Bank Account System

#### Background:

You are tasked with simulating the transactions of a bank account. You have been given a starting schema that keeps track of user transactions, including deposits and withdrawals, and automatically calculates the running balance for each user.

#### Task:

Currently, when a user withdraws money from their account, the balance is updated accordingly. However, if a withdrawal causes the balance to go below zero, an **overdraft fee** should be applied. The overdraft fee should be added to the transaction table as a separate line item.

You are required to implement the following:

1. **Overdraft Fee Logic**: If a user’s account balance goes below zero after a withdrawal, an overdraft fee of $25.00 should be charged.
2. **Separate Overdraft Transaction**: The overdraft fee should appear as a separate transaction with a type of `'overdraft_fee'` and a negative amount in the transaction table.

#### Given Schema:

You are provided with the following code to get started. This code creates the necessary table (`TR`) to store transactions and a trigger that calculates the running balance after each transaction.

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

#### Instructions:

1. **Modify the Trigger**: Update the `running_balance` trigger to check if the account balance goes below zero after a withdrawal. If it does, add an overdraft fee transaction.

2. **Overdraft Fee Transaction**: Add a new transaction with:

   * A type of `'overdraft_fee'`
   * A negative amount of `-25.00` (this represents the fee charged for overdrafting).

3. **Test Your Implementation**: Insert several transactions, including withdrawals that will cause the balance to go negative, and verify that the overdraft fee is correctly applied as a separate transaction.

#### Example:

After running the following series of transactions:

```sql
insert into TR (userid, amount, type) values (1, 50, 'deposit');  -- User 1 deposits $50
insert into TR (userid, amount, type) values (1, 70, 'withdraw'); -- User 1 withdraws $70
insert into TR (userid, amount, type) values (1, 10, 'withdraw'); -- User 1 withdraws another $10 (total balance -30)
```

The expected output in the `TR` table should look like:

| tid | userid | amount | type          | balance |
| --- | ------ | ------ | ------------- | ------- |
| 1   | 1      | 50.00  | deposit       | 50.00   |
| 2   | 1      | 70.00  | withdraw      | -20.00  |
| 3   | 1      | 10.00  | withdraw      | -30.00  |
| 4   | 1      | 25.00  | overdraft_fee | -55.00  |

#### Submission:

Submit the SQL code for the trigger and any necessary modifications to the schema. Be sure to include sample test cases that demonstrate how your solution works.

---
