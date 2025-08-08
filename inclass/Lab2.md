# Lab 2: Advanced SQL Queries and Multi-Table Operations

## 🎯 Learning Objectives
By the end of this lab, you will be able to:
- Work with complex multi-table database schemas
- Master JOIN operations (INNER, LEFT, RIGHT)
- Use aggregate functions (COUNT, SUM, AVG, MAX, MIN)
- Apply GROUP BY and HAVING clauses effectively
- Write nested queries and subqueries
- Understand set operations (UNION, INTERSECT)
- Handle NULL values in queries

## 📋 Prerequisites
- Completion of [Lab 1](InClassExercises.md) or equivalent knowledge
- Understanding of basic SQL operations
- Familiarity with primary and foreign keys

## 🏫 Scenario: University Database System

In this lab, we'll work with a university database containing information about students, courses, and enrollments. This realistic scenario will help you understand how databases are used in real-world applications.

### Database Schema Overview

Our database consists of three related tables:
- **Student**: Contains student information (ID, name, GPA)
- **Course**: Contains course details (ID, code, name, credit hours)
- **Enrolled**: Links students to courses with grades (many-to-many relationship)

## 🚀 Getting Started

### Step 1: Create the Database
```sql
-- Clean slate: drop existing database if it exists
DROP DATABASE IF EXISTS lab2;
CREATE DATABASE lab2;
USE lab2;
```

### Step 2: Create the Table Structure
```sql
-- Drop tables in correct order (child tables first due to foreign key constraints)
DROP TABLE IF EXISTS Enrolled;  -- Junction table (child)
DROP TABLE IF EXISTS Student;   -- Parent table
DROP TABLE IF EXISTS Course;    -- Parent table

-- Create Student table
CREATE TABLE Student (
    sid INT PRIMARY KEY,           -- Student ID (unique identifier)
    fname CHAR(20),               -- First name (fixed length)
    lname CHAR(20),               -- Last name (fixed length)
    gpa FLOAT                     -- Grade Point Average (can be NULL)
);

-- Create Course table  
CREATE TABLE Course (
    cid INT PRIMARY KEY,          -- Course ID (unique identifier)
    code CHAR(10),               -- Course code (e.g., "CS101")
    name CHAR(40),               -- Course name (e.g., "Intro to Programming")
    credithours SMALLINT         -- Credit hours (1-4 typically)
);

-- Create Enrolled table (junction table for many-to-many relationship)
CREATE TABLE Enrolled (
    sid INT,                     -- Student ID (foreign key)
    cid INT,                     -- Course ID (foreign key)
    grade CHAR(2),               -- Letter grade (A+, A, B+, etc.)
    PRIMARY KEY (sid, cid),      -- Composite primary key
    FOREIGN KEY (sid) REFERENCES Student(sid),   -- Link to Student table
    FOREIGN KEY (cid) REFERENCES Course(cid)     -- Link to Course table
);
```

**Key Design Concepts**:
- **Composite Primary Key**: `(sid, cid)` ensures one grade per student per course
- **Foreign Key Constraints**: Maintain referential integrity
- **Many-to-Many Relationship**: Students can enroll in multiple courses, courses can have multiple students
### Step 3: Populate the Database with Sample Data

#### Insert Student Data
```sql
-- Insert student records (some students have NULL GPA - not yet calculated)
INSERT INTO Student VALUES(1,'Amie','Massey',3.0);
INSERT INTO Student VALUES(2,'Abigail','Larsen',NULL);
INSERT INTO Student VALUES(3,'Cora','Rowland',4);
INSERT INTO Student VALUES(4,'Alesha','Ferrell',3.5);
INSERT INTO Student VALUES(5,'Nina','Lowery',NULL);
INSERT INTO Student VALUES(6,'Scarlet','Lane',2.6);
INSERT INTO Student VALUES(7,'Lukas','Reeves',3.6);
INSERT INTO Student VALUES(8,'Ray','Chang',3.2);
INSERT INTO Student VALUES(9,'Ioan','Reid',2.5);
INSERT INTO Student VALUES(10,'Ryan','Peck',3.1);
INSERT INTO Student VALUES(11,'Marco','Lowery',3.8);
INSERT INTO Student VALUES(12,'Pearl', 'Mayo',3.7);
INSERT INTO Student VALUES(13,'Elmer', 'Cain',2.7);
INSERT INTO Student VALUES(14,'Isla', 'Mccall',2.2);
INSERT INTO Student VALUES(15,'Kate', 'Kimmel',NULL);
```

