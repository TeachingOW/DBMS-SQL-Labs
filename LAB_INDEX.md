# DBMS-SQL-Labs - Complete Lab Index

## 📑 Quick Navigation

- [Getting Started Guide](docs/GETTING_STARTED.md)
- [Course Syllabus](docs/COURSE_SYLLABUS.md)
- [SQL Cheat Sheet](docs/SQL_CHEAT_SHEET.md)
- [Contributing Guide](docs/CONTRIBUTING.md)
- [Main README](Readme.md)

---

## 📚 All Labs by Category

### 🟢 Beginner Level (Start Here!)

#### Lab 1: Database Creation & Basic Queries
**Topics**: CREATE DATABASE, CREATE TABLE, INSERT, SELECT basics  
**Duration**: 2-3 hours  
**Prerequisites**: None  
**Link**: [Lab 1](labs/html_labs/InClassExercises.html)

**What You'll Learn:**
- Create databases and tables
- Insert data into tables
- Select data with WHERE clause
- Use basic filtering and sorting

**Key Concepts**: `CREATE`, `INSERT`, `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`

---

#### In-Class Exercise: Workers Database
**Topics**: Practical application of Lab 1 concepts  
**Duration**: 1-2 hours  
**Prerequisites**: Lab 1  
**Link**: [Workers Exercise](In-Class%20Exercise)

**What You'll Learn:**
- Apply constraints (PRIMARY KEY, NOT NULL)
- Work with real-world data relationships
- Practice data modeling

---

#### Lab 2: Advanced Queries & Joins
**Topics**: Multi-table queries, JOIN operations  
**Duration**: 3-4 hours  
**Prerequisites**: Lab 1  
**Link**: [Lab 2](labs/html_labs/Lab2.html)

**What You'll Learn:**
- INNER JOIN, LEFT JOIN, RIGHT JOIN
- Multi-table queries
- Complex WHERE conditions
- Aliases for tables and columns

**Key Concepts**: `JOIN`, `ON`, `USING`, aliases

---

#### Lab 3: Foreign Keys & Relationships
**Topics**: Referential integrity, relationships  
**Duration**: 2 hours  
**Prerequisites**: Lab 1, Lab 2  
**Link**: [Foreign Keys](labs/html_labs/Foreign_Keys.html)

**What You'll Learn:**
- Create foreign key constraints
- Understand parent-child relationships
- Implement referential integrity
- CASCADE operations

**Key Concepts**: `FOREIGN KEY`, `REFERENCES`, `ON DELETE CASCADE`

---

#### Lab 4: Multi-Table Operations
**Topics**: Complex joins, multiple table queries  
**Duration**: 3 hours  
**Prerequisites**: Lab 2, Lab 3  
**Link**: [Multi Tables](labs/html_labs/Multi_Tables.html)

**What You'll Learn:**
- Join 3+ tables
- Self-joins
- Cross joins
- Query optimization basics

---

### 🟡 Intermediate Level

#### Lab 5: Set Operations & Nested Queries
**Topics**: UNION, INTERSECT, subqueries  
**Duration**: 3 hours  
**Prerequisites**: Lab 2  
**Link**: [Lab 2 Advanced](labs/html_labs/Lab2.html)

**What You'll Learn:**
- UNION and UNION ALL
- Subqueries in WHERE clause
- Subqueries in FROM clause
- EXISTS and NOT EXISTS

**Key Concepts**: `UNION`, `INTERSECT`, `EXCEPT`, subqueries, `EXISTS`

---

#### Lab 6: Aggregate Functions & Grouping
**Topics**: COUNT, SUM, AVG, GROUP BY, HAVING  
**Duration**: 3 hours  
**Prerequisites**: Lab 2  
**Link**: [Lab 2 Aggregates](labs/html_labs/Lab2.html)

**What You'll Learn:**
- Aggregate functions
- GROUP BY clause
- HAVING clause
- Combining aggregates with joins

