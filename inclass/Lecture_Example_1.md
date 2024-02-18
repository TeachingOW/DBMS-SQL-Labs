## Lecture Example


```sql
CREATE  database Lec;
USE Lec; 

create table product(
       pname        varchar(20) primary key, -- name of the product
       price        decimal(10,2),               -- price of the product
       category     varchar(20),             -- category
       manufacturer varchar(20) NOT NULL     -- manufacturer
);
insert into product values('Gizmo', 19.99, 'Gadgets', 'GizmoWorks');    
insert into product values('PowerGizmo', 29.99, 'Gadgets', 'GizmoWorks');  
insert into product values('MultiTouch', 203.99, 'Household', 'Hitachi'); 
insert into product values('SingleTouch', 149.99, 'Photography', 'Canon')

```

### Exercise 1
Try writing a query to get an output table of all the products with "Touch" in the name, showing just their name and price, 
and sorted alphabetically by manufacturer.


Next, write a query that returns the distinct names of manufacturers that make products with "Gizmo" in its name



### Exercise 2

Try some of these queries but first guess what they return.

```sql
SELECT DISTINCT category FROM product ORDER BY category;
SELECT category FROM product ORDER BY pname;
SELECT DISTINCT category FROM product ORDER BY pname;
```
