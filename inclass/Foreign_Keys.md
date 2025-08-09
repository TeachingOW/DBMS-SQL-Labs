# Lab 3: Foreign Keys and Referential Integrity

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
- Understand the concept and importance of foreign keys
- Create tables with foreign key constraints
- Understand referential integrity and its enforcement
- Work with CASCADE operations (DELETE CASCADE, UPDATE CASCADE)
- Handle foreign key constraint violations
- Understand the relationship between parent and child tables

## 📋 Prerequisites
- Completion of [Lab 1](InClassExercises.md) and [Lab 2](Lab2.md)
- Understanding of primary keys and table relationships
- Basic knowledge of INSERT, UPDATE, and DELETE operations

## 🔗 What are Foreign Keys?

A **foreign key** is a column (or combination of columns) that creates a link between two tables. It ensures **referential integrity** by guaranteeing that values in the foreign key column must exist in the referenced table's primary key column.

### Key Concepts:
- **Parent Table**: Contains the primary key being referenced
- **Child Table**: Contains the foreign key that references the parent
- **Referential Integrity**: Ensures data consistency across related tables

## 🚀 Getting Started

### Alternative Setup
If MySQL is not available, you can use [SQLFiddle](http://sqlfiddle.com/) for online practice.

### Step 1: Create the Database
```sql
-- Create a clean database for foreign key experiments
DROP DATABASE IF EXISTS foreign_key_lab;
CREATE DATABASE foreign_key_lab;
USE foreign_key_lab;
```

## 🏗️ Building Tables with Foreign Key Relationships

### Step 2: Create Tables with Foreign Key Constraints

**Important**: Always create parent tables before child tables!

```sql
-- Drop tables in correct order (child first, then parent)
DROP TABLE IF EXISTS Enrolled;  -- Child table
DROP TABLE IF EXISTS Students;  -- Parent table

-- Create the parent table first
CREATE TABLE Students (
    sid CHAR(10) PRIMARY KEY,    -- Student ID (primary key)
    name CHAR(20),               -- Student name
    gpa FLOAT                    -- Grade Point Average
);

-- Create the child table with foreign key constraint
CREATE TABLE Enrolled (
    sid CHAR(10),                -- Student ID (foreign key)
    cid CHAR(10),                -- Course ID
    grade CHAR(2),               -- Letter grade
    PRIMARY KEY (sid, cid),      -- Composite primary key
    FOREIGN KEY (sid) REFERENCES Students(sid)  -- Foreign key constraint
);
```

**🤔 Why create Students before Enrolled?**
The foreign key in `Enrolled` references the primary key in `Students`. MySQL needs the referenced table to exist first to validate the constraint.

### Step 3: Insert Data and Test Foreign Key Constraints

#### Insert Parent Table Data First
```sql
-- Insert students (parent table data)
INSERT INTO Students VALUES('s1', 'Alice Johnson', 3.1);
INSERT INTO Students VALUES('s2', 'Bob Smith', 3.2);
INSERT INTO Students VALUES('s3', 'Carol Davis', 2.2);
INSERT INTO Students VALUES('s4', 'David Wilson', NULL);  -- NULL GPA allowed
```

#### Insert Child Table Data
```sql
-- Insert enrollments (child table data)
INSERT INTO Enrolled VALUES('s1','cs101', 'A+');
INSERT INTO Enrolled VALUES('s1','cs102', 'A-');
INSERT INTO Enrolled VALUES('s1','cs103', 'B');
INSERT INTO Enrolled VALUES('s1','cs104', 'B');
INSERT INTO Enrolled VALUES('s2','cs101', 'A+');
INSERT INTO Enrolled VALUES('s2','cs103', 'A');
INSERT INTO Enrolled VALUES('s3','cs101', 'A-');
INSERT INTO Enrolled VALUES('s3','cs102', 'C');
INSERT INTO Enrolled VALUES('s3','cs105', 'B');
```

**🔑 Key Point**: Students must be inserted before their enrollments due to the foreign key constraint.

#### Verify the Data
```sql
-- Check students table
SELECT * FROM Students;

-- Check enrollments table  
SELECT * FROM Enrolled;

-- See the relationship in action
SELECT s.name, e.cid, e.grade
FROM Students s
JOIN Enrolled e ON s.sid = e.sid
ORDER BY s.name, e.cid;
```

## 🚫 Testing Foreign Key Constraint Violations

### Exercise 1: Invalid Foreign Key Insert

**Try this command** (it should fail):
```sql
INSERT INTO Enrolled VALUES('s5','cs105', 'B');
```

**Expected Error**:
```
Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails
```

**Why it fails**: Student 's5' doesn't exist in the Students table, violating referential integrity.

### Exercise 2: Attempting to Delete Referenced Records

**Try to delete a student who has enrollments**:
```sql
DELETE FROM Students WHERE sid='s3';
```

**Expected Error**:
```
Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails
```

**Why it fails**: Student 's3' has enrollment records. Deleting the parent would leave orphaned child records.

### Exercise 3: Successful Deletion (No Dependencies)

**Delete a student with no enrollments**:
```sql
DELETE FROM Students WHERE sid='s4';  -- David Wilson has no enrollments
```

**This works** because 's4' has no dependent records in the Enrolled table.

### Exercise 4: Manual Cascade Delete

**To delete a student with enrollments, delete child records first**:
```sql
-- Step 1: Delete the student's enrollments
DELETE FROM Enrolled WHERE sid='s3';

-- Step 2: Now delete the student
DELETE FROM Students WHERE sid='s3';
```

**Verify the deletion**:
```sql
SELECT * FROM Students;
SELECT * FROM Enrolled;
```

---

## ⚡ CASCADE Operations

Manual deletion is tedious. MySQL provides CASCADE options to automatically handle dependent records.

### Step 4: Create Tables with CASCADE DELETE

```sql
-- Drop existing tables
DROP TABLE IF EXISTS Enrolled;
DROP TABLE IF EXISTS Students;

-- Recreate with CASCADE DELETE
CREATE TABLE Students (
    sid CHAR(10) PRIMARY KEY,
    name CHAR(20),
    gpa FLOAT
);

CREATE TABLE Enrolled (
    sid CHAR(10),
    cid CHAR(10),
    grade CHAR(2),
    PRIMARY KEY (sid, cid),
    FOREIGN KEY (sid) REFERENCES Students(sid) ON DELETE CASCADE
);
```

### Step 5: Test CASCADE DELETE

#### Insert Test Data
```sql
-- Insert fresh data
INSERT INTO Students VALUES('s1', 'Alice Johnson', 3.1);
INSERT INTO Students VALUES('s2', 'Bob Smith', 3.2);
INSERT INTO Students VALUES('s3', 'Carol Davis', 2.2);

INSERT INTO Enrolled VALUES('s1','cs101', 'A+');
INSERT INTO Enrolled VALUES('s1','cs102', 'A-');
INSERT INTO Enrolled VALUES('s2','cs101', 'A+');
INSERT INTO Enrolled VALUES('s3','cs101', 'A-');
INSERT INTO Enrolled VALUES('s3','cs102', 'C');
```

#### Test CASCADE DELETE
```sql
-- This will now work and automatically delete related enrollments
DELETE FROM Students WHERE sid='s3';
```

**Verify the cascade effect**:
```sql
-- Check both tables - Carol Davis and her enrollments should be gone
SELECT * FROM Students;
SELECT * FROM Enrolled;
```

**🎉 Success!** The CASCADE DELETE automatically removed Carol's enrollment records when we deleted her student record.

## 🔄 Other CASCADE Options

### ON UPDATE CASCADE
```sql
CREATE TABLE Enrolled (
    sid CHAR(10),
    cid CHAR(10),
    grade CHAR(2),
    PRIMARY KEY (sid, cid),
    FOREIGN KEY (sid) REFERENCES Students(sid) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);
```

### CASCADE Options Summary
- **ON DELETE CASCADE**: Automatically delete child records when parent is deleted
- **ON UPDATE CASCADE**: Automatically update foreign key values when parent key changes
- **ON DELETE SET NULL**: Set foreign key to NULL when parent is deleted
- **ON DELETE RESTRICT**: Prevent deletion of parent if children exist (default)

## 💡 Best Practices

### 1. Design Considerations
- **Use CASCADE carefully**: It can delete large amounts of data
- **Consider SET NULL**: For optional relationships
- **Use RESTRICT**: When you want explicit control over deletions

### 2. Common Patterns
```sql
-- User and their posts (delete posts when user is deleted)
FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE

-- Order and customer (keep orders when customer is deleted, set to NULL)
FOREIGN KEY (customer_id) REFERENCES Customers(id) ON DELETE SET NULL

-- Critical relationships (prevent accidental deletions)
FOREIGN KEY (department_id) REFERENCES Departments(id) ON DELETE RESTRICT
```

## 🎓 Summary

You've learned how to:
✅ Create foreign key constraints
✅ Understand referential integrity enforcement
✅ Handle constraint violations
✅ Use CASCADE operations for automatic maintenance
✅ Choose appropriate CASCADE options for different scenarios

## 🔗 Next Steps
- **[Lab 4](Multi_Tables.md)**: Advanced multi-table queries and complex joins
- **[Lab 5](Lab2.md)**: Aggregate functions and advanced SQL operations

## 🐛 Troubleshooting

**Common Issues**:

1. **Cannot create foreign key**: Ensure parent table exists first
2. **Cannot insert child record**: Verify parent record exists
3. **Cannot delete parent**: Check for dependent child records
4. **CASCADE not working**: Verify CASCADE option is specified in constraint

**Useful Commands**:
```sql
-- Show table structure and constraints
DESCRIBE table_name;

-- Show foreign key constraints
SHOW CREATE TABLE table_name;
```