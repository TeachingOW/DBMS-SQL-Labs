DROP TABLE  IF EXISTS user;
DROP TABLE IF EXISTS transactions;


-- CREATE the user TABLE
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
    type INT DEFAULT 0,  -- TRANSACTION type
    FOREIGN KEY (userid) REFERENCES user(id) ON DELETE CASCADE
);

DROP  TRIGGER IF EXISTS check_transaction_trigger;

-- TRIGGER to handle transactions AND fees
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

    -- Step 3: Apply a $30 fee IF balance goes below zero AFTER a withdrawal
    IF balance_after_transaction < 0 AND NEW.amount < 0 AND NEW.type=0 THEN
        -- INSERT a NEW ROW IN the transactions TABLE FOR the overdraft fee
        INSERT INTO transactions (userid, amount, type)
        VALUES (NEW.userid, -30.00,1 );
        
        -- Deduct the $30 fee FROM the user's balance
        UPDATE user
        SET balance = balance - 30
        WHERE id = NEW.userid;
    END IF;

END$$

DELIMITER ;


DELIMITER ;


-- INSERT sample users INTO the user TABLE
INSERT INTO user (name, balance) VALUES ('Alice', 500.00);
INSERT INTO user (name, balance) VALUES ('Bob', 1000.00);
INSERT INTO user (name, balance) VALUES ('Charlie', 50.00);
INSERT INTO user (name, balance) VALUES ('Diana', 0.00);
INSERT INTO user (name, balance) VALUES ('Eve', 250.00);

INSERT INTO transactions (userid, amount)  VALUES (1,-300);
