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

#### Lab 2: JOINs and Multi-Table Queries
**Topics**: INNER/LEFT/RIGHT joins, multi-table queries  
**Duration**: 1.5-2 hours  
**Prerequisites**: Lab 1  
**Link**: [Lab 2](labs/html_labs/Lab2_Part1_Joins.html)

**What You'll Learn:**
- INNER JOIN, LEFT JOIN, RIGHT JOIN
- Multi-table queries with 3+ tables
- Complex WHERE conditions
- Table and column aliases
- String functions with JOINs
- Combining data from multiple sources

**Key Concepts**: `JOIN`, `ON`, `USING`, `CONCAT`, aliases

**Examples Included**:
- University database with students, courses, and enrollments
- Employee-Department relationships
- Product catalogs with suppliers

---

#### Lab 3: Aggregate Functions and GROUP BY
**Topics**: COUNT, SUM, AVG, GROUP BY, HAVING  
**Duration**: 1.5-2 hours  
**Prerequisites**: Lab 1, Lab 2  
**Link**: [Lab 3](labs/html_labs/Lab2_Part2_Aggregates.html)

**What You'll Learn:**
- COUNT, SUM, AVG, MIN, MAX
- GROUP BY clause
- HAVING clause for filtering groups
- COUNT() vs COUNT(DISTINCT)
- Combining aggregates with JOINs
- Statistical analysis of data

**Key Concepts**: `COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING`

**Examples Included**:
- Sales analysis and revenue calculations
- Student performance statistics
- Inventory management aggregations

---

#### Lab 4: Set Operations and Advanced Queries
**Topics**: UNION, set operations, complex queries  
**Duration**: 1.5-2 hours  
**Prerequisites**: Lab 2, Lab 3  
**Link**: [Lab 4](labs/html_labs/Lab2_Part3_SetOperations.html)

**What You'll Learn:**
- UNION and UNION ALL
- Set operations (MySQL alternatives for INTERSECT)
- UPDATE and DELETE with multiple rows
- Division operation in SQL
- Complex nested subqueries
- Data merging from multiple sources

**Key Concepts**: `UNION`, `UNION ALL`, nested queries, division

**Examples Included**:
- Combining customer data from multiple sources
- Finding common elements across tables
- Complex filtering with subqueries

---

#### Lab 5: Foreign Keys & Relationships
**Topics**: Referential integrity, relationships  
**Duration**: 2 hours  
**Prerequisites**: Lab 1, Lab 2  
**Link**: [Lab 5](labs/html_labs/Foreign_Keys.html)

**What You'll Learn:**
- Create foreign key constraints
- Understand parent-child relationships
- Implement referential integrity
- CASCADE operations
- Managing relationships in database design

**Key Concepts**: `FOREIGN KEY`, `REFERENCES`, `ON DELETE CASCADE`

**Examples Included**:
- Customer-Order relationships
- Department-Employee hierarchies
- Product-Category associations

---

#### Lab 6: Multi-Table Operations
**Topics**: Complex joins, multiple table queries  
**Duration**: 3 hours  
**Prerequisites**: Lab 2, Lab 5  
**Link**: [Lab 6](labs/html_labs/Multi_Tables.html)

**What You'll Learn:**
- Join 3+ tables
- Self-joins
- Cross joins
- Query optimization basics
- Complex relationship navigation

**Examples Included**:
- Multi-level organizational structures
- Supply chain queries with multiple vendors
- Social network friend-of-friend queries

---

### 🟡 Intermediate Level

#### Lab 7: CASE Expressions
**Topics**: Conditional logic in SQL  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 3  
**Link**: [Lab 7](Lab_Case_Expression.md)

**What You'll Learn:**
- Simple CASE expressions
- Searched CASE expressions
- CASE with aggregate functions
- Conditional counting and summing
- Real-world data categorization
- Data transformation techniques

**Key Concepts**: `CASE WHEN`, conditional logic, data transformation

**Highlights**: 
- ✨ Comprehensive guide with real-world examples
- ✨ Compare different query approaches
- ✨ Practice exercises with solutions

**Examples Included**:
- Grade categorization (A, B, C, etc.)
- Sales tier classification
- Customer segmentation
- Performance rating systems

---

#### Lab 8: Window Functions & Recursive Queries
**Topics**: Analytical functions, partitioning  
**Duration**: 3-4 hours  
**Prerequisites**: Lab 3  
**Link**: [Lab 8](labs/html_labs/Lab4.html)

**What You'll Learn:**
- ROW_NUMBER, RANK, DENSE_RANK
- PARTITION BY clause
- Running totals
- Moving averages
- Recursive CTEs
- Advanced analytical operations

**Key Concepts**: Window functions, `OVER`, `PARTITION BY`, recursion

**Examples Included**:
- Top N queries per category
- Running sum calculations
- Year-over-year comparisons
- Hierarchical data traversal

---

#### Lab 9: Views & Virtual Tables
**Topics**: Creating and managing views  
**Duration**: 2 hours  
**Prerequisites**: Lab 2  
**Link**: [Lab 9](labs/html_labs/Lab5_views.html)

