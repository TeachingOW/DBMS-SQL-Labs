### Multi Table join

```sql
create table company (
    cname varchar(20) primary key, -- company name uniquely identifies the company.
    stockprice decimal(10,2), -- stock price is in money 
    country varchar(10)); -- country is just a string
insert into company values ('GizmoWorks', 25.0, 'USA');
insert into company values ('Canon', 65.0, 'Japan');
insert into company values ('Hitachi', 15.0, 'Japan');
```

## Another Example
```sql
drop table if exists product; 
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

## In Class Exerices


```sql
DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies(title VARCHAR(50), year INT, director VARCHAR(50), length INT);
INSERT INTO Movies VALUES('Database Wars', 1967, 'John Joe', 123);
INSERT INTO Movies VALUES('The Databaser', 1992, 'John Bob', 190);
INSERT INTO Movies VALUES('Database Wars', 1998, 'John Jim', 176);
```

## Exercise
Can you write the movie query from lecture as a single SFW query?

Recall that we are trying to find all movie titles that were used for more than one movie, and our schema for the movies table is:
```
title VARCHAR(50)
year INT
director VARCHAR(50)
length INT
```
Let's try to write the nested query that solves this from lecture:

use ANY to write it.


use join to write it.



# Another example

```sql
DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies(title VARCHAR(50), year INT, director VARCHAR(50), length INT);
INSERT INTO Movies VALUES('Database Wars', 1967, 'John Joe', 123);
INSERT INTO Movies VALUES('The Databaser', 1992, 'John Bob', 190);
INSERT INTO Movies VALUES('Database Wars', 1998, 'John Jim', 176);
```

## Exercise #1
Can you write the movie query from lecture as a single SFW query?

Recall that we are trying to find all movie titles that were used for more than one movie, and our schema for the movies table is:

title STRING
year INT
director STRING
length INT

Let's try to write the nested query that solves this from lecture:

use ANY to write it.


use join to write it.

