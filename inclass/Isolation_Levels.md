<table>
 <tr>
   <td>
 
```sql
create table product
(id  int primary key,
name varchar(10),
price float
);

insert into product values (1,'phone',100);
insert into product values (2,'tv',200);
```

  </td>
 </tr>
</table>

<table>
<tr>
   <td colspan="2"> READ UNCOMMITTED </td>
  </tr>
  <tr>
    <td> Terminal 1 </td> <td> Terminal 2 </td> </tr>

<tr>
<td>
  
```sql 
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
BEGIN;
SELECT * FROM product WHERE id = 1; 
```
</td>
  <td></td>
</tr>

<tr>
<td> </td>
<td>
  
  ```sql
Begin;
UPDATE product SET price = 1000 WHERE id = 1;
```
 
  </td> </tr> <tr>   <td>

```sql

SELECT  * FROM product  WHERE id = 1;
```

 </td>
 <td></td>
  </tr>
  
</table>

This would return the uncommited values;



<table>
 <tr>
   <td colspan="2"> READ COMMITTED </td>
 </tr>
  <tr>
    <td> Terminal 1 </td> <td> Terminal 2 </td> </tr>

<tr>
<td>
  
```sql 
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
SELECT * FROM product; 
```

</td>
  <td></td>
</tr>

<tr>
<td> </td>
<td>
  
```sql
BEGIN;
UPDATE product SET price = 1000 WHERE id = 1;
```
 
  </td>
</tr>
  
  <tr>
    <td>

```sql

SELECT  * FROM product;
```

 </td>
 <td></td>
  </tr>
  
 <tr>
   <td>
     
   </td>
   
   <td>
     
```sql
Commit;
```
 
   </td>
 </tr> 
  
 <tr>
   <td>
     
```sql
SELECT * from Product;
``` 
   </td>
   
   <td>
     

 
   </td>
 </tr>   
</table>



<table>
 <tr>
   <td colspan="2"> Repeatable Read </td>
 </tr>
  <tr>
    <td> Terminal 1 </td> <td> Terminal 2 </td> </tr>

<tr>
<td>
  
```sql 
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
SELECT COUNT(*) FROM product; 
```

</td>
  <td></td>
</tr>

<tr> <td> </td> <td>
  
```sql
BEGIN;
 INSERT INTO `product` VALUES (3,“C”, 5);
commit;
```
 
  </td>
</tr> <tr> <td>

```sql

SELECT  * FROM product;
```

 </td>
 <td></td>
  </tr>

</table>

<table>
 <tr>
   <td colspan="2"> Serializable </td>
 </tr>
  <tr>
    <td> Terminal 1 </td> <td> Terminal 2 </td> </tr>
<tr>
<td>
 
```sql 
SET SESSION TRANSACTION ISOLATION LEVEL Serializable;
BEGIN;
SELECT COUNT(*) FROM product; 
```
</td>
  <td></td>
</tr>
<tr>
<td> </td>
<td>

 ```sql
BEGIN;
 INSERT INTO `product` VALUES (4,'D', 5);
commit;
 ```
 </td>
</tr>
 <tr> <td>

```sql

SELECT  * FROM product;
```

 </td>
 <td></td>
  </tr>

</table>
<~---~>
<table>
 <tr>
   <td colspan="2"> Example I </td>
 </tr>
  <tr>
    <td> Terminal 1 </td> <td> Terminal 2 </td> </tr>
<tr>
<td>
 
```sql 
SET SESSION TRANSACTION ISOLATION LEVEL Serializable;
BEGIN;

```
</td>
  <td></td>
</tr>
<tr>
<td> </td>
<td>

 ```sql
 SET SESSION TRANSACTION ISOLATION LEVEL Serializable;
BEGIN;
 SELECT COUNT(*) FROM product; 
 INSERT INTO `product` VALUES (5,'E', 5);

 ```
 </td>
</tr>
 <tr> <td>

```sql

SELECT  * FROM product;
 
 INSERT INTO `product` VALUES (6,'F', 6);
```

 </td>
 <td></td>
  </tr>

</table>
<~---~>
<table>
 <tr>
   <td colspan="2"> Example II </td>
 </tr>
  <tr>
    <td> Terminal 1 </td> <td> Terminal 2 </td> </tr>
<tr>
<td>
 
```sql 
SET SESSION TRANSACTION ISOLATION LEVEL Serializable;
BEGIN;

```
</td>
  <td></td>
</tr>
<tr>
<td> </td>
<td>

 ```sql
 SET SESSION TRANSACTION ISOLATION LEVEL Serializable;
BEGIN;

 INSERT INTO `product` VALUES (10,'G', 5);

 ```
 </td>
</tr>
 <tr> <td>

```sql

 
 INSERT INTO `product` VALUES (10,'H', 6);
```

 </td>
 <td></td>
  </tr>

 <tr>
  <td> 
   
  ```sql
   commit;
   ```
  </td>

  <td> 
   
  ```sql
   commit;
   ```
  </td>
 
 </tr>
 
</table>

<table>
 <tr>
   <td colspan="2"> Example III </td>
 </tr>
  <tr>
    <td> Terminal 1 </td> <td> Terminal 2 </td> </tr>
<tr>
<td>
 
```sql 
SET SESSION TRANSACTION ISOLATION LEVEL Repeatable Read;
BEGIN;
SELECT  count(*) from Product;
```
</td>
  <td></td>
</tr>
<tr>
<td> </td>
<td>

 ```sql
 SET SESSION TRANSACTION ISOLATION LEVEL Serializable;
BEGIN;

 INSERT INTO `product` VALUES (11,'G', 5);
commit;
 ```
 </td>
</tr>
 <tr> <td>

```sql

 
SELECT  count(*) from Product;
   commit;
```

 </td>
 <td></td>
  </tr>


 
</table>


|Isolation Level | dirty read | non repeatable reads |Phantoms|
|-----------------|------------|--------------------|----------|
|Read uncommited| Y |Y|Y|
|Read Commited|N | Y|Y|
Repeatable read|N|N|Y*|
Serializable |N|N|N|N


MySQL at REPEATABLE isolation level:

- When using just select statement, phantom read doesn’t happen as SQL standard mentioned.
- When the transaction modifies data (write/delete/update), we can write successfully to “unseen data” .the behavior is a mix of Repeatable Read (rows not modified are not visible) and Read Committed (modified rows are visible).
