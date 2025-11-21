# Database Management System (DBMS) SQL Labs

A comprehensive collection of hands-on SQL laboratories designed to teach database concepts from basic queries to advanced database management techniques. These labs provide practical experience with SQL, database design, and modern database technologies.


## 🎯 Learning Objectives

By completing these labs, students will:
- Master fundamental SQL operations (SELECT, INSERT, UPDATE, DELETE)
- Understand database design principles and normalization
- Learn advanced SQL concepts (joins, subqueries, window functions)
- Gain experience with database programming and interfaces
- Explore modern database technologies (NoSQL, Graph databases)
- Understand transaction management and concurrency control

## 📚 Lab Structure

### Foundational Labs (SQL Basics)

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 1 | Database Creation & Basic Queries | Learn to create databases, tables, and perform simple SELECT operations | [Lab 1](html_labs/InClassExercises.html) |
| 2 | Advanced Queries & Joins | Master multi-table queries, joins, and complex WHERE clauses | [Lab 2](html_labs/Lab2.html) |
| 3 | Foreign Keys & Relationships | Understand referential integrity and table relationships | [Foreign Keys](html_labs/Foreign_Keys.html) |
| 4 | Multi-Table Operations | Practice complex joins and relationship queries | [Multi Tables](html_labs/Multi_Tables.html) |

### Intermediate Labs (Advanced SQL)

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 5 | Set Operations & Nested Queries | Learn UNION, INTERSECT, and subquery techniques | [Lab 2 Advanced](html_labs/Lab2.html) |
| 6 | Aggregate Functions & Grouping | Master COUNT, SUM, AVG, GROUP BY, and HAVING clauses | [Lab 2 Aggregates](html_labs/Lab2.html) |
| 7 | Window Functions | Learn advanced analytical functions and partitioning | [Window Functions](html_labs/Lab4.html) |
| 8 | Views & Virtual Tables | Create and manage database views for data abstraction | [Views Lab](html_labs/Lab5_views.html) |

### Database Design Labs

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 9 | Database Normalization | Learn 1NF, 2NF, 3NF and database design principles | [Normal Forms](html_labs/Lab3_Normal_forms.html) |
| 10 | Advanced SQL Techniques | Practice complex queries and optimization | [Advanced SQL](html_labs/Lab4_sql.html) |

### Programming Integration Labs

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 11 | Java Database Interface | Connect Java applications to databases  | [Java Lab](html_labs/lab_java_3.html) |
| 12 | Python Database Interface | Connect Python applications to databases using connectors | [Python Lab](html_labs/Lab_Python.html) |
| 13 | Jupyter Notebook Integration | Interactive database analysis with Jupyter notebooks | [Jupyter Lab](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Mysql-Jupyter.ipynb)|

### Advanced Database Concepts

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 14 | Analytical Functions | Master ROLLUP, CUBE, and advanced grouping operations | [Rollup Lab](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Rollup.ipynb) |
| 15 | Triggers & Stored Procedures | Implement database automation and business logic | [Triggers Lab](html_labs/Triggers.html) |
| 16 | Transaction Management | Understand ACID properties and concurrency control | [Transactions](html_labs/Transactions.html) |
| 17 | Isolation Levels | Learn about database isolation and consistency | [Isolation Levels](html_labs/Isolation_Levels.html) |

### Modern Database Technologies

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 18 | JSON & XML Processing | Handle semi-structured data in relational databases | [JSON/XML Lab](html_labs/Lab_JSON-XML.html) |
| 19 | MongoDB (NoSQL) | Introduction to document-based databases | [MongoDB Lab](html_labs/Lab10_mongoDB.html) |
| 20 | Neo4j (Graph Database) | Explore graph database concepts and Cypher queries | [Neo4j Lab](html_labs/Lab11_neo4j.html) |

## 🗃️ Data Sets

The repository includes several real-world datasets for hands-on practice:

| Dataset | Description | Use Cases |
|---------|-------------|-----------|
| [IMDB Movie Data](data/IMDB-Movie-Data.csv) | Movie information including ratings, genres, and revenue | Complex queries, aggregations, data analysis |
| [Air Travel Data](data/airtravel.csv) | Flight and passenger information | Time-series analysis, grouping operations |
| [Cities Data](data/cities.csv) | Geographic and demographic information | Joins, geographic queries |
| [Employee Data](data/employees.csv) | HR database with employee information | Relationship modeling, hierarchical queries |
| [Student Grades](data/grades.csv) | Academic performance data | Statistical analysis, ranking functions |
| [Drivers Database](data/drivers.sql) | Complete database schema with sample data | Full database operations, complex relationships |


## Sheet Cheat

- [Mysql Sheet Cheat](https://gemini.google.com/share/d3fa0a47a9d0)

## 🛠️ Tools and Technologies

### Database Systems
- **MySQL/MariaDB**: Primary database system for most labs
- **MongoDB**: NoSQL document database (Lab 18)
- **Neo4j**: Graph database system (Lab 19)

### Programming Languages
- **SQL**: Standard query language for relational databases
- **Python**: Database connectivity and data analysis
- **Cypher**: Query language for Neo4j graph database

### Development Environment
- **Jupyter Notebooks**: Interactive data analysis and visualization
- **Command Line Tools**: Direct database interaction
- **Database Clients**: GUI tools for database management

## 📖 Additional Learning Resources

### Interactive Tutorials
- [SQLZoo](https://sqlzoo.net/wiki/SQL_Tutorial) - Interactive SQL tutorial with exercises
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/) - Comprehensive SQL reference
- [MySQL Tutorial](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/) - Official MySQL documentation

### Advanced Topics
- [Database Design Principles](https://www.lucidchart.com/pages/database-diagram/database-design) - ER modeling and normalization
- [SQL Performance Tuning](https://use-the-index-luke.com/) - Query optimization techniques
- [NoSQL Databases](https://www.mongodb.com/nosql-explained) - Understanding document and graph databases

### Practice Platforms
- [HackerRank SQL](https://www.hackerrank.com/domains/sql) - SQL coding challenges
- [LeetCode Database](https://leetcode.com/problemset/database/) - Database problem solving
- [SQLBolt](https://sqlbolt.com/) - Interactive SQL lessons

## 🤝 Contributing

We welcome contributions to improve these labs! Please:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

### Areas for Contribution
- Additional practice exercises
- New dataset examples
- Improved explanations and documentation
- Bug fixes and corrections


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌐 Project Website

Visit the project website at [https://teachingow.github.io/DBMS-SQL-Labs/](https://teachingow.github.io/DBMS-SQL-Labs/) for additional resources and updates.