**Verify student data**:
```sql
SELECT * FROM Student ORDER BY sid;
```

#### Insert Course Data
```sql
-- Insert computer science courses with varying credit hours
INSERT INTO Course VALUES(1,'CS101', 'Computer Programming I',3);
INSERT INTO Course VALUES(2,'CS102', 'Computer Programming II',3);
INSERT INTO Course VALUES(3,'CS321', 'Data Structures',4);
INSERT INTO Course VALUES(4,'CS5710', 'Network',4);
INSERT INTO Course VALUES(5,'CS4550', 'Database',4);
INSERT INTO Course VALUES(6,'CS5990', 'Capstone Project',4);
INSERT INTO Course VALUES(7,'CS6020', 'Data Mining',4);
```

**Verify course data**:
```sql
SELECT * FROM Course ORDER BY cid;
```

#### Insert Enrollment Data
```sql
-- CS101 enrollments (all 15 students enrolled)

INSERT INTO Enrolled VALUES(1,1, 'A+');
INSERT INTO Enrolled VALUES(2,1, 'A-');
INSERT INTO Enrolled VALUES(3,1, 'B');
INSERT INTO Enrolled VALUES(4,1, 'C');
INSERT INTO Enrolled VALUES(5,1, 'D');
INSERT INTO Enrolled VALUES(6,1, 'A');
INSERT INTO Enrolled VALUES(7,1, 'B-');
INSERT INTO Enrolled VALUES(8,1, 'C+');
INSERT INTO Enrolled VALUES(9,1, 'D');
INSERT INTO Enrolled VALUES(10,1, 'C+');
INSERT INTO Enrolled VALUES(11,1, 'A-');
INSERT INTO Enrolled VALUES(12,1, 'A');
INSERT INTO Enrolled VALUES(13,1, 'B+');
INSERT INTO Enrolled VALUES(14,1, 'C+');
INSERT INTO Enrolled VALUES(15,1, 'A');
INSERT INTO Enrolled VALUES(1,2, 'A');
INSERT INTO Enrolled VALUES(2,2, 'C');
INSERT INTO Enrolled VALUES(3,2, 'B+');
INSERT INTO Enrolled VALUES(4,2, 'C-');
INSERT INTO Enrolled VALUES(5,2, 'D+');
INSERT INTO Enrolled VALUES(6,2, 'A-');
INSERT INTO Enrolled VALUES(7,2, 'C-');
INSERT INTO Enrolled VALUES(8,2, 'C');
INSERT INTO Enrolled VALUES(9,2, 'D+');
INSERT INTO Enrolled VALUES(10,2, 'C+');
INSERT INTO Enrolled VALUES(11,2, 'A-');
INSERT INTO Enrolled VALUES(12,2, 'A');
INSERT INTO Enrolled VALUES(13,2, 'B-');
INSERT INTO Enrolled VALUES(14,2, 'C');

INSERT INTO Enrolled VALUES (1,3,'C-');
INSERT INTO Enrolled VALUES (2,3,'B-');
INSERT INTO Enrolled VALUES (3,3,'D+');
INSERT INTO Enrolled VALUES (4,3,'C');
INSERT INTO Enrolled VALUES (5,3,'A+');
INSERT INTO Enrolled VALUES (6,3,'D+');
INSERT INTO Enrolled VALUES (7,3,'F');
INSERT INTO Enrolled VALUES (8,3,'A-');
INSERT INTO Enrolled VALUES (9,3,'D+');
INSERT INTO Enrolled VALUES (10,3,'D');
INSERT INTO Enrolled VALUES (11,3,'A+');
INSERT INTO Enrolled VALUES (12,3,'A');
INSERT INTO Enrolled VALUES (13,3,'B-');
INSERT INTO Enrolled VALUES (14,3,'C');
INSERT INTO Enrolled VALUES (15,3,'B-');

INSERT INTO Enrolled VALUES (1,4,'F');
INSERT INTO Enrolled VALUES (2,4,'A');
INSERT INTO Enrolled VALUES (3,4,'D-');
INSERT INTO Enrolled VALUES (4,4,'A-');
INSERT INTO Enrolled VALUES (5,4,'B-');
INSERT INTO Enrolled VALUES (6,4,'A-');
INSERT INTO Enrolled VALUES (7,4,'D+');
INSERT INTO Enrolled VALUES (8,4,'B+');
INSERT INTO Enrolled VALUES (9,4,'C+');
INSERT INTO Enrolled VALUES (10,4,'B');
INSERT INTO Enrolled VALUES (11,4,'F');
INSERT INTO Enrolled VALUES (12,4,'F');
INSERT INTO Enrolled VALUES (13,4,'A+');
INSERT INTO Enrolled VALUES (14,4,'A+');

INSERT INTO Enrolled VALUES (1,5,'A+');
INSERT INTO Enrolled VALUES (2,5,'A+');
INSERT INTO Enrolled VALUES (3,5,'B');
INSERT INTO Enrolled VALUES (4,5,'D+');
INSERT INTO Enrolled VALUES (5,5,'C-');
INSERT INTO Enrolled VALUES (6,5,'B-');
INSERT INTO Enrolled VALUES (7,5,'B');
INSERT INTO Enrolled VALUES (8,5,'B+');
INSERT INTO Enrolled VALUES (9,5,'A');
INSERT INTO Enrolled VALUES (10,5,'B');
INSERT INTO Enrolled VALUES (11,5,'D');
INSERT INTO Enrolled VALUES (12,5,'B');
INSERT INTO Enrolled VALUES (13,5,'B');
INSERT INTO Enrolled VALUES (14,5,'A+');

INSERT INTO Enrolled VALUES (1,6,'A+');
INSERT INTO Enrolled VALUES (2,6,'D');
INSERT INTO Enrolled VALUES (3,6,'D-');
INSERT INTO Enrolled VALUES (4,6,'C-');
INSERT INTO Enrolled VALUES (5,6,'C');
INSERT INTO Enrolled VALUES (6,6,'C-');
INSERT INTO Enrolled VALUES (7,6,'A-');
INSERT INTO Enrolled VALUES (8,6,'D');
INSERT INTO Enrolled VALUES (9,6,'B');
INSERT INTO Enrolled VALUES (10,6,'B-');
INSERT INTO Enrolled VALUES (11,6,'F');
INSERT INTO Enrolled VALUES (12,6,'C+');
INSERT INTO Enrolled VALUES (15,6,'F');
```

