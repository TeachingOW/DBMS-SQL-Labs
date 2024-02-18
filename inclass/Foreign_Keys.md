If MYSQL does not work, you can use  [SQLFiddle](http://sqlfiddle.com/)

Step 0: Create Database
-----------------------

To create the database, write down `CREATE DATABASE Test;`  
This would create the database.  
To connect to the database. `USE Test;`

Step 1: Creating Relational Schema
----------------------------------

1.  Remove the student table, if exists.

```sql
DROP TABLE IF EXISTS Students;
```

2.  Removing the enrolled table, if exists
```sql
DROP TABLE IF EXISTS Enrolled;
```

3.  Create the `Enrolled` and `Students` table, only if they do not exist.

```sql
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

```sql
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
```sql
SELECT * FROM Students;
```
&
```sql
SELECT * FROM Enrolled;
```
7.  Try to delete student with sid=‘s3’
```sql
DELETE  FROM Students WHERE sid='s3';
```
The command could not be executed, due to the foreign key constraint. Mysql reports the following error:

>     Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`test`.`enrolled`, CONSTRAINT `enrolled_ibfk_1`  FOREIGN KEY (`sid`) REFERENCES `students` (`sid`))
>     

8.  However, you can delete student `s4` as there are no records (in the enrolled table).

```sql
DELETE  FROM Students WHERE sid='s4';
```

9.  To Delete student with sid ‘s3’, first we delete his(her) enrolled courses
```sql
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
```sql
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
```sql
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
