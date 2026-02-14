# Getting Started with DBMS-SQL-Labs

## 📋 Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Quick Start Guide](#quick-start-guide)
- [Lab Navigation](#lab-navigation)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

## Introduction

Welcome to DBMS-SQL-Labs! This repository contains a comprehensive collection of hands-on SQL laboratories designed to teach database concepts from basic queries to advanced database management techniques. Whether you're a beginner learning SQL for the first time or an experienced developer looking to sharpen your database skills, these labs provide structured, practical experience.

## Prerequisites

### Required Knowledge
- Basic understanding of computer programming concepts
- Familiarity with command-line interfaces
- Basic understanding of data structures

### Software Requirements

#### 1. Database Management System
You'll need at least one of the following:

**MySQL/MariaDB** (Recommended for most labs)
- Download: [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
- Or install via package manager:
  ```bash
  # Ubuntu/Debian
  sudo apt-get update
  sudo apt-get install mysql-server
  
  # macOS (using Homebrew)
  brew install mysql
  
  # Windows
  # Download installer from MySQL website
  ```

**PostgreSQL** (Alternative option)
- Download: [PostgreSQL](https://www.postgresql.org/download/)

#### 2. Programming Languages (for integration labs)

**Python** (Labs 13-15)
- Python 3.7 or higher
- Install MySQL connector:
  ```bash
  pip install mysql-connector-python
  pip install pymysql
  ```

**Java** (Lab 12)
- JDK 11 or higher
- MySQL Connector/J library
- Maven or Gradle (recommended)

**Node.js** (Labs 7-8)
- Node.js 14 or higher
- Install MySQL package:
  ```bash
  npm install mysql2
  ```

#### 3. Additional Tools

**Jupyter Notebooks** (For interactive labs)
```bash
pip install jupyter
pip install ipython-sql
pip install pymysql
```

**MongoDB** (Lab 20)
- Download: [MongoDB Community Edition](https://www.mongodb.com/try/download/community)

**Neo4j** (Lab 21)
- Download: [Neo4j Desktop](https://neo4j.com/download/)

**Database GUI Tools** (Optional but recommended)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
- [DBeaver](https://dbeaver.io/) (Universal database tool)
- [DataGrip](https://www.jetbrains.com/datagrip/) (Commercial)

## Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/TeachingOW/DBMS-SQL-Labs.git
cd DBMS-SQL-Labs
```

### Step 2: Set Up MySQL
1. Start MySQL service:
   ```bash
   # Linux
   sudo systemctl start mysql
   
   # macOS
   brew services start mysql
   
   # Windows
   # Use MySQL Workbench or Services panel
   ```

2. Secure your installation (recommended):
   ```bash
   sudo mysql_secure_installation
   ```

3. Log into MySQL:
   ```bash
   mysql -u root -p
   ```

4. Create a database for practice:
   ```sql
   CREATE DATABASE practice_db;
   USE practice_db;
   ```

### Step 3: Test Your Setup
Run a simple query to verify everything works:
```sql
SELECT 'Hello, SQL!' AS greeting;
```

If you see the output, you're ready to start!

## Quick Start Guide

### For Complete Beginners
Start with these labs in order:

1. **Lab 1**: [Database Creation & Basic Queries](../labs/01_foundations/foundations_lab.html)
   - Learn to create databases and tables
   - Master SELECT statements
   - Understand basic data types

2. **labs/01_foundations/inclass_exercise.html**: [Workers Database](../labs/01_foundations/inclass_exercise.html)
   - Practice CREATE TABLE and INSERT
   - Apply what you learned in Lab 1

3. **Lab 2**: [Advanced Queries & Joins](../labs/02_single_table/single_table_queries.html)
   - Multi-table queries
   - JOIN operations
   - Complex WHERE clauses

### For Intermediate Users
If you already know basic SQL:

1. **Lab 7**: [CASE Expressions](../labs/06_case_expression/case_expression.html)
2. **Lab 8**: [Window Functions](../labs/07_window_recursive/window_recursive.html)
3. **Lab 9**: [Views](../labs/09_views/views.html)

### For Advanced Users
Jump to these advanced topics:

1. **Lab 16**: [Triggers & Stored Procedures](../labs/12_transactions_triggers/triggers.html)
2. **Lab 17**: [Transaction Management](../labs/12_transactions_triggers/transactions.html)
3. **Lab 20**: [MongoDB (NoSQL)](../labs/13_nosql/mongodb.html)
4. **Lab 21**: [Neo4j (Graph Database)](../labs/13_nosql/neo4j.html)

## Lab Navigation

### Lab Structure
Each lab follows this structure:
- **Learning Objectives**: What you'll learn
- **Prerequisites**: Required knowledge
- **Introduction**: Concept overview
- **Exercises**: Hands-on practice
- **Solutions**: Example solutions (where applicable)
- **Additional Resources**: Further reading

### Lab Categories

#### 📘 Foundational Labs (Weeks 1-4)
- Basic SQL operations
- Table creation and data manipulation
- Simple queries and filtering

#### 📗 Intermediate Labs (Weeks 5-8)
- Complex queries and joins
- Aggregate functions
- Set operations
- Window functions

#### 📙 Advanced SQL (Weeks 9-12)
- Stored procedures and triggers
- Transaction management
- Optimization techniques
- Database design

#### 📕 Programming Integration (Weeks 13-14)
- Python database connectivity
- Java database integration
- Web application development

#### 📓 Modern Databases (Weeks 15-16)
- NoSQL databases
- Graph databases
- JSON/XML handling

## Troubleshooting

### Common Issues

#### 1. "Access denied for user"
**Problem**: Can't connect to MySQL
**Solution**:
```bash
# Reset MySQL root password
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newpassword';
FLUSH PRIVILEGES;
```

#### 2. "Can't connect to local MySQL server"
**Problem**: MySQL service not running
**Solution**:
```bash
# Start MySQL service
sudo systemctl start mysql  # Linux
brew services start mysql   # macOS
```

#### 3. "Unknown database"
**Problem**: Database doesn't exist
**Solution**:
```sql
-- Create the database first
CREATE DATABASE your_database_name;
USE your_database_name;
```

#### 4. "Table doesn't exist"
**Problem**: Trying to query a table that hasn't been created
**Solution**:
- Make sure you've run the CREATE TABLE statement
- Check you're in the correct database: `SELECT DATABASE();`
- List all tables: `SHOW TABLES;`

#### 5. Jupyter Notebook can't connect to MySQL
**Problem**: Jupyter can't find MySQL connection
**Solution**:
```python
# Install required packages
!pip install pymysql ipython-sql

# Load SQL extension
%load_ext sql

# Connect to MySQL
%sql mysql+pymysql://username:password@localhost/database_name
```

### Getting Help
- Check the [Main README](../Readme.md) for overview
- Review specific lab instructions carefully
- Search for error messages online
- Post issues on the [GitHub repository](https://github.com/TeachingOW/DBMS-SQL-Labs/issues)

## Additional Resources

### Learning Platforms
- [SQLZoo](https://sqlzoo.net/) - Interactive SQL tutorials
- [W3Schools SQL](https://www.w3schools.com/sql/) - SQL reference and examples
- [LeetCode Database](https://leetcode.com/problemset/database/) - Practice problems
- [HackerRank SQL](https://www.hackerrank.com/domains/sql) - SQL challenges

### Documentation
- [MySQL Official Documentation](https://dev.mysql.com/doc/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MongoDB Manual](https://docs.mongodb.com/manual/)
- [Neo4j Documentation](https://neo4j.com/docs/)

### Video Tutorials
- [MySQL Tutorial for Beginners](https://www.youtube.com/watch?v=7S_tz1z_5bA) (Programming with Mosh)
- [SQL Full Course](https://www.youtube.com/watch?v=HXV3zeQKqGY) (freeCodeCamp)

### Books
- "SQL in 10 Minutes" by Ben Forta
- "Learning SQL" by Alan Beaulieu
- "Database System Concepts" by Silberschatz, Korth, and Sudarshan

### Practice Datasets
The `data/` directory contains several datasets for practice:
- **IMDB Movie Data**: Movie ratings and information
- **Employee Data**: HR database with hierarchies
- **Drivers Database**: Complete relational database example
- **Student Grades**: Academic performance data

## Next Steps

Once you've completed the setup:

1. ✅ Start with [Lab 1: Basic Queries](../labs/01_foundations/foundations_lab.html)
2. ✅ Complete the [labs/01_foundations/inclass_exercise.html](../labs/01_foundations/inclass_exercise.html)
3. ✅ Progress through labs sequentially
4. ✅ Practice with the provided datasets
5. ✅ Try the challenge exercises
6. ✅ Build your own projects using learned concepts

Happy Learning! 🚀

---

**Need Help?** 
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the main README for additional guidance
