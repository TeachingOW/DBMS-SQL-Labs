# Database Management System (DBMS) SQL Labs

[![GitHub stars](https://img.shields.io/github/stars/TeachingOW/DBMS-SQL-Labs?style=social)](https://github.com/TeachingOW/DBMS-SQL-Labs)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)

A comprehensive collection of hands-on SQL laboratories designed to teach database concepts from basic queries to advanced database management techniques. These labs provide practical experience with SQL, database design, and modern database technologies.

## 📋 Quick Links

- 🚀 **[Getting Started Guide](docs/GETTING_STARTED.md)** - Setup instructions and prerequisites
- 📚 **[Complete Lab Index](LAB_INDEX.md)** - Detailed list of all labs with descriptions
- 📖 **[Course Syllabus](docs/COURSE_SYLLABUS.md)** - 16-week structured curriculum
- 📝 **[SQL Cheat Sheet](docs/SQL_CHEAT_SHEET.md)** - Quick reference for SQL commands
- 🤝 **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute to this project
- 🌐 **[Project Website](https://teachingow.github.io/DBMS-SQL-Labs/)** - Additional resources

## 🎯 Learning Objectives

By completing these labs, students will:
- Master fundamental SQL operations (SELECT, INSERT, UPDATE, DELETE)
- Understand database design principles and normalization
- Learn advanced SQL concepts (joins, subqueries, window functions)
- Gain experience with database programming and interfaces
- Explore modern database technologies (NoSQL, Graph databases)
- Understand transaction management and concurrency control

## 📚 Lab Structure

### 🆕 Quick Start & Comprehensive Labs

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| **QUICK START** | **SQL Quick Start Guide** | **⚡ Streamlined, beginner-friendly guide (3-4 hrs). Perfect for fast learners who want practical examples without extensive theory. Covers all 10 SQL fundamentals in a concise, easy-to-follow format.** | **[Quick Start Guide](SQL_Quick_Start_Guide.md)** ⭐ **NEW** |
| **COMPREHENSIVE** | **SQL Fundamentals - Complete Guide** | **📚 In-depth comprehensive lab (8-12 hrs). Detailed explanations, multiple examples per concept, best practices, and 40+ exercises. Ideal for thorough learning.** | **[Complete Lab](Lab_Reorganized_SQL_Fundamentals.md)** ⭐ |

### Foundational Labs (SQL Basics)

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 1 | Database Creation & Basic Queries | Learn to create databases, tables, and perform simple SELECT operations | [Lab 1](labs/html_labs/InClassExercises.html) |
| 2 | JOINs and Multi-Table Queries | Master multi-table queries, INNER/LEFT/RIGHT joins | [Lab 2](labs/html_labs/Lab2_Part1_Joins.html) |
| 3 | Aggregate Functions & GROUP BY | Learn COUNT, SUM, AVG, GROUP BY, and HAVING clauses | [Lab 3](labs/html_labs/Lab2_Part2_Aggregates.html) |
| 4 | Set Operations & Advanced Queries | Master UNION, division, and complex nested queries | [Lab 4](labs/html_labs/Lab2_Part3_SetOperations.html) |
| 5 | Foreign Keys & Relationships | Understand referential integrity and table relationships | [Lab 5](labs/html_labs/Foreign_Keys.html) |
| 6 | Multi-Table Operations | Practice complex joins and relationship queries | [Lab 6](labs/html_labs/Multi_Tables.html) |

### Intermediate Labs (Advanced SQL)

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 7 | CASE Expressions | Master conditional logic in SQL with CASE statements | [Lab 7](Lab_Case_Expression.md) ⭐ |
| 8 | Window Functions & Recursive Query | Learn advanced analytical functions and partitioning | [Lab 8](labs/html_labs/Lab4.html) |
| 9 | Views & Virtual Tables | Create and manage database views for data abstraction | [Lab 9](labs/html_labs/Lab5_views.html) |

### Database Design Labs

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 10 | Database Normalization | Learn 1NF, 2NF, 3NF and database design principles | [Lab 10](labs/html_labs/Lab3_Normal_forms.html) |
| 11 | Advanced SQL Techniques | Practice complex queries and optimization | [Lab 11](labs/html_labs/Lab4_sql.html) |

### Programming Integration Labs

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 12 | Java Database Interface | Connect Java applications to databases | [Lab 12](labs/html_labs/lab_java_3.html) |
| 13 | Python Database Interface | Connect Python applications to databases using connectors | [Lab 13](labs/html_labs/Lab_Python.html) |
| 14 | Jupyter Notebook Integration | Interactive database analysis with Jupyter notebooks | [Lab 14](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Mysql-Jupyter.ipynb)|

### Advanced Database Concepts

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 15 | Analytical Functions | Master ROLLUP, CUBE, and advanced grouping operations | [Lab 15](https://nbviewer.org/github/teachingow/DBMS-SQL-Labs/blob/main/inclass/Rollup.ipynb) |
| 16 | Triggers & Stored Procedures | Implement database automation and business logic | [Lab 16](labs/html_labs/Triggers.html) |
| 17 | Transaction Management | Understand ACID properties and concurrency control | [Lab 17](labs/html_labs/Transactions.html) |
| 18 | Isolation Levels | Learn about database isolation and consistency | [Lab 18](labs/html_labs/Isolation_Levels.html) |

### Modern Database Technologies

| Lab | Topic | Description | Resource |
|-----|-------|-------------|----------|
| 19 | JSON & XML Processing | Handle semi-structured data in relational databases | [Lab 19](labs/html_labs/Lab_JSON-XML.html) |
| 20 | MongoDB (NoSQL) | Introduction to document-based databases | [Lab 20](labs/html_labs/Lab10_mongoDB.html) |
| 21 | Neo4j (Graph Database) | Explore graph database concepts and Cypher queries | [Lab 21](labs/html_labs/Lab11_neo4j.html) |

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


## Quick Reference

- 📝 **[SQL Cheat Sheet](docs/SQL_CHEAT_SHEET.md)** - Comprehensive SQL commands reference
- 🔗 [MySQL Cheat Sheet (External)](https://gemini.google.com/share/d3fa0a47a9d0)

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
- [DataLemur](https://datalemur.com/)
- [HackerRank SQL](https://www.hackerrank.com/domains/sql) - SQL coding challenges
- [LeetCode Database](https://leetcode.com/problemset/database/) - Database problem solving
- [SQLBolt](https://sqlbolt.com/) - Interactive SQL lessons

## 🤝 Contributing

We welcome contributions to improve these labs! Please read our **[Contributing Guide](docs/CONTRIBUTING.md)** for detailed information.

**Quick Start:**
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

### Areas for Contribution
- Additional practice exercises
- New dataset examples
- Improved explanations and documentation
- Bug fixes and corrections




## 🌐 Project Website

Visit the project website at [https://teachingow.github.io/DBMS-SQL-Labs/](https://teachingow.github.io/DBMS-SQL-Labs/) for additional resources and updates.

---

## 📚 Documentation

This repository now includes comprehensive documentation to help you learn effectively:

### For Students
- **[Getting Started Guide](docs/GETTING_STARTED.md)** - Complete setup instructions, prerequisites, and troubleshooting
- **[Lab Index](LAB_INDEX.md)** - Detailed catalog of all labs with learning objectives and prerequisites
- **[SQL Cheat Sheet](docs/SQL_CHEAT_SHEET.md)** - Quick reference for all SQL commands and syntax
- **[Course Syllabus](docs/COURSE_SYLLABUS.md)** - 16-week structured curriculum with weekly topics

### For Instructors
- **[Course Syllabus](docs/COURSE_SYLLABUS.md)** - Complete course structure with grading policy
- **Weekly schedule** with topics, labs, and assessments
- **Project ideas** and deliverables

### For Contributors
- **[Contributing Guide](docs/CONTRIBUTING.md)** - Guidelines for contributing code, content, and documentation
- Code style guidelines
- Pull request process

---

## 🎓 How to Use This Repository

### For Complete Beginners
1. Start with the [Getting Started Guide](docs/GETTING_STARTED.md)
2. Set up your MySQL environment
3. Begin with Lab 1 and progress sequentially
4. Complete the in-class exercise after Lab 1
5. Use the [SQL Cheat Sheet](docs/SQL_CHEAT_SHEET.md) as reference

### For Self-Paced Learning
1. Review the [Lab Index](LAB_INDEX.md) to understand all available labs
2. Choose a learning path that matches your goals
3. Work through labs at your own pace
4. Practice with the provided datasets in `/data` directory

### For Instructors
1. Review the [Course Syllabus](docs/COURSE_SYLLABUS.md)
2. Adapt the 16-week schedule to your needs
3. Use the labs sequentially or mix-and-match
4. Assign projects from the syllabus
5. Encourage students to contribute back via [Contributing Guide](docs/CONTRIBUTING.md)

---

## 🌐 Project Website

Visit the project website at [https://teachingow.github.io/DBMS-SQL-Labs/](https://teachingow.github.io/DBMS-SQL-Labs/) for additional resources and updates.
