# Additional Practice Exercises

This document contains supplementary exercises to reinforce concepts learned in the labs. These exercises are organized by topic and difficulty level.

## Table of Contents
- [Basic SQL Queries](#basic-sql-queries)
- [Joins and Relationships](#joins-and-relationships)
- [Aggregate Functions](#aggregate-functions)
- [Subqueries](#subqueries)
- [Window Functions](#window-functions)
- [Database Design](#database-design)
- [Transactions](#transactions)
- [Challenge Problems](#challenge-problems)

---

## Basic SQL Queries

### Exercise 1: Simple SELECT
**Difficulty**: 🟢 Easy  
**Topics**: SELECT, WHERE, ORDER BY

Create a table `books` with columns: id, title, author, year, price.
1. Select all books published after 2010
2. Find all books by a specific author
3. List books ordered by price (highest to lowest)
4. Find the 5 most expensive books

### Exercise 2: Pattern Matching
**Difficulty**: 🟢 Easy  
**Topics**: LIKE, wildcards

Using the books table:
1. Find all books with "Python" in the title
2. Find all books by authors whose last name starts with 'S'
3. Find all books with exactly 4-letter titles

### Exercise 3: Multiple Conditions
**Difficulty**: 🟡 Medium  
**Topics**: AND, OR, NOT, IN, BETWEEN

1. Find books published between 2015 and 2020 with price under $30
2. Find books by authors 'Smith', 'Johnson', or 'Williams'
3. Find books NOT published in 2018, 2019, or 2020

---

## Joins and Relationships

### Exercise 4: Library Database
**Difficulty**: 🟡 Medium  
**Topics**: Multiple joins

Create tables:
- `members` (id, name, email, join_date)
- `books` (id, title, author, isbn)
- `loans` (id, member_id, book_id, loan_date, return_date)

Write queries to:
1. List all current loans (books not yet returned)
2. Find members who have never borrowed a book
3. List the most popular books (most loans)
4. Find overdue books (loans > 14 days without return)

### Exercise 5: E-commerce Schema
**Difficulty**: 🟠 Hard  
**Topics**: Complex joins, multiple tables

Create tables for an e-commerce system:
- `customers` (id, name, email, city)
- `products` (id, name, category, price)
- `orders` (id, customer_id, order_date, total)
- `order_items` (id, order_id, product_id, quantity, price)

Write queries to:
1. Find customers who have spent more than $1000
2. List products never ordered
3. Find the best-selling product in each category
4. Calculate revenue by month
5. Find customers who ordered in Q1 but not in Q2

---

## Aggregate Functions

### Exercise 6: Sales Analysis
**Difficulty**: 🟡 Medium  
**Topics**: GROUP BY, HAVING, aggregates

Using the e-commerce tables:
1. Calculate total revenue by category
2. Find categories with average product price > $100
3. Count orders per customer
4. Find customers with more than 5 orders
5. Calculate monthly revenue growth rate

### Exercise 7: Employee Statistics
**Difficulty**: 🟡 Medium  
**Topics**: Nested aggregates

Create an `employees` table (id, name, department, salary, hire_date).

1. Find departments with average salary > company average
2. Count employees hired each year
3. Find the salary range (max - min) in each department
4. List departments with more than 10 employees
5. Calculate median salary by department

---

## Subqueries

### Exercise 8: Correlated Subqueries
**Difficulty**: 🟠 Hard  
**Topics**: Correlated subqueries, EXISTS

Using employees table:
1. Find employees earning more than their department average
2. List departments with at least one employee earning > $100k
3. Find employees who are not managers
4. List products more expensive than average in their category

### Exercise 9: Subquery Alternatives
**Difficulty**: 🟠 Hard  
**Topics**: Subqueries vs joins

For each problem, write solutions using:
a) Subquery approach
b) JOIN approach

1. Find customers who have placed orders
2. Find products in categories that have active orders
3. List employees in departments with > 50 people

---

## Window Functions

### Exercise 10: Ranking and Analytics
**Difficulty**: 🟠 Hard  
**Topics**: ROW_NUMBER, RANK, DENSE_RANK

Using a `sales` table (salesperson, region, month, amount):

1. Rank salespeople by total sales
2. Find top 3 salespeople in each region
3. Calculate running total of sales by month
4. Find month-over-month sales change
5. Identify salespeople whose sales increased every month

### Exercise 11: Advanced Window Functions
**Difficulty**: 🔴 Expert  
**Topics**: LEAD, LAG, window frames

1. Calculate 3-month moving average of sales
2. Find the difference between current and previous month sales
3. Calculate year-to-date cumulative sales
4. Find the percentage of total sales for each salesperson
5. Identify gaps in time series data (missing months)

---

## Database Design

### Exercise 12: University Database
**Difficulty**: 🟡 Medium  
**Topics**: ER modeling, normalization

Design a database for a university with:
- Students (with personal info)
- Courses (with course details)
- Instructors (with credentials)
- Enrollments (students in courses)
- Grades

Requirements:
1. Draw ER diagram
2. Identify entities and relationships
3. Normalize to 3NF
4. Write CREATE TABLE statements with constraints
5. Write 5 useful queries

### Exercise 13: Social Media Platform
**Difficulty**: 🟠 Hard  
**Topics**: Complex relationships, self-joins

Design a basic social media database:
- Users
- Posts
- Comments
- Likes
- Friendships (mutual relationships)
- Followers (one-way relationships)

Include:
1. ER diagram
2. Schema in 3NF
3. Queries for: friend recommendations, trending posts, user feed

---

## Transactions

### Exercise 14: Banking System
**Difficulty**: 🟠 Hard  
**Topics**: Transactions, ACID

Create a simple banking system:
- `accounts` (id, customer_name, balance)
- `transactions` (id, from_account, to_account, amount, timestamp)

Implement:
1. Transfer function with transaction control
2. Handle insufficient funds
3. Implement transaction history
4. Add overdraft protection
5. Implement daily withdrawal limits

### Exercise 15: Inventory Management
**Difficulty**: 🟠 Hard  
**Topics**: Concurrency, isolation levels

Create an inventory system:
- `products` (id, name, stock_quantity)
- `orders` (id, product_id, quantity, status)

Implement:
1. Order processing with stock deduction
2. Handle concurrent orders for same product
3. Implement stock reservation system
4. Add reorder alerts
5. Handle order cancellations

---

## Challenge Problems

### Challenge 1: Find Consecutive Numbers
**Difficulty**: 🔴 Expert  

Table `numbers` has a column `num`.
Write a query to find all numbers that appear at least 3 consecutive times.

**Example:**
```
| id | num |
|----|-----|
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
```

Output: `1` (appears in rows 1, 2, 3)

### Challenge 2: Department Top Three Salaries
**Difficulty**: 🔴 Expert  

Table `employee` (id, name, salary, department_id).
Write a query to find top 3 highest salaries in each department.
If there are fewer than 3 employees, show all.

### Challenge 3: Friend Recommendations
**Difficulty**: 🔴 Expert  

Table `friendships` (user_id, friend_id).
Recommend friends for a user based on mutual friends.
Recommend users who:
- Are not already friends
- Have at least 2 mutual friends
- Order by number of mutual friends (descending)

### Challenge 4: Gap and Islands Problem
**Difficulty**: 🔴 Expert  

Table `attendance` (employee_id, date).
Find consecutive periods of attendance for each employee.

**Example:**
```
| employee_id | date       |
|-------------|------------|
| 1           | 2024-01-01 |
| 1           | 2024-01-02 |
| 1           | 2024-01-03 |
| 1           | 2024-01-05 |  <- gap
| 1           | 2024-01-06 |
```

Output should show "islands" of consecutive days.

### Challenge 5: Hierarchical Data Query
**Difficulty**: 🔴 Expert  

Table `employees` (id, name, manager_id).
Write a query to:
1. Show the full reporting chain for each employee
2. Calculate depth in the organizational hierarchy
3. Find all subordinates of a given manager (recursive)
4. Identify employees with no direct reports

### Challenge 6: Time Series Analysis
**Difficulty**: 🔴 Expert  

Table `stock_prices` (date, symbol, price).
Write queries to:
1. Find the longest streak of consecutive price increases
2. Calculate 50-day and 200-day moving averages
3. Identify "golden cross" (50-day crosses above 200-day)
4. Find maximum drawdown (peak to trough decline)

---

## Solutions

Solutions to selected exercises are available in the `/solutions` directory. Try solving the problems yourself before looking at the solutions!

### Tips for Success

1. **Start Simple**: Begin with easy exercises and gradually increase difficulty
2. **Test Your Queries**: Always test with sample data
3. **Optimize**: Try to write efficient queries
4. **Multiple Approaches**: Try solving the same problem different ways
5. **Read Documentation**: Consult MySQL documentation when needed
6. **Practice Regularly**: Consistency is key to mastery

---

## Additional Practice Resources

- [LeetCode Database Problems](https://leetcode.com/problemset/database/)
- [HackerRank SQL](https://www.hackerrank.com/domains/sql)
- [SQLZoo](https://sqlzoo.net/)
- [DataLemur SQL Interview Questions](https://datalemur.com/)
- [Stratascratch](https://www.stratascratch.com/)

---

**Keep practicing! The more SQL you write, the better you'll get.** 💪
