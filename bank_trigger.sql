-- Create the user table
drop table if exists user;
drop table if exists transactions;
drop table if exists overdraft_fees;

DROP  TRIGGER if exists check_transaction_trigger;
DROP EVENT if exists process_overdraft_fees;


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
    type INT DEFAULT 0,  -- 0 for non-automatic, 1 for automatic
    FOREIGN KEY (userid) REFERENCES user(id) ON DELETE CASCADE
);

-- Table for tracking overdraft fees to be processed
CREATE TABLE overdraft_fees (
    userid INT NOT NULL,
    fee_amount DECIMAL(10, 2) DEFAULT -30.00,
    processed BOOLEAN DEFAULT FALSE
);

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

    -- Step 3: Insert into overdraft_fees if balance is below zero after a non-automatic withdrawal
    IF balance_after_transaction < 0 AND NEW.amount < 0 AND NEW.type = 0 THEN
        INSERT INTO overdraft_fees (userid) VALUES (NEW.userid);
        
        -- Deduct the $30 fee from the user's balance
        UPDATE user
        SET balance = balance - 30
        WHERE id = NEW.userid;
    END IF;

END$$

DELIMITER ;


DELIMITER $$

CREATE EVENT process_overdraft_fees
ON SCHEDULE EVERY 1 MINUTE
DO
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE overdraft_userid INT;

    -- Cursor to iterate through unprocessed overdraft fees
    DECLARE fee_cursor CURSOR FOR 
        SELECT userid FROM overdraft_fees WHERE processed = FALSE;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN fee_cursor;

    read_loop: LOOP
        FETCH fee_cursor INTO overdraft_userid;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Insert the fee transaction into the transactions table
        INSERT INTO transactions (userid, amount, type)
        VALUES (overdraft_userid, -30.00, 1);

        -- Mark the fee as processed
        UPDATE overdraft_fees
        SET processed = TRUE
        WHERE userid = overdraft_userid;
    END LOOP;

    CLOSE fee_cursor;
END$$

DELIMITER ;


-- Insert sample users into the user table
INSERT INTO user (name, balance) VALUES ('Alice', 500.00);
INSERT INTO user (name, balance) VALUES ('Bob', 1000.00);
INSERT INTO user (name, balance) VALUES ('Charlie', 50.00);
INSERT INTO user (name, balance) VALUES ('Diana', 0.00);
INSERT INTO user (name, balance) VALUES ('Eve', 250.00);

INSERT INTO transactions(userid, amount) values (1,-300);
