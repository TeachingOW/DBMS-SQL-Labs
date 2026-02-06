
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
CREATE TABLE TR (
	tid INT AUTO_INCREMENT PRIMARY KEY,
	userid INT,
	amount DECIMAL(10,2),
	type CHAR(10)
);

ALTER TABLE TR ADD COLUMN balance DECIMAL(10,2);

DELIMITER //
CREATE TRIGGER running_balance 
BEFORE INSERT ON TR
FOR EACH ROW
BEGIN
DECLARE user_balance DECIMAL(10,2);

SELECT balance INTO user_balance FROM TR  WHERE userid=NEW.userid ORDER BY tid DESC LIMIT 1;
IF user_balance IS NULL THEN 
SET user_balance=0;
END IF;
IF NEW.type='withdraw' THEN
SET user_balance=user_balance -NEW.amount;
END IF;

IF NEW.type='deposit' THEN
	SET user_balance=user_balance + NEW.amount;
END IF;

SET NEW.balance=user_balance;

END //
DELIMITER ;

INSERT INTO TR (userid, amount, type) VALUES (1,20,'deposit');
INSERT INTO TR (userid, amount, type) VALUES (2,30,'deposit');
INSERT INTO TR (userid, amount, type) VALUES (2,10,'withdraw');
INSERT INTO TR (userid, amount, type) VALUES (2,30,'withdraw');

SELECT * FROM TR;
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
INSERT INTO TR (userid, amount, type) VALUES (1, 50, 'deposit');  -- User 1 deposits $50
INSERT INTO TR (userid, amount, type) VALUES (1, 70, 'withdraw'); -- User 1 withdraws $70
INSERT INTO TR (userid, amount, type) VALUES (1, 10, 'withdraw'); -- User 1 withdraws another $10 (total balance -30)
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