**Verify enrollment data**:
```sql
-- Check total enrollments
SELECT COUNT(*) as total_enrollments FROM Enrolled;

-- See sample enrollments with student and course names
SELECT s.fname, s.lname, c.code, c.name, e.grade
FROM Student s
JOIN Enrolled e ON s.sid = e.sid
JOIN Course c ON e.cid = c.cid
LIMIT 10;
```

---

## 🔍 Query Exercises

Now that we have our database populated, let's practice various types of queries. Each exercise builds on previous concepts while introducing new techniques.

### Exercise 1: Multi-Table JOIN with String Functions

**Problem**: Find all students who received an 'A' or 'A+' in the Database course, ordered by their full name.

**Analysis**: 
- We need data from all three tables:
  - `Student` table: for student names
  - `Course` table: to identify the Database course
  - `Enrolled` table: for grades
- This requires joining three tables with two join conditions

**Your Solution**:
```sql
-- Write your query here

```

<details>
<summary>💡 Click to see the solution</summary>

```sql
SELECT CONCAT(fname, ' ', lname) AS student_name 
FROM Student s, Course c, Enrolled e
WHERE c.cid = e.cid 
  AND s.sid = e.sid
  AND (e.grade = 'A+' OR e.grade = 'A')
  AND c.name LIKE '%Database%' 
ORDER BY student_name;
```

