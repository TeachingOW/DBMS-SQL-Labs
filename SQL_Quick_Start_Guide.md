# SQL Quick Start Guide

> **A straightforward, beginner-friendly introduction to SQL fundamentals**

## 🎯 What You'll Learn

This guide covers 10 essential SQL topics in order. Each section is concise with practical examples you can run immediately.

**Estimated Time:** 3-4 hours

**Prerequisites:** MySQL or MariaDB installed

---

## 📋 Table of Contents

1. [Create Tables](#1-create-tables)
2. [Single Table Query](#2-single-table-query)
3. [Subqueries and Nested Queries](#3-subqueries-and-nested-queries)
4. [DISTINCT](#4-distinct)
5. [ORDER BY](#5-order-by)
6. [Foreign Key](#6-foreign-key)
7. [Multi Table](#7-multi-table)
8. [Aggregate Functions](#8-aggregate-functions)
9. [GROUP BY](#9-group-by)
10. [HAVING](#10-having)
11. [Set Operations](#11-set-operations)

---

## 1. Create Tables

### Setup Database

```sql
CREATE DATABASE store;
USE store;
```

### Create Your First Table

```sql
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10,2),
    category VARCHAR(30)
);
```

**Key Points:**
- `PRIMARY KEY`: Unique identifier
- `VARCHAR(n)`: Text up to n characters
- `DECIMAL(10,2)`: Numbers with 2 decimal places

### Add Data

```sql
INSERT INTO products VALUES
(1, 'Laptop', 999.99, 'Electronics'),
(2, 'Mouse', 25.50, 'Electronics'),
(3, 'Desk', 299.99, 'Furniture'),
(4, 'Chair', 199.99, 'Furniture'),
(5, 'Monitor', 349.99, 'Electronics');
```

### ✏️ Practice
Create a `customers` table with: id, name, email, city.

---

## 2. Single Table Query

### Select All Data

```sql
SELECT * FROM products;
```

### Select Specific Columns

```sql
SELECT name, price FROM products;
```

### Filter with WHERE

```sql
-- Products under $300
SELECT * FROM products WHERE price < 300;

-- Products in Electronics category
SELECT * FROM products WHERE category = 'Electronics';

-- Multiple conditions with AND
SELECT * FROM products 
WHERE category = 'Electronics' AND price < 500;

-- Multiple conditions with OR
SELECT * FROM products 
WHERE category = 'Electronics' OR category = 'Furniture';
```

### Pattern Matching with LIKE

```sql
-- Products starting with 'M'
SELECT * FROM products WHERE name LIKE 'M%';

-- Products containing 'top'
SELECT * FROM products WHERE name LIKE '%top%';
```

### ✏️ Practice
Find all furniture items priced between $100 and $300.

---

## 3. Subqueries and Nested Queries

### What are Subqueries?

A subquery (or nested query) is a query inside another query. Subqueries can be used in WHERE, FROM, or HAVING clauses.

### Basic Subquery

```sql
-- Find products more expensive than the average price
SELECT name, price 
FROM products 
WHERE price > (SELECT AVG(price) FROM products);
```

### IN Operator with Subquery

**IN** checks if a value exists in a list or result set.

```sql
-- Find products in Electronics or Furniture categories
SELECT * FROM products 
WHERE category IN ('Electronics', 'Furniture');

-- Using subquery: Find products from USA suppliers
SELECT * FROM products 
WHERE supplier_id IN (
    SELECT id FROM suppliers WHERE country = 'USA'
);
```

### NOT IN Operator

**NOT IN** finds values that are NOT in a list or result set.

```sql
-- Find products NOT from USA suppliers
SELECT * FROM products 
WHERE supplier_id NOT IN (
    SELECT id FROM suppliers WHERE country = 'USA'
);

-- Find products that haven't been ordered
-- (assuming we have an orders table)
SELECT name FROM products 
WHERE id NOT IN (SELECT DISTINCT product_id FROM orders);
```

### EXISTS Operator

**EXISTS** checks if a subquery returns any rows (returns TRUE/FALSE).

```sql
-- Find suppliers that have at least one product
SELECT name FROM suppliers s
WHERE EXISTS (
    SELECT 1 FROM products p 
    WHERE p.supplier_id = s.id
);

-- Find categories that have expensive products (over $500)
SELECT DISTINCT category FROM products p1
WHERE EXISTS (
    SELECT 1 FROM products p2 
    WHERE p2.category = p1.category AND p2.price > 500
);
```

### NOT EXISTS Operator

**NOT EXISTS** checks if a subquery returns no rows.

```sql
-- Find suppliers with NO products listed
SELECT name FROM suppliers s
WHERE NOT EXISTS (
    SELECT 1 FROM products p 
    WHERE p.supplier_id = s.id
);
```

### Complex Nested Query Example

```sql
-- Find products made by suppliers who also make laptops
SELECT name, price FROM products
WHERE supplier_id IN (
    SELECT supplier_id FROM products 
    WHERE name = 'Laptop'
)
AND name != 'Laptop';
```

### When to Use Each

- **IN/NOT IN**: When comparing against a list of values
- **EXISTS/NOT EXISTS**: When checking for existence (often faster for large datasets)
- **Subquery in SELECT**: For calculated columns
- **Subquery in FROM**: To create temporary result sets

### ✏️ Practice
1. Find all products that cost more than the average price
2. Find suppliers from Canada who have products listed
3. Find categories with no products under $100

---

## 4. DISTINCT

### Get Unique Values

```sql
-- List all unique categories
SELECT DISTINCT category FROM products;

-- Count unique categories
SELECT COUNT(DISTINCT category) FROM products;
```

**When to use:** Eliminate duplicate rows from results.

### ✏️ Practice
Find all unique price values in the products table.

---

## 5. ORDER BY

### Sort Results

```sql
-- Sort by price (ascending)
SELECT * FROM products ORDER BY price;

-- Sort by price (descending)
SELECT * FROM products ORDER BY price DESC;

-- Sort by multiple columns
SELECT * FROM products ORDER BY category, price DESC;
```

**Tips:**
- `ASC` = ascending (default)
- `DESC` = descending
- Can sort by multiple columns

### ✏️ Practice
List all products sorted by category (A-Z) and then by price (high to low).

---

## 6. Foreign Key

### Why Foreign Keys?
Foreign keys link tables together and ensure data integrity.

### Create Related Tables

```sql
-- Suppliers table (parent)
CREATE TABLE suppliers (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    country VARCHAR(30)
);

-- Products with foreign key (child)
CREATE TABLE products_fk (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10,2),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);
```

### Add Data

```sql
-- Add suppliers first
INSERT INTO suppliers VALUES
(1, 'TechCorp', 'USA'),
(2, 'FurnitureCo', 'Canada');

-- Add products that reference suppliers
INSERT INTO products_fk VALUES
(1, 'Laptop', 999.99, 1),
(2, 'Desk', 299.99, 2);
```

**Important:** You must insert parent records (suppliers) before child records (products).

### ✏️ Practice
Try inserting a product with a supplier_id that doesn't exist. What happens?

---

## 7. Multi Table

### JOIN Tables

```sql
-- Show products with their supplier information
SELECT 
    p.name AS product_name,
    p.price,
    s.name AS supplier_name,
    s.country
FROM products_fk p
INNER JOIN suppliers s ON p.supplier_id = s.id;
```

### Types of JOINs

**INNER JOIN** - Only matching rows
```sql
SELECT p.name, s.name
FROM products_fk p
INNER JOIN suppliers s ON p.supplier_id = s.id;
```

**LEFT JOIN** - All from left table, matching from right
```sql
SELECT p.name, s.name
FROM products_fk p
LEFT JOIN suppliers s ON p.supplier_id = s.id;
```

**Tip:** Start with INNER JOIN. It's the most common.

### ✏️ Practice
Join customers and orders tables (create these tables first).

---

## 8. Aggregate Functions

### Common Functions

```sql
-- Count all products
SELECT COUNT(*) FROM products;

-- Sum of all prices
SELECT SUM(price) FROM products;

-- Average price
SELECT AVG(price) FROM products;

-- Highest price
SELECT MAX(price) FROM products;

-- Lowest price
SELECT MIN(price) FROM products;
```

### All in One Query

```sql
SELECT 
    COUNT(*) AS total_products,
    SUM(price) AS total_value,
    AVG(price) AS average_price,
    MAX(price) AS highest_price,
    MIN(price) AS lowest_price
FROM products;
```

### ✏️ Practice
Calculate the total value of all electronics products.

---

## 9. GROUP BY

### Group Data

```sql
-- Count products by category
SELECT category, COUNT(*) AS count
FROM products
GROUP BY category;

-- Average price by category
SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category;

-- Multiple aggregations
SELECT 
    category,
    COUNT(*) AS count,
    AVG(price) AS avg_price,
    MAX(price) AS max_price
FROM products
GROUP BY category;
```

**Rule:** Every column in SELECT must be either in GROUP BY or an aggregate function.

### ✏️ Practice
Find the total value of products in each category.

---

## 10. HAVING

### Filter Grouped Results

**WHERE** filters rows before grouping  
**HAVING** filters groups after aggregation

```sql
-- Categories with more than 2 products
SELECT category, COUNT(*) AS count
FROM products
GROUP BY category
HAVING COUNT(*) > 2;

-- Categories with average price over $300
SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 300;
```

### Combined Example

```sql
-- Electronics products, grouped by category, 
-- only show groups with avg price > $100
SELECT category, AVG(price) AS avg_price
FROM products
WHERE category = 'Electronics'
GROUP BY category
HAVING AVG(price) > 100;
```

### ✏️ Practice
Find categories that have at least 1 product and average price under $250.

---

## 11. Set Operations

### UNION - Combine Results

```sql
-- Combine two queries
SELECT name FROM products WHERE category = 'Electronics'
UNION
SELECT name FROM products WHERE price > 500;
```

**UNION** removes duplicates  
**UNION ALL** keeps duplicates

```sql
-- Keep all rows including duplicates
SELECT category FROM products WHERE price < 300
UNION ALL
SELECT category FROM products WHERE price > 200;
```

**Rules:**
- Same number of columns in each SELECT
- Compatible data types
- Column names from first SELECT are used

### ✏️ Practice
Combine a list of product names under $100 with product names in the Furniture category.

---

## 🎓 Quick Reference Summary

### Create & Insert
```sql
CREATE TABLE table_name (column datatype constraints);
INSERT INTO table_name VALUES (val1, val2, ...);
```

### Query
```sql
SELECT columns FROM table WHERE condition ORDER BY column;
```

### Join
```sql
SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.id;
```

### Aggregate & Group
```sql
SELECT column, COUNT(*), AVG(column2)
FROM table
WHERE condition
GROUP BY column
HAVING COUNT(*) > value;
```

### Combine
```sql
SELECT columns FROM table1
UNION
SELECT columns FROM table2;
```

---

## 📚 Next Steps

**You've learned:**
✅ Creating tables and inserting data  
✅ Querying and filtering data  
✅ Sorting and removing duplicates  
✅ Linking tables with foreign keys  
✅ Joining multiple tables  
✅ Calculating statistics  
✅ Grouping and filtering groups  
✅ Combining query results  

**Continue learning:**
- Views and Virtual Tables
- Subqueries and Nested Queries
- Indexes and Performance
- Transactions and ACID
- Stored Procedures and Triggers

---

## 💡 Tips for Success

1. **Practice by typing** - Don't copy/paste. Type the SQL yourself.
2. **Use real data** - Create your own tables with data you care about.
3. **Read error messages** - They tell you exactly what's wrong.
4. **Start simple** - Master SELECT before complex JOINs.
5. **Draw your tables** - Sketch table relationships on paper.

---

## 🔗 Resources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [SQLZoo Interactive Tutorial](https://sqlzoo.net/)

---

**Ready to code? Start with Section 1 and work your way through!** 🚀