**What You'll Learn:**
- Create views
- Query views
- Update through views
- Materialized views concept
- Security and abstraction benefits

**Key Concepts**: `CREATE VIEW`, virtual tables, data abstraction

**Examples Included**:
- Employee summary views
- Sales dashboard views
- Filtered data access for different user roles

---

### 🟠 Database Design & Advanced SQL

#### Lab 10: Database Normalization
**Topics**: 1NF, 2NF, 3NF, BCNF  
**Duration**: 3-4 hours  
**Prerequisites**: Lab 5  
**Link**: [Lab 10](labs/html_labs/Lab3_Normal_forms.html)

**What You'll Learn:**
- Database normalization principles
- First, Second, Third Normal Forms
- Boyce-Codd Normal Form
- When to denormalize
- Design patterns
- Dependency analysis

**Key Concepts**: Normalization, dependencies, decomposition

**Examples Included**:
- Poorly designed database transformations
- Student registration system normalization
- E-commerce database design

---

#### Lab 11: Advanced SQL Techniques
**Topics**: Complex queries and optimization  
**Duration**: 3 hours  
**Prerequisites**: Lab 8  
**Link**: [Lab 11](labs/html_labs/Lab4_sql.html)

**What You'll Learn:**
- Query optimization
- Complex analytical queries
- Advanced subquery techniques
- Performance considerations
- Index usage strategies

**Examples Included**:
- Query execution plan analysis
- Optimizing slow queries
- Complex reporting queries

---

### 🔵 Programming Integration

#### Lab 12: Java Database Interface
**Topics**: JDBC, connecting Java to databases  
**Duration**: 3-4 hours  
**Prerequisites**: Basic Java knowledge  
**Link**: [Lab 12](labs/html_labs/lab_java_3.html)

**What You'll Learn:**
- JDBC basics
- Connection management
- PreparedStatements
- ResultSet handling
- Error handling
- Connection pooling

**Key Concepts**: JDBC, `Connection`, `Statement`, `ResultSet`

**Examples Included**:
- Simple CRUD operations in Java
- Database-backed Java applications
- Transaction management in JDBC

---

#### Lab 13: Python Database Interface
**Topics**: Python MySQL connector  
**Duration**: 2-3 hours  
**Prerequisites**: Basic Python knowledge  
**Link**: [Lab 13](labs/html_labs/Lab_Python.html)

**What You'll Learn:**
- mysql-connector-python
- PyMySQL
- Connection pooling
- Parameterized queries
- Error handling
- Pandas integration

**Key Concepts**: Python DB-API, connectors, cursors

**Examples Included**:
- Database operations with Python
- Data analysis with Pandas
- Web application database backends

---

#### Lab 14: Jupyter Notebook Integration
**Topics**: Interactive database analysis  
**Duration**: 2 hours  
**Prerequisites**: Lab 13  
**Link**: [Lab 14](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Mysql-Jupyter.ipynb)

**What You'll Learn:**
- IPython SQL magic
- Pandas integration
- Data visualization
- Interactive queries
- Exploratory data analysis

**Examples Included**:
- Interactive SQL queries in Jupyter
- Data visualization with matplotlib
- Statistical analysis of database data

---

### 🟣 Advanced Database Concepts

#### Lab 15: Analytical Functions
**Topics**: ROLLUP, CUBE, advanced grouping  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 3, Lab 8  
**Link**: [Lab 15](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Rollup.ipynb)

**What You'll Learn:**
- ROLLUP for subtotals
- CUBE for multi-dimensional analysis
- GROUPING function
- Advanced analytics
- Cross-tabulation queries

**Key Concepts**: `ROLLUP`, `CUBE`, `GROUPING SETS`

**Examples Included**:
- Sales reports with subtotals
- Multi-dimensional analysis
- Pivot table-like queries

---

#### Lab 16: Triggers & Stored Procedures
**Topics**: Database automation and business logic  
**Duration**: 3-4 hours  
**Prerequisites**: Lab 11  
**Link**: [Lab 16](labs/html_labs/Triggers.html)

**What You'll Learn:**
- Create triggers (BEFORE/AFTER)
- Stored procedures
- Functions
- Parameters
- Error handling
- Audit logging

**Key Concepts**: `TRIGGER`, `PROCEDURE`, `FUNCTION`, automation

**Related Assignment**: [Bank Overdraft System](bank.md)

**Examples Included**:
- Automatic timestamp updates
- Audit trail implementation
- Business rule enforcement
- Data validation triggers

---

#### Lab 17: Transaction Management
**Topics**: ACID properties, concurrency  
**Duration**: 3 hours  
**Prerequisites**: Lab 16  
**Link**: [Lab 17](labs/html_labs/Transactions.html)

**What You'll Learn:**
- BEGIN, COMMIT, ROLLBACK
- ACID properties
- Transaction isolation
- Savepoints
- Deadlock handling
- Error recovery

**Key Concepts**: Transactions, `COMMIT`, `ROLLBACK`, ACID

