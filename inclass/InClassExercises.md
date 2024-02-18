
you need to create a database to do that
```sql
create database test;
```
test is the name of the database

then to use that database

```sql
use test; 
```
Please note that you need to create the database only once.
```sql
create table product(
       pname        varchar(20) primary key, -- name of the product
       price        decimal(10,2),               -- price of the product
       category     varchar(20),             -- category
       manufacturer varchar(20) NOT NULL     -- manufacturer
);
insert into product values('Gizmo', 19.99, 'Gadgets', 'GizmoWorks');    X
insert into product values('PowerGizmo', 29.99, 'Gadgets', 'GizmoWorks');  X
insert into product values('MultiTouch', 203.99, 'Household', 'Hitachi'); 
insert into product values('SingleTouch', 149.99, 'Photography', 'Canon');
```


## Exercise #1
Try writing a query to get an output table of all the products with "Touch" in the name, showing just their name and price, and sorted alphabetically by manufacturer.

Let's look at the products first:


Write your query here:

Next, write a query that returns the distinct names of manufacturers that make products with "Gizmo" in the name:



## Exercise #2

Try some of these queries but first guess what they return.
```sql
SELECT DISTINCT category FROM product ORDER BY category;
SELECT category FROM product ORDER BY pname;
SELECT DISTINCT category FROM product ORDER BY pname;
```

## Exercise # 3
```sql
drop table if exists product; -- This needs to be dropped if exists, see why further down!
drop table if exists company;

create table company (
    cname varchar(20) primary key, -- company name uniquely identifies the company.
    stockprice decimal(10,2), -- stock price is in money 
    country varchar(10)); -- country is just a string
insert into company values ('ToyWorks', 25.0, 'USA');
insert into company values ('ToyFriends', 65.0, 'China');
insert into company values ('ToyCo', 15.0, 'China');

create table product(
       pname varchar(10), -- name of the product
       price decimal(10,2), -- price of the product
       category varchar(10), -- category
       manufacturer varchar(10), -- manufacturer
       primary key (pname, manufacturer),
       foreign key (manufacturer) references company(cname));
insert into product values('Pikachu', 19.99, 'Toy', 'ToyWorks');
insert into product values('Pikachu', 19.99, 'Toy', 'ToyFriends');
insert into product values('Pokeball', 29.99, 'Electronic', 'ToyCo');
insert into product values('Bulbasaur', 149.99, 'Toy', 'ToyFriends');
insert into product values('Charizard', 203.99, 'Toy', 'ToyCo');
insert into product values('PokeCamera', 19.99, 'Electronic', 'ToyWorks');
```

Our goal is to answer the following question:
Find all categories of products that are made by Chinese companies









## References

Use these references for review and to learn some new things that you'll be needing:

  * data types:
    [https://dev.mysql.com/doc/refman/8.0/en/data-types.html]
  * Create tables:
    [https://dev.mysql.com/doc/refman/8.0/en/create-table.html]
  * Inserting data (contains more than you need right now):
    [https://mariadb.com/kb/en/mariadb/how-to-quickly-insert-data-into-mariadb/]



   

