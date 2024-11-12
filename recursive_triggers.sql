drop table  if exists user;
drop table if exists transactions;


-- Create the user table
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00  -- Balance with two decimal places
);

-- Create the transactions table
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,  -- Positive for deposits, negative for withdrawals
    type int default 0,  -- Transaction type
    FOREIGN KEY (userid) REFERENCES user(id) ON DELETE CASCADE
);

DROP  TRIGGER if exists check_transaction_trigger;

-- Trigger to handle transactions and fees
DELIMITER $$

CREATE TRIGGER check_transaction_trigger
AFTER INSERT ON transactions
FOR EACH ROW
BEGIN
    DECLARE balance_after_transaction DECIMAL(10, 2);

    -- Step 1: Update the user's balance based on transaction amount
    UPDATE user
    SET balance = balance + NEW.amount
    WHERE id = NEW.userid;

    -- Step 2: Check the balance after the transaction
    SELECT balance INTO balance_after_transaction FROM user WHERE id = NEW.userid;

    -- Step 3: Apply a $30 fee if balance goes below zero after a withdrawal
    IF balance_after_transaction < 0 AND NEW.amount < 0 and new.type=0 THEN
        -- Insert a new row in the transactions table for the overdraft fee
        INSERT INTO transactions (userid, amount, type)
        VALUES (NEW.userid, -30.00,1 );
        
        -- Deduct the $30 fee from the user's balance
        UPDATE user
        SET balance = balance - 30
        WHERE id = NEW.userid;
    END IF;

END$$

DELIMITER ;


DELIMITER ;


-- Insert sample users into the user table
INSERT INTO user (name, balance) VALUES ('Alice', 500.00);
INSERT INTO user (name, balance) VALUES ('Bob', 1000.00);
INSERT INTO user (name, balance) VALUES ('Charlie', 50.00);
INSERT INTO user (name, balance) VALUES ('Diana', 0.00);
INSERT INTO user (name, balance) VALUES ('Eve', 250.00);

insert into transactions (userid, amount)  values (1,-300);
