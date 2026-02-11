# SQL Fundamentals - Reorganized Lab Guide

## 📚 Table of Contents

1. [Create Tables](#1-create-tables)
2. [Single Table Query](#2-single-table-query)
3. [DISTINCT](#3-distinct)
4. [ORDER BY](#4-order-by)
5. [Foreign Key](#5-foreign-key)
6. [Multi Table](#6-multi-table)
7. [Aggregate Function](#7-aggregate-function)
8. [GROUP BY](#8-group-by)
9. [HAVING](#9-having)
10. [Set Operation](#10-set-operation)

---

## 🎯 Overview

This comprehensive guide covers fundamental SQL concepts in a logical progression, from basic table creation to advanced set operations. Each section builds upon the previous one, providing a structured learning path for database management.

**Prerequisites:**
- MySQL or MariaDB server installed and running
- Basic understanding of relational database concepts
- Access to a SQL client (command line, MySQL Workbench, etc.)

---

## 1. Create Tables

### 1.1 Introduction to Database and Table Creation

A database is a container that holds related tables. Before creating tables, you must first create and select a database.

### 1.2 Create a Database

```sql
-- Create a new database
CREATE DATABASE sql_fundamentals;

-- Switch to the database
USE sql_fundamentals;
```

**Note:** Database names are case-sensitive on some systems. Use lowercase for consistency.

### 1.3 Understanding Data Types

Common MySQL data types:
- `INT`: Integer numbers
- `DECIMAL(p,s)`: Fixed-point numbers (e.g., DECIMAL(10,2) for prices)
- `VARCHAR(n)`: Variable-length strings up to n characters
- `CHAR(n)`: Fixed-length strings
- `DATE`: Date values (YYYY-MM-DD)
- `DATETIME`: Date and time values
- `TEXT`: Long text fields

### 1.4 Create Your First Table

```sql
-- Create a product table
CREATE TABLE product(
    pname        VARCHAR(20) PRIMARY KEY,  -- Product name (unique identifier)
    price        DECIMAL(10,2),            -- Price with 2 decimal places
    category     VARCHAR(20),              -- Product category
    manufacturer VARCHAR(20) NOT NULL      -- Manufacturer (required field)
);
```

**Key Concepts:**
- `PRIMARY KEY`: Ensures each value is unique and not null
- `NOT NULL`: Field cannot be empty
- `DECIMAL(10,2)`: Stores numbers with up to 10 digits, 2 after decimal point
- `VARCHAR(20)`: Variable-length string up to 20 characters

### 1.5 Insert Sample Data

```sql
-- Insert sample products
INSERT INTO product VALUES('Gizmo', 19.99, 'Gadgets', 'GizmoWorks');
INSERT INTO product VALUES('PowerGizmo', 29.99, 'Gadgets', 'GizmoWorks');
INSERT INTO product VALUES('MultiTouch', 203.99, 'Household', 'Hitachi');
INSERT INTO product VALUES('SingleTouch', 149.99, 'Photography', 'Canon');
INSERT INTO product VALUES('SuperGizmo', 49.99, 'Gadgets', 'GizmoWorks');
INSERT INTO product VALUES('UltraTouch', 99.99, 'Photography', 'Nikon');
```

### 1.6 Verify Your Data

```sql
-- View all products
SELECT * FROM product;
```

**Expected Output:**
```
+-------------+--------+-------------+--------------+
| pname       | price  | category    | manufacturer |
+-------------+--------+-------------+--------------+
| Gizmo       |  19.99 | Gadgets     | GizmoWorks   |
| PowerGizmo  |  29.99 | Gadgets     | GizmoWorks   |
| MultiTouch  | 203.99 | Household   | Hitachi      |
| SingleTouch | 149.99 | Photography | Canon        |
| SuperGizmo  |  49.99 | Gadgets     | GizmoWorks   |
| UltraTouch  |  99.99 | Photography | Nikon        |
+-------------+--------+-------------+--------------+
```

### 1.7 Additional Table Creation Examples

```sql
-- Create a company table
CREATE TABLE company(
    cname    VARCHAR(20) PRIMARY KEY,
    city     VARCHAR(20),
    country  VARCHAR(20)
);

-- Insert company data
INSERT INTO company VALUES('GizmoWorks', 'Seattle', 'USA');
INSERT INTO company VALUES('Canon', 'Tokyo', 'Japan');
INSERT INTO company VALUES('Hitachi', 'Osaka', 'Japan');
INSERT INTO company VALUES('Nikon', 'Tokyo', 'Japan');
```

### 1.8 Practice Exercises

**Exercise 1:** Create a `customer` table with the following columns:
- `customer_id` (INT, PRIMARY KEY)
- `first_name` (VARCHAR(50), NOT NULL)
- `last_name` (VARCHAR(50), NOT NULL)
- `email` (VARCHAR(100))
- `city` (VARCHAR(50))

**Exercise 2:** Create an `orders` table with columns for order_id, customer_id, order_date, and total_amount.

---

## 2. Single Table Query

### 2.1 Introduction to SELECT

The SELECT statement is used to query data from a database. The simplest form retrieves all columns from a table.

### 2.2 Basic SELECT Syntax

```sql
SELECT column1, column2, ...
FROM table_name;
```

### 2.3 Retrieve All Columns

```sql
-- Select all columns from product table
SELECT * FROM product;
```

**Note:** While `SELECT *` is convenient for exploration, it's better to explicitly list columns in production queries for clarity and performance.

### 2.4 Select Specific Columns

```sql
-- Select only product name and price
SELECT pname, price FROM product;

-- Select product name and category
SELECT pname, category FROM product;
```

### 2.5 WHERE Clause - Filtering Data

The WHERE clause filters records based on specified conditions.

```sql
-- Find products in the Gadgets category
SELECT * FROM product
WHERE category = 'Gadgets';

-- Find products priced over $50
SELECT pname, price FROM product
WHERE price > 50;

-- Find products from GizmoWorks
SELECT * FROM product
WHERE manufacturer = 'GizmoWorks';
```

### 2.6 Comparison Operators

```sql
-- Equal to
SELECT * FROM product WHERE category = 'Photography';

-- Greater than
SELECT * FROM product WHERE price > 100;

-- Less than or equal to
SELECT * FROM product WHERE price <= 50;

-- Not equal to
SELECT * FROM product WHERE category != 'Gadgets';
-- or
SELECT * FROM product WHERE category <> 'Gadgets';
```

### 2.7 Logical Operators (AND, OR, NOT)

```sql
-- AND: Both conditions must be true
SELECT * FROM product
WHERE category = 'Gadgets' AND price < 30;

-- OR: At least one condition must be true
SELECT * FROM product
WHERE category = 'Gadgets' OR category = 'Photography';

-- NOT: Negates a condition
SELECT * FROM product
WHERE NOT category = 'Gadgets';
```

### 2.8 BETWEEN Operator

```sql
-- Find products priced between $20 and $100
SELECT * FROM product
WHERE price BETWEEN 20 AND 100;
```

### 2.9 IN Operator

```sql
-- Find products in specific categories
SELECT * FROM product
WHERE category IN ('Gadgets', 'Photography');

-- Find products from specific manufacturers
SELECT * FROM product
WHERE manufacturer IN ('Canon', 'Nikon');
```

### 2.10 LIKE Operator - Pattern Matching

```sql
-- Find products whose name contains 'Gizmo'
SELECT * FROM product
WHERE pname LIKE '%Gizmo%';

-- Find products starting with 'Multi'
SELECT * FROM product
WHERE pname LIKE 'Multi%';

-- Find products ending with 'Touch'
SELECT * FROM product
WHERE pname LIKE '%Touch';
```

**Wildcards:**
- `%` : Matches any sequence of characters
- `_` : Matches a single character

### 2.11 NULL Values

```sql
-- Find products with no price specified
SELECT * FROM product
WHERE price IS NULL;

-- Find products with a price specified
SELECT * FROM product
WHERE price IS NOT NULL;
```

### 2.12 Practice Exercises

**Exercise 1:** Write a query to find all products that cost more than $100.

**Exercise 2:** Write a query to find all products in the 'Photography' category made by Canon.

**Exercise 3:** Write a query to find all products whose name starts with 'Super'.

---

## 3. DISTINCT

### 3.1 Introduction to DISTINCT

The DISTINCT keyword is used to return only unique (different) values, eliminating duplicate rows from the result set.

### 3.2 Basic DISTINCT Syntax

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

### 3.3 Find Unique Categories

```sql
-- Without DISTINCT - shows duplicates
SELECT category FROM product;

-- With DISTINCT - shows only unique categories
SELECT DISTINCT category FROM product;
```

**Output without DISTINCT:**
```
+-------------+
| category    |
+-------------+
| Gadgets     |
| Gadgets     |
| Household   |
| Photography |
| Gadgets     |
| Photography |
+-------------+
```

**Output with DISTINCT:**
```
+-------------+
| category    |
+-------------+
| Gadgets     |
| Household   |
| Photography |
+-------------+
```

### 3.4 Find Unique Manufacturers

```sql
-- Get list of unique manufacturers
SELECT DISTINCT manufacturer FROM product;
```

### 3.5 DISTINCT with Multiple Columns

When you use DISTINCT with multiple columns, it returns unique combinations of those columns.

```sql
-- Get unique combinations of category and manufacturer
SELECT DISTINCT category, manufacturer FROM product;
```

### 3.6 COUNT with DISTINCT

```sql
-- Count how many different categories exist
SELECT COUNT(DISTINCT category) AS unique_categories FROM product;

-- Count how many different manufacturers exist
SELECT COUNT(DISTINCT manufacturer) AS unique_manufacturers FROM product;
```

### 3.7 Important Notes About DISTINCT

**Note 1:** DISTINCT applies to all selected columns, not just one.

```sql
-- This finds unique combinations of pname AND category
SELECT DISTINCT pname, category FROM product;
```

**Note 2:** DISTINCT can affect performance on large tables. Use it only when necessary.

**Note 3:** DISTINCT removes only exact duplicate rows. NULL values are considered equal for DISTINCT purposes.

### 3.8 Practice Exercises

**Exercise 1:** Find all unique cities where companies are located.

**Exercise 2:** Count how many different countries have companies in the database.

**Exercise 3:** Find unique combinations of category and price from the product table.

---

## 4. ORDER BY

### 4.1 Introduction to ORDER BY

The ORDER BY clause is used to sort the result set in ascending or descending order.

### 4.2 Basic ORDER BY Syntax

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

- `ASC`: Ascending order (default)
- `DESC`: Descending order

### 4.3 Sort by Single Column

```sql
-- Sort products by price (ascending - lowest to highest)
SELECT * FROM product
ORDER BY price;

-- Sort products by price (descending - highest to lowest)
SELECT * FROM product
ORDER BY price DESC;

-- Sort products by name (alphabetically)
SELECT * FROM product
ORDER BY pname;
```

### 4.4 Sort by Multiple Columns

```sql
-- Sort by category first, then by price within each category
SELECT * FROM product
ORDER BY category, price;

-- Sort by category (ascending) and price (descending)
SELECT * FROM product
ORDER BY category ASC, price DESC;
```

### 4.5 Combining WHERE and ORDER BY

```sql
-- Find Gadgets and sort by price
SELECT * FROM product
WHERE category = 'Gadgets'
ORDER BY price;

-- Find products over $50 and sort by manufacturer
SELECT * FROM product
WHERE price > 50
ORDER BY manufacturer;
```

### 4.6 ORDER BY with Column Position

You can use column position numbers instead of names:

```sql
-- Sort by the first column in SELECT list
SELECT pname, price, category FROM product
ORDER BY 1;  -- Orders by pname

-- Sort by the second column
SELECT pname, price, category FROM product
ORDER BY 2;  -- Orders by price
```

**Note:** Using column positions is less readable and not recommended in production code.

### 4.7 Combining DISTINCT and ORDER BY

```sql
-- Get unique categories and sort them
SELECT DISTINCT category FROM product
ORDER BY category;

-- Get unique manufacturers and sort them
SELECT DISTINCT manufacturer FROM product
ORDER BY manufacturer;
```

### 4.8 Important Rule: ORDER BY with DISTINCT

When using DISTINCT, you can only ORDER BY columns that appear in the SELECT clause.

```sql
-- This works - pname is in the SELECT list
SELECT DISTINCT category FROM product
ORDER BY category;

-- This will produce an ERROR - pname is not in the SELECT list
-- SELECT DISTINCT category FROM product
-- ORDER BY pname;
```

**Key Learning:** When using DISTINCT, you can only ORDER BY columns that are in the SELECT clause.

### 4.9 NULL Values in ORDER BY

- `ASC`: NULL values appear first
- `DESC`: NULL values appear last

```sql
-- Sort with NULLs first (default for ASC)
SELECT * FROM product
ORDER BY price ASC;

-- Sort with NULLs last (default for DESC)
SELECT * FROM product
ORDER BY price DESC;
```

### 4.10 Practice Exercises

**Exercise 1:** List all products sorted by manufacturer name, then by price (descending) within each manufacturer.

**Exercise 2:** Find all products in the Photography category and sort them by price from highest to lowest.

**Exercise 3:** List unique categories sorted alphabetically.

---

## 5. Foreign Key

### 5.1 Introduction to Foreign Keys

A foreign key is a field (or collection of fields) in one table that refers to the primary key in another table. Foreign keys are used to establish and enforce relationships between tables, ensuring referential integrity.

### 5.2 Why Use Foreign Keys?

**Benefits:**
- **Data Integrity**: Prevents invalid data from being inserted
- **Referential Integrity**: Ensures relationships between tables remain consistent
- **Cascading Actions**: Automatically handle related records when parent records are updated or deleted
- **Documentation**: Makes database relationships explicit and clear

### 5.3 Creating Tables with Foreign Keys

Let's create a complete example with companies and products:

```sql
-- First, create the parent table (company)
CREATE TABLE company(
    cname    VARCHAR(20) PRIMARY KEY,
    city     VARCHAR(20),
    country  VARCHAR(20)
);

-- Then, create the child table (product) with a foreign key
CREATE TABLE product_fk(
    pname        VARCHAR(20) PRIMARY KEY,
    price        DECIMAL(10,2),
    category     VARCHAR(20),
    manufacturer VARCHAR(20) NOT NULL,
    FOREIGN KEY (manufacturer) REFERENCES company(cname)
);
```

**Key Points:**
- The `company` table must be created first (parent table)
- The `product_fk` table references `company` through the manufacturer field
- The foreign key ensures that every manufacturer in product_fk must exist in company

### 5.4 Insert Data with Foreign Key Constraints

```sql
-- First, insert companies (parent records)
INSERT INTO company VALUES('GizmoWorks', 'Seattle', 'USA');
INSERT INTO company VALUES('Canon', 'Tokyo', 'Japan');
INSERT INTO company VALUES('Hitachi', 'Osaka', 'Japan');

-- Now insert products (child records)
INSERT INTO product_fk VALUES('Gizmo', 19.99, 'Gadgets', 'GizmoWorks');
INSERT INTO product_fk VALUES('MultiTouch', 203.99, 'Household', 'Hitachi');
INSERT INTO product_fk VALUES('SingleTouch', 149.99, 'Photography', 'Canon');
```

### 5.5 Foreign Key Constraint Violations

```sql
-- This will FAIL because 'UnknownCompany' doesn't exist in company table
-- INSERT INTO product_fk VALUES('BadProduct', 99.99, 'Gadgets', 'UnknownCompany');
-- Error: Cannot add or update a child row: a foreign key constraint fails
```

**Error Prevention:** Always ensure parent records exist before inserting child records.

### 5.6 CASCADE Options

CASCADE options define what happens to child records when parent records are modified or deleted.

#### 5.6.1 ON DELETE CASCADE

```sql
-- Create tables with ON DELETE CASCADE
CREATE TABLE company_cascade(
    cname    VARCHAR(20) PRIMARY KEY,
    city     VARCHAR(20),
    country  VARCHAR(20)
);

CREATE TABLE product_cascade(
    pname        VARCHAR(20) PRIMARY KEY,
    price        DECIMAL(10,2),
    category     VARCHAR(20),
    manufacturer VARCHAR(20) NOT NULL,
    FOREIGN KEY (manufacturer) REFERENCES company_cascade(cname)
        ON DELETE CASCADE
);
```

**Behavior:** When a company is deleted, all its products are automatically deleted.

```sql
-- Insert data
INSERT INTO company_cascade VALUES('TempCompany', 'Boston', 'USA');
INSERT INTO product_cascade VALUES('TempProduct', 50.00, 'Test', 'TempCompany');

-- Delete company - product is also deleted automatically
DELETE FROM company_cascade WHERE cname = 'TempCompany';
```

#### 5.6.2 ON UPDATE CASCADE

```sql
CREATE TABLE product_update_cascade(
    pname        VARCHAR(20) PRIMARY KEY,
    price        DECIMAL(10,2),
    category     VARCHAR(20),
    manufacturer VARCHAR(20) NOT NULL,
    FOREIGN KEY (manufacturer) REFERENCES company_cascade(cname)
        ON UPDATE CASCADE
);
```

**Behavior:** When a company name is updated, all product manufacturer references are automatically updated.

#### 5.6.3 Other CASCADE Options

- `ON DELETE SET NULL`: Sets foreign key to NULL when parent is deleted
- `ON DELETE RESTRICT`: Prevents deletion of parent if children exist (default)
- `ON UPDATE RESTRICT`: Prevents update of parent key if children exist (default)
- `ON DELETE NO ACTION`: Similar to RESTRICT
- `ON UPDATE NO ACTION`: Similar to RESTRICT

### 5.7 Viewing Foreign Key Constraints

```sql
-- Show table structure including foreign keys
SHOW CREATE TABLE product_fk;

-- Show all foreign keys in current database
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'sql_fundamentals'
    AND REFERENCED_TABLE_NAME IS NOT NULL;
```

### 5.8 Multiple Foreign Keys

A table can have multiple foreign keys referencing different tables:

```sql
-- Create an orders table with multiple foreign keys
CREATE TABLE orders(
    order_id     INT PRIMARY KEY AUTO_INCREMENT,
    customer_id  INT NOT NULL,
    product_name VARCHAR(20) NOT NULL,
    order_date   DATE,
    quantity     INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_name) REFERENCES product_fk(pname)
);
```

### 5.9 Composite Foreign Keys

Foreign keys can reference composite primary keys:

```sql
-- Example with composite primary key
CREATE TABLE enrollment(
    student_id  INT,
    course_id   INT,
    semester    VARCHAR(20),
    grade       CHAR(2),
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (course_id) REFERENCES course(id)
);
```

### 5.10 Practice Exercises

**Exercise 1:** Create a `customer` table and an `orders` table where orders reference customers through a foreign key.

**Exercise 2:** Add foreign key constraints to existing tables (if they don't have them).

**Exercise 3:** Create tables with ON DELETE CASCADE and test the cascading behavior.

**Exercise 4:** Try to insert a record with an invalid foreign key reference and observe the error message.

---

## 6. Multi Table

### 6.1 Introduction to Multi-Table Queries

Real-world databases typically have multiple related tables. Multi-table queries allow us to combine data from two or more tables to answer complex questions.

### 6.2 Understanding JOINs

JOINs are used to combine rows from two or more tables based on a related column between them.

**Types of JOINs:**
- **INNER JOIN**: Returns records that have matching values in both tables
- **LEFT JOIN (LEFT OUTER JOIN)**: Returns all records from the left table and matched records from the right
- **RIGHT JOIN (RIGHT OUTER JOIN)**: Returns all records from the right table and matched records from the left
- **CROSS JOIN**: Returns the Cartesian product of both tables

### 6.3 Preparing Sample Data

```sql
-- Use our existing product and company tables
-- Ensure data is present
SELECT * FROM product;
SELECT * FROM company;
```

### 6.4 INNER JOIN

INNER JOIN returns only the rows where there is a match in both tables.

```sql
-- Join products with their company information
SELECT p.pname, p.price, p.category, c.city, c.country
FROM product p
INNER JOIN company c ON p.manufacturer = c.cname;
```

**Explanation:**
- `p` and `c` are table aliases for easier reference
- `ON p.manufacturer = c.cname` specifies the join condition
- Only products with a matching company are returned

### 6.5 Alternative JOIN Syntax

```sql
-- Using USING clause (when column names are identical)
SELECT p.pname, p.price, c.city, c.country
FROM product p
INNER JOIN company c USING (cname);

-- Traditional comma syntax (older style, not recommended)
SELECT p.pname, p.price, c.city, c.country
FROM product p, company c
WHERE p.manufacturer = c.cname;
```

### 6.6 LEFT JOIN (LEFT OUTER JOIN)

LEFT JOIN returns all records from the left table, and matched records from the right table. If there's no match, NULL values are returned for the right table.

```sql
-- Get all products, including those without a matching company
SELECT p.pname, p.price, p.manufacturer, c.city, c.country
FROM product p
LEFT JOIN company c ON p.manufacturer = c.cname;
```

**Use Case:** Find products that don't have a company entry:
```sql
SELECT p.pname, p.manufacturer
FROM product p
LEFT JOIN company c ON p.manufacturer = c.cname
WHERE c.cname IS NULL;
```

### 6.7 RIGHT JOIN (RIGHT OUTER JOIN)

RIGHT JOIN returns all records from the right table, and matched records from the left table.

```sql
-- Get all companies, including those without products
SELECT c.cname, c.city, p.pname, p.price
FROM product p
RIGHT JOIN company c ON p.manufacturer = c.cname;
```

**Use Case:** Find companies that don't have any products:
```sql
SELECT c.cname, c.city
FROM product p
RIGHT JOIN company c ON p.manufacturer = c.cname
WHERE p.pname IS NULL;
```

### 6.8 Joining More Than Two Tables

```sql
-- Create an additional table for demonstration
CREATE TABLE sales(
    sale_id      INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(20),
    sale_date    DATE,
    quantity     INT,
    FOREIGN KEY (product_name) REFERENCES product(pname)
);

-- Insert sample sales data
INSERT INTO sales (product_name, sale_date, quantity) 
VALUES ('Gizmo', '2024-01-15', 5);
INSERT INTO sales (product_name, sale_date, quantity) 
VALUES ('MultiTouch', '2024-01-16', 2);
INSERT INTO sales (product_name, sale_date, quantity) 
VALUES ('Gizmo', '2024-01-17', 3);

-- Join three tables
SELECT 
    s.sale_id,
    s.sale_date,
    p.pname,
    p.category,
    c.cname AS manufacturer,
    c.city,
    s.quantity
FROM sales s
INNER JOIN product p ON s.product_name = p.pname
INNER JOIN company c ON p.manufacturer = c.cname;
```

### 6.9 Self-Join

A self-join is when a table is joined with itself. This is useful for hierarchical data.

```sql
-- Create an employee table with manager references
CREATE TABLE employee(
    emp_id   INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employee(emp_id)
);

-- Insert sample data
INSERT INTO employee VALUES(1, 'Alice', NULL);      -- CEO, no manager
INSERT INTO employee VALUES(2, 'Bob', 1);           -- Reports to Alice
INSERT INTO employee VALUES(3, 'Charlie', 1);       -- Reports to Alice
INSERT INTO employee VALUES(4, 'David', 2);         -- Reports to Bob
INSERT INTO employee VALUES(5, 'Eve', 2);           -- Reports to Bob

-- Self-join to show employees with their managers
SELECT 
    e.emp_name AS employee,
    m.emp_name AS manager
FROM employee e
LEFT JOIN employee m ON e.manager_id = m.emp_id;
```

### 6.10 CROSS JOIN

CROSS JOIN produces a Cartesian product - every row from the first table combined with every row from the second table.

```sql
-- Get all possible combinations of products and companies
SELECT p.pname, c.cname
FROM product p
CROSS JOIN company c;
```

**Warning:** CROSS JOIN can produce very large result sets. Use with caution.

### 6.11 Filtering Multi-Table Results

```sql
-- Find products made by Japanese companies
SELECT p.pname, p.price, c.cname, c.country
FROM product p
INNER JOIN company c ON p.manufacturer = c.cname
WHERE c.country = 'Japan';

-- Find products in Gadgets category with company in USA
SELECT p.pname, p.price, c.cname, c.city
FROM product p
INNER JOIN company c ON p.manufacturer = c.cname
WHERE p.category = 'Gadgets' AND c.country = 'USA';
```

### 6.12 Combining Joins and Sorting

```sql
-- Get products with companies, sorted by country and price
SELECT p.pname, p.price, c.cname, c.country
FROM product p
INNER JOIN company c ON p.manufacturer = c.cname
ORDER BY c.country, p.price DESC;
```

### 6.13 Practice Exercises

**Exercise 1:** Write a query to find all products along with their manufacturer's city and country.

**Exercise 2:** Find all companies that manufacture products in the 'Photography' category.

**Exercise 3:** List all products made by companies in Japan, sorted by price.

**Exercise 4:** Create a query that shows employee names along with their manager names (use self-join).

**Exercise 5:** Find companies that don't have any products in the database.

---

## 7. Aggregate Function

### 7.1 Introduction to Aggregate Functions

Aggregate functions perform a calculation on a set of values and return a single value. They are essential for data analysis and reporting.

**Common Aggregate Functions:**
- `COUNT()`: Returns the number of rows
- `SUM()`: Returns the sum of values
- `AVG()`: Returns the average of values
- `MAX()`: Returns the maximum value
- `MIN()`: Returns the minimum value

### 7.2 COUNT Function

```sql
-- Count total number of products
SELECT COUNT(*) AS total_products FROM product;

-- Count products in a specific category
SELECT COUNT(*) AS gadget_count 
FROM product 
WHERE category = 'Gadgets';

-- Count non-NULL values in a column
SELECT COUNT(price) AS products_with_price FROM product;

-- Count distinct values
SELECT COUNT(DISTINCT category) AS unique_categories FROM product;
SELECT COUNT(DISTINCT manufacturer) AS unique_manufacturers FROM product;
```

**COUNT(*) vs COUNT(column):**
- `COUNT(*)`: Counts all rows, including those with NULL values
- `COUNT(column)`: Counts only non-NULL values in that column

### 7.3 SUM Function

```sql
-- Calculate total value of all products
SELECT SUM(price) AS total_value FROM product;

-- Calculate total value of products in a specific category
SELECT SUM(price) AS gadgets_total_value 
FROM product 
WHERE category = 'Gadgets';

-- Sum with calculation
SELECT SUM(price * 1.1) AS total_with_tax FROM product;
```

**Note:** SUM() ignores NULL values.

### 7.4 AVG Function

```sql
-- Calculate average product price
SELECT AVG(price) AS average_price FROM product;

-- Calculate average price by category
SELECT AVG(price) AS avg_gadget_price 
FROM product 
WHERE category = 'Gadgets';

-- Round the average to 2 decimal places
SELECT ROUND(AVG(price), 2) AS avg_price FROM product;
```

**Note:** AVG() ignores NULL values. To include NULLs as zeros, use: `AVG(COALESCE(price, 0))`

### 7.5 MAX and MIN Functions

```sql
-- Find highest priced product
SELECT MAX(price) AS highest_price FROM product;

-- Find lowest priced product
SELECT MIN(price) AS lowest_price FROM product;

-- Find price range
SELECT 
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    MAX(price) - MIN(price) AS price_range
FROM product;
```

**Note:** MAX() and MIN() work with numbers, dates, and strings (alphabetical order).

### 7.6 Multiple Aggregate Functions

```sql
-- Get comprehensive statistics
SELECT 
    COUNT(*) AS total_products,
    COUNT(DISTINCT category) AS unique_categories,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    AVG(price) AS avg_price,
    SUM(price) AS total_value
FROM product;
```

### 7.7 Aggregates with WHERE Clause

```sql
-- Statistics for Gadgets category only
SELECT 
    COUNT(*) AS count,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    AVG(price) AS avg_price
FROM product
WHERE category = 'Gadgets';
```

### 7.8 Aggregates with Joins

```sql
-- Count products by country
SELECT 
    c.country,
    COUNT(p.pname) AS product_count,
    AVG(p.price) AS avg_price
FROM company c
LEFT JOIN product p ON c.cname = p.manufacturer
GROUP BY c.country;
```

### 7.9 String Aggregation

```sql
-- MySQL specific: GROUP_CONCAT
SELECT 
    category,
    GROUP_CONCAT(pname ORDER BY pname SEPARATOR ', ') AS products
FROM product
GROUP BY category;
```

### 7.10 Conditional Aggregation

```sql
-- Count products above and below average price
SELECT 
    COUNT(CASE WHEN price > (SELECT AVG(price) FROM product) 
          THEN 1 END) AS above_avg_count,
    COUNT(CASE WHEN price <= (SELECT AVG(price) FROM product) 
          THEN 1 END) AS below_avg_count
FROM product;
```

### 7.11 NULL Handling in Aggregates

```sql
-- Demonstrate NULL handling
CREATE TABLE test_nulls(
    id INT,
    value DECIMAL(10,2)
);

INSERT INTO test_nulls VALUES(1, 10.00);
INSERT INTO test_nulls VALUES(2, 20.00);
INSERT INTO test_nulls VALUES(3, NULL);
INSERT INTO test_nulls VALUES(4, 30.00);

-- Compare different functions with NULL
SELECT 
    COUNT(*) AS count_all,           -- Returns 4
    COUNT(value) AS count_values,    -- Returns 3 (excludes NULL)
    SUM(value) AS sum_values,        -- Returns 60 (excludes NULL)
    AVG(value) AS avg_values         -- Returns 20 (60/3, excludes NULL)
FROM test_nulls;
```

### 7.12 Practice Exercises

**Exercise 1:** Find the total number of products and their total value.

**Exercise 2:** Calculate the average price of products for each manufacturer.

**Exercise 3:** Find the highest and lowest priced products in the Photography category.

**Exercise 4:** Count how many products each company manufactures.

**Exercise 5:** Calculate the average price difference between Gadgets and Photography products.

---

## 8. GROUP BY

### 8.1 Introduction to GROUP BY

The GROUP BY clause groups rows that have the same values in specified columns into summary rows. It's typically used with aggregate functions to produce summary reports.

### 8.2 Basic GROUP BY Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1;
```

### 8.3 Simple GROUP BY Examples

```sql
-- Count products in each category
SELECT category, COUNT(*) AS product_count
FROM product
GROUP BY category;

-- Average price by category
SELECT category, AVG(price) AS avg_price
FROM product
GROUP BY category;

-- Count products by manufacturer
SELECT manufacturer, COUNT(*) AS product_count
FROM product
GROUP BY manufacturer;
```

**Expected Output Example:**
```
+-------------+---------------+
| category    | product_count |
+-------------+---------------+
| Gadgets     |             3 |
| Household   |             1 |
| Photography |             2 |
+-------------+---------------+
```

### 8.4 GROUP BY with Multiple Columns

```sql
-- Count products by category and manufacturer
SELECT 
    category,
    manufacturer,
    COUNT(*) AS product_count
FROM product
GROUP BY category, manufacturer
ORDER BY category, manufacturer;
```

### 8.5 GROUP BY with Multiple Aggregates

```sql
-- Comprehensive statistics by category
SELECT 
    category,
    COUNT(*) AS product_count,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    AVG(price) AS avg_price,
    SUM(price) AS total_value
FROM product
GROUP BY category;
```

### 8.6 GROUP BY with WHERE Clause

The WHERE clause filters rows BEFORE grouping occurs.

```sql
-- Average price by category for products over $50
SELECT 
    category,
    COUNT(*) AS count,
    AVG(price) AS avg_price
FROM product
WHERE price > 50
GROUP BY category;
```

**Important:** WHERE filters individual rows before aggregation.

### 8.7 GROUP BY with Joins

```sql
-- Count products by country
SELECT 
    c.country,
    COUNT(p.pname) AS product_count,
    AVG(p.price) AS avg_price
FROM company c
LEFT JOIN product p ON c.cname = p.manufacturer
GROUP BY c.country;
```

### 8.8 GROUP BY with ORDER BY

```sql
-- Products per category, sorted by count (descending)
SELECT 
    category,
    COUNT(*) AS product_count
FROM product
GROUP BY category
ORDER BY product_count DESC;

-- Average price by manufacturer, sorted alphabetically
SELECT 
    manufacturer,
    AVG(price) AS avg_price
FROM product
GROUP BY manufacturer
ORDER BY manufacturer;
```

### 8.9 GROUP BY Rules and Best Practices

**Rule 1:** Every column in the SELECT list must either:
- Be in the GROUP BY clause, OR
- Be used in an aggregate function

```sql
-- CORRECT: pname is in GROUP BY
SELECT category, COUNT(*) AS count
FROM product
GROUP BY category;

-- INCORRECT: pname is not in GROUP BY and not aggregated
-- SELECT category, pname, COUNT(*) AS count
-- FROM product
-- GROUP BY category;
```

**Rule 2:** You can use column positions instead of names:

```sql
-- Group by first column in SELECT
SELECT category, COUNT(*) AS count
FROM product
GROUP BY 1;
```

**Best Practice:** Use column names for better readability.

### 8.10 GROUP BY with DISTINCT

```sql
-- Count distinct manufacturers per category
SELECT 
    category,
    COUNT(DISTINCT manufacturer) AS manufacturer_count
FROM product
GROUP BY category;
```

### 8.11 GROUP BY with Calculated Fields

```sql
-- Group by price range
SELECT 
    CASE 
        WHEN price < 50 THEN 'Budget'
        WHEN price BETWEEN 50 AND 150 THEN 'Mid-range'
        ELSE 'Premium'
    END AS price_range,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM product
GROUP BY price_range
ORDER BY avg_price;
```

### 8.12 Grouping with NULL Values

```sql
-- NULL values are grouped together
SELECT 
    category,
    COUNT(*) AS count
FROM product
GROUP BY category;
-- Products with NULL category will be in one group
```

### 8.13 GROUP BY Performance Considerations

- Indexes on GROUP BY columns can improve performance
- GROUP BY can be memory-intensive with many groups
- Consider using LIMIT with ORDER BY for large result sets

### 8.14 Practice Exercises

**Exercise 1:** Group products by manufacturer and show the count and average price for each.

**Exercise 2:** Find the number of products in each category, but only for categories with more than 1 product.

**Exercise 3:** Group products by price range (e.g., 0-50, 51-100, 101+) and count how many fall in each range.

**Exercise 4:** Show the total value of products for each manufacturer, sorted by total value descending.

**Exercise 5:** Find the average price per country (using joins with the company table).

---

## 9. HAVING

### 9.1 Introduction to HAVING

The HAVING clause filters groups AFTER aggregation has occurred. While WHERE filters individual rows before grouping, HAVING filters the grouped results.

### 9.2 Difference Between WHERE and HAVING

| Clause | When Applied | What It Filters | Can Use Aggregates |
|--------|--------------|-----------------|-------------------|
| WHERE  | Before GROUP BY | Individual rows | No |
| HAVING | After GROUP BY | Grouped results | Yes |

### 9.3 Basic HAVING Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

### 9.4 Simple HAVING Examples

```sql
-- Find categories with more than 2 products
SELECT 
    category,
    COUNT(*) AS product_count
FROM product
GROUP BY category
HAVING COUNT(*) > 2;

-- Find manufacturers with average price over $50
SELECT 
    manufacturer,
    AVG(price) AS avg_price
FROM product
GROUP BY manufacturer
HAVING AVG(price) > 50;
```

### 9.5 HAVING with Multiple Conditions

```sql
-- Categories with more than 1 product AND average price > $30
SELECT 
    category,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM product
GROUP BY category
HAVING COUNT(*) > 1 AND AVG(price) > 30;

-- Manufacturers with at least 2 products OR total value > $100
SELECT 
    manufacturer,
    COUNT(*) AS product_count,
    SUM(price) AS total_value
FROM product
GROUP BY manufacturer
HAVING COUNT(*) >= 2 OR SUM(price) > 100;
```

### 9.6 Combining WHERE and HAVING

```sql
-- Find categories (excluding Household) with more than 1 product
SELECT 
    category,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM product
WHERE category != 'Household'  -- Filter rows before grouping
GROUP BY category
HAVING COUNT(*) > 1;            -- Filter groups after aggregation
```

**Execution Order:**
1. WHERE filters individual rows
2. GROUP BY groups the remaining rows
3. Aggregate functions calculate values
4. HAVING filters the groups
5. ORDER BY sorts the final result

### 9.7 HAVING with Range Conditions

```sql
-- Categories with average price between $30 and $100
SELECT 
    category,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM product
GROUP BY category
HAVING AVG(price) BETWEEN 30 AND 100;
```

### 9.8 HAVING with IN Operator

```sql
-- Find manufacturers with specific product counts
SELECT 
    manufacturer,
    COUNT(*) AS product_count
FROM product
GROUP BY manufacturer
HAVING COUNT(*) IN (2, 3, 4);
```

### 9.9 HAVING with Calculated Values

```sql
-- Categories where max price is more than 3x min price
SELECT 
    category,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    MAX(price) / MIN(price) AS price_ratio
FROM product
GROUP BY category
HAVING MAX(price) / MIN(price) > 3;
```

### 9.10 HAVING with Joins

```sql
-- Countries with more than 2 products
SELECT 
    c.country,
    COUNT(p.pname) AS product_count
FROM company c
INNER JOIN product p ON c.cname = p.manufacturer
GROUP BY c.country
HAVING COUNT(p.pname) > 2;
```

### 9.11 HAVING with Subqueries

```sql
-- Categories with average price above overall average
SELECT 
    category,
    AVG(price) AS avg_price
FROM product
GROUP BY category
HAVING AVG(price) > (SELECT AVG(price) FROM product);
```

### 9.12 Complete Example: WHERE, GROUP BY, HAVING, ORDER BY

```sql
-- Find high-value product categories
SELECT 
    category,
    COUNT(*) AS product_count,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    AVG(price) AS avg_price,
    SUM(price) AS total_value
FROM product
WHERE price > 20                    -- Only products over $20
GROUP BY category                   -- Group by category
HAVING COUNT(*) >= 2                -- At least 2 products
    AND AVG(price) > 30             -- Average over $30
ORDER BY total_value DESC;          -- Sort by total value
```

### 9.13 Common HAVING Mistakes

**Mistake 1:** Using column alias in HAVING (not allowed in standard SQL)
```sql
-- INCORRECT in many databases
-- SELECT category, COUNT(*) AS cnt
-- FROM product
-- GROUP BY category
-- HAVING cnt > 2;

-- CORRECT
SELECT category, COUNT(*) AS cnt
FROM product
GROUP BY category
HAVING COUNT(*) > 2;
```

**Mistake 2:** Filtering non-aggregated columns
```sql
-- Use WHERE for non-aggregated conditions
-- CORRECT
SELECT category, COUNT(*) AS count
FROM product
WHERE manufacturer = 'GizmoWorks'
GROUP BY category;
```

### 9.14 HAVING Performance Tips

- Use WHERE instead of HAVING when possible (filters before grouping = better performance)
- Index columns used in GROUP BY
- Be cautious with complex HAVING conditions on large datasets

### 9.15 Practice Exercises

**Exercise 1:** Find manufacturers that produce more than 2 different products.

**Exercise 2:** Find categories where the total value of products exceeds $100.

**Exercise 3:** Find manufacturers whose cheapest product costs more than $50.

**Exercise 4:** List categories that have products from more than one manufacturer.

**Exercise 5:** Find countries (using joins) where the average product price is above the global average.

---

## 10. Set Operation

### 10.1 Introduction to Set Operations

Set operations combine the results of two or more SELECT statements. They treat query results as mathematical sets, allowing for union, intersection, and difference operations.

**Common Set Operations:**
- `UNION`: Combines results from multiple queries, removing duplicates
- `UNION ALL`: Combines results, keeping all duplicates
- `INTERSECT`: Returns only rows that appear in both queries (not directly supported in MySQL)
- `EXCEPT` (or `MINUS`): Returns rows from first query not in second (not directly supported in MySQL)

### 10.2 UNION Operator

UNION combines results from multiple SELECT statements and removes duplicate rows.

```sql
-- Products from Gadgets OR Photography categories
SELECT pname, category FROM product WHERE category = 'Gadgets'
UNION
SELECT pname, category FROM product WHERE category = 'Photography';
```

**UNION Rules:**
1. Each SELECT must have the same number of columns
2. Columns must have compatible data types
3. Column names from the first SELECT are used in the result

### 10.3 UNION ALL Operator

UNION ALL combines results but keeps all duplicate rows.

```sql
-- Combine products from two queries, keeping duplicates
SELECT pname, category FROM product WHERE category = 'Gadgets'
UNION ALL
SELECT pname, category FROM product WHERE price > 50;
```

**When to use UNION ALL:**
- When you know there are no duplicates
- When you want to keep duplicates
- Better performance (no duplicate removal)

### 10.4 UNION vs UNION ALL Performance

```sql
-- UNION (slower - removes duplicates)
SELECT manufacturer FROM product WHERE category = 'Gadgets'
UNION
SELECT manufacturer FROM product WHERE category = 'Photography';

-- UNION ALL (faster - keeps duplicates)
SELECT manufacturer FROM product WHERE category = 'Gadgets'
UNION ALL
SELECT manufacturer FROM product WHERE category = 'Photography';
```

### 10.5 UNION with Different Tables

```sql
-- Combine product names and company names into one list
SELECT pname AS name, 'Product' AS type FROM product
UNION
SELECT cname AS name, 'Company' AS type FROM company
ORDER BY name;
```

### 10.6 UNION with Aggregates

```sql
-- Combine statistics from different queries
SELECT 'Gadgets' AS category, COUNT(*) AS count, AVG(price) AS avg_price
FROM product WHERE category = 'Gadgets'
UNION ALL
SELECT 'Photography', COUNT(*), AVG(price)
FROM product WHERE category = 'Photography'
UNION ALL
SELECT 'All Categories', COUNT(*), AVG(price)
FROM product;
```

### 10.7 INTERSECT Operation (MySQL Alternative)

MySQL doesn't have native INTERSECT, but you can achieve it using joins or subqueries.

```sql
-- Find products that are both in Gadgets and have price > 25
-- Method 1: Using INNER JOIN
SELECT DISTINCT p1.pname
FROM product p1
INNER JOIN product p2 ON p1.pname = p2.pname
WHERE p1.category = 'Gadgets' AND p2.price > 25;

-- Method 2: Using IN
SELECT pname FROM product WHERE category = 'Gadgets'
AND pname IN (SELECT pname FROM product WHERE price > 25);

-- Method 3: Using EXISTS
SELECT p1.pname FROM product p1
WHERE p1.category = 'Gadgets'
AND EXISTS (SELECT 1 FROM product p2 WHERE p2.pname = p1.pname AND p2.price > 25);
```

### 10.8 EXCEPT/MINUS Operation (MySQL Alternative)

MySQL doesn't have native EXCEPT, but you can use NOT IN or NOT EXISTS.

```sql
-- Find products in Gadgets that are NOT priced over $40
-- Method 1: Using NOT IN
SELECT pname FROM product WHERE category = 'Gadgets'
AND pname NOT IN (SELECT pname FROM product WHERE price > 40);

-- Method 2: Using NOT EXISTS
SELECT p1.pname FROM product p1
WHERE p1.category = 'Gadgets'
AND NOT EXISTS (
    SELECT 1 FROM product p2 
    WHERE p2.pname = p1.pname AND p2.price > 40
);

-- Method 3: Using LEFT JOIN with NULL check
SELECT p1.pname
FROM product p1
LEFT JOIN (SELECT pname FROM product WHERE price > 40) p2 
    ON p1.pname = p2.pname
WHERE p1.category = 'Gadgets' AND p2.pname IS NULL;
```

### 10.9 Complex UNION Examples

```sql
-- Comprehensive product and company report
SELECT 
    'Product' AS type,
    pname AS name,
    category AS detail,
    price AS value
FROM product
UNION ALL
SELECT 
    'Company' AS type,
    cname AS name,
    country AS detail,
    NULL AS value
FROM company
ORDER BY type, name;
```

### 10.10 UNION with WHERE and ORDER BY

```sql
-- Expensive products from multiple categories
(SELECT pname, price, category FROM product 
 WHERE category = 'Gadgets' AND price > 30)
UNION
(SELECT pname, price, category FROM product 
 WHERE category = 'Photography' AND price > 100)
ORDER BY price DESC;
```

**Note:** When using ORDER BY with UNION, place it after the last SELECT and it applies to the entire result.

### 10.11 UNION with LIMIT

```sql
-- Get top 2 from each category
(SELECT pname, price, category FROM product 
 WHERE category = 'Gadgets' 
 ORDER BY price DESC LIMIT 2)
UNION ALL
(SELECT pname, price, category FROM product 
 WHERE category = 'Photography' 
 ORDER BY price DESC LIMIT 2)
ORDER BY price DESC;
```

### 10.12 Practical Set Operation Examples

#### Example 1: Customer Activity Report
```sql
-- Combine new and returning customers
SELECT customer_id, 'New' AS status FROM orders 
WHERE order_date >= '2024-01-01'
AND customer_id NOT IN (SELECT customer_id FROM orders WHERE order_date < '2024-01-01')
UNION
SELECT customer_id, 'Returning' AS status FROM orders 
WHERE order_date >= '2024-01-01'
AND customer_id IN (SELECT customer_id FROM orders WHERE order_date < '2024-01-01');
```

#### Example 2: Product Inventory Report
```sql
-- Combine high stock, low stock, and out of stock products
SELECT product_id, name, 'High Stock' AS status 
FROM inventory WHERE quantity > 100
UNION ALL
SELECT product_id, name, 'Low Stock' AS status 
FROM inventory WHERE quantity BETWEEN 1 AND 100
UNION ALL
SELECT product_id, name, 'Out of Stock' AS status 
FROM inventory WHERE quantity = 0
ORDER BY status, name;
```

### 10.13 Set Operations with Joins

```sql
-- Products from US companies UNION products from Japanese companies
SELECT p.pname, p.category, c.country
FROM product p
INNER JOIN company c ON p.manufacturer = c.cname
WHERE c.country = 'USA'
UNION
SELECT p.pname, p.category, c.country
FROM product p
INNER JOIN company c ON p.manufacturer = c.cname
WHERE c.country = 'Japan'
ORDER BY country, pname;
```

### 10.14 Common Set Operation Mistakes

**Mistake 1:** Different number of columns
```sql
-- INCORRECT
-- SELECT pname FROM product
-- UNION
-- SELECT cname, city FROM company;  -- Different column count!
```

**Mistake 2:** Incompatible data types
```sql
-- INCORRECT
-- SELECT pname FROM product
-- UNION
-- SELECT price FROM product;  -- VARCHAR and DECIMAL don't match well
```

**Mistake 3:** Using ORDER BY in individual SELECTs
```sql
-- INCORRECT
-- SELECT pname FROM product ORDER BY pname
-- UNION
-- SELECT cname FROM company ORDER BY cname;

-- CORRECT
SELECT pname AS name FROM product
UNION
SELECT cname AS name FROM company
ORDER BY name;
```

### 10.15 Set Operations Performance Tips

1. Use UNION ALL instead of UNION when duplicates don't matter (faster)
2. Add WHERE clauses to filter before UNION (reduces rows to process)
3. Ensure columns used in ORDER BY are indexed
4. Use parentheses to control execution order in complex unions
5. Consider materialized views for frequently used union queries

### 10.16 Practice Exercises

**Exercise 1:** Create a UNION query that lists all unique cities from both the company and customer tables.

**Exercise 2:** Find products that are either in the 'Gadgets' category OR priced above $100, removing duplicates.

**Exercise 3:** Create a report combining products with low stock and products that haven't sold in 30 days.

**Exercise 4:** Simulate an INTERSECT operation to find products that are both in 'Photography' category AND made by Japanese companies.

**Exercise 5:** Simulate an EXCEPT operation to find products in 'Gadgets' category that have never been ordered.

---

## 📚 Summary and Next Steps

### What You've Learned

In this comprehensive guide, you've mastered:

1. **Create Tables**: Database and table creation with proper data types and constraints
2. **Single Table Query**: SELECT statements with filtering using WHERE clause
3. **DISTINCT**: Removing duplicates and finding unique values
4. **ORDER BY**: Sorting results in ascending or descending order
5. **Foreign Key**: Establishing referential integrity and table relationships
6. **Multi Table**: Joining tables using INNER JOIN, LEFT JOIN, RIGHT JOIN
7. **Aggregate Function**: Using COUNT, SUM, AVG, MIN, MAX for data analysis
8. **GROUP BY**: Grouping data for summary statistics
9. **HAVING**: Filtering grouped results
10. **Set Operation**: Combining queries with UNION and UNION ALL

### Recommended Next Steps

1. **Practice, Practice, Practice**: Work through all exercises in each section
2. **Real-World Projects**: Apply these concepts to your own database projects
3. **Advanced Topics**: Explore subqueries, window functions, stored procedures
4. **Performance Optimization**: Learn about indexes, query optimization, and execution plans
5. **Database Design**: Study normalization and entity-relationship modeling

### Additional Resources

- [MySQL Official Documentation](https://dev.mysql.com/doc/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [SQLZoo Interactive Tutorial](https://sqlzoo.net/)
- [LeetCode Database Problems](https://leetcode.com/problemset/database/)

### Practice Database

All examples in this guide use the `sql_fundamentals` database. You can recreate it by running all the CREATE TABLE and INSERT statements in order.

---

## 🎓 Final Practice Project

Create a complete database system for a bookstore with the following requirements:

1. **Tables**: Books, Authors, Publishers, Customers, Orders, OrderDetails
2. **Relationships**: Implement foreign keys between all related tables
3. **Queries**: Write queries using all concepts learned:
   - List all books with their authors and publishers (multi-table)
   - Find the top 5 best-selling books (aggregate + order by)
   - Calculate total sales by genre (group by + having)
   - Find customers who haven't ordered in 6 months (set operations)
   - Get unique genres available (distinct)

This project will reinforce all concepts covered in this guide.

---

**Good luck with your SQL journey! 🚀**
