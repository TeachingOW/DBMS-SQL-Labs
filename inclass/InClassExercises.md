
# Lab 1: Database Creation and Basic SQL Operations

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
- Create and manage databases in MySQL/MariaDB
- Design and create tables with appropriate data types
- Insert data into tables
- Write basic SELECT queries with filtering and sorting
- Understand primary keys and constraints

## 📋 Prerequisites
- MySQL or MariaDB server installed and running
- Basic understanding of relational database concepts
- Access to a SQL client (command line, MySQL Workbench, etc.)

## 🚀 Getting Started

### Step 1: Create Your First Database

A database is a container that holds related tables. Let's create one for our exercises:

```sql
-- Create a new database (only needed once)
CREATE DATABASE lab1_exercises;
```

**Note**: Database names are case-sensitive on some systems. Use lowercase for consistency.

### Step 2: Select the Database

Before creating tables, you must specify which database to use:

```sql
-- Switch to our new database
USE lab1_exercises;
```

**Important**: You need to run `USE database_name;` every time you start a new session.

### Step 3: Create Your First Table

Let's create a product catalog table with proper data types and constraints:

```sql
-- Create the product table with detailed comments
CREATE TABLE product(
    pname        VARCHAR(20) PRIMARY KEY,  -- Product name (unique identifier)
    price        DECIMAL(10,2),            -- Price with 2 decimal places
    category     VARCHAR(20),              -- Product category
    manufacturer VARCHAR(20) NOT NULL      -- Manufacturer (required field)
);
```

**Key Concepts**:
- `PRIMARY KEY`: Ensures each product name is unique
- `DECIMAL(10,2)`: Stores numbers with up to 10 digits, 2 after decimal point
- `NOT NULL`: This field cannot be empty
- `VARCHAR(20)`: Variable-length string up to 20 characters

### Step 4: Insert Sample Data

Now let's add some products to our table:

```sql
-- Insert sample products
INSERT INTO product VALUES('Gizmo', 19.99, 'Gadgets', 'GizmoWorks');
INSERT INTO product VALUES('PowerGizmo', 29.99, 'Gadgets', 'GizmoWorks');
INSERT INTO product VALUES('MultiTouch', 203.99, 'Household', 'Hitachi');
INSERT INTO product VALUES('SingleTouch', 149.99, 'Photography', 'Canon');
```

**Verify your data**:
```sql
-- View all products
SELECT * FROM product;
```

**Expected Output**:
| pname | price | category | manufacturer |
|-------|-------|----------|--------------|
| Gizmo | 19.99 | Gadgets | GizmoWorks |
| PowerGizmo | 29.99 | Gadgets | GizmoWorks |
| MultiTouch | 203.99 | Household | Hitachi |
| SingleTouch | 149.99 | Photography | Canon |


## 💡 Practice Exercises

### Exercise #1: Filtering and Sorting

**Task**: Write a query to get all products with "Touch" in the name, showing only their name and price, sorted alphabetically by manufacturer.

**Step-by-step approach**:
1. First, let's see all our products to understand the data:
   ```sql
   SELECT * FROM product;
   ```

2. Now identify products with "Touch" in the name:
   ```sql
   SELECT * FROM product WHERE pname LIKE '%Touch%';
   ```

3. **Your turn**: Write the complete query here:
   ```sql
   -- Write your solution here
   
   ```

<details>
<summary>💡 Click to see the solution</summary>

```sql
SELECT pname, price 
FROM product 
WHERE pname LIKE '%Touch%' 
ORDER BY manufacturer;
```

**Expected Output**:
| pname | price |
|-------|-------|
| SingleTouch | 149.99 |
| MultiTouch | 203.99 |

**Explanation**:
- `LIKE '%Touch%'`: Finds any product name containing "Touch"
- `ORDER BY manufacturer`: Sorts by manufacturer (Canon comes before Hitachi alphabetically)
</details>

### Exercise #1b: Distinct Values

**Task**: Write a query that returns the distinct names of manufacturers that make products with "Gizmo" in the name.

**Your solution**:
```sql
-- Write your solution here

```

<details>
<summary>💡 Click to see the solution</summary>

