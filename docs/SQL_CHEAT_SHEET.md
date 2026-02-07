# SQL Quick Reference Cheat Sheet

## Table of Contents
- [Database Operations](#database-operations)
- [Table Operations](#table-operations)
- [Data Manipulation](#data-manipulation)
- [Querying Data](#querying-data)
- [Joins](#joins)
- [Aggregate Functions](#aggregate-functions)
- [Subqueries](#subqueries)
- [String Functions](#string-functions)
- [Date Functions](#date-functions)
- [Window Functions](#window-functions)
- [Transactions](#transactions)
- [Indexes](#indexes)
- [Views](#views)
- [Stored Procedures](#stored-procedures)
- [Triggers](#triggers)

---

## Database Operations

### Create Database
```sql
CREATE DATABASE database_name;
```

### Use Database
```sql
USE database_name;
```

### Show Databases
```sql
SHOW DATABASES;
```

### Drop Database
```sql
DROP DATABASE database_name;
```

---

## Table Operations

### Create Table
```sql
CREATE TABLE table_name (
    column1 datatype PRIMARY KEY,
    column2 datatype NOT NULL,
    column3 datatype DEFAULT value,
    column4 datatype UNIQUE,
    FOREIGN KEY (column) REFERENCES other_table(column)
);
```

### Common Data Types
```sql
-- Numeric
INT, BIGINT, SMALLINT, TINYINT
DECIMAL(p,s), NUMERIC(p,s)
FLOAT, DOUBLE

-- String
CHAR(n), VARCHAR(n)
TEXT, MEDIUMTEXT, LONGTEXT

-- Date/Time
DATE, TIME, DATETIME, TIMESTAMP
YEAR

-- Boolean
BOOLEAN (TINYINT(1))

-- Binary
BLOB, MEDIUMBLOB, LONGBLOB
```

### Modify Table
```sql
-- Add column
ALTER TABLE table_name ADD column_name datatype;

-- Drop column
ALTER TABLE table_name DROP COLUMN column_name;

-- Modify column
ALTER TABLE table_name MODIFY COLUMN column_name new_datatype;

-- Rename column
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;

-- Rename table
ALTER TABLE old_table_name RENAME TO new_table_name;
```

### Drop Table
```sql
DROP TABLE table_name;
```

### Show Tables
```sql
SHOW TABLES;
```

### Describe Table
```sql
DESCRIBE table_name;
-- or
SHOW COLUMNS FROM table_name;
```

---

## Data Manipulation

### INSERT - Add new rows
```sql
-- Insert single row
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);

-- Insert multiple rows
INSERT INTO table_name (column1, column2, column3)
VALUES 
    (value1a, value2a, value3a),
    (value1b, value2b, value3b),
    (value1c, value2c, value3c);

-- Insert from another table
INSERT INTO table_name (column1, column2)
SELECT column1, column2 FROM other_table
WHERE condition;
```

### UPDATE - Modify existing rows
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

-- Update with calculation
UPDATE table_name
SET price = price * 1.1
WHERE category = 'electronics';
```

### DELETE - Remove rows
```sql
DELETE FROM table_name
WHERE condition;

-- Delete all rows (but keep table structure)
DELETE FROM table_name;

-- Faster delete (cannot be rolled back)
TRUNCATE TABLE table_name;
```

---

## Querying Data

### Basic SELECT
```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Select with alias
SELECT column1 AS alias1, column2 AS alias2
FROM table_name;
```

### WHERE Clause
```sql
SELECT * FROM table_name
WHERE condition;

-- Operators: =, !=, <, >, <=, >=, <>, BETWEEN, LIKE, IN, IS NULL
```

### WHERE Examples
```sql
-- Equality
WHERE age = 25

-- Comparison
WHERE salary > 50000

-- Range
WHERE age BETWEEN 18 AND 65

-- Pattern matching
WHERE name LIKE 'J%'        -- Starts with J
WHERE name LIKE '%son'      -- Ends with son
WHERE name LIKE '%a%'       -- Contains a
WHERE name LIKE '_a%'       -- Second char is a

-- Multiple values
WHERE country IN ('USA', 'Canada', 'Mexico')

-- NULL checking
WHERE email IS NULL
WHERE email IS NOT NULL

-- Logical operators
WHERE age > 18 AND country = 'USA'
WHERE city = 'NYC' OR city = 'LA'
WHERE NOT (age < 18)
```

### ORDER BY
```sql
-- Ascending (default)
SELECT * FROM table_name
ORDER BY column1;

-- Descending
SELECT * FROM table_name
ORDER BY column1 DESC;

-- Multiple columns
SELECT * FROM table_name
ORDER BY column1 ASC, column2 DESC;
```

### LIMIT
```sql
-- Limit number of rows
SELECT * FROM table_name
LIMIT 10;

-- Offset and limit (skip first 10, get next 20)
SELECT * FROM table_name
LIMIT 10, 20;
-- or
SELECT * FROM table_name
LIMIT 20 OFFSET 10;
```

### DISTINCT
```sql
-- Get unique values
SELECT DISTINCT column1 FROM table_name;

-- Unique combinations
SELECT DISTINCT column1, column2 FROM table_name;
```

---

## Joins

### INNER JOIN
```sql
SELECT t1.column1, t2.column2
FROM table1 t1
INNER JOIN table2 t2 ON t1.id = t2.foreign_id;
```

### LEFT JOIN (LEFT OUTER JOIN)
```sql
SELECT t1.column1, t2.column2
FROM table1 t1
LEFT JOIN table2 t2 ON t1.id = t2.foreign_id;
```

### RIGHT JOIN (RIGHT OUTER JOIN)
```sql
SELECT t1.column1, t2.column2
FROM table1 t1
RIGHT JOIN table2 t2 ON t1.id = t2.foreign_id;
```

### FULL OUTER JOIN (MySQL workaround)
```sql
SELECT * FROM table1
LEFT JOIN table2 ON table1.id = table2.id
UNION
SELECT * FROM table1
RIGHT JOIN table2 ON table1.id = table2.id;
```

### CROSS JOIN
```sql
SELECT * FROM table1
CROSS JOIN table2;
```

### SELF JOIN
```sql
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.id;
```

---

## Aggregate Functions

### Basic Aggregates
```sql
-- Count rows
SELECT COUNT(*) FROM table_name;
SELECT COUNT(column) FROM table_name;
SELECT COUNT(DISTINCT column) FROM table_name;

-- Sum values
SELECT SUM(column) FROM table_name;

-- Average
SELECT AVG(column) FROM table_name;

-- Minimum and Maximum
SELECT MIN(column) FROM table_name;
SELECT MAX(column) FROM table_name;
```

### GROUP BY
```sql
SELECT column1, COUNT(*), AVG(column2)
FROM table_name
GROUP BY column1;

-- Multiple grouping columns
SELECT column1, column2, SUM(column3)
FROM table_name
GROUP BY column1, column2;
```

### HAVING
```sql
-- Filter groups (use after GROUP BY)
SELECT column1, COUNT(*) as count
FROM table_name
GROUP BY column1
HAVING COUNT(*) > 10;

-- HAVING with multiple conditions
SELECT category, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 100 AND COUNT(*) >= 5;
```

---

## Subqueries

### Subquery in WHERE
```sql
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### Subquery with IN
```sql
SELECT * FROM employees
WHERE department_id IN (
    SELECT id FROM departments WHERE location = 'NY'
);
```

### Subquery in FROM (Derived Table)
```sql
SELECT dept_name, avg_salary
FROM (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
) AS dept_avg
JOIN departments ON dept_avg.department_id = departments.id;
```

### Correlated Subquery
```sql
SELECT e1.name, e1.salary
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

### EXISTS
```sql
SELECT * FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.id
);
```

---

## String Functions

```sql
-- Concatenation
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;

-- Length
SELECT LENGTH(column) FROM table_name;

-- Substring
SELECT SUBSTRING(column, start, length) FROM table_name;
SELECT LEFT(column, n) FROM table_name;
SELECT RIGHT(column, n) FROM table_name;

-- Case conversion
SELECT UPPER(column) FROM table_name;
SELECT LOWER(column) FROM table_name;

-- Trim whitespace
SELECT TRIM(column) FROM table_name;
SELECT LTRIM(column) FROM table_name;
SELECT RTRIM(column) FROM table_name;

-- Replace
SELECT REPLACE(column, 'old', 'new') FROM table_name;

-- Position
SELECT POSITION('substring' IN column) FROM table_name;
SELECT LOCATE('substring', column) FROM table_name;
```

---

## Date Functions

```sql
-- Current date/time
SELECT NOW();           -- Current datetime
SELECT CURDATE();       -- Current date
SELECT CURTIME();       -- Current time

-- Extract parts
SELECT YEAR(date_column) FROM table_name;
SELECT MONTH(date_column) FROM table_name;
SELECT DAY(date_column) FROM table_name;
SELECT HOUR(datetime_column) FROM table_name;

-- Date arithmetic
SELECT DATE_ADD(date_column, INTERVAL 7 DAY) FROM table_name;
SELECT DATE_SUB(date_column, INTERVAL 1 MONTH) FROM table_name;

-- Date difference
SELECT DATEDIFF(date1, date2) FROM table_name;
SELECT TIMESTAMPDIFF(MINUTE, datetime1, datetime2) FROM table_name;

-- Format date
SELECT DATE_FORMAT(date_column, '%Y-%m-%d') FROM table_name;
SELECT DATE_FORMAT(datetime_column, '%W, %M %d, %Y %H:%i:%s') FROM table_name;
```

---

## Window Functions

### ROW_NUMBER
```sql
SELECT 
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM employees;
```

### RANK and DENSE_RANK
```sql
SELECT 
    name,
    score,
    RANK() OVER (ORDER BY score DESC) as rank,
    DENSE_RANK() OVER (ORDER BY score DESC) as dense_rank
FROM students;
```

### PARTITION BY
```sql
SELECT 
    department,
    name,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;
```

### Aggregate Window Functions
```sql
SELECT 
    name,
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary,
    salary - AVG(salary) OVER (PARTITION BY department) as diff_from_avg
FROM employees;
```

### LEAD and LAG
```sql
SELECT 
    date,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY date) as prev_day_revenue,
    LEAD(revenue, 1) OVER (ORDER BY date) as next_day_revenue
FROM daily_sales;
```

---

## Transactions

```sql
-- Start transaction
START TRANSACTION;
-- or
BEGIN;

-- Execute queries
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit changes
COMMIT;

-- Or rollback if error
ROLLBACK;
```

### Transaction with Savepoint
```sql
START TRANSACTION;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
SAVEPOINT sp1;

UPDATE accounts SET balance = balance + 100 WHERE id = 2;
SAVEPOINT sp2;

-- Rollback to savepoint
ROLLBACK TO sp1;

COMMIT;
```

---

## Indexes

### Create Index
```sql
-- Single column index
CREATE INDEX idx_name ON table_name (column);

-- Multiple column index
CREATE INDEX idx_name ON table_name (column1, column2);

-- Unique index
CREATE UNIQUE INDEX idx_name ON table_name (column);
```

### Drop Index
```sql
DROP INDEX idx_name ON table_name;
```

### Show Indexes
```sql
SHOW INDEX FROM table_name;
```

---

## Views

### Create View
```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

### Use View
```sql
SELECT * FROM view_name;
```

### Update View
```sql
CREATE OR REPLACE VIEW view_name AS
SELECT new_columns
FROM table_name
WHERE new_condition;
```

### Drop View
```sql
DROP VIEW view_name;
```

---

## Stored Procedures

### Create Procedure
```sql
DELIMITER //
CREATE PROCEDURE procedure_name(IN param1 INT, OUT param2 VARCHAR(100))
BEGIN
    -- SQL statements
    SELECT column INTO param2
    FROM table_name
    WHERE id = param1;
END //
DELIMITER ;
```

### Call Procedure
```sql
CALL procedure_name(value1, @result);
SELECT @result;
```

### Drop Procedure
```sql
DROP PROCEDURE procedure_name;
```

---

## Triggers

### Create Trigger
```sql
DELIMITER //
CREATE TRIGGER trigger_name
BEFORE INSERT ON table_name
FOR EACH ROW
BEGIN
    -- Trigger logic
    SET NEW.created_at = NOW();
END //
DELIMITER ;
```

### Trigger Types
- `BEFORE INSERT`, `AFTER INSERT`
- `BEFORE UPDATE`, `AFTER UPDATE`
- `BEFORE DELETE`, `AFTER DELETE`

### Drop Trigger
```sql
DROP TRIGGER trigger_name;
```

---

## CASE Expression

### Simple CASE
```sql
SELECT 
    name,
    CASE grade
        WHEN 'A' THEN 'Excellent'
        WHEN 'B' THEN 'Good'
        WHEN 'C' THEN 'Average'
        ELSE 'Needs Improvement'
    END AS performance
FROM students;
```

### Searched CASE
```sql
SELECT 
    name,
    salary,
    CASE
        WHEN salary > 100000 THEN 'High'
        WHEN salary > 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_range
FROM employees;
```

---

## Set Operations

### UNION
```sql
-- Combine results, remove duplicates
SELECT column FROM table1
UNION
SELECT column FROM table2;

-- Keep duplicates
SELECT column FROM table1
UNION ALL
SELECT column FROM table2;
```

### INTERSECT (MySQL 8.0+)
```sql
SELECT column FROM table1
INTERSECT
SELECT column FROM table2;
```

### EXCEPT (MySQL workaround)
```sql
SELECT column FROM table1
WHERE column NOT IN (SELECT column FROM table2);
```

---

## Common Table Expressions (CTEs)

```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT * FROM cte_name
WHERE another_condition;
```

### Recursive CTE
```sql
WITH RECURSIVE cte_name AS (
    -- Base case
    SELECT id, name, parent_id, 1 as level
    FROM table_name
    WHERE parent_id IS NULL
    
    UNION ALL
    
    -- Recursive case
    SELECT t.id, t.name, t.parent_id, c.level + 1
    FROM table_name t
    JOIN cte_name c ON t.parent_id = c.id
)
SELECT * FROM cte_name;
```

---

## Best Practices

1. **Use appropriate data types** - Choose the smallest type that fits your data
2. **Index strategically** - Index columns used in WHERE, JOIN, ORDER BY
3. **Avoid SELECT *** - Specify only needed columns
4. **Use LIMIT** - When you don't need all rows
5. **Use transactions** - For multiple related updates
6. **Normalize your database** - Reduce redundancy
7. **Use meaningful names** - For tables, columns, and constraints
8. **Comment complex queries** - Explain non-obvious logic
9. **Test with small datasets first** - Before running on production data
10. **Back up before major changes** - Always have a recovery plan

---

## Performance Tips

- **Use indexes** on columns in WHERE, JOIN, ORDER BY clauses
- **Avoid functions in WHERE** - They prevent index usage
- **Use EXPLAIN** to analyze query performance
- **Limit returned rows** with WHERE and LIMIT
- **Use EXISTS instead of IN** for large subqueries
- **Avoid wildcard at start** of LIKE pattern (`%abc` prevents index use)
- **Use appropriate JOIN types** - Don't use LEFT JOIN when INNER JOIN suffices
- **Batch operations** instead of row-by-row updates
- **Optimize subqueries** - Consider using JOINs or EXISTS
- **Keep statistics updated** - Run ANALYZE TABLE regularly

---

**For more details, visit the [MySQL Documentation](https://dev.mysql.com/doc/)**