**Alternative using explicit JOIN syntax**:
```sql
SELECT CONCAT(s.fname, ' ', s.lname) AS student_name
FROM Student s
JOIN Enrolled e ON s.sid = e.sid
JOIN Course c ON e.cid = c.cid
WHERE (e.grade = 'A+' OR e.grade = 'A')
  AND c.name LIKE '%Database%'
ORDER BY student_name;
```

**Expected Output**:
| student_name |
|--------------|
| Abigail Larsen |
| Amie Massey |
| Isla Mccall |

**Key Concepts**:
- `CONCAT()`: Combines first and last names
- Multiple table joins: Connect related data across tables
- `LIKE '%Database%'`: Pattern matching for course names
- `OR` condition: Multiple grade criteria
</details>


### Query 2
Find all countries that manufacture some product in the ‘Gadgets’ category.
Assume you have the following data:

```sql
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Product;

CREATE TABLE Product(
	PName char(20) Primary key,
  	Price double,
  	category char(20),
  	Manufacturer char(20)
);

CREATE TABLE Company(
	CName char(20) Primary key,
  	StockPrice double,
  	Country char(20)
);

ALTER TABLE Product ADD FOREIGN KEY (Manufacturer) references Company(CName);

INSERT INTO Company VALUES('GizmoWorks',25,'USA');
INSERT INTO Company VALUES('Canon',65,'Japan');
INSERT INTO Company VALUES('Hitachi',15, 'Japan');

INSERT INTO Product VALUES('Gizmo',19.99,'Gadgets','GizmoWorks');
INSERT INTO Product VALUES('Powergizmo',29.99,'Gadgets','GizmoWorks');
INSERT INTO Product VALUES('SingleTouch',149.99,'Photography','Canon');
INSERT INTO Product VALUES('MultiTouch',203.99,'Household','Hitachi');
SELECT Country FROM Product, Company
WHERE Manufacturer=CName AND Category='Gadgets'
```

This would return:
Country
USA
USA
How to get USA only once.


### Query 3: An Unintuitive Query
Prepare the database as follows:
```sql
DROP TABLE IF EXISTS R;
DROP TABLE IF EXISTS T;
DROP TABLE IF EXISTS S;

CREATE TABLE R(A int);
CREATE TABLE S(A int);
CREATE TABLE T(A int);

INSERT INTO R VALUES (1);
INSERT INTO R VALUES (1);
INSERT INTO R VALUES (2);
INSERT INTO R VALUES (3);
INSERT INTO R VALUES (5);
INSERT INTO R VALUES (7);
INSERT INTO R VALUES (7);
INSERT INTO R VALUES (8);

INSERT INTO S VALUES (1);
INSERT INTO S VALUES (1);
INSERT INTO S VALUES (2);
INSERT INTO S VALUES (3);

INSERT INTO T VALUES (1);
INSERT INTO T VALUES (2);
INSERT INTO T VALUES (3);
INSERT INTO T VALUES (7);
```
Run this query
```sql
SELECT  DISTINCT R.A
FROM R, S, T
WHERE R.A=S.A OR R.A=T.A
```
This would return the following
| A |
|---|
| 1 |
| 2 |
| 3 |
| 7 |

Remove all tuples from S
```sql 
SET SQL_SAFE_UPDATES = 0;
DELETE FROM S;
SET SQL_SAFE_UPDATES = 1;
```
MySQL has something called safe mode, to disable it. We run SET SQL_SAFE_UPDATES = 0; and to enable it again SET SQL_SAFE_UPDATES = 1;
Rerun the query
```sql
SELECT DISTINCT R.A
FROM   R, S, T
WHERE  R.A=S.A OR R.A=T.A
```