**Key Concepts**: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP BY`, `HAVING`

---

#### Lab 7: CASE Expressions
**Topics**: Conditional logic in SQL  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 6  
**Link**: [CASE Expressions Lab](Lab_Case_Expression.md)

**What You'll Learn:**
- Simple CASE expressions
- Searched CASE expressions
- CASE with aggregate functions
- Conditional counting and summing
- Real-world data categorization

**Key Concepts**: `CASE WHEN`, conditional logic, data transformation

**Highlights**: 
- ✨ Comprehensive guide with real-world examples
- ✨ Compare different query approaches
- ✨ Practice exercises with solutions

---

#### Lab 8: Window Functions & Recursive Queries
**Topics**: Analytical functions, partitioning  
**Duration**: 3-4 hours  
**Prerequisites**: Lab 6  
**Link**: [Window Functions](labs/html_labs/Lab4.html)

**What You'll Learn:**
- ROW_NUMBER, RANK, DENSE_RANK
- PARTITION BY clause
- Running totals
- Moving averages
- Recursive CTEs

**Key Concepts**: Window functions, `OVER`, `PARTITION BY`, recursion

---

#### Lab 9: Views & Virtual Tables
**Topics**: Creating and managing views  
**Duration**: 2 hours  
**Prerequisites**: Lab 2  
**Link**: [Views Lab](labs/html_labs/Lab5_views.html)

**What You'll Learn:**
- Create views
- Query views
- Update through views
- Materialized views concept

**Key Concepts**: `CREATE VIEW`, virtual tables, data abstraction

---

### 🟠 Database Design & Advanced SQL

#### Lab 10: Database Normalization
**Topics**: 1NF, 2NF, 3NF, BCNF  
**Duration**: 3-4 hours  
**Prerequisites**: Lab 3  
**Link**: [Normal Forms](labs/html_labs/Lab3_Normal_forms.html)

**What You'll Learn:**
- Database normalization principles
- First, Second, Third Normal Forms
- Boyce-Codd Normal Form
- When to denormalize
- Design patterns

**Key Concepts**: Normalization, dependencies, decomposition

---

#### Lab 11: Advanced SQL Techniques
**Topics**: Complex queries and optimization  
**Duration**: 3 hours  
**Prerequisites**: Lab 8  
**Link**: [Advanced SQL](labs/html_labs/Lab4_sql.html)

**What You'll Learn:**
- Query optimization
- Complex analytical queries
- Advanced subquery techniques
- Performance considerations

---

### 🔵 Programming Integration

#### Lab 12: Java Database Interface
**Topics**: JDBC, connecting Java to databases  
**Duration**: 3-4 hours  
**Prerequisites**: Basic Java knowledge  
**Link**: [Java Lab](labs/html_labs/lab_java_3.html)

**What You'll Learn:**
- JDBC basics
- Connection management
- PreparedStatements
- ResultSet handling
- Error handling

**Key Concepts**: JDBC, `Connection`, `Statement`, `ResultSet`

---

#### Lab 13: Python Database Interface
**Topics**: Python MySQL connector  
**Duration**: 2-3 hours  
**Prerequisites**: Basic Python knowledge  
**Link**: [Python Lab](labs/html_labs/Lab_Python.html)

**What You'll Learn:**
- mysql-connector-python
- PyMySQL
- Connection pooling
- Parameterized queries
- Error handling

**Key Concepts**: Python DB-API, connectors, cursors

---

#### Lab 14: Jupyter Notebook Integration
**Topics**: Interactive database analysis  
**Duration**: 2 hours  
**Prerequisites**: Lab 13  
**Link**: [Jupyter Lab](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Mysql-Jupyter.ipynb)

**What You'll Learn:**
- IPython SQL magic
- Pandas integration
- Data visualization
- Interactive queries

---

### 🟣 Advanced Database Concepts

#### Lab 15: Analytical Functions
**Topics**: ROLLUP, CUBE, advanced grouping  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 6, Lab 8  
**Link**: [Rollup Lab](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Rollup.ipynb)

**What You'll Learn:**
- ROLLUP for subtotals
- CUBE for multi-dimensional analysis
- GROUPING function
- Advanced analytics

**Key Concepts**: `ROLLUP`, `CUBE`, `GROUPING SETS`

---

#### Lab 16: Triggers & Stored Procedures
**Topics**: Database automation and business logic  
**Duration**: 3-4 hours  
**Prerequisites**: Lab 11  
**Link**: [Triggers Lab](labs/html_labs/Triggers.html)

**What You'll Learn:**
- Create triggers (BEFORE/AFTER)
- Stored procedures
- Functions
- Parameters
- Error handling

**Key Concepts**: `TRIGGER`, `PROCEDURE`, `FUNCTION`, automation

**Related Assignment**: [Bank Overdraft System](bank.md)

---

#### Lab 17: Transaction Management
**Topics**: ACID properties, concurrency  
**Duration**: 3 hours  
**Prerequisites**: Lab 16  
**Link**: [Transactions](labs/html_labs/Transactions.html)

**What You'll Learn:**
- BEGIN, COMMIT, ROLLBACK
- ACID properties
- Transaction isolation
- Savepoints
- Deadlock handling

**Key Concepts**: Transactions, `COMMIT`, `ROLLBACK`, ACID

---

#### Lab 18: Isolation Levels
**Topics**: Concurrency control, consistency  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 17  
**Link**: [Isolation Levels](labs/html_labs/Isolation_Levels.html)

**What You'll Learn:**
- READ UNCOMMITTED
- READ COMMITTED
- REPEATABLE READ
- SERIALIZABLE
- Dirty reads, phantom reads

**Key Concepts**: Isolation levels, concurrency problems

---

### 🔴 Modern Database Technologies

#### Lab 19: JSON & XML Processing
**Topics**: Semi-structured data in SQL  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 2  
**Link**: [JSON/XML Lab](labs/html_labs/Lab_JSON-XML.html)

**What You'll Learn:**
- JSON data type
- JSON functions
- XML handling
- Querying nested data

**Key Concepts**: JSON, XML, semi-structured data

---

#### Lab 20: MongoDB (NoSQL)
**Topics**: Document-based databases  
**Duration**: 3-4 hours  
**Prerequisites**: Basic database knowledge  
**Link**: [MongoDB Lab](labs/html_labs/Lab10_mongoDB.html)

**What You'll Learn:**
- MongoDB basics
- Document model
- CRUD operations
- Aggregation pipeline
- When to use NoSQL

**Key Concepts**: NoSQL, documents, collections, MongoDB

---

#### Lab 21: Neo4j (Graph Database)
**Topics**: Graph database concepts  
**Duration**: 3-4 hours  
**Prerequisites**: Basic database knowledge  
**Link**: [Neo4j Lab](labs/html_labs/Lab11_neo4j.html)

**What You'll Learn:**
- Graph data model
- Nodes and relationships
- Cypher query language
- Path queries
- Graph algorithms

**Key Concepts**: Graph databases, Cypher, nodes, edges

---

## 📊 Learning Paths

### Path 1: Complete Beginner to SQL Master (16 weeks)
Week 1-2: Labs 1-2  
Week 3-4: Labs 3-4  
Week 5-6: Labs 5-6  
Week 7-8: Labs 7-8, 9  
Week 9-10: Labs 10-11  
Week 11-12: Labs 12-13, 16-18  
Week 13-14: Labs 14-15  
Week 15-16: Labs 19-21

### Path 2: Quick SQL Review (4 weeks)
Week 1: Labs 1-4  
Week 2: Labs 5-8  
Week 3: Labs 16-17  
Week 4: Labs 20-21

### Path 3: Programming Integration Focus (6 weeks)
Week 1-2: Labs 1-2 (refresh)  
Week 3: Labs 12-13 (Python/Java)  
Week 4: Lab 14 (Jupyter)  
Week 5: Labs 16-17 (Triggers/Transactions)  
Week 6: Project work

### Path 4: Modern Databases (4 weeks)
Week 1: Labs 7-8 (SQL advanced)  
Week 2: Lab 19 (JSON/XML)  
Week 3: Lab 20 (MongoDB)  
Week 4: Lab 21 (Neo4j)

---

## 📁 Additional Resources

### Data Files
All practice datasets are in the `/data` directory:
- `IMDB-Movie-Data.csv` - Movie database
- `employees.csv` - HR data
- `drivers.sql` - Complete database example
- `grades.csv` - Student performance
- `cities.csv` - Geographic data
- `airtravel.csv` - Flight data

### Code Examples
Programming examples in `/labs/code`:
- Lab 6: Node.js examples
- Lab 7: Express.js server
- Lab 8: Web application

### Jupyter Notebooks
Interactive notebooks in `/labs/notebooks`:
- Mysql-Jupyter.ipynb
- Rollup.ipynb
- Triggers.ipynb

---

## 🎯 Lab Difficulty Levels

| Level | Labs | Description |
|-------|------|-------------|
| 🟢 Beginner | 1-4 | Basic SQL, tables, joins |
| 🟡 Intermediate | 5-9 | Advanced queries, aggregates |
| 🟠 Advanced SQL | 10-11 | Design, optimization |
| 🔵 Programming | 12-14 | Integration with code |
| 🟣 Expert | 15-18 | Triggers, transactions |
| 🔴 Modern | 19-21 | NoSQL, Graph databases |

---

## 🔍 Search by Topic

**Basic Operations**: Labs 1, 2  
**Joins**: Labs 2, 3, 4  
**Aggregations**: Labs 6, 15  
**Subqueries**: Labs 5, 7  
**Window Functions**: Lab 8  
**Views**: Lab 9  
**Database Design**: Labs 3, 10  
**Stored Procedures**: Lab 16  
**Triggers**: Lab 16  
**Transactions**: Labs 17, 18  
**Python**: Lab 13, 14  
**Java**: Lab 12  
**NoSQL**: Lab 20  
**Graph Databases**: Lab 21  
**JSON/XML**: Lab 19

---

## ✅ Recommended Order for Self-Study

1. Start with [Getting Started Guide](docs/GETTING_STARTED.md)
2. Complete Labs 1-4 (Foundations)
3. Do In-Class Exercise
4. Continue with Labs 5-9 (Intermediate)
5. Study Lab 10 (Design)
6. Pick programming language: Lab 12 (Java) or Lab 13 (Python)
7. Complete Labs 16-18 (Advanced concepts)
8. Explore Labs 19-21 (Modern databases)

---

## 🆘 Need Help?

- 📖 Check [Getting Started Guide](docs/GETTING_STARTED.md)
- 📝 Review [SQL Cheat Sheet](docs/SQL_CHEAT_SHEET.md)
- 💬 Open an issue on GitHub
- 🔍 Search existing issues
- 📚 Consult external resources in each lab

---

**Happy Learning! 🚀**

[Back to Main README](Readme.md)