```sql
SELECT DISTINCT manufacturer 
FROM product 
WHERE pname LIKE '%Gizmo%';
```

**Expected Output**:
| manufacturer |
|--------------|
| GizmoWorks |

**Explanation**:
- `DISTINCT`: Removes duplicate manufacturer names
- Only GizmoWorks makes products with "Gizmo" in the name
</details>

### Exercise #2: Understanding DISTINCT and ORDER BY

**Task**: Before running these queries, predict what each will return. Then run them to check your understanding.

```sql
-- Query A
SELECT DISTINCT category FROM product ORDER BY category;

-- Query B  
SELECT category FROM product ORDER BY pname;

-- Query C
SELECT DISTINCT category FROM product ORDER BY pname;
```

**Predictions**:
- Query A will return: ________________
- Query B will return: ________________  
- Query C will return: ________________

<details>
<summary>💡 Click to see the answers</summary>

**Query A Results**:
| category |
|----------|
| Gadgets |
| Household |
| Photography |

**Explanation**: Returns unique categories sorted alphabetically.

**Query B Results**:
| category |
|----------|
| Gadgets |
| Household |
| Photography |
| Gadgets |

**Explanation**: Returns all categories (including duplicates) in the order of product names.

**Query C Results**:
This query will produce an **ERROR**! You cannot use `ORDER BY pname` when `pname` is not in the SELECT list and you're using DISTINCT.

**Key Learning**: When using DISTINCT, you can only ORDER BY columns that are in the SELECT clause.
</details>

### Exercise #3: Multi-Table Relationships and Foreign Keys

**Learning Focus**: Understanding table relationships, foreign keys, and multi-table queries.

#### Setting Up the Database Schema

We need to recreate our tables to demonstrate foreign key relationships:

```sql
-- Clean up existing tables (order matters due to foreign key constraints!)
DROP TABLE IF EXISTS product;  -- Drop child table first
DROP TABLE IF EXISTS company;   -- Then drop parent table

-- Create the parent table (company)
CREATE TABLE company (
    cname VARCHAR(20) PRIMARY KEY,    -- Company name (unique identifier)
    stockprice DECIMAL(10,2),         -- Stock price in dollars
    country VARCHAR(10)               -- Country of origin
);

-- Insert company data
INSERT INTO company VALUES ('ToyWorks', 25.0, 'USA');
INSERT INTO company VALUES ('ToyFriends', 65.0, 'China');
INSERT INTO company VALUES ('ToyCo', 15.0, 'China');
```

**Verify company data**:
```sql
SELECT * FROM company;
```

Now create the product table with a foreign key relationship:

```sql
-- Create the child table (product) with foreign key constraint
CREATE TABLE product(
    pname VARCHAR(10),                -- Product name
    price DECIMAL(10,2),              -- Product price
    category VARCHAR(10),             -- Product category
    manufacturer VARCHAR(10),         -- Manufacturer (references company)
    PRIMARY KEY (pname, manufacturer), -- Composite primary key
    FOREIGN KEY (manufacturer) REFERENCES company(cname)  -- Foreign key constraint
);

-- Insert product data
INSERT INTO product VALUES('Pikachu', 19.99, 'Toy', 'ToyWorks');
INSERT INTO product VALUES('Pikachu', 19.99, 'Toy', 'ToyFriends');
INSERT INTO product VALUES('Pokeball', 29.99, 'Electronic', 'ToyCo');
INSERT INTO product VALUES('Bulbasaur', 149.99, 'Toy', 'ToyFriends');
INSERT INTO product VALUES('Charizard', 203.99, 'Toy', 'ToyCo');
INSERT INTO product VALUES('PokeCamera', 19.99, 'Electronic', 'ToyWorks');
```

**Key Concepts Explained**:
- **Composite Primary Key**: `(pname, manufacturer)` together uniquely identify each row
- **Foreign Key**: `manufacturer` must exist in the `company` table
- **Referential Integrity**: You cannot insert a product with a non-existent manufacturer

#### The Challenge

**Task**: Find all categories of products that are made by Chinese companies.

**Step-by-step approach**:

1. **First, explore the data**:
   ```sql
   -- See all companies
   SELECT * FROM company;
   
   -- See all products  
   SELECT * FROM product;
   
   -- See which companies are Chinese
   SELECT * FROM company WHERE country = 'China';
   ```

2. **Your turn**: Write the query to find categories made by Chinese companies:
   ```sql
   -- Write your solution here
   
   ```

<details>
<summary>💡 Click to see the solution</summary>

**Solution using JOIN**:
```sql
SELECT DISTINCT p.category
FROM product p
JOIN company c ON p.manufacturer = c.cname
WHERE c.country = 'China';
```

**Alternative solution using WHERE clause**:
```sql
SELECT DISTINCT category
FROM product, company
WHERE manufacturer = cname 
  AND country = 'China';
```

**Expected Output**:
| category |
|----------|
| Toy |
| Electronic |

**Explanation**:
- We need to connect the `product` and `company` tables
- Filter for companies where `country = 'China'`
- Use `DISTINCT` to avoid duplicate categories
- Chinese companies (ToyFriends, ToyCo) make both Toy and Electronic products
</details>

#### Bonus Challenge

**Task**: Find the names of all products made by companies with stock price > $20.

```sql
-- Write your solution here

```

<details>
<summary>💡 Click to see the bonus solution</summary>

```sql
SELECT p.pname
FROM product p
JOIN company c ON p.manufacturer = c.cname
WHERE c.stockprice > 20;
```

**Expected Output**:
| pname |
|-------|
| Pikachu |
| Pikachu |
| Bulbasaur |
| PokeCamera |

**Note**: Pikachu appears twice because it's made by two different companies (ToyWorks and ToyFriends), both with stock prices > $20.
</details>









## 🎓 Summary

Congratulations! You've completed Lab 1. You should now be comfortable with:

✅ **Database Operations**:
- Creating and using databases
- Understanding database vs. table concepts

✅ **Table Management**:
- Creating tables with appropriate data types
- Understanding primary keys and constraints
- Using foreign keys for referential integrity

✅ **Basic Queries**:
- SELECT statements with filtering (WHERE)
- Using LIKE for pattern matching
- Sorting results with ORDER BY
- Removing duplicates with DISTINCT

✅ **Multi-table Concepts**:
- Understanding table relationships
- Basic JOIN operations
- Foreign key constraints

## 🔗 Additional Resources

### Essential References
- **MySQL Data Types**: [Official Documentation](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)
  - Learn about VARCHAR, DECIMAL, INT, DATE, and other data types
- **CREATE TABLE Syntax**: [MySQL Reference](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
  - Complete guide to table creation options
- **INSERT Statement**: [MariaDB Guide](https://mariadb.com/kb/en/mariadb/how-to-quickly-insert-data-into-mariadb/)
  - Various ways to insert data efficiently

### Practice Resources
- **SQLZoo**: [Interactive SQL Tutorial](https://sqlzoo.net/wiki/SQL_Tutorial)
  - Practice SELECT statements with immediate feedback
- **W3Schools SQL**: [Comprehensive Tutorial](https://www.w3schools.com/sql/)
  - Step-by-step learning with examples

### Next Steps
Ready for more advanced topics? Continue with:
- **[Lab 2](Lab2.md)**: Advanced queries, joins, and aggregations
- **[Foreign Keys Lab](Foreign_Keys.md)**: Deep dive into referential integrity
- **[Multi-table Queries](Multi_Tables.md)**: Complex JOIN operations

## 🐛 Troubleshooting

**Common Issues and Solutions**:

1. **"Database doesn't exist" error**:
   ```sql
   -- Make sure you created and selected the database
   CREATE DATABASE lab1_exercises;
   USE lab1_exercises;
   ```

2. **"Table already exists" error**:
   ```sql
   -- Drop the table first, then recreate
   DROP TABLE IF EXISTS table_name;
   ```

3. **Foreign key constraint fails**:
   - Ensure the parent table exists before creating child table
   - Check that referenced values exist in parent table

4. **Syntax errors**:
   - Check for missing semicolons
   - Verify proper quotation marks around strings
   - Ensure correct spelling of keywords

Need help? Check the [main README](../Readme.md) for additional resources and support options.



   