### Multiset Operations
MySQL does not have INTERSECT or EXCEPT keyword. In the next lecture, we will explain an alternative.
*Compare these two queries *
```sql
SELECT  R.A 
FROM   R, S 
WHERE  R.A=S.A
UNION  
SELECT R.A 
FROM   R, T  
WHERE  R.A=T.A 
```
```sql
SELECT  R.A
FROM   R, S
WHERE  R.A=S.A
UNION ALL
SELECT R.A
FROM   R, T
WHERE  R.A=T.A
```


#### Try the following SQL code
```sql
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Company;

CREATE TABLE Product(
  PName char(20) Primary key,
    maker char(20),
    factory_loc char(20)
);
CREATE TABLE Company(
  CName char(20) Primary key,
    hq_city char(20)
);

ALTER TABLE Product ADD FOREIGN KEY (maker) references Company(CName);

INSERT INTO Company VALUES('X co.','Seattle');
INSERT INTO Company VALUES('Y inc.','Seattle');
INSERT INTO Company VALUES('A co.', 'Tokyo');

INSERT INTO Product VALUES('X','X co.','US');
INSERT INTO Product VALUES('A','A co.','China');
INSERT INTO Product VALUES('A+','A co.','US');
INSERT INTO Product VALUES('Y','Y inc.','China');
```
Compare the three queries below:
```sql
SELECT hq_city
FROM   Company, Product
WHERE  maker = cname 
  AND factory_loc='US'
AND hq_city in (
SELECT hq_city
FROM   Company, Product
WHERE  maker = cname
AND factory_loc='China'
);
```
```sql
SELECT maker, hq_city
FROM   Company, Product
WHERE  maker = cname 
  AND factory_loc='US'
AND (maker,hq_city) in (
SELECT maker, hq_city
FROM   Company, Product
WHERE  maker = cname
AND factory_loc='China'
);
```
```sql
SELECT DISTINCT hq_city
FROM   Company, Product
WHERE  maker = cname 
       AND cname IN (
		SELECT maker
	  	FROM   Product
	  	WHERE  factory_loc = 'US')
	 AND cname IN (
		SELECT maker
	  	FROM   Product
	  	WHERE  factory_loc = 'China');
```

### To Delete or update multiple rows
To disable safe updates or delete
```sql
SET SQL_SAFE_UPDATES=0;
```

To enable them back

```sql
SET SQL_SAFE_UPDATES=0;
```




# Lab2.2

Run the following query
```sql
SELECT DISTINCT hq_city
FROM   Company, Product
WHERE  maker = cname 
       AND cname IN (
    SELECT maker
      FROM   Product
      WHERE  factory_loc = 'US')
   AND cname IN (
    SELECT maker
      FROM   Product
      WHERE  factory_loc = 'China')
```
To understand the previous query, you may break it into three parts.

Q1:
```sql
    SELECT maker
    FROM   Product
      WHERE  factory_loc = 'US'
     ``` 
Q2:
```sql
SELECT maker
      FROM   Product
      WHERE  factory_loc = 'China'
```
Q3:
```sql
SELECT *
FROM   Company, Product
WHERE  maker = cname 
```

Another way:
```sql
SELECT DISTINCT hq_city
FROM   Company, (SELECT maker
      FROM   Product
      WHERE  factory_loc = 'US') US, 
      (SELECT maker
      FROM   Product
      WHERE  factory_loc = 'China') Ch
WHERE  us.maker = cname 
AND    ch.maker= cname 
```
Another one:
```sql
SELECT DISTINCT hq_city
FROM   Company, Product p1,   Product p2
WHERE  p1.maker = cname 
AND    p2.maker= cname 
AND  p1.factory_loc = 'US'
AND  p2.factory_loc = 'China';
```
### Example 

