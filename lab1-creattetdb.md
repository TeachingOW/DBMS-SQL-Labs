If MYSQL does not work, you can use  [SQLFiddle](http://sqlfiddle.com/)

Step 0: Create Database
-----------------------

To create the database, write down `CREATE DATABASE Test;`  
This would create the database.  
To connect to the database. `USE Test;`

Step 1: Creating Relational Schema
----------------------------------

1.  Remove the student table, if exists.

```
DROP TABLE IF EXISTS Students;
```

2.  Removing the enrolled table, if exists
```
DROP TABLE IF EXISTS Enrolled;
```

3.  Create the `Enrolled` and `Students` table, only if they do not exist.

```
   CREATE TABLE IF NOT EXISTS Students (
  		sid char(10),
  	    name char(20),
  	    gpa float,
  	    PRIMARY KEY (sid)
  );
  CREATE TABLE IF NOT EXISTS Enrolled (
  sid char(10),
  cid char(10),
  grade char(2),
  PRIMARY KEY (sid,cid),
  FOREIGN KEY (sid) references students(sid)
  );
  ```

**_NOTE:_**  
You need to create the table `Students` before table `Enrolled`. Why?

4.  Insert data into tables

```
INSERT INTO Students VALUES('s1', 'student1', 3.1);
INSERT INTO Students VALUES('s2', 'student2', 3.2);
INSERT INTO Students VALUES('s3', 'student3', 2.2);
INSERT INTO Students VALUES('s4', 'student4', NULL);

INSERT INTO Enrolled VALUES('s1','cs101', 'A+');
INSERT INTO Enrolled VALUES('s1','cs102', 'A-');
INSERT INTO Enrolled VALUES('s1','cs103', 'B');
INSERT INTO Enrolled VALUES('s1','cs104', 'B');
INSERT INTO Enrolled VALUES('s2','cs101', 'A+');
INSERT INTO Enrolled VALUES('s2','cs103', 'A');
INSERT INTO Enrolled VALUES('s3','cs101', 'A-');
INSERT INTO Enrolled VALUES('s3','cs102', 'C');
INSERT INTO Enrolled VALUES('s3','cs105', 'B');
```

**_NOTE:_**  
Due to the foreign key constraint, students needed to be INSERTed before INSERTing the enrollment in the the Enrolled table.

5.  Try to run the following command

 INSERT INTO Enrolled VALUES('s5','cs105', 'B');

This should not work, because there is no students with sid of ‘s5’

6.  Make sure to inspect data in the tables.
```
SELECT * FROM Students;
```
&
```
SELECT * FROM Enrolled;
```
7.  Try to delete student with sid=‘s3’
```
DELETE  FROM Students WHERE sid='s3';
```
The command could not be executed, due to the foreign key constraint. Mysql reports the following error:

>     Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`test`.`enrolled`, CONSTRAINT `enrolled_ibfk_1`  FOREIGN KEY (`sid`) REFERENCES `students` (`sid`))
>     

8.  However, you can delete student `s4` as there are no records (in the enrolled table).

```
DELETE  FROM Students WHERE sid='s4';
```

9.  To Delete student with sid ‘s3’, first we delete his(her) enrolled courses
```
DELETE  FROM Enrolled WHERE sid='s3';
```

Then, you can delete the student
```
DELETE  FROM Students WHERE sid='s3';
```

10.  Inspect data in the tables.
```
SELECT * FROM Students;
```

&
```
SELECT * FROM Enrolled;
```

**_NOTE:_**  
We have tested the default behavior for foreign keys.

11.  We will create a foreign key with cascades:
```
 DROP TABLE IF EXISTS Enrolled ;
 DROP TABLE IF EXISTS Students;
 CREATE TABLE IF NOT EXISTS Students (
    		sid char(10),
		    name char(20),
		    gpa float,
		    PRIMARY KEY (sid)
    );
    CREATE TABLE IF NOT EXISTS Enrolled (
		    sid char(10),
		    cid char(10),
		    grade char(2),
		    PRIMARY KEY (sid,cid),
    FOREIGN KEY (sid) references students(sid) ON DELETE cascade
    );
  
	INSERT INTO Students VALUES('s1', 'student1', 3.1);
	INSERT INTO Students VALUES('s2', 'student2', 3.2);
	INSERT INTO Students VALUES('s3', 'student3', 2.2);
	INSERT INTO Students VALUES('s4', 'student4', NULL);
	
	INSERT INTO Enrolled VALUES('s1','cs101', 'A+');
	INSERT INTO Enrolled VALUES('s1','cs102', 'A-');
	INSERT INTO Enrolled VALUES('s1','cs103', 'B');
	INSERT INTO Enrolled VALUES('s1','cs104', 'B');
	INSERT INTO Enrolled VALUES('s2','cs101', 'A+');
	INSERT INTO Enrolled VALUES('s2','cs103', 'A');
	INSERT INTO Enrolled VALUES('s3','cs101', 'A-');
	INSERT INTO Enrolled VALUES('s3','cs102', 'C');
	INSERT INTO Enrolled VALUES('s3','cs105', 'B');
```

12.  Inspect the tables:
```
SELECT * FROM Students;
```
&
```
SELECT * FROM Enrolled;
```
13.  However, because we are using cascade in the foreign key, we can delete student with sid=`s3`.
```
DELETE  FROM Students WHERE sid='s3';
```
14.  Inspect the tables:
```
SELECT * FROM Students;
```
&
```
SELECT * FROM Enrolled;
```

## In-Class Exercise (from UMM)

Feel Free to search for the exact command format.

In particular you are going to need to figure out how the `CREATE TABLE` and `INSERT` statements work.  You will also need to figure out a little bit about SQL data-types.  If you have any questions feel free to ask. With that in mind, here's what I
want you to do (or have already done):

1. Create your database.  You will use this database for all your work.

2. Create a table called `workers` with the following fields (all capital):

Column Name | Description
------------|--------------
EMPLOYEE    | The person's name
MANAGER     | The manager's name
JOB         | A job title
SALARY      | a yearly salary
YEARS_WORKED| The number of years worked

You get to pick the data-types for the fields

1. Enter data that satisfies ALL of the following restrictions into your table:
  *  Roberts, Ruskin, and Raphael are all ticket agents.
  *  Rayburn is a baggage handler.
  *  Rice is a flight mechanic.
  *  Price manages all ticket agents.
  *  Powell manages Rayburn.
  *  Porter manages Rice, Price, Powell and himself.
  *  Powell is head of ground crews and Porter is chief of operations.
  *  Every employee receives a 10% raise for each complete year worked.
  *  Roberts, Ruskin, Raphael, and Rayburn all started at $12,000. Roberts just started work, Ruskin
and Raphael have worked for a year and a half, and Rayburn has worked for 2 years.
  *  Rice started at $18,000 and now makes $21,780.
  *  Price and Powell started at $16,000 and have both been working for three years.
  *  Porter started at $20,000 and has been around two years longer than anyone else.


## References

Use these references for review and to learn some new things that you'll be needing:

  * data types:
    [https://dev.mysql.com/doc/refman/8.0/en/data-types.html]
  * Create tables:
    [https://dev.mysql.com/doc/refman/8.0/en/create-table.html]
  * Inserting data (contains more than you need right now):
    [https://mariadb.com/kb/en/mariadb/how-to-quickly-insert-data-into-mariadb/]


   