**Examples Included**:
- Banking transaction scenarios
- Multi-step operations
- Error handling and rollback

---

#### Lab 18: Isolation Levels
**Topics**: Concurrency control, consistency  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 17  
**Link**: [Lab 18](labs/html_labs/Isolation_Levels.html)

**What You'll Learn:**
- READ UNCOMMITTED
- READ COMMITTED
- REPEATABLE READ
- SERIALIZABLE
- Dirty reads, phantom reads
- Concurrency issues

**Key Concepts**: Isolation levels, concurrency problems

**Examples Included**:
- Demonstrating dirty reads
- Phantom read scenarios
- Non-repeatable read examples

---

### 🔴 Modern Database Technologies

#### Lab 19: JSON & XML Processing
**Topics**: Semi-structured data in SQL  
**Duration**: 2-3 hours  
**Prerequisites**: Lab 2  
**Link**: [Lab 19](labs/html_labs/Lab_JSON-XML.html)

**What You'll Learn:**
- JSON data type
- JSON functions
- XML handling
- Querying nested data
- Storing semi-structured data

**Key Concepts**: JSON, XML, semi-structured data

**Examples Included**:
- Storing and querying JSON documents
- Extracting values from nested JSON
- XML data manipulation

---

#### Lab 20: MongoDB (NoSQL)
**Topics**: Document-based databases  
**Duration**: 3-4 hours  
**Prerequisites**: Basic database knowledge  
**Link**: [Lab 20](labs/html_labs/Lab10_mongoDB.html)

**What You'll Learn:**
- MongoDB basics
- Document model
- CRUD operations
- Aggregation pipeline
- When to use NoSQL
- Schema design for documents

**Key Concepts**: NoSQL, documents, collections, MongoDB

**Examples Included**:
- Blog post storage and retrieval
- E-commerce product catalogs
- Social media data modeling

---

#### Lab 21: Neo4j (Graph Database)
**Topics**: Graph database concepts  
**Duration**: 3-4 hours  
**Prerequisites**: Basic database knowledge  
**Link**: [Lab 21](labs/html_labs/Lab11_neo4j.html)

**What You'll Learn:**
- Graph data model
- Nodes and relationships
- Cypher query language
- Path queries
- Graph algorithms
- When to use graph databases

**Key Concepts**: Graph databases, Cypher, nodes, edges

**Examples Included**:
- Social network modeling
- Recommendation engines
- Shortest path problems
- Network analysis

---

## 📊 Learning Paths

### Path 1: Complete Beginner to SQL Master (16 weeks)
Week 1-2: Labs 1-2  
Week 3-4: Labs 3-6  
Week 5-6: Labs 7-9  
Week 7-8: Labs 10-11  
Week 9-10: Labs 12-13, 16-18  
Week 11-12: Labs 14-15  
Week 13-16: Labs 19-21 and capstone project

### Path 2: Quick SQL Review (4 weeks)
Week 1: Labs 1-3  
Week 2: Labs 4-8  
Week 3: Labs 16-17  
Week 4: Labs 20-21

### Path 3: Programming Integration Focus (6 weeks)
Week 1-2: Labs 1-3 (refresh)  
Week 3: Labs 12-13 (Python/Java)  
Week 4: Lab 14 (Jupyter)  
Week 5: Labs 16-17 (Triggers/Transactions)  
Week 6: Project work

### Path 4: Modern Databases (4 weeks)
Week 1: Labs 7-8 (SQL advanced)  
Week 2: Lab 19 (JSON/XML)  
Week 3: Lab 20 (MongoDB)  
Week 4: Lab 21 (Neo4j)

### Path 5: Data Analysis Track (5 weeks)
Week 1: Labs 1-3 (Foundations)  
Week 2: Labs 7-8 (CASE & Window Functions)  
Week 3: Labs 13-14 (Python & Jupyter)  
Week 4: Lab 15 (ROLLUP/CUBE)  
Week 5: Labs 19-20 (JSON & MongoDB)

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
| 🟢 Beginner | 1-6 | Basic SQL, tables, joins |
| 🟡 Intermediate | 7-9 | Advanced queries, window functions |
| 🟠 Advanced SQL | 10-11 | Design, optimization |
| 🔵 Programming | 12-14 | Integration with code |
| 🟣 Expert | 15-18 | Triggers, transactions |
| 🔴 Modern | 19-21 | NoSQL, Graph databases |

---

## 🔍 Search by Topic

**Basic Operations**: Labs 1, 2  
**Joins**: Labs 2, 5, 6  
**Aggregations**: Labs 3, 15  
**Subqueries**: Labs 4, 7  
**Window Functions**: Lab 8  
**Views**: Lab 9  
**Database Design**: Labs 5, 10  
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
2. Complete Labs 1-6 (Foundations)
3. Continue with Labs 7-9 (Intermediate)
4. Study Lab 10 (Design)
5. Pick programming language: Lab 12 (Java) or Lab 13 (Python)
6. Complete Labs 16-18 (Advanced concepts)
7. Explore Labs 19-21 (Modern databases)

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