```sql
DROP table if exists company;
DROP table if exists Product;
DROP table if exists Purchase;

CREATE TABLE Company (
cname char(20) Primary key,
city char(20)
);

CREATE TABLE Product (
  pname char(20) ,
  maker char(20),
  price double,
  Foreign key (maker) REFERENCES company(cname),
  primary key (pname, maker)
);

CREATE TABLE Purchase 
(id int primary key,
 product char(20),
 buyer varchar(30),
Foreign key (product) REFERENCES Product(pname)
 );

INSERT INTO Company VALUES('X co','Seattle');
INSERT INTO Company VALUES('Y co','Jeffersonville');
INSERT INTO Company VALUES('A co','Seattle');
INSERT INTO Company VALUES('A inc','LA');
INSERT INTO Company VALUES('B co','NYC');
INSERT INTO Product VALUES('X','X co',20);
INSERT INTO Product VALUES('X+','X co',10);
INSERT INTO Product VALUES('Y','Y co',5);
INSERT INTO Product VALUES('A','A co',8);
INSERT INTO Product VALUES('T','A co',18);
INSERT INTO Product VALUES('A','A inc',5);
INSERT INTO Product VALUES('AA','A co',30);
INSERT INTO Product VALUES('AAA','A co',20);
INSERT INTO Product VALUES('B','B co',8);
INSERT INTO Purchase VALUES(1,'A','Joe Blow');
INSERT INTO Purchase VALUES(2,'A','Joe Smith');
INSERT INTO Purchase VALUES(3,'A','John Oliver');
INSERT INTO Purchase VALUES(4,'A','John Oliver');
INSERT INTO Purchase VALUES(5,'Y','Joe Blow');
INSERT INTO Purchase VALUES(6,'X','Joe Blow');
INSERT INTO Purchase VALUES(7,'A','Joe Blow');
INSERT INTO Purchase VALUES(8,'A','Joe Blow');
INSERT INTO Purchase VALUES(9,'A','Joe Blow');
```

### Query Q1
Cities where one can find companies that manufacture products bought
by "Joe Blow”.
```sql
SELECT  c.city
FROM   Company c
WHERE  c.cname  IN (
  SELECT pr.maker
      FROM   Purchase p, Product pr
      WHERE  p.product = pr.pname 
     AND p.buyer = 'Joe Blow')
```    
Note that we got Seattle twice for X co and A co

### Query Q2
```sql
SELECT c.city
 FROM   Company c, 
        Product p, 
        Purchase pu
 WHERE  c.cname = p.maker
   AND  p.pname = pu.product
   AND  pu.buyer = 'Joe Blow'
```
Compare the  previous two queries.

### Question 1
Find products that are more expensive than all those produced by “X co”
<details>
  <summary>Solution</summary>


```sql
SELECT pname
FROM   Product
WHERE  price > ALL(
  SELECT price
     FROM   Product
     WHERE  maker = 'X co')
```
  </details>
  
 ### Question 2 
Find ‘copycat’ products, i.e. products made by competitors with the same names as products made by ‘A co’

 <details>
  <summary>Solution</summary>
  
```sql
 SELECT p1.pname
FROM   Product p1
WHERE  p1.maker = 'A co'
   AND EXISTS(
  SELECT p2.pname
      FROM   Product p2
      WHERE  p2.maker <> 'A co'
     AND p1.pname = p2.pname)
```
</details>
  
```sql
DROP TABLE Purchase;
CREATE TABLE Purchase (
product char(20), 
pdate date, 
price double,
 quantity int
);
INSERT INTO Purchase VALUES('bagel','2021-10-21',1,20);
INSERT INTO Purchase VALUES('banana','2021-10-3',0.5,10);
INSERT INTO Purchase VALUES('banana','2021-10-10',1,10);
INSERT INTO Purchase VALUES('bagel','2021-10-25',1.5,20);
```

  Note that we do not have a primary key.

Get the number of purchases.

  ```sql
  select count(*) from purchase
  ```
  
Find the sales after ‘10/10/2021’
```sql
  SELECT product,
SUM(price * quantity) AS TotalSales
FROM Purchase
WHERE pdate > '2021-10-10'
GROUP BY product
  ```
