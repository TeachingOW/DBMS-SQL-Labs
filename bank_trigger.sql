-- CREATE the user TABLE
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS overdraft_fees;

DROP  TRIGGER IF EXISTS check_transaction_trigger;
DROP EVENT IF EXISTS process_overdraft_fees;


CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00  -- Balance WITH two DECIMAL places
);

-- CREATE the transactions TABLE
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userid INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,  -- Positive FOR deposits, negative FOR withdrawals
    type INT DEFAULT 0,  -- 0 FOR non-automatic, 1 FOR automatic
    FOREIGN KEY (userid) REFERENCES user(id) ON DELETE CASCADE
);

-- TABLE FOR tracking overdraft fees to be processed
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

    -- Step 1: UPDATE the user's balance based ON TRANSACTION amount
    UPDATE user
    SET balance = balance + NEW.amount
    WHERE id = NEW.userid;

    -- Step 2: CHECK the balance AFTER the TRANSACTION
    SELECT balance INTO balance_after_transaction FROM user WHERE id = NEW.userid;

    -- Step 3: INSERT INTO overdraft_fees IF balance IS below zero AFTER a non-automatic withdrawal
    IF balance_after_transaction < 0 AND NEW.amount < 0 AND NEW.type = 0 THEN
        INSERT INTO overdraft_fees (userid) VALUES (NEW.userid);
        
        -- Deduct the $30 fee FROM the user's balance
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

    -- CURSOR to iterate through unprocessed overdraft fees
    DECLARE fee_cursor CURSOR FOR 
        SELECT userid FROM overdraft_fees WHERE processed = FALSE;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN fee_cursor;

    read_loop: LOOP
        FETCH fee_cursor INTO overdraft_userid;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- INSERT the fee TRANSACTION INTO the transactions TABLE
        INSERT INTO transactions (userid, amount, type)
        VALUES (overdraft_userid, -30.00, 1);

        -- Mark the fee AS processed
        UPDATE overdraft_fees
        SET processed = TRUE
        WHERE userid = overdraft_userid;
    END LOOP;

    CLOSE fee_cursor;
END$$

DELIMITER ;


-- INSERT sample users INTO the user TABLE
INSERT INTO user (name, balance) VALUES ('Alice', 500.00);
INSERT INTO user (name, balance) VALUES ('Bob', 1000.00);
INSERT INTO user (name, balance) VALUES ('Charlie', 50.00);
INSERT INTO user (name, balance) VALUES ('Diana', 0.00);
INSERT INTO user (name, balance) VALUES ('Eve', 250.00);

INSERT INTO transactions(userid, amount) VALUES (1,-300);