Another way for the same query:
  ```sql
SELECT DISTINCT  x.product,
(SELECT Sum(y.price*y.quantity)  
FROM Purchase y WHERE  x.product = y.product AND y.pdate > '2021-10-10')   TotalSales FROM Purchase x WHERE  x.pdate > '2021-10-10'
```
  ### HAVING Clause 
Same query as before, except that we consider only products that have more than 100 buyers
  ```sql
SELECT   product, SUM(price*quantity)
FROM     Purchase
WHERE    pdate > '2021-10-1'
GROUP BY product
HAVING   SUM(quantity) > 100
  ```


Purchase

| Id | Product | Price | Quantity |
|----|---------|-------|----------|
| 1  | bagel   | 1.0   | 5        |
| 2  | banana  | 0.5   | 6        |
| 3  | Juice   | 1.0   | 4        |
| 4  | donuts  | 1.5   | 8        |
| 5  | bagel   | 1.5   | 7        |
| 6  | banana  | 1.0   | 4        |
| 7  | banana  | 1.0   | 3        |
| 8  | juice   | 3.0   | 5        |

```sql

DROP TABLE IF Exists Purchase;
CREATE TABLE Purchase (
  ID int PRIMARY KEY AUTO_INCREMENT,
  Product char(20),
  Price Decimal(10,2),
  Quantity int
  );

INSERT INTO Purchase(Product, Price, Quantity) values('bagel',1.0,5),
('banana',.5,6), ('juice',1.0,4),
('donuts', 1.5,8), ('bagel', 1.5,7),
('banana',1.0,4),('banana',1,3), ('juice',3.0,5)
;
```
*NOTE:*
AUTO_INCREMENT, and how we insert into the table.
```sql
SELECT SUM(Price*Quantity) as Total_sales
FROM Purchase
WHERE product='bagel'
```
1. Executing from & WHERE

| Id | Product | Price | Quantity |
|----|---------|-------|----------|
| 1  | bagel   | 1.0   | 5        |
| 5  | bagel   | 1.5   | 7        |

2. Computing the aggregate.

| Price| X | Quantity|    
|------|---|---------|
| 1.0  | x | 5 |
| 1.5  | x | 7 |
| 15.5 |   |   |

### COUNT() vs COUNT(DISTINCT)
Run the following two queries:
```sql
SELECT COUNT(*) 
FROM Purchase;
```
```sql 
SELECT COUNT(DISTINCT product)
FROM Purchase;
```

First query returns 8 while the second returns 4.

### Group By clause
The following query would find the total number of the units sold from all products.
```sql
SELECT SUM(Quantity) 
FROM Purchase
```
The query returns 36.
To find the number of units sold for each product.
```sql
SELECT Product, SUM(Quantity) 
FROM Purchase
GROUP BY Product
```



Find products and the sales that has sold more than 10 units.
<details>
  <summary>Solution</summary>

```sql
SELECT Product, SUM(Quantity*Price)
FROM Purchase
GROUP BY Product
HAVING SUM(Quantity)> 10
  

```

|Product | SUM(Quantity*Price)|
|--------|-------|
| bagel  | 15.50 |
| banana | 10.00 |
  
</details>
    
Find the product with the most units sold.
<details>
<summary>Solution</summary>
  

```sql

  SELECT Product, SUM(Quantity*Price)
FROM Purchase
GROUP BY Product
HAVING SUM(Quantity)= (
  SELECT MAX(t.units) 
  FROM  
  (SELECT SUM(Quantity) as units 
   FROM Purchase
   GROUP BY Product) t
);
```
 
</details>
  
To understand the query, let us start with:
```sql
SELECT SUM(Quantity) 
FROM Purchase
GROUP BY Product
```
```sql
SELECT MAX(t.units) 
FROM  (SELECT SUM(Quantity) as units 
     FROM Purchase
     GROUP BY Product) t
```
The query above finds the maximum of the total unit sold.



Run the following queries, to create the schema:
```sql
drop table if exists product;
drop table if exists supplier;

create table supplier(
id int,
sname varchar(30) not null,
primary key (id),
unique(sname)
);

create table product(
id int primary key, 
pname varchar(30) not null,
price float,
supplierid int,
foreign key (supplierid) references supplier(id)
);
```
Insert Data
```sql
insert into supplier(id, sname) values (1, 'bike Ltd');
insert into supplier(id, sname) values (2, 'bike USA');
insert into supplier(id, sname) values (3, 'bikes4all');

insert into product values (1,'girl bike', 110, 1);
insert into product values (2,'boy bike', 110, 2);
insert into product values (3,'mountain bike', 510, 2);
insert into product values (4,'bike', 180, NULL );
insert into product values (5,'ebike', 280, NULL );
```
Try to insert the following
```
insert into supplier(id, sname) values (4, 'bike Ltd');
```
The previous SQL insert should not work, as we have specified that  the supplier name to be unique.


Q1:

Find all products with unknown supplier.

A supplier of a product is recorded in product table
to find out products with unknown supplier, we need to find those that are NULL.
<details>
  <summary>Solution</summary>

```sql
  SELECT * from product where supplierid IS NULL
```  
</details>
  
Q2:
Find all suppliers with no product listed.
<details>
  <summary>Solution</summary>

  ```sql
SELECT * from Supplier s
WHERE NOT exists (select * from product p
  where p.supplierid=s.id)
``` 

</details> 

Q3:
For each product list the supplier information.

<details>
  <summary>Solution</summary>

```sql
SELECT *
FROM   supplier s, Product p
WHERE  s.id = p.supplierid
 ```
Another way to write the above query
is by using join clause, as follow:
  
```sql
select * from product p 
join supplier s 
on p.supplierid=s.id;
```
 However, running the above query, you are not returning
information about Products with no supplier information (e.g., products with id 4 and 5).
```sql
  select * from product p 
left outer join supplier s 
on p.supplierid=s.id;
```
  
 </details> 
 
 Q4:
Find supplier (along with the supplied products)

<details>
  <summary>Solution</summary>

```sql
select * from product p
right outer join supplier s 
on p.supplierid=s.id;
```
</details>
  Q5
Find supplier and products including not matched
<details>
  <summary>Solution</summary>

```sql
select * from product p 
full outer join supplier s 
on p.supplierid=s.id;
```
Mysql does not support full outer join. It is can executed as follow:
	
```sql
select * from product p 
left outer join supplier s 
on p.supplierid=s.id
union
select * from product p 
right outer join supplier s 
on p.supplierid=s.id;
```
  </details>
	
## Division	
  
 ```sql
 create table student (SID int primary key,Name varchar(10),Major
 varchar(4)); 
 CREATE TABLE enrolled (SID int,cid varchar(5),primary key
 (sid,cid)); 
 insert into student values (40,'alex','cs'), (41, 'john','cs'), (42, 'mat', 'cs'), (43, 'zack', 'math');
 insert into Enrolled values (40,'cs101'),(40,  'cs102'),(41, 'cs101'),(41,  'cs404'),(41,'cs405'), (42,'cs101'),(42,'cs102'),(42,'cs203'),(43,'cs101'),(43,'cs102');
```

Find students who are taking all courses taken by student 40

<details>
  <summary>Solution</summary>

```sql
SELECT DISTINCT NAME FROM STUDENT S WHERE major='cs’ AND NOT EXISTS
 (SELECT * FROM ENROLLED E2 WHERE SID=40 and CID NOT IN (SELECT CID
 FROM ENROLLED E WHERE E.SID=S.SID) )
```
  
```sql
  SELECT DISTINCT NAME FROM STUDENT S WHERE major=‘cs’ AND  NOT EXISTS
     (SELECT * FROM ENROLLED E2  WHERE SID=40 AND NOT EXISTS ( SELECT *
     FROM ENROLLED E WHERE E.SID=S.SID AND E2.CID=E.CID) )
```
</details>
